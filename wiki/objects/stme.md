---
type: object
title: STME, STME? - (SiTe Match Enable)
layer: L1
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.250_STME__STME__-__SiTe_Match_Enable.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# STME, STME? - (SiTe Match Enable)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,107 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.250_STME__STME__-__SiTe_Match_Enable.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### STME

```
STME {ON|OFF|AUTO|FAST},
```

### STME?

```
STME?
```

returns:

STME

{
ON
|
OFF
|
FAST
),

### Parameters

[表]
行 1:
  ON
  Turns the site match function on.
行 2:
  OFF
  Turns the site match function off.
行 3:
  AUTO
  Starting the sites successively affects the test negatively if the pin
    configuration contains at least one shared digital channel for triggering an analog module.
    The AUTO option checks if such a shared channel exists. If it does, the
    match site function is set to OFF; if not, it is set to
    ON. AUTO is the default.
行 4:
  FAST
  Activates the `Fast Sync`（raw: `150814.htm`） feature (local synchronization) of the test
    processor. After setting this option," STME ON" is required to turn on
    the site match function.

### Example

```
> STME AUTO,
> STME?
< STME ON,
```

This example sets the
site match function to
AUTO
, then reads the actual setting. Since the actual
setting is
ON
, the pin configuration cannot contain a shared digital
channel.

```
>SQST OFF
>NIFE 2
>STME FAST,
>STME ON,
```

This example configures the Fast Sync feature, and sets two independent Fast Sync ports
on each test processor.

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
