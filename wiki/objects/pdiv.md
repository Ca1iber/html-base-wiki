---
type: object
title: PDIV? - (Period DIVider)
layer: L1
stage: timing
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.176_PDIV__-__Period_DIVider.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# PDIV? - (Period DIVider)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,228 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.176_PDIV__-__Period_DIVider.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
PDIV? {specset_id|"multi-port_spec"|"wavetbl"} [,spec_type][,(pinlist)]
```

returns:

```
PDIV {specset_id|"multi-port_spec"}, {period_div}
```

### Parameters

[表]
行 1:
  specset_id
  Identifier of a timing [跨 2 列]
    specification, which is derived as follows:
    
    100 * equation_set_no + specset_no
行 2:
  multi-port_spec
  To query a multi-port [跨 2 列]
    specification, enter the name of the specification.
行 3:
  wavetbl
  Name of a wavetable. This [跨 2 列]
    requires that spec_type is set to WFT.
行 4:
  period_div
  Possible values are -1 (for [跨 2 列]
    standard pins), 2, 3, 4, 6, 8 (only for fast pins).
行 5:
  spec_type [跨 3 行]
  Possible values are: [跨 2 列]
行 6:
  TIM
  Returns the period divider of the timing sets (fast pins). If
    not all timing sets have the same period divider for the same fast pin,
    PDIV? returns an error.
行 7:
  WFT
  Returns the implicit period divider of the wavetable
    specified as the first parameter.
行 8:
  pinlist
  This parameter is only [跨 2 列]
    applicable to fast pins. For standard pins,-1 is returned.

### Example

```
> PDIV? "fast",WFT,(I1)
< PDIV "fast",WFT,6,(I1)
```

This
example queries the implicit period divider of the fast pin
I1
 in the
wavetable
fast
. The factor is 6.

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
