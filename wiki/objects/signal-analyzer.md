---
type: object
title: Signal Analyzer
layer: gui
stage: results
tags: []
related: []
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.26_Signal_Analyzer.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Signal Analyzer

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **90 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.26_Signal_Analyzer.htm>` 及其子主题 `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.26.03.04_Rectangular_Plot.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Rectangular Plot）

The following picture illustrates an S-Parameter rectangular plot in the Smith Chart
Tool.

<!-- 语法节 end -->

## 是什么

**文档事实** Signal Analyzer 提供一个 waveform viewing environment，具备可定制、易用的图形显示与分析能力，用于有效调试测试应用。

**文档事实** 主窗口分为两个子面板：Waveform Navigator Tool (WNT) 显示当前 device file directory 中保存的 waveform 列表；Waveform Graphs Tool (WGT) 用于创建、查看、download、upload 与分析 waveform，并统一显示 setup data 与 result data。Navigator 可折叠，以放大其他面板。

**文档事实** 功能通过菜单栏访问；工具栏覆盖 Graph Customization、Hardware Access、Cursor Functions、Marker Functions、Slope Marker Functions、User Defined Functions。User Defined Panel 的函数可用 Data Display API 与 DSP Test Method API 编程，且独立于 test method 程序。大部分功能也可通过 Data Display API 以编程方式控制。

**文档事实** 文档列出的功能族包括：载入 data log 并选择其中的 waveform（Load Datalog、Select Waveform）；生成任意 waveform（Generate 及其 Waveform Editor、Multitone Setup、Waveform Equation、Point-by-Point、Binary Sequence Editor、Marker Setup）；修改 waveform（Test Mask、Translate、Inject Jitter、Cable Simulation），Tools 菜单还提供 Coherent Reconstruction；计算谐波与互调频率（Harmonics）；为 DSM 测试设置 vector（DSM）；复制粘贴与删除 waveform；以及给 waveform 分配 user defined function。

**文档事实** Smith Chart 是 Signal Analyzer 中引入的一种 graph type，用于传输线与匹配电路问题。其子主题包括 Smith Chart format setting、Reflection Coefficient representation、Data File、Rectangular Plot、Impedance Matching、Port Extension。Demodulation in the Signal Analyzer 也是其子主题族。

**文档事实** 一个 Signal Analyzer 内可打开多个 Data Display Panel，但在一个 SmarTest 环境内不能同时运行多个 Signal Analyzer。

**推断** 从文档以 waveform、Smith Chart、demodulation 与 ARRAY/DGT 为核心的说明看，该工具面向已采集模拟波形的查看、测量与调试，而不是数字 pass/fail 结果的统一分析入口；数字结果分析由 analysis views、Integrated Result Tool 等承担。

## 典型用法

**文档事实** 启动方式有四种：V93000 菜单 `93000 > Analog > Signal Analyzer`；Test Program Explorer 中双击 `Waveform` 项；pattern editor 选中单元格后用快捷菜单 `Edit with Signal Analyzer`；Hardware Response Emulator 的 ARRAY_X 对话框点 `Signal Analyzer`。

**文档事实** 调试从硬件采集的 waveform 时，先用 PUT_DEBUG API 或 Data Display API 把 waveform 取回并送入 Signal Analyzer。文档示例为 `Analog.DGT("dgt1").getWaveform()` 与 `Analog.DGT("dgt2").getWaveform()`，再分别 `PUT_DEBUG("dgt1","first",waveform1)`、`PUT_DEBUG("dgt2","second",waveform2)`；WNT 会逐条列出这些 waveform。

**文档事实** 在 WNT 中右键某行并选 `Upload (New Window)`，waveform 会显示到 WGT 的新 waveform display area，同时在 WNT 的新分类下列出。

**文档事实** 从 pattern editor 进入时，若 waveform 存在并在 Signal Analyzer 中获得焦点，会同时打开 Download Vector Memory 对话框；pattern editor 数据未过期时用其值填充，否则填默认值。手动打开该对话框则显示先前配置值或默认值。

