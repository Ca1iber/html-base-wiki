---
type: object
title: Hardware bin summary tab
layer: gui
stage: results
tags: []
related: []
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02.04_Hardware_bin_summary_tab.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Hardware bin summary tab

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **0 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02.04_Hardware_bin_summary_tab.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example



<!-- 语法节 end -->

## 是什么

**文档事实**：Hardware bin summary tab 是 data store 的 summary view 中按 hardware bin 汇总的标签页，显示 data store 内所有 hardware bin 合并后的结果，并给出每个 bin 的基础统计评估。

**文档事实**：表格每行汇总一个 bin；点击行内任一字段会选中整行（例如用于复制）。表格最上面一行（青色背景）是 table filter，可输入条件限制显示的行。

**文档事实**：可显示的列有：`HW Bin`（hardware bin 号）、`Desc`（hardware bin 的描述字符串，若已指定）、`Site`（测试 site 号，仅在按 site 分组时显示）、`Site%`（该 site 中被放入此 bin 的器件百分比，仅在按 site 分组时显示）、`Device#`（放入此 bin 的器件数）、`Bin%`（放入此 bin 的器件百分比，等于 `Device#` 除以总测试器件数，单元格内以蓝色横条图形表示）。显示哪些列及列顺序在 preferences 中设置。

**文档事实**：若该 tab 属于 correlation view，会额外显示附加列（见 Correlation data store structure）。

**文档事实**：快捷菜单包含：`Refresh`、`Pause`、`Resume`、`Clear`、`Save and Clear`（这五项仅在标签页显示 system data log stream 时可用）、`Open Definition`（在 testflow 中显示所选 bin 的定义；若当前加载的 testflow 不是产生该 data log 的那个、但含同名 bin，则显示该同名 bin 的定义）、`Exclude`（`Selection` / `Other` / `None`，从 data store 评估中排除记录，且在其他标签页同样生效）、`Filter > Show Similar`、`Width > Autofit`、`Group By > Site`、`Copy`（以 tab 分隔文本复制选中行）、`Alerts`、`Preferences`。

## 典型用法

**文档事实**：点击列标题按该列升序排序（小值在前），再次点击降序，第三次点击取消排序并恢复 data store 中的出现顺序；点击行内字段选中整行。

**文档事实**：`Filter > Show Similar` 把显示限制为与所选 bin 具有相同 hardware bin 号的 bin，等价于在表格顶部 table filter 行输入该 bin 号；点击 table filter 行最左侧可清除所有过滤，重新显示全部行。

**文档事实**：`Group By > Site` 使每个 bin 按 site 显示多行，并显示 `Site` 与 `Site%` 列；若已按 site 分组，再次选择 `Group by > Site` 会取消分组。

**文档事实**：`Exclude` 子菜单（`Selection` 排除所选行对应的测试、`Other` 排除所选行以外的所有测试、`None` 结束当前排除）控制哪些记录参与 data store 评估；在本标签页排除的记录在其他标签页也被排除。

**文档事实**：`Open Definition` 在 testflow 中显示所选 bin 的定义；`Copy` 把所选行以 tab 分隔文本复制到剪贴板；`Width > Autofit` 使各列宽度刚好容纳内容。

## 和谁有关

**文档事实**：以下关系均由来源文档的正文、同章列表或回链证据支撑。

- [[data-navigation-views]]：把 Hardware bin summary tab 列为 summary view 的标签页之一，并说明其快捷菜单也支持按 site 分组（回链证据）。
- [[table-filter]]：本页明确顶部青色行是 table filter，`Show Similar` 是向该 filter 行输入 hardware bin 号的快捷方式。
- [[software-bin-summary-tab]]、[[test-summary-tab]]、[[wafer-summary-tab]]、[[device-summary-tab]]：同一 summary view 的其他汇总标签页（同章与回链证据）。
- [[bin]]：本页的 `HW Bin` 列与 `Open Definition` 命令涉及 bin 及其在 testflow 中的定义（本页正文明确写出）。
- [[integrated-result-tool]]：`Clear` / `Save and Clear` 作用于该工具的 system data log stream 显示（本页正文明确写出）。
- `HW Bin Summary preference settings`（`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.05.09_HW_Bin_Summary_preference_settings.htm`）、`Hardware Bin Correlation preference settings`（`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.05.07_Hardware_Bin_Correlation_preference_settings.htm`）：分别设置普通与 correlation view 中本标签页的列（回链证据）。
- `Correlation data store structure`（`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.02.02.04.01_Correlation_data_store_structure.htm`）：说明本页在 correlation view 中额外列的含义（本页正文直接指向）。
- `Separating summary results by wafer, site, or pin`（`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.02.03.05_Separating_summary_results_by_wafer__site__or_pin.htm`）：回链称 HW Bin Summary 的测试汇总可按 site 拆分，对应本页 `Group By > Site`（回链证据）。

## 版本

**文档事实**：`Functional changes` 记录：Introduced in SmarTest 7.2.0；SmarTest 7.2.1 重命名部分列；SmarTest 7.2.2 增加若干快捷菜单命令。

## 出处

- 主源（「语法 / 参数」与正文、Functional changes 的来源）：`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02.04_Hardware_bin_summary_tab.htm`。
- 回链证据：`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02_Data_navigation_views.htm`、`02.08.04.13.03.05.09_HW_Bin_Summary_preference_settings.htm`、`02.08.04.13.03.05.07_Hardware_Bin_Correlation_preference_settings.htm`、`02.08.04.13.02.03.05_Separating_summary_results_by_wafer__site__or_pin.htm`、`02.08.04.13.02.02.04.01_Correlation_data_store_structure.htm`。
