---
type: object
title: XPS256 status flags
layer: L2
stage: level
tags: []
related: []
sources:
  - 02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.02_XPS256_status_flags.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# XPS256 status flags

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

**文档事实**：本页是 XPS256 卡的状态标志参考。XPS256 提供若干自保护机制，并用标志指示工作状态、异常工况或测试结果。文档把标志分为三组：

- **Status flags and warnings**：Clamp distance too low；surge tracker 的 6 个标志（High voltage or current of surge tracker exceeded、High voltage of surge tracker reached、High current of surge tracker reached、Low voltage or current of surge tracker exceeded、Low voltage of surge tracker reached、Low current of surge tracker reached）；Measurement range change failed；Range overflow；Voltage drop force warning；Voltage drop return warning。
- **Operating state**：Constant current、Constant voltage。
- **Safety and self-protection**：Current limit disconnect、DUT board disconnect、Overpower / Overcurrent / Power budget exceeded、Overtemperature、Overvoltage、Safety line、Unregulated、Voltage drop force、Voltage drop return。

**文档事实**：每个标志按 Trigger → Action → Availability → API(s) 说明，Availability 一律为 per channel。Operating state 的两个标志只用于指示（"for information only"，不执行附加动作）；Safety and self-protection 组的动作由卡或通道控制逻辑自动执行，"cannot be blocked or disabled"。

**文档事实**：各标志的动作后果不同：Clamp distance too low 把施加的 clamp 值调整为硬件规定的最小 clamp 距离，并在 UI report 窗口给出警告；Measurement range change failed 与 Range overflow 也给出警告（Range overflow 还把施加值限制到该量程的最大值）；Overpower / Overcurrent / Power budget exceeded、Overtemperature、Overvoltage、Unregulated 会断开相关通道（Overpower 条件是过流持续超过 50 ms，Unregulated 是输出级到限持续超过 10 ms）；Current limit disconnect 断开相关通道或整个 ganging group；DUT board disconnect 断开所有 XPS256 通道；Safety line 只断开分配给对应 trigger source 的 XPS256 通道；Voltage drop force / Voltage drop return 默认保持连接，只有对应 pin 的 `Vdrop Disco` 为 ON 时才断开。

**文档事实**：本页另有 "DC event status" 一节，列出 `TSST?` 返回的、XPS256 支持的 DC Event test result flags 与 test status flags 位表；test result 中部分位可由 DC events 的成员函数按 measurement event 开关（示例 `...clampChecks()`、`...outOfRangeCheck()`），test status 位不可开关，两类都在下一次 functional test 开始时清除。

## 典型用法

**文档事实**：读标志用对应的 `DPS_AUX_TASK` getter：`getClampDistanceTooLow()`（clamp distance）、`getSurgeTrackerStatus()`（surge tracker 六个标志）、`getRangeError()`（measurement range change failed）、`getRangeOverflow()`、`getVoltageDropForceWarn()` / `getVoltageDropReturnWarn()`、`getConstantCurrent()` / `getConstantVoltage()`、`getConstantCurrentLimitDisconnect()`、`getDutBoardDisconnect()`、`getOvercurrent()`、`getOvertemperature()`、`getOvervoltage()`、`getSafetyLine()`、`getUnregulated()`、`getVoltageDropForce()`、`getVoltageDropReturn()`。总入口是本页 Related information 列出的 `DPS power flags - get...() functions` 与 `DPS status flags - get...() functions`。

**文档事实**：Voltage drop force warning / Voltage drop return warning 仅供信息，文档要求至少在每个 testflow 结束时查询标志（"You should query the flags at least at the end of the testflow"）。

**文档事实**：testflow 中通道被断开后的恢复顺序：确认断开原因已消除 → 用上述 API 检查标志 → 由 SmarTest 执行 disconnect（报告窗口显示错误信息并清除状态标志）→ connect。硬件视图中的步骤不同：PMU 模式在 ADC 子面板以 relay action = NT 启动一次 dummy measurement；DPS 模式点击 Eclipse Work Center 工具栏的 Disconnect 按钮，然后 Connect。

