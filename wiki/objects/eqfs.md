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

（待补）

## 典型用法

（待补）

## 和谁有关

（待补）

## 版本

（待补）

## 出处

（待补）
