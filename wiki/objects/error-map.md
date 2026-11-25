---
type: object
title: Error Map
layer: file
stage: results
tags: []
related: []
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.08.01_Error_Map.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Error Map

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

**文档事实** Error Map（错误图）是分析测试结果的基础；SmarTest 用它记录 failing test cycles 的信息。

**文档事实** SmarTest 提供两种 error map：detailed error map 与 overview error map。detailed error map 提供 cycle 甚至 edge 级别的信息；overview error map 按 test setup 的 cycle 数，把每 2000 个或更多 cycle 合并为一个结果。

**文档事实** 两者都位于 test processor 内；detailed error map 也可放在外部 RDRAM，默认使用内部 error map，配置见 Result Mode。

**文档事实** 所有结果分析工具（Error Map Tool、Timing Diagram 等）都使用 error map 生成结果的不同视图。

**文档事实** 该页是 Error Map 主题的父页，子主题为 Detailed error map、Setting the acquisition mode、Aligning Timing Diagram and Error Map tool。

**推断** Error Map 是结果数据层的对象而非命令或 test method：本页没有 Syntax/Parameters/Example 段标记，正文只描述记录机制与工具关系。

## 典型用法

**文档事实** 失败分析以 error map 为依据：SmarTest 记录 failing test cycles，各结果分析工具再基于它生成视图。

**文档事实** cycle/edge 级失败用 detailed error map 查看，其数据在 Error Map Tool 的 Cycles 与 Edges 标签中以 cell 矩阵显示；粗略浏览用 overview error map。

**文档事实** detailed error map 可先在 Overview 标签选择一个 cell 再执行测试来聚焦；后续 cell 的 cycles 或 failures（取决于 Acquisition Modes）用于填满 detailed error map 的 8K 内存。

**文档事实** 若测试 cycle 数很大导致 overview block size 大于 2k，或 acquisition mode 设为 Force Cycle Oriented Mode，可能无法在 cycles/edges 中找到错误；处理方式是用扩展内存（见 Result Mode）或把 acquisition mode 改为 Force Failure Oriented。

**文档事实** detailed error map 的位置与分辨率由 Result Mode 配置；Result Mode 按 port 配置 error code 分辨率（1 bit 或 2 bit）、result granularity 与存储位置。

**建议** 先按 port 在 Result Mode 配好 error code 分辨率与 detailed error map 存放位置，再选择 Acquisition Mode，避免概览块过大导致明细不可见。

## 和谁有关

- **文档事实** Detailed error map，本页列为子主题；它提供 cycle/edge 级信息，并说明 detailed error map 位于 test processor 或外部内存、8K 内存，以及看不到错误时的两种处理方式。
- **文档事实** Setting the acquisition mode，本页列为子主题；detailed error map 记录 cycles 还是 failures 取决于 Acquisition Modes。
- **文档事实** Aligning Timing Diagram and Error Map tool，本页列为子主题。
- **文档事实** Result Mode，本页正文指向它说明 error map 的配置与 detailed error map 位置；该页按 port 配置 error code 分辨率、result granularity 与存储位置。
- **文档事实** Error Map Tool，objpack 入边引文显示该页包含 Using the Error Map Tool、Elements of the Error Map Tool、Result Configuration、Hidden Error Map、Upload/Print Error Map Data 等小节，说明工具消费 error map 数据。
- **文档事实** Result areas and vector memory consumption，objpack 入边引文说明 test processor 有一小块嵌入式内存只用作 error map memory；错误很多时可把 error map memory 重定向到 vector memory。
- **文档事实** Result commands（02.06.11.01.02.01.06），objpack 入边引文说明该页给出配置 Error Map 并取回结果的示例，并把 Error Map 列为结果命令相关主题。
- **文档事实** FFCI 与 FFPM，objpack 入边引文把 Error Map 列为两者的 Application，说明首次失败周期信息命令/工具与 error map 相关。
- **推断** 从这些引用看，Error Map 是 Result 体系的下层数据源：FFCI/FFPM、Error Map Tool、Timing Diagram 在其之上做展示或提取。

## 版本

**文档事实** Functional changes 记载：

- Introduced before SmarTest 6.3.2
- SmarTest 7.0.1：当使用 Pin Scale 9G 引脚生成 PRBS 或将 DUT 数据与 PRBS 比较时，error map 不工作

## 出处

- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.08.01_Error_Map.htm`，主源，含概述、子主题与 Functional changes。
- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.08.01.01_Detailed_error_map.htm`、`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.08.04.01_Result_Mode.htm`，用于核对 detailed error map 的 8K 内存、定位与 Result Mode 的 port 级配置（已用 show.py 读取）。
- Error Map Tool、Result commands、FFCI/FFPM、Result areas and vector memory consumption 的引文取自 `extract/objpack.py` 入边索引。
