#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""objpack.py — 把建一个对象页所需的材料打成一包（html 版）。

与 md 版同职责，但**不重读语料**：
`extract_html.py` 已经把语法/参数、报错段逐字抽进 `sections.jsonl` 了。

对外提供：
  load_docs()           rel → docs.jsonl 记录
  sections_of(rel)      该文档的全部结构段
  collect_syntax(rel)   [(段名, 正文)] + 用到的 rel 列表
  edges_in(rel)         入边（谁引用了它，带语境句）
  pack(rel, ...)        打成一页材料（给 LLM 建页时用）
"""

import json
import re
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
OUT = BASE / 'extract'

SYNTAX_GROUPS = {'syntax'}
ERROR_GROUPS = {'error'}
ERR_MIN = 60          # 比分这短的段不算材料（与 md 版一致）

_docs = None
_sections = None
_topic2rel = None


def load_docs():
    global _docs
    if _docs is None:
        _docs = {}
        with (OUT / 'docs.jsonl').open(encoding='utf-8') as f:
            for l in f:
                d = json.loads(l)
                _docs[d['rel']] = d
    return _docs


def load_sections():
    global _sections
    if _sections is None:
        _sections = {}
        with (OUT / 'sections.jsonl').open(encoding='utf-8') as f:
            for l in f:
                s = json.loads(l)
                _sections.setdefault(s['doc'], []).append(s)
    return _sections


def topic_to_rel(topic):
    """`26580.htm` → 分类路径 rel。Subtopics 里写的是 topic id。"""
    global _topic2rel
    if _topic2rel is None:
        _topic2rel = {}
        for rel, d in load_docs().items():
            t = (d.get('frontmatter') or {}).get('source_topic')
            if t:
                _topic2rel[t] = rel
    return _topic2rel.get(topic)


def sections_of(rel):
    return load_sections().get(rel, [])


def _child_rels(rel):
    """从 `Subtopics` 段里取子文档的 rel（body 里现在是 `[文字](rel)`）。"""
    out = []
    for s in sections_of(rel):
        if (s.get('h2') or '').strip().lower() == 'subtopics':
            for m in re.finditer(r'\]\(([^)]+)\)', s.get('body') or ''):
                r = m.group(1).strip().split('#')[0]
                r = topic_to_rel(r) or r
                if r and r not in out:
                    out.append(r)
    return out


def collect_syntax(rel, follow_subtopics=True, max_depth=2):
    """返回 ([(段名, 正文)], [用到的 rel])。

    跟随 `Subtopics`（最多两层）：定义文档自己没语法段时，
    子主题 / 孙主题里常常有。段名会标「取自子主题 …」。
    """
    parts, srcs = [], []
    seen = set()

    def add(r, suffix=''):
        if r in seen:
            return
        seen.add(r)
        for s in sections_of(r):
            if s.get('group') in SYNTAX_GROUPS and not s.get('truncated'):
                parts.append((s['h2'] + suffix, s['body']))
                srcs.append(r)

    def walk(r, depth, suffix):
        add(r, suffix)
        if depth <= 0:
            return
        for ch in _child_rels(r):
            title = ((load_docs().get(ch, {}).get('frontmatter') or {}).get('title') or ch)
            walk(ch, depth - 1, f'（取自子主题 {title}）')

    walk(rel, max_depth if follow_subtopics else 0, '')
    return parts, srcs


def collect_errors(rel):
    return [(s['h2'], s['body']) for s in sections_of(rel)
            if s.get('group') in ERROR_GROUPS
            and s.get('chars', 0) >= ERR_MIN and not s.get('truncated')]


def edges_in(rel):
    """入边：谁引用了本页，带 context。给「和谁有关」用。"""
    out = []
    with (OUT / 'edges.jsonl').open(encoding='utf-8') as f:
        for l in f:
            e = json.loads(l)
            if e.get('to') == rel and e.get('resolved'):
                out.append(e)
    return out


def pack(rel, limit_edges=60):
    """一页对象页的材料：定义文档 + 语法/参数 + 报错 + 入边。"""
    d = load_docs().get(rel, {})
    parts, _ = collect_syntax(rel)
    errs = collect_errors(rel)
    ins = edges_in(rel)[:limit_edges]
    w = [f'# {((d.get("frontmatter") or {}).get("title") or rel)}', '',
         f'- rel: `{rel}`',
         f'- topic: `{((d.get("frontmatter") or {}).get("source_topic") or "")}`',
         f'- 首段: {d.get("first_para") or "（无）"}', '',
         '## 语法 / 参数（逐字）', '']
    for name, body in parts:
        w += [f'### {name}', '', body, '']
    if errs:
        w += ['## 报错条件（逐字）', '']
        for name, body in errs:
            w += [f'### {name}', '', body, '']
    if ins:
        w += ['## 入边（谁引用了它）', '']
        for e in ins:
            w += [f'- `{e["from"]}`：{e.get("context") or ""}']
        w += ['']
    return '\n'.join(w)


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        raise SystemExit('用：python objpack.py <rel>')
    print(pack(sys.argv[1]))
