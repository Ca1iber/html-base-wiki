---
type: object
title: Device summary tab
layer: gui
stage: results
tags: []
related: []
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02.03_Device_summary_tab.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Device summary tab

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **0 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02.03_Device_summary_tab.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example



<!-- 语法节 end -->

## 是什么

**文档事实** 对 data store 的 summary view 而言，device summary tab 按 device 汇总该 data store 中所有 test 的结果，并为每个 device 给出基本统计评估。

**文档事实** 表格每一行汇总某个 device 的所有 test 执行；点击行内任意字段会选中整行（例如用于复制）。

**文档事实** 表格最上面一行（青色背景）是 table filter，可输入条件限制表格显示哪些行。

**文档事实** 文档列出的可显示列：Device（器件编号，由 Integrated Result Tool 自动分配）、Device ID（来自 data log）、Part ID（来自 data log）、Part Txt（part description text，PART_TXT）、Testflow（testflow 编号，由 Integrated Result Tool 创建，每次运行加 1）、Wafer（器件所在 wafer 号）、Site（器件所属 site 号）、P/F（器件进入 good bin 还是 bad bin）、SW Bin（test 将器件放入的软件 bin 编号）、HW Bin（test 将器件放入的硬件 bin 编号）、Time（该 device 所有 test 执行时间之和）、All Fail Bins（该 device 进入的所有软件 fail bin 的逗号分隔列表；overon 开启时一个 device 可能进入多个 fail bin）。

**文档事实** 显示哪些列及其顺序可在 Device Summary preference settings 中设置。

**文档事实** tab 左右边距含可配置的 fail 与 alert 标记：annotation ruler（左边距）用图标标记失败行、含 alert 的行、以及两者兼有的行；overview ruler（右边距）为含失败 device 或 alert 的行显示彩色小矩形，点击矩形可选中对应行，悬停显示 alert 原因，视图右上角小色块的 tooltip 显示失败行数与含 alert 行数。默认 alert 指示为黄色、fail 指示为红色，两者均启用；颜色与启用状态可在 Annotations preference page 设置。

**文档事实** 快捷菜单含 Refresh、Pause、Resume、Clear、Save and Clear、Show In、Exclude、Width（含 Autofit）、Copy、Alerts、Preferences。

## 典型用法

**文档事实** 排序：点击列标题按该列升序排序（以小三角标示），再次点击按降序（倒三角），第三次点击取消排序并恢复 data store 中的行顺序。

**文档事实** 过滤：使用表格最上面的 table filter 行输入条件。

**文档事实** 配置列：在 Device Summary preference page 设置显示的列及顺序。

**文档事实** 从 wafer map 定位：在 wafer map 中右键单元格并选 `Show in Device Summary`，会在 device summary tab 中高亮包含该 device 数据的行。

**文档事实** 排除记录：Exclude 子菜单中，Selection 排除选中行汇总的 test，Other 排除选中行以外的所有 test，None 结束当前排除；在本 tab 中排除的记录也会在其他 tab 中排除。

**文档事实** 复制与显示：Copy 把选中行以 tab 分隔文本复制到剪贴板；Show In 把选中行显示在 raw data view。

**文档事实** Refresh、Pause、Resume、Clear、Save and Clear 仅在 tab 中显示 system data log stream 时可用；Save and Clear 会把当前 system event stream 存为 EDL 文件后清空。

## 和谁有关

- **文档事实** `[[data-navigation-views]]` — 该页把 Device summary tab 与 Test summary tab、Wafer summary tab、Hardware bin summary tab、Software bin summary tab、Table filter 并列为 data navigation views，并注明 correlation data store 不提供 Device summary。
- **文档事实** `[[test-summary-tab]]`、`[[wafer-summary-tab]]`、`[[hardware-bin-summary-tab]]`、`[[software-bin-summary-tab]]` — 与 Device summary tab 同属 summary view 的兄弟 tab（由 Data navigation views 页并列表述）。
- **文档事实** `[[table-filter]]` — device summary tab 最上面一行就是 table filter，详见该页。
- **文档事实** `[[raw-data-views]]` — 快捷菜单 Show In 把选中行显示在 raw data view。
- **文档事实** `[[integrated-result-tool]]` — Device 编号由该工具自动分配；Clear 与 Save and Clear 也作用于该工具中的 system data log stream 显示。
- **文档事实** Bin wafer map view（`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.04.11_Bin_wafer_map_view.htm`）— 其 `Show in Device Summary` 命令会高亮本 tab 中包含该 device 数据的行。
- **文档事实** Device Summary preference settings（`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.05.05_Device_Summary_preference_settings.htm`）— 配置本 tab 的列与顺序；本页 Related information 也列出该页。
- **文档事实** Annotations preference settings（`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.05.02_Annotations_preference_settings.htm`）与 Alerts preference settings（`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.05.01_Alerts_preference_settings.htm`）— 分别配置 fail/alert 指示与 alert 相关设置；快捷菜单 Alerts 打开 Alerts preference page。
- **文档事实** Highlighting specific data（`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.02.03.03_Highlighting_specific_data.htm`）— 本页指向它了解 fail 指示与 alert 的更详细配置。
- **文档事实** Specific analysis（`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.02.04.06_Specific_analysis.htm`）— 该页提到可在 wafer summary tab 或 device summary tab 查看 `T$` 列。

## 版本

**文档事实** Functional changes 记载：`Introduced in SmarTest 7.2.0`；`SmarTest 7.2.1: Renamed some columns`；`SmarTest 7.2.2: Added several shortcut menu commands`；`SmarTest 7.2.3: Added Part ID and Part Txt columns`；`SmarTest 7.3.1: Added All Fail Bins column`。

## 出处

- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02.03_Device_summary_tab.htm`，主源，含 tab 定义、Table 列、边距标记、Shortcut menu、Related information 与 Functional changes。
- 关系佐证另读 Data navigation views（`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02_Data_navigation_views.htm`）与 Device Summary preference settings（`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.05.05_Device_Summary_preference_settings.htm`）。
