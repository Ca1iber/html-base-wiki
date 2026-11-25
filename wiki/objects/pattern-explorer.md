---
type: object
title: Pattern Explorer
layer: gui
stage: pattern
tags: []
related: []
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01_Pattern_Explorer.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Pattern Explorer

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,639 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01_Pattern_Explorer.htm>` 及其子主题 `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.06_Cloning_a_pattern.htm>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.07_Moving_or_copying_pattern_files.htm>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.08_Deleting_pattern_files.htm>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.09_Checking_pattern_references.htm>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.14.01_Moving_vectors_to_another_memory_type.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Cloning a pattern）

The following examples explain the transformation to NOP instructions in more
detail.

For the instruction
SSRC dsm_data_pattern
, if the port of the pattern

dsm_data_pattern
 is also the port of the target pattern, the

SSRC
 instruction is cloned to the target pattern without change.

For the instruction
JSUB sub_pattern
, as the port of the pattern

sub_pattern
 is not the same as that of the source pattern, in the target
pattern, the
JSUB
 instruction is replaced by an
NOP

instruction and a warning message is displayed on the console tab.

If an instruction is replaced by
NOP
 in the target pattern (for example,
the
JSUB sub_pattern
 instruction), you must modify the instruction
manually:

Create a new subroutine pattern
sub_pattern_clone
 by cloning the

sub_pattern
 pattern with the port of the target pattern.

Replace
NOP
 with the
JSUB
 instruction using the new
pattern:
JSUB sub_pattern_clone.

### Example（取自子主题 Moving or copying pattern files）

Update of pattern master file when moving
pattern 4
 from the

patterns_a
 folder to the
patterns_b

 folder
:

[表]
列: Before | After
行 1:
  ```
    hp93000,pattern_master_file,0.1
    
    path:
    ../data/patterns_a
    
    files:
    pattern1
    pattern2
    pattern3
    pattern4
    
    path:
    ../data/patterns_b
    
    files:
    pattern5
    pattern6
    ```
  ```
    hp93000,pattern_master_file,0.1
    
    path:
    ../data/patterns_a
    
    files:
    pattern1
    pattern2
    pattern3
    
    path:
    ../data/patterns_b
    
    files:
    pattern4
    pattern5
    pattern6
    ```

### Example（取自子主题 Deleting pattern files）

"Cannot delete ..." error message:

Confirmation dialog:

### Example（取自子主题 Checking pattern references）



### Example（取自子主题 Moving vectors to another memory type）

conv_vector -target SM -p pins_soc pattern_vm
pattern_sm

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
