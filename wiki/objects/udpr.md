---
type: object
title: UDPR - (UnDefine Pin Role)
layer: L1
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.297_UDPR_-__UnDefine_Pin_Role.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# UDPR - (UnDefine Pin Role)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **725 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.297_UDPR_-__UnDefine_Pin_Role.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
UDPR "alias_set_name"|@,"pin_alias",(package_pin_name|@)
```

### Parameters

[表]
行 1:
  alias_set_name
  The alias set name.
    
    The alias of the pin (specified by the pin name parameter) defined in
    this alias set is deleted.
    
    The symbol @ can be used to list all the required alias set names.
行 2:
  pin_alias
  The pin alias.
行 3:
  package_pin_name
  The package pin name.
    
    The symbol @ can be used to list all the required package pin names.

### Example

```
UDPR "@","",(@)
```

This example deletes all the
alias sets.

```
UDPR "FUNC","",(@)
```

This example deletes
the alias set FUNC.

```
UDPR "FUNC","CLK",(CP)
```

This
example deletes the pair of package pin name CP and the pin alias CLK from the alias set
FUNC.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.297_UDPR_-__UnDefine_Pin_Role.htm>` 的 `## Errors` 段。**不是转述。**
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if the package pin name has not been
defined.

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
