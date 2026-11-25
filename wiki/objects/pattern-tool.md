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

**文档事实** Pattern Tools 是 SmarTest 中用于创建、编辑和调试 pattern 与 burst 的一组工具，由 Pattern Explorer、Pattern Editor 与 Multiport Burst Editor 三部分组成。

**文档事实** Pattern Explorer 用于浏览已加载 setup 中的 pattern、创建和删除 pattern/port burst/multiport burst、编辑 burst，并可启动 Pattern Editor 与 Multiport Burst Editor。

**文档事实** Pattern Editor 用于显示已加载 setup 的 pattern、编辑 pattern 与分析错误；源页注明超过 500,000 条指令的 pattern 无法在 Pattern Editor 中打开。

**文档事实** Multiport Burst Editor 用于创建和显示 port burst，在单页与 Overview 页编辑 port burst，按 sync group 显示 multiport port burst 的时间线同步，并分析错误。

**文档事实** 源页注明 F330 Scan 自 release 7.0.1 起已废弃，基于 Eclipse 的 pattern 工具不支持 F330 scan pattern；加载时会报 "Unsupported pattern type" 等错误，需在 6.5.2 之前的 SmarTest 版本中用旧版 pattern debug 工具查看和编辑。

## 典型用法

**文档事实** 典型流程是先在 Pattern Explorer 中浏览/创建 pattern 或 burst，再从 Pattern Explorer 启动 Pattern Editor 或 Multiport Burst Editor 进行编辑与错误分析。

**文档事实** 编辑 pattern 用 Pattern Editor，编辑 port burst 用 Multiport Burst Editor；后者同时提供 Overview 页和按 sync group 的时间线同步视图。

**文档事实** 文档把 Pattern Tools 列为数字通道 setup 的步骤之一：用 Pattern Tools 为数字引脚设置 vector。

**文档事实** UHC4T 文档指出动态测量设置可使用 Pattern Tools，做法与 Pin Scale 数字卡测量类似。

**建议** 源页建议关闭 Klipper（KDE 剪贴板工具），以免与 SmarTest work center 和 pattern debug 工具的复制粘贴操作冲突。

**文档事实** 源页提醒 Pattern Explorer 与 Pattern tool 不发送 firmware 命令，因此其活动不记录在 MCDLog；部分 Test Method API 也是如此。

## 和谁有关

- **文档事实** Pattern Explorer、Pattern Editor、Multiport Burst Editor：它们是本页列出的三个组成工具，也是本页 Subtopics 与 Related information 中的直接子主题。
- **文档事实** Definitions: Vector, Pattern, Burst, etc. ...：本页 Related information 指向该定义页，用于解释 vector、pattern、burst 等术语。
- **文档事实** Task 3: Setups for Digital Channels：该页把“用 Pattern Tools 为数字引脚设置 vector”列为数字通道 setup 的一步，说明本页与数字通道配置相关。
- **文档事实** UHC4T measurement modes：该页说明动态测量设置可使用 Pattern Tools，且与 Pin Scale 数字卡测量类似。
- **文档事实** Using the Trace Function：该页注明 Pattern Explorer 与 Pattern tool 不发送 firmware 命令、活动不记入 MCDLog，说明两者在 MCDLog 记录范围上的关系。
- **文档事实** Tools in alphabetical order 与 Tools grouped by function：这两个工具索引页均引用本页，用于工具检索与按功能分组。

## 版本

**文档事实** Functional changes 记 Introduced before SmarTest 6.3.2；SmarTest 7.1.3 新增 Multiport Burst Editor。

## 出处

- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16_Pattern_Tools.htm`，主源，含工具组成、各工具职责与注意事项、Related information 与 Functional changes。
- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.06_Cloning_a_pattern.htm`、`...16.01.07_Moving_or_copying_pattern_files.htm`、`...16.01.08_Deleting_pattern_files.htm`、`...16.01.09_Checking_pattern_references.htm`、`...16.02.01_Collapsed_and_expanded_mode.htm`、`...16.02.02_Signal_and_pin_group_representations.htm`、`...16.02.03_Pattern_editor_properties_view.htm`、`...16.04.09_Protocol_pattern_specifics_of_the_Pattern_Explorer.htm`，语法节逐字抽取来源。
