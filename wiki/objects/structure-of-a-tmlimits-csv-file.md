---
type: object
title: Structure of a TMLimits CSV file
layer: file
stage: testmethod
tags: []
related: []
sources:
  - 02_System_reference/02.10_Data_Logging/02.10.01.08.01.01.03.01_Structure_of_a_TMLimits_CSV_file.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Structure of a TMLimits CSV file

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,590 字符逐字取自** `<02_System_reference/02.10_Data_Logging/02.10.01.08.01.01.03.01_Structure_of_a_TMLimits_CSV_file.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example

The example shown below is part of a bigger TMLimits CSV file. Only a few tests
and just one test mode are
shown:

```
"Suite name", "Test name", "Test number", "Units", "Lsl", "Usl", "Test_remarks"
"Test mode", "", "", "QA", "QA", "QA", ""
"Continuity2", "DC_CONT_P", "555", "UNIT", "-0.1", "0.1", "WalkZP"
"Continuity2", "DC_CONT_N", "565", "UNIT", "-0.1", "0.1", "WalkZP"
"DC_FreeVI", "IDD_Shutdown", "575", "uA", "-1", "6.88", "FreerunVI"
"DC_FreeVI", "IDD_FREG_PWR_ON", "585", "mA", "1", "10", "FreerunVI"
"DC_FreeVI", "FREG_OUT_PWR_ON", "595", "V", "1.6", "2.1", "FreerunVI"
"DC_FreeVI", "VDD_ALDO_PWR_ON", "605", "V", "1.25", "1.6", "FreerunVI"
"DC_FreeVI", "VDD_DREG_PWR_ON", "615", "V", "1.085", "1.315", "FreerunVI"
"ATECtrl", "ATECtrl", "625", "", "-0.1", "0.1", "ATEctrlEdl"
```

This
is the same example with an added user-defined column
"Status":

```
"Suite name", "Test name", "Test number", "Units", "Status", "Lsl", "Usl", "Test_remarks"
"Test mode", "", "", "QA" "", "QA", "QA", ""
"Continuity2", "DC_CONT_P", "555", "UNIT", "4", "-0.1", "0.1", "WalkZP"
"Continuity2", "DC_CONT_N", "565", "UNIT", "3", "-0.1", "0.1", "WalkZP"
"DC_FreeVI", "IDD_Shutdown", "575", "uA", "3", "-1", "6.88", "FreerunVI"
"DC_FreeVI", "IDD_FREG_PWR_ON", "585", "mA", "0", "1", "10", "FreerunVI"
"DC_FreeVI", "FREG_OUT_PWR_ON", "595", "V", "1", "1.6", "2.1", "FreerunVI"
"DC_FreeVI", "VDD_ALDO_PWR_ON", "605", "V", "4", "1.25", "1.6", "FreerunVI"
"DC_FreeVI", "VDD_DREG_PWR_ON", "615", "V", "2", "1.085", "1.315", "FreerunVI"
"ATECtrl", "ATECtrl", "625", "", "4", "-0.1", "0.1", "ATEctrlEdl"
```

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
