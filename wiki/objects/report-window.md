---
type: object
title: Report window
layer: gui
stage: results
tags: []
related: []
sources:
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.13_Report_window.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Report window

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,153 字符逐字取自** `<01_Getting_started/01.01_SmarTest_Work_Center/01.01.13_Report_window.htm>` 及其子主题 `<01_Getting_started/01.01_SmarTest_Work_Center/01.01.13.03_Configuring_the_messages_printed_in_the_Report_Window.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Examples（取自子主题 Configuring the messages printed in the Report Window）

### Printing messages for passed and failed sites in the Report Window

This example shows how you can configure the

.testflow.ReportUiOutput.user_def
 file to print messages in the

Report Window
 for all passed and failed sites after a testflow is
executed:

```
<passed>Site: %site -> Bin: %bin -> PASS (Cool)
<failed>Site: %site -> Bin: %bin -> FAIL (Bad)
#<text> This is an example for a commented line (using "#" at the beginning)
```

The messages that are printed in the Report Window are as in the following figure:

### Printing messages for failed sites only in the Report Window

This example shows how you can configure the

.testflow.ReportUiOutput.user_def
 so that only messages for the failed
sites are printed in the
Report Window
:

```
<failed>Site : %site -> Bin: %bin -> FAIL (Bad)
```

### Printing messages in the Report Window for the failed sites after a test suite is executed

This example shows how you can configure your

.testflow.ReportUiOutput.user_def
 file to print a message in the

Report Window
 for the failed sites after a test suite is executed:

```
<failed>TestSuite: %testSuiteName -> Site: %site -> FAIL
```

<!-- 语法节 end -->

## 是什么

**文档事实** Report window 持续、即时地反馈系统上正在发生的事情；窗口顶部两行持续监控硬件状态与系统性能。

**文档事实** Report window 在软件启动时即打开，并在整个 SmarTest 使用期间保持打开；若软件意外关闭，它把记录的数据写入 `/tmp/ReportWindow.dump`。

**文档事实** SmarTest 的图形界面基于 X window system；可修改 `/opt/hp93000/soc/pws/data/.Xdefaults` 中 report window 的 Geometry 资源来改变其大小与屏幕位置。

**文档事实** Report window 的行数始终保持在 5000 到 10000 之间；若要改变默认值，须修改上述文件中的 `XReport.purgeLines` 与 `XReport.maxLines` 资源。修改任何 X 资源后，须把新值提供给 system controller。

## 典型用法

**文档事实** 进行特性测试时，data log report section 用于报告测量值。

**文档事实** Datalog 菜单可打开或关闭 value logging（会覆盖此前已做的同类设置），也可显示 bin statistics 并从 Datalog 清除 bins。

**文档事实** 可配置在 testflow、test suite 或 run configuration 被手动执行后 Report Window 打印的消息，配置写在 `.testflow.ReportUiOutput.user_def` 文件中；语法节示例包括：用 `<passed>Site: %site -> Bin: %bin -> PASS (Cool)` 与 `<failed>...` 同时报告通过和失败的 site；只用 `<failed>` 报告失败 site；以及 test suite 执行后打印 `<failed>TestSuite: %testSuiteName -> Site: %site -> FAIL`。以 `#` 开头的行是注释行。

**文档事实** 文档称该消息配置面向 "所有通过和失败的 site" 或 "仅失败的 site"，两种粒度都有示例。

**推断** 消息配置需在对应执行动作（testflow/test suite/run configuration）被手动执行之后才体现在 Report Window 上，因为原文表述是 "after ... is manually executed"。

## 和谁有关

- **文档事实** V93000 system status line — 该页对 Report window 的描述（持续反馈、顶部两行监控硬件与性能）与本页一致，并链接到本页作详情。
- **文档事实** Configuring the messages printed in the Report Window — 本页子主题，给出 `.testflow.ReportUiOutput.user_def` 的三种示例，语法节逐字收录。
- **文档事实** Loading Progress Meter、Printing the hardware configuration and license checkout information — 本页子主题，分别对应加载进度显示与硬件配置/许可签出信息的打印。
- **文档事实** Console view、Console view: System console、Console view: Data log console — 本页 Related information 列出，是与之并列的输出视图。
- **文档事实** Collecting log files if SmarTest crashed — Related information 列出，与 Report window 意外关闭时写 `/tmp/ReportWindow.dump` 的机制相关。
- **文档事实** Timing Diagram Tool、Using the Timing Diagram Tool、How data is displayed in the timing diagram — 说明若有 pin 未显示，SmarTest 会在 Report window 发出警告消息。
- **文档事实** Debugging a testflow、Alphabetical list of flags — 说明可设 Debug Mode flag 选择调试执行期间在 Report window 显示的调试信息级别。
- **文档事实** FwGuard、rdi.func__.startVec、rdi.func__.stopVec — 说明 SmarTest 会在 Report window 打印相应消息或限制说明。
- **文档事实** Pull-down function（多页）、Scalable A-Class test head — 说明 SmarTest 启动或硬件确认时会在 Report window 显示 pull-down 电阻状态、测试头型号等信息。

## 版本

**文档事实** Functional changes 仅记载：Introduced before SmarTest 6.3.2。

## 出处

- `01_Getting_started/01.01_SmarTest_Work_Center/01.01.13_Report_window.htm`，主源，含 X window 配置、logging panes、消息配置入口、Related information 与 Functional changes。
- 语法节子主题 `01_Getting_started/01.01_SmarTest_Work_Center/01.01.13.03_Configuring_the_messages_printed_in_the_Report_Window.htm`。
