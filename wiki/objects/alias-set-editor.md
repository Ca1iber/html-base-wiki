---
type: object
title: Alias Set Editor
layer: gui
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.04_Alias_Set_Editor.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Alias Set Editor

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

**文档事实** Alias Set Editor 显示 pin alias set 的内容，包括 package pin name 与 pin alias；文档以名为 `Trans_IO` 的 alias set 为例。

**文档事实** 用它可创建、编辑、复制、粘贴和删除 pin alias set；其中复制、粘贴、删除的操作方式与 pin group 类似。

**文档事实** 它是 Pin Configuration Tool 的组成部分；Elements of the Pin Configuration Tool 把它与 pin setting editors、Pin group editor、Port Editor 等并列。

## 典型用法

**文档事实** 创建 pin alias set：在 Test Program Explorer 视图右键 `Alias Sets` 并选 `New`，在弹出的 `New Alias` 窗口输入 alias set 名称，点 `OK`。

**文档事实** 编辑 alias set：在 Alias Set Editor 打开目标 set（新建 set 的可编辑区为空）。在 `Alias` 列填别名，在 `Pin` 列填 Pin Setting Editors 中定义的 package pin name；每填完一对后按 Tab 生成新行，继续填写其余 pin。

**文档事实** 编辑完成后应用数据并保存 pin configuration file。

**文档事实** 查看某个 pin 的全部别名：在该 pin 的行号上右键选 `Aliases per Pin`，Search 视图会按 `<alias_set_name>::<alias_name>` 的格式列出所有别名。

## 和谁有关

- **文档事实** `[[pin-configuration-tool]]` — Elements 页把 Alias Set Editor 列为该工具的组成部分；Alias set 页写明用 Pin Configuration Tool 可创建 alias set，并把 pin alias 用作 pin group 成员。
- **文档事实** `Alias Sets`（Test Program Explorer 节点）— 新建 alias set 的入口是右键该节点选 New。
- **文档事实** Pin Setting Editors — 编辑 alias set 时 `Pin` 列填写的是其中定义的 package pin name。
- **文档事实** `[[pin-configuration-file]]` — 编辑完成后要应用数据并保存 pin configuration file。
- **文档事实** Search view — `Aliases per Pin` 的结果显示在 Search 视图。
- **文档事实** Editors（SmarTest Work Center）— 该页把 Alias Set Editor 列为编辑器之一。
- **文档事实** Pin group — 复制、粘贴、删除 pin alias set 的操作与 pin group 类似。

## 版本

**文档事实** Functional changes 记载 Introduced in SmarTest 6.5.2。

## 出处

- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.04_Alias_Set_Editor.htm`，主源，含编辑器用途、创建/编辑 alias set 的步骤、Aliases per Pin 与 Functional changes。
