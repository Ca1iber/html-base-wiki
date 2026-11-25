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

**文档事实**：Spec Tool 章节更详细地说明如何使用 Spec Tool：介绍其功能，并解释日常任务。

**文档事实**：可从 Level Setup tool 的 Select > Edit Specifications 打开 Spec Tool，也可通过 <93000> <Setup> <Spec Tool> 打开；若出现 Select specification 窗口，在其中点击 done。

**文档事实**：Spec Tool 主窗口顶部是 shortcut icons；refresh 按钮按当前 test suite 刷新所显示的 specification——执行某个 test suite 后点击 refresh，该 test suite 所用 primary sets 对应的 specification 会显示在 Spec Tool 中。

**文档事实**：shortcut icons 下方显示 Timing Setup 中当前的 Specification 与 Equation Sets，再下一行显示该 spec set 关联的 wavetable。中部区域（需从 Code 下拉菜单激活 Show Timing Info）用于选择 edge order checks 以及其中 drive/receive periods 的数量。

**文档事实**：最下方表格显示 spec set 中的变量，可定义其初始值以及 min/max sweep range 值；用 measure 按钮做实际测量时，测量值也会显示。

**文档事实**：可同时打开多个 Spec Tool 窗口，以便（必要时）同时显示 timing 与 level specifications。

**文档事实**：Timing Set 与 Wavetable 实体可直接编辑：点击相应编辑框，输入新值后按 return；可输入最多 9 位小数，输入后显示最接近的匹配实体。中部 timing/edge check 信息通过相应 radio button 修改。

**文档事实**：底部变量表中，除变量名和单位外都可编辑（变量名与单位自动从 equation file 取回）；编辑某个值（actual、min、max 等）时双击相应字段，双击现有值，输入新值后按 return。单位只能在该 equation based spec setup 中定义，不能用 Spec Tool 定义。

**文档事实**：与 Level setup tool 不同，Spec Tool 不会自动更新 hardware frontend。Spec Tool UI 的 download 会改变 backend hardware 中的 levels 或 DPS sets，但不改变 frontend state；要应用到 frontend，需先按 download 按钮把修改下载到 backend，再激活 primaries：用 SmarTest Eclipse 窗口 shortcut bar 的 Connect/disconnect 按钮做 global disconnect/connect，或用 Hardware view 对单个 channel 做 disconnect/connect，或在 Firmware view 调用 FW 命令 APRM。

**文档事实**：若加载的 SPECSET 单位与所引用 EQNSET 定义的单位不同，SmarTest 显示 warning；此情形只使用 EQNSET 单位。按 warning 的指引，可 Download 后再 File > Save 用 EQNSET 单位覆盖 SPECSET 单位，或编辑 EQNSET 使其单位与 SPECSET 相同以保留 SPECSET 单位。

## 典型用法

**文档事实**：不使用变量的创建流程（Example 1）：Level Setup tool 中 Select > Edit Specifications（或 <93000> <Setup> <Spec Tool>）→ Select specification 窗口点 done → Change > Create Specification → 在 Eqn Description 区域选择 equation set 1 NonSpecs → create → Create level spec set 窗口的 Unused Numbers 选 1（该行变红）→ Description 输入 nospecs → Create → Select level equation set 窗口点 done → Levels 行显示 "modified, download required" → 点击 Download（Spec Tool 的下箭头图标）→ 在 Test Program Explorer 保存 levels 文件。

**文档事实**：使用变量的创建流程（Example 1, using a variable）：Level Setup 窗口 Select > Edit Specifications 打开 Spec Tool → Change > Create Specification → 选择 Equation Set 2 specs → create → Create level spec set 窗口选 1（定义一个指向 spec set 1 的 specification）→ Description 输入 Vcc = 4.5V → create → Select level equation set 窗口点 done → SpecTool Name 列显示该 spec set 的变量名 → 对每个 spec variable 重复该过程 → 点击 Download 图标并检查 Report window 是否有错误 → 在 Test Program Explorer 右键 level 文件并 Save。

**文档事实**：日常编辑可在底部变量表双击 actual/min/max 字段修改值并按 return；Download 后还需按上述方式 disconnect/connect 或调用 APRM，修改才会作用到 hardware frontend。

**文档事实**：Spec Tool 的通用编辑功能还包括：创建、复制、删除 specification set；修改 description；把 spec set 指派到另一个 equation set；修改 spec set 编号；修改 compatibility options；把 spec set 指派到另一个 wavetable；修改版本头与 header；修改 check options；添加/删除 spec variable；修改 spec values；从不同 specification set 复制 spec values；设置 multiport timing specification；执行 measurement；以及在 Timing/Level Setup 窗口修改 equation 设置后恢复。

## 和谁有关

**文档事实**：以下关系均有本页正文、子主题或回链证据支撑。

- [[level-setup-tool]]：Spec Tool 可从 Level Setup tool 的 Select > Edit Specifications 打开；本页还直接把它与 Level setup tool 比较，说明 Spec Tool 不自动更新 hardware frontend。
- [[timing-setup-tool]]：Spec Tool 窗口显示 Timing Setup 中的当前 Specification、Equation Sets 与关联 wavetable，并可编辑 timing 相关设置。
- [[aprm]]：本页说明把修改应用到 frontend 可在 Firmware view 调用 FW 命令 APRM 激活 primaries。
- [[spec-set]]：Spec sets 文档回链说明，创建 spec set 并指定或修改其值要使用 Spec Tool；本页的创建/复制/删除 specification sets 与修改 spec values 正对应此职责。
- [[report-window]]：本页示例要求点击 Download 后检查 Report window 是否有错误。
- `The Spec Tool window`、`General Editing Features of the Spec Tool`（本页子主题）：前者说明窗口布局与 measure 按钮，后者列出创建、复制、删除、指派 spec set 及修改 spec values 等日常编辑功能。

## 版本

**文档事实**：本页 Functional changes 仅记载 Introduced before SmarTest 6.3.2——这是哨兵值，表示文档集覆盖范围之前已有，不能理解为 6.3.2 的新增或变更。

**文档事实**：子主题 The Spec Tool window、General Editing Features of the Spec Tool 的 Functional changes 也仅有同一哨兵值；本页未记载后续版本变更，后续变更文档未覆盖。

## 出处

- 主源：`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.30_Spec_Tool.htm`（正文、Functional changes）。
- 子主题：`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.30.01_The_Spec_Tool_window.htm`（窗口布局、shortcut icons、变量表、measure 按钮、多窗口）。
- 子主题：`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.30.02_General_Editing_Features_of_the_Spec_Tool.htm`（Editable sections、Update between software and hardware、Unit conflict between EQNSET and SPECSET、通用编辑功能列表）。
- 子主题：`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.30.02.01_Creating_new_specification_sets.htm`（「语法 / 参数」逐字来源）。
