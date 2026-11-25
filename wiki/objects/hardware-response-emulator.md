---
type: object
title: Hardware Response Emulator
layer: gui
stage: run
tags: []
related: []
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.06_Hardware_Response_Emulator.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Hardware Response Emulator

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **619 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.06_Hardware_Response_Emulator.htm>` 及其子主题 `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.06.02_Using_hardware_response_files_for_execution.htm>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.06.03_Hardware_response_files.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Using hardware response files for execution）

When the hardware response file is not found for the execution of a test suite with
the pass/fail result, the
Hardware Response Emulator Pass/Fail Dialog

window for the "Import" mode opens.

### Example（取自子主题 Hardware response files）

The hardware response file
TS1;Analog.DGT("a_out").getWaveform(1);1;1

is related to the first execution of the
Analog.DGT("a_out").getWaveform()
 API
called on site 1 in the method program in the
TS1
 test suite. Note that a
hardware response file name contains a default input value even if the value was not set in the
related API. This is the reason why the file name contains
Waveform(1)
 even if
"1" is not set for the API.

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
