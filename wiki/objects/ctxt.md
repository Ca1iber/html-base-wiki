---
type: object
title: CTXT, CTXT? - (ConTeXT)
layer: L1
stage: level
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.35_CTXT__CTXT__-__ConTeXT.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# CTXT, CTXT? - (ConTeXT)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **576 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.35_CTXT__CTXT__-__ConTeXT.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### CTXT

```
CTXT {action},{"name"}
```

### CTXT?

```
CTXT?ALL
```

returns:

```
CTXT {DEFINE},{"name"}
```

### Parameters

[表]
行 1:
  action [跨 4 行]
  Specifies the action. Possible values [跨 2 列]
    are:
行 2:
  DEFINE
  Defines a new mode context
行 3:
  DELETE
  Deletes a mode context
行 4:
  ALL
  Displays all existing mode contexts (only in the query).
行 5:
  name
  The name of the mode context. If the [跨 2 列]
    action parameter is set to DELETE, you can also
    specify ALL to delete all mode contexts.

### Example

```
> CTXT? ALL
< CTXT DEFINE,"DEFAULT"
< CTXT DEFINE,"differential"
< CTXT DEFINE,"PdrvNPrcv"
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
