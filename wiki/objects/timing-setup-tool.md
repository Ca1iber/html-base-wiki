---
type: object
title: Timing Setup Tool
layer: gui
stage: timing
tags: []
related: []
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34_Timing_Setup_Tool.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Timing Setup Tool

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

**文档事实** Timing Setup Tool 是用于为被测器件设置 timing 的工具；本页所属章节说明设置 timing 所需的背景知识、界面描述与任务相关信息。

**文档事实** 章节先介绍 V93000 Timing System 及其资源，说明它如何生成 timing 信号，并概览 device cycles 与 waveforms；随后说明 waveform 与 timing sets，以及实现测试优化的途径。

**文档事实** 章节介绍 Timing Setup commands，并说明如何用这些命令定义 waveform、timing specification 等内容，同时给出搭建 equation based timing tests 所需的基础工具。

**文档事实** 章节列出用 Timing Setup tool 完成的任务：设置 system period 与 clock source；通过定义 device cycles、放置 edges、创建 waveforms 来生成和编辑 device cycles；跟踪 system resources；执行 compatibility checks；通过 Table Format 显示关注的 pins/pin groups；按需调整 Timing Setup window；使用 waveform 与 timing sets。

**文档事实** 章节最后简要讨论 Timing Setup window 这一用户界面，以说明其机制。

## 典型用法

**文档事实** 文档描述的任务顺序为：设置 system period 与 clock source，定义 device cycles 并放置 edges、创建 waveforms，跟踪 system resources 并执行 compatibility checks，再通过 Table Format 显示关注的 pins/pin groups，最后处理 waveform 与 timing sets。

**文档事实** 具体操作步骤不在本概述页，而在子主题 Using the Timing Setup Tool；窗口布局与操作机制在子主题 The Timing Setup Window。

**文档事实** 命令用法在子主题 Timing Setup Commands，方程式 timing 的做法在子主题 Equation based timing setup，mode context 的说明在子主题 Mode context in timing setup。

**文档事实** Related information 把 How to set up a multiport timing specification 列为相关页面，用于 multiport timing specification 的设置。

**建议** 按子主题顺序先读 Description of the Timing System 与 Timing Setup Commands，再进入 Using the Timing Setup Tool，可避免只看本页任务清单就下手。

## 和谁有关

- **文档事实** Description of the Timing System、Timing Setup Commands、Waveform and timing sets、Equation based timing setup、Mode context in timing setup、Using the Timing Setup Tool、The Timing Setup Window，这七页是本页列出的子主题，分别承载 timing 系统背景、命令、waveform/timing sets、方程式 timing、mode context、操作步骤与窗口说明。
- **文档事实** How to set up a multiport timing specification，本页 Related information 将其列为 multiport timing specification 的相关做法。
- **文档事实** Tools in alphabetical order 与 Tools grouped by function，两个工具目录页都把 Timing Setup Tool 列入工具清单。
- **文档事实** 93000 menu and its tools，该页在 93000 菜单的工具列表里包含 Timing Setup Tool。
- **文档事实** Preliminary Checklist，该页把 Timing Setup Tool 列入新建或选择已有 device 的预备清单。
- **文档事实** Task 3: Setups for Digital Channels，该页要求用 Timing Setup Tool 定义数字引脚的 digital waveform shapes。
- **文档事实** Setting up sequencer control of utility lines，该页要求用 Timing Setup Tool 为串行接口引脚创建 wavetable 并设置 timing；System reference 与 Use case 两个版本都有该表述。
- **文档事实** Timing Diagram Tool、Pin Scale 5000 timing setup、Timing file（Memory Test Plus 7.10.2）都引用了 Timing Setup Tool。

## 版本

**文档事实** 主源页面没有 Functional changes 段，版本信息文档未覆盖。

## 出处

- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34_Timing_Setup_Tool.htm`，主源，含 Subtopics、章节概述、任务清单与 Related information。
- 与引用页的关系取自 `extract/objpack.py` 的入边索引（引用页原文片段），未逐页通读这些引用页。
