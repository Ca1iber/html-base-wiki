---
type: object
title: PSFC, PSFC? - (Parallel Setup FoCus)
layer: L1
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.191_PSFC__PSFC__-__Parallel_Setup_FoCus.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# PSFC, PSFC? - (Parallel Setup FoCus)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,556 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.191_PSFC__PSFC__-__Parallel_Setup_FoCus.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### PSFC

```
PSFC {site|"site_string"|ALL}
```

### PSFC?

```
PSFC? [STR]
```

returns

```
PSFC {"site_string"|ALL}
```

### Parameters

[表]
行 1:
  site
  A single integer representing the site number.
行 2:
  site_string
  A string of characters ("0" or "1"). The length of the string
    corresponds to the number of the configured sites. The
    nth character of this string
    stands for site n.
    
    1 means that the site is (to be) addressed by any
    subsequent commands that take the setup focus into
    account.
    
    0 means that the site is not (to be) addressed by any
    subsequent commands.
    
    If some of the sites that are required to get the setup focus are
    not available (because they use a channel that is inactivated in
    the MCDIgnore file) the setup status of
    these sites will not be changed.
行 3:
  ALL
  In the command, this means that all sites that are available for testing
    (that is, do not use a channel that is inactivated in the MCDIgnore
    file) are to be addressed by subsequent (setup focus aware) commands.
    
    ALL is returned in the query reply, if the query is issued without the
    STR parameter, and if all available sites have the setup focus.
行 4:
  STR
  forces the query to return a site string even if all available sites
    have the setup focus. This can be used to check if some sites are not available.

### Example

```
PSFC "11111110"
```

In this example, 8 sites are defined. The

PSFC
 command unsets the setup focus for the last site. The setup data of
this site will not be changed by any subsequent command execution.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.191_PSFC__PSFC__-__Parallel_Setup_FoCus.htm>` 的 `## Errors` 段。**不是转述。**
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if not all pins at the site have had their channels assigned by the

PALS
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
