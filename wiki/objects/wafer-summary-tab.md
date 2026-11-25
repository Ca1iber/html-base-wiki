---
type: object
title: Wafer summary tab
layer: gui
stage: results
tags: []
related: []
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02.02_Wafer_summary_tab.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Wafer summary tab

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **0 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02.02_Wafer_summary_tab.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example



<!-- 语法节 end -->

## 是什么

**文档事实**：Wafer summary tab 是 data store 的 summary view 中按 wafer 汇总的标签页，显示 data store 内所有测试按 wafer 合并的结果，并给出每个 wafer 的基础统计评估。

**文档事实**：表格每行汇总某个 wafer 的全部测试执行；点击行内任一字段会选中整行（例如用于复制）。表格最上面一行（青色背景）是 table filter，可输入条件限制显示的行。

**文档事实**：可显示的列有：`Wafer`（wafer 编号，由 Integrated Result Tool 自动分配，不可取消选择、始终可见）、`Wafer ID`（来自 data log 的 wafer ID）、`Device#`（该 wafer 上测过的 die 数）、`Pass#`（pass 的器件数）、`Pass%`（pass 百分比，单元格内以绿色横条图形表示）、`Fail#`（fail 的器件数）、`Fail%`（fail 百分比，以红色横条表示）、`Time`（该 wafer 所有测试执行时间之和；因算法开销可能不等于实际执行时间）。显示哪些列及列顺序在 preferences 中设置。

**文档事实**：标签页左右边距是 annotation ruler 与 overview ruler：左侧用图标标出有 fail 的行、含 alert 单元格的行、以及两者都有的行；右侧为每个含失败器件或 alert 的行显示彩色小矩形，点击矩形可选中对应行，悬停可看 alert 的原因，悬停视图右上角小方块可看失败行与 alert 行的总数。颜色与启用/禁用可在 Annotations preference page 设置；默认 alert 为黄色、fail 为红色，两类均启用。

**文档事实**：快捷菜单包含：`Refresh`、`Pause`、`Resume`、`Clear`、`Save and Clear`（这五项仅在标签页显示 system data log stream 时可用；`Save and Clear` 可把当前 system event stream 保存为 EDL 文件后清空显示）、`Show In`（把所选行显示为 bin wafer map）、`Auto Update Wafer Chart`（切换 data log stream 图表是否随新条目动态更新，默认关闭）、`Exclude`（`Selection` / `Other` / `None`，从 data store 评估中排除记录，且在其他标签页同样生效）、`Width > Autofit`、`Copy`（以 tab 分隔文本复制选中行）、`Alerts`、`Preferences`。

## 典型用法

**文档事实**：在顶部 table filter 行输入条件，限制表格显示哪些 wafer 行（详见 Table filter）。

**文档事实**：点击列标题按该列升序排序（小值在前），再次点击降序，第三次点击取消排序并恢复 data store 中的出现顺序。

**文档事实**：选中若干行后，用快捷菜单 `Show In > Bin Wafer Map` 打开 bin wafer map；用 `Exclude` 子菜单（`Selection` 排除所选行对应的测试、`Other` 排除所选行以外的所有测试、`None` 结束当前排除）控制哪些记录参与 data store 评估。

**文档事实**：`Copy` 把所选行以 tab 分隔文本复制到剪贴板；`Width > Autofit` 使各列宽度刚好容纳内容。

**建议**：这是结果查看 GUI，文档没有给出与之对应的编程接口；自动化需求应另找文档覆盖的机制。

## 和谁有关

**文档事实**：以下关系均由来源文档的正文、同章列表或回链证据支撑。

- [[data-navigation-views]]：把 Wafer summary tab 列为 summary view 的标签页之一，并说明 correlation data store 不提供 Wafer summary（回链证据）。
- [[table-filter]]：本页明确顶部青色行是 table filter，具体用法指向该页。
- [[integrated-result-tool]]：`Wafer` 编号由 Integrated Result Tool 自动分配；`Clear` / `Save and Clear` 作用于该工具的 system data log stream 显示。
- [[test-summary-tab]]、[[device-summary-tab]]、[[software-bin-summary-tab]]、[[hardware-bin-summary-tab]]：同一 summary view 的其他汇总标签页（同章与回链证据），其中 hardware bin summary tab 也回链本页。
- `Bin wafer map`（`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.04.11_Bin_wafer_map_view.htm`）：`Show In` 子菜单用它显示所选行；该页说明其信息类别与 wafer summary tab 的列相同（回链证据）。
- `Wafer Summary preference settings`（`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.05.23_Wafer_Summary_preference_settings.htm`）、`Annotations preference settings`（`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.05.02_Annotations_preference_settings.htm`）、`Alerts preference settings`（`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.05.01_Alerts_preference_settings.htm`）、`Highlighting specific data`（`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.02.03.03_Highlighting_specific_data.htm`）：分别设置本页的列、标注图标与颜色、Alerts 及 fail/alert 高亮（本页正文直接指向）。
- `Specific analysis`（`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.02.04.06_Specific_analysis.htm`）：回链称也可在 wafer summary tabs 或 device summary tabs 中查看 `T$` 列；本页列清单未列出 `T$`，照原样记录该差异。

## 版本

**文档事实**：`Functional changes` 记录：Introduced in SmarTest 7.2.0；SmarTest 7.2.1 重命名部分列；SmarTest 7.2.2 增加若干快捷菜单命令；SmarTest 7.2.3 增加用于启用/禁用 system data log stream 图表动态更新的快捷菜单命令。

## 出处

- 主源（「语法 / 参数」与正文、Functional changes 的来源）：`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02.02_Wafer_summary_tab.htm`。
- 回链证据：`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02_Data_navigation_views.htm`、`02.08.04.13.03.05.23_Wafer_Summary_preference_settings.htm`、`02.08.04.13.03.04.11_Bin_wafer_map_view.htm`、`02.08.04.13.03.02.04_Hardware_bin_summary_tab.htm`、`02.08.04.13.02.04.06_Specific_analysis.htm`。
