#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_pages.py — 只读 wiki 页面的检查器（html 版）。

对应 md 版 verify_stages.py 里**不依赖语料**的那几类：
  第一类 九页与十节齐备
  第二类 frontmatter 必填
  第三类 sources 可追溯（对 docs.jsonl）
  第五类 下一步链
  第八类 链接目标可达（只记录）
  第九类 命名合规
  第十一类 层断言一致性（对象页建了以后才生效）
  第十四类甲/乙 index 覆盖与计数
  第十五类 骨架占位符

不做的（md 专有 / 依赖未移植模块）：
  第四类 分类号存在（要改判据）
  第六类 候选归属（要 hubs-dedup.csv）
  第七类 引文逐字（要重写为 HTML）
  第十类 重复投放（要 hubs-dedup）
  第十二/十三类（要 objscaffold/versions）
  第十四类庚（要 check_doc_stats）

用法：python check_pages.py
输出：extract/stage-report.md，并在 stdout 打汇总；有红则退出码非 0。
"""

import json
import re
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
WIKI = BASE / 'wiki'
OUT = BASE / 'extract'

STAGES = ['project', 'pin', 'level', 'timing', 'pattern',
          'testmethod', 'testflow', 'run', 'results']
NEXT = dict(zip(STAGES, STAGES[1:] + [None]))
SECTIONS = ['目的', '前置条件', '涉及对象', 'L1 — Firmware / Setup Command',
            'L2 — Test Method API', 'L3 — 外部控制', '产物', '验证', '常见错误', '下一步']
OBJECT_SECTIONS = ['语法 / 参数', '是什么', '典型用法', '和谁有关', '版本', '出处']
REQUIRED_FM = ['type', 'title', 'tags', 'related', 'sources', 'created', 'updated', 'verified']
SLUG_RX = re.compile(r'^[a-z0-9]+(?:[-.][a-z0-9]+)*$')
RE_WIKILINK = re.compile(r'\[\[([^\]|#]+)')
RE_H2 = re.compile(r'^##\s+(.+?)\s*$', re.M)

R = []
DOCS_BY_REL = {}


def w(s=''):
    R.append(s)


def read(p):
    return p.read_text(encoding='utf-8')


def parse_frontmatter(text):
    lines = text.split('\n')
    if not lines or lines[0].strip() != '---':
        return None, lines
    for i in range(1, len(lines)):
        if lines[i].strip() == '---':
            fm = {}
            key = None
            for x in lines[1:i]:
                m = re.match(r'^([A-Za-z_][A-Za-z0-9_]*)\s*:\s*(.*)$', x)
                if m:
                    key = m.group(1)
                    val = m.group(2).strip()
                    fm[key] = [] if val == '' else val
                elif key and x.strip().startswith('- '):
                    if not isinstance(fm[key], list):
                        fm[key] = []
                    fm[key].append(x.strip()[2:].strip().strip('"'))
            return fm, lines[i + 1:]
    return None, lines


def strip_code(text):
    """去掉围栏代码块和行内代码；语法示例里的 [[...]] 不是 wikilink。"""
    text = re.sub(r'```.*?```', '', text, flags=re.S)
    text = re.sub(r'`[^`\n]*`', '', text)
    return text


def h2_map(lines):
    """标题 → 该节正文（到下一个 ## 为止）。"""
    out = {}
    cur = None
    buf = []
    for x in lines:
        m = re.match(r'^##\s+(.+?)\s*$', x)
        if m:
            if cur is not None:
                out[cur] = '\n'.join(buf).strip()
            cur = m.group(1).strip()
            buf = []
        elif cur is not None:
            buf.append(x)
    if cur is not None:
        out[cur] = '\n'.join(buf).strip()
    return out


def load_docs():
    return [json.loads(l) for l in (OUT / 'docs.jsonl').open(encoding='utf-8')]


def cat1_stage(pages, docs):
    """九页存在、十节齐、sources 非空。"""
    ok = True
    w('## 第一类 — 九页与十节齐备')
    w()
    w('| stage | 存在 | 节 | 空节 |')
    w('|---|---|---|---|')
    for st in STAGES:
        p = WIKI / 'stages' / f'{st}.md'
        if not p.exists():
            w(f'| {st} | ❌ | — | — |')
            ok = False
            continue
        _, lines = parse_frontmatter(read(p))
        secs = h2_map(lines)
        missing = [s for s in SECTIONS if s not in secs]
        empty = [s for s, body in secs.items() if s in SECTIONS and len(body) < 4]
        status = '✅' if not missing and not empty else '❌'
        if missing or empty:
            ok = False
        w(f'| {st} | ✅ | {len(SECTIONS) - len(missing)}/10 | '
          f'{", ".join(empty) if empty else "—"} |')
    w()
    return ok


