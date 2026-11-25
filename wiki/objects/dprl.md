---
type: object
title: DPRL, DPRL? - (Default PRimary Level sets)
layer: L1
stage: level
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.82_DPRL__DPRL__-__Default_PRimary_Level_sets.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# DPRL, DPRL? - (Default PRimary Level sets)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **507 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.82_DPRL__DPRL__-__Default_PRimary_Level_sets.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### DPRL

```
DPRL {level_set}, {dps_set}, [screen_select]
```

### DPRL?

```
DPRL?
```

returns:

```
DPRL {level_set}, {dps_set}, [screen_select]
```

### Parameters

[表]
行 1:
  level_set
  Level Set number. [跨 2 列]
行 2:
  dps_set
  DPS Set number. [跨 2 列]
行 3:
  screen_select [跨 4 行]
  LEV
  level
行 4:
  DPS
  DPS
行 5:
  DOV
  DPS overvoltage
行 6:
  FST
  FAST Eqn & Spec Results

### Example

```
DPRL?
```

returns:

```
DPRL 1,2,LEV
```

On sending
a query, the system reports that the default primary level set is 1 and the default primary DPS
set is 2.

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
