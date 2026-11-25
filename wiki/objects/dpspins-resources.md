---
type: object
title: DPSPINS resources
layer: L2
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.02.03.07.01_DPSPINS_resources.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# DPSPINS resources

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **734 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.02.03.07.01_DPSPINS_resources.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Examples

### Example 1: All resource keywords

See
`Example 1: Copy/paste example with all resource keywords`（raw: `16886.htm#_16886__copy_paste_example`）
 in
`DPSPINS`（raw: `16886.htm`）
 for a copy/paste example with all
resource keywords.

### Example 2: Using the voltage ramp parameters

Parameter

t_ms
 cannot be specified in combination with one of the parameters

vout_rise_t_ms_per_volt
(_c2c
),

vout_fall_t_ms_per_volt
(
_c2c
),

vout_rise_settling_t_ms
(
_c2c
), and

vout_fall_settling_t_ms
(
_c2c
). Valid examples
are

```
t_ms=50
```

or

```
vout_rise_t_ms_per_volt=10
vout_fall_t_ms_per_volt=10
vout_rise_settling_t_ms=50
vout_fall_settling_t_ms=70
```

For further details see also
`DPS connect setup time and voltage ramps`（raw: `125205.htm`）
.

<!-- 语法节 end -->

## 是什么

**文档事实**DPSPINS resources 的参数定义 DPS pin 在 equation based level setup 中的行为，必须用特定关键字和值来定义资源参数。文档按功能把参数分组：

- Connections and timing：connect_state、t_ms
- Current：ilimit、ilimit_sink、ilimit_source、iout_clamp_rng、offcurr
- Constant current check：disable_const_curr_check、ms_const_curr_disconnect、ms_const_curr_time_to_alarm
- Dynamic behavior：capacitance、load_step_mode、current_filter_frequency、voltage_filter_frequency
- Maximum voltage drop：max_voltage_drop_force、max_voltage_drop_return、warn_voltage_drop_force、warn_voltage_drop_return
- Other：ms_fast_preload、open_loop_protection、protect、pulldown
- Voltage：vout、vout_frc_rng
- Voltage settling time：vout_rise_settling_t_ms(_c2c)、vout_fall_settling_t_ms(_c2c)
- Voltage slew rate：vout_rise_t_ms_per_volt(_c2c)、vout_fall_t_ms_per_volt(_c2c)、voltage_slew_rate

**文档事实**正文含一张“Resource parameter / Expression / Description”的大参数表，并给出 UHC4T force line 上 max_voltage_drop_force + max_voltage_drop_return 之和受编程 force 电压限制的约束图。

**文档事实**文档明确：不检查表达式中各 spec 的单位是否兼容或缩放是否正确，需用户自行保证表达式定义正确。

**推断**该页是 DPSPINS 父页的资源关键字子集：本页只讲“资源参数”，DPSPINS 本身还含布局/使用层面的内容（Related information 指向 DPSPINS 可佐证）。

## 典型用法

**文档事实**这些关键字写在 equation based level setup 的 DPSPINS 语句中。文档（DPS128/DPS64 power budget 与 UHC4T setup）给出的写法类似：

```
DPSPINS VDD
vout = 1.8
vout_frc_rng = 3.5 #max bump voltage
```

以及 UHC4T 的（原文为单行，此处仅按参数拆行）：

```
DPSPINS UHC4T_dps2 protect
vout = 3.3
ilimit = 1000
```

**文档事实**电压斜坡有两种写法且互斥：要么只写 `t_ms=50`，要么写 `vout_rise_t_ms_per_volt=10`、`vout_fall_t_ms_per_volt=10`、`vout_rise_settling_t_ms=50`、`vout_fall_settling_t_ms=70`；t_ms 不能与任一 vout_rise/fall_* 参数同时指定。更多见 DPS connect setup time and voltage ramps。

**文档事实**Example 1 指向 DPSPINS 父页中的 copy/paste 全关键字示例。