**文档事实**：取 DC event 的累积结果用 `TSST?`；本页给出 XPS256 支持的 test result 位（bit0 Upper limit、bit1 Lower limit、bit2 Global status、bit3 Low clamp violation、bit4 High clamp violation、bit5 Range underflow（不支持）、bit6 Range overflow、bit7 Distance too small/internal buffer overflow、bit8 Lost measurements、bit9 Type mismatch、bit10 Wrong hardware state）与 test status 位（bit0 Current sink limit reached、bit1 Current source limit、bit2 Clamp low was reached、bit3 Clamp high was reached、bit4 Range underflow、bit5 Range overflow）。

**建议**：把关键 getter 放进 testflow 收尾与异常处理路径，不要只在失败后临时查询；文档只对 voltage drop warning 明确"至少每个 testflow 末尾查一次"。

## 和谁有关

- `DPS power flags - get...() functions` / `DPS status flags - get...() functions`：**文档事实**——本页 Related information 直接列出，且表中每个 flag 的 API(s) 行给出属于这两个系列的具体 getter；它们是本页标志的程序侧读取入口。
- `DPS_AUX_PIN_TASK.checkSurgeTracker()`：**文档事实**——该页说明对 XPS256 它读取 "High voltage of surge tracker reached"、"High current of surge tracker reached"、"Low voltage of surge tracker reached"、"Low current of surge tracker reached" 的状态，并写 "refer to XPS256 status flags"；`DPS_AUX_PIN_TASK.checkPowerFlags()` 的入边语境同样是 "XPS256 status flags"。
- `DPSPINS resources`：**文档事实**——本页把 `warn_voltage_drop_force`、`warn_voltage_drop_return`、`ms_const_curr_time_to_alarm`、`ms_const_curr_disconnect`、`disable_const_curr_check`、`max_voltage_drop_force`、`max_voltage_drop_return` 作为 DPS 模式下各标志的阈值/延时参数；该页入边也多次写 "refer to ... in XPS256 status flags"。
- `XPS256 programming - Default values` / DC Scale Safety editor：**文档事实**——本页说 `Vdrop Hold time` 与 `Vdrop Disco` 只能在 DC Scale Safety editor 设置（参数条目见 `XPS256 programming - Default values`），它们决定电压降标志的置位保持时间与是否断开。
- `XPS256 surge tracker`、`XPS256 safety line and DUT board disconnect`：**文档事实**——本页在这两组标志的 Trigger/Note 中直接链接这两篇，前者定义 surge tracker，后者定义 Safety line shutdown 与 DUT board disconnect shutdown 信号的来源。
- `XPS256 programming overview`、`XPS256 sitemap`：**文档事实**——这两篇的入边都出现 "XPS256 status flags"（sitemap 的语境是 "Status flags - Default values"），说明 XPS256 编程总览与站点地图把本页收在其主题列表里。
- `TSST? - (TeSt STatus)`：**文档事实**——本页 "DC event status" 一节说明 `TSST?` 返回什么，并给出 XPS256 的位定义。
- `DPS_AUX_TASK.getStatusWithoutConstVol()`、`getStatusWithoutConstCur()`、`getAllStatus()`：**文档事实**——这三个 getter 出现在 Operating state 的 Constant current / Constant voltage 行，用于读取工作状态（前两个分别排除对方状态）。
- `PSAS?`：**文档事实**——PSAS? 的 Related information 列出本页；**推断**：PSAS? 的 bit0–bit16 名称（Constant voltage … Voltage drop return warning）与本页标志同名，二者分别从命令侧与 API 侧描述同一组 DPS 状态；文档没有直接声明两者等价。

## 版本

**文档事实**：Functional changes 写 "Introduced in SmarTest 7.10.1"，并记录 "SmarTest 7.10.2: New 'DUT board disconnect' and 'Safety line' status flags." 文档未给出其它版本差异。

## 出处

- `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.02_XPS256_status_flags.htm`——本页正文、标志表、API 行、DC event 位表与 Functional changes 均取自本篇。