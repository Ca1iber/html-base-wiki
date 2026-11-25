---
type: object
title: The Testflow Analyzer Tool (TAT)
layer: L3
stage: project
tags: []
related: []
sources:
  - 02_System_reference/02.04_Model_File_and_Licensing/02.04.05.07_The_Testflow_Analyzer_Tool__TAT.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# The Testflow Analyzer Tool (TAT)

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

**文档事实** TAT（Testflow Analyzer Tool）是一个命令行工具，本页说明它的功能和一般用法。

**文档事实** TAT 依据给定的 testflow 以及 hardware definition file（HDF）或 model file，生成 device license file（`.licenses`），其中只列出该 testflow 所需的最小能力集合，用于确定所需的 license 最低配置、优化 license 使用。

**文档事实** HDF 描述测试机的硬件（类型、插卡、memory mode）。

**文档事实** TAT 的部分可选参数需要安装 line model encrypted database（`smartest_aslmedb*`）。

**文档事实** TAT 不改动、也不优化 technology file；但它会在生成的 `.licenses` 的注释段给出该 device 使用的 set 数量：level sets、DPS sets、wavetables、timing sets。

**文档事实** TAT 不会列出以下 SmarTest 特性：Per Pin TIA（ppTIA）、Rapid Source Sync（RSS）、Xpress Data Mode（xpressdata）。

## 典型用法

**文档事实** 启动 TAT 前须满足两个条件：SmarTest 正在运行；已加载一个 testflow。

**文档事实** 启动命令为 `/opt/hp93000/soc/prod_pws/bin/tat -f <filename>`。`-f` 是必选参数，`<filename>` 可以是 HDF、model file 或已存在的 device license file。

**文档事实** 其他可选参数见 How to generate and provide a device license file 一页。

**文档事实** TAT 分析 testflow 后在当前目录生成 `.licenses`，该文件只列所给 testflow 所需的最小能力。

**文档事实** 生成的 `.licenses` 注释段会显示用量示例：Level Sets 220、DPS Sets 79、Wavetables 128、Timing Sets 726。

**建议** 要评估某套硬件配置的最低 license 需求，可用对应的 HDF 运行 TAT，再读取生成的 `.licenses` 中 set 数量注释段。

## 和谁有关

- **文档事实** The hardware definition file (HDF)，源文称 TAT 以 HDF（或 model file）作为输入来描述测试机硬件。
- **文档事实** The model file，源文把 model file 与 HDF 并列为 `-f` 可接受的输入。
- **文档事实** The device license file，TAT 生成 `.licenses`，源文 Related information 也列出该页。
- **文档事实** Installing the line model encrypted database，源文说明 TAT 的部分可选参数需要安装该数据库，并把它列为子主题和 Related information。
- **文档事实** Optimizing the technology file，源文子主题；源文明确 TAT 不改动也不优化 technology file。
- **文档事实** How to generate and provide a device license file，源文子主题，承载 TAT 可选参数的说明。
- **文档事实** Technology file for a device，源文 Related information 列出。
- **文档事实** Testflow file，TAT 以已加载的 testflow 为分析对象，源文把「已加载一个 testflow」列为启动前提。

## 版本

**文档事实** Functional changes 记载 Introduced before SmarTest 6.3.2；SmarTest 7.2.1 新增 Numbers of sets（set 数量）。

## 出处

- `02_System_reference/02.04_Model_File_and_Licensing/02.04.05.07_The_Testflow_Analyzer_Tool__TAT.htm`，主源，含 Subtopics、功能与用法说明、Related information 与 Functional changes。
