---
type: object
title: Displaying test results in analysis views
layer: gui
stage: results
tags: []
related: []
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.02.04.03_Displaying_test_results_in_analysis_views.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Displaying test results in analysis views

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

**文档事实** 本页说明如何把测试结果以 analysis view 显示。操作是在 data log 的 data navigation view 中选择 summary 行，再从快捷菜单的 Show In 子菜单选择视图类型。

**文档事实** 目的为把 numeric data log summaries 显示为图或表，以便发现异常或问题数据点，或纵览结果。

**文档事实** 不同视图对选择行数与来源 tab 有要求。Trend chart 需要 Test summary tab 的一个或多个行。Histogram、Probability chart、Box chart 需要一个或多个 Test summary tab 行，且所有行必须共享同一 test suite、test method 与 test。Scatter chart 需要两行且两行共享同一 device，另需满足 Scatter chart view 的附加条件。Range chart 是 scatter chart 的特殊模式，需要三行或更多行，或两行后点 scatter chart 的 Switch 按钮。FFC Pareto chart 与 Parametric wafer map 需要一行。Protocol Monitor view 需要含 Protocol 类型结果的行。Scan view 需要含 Scan 类型结果的行。Shmoo plot 需要一行汇总 shmoo 结果。Bin wafer map 需要 Wafer summary tab 的一行或多行。

**文档事实** 若所需类型的 analysis view 已打开且未被 pin，选择会自动显示到该视图。若没有未 pin 的同类型视图，需按步骤打开。

**文档事实** 同一时间可在图表中显示的行数有上限，该上限在 Result Tool preferences 中设置。

**文档事实** 图表行共享同一 test suite、test method 与 test 时，图中显示 limits。

**文档事实** Pin 按钮会中断动态更新并冻结当前数据，Link 按钮恢复更新。

**文档事实** 把 system data log stream 显示在 analysis view 时，默认不随新日志条目更新。要启用动态更新，Test summary tab 用 Auto Update Chart，Wafer summary tab 用 Auto Update Wafer Chart。这两条命令不适用于 EDL 与 STDF 数据日志。

**文档事实** 要显示为 shmoo plot 的 data log 必须由 SmarTest 7.2.0 或更高版本创建。Integrated Result Tool 无法从 SmarTest 7.1.4 或更早版本的日志生成 shmoo plot。

## 典型用法

**文档事实** 前置条件是打开 data log。然后在 data navigation view 选中目标行，右键并从 Show In 子菜单选择视图类型。

**文档事实** 对 parametric wafer map 与 shmoo plot，可在图表右键的 Accumulation 子菜单选择显示最小、平均或最大值。

**文档事实** 对 shmoo plot，可在图表右键的 Pin 子菜单选引脚，在 Result Types 子菜单选结果类型。

**文档事实** 已有一个图表时，点图表视图的 New 按钮可打开同类型的附加图表，之后在其中显示不同数据。

**文档事实** 视图默认显示最前面 data navigation view 的当前选择，选择变化时视图变化。需要固定时点 Pin。

**文档事实** 打开视图后可继续设置图表显示选项，文档把 Setting chart display options 列为下一步。

**建议** 比较两个 data log 的对应结果时，打开同类型图表并用 pin 固定，避免选择变化导致图表自动切换。

## 和谁有关

- **文档事实** Opening a data log for examination，打开 data log 是本页的前置条件。
- **文档事实** Data navigation views、Test summary tab、Wafer summary tab，选择行来自这些视图，视图类型的选择要求也按 tab 区分。
- **文档事实** Trend chart view、Histogram view、Probability chart view、Box chart view、Scatter chart view、FFC Pareto chart view、Protocol Monitor view、Shmoo view、Parametric wafer map view、Scan view、Bin wafer map view，这些页面定义 Show In 菜单可选的各类 analysis view，本页给出每类视图所需的选择行数与行来源。
- **文档事实** Shmoo graph modes，Shmoo view 页把可用的 shmoo 变体说明放在该子主题。
- **文档事实** Result Tool preferences，图表同时显示的最大行数在该偏好设置中指定。
- **文档事实** Setting chart display options，本页 What to do next 指向该页。
- **文档事实** Excluding data from evaluation 与 Working with result data tables，本页 Related information 列为相关主题。
- **文档事实** Specific analysis，该页说明按 site 分组、对两个日志的对应行打开同类型图并 pin、查看 mean 与 sigma、用 box chart 找 outlier、用 scatter chart 看测试相关性等分析做法。
- **文档事实** Separating summary results by wafer, site, or pin，该页把在 analysis view 中打开分组后的测试列为分析结果的做法。

## 版本

**文档事实** Functional changes 记载 Introduced in SmarTest 7.2.0。SmarTest 7.2.1 部分图表类型可显示多个 data series。SmarTest 7.2.2 新增 scan view。SmarTest 7.2.2 新增针对两个测试的 range chart。SmarTest 7.2.3 新增 system data log stream 图表的动态更新开关。SmarTest 7.3.2 新增 Protocol Monitor view。

## 出处

- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.02.04.03_Displaying_test_results_in_analysis_views.htm`，主源，含 About this task、Procedures、Results、Related information 与 Functional changes。
