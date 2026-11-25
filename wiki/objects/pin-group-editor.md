---
type: object
title: Pin group editor
layer: gui
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.02_Pin_group_editor.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Pin group editor

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

**没有加标记的语法段。** 定义文档里没有 `Syntax` / `Parameters` / `Example`
这类**段标记**。本脚本一个字都不收录——没有段标记时「哪一段是语法」是猜，
而猜就是编。要看原文：`python show.py <分类号>`。

<!-- 语法节 end -->

## 是什么

**文档事实** Pin group editor 用于为 group 选择成员。

**文档事实** 文档把 group 分为两类，建立方式不同：fixed group 与 expression-based group。

**文档事实** Fixed group 是基本 group，成员只包含 digital pin 与 pin alias。

**文档事实** Expression-based group 的成员可以是 digital pin、pin alias 和/或其他 group（digital fixed 或 expression-based），并支持 group arithmetic；group expression 求值后得到 group 实际包含的 pin，文档给出的表达式例子是 `(group1 + pin1 + pin4 + group3) * group2`。

**文档事实** 支持的 group 运算：UNION（`+`）、DIFFERENCE（`-`）、INTERSECTION（`*`）以及嵌套 expression。

**文档事实** Component Type 列表决定 group 中 active pin 的类型（I、O、IO、DC）。非所选类型的 pin 会作为 inactive member 插入；文档给出的理由是：若另一 group 以本 group 为定义成员且 component type 不同，这些 pin 必须先存在于本 group 中才能被激活。

**文档事实** Available Group/Pin List 中用 `√` 标记已加入 group 的 pin；Type 列标识 pin 类型（I、O、IO）与 group 类型（D 为 digital fixed group，E 为 expression-based group）；Group Members 区的 Type 列中用 `*` 标记类型与 Component Type 不同的 inactive member。

## 典型用法

**文档事实** 选择成员：在 Available Pin List 中把 pin 加入 group，pin 名前的 `√` 表示已加入。

**文档事实** 定义 expression-based group：用 pin、pin alias 与其他 group 组成 group expression，例如 `(group1 + pin1 + pin4 + group3) * group2`，由求值结果得到实际 pin。

**文档事实** 在 Component Type 列表中选择 I、O、IO 或 DC，决定哪些 pin 作为 active member 进入 Group Members 区，其余作为 inactive member。

**建议** 建组前先读子主题 Rules for defining groups 与 Incompatible pin groups：前者给出 fixed group 上限 2400、全部 group 的 pin 总数上限 1,228,800、新 group 不得与已有 digital pin/digital group 重名；后者列出在 Timing/Level/Vector setup 窗口中会导致不兼容的 pin 组合。

## 和谁有关

- **文档事实** `[[pin-configuration-tool]]` — Elements of the Pin Configuration Tool 把 Pin group editor 与 Pin setting editors、Port Editor、Alias Set Editor、各 DC Scale editor、Ground sense editor、Protocol assignments 等并列为该工具的组成部分。
- **文档事实** Pin group（`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.01.02_Pin_group.htm`）— 该页说明可以把 pin 分组并像单个 pin 一样处理，本页 Related information 指向 Pin group；Pin group 页也链回 Pin group editor。
- **文档事实** Editing a fixed group（`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.02.08.02_Editing_a_fixed_group.htm`）与 Editing an expression-based group（`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.02.08.03_Editing_an_expression-based_group.htm`）— 两个操作页都指向本编辑器。
- **文档事实** Rules for defining groups（`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.02.01_Rules_for_defining_groups.htm`）— 本页子主题，规定 fixed group 数与全部 group 的 pin 数上限、以及新 group 不得与已有 digital pin/digital group 重名。
- **文档事实** Incompatible pin groups（`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.02.02_Incompatible_pin_groups.htm`）— 本页子主题，说明在 Timing、Level、Vector setup 窗口中会导致不兼容的 pin 组合。
- **文档事实** Editors（SmarTest Work Center，`01_Getting_started/01.01_SmarTest_Work_Center/01.01.09_Editors.htm`）— 该页的编辑器清单中有一项链接到本页（文字为 Group Editor）。
- **文档事实** `[[port-editor]]`、`[[alias-set-editor]]` — 二者与本编辑器同列在 Elements of the Pin Configuration Tool 的成员清单中。

## 版本

**文档事实** Functional changes 记载 `Introduced before SmarTest 6.3.2`（哨兵值，表示在文档集覆盖范围开始前就已存在）；`SmarTest 6.5.3: When a pin group is created, the pin alias can be added as a group member`。

## 出处

- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.02_Pin_group_editor.htm`，主源，含两类 group、group 运算、Component Type、列表标记、Related information 与 Functional changes。
- 关系与用法佐证另读子主题 `02.08.04.18.03.02.01_Rules_for_defining_groups.htm`、`02.08.04.18.03.02.02_Incompatible_pin_groups.htm` 与 `02.08.04.18.01.02_Pin_group.htm`。