**建议**文档要求用户自行保证表达式中单位/缩放一致（不自动校验）。

## 和谁有关

- `02.08.04.14.02.03.07_DPSPINS.htm`：父页；本页是其资源关键字说明。
- `02.08.04.14_Equation_based_level_setup.htm`：这些参数所在的 equation based level setup。
- `02.08.04.14.06.01.02_DPS_connect_setup_time_and_voltage_ramps.htm`、`...02.02_DPS_pins_with_voltage_ramps.htm`、`...02.02.01_Voltage_ramps.htm`、`...02.02.02_Voltage_ramp_example.htm`：t_ms 与 rise/fall 斜坡参数的详细说明与图形；Voltage ramps 页用 vout_rise/fall_t_ms_per_volt(_c2c) 计算步数。
- `02.08.04.14.06.01.03_Using_the_UNGANG_connect_state_with_DC_Scale_DPS_cards.htm`：connect_state=ungang 的用法。
- UHC4T 系列（`02.05.05.02.03...`、`02.05.05.02.05...`、`UHCM` 命令）：UHC4T 特有参数（protect、ms_fast_preload、max_voltage_drop_force/return、disable_const_curr_check 等）都回指本页；文档说明要用 UHC4T 全部特性必须使用 equations 与 DPSPINS resources。
- `PSSR` / `PSLV` 命令：PSSR 的 rise/fall 与 PSLV 的 setup_time 互斥，这一规则同样适用于 t_ms（回指 DPSPINS / DPSPINS resources）。
- `02.05.05.01.09_DPS128___DPS64_specific_setup_tasks.htm`：Level Setup 工具会显示 DC Scale 卡当前生效的 DPSPINS 资源设置，并列出 DPS128/DPS64 改变/引入的资源。
- `02.11.01.04.07_Setting_up_additional_DC_levels_and_options.htm`、`02.09.03.04.12_Off_DC_levels_table.htm`：DC level / off level 设置使用同一组参数（如 connect_state）。
- XPS256：Functional changes 记 7.10.1 支持 XPS256，并新增若干面向 XPS256 的参数；7.10.3 新增 open_loop_protection。

## 版本

**文档事实**本页 Functional changes：

- Introduced before SmarTest 6.3.2
- SmarTest 6.5.3：新增 vout_rise_t_ms_per_volt、vout_fall_t_ms_per_volt、vout_rise_settling_t_ms、vout_fall_settling_t_ms；修改 max_voltage_drop_force、max_voltage_drop_return 的电压限值
- SmarTest 6.5.4：增强并扩展 connect_state=ungang 支持（6.5.4.10）
- SmarTest 7.1.0：新增 vout_rise/fall_t_ms_per_volt_c2c、vout_rise/fall_settling_t_ms_c2c；修改 t_ms 定义与范围（连接建立时间 -2147483647 到 217483647 ms）；修改 vout_rise/fall_settling_t_ms 范围为 -10000 到 10000 ms
- SmarTest 7.1.3：新增 off current 模式 act_min、act_open
- SmarTest 7.1.4：进一步扩展 ungang 支持
- SmarTest 7.2.1：新增/修改 ilimit、ilimit_source、ilimit_sink
- SmarTest 7.3.1：新增/修改 connect_state、voltage_filter_frequency、current_filter_frequency；支持 DC Scale PVI8 卡
- SmarTest 7.3.2：支持 DC Scale UHC4T 卡
- SmarTest 7.4.0：支持 DC Scale AVI64 卡
- SmarTest 7.5.0：支持 DC Scale FVI16 卡
- SmarTest 7.10.1：支持 DC Scale XPS256 卡；新增 capacitance、load_step_mode、ms_const_curr_time_to_alarm、pulldown、warn_voltage_drop_force、warn_voltage_drop_return、voltage_slew_rate（面向 XPS256）
- SmarTest 7.10.3：新增 open_loop_protection（面向 XPS256）

## 出处

- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.02.03.07.01_DPSPINS_resources.htm`
