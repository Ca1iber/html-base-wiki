---
type: object
title: Multiport Burst Editor
layer: gui
stage: pattern
tags: []
related: []
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.03_Multiport_Burst_Editor.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Multiport Burst Editor

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

**文档事实** Multiport Burst Editor 是 pattern tools 之一，用于访问 multiport burst 与各 port burst。port burst 是某个 port 或 pin group 的 pattern 序列，始终是 multiport burst 的一部分。

**文档事实** 可打开任意多个 multiport burst editor。每个实例提供 Overview 页面以及一个或多个 tab 页面，tab 页面显示各 port burst 与 sync group。

**文档事实** Overview 页面始终可见，在一页上显示所有 port burst。expanded 模式下 Overview 可把每次调用的 start cycle 与 start time 作为附加列显示，这两列须在 Pattern Tool preference page 设为 Appearance option，这些列的 tooltip 显示每次调用的 cycle count 与 duration。

**文档事实** port burst 页面按 port burst 的字母顺序排列，可被隐藏。sync group 页面默认名为 DEFAULT，按分配的 synchronization group 显示 port burst，多个 sync group 页面按字母顺序排列，也可被隐藏。

**文档事实** 蓝白标记表示当前 primary 与可展开项，红绿标记表示带结果的项。

**文档事实** 主工具栏图标在很大程度上与 Pattern Editor 相同，包括红色单元格着色与失败数据图标。另有附加功能的图标，用于展开或折叠当前编辑器页面、只展开 port burst 中被选中的 CALL 指令、隐藏或显示 sync group tab、隐藏或显示 port burst tab。

**文档事实** 展开图标要激活必须先执行 testflow。展开模式会在 Overview 页面显示每个 port burst 的 cycle 数，在 port burst 页面显示 Vector#、Instruction 与 Comment 列，在 sync group 页面按时间线对齐显示 vectors，并在 Overview 与 sync 页面显示每个 pattern 的 fail 信息。

## 典型用法

**文档事实** 创建 multiport burst 从 Pattern Explorer 的 New > Multiport Burst 进入 New Multiport Burst 对话框。输入名称，在 Port Bursts 列表选择端口，可选修改每个端口的 sync group，指定 port burst 文件所在 Folder，点 Finish 后 multiport burst 以 Type = MPBurst 出现在 Pattern Explorer。

**文档事实** 不能把共享同一 pin 的两个或多个 port 分配给同一个 multiport burst。创建前应先定义多个 port。

**文档事实** sync group 强制端口始终在同一时间点启动。可用 Ctrl+space 的内容辅助选择 sync group，或输入名称新建，否则使用 DEFAULT。之后也可在 Pattern Explorer 中修改 sync group。

**文档事实** port burst 文件在显式保存 multiport burst 之后才写入指定的 folder。

**文档事实** 可在 Multiport Burst Editor 与 Pattern Explorer 中编辑 multiport burst setup，例如插入 CALL 与 NOP 指令、修改 sync group。Open、Cut、Copy、Paste、Insert、Delete、Up、Down 等多数任务与 Pattern Editor tasks 相同。

**文档事实** 在 Overview 页面或 sync group 页面，可选中一行中的多个相邻单元格或整行，右键选 Insert Instruction。输入包含 port 名的指令后，其他新增单元格自动获得相关的 CALL 指令。若指令未在开头或结尾包含该 port，其他单元格填入 NOP 并显示警告。若使用的 port 不属于目标 port burst，目标单元格的指令被替换为 NOP。

**文档事实** 双击状态行的 location 字段可打开 Go To 对话框。对 multiport burst overview 页面与 collapsed sync group 页面，Go To 对话框可跳到 Instructions 列和 Index/Call Number。

**文档事实** 插入 CALL 指令的单元格可用 Ctrl+space 内容辅助。点按钮打开 Select Pattern 对话框，从中选择被调用的 pattern。

## 和谁有关

- **文档事实** Pattern Editor，Multiport Burst Editor 的主工具栏图标很大程度与 Pattern Editor 相同，包括红色单元格着色与失败数据图标，多数编辑任务也与 Pattern Editor tasks 相同。
- **文档事实** Pattern Explorer，创建 multiport burst 的入口，也是编辑 port burst 调用与 sync group 的场所，新建的 MPBurst 会出现在其中。
- **文档事实** Working with sync groups，本页把 sync group 页面列为编辑器组成部分，并说明 sync group 页面按分配的同步组显示 port burst，展开模式在 sync group 页面按时间线对齐 vectors。
- **文档事实** Pattern Tool preference page，Overview 页面的 start cycle 与 start time 列须作为 Appearance option 在该偏好页设置。
- **文档事实** Definitions: Vector, Pattern, Burst, etc.，本页 Related information 指向该页以说明 vector、pattern、burst 等术语。
- **文档事实** Converting an ASCII Scan Setup Into a Binary Multi-Port Setup，本页 Related information 将其列为相关主题。
- **文档事实** Pattern Editor tasks 与 Pattern Explorer 编辑页面，编辑 multiport burst setup 时多数通用任务沿用这些页面的操作。
- **文档事实** V93000 Components and Compatibility，兼容性页面记有 Superseded by Eclipse based Multiport Burst Editor，说明本工具取代了旧版编辑器。

## 版本

**文档事实** Functional changes 记载 Introduced in SmarTest 7.1.3。子主题 Creating a multiport burst 与 Editing a multiport burst setup 的 Functional changes 同样记为 Introduced in SmarTest 7.1.3。

## 出处

- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.03_Multiport_Burst_Editor.htm`，主源，含编辑器组成、Main toolbar icons、Related information 与 Functional changes。
- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.03.01_Creating_a_multiport_burst.htm`
- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.03.03_Editing_a_multiport_burst_setup.htm`
