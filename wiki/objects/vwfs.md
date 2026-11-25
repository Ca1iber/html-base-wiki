---
type: object
title: VWFS? - (Verify WaveForm Sets)
layer: L1
stage: timing
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.331_VWFS__-__Verify_WaveForm_Sets.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# VWFS? - (Verify WaveForm Sets)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,038 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.331_VWFS__-__Verify_WaveForm_Sets.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
VWFS? {waveform_set_1},{waveform_set_2},{(pinlist)}
```

returns:

```
VWFS {status}, {(pinlist)}
```

### Parameters

[表]
行 1:
  waveform_set_x
  Waveform set number. Enter an integer in [跨 2 列]
    the range 1 to the maximum number of allowed waveform sets. The maximum number is
    determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `98878.htm`）.
行 2:
  pinlist
  The name of the pin or pins for which you [跨 2 列]
    wish to check waveform set compatibility. This parameter can also include groups previously
    created by `DFGP, DFGP? - (DeFine GrouP)`（raw: `98546.htm`）. If more than one pin is to be included, the names must
    be separated with a comma. The symbol @ can be used to check all configured pins.
行 3:
  status
  The system returns: [跨 2 列]
行 4:
  
  0
  The waveform sets are not compatible.
行 5:
  
  1
  The waveform sets are compatible.

### Example

```
VWFS? 1,2,(DATA)
```

This example checks whether waveform sets 1 and
2 are the same for the pins in the group DATA. If they are the same the following string is
returned:

```
VWFS 1,(DATA)
```

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.331_VWFS__-__Verify_WaveForm_Sets.htm>` 的 `## Errors` 段。**不是转述。**
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if
waveform_set
 is
greater than the range allowed by the
`WSUS`（raw: `98878.htm`）
 command.

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
