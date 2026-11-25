---
type: object
title: Event Formatter
layer: gui
stage: results
tags: []
related: []
sources:
  - 02_System_reference/02.10_Data_Logging/02.10.02_Event_Formatter.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Event Formatter

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **4,841 字符逐字取自** `<02_System_reference/02.10_Data_Logging/02.10.02_Event_Formatter.htm>` 及其子主题 `<02_System_reference/02.10_Data_Logging/02.10.02.04_Shmoo_output_of_the_Event_Formatter.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Shmoo output of the Event Formatter）

A shmoo data log shown with Event Formatter is similar to the one
below.

```
======== Started Testsuite Shmoo_2D ============================================

******** Started Site : 1 ******************************************************
Equation Set 512; Spec Set 256; Timing Set 256
Equation Set 512; Spec Set 512; Level Set 512
Startlabel: spec_search

-------- Test Name: 714 parameters[1] -----------------------------------------
-------- Shmoo -----------------------------------------------------------------
Title: 714 parameters
Test Mode: pass/fail,cycle error count
Result Pins: @
Result Resolution: 1.000000
Description:

........ Shmoo Axis Information ................................................
X-Axis
TotalSteps: 10
LinearSteps: 1
Test Range: [0.000000 ... 1.000000]
Scale: Linear
=> Step Ratio: 0.100000
PrimaryValue: 0.500000
Parameter: Spec Variable
Spec: LEV.2.VIL[V]
SetupPins: I/O0,I/O1
Description:

Y-Axis
TotalSteps: 10
LinearSteps: 1
Test Range: [0.000000 ... 10.000000]
Scale: Linear
=> Step Ratio: 1.000000
PrimaryValue: 5.000000
Parameter: Spec Variable
Spec: TIM.2.tpd_CP_IOx[ns]
SetupPins: @
Description:

........ Shmoo Matrix ..........................................................
' ' = point not calculated
'.' = point passed
'*' = point failed
'E' = point returned an error

Shmoo Pin Number : 1
Shmoo TestMode Number : 2
Shmoo Pin Names : @;
Shmoo Test Modes : pass/fail;cycle error count;

Number Of Cells : 121

Pin: @, TestMode : pass/fail

00000000001
...........
01234567890
00000000000
00000000000
+---------->
0.000|...........
1.000|...........
2.000|...........
3.000|...........
4.000|...........
5.000|...........
6.000|...........
7.000|...........
8.000|...........
9.000|...........
10.000v...........

Pin: @, TestMode : cycle error count

0 0 0 0 0 0 0 0 0 0 1
. . . . . . . . . . .
0 1 2 3 4 5 6 7 8 9 0
0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0
+------------------------------------------->
0.000| 0 0 0 0 0 0 0 0 0 0 0
1.000| 0 0 0 0 0 0 0 0 0 0 0
2.000| 0 0 0 0 0 0 0 0 0 0 0
3.000| 0 0 0 0 0 0 0 0 0 0 0
4.000| 0 0 0 0 0 0 0 0 0 0 0
5.000| 0 0 0 0 0 0 0 0 0 0 0
6.000| 0 0 0 0 0 0 0 0 0 0 0
7.000| 0 0 0 0 0 0 0 0 0 0 0
8.000| 0 0 0 0 0 0 0 0 0 0 0
9.000| 0 0 0 0 0 0 0 0 0 0 0
10.000v 0 0 0 0 0 0 0 0 0 0 0

Executed Testmethod ac_tml.AcTest.Shmoo on Site 1: PASSED
******** Ended Site : 1 ******************************************************

******** Started Site : 2 ******************************************************
Equation Set 512; Spec Set 256; Timing Set 256
Equation Set 512; Spec Set 512; Level Set 512
Startlabel: spec_search

-------- Test Name: 714 parameters[1] -----------------------------------------
-------- Shmoo -----------------------------------------------------------------
Title: 714 parameters
Test Mode: pass/fail,cycle error count
Result Pins: @
Result Resolution: 1.000000
Description:

........ Shmoo Axis Information ................................................
X-Axis
TotalSteps: 10
LinearSteps: 1
Test Range: [0.000000 ... 1.000000]
Scale: Linear
=> Step Ratio: 0.100000
PrimaryValue: 0.500000
Parameter: Spec Variable
Spec: LEV.2.VIL[V]
SetupPins: I/O0,I/O1
Description:

