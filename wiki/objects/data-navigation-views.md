---
type: object
title: Data navigation views
layer: gui
stage: results
tags: []
related: []
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02_Data_navigation_views.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Data navigation views

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **5,682 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02_Data_navigation_views.htm>` 及其子主题 `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.02.02.04.01_Correlation_data_store_structure.htm>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.02.02.04_Correlating_data_logs.htm>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02.01_Test_summary_tab.htm>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02.02_Wafer_summary_tab.htm>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02.03_Device_summary_tab.htm>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02.04_Hardware_bin_summary_tab.htm>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02.05_Software_bin_summary_tab.htm>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02.06_Table_filter.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Test summary tab）



### Example（取自子主题 Wafer summary tab）



### Example（取自子主题 Device summary tab）



### Example（取自子主题 Hardware bin summary tab）



### Example（取自子主题 Software bin summary tab）

Depending on your preference settings, the bin summary could look like this:

### Syntax（取自子主题 Table filter）

In the fields of the table filter, you can enter:

Plain text (for text columns).

Only those rows are displayed where the content in the
filtered column contains the text you have entered.

Regular expression (for text columns).

Only those rows are displayed where the content in
the filtered column matches the regular expression. You can use Content Assist (Ctrl+Space) to
insert common regular expression terms.

Number (for number columns).

Only those rows are displayed where the content in the
filtered column is exactly the number you entered.

Range; two numbers separated by a ~ tilde (for number columns).

Only those rows are
displayed where the content in the filtered column is greater than the first number you
entered and less than the second number.

If you leave out one of the numbers, the range is open-ended. For example, entering

~2
 displays all row with a value smaller than 2 in the column.

Multiple numbers, separated by commas (for number columns).

Only those rows are displayed
where the content in the filtered column is exactly any of the numbers you entered. (This is
an "or" query.)

You can use both simple numbers and ranges. For example,
3~,3
 finds
all rows with values greater than 3 or equal to three.
-1,-1~1,1
 finds
all numbers from -1 to 1, including -1 and 1.

### Example（取自子主题 Correlating data logs）

This sample report from the console describes the correlation of two data
logs:

```
Test Summary Correlation Information:
Data log [A] summary information
TS=myTestSuite,TM=IDD,T=IDD1,TN=343500
TS=myOtherTS,TM=Die_Info,T=Die_X,TN=343600
Data log [B] summary information
+ TS=StdTS,TM=IO_v3,T=TPIO,TN=335700
- TS=myOtherTS,TM=Die_Info,T=Die_X,TN=343600

HW Bin Summary Correlation Information:
Data log [A] summary information
HB=1
HB=2
Data log [B] summary information
all data match 'A'

SW Bin Summary Correlation Information:
Data log [A] summary information
HB=1,SB=7
HB=1,SB=1078
HB=1,SB=1079
HB=2,SB=221
HB=2,SB=1002
Data log [B] summary information
- HB=2,SB=221
```

How
to read this report:

The base data log (data log [A]) contains two test suites, named "myTestSuite" and
"myOtherTS". The first of these test suites uses the test method "IDD" and performs a test
named "IDD1" that has the number 343500.

