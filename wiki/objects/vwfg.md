---
type: object
title: VWFG? - (Verify WaveForms in Groups)
layer: L1
stage: timing
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.330_VWFG__-__Verify_WaveForms_in_Groups.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# VWFG? - (Verify WaveForms in Groups)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,744 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.330_VWFG__-__Verify_WaveForms_in_Groups.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

There are three different ways to call

VWFG?
:

```
VWFG? {waveform_set}, ["dev_cyc_name"], {(pinlist)}
VWFG? {specset_id},["dev_cyc_name"],{(pinlist)}
VWFG? {wavetable_name}, ["dev_cyc_name"], {(pinlist)}
```

All
three forms
return:

```
VWFG {status}
```

### Parameters

[表]
行 1:
  waveform_set
  Waveform Set Number. Enter PRM for the Primary Waveform Set, or
    an integer in the range 1 to the maximum number of allowed waveform sets. The maximum
    number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `98878.htm`）.
行 2:
  specset_id
  Derived as follows:
    
    100 * equation_set_no + specset_no
行 3:
  wavetable_name
  The wavetable name. Enter a string of up to 40 alphanumeric characters (upper or
    lower case) enclosed in double quotes.
行 4:
  dev_cyc_name
  If you specify the name of a device cycle, only this device cycle will be checked.
    Enter ALL for all device cycle names in the device cycle table.
行 5:
  pinlist
  The name of the pin or pins whose definitions you want to check. This parameter can
    also include groups previously created by `DFGP, DFGP? - (DeFine GrouP)`（raw: `98546.htm`）. If more than one pin is
    to be included, the names must be separated with a comma. The symbol @ can be used
    to check all configured pins.
行 6:
  status
  The system returns:
    
    0: The definitions are not the same.
    
    1: The definitions are the same.

### Example

```
> VWFG? "spec_search_wtb","SBC",(ser_in)
< VWFG 1
> VWFG? "spec_search_wtb",,(ser_in)
< VWFG 0
```

According
to this example, the waveform and device cycle definition for device cycle SBC are the same for
the pins in the group ser_in within the wavetable spec_search_wtb, but this does not hold for
all device cycles that are defined for the pins of this group.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.330_VWFG__-__Verify_WaveForms_in_Groups.htm>` 的 `## Errors` 段。**不是转述。**
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

waveform_set
 is greater than the range allowed by the
`WSUS`（raw: `98878.htm`）
 command.

specset_id
 is invalid because
equation_set_no
,

specset_no
 or both are invalid.

specset_id
 does not reference a defined wavetable.

wavetable_name
 does not reference a defined wavetable.

multi-port spec
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
