---
type: object
title: WFDS, WFDS? - (WaveForm Definition String)
layer: L1
stage: timing
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.335_WFDS__WFDS__-__WaveForm_Definition_String.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# WFDS, WFDS? - (WaveForm Definition String)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **6,138 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.335_WFDS__WFDS__-__WaveForm_Definition_String.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### WFDS

```
WFDS {wvf_set}, {wfIndex}, [mode], {definition_string}, {(pinlist)}
WFDS {specset_id|"multiport_spec"}, {wfIndex}, [mode], {definition_string}, {(pinlist)}, ALLOW_EQ
```

### WFDS?

```
WFDS? {wvf_set|"wavetable"|specset_id|"multiport_spec"}, {wfIndex}, [mode], {(pinlist)}
```

returns:

```
WFDS {wvf_set|"wavetable"|specset_id|"multiport_spec"}, {wfIndex}, [mode], {definition_string}, {(pinlist)}
```

### Parameters

[表]
行 1:
  wvf_set
  Waveform set number. Enter an integer in [跨 3 列]
    the range 1 to the maximum number of allowed waveform sets. The maximum number is
    determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `98878.htm`）. For the query you can also enter
    ALL for all waveform sets. Enter PRM to select the
    primary waveform set.
行 2:
  wavetable_name
  The wavetable name. Enter a string of up to [跨 3 列]
    40 alphanumeric characters (upper or lower case) enclosed by double quotes.
行 3:
  specset_id
  Derived as follows: [跨 3 列]
    
    100 * equation_set_no + specset_no
行 4:
  multiport_spec
  To query a multiport specification, enter [跨 3 列]
    the name of the specification.
行 5:
  wfIndex
  Waveform index. Enter an integer between 0 and 255. The index references a waveform in a device [跨 3 列]
    cycle. For the query you can also enter ALL for all waveform DC/DC power units.
    The waveform index is also used by the
    `WAVE, WAVE? - (WAVEform)`（raw: `98869.htm`） command.
    
    Note that the index must be specified decimally here, whereas in the wavetable, it is
    coded hexadecimally.
行 6:
  mode
  Not used. [跨 3 列]
行 7:
  definition_string
  Edge action definition string which consists of drive [跨 3 列]
    actions for the drive/ bidirectional edges only. On Pin Scale systems, there is only one
    drive edge type, which is denoted by di (1 ≤
    i ≤ 8).
    
    With these edges you can associate the following actions:
    
    N: No action
    
    F0N: Drive 0, no tri-state action
    
    F1N: Drive 1, no tri-state action
    
    FN0: No drive action, tri-state off
    
    FNZ: No drive action, tri-state on
    
    F00: Drive 0, tri-state off
    
    F0Z: Drive 0, tri-state on
    
    F10: Drive 1, tri-state off
    
    F1Z: Drive 1, tri-state on
    
    D1N: Drive parameter 1 (DD1), no tri-state action
    
    D1N: Drive parameter 2 (DD2), no tri-state action
    
    C1N: Drive complement of parameter 1 (DD1), no tri-state action
    
    C2N: Drive complement of parameter 2 (DD2), no tri-state action
    
    DN1: No drive action, tri-state parameter 1 (DD1)
    
    DN2: No drive action, tri-state parameter 2 (DD2)
    
    D11: Drive parameter 1 (DD1), tri-state parameter 1 (DD1)
    
    C11: Drive complement of parameter 1 (DD1), tri-state parameter 1
    (DD1)
    
    D22: Drive parameter 2 (DD2), tri-state parameter 2 (DD2)
    
    C22: Drive complement of parameter 2 (DD2), tri-state parameter 2
    (DD2)
    
    All edges which are not explicitly set are set to N. In the query
    only those edges that are used are printed.
    
    The following table shows which data-dependent drive actions use the driver formatter,
    which use the tri-state formatter, and which use both. You have to consider this when
    assigning parameters to the `WAVE`（raw: `98869.htm`） command. See also `Specifying the actions`（raw: `103901.htm`）.
