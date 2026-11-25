# 页面检查报告（html 版）

对象：`wiki/stages/*.md`（九页）。
本文件只做**不依赖语料**的检查；第七/十二/十三类等需另行重写。

## 第一类 — 九页与十节齐备

| stage | 存在 | 节 | 空节 |
|---|---|---|---|
| project | ✅ | 10/10 | — |
| pin | ✅ | 10/10 | — |
| level | ✅ | 10/10 | — |
| timing | ✅ | 10/10 | — |
| pattern | ✅ | 10/10 | — |
| testmethod | ✅ | 10/10 | — |
| testflow | ✅ | 10/10 | — |
| run | ✅ | 10/10 | — |
| results | ✅ | 10/10 | — |

## 第二类 — frontmatter 必填

- ✅ 九页 frontmatter 全部合规

## 第三类 — sources 可追溯

- ✅ 九页所有 `sources:` 都能在 `docs.jsonl` 里查到

## 第五类 — 下一步链

- ✅ `project` → `[[pin]]`
- ✅ `pin` → `[[level]]`
- ✅ `level` → `[[timing]]`
- ✅ `timing` → `[[pattern]]`
- ✅ `pattern` → `[[testmethod]]`
- ✅ `testmethod` → `[[testflow]]`
- ✅ `testflow` → `[[run]]`
- ✅ `run` → `[[results]]`
- `results`：末页，无强制下一步

## 第八类 — 链接目标可达（只记录）

- ✅ 没有指向不存在页面的 wikilink

## 第九类 — 命名合规

- ✅ 文件名全部合规、无重复 stem

## 第十四类甲 — index 覆盖

- ✅ 九页全部在 index.md 里

## 第十五类 — 骨架占位符

- ✅ 九页没有「待补」占位符

## 对象页 — 节 / frontmatter / sources

- 对象页 **289** 个
- 节缺失：**0**
- frontmatter 异常：**0**
- sources 查不到：**0**
- 仍是骨架（有「待补」）：**78**（预期 78，不判红）

## 对象页 index 覆盖

- ✅ `index-objects.md` 覆盖全部 289 个对象页

## 汇总

| 检查 | 结果 |
|---|---|
| 第一类 九页与十节齐备 | ✅ 通过 |
| 第二类 frontmatter 必填 | ✅ 通过 |
| 第三类 sources 可追溯 | ✅ 通过 |
| 第五类 下一步链 | ✅ 通过 |
| 第八类 链接目标可达 | — 记录 |
| 第九类 命名合规 | ✅ 通过 |
| 第十四类甲 index 覆盖 | ✅ 通过 |
| 第十五类 骨架占位符 | ✅ 通过 |
| 对象页 节/frontmatter/sources | ✅ 通过 |
| 对象页 index 覆盖 | ✅ 通过 |

