---
type: object
title: APRM - (Activate PRiMary sets)
layer: L1
stage: level
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.01_APRM_-__Activate_PRiMary_sets.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# APRM - (Activate PRiMary sets)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **318 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.05.02.01_APRM_-__Activate_PRiMary_sets.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
APRM {mode}
```

### Parameters

[表]
行 1:
  mode [跨 3 行]
  Selects the activation [跨 2 列]
    mode:
行 2:
  FRC
  Forced activation. Primary sets are always
    activated.
行 3:
  CNL
  Conditional activation, depends on previous activation
    performed by APRM or by any of the commands in
    the second list above.

### Example

```
APRM CNL
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
