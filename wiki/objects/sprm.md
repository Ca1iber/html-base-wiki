---
type: object
title: SPRM, SPRM? - (Set PRiMary sets)
layer: L1
stage: level
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.22_SPRM__SPRM__-__Set_PRiMary_sets.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# SPRM, SPRM? - (Set PRiMary sets)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **4,307 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.05.02.22_SPRM__SPRM__-__Set_PRiMary_sets.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### SPRM

```
SPRM [waveform_set_no], [timing_set_no], [level_set_no|level_set_id], [dps_set_no|dps_set_id]
```

or:

```
SPRM {timing_specset_id}, [timing_set_no], [level_set_no|level_set_id], [dps_set_no|dps_set_id]
```

or,
for multiport
specifications:

```
SPRM {"multi-port_spec"}, [timing_set_no|"timing_set_list"], [level_set_id|level_set_no],[dps_set_id|dps_set_no] [,(port)]
```

### SPRM?

```
SPRM?
```

returns:

```
SPRM {waveform_set_no}, {timing_set_no}, {level_set_no|level_set_id}, {dps_set_no|dps_set_id}
```

or:

```
SPRM {timing_specset_id}, {timing_set_no}, {level_set_id|level_set_no}, {dps_set_id|dps_set_no}
```

or,
for multiport
specifications:

```
SPRM? [(port)]
```

returns:

```
SPRM {"multi-port_spec"}, {timing_set_no|"timing_set_list"}, {level_set_id|level_set_no},{dps_set_id|dps_set_no} [,(port)]
```

### Parameters

[表]
行 1:
  waveform_set_no
  The identification number of the waveform set. Enter an integer in the range 1 to
    the maximum number of allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `98878.htm`）. The number you enter must also be less than or equal to the maximum
    number of waveform sets allowed - as defined by `CONF, CONF? - (CONFiguration)`（raw: `98510.htm`）.
行 2:
  timing_specset_id
  Derived as follows:
    
    100 * equation_set_no + specset_no
    
    Note that the spec set ID also identifies the primary wavetable in equation based
    testing.
行 3:
  multi-port_spec
  For a multi-port setup, specify a primary multi-port specification.
行 4:
  timing_set_no
  The identification number of the timing set. Enter an integer in the range 1 to the
    maximum number of allowed timing sets (of the selected waveform set or timing
    specification). The maximum number is determined by `TSUS, TSUS? - (Timing Sets USed)`（raw: `98817.htm`）. The number you
    enter must also be less than or equal to the maximum number of timing sets allowed (as
    defined by `DSCP`（raw: `98578.htm`）).
    
    In a multiport setup, the timing set number applies to all ports of the specification if
    you do not specify a port. If you do, the number applies to the specified port.
行 5:
  timing_set_list
  In a multi-port setup, you can specify primary timing sets for all ports of the
    specification by entering a list of numbers separated by commas. The order of the timing
    sets must correspond to the order of the ports in the multi-port timing specification.
    
    In the query, the numbers of the primary timing sets are returned in a list for all ports
    of the primary specification unless the numbers are identical for all ports or a port has
    been specified in the query.
行 6:
  level_set_no
  The identification number of the level set. Enter an integer in the range 1 to the
    maximum number of allowed level sets. The maximum number is determined by `LSUS, LSUS? - (Level Sets USed)`（raw: `98641.htm`）. The number you enter must also be less than or equal to the maximum
    number of level sets allowed (as defined by `DSCP`（raw: `98578.htm`）).
行 7:
  dps_set_no
  The identification number of the DPS set. Enter an integer in the range 1 to the
    maximum number of allowed DPS sets. The maximum number is determined by `DSUS, DSUS? - (Dps Sets USed)`（raw: `98580.htm`）. The number you enter must be less than or equal to the maximum number of
    DPS sets allowed (as defined by `DSCP`（raw: `98578.htm`）).
行 8:
  level_set_id
  Derived as follows:
    
    100000 * equation_set_no + 1000 * specset_no + level_set_no
行 9:
  dps_set_id
  Derived as follows:
    
    100000 * equation_set_no + 1000 * specset_no + 1
行 10:
  port
  In a multiport setup, you can specify a port of the specification that was entered
    as the first parameter. In this case, the timing set number specified as the second
    parameter will only be applied to the specified port. The port parameter is ignored if a
    timing set list is specified.

### Example

The following example shows how to define and query primary timing sets for the
multi-port specification spec_ClockP_P1_P2, which contains three
ports:

```
> SPRM "spec_ClockP_P1_P2","2,1,2",,
> SPRM?
< SPRM "spec_ClockP_P1_P2","2,1,2",101002,101003
> SPRM "spec_ClockP_P1_P2",2,,,(port_1.CP_1)
> SPRM?
< SPRM "spec_ClockP_P1_P2",2,101002,101003
> SPRM? (port_1.CP_1)
< SPRM "spec_ClockP_P1_P2",2,101002,101003,(port_1.CP_1)
```

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.05.02.22_SPRM__SPRM__-__Set_PRiMary_sets.htm>` 的 `## Errors` 段。**不是转述。**
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

The set number given is greater than the maximum number allowed by the
`DSCP`（raw: `98578.htm`）
 (Define System Control Parameter) command (the specified set is not configured),
or the equivalent for equation based tests where a spec number is out of the allowed
range.

specset_id
 is invalid because
equation_set_no
,

specset_no
, or both are invalid.

specset_id
 does not reference a defined wavetable.

level_set_id
 does not describe a defined equation set, spec set or level
set.

dps_set_no
 is undefined or out of range.

dps_set_id
 does not describe a defined equation set or spec set.

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
