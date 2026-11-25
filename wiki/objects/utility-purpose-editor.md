---
type: object
title: Utility Purpose Editor
layer: gui
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.01.05_Utility_Purpose_Editor.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Utility Purpose Editor

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

**文档事实**：Utility Purpose Editor 用于为一个 utility purpose 选择 utility line。文档图例中的 utility purpose `UP1` 有三个 member：`16501`、`16502`、`16508`。

**文档事实**：编辑器标题就是 utility purpose 名，最多 16 个字母数字字符；不得含空格，也不得含文档列出的字符——原文该行排版为 `# ; ('' ) ? @`，逗号另起一行。

**文档事实**：

- `Utility Lines` 区：utility line 前的 `√` 表示该 line 已加入当前 utility purpose；
- `Utility Members` 区：显示已选 utility line 以及各 site 的设置状态 `1`、`0`、`X`（Do not care）；
- `Settling Time` 文本框：设置该 utility purpose 写动作之后的等待时间（例如受该 utility purpose 控制的用户继电器 settle 时间），范围是 `0 ... 2147483.646 ms`；multi-site 测试必须对所有 site 设同一值。

**文档事实**：即使某 utility line 已经单独定义过，utility purpose 仍可包含它；同一 utility line 可以重叠地定义在多个 utility purpose 中。

## 典型用法

**文档事实**：文档描述的编辑器使用要素如下（不是逐步菜单流程）：

1. 以 utility purpose 名作编辑器标题，需满足上面的长度与字符限制；
2. 在 `Utility Lines` 区选择要加入的 utility line，已加入的 line 前显示 `√`；
3. 在 `Utility Members` 区为每个 site 设置 `1` / `0` / `X`；
4. 在 `Settling Time` 设置写动作后的等待时间，multi-site 时各 site 同值。

**文档事实**：具体的操作主题在 `Working with utility purposes`（`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.02.10_Working_with_utility_purposes.htm`）及其子页 `Editing a utility purpose`；本页正文只描述编辑器各区域的含义。

## 和谁有关

**文档事实**：以下关系均有来源文档中的正文、参数说明或回链证据支撑。

- `Pin setting editors`（`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.01_Pin_setting_editors.htm`）：该页把本编辑器列为 pin setting editor 之一。为什么：回链显示它直接引用本页，且 `SetUtilityLines` 文档说 utility line 的合法名字在 Pin setting editors 中定义、在本编辑器中配置。
- `SetUtilityLines`（`02_System_reference/02.07_Test_Method_Reference/02.07.05.04.07_SetUtilityLines.htm`）：其参数说明直接指向本编辑器配置的 utility line 名。
- [[flex-relay]]：`FLEX_RELAY` 接受 utility purpose 名或其逗号分隔列表，名字可在本编辑器中定义（回链证据）。
- `Utility purpose`（`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.01.05_Utility_purpose.htm`）、`Working with utility purposes`（`02.08.04.18.02.10`）、`Utility Purpose view`（`01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.05.06_Utility_Purpose_view.htm`）：本页 `Related information` 列出的三条。
- `Utility line control software`（`02_System_reference/02.03_DUT_board_design_reference/02.03.04.04_Utility_line_control_software.htm`）：该页说明 utility line 可连同其控制数据（0、1、Do not care）成组定义，组在本编辑器中定义（回链证据）。
- `Editors`（`01_Getting_started/01.01_SmarTest_Work_Center/01.01.09_Editors.htm`）：回链把本页列为编辑器之一。

## 版本

**文档事实**：`Functional changes` 记录：
- `Introduced before SmarTest 6.3.2`——哨兵值，表示文档集覆盖范围之前已有，不能当作 6.3.2 的变更；
- SmarTest 7.1.3：site 信息移到 `Utility Members` 区；
- SmarTest 7.1.3：state buttons 被移除；
- SmarTest 7.2.0：引入 `Utility Purpose view`；
- SmarTest 7.10.1：在 V93000 EXA Scale 系统上使用三位 utility pogo block designator。

## 出处

- 主源：`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.01.05_Utility_Purpose_Editor.htm`（正文、Related information、Functional changes）。
- 「语法 / 参数」节脚本未收录（原文没有 `Syntax` / `Parameters` / `Example` 段标记）；原文用 `python show.py 02.08.04.18.03.01.05` 查看。
- 回链证据：`02.08.04.18.03.01_Pin_setting_editors.htm`、`02.07.05.04.07_SetUtilityLines.htm`、`02.07.04.01.68_FLEX_RELAY.htm`、`02.03.04.04_Utility_line_control_software.htm`。
