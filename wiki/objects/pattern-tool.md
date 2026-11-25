---
type: object
title: Pattern Tools
layer: gui
stage: pattern
tags: []
related: []
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16_Pattern_Tools.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Pattern Tools

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **3,958 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16_Pattern_Tools.htm>` 及其子主题 `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.06_Cloning_a_pattern.htm>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.07_Moving_or_copying_pattern_files.htm>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.08_Deleting_pattern_files.htm>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.09_Checking_pattern_references.htm>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.01_Collapsed_and_expanded_mode.htm>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.02_Signal_and_pin_group_representations.htm>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.03_Pattern_editor_properties_view.htm>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.04.09_Protocol_pattern_specifics_of_the_Pattern_Explorer.htm>`。**不是转述。**
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



### Example（取自子主题 Collapsed and expanded mode）

The
following two figures show the same pattern in collapsed mode and in expanded mode.

The pattern contains the sequencer instruction RPTV 3 2, which means the next three
vectors are performed twice.

In the figure below, which shows the same pattern in expanded
mode, you can see the resolved sequencer instruction and the Cycle# column.

### Example（取自子主题 Signal and pin group representations）

The following figure shows the signals Pin 1, Pin 2 and Pin 3 in three different
formats. The signal column headers contain the signal name (for example Pin 1) and the format
(SC, DVC, PW).

### Examples（取自子主题 Pattern editor properties view）

### Vector properties

The graphic below shows the properties of a vector in
device cycle (DVC) format.

On vector properties views you cannot edit any parameters. Do this in the pattern
editor.

The vector properties view always shows the physical waveform. Drive edges and
receive edges appear on two different lines. In collapsed mode the view is based on the
`base wavetable`（raw: `107915.htm`）
, in expanded mode the properties are taken from the
primary wavetable.

Any abbreviations you may use in your wavetables, are translated into
the proper action code for
`drive edges`（raw: `10603.htm`）
 and
`receive edges`（raw: `10606.htm`）
.

[表]
列: Drive edges | | | Receive edges |
行 1:
  Abbreviation
  Action code
  
  Abbreviation
  Action code
行 2:
  0
  F00
  
  L
  E0
行 3:
  1
  F10
  
  H
  E1
行 4:
  !Z
  FN0
  
  M
  EI
行 5:
  Z
  FNZ
  
  U
  EU
行 6:
  . (period)
  N
  
  X
  EX
行 7:
  
  
  
  . (period)
  N

### Test point properties

The graphic below shows the properties of a test
point, in this case the highlighting of a force value in a dynamic DC test setup.

The properties view of a dynamic DC measure test point will also show the measure
result. See below:

### Vector variable properties

The properties view of a vector variable (see
below) allows to edit for example, the assigned pins, the transfer mode, and other parameters.
To display additional data upload formatting parameters (Upload Parameters) click the

Show Advanced Properties
 icon. For a definition of the vector variable
parameters see
`Creating a Digital Capture setup`（raw: `116306.htm`）
.

Note
 The Upload Parameters shown here are the last which were used by the
system. If you stop a testflow at a particular test suite and then open the pattern editor, the
vector variable data is shown exactly as it was last uploaded from any test method or any
command line operation.

### Example（取自子主题 Protocol pattern specifics of the Pattern Explorer）



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
