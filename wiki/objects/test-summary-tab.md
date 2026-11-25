---
type: object
title: Test summary tab
layer: gui
stage: results
tags: []
related: []
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02.01_Test_summary_tab.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Test summary tab

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **0 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02.01_Test_summary_tab.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example



<!-- 语法节 end -->

## 是什么

**文档事实** test summary tab 是 data store 的 data navigation view 中的一个标签页，显示该 data store 内各 test 的汇总结果，对某个 test 的所有执行给出基本统计评估。

**文档事实** 表格每一行汇总一个 test 的所有执行结果；点击行内任一字段会选中整行（例如用于复制）。表格最顶行（青色背景）是 table filter，可输入条件限制显示哪些行。

**文档事实** 除描述各 test 的列之外，该 tab 还在左右边距提供可配置的 fail 与 alert 标记，并带有快捷菜单。

**文档事实** 表格可显示以下列：Test Suite（test suite 名）、Test Method（test method 名）、Test（由 `TESTSET.testname()` 指定的 test 名）、Test#（test number）、Type（parametric / functional / shmoo / unknown）、Pattern Name、Wafer（wafer 号）、Site（site 号）、Pin（被测引脚名）、Lower（下限）、Upper（上限）、Unit、Min（行内汇总的最低测量值）、Max（最高值）、Mean（均值）、Sdev（标准差）、Cp、Cpk、Cpl、Cpu、Device#（汇总行的被测 device 数）、Pass#、Pass%（通过百分比，单元格内以绿色横条图示）、Fail#、Fail%（失败百分比，以红色横条图示）、Time（test 执行时间）、TS Time（test suite 执行时间）。文档注明 Time 与 TS Time 因算法开销可能不是精确的实际执行时间。

**文档事实** 显示哪些列及其顺序可在 Test Summary preference 中设置。

**文档事实** 如果 test summary tab 属于 correlation view，会显示额外的列，参见 Correlation data store structure。

## 典型用法

**文档事实** 点击列标题：第一次按该列升序排序（值小的行在前，标题显示向上三角形）；再点按降序排序（倒三角）；再点取消排序，行恢复为 data store 中的原始顺序。

**文档事实** 左侧 annotation ruler 用图标标出四类行：该行汇总的 test 至少在一个 device 上失败、该行含 alert 单元格、该 test 的数据记录已在 raw data view 中被排除、该行汇总的 test 含 shmoo hole。多个图标会重叠；指向图标会显示含 fail 与 alarm 计数的 tooltip。图标类别可在 Annotations preference page 中禁用，默认全部启用。

**文档事实** 右侧 overview ruler 为每个含失败 device 的行和每个含 alert 的行显示彩色小矩形。点击矩形选中对应行；鼠标悬停显示 alert 原因；悬停视图右上角的小方块显示失败行数、含被排除数据集的行数、含 alert 的行数。颜色可在 Annotations preference page 中设置，默认 fail 为红、exclusion 为蓝、alert 为黄、shmoo hole 为青，且全部启用。

**文档事实** 快捷菜单提供以下命令：

