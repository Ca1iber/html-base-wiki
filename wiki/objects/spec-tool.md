---
type: object
title: Spec Tool
layer: gui
stage: level
tags: []
related: []
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.30_Spec_Tool.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Spec Tool

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,844 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.30_Spec_Tool.htm>` 及其子主题 `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.30.02.01_Creating_new_specification_sets.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

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
