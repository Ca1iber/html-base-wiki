---
type: object
title: Debug View
layer: gui
stage: run
tags: []
related: []
sources:
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.08.06_Debug_View.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Debug View

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

**文档事实** Debug View 用于控制程序或 testflow 的调试过程。

**文档事实** 当某个 class 或 function 被 suspend 时，其 stack frames 会作为 program 或 testflow 的子元素显示。

**文档事实** 也可以使用 Setup perspective 主工具栏上对应的调试按钮。

**文档事实** 对 testflow 执行，SmarTest 会自动显示 Debug view。

**文档事实** testflow 调试图标包括：移除所有已终止的 testflow、Restart（重启 testflow 执行）、Resume（继续执行，除非 test method 中有已启用的 breakpoints）、Suspend（停止执行）、Terminate（中止执行）、Step over（执行恰好下一个 test suite）。

**文档事实** test method 调试（C++ debugging）的 Debug view 细节，文档指向 Help > Help Contents > C/C++ Development User Guide > Reference > Debug views > Debug view。

## 典型用法

**文档事实** testflow 执行时 Debug view 自动出现，可用其图标控制执行。

**文档事实** 需要从头重跑时用 Restart；需要继续运行时用 Resume（若 test method 中有已启用的 breakpoint 则会停下）；需要暂停用 Suspend；需要中止用 Terminate。

**文档事实** 用 Step over 执行恰好一个（下一个）test suite，用于逐步推进 testflow。

**文档事实** 用相应图标移除 Debug view 中所有已终止的 testflow。

**推断** 上述按钮对应 testflow 级调试；test method 内部的 C++ 调试需按源文指出的 C/C++ Development User Guide 使用。

## 和谁有关

- [[setup-perspective]]：**文档事实** 本页说可用 Setup perspective 主工具栏上的调试按钮，Related information 也指向它。为什么：调试按钮的入口在该 perspective。
- [[debug-perspective]]：**文档事实** 入边显示 Debug perspective 页说 Debug view 显示 test method 执行与调试过程，可在此控制 test method 执行。为什么：Debug view 是 Debug perspective 的核心视图。
- Views（`01_Getting_started/01.01_SmarTest_Work_Center/01.01.08_Views.htm`）：**文档事实** 入边显示该页把 Debug View 列在可打开并加入 perspective 的视图之中。为什么：说明它是工作台视图家族的一员。
- Single step testflow debugging（`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.04.01_Single_step_testflow_debugging.htm`）：**文档事实** 本页 Related information 指向它，入边也点名 Debug View。为什么：单步 testflow 调试直接使用本视图。
- Using the debugger（`01_Getting_started/01.03_Using_SmarTest/01.03.03.01_Using_the_debugger.htm`）：**文档事实** 入边点名 Debug View。为什么：调试器使用说明引用本视图。
- Run menu（`01_Getting_started/01.01_SmarTest_Work_Center/01.01.11.03_Run_menu.htm`）：**文档事实** 入边把 Debug View 与 Run 菜单的 debug launch shortcuts 关联。为什么：调试启动入口在 Run 菜单。

## 版本

**文档事实** Functional changes 记：Introduced in SmarTest 7.1.0。

## 出处

- `01_Getting_started/01.01_SmarTest_Work_Center/01.01.08.06_Debug_View.htm`，主源，含概览、Testflow debugging、Test method debugging、Related information 与 Functional changes，已用 `show.py 01.01.08.06` 读取。
- 关系与入边取自 `extract/objpack.py`（`edges.jsonl`）：Views、Debug perspective、Single step testflow debugging、Using the debugger、Run menu。
