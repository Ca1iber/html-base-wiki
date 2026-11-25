---
type: object
title: Level setup master file
layer: file
stage: level
tags: []
related: []
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.02.05_Level_setup_master_file.htm
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02.04.04_Creating_a_level_master_file.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Level setup master file

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **563 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.02.05_Level_setup_master_file.htm>` 及其子主题 `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.02.05.01_Master_file_format_for_level_setup.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Master file format for level setup）

### Level master file
```
hp93000,level_master_file,0.1

# this is a comment
testerfile: demo.lev

EQNSET 1 [PIN_ALIAS_SET usb_set]: files/eqnset01.lev
EQNSET 2 : files/eqnset02.lev
EQNSET 3 : files/eqnset_34.lev
EQNSET 4 : files/eqnset_34.lev
TESTDATA : files/testdata.lev
DEFINES : files/defines.lev
GENERAL: GENERAL.lev
```

In
the assembled level setup file
demo.lev
, the alias set
usb_set

is used in the equation set 1. When
demo.lev
 is splitted, the alias set

usb_set
 is removed from the generated sub-file
eqnset01.lev

and package pin names are used.

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
