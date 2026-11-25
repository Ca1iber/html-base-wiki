---
type: object
title: PACT, PACT? - (Parallel ACTivities control)
layer: L1
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.171_PACT__PACT__-__Parallel_ACTivities_control.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# PACT, PACT? - (Parallel ACTivities control)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,583 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.171_PACT__PACT__-__Parallel_ACTivities_control.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### PACT

PACT
 {
control
},
{
site
|
ALL
}

PACT

{"
site_string
"}

### PACT?

```
PACT?
```

returns

```
PACT {control}, {site}
```

Or:

```
PACT?STR
```

returns

```
PACT {"site_string"}
```

### Parameters

[表]
行 1:
  control
  The control parameter [跨 2 列]
    is:
行 2:
  
  ACTIVE
  When a site is ACTIVE it receives all test data, and
    generates results for the tests.
行 3:
  
  MASKED
  When a site is MASKED, it receives all test data, as with the
    ACTIVE parameter. However, the receivers for the site are disabled and
    no result information is available.
行 4:
  site
  A single integer representing a site [跨 2 列]
    number.
行 5:
  site_string
  A string consisting of "0" and "1". One [跨 2 列]
    character must be given for every site that is configured in the pin configuration. "0"
    indicates that the respective site is (to be) masked. "1" indicates that the respective
    site is (to be) activated.
行 6:
  ALL
  means that all configured sites that are [跨 2 列]
    available for testing (that is, do not use a channel that is inactivated in the MCDIgnore
    file) are to be activated or masked.
    
    For the MCDIgnore file see MCDIgnore usage and restrictions in Service Guide Part
    1.
行 7:
  STR
  forces the query to return a site string [跨 2 列]
    instead of a single line for every site.

### Example

```
> PACT ACTIVE, 1
> PACT MASKED, 2
> PACT MASKED, 3
```

This
example masks site 2 and site 3, and makes site 1 active.

```
> PACT?
< PACT ACTIVE,1
< PACT MASKED,2
< PACT MASKED,3
> PACT? STR
< PACT "100"
```

This
example shows the impact of the optional
STR
 parameter for the
query.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.171_PACT__PACT__-__Parallel_ACTivities_control.htm>` 的 `## Errors` 段。**不是转述。**
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if not all pins at the site have had their
channels assigned by the
`PALS`（raw: `98680.htm`）
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