行 8:
   [跨 4 行]
  Data-dependent Drive Action
  Driver
  Tri-state
行 9:
  D1N, D2N, C1N, C2N
  yes
  no
行 10:
  DN1, DN2
  no
  yes
行 11:
  D11, C11, D22, C22
  yes
  yes
行 12:
  
  On Smart Scale systems, there are two types [跨 3 列]
    of drive edges, denoted by fi and
    si (1 ≤ i ≤ 8). For both of them,
    only the action codes 0, 1, and N are admitted. But the Smart Scale systems also support the old
    di syntax. For more information see `Defining waveforms for Smart Scale pins`（raw: `113740.htm`）.
行 13:
  
  On the expected data side the actions you [跨 3 列]
    can define are:
    
    N: No action
    
    E0: Edge compare to 0
    
    E1: Edge compare to 1
    
    EI: Edge compare to intermediate
    
    EX: Edge compare to mask
    
    EU: Edge compare to unstable
    
    C: Capture digital data (selective digital capture)
    
    D: Do not capture digital data (selective digital capture)
    Note
    that waveforms that are to be used for selective digital capture must contain exactly one
    compare action.
    
    W0: Window open with compare to 0
    
    W1: Window open with compare to 1
    
    WI: Window open with compare to intermediate
    
    WX: Window open with compare to mask
    
    WU: Window open with compare to unstable
    
    WC: Window close
    
    EE1: Edge compare to parameter 1 (ED1)
    
    EE2: Edge compare to parameter 1 (ED2)
    
    WE1: Window open with compare to parameter 1 (ED1)
    
    WE2: Window open with compare to parameter 1 (ED2)
行 14:
  pinlist
  The name of the pin or pins for which the [跨 3 列]
    waveform is to be defined or read back. This parameter can also include groups previously
    created by `DFGP, DFGP? - (DeFine GrouP)`（raw: `98546.htm`）. The @ symbol can be used to specify
    all configured pins. If more than one pin is to be included, the names must be separated
    with a comma.
行 15:
  ALLOW_EQ
  This extra parameter allows you to define [跨 3 列]
    or change logical waveforms for an equation based timing. Note that only the runtime
    settings are affected; the definitions in the wavetable are not changed.
    
    Note also the following:
    
    Every runtime change will affect all specifications that use the respective
    wavetable.
    
    Since the new or changed waveform must be evaluated and downloaded for every
    specification that uses the respective wavetable, the change tends to be rather slow.
    
    The runtime definitions are not checked for consistency. It is up to the user to ensure
    this.

### Example

```
> WFDS 1,0,,"e1:F00 e2:D1N e3:F00",(io)
> WFDS 1,1,,"r4:EE1",(io)
> WFDS 1,0,,"d1:F00 d2:F10 d3:F10 d4:F00 d5:F10 d6:F00 d7:F10 d8:F00",(clk)

> WFDS? 1,ALL,,(@)
< WFDS 1,0,,"d1:F00 d2:D1N d3:F00",(io)
< WFDS 1,1,,"r4:EE1",(io)
< WFDS 1,0,,"d1:F00 d2:F10 d3:F10 d4:F00 d5:F10 d6:F00 d7:F10 d8:F00",(clk)
```

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.335_WFDS__WFDS__-__WaveForm_Definition_String.htm>` 的 `## Errors`、`## Warnings` 段。**不是转述。**
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

wvf_set
 is greater than the range allowed by the
WSUS

command, or < 1

The waveform index is outside the range of 0 - 256 (Pin Scale systems)

There is a mismatch between the edge actions and edge order in the specified waveform

You specify a drive action for an output pin

You specify a receive action for an input pin

There is a mismatch in edge direction between the waveform you have defined and existing
waveforms

There is a missing window close action between two window open actions

There is a missing window open action between two window close actions

### Warnings

A warning is generated if edge delays are auto-corrected to fit
in with the programmed waveform. The timing sets belonging to the affected waveform set are
modified as necessary

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
