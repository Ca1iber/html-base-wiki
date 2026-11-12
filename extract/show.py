#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# show.py — 按分类号打印 HTML 语料原文（只读，给建页时核对用）
#
# 用法  python show.py 02.06.05 01.07.01          # 精确匹配分类号
#       python show.py --head 02.06.05             # 只打前 800 字符
#       python show.py --grep 定义                  # 按标题关键词找
#       python show.py --list 02.06.03.02          # 列出子树下的全部文档（建页覆盖面清单）
#
# 与 md 版的 show.py 同名、同参数、同输出格式。
# 区别只在背后读的是原始 HTML，返回的是抽取后的文本（表格按结构展开）。
#
# 存在的理由：建页时**不许凭印象写**，每句话都要能回到原文。
# 这个脚本让「回原文」是一行命令，而不是一次搜索。

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import extract_html as E          # 复用解析器与表格渲染

INDEX = Path(__file__).resolve().parent / 'docs.jsonl'
RE_STEM = re.compile(r'(\d+(?:\.\d+)*)_(.*)')


def resolve(topic):
    """source_topic 通常是扁平文件名；少数在 search 子目录里，需回退查找。"""
    p = E.RAW / topic
    if p.exists():
        return p
    for q in E.RAW.rglob(topic):
        return q
    return None


def body(topic, limit=None):
    p = resolve(topic)
    if p is None:
        return f'(找不到源文件：{topic})'
    root = E.parse_html(p)
    art = E.find_article(root)
    if art is root:
        for n in E.iter_nodes(root):
            if n.tag == 'body':
                art = n
                break
    txt = E.text_with_tables(art).strip()
    return txt[:limit] if limit else txt


def stem_of(rel):
    return rel.split('/')[-1].rsplit('.', 1)[0]


def fix_links(txt, topic2rel):
    """把 `](98752.htm)` 换成 `](分类路径.htm)`，与 md 版一致。"""
    def repl(m):
        href = m.group(1)
        base, sep, anchor = href.partition('#')
        return '](' + topic2rel.get(base, base) + sep + anchor + ')'
    return re.sub(r'\]\(([^)\s]+)\)', repl, txt)


def main():
    if (sys.stdout.encoding or '').lower().replace('-', '') != 'utf8':
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')

    args = sys.argv[1:]
    limit = None
    if args and args[0] == '--head':
        limit = 800
        args = args[1:]
    grep = None
    if args and args[0] == '--grep':
        grep = args[1]
        args = args[2:]
    list_prefix = None
    if args and args[0] == '--list':
        list_prefix = args[1]
        args = args[2:]

    if not INDEX.exists():
        sys.exit(f'缺少索引：{INDEX}\n先跑 python extract_html.py')

    rows = [json.loads(l) for l in INDEX.open(encoding='utf-8')]
    topic2rel = {(d.get('frontmatter') or {}).get('source_topic'): d['rel'] for d in rows}

    if grep:
        for d in rows:
            stem = stem_of(d['rel'])
            m = RE_STEM.match(stem)
            hay = (d.get('title') or '') + ' ' + stem
            if grep.lower() in hay.lower():
                print(f'{m.group(1) if m else "?":14s} {d["rel"]}')
        return

    if list_prefix is not None:
        n = 0
        for d in rows:
            stem = stem_of(d['rel'])
            if not stem.startswith(list_prefix):
                continue
            m = RE_STEM.match(stem)
            if not m:
                continue
            n += 1
            print(f'{m.group(1):20s} {d.get("title") or stem}')
        print(f'# {n} 条', file=sys.stderr)
        return

    want = set(args)
    if not want:
        sys.exit(__doc__ or '用法见文件头')

    hit = 0
    for d in rows:
        stem = stem_of(d['rel'])
        m = RE_STEM.match(stem)
        if not m or m.group(1) not in want:
            continue
        hit += 1
        print('=' * 74)
        print(f'#### {d["rel"]}   [{d["bytes"]}B]')
        topic = (d.get('frontmatter') or {}).get('source_topic') or stem + '.htm'
        print(fix_links(body(topic, limit), topic2rel))
        print()

    if not hit:
        sys.exit(f'没找到：{sorted(want)}')


if __name__ == '__main__':
    main()
