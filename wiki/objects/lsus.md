---
type: object
title: LSUS, LSUS? - (Level Sets USed)
layer: L1
stage: level
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.155_LSUS__LSUS__-__Level_Sets_USed.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# LSUS, LSUS? - (Level Sets USed)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **904 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.155_LSUS__LSUS__-__Level_Sets_USed.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### LSUS

```
LSUS {level_set_no}
```

### LSUS?

```
LSUS? [level_set_no]
```

returns:

```
LSUS {level_set_no}
```

or:

```
LSUS? [equation_set_no]
```

returns:

```
LSUS {level_set_no}
```

### Parameters

[表]
行 1:
  level_set_no
  Level Set Number. This is the highest number currently allocated to a level set or
    the highest number of set you want to load. The number you type must not exceed the maximum
    number of level sets allowed (defined by the `DSCP`（raw: `98578.htm`） command).
    
    This number is automatically updated to include any new level set as it is created. At
    power-on only one level set (containing the default values) is available.
行 2:
  equation_set_no
  The level equation set number for which the number of currently defined level sets
    is to be determined. Enter an integer in the range 1 to 99. Valid for Equation based
    testing only.

### Example

```
LSUS 4
```

This example defines a maximum of 4 level
sets.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.155_LSUS__LSUS__-__Level_Sets_USed.htm>` 的 `## Errors` 段。**不是转述。**
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
equation_set_no
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
