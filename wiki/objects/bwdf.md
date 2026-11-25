---
type: object
title: BWDF, BWDF? - (Break Waveform DeFinition)
layer: L1
stage: timing
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.13_BWDF__BWDF__-__Break_Waveform_DeFinition.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# BWDF, BWDF? - (Break Waveform DeFinition)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,822 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.13_BWDF__BWDF__-__Break_Waveform_DeFinition.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### BWDF

```
BWDF {wvf_set}, {a1}, {a2}, {a3}, {a4}, {a5}, {a6}, {(pinlist)}
```

### BWDF?

```
BWDF? {wvf_set|"wavetable_name"|specset_id|"multiport_spec"}, {(pinlist)}
```

returns:

```
BWDF {wvf_set|"wavetable_name"|specset_id|"multiport_spec"}, {a1}, {a2}, {a3}, {a4}, {a5}, {a6}, {(pinlist)}
```

### Parameters

[表]
行 1:
  wvf_set
  Waveform Set Number. Enter [跨 2 列]
    ALL for all waveform sets, or an integer in the range 1 to the maximum
    number of allowed waveform sets. The maximum number is determined by the command `WSUS, WSUS? - (Waveform Sets USed)`（raw: `98878.htm`）.
行 2:
  specset_id
  Derived as follows: [跨 2 列]
    
    100 * equation_set_no +
    specset_no
行 3:
  wavetable_name
  The wavetable name. Enter a string of up to [跨 2 列]
    40 alphanumeric characters (upper or lower case) enclosed in double quotes.
行 4:
  multiport_spec
  To query a multi-port specification, enter [跨 2 列]
    the name of the specification.
行 5:
  a1..a6 [跨 10 行]
  Edge action. The actions you can define [跨 2 列]
    are:
行 6:
  N
  no action
行 7:
  F0N
  drive 0, no tri-state action
行 8:
  F1N
  drive 1, no tri-state action
行 9:
  FN0
  no drive action, tri-state off
行 10:
  FNZ
  no drive action, tri-state on
行 11:
  F00
  drive 0, tri-state off
行 12:
  F0Z
  drive 0, tri-state on
行 13:
  F10
  drive 1, tri-state off
行 14:
  F1Z
  drive 1, tri-state on
行 15:
  pinlist
  The name of the pin or pins for which break [跨 2 列]
    waveform definitions are to be made or read back. The symbol @ can be used to
    specify all configured input and IO pins. If more than one pin is to be included, the names
    must be separated with a comma.

### Example

```
BWDF 1,N,N,N,F1N,F0N,N,(D0,D1,D2,D3)
```

This example defines a
pulse for waveform set 1, and for pins D0 to D3, driving to 1 at edge action 4 and to 0 at edge
action 5. The tri-state formatter is not used.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.13_BWDF__BWDF__-__Break_Waveform_DeFinition.htm>` 的 `## Errors` 段。**不是转述。**
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

waveform_set
 is greater than the range allowed by the command
`WSUS, WSUS? - (Waveform Sets USed)`（raw: `98878.htm`）
.

There is a mismatch between the edge actions and edge order in the specified waveform.

A tri-state action is defined or implicitly required on edge 2 or 5.

specset_id
 is invalid because
equation_set_no
,

specset_no
, or both are invalid, or because
specset_id
 does not reference a defined wavetable.

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
