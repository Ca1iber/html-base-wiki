---
type: object
title: MSCF, MSCF? - (Modulation Set ConFiguration)
layer: L1
stage: timing
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.162_MSCF__MSCF__-__Modulation_Set_ConFiguration.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# MSCF, MSCF? - (Modulation Set ConFiguration)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **3,592 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.162_MSCF__MSCF__-__Modulation_Set_ConFiguration.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### MSCF

```
MSCF {"modulation_set_name"}, {"property"}, {"property_value"}
```

### MSCF?

```
MSCF? {"modulation_set_name"|ALL}, {"property"|ALL}
```

returns:

```
MSCF {"modulation_set_name"}, {"property"}, {"property_value"}
```

### Parameters

[表]
行 1:
  modulation_set_name
  Specifies the name of a modulation set that must have been defined with
    MSDF.
行 2:
  property
  Specifies a property of the modulation set. For a list see the table below.
行 3:
  ALL
  This value can be specified in the query to retrieve the configuration data of all
    modulation sets.
行 4:
  property_value
  Specifies the value for the specified property. The values that are admitted for
    the individual properties are listed in the table below.

### Properties and their values

[表]
列: Property | Explanation and values
行 1:
  SHAPE
  This parameter either [跨 2 列]
    
    (a) defines a list of offsets (in picoseconds) from the edge delays specified in the
    currently active timing set, or
    
    (b) selects a predefined waveform.
    
    In case (a), the list items must be separated by a comma, and the maximum number of items
    is 3072. Note that case (a) is only supported for STDDIFF pins.
    
    The list items of case (a) do not define the actual delays, but only their mutual
    proportions. The actual values are computed from the list and the required maximum value
    (AMPLITUDE property) by
    
    list_item * ( max_value /
    max_item),
    
    where max_item is the greatest item in the specified list. To give a
    simple example, if the specified list is
    
     0, 10, 20, 10, 0, -5, -10, -5, 0
    
    and the required maximum value is 30ps, then the actual waveform is calculated by
    
    list_item * ( 30 / 20)
    
    as
    
     0, 15, 30, 15, 0, -7.5, -15, -7.5, 0
    
    picoseconds. If no amplitude is specified, the default of 100ps is assumed.
    
    The predefined waveforms (case (b)) are:
行 2:
  
  SINE
  Creates a sinusoidal waveform.
行 3:
  
  RANDOM
  Generates random jitter within delay -
    amplitude and delay +
    amplitude,
    
    where delay is the delay that is defined in the currently active
    timing set for the pins that are associated with the modulation set in the respective
    jitter set, and amplitude is the value of the
    AMPLITUDE property.
行 4:
  PHASE
  This property is intended to [跨 2 列]
    define a phase offset for the RESTART mode (the mode is defined with
    JSCF). This value must be specified as a degree. The maximum is
    360°.
行 5:
  AMPLITUDE
  This property determines the amplitude (that is, half of the peak-to-peak value) of a predefined [跨 2 列]
    shape.
    
    The maximum is 200 ps. The default is always 100 ps.
行 6:
  PERIOD
  This property defines the jitter [跨 2 列]
    period in picoseconds.
    
    In general, the maximum period depends on the clock resolution as follows:
    
    2 * clock_resolution * 1024 * 512
    
    The clock resolution is calculated from the period resolution, but also takes other
    parameters into account. Therefore a different clock resolution may be calculated from the
    same period resolution in different circumstances.
    
    If you want to have complete control over the clock resolution, you must specify a period
    resolution not greater than 2 * minimal_clock_resolution manually (with
    the period_res keyword). Then the clock resolution will equal the period
    resolution. See also `Period resolution, clock resolution, and master clock period`（raw: `98412.htm`）.

### Example

```
> MSCF? "mod1",ALL
< MSCF "mod1",SHAPE,SINE
< MSCF "mod1",PERIOD,250
< MSCF "mod1",PHASE,180
< MSCF "mod1",AMPLITUDE,305
```

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.162_MSCF__MSCF__-__Modulation_Set_ConFiguration.htm>` 的 `## Errors` 段。**不是转述。**
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if no modulation set with the specified name
exists.

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
