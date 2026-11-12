# Purpose — 93K 测试开发 LLM Wiki

## 要解决的问题

让 agent 能**独立完成 Advantest V93000 / SmarTest 测试开发**，而不是只会查文档回答问题。

目标形态：agent 拿到一个器件，能自己走完

```
建工程 → Pin → Level → Timing → Pattern → Test Method → Testflow → 运行 → 结果
```

横跨三层接口：

| 层 | 内容 |
|---|---|
| **L1** | Firmware / setup command（配置文件里的命令） |
| **L2** | Test Method API（C++ 测试方法） |
| **L3** | 外部控制（SmartShell / Test suite control API / HVM） |

## 范围

**在范围内**

- 一个 LLM wiki：raw 层（已有）+ wiki 层（要建）+ schema 层（已定）
- 全栈知识覆盖：L1 + L2 + L3，九段流程

**当前不在范围内（后话）**

- MCP / 工具层（让 agent 真的发命令、改文件、调 API）
- 执行反馈闭环（跑完看结果、失败回查）

**wiki 只告诉 agent「该怎么做」。「做得到」是工具层的事，不要混为一谈。**

## 语料

- **来源**：SmarTest 7.10.3 TDC 文档
- **位置**：`F:\master-dev\dorm-wsl-sytest\tdc-html\raw`
- **规模**：9,393 篇（9,321 `.htm` + 72 `.html`）/ 约 60 MB
- **结构**：raw 层是**扁平的**——`raw/<topicid>.htm`，没有子目录。
  分类树不来自目录，来自上游的 `raw/toc.xml`（Eclipse help TOC，最深 12 层）；
  按深度优先给节点编号即得分类号——**9,145 篇与 md 臂逐条相同，零差异**。

```
00_Overview                                     1
01_Getting_started                            255
02_System_reference                         8,316   ← 89%
03_Use_cases_and_application_papers           573
99_Unlisted_or_Unreferenced                   248
```

**铁律：raw 层不可变。** 缺什么错什么，都在 wiki 层标注，不许回头改证据。

**这一版没有例外。** raw 就是 TDC 的**原件**，中间没有转换层——
不存在「转换损坏」，也就没有需要破例去修的东西。
md 臂那条 A 类例外（2026-09-22 立）是为修补转换损失立的，**在这里是空的**。

**上游本身就写错的，照旧一个字都不许动。** 那不是我们造成的，也不许替它改。
