#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""objscaffold.py — 建对象页骨架（html 版）。

与 md 版同职责：
  · `## 语法 / 参数` 从 sections.jsonl 逐字取（含真表）
  · `## 报错条件` 从 sections.jsonl 逐字取
  · 其余五节留 `（待补）` 给 LLM

用法：
  python objscaffold.py                     # 建 wiki-plan.csv 里 status=todo 的页
  python objscaffold.py --force             # 覆盖已存在的页
  python objscaffold.py --refresh-syntax <slug> [...]
  python objscaffold.py --refresh-errors <slug> [...] | --all
"""

import csv
import re
import sys
from datetime import date
from pathlib import Path

import objpack as op

BASE = Path(__file__).resolve().parent.parent
OUT = BASE / 'extract'
WIKI = BASE / 'wiki'
PLAN = OUT / 'wiki-plan.csv'

DIRS = {'object': 'objects', 'concept': 'concepts', 'constraint': 'constraints',
        'mapping': 'mappings', 'error': 'errors', 'version': 'versions',
        'stage': 'stages'}

LINK = re.compile(r'\[([^\]]*)\]\(\s*<?([^)>\s]+)>?\s*\)')
PLACEHOLDER = '（待补）'


def unlink(m):
    """`[T](P)` → ``T``（raw: `P`）——两个都留，路径是回查原文的唯一线索。"""
    t, p = m.group(1), m.group(2)
    return f'`{t.strip() or p}`（raw: `{p}`）'


HEAD = '## 语法 / 参数'
MARK_BEGIN = ('<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，'
              '**手改会在下次 `--refresh-syntax` 时消失** -->')
MARK_END = '<!-- 语法节 end -->'

ERR_HEAD = '## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）'
ERR_BEGIN = ('<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，'
             '**手改会在下次 `--refresh-errors` 时消失** -->')
ERR_END = '<!-- 报错节 end -->'

PAGE_HEADS = ('是什么', '典型用法', '和谁有关', '版本', '出处')


def rels_of(row):
    """rel 列可写多篇：`主文档;补充1;补充2`。第一篇是主文档（语法节从它抽）。"""
    return [x.strip() for x in (row.get('rel') or '').split(';') if x.strip()]


def syntax_block(rel):
    parts, srcs = op.collect_syntax(rel)
    w = [HEAD, '', MARK_BEGIN, '']
    if not parts:
        w += ['**没有加标记的语法段。** 定义文档里没有 `Syntax` / `Parameters` / `Example`',
              '这类**段标记**。本脚本一个字都不收录——没有段标记时「哪一段是语法」是猜，',
              '而猜就是编。要看原文：`python show.py <分类号>`。', '']
        w += [MARK_END, '']
        return '\n'.join(w)

    tot = sum(len(b) for _, b in parts)
    w += [f'> 本节 **{tot:,} 字符逐字取自** `<{rel}>`。**不是转述。**',
          '> 脚本能产出的不许调 LLM；参数表照抄，不改写。',
          '> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。', '']
    for name, body in parts:
        w += [f'### {name}', '', LINK.sub(unlink, body).strip(), '']
    w += [MARK_END, '']
    return '\n'.join(w)


def error_block(rel):
    parts = op.collect_errors(rel)
    if not parts:
        return ''
    w = [ERR_HEAD, '', ERR_BEGIN, '',
         f'> 本节**逐字取自** `<{rel}>` 的 '
         + '、'.join('`## ' + n + '`' for n, _ in parts) + ' 段。**不是转述。**',
         '> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。', '']
    for name, body in parts:
        w += [f'### {name}', '', LINK.sub(unlink, body).strip(), '']
    w += [ERR_END, '']
    return '\n'.join(w)


def build(row):
    rels = rels_of(row)
    rel = rels[0]
    d = op.load_docs().get(rel, {})
    title = ((d.get('frontmatter') or {}).get('title') or row['slug'])
    today = date.today().isoformat()

    w = ['---',
         f"type: {row['type']}",
         f'title: {title}']
    if row.get('layer'):
        w.append(f"layer: {row['layer']}")
    if row.get('stage'):
        w.append(f"stage: {row['stage']}")
    w += ['tags: []', 'related: []', 'sources:']
    w += [f'  - {r}' for r in rels]
    w += [f'created: {today}', f'updated: {today}', 'verified: doc-only',
          '---', '', f'# {title}', '',
          '<!-- 骨架由 `extract/objscaffold.py` 生成。',
          '     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；',
          '     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->', '']

    w += [syntax_block(rel)]
    eb = error_block(rel)
    if eb:
        w += [eb]
    for sec in ['是什么', '典型用法', '和谁有关', '版本', '出处']:
        w += [f'## {sec}', '', PLACEHOLDER, '']
    return '\n'.join(w), title


def section_end(text, i):
    k = text.find(MARK_END, i)
    if k >= 0:
        e = text.find('\n', k)
        return len(text) if e < 0 else e + 1
    best = -1
    for h in PAGE_HEADS:
        k = text.find(f'\n## {h}', i + 1)
        if k >= 0 and (best < 0 or k < best):
            best = k
    return best if best >= 0 else len(text)


def refresh(row):
    p = WIKI / DIRS[row['type']] / f"{row['slug']}.md"
    text = p.read_text(encoding='utf-8')
    i = text.find(HEAD)
    if i < 0:
        raise SystemExit(f'❌ {p.name} 里找不到 `{HEAD}`——不猜位置，先看页面')
    j = section_end(text, i)
    block = syntax_block(rels_of(row)[0])
    if MARK_END not in text[i:j]:
        inside = set(re.findall(r'^## .+$', block, re.M))
        strangers = [h for h in re.findall(r'^## .+$', text[i:j], re.M) if h not in inside]
        if strangers:
            raise SystemExit(f'❌ {p.name}：语法节里没有 `{MARK_END}`，兜底会吞掉 '
                             f'{strangers}——拒绝执行')
    new = text[:i] + block + text[j:]
    if new == text:
        print(f'＝ 无变化：{p.name}')
        return
    p.write_text(new, encoding='utf-8')
    print(f'🔄 {p.name}  语法节重刷（{len(text):,} → {len(new):,}，{len(new)-len(text):+,}）')


def refresh_errors(row):
    p = WIKI / DIRS[row['type']] / f"{row['slug']}.md"
    text = p.read_text(encoding='utf-8')
    block = error_block(rels_of(row)[0])
    if ERR_BEGIN in text:
        i = text.find(ERR_HEAD)
        if i < 0:
            raise SystemExit(f'❌ {p.name}：有报错节标记却没有标题 `{ERR_HEAD}`')
        j = text.index(ERR_END, i) + len(ERR_END)
        e = text.find('\n', j)
        j = len(text) if e < 0 else e + 1
        if not block:
            raise SystemExit(f'❌ {p.name}：页里有报错节，但已取不到材料')
        p.write_text(text[:i] + block.rstrip('\n') + '\n' + text[j:], encoding='utf-8')
        return 'refreshed'
    if not block:
        return 'skip'
    k = text.find(MARK_END)
    if k < 0:
        raise SystemExit(f'❌ {p.name}：找不到 `{MARK_END}`，无法定位插入点')
    e = text.find('\n', k) + 1
    p.write_text(text[:e] + '\n' + block + text[e:], encoding='utf-8')
    return 'inserted'


def main():
    if (sys.stdout.encoding or '').lower().replace('-', '') != 'utf8':
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    force = '--force' in sys.argv

    rows = [r for r in csv.DictReader(PLAN.open(encoding='utf-8'))
            if r.get('slug') and not r['slug'].startswith('#')]
    have = {p.stem for p in WIKI.rglob('*.md')}
    seen = {}
    for r in rows:
        s = r['slug']
        if s in seen:
            raise SystemExit(f'❌ 两条计划撞同一个 slug：{s}')
        seen[s] = r['rel']
        if r['type'] not in DIRS:
            raise SystemExit(f'❌ 未知 type：{r["type"]}（{s}）')
        if r['status'] not in ('todo', 'skeleton', 'done'):
            raise SystemExit(f'❌ 未知 status：{r["status"]}（{s}）')

    docs = op.load_docs()
    for r in rows:
        for x in rels_of(r):
            if x not in docs:
                raise SystemExit(f'❌ {r["slug"]} 的 rel 不在 docs.jsonl 里：{x}')

    if '--refresh-errors' in sys.argv:
        k = sys.argv.index('--refresh-errors')
        rest = sys.argv[k + 1:]
        all_flag = '--all' in rest
        slugs = [s for s in rest if not s.startswith('--')]
        by = {r['slug']: r for r in rows}
        targets = ([r for r in rows if r['type'] == 'object'] if all_flag
                   else [by[s] for s in slugs if s in by])
        n = {'inserted': 0, 'refreshed': 0, 'skip': 0}
        for r in targets:
            n[refresh_errors(r)] += 1
        print(f"✅ 报错节：插入 {n['inserted']}、重刷 {n['refreshed']}、无材料 {n['skip']}")
        return

    if '--refresh-syntax' in sys.argv:
        k = sys.argv.index('--refresh-syntax')
        slugs = [s for s in sys.argv[k + 1:] if not s.startswith('--')]
        by = {r['slug']: r for r in rows}
        for s in slugs:
            if s not in by:
                raise SystemExit(f'❌ wiki-plan.csv 里没有这个 slug：{s}')
            refresh(by[s])
        return

    for r in rows:
        if r['status'] != 'todo':
            continue
        p = WIKI / DIRS[r['type']] / f"{r['slug']}.md"
        if p.exists() and not force:
            print(f'⏭  已存在，跳过：{p.name}（要覆盖加 --force）')
            continue
        if r['slug'] in have and not p.exists():
            raise SystemExit(f'❌ slug 撞上已存在的页：{r["slug"]}——先定限定词')
        text, title = build(r)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding='utf-8')
        print(f'✅ {p.relative_to(BASE)}  （{len(text):,} 字符）  {title}')


if __name__ == '__main__':
    main()
