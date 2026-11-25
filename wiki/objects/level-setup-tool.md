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

（待补）

## 典型用法

（待补）

## 和谁有关

（待补）

## 版本

（待补）

## 出处

（待补）
