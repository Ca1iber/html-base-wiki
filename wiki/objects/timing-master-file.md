---
type: object
title: Timing setup master file
layer: file
stage: timing
tags: []
related: []
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.04.05_Timing_setup_master_file.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Timing setup master file

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **630 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.04.05_Timing_setup_master_file.htm>` 及其子主题 `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.04.05.01_Master_file_format_for_timing_setup.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Master file format for timing setup）

The following is an example of a timing master file:

```
hp93000,timing_master_file,0.1
# this is a comment
testerfile: demo.tim

EQNSET 1: files/part1.tim
EQNSET 2 [PIN_ALIAS_SET usb_set]: files/eqnset02.tim

WAVETABLE wtbl_1: files/part1.tim
WAVETABLE wtbl_2: files/wtbl_2.tim

MULTIPORT_SPEC "spec_1":files/part1.tim
MULTIPORT_SPEC "spec_2":files/spec_2.tim
DEFINES: files/defines.tim
```

In the assembled level setup file
demo.tim
, the alias set

usb_set
 is used in the equation set 2. When
demo.tim
 is
splitted, the alias set
usb_set
 is removed from the generated sub-file

eqnset02.tim
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
