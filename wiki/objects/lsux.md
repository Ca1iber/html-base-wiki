---
type: object
title: LSUX, LSUX? - (Level Sets Used eXtended)
layer: L1
stage: level
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.156_LSUX__LSUX__-__Level_Sets_Used_eXtended.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# LSUX, LSUX? - (Level Sets Used eXtended)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **609 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.156_LSUX__LSUX__-__Level_Sets_Used_eXtended.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### LSUX

```
LSUX {level_set_no|SWAP|NONE}
```

### LSUX?

```
LSUX?
```

returns:

```
LSUX {level_set_no}
```

### Parameters

[表]
行 1:
  level_set_no [跨 3 行]
  Level Set Number. If the number is smaller [跨 2 列]
    than the current value of LSUS then LSUX is set to
    this value. Otherwise it is set to the current value of LSUS.
行 2:
  SWAP
  This command parameter causes the values set by LSUS and LSUX to be switched, that is, LSUS is
    set to the current value of LSUX, and LSUX to that of
    LSUS.
行 3:
  NONE
  This command parameter sets the value of LSUX back to
    1.

### Example

```
LSUX 4
```

This example defines a maximum of 4 level sets.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.156_LSUX__LSUX__-__Level_Sets_Used_eXtended.htm>` 的 `## Errors` 段。**不是转述。**
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

The
level_set_no
 is greater than the range allowed by the
`DSCP`（raw: `98578.htm`）
 command.

The
level_set_no
 is smaller than one.

The
level_set_no
 is undefined.

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
