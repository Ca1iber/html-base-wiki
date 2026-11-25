---
type: object
title: TSUX, TSUX? - (Timing Sets Used eXtended)
layer: L1
stage: timing
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.284_TSUX__TSUX__-__Timing_Sets_Used_eXtended.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# TSUX, TSUX? - (Timing Sets Used eXtended)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **834 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.284_TSUX__TSUX__-__Timing_Sets_Used_eXtended.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### TSUX

```
TSUX {waveform_set},{timing_set}
```

### TSUX?

```
TSUX? {waveform_set}
```

returns:

```
TSUX {waveform_set},{timing_set}
```

### Parameters

[表]
行 1:
  waveform_set
  Waveform set number. Enter [跨 2 列]
    ALL for all waveform sets in the query command.
行 2:
  timing_set [跨 3 行]
  Timing set number. In the command, [跨 2 列]
    TSUX is set to this value for the specified waveform set, if the number
    is smaller than the current value of `TSUS`（raw: `98817.htm`） for this set.
    Otherwise, it is set to the current value of TSUS.
行 3:
  SWAP
  This command parameter causes the values set by `TSUS`（raw: `98817.htm`）and TSUX to be switched, that is, TSUS is set to the current value of TSUX , and
    TSUX to that of TSUS for the specified waveform
    set.
行 4:
  NONE
  This command parameter sets the value of TSUX back to
    1 for the specified waveform set.

<!-- 语法节 end -->

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
