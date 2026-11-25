---
type: object
title: VCLK? - (Verify CLocK)
layer: L1
stage: timing
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.319_VCLK__-__Verify_CLocK.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# VCLK? - (Verify CLocK)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **2,026 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.319_VCLK__-__Verify_CLocK.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
VCLK? {waveform_set}, {timing_set}, {period}, {(pinlist)}
```

returns:

```
VCLK {autocorrect}
```

### Equation-based testing

```
VCLK? {specset_id|"multi-port_spec"}, {timing_set}, {period},{(pinlist)}
```

returns:

```
VCLK {autocorrect}
```

### Parameters

[表]
行 1:
  waveform_set
  Waveform set number. Enter PRM for the primary waveform set, or an integer in the range 1 to the maximum number [跨 2 列]
    of allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `98878.htm`）.
行 2:
  specset_id
  Derived as follows: [跨 2 列]
    
    100 * equation_set_no + specset_no
行 3:
  multi-port_spec
  To enter a multi-port specification is only [跨 2 列]
    possible if the specification is associated with the default port and if no other ports are
    configured.
行 4:
  timing_set
  Timing set number. Enter PRM for the primary timing set, ALL for all timing sets, or an [跨 2 列]
    integer in the range 1 to the maximum number of allowed timing sets. The maximum number is
    determined by `TSUS, TSUS? - (Timing Sets USed)`（raw: `98817.htm`）.
行 5:
  period
  Enter the test system period in ns for [跨 2 列]
    which you wish to check whether auto-correction will take place or not.
    period must be within the maximum and minimum test system periods of the
    model.
行 6:
  pinlist
  The name of the pin or pins whose period [跨 2 列]
    you want to check. This parameter can also include groups previously created by `DFGP, DFGP? - (DeFine GrouP)`（raw: `98546.htm`）. If more than one pin is to be included, the names must be separated with
    a comma. The @ symbol can be used to check all configured pins.
行 7:
  autocorrect [跨 3 行]
  The auto-correction flag returned by the [跨 2 列]
    system. It can be:
行 8:
  0
  No auto-correction will occur.
行 9:
  1
  Auto-correction will occur.

### Example

```
VCLK? 1,1,20,(@)
```

This example checks if a period of 20 ns will
cause auto-correction to the edge placements in Timing Set 1 of Waveform Set 1 on any pin. If no
auto-correction will occur the following string is returned:

```
VCLK 0
```

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.319_VCLK__-__Verify_CLocK.htm>` 的 `## Errors` 段。**不是转述。**
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

The period is outside the given range.

waveform_set
 is outside the valid range.

timing_set
 is outside the valid range.

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
