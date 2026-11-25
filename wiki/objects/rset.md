---
type: object
title: RSET - (ReSET)
layer: L1
stage: level
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.210_RSET_-__ReSET.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# RSET - (ReSET)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **2,164 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.210_RSET_-__ReSET.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
RSET {specifier}
```

### Parameters

[表]
行 1:
  specifier [跨 11 行]
  The specifier can be: [跨 2 列]
行 2:
  DPS
  Loads the default power supply setup for standard DPSs.
行 3:
  FCR
  Loads the default clock routing.
行 4:
  LEV
  Loads the default power supply setup for standard DPSs.
    
    Level: 0 V
    
    Current: 50 mA
    
    Off state: minimum current
    
    Setup time: 0 ms
    
    This default states are:
    
    UHC4T
    
    Connect state: normal
    
    Level: 0 V
    
    Range: 4 V
    
    Clamp: 4 A
    
    Clamp-Range: 40 A
    
    Disconnect state: HIZ
    
    Voltage drop force: 250 mV
    
    Voltage drop return: 250 mV
    
    Clamp mode: limit (see `UHCM`（raw: `106910.htm`）)
    
    DUT capacitor mode: off
    
    Fast preload: 0 ms
行 5:
  TIM
  Loads the default timing setup. The settings are:
    
    Timing Sets
    
    Defined Timing Sets: 1
    
    Allowed Timing Sets: 256
    
    Waveform Sets
    
    Defined Waveform Sets: 1
    
    Allowed Waveform Sets: 16
    
    Waveforms: not defined
    
    Breakwaveform: defined
    
    Events
    
    Action: NOP
    
    Timing: 0 ns
    
    Min Period: 4 ns
    
    This is dependent on the test system hardware configuration.
    
    Device Cycles: not defined
    
    Default Device Cycle: ""
行 6:
  VEC
  Loads the default vector setup. The Vector Memory contains:
    
    No vectors
    
    No tests (and therefore no labels)
    
    No comments
    
    No sequencer programs (no instructions)
行 7:
  ATR
  Loads the default edge attributes.
    
    Pin attribute: set to 0
行 8:
  PDL
  Loads the default path delay attributes.
    
    Cable assembly delay attribute: set to 0
    
    Fixture delay attribute: set to 0
    
    System attribute: set to 0
行 9:
  CAL
  Loads the default calibration data.
    
    Level calibration data
    
    Timing calibration data
行 10:
  MTPP
  Resets memory test and per-pin sequencer subroutine data.

### Example

```
RSET TIM
```

This example resets all waveform sets and timing sets
and loads the hardware with the default vector rate and edge placement values. Only waveform set
1 and timing set 1 in waveform set 1 is active.

<!-- 语法节 end -->

## 是什么

**文档事实** RSET（ReSET）命令把指定类型文件的 power-on 默认值装入硬件。

**文档事实** specifier 可取：DPS（标准 DPS 的默认电源设置）、FCR（默认时钟布线）、LEV（默认电源设置，文档给出 Level 0 V、Current 50 mA、Off state minimum current、Setup time 0 ms 等值；其中 UHC4T 的 clamp mode 为 limit，见 UHCM）、TIM（默认 timing 设置）、VEC（默认 vector 设置，Vector Memory 中无 vector、无 test/label、无 comment、无 sequencer program）、ATR（默认 edge attribute，pin attribute 置 0）、PDL（默认 path delay attribute，cable assembly、fixture、system attribute 均置 0）、CAL（默认 level 与 timing 校准数据）、MTPP（复位 memory test 与 per-pin sequencer subroutine 数据）。

**文档事实** 文档的 Application 一栏写的是 Test Program Explorer。

## 典型用法

**文档事实** 语法为 `RSET {specifier}`，每次指定一种 specifier。

**文档事实** 最小示例是 `RSET TIM`：文档说明它重置所有 waveform set 与 timing set，并把默认 vector rate 与 edge placement 装入硬件；此后只有 waveform set 1 和 waveform set 1 中的 timing set 1 处于 active。

**建议** 需要把某一类 setup 恢复为 power-on 默认值时选对应 specifier；具体默认值见上方参数表，执行前先确认要覆盖的范围。

## 和谁有关

- **文档事实** `*RST`（`02_System_reference/02.06_Command_Reference/02.06.02.02.345_RST_-__ReSeT.htm`）— 该页写明 *RST 复位 firmware 与全部校准数据，使硬件装入 power-up 默认值，并注明「For default values see the RSET command」。
- **文档事实** DCCH（`02_System_reference/02.06_Command_Reference/02.06.02.02.40_DCCH_-__DC_Current_measurement_High_precision_pmu.htm`）与 DCVH（`02_System_reference/02.06_Command_Reference/02.06.02.02.52_DCVH_-__DC_Voltage_measurement_High_precision_pmu.htm`）— 两页都把 `RSET DC` 与 DCCH、DCVH、*RST、UDEF 并列为「执行一次复位」的情形。
- **文档事实** `UHCM`（`02_System_reference/02.06_Command_Reference/02.06.02.02.303_UHCM__UHCM__-__Ultra_High_Current_power_supply_Modes.htm`）— RSET 的 LEV 默认值中 clamp mode 为 limit，文档在此注明见 UHCM。
- **文档事实** `02_System_reference/02.06_Command_Reference/02.06.02.02_List_of_commands.htm` — 该命令清单列出 RSET。
- **文档事实** RSET 本页参数表列出的 specifier 中没有 DC，而 DCCH/DCVH 页出现 `RSET DC`；两处记载并列，不自行取舍。

## 版本

**文档事实** Functional changes 记载 `Introduced before SmarTest 6.3.2`（哨兵值，表示在文档集覆盖范围开始前就已存在）；`SmarTest 7.0.3: Removed MTST parameter option`。

## 出处

- `02_System_reference/02.06_Command_Reference/02.06.02.02.210_RSET_-__ReSET.htm`，主源，含命令用途、参数表、Application、Example 与 Functional changes。
- 关系与版本佐证另读 `02.06.02.02.345_RST_-__ReSeT.htm`、`02.06.02.02.40_DCCH_-__DC_Current_measurement_High_precision_pmu.htm`、`02.06.02.02.52_DCVH_-__DC_Voltage_measurement_High_precision_pmu.htm`、`02.06.02.02.303_UHCM__UHCM__-__Ultra_High_Current_power_supply_Modes.htm`。
