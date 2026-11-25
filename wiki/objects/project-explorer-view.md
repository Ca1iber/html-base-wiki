---
type: object
title: Project Explorer view
layer: gui
stage: project
tags: []
related: []
sources:
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.08.02_Project_Explorer_view.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Project Explorer view

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **2,078 字符逐字取自** `<01_Getting_started/01.01_SmarTest_Work_Center/01.01.08.02_Project_Explorer_view.htm>` 及其子主题 `<01_Getting_started/01.01_SmarTest_Work_Center/01.01.08.08_Firmware_view.htm>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.03_Pattern_editor_properties_view.htm>`。**不是转述。**
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

**文档事实** Project Explorer 视图是 Setup perspective 的一部分，提供 device directory 的层级视图。

**文档事实** 在该视图中可以添加（导入）或移除 workspace 中的 device，并激活当前正在处理的 device。

**文档事实** 文档列出可在视图中完成的操作：导航到 test method project 的元素；在 editor 视图中打开并编辑 class source file；创建新 project 与 class source file；管理已有 project、class source file 和 method（剪切、粘贴、删除、移动、重命名）；编译 source 以构建 test method shared library；导入或移除外部 test method project。

**文档事实** 右键视图中的文件会打开快捷菜单，可执行复制、移动、新建文件和文件比较等操作。

**文档事实** 视图工具栏含三个图标：折叠所有文件树；切换视图选择是否与 active editor 联动（选中时，切换 active editor 会自动把视图选择更新为正在编辑的资源）；提供排序/过滤文件以及创建、选择 working set 的菜单项。

**文档事实** 本页的四个子主题是 Working with Project Explorer view、Working Sets、Device Directories、SmarTest lock mechanism。

## 典型用法

**文档事实** 导入 device 到 workspace、从 workspace 移除 device、切换 device：分别见 Working with Project Explorer view 下的子主题。

**文档事实** 直接编辑 setup file：见 Editing a Setup File Directly；其做法是在 Project Explorer 视图中打开 device directory。

**文档事实** 创建 working set：见 Creating a Working Set；working set 与排序、过滤入口在工具栏第三个图标的菜单中。

**建议** 希望视图选中项跟随当前编辑的资源时，启用工具栏中「与 active editor 联动」的切换图标。

## 和谁有关

- **文档事实** `[[setup-perspective]]` — 本页写明 Project Explorer 视图是 Setup perspective 的一部分；Setup perspective 页把它描述为以树形显示 test method project 与 class、便于导航到程序代码、并可在其中新建 project 和 class 的视图。
- **文档事实** Views（`01_Getting_started/01.01_SmarTest_Work_Center/01.01.08_Views.htm`）— 本页 Related information 列出 Views；Views 页称 view 支持 editor，并把 Project Explorer 作为显示所处理 device 及其 setup data 的视图举例。
- **文档事实** `[[debug-perspective]]` — Debug perspective 页也列出 Project Explorer，说明它显示当前 workspace 中的 test method project 与 device，并支持新建 project 和 class。
- **文档事实** C/C++ perspective（`01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.03_C_C___perspective.htm`）— 该页在同一位置列出 Project Explorer，说明它以树形显示 test method project 与 class。
- **文档事实** Editor view — 本页写明可在 editor 视图中打开并编辑 class source file，且工具栏可让视图选择跟随 active editor。
- **文档事实** Device Directories（`01_Getting_started/01.01_SmarTest_Work_Center/01.01.08.02.03_Device_Directories.htm`）— 本页是 device directory 的层级视图，device 的导入、移除与激活都在此进行。
- **文档事实** Working Sets（`01_Getting_started/01.01_SmarTest_Work_Center/01.01.08.02.02_Working_Sets.htm`）与 SmarTest lock mechanism（`01_Getting_started/01.01_SmarTest_Work_Center/01.01.08.02.04_SmarTest_lock_mechanism.htm`）— 本页的子主题。

## 版本

**文档事实** Functional changes 记载 `Introduced before SmarTest 6.3.2`（哨兵值，表示在文档集覆盖范围开始前就已存在）；`SmarTest 6.5.3: The Navigator view is renamed as Project Explorer view`。

## 出处

- `01_Getting_started/01.01_SmarTest_Work_Center/01.01.08.02_Project_Explorer_view.htm`，主源，含视图职责、可执行操作、工具栏、Related information 与 Functional changes。
- 子主题 `01.01.08.02.01_Working_with_Project_Explorer_view.htm`、`01.01.08.02.02_Working_Sets.htm`、`01.01.08.02.03_Device_Directories.htm`、`01.01.08.02.04_SmarTest_lock_mechanism.htm` 用于典型用法。
