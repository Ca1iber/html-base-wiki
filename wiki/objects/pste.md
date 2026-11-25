---
type: object
title: PSTE, PSTE? - (Parallel SiTe Enable)
layer: L1
stage: run
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.199_PSTE__PSTE__-__Parallel_SiTe_Enable.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# PSTE, PSTE? - (Parallel SiTe Enable)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,365 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.199_PSTE__PSTE__-__Parallel_SiTe_Enable.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### PSTE

```
PSTE {sites}
```

### PSTE?

```
PSTE? [STR]
```

returns

```
PSTE {sites|"site_string"}
```

### Parameters

[表]
行 1:
  sites
  The sites parameter is an integer that
    specifies the number of sites (to be) configured. The maximum is
    1024.
    
    For more information, refer to `Number of sites`（raw: `116532.htm#_116532__r_numberOfSites`） in
    `SmarTest system parameters - default values and limits`（raw: `116532.htm`）.
行 2:
  site_string
  A string consisting of "0" and "1". The length of the string corresponds to the
    number of the configured sites. The nth character of this
    string stands for site n.
    
    "0" indicates that the respective site uses a channel that is listed in the
    MCDIgnore file, and that this site therefore cannot be used for
    testing. "1" indicates that the site can be used.
行 3:
  STR
  If you specify this optional keyword in the query, PSTE? will return a site
    string.
    
    If this parameter is omitted, PSTE? will return the number of sites
    that are configured in the pin configuration.

### Example

```
> PSTE 3
```

This example configures three sites (site 1, site 2,
and site 3).

```
> PSTE? STR
< PSTE "101"
```

This example says that
three sites are configured, but that only two of them (site 1 and site 3) are available for
testing. Site 2 uses a channel that is listed in the
MCDIgnore
 file, and
therefore cannot be used for testing.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.199_PSTE__PSTE__-__Parallel_SiTe_Enable.htm>` 的 `## Errors` 段。**不是转述。**
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

Not all pins at the site have had their channels assigned by the
`PALS`（raw: `98680.htm`）
 command.

All channels are listed in the
MCDIgnore
 file and therefore not
available for testing.

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
