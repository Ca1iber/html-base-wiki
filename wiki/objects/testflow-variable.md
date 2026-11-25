---
type: object
title: Testflow variable mapping table
layer: file
stage: testflow
tags: []
related: []
sources:
  - 02_System_reference/02.09_Test_Program_Management/02.09.03.04.08_Testflow_variable_mapping_table.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Testflow variable mapping table

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,189 字符逐字取自** `<02_System_reference/02.09_Test_Program_Management/02.09.03.04.08_Testflow_variable_mapping_table.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

Each row in the testflow variable mapping table describes the mapping of a specific
variable or flag. The table contains these columns:

STP
: The name of the STP from which the variable is imported

For
system testflow flags, this column contains
SYSTEM_FLAGS
.

STP Var
: The name of the variable or flag in the STP

For system
testflow flags, this column is empty.

MTP Var
: The name of the MTP variable or flag to which the STP
variable or flag is mapped

Type
: The data type of the MTP variable or flag

Value
: The value to which the MTP variable or flag is set

For
system flags, the value may initially be empty if a flag was defined in none of the STPs or
had different settings in different STPs. You must fill in any empty cells in this column;
otherwise, STPM will generate an error when creating the MTP.

Notes
: This column allows both you and STPM MCM to add remarks about
the variable or flag. These notes are just for human consumption and are never processed
automatically by STPM MCM. They may be overwritten when the tables are updated, so they are not
a suitable place for storing important information.

STPM MCM notes here any conflicts and
other issues detected.

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
