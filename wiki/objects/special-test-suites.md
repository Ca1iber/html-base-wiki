---
type: object
title: Special test suites
layer: file
stage: testflow
tags: []
related: []
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.01.02_Special_test_suites.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Special test suites

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

- **文档事实** — Special test suites 在特定时间点执行，可依赖或不依赖 testflow，例如向测试系统下载初始值、定义 abort 时执行什么。
- **文档事实** — 它们不作为节点出现在 Flow Sequence Editor 中，而是在 Flow Data Editor 的 Test Suites page 默认排序时显示在末尾。
- **文档事实** — 原文写 "There are seven types of special test suites"，但紧随其后的表列出 8 项：Init、bin_disconnect、Abort、Reset、Pause、multi_bin_decision、Exit、Download；原文如此，数目不一致。
- **文档事实** — Init 是可选 suite，给测试系统初始设置（testflow 变量、外部设备初始状态等），在 Download 之后、testflow 执行开始之前运行。
- **文档事实** — Download 在 testflow 载入后执行，用于加载 Flow Data Editor 的 Setups page 中选定的 pin configuration setup 或其他 setup 文件。
- **文档事实** — bin_disconnect 在器件落入某个 bin 时执行；Abort/Reset/Pause/Exit 分别在 abort/reset/pause/exit 状态执行；multi_bin_decision 在一个或多个 site 到达 testflow 的 multi_bin 节点时执行。
- **文档事实** — 不要从 special test suites 内抛异常，因为其处理与 testflow executor 不兼容。
- **文档事实** — bin_disconnect 是断开失败器件的 legacy 方法；新器件推荐用 Multibin SmartDisconnect test suite（multibin 节点与用户定义 test suite 的组合）。

## 典型用法

- **文档事实** — Init 的执行位置：test program loaded → testflow loaded → pin configuration loaded → Download suite 执行 → Init suite 执行 → testflow 第一次运行开始 → 下载尚未加载的 setup 文件 → 第一个 test suite 执行。
- **文档事实** — bin_disconnect 内若使用 `DISCONNECT` API：器件定义了 disconnect sequence 就执行该序列，否则执行标准 disconnect sequence。
- **文档事实** — multi_bin_decision 内可用 `SET_MULTIBIN` API 在 test method 中决定使用哪个 bin。
- **文档事实** — Download 在 testflow 载入后执行，用于加载 pin configuration 或其他 setup 文件；其执行位置与 Init 的关系见上条。
- **文档事实** — Abort 卸载 test program 并断开测试系统，但不复位测试系统硬件；Reset 会卸载 test program、进入 initialized（disconnected）状态并复位硬件，因此重启前必须重新下载原始设置。

## 和谁有关

- [[test-suite]] — Test suites 文档把 "Special test suites" 与 Run/Run and Branch test suites、Floating test suite 等并列。
- [[test-suites-page]] — special test suites 在 Flow Data Editor 的 Test Suites page 中显示（文档说默认排序在末尾）。
- [[flow-data-editor]] — Test Suites page 属于该编辑器；special test suites 在这里可见但不在 Flow Sequence Editor 作为节点。
- [[flow-sequence-editor]] — 主文档明确 special test suites 不作为节点出现在这里。
- [[disconnect]] — bin_disconnect 的文档提到使用 `DISCONNECT` API 及其 disconnect sequence。
- `Multibin SmartDisconnect test suite`（`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.01.04_Multibin_SmartDisconnect_test_suite.htm`）— 主文档推荐用它替代 legacy 的 bin_disconnect。
- `SET_MULTIBIN`（`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.212_SET_MULTIBIN.htm`）— multi_bin_decision 中决定 bin 的 API。

## 版本

- **文档事实** — "Introduced before SmarTest 6.3.2"；这是哨兵值，表示文档集覆盖范围之前已存在，不是 6.3.2 的变更。
- **文档事实** — "SmarTest 6.3.2: Special test suites are now displayed in the Tabular Testflow Editor."
- **文档事实** — "SmarTest 6.5.0: New special test suite bin_disconnect."
- **文档事实** — "SmarTest 6.5.2: New special test suite multi_bin_decision."

## 出处

- 主文档 `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.01.02_Special_test_suites.htm`（`show.py 02.08.04.32.01.02.01.02` / `objpack.py`）。
- 本页语法节标为「没有加标记的语法段」，因此散文依据主文档正文。
