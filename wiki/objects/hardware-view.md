---
type: object
title: Hardware view
layer: gui
stage: run
tags: []
related: []
sources:
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.05.03_Hardware_view.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Hardware view

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,256 字符逐字取自** `<01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.05.03_Hardware_view.htm>` 及其子主题 `<01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.05.03.05_Profiling_of_DC_Scale_cards_with_Hardware_view.htm>`、`<01_Getting_started/01.01_SmarTest_Work_Center/01.01.08.08_Firmware_view.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Profiling of DC Scale cards with Hardware view）

### Utility serial configuration for DC profiling

The following screen shot shows a part of the DPS128 Hardware view.

The
Profile
 button at the bottom is marked in red and opens
the DPS Profile dialog.

You can define the configuration of sequencer‑controlled utility lines, which is
programmed to hardware before any pattern execution.

The UTSC firmware syntax is one of the following:

UTSC [1-8],[RW|RD][,MASK]

UTSC ([-,1-8),[RW|RD][,MASK]

For example:

UTSC 1,RW; UTSC (2,3),RW,MASK; UTSC (5-8),RD

After the pattern finishes, SmarTest applies:
UTSC ALL,OFF.

Multiple serial buses are supported. Each bus can range from 1 single utility block
to up to 8 consecutive blocks.

For example:

Single bus: 1-8. (Block 1 is master. Blocks 2-8 are slaves)

Two buses: 2-3,5-7 (Blocks 2 and 5 are masters. Others are slaves)

If the
Seq Ctrl'd Util Blocks
 field is empty, no sequencer
control is enabled during profiling.

The content of the
Seq Ctrl'd Util Blocks
 field is not
stored/restored after closing the dialog.

### Example（取自子主题 Firmware view）

As the following example shows, the
VECD?
 query returns vector data
from the sequencer memory in the range between 0 and 8, for the S0_1 pin.

Add the
$
 prefix to the query command to retrieve the binary data in a
readable format.

<!-- 语法节 end -->

## 是什么

**文档事实** Hardware view 是 Hardware Perspective 的一部分，与 Pin Browser view 关联。在 Pin Browser 中选中 pin 时，Hardware view 顶部显示该 pin 的 site 号、pin 名和通道号，图中显示与所选 pin 相关的测试系统电路。

**文档事实** 图中原理图是简化图，不精确表示系统中的实际硬件。

**文档事实** 文档列出四项功能。显示所选 pin 的当前设置。允许为调试修改部分设置。允许通过电流或电压测量评估修改。允许多个 Hardware view 比较不同 pin 的设置。

**文档事实** 执行测量代码后，结果显示在 Hardware view。若需要更新，屏幕底部出现警告，点 Refresh 按钮更新显示。

**文档事实** Hardware Perspective 页说明该视图显示数字通道参数与 relay 设置、relay 状态、DPS 参数，并可用它执行电压和电流测量。

**文档事实** offline 模式下 Hardware view 不一定能返回正确的硬件设置，尤其当硬件设置依赖 pattern-based conditional jumps 和 match loops 时。若 SmarTest 判断无法正确评估硬件状态，会在 ui_report 窗口发出 WARNING 消息，内容为 reported last DC state 可能不反映 online state。

**文档事实** 工具栏图标包括 Refresh、Link with editor and selection、Pin this view、Open new Hardware view、Zoom out、Zoom in、resize to graph default size、fit to screen、Setup preferences、Show or hide properties。Show or hide properties 仅对 RF pin 有效，用于显示或隐藏 RF board 当前硬件状态的表格。Refresh 会在执行 test method 后把视图中的硬件设置更新为 test method 的设置。Link with editor and selection 按下时，在 Pin Browser 中点 pin 会立即更新 Hardware view。

**文档事实** Pin this view 把 Hardware view 的显示固定到当前 pin。Open new Hardware view 打开一个显示同一 pin 设置的新 Hardware view，可用于比较不同 pin 的设置。

## 典型用法

**文档事实** 数字 pin。在 Pin Browser 选中数字 pin，Hardware view 显示该 pin 硬件的当前状态。可点击原理图中的 relay 改变 relay 状态，也可修改 Driver、Clamp、Comparator、Termination、Pin PMU、Board ADC 的设置。Driver setup 窗口改 driver levels，Clamp setup 窗口改 clamp mode 与 clamp 高低电压，Termination Mode Setup 窗口选择 termination mode，可选模式由 pin 连接的数字卡类型决定。

**文档事实** 数字 pin 的若干细节。Pin Scale 5000 通道支持通过单独 pin 做地线远端感测，Hardware view 中可查看所选 pin 是否启用 ground sense，线为黑色表示启用，置灰表示未启用。可用于差分模式的 pin 会在图中标出相邻通道。Board ADC 的 BADC relay 断开与闭合可打开不同窗口，分别做普通 DC 测量与高阻电压测量。

**文档事实** DPS 与 VI pin。选中 DPS/VI pin 后，Hardware view 显示该 pin 硬件的当前状态，可做电流测量、force/sense line 检查、DPS level setup、Surge tracker 测量以及设置 force/sense 与 gang connection 检查的最大电阻。DPS level setup 含 DPS force voltage、current limit、off current state 与 setup time。Status 字段显示 tester 处于 connected 或 disconnected。

**文档事实** DPS 测量的范围。在 DPS Measurement 窗口输入的 Pass Min 与 Pass Max 值须在 -200 A 到 +200 A 之间。可选择 Single Measurement 或 Looped Measurement，后者需输入以秒为单位的 loop rate。文档提醒这些窗口中的改动只用于调试，应据此改动测试 setup。

**文档事实** XPS256 的 line check 与 gang check。force/sense line 检查对 DC Scale XPS256 卡弹出 DPS force sense 窗口，输入以 Ohm 计的最大电阻后点 MEAS，点 DONE 后可在 Hardware view 看到 PASS 或 FAIL。检查 force/sense line 前必须确保测试系统处于 disconnected 状态。gang connection 检查仅 XPS256 有，同样输入最大电阻后测。Surge tracker 测量仅 DPS128 与 DPS64 有，输入高低阈值后点 Activate。

**文档事实** 执行测量。在 Hardware view 点 Measure，在 Measurement Dialogs 选 Focus Site Only，在 Measurement window 修改测量值，更改值以青色背景标记，点 MEAS。信号支持 multisite 测量的是 PS1600 与 DPS128HC。再在 Measurement Dialogs 选 All Active Sites，可查看所有活动 site 的结果概览，改过的值也会更新到 Hardware view。

**文档事实** 快速测量。已用 Hardware view 执行过一次测量后，点 Quick 可对 focus site 做快速重复测量，无需打开 Measurement window。

**文档事实** 同时比较多个 pin 与多个 site。在 Pin Browser 右键 pin 选 Show in Hardware 可打开该 pin 的 Hardware view，点 Pin this view 固定后，可再打开另一 pin 的 Hardware view 以比较设置。Link with Editor and Selection 取消选中时，可另开 Hardware view 显示更多信号。也可从 Hardware view 点 Measure 为关联信号打开 Measurement window，并在多个 Measurement window 中修改设置后分别点 MEAS。选择 Focus Site Only 修改某 site 设置后再选 All Active Sites，跨 site 不一致的值以黄色背景显示。

**文档事实** Profiling。DC Profiler 可测量并显示 pattern 执行期间的电流和电压波形，支持所有 DC Scale 通道的 DPS 与 PMU 工作模式。在 Hardware view 底部点 Profile 打开 DPS Profile 对话框，可设 Measure Range、Sampling Rate、Average Factor、Current 或 Voltage Measurement、Single 或 Looped Measurement。点 MEAS 后 Waveform view 显示所得波形，Looped Measurement 会持续重复直到关闭对话框或改选 Single Measurement。

**文档事实** Profiling 采样率。DPS128 在每 test processor 1 个通道时最高 100 ksps、最小周期 0.010 ms，2 至 8 个通道时 50 ksps、0.020 ms。UHC4T 在每卡 1 个通道时 100 ksps、0.010 ms，2 至 4 个通道时 50 ksps、0.020 ms。XPS256 为 1 Msps、0.001 ms。若 pin 处于 UNGANG 模式，不支持对电流做 DC profiling。

**文档事实** Profiling 会为所执行的测量在 Sample Code view 生成示例 test method 代码，可直接复制粘贴到测试方法程序。

**文档事实** Profiling 的 utility 串行配置使用 firmware 语法 UTSC。两种写法为 `UTSC [1-8],[RW|RD][,MASK]` 与 `UTSC ([-,1-8),[RW|RD][,MASK]`。示例为 `UTSC 1,RW; UTSC (2,3),RW,MASK; UTSC (5-8),RD`。pattern 结束后 SmarTest 应用 `UTSC ALL,OFF`。支持多条串行总线，每条总线可从 1 个 utility block 到最多 8 个连续 block。Seq Ctrl'd Util Blocks 字段为空表示 profiling 期间不启用 sequencer 控制，该字段内容在关闭对话框后不保存也不恢复。

**文档事实** Hardware view preference page 可设三项。Continuously refresh with an interval delay 与 Refresh Delay 控制连续刷新及间隔。Block Diagram Follows the Site in Focus 使 Hardware view 的硬件信息始终跟随 focus site。

## 和谁有关

**文档事实** Pin Browser view `01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.05.02_Pin_Browser_view.htm`。Hardware view 与之关联，选 pin 后显示该 pin 的 site、pin 名、通道号与电路。Pin Browser 页也说明选中数字或 DPS pin 后 Hardware view 显示相关电路，并允许改部分设置与观察结果。

**文档事实** Hardware Perspective `01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.05_Hardware_Perspective.htm`。Hardware view 是其中一部分，该页说明它显示数字通道参数与 relay 设置、relay 状态、DPS 参数，并可执行电压和电流测量。

**文档事实** Site Control Window `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.27_Site_Control_Window.htm`。数字 pin 的多 site 调试用 Site Control window 的 focus 按钮选择 site，Hardware view 的标号显示 focus site，设置修改只作用于该 site。

**文档事实** Hardware view preference page `01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.05.03.11_Hardware_view_preference_page.htm`。可设连续刷新与间隔，以及 Block Diagram Follows the Site in Focus。

**文档事实** Hardware view for digital pins `01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.05.03.03_Hardware_view_for_digital_pins.htm` 与 Hardware view for DPS and VI pins `01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.05.03.04_Hardware_view_for_DPS_and_VI_pins.htm`。分别说明数字 pin 与 DPS/VI pin 可修改的设置。

**文档事实** Profiling of DC Scale cards with Hardware view `01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.05.03.05_Profiling_of_DC_Scale_cards_with_Hardware_view.htm`。DC Profiler 的操作、采样率表与 UTSC 配置在该子主题。

**文档事实** DPS operating mode of DC Scale cards 与 PMU operating mode of DC Scale cards `02_System_reference/02.05_Test_Head_Cards/02.05.05.04_DPS_operating_mode_of_DC_Scale_cards.htm`、`02_System_reference/02.05_Test_Head_Cards/02.05.05.05_PMU_operating_mode_of_DC_Scale_cards.htm`。profiling 在两种模式下行为不同，这两篇是 Related information。

**文档事实** DC_PROFILING_DEFINE、DC_PROFILING_ENABLE、DC_PROFILING_ON、DC_PROFILING_OFF `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.24_DC_PROFILING_DEFINE.htm`、`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.25_DC_PROFILING_ENABLE.htm`、`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.26_DC_PROFILING_OFF.htm`、`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.27_DC_PROFILING_ON.htm`。它们是 profiling 对应的 L2 API。profiling 页说明 measureRange 参数在 DPS128 上被忽略，在 XPS256 上也不需要但须设为有效范围。

**文档事实** Sample Code view `01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.05.07_Sample_Code_view.htm`。profiling 后生成示例 test method 代码。

**文档事实** XPS256 profiling `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.03.05_XPS256_profiling.htm`。XPS256 可在 DPS 或 PMU 模式的 Hardware view 中 profiling。

**文档事实** XPS256 编程与测量页 `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.12_XPS256_programming_-_Kelvin_test___sense_connection_test.htm`、`02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.13_XPS256_programming_-_Measure_currents.htm`、`02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.14_XPS256_programming_-_Measure_voltages.htm`、`02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.10_XPS256_programming_-_Ganging.htm`。电流与电压测量、Kelvin 与 sense 连接检查、gang 连接测试都由 DPS 或 PMU 模式的 XPS256 Hardware view 支持。

**文档事实** XPS256 programming - Surge tracker `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.17_XPS256_programming_-_Surge_tracker.htm`。该页说明 XPS256 的 surge tracker 功能与对应 API，并说明 Kelvin test 与 sense connection test 由 DPS 或 PMU 模式的 Hardware view 支持。本页正文提到的 Surge tracker 测量则仅 DPS128 与 DPS64 有。

**文档事实** XPS256 programming - Current monitor `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.04_XPS256_programming_-_Current_monitor.htm`。配置为 current monitor output pin 的 pin 在 Hardware view 中不可见。

**文档事实** Termination mode `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.05.01_Termination_mode.htm`。可在 Hardware view 中查看和修改 Pin Scale 卡使用的 termination mode。

**文档事实** General Editing Features of the Spec Tool `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.30.02_General_Editing_Features_of_the_Spec_Tool.htm`。可用 Hardware view 对单个通道执行 disconnect 或 connect sequence。

**文档事实** Firmware view `01_Getting_started/01.01_SmarTest_Work_Center/01.01.08.08_Firmware_view.htm`。本页语法节的 VECD? 示例取自该页。Firmware view 可直接输入 firmware 命令并从 task history 选择，加 `$` 前缀取二进制返回，但不支持向 tester 下载二进制数据。

**文档事实** Views 与 93000 menu `01_Getting_started/01.01_SmarTest_Work_Center/01.01.08_Views.htm`、`01_Getting_started/01.01_SmarTest_Work_Center/01.01.11.01_93000_menu_and_its_tools.htm`、`02_System_reference/02.08_Setup_and_Result_Tools/02.08.02_93000_menu_and_its_tools.htm`。这些页把 Hardware view 列为 Work Center 的视图与工具之一。

## 版本

**文档事实** 主页 Functional changes 记载，Introduced before SmarTest 6.3.2。6.5.0 新增 Link with editor and selection 按钮与 Pin this view 按钮，并可打开多个 Hardware view。6.5.2 新增 Open new Hardware view 按钮与 RF hardware state 按钮。

**文档事实** 数字 pin 子主题 Functional changes 记载，6.5.0 去掉 DC measurement 窗口的 DC set 字段并新增 DC rail 字段，6.5.2 支持用 Board ADC 做高阻电压测量，6.5.3 在 Board ADC 连接到当前卡笼中任一数字通道时将其本地 DC rail 标红，并可在 Hardware view 改数字 pin 的 driver、clamp、comparator 设置。

**文档事实** DPS 与 VI pin 子主题 Functional changes 记载，6.5.3 可在 Hardware view 设 DPS level 与 VBump，7.10.3 新增控制 XPS256 force/sense line 检查与 gang connection 检查电阻的对话框。

**文档事实** 其余子主题 Functional changes 记载，Executing a measurement 于 7.10.0 引入；Quick measurements 于 7.10.0 与 7.6.1；Opening additional signals 于 7.10.0；Opening additional measurements 与 Changing settings in multiple Measurement windows 于 7.4.3；Finding non-matching settings across sites 于 7.6.1；Opening multiple Hardware views of different pins 于 6.5.0；Hardware view preference page 于 6.5.2；Profiling 于 7.2.0；Firmware view 于 6.5.2。

## 出处

- `01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.05.03_Hardware_view.htm`。主源，含功能列表、图标、offline 说明、Functional changes。
- `01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.05.03.01_Executing_a_measurement.htm` 至 `01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.05.03.11_Hardware_view_preference_page.htm`。数字 pin、DPS 与 VI pin、profiling、多视图、preference 等子主题全部读过。
- `01_Getting_started/01.01_SmarTest_Work_Center/01.01.08.08_Firmware_view.htm`。用于语法节示例的工具说明。
