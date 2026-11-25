---
type: object
title: Flags page
layer: gui
stage: run
tags: []
related: []
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.01.06_Flags_page.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Flags page

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

**文档事实** Flags page 用于设置 system flags 与 testflow flags。

**文档事实** 在 engineering 模式下运行 SmarTest 时，也可通过 Operation Control window（经 Production Settings）访问 system flags 与 testflow flags。

**文档事实** 要真正修改 flags，必须把所有窗口从 Operation Control window 设为 Testflow settings mode（而非 Production settings mode）。

**文档事实** Flow Data Editor 的页面标签列表中包含 Flags page（与 Test Suites、Parameters、Tests、Bins、Variables、Setups、Information 等并列），即它是 Flow Data Editor 的一个页面。

**推断** 文档有时把 "Flags page" 称作 "Flags tab"（例如 "On the Flag tab of the Flow Data Editor set parallel_mode = on"），两者应指同一处。

## 典型用法

**文档事实** 在 Flags page 上设置 testflow flags。文档中给出的具体 flag 例子包括：`global_overon`（启用 Overon 功能）、`debug_mode`（把结果输出到 report window）、`parallel_mode`（并行测试）、`test_number_enable`（生成 per-pin test numbers）。

**文档事实** 修改 flags 前须把所有窗口设为 Testflow settings mode。

**文档事实** 在 engineering 模式下，flags 也可从 Operation Control window 的 Production Settings 进入；但若要把改动落地，仍须切回 Testflow settings mode。

**建议** 设置某个 flag 前先查 Testflow flags、Testflow flags for data logging 与 Alphabetical list of flags，确认该 flag 的名称与取值语义。

## 和谁有关

- **文档事实** Flow Data Editor — 其页面列表包含 Flags page，说明 Flags page 是 Flow Data Editor 的一个页面。
- **文档事实** Testflow flags、Testflow flags for data logging、Alphabetical list of flags — 本页 Related information 列出；Alphabetical list 说明 "Flags page 或 Testflow Tool 的 Test suite properties 视图显示的是 flag 名"，并定义各 flag。
- **文档事实** Setting up flags — 引用 Flags page。
- **文档事实** Operation Control window、Activating event data logging — 说明 engineering 模式下可经 Production Settings 访问 flags，且修改须切到 Testflow settings mode。
- **文档事实** Running a testflow — 说明在 Flags page 把 `debug_mode` 设为非 off 值即可把结果输出到 report window。
- **文档事实** Using the Overon feature while running a testflow — 说明在 Flags page 设 testflow flag `global_overon` 为 on。
- **文档事实** Generating per-pin test numbers — 说明在 testflow flag page 打开 `test_number_enable`。
- **文档事实** Setting Flags for Parallel Execution、Performance Cookbook 的 Generic Test Program Setup 与 Usage of Parallel Hardware (PPMU) — 说明设 `parallel_mode` 与 Allow Parallel 以启用并行测试。
- **文档事实** Using the Trace Function — 引用 Flags page。

## 版本

**文档事实** Functional changes 仅记载：Introduced before SmarTest 6.3.2。

## 出处

- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.01.06_Flags_page.htm`，主源，含 system/testflow flags 说明、修改前置条件、Related information 与 Functional changes。
- 该页无子主题；语法节为空，因原文没有 `Syntax` / `Parameters` / `Example` 段标记。
