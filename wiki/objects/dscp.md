---
type: object
title: DSCP, DSCP? - (Define System Control Parameter)
layer: L1
stage: project
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# DSCP, DSCP? - (Define System Control Parameter)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **3,390 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### DSCP

```
DSCP [device_cycle], [waveform_set], [timing_set], [level_set], [dps_set], [pmu_set],
[devicecycle_set], [routing_set], [period_res_prec],
```

### DSCP?

```
DSCP?
```

returns:

```
DSCP {device_cycle}, {waveform_set}, {timing_set}, {level_set}, {dps_set},
{pmu_set}, {devicecycle_set}, {routing_set}, [period_res_prec],
[period_res_compatibility_model]
```

### Parameters

[表]
行 1:
  device_cycle
  The device_cycle parameter is an integer that defines the absolute
    maximum number of device cycles that you can create for one
    pin.
    Default: 256
    
    Maximum: 16384
    
    Note that the
    total number of device cycles gets evenly divided between the
    combined number of waveform sets and wavetables. If you use the
    default values, then 256 device cycles divides into the total
    number of 32 `waveform sets and wavetables`（raw: `98578.htm#_98578__row_waveform_set`） to give you 8 device cycles per
    waveform set/wavetable. If you choose values that do not divide
    evenly, then the number of device cycles will be rounded up to
    the next multiple of the `waveform_set`（raw: `98578.htm#_98578__row_waveform_set`） parameter.
行 2:
  devicecycle_set
  The devicecycle_set parameter is an integer
    that defines the maximum number of device cycle sets that you
    can create. Device cycle sets are needed for selective digital
    capture.
    
    Default: 1
    
    Maximum: 128
行 3:
  dps_set
  The dps_set parameter is an integer that
    defines the maximum number of DPS sets you can create.
    
    Default: 32
    
    Maximum: 256
行 4:
  level_set
  The level_set parameter is an integer that
    defines the combined total of level sets for fixed and equation
    based levels that you can create.
    
    Default: 32
    
    Maximum: 256
行 5:
  period_res_prec
  This parameter defines the precision with which the period
    resolution is calculated by the system. It has no effect
    on a user defined period resolution (using, for example, the
    period_res keyword in the equation
    set).
    
    The default is 4, if the .technology file
    does not contain this parameter.
    
    If it does, the value of the .technology
    file is the default.
    
    This value is set to 9, the greatest possible value, when a
    device is created.
行 6:
  pmu_set
  The pmu_set parameter is an integer that
    defines the maximum number of actions that can be contained in
    all measurement sets of all PPMU DC sets.
    
    Default: 1024
    
    Maximum: 12800
行 7:
  routing_set
  Defines the number of routing sets managed by the firmware,
    provided by the MCD.
    
    Default: 256
    
    Maximum: 512
行 8:
  timing_set
  The timing_set parameter is an integer that
    defines the maximum combined total of timing sets for fixed and
    equation based timing you can create.
    
    Default: 256
    
    Maximum: 999
    
    The number of timing sets must be equal to or greater than the
    number of waveform sets, as there must be at least one timing
    set per waveform set.
行 9:
  waveform_set
  The waveform_set parameter defines the maximum
    combined total of waveform sets (fixed timing) and wavetables
    (equation based timing) you can create. Thus, if you specify a
    value of 32, you could, for example, create 10 waveform sets and
    22 wavetables.
    
    Default: 32
    
    Maximum: 128

### Example

```
DSCP 256,16,256,32,32,1024,16,1,256,
```

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.htm>` 的 `## Errors` 段。**不是转述。**
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

The number of device cycles defined is out of range.

The number of waveform sets defined is out of range.

The number of timing sets defined is out of range.

The number of level sets defined is out of range.

The number of DPS sets defined is out of range.

The specified set size is too large for the memory configuration.

The specified number of timing sets is smaller than the number of waveform sets.

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
