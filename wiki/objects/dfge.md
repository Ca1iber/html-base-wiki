---
type: object
title: DFGE, DFGE? - (DeFine Group by Expressions)
layer: L1
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.59_DFGE__DFGE__-__DeFine_Group_by_Expressions.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# DFGE, DFGE? - (DeFine Group by Expressions)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **2,208 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.59_DFGE__DFGE__-__DeFine_Group_by_Expressions.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### DFGE

```
DFGE {group_type}, {"group_expression"}, {(pin_group)}
```

### DFGE?

```
DFGE? {(pin_group)}
```

returns:

```
DFGE {group_type}, {("group_expression")}, {(pin_group)}
```

for
expression-based groups,
and

```
DFGP {pin_type}, {(pinlist)}, {(pin_group)}
```

for
digital fixed groups.

### Parameters

[表]
行 1:
  group_type [跨 5 行]
  Defines the type of pins in the group. This [跨 3 列]
    can be:
行 2:
  I [跨 2 列]
  Identifies a group of device input pins.
行 3:
  O [跨 2 列]
  Identifies a group of device output pins.
行 4:
  IO [跨 2 列]
  Identifies a group of bidirectional pins.
行 5:
  DC [跨 2 列]
  Identifies a group of DC type pins.
行 6:
  group_expression
  The expression that describes the pins to [跨 3 列]
    be included in the group. The expression must be built up from pin or pin group names which
    serve as arguments for the following operators:
行 7:
  
  +
  returns the union of its arguments, that [跨 2 列]
    is, all pins that are contained in one of its arguments.
行 8:
  
  *
  returns the intersection of its arguments, [跨 2 列]
    that is, all pins that are contained in both of its arguments.
行 9:
  
  -
  returns the difference of its arguments, that is, all [跨 2 列]
    pins that are contained in the first argument, but not in the second.
行 10:
  
  You can also use parentheses to force a [跨 3 列]
    certain processing order.
行 11:
  pin_group
  The name assigned to the pin group. You can [跨 3 列]
    use the same name for groups of different type.
    
    The symbol @ can be used with the DFGE? query to
    list all groups previously defined using the DFGP and
    DFGE command. If you query a non-existent group, the system returns
    nothing.

### Example

```
> DFGP? (SCAN)
< DFGP X,(SI1,SI2,SO1,SO2),(SCAN)
> DFGP? (OUT)
< DFGP O,(O1,SO1,SO2),(OUT)
> DFGE O,"SCAN * OUT",(SCAN_OUT)
> DFGE? (SCAN_OUT)
< DFGE O,"SCAN * OUT",(SCAN_OUT)
> DFGP? (SCAN_OUT)
< DFGP O,(SO1,SO2),(SCAN_OUT)
```

This
example defines a group called SCAN_OUT which contains the pins that occur both in pin groups
OUT and SCAN. Note that you must use the
DFGP?
 query to display the pins of
SCAN_OUT.
DFGE?
 returns the group definition.

The same result would be
obtained with the
definition

```
> DFGE O,"OUT - O1",(SCAN_OUT)
```

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.59_DFGE__DFGE__-__DeFine_Group_by_Expressions.htm>` 的 `## Errors`、`## Warnings` 段。**不是转述。**
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

 More than 2400 groups are defined.

 Another group_type than
I
,
O
,
IO,

or
DC
 is used.

 There are too many pins in the group (max. number of pins in
all
 groups is
1843200).

 The group definition is recursive.

 The group expression is empty.

 The group expression contains errors.

 The intended group name is already being used for a pin.

 The group name is already used by a digital pin, an analog group or non-group analog
pin.

### Warnings

A warning is generated if:

The group name is already used by a digital core group or expression-based group (in which
case the old definition will be overwritten).

The group expression contains undefined pins or groups.

The evaluation of the group expression results in an empty group.

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
