---
type: object
title: Software bin summary tab
layer: gui
stage: results
tags: []
related: []
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02.05_Software_bin_summary_tab.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Software bin summary tab

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **76 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02.05_Software_bin_summary_tab.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example

Depending on your preference settings, the bin summary could look like this:

<!-- 语法节 end -->

## 是什么

**文档事实** Software bin summary tab 是 data store 的 summary view 中的一个 tab，汇总该 data store 中所有 software bin 的结果，并为每个 bin 显示基本统计评估。

**文档事实** 除描述各 bin 的列之外，该 tab 还带一个 shortcut menu。

**文档事实** 表格每行对应一个 bin 的汇总；点击某行任一字段会选中整行（例如用于复制）。表格最顶行（青色背景）是 table filter，可输入条件限制表中显示的行。

**文档事实** 可显示的列有：`SW Bin`（software bin 编号）、`Desc`（software bin 的描述串，若已指定）、`Site`（被测 site 编号，仅当 hardware bin summary 按 site 分组时显示）、`Site%`（该 site 中落入此 bin 的器件百分比，同样仅在按 site 分组时显示）、`Device#`（落入此 bin 的器件数）、`Bin%`（该 bin 器件数除以被测器件总数，并以水平蓝条在单元格中图示）、`Good Bin`（good bin 记 Y、否则 N）、`Reprobe Bin`（reprobe bin 记 Y、否则 N）。

**文档事实** 显示哪些列及其顺序在 preferences（SW Bin Summary preference settings）中设置。

**文档事实** 若该 tab 属于 correlation view，会额外显示列；细节见 Correlation data store structure。

**文档事实** 点击列标题按该列升序排序（以三角标记），再点按降序排序（以倒三角标记），再点取消排序（恢复 data store 中的顺序）。

## 典型用法

**文档事实** 用顶行 table filter 输入条件限制显示的行；选中某 bin 后用快捷菜单 `Filter > Show Similar`，等价于把该 bin 的 software bin 编号填入 table filter；要恢复显示全部行，点击 table filter 行最左侧以清除所有过滤。

**文档事实** 快捷菜单包含：`Refresh`、`Pause`、`Resume`、`Clear`、`Save and Clear`（这几个仅在 tab 显示 system data log stream 时可用）；`Exclude`（子项 `Selection` / `Other` / `None`）；`Filter > Show Similar`；`Width > Autofit`；`Group By > Site`；`Copy`（把选中行以 tab 分隔文本复制到剪贴板）；`Alerts`（打开 Alerts preference page）；`Preferences`（打开 SW Bin Summary preference page）。

**文档事实** `Group By > Site` 让汇总按 site 分组：不再是每个 bin 一行，而是每个 bin 的每个 site 一行，并显示 `Site` 列；若已按 site 分组，再次选择该项会取消分组。

**文档事实** 文档在描述快捷菜单时写的是 "The shortcut menu of a hardware bin summary tab"，与本节主题 software bin summary tab 的命名不一致（原文如此）。

**建议** 需要按 site 细分结果时用 `Group By > Site`，但 `Site` 与 `Site%` 两列的显示受 hardware bin summary 是否按 site 分组决定，使用前先确认该分组状态。

## 和谁有关

- **文档事实** `[[data-navigation-views]]` — 该页把 Software bin summary tab 列为 data navigation view 之一，并说明按 site 分组也可从该 tab 的快捷菜单使用（此类视图中工具栏按钮被禁用）。
- **文档事实** `[[table-filter]]` — 顶行 table filter 的详细说明见该页。
- **文档事实** SW Bin Summary preference settings（`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.05.19_SW_Bin_Summary_preference_settings.htm`）— 配置 software bin summary tab 显示哪些列及顺序；本页 Related information 也指向它。
- **文档事实** Software Bin Correlation preference settings（`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.05.17_Software_Bin_Correlation_preference_settings.htm`）— 配置显示相关数据 store 的 software bin summary tab 的列，并指向本页作为列说明。
- **文档事实** Correlation data store structure（`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.02.02.04.01_Correlation_data_store_structure.htm`）— 说明 correlation view 中额外的列。
- **文档事实** Separating summary results by wafer, site, or pin（`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.02.03.05_Separating_summary_results_by_wafer__site__or_pin.htm`）— 该页把 SW Bin Summary 列为可按 site 分割的汇总。
- **文档事实** `[[hardware-bin-summary-tab]]` — `Site` 与 `Site%` 列的显示条件取决于 hardware bin summary 是否按 site 分组。
- **文档事实** Alerts preference page（`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.05.01_Alerts_preference_settings.htm`）— 快捷菜单 `Alerts` 打开该页。

## 版本

**文档事实** Functional changes 记载 Introduced in SmarTest 7.2.0。SmarTest 7.2.1 重命名了部分列。SmarTest 7.2.2 新增若干快捷菜单命令。

## 出处

- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02.05_Software_bin_summary_tab.htm`，主源，含 tab 用途、Table 列说明、Shortcut menu、Example、Related information 与 Functional changes。
