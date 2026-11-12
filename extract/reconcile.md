# 索引对账：md 版 vs html 版

- md 版：`F:\master-dev\understand-anything-wiki\extract`
- html 版：`F:\master-dev\html-wiki\extract`

## 1. 文档覆盖

| | 数量 |
|---|---:|
| md 版 | 9,398 |
| html 版 | 9,393 |
| 两边都有 | 9,393 |
| 只在 md | 0 |
| 只在 html | 0 |
| 结构（struct_sections）完全相同 | 9,332 / 9,393 |

### 结构差异归类

| 类别 | 文档数 | 含义 |
|---|---:|---|
| md 把 h1 标题也当成节 | 11 | 设计差异，不是内容丢失 |
| **md 少了整节** | **49** | **html 版捞回来了** |
| md 多出节 | 1 | 反向，需个别核对 |

md 少节的样例：
- `96863.htm`：Member Functions
- `29154.htm`：Syntax
- `26644.htm`：Parameters
- `71358.htm`：Member functions
- `126273.htm`：Class definition

md 多出节的样例：
- `353396.htm`：Functional changes, Related information

## 2. 表格

| | 数量 |
|---|---:|
| md 版含「表格指针」的段 | 2,675 |
| html 版含 `[表]` 的段 | 2,698 |
| html 版 `[表]` 总数 | 3,494 |
| html 版 `[子表]` 总数 | 152 |

## 3. 交叉引用（不含 index 目录链接）

| | 数量 |
|---|---:|
| md 版 | 30,459 |
| html 版 | 32,159 |
| 两边都有 | 30,445 |
| 只在 md | 14 |
| 只在 html | 1,714 |

> md 独有的 14 条全部是 Doxygen 页的**导航面包屑**
> （`div.header > div.headertitle > div.subTitle > a`），不是正文引用；
> html 版只取内容容器 `div.contents`，故不计。
> html 独有的 1,714 条主要是表格单元格里的链接——md 把表换成指针时丢了。

## 4. 编码

| | 含坏字的段 |
|---|---:|
| md 版 | 0 |
| html 版 | 0 |

> **注意**：md 版的编码损坏（1,053 篇 / 7,906 段）已在 2026-09/10 修复，
> 所以当前两边都是 0。html 版的优势是「不需要修」，不是「比当前 md 更干净」。

## 5. 失败分类

| md 版 | html 版 |
|---|---|
| no_frontmatter: 5 | no_frontmatter: 0 |
| no_h1: 6 | no_h1: 42 |
| no_headings: 55 | no_headings: 0 |
| no_sections: 0 | no_sections: 1110 |
| not_in_catalog: 5 | not_in_catalog: 0 |

## 6. 结论

- 文档覆盖完全一致：9,393 篇两边都有，零缺口。
- **49 篇**在 md 转换时丢了整节，html 版全部捞回。
- html 版有 **3,494 张真表**（另有 152 张嵌套子表）；
  md 版对应位置是 **2,675 段表格指针**。
- 交叉引用：html 版多 **1,714** 条，md 版多 14 条。
- 抽取器结构自检：99.35% 的文档节集合完全一致。
