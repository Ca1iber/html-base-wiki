---
type: object
title: Report window
layer: gui
stage: results
tags: []
related: []
sources:
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.13_Report_window.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Report window

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,153 字符逐字取自** `<01_Getting_started/01.01_SmarTest_Work_Center/01.01.13_Report_window.htm>` 及其子主题 `<01_Getting_started/01.01_SmarTest_Work_Center/01.01.13.03_Configuring_the_messages_printed_in_the_Report_Window.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Examples（取自子主题 Configuring the messages printed in the Report Window）

### Printing messages for passed and failed sites in the Report Window

This example shows how you can configure the

.testflow.ReportUiOutput.user_def
 file to print messages in the

Report Window
 for all passed and failed sites after a testflow is
executed:

```
<passed>Site: %site -> Bin: %bin -> PASS (Cool)
<failed>Site: %site -> Bin: %bin -> FAIL (Bad)
#<text> This is an example for a commented line (using "#" at the beginning)
```

The messages that are printed in the Report Window are as in the following figure:

### Printing messages for failed sites only in the Report Window

This example shows how you can configure the

.testflow.ReportUiOutput.user_def
 so that only messages for the failed
sites are printed in the
Report Window
:

```
<failed>Site : %site -> Bin: %bin -> FAIL (Bad)
```

### Printing messages in the Report Window for the failed sites after a test suite is executed

This example shows how you can configure your

.testflow.ReportUiOutput.user_def
 file to print a message in the

Report Window
 for the failed sites after a test suite is executed:

```
<failed>TestSuite: %testSuiteName -> Site: %site -> FAIL
```

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
