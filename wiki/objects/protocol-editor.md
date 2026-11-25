---
type: object
title: Protocol editor
layer: gui
stage: pattern
tags: []
related: []
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.22_Protocol_editor.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Protocol editor

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,504 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.22_Protocol_editor.htm>` 及其子主题 `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.22.02_Transaction_details.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Parameters（取自子主题 Transaction details）

Transaction parameters can be used within test methods to
pass variables to a transaction. This way one can create dynamic transactions. Typical
parameters of read/write transactions are register address, physical address and register
data.

The order of the parameter definition has an impact to the corresponding transaction
and the resulting state character sequence.

The state character sequence representing a
decoded field will be mapped back to transaction parameters during parameter reconstruction in
order to be readable from test methods.

[表] Properties
列: Property | Description
行 1:
  Direction
  Defines the direction from a DUT perspective.
    
    IN - parameter values will be passed to the DUT
    
    OUT - the DUT is passing parameter values to the application
行 2:
  Length
  Defines the length of this parameter in bits/state characters.
行 3:
  Decode function
  For input parameters the decode functions describes which field is used to fill in
    the parameter value.
    
    For output parameters the decode function describes how the received bits/state character
    sequence (represented by the parameter value) is transferred back to fields.
行 4:
  Display mode
  Specifies the number format in which numerical parameter values are displayed in
    the TA column of the Pattern Debug Tool. Possible values are "BINARY", "DECIMAL",
    and "HEX". HEX is the default.
    
    The property is ignored if the parameter value is specified as a state character
    sequence.

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
