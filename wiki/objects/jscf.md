---
type: object
title: JSCF, JSCF? - (Jitter Set ConFiguration)
layer: L1
stage: timing
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.147_JSCF__JSCF__-__Jitter_Set_ConFiguration.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# JSCF, JSCF? - (Jitter Set ConFiguration)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **5,698 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.147_JSCF__JSCF__-__Jitter_Set_ConFiguration.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### JSCF

```
JSCF {"jitter_set_name"}, {"property"}, {"property_value"}, {(pinlist)}
```

### JSCF?

```
JSCF? {"jitter_set_name"|ALL|PRM}, {"property"|ALL}, {(pinlist)}
```

returns:

```
JSCF {"jitter_set_name"}, {"property"}, {"property_value"}, {(pinlist)}
```

### Parameters

[表]
行 1:
  jitter_set_name
  Specifies the name of a jitter set that must have been defined with
    JSDF.
行 2:
  property
  Specifies a property of the jitter set. For a list see the table below.
行 3:
  ALL
  This value can be specified in the query to retrieve the configuration data of all
    jitter sets.
行 4:
  PRM
  This value can be specified in the query to retrieve the configuration of the
    current primary jitter set.
行 5:
  property_value
  Specifies the value for the specified property. The values that are admitted for
    the individual properties are listed in the table below.
行 6:
  pinlist
  Specifies the pins to which this configuration is to be applied.

### Properties and their values

[表]
列: Property | Explanation and values
行 1:
  MODE [跨 4 行]
  This parameter defines the operation mode [跨 3 列]
    of the jitter injection. The possible values are:
行 2:
  OFF
  No jitter injection takes place. This is [跨 2 列]
    the default.
行 3:
  CONT
  Jitter injection is started with the first [跨 2 列]
    functional test and then keeps running until it is explicitly terminated.
行 4:
  RESTART
  Jitter injection is stopped after every [跨 2 列]
    functional test and restarted with the next functional test.
行 5:
  MODULATION_SETS
  By this parameter, you can associate one or [跨 3 列]
    two modulation sets with the jitter set. If two modulation sets are specified, they must be
    separated by a comma. In this case the name list, not the individual names, must be
    included by quotes.
    
    Note also that when you specify this property, you cannot specify any of the other
    properties except MODE.
行 6:
  WAVEFORM
  This parameter either (a) defines a list of [跨 3 列]
    offsets from the edge delays specified in the currently active timing set, or (b) selects a
    predefined waveform. In case (a), the list items must be separated by a comma, and the
    maximum number of items is 512.
行 7:
   [跨 4 行]
  The list items of case (a) specify the actual delays in picoseconds. [跨 3 列]
    
    The following restrictions apply:
    
    The maximum offset from the delay defined in the timing set is 200 ps in either
    direction.
    
    If the successor in the list is smaller than its predecessor, the maximum difference
    max_diff between the two items depends on the clock resolution as
    follows:
    max_diff = clock_resolution/2 - 410 ps
    
    The list can be used to approximate a jitter modulation waveform.
    
    There are three predefined such waveforms (case (b)) which can be selected by the
    following keywords:
行 8:
  SINUSOIDAL [跨 2 列]
  Creates a sinusoidal waveform.
行 9:
  RECTANGLE [跨 2 列]
  Creates a rectangular waveform.
行 10:
  TRIANGLE [跨 2 列]
  Creates a triangular waveform.
行 11:
  PERIODFACTOR
  An integer n that defines the distance between two items of the list defined by [跨 3 列]
    WAVEFORM. It only applies to user defined waveforms and specifies a multiple of 2 *
    clock_resolution. The default for n is 1, the maximum is
    1024.
    
    The clock resolution is calculated from the period resolution, but also takes other
    parameters into account. Therefore a different clock resolution may be calculated from the
    same period resolution in different circumstances.
    
    If you want to have complete control over the clock resolution, you must specify a period
    resolution not greater than 2 * minimal_clock_resolution manually (with
    the period_res keyword). Then the clock resolution will equal the period
    resolution. See also `Period resolution, clock resolution, and master clock period`（raw: `98412.htm`）.
行 12:
  PHASE
  This property, which only applies to [跨 3 列]
    predefined waveforms, is intended to define a phase offset for the
    RESTART mode. This value must be specified as a degree. The maximum is
    360°.
行 13:
  AMPLITUDE
  This property determines the amplitude (that is, half of the peak-to-peak value) of a predefined [跨 3 列]
    waveform.
    
    It is not applicable to user defined waveforms for Smart Scale
    STDDIFF pins.
    
    The maximum is 200 ps. The default is always 100 ps.
行 14:
  PERIOD
  This property defines the period of a predefined waveform in ps. [跨 3 列]
    
    It is not applicable to user defined waveforms for Smart Scale
    STDDIFF pins.
    
    The maximum period depends on the clock
    resolution as follows:
    
    2 * clock_resolution * 1024 * 512
    
    For clock_resolution, see the PERIODFACTOR
    property.
行 15:
  DUTYCYCLE
  This property defines the ratio between the [跨 3 列]
    positive half wave and the full wave. It is only applicable to the
    TRIANGLE and RECTANGLE waveforms. The default is
    50%.
行 16:
  NOISE
  Setting this property will add random noise [跨 3 列]
    to every waveform. The value given with this property is interpreted as the amplitude of
    the random noise to be added.
    
    The maximum amplitude is 400 ps. The default is 0.
行 17:
  ALLOWED_NOISE
  This parameter defines the maximum step width that is [跨 3 列]
    allowed between two sampling points in a predefined waveform for a STD
    or STDDIFF pin. If this value is exceeded, an error message will be
    issued.

### Example

```
> JSCF? "my_J_SET",ALL,(Pin1)
< JSCF "my_J_SET",MODE,CONT,(Pin1)
< JSCF "my_J_SET",WAVEFORM,"-100,-50,0,50,100,50,0,-50",(Pin1)
< JSCF "my_J_SET",PERIODFACTOR,25,(Pin1)
```

This
example defines a simple sawtooth waveform with a peak-to-peak value of 200ps for a

STDDIFF
 or
STD
 pin.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.147_JSCF__JSCF__-__Jitter_Set_ConFiguration.htm>` 的 `## Errors` 段。**不是转述。**
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if no jitter set with the specified name
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
