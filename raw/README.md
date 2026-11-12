# raw/ — 证据层

**这里没有语料文件，这是故意的。**

语料约 60 MB，复制一份进 wiki 目录是浪费。本仓库的 `raw/` 只是**指针目录**；
真正的语料在下面的外部路径。**`tdc-html/raw/` 才是语料层，`html-wiki/raw/` 不是。**

## 位置

```
F:\master-dev\dorm-wsl-sytest\tdc-html\raw
```

## 规模

| 文件 | 数量 |
|---|---:|
| `*.htm` | 9,321 |
| `*.html` | 72 |
| `toc.xml` | 1 |
| `contexts.xml` | 1 |
| 图片（png / jpg / gif / svg） | 5,514 |

合计 **9,393 篇**。

## 结构

**语料目录是扁平的**：`raw/<topicid>.htm`，没有子目录。

分类树不来自目录，来自 `raw/toc.xml`（Eclipse help TOC，最深 12 层）。
按深度优先给节点编号即得分类号：

```
02_System_reference/02.06_Command_Reference/02.06.02.02.63_DFPN__DFPN__-__DeFine_Pin_Name.htm
```

编号推导规则与验证见 `schema-pipeline.md` §2。

## 铁律

- **只读。** 语料层 `tdc-html/raw/` 一个字节都不许改。
- **本臂没有例外。** raw 就是 TDC 原件，中间没有转换层——
  不存在「转换损坏」，也就没有需要破例去修的东西。
- **上游本身写错的，照旧一个字都不许动。**
  那不是我们造成的，也不许替它改；在页面里照实记录（见 `schema-pipeline.md` §8）。
- **引用时用 `rel`（分类路径）**，写进页面的 `sources:`。
- wiki 里每一句断言都要能追回这里的某个文件。追不回去的，就是编的。

## 已知的上游瑕疵

| 编号 | 瑕疵 | 规模 |
|---|---|---:|
| ② | `Introduced before SmarTest 6.3.2` 是哨兵值 | 2,677 行 |
| ④ | 同一版本号跨产品线撞车 | 15 个版本号 |
| ⑤ | 整词替换：`dqIndex` → `DC/DC power units` | 128 篇 |
| ⑥ | 上游表格写错（如 `Timing file` 格配 `.pin`） | 已知 1 处 |

**编码损坏（①）和脚注吞并（③）是 md 转换造成的，在本臂不存在。**

## 怎么读

```bash
cd F:\master-dev\html-wiki\extract
python extract_html.py            # 重建五张表
python show.py 02.06.05           # 按分类号看原文（待实现）
```
