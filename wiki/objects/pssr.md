---
type: object
title: PSSR, PSSR? -(Power Supply Slew Rate)
layer: L1
stage: level
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.197_PSSR__PSSR__-_Power_Supply_Slew_Rate.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# PSSR, PSSR? -(Power Supply Slew Rate)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **4,650 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.197_PSSR__PSSR__-_Power_Supply_Slew_Rate.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### PSSR

```
PSSR {dps_No|dps_set_id}, [rise_tm_per_v], [rise_settm], [fall_tm_per_v], [fall_settm], [rise_t_per_v_c2c], [rise_setup_t_c2c], [fall_t_per_v_c2c], [fall_setup_t_c2c], (pinlist)
```

### PSSR?

```
PSSR? {dps_No|dps_set_id}, (pinlist)
```

returns:

```
PSSR {dps_No|dps_set_id}, [rise_tm_per_v], [rise_settm], [fall_tm_per_v], [fall_settm], [rise_t_per_v_c2c], [rise_setup_t_c2c], [fall_t_per_v_c2c], [fall_setup_t_c2c], (pinlist)
```

### Parameters

Note
 The
rise_...
 and
fall_...
 parameters of the

PSSR
 command and the settling time parameter
(
setup_time
) of the
`PSLV`（raw: `98702.htm`）
 command
exclude each other. This also applies to the
t_ms
 equation
parameter (see
`DPSPINS`（raw: `16886.htm`）
 and
`DPSPINS resources`（raw: `16887.htm`）
).

Note
 All time values have a resolution of microseconds (floating point values are
rounded to three decimal places).

[表]
行 1:
  dps_No
  Needed for non-equation-based setup.
    
    The identification number of the DPS set which you want to modify. The number must not
    exceed the maximum number allowed (as defined by the DSCP (Define System
    Control Parameter) command). Entering ALL modifies all the existing
    fixed DPS sets. Entering PRM modifies the primary DPS set. Entering
    ACT (only for PSSR?) displays the settings of the actual enabled DPS
    set.
行 2:
  dps_set_id
  Needed for equation-based setup.
    
    This parameter is derived as follows:
    
    100000*equation_set_no + 1000*specset_no+1
行 3:
  rise_tm_per_v
  Sets the inverse slew rate for the rising edge in ms/V.
    
    The allowed range is 0 to 10000 ms/V.
行 4:
  rise_settm
  Sets the settling time for the rising edge in ms.
    
    The allowed range is 0 to 10000 ms.
行 5:
  fall_tm_per_v
  Sets the inverse slew rate for the falling edge in ms/V.
    
    The allowed range is 0 to 10000 ms/V.
行 6:
  fall_settm
  Sets the settling time for the falling edge in ms.
    
    The allowed range is 0 to 10000 ms.
行 7:
  rise_t_per_v_c2c
  Sets the inverse slew rate for the rising edge. expression must define a value in ms/V.
    
    The allowed range is 0 to 10000 ms/V.
    
    The parameter is optional. If specified, it is used for "connect-to-connect-" cases, that
    is for level changes caused by a reprogramming of the output
    voltage within one DPS set, or by a switch to another DPS set
    while the DPS is connected. If omitted, the above
    vout_rise_t_ms_per_volt parameter is used
    instead.
    
    This parameter is for both DPS-slot DPS and DC Scale pins.
行 8:
  rise_setup_t_c2c
  Sets the settling time for the rising edge. expression must define a value in ms.
    
    The allowed range is -10000 to 10000 ms.
    
    The parameter is optional. If specified, it is used for "connect-to-connect-" cases, that
    is for level changes caused by a reprogramming of the output
    voltage within one DPS set, or by a switch to another DPS set
    while the DPS is connected. If omitted, the above
    vout_rise_settling_t_ms parameter is used
    instead.
    
    This parameter is for both DPS-slot DPS and DC Scale pins.
行 9:
  fall_t_per_v_c2c
  Sets the inverse slew rate for the falling edge. expression must define a value in ms/V.
    
    The allowed range is 0 to 10000 ms/V.
    
    The parameter is optional. If specified, it is used for "connect-to-connect-" cases, that
    is for level changes caused by a reprogramming of the output
    voltage within one DPS set, or by a switch to another DPS set
    while the DPS is connected. If omitted, the above
    vout_fall_t_ms_per_volt parameter is used
    instead.
    
    This parameter is for both DPS-slot DPS and DC Scale pins.
行 10:
  fall_setup_t_c2c
  Sets the settling time for the falling edge. expression must define a value in ms.
    
    The allowed range is -10000 to 10000 ms.
    
    The parameter is optional. If specified, it is used for "connect-to-connect" cases, that
    is for level changes caused by a reprogramming of the output
    voltage within one DPS set, or by a switch to another DPS set
    while the DPS is connected. If omitted, the above
    vout_fall_settling_t_ms parameter is used
    instead.
    
    This parameter is for both DPS-slot DPS and DC Scale pins.
行 11:
  pinlist
  pinlist must contain the names of pins previously defined by the `DFPS`（raw: `98551.htm`） command. If a pin is associated
    with a DPS-slot DPS, it is ignored. @ refers to all pins that
    are associated with a DC Scale channel.

### Example

```
PSSR PRM,10,50,20,70,(Vcc)
```

This example sets the following
parameters for the primary set of DPS pin Vcc:

rise_tm_per_v = 10 ms/V

rise_settm = 50 ms

fall_tm_per_v = 20 ms/V

fall_settm = 70 ms

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.197_PSSR__PSSR__-_Power_Supply_Slew_Rate.htm>` 的 `## Errors` 段。**不是转述。**
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

The DPS set number is out of range

A programmed parameter is out of range

<!-- 报错节 end -->

## 是什么

（待补）

## 典型用法

（待补）

## 和谁有关

（待补）

## 版本

（待补）

## 出处

（待补）
