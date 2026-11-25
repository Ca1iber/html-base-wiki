---
type: object
title: SetupLevelSet0
layer: L2
stage: level
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.05.04.06_SetupLevelSet0.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# SetupLevelSet0

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,695 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.05.04.06_SetupLevelSet0.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Parameters

[表]
行 1:
  Pins[]
  string
  array of pins
    
    Separate pins with semicolon (;). Valid pin types include I, O,
    or IO digital pin.
行 2:
  ClampVoltage.Mode[]
  string
  array of clamp mode. It can be:
    
    ON: Clamp is set to on with low/high voltage.
    
    OFF: Clamp is set to off.
    
    To specify different configuration for different pins, separate
    the values with semicolon (;).
行 3:
  ClampVoltage.Low_V[]
  string
  array of low clamp voltage in unit [V]
    
    To specify different configuration for different pins, separate
    the values with semicolon (;).
行 4:
  ClampVoltage.High_V[]
  string
  array of high clamp voltage in unit [V]
    
    To specify different configuration for different pins, separate
    the values with semicolon (;).
行 5:
  ActiveLoad.Mode[]
  string
  array of active load mode. It can be:
    
    ON: set up active load setting,
    Vt, Iol and Ioh
    
    OFF: turn off active load
    
    To specify different configuration for different pins, separate
    the values with semicolon (;).
行 6:
  ActiveLoad.CommutationVoltage_V[]
  string
  array of commutation voltage (Vcom), in unit
    [V]
    
    To specify different configuration for different pins, separate
    the values with semicolon (;).
行 7:
  ActiveLoad.SourceCurrent_A[]
  string
  array of active load source current (Ioh), in unit
    [A]
    
    To specify different configuration for different pins, separate
    the values with semicolon (;).
行 8:
  ActiveLoad.SinkCurrent_A[]
  string
  array of active load sink current (Iol), in unit
    [A]
    
    To specify different configuration for different pins, separate
    the values with semicolon (;).

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
