---
type: object
title: Flow Sequence Editor
layer: gui
stage: testflow
tags: []
related: []
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.02_Flow_Sequence_Editor.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Flow Sequence Editor

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

**文档事实** Flow Sequence Editor 以图形形式显示 testflow 序列并允许编辑。主窗口显示由 insertion points 与 testflow components 组成的图形 testflow 序列。

**文档事实** 左侧 Palette 用于把 Testflow components 插入 testflow。

**文档事实** 可用主工具栏的 Zoom in / Zoom out 按钮，或在按钮旁的字段输入百分比缩放级别，放大或缩小图形。

**文档事实** 它是 Testflow Tool 的两个编辑器之一。两个编辑器处理 `<device directory>/testflow` 下的同一个 testflow 文件，只是表示方式不同：Flow Data Editor 用表格式显示 testflow 元素，Flow Sequence Editor 显示 test 的 flow diagram，提供 testflow 结构信息。

**文档事实** Flow Data Editor 会自动保持其 focus 的 test suite 与 Flow Sequence Editor 同步，反之亦然；Flow Data Editor 的各页之间也自动同步。

**推断** 因此 Flow Sequence Editor 是 testflow 的「结构视图」，适合查看分支与执行顺序；具体属性值由 Flow Data Editor 与 Testflow Properties view 维护，二者同步显示同一份 testflow 数据。

## 典型用法

**文档事实** 在已打开的 testflow 中，用左侧 Palette 插入 testflow components，搭建或调整序列；相关操作页为 Inserting a test suite into the testflow、Working with nodes、Deleting nodes。

**文档事实** 缩放：点主工具栏 Zoom in / Zoom out，或在旁边字段输入目标百分比。

**文档事实** 可从此编辑器执行整条 testflow 或选中的 test suite / group（Working with testflows efficiently 页）。

**文档事实** 可把 floating test suite 连接到 Flow Sequence Editor 中的 testflow，连接后它成为普通 test suite。

**文档事实** 右键 test suite 可选 `Shmoo > Show In Shmoo Tool`，把该 suite 送入 Shmoo Tool。

**文档事实** 可在此编辑器为 test suite 启用 Output on pass、Output on fail、Pass value、Fail value、Per pin on pass、Per pin on fail 等 flags，以配合 Integrated Result Tool。

**文档事实** 可从此编辑器打印图形表示：File > Save as picture，保存为图片（如 `testflow.jpg`）。

**文档事实** 可从此编辑器激活 offline result emulation（Activating offline result emulation in the testflow 页要求先在 Flow Sequence Editor 打开 testflow）。

**建议** 结构性改动（插入、删除、连接节点）在此编辑器完成，属性值在 Flow Data Editor 填写；两者自动同步，改完一处后到另一处确认即可，不必重复录入。

## 和谁有关

- **文档事实** Flow Data Editor：Synchronization 子主题说明二者自动保持 test suite focus 同步；Elements of the Testflow Tool 说明二者处理同一 testflow 文件，分别用表格与流程图表示。
- **文档事实** Testflow Tool：Flow Sequence Editor 属于 Testflow Tool 的两个编辑器之一（Elements of the Testflow Tool）。
- **文档事实** Testflow components：Palette 插入的对象，本页正文链接到该页。
- **文档事实** Opening the Testflow Tool、Inserting a test suite into the testflow、Working with nodes、Deleting nodes：本页 Related information 列出的直接操作页。
- **文档事实** Synchronization between the Flow Data Editor and the Flow Sequence Editor：本页 Related information 列出的同步说明页。
- **文档事实** Testflow Properties view：显示当前在 Flow Sequence Editor 中选中的 test suite 的所有属性（objpack 入边）。
- **文档事实** Group node 与 Bins：Go To 会在此编辑器中高亮所选 group / bin；floating bin 不在此显示，但其 multibin 插入后会显示；普通 bin node 只能在此编辑器中删除。
- **文档事实** Special test suites：bin_disconnect 等特殊 test suite 不在此编辑器中显示为图标。
- **文档事实** Hardware Response Emulator：使用前要求 testflow 已在 Flow Sequence Editor 打开。
- **文档事实** Shmoo Tool：可在此编辑器右键 test suite，选 Shmoo > Show In Shmoo Tool。
- **文档事实** Integrated Result Tool：需先在此编辑器为 test suite 启用相应 flags（Output on pass / Output on fail / Pass value / Fail value / Per pin on pass / Per pin on fail）。
- **文档事实** Testflow Tool preference page：提供 "Synchronize selection between Flow Data Editor and Flow Sequence Editor" 选项。
- **文档事实** Printing a graphical representation of the testflow：File > Save as picture 把编辑器内容存为图片。
- **文档事实** Offline result emulation：该页要求在此编辑器中打开 testflow 后激活。

## 版本

**文档事实** Functional changes 记：Introduced before SmarTest 6.3.2；SmarTest 6.5.2 起 Flow Sequence Editor 取代 Graphical Testflow Editor；SmarTest 6.5.2 起 bin node 不支持 OOC (Out Of Control) rule。Elements of the Testflow Tool 的 Functional changes 还记：SmarTest 6.5.2 起 Flow Sequence Editor 集成到 SmarTest Eclipse Work Center，Properties view 取代 Testsuite view。

## 出处

- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.02_Flow_Sequence_Editor.htm`，主源，含编辑器说明、Related information 与 Functional changes，已用 `show.py` 读取。
- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03_Elements_of_the_Testflow_Tool.htm`，用于两个编辑器、同一 testflow 文件、Flow Data Editor 表格视图与版本说明，已用 `show.py` 读取。
- 其余关系与引文取自 `extract/objpack.py` 的入边索引。
