---
type: object
title: Setup perspective
layer: gui
stage: project
tags: []
related: []
sources:
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02_Setup_perspective.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Setup perspective

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **2,078 字符逐字取自** `<01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02_Setup_perspective.htm>` 及其子主题 `<01_Getting_started/01.01_SmarTest_Work_Center/01.01.08.08_Firmware_view.htm>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.03_Pattern_editor_properties_view.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

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

### Example（取自子主题 Firmware view）

As the following example shows, the
VECD?
 query returns vector data
from the sequencer memory in the range between 0 and 8, for the S0_1 pin.

Add the
$
 prefix to the query command to retrieve the binary data in a
readable format.

<!-- 语法节 end -->

## 是什么

**文档事实** Setup perspective 是默认 perspective，SmarTest 首次启动时即处于激活状态；它包含编辑 SmarTest setup 数据所需的视图。

**文档事实** 该 perspective 包含下列视图：Test Program Explorer（层级显示全部测试数据的逻辑结构，并从此启动编辑 device setup 数据的全部工具）、Project Explorer（以树形显示 test method projects 与 classes，可新建项目与类）、Properties（显示当前高亮对象的属性，如 test method project 的位置与修改日期）、Outline（显示编辑器所打开文件的大纲，内容随当前编辑器而定）、Help view（基于 TDC Viewer，可用 Shift+F1 显示上下文帮助，也可经 Help > Help Content 打开 TDC Viewer）、Problems View（以列表显示错误/警告及其位置，双击错误跳到编辑器对应行）、Firmware view（可执行 firmware 命令）、Console view（显示与特定测试系统资源相关的错误）、Error Log View（显示来自测试系统与 Eclipse 插件的全部错误）。

**文档事实** 关于可用 perspective 及如何自定义，文档指向 Perspectives 页。

## 典型用法

**文档事实** 首次启动 SmarTest 默认打开 Setup perspective，用它编辑 setup 数据。

**文档事实** 在 Test Program Explorer 中双击 setup 组件即可打开对应工具（Test Program Explorer 页示例：双击 Pin Configuration 打开 Pin Configuration Tool）。

**文档事实** 在 Problems View 双击错误，光标会移到编辑器中出错的行。

**文档事实** 需要帮助时按 Shift+F1 获取上下文帮助，或经 Help > Help Content 打开 TDC Viewer。

**文档事实** Firmware view 可用来执行 firmware 命令；自 SmarTest 6.5.2 起该视图默认可见。

**推断** 若要调整视图布局或切换到其他 perspective，应按文档指引阅读 Perspectives 与 Working with a perspective（本页未给出具体步骤）。

## 和谁有关

- **文档事实** Perspectives — 该页把 Setup perspective 与 C/C++、Debug、Hardware perspective 并列列出，是理解本页在 perspective 体系中位置的上层页。
- **文档事实** Working with a perspective — 说明 93000 setup perspective 含有编辑 setup 数据所需的视图，并回链本页作详情。
- **文档事实** Opening a perspective — 记载首次启动 SmarTest 时默认打开 93000 Setup perspective。
- **文档事实** Test Program Explorer — 明确写明它包含于 Setup perspective，提供测试 setup 数据的层级视图并从此启动 device setup 工具（两页互相引用）。
- **文档事实** Project Explorer view — 说明它是 Setup perspective 的一部分，以层级视图展示 device 目录。
- **文档事实** Error Log View、Console view: System console、Console view: Data log console — 均声明属于 Setup perspective；Error Log 显示测试系统与 Eclipse 插件的错误，System console 显示与特定测试系统资源相关的错误。
- **文档事实** Firmware view — 说明可在 Setup perspective 上执行 firmware 命令；本页语法节逐字收录了它的 VECD? 示例。
- **文档事实** Debug View — 说明可使用 Setup perspective 主工具栏上对应的调试按钮。
- **文档事实** Site Select view — 说明该视图默认包含在 Setup、Debug、C/C++、Hardware 等主要 perspective 中。
- **文档事实** Device Technology Defaults — 本页子主题，引用 Setup perspective。
- **文档事实** Loading a data logging profile、Unloading a data logging profile — 说明可从属于 Setup perspective 的 Test Program Explorer 加载/卸载 data logging profile。

## 版本

**文档事实** Functional changes 记载：Introduced before SmarTest 6.3.2；SmarTest 6.5.2：Firmware view 默认可见。

## 出处

- `01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02_Setup_perspective.htm`，主源，含视图列表、Related information 与 Functional changes。
- 语法节子主题 `01_Getting_started/01.01_SmarTest_Work_Center/01.01.08.08_Firmware_view.htm`。
- 语法节子主题 `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.03_Pattern_editor_properties_view.htm`。