Data log [B], the first correlated data log (and the
only one in this case) contains an additional test suite, named "StdTS" but does not contain
the "myOtherTS" test method. (Any test methods from data log A that are not mentioned in the
summary of data log B re also present in data log B.

Data log A contains two hardware bins, numbered 1 and 2.

Data log B contains exactly the
same bins, not more and not fewer.

Data log A contains five software bins. The first one is numbered 7 and is connected to
hardware bin 1.

Data log B contains all software bins from data log, except bin 221.

### Rows（取自子主题 Correlation data store structure）

The correlation data store contains all test results from the base
data log (the one that was selected when the
Correlate
 command was
chosen) in the same order as in the base data log.

In addition, it contains all results
for the same tests from the other correlated data stores. These test results are sorted so that
all results for one test appear together.

The correlation data store does not contain
results from test that are not found in the base data log, even if they are contained in one or
more of the correlated data logs.

### Columns（取自子主题 Correlation data store structure）

The correlated data store contains all columns from the base data
log. In addition, it contains new columns showing how the results of the test from the
additional data stores differ from the results of the test in the base data store:

Data Store
: The data store from which the data for this row was
taken.

ΔMean
: The difference between the value in the

Mean
 column of the test from the base data log and the value in the

Mean
 column of the current test.

ΔMean%
: The relative difference (in percent) between the value in the

Mean
 column of the test from the base data log and the value in the

Mean
 column of the current test.

ΔSdev
: As
ΔMean
, but for the

Sdev
 column.

ΔSdev%
: As
ΔMean%
, but for the

Sdev
 column.

ΔRange%
: The value in the
ΔMean
 column as a
percentage of the test range of the base data log (difference between the highest and the
lowest measured values).

ΔStDev%
: The value in the
ΔMean
 column as a
percentage of the standard deviation of the test from the base data log.

ΔCp
: As
ΔMean
, but for the

Cp
 column.

ΔCp%
: As
ΔMean%
, but for the

Cp
 column.

ΔCpk
: As
ΔMean
, but for the

Cpk
 column.

ΔCpk%
: As
ΔMean%
, but for the

Cpk
 column.

ΔCpl
: As
ΔMean
, but for the

Cpl
 column.

ΔCpl%
: As
ΔMean%
, but for the

Cpl
 column.

ΔCpu
: As
ΔMean
, but for the

Cpu
 column.

ΔCpu%
: As
ΔMean%
, but for the

Cpu
 column.

ΔTime
: As
ΔMean
, but for the

Time
 column.

ΔTime%
: As
ΔMean%
, but for the

Time
 column.

ΔTS Time
: As
ΔMean
, but for the
TS
Time
 column.

ΔTS Time%
: As
ΔMean%
, but for the
TS
Time
 column.

These columns may appear in the HW Bin Summary and SW Bin Summary tabs of correlated data
store views:

Data Store
: The data store from which the data for this row was
taken.

ΔDevice#
: As
ΔMean
, but for the

Device#
 column.

ΔDevice%
: As
ΔMean%
, but for the

Device%
 column.

Note that some of these columns may not be displayed, depending on the visible columns
you have specified in the
`preferences`（raw: `136367.htm`）
.

All columns described
above have an entry of "***" for tests from the base data log.

### Example（取自子主题 Correlation data store structure）

This image shows a sample correlation data store in the summary view:

Note that there are additional columns and rows outside the section shown in the
image.

<!-- 语法节 end -->

## 是什么

**文档事实**：Result perspective 的 data navigation 区为每个已打开的 data store 建立一个 data navigation view；每个 view 最多有五个 tab，分别给出该 data store 的不同汇总：Test summary、Wafer summary（correlation data store 没有）、Device summary（correlation data store 没有）、Hardware bin summary、Software bin summary。

**文档事实**：data log 文件的 view 是静态的，内容不随文件变化；system data log stream 是动态的——运行中的 test 产生新 data log entry 会立即加入已打开的 log，summary 和 result display 随之更新。

**文档事实**：data navigation view 的工具栏是 SmarTest 主工具栏的一部分。按钮对最前 tab 中的 test summary 做 grouping：把原本一行显示的 summary 拆成每个子类一行（例如按 site 分组后，每个 test 的结果按 site 分行显示）。`Group by wafer`、`Group by site`、`Group by pin` 可用；按 site 分组也可从 hardware bin summary / software bin summary tab 的右键菜单使用（但这些视图里工具栏按钮禁用）。

**文档事实**：`Refresh`、`Pause`、`Resume`、`Clear`、`Save and Clear` 只在最前 tab 是 system data log stream 的 test summary tab 时可用。`Refresh` 更新暂停中的显示但不恢复自动更新；`Pause` 暂停 system data log stream 的更新并变为 `Resume`；`Resume` 恢复自动更新；`Clear` 清空 Integrated Result Tool 中 system data log stream 的显示并清除 system event stream；`Save and Clear` 先把 system event stream 存成 EDL 文件，再清空显示和 event stream。最前 tab 不是 test summary tab 时这些按钮禁用。

**文档事实**：子主题 `Table filter` 规定过滤输入：文本列可用 plain text 或正则（`Ctrl+Space` 可插入常用正则项），数字列可用精确数字、`~` 范围（可省略一端，如 `~2` 显示小于 2 的行）、逗号分隔多值（OR）；数字与范围可混用（如 `3~,3`、`-1,-1~1,1`）。

**文档事实**：子主题 `Correlation data store structure` 规定：correlation store 按 base data log 的顺序包含 base 的全部 test results，并附加其他 correlated store 中同一 test 的结果，使同一 test 的所有结果排在一起；不包含 base 中不存在的 test。列在 base 全部列之外增加 `Data Store` 以及 `ΔMean`、`ΔMean%`、`ΔSdev`、`ΔSdev%`、`ΔRange%`、`ΔStDev%`、`ΔCp`、`ΔCp%`、`ΔCpk`、`ΔCpk%`、`ΔCpl`、`ΔCpl%`、`ΔCpu`、`ΔCpu%`、`ΔTime`、`ΔTime%`、`ΔTS Time`、`ΔTS Time%`；HW/SW bin summary tab 还可有 `ΔDevice#`、`ΔDevice%`。base data log 的行在这些列显示 `***`。显示哪些列取决于 preferences 中的 visible columns。

## 典型用法

**文档事实**：在 Data Log Explorer 中打开一个 data log，会为它打开一个 data navigation view，并自动生成统计汇总表；每份选中的 log 对应一个 view。卸载 log 时，若已有对应的 data navigation view，会被关闭。

**文档事实**：在 summary 表中选择一行，即可在 detail data view / raw data view / analysis views 中查看该汇总行的底层数据；analysis view 默认显示最前 data navigation view 的当前选择，选择变化时显示随之变化。

**文档事实**：分组：用工具栏 `Group by wafer`/`Group by site`/`Group by pin`，或在 HW/SW bin summary tab 右键按 site。

**文档事实**：过滤：在 table filter 字段输入上述文本/正则/数字/范围/多值。

**文档事实**：动态 log：对 system data log stream 用 `Pause`/`Resume`/`Refresh`；用 `Save and Clear` 保存 EDL 并清空。

**文档事实**：相关日志：对 base log 执行 `Correlate` 命令生成 correlation data store；其 view 没有 Wafer summary 与 Device summary，可用 Δ 列比较其他 store 与 base 的差异；base 行显示 `***`。

## 和谁有关

- [[integrated-result-tool]]：data navigation view 属于 Result perspective；IRT 的 principles 页说这些 summary/statistical tables 是 IRT 的核心。（文档事实）
- **五个 tab**：[[test-summary-tab]]、[[wafer-summary-tab]]、[[device-summary-tab]]、[[hardware-bin-summary-tab]]、[[software-bin-summary-tab]]；Wafer/Device 对 correlation data store 不出现。为什么：本页正文与 `Subtopics` 明确列出它们。
- [[table-filter]]：table filter 的输入语法由其子页定义；本页只给入口。
- **Data Log Explorer**：`Link with Editor` 会把对应 data navigation view 提到前台；打开/卸载 log 会创建/关闭 view。为什么：Explorer 与 view 一一对应。
- [[raw-data-views]]、[[analysis-views]]：raw data view 显示选中 summary 行所汇总的 log entry；analysis view 默认跟随最前 data navigation view 的选择（Link 模式）。
- **Correlating data logs / correlation data store**：`Correlate` 命令产生 correlation data store，本页 tab 组成与 Δ 列按它的结构定义。
- **Preferences**：visible columns 决定显示哪些 Δ 列；`Synchronize selections in navigation views` 决定多个 data navigation view 的选择是否同步；Alerts/Annotations/Shmoo 偏好会在这些 view 中显示高亮或注记。
- **Sorting tables**：data navigation view 的表可按列标题排序。
- **Saving the system data log stream**：`Save and Clear` 把 system data log stream 存为 EDL。

## 版本

**文档事实**：`Functional changes` 写 “Introduced in SmarTest 7.2.0”；SmarTest 7.2.2 新增 `Refresh`、`Clear`、`Save and Clear` 按钮；SmarTest 7.2.2 新增 `Save and Clear` shortcut menu 命令。

## 出处

- 主源：`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02_Data_navigation_views.htm`（正文、Toolbar、Related information、Functional changes）。
- 上面「语法 / 参数」节另逐字取自其子主题：`02.08.04.13.03.02.01`–`.06`（Test/Wafer/Device/HW bin/SW bin summary tab、Table filter），以及 `02.08.04.13.02.02.04`、`02.08.04.13.02.02.04.01`（Correlating data logs、Correlation data store structure）。
