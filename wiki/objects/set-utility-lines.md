---
type: object
title: SetUtilityLines
layer: L2
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.05.04.07_SetUtilityLines.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# SetUtilityLines

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **2,453 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.05.04.07_SetUtilityLines.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Parameters

[表]
列: Parameter | Type | Description
行 1:
  type
  STRING
  The type of the utility line. It can be:
    
    UtilitylineName: The utility line name
    defined in the `Pin setting editors`（raw: `17548.htm`）.
    
    The utility lines to be set to on or to off can be
    defined by parameters
    
    utilityLineNameOn,
    
    utilityLineNameOff, or
    
    utilityPurpose.
    
    All three parameters can be filled with data at the same
    time.
    
    UtilitylineChannel: Utility lines are
    defined by the channel number.
    
    The utility channels to be set to on or to off can be
    defined by parameters
    
    utilityLineChannelOn or
    
    utilityLineChannelOff.
    
    Both parameters can be filled with data at the same
    time.
行 2:
  utilityLineNameOn
  STRING [跨 2 行]
  A single utility pin or a comma‑separated list of utility pins to be set to on or [跨 2 行]
    to off.
    
    Valid names are defined in the `Utility Pins editor`（raw: `105637.htm`）.
行 3:
  utilityLineNameOff
行 4:
  utilityPurpose
  STRING
  A utility purpose or a comma‑separated list of utility
    purposes to be applied.
    
    Valid names are defined in the `Pin setting editors`（raw: `17548.htm`） and
    configured in the `Utility Purpose Editor`（raw: `17603.htm`）.
行 5:
  utilityLineChannelOn
  STRING [跨 2 行]
  A single utility channel or a comma‑separated list of [跨 2 行]
    utility channels to be set to on or to off.
    
    The utility channels are to be defined like
    UTI101, UTI102.
    
    The format using three digits for the pogo blocks
    is also supported. For this format, the utility pins are to be
    defined as UTI16501 or
    UTI16502, for example.
    
    For the second optional `Utility Card`（raw: `351250.htm`） of EXA Scale systems, the utility pins
    can be defined only using the three‑digit format of
    the pogo blocks. The valid range for the second card is
    UTI26501 ... UTI27232.
    
    See also `Utility pogo block mapping`（raw: `347642.htm#_347642__s_Utility_pogo_block_mapping`）
    in `Utility pogo block - Utility Card (V93000 EXA Scale systems)`（raw: `347642.htm`）.
行 6:
  utilityLineChannelOff
行 7:
  waittime
  DOUBLE
  The time to wait after controlling all relays. It must not be
    negative.
    
    Default value is 0.0.
    
    Units are seconds.

For a coding example see the file

/opt/hp93000/soc/testmethod/library/miscellaneous_tml/SetUtilityLines.cpp

in
`Miscellaneous test methods (miscellaneous_tml)`（raw: `114358.htm`）

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
