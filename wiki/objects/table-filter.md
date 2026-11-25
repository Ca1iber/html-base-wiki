---
type: object
title: Table filter
layer: gui
stage: results
tags: []
related: []
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02.06_Table_filter.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Table filter

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,307 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02.06_Table_filter.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

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

<!-- 语法节 end -->

## 是什么

**文档事实**：Table filter 是每个 summary tab、raw data view、stream data view 中表格的最上面一行（青色背景）；它按你指定的条件限制表格显示的记录。

**文档事实**：双击 table filter 的某个单元格，即可为该列输入条件；单元格右侧的下拉列表可选择最近输入过的条件，某些字段还可选预定义值。

**文档事实**：在多列都输入条件时，只显示同时满足所有条件的记录（AND 关系）。

**文档事实**：点击 table filter 行最左侧的小字段会清除全部条件，表格重新显示所有行。

## 典型用法

**文档事实**：按列类型的输入写法（本页 `Syntax` 节已逐字列出）：

- 文本列：plain text，列内容包含该文本即显示；或正则表达式，列内容匹配正则即显示（`Ctrl+Space` 的 Content Assist 可插入常用正则项）；
- 数字列：精确数字；用 `~` 连接的两个数字表示范围（大于第一个、小于第二个，可省略一端，如 `~2` 表示小于 2）；逗号分隔多个数字表示 OR；数字与范围可混用（如 `3~,3` 表示大于 3 或等于 3，`-1,-1~1,1` 表示 -1 到 1 含两端）。

**文档事实**：操作方式为「双击目标列单元格 → 输入条件」；多列条件叠加；从下拉列表选最近条件或预定义值可复用条件；点最左侧小字段清除全部条件。

## 和谁有关

**文档事实**：以下关系均有来源文档中的正文或回链证据支撑。

- [[data-navigation-views]]：该页把 Table filter 列为其组成部分，并说明每个 data navigation view 的表格顶行就是它。
- [[test-summary-tab]]、[[wafer-summary-tab]]、[[device-summary-tab]]、[[hardware-bin-summary-tab]]、[[software-bin-summary-tab]]：这五个 summary tab 的文档都写明表格最上面一行为 table filter，并指向本页。
- [[raw-data-views]]：raw data view 的文档同样写明其表格最上面一行为 table filter。
- `Stream data view`（`02.08.04.13.03.03.02_Stream_data_view.htm`）、`Protocol Monitor view`（`02.08.04.13.03.04.07_Protocol_Monitor_view.htm`）：两页都声明其表格顶行为 table filter（回链证据）。
- `Filtering test result data`（`02.08.04.13.02.03.02_Filtering_test_result_data.htm`）：本页 `Related information` 指向它，给出在结果表上设置与清除过滤的操作主题。
- `Detail data views`（`02.08.04.13.03.03_Detail_data_views.htm`）：本页 `Related information` 列出。

## 版本

**文档事实**：`Functional changes` 写 `Introduced in SmarTest 7.2.0`。

## 出处

- 主源（「语法 / 参数」的逐字来源）：`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02.06_Table_filter.htm`（正文、Syntax、Related information、Functional changes）。
- 回链证据：`02.08.04.13.03.02_Data_navigation_views.htm` 及 `02.08.04.13.03.02.01`–`.05` 的五个 summary tab、`02.08.04.13.03.03.01_Raw_data_views.htm`、`02.08.04.13.03.03.02_Stream_data_view.htm`、`02.08.04.13.03.04.07_Protocol_Monitor_view.htm`。
