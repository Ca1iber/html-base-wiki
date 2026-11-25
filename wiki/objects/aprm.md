---
type: object
title: APRM - (Activate PRiMary sets)
layer: L1
stage: level
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.01_APRM_-__Activate_PRiMary_sets.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# APRM - (Activate PRiMary sets)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **318 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.05.02.01_APRM_-__Activate_PRiMary_sets.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
APRM {mode}
```

### Parameters

[表]
行 1:
  mode [跨 3 行]
  Selects the activation [跨 2 列]
    mode:
行 2:
  FRC
  Forced activation. Primary sets are always
    activated.
行 3:
  CNL
  Conditional activation, depends on previous activation
    performed by APRM or by any of the commands in
    the second list above.

### Example

```
APRM CNL
```

<!-- 语法节 end -->

## 是什么

**文档事实** APRM（Activate PRiMary sets）在硬件中激活 primary sets；这些 primary sets 已由 SPRM（Set PRiMary sets）告知 firmware。

**文档事实** `mode` 有两种：`FRC` 为强制激活，primary sets 总是被激活；`CNL` 为条件激活，取决于此前由 APRM 或上述命令执行的激活。

**文档事实** Application 为 AC tests 与 DC Measurement Commands。

**推断** 因此 APRM 是把 SPRM 选定的 primary sets 真正推向硬件的激活步骤：需要强制应用新 primary set 用 FRC，需要沿用前次激活结果用 CNL。

## 典型用法

**文档事实** 示例只给出 `APRM CNL`。

**文档事实** `FRC`：强制激活，primary sets 总是被激活；`CNL`：条件激活，依赖前次 APRM 或同类命令的激活结果。

**文档事实** FTST?、RCLS?、SQST RUN、PSST 不需要事先执行 APRM，因为它们自身就执行这一功能。

**文档事实** FwEscape 页提醒：使用该 test method 时，本 test suite 指定的 primary sets 不被使用，而使用前一个已执行 test suite 的 primary sets；要让本 suite 用其指定的 primary sets，应在 FW execution command 开头插入 `APRM CNL`。

**文档事实** primary sets 由 SPRM 定义和修改，包含 timing equation set 与 spec set、multiport specification、waveform set、timing set（多端口时为 timing set list）、level equation set/spec set/level set 等（SPRM 页）。

**建议** AC 测试或 DC 测量前，若不确定前序命令是否已激活所需 primary sets，显式执行 `APRM CNL`（或需强制时 `APRM FRC`）。

## 和谁有关

- **文档事实** SPRM, SPRM?：APRM 激活的 primary sets 由 SPRM 定义/修改并告知 firmware；SPRM 页列出 primary sets 的组成。
- **文档事实** FTST?、RCLS?、SQST RUN、PSST：主源明确这四个命令不需要事先 APRM，因为它们自身执行该激活功能。
- **文档事实** FwEscape：该 test method 使用前一 test suite 的 primary sets；要在本 suite 使用指定的 primary sets，需在 FW execution command 开头加 `APRM CNL`（入边与正文）。
- **文档事实** List of level setup commands：APRM 列在 level setup commands 下；主源 Application 指向 AC tests 与 DC Measurement Commands。
- **文档事实** List of commands：APRM 列在命令参考总表，并出现在 “Site dependent firmware commands” 列表中（入边）。
- **文档事实** DC Measurement Commands：主源 Application 将其列为 APRM 的应用范围。

## 版本

**文档事实** Functional changes 记：Introduced before SmarTest 6.3.2。

## 出处

- `02_System_reference/02.06_Command_Reference/02.06.05.02.01_APRM_-__Activate_PRiMary_sets.htm`，主源，含概览、Mode of operation、Syntax、Parameters、Application、Example 与 Functional changes，已用 `show.py` 读取。
- `02_System_reference/02.06_Command_Reference/02.06.02.02.228_SPRM__SPRM__-__Set_PRiMary_sets.htm`，用于 primary sets 的组成，已用 `show.py` 读取。
- `02_System_reference/02.07_Test_Method_Reference/02.07.05.04.04_FwEscape.htm`，用于 `APRM CNL` 的典型用法，已用 `show.py` 读取。
- 命令族与入边语境取自 `extract/objpack.py` / `edges.jsonl`。
