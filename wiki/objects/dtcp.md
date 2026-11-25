---
type: object
title: DTCP, DTCP? - (Define Technology Control Parameters)
layer: L1
stage: project
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.93_DTCP__DTCP__-__Define_Technology_Control_Parameters.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# DTCP, DTCP? - (Define Technology Control Parameters)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **818 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.93_DTCP__DTCP__-__Define_Technology_Control_Parameters.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### DTCP

```
DTCP {"key"}, {"value"}
```

### DTCP?

```
DTCP? {"key"}
```

returns:

```
DTCP {"key"}, {"value"}
```

### Parameters

[表]
行 1:
  key
  The string specifies the system control parameter.
    Currently, the only supported control parameters are testpoints and
    extended_dram_factor.
    
    For more information, refer to `testpoints`（raw: `49363.htm#_49363__row_testpoints`）
    and `extended_dram_factor`（raw: `49363.htm#_49363__row_extended_dram_factor`）
    in `Technology file for a device`（raw: `49363.htm`）.
行 2:
  value
  The value to be set as string.

### Examples

```
> DTCP? "testpoints"
< DTCP "testpoints", "0"
> DTCP "testpoints", "100"
> DTCP? "testpoints"
< DTCP "testpoints", "100"
> *RST
> DTCP? "testpoints"
< DTCP "testpoints", "100"
```

```
> DTCP "extended_dram_factor","90"
> *RST
> DTCP? "extended_dram_factor"
< DTCP "extended_dram_factor","90"
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
