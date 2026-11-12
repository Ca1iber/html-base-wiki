#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""extract_html.py — 从 TDC 原始 HTML 抽结构数据，产出建 wiki 页的依据。

零 LLM / 零网络 / **零第三方依赖**（仅 stdlib，与 md 臂的 extract.py 一致）。

输入  F:\\master-dev\\dorm-wsl-sytest\\tdc-html\\raw\\*.htm
      F:\\master-dev\\dorm-wsl-sytest\\tdc-html\\raw\\toc.xml
输出  F:\\master-dev\\html-wiki\\extract\\
        docs.jsonl      每篇一行（字段与 md 臂逐名相同）
        edges.jsonl     每条交叉引用一行
        sections.jsonl  每个结构段落一行
        failures.jsonl  解析失败 / 异常
        hubs.csv        入度 / 出度

设计约束（见 schema-pipeline.md）：
  · rel 从 toc.xml 深度优先推编号，再按 md 臂的规则拼路径
  · <table id="vr"> 是空壳，必须跳过
  · <h1 class="topictitle1"> 是页标题，不是节
  · 表格按结构写入 body，不压平成管道表
"""

import csv
import json
import re
import sys
from collections import Counter, defaultdict
from html.parser import HTMLParser
from pathlib import Path
import xml.etree.ElementTree as ET

# ---------------------------------------------------------------- 配置

RAW = Path(r'F:\master-dev\dorm-wsl-sytest\tdc-html\raw')
OUTDIR = Path(r'F:\master-dev\html-wiki\extract')

CONTEXT_MIN = 20
CONTEXT_MERGE_MAX = 3
CONTEXT_MAX = 300
FIRST_PARA_MAX = 300
SECTION_MAX = 6000
LABEL_MAX = 72          # md 臂的文件名规则：标签截到 72 字符

SECTION_GROUPS = {
    'constraint': {'Dependency', 'Dependencies', 'Predependencies', 'Postdependencies',
                   'Dependency and constraints', 'Dependency and Constraints',
                   'Before you begin', 'Prerequisites', 'Preconditions', 'Requirements'},
    'procedure':  {'Procedure', 'Procedures', 'About this task', 'What to do next'},
    'error':      {'Errors', 'Error', 'Warnings', 'Limits'},
    'version':    {'Functional changes'},
    'syntax':     {'Syntax', 'Parameters', 'Return value', 'Return Value',
                   'Prototype', 'Member functions', 'Class definition',
                   'Example', 'Examples'},
    'concept':    {'Mode of operation', 'Application'},
    'related':    {'Related information', 'Further information', 'More Info', 'Subtopics'},
}
SECTION_H2 = {h: g for g, hs in SECTION_GROUPS.items() for h in hs}

RE_HREF = re.compile(r'^(?:[^#]*?)([^/#]+\.(?:htm|html))?(?:#(.+))?$')
VOID = {'br', 'img', 'hr', 'meta', 'link', 'input', 'area', 'base', 'col',
        'embed', 'param', 'source', 'track', 'wbr'}
AUTO_CLOSE = {'p': {'p'}, 'li': {'li'}, 'tr': {'tr'},
              'td': {'td', 'th'}, 'th': {'td', 'th'}, 'option': {'option'}}

BLOCK_TAGS = {'p', 'div', 'li', 'ul', 'ol', 'tr', 'br', 'h1', 'h2', 'h3', 'h4',
              'h5', 'h6', 'pre', 'table', 'section', 'article', 'nav', 'figure'}


def slug(s):
    """md 臂的 slug 规则：非字母数字/点/连字符 → 下划线，去首尾，标签截 72。"""
    s = re.sub(r'[^A-Za-z0-9.\-]', '_', s)
    s = s.strip('_.')
    if len(s) > LABEL_MAX:
        s = s[:LABEL_MAX].rstrip('_')
    return s


# ---------------------------------------------------------------- 极简 DOM

class Node:
    __slots__ = ('tag', 'attrs', 'children', 'parent', 'line')

    def __init__(self, tag, attrs, parent, line):
        self.tag = tag
        self.attrs = attrs
        self.children = []
        self.parent = parent
        self.line = line

    def get(self, k, default=None):
        return self.attrs.get(k, default)

    def has_class(self, name):
        return name in (self.attrs.get('class') or '').split()


class DomBuilder(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node('#root', {}, None, 0)
        self.stack = [self.root]

    def _push(self, tag, attrs):
        # 自动闭合：<p> 遇 <p>、<li> 遇 <li> …
        close = AUTO_CLOSE.get(tag)
        if close:
            while len(self.stack) > 1 and self.stack[-1].tag in close:
                self.stack.pop()
        n = Node(tag, dict(attrs), self.stack[-1], self.getpos()[0])
        self.stack[-1].children.append(n)
        if tag not in VOID:
            self.stack.append(n)

    def handle_starttag(self, tag, attrs):
        self._push(tag, attrs)

    def handle_startendtag(self, tag, attrs):
        n = Node(tag, dict(attrs), self.stack[-1], self.getpos()[0])
        self.stack[-1].children.append(n)

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i].tag == tag:
                del self.stack[i:]
                return
        # 未匹配的结束标签：忽略

    def handle_data(self, data):
        if data:
            self.stack[-1].children.append(data)


def parse_html(path):
    text = path.read_text(encoding='utf-8', errors='replace')
    b = DomBuilder()
    b.feed(text)
    b.close()
    return b.root


# ---------------------------------------------------------------- 文本与遍历

def iter_nodes(node):
    for c in node.children:
        if not isinstance(c, str):
            yield c
            yield from iter_nodes(c)


def text_of(node, skip=('script', 'style')):
    """取节点文本，块级元素之间补换行。"""
    if node is None:
        return ''
    parts = []

    def walk(n):
        if isinstance(n, str):
            parts.append(n)
            return
        if n.tag in skip:
            return
        block = n.tag in BLOCK_TAGS
        if block:
            parts.append('\n')
        for c in n.children:
            walk(c)
        if block:
            parts.append('\n')

    walk(node)
    s = ''.join(parts)
    s = s.replace('\xa0', ' ')
    s = re.sub(r'[ \t\r\f\v]+', ' ', s)
    s = re.sub(r' *\n *', '\n', s)
    s = re.sub(r'\n{3,}', '\n\n', s)
    return s.strip()


def norm(s, limit=None):
    s = re.sub(r'\s+', ' ', s or '').strip()
    if limit and len(s) > limit:
        s = s[:limit]
    return s


def nearest_ancestor(node, tags):
    p = node.parent
    while p is not None:
        if p.tag in tags:
            return p
        p = p.parent
    return None


def in_code(node):
    p = node.parent
    while p is not None:
        if p.tag in ('code', 'pre'):
            return True
        p = p.parent
    return False


def find_article(root):
    """DITA 页用 <article>；Doxygen 页用 <div class="contents">。"""
    article = None
    for n in iter_nodes(root):
        if n.tag == 'article':
            article = n
            break
    if article is not None and any(
            c.tag == 'h1' and c.has_class('topictitle1')
            for c in iter_nodes(article)):
        return article
    for n in iter_nodes(root):
        if n.tag == 'div' and n.has_class('contents'):
            return n
    if article is not None:
        return article
    for n in iter_nodes(root):
        if n.tag == 'main':
            return n
    for n in iter_nodes(root):
        if n.tag == 'body':
            return n
    return root


def page_title(root, article):
    for n in iter_nodes(article):
        if n.tag == 'h1' and (n.has_class('topictitle1') or n.get('id') == 'ariaid-title1'):
            return norm(text_of(n))
    for n in iter_nodes(article):
        if n.tag == 'h1':
            return norm(text_of(n))
    # Doxygen 页：标题在 div.headertitle 或 <title>
    for n in iter_nodes(root):
        if n.tag == 'div' and n.has_class('headertitle'):
            return norm(text_of(n))
    for n in iter_nodes(root):
        if n.tag == 'title':
            return norm(text_of(n))
    return ''


def meta_content(root, name):
    for n in iter_nodes(root):
        if n.tag == 'meta' and (n.get('name') or '').lower() == name:
            return norm(n.get('content') or '')
    return ''


# ---------------------------------------------------------------- 表格

def render_table(node, depth=0):
    """把表格按结构写成文本：保留行/格/格内换行、跨行列标记与嵌套层级。"""
    cap = ''
    for n in iter_nodes(node):
        if n.tag == 'caption':
            cap = norm(text_of(n))
            break

    rows = []
    for tr in iter_nodes(node):
        if tr.tag != 'tr':
            continue
        # 只取属于本表（不经嵌套表）的行
        parent = tr.parent
        nested = False
        while parent is not None and parent is not node:
            if parent.tag == 'table':
                nested = True
                break
            parent = parent.parent
        if nested:
            continue
        cells = []
        for c in tr.children:
            if isinstance(c, str):
                continue
            if c.tag in ('td', 'th'):
                cells.append(c)
        if cells:
            rows.append(cells)

    if not rows:
        return ''

    ind = '  ' * depth
    tag = '[表]' if depth == 0 else '[子表]'
    rowtag = '行' if depth == 0 else '子行'
    out = []
    out.append(f'{ind}{tag} {cap}' if cap else f'{ind}{tag}')
    header = [norm(text_with_tables(c, depth + 1)) for c in rows[0] if c.tag == 'th']
    if header:
        out.append(f'{ind}列: ' + ' | '.join(header))
        body_rows = rows[1:]
    else:
        body_rows = rows

    for i, cells in enumerate(body_rows, 1):
        out.append(f'{ind}{rowtag} {i}:')
        for c in cells:
            t = text_with_tables(c, depth + 1)
            marks = []
            rs = c.get('rowspan')
            cs = c.get('colspan')
            if rs and rs != '1':
                marks.append(f'跨 {rs} 行')
            if cs and cs != '1':
                marks.append(f'跨 {cs} 列')
            mark = f' [{", ".join(marks)}]' if marks else ''
            lines = t.split('\n') if t else ['']
            out.append(f'{ind}  {lines[0]}{mark}')
            for ln in lines[1:]:
                out.append(f'{ind}    {ln}')
    return '\n'.join(out)


def text_with_tables(node, depth=0):
    """取文本；遇到嵌套表则递归渲染，而不是拍平。"""
    parts = []

    def walk(n):
        for c in n.children:
            if isinstance(c, str):
                parts.append(c)
            elif c.tag in ('script', 'style'):
                continue
            elif c.tag == 'table':
                parts.append('\n' + render_table(c, depth) + '\n')
            elif c.tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
                parts.append('\n' + '#' * int(c.tag[1]) + ' ' + norm(text_of(c)) + '\n')
            elif c.tag == 'pre':
                parts.append('\n```\n' + text_of(c) + '\n```\n')
            elif c.tag == 'a':
                href = (c.get('href') or '').strip()
                t = norm(text_of(c))
                parts.append(f'[{t}]({href})' if href else t)
            else:
                if c.tag in BLOCK_TAGS:
                    parts.append('\n')
                walk(c)
                if c.tag in BLOCK_TAGS:
                    parts.append('\n')

    walk(node)
    return clean_text(''.join(parts))


# ---------------------------------------------------------------- 分类树

def load_toc():
    """返回 (href_basename -> rel, href_basename -> number)。"""
    root = ET.parse(RAW / 'toc.xml').getroot()
    info = {}      # number -> (label, parent)
    href = {}      # number -> href

    def walk(e, path='', parent='00'):
        for i, c in enumerate(e, 1):
            num = f'{i:02d}' if not path else f'{path}.{i:02d}'
            info[num] = (c.get('label', ''), parent)
            href[num] = c.get('href') or c.get('topic') or ''
            walk(c, num, num)

    info['00'] = (root.get('label', ''), '')
    href['00'] = root.get('topic') or ''
    walk(root)

    def chain_of(n):
        ch = []
        while n:
            ch.append(n)
            n = info[n][1]
        return list(reversed(ch))

    def rel_of(num, ext):
        ch = chain_of(num)
        lvl = len(ch) - 1
        if lvl == 0:
            dirs = ['00_Overview']
        elif lvl == 1:
            dirs = [f'{ch[1]}_{slug(info[ch[1]][0])}']
        else:
            dirs = [f'{ch[1]}_{slug(info[ch[1]][0])}',
                    f'{ch[2]}_{slug(info[ch[2]][0])}']
        stem = f'{num}_{slug(info[num][0])}'
        return '/'.join(dirs + [stem + ext]), num

    by_href = {}
    for num, h in href.items():
        if not h:
            continue
        base = h.split('#')[0].split('/')[-1]
        if not base:
            continue
        ext = Path(base).suffix.lower()
        if ext not in ('.htm', '.html'):
            continue
        if base in by_href:
            continue
        rel, _ = rel_of(num, ext)
        by_href[base] = (rel, num)
    return by_href


def build_file_map():
    """所有源文件 → rel。键是**相对 RAW 的路径**（子目录文件不会撞名）。"""
    by_href = load_toc()
    files = sorted([p for p in RAW.rglob('*')
                    if p.is_file() and p.suffix.lower() in ('.htm', '.html')])
    mapping = {}
    unlisted = []
    for p in files:
        key = p.relative_to(RAW).as_posix()
        if p.name in by_href:
            mapping[key] = by_href[p.name][0]
        else:
            unlisted.append(p)
    for i, p in enumerate(sorted(unlisted, key=lambda x: x.relative_to(RAW).as_posix()), 1):
        key = p.relative_to(RAW).as_posix()
        mapping[key] = f'99_Unlisted_or_Unreferenced/99.{i:04d}_{slug(p.stem)}{p.suffix}'
    return mapping, by_href


# ---------------------------------------------------------------- 单篇抽取

def flatten_events(article):
    """按文档顺序产出 ('h', level, text, node) / ('t', text) / ('b', 结构化文本)。"""
    events = []

    def walk(n):
        for c in n.children:
            if isinstance(c, str):
                if c.strip():
                    events.append(('t', c))
                continue
            if c.tag == 'h1':
                continue
            if c.tag in ('h2', 'h3', 'h4', 'h5', 'h6'):
                events.append(('h', int(c.tag[1]), norm(text_of(c)), c))
                continue
            if c.tag in ('script', 'style'):
                continue
            if c.tag == 'table':
                events.append(('b', render_table(c)))
                continue
            if c.tag == 'pre':
                events.append(('b', '```\n' + text_of(c) + '\n```'))
                continue
            if c.tag in BLOCK_TAGS:
                events.append(('t', '\n'))
            walk(c)
            if c.tag in BLOCK_TAGS:
                events.append(('t', '\n'))

    walk(article)
    return events


SECTION_CI = {h.lower(): g for h, g in SECTION_H2.items()}


def group_of(text):
    return SECTION_CI.get((text or '').lower())


def extract_doc(path, rel, by_href, mapping, all_topic_ids):
    root = parse_html(path)
    article = find_article(root)
    title = page_title(root, article)
    headings = []
    for n in iter_nodes(article):
        if n.tag in ('h2', 'h3', 'h4'):
            t = norm(text_of(n))
            if t:
                headings.append({'level': int(n.tag[1]), 'text': t, 'line': n.line})

    # 段落
    sections = []
    cur = None
    cur_level = None
    parts = []
    for ev in flatten_events(article):
        if ev[0] == 'h':
            _, level, text, node = ev
            if cur is not None and level <= cur_level:
                sections.append(_make_section(rel, cur, cur_level, parts))
                cur = None
                parts = []
            if cur is None and group_of(text):
                cur = (text, node.line)
                cur_level = level
            elif cur is not None and level > cur_level:
                parts.append(text)
        elif ev[0] == 't':
            if cur is not None:
                parts.append(ev[1])
        else:  # 'b'
            if cur is not None:
                parts.append(ev[1])
    if cur is not None:
        sections.append(_make_section(rel, cur, cur_level, parts))

    # 链接
    edges = []
    link_kinds = Counter()
    for n in iter_nodes(article):
        if n.tag != 'a':
            continue
        href = (n.get('href') or '').strip()
        if not href:
            continue
        if re.match(r'^[A-Za-z][A-Za-z0-9+.\-]*://', href):
            link_kinds['external'] += 1
            continue
        base, _, anchor = href.partition('#')
        base_name = base.split('/')[-1]
        if not base_name:
            link_kinds['anchor'] += 1
            continue
        if not base_name.lower().endswith(('.htm', '.html')):
            link_kinds['asset'] += 1
            continue
        link_kinds['doc'] += 1
        to = mapping.get(base_name)
        anc = nearest_ancestor(n, {'p', 'li'})
        ctx_src = text_of(anc) if anc is not None else text_of(n.parent)
        ctx = norm(ctx_src, CONTEXT_MAX)
        if len(ctx) < CONTEXT_MIN and anc is not None:
            prev = anc.parent
            if prev is not None:
                ctx = norm(text_of(prev), CONTEXT_MAX)
        edges.append({
            'from': rel,
            'to': to,
            'to_raw': href,
            'anchor': anchor or None,
            'resolved': to is not None,
            'kind': 'inline',
            'in_code_span': in_code(n),
            'line': n.line,
            'link_text': norm(text_of(n)),
            'context': ctx,
        })

    # 正文统计
    body_text = text_of(article)
    first_para = ''
    for n in iter_nodes(article):
        if n.tag == 'p':
            t = norm(text_of(n), FIRST_PARA_MAX)
            if t:
                first_para = t
                break
    code_blocks = sum(1 for n in iter_nodes(article) if n.tag == 'pre')

    struct_sections = sorted({h['text'] for h in headings if group_of(h['text'])})
    struct_groups = sorted({group_of(h) for h in struct_sections})

    doc = {
        'rel': rel,
        'bytes': path.stat().st_size,
        'chars': len(body_text),
        'is_index': False,
        'in_catalog': not rel.startswith('99_'),
        'frontmatter': {
            'title': title,
            # 相对 RAW 的路径：顶层就是 `98550.htm`，
            # search 子目录里则是 `254242-search/all_0.html`（与 md 版一致）。
            'source_topic': path.relative_to(RAW).as_posix(),
            'source_html': rel,
        },
        'title': title or None,
        'headings': headings,
        'heading_count': len(headings),
        'first_para': first_para,
        'code_blocks': code_blocks,
        'out_degree': len(edges),
        'edge_angle': len(edges),
        'edge_plain': 0,
        'link_kinds': dict(link_kinds),
        'struct_sections': struct_sections,
        'struct_groups': struct_groups,
    }
    return doc, edges, sections


def clean_text(s):
    """归一化空白，但**保留行首缩进**（嵌套表的层级靠它）。"""
    s = (s or '').replace('\xa0', ' ')
    out = []
    for ln in s.split('\n'):
        lead = len(ln) - len(ln.lstrip(' '))
        body = re.sub(r'[ \t\r\f\v]+', ' ', ln.strip())
        out.append(' ' * lead + body)
    s = '\n'.join(out).strip('\n')
    s = re.sub(r'\n{3,}', '\n\n', s)
    return s.strip()


def _make_section(rel, cur, level, parts):
    body = clean_text('\n'.join(p for p in parts if p))
    chars = len(body)
    truncated = chars > SECTION_MAX
    if truncated:
        body = body[:SECTION_MAX]
    return {
        'doc': rel,
        'h2': cur[0],
        'group': group_of(cur[0]) or 'other',
        'level': level,
        'line': cur[1],
        'chars': chars,
        'truncated': truncated,
        'body': body,
    }


# ---------------------------------------------------------------- 主流程

def main(argv):
    limit = None
    if '--limit' in argv:
        limit = int(argv[argv.index('--limit') + 1])

    OUTDIR.mkdir(parents=True, exist_ok=True)
    mapping, by_href = build_file_map()
    files = sorted([p for p in RAW.rglob('*')
                    if p.is_file() and p.suffix.lower() in ('.htm', '.html')],
                   key=lambda p: p.relative_to(RAW).as_posix())
    if limit:
        files = files[:limit]

    # 链接解析用 basename → rel（href 里写的是扁平文件名）
    name2rel = {p.name: mapping[p.relative_to(RAW).as_posix()]
                for p in files if p.relative_to(RAW).as_posix() in mapping}

    docs, edges_all, sections_all, failures = [], [], [], []
    topic_ids = set(mapping)

    for i, p in enumerate(files, 1):
        rel = mapping.get(p.relative_to(RAW).as_posix())
        if rel is None:
            failures.append({'doc': p.name, 'kind': 'unmapped', 'detail': 'no rel'})
            continue
        try:
            doc, edges, sections = extract_doc(p, rel, by_href, name2rel, topic_ids)
        except Exception as e:  # 单篇失败不拖垮全库
            failures.append({'doc': rel, 'kind': 'parse_error', 'detail': repr(e)})
            continue
        docs.append(doc)
        edges_all.extend(edges)
        sections_all.extend(sections)
        if not doc['title']:
            failures.append({'doc': rel, 'kind': 'no_h1', 'detail': 'no topictitle1'})
        elif not doc['headings']:
            # 只有 h1、没有 h2–h4 的页是正常的，记为信息项，不是错误。
            failures.append({'doc': rel, 'kind': 'no_sections', 'detail': 'h1 only'})

    # hubs
    in_all = Counter()
    in_inline = Counter()
    in_src = defaultdict(set)
    out = Counter()
    for d in docs:
        out[d['rel']] = d['out_degree']
    for e in edges_all:
        if e['resolved']:
            in_all[e['to']] += 1
            if e['kind'] == 'inline':
                in_inline[e['to']] += 1
            in_src[e['to']].add(e['from'])

    with open(OUTDIR / 'docs.jsonl', 'w', encoding='utf-8', newline='\n') as f:
        for d in docs:
            f.write(json.dumps(d, ensure_ascii=False, sort_keys=True) + '\n')
    with open(OUTDIR / 'edges.jsonl', 'w', encoding='utf-8', newline='\n') as f:
        for e in edges_all:
            f.write(json.dumps(e, ensure_ascii=False, sort_keys=True) + '\n')
    with open(OUTDIR / 'sections.jsonl', 'w', encoding='utf-8', newline='\n') as f:
        for s in sections_all:
            f.write(json.dumps(s, ensure_ascii=False, sort_keys=True) + '\n')
    with open(OUTDIR / 'failures.jsonl', 'w', encoding='utf-8', newline='\n') as f:
        for x in failures:
            f.write(json.dumps(x, ensure_ascii=False, sort_keys=True) + '\n')

    with open(OUTDIR / 'hubs.csv', 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f)
        w.writerow(['path', 'in_all', 'in_inline', 'in_src', 'out', 'is_index'])
        for d in docs:
            rel = d['rel']
            w.writerow([rel, in_all[rel], in_inline[rel],
                        len(in_src[rel]), out[rel], 0])

    print(f'docs={len(docs)} edges={len(edges_all)} '
          f'sections={len(sections_all)} failures={len(failures)}')


if __name__ == '__main__':
    main(sys.argv[1:])
