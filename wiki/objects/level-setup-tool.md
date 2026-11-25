---
type: object
title: Level setup tool
layer: gui
stage: level
tags: []
related: []
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14_Level_setup_tool.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Level setup tool

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **3,912 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14_Level_setup_tool.htm>` 及其子主题 `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.04.02_Specifying_the_context_for_levels.htm>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.04.03_How_to_create_an_equation_set_using_the_Equation_editor.htm>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.04.04_Creating_new_specification_sets.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Examples（取自子主题 Specifying the context for levels）

### Context "DEFAULT"

The level equation set shown in the figure below
defines the levels for the context
DEFAULT
. Because it is a conventional level setup for

std
 pins, it is not, in fact, necessary to define any context as the DEFAULT context
will be automatically assumed when no context is defined.

This level equation set
represents a DEFAULT context, and it defines the levels for all
std
 mode pins without any

FAST
 mode pins in a single-ended configuration.

### Context "differential"

The name
differential
 is an arbitrary
context name given here to describe a differential setup but any other name except

DEFAULT
 could also be used.

The level setup for this example includes differential
pins in
FAST
 mode and a termination chosen to be
center_tap
 to set up a
differential configuration.

### Example（取自子主题 How to create an equation set using the Equation editor）

In the Test Program Explorer, double-click the
<Levels>

icon.

The Level Setup window opens.

In the Level Setup window, click on the menu

Select
 >
Edit Equations
.

The equation editor (NEdit) opens.

In the first line, type:

EQNSET 1 "NonSpecs"

Enter data for the DPS pin

Vcc
:

```
DPSPINS Vcc
vout = 4.5
ilimit = 1000
t_ms =4
offcurr = act
```

Create the level set (every level set must contain information for all pins defined in your
pin configuration)

LEVELSET 1 "nominal"

Enter information for the input
pins:

```
PINS ctrl ser_in
vil = 0
vih = 4.3
```

Enter information for the output
pins:

```
PINS ser_out
vol = 2.4
voh = 2.6
```

Enter information for the I/O
pins:

```
PINS io_pins
vil = 0
vih = 4.3
vol = 2.4
voh = 2.6
```

On the menu, click
Shell
 >
Download
to download the level to the tester hardware and make sure you correct any
reported error in the Report window.

Save your changes in the Test Program Explorer:

Right-click
<Levels...>
.

Click
Save As
.

In the Enter or select NEW file name window type the file name (for example: levels).

Click
OK
.

_Do not use the File > Save option of NEdit. In order to save your work you must
first download the changed data, and then save them from the Test Program
Explorer.

### Examples（取自子主题 Creating new specification sets）

### Example 1 (without using variables)

In the Level Setup tool, select the menu item
Select
 >
Edit Specifications
.

Alternatively you can go
<93000> <Setup> <Spec
Tool>.

If the Select specification window opens:

In the window click
done
.

You access
`The Spec Tool window`（raw: `17361.htm`）
.

On the menu, click
Change
 >
Create Specification
.

Click the equation set 1
NonSpecs
 in the
Eqn Description

area.

Click
create
.

The Create level spec set window opens.

Select "1" in the Unused Numbers area.

The line of the selected number will be highlighted
in red.

In the
Description
 field, enter
nospecs
.

Click
Create
.

In the Select level equation set window, click
done
.

In the Levels
line, the Spec Tool shows the message "modified, download required".

Click
Download
(the Down arrow icon in the Spec Tool).

Since the
specification "nospecs" has no values, no further action is required.

This level specset
is now ready to use in SmarTest.

In the Test Program Explorer save the levels file.

### Example 1 (using a variable)

From the Level Setup window select
Select
 >
Edit Specifications
. This opens the Spec Tool.

In the SpecTool, select
Change
 >
Create Specification
.

Select the Equation Set
2 specs
.

Click
create
.

You now see a window with the heading

Create level spec set
.

Select
1
.

You are defining a specification that points to spec set
1.

In the Description field, enter
Vcc = 4.5V
.

Click
create
.

Click
done
 in the Select level equation set window.

You see the
variable names for this spec set in the SpecTool Name column.

Repeat the procedure for all spec variables accordingly.

After you have defined the
specifications:

