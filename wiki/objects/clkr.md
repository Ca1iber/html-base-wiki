---
type: object
title: CLKR, CLKR? - (CLocK Resolution)
layer: L1
stage: timing
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.24_CLKR__CLKR__-__CLocK_Resolution.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# CLKR, CLKR? - (CLocK Resolution)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,973 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.24_CLKR__CLKR__-__CLocK_Resolution.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### CLKR

```
CLKR {waveform_set|specset_id|"multi-port_spec"}, [ref_period],{period_res}
```

### CLKR?

```
CLKR?[type,] {waveform_set|specset_id|"multi-port_spec"}
```

returns:

```
CLKR {waveform_set|specset_id|"multi-port_spec"}, [ref_period],{period_res|clock_res}
```

### Parameters

[表]
行 1:
  waveform_set
  Waveform Set Number. Enter an integer in the range 1 to the maximum number of
    allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `98878.htm`）. For the
    query command you can also enter ALL for all waveform sets.
行 2:
  specset_id
  Derived as follows:
    
    100 * equation_set_no +
    specset_no
行 3:
  multi-port_spec
  To set or query the resolution of a multi-port timing specification, specify the
    name of the specification.
行 4:
  ref_period
  Not used. (Ignored)
行 5:
  period_res
  The period resolution (in ns) for the specified specification or waveform set.
    
    If necessary, period_res is rounded to nine digits after the decimal
    point. The allowable maximum period resolution is the maximum tester period value. The
    minimum period resolution is determined by the hardware (see `Automatic calculation of period resolution for single-port setups`（raw: `98092.htm`）).
行 6:
  type
  In the query, the type parameter specifies which resolution is queried. The
    allowed values are:
    
    VIRTUAL: The period resolution (period_res) is
    queried. This is the default.
    
    EXACT: The clock resolution (clock_res) is
    queried.
行 7:
  clock_res
  In the answer to the query, the clock resolution is returned if type is set to
    EXACT in the query.

### Example

```
> CLKR 1,,10
> CLKR? 1
< CLKR 1,1000,10
```

This example sets and queries the period resolution (10 ns) for waveform set 1. Ignore
the returned value of the
ref_period
 parameter.

```
> CLKR? "spec_port_1_port_2"
< CLKR "spec_port_1_port_2",50,5.555555556
```

This
example queries the period resolution for the multi-port specification

spec_port_1_port_2
.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.24_CLKR__CLKR__-__CLocK_Resolution.htm>` 的 `## Errors` 段。**不是转述。**
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

waveform_set
 is less than 1.

waveform_set
 is greater than the range allowed by the
`WSUS`（raw: `98878.htm`）
 command.

period_res
 is outside the allowed range.

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
