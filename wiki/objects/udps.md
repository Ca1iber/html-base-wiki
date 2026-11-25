---
type: object
title: UDPS - (Undefine DPS pin)
layer: L1
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.298_UDPS_-__Undefine_DPS_pin.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# UDPS - (Undefine DPS pin)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **464 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.298_UDPS_-__Undefine_DPS_pin.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
UDPS {(pinlist)}
```

### Parameters

[表]
行 1:
  pinlist
  Consists of single or multiple pin names or the symbol @ which undefines all
    DPS pins. If more than one pin is to be removed, the names must be separated with a comma.

### Example

```
UDPS (Vee)
```

This example removes pin Vee from the setup. The
software saves the level data associated with the DPS channel. Therefore if you redefine the
channel using the same or a different name, the DPS settings are immediately restored.

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
