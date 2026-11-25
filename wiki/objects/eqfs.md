---
type: object
title: EQFS - (EQuation FileS command transfer)
layer: L1
stage: timing
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.09_EQFS_-__EQuation_FileS_command_transfer.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# EQFS - (EQuation FileS command transfer)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **964 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.05.02.09_EQFS_-__EQuation_FileS_command_transfer.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
EQFS {spec_type}, {part}, {operation},{"eqn_filename"}, ["error_filename"]
```

### Parameters

[表]
行 1:
  spec_type [跨 3 行]
  Which specification to use: [跨 2 列]
行 2:
  LEV
  to specify levels, or
行 3:
  TIM
  to specify timing.
行 4:
  part [跨 5 行]
  Which part of the specification type to [跨 2 列]
    use:
行 5:
  WVT
  to specify wavetable (only for spec_type =
    TIM),
行 6:
  EQN
  to specify equations, or
行 7:
  SPS
  to specify specs.
行 8:
  operation
  Use LOAD or [跨 2 列]
    SAVE.
行 9:
  eqn_filename
  The absolute filename of the temporary [跨 2 列]
    equation based timing file.
行 10:
  error_filename
  The absolute filename of the file to which [跨 2 列]
    error reports are written.
    
    Use UI_REPORT to direct error reports to the report window.
    
    If this parameter is not specified, only a summarized error message is reported.

### Example

```
EQFS LEV,EQN,LOAD,"/tmp/level_equation",
```

This example loads the
level equation file from
/tmp/level_equation
.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.05.02.09_EQFS_-__EQuation_FileS_command_transfer.htm>` 的 `## Errors` 段。**不是转述。**
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

eqn_filename
does not exist.

error_filename
does not exist.

<!-- 报错节 end -->

## 是什么

**文档事实** EQFS 提供编辑器工具所需的 load/save 操作，用于把 equation based testing 文件从临时文件载入，或保存到临时文件。

**文档事实** spec_type 决定规范类型：LEV 表示 levels，TIM 表示 timing。part 决定该类型中的哪一部分：WVT 表示 wavetable（仅当 spec_type=TIM），EQN 表示 equations，SPS 表示 specs。

**文档事实** operation 取 LOAD 或 SAVE；`eqn_filename` 为临时 equation based timing 文件的绝对文件名；`error_filename` 为写入错误报告的文件的绝对文件名。

**文档事实** `error_filename` 可写 UI_REPORT，把错误报告送到 report window；若省略该参数，则只报告一条汇总的错误消息。

**文档事实** Application 记：Editor tools、The Spec tool。

**文档事实** 报错条件仅两条：`eqn_filename` 不存在，或 `error_filename` 不存在。

## 典型用法

**文档事实** 文档示例 `EQFS LEV,EQN,LOAD,"/tmp/level_equation",` 从 `/tmp/level_equation` 载入 level equation 文件；最后一个参数为空，因此不写单独的错误报告文件。

**文档事实** `eqn_filename` 被定义为临时 equation based timing 文件的绝对文件名；operation 取 LOAD 或 SAVE。

**推断** 按参数含义，LOAD 应从 `eqn_filename` 读入、SAVE 应写出到 `eqn_filename`；主源只给出两个 operation 取值与文件名定义，未逐句说明方向。

**文档事实** 需要详细错误报告时，把 `error_filename` 填为绝对路径；希望直接看报告时写 `UI_REPORT`，让错误进入 report window。

**文档事实** part 的取值为 WVT（参数表注明仅当 spec_type=TIM）、EQN、SPS；spec_type 可取 LEV 或 TIM。文档没有给出 LEV 与 TIM 各自可用 part 的完整对照表，只明确 WVT 限 TIM。

**建议** 交互调试时用 `UI_REPORT` 便于立即看到报告；在工具/批处理中改用明确的 `error_filename`，并确保目录与文件路径已存在，否则会触发本命令的两条报错条件。

## 和谁有关

- **文档事实** `[[eqsp]]` — Data organization of equation based timing 页称 equation based 的数据集合由 EQFS 与 EQSP 下载；Fixed timing 页称这类集合作为 EQSP 或 EQFS 的一个字符串参数传给 tester。两者同属 equation based 数据通道：EQFS 做临时文件 LOAD/SAVE，EQSP 做面向 firmware 的二进制集合传输（后者见 EQSP 主源）。
- **文档事实** `[[level-equation-file]]` — 该页示例用 `EQSP LEV,EQN,#9000005436`，而 EQFS 主源示例 `EQFS LEV,EQN,LOAD,"/tmp/level_equation"` 正是载入同类 level equation 文件，二者在 level 侧配套。
- **文档事实** `[[spec-tool]]` — EQFS 主源 Application 明确列出 Editor tools 与 The Spec tool，说明本命令服务于这些工具的文件读写。
- **文档事实** `[[timing-specification]]` — Defining the timing specification 页称 specification 通常由 spec tool 定义；若要用 EQFS 或 EQSP 下载，必须按 timing setup file 中的编码书写，说明 EQFS 的输入文件需与 timing setup 文件编码一致。
- **文档事实** `02_System_reference/02.06_Command_Reference/02.06.05.02_List_of_level_setup_commands.htm` — 该命令总表把 EQFS 列入 level setup commands（objpack 入边）。

## 版本

**文档事实** Functional changes 记：`Introduced before SmarTest 6.3.2`。

## 出处

- `02_System_reference/02.06_Command_Reference/02.06.05.02.09_EQFS_-__EQuation_FileS_command_transfer.htm`，主源，含首段、语法/参数、Application、Errors、Example 与 Functional changes，已用 `show.py` 与 `objpack.py` 读取。
- `02_System_reference/02.06_Command_Reference/02.06.06.01.02_Data_organization_of_equation_based_timing.htm`、`02.06.06.01.05_Defining_the_timing_specification.htm`、`02.07_Test_Method_Reference/02.07.11.01.05.01_Level_equation_file.htm`，用于核对 EQFS/EQSP 分工、spec tool 与编码关系、level 侧示例，已用 `show.py` 读取。
- `02.06.06.01.07_Fixed_timing.htm`（“EQSP 或 EQFS”表述）取自 `extract/sections.jsonl` 摘录，命令清单入边取自 `extract/objpack.py` 的 `edges.jsonl`。
