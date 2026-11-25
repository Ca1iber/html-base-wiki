---
type: object
title: Utility Line view
layer: gui
stage: run
tags: []
related: []
sources:
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.05.04_Utility_Line_view.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Utility Line view

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

**文档事实** Utility Line view 是 Hardware Perspective 的一部分，提供查询 utility line 读写状态、设置 utility line 写状态的界面，用于调试 test setup。

**文档事实** V93000 test head 上的 utility lines 用于控制继电器、指示灯等外部设备，或从外部设备读取。

**文档事实** 该视图可监视或控制所有 utility lines，包括未在 pin configuration 中定义的那些。

**文档事实** 文档补充：若要使用 Routing Setup Tool 创建的 routing sets 控制 utility line 写状态，则必须在 pin configuration 中定义 utility line 名称或 utility purposes。

**文档事实** 视图左列代表 utility pogo blocks；前八个 utility pogo blocks 显示的标识符是旧式 "UTI#" 与新的三位 pogo block 号的组合。截图还显示第二个可选 Utility Card 的另外八个 pogo blocks，文档说明截图为每个 pogo block 32 条 utility lines。

**文档事实** header row 中 SmarTest 显示 utility lines 的 channel numbers，范围 [01 … 32]，从右到左；utility line 自身编号有 -1 偏移，范围 [00 … 31]，对应 DUT Board Design Guidelines 中 "Utility pogo pin layouts" 的 "URW##" 方案。

## 典型用法

**文档事实** 调试 test setup 时，用该视图查询 utility line 的读状态与写状态，并设置写状态。

**文档事实** 顶部有三个图标：Setup Preferences 图标打开偏好窗口，其设置与 Utility Line preference page 相同；Refresh 图标手动刷新 Utility Line View；中间图标把写更改应用到所有 utility blocks。

**文档事实** Utility Purpose view 页说明：应用 utility purpose 后可在 Utility Line view 中检查指定值；取决于 preferences 配置，需要刷新该视图。

**文档事实** Pin Browser 页说明：utility pins 的定义名称、写状态与 channel 号可在 Pin Browser 查看；要查询读写状态或更改写状态，使用 Utility Line view。

**建议** 改了 utility purpose 后先点 Refresh 再读取状态，避免显示值仍是刷新前的结果。

**建议** 若要按 routing set 批量控制写状态，先在 pin configuration 中定义 utility line 名称或 utility purpose，这是文档给出的前提。

## 和谁有关

- **文档事实** Hardware Perspective，本页说明 Utility Line view 是该视角的一部分。
- **文档事实** Utility Line preference page，Setup Preferences 图标打开的偏好窗口使用与该页相同的设置。
- **文档事实** Utility Purpose view，该页把应用 utility purpose 后的值检查指向 Utility Line view，并提示可能需要刷新。
- **文档事实** Pin Browser view，该页让用户在 Pin Browser 看 utility pin 的定义名称、写状态与 channel 号，而把读写状态查询与写状态更改交给 Utility Line view。
- **文档事实** Utility Pins editor，本页 Related information 把它列为相关页面。
- **文档事实** Routing Setup Tool，本页说明用其 routing sets 控制写状态时需在 pin configuration 中定义 utility line 名称或 utility purposes。
- **文档事实** Utility lines，本页正文与 Related information 都引用该页说明 utility line 的用途。
- **文档事实** DUT interface layout 与 Utility pogo block mapping（Utility Card, V93000 EXA Scale systems），本页在 pogo block 与编号说明处引用。
- **文档事实** Utility line assignments，本页指向该页以了解 utility pogo blocks。
- **文档事实** Utility Card，本页说明截图中的第二个可选 Utility Card 还有八个 pogo blocks。

## 版本

**文档事实** Functional changes 记：Introduced before SmarTest 6.3.2；SmarTest 6.5.3 起 Utility Line View 以 bit numbers 01 到 16 显示 utility lines；SmarTest 7.2.0 引入 Utility Purpose view；SmarTest 7.10.1 在 EXA Scale 系统上使用三位 utility pogo block 标识。

## 出处

- `01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.05.04_Utility_Line_view.htm`，主源，含概述、图标说明、Related information 与 Functional changes。
- `01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.05.06_Utility_Purpose_view.htm` 与 `01.01.07.05.02_Pin_Browser_view.htm`，用于核对刷新与 Pin Browser 的分工（已用 show.py 读取）。