**文档事实** 波形分析可用 WGT 的 Overlay Waveforms、Change Graph Style、Mask Waveform、Label Trace、Cursors、Markers、Multiple Data Display Panels；图形侧可用 File > Save Trace As、Rectangular Plot，以及 Smith Chart 的格式设置、反射系数表示、Data File、Impedance Matching、Port Extension。

**建议** 先确认 WNT 中目标 waveform 已选中，再执行 mask、translate、jitter 等修改和 Save Trace As，避免把结果保存到错误 trace 或对错误 waveform 做修改。

## 和谁有关

- **文档事实** Pattern Editor：其快捷菜单 `Edit with Signal Analyzer` 打开 Signal Analyzer，并在有焦点 waveform 时打开 Download Vector Memory 对话框（Starting Up Signal Analyzer 子主题）。
- **文档事实** Hardware Response Emulator：其 ARRAY_X 对话框提供 Signal Analyzer 入口（同一子主题）。
- **文档事实** Data Display API 与 DSP Test Method API：User Defined Panel 的函数由二者编程；Data Display API 还可编程控制大部分功能；Data Display API 与 PUT_DEBUG 是把硬件 waveform 送入 Signal Analyzer 的通道（Elements 与 Passing Waveform 子主题）。
- **文档事实** PUT_DEBUG API：Passing Waveform into Signal Analyzer 用它把 waveform 送入 WNT。
- **文档事实** Smith Chart Tool：Smith Chart 是 Signal Analyzer 的 graph type；其子主题覆盖格式、反射系数、Data File、Rectangular Plot、Impedance Matching 与 Port Extension。
- **文档事实** Demodulation in the Signal Analyzer：Signal Analyzer 的子主题族，含访问解调工具、指定 waveform 与标准、编辑输入参数、执行解调、验证结果、配置参数列表。
- **文档事实** Per-Pin Signal Generator (PPSG)：PPSG 集成在 Signal Analyzer 中，从其 Tool 菜单启动。
- **文档事实** Normal DSM setup：waveform DC/DC power units 也可用 Signal Analyzer Tool 下载。
- **文档事实** Timing Diagram Tool：其页引用 Signal Analyzer（objpack 入边）。
- **文档事实** 93000 menu and its tools 与 Tools grouped by function：Signal Analyzer Tool 被列为 SmarTest 工具之一（objpack 入边）。
- **文档事实** De-Embedding page of the Channel Attributes Editor：该页提到 signal analyzer plotting of parameters，并引用 Signal Analyzer。
- **文档事实** Rectangular Plot：其示例为 Smith Chart Tool 中的 S-Parameter rectangular plot，本页语法节的逐字示例即取自该子主题。

## 版本

**文档事实** 主篇 `02.08.04.26_Signal_Analyzer.htm` 没有 Functional changes 段。子主题 Elements of the Signal Analyzer Tool 的 Functional changes 记：Introduced before SmarTest 6.3.2；SmarTest 6.5.3 起，用 FFT 分析的 waveform 大小可为任意整数。子主题 Smith Chart Tool 的 Functional changes 记：Introduced in SmarTest 7.0.3。

**推断** 因此该工具在 SmarTest 6.3.2 之前已存在，Smith Chart 图形是 SmarTest 7.0.3 新增的能力。

## 出处

- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.26_Signal_Analyzer.htm`，主源，含子主题列表与首段定义。
- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.26.01_Using_the_Signal_Analyzer_Tool.htm`、`...01.01_Starting_Up_Signal_Analyzer.htm`、`...01.02_Passing_Waveform_into_Signal_Analyzer.htm`、`...02_Elements_of_the_Signal_Analyzer_Tool.htm`、`...03_Smith_Chart_Tool.htm`，用于启动方式、波形传入、界面元素与 Smith Chart 说明，已用 `show.py` 读取。
- 入边关系与引文取自 `extract/objpack.py` 的入边索引。