Click the Download icon (the down arrow in the SpecTool) and check the Report window for
errors.

In the Test Program Explorer right-click the level file and

Save
.

<!-- 语法节 end -->

## 是什么

**文档事实** Level setup tool 是 SmarTest 的 level 设置工具与章节，用于为器件设置 level；源页说明它提供背景信息、界面说明与任务相关信息。

**文档事实** 源页把内容组织为 Basic concepts of levels、Equation based level setup、Elements of the Level Setup window、Opening and using the Level Setup Tool、Level setup related card specifications、Level setup related use cases 等子主题。

**文档事实** Level setup 支持 context 概念：未定义 context 时自动采用 DEFAULT context，DEFAULT 适用于 std 引脚的传统 level setup；差分设置可另取 context 名（源页以 differential 为例，名称除 DEFAULT 外可任意），其中包含 FAST 模式差分引脚，并把 termination 设为 center_tap。

## 典型用法

**文档事实** 创建 level equation set 的步骤为：在 Test Program Explorer 双击 <Levels> 打开 Level Setup 窗口，选择 Select > Edit Equations 打开 equation editor（NEdit），用 EQNSET 定义 equation set，为 DPS、输入/输出/I/O 引脚写 level 设置，再执行 Shell > Download 下载到测试机并检查 Report 窗口。

**文档事实** 源页示例用 `EQNSET 1 "NonSpecs"`，为 DPS 引脚 Vcc 写 vout/ilimit/t_ms/offcurr，再用 `LEVELSET 1 "nominal"` 与 PINS 块设置输入、输出、I/O 引脚；每个 level set 必须覆盖 pin configuration 中定义的所有引脚。

**文档事实** 保存方式是在 Test Program Explorer 中右键 <Levels...> 选择 Save As 输入文件名；源页明确不要用 NEdit 的 File > Save，必须先下载修改后的数据再从 Test Program Explorer 保存。

**文档事实** 创建 specification set 可通过 Select > Edit Specifications 进入 Spec Tool（也可走 <93000> <Setup> <Spec Tool>），用 Change > Create Specification 选择 equation set、创建 level spec set 并 Download；可定义不带变量的 spec，也可定义指向 spec set 的变量（如 Vcc = 4.5V）。

## 和谁有关

- **文档事实** Basic concepts of levels、Equation based level setup、Elements of the Level Setup window、Opening and using the Level Setup Tool、Level setup related card specifications、Level setup related use cases：这些是本页的子主题，分别承载概念、方程式 level setup、窗口元素、打开与使用、卡规格与用例。
- **文档事实** Spec Tool：源页示例多次要求从 Level Setup 进入 Spec Tool（Select > Edit Specifications 或 <93000> <Setup> <Spec Tool>），并在其中创建 specification，说明两者是配套工具。
- **文档事实** Test Program Explorer：源页要求在其中双击 <Levels> 打开工具，并通过右键 Save As 保存 level 文件。
- **文档事实** Pin configuration tool 与 Timing Setup Tool：工具索引与入门流程把 Level setup tool 与这两者并列为同一套 setup 工具；源页还要求 level set 覆盖 pin configuration 中定义的所有引脚。
- **文档事实** XPS256 programming - DPS operating mode：该页说明 XPS256 在 DPS 模式下的 force/clamp 设置由 level setup 控制，访问全部特性需使用 equations，并指向 Equation based level setup 与 DPSPINS。
- **文档事实** Task 3: Setups for Digital Channels：该页把用 Level setup tool 设置电源电压、数字引脚驱动与接收条件列为数字通道 setup 的一步。
- **文档事实** Setting up sequencer control of utility lines（DUT board 与 use case 两个版本）：两者都把用 Level setup tool 设置串行接口引脚 level 列为步骤。

## 版本

**文档事实** 源页没有 Functional changes 段，版本信息「文档未覆盖」。

## 出处

- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14_Level_setup_tool.htm`，主源，含章节导语、子主题列表与文档定位。
- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.04.02_Specifying_the_context_for_levels.htm`、`...04.03_How_to_create_an_equation_set_using_the_Equation_editor.htm`、`...04.04_Creating_new_specification_sets.htm`，语法节逐字抽取来源。
