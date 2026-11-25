---
type: object
title: PRLT? - (request Parallel ResuLTs)
layer: L1
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.183_PRLT__-__request_Parallel_ResuLTs.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# PRLT? - (request Parallel ResuLTs)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **887 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.183_PRLT__-__request_Parallel_ResuLTs.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
PRLT? ["exec_context",] {site}
```

returns:

```
PRLT {site}, {"result"}
```

### Parameters

[表]
行 1:
  exec_context
  An execution context. For more information
    on execution contexts see `Using execution contexts`（raw: `135848.htm`）.
行 2:
  site
  The site parameter is
    
    number
    A single integer representing the site number.
    
    ALL
    Means that all the results of all configured sites are
    returned.
行 3:
  result
  The result parameter is a string containing one character for every
    site. The nth character stands for
    site n. Possible characters are:
    
    P
    If the last test passed on all pins.
    
    F
    If the last test failed at any pin.
    
    0
    If the site was masked during the last test.

### Example

```
PRLT? ALL
```

returns:

```
PRLT ALL, "PF0"
```

In
this example, site 1 passed the last test, site 2 failed it, and site 3 was masked during the
test.

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
