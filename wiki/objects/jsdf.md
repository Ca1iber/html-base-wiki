---
type: object
title: JSDF, JSDF? - (Jitter Set DeFinition)
layer: L1
stage: timing
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.148_JSDF__JSDF__-__Jitter_Set_DeFinition.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# JSDF, JSDF? - (Jitter Set DeFinition)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **723 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.148_JSDF__JSDF__-__Jitter_Set_DeFinition.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### JDSF

```
JSDF {"js_set_name"} [, "mode_context"]
```

### JDSF?

```
JSDF? ["js_set_name"|ALL]
```

returns:

```
JSDF {"js_set_name"} [, "mode_context"]
```

### Parameters

[表]
行 1:
  js_set_name
  In the command, this is the name of a new jitter set. In the query, it is a name of
    an existing jitter set. If you omit this parameter in the query, JSDF?
    will return the names of all user defined jitter sets.
行 2:
  mode_context
  The mode context with which the jitter set is associated. If this parameter is
    omitted, the DEFAULT context is assumed.
行 3:
  ALL
  With this parameter, the query returns all existing jitter sets.

### Example

```
> JSDF "js_set1"
> JSDF "js_set2"
> JSDF "js_set3"

> JSDF?
< JSDF "js_set1"
< JSDF "js_set2"
< JSDF "js_set3"
```

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.148_JSDF__JSDF__-__Jitter_Set_DeFinition.htm>` 的 `## Errors` 段。**不是转述。**
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if a jitter set with the specified name
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
