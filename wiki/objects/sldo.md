---
type: object
title: SLDO - (Switch Level and Dps Order)
layer: L1
stage: level
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.223_SLDO_-__Switch_Level_and_Dps_Order.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# SLDO - (Switch Level and Dps Order)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,623 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.223_SLDO_-__Switch_Level_and_Dps_Order.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### SLDO

```
SLDO {order}, [report]
```

### SLDO?

```
SLDO? [operation]
```

returns:

```
SLDO {order}, [report]
```

### Parameters

[表]
行 1:
  order [跨 3 行]
  This parameter sets the switching order [跨 2 列]
    mode:
行 2:
  FDSL
  First DPS, second levels. If this parameter is specified, the DPS
    voltage values are always switched before the voltage values of the levels.
行 3:
  CVDL
  There are three possibilities:
    
    1. If DPS voltage values are increasing or stable, DPS voltages are switched before level
    voltages.
    
    2. If DPS voltage values are decreasing or stable, level voltages are switched before DPS
    voltages.
    
    3. If the voltages of some DPS pins are decreasing while the voltages of others are
    increasing (ambiguous case), DPS voltages are always switched first.
行 4:
  report [跨 5 行]
  This parameter sets the report mode, which [跨 2 列]
    can be one of the following:
行 5:
  ALL
  Reports a change in the switching order from DPS voltages (first) to
    level voltages (first) and vice versa.
行 6:
  FLSD
  First levels, second DPS. Reports a change in the switching order to
    switching level voltages first.
行 7:
  AMBI
  Ambiguous case. Reports an ambiguous case.
行 8:
  NONE
  Nothing is reported. This is the default report mode.
行 9:
  operation
  This is the mode of operation. [跨 2 列]
    SAVE returns values for everything that can be set.

### Example

```
SLDO CVDL, AMBI
```

This example switches either the DPS voltage
values or the level voltage values first when changing from one DPS or level set to the next
depending on which of the three above mentioned cases occur and reports any ambiguous
case.

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