Y-Axis
TotalSteps: 10
LinearSteps: 1
Test Range: [0.000000 ... 10.000000]
Scale: Linear
=> Step Ratio: 1.000000
PrimaryValue: 5.000000
Parameter: Spec Variable
Spec: TIM.2.tpd_CP_IOx[ns]
SetupPins: @
Description:

........ Shmoo Matrix ..........................................................
' ' = point not calculated
'.' = point passed
'*' = point failed
'E' = point returned an error

Shmoo Pin Number : 1
Shmoo TestMode Number : 2
Shmoo Pin Names : @;
Shmoo Test Modes : pass/fail;cycle error count;

Number Of Cells : 121

Pin: @, TestMode : pass/fail

00000000001
...........
01234567890
00000000000
00000000000
+---------->
0.000|...........
1.000|...........
2.000|...........
3.000|...........
4.000|...........
5.000|...........
6.000|...........
7.000|...........
8.000|...........
9.000|...........
10.000v...........

Pin: @, TestMode : cycle error count

0 0 0 0 0 0 0 0 0 0 1
. . . . . . . . . . .
0 1 2 3 4 5 6 7 8 9 0
0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0
+------------------------------------------->
0.000| 0 0 0 0 0 0 0 0 0 0 0
1.000| 0 0 0 0 0 0 0 0 0 0 0
2.000| 0 0 0 0 0 0 0 0 0 0 0
3.000| 0 0 0 0 0 0 0 0 0 0 0
4.000| 0 0 0 0 0 0 0 0 0 0 0
5.000| 0 0 0 0 0 0 0 0 0 0 0
6.000| 0 0 0 0 0 0 0 0 0 0 0
7.000| 0 0 0 0 0 0 0 0 0 0 0
8.000| 0 0 0 0 0 0 0 0 0 0 0
9.000| 0 0 0 0 0 0 0 0 0 0 0
10.000v 0 0 0 0 0 0 0 0 0 0 0

Shmoo picture has been saved in: /home/Devices/74HC299/shmoo/shmooPNG/shmoo_2D
Executed Testmethod ac_tml.AcTest.Shmoo on Site 2: PASSED
******** Ended Site : 2 ******************************************************

