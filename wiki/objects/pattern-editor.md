---
type: object
title: Pattern Editor
layer: gui
stage: pattern
tags: []
related: []
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02_Pattern_Editor.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Pattern Editor

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **9,411 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02_Pattern_Editor.htm>` 及其子主题 `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.01_Collapsed_and_expanded_mode.htm>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.02_Signal_and_pin_group_representations.htm>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.03_Pattern_editor_properties_view.htm>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.04.03_STATEMAP_section_of_the_wavetable.htm>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.06.16_Creating_a_Digital_Source_setup.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

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

### Examples（取自子主题 STATEMAP section of the wavetable）

### STATEMAP section with X1 waveforms
```
WAVETBL mytable
PINS io_pins
0 "d1:0 r1:X" 0
1 "d1:1 r1:X" 1
2 "d1:Z r1:L" L
3 "d1:Z r1:H" H
4 "d1:Z r1:X" X
brk ""
STATEMAP
#physSeq statechars x-mode selector
0 0 x1
1 1 x1
2 L x1
3 H x1
4 X x1
```

The
five STATEMAP lines of above example define X1 waveforms.

The second STATEMAP example
below defines xN and x1/N mode
waveforms.

```
WAVETBL mytable
P1NS a11
0 "{d:1:0 d2:0 r1:H} {d3:0 d4:0 r3:H} {d5:0 d6:0 r5:H}" drv0-3
1 "{d1:1 d2:0 r1:H} {d3:1 d4:0 r3:H} {d5:1 d6:0 rS:H}" drv1-3
2 "{d1:0 d2:0 r1:H} {d3:0 d4:0 r3:H} {d5:0 d6:0 r5:H} {d7:0 d8:0 r7:H}" drv0-4
3 "{d1:1 d2:0 r1:H} {d3:1 d4:0 r3:H} {d5:1 d6:0 r5:H} {d7:1 d8:0 r7:H}" drv1-4
4 "{d1:0 r1:H} {d2:0 r2:H} {d3:0 r3:H} {d4:0 r4:H} {d5:0 r5:H} {d6:0 r6:H} {d7:0 r7:H} {d8:0 r8:H}" drv0-8
5 "{d1:1 r1:H} {d2:1 r2:H} {d3:1 r3:H} {d4:1 r4:H} {d5:1 r5:H} {d6:1 r6:H} {d7:1 r7:H} {d8:1 r8:H}" drv1-8
6 "d1:FOO" drv0
7 "d1:F10" drv1
STATEMAP
#physSeq statechars x-mode se1ector
0 000 x3
1 111 x3
2 0000 x4
3 1111 x4
4 00000000 x8
5 11111111 x8
6,6,6,6 0 x1/4
7,7,7,7 1 x1/4
6{8} 0 x1/8
7{8} 1 x1/8
6{16} 0 x1/16
7{16} 1 x1/16
```

The
first six lines of above example STATEMAP section define xN waveforms and the last six lines
define x1/N waveforms.

### General

The STATEMAP section is appended after the PINS statement
containing all waveform definitions. The STATEMAP ends when a new WAVETBL or PINS keyword is
found or at end-of-file (equation setup file).

Within a single WAVETBL several PINS and
corresponding waveform definitions may be defined. All edges belonging to the same X-waveform
are enclosed in {} braces (see also
`Representing a pattern in device orientation`（raw: `106829.htm`）
). The STATEMAP may also be defined
per PINS statement.

### physSeq

Defines the sequence of physical waveforms. Each value of the
physSeq column references an existing physical waveform defined in the PINS section. Similarly,
each waveform defined in the PINS section must be represented at least once in the STATEMAP
section. That is full consistency between the waveforms defined in the PINS section and the
STATEMAP section.

The physSeq specifications must match the x-mode as follows:

xN-mode: one hex number

x1/N-mode: N hex numbers, comma separated, N ≤ 1024

When defining x1/N-mode, you can use the following syntax:

Wildcard string *

Example 1: when defining x1/4-mode: 0,A*,2 represents 0,A,A,2

Example 2: when defining x1/16-mode: 2*,F,3 represents 2,2,2,2,2,2,2,2,2,2,2,2,2,2,F,3

Repetition factor in curly braces {n}

Example: when defining x1/16-mode: 2{14},F,3
represents 2,2,2,2,2,2,2,2,2,2,2,2,2,2,F,3

### statechars

Defines the state characters displayed in the Pattern Editor.
The Pattern Editor and the Configure Layout dialog list state characters (statechars) as SC. The
state characters consist of the characters [a-z][A-Z][0][1]. The length is:

always one character for x1/N-mode and

N characters for xN-mode.

Examples:

when defining x1/8 mode: 0

when defining x8-mode: 00000000

### x-mode

Defines the x-mode. The maximum values are:

for xN-mode: x8

for 1/N-mode: x1/1024.

### selector

The selector is optional and not used in these examples.

It allows to assign the same state character to different tester waveforms (waveform
sequences) with the same x-mode. In this case the two waveforms (waveform sequences) are
uniquely identified by the selector. This is required for a unique translation of state
characters to indexes and vice versa.

### Examples（取自子主题 Creating a Digital Source setup）

### Digital Source setup of audio device

[表] Setup in the Setup Wizard
列: Create source port and new data container
行 1:
  Data Container
  New DSRC label
行 2:
  Pins
  datain
行 3:
  Matching port
  dataport
行 4:
  Offset
  0
行 5:
  Number of frames
  256
[表]
列: Create new configuration
行 1:
  Configuration
  audio_vvc
行 2:
  Type
  Serial
行 3:
  Option
  MSB first
行 4:
  Variable(width)
  VVLeft(8)
    
    VVRight(8)
行 5:
  Map "0" to
  d0
行 6:
  Map "1" to
  d1

After you finish, the Digital Source setup
audio_vcc
 appears in the
Outline view. Open it, the VVC
audio_vvc
 is shown as the
following:

```
ATTR DIGDATA #Source type

#Declaration of variables
VARIABLES VVLeft,VVRight

PINS datain
SOURCE_DATA_TEMPLATE VVLeft[7-0],VVRight[7-0]
MAPPING
0 d0
1 d1
```

According
to the frame structure, you need use semicolon in the
SOURCE_DATA_TEMPLATE

section. You can open the Digital Source setup in the Outline view and edit it as the
following:

```
SOURCE_DATA_TEMPLATE L[7-0];R[7-0]
```

The semicolon means
only the bits of frame section #2 and #4 included in the source memory, and the bits of frame
section #3 not included.

### VVC of video device

[表] Setup in the Setup Wizard
列: Create source port and new data container
行 1:
  Data Container
  New DSRC label
行 2:
  Pins
  R_In
    
    G_In
    
    B_In
行 3:
  Matching port
  dataport
行 4:
  Offset
  0
行 5:
  Number of frames
  256
[表]
列: Create new configuration
行 1:
  Configuration
  video_vvc
行 2:
  Type
  Parallel
行 3:
  Option
  MSB first
行 4:
  Variable(width)
  VV_Red(8)
    
    VV_Green(8)
    
    VV_Blue(8)
行 5:
  Map "0" to
  d0
行 6:
  Map "1" to
  d1

After you finish, the Digital Source setup
video_vcc
 appears in the
Outline view. Open it, the VVC
video_vcc
 is shown as the
following:

```
ATTR DIGDATA #Source type

#Declaration of variables
VARIABLES VV_Red,VV_Green,VV_Blue

PINS R_In
SOURCE_DATA_TEMPLATE VV_Red[7-0]
MAPPING
0 d0
1 d1

PINS G_In
SOURCE_DATA_TEMPLATE VV_Green[7-0]
MAPPING
0 d0
1 d1

PINS B_In
SOURCE_DATA_TEMPLATE VV_Blue[7-0]
MAPPING
0 d0
1 d1
```

### VVC of parallel audio device

[表] Setup in the Setup Wizard
列: Create new data container and pin configuration
行 1:
  Data Container
  Re-use DSRC label
行 2:
  Pins
  R_In
    
    G_In
    
    B_In
行 3:
  Matching port
  dataport
行 4:
  Offset
  0
行 5:
  Number of frames
  256
[表]
列: Create new configuration
行 1:
  Configuration
  p_audio_vvc
行 2:
  Type
  Custom (from Template)

If you want to use two variables, you cannot set the parameters in the Setup Wizard
and then automatically create the VVC. The reason is that the number of variables does not match
the number of source pins. You must directly enter the VVC in the editor which is launched by
clicking the
Custom (from Template)
 button on the

Type
 panel. The VVC
p_audio_vvc
 is shown as the
following:

```
ATTR DIGDATA #Source type

#Declaration of variables
VARIABLES Left_VV,Right_VV

PINS datain_7
SOURCE_DATA_TEMPLATE Left_VV[7];Right_VV[7]
MAPPING
0 d0
1 d1

PINS datain_6
SOURCE_DATA_TEMPLATE Left_VV[6];Right_VV[6]
MAPPING
0 d0
1 d1

PINS datain_5
SOURCE_DATA_TEMPLATE Left_VV[5];Right_VV[5]
MAPPING
0 d0
1 d1

PINS datain_4
SOURCE_DATA_TEMPLATE Left_VV[4];Right_VV[4]
MAPPING
0 d0
1 d1

PINS datain_3
SOURCE_DATA_TEMPLATE Left_VV[3];Right_VV[3]
MAPPING
0 d0
1 d1

PINS datain_2
SOURCE_DATA_TEMPLATE Left_VV[2];Right_VV[2]
MAPPING
0 d0
1 d1

PINS datain_1
SOURCE_DATA_TEMPLATE Left_VV[1];Right_VV[1]
MAPPING
0 d0
1 d1

PINS datain_0
SOURCE_DATA_TEMPLATE Left_VV[0];Right_VV[0]
MAPPING
0 d0
1 d1
```

<!-- 语法节 end -->

## 是什么

**文档事实** Pattern Editor 是 SmarTest 的 pattern 显示与编辑工具。文档列出三项能力：显示当前已加载 setup 的 patterns、编辑 patterns、分析错误。

