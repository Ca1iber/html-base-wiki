---
type: object
title: XPS256 programming - DPS operating mode
layer: L2
stage: level
tags: []
related: []
sources:
  - 02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.07_XPS256_programming_-_DPS_operating_mode.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# XPS256 programming - DPS operating mode

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

**文档事实** XPS256 引脚在 DPS operating mode 下可以通过 level setups、APIs 或 SmartRDI 编程。

**文档事实** 要把 XPS256 引脚置于 DPS operating mode，需在 DPS Pins editor 中把它定义为 device power supply；与其他所有 DC Scale 卡一样，参数 Pol 要设为 POS。

**文档事实** 该模式的 force 与 clamp 设置以及动态行为由 level setup 控制；要访问卡的全部特性必须使用 equations，细节见 Equation based level setup 与 DPSPINS resources。

**文档事实** level setup 支持的参数包括以下几组。Connections and timing 有 connect_state、t_ms。Current 有 ilimit、ilimit_sink、ilimit_source、iout_clamp_rng、offcurr。Constant current check 有 disable_const_curr_check、ms_const_curr_disconnect、ms_const_curr_time_to_alarm。Dynamic behavior 有 capacitance、load_step_mode、current_filter_frequency、voltage_filter_frequency。Maximum voltage drop 有 max_voltage_drop_force、max_voltage_drop_return、warn_voltage_drop_force、warn_voltage_drop_return。Other 有 open_loop_protection、pulldown。Voltage 有 vout、vout_frc_rng。Voltage settling time 有 vout_rise_settling_t_ms、vout_rise_settling_t_ms_c2c、vout_fall_settling_t_ms、vout_fall_settling_t_ms__c2c。Voltage slew rate 有 vout_rise_t_ms_per_volt、vout_rise_t_ms_per_volt_c2c、vout_fall_t_ms_per_volt、vout_fall_t_ms_per_volt_c2c、voltage_slew_rate。

**文档事实** connect_state 支持 norm、ungang、himp 三种连接状态。默认值 norm 可以在 Level setup tool 的 DPS Setup window 中选择，也可以通过命令 PSLR 编程，但不能在 level setup equations 中显式编程；要在 equations 中取默认 norm，必须省略 connect_state 参数。

**文档事实** SmartRDI 的 dc() API 覆盖该模式下 XPS256 引脚的全部设置功能，同时支持 code-based mode 与 pattern-based mode。电压或电流测量由 API DPS_TASK 覆盖；pattern-based 的 setup 与测量由 DC events 支持。

## 典型用法

**文档事实** 文档建议用 level setup 编程基本设置，然后用 SmartRDI 的 pattern-based mode 或 DC events 应用变更。

**文档事实** 需要卡的全部特性时，用 Equation based level setup 配合 DPSPINS resources；要取默认连接状态 norm 时不要在方程里写 connect_state。

**文档事实** 代码式设置走 SmartRDI 的 dc() API，测量走 DPS_TASK，pattern 级 setup 与测量走 DC events；pattern 的最大频率另见 Minimum period / maximum frequency of the sequencer。

**文档事实** XPS256 的 Hardware view 在 DPS operating mode 下提供 Measure、Check Status Flags、Profiling、Force Sense Check、Surge Tracker、Max Voltage Drop、Measure Voltage Drop、Check Gang Connection 按钮。Measure 对话框可为测量接通 DUT 板上的电容，并定义相关 utility pin、引脚目标状态与目标电容；白色字段可在子对话框中修改，例如 DPS Protection 对话框可改最大电压降与 Open Loop Protection。

**文档事实** Hardware view 顶部可选 Focus Site Only 或 All Active Sites。前者只显示 focus site 的测量结果，子对话框中白色字段的修改只作用于 focus site；后者显示所有 active site 的结果，修改作用于所有 active site，设置不同的字段以黄色高亮并能用 tooltip 查看差异。All Active Sites 下由 Measure、Max Voltage Drop、Measure Voltage Drop、Force Sense Check 或 Check Gang Connection 触发的测量会在所有 active site 执行，并在右侧打开结果表；结果表只显示最后一次测量，可按列排序和用蓝色首行过滤，Export 按钮可导出 CSV。

## 和谁有关

**文档事实** DPS Pins editor 决定引脚是否处于该模式，因为它把 XPS256 定义为 device power supply。

**文档事实** Level setup tool 及其 Equation based level setup、DPSPINS resources 决定 force、clamp 与动态行为；DPS Setup window 与命令 PSLR 参与 connect_state 默认值 norm。

**文档事实** SmartRDI 的 dc() API 与 Setting up DC Scale pins with SmartRDI 是完整的软件设置入口；DPS_TASK 负责测量；DC events 负责 pattern-based setup 与测量。

**文档事实** 文档的 Related information 与正文链接把它与 XPS256 programming - PMU operating mode、XPS256 operating modes、DPSPINS、DPSPINS resources 关联。硬件视图功能分别见 XPS256 status flags、XPS256 profiling、XPS256 programming - Kelvin test / sense connection test、XPS256 programming - Surge tracker、XPS256 programming - Voltage drop measurement、XPS256 programming - Ganging、XPS256 programming - Open loop protection、XPS256 programming - Current monitor、XPS256 programming - Measure currents、XPS256 programming - Measure voltages。

**文档事实** DPS_PIN_TASK 文档写明该功能仅在 DPS operating mode 的 XPS256 specifications 下支持。

**文档事实** 文档把 PMU operating mode 列为相关主题，两者是 XPS256 的两种操作模式，见 XPS256 operating modes。

## 版本

**文档事实** 该主题在 SmarTest 7.10.1 引入。

**文档事实** SmarTest 7.10.3 改进了 Hardware view，增加 site selection 与 multisite results table。

## 出处

- `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.07_XPS256_programming_-_DPS_operating_mode.htm`
