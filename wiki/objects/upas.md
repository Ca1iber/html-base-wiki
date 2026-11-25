---
type: object
title: UPAS, UPAS? - (Utility Purpose ASsignment for multi-site)
layer: L1
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.304_UPAS__UPAS__-__Utility_Purpose_ASsignment_for_multi-site.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# UPAS, UPAS? - (Utility Purpose ASsignment for multi-site)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,759 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.304_UPAS__UPAS__-__Utility_Purpose_ASsignment_for_multi-site.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### UPAS

```
UPAS {site}, ["{setting}"], {(purpose_name)}
```

### UPAS?

```
UPAS? {site}, {(purpose_name)}
```

returns:

```
UPAS {site}, "{setting}", {(purpose_name)}
```

### Parameters

[表]
行 1:
  site
  The site parameter is an integer that defines the number of the site where the
    channels are to be defined.
    
    The integer must be greater than 1.
    
    When specified as part of the UPAS? query, you
    can use the parameter ALL to read the
    standard output states for all sites.
行 2:
  setting
  Output states for each member of the utility purpose on the specified site.
    
    Set the output state of each utility line with the following
    specifiers:
    
    0: Sets the corresponding (write) channel to high (high impedance state)
    
    1: Sets the corresponding (write) channel to low
    
    X (x): No action
    
    The number and order of characters must correspond to the ch_No_list parameter
    of the `DFUP`（raw: `98559.htm`） command.
    
    If this parameter is omitted, the specified site is set to the same states as site 1.
行 3:
  purpose_name
  Name of a utility purpose defined by the `DFUP`（raw: `98559.htm`） command.
    
    In the query, the symbol @ can be used to list all defined
    utility purposes.

### Example

```
> DFUP (101,102,103,104),"11XX",(AWG_CNCT)
> UPAS 2,"XX11",(AWG_CNCT)
> UPST ,(AWG_CNCT)
> FLSH
> UPST? (AWG_CNCT)
< UPST "11XX", (AWG_CNCT)
> PSFC 2
> UPST ,(AWG_CNCT)
> FLSH
> UPST? (AWG_CNCT)
< UPST "XX11", (AWG_CNCT)
```

In
this example, the
`DFUP`（raw: `98559.htm`）
 command defines a utility purpose AWG_CNCT
and output states for site 1. The
UPAS
 command defines the output states of
AWG_CNCT for site 2. First the settings of site 1 are activated. Then the setup focus is
restricted to site 2, and the output states for site 2 are activated.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.304_UPAS__UPAS__-__Utility_Purpose_ASsignment_for_multi-site.htm>` 的 `## Errors` 段。**不是转述。**
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

A multisite setting is not performed with the
`PSTE`（raw: `98711.htm`）
 command.

The specified site number is less than 0 or greater than that of the max site.

The given name is not allocated to any utility purpose.

The given name has already been assigned to a digital pin, analog pin, DPS pin, or utility
name.

Inconsistent settings are specified for one channel (for an example, see the
`DFUP`（raw: `98559.htm`）
 command).

The setting contains characters other than "0", "1" and "X (or x)".

The number of characters in the setting is not equal to that of the channel list in the

`DFUP`（raw: `98559.htm`）
 command.

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
