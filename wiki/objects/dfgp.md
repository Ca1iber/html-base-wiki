---
type: object
title: DFGP, DFGP? - (DeFine GrouP)
layer: L1
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# DFGP, DFGP? - (DeFine GrouP)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,104 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### DFGP

```
DFGP {pin_type}, {(pinlist)}, {(pin_group)}
```

### DFGP?

```
DFGP? {(pin_group)}
```

returns:

```
DFGP {pin_type}, {(pinlist)}, {(pin_group)}
```

### Parameters

[表]
行 1:
  pin_type [跨 5 行]
  Defines the type of pins in the [跨 2 列]
    group. This can be:
行 2:
  I
  Identifies a group of device input pins.
行 3:
  O
  Identifies a group of device output pins.
行 4:
  DC
  Identifies a group of DC type pins.
行 5:
  X
  Identifies a group that may contain pins of any type.
行 6:
  pinlist
  The names of the pins to be [跨 2 列]
    included in the group. All pin names must be separated with a comma.
行 7:
  pin_group
  The name assigned to the pin [跨 2 列]
    group. You can use the same name for groups of different type.
    
    The symbol @ can be used with the DFGP? query to
    list all groups previously defined using the DFGP command. If you query
    a non-existent group, the system returns nothing.
    
    Maximum number of characters is 16 for 32-bit SmarTest and 64 for 64-bit SmarTest.

### Example

```
DFGP O,(Q0,Q1,Q2,Q3),(outputs)
```

This example defines a group
called
outputs
 which contains pins Q0, Q1, Q2 and Q3.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.htm>` 的 `## Errors`、`## Warnings` 段。**不是转述。**
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

 More than 2400 groups are defined.

 The intended group name is already being used for a pin.

 The intended group name is already being used for a DPS pin.

 There are too many pins in the group (max. number of pins in
all
 groups is 1843200).

### Warnings

A warning is generated if:

 A pin cannot be part of the specified group and is therefore ignored.

 A group cannot be part of the specified group and is therefore ignored.

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