**文档事实** 它有两种显示模式：expanded 模式按实际执行顺序显示 cycle，并显示失败数据；collapsed 模式不显示 sequencer 指令的动态行为。只有当前的 primary pattern（start label）能在 expanded 模式下查看。

**文档事实** 工具栏提供以下功能图标：在 collapsed/expanded 间切换；仅展开 burst 中选中的 CALL 指令（对 port burst 也适用，启用后 expanded 页面会显示 "Expand Selection Mode" 项）；在 expanded 模式围绕标记行生成失败注解；切换到水平 pattern 视图；显示失败数据时与其它结果分析工具对齐；隐藏/显示 header instructions、vectors、x-mode areas、protocols、header comments；放大/缩小；跳到下/上一个注解；后退/前进导航。多数功能在主菜单也有对应项。

**文档事实** Pattern Editor 的状态行位于 SmarTest 主窗口底部。

**文档事实** 缩小到一定程度后，缩放会把多行 vector 或 cycle 合并为一行，编号从连续（1, 2, 3, 4, 5, …）变为不连续（如 1, 3, 5, … 或 1, 5, 9, …）；被隐藏行的 vector 数据（含错误信息）不再显示，需要放大才能看到。

## 典型用法

**文档事实** 常规用途是打开当前 setup 的 pattern、编辑 vector 与 sequencer 指令，并借助失败数据显示定位错误。文档的 Pattern Editor tasks 子主题覆盖打开 Pattern Editor、配置编辑器布局、编辑 pattern、插入/编辑/删除 sequencer 指令、在信号或 vector 间跳转、复制 pattern、插入/编辑注释、屏蔽与激活信号、显示失败数据、对齐显示等操作。

**文档事实** 在 expanded 模式显示失败数据时，如果已获取的失败数量很大，注解数量会受到限制；此时可先标记一行，再用工具栏按钮围绕该行生成注解。

**文档事实** 选中 vector、test point 或 vector variable 时，可在 properties view 查看属性。vector 属性视图不能编辑，修改要在 pattern editor 中进行；该视图始终显示物理波形，drive edges 与 receive edges 分两行显示。collapsed 模式基于 base wavetable，expanded 模式的属性取自 primary wavetable。

**文档事实** vector variable 的 properties view 可编辑 assigned pins、transfer mode 等参数；点 Show Advanced Properties 图标可显示额外的数据上传格式参数（Upload Parameters）。文档提醒：这里显示的 Upload Parameters 是系统上一次使用的值。

**文档事实** 在用于动态 DC 测试的 test point 属性视图中，会高亮 force 值；动态 DC measure test point 的属性视图还会显示测量结果。

**文档事实** 文档示例中的 `RPTV 3 2` 表示后续三个 vector 执行两次；在 expanded 模式下可以看到解析后的 sequencer 指令和 Cycle# 列。

## 和谁有关

**文档事实** Pattern Explorer（`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01_Pattern_Explorer.htm`）：位于本页 Related information；另一文档说明可将 Pattern Explorer 与 Pattern Editor 配合，创建、克隆、编辑和调试 patterns 与 bursts，并保存 partial patterns。

**文档事实** Multiport Burst Editor（`02.08.04.16.03`）：其主工具栏图标在很大程度上与 Pattern Editor 相同（包括红色单元格着色和失败数据图标），另有附加图标；Pattern Editor 中也有针对 burst/port burst 的「仅展开选中 CALL 指令」按钮。

**文档事实** Pattern Editor tasks 系列子主题（`02.08.04.16.02.06.*`）：打开、布局、编辑、跳转、失败数据、对齐、屏蔽信号等操作的具体步骤在这些页面中。

**文档事实** STATEMAP 段（本页子主题 STATEMAP section of the wavetable）：`statechars` 定义的就是 Pattern Editor 中显示的状态字符，Pattern Editor 与 Configure Layout 对话框把状态字符列为 SC；字符集为 `[a-z][A-Z][0][1]`，x1/N 模式长度恒为 1，xN 模式长度为 N。

**文档事实** Creating a Digital Capture setup（`02_System_reference/02.08_Setup_and_Result_Tools/02.08.01.02.07.02.05.01_Creating_a_Digital_Capture_setup.htm`）：vector variable 参数的定义参见该页。

**文档事实** Signal Analyzer：`Functional changes` 记载 SmarTest 7.0.3 新增了用 Signal Analyzer 编辑 vector 的快捷菜单。

**文档事实** Editor status line（`02.08.04.16.04.02`）：编辑器状态行页面被列为本页相关主题，用于说明 Pattern Editor 底部状态行的内容。

## 版本

**文档事实** `Functional changes` 记载：Introduced before SmarTest 6.3.2；SmarTest 7.0.3 新增用 Signal Analyzer 编辑 vector 的快捷菜单；SmarTest 7.1.3 增强编辑器数据表的控制；SmarTest 7.5.1 起，测试程序重跑后保持已打开 Pattern Editor 的位置。

## 出处

- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02_Pattern_Editor.htm`（主源：能力列表、工具栏、缩放、Related information、Functional changes）
