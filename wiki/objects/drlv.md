---
type: object
title: DRLV, DRLV? - (DRive LeVel)
layer: L1
stage: level
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.89_DRLV__DRLV__-__DRive_LeVel.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# DRLV, DRLV? - (DRive LeVel)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **2,786 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.89_DRLV__DRLV__-__DRive_LeVel.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### DRLV

```
DRLV {level_set_no | level_set_id}, [logic_0_level], [logic_1_level], [v3h_level | range,] {(pinlist)}
```

### DRLV?

```
DRLV? {level_set_no | level_set_id}, {(pinlist)}
```

returns:

```
DRLV {level_set | level_set_id}, [logic_0_level], [logic_1_level], [v3h_level | range,] {(pinlist)}
```

### Parameters

[表]
行 1:
  level_set_no
  The identification number of the level set (fixed levels) in which you want the
    levels to be included. The number must not exceed the maximum number of level sets allowed
    (as defined by the `DSCP`（raw: `98578.htm`） command). Typing ALL in this field sets the levels for all existing level sets. Typing PRM sets the drive voltage levels for the primary level set.
行 2:
  level_set_id
  Used in equation based level setup. It is derived as follows:
    
    100000 * equation_set_no + 1000 * specset_no +
    level_set_no
    
    Note that if you use the command for an equation based level setup, you modify only the
    runtime values, not the value in the level set.
行 3:
  logic_0_level
  An integer (in mV) which sets the low level voltage for the drive amplifier.
行 4:
  logic_1_level
  An integer (in mV) which sets the high level voltage for the drive amplifier.
行 5:
  v3h_level
  Input (drive) 3rd level definition (high level voltage shift). The expression of
    this extra parameter must define a value in millivolts (mV).
    
    This parameter is no longer used.
行 6:
  range
  This extra parameter selects the drive range in mV:
    
     
    
    -8000.0 ... 8000.0 selects the 8 V range
    
    -30000.0 ... 30000.0 selects the 30 V range
    
    all other values select the -40 V ... +80 V range
    
     
    
    If not specified the best fit range will be selected based on
    logic_0_level and logic_1_level.
    
    This parameter is currently not available.
    
    The query returns the parameter only if it is defined for the queried level set.
行 7:
  pinlist
  The name of the pin or pins whose levels you want to set. This parameter can also
    include groups previously created by the `DFGP`（raw: `98546.htm`） (DeFine GrouP)
    command. If more than one pin is to be included, the names must be separated with a comma.
    The symbol @ sets or reads the drive levels of all input pins in the level set. You
    can include I and IO pin types in pinlist.

For card specifications, like level ranges, see
`Digital Cards`（raw: `132413.htm`）
, for
example:

`Pin Scale 1600`（raw: `126230.htm`）

`Pins Scale 5000`（raw: `351223.htm`）

### Examples

### Example 1
```
DRLV 1,-1750,-850,(Q0,Q1,Q2,Q3)
```

This
example sets the driver levels for level set 1 for pins Q0, Q1, Q2 and Q3. The logic 0 level is
set to -1750 mV and the logic 1 level to -850 mV.

### Example 2
```
DRLV 1,-1750,-850,8000,(avi64Pin1)
```

This
example shows how the 8 V drive range of an AVI64 pin is selected.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.89_DRLV__DRLV__-__DRive_LeVel.htm>` 的 `## Errors`、`## Warnings` 段。**不是转述。**
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

The high or low level is out of range;

The swing limitations are exceeded;

The set number is out of range;

The set number is out of the range defined by the
DSCP
command;

The set number is out of the used range of sets (
DRLV?
 only).

The parameter "
range
" exceeds the hardware defined maximum range.

### Warnings

A warning is generated if:

Auto-correction of logic level 1 or 0 occurs.

The logic 1 or 0 level for a pin lies outside the specification.

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
