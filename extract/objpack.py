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
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
OUT = BASE / 'extract'

SYNTAX_GROUPS = {'syntax'}
ERROR_GROUPS = {'error'}
ERR_MIN = 60          # 比分这短的段不算材料（与 md 版一致）

_docs = None
_sections = None


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


def sections_of(rel):
    return load_sections().get(rel, [])


def collect_syntax(rel):
    """返回 ([(段名, 正文)], [rel])。只取 group == 'syntax' 且未截断的段。"""
    parts = [(s['h2'], s['body']) for s in sections_of(rel)
             if s.get('group') in SYNTAX_GROUPS and not s.get('truncated')]
    return parts, [rel]


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