======== Ended Testsuite Shmoo_2D ==============================================
```

<!-- 语法节 end -->

## 是什么

**文档事实** Event Formatter 是用于交互式调试的 report generating tool；它有自己的 dialog window，可定制数据输出的格式与范围，文档称其为强大的 data logging tool。

**文档事实** 本章说明：如何激活 Event Formatter；如何使用 Event Formatter 为 report window 新增的菜单；如何用 Report Dialog window 控制输出；结果数据在输出中如何呈现；如何按需定制 Event Formatter。

**文档事实** 本章最后给出 Event Formatter 工作原理的背景，并强调编写自有 event-based report formatter 时的重要考虑。

**文档事实** Appendix A 说明 Event Formatter 是 SmarTest 随附的标准 event-based report formatter，构建文件位于 `/opt/hp93000/soc/formatter/EventFormatter` 目录；它充分利用 event data logging 能力，并把取回的数据写入 report window。

**文档事实** Data Retrieval Library 页说明 Event Formatter 构建在 DRL 之上。

## 典型用法

**文档事实** 激活方式：在 Report Formatter window 选择 EventFormatter 并点 Select；选择后自动设置 `log_events_enable` 系统 flag（即激活 event logging），随后读取 `.formatterrc` 配置 Event Formatter：先读 home 目录下的文件，没有则用默认 `.formatterrc.de`。

**文档事实** Report Dialog window 用于设置控制 Event Formatter 输出的选项，从 report window 的 Datalog 菜单选 Open Report Dialog 打开。

**文档事实** 文档说明可在 Report Dialog window 选择要记录的信息种类；report formatter 的输出始终包含 test program、application model level 与 test flow 的信息。

**文档事实** 记录 shmoo 时，若要把 shmoo setups 与 plots 记录到 report window，并把生成的 shmoo plots 保存为 .png 或 ASCII 文件，使用 Event Formatter；把 `.formatterrc.def` 复制为 home 目录下的 `.formatterrc` 并设 `shmoo_picture_generation` 为 1 可保存 .png，执行后文件路径显示在 Console view 与 Event Formatter 输出窗口。

**文档事实** 用 TEST API 记录测试数据并以 Event Formatter 显示报告时，必须把 report formatter 设为 EventFormatter 并启用所需 flags；系统提供的 Event Formatter 不把 event data log stream 上的 unreliable 状态写入 report window，但每个测试的 pass/fail 对 unreliable 结果显示空白，且该行为仅适用于 DC test 或 functional test 的 global pass/fail 结果。

**文档事实** Memory Test Plus 的 Logging formats 页说明 Event Formatter 记录 TEST_TYPE_MEMORY 类型事件，并支持 DRLPinSpecificAddresses 与 DRLRARepairResultsAttr 数据类型。

**文档事实** 子主题 Shmoo output of the Event Formatter 给出一个完整 shmoo data log 输出样例，已逐字收录在本页「语法 / 参数」节。

**建议** 先按 Activating the Event Formatter 激活并确认 `.formatterrc` 生效，再执行要记录的 test suite，否则 report window 不会按 Event Formatter 的格式输出。

## 和谁有关

- **文档事实** Data Retrieval Library（DRL），该页说明 Event Formatter 构建在 DRL 之上；附录 A 说明 Event Formatter 充分使用 event data logging 能力。
- **文档事实** Report window，Event Formatter 把取回的数据写入 report window，并为其新增菜单；Report Dialog 从 report window 的 Datalog 菜单打开。
- **文档事实** Activating the Event Formatter，该子主题说明在 Report Formatter window 选择 EventFormatter，并说明会自动激活 event logging 与读取 `.formatterrc`。
- **文档事实** Activating event data logging，激活 Event Formatter 会自动设置 `log_events_enable`；该页是 event logging 的说明入口。
- **文档事实** Report window menus、Report Dialog window、Standard output of the Event Formatter、Shmoo output of the Event Formatter、Fine result granularity、How the Event Formatter works、Settings for the Event Formatter、Handling of test suite flags by the Event Formatter、Report window resources、Running report formatters as standalone tools、Appendix A/B/C，这些页面都是本页列出的子主题，分别承载菜单、输出、设置、原理、文件与示例等内容。
- **文档事实** TEST API，该页说明用 TEST API 记录数据并以 Event Formatter 显示报告时，需把 report formatter 设为 EventFormatter 并启用 flags。
- **文档事实** Saving shmoo plots to png or ASCII files，该页把记录 shmoo 到 report window 并保存 .png/ASCII 的做法交给 Event Formatter。
- **文档事实** Logging formats and data types（Memory Test Plus 7.10.2），该页说明 Event Formatter 的 TEST_TYPE_MEMORY 事件类型与两个支持的数据类型。
- **文档事实** Yield monitor 示例（Test Program Management 与 Data Logging 两个版本），文档说 Event Formatter 使用与 yield monitor 相同的数据检索机制。
- **文档事实** SmarTest Data Formatter，Data Logging 总览页把 Event Formatter 与 SmarTest Data Formatter 并列列出。

## 版本

**文档事实** Functional changes 只记 Introduced before SmarTest 6.3.2，没有更早或更晚的版本条目。

## 出处

- `02_System_reference/02.10_Data_Logging/02.10.02_Event_Formatter.htm`，主源，含 Subtopics、章节说明与 Functional changes。
- `02_System_reference/02.10_Data_Logging/02.10.02.04_Shmoo_output_of_the_Event_Formatter.htm`，其样例被骨架逐字收入「语法 / 参数」节。
- 已用 show.py 读取 `02.10.02.01_Activating_the_Event_Formatter.htm`、`02.10.02.06_Report_Dialog_window.htm`、`02.09.01.16.02_How_to_capture_the_test_result_in_real_time.htm`、`02.08.04.25.03.07_Saving_shmoo_plots_to_png_or_ASCII_files.htm`、`02.10.02.12_Appendix_A__Event_Formatter_Files.htm`、`02.10.01.04_Data_Retrieval_Library.htm`，以核对激活、输出内容、shmoo、附录与 DRL 关系。
