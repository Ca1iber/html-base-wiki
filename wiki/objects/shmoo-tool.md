---
type: object
title: Shmoo Tool
layer: gui
stage: results
tags: []
related: []
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.25_Shmoo_Tool.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Shmoo Tool

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

**文档事实** Shmoo Tool 用于创建 shmoo tests 并查看 shmoo plots。

**文档事实** 可用它执行：对 functional test 做 shmoo；对已有 test suite 或多个 test suite 做 shmoo；针对 MTP 的 fail bit count shmoo；以及自定义 shmoo tests。

**文档事实** 对 test suite 做 shmoo 时，可以在 shmoo plot 上查看 value 结果。

**文档事实** 它支持 multisite shmoo tests，并支持覆盖（overlay）shmoo plots。

**文档事实** 文档把使用流程拆成 set up、execute、view 三步，并另设打开工具、工具界面、命令附录等子主题。

## 典型用法

**文档事实** 在 Shmoo Tool 中设置、执行并查看 shmoo test；对 test suite 做 shmoo 时可查看其 value 结果。

**文档事实** 可用 Shmoo Tool 做 multisite shmoo，并覆盖查看不同 site 的 shmoo 图。

**文档事实** 与 Testflow Tool 交互可：显示某个 shmoo test suite 的 shmoo plot；在 Shmoo Tool 与 test suite 之间转移 shmoo setup。

**文档事实** 要把 shmoo 数据记入 report window，或把 shmoo plot 保存为 PNG/ASCII 文件，必须先把 shmoo tests 从 Shmoo Tool 转移到 testflow。

**文档事实** 要在 Integrated Result Tool 中显示 shmoo plot，同样必须先把 shmoo tests 从 Shmoo Tool 转移到 testflow。

**建议** 需要进报告或长期保存时，先在 Shmoo Tool 中调好 shmoo setup，再转移到 testflow，之后才能写入 report window 或导出 PNG/ASCII。

## 和谁有关

- **文档事实** Testflow Tool，源文列出的交互包括显示 shmoo test suite 的 shmoo plot、在 Shmoo Tool 与 test suite 之间转移 shmoo setup。
- **文档事实** Integrated Result Tool，源文称可与之交互以在其中显示 shmoo plots，前提是先把 shmoo tests 转移到 testflow。
- **文档事实** Report window，源文称可把 shmoo 数据记入 report window，前提同上。
- **文档事实** Test suites，源文称可对已有 test suite 或多个 test suite 做 shmoo，并可在 Shmoo Tool 与 test suite 间转移 shmoo setup。
- **文档事实** MTP_MEMORY_TEST，源文把 fail bit count shmoo for MTP 列为用途之一。

## 版本

**文档事实** Functional changes 记载 SmarTest 7.2.2 引入对多个 test suite 做 shmoo；SmarTest 7.2.2 将 shmoo plots 与 results 保存为 ASCII 文件。

## 出处

- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.25_Shmoo_Tool.htm`，主源，含 Subtopics、功能与用途说明、与 Testflow Tool 及 Integrated Result Tool 的交互说明与 Functional changes。
