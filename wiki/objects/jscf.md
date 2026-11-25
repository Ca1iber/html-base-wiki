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

**文档事实** JSCF 即 Jitter Set ConFiguration，用于定义和查询指定引脚的 jitter injection（抖动注入）配置；被配置的 jitter set 必须已用 JSDF 定义。

**文档事实** 命令形式为 `JSCF {"jitter_set_name"}, {"property"}, {"property_value"}, {(pinlist)}`；查询 `JSCF? {"jitter_set_name"|ALL|PRM}, {"property"|ALL}, {(pinlist)}` 可用具体 jitter set 名、ALL（所有 jitter set）或 PRM（当前 primary jitter set）。

**文档事实** 属性包括 MODE（OFF/CONT/RESTART）、MODULATION_SETS、WAVEFORM、PERIODFACTOR、PHASE、AMPLITUDE、PERIOD、DUTYCYCLE、NOISE、ALLOWED_NOISE。

**文档事实** MODULATION_SETS 与除 MODE 外的其他属性互斥；WAVEFORM 既可直接给出偏移列表（最多 512 项，单位 ps，相对当前 timing set 的 edge delay，偏移最大 ±200 ps），也可选择预定义波形 SINUSOIDAL、RECTANGLE、TRIANGLE。

**文档事实** 该命令配置的是具有 setup focus 的 site，一次只能有一个 site 处于 focus；文档将其 Application 标为 Jitter injection。

**文档事实** 文档示例用 WAVEFORM 偏移列表定义了峰峰值 200 ps 的锯齿波，适用于 STDDIFF 或 STD 引脚。

**推断** JSCF 是 jitter set 的「参数配置面」，与负责定义 jitter set 的 JSDF 成对使用；MODE 决定抖动循环跨 functional test 的运行方式。

## 典型用法

**文档事实** 查询示例 `JSCF? "my_J_SET",ALL,(Pin1)` 返回该 jitter set 在该引脚上的 MODE、WAVEFORM、PERIODFACTOR 配置行。

**文档事实** 示例中 MODE 设为 CONT，抖动从第一个 functional test 开始并持续运行直到被显式终止；WAVEFORM 给出 `"-100,-50,0,50,100,50,0,-50"` 的偏移列表；PERIODFACTOR 设为 25。

**文档事实** PERIODFACTOR 只适用于用户自定义波形，n 表示 2 * clock_resolution 的倍数，默认 1、最大 1024。

**文档事实** PHASE 只适用于预定义波形，为 RESTART 模式定义相位偏移，以度为单位，最大 360°。

**文档事实** AMPLITUDE 为预定义波形幅度（峰峰值的一半），最大 200 ps、默认 100 ps；PERIOD 为预定义波形周期（ps），最大值 2 * clock_resolution * 1024 * 512；DUTYCYCLE 只适用于 TRIANGLE/RECTANGLE，默认 50%；NOISE 为每个波形加入随机噪声，最大幅度 400 ps、默认 0。

**文档事实** 若列表中后一项小于前一项，两者最大差 max_diff = clock_resolution/2 - 410 ps。

**文档事实** 若需完全控制 clock resolution，必须用 period_res 关键字手动指定不大于 2 * minimal_clock_resolution 的 period resolution，此时 clock resolution 等于 period resolution。

**建议** 修改前先用 JSCF? 读回现有属性，避免在 MODULATION_SETS 与其它属性互斥时产生配置冲突。

## 和谁有关

- **文档事实** JSDF，本页参数说明要求 jitter_set_name 必须是 JSDF 定义过的 jitter set；Principles of jitter injection 页说明 jitter set 由 JSDF 与 JSCF 共同定义。
- **文档事实** JSPR，Principles of jitter injection 页说明 jitter injection 通过 JSPR 定义或取消 primary jitter set 来激活与停止；不存在 primary jitter set 时 JTIN 指令被忽略。
- **文档事实** JTIN，Principles of jitter injection 页说明它是 pattern 内局部启停 jitter injection 的 sequencer 指令，可局部覆盖全局循环配置，且只在其所在的 functional test 内有效。
- **文档事实** PSFC，本页正文链接 PSFC，说明 JSCF 配置处于 setup focus 的 site。
- **文档事实** Period resolution, clock resolution, and master clock period，本页 PERIODFACTOR/PERIOD 说明依赖 clock resolution；该页正文也反向引用 JSCF 作为需要计及 clock resolution 的例子（PS1600 上 clock resolution 需在 1.76–3.52 ns）。
- **文档事实** Principles of jitter injection，本页正文指向它作为总览；该页说明 jitter injection 仅允许用于 drive pins，并描述 Smart Scale/STD/STDDIFF 下的实现差异与 JSWF? 查询。
- **文档事实** Two ways of organizing jitter setup data，本页正文指向它说明 MODULATION_SETS 与其它属性的互斥关系，以及 jitter setup data 的两种组织方式。
- **推断** MODULATION_SETS 与 modulation set 相关，但文档正文没有给出 modulation set 的独立对象页，因此这里只记录属性层面的联系，不外推其定义命令。
- **文档事实** List of commands 与 Site dependent firmware commands（02.06.01.05、02.06.02.02.01 两处），这些索引页把 JSCF 列入命令清单；其中 Site dependent firmware commands 页把 JSCF 归入 site dependent firmware commands（引文取自 objpack 入边）。

## 版本

**文档事实** Functional changes 记载：

- Introduced in SmarTest 7.0.1
- SmarTest 7.1.1：WAVEFORM 参数的 SINUS 改为 SINUSOIDAL
- SmarTest 7.3.0：新增 MODULATION_SETS 属性
- SmarTest 7.3.1：用户自定义 jitter waveform 开始支持 FASTDIFF 引脚

## 出处

- `02_System_reference/02.06_Command_Reference/02.06.02.02.147_JSCF__JSCF__-__Jitter_Set_ConFiguration.htm`，主源，含概述、Syntax、Parameters、Properties、Application、Errors、Example 与 Functional changes。
- `02_System_reference/02.06_Command_Reference/02.06.16.01_Principles_of_jitter_injection.htm`，用于核对 JSDF、JSPR、JTIN 与 jitter set 的关系（已用 show.py 读取）。
- Period resolution 页（02.06.06.01.04.01.02.03）、List of commands、Site dependent firmware commands 的语句取自 `extract/objpack.py` 入边索引。
