---
type: object
title: GCTX? - (Get ConTeXt))
layer: L1
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.129_GCTX__-__Get_ConTeXt.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# GCTX? - (Get ConTeXt))

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,384 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.129_GCTX__-__Get_ConTeXt.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
GCTX? {setup_type},[setup_comp]
```

returns:

GCTX

{
setup_type
}{,
setup_nr
|"
name
"},"[
context_name
]"

### Parameters

[表]
行 1:
  setup_type [跨 7 行]
  The type of the setup component for which [跨 2 列]
    the mode context is queried. Possible values are:
行 2:
  TIM
  Timing equation set
行 3:
  LEV
  Level equation set
行 4:
  WAVE
  Wavetable
行 5:
  LBL
  Sequencer label
行 6:
  SPCF
  Multi-port specification
行 7:
  CURR
  The mode context for the current primary sets (as defined with the
    SPRM command) and the current start label (as defined with the
    SQSL command).
行 8:
  setup_nr
  The number of a setup component. This [跨 2 列]
    parameter is ignored for setup type CURR.
行 9:
  name
  The name of a wavetable, or the name of a [跨 2 列]
    multi-port specification. This parameter is ignored for setup type CURR.
行 10:
  context_name
  The name of the mode context. If you [跨 2 列]
    specified CURR for the setup_type parameter, and the current mode
    context is not correct, GCTX? returns an empty string.
    
    The context is only correct when all primary sets (defined by SPRM)
    and the current start label (defined by SQSL) are associated with the
    same mode context. Furthermore, if there exists a primary multi-port specification, the
    mode context must be the same for all ports of this specification.

### Example

```
> GCTX? TIM,101
< GCTX TIM,101,"High-Speed"
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
