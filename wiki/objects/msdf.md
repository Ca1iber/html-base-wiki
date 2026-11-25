---
type: object
title: MSDF, MSDF? - (Modulation Set DeFinition)
layer: L1
stage: timing
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.163_MSDF__MSDF__-__Modulation_Set_DeFinition.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# MSDF, MSDF? - (Modulation Set DeFinition)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **713 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.163_MSDF__MSDF__-__Modulation_Set_DeFinition.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### MDSF

```
MSDF {"ms_set_name"} ,{modulation_type}
```

### MDSF?

```
MSDF? ["ms_set_name"|ALL]
```

returns:

```
MSDF {"ms_set_name"} ,{modulation_type}
```

### Parameters

[表]
行 1:
  ms_set_name
  In the command, this is the name of a new modulation set. In the query, it is a
    name of an existing modulation set. If you omit this parameter in the query,
    MSDF? will return the names of all user defined modulation sets.
行 2:
  modulation_type
  Currently, the only allowed modulation type is TIM (for
    "timing").
行 3:
  ALL
  With this parameter, the query returns all existing modulation sets.

### Example

```
> MSDF "ms_set1",TIM
> MSDF "ms_set2",TIM
> MSDF "ms_set3",TIM

> MSDF?
< MSDF "ms_set1",TIM
< MSDF "ms_set2",TIM
< MSDF "ms_set3",TIM
```

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.163_MSDF__MSDF__-__Modulation_Set_DeFinition.htm>` 的 `## Errors` 段。**不是转述。**
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if a modulation set with the specified name
already exists.

<!-- 报错节 end -->

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
