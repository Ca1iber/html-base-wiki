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

（待补）

## 典型用法

（待补）

## 和谁有关

（待补）

## 版本

（待补）

## 出处

（待补）
