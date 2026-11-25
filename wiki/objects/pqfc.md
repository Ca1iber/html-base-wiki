---
type: object
title: PQFC, PQFC? - (Parallel Query FoCus)
layer: L1
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.03.02.19_PQFC__PQFC__-__Parallel_Query_FoCus.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# PQFC, PQFC? - (Parallel Query FoCus)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **226 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.03.02.19_PQFC__PQFC__-__Parallel_Query_FoCus.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### PQFC

```
PQFC {site}
```

### PQFC?

```
PQFC?
```

### Parameters

[表]
行 1:
  site
  The site parameter is single integer representing the number of
    the site that has or shall have the query focus.

### Example

```
PQFC 2
```

This example sets the query focus to site
2.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.03.02.19_PQFC__PQFC__-__Parallel_Query_FoCus.htm>` 的 `## Warnings`、`## Errors` 段。**不是转述。**
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Warnings

PQFC
 returns a warning if the specified site
is not available. In such cases the query focus is not changed.

### Errors

An error is generated if not all pins at the site have had their
channels assigned by the
PALS
 command. \

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