- Refresh / Pause / Resume / Clear / Save and Clear：仅当该 tab 显示 system data log stream 时可用。Refresh 在暂停时更新为最新日志数据但不恢复自动更新；Pause 停止自动更新；Resume 恢复自动更新；Clear 清空 Integrated Result Tool 中的 system data log stream 显示并清空 system event stream；Save and Clear 先弹出标准 Save 对话框把当前 system event stream 存为 EDL 文件，然后清空日志显示和事件流。
- Open Definition：打开 Testflow Tool 并显示所选行的 test 定义，要求 SmarTest 已加载 testflow。
- Open Test Limit：打开 Testflow Tool 并显示所选行的 test limits。使用 test table 时打开 test table 并高亮相应行；不使用 test table 时打开 Tests 页面并高亮该行。
- Show In：把选中行显示为 Trend chart、Histogram、Probability chart、Box chart、Scatter chart、FFC Pareto chart、Raw data view、Shmoo plot、Scan view 或 Parametric wafer map。
- Auto Update Chart：切换显示数据日志流数据的图表是否随新日志条目动态更新；默认关闭，条目很多时性能可能受影响。该命令仅在显示 system data log stream 时可用，且不影响在 test summary tab 中切换选中行时图表视图的自动更新。
- Exclude：Pass（排除只含通过 test 的汇总）、Fail（排除至少含一个失败 test 的汇总）、None（不排除任何 test，并结束当前排除）。在此 tab 排除的记录也会在其他 tab 中排除。
- Filter：含 Show Similar，把 tab 显示限制为与所选汇总具有相同 test suite 和 test 名的行；等价于在表格顶部 filter 行填入这两个名称。点 filter 行最左侧可清除全部过滤。
- Width：含 Autofit，把每列调到刚好显示全部内容所需宽度。
- Group By：按 Wafer、Site 或 Pin 分组；分组后每个 test 按 wafer/site/pin 每组一行，并显示对应列。可同时按多个类别分组（例如每个 test 的每个 test+wafer+site 组合一行）；再次选择已分组的类别会取消该分组。
- Yield Calculator / Cpk Limit Calculator：分别打开 Yield Calculator 和 Cpk and limit calculator。
- Copy：把选中行以 tab 分隔文本复制到剪贴板。
- Alerts / Preferences：打开 Alerts preference page / Test Summary preference page。

## 和谁有关

**文档事实** Data navigation views（`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02_Data_navigation_views.htm`）：父主题把 test summary tab 与 wafer summary tab、device summary tab、hardware bin summary tab、software bin summary tab、table filter 并列。

**文档事实** Table filter（`02.08.04.13.03.02.06`）：表格顶部 filter 行的条件语法与用法在该页详述。

**文档事实** Test Summary preference settings（`02.08.04.13.03.05.21`）与 Test Correlation preference settings（`02.08.04.13.03.05.20`）：分别配置 test summary 与 correlation 场景下显示哪些列及其顺序。

**文档事实** Correlation data store structure（`02.08.04.13.02.02.04.01`）：当 tab 属于 correlation view 时，额外列的定义参见该页。

**文档事实** Yield Calculator（`02.08.04.13.03.02.01.01`）与 Cpk & Limit Calculator（`02.08.04.13.03.02.01.02`）：是本页子主题，并可分别从快捷菜单的 Yield Calculator / Cpk Limit Calculator 打开。

**文档事实** Show In 的目标视图：本页快捷菜单的 Show In 子菜单列出 Trend chart、Histogram、Probability chart、Box chart、Scatter chart、FFC Pareto chart、Raw data view、Shmoo plot、Scan view、Parametric wafer map；其中 Trend chart、Histogram、Shmoo view、Parametric wafer map、FFC Pareto chart、Scatter chart、Box chart、Probability chart、Scan view 等页面也说明可从 Test summary tab 的快捷菜单打开。

**文档事实** Testflow Tool：Open Definition 和 Open Test Limit 都需要 SmarTest 中已加载 testflow；后者在不使用 test table 时打开 Tests 页面。

**文档事实** `TESTSET.testname()`（`02.07.04.01.244.23`）：Test 列的 test 名由该函数指定。

**文档事实** Raw data view 与 Excluding data from evaluation（`02.08.04.13.02.04.02`）：annotation ruler 中「数据记录已在 raw data view 中被排除」的图标与该排除机制对应。

**文档事实** Highlighting specific data（`02.08.04.13.02.03.03`）：配置 fail 指示与 alert 的说明参见该页。

## 版本

**文档事实** `Functional changes` 记载：Introduced in SmarTest 7.2.0；SmarTest 7.2.1 起 Open Test Limit 会选择相应行、重命名了部分列、含被排除行或 shmoo hole 的 test summary 会有指示；SmarTest 7.2.2 增加 yield calculator 菜单命令、Pattern Name 列、Save and Clear 快捷菜单命令，且 Clear 命令同时清空 system event stream；SmarTest 7.2.3 增加启用/禁用 system data log stream 图表动态更新的选项；SmarTest 7.50 在 tooltip 中增加 alarm count。

## 出处

- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02.01_Test_summary_tab.htm`（主源：表格列、左右 rulers、快捷菜单、Related information、Functional changes）