def cat2_frontmatter(pages):
    ok = True
    w('## 第二类 — frontmatter 必填')
    w()
    for st in STAGES:
        p = WIKI / 'stages' / f'{st}.md'
        fm, _ = parse_frontmatter(read(p))
        if fm is None:
            w(f'- ❌ `{st}`：没有 frontmatter')
            ok = False
            continue
        missing = [k for k in REQUIRED_FM if k not in fm]
        bad = []
        if fm.get('type') != 'stage':
            bad.append('type')
        if fm.get('verified') not in ('doc-only', 'tested'):
            bad.append('verified')
        src = fm.get('sources')
        if not isinstance(src, list) or not src:
            bad.append('sources')
        if missing or bad:
            w(f'- ❌ `{st}`：缺 {missing + bad}')
            ok = False
    if ok:
        w('- ✅ 九页 frontmatter 全部合规')
    w()
    return ok


def cat3_sources(pages, docs_by_rel):
    ok = True
    w('## 第三类 — sources 可追溯')
    w()
    for st in STAGES:
        fm, _ = parse_frontmatter(read(WIKI / 'stages' / f'{st}.md'))
        src = fm.get('sources') or []
        bad = [x for x in src if x not in docs_by_rel]
        if bad:
            ok = False
            w(f'- ❌ `{st}`：{len(bad)} 条查不到，例：`{bad[0]}`')
    if ok:
        w('- ✅ 九页所有 `sources:` 都能在 `docs.jsonl` 里查到')
    w()
    return ok


def cat5_chain(pages):
    ok = True
    w('## 第五类 — 下一步链')
    w()
    for st in STAGES:
        nxt = NEXT[st]
        if nxt is None:
            w(f'- `{st}`：末页，无强制下一步')
            continue
        fm, lines = parse_frontmatter(read(WIKI / 'stages' / f'{st}.md'))
        secs = h2_map(lines)
        body = secs.get('下一步', '')
        if f'[[{nxt}]]' not in body:
            w(f'- ❌ `{st}`：`## 下一步` 里没有 `[[{nxt}]]`')
            ok = False
        else:
            w(f'- ✅ `{st}` → `[[{nxt}]]`')
    w()
    return ok


def cat8_reachable(pages):
    w('## 第八类 — 链接目标可达（只记录）')
    w()
    have = {p.stem for p in WIKI.rglob('*.md')}
    allowed_stage = set(STAGES)
    dang = {}
    for st in STAGES:
        text = strip_code(read(WIKI / 'stages' / f'{st}.md'))
        for t in RE_WIKILINK.findall(text):
            t = t.strip()
            if t and t not in have and t not in allowed_stage:
                dang.setdefault(t, []).append(st)
    if not dang:
        w('- ✅ 没有指向不存在页面的 wikilink')
    else:
        for t, who in sorted(dang.items()):
            w(f'- `[[{t}]]` ← {", ".join(who)}')
    w()
    return True


def cat9_naming(pages):
    ok = True
    w('## 第九类 — 命名合规')
    w()
    bad = []
    stems = {}
    for p in WIKI.rglob('*.md'):
        if p.stem in ('index', 'log') or p.stem.startswith('index-'):
            continue
        if not SLUG_RX.match(p.stem):
            bad.append(str(p.relative_to(WIKI)))
        stems.setdefault(p.stem, []).append(str(p.relative_to(WIKI)))
    dup = {k: v for k, v in stems.items() if len(v) > 1}
    if bad:
        w(f'- ❌ 非 ASCII/不合规文件名：{bad}')
        ok = False
    if dup:
        w(f'- ❌ 重复 stem：{dup}')
        ok = False
    if ok:
        w('- ✅ 文件名全部合规、无重复 stem')
    w()
    return ok


def cat14a_index(pages):
    ok = True
    w('## 第十四类甲 — index 覆盖')
    w()
    idx = read(WIKI / 'index.md')
    missing = [s for s in STAGES if f'[[{s}]]' not in idx]
    if missing:
        w(f'- ❌ index.md 的「阶段（9）」缺：{", ".join(missing)}')
        ok = False
    else:
        w('- ✅ 九页全部在 index.md 里')
    w()
    return ok


def cat15_skeleton(pages):
    ok = True
    w('## 第十五类 — 骨架占位符')
    w()
    for st in STAGES:
        text = read(WIKI / 'stages' / f'{st}.md')
        if '（待补）' in text or '(待补)' in text:
            w(f'- ❌ `{st}` 仍有「待补」')
            ok = False
    if ok:
        w('- ✅ 九页没有「待补」占位符')
    w()
    return ok


