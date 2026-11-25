---
type: object
title: TimeStampAttrType
layer: file
stage: results
tags: []
related: []
sources:
  - 02_System_reference/02.10_Data_Logging/02.10.01.06.05.65_TimeStampAttrType.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# TimeStampAttrType

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

**文档事实** TimeStampAttrType 表示事件发生的时间，其数据类型为 DRLTimeStampAttr。

**文档事实** 它包含四个字段：`length`（int，attribute 长度）、`type`（short，attribute 类型）、`secs`（int，秒）、`usecs`（int，微秒）。

**文档事实** `length` 与 `type` 组成 attribute header。

**文档事实** `secs` 与 `usecs` 表示自 1970-01-01 起经过的秒数和微秒数，即 Linux 的标准时间度量。

**文档事实** Related information 把本页归入 EDF data types 与 EDF data organization。

**推断** 因此 TimeStampAttrType 是 EDF 事件记录中承载“事件何时发生”的 attribute，时间基准是 Unix epoch。

## 典型用法

**文档事实** 本页只给出字段结构和类型，没有给出代码示例或调用步骤。

**文档事实** 各类事件类型页把 TimeStampAttrType 用作事件时间字段：例如 ActionEventType 用它保存事件被记录的时间；TestProgramStartEventType 用它保存 test program 启动时间，TestProgramEndEventType 保存结束时间，二者可用于计算 test program 的执行时间。

**文档事实** TestFlowStartEventType 与 TestFlowEndEventType 分别保存 testflow 开始与结束执行的时间；TestFunctionStartEventType 与 TestFunctionEndEventType 分别保存 test function 开始与完成的时间。

**文档事实** TestSuiteStartEventType、TestEventType、BinReachedEventType、AssignmentEventType、PrintToDatalogEventType、UserProcedureEventType、ConfigurationChangedEventType、GenericDataEventType、ManualExecutionEventType 等事件页也说明对应时间由 TimeStampAttrType 保存。

**推断** 典型用途是给测试程序、testflow、test suite、test function 及 binning 等事件打时间戳，并用起止时间戳计算阶段耗时。

## 和谁有关

- **文档事实** DRLTimeStampAttr，本页正文明确说 TimeStampAttrType 的数据类型是 DRLTimeStampAttr。
- **文档事实** EDF data types 与 EDF data organization，本页 Related information 链接这两页，把 TimeStampAttrType 放进 EDF 类型体系。
- **文档事实** Attribute types，objpack 入边显示该页把 TimeStampAttrType 列入 attribute 类型清单。
- **文档事实** ActionEventType、TestProgramStartEventType、TestProgramEndEventType、TestFlowStartEventType、TestFlowEndEventType、TestFunctionStartEventType、TestFunctionEndEventType 等事件页，objpack 入边引文说明这些事件的时间字段由 TimeStampAttrType 保存。
- **文档事实** TestSuiteStartEventType/TestSuiteEndEventType、TestEventType、BinReachedEventType、AssignmentEventType、PrintToDatalogEventType、UserProcedureEventType/UserProcedureStartEventType、ConfigurationChangedEventType、GenericDataEventType、ManualExecutionEventType、AppModelLevelStartEventType/AppModelLevelEndEventType/AppModelLevelLoopEventType，objpack 入边引文同样以 TimeStampAttrType 保存对应事件时间。
- **推断** 这些关系表明 TimeStampAttrType 是事件类型页的通用时间字段类型，而不是某个单一事件专用。

## 版本

**文档事实** Functional changes 只记一条：Introduced before SmarTest 6.3.2。

## 出处

- `02_System_reference/02.10_Data_Logging/02.10.01.06.05.65_TimeStampAttrType.htm`，主源，含字段表、Related information 与 Functional changes。
- 事件类型页与 Attribute types 的引用关系取自 `extract/objpack.py` 入边索引。
