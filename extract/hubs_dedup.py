# -*- coding: utf-8 -*-
"""枢纽排名（**去重版**）——html 版。

`hubs.csv` 的 `in_src` 有两个灌水来源，都要去掉：

1. **引用方重复**：同一篇页存在多个副本，各记一次引用。
2. **被引方重复**：同一对象有多个副本路径，入度散在多条路径上。

两端都必须归一到 `source_topic`（去掉扩展名与 `_N` 后缀）。

产出 `hubs-dedup.csv`：canonical topic、代表路径、标题、去重 in_src。
"""

import csv
import json
import re
from collections import defaultdict
from pathlib import Path

OUTDIR = Path(__file__).resolve().parent


def canon_topic(fm):
    t = ((fm or {}).get('source_topic') or '').strip()
    if not t:
        return None
    if t.lower().endswith(('.htm', '.html')):
        t = t.rsplit('.', 1)[0]
    return re.sub(r'_\d+$', '', t)


def main():
    docs = [json.loads(l) for l in open(OUTDIR / 'docs.jsonl', encoding='utf-8')]
    edges = [json.loads(l) for l in open(OUTDIR / 'edges.jsonl', encoding='utf-8')]

    rel2topic, title = {}, {}
    for d in docs:
        t = canon_topic(d.get('frontmatter'))
        if t:
            rel2topic[d['rel']] = t
        if t and (t not in title or len(d['rel']) < len(title[t][0])):
            title[t] = (d['rel'], (d.get('title') or '').strip())

    refs, raw = defaultdict(set), defaultdict(set)
    skipped = 0
    for e in edges:
        if e.get('kind') != 'inline':
            skipped += 1
            continue
        src, tgt = e.get('from'), e.get('to')
        if not tgt:
            continue
        raw[tgt].add(src)
        cs, ct = rel2topic.get(src), rel2topic.get(tgt)
        if cs is None or ct is None:
            continue
        refs[ct].add(cs)

    # 交叉验证：未去重入度必须与 hubs.csv 的 in_src 逐行相等
    xcheck, bad = 0, []
    for r in csv.DictReader((OUTDIR / 'hubs.csv').open(encoding='utf-8')):
        mine = len(raw.get(r['path'], ()))
        theirs = int(r['in_src'])
        xcheck += 1
        if mine != theirs:
            bad.append((r['path'], theirs, mine))
    print(f'交叉验证：与 hubs.csv 逐行比对 {xcheck} 行，不符 {len(bad)} 行')
    for p, t, m in bad[:5]:
        print(f'    {p}: hubs.csv={t} 本脚本={m}')
    if bad:
        raise SystemExit('未去重入度对不上，去重结果不可信 —— 先查明再往下走')

    rows = []
    for t, s in refs.items():
        rel, ti = title.get(t, ('', ''))
        rows.append({'topic': t, 'rel': rel, 'title': ti, 'in_src': len(s)})
    rows.sort(key=lambda r: (-r['in_src'], r['topic']))

    out = OUTDIR / 'hubs-dedup.csv'
    with out.open('w', encoding='utf-8', newline='\n') as f:
        wr = csv.DictWriter(f, fieldnames=['topic', 'rel', 'title', 'in_src'])
        wr.writeheader()
        wr.writerows(rows)

    n20 = sum(1 for r in rows if r['in_src'] >= 20)
    print(f'唯一 topic {len(title)} 个；有入度的 {len(rows)} 个')
    print(f'剔除非 inline 边 {skipped} 条')
    print(f'in_src >= 20: {n20} 个；>= 10: '
          f'{sum(1 for r in rows if r["in_src"] >= 10)} 个；'
          f'>= 5: {sum(1 for r in rows if r["in_src"] >= 5)} 个')
    print('\n去重后前 20：')
    for r in rows[:20]:
        print(f'{r["in_src"]:>4}  {r["title"][:44]:<44} {r["topic"]}')
    print(f'\n-> {out}')


if __name__ == '__main__':
    main()