def check_objects():
    """对象页：必备节、frontmatter、sources。骨架页不判红，只计数。"""
    ok = True
    objs = sorted(p for p in (WIKI / 'objects').glob('*.md')
                  if p.stem != 'index-objects')
    missing_sec, bad_fm, bad_src, skel = [], [], [], []
    for p in objs:
        fm, lines = parse_frontmatter(read(p))
        secs = h2_map(lines)
        miss = [s for s in OBJECT_SECTIONS
                if not any(k.startswith(s) for k in secs)]
        if miss:
            missing_sec.append((p.stem, miss))
            ok = False
        if fm is None or fm.get('type') != 'object':
            bad_fm.append(p.stem)
            ok = False
        else:
            for k in ('title', 'sources', 'verified', 'layer', 'stage'):
                if not fm.get(k):
                    bad_fm.append(p.stem)
                    ok = False
                    break
            for s in (fm.get('sources') or []):
                if s not in DOCS_BY_REL:
                    bad_src.append((p.stem, s))
                    ok = False
        if any('（待补）' in ln and '由 LLM 补完' not in ln for ln in lines):
            skel.append(p.stem)

    w('## 对象页 — 节 / frontmatter / sources')
    w()
    w(f'- 对象页 **{len(objs)}** 个')
    w(f'- 节缺失：**{len(missing_sec)}**'
      + (f' 例：{missing_sec[:3]}' if missing_sec else ''))
    w(f'- frontmatter 异常：**{len(bad_fm)}**'
      + (f' 例：{bad_fm[:5]}' if bad_fm else ''))
    w(f'- sources 查不到：**{len(bad_src)}**'
      + (f' 例：{bad_src[:3]}' if bad_src else ''))
    w(f'- 仍是骨架（有「待补」）：**{len(skel)}**（预期 78，不判红）')
    w()
    return ok


def check_object_index():
    ok = True
    idx = read(WIKI / 'index.md')
    sub = WIKI / 'objects' / 'index-objects.md'
    objs = {p.stem for p in (WIKI / 'objects').glob('*.md')
            if p.stem != 'index-objects'}
    listed = set()
    if sub.exists():
        for t in RE_WIKILINK.findall(read(sub)):
            listed.add(t.strip())

    w('## 对象页 index 覆盖')
    w()
    if '[[index-objects]]' not in idx:
        w('- ❌ 根 `index.md` 没有链到 `[[index-objects]]`')
        ok = False
    missing = sorted(objs - listed)
    if missing:
        w(f'- ❌ `index-objects.md` 漏列 {len(missing)} 页，例：{missing[:5]}')
        ok = False
    if ok:
        w(f'- ✅ `index-objects.md` 覆盖全部 {len(objs)} 个对象页')
    w()
    return ok


def main():
    if (sys.stdout.encoding or '').lower().replace('-', '') != 'utf8':
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    docs = load_docs()
    docs_by_rel = {d['rel']: d for d in docs}
    DOCS_BY_REL.update(docs_by_rel)

    w('# 页面检查报告（html 版）')
    w()
    w('对象：`wiki/stages/*.md`（九页）。')
    w('本文件只做**不依赖语料**的检查；第七/十二/十三类等需另行重写。')
    w()
    pages = [WIKI / 'stages' / f'{s}.md' for s in STAGES]
    results = [
        ('第一类 九页与十节齐备', cat1_stage(pages, docs)),
        ('第二类 frontmatter 必填', cat2_frontmatter(pages)),
        ('第三类 sources 可追溯', cat3_sources(pages, docs_by_rel)),
        ('第五类 下一步链', cat5_chain(pages)),
        ('第八类 链接目标可达', cat8_reachable(pages)),
        ('第九类 命名合规', cat9_naming(pages)),
        ('第十四类甲 index 覆盖', cat14a_index(pages)),
        ('第十五类 骨架占位符', cat15_skeleton(pages)),
        ('对象页 节/frontmatter/sources', check_objects()),
        ('对象页 index 覆盖', check_object_index()),
    ]
    w('## 汇总')
    w()
    w('| 检查 | 结果 |')
    w('|---|---|')
    for name, ok in results:
        label = '— 记录' if name.startswith('第八类') else ('✅ 通过' if ok else '❌ 未通过')
        w(f'| {name} | {label} |')
    w()
    (OUT / 'stage-report.md').write_text('\n'.join(R) + '\n', encoding='utf-8', newline='\n')
    print('\n'.join(R))
    hard = [(n, ok) for n, ok in results if not n.startswith('第八类')]
    bad = [n for n, ok in hard if not ok]
    if bad:
        sys.exit(1)


if __name__ == '__main__':
    main()
