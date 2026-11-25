---
type: object
title: JSPR, JSPR? - (Jitter Set PRimary set)
layer: L1
stage: timing
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.149_JSPR__JSPR__-__Jitter_Set_PRimary_set.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# JSPR, JSPR? - (Jitter Set PRimary set)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **285 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.149_JSPR__JSPR__-__Jitter_Set_PRimary_set.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### JSPR

```
JSPR {"js_set_name"|""}
```

### JSPR?

```
JSPR?
```

returns:

```
JSPR {"js_set_name"|""}
```

### Parameters

[表]
行 1:
  js_set_name
  Specifies the name of an existing jitter set. Specify an empty string to inactivate
    the current primary set and thus to disable jitter injection.

### Example

```
> JSPR "js_set1"
```

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.149_JSPR__JSPR__-__Jitter_Set_PRimary_set.htm>` 的 `## Errors` 段。**不是转述。**
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if no jitter set with the specified name
exists.

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
