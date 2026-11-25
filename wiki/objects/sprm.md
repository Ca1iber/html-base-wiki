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

**文档事实** SPRM（Set PRiMary sets）用于为 test suite 或在 user procedure 中定义的 test 定义和更改 primary sets。

**文档事实** primary sets 包括：timing equation set 与 spec set（equation based testing）；multi-port specification（multiport setup）；waveform set（非 equation based testing）；timing set，或 multiport setup 下的 timing set list；level equation set、level spec set 与 level set（equation based testing）；level set（非 equation based testing）；DPS set。

**文档事实** SPRM 不激活硬件中的 primary sets，激活由 APRM 负责。

**文档事实** 若测试需要用不同参数重复 functional test，可用 SPRM 为每次 test run 定义 primary sets；除非另行指定，functional test 使用实际 primary sets 中定义的参数。

**文档事实** FTST?、RCLS?、SQST/SQST?、PSST/PSST? 也依赖 SPRM，但不需要事先执行 APRM。

**文档事实** 在 equation based timing/level setup 中须给出 spec set ID、level set ID、DPS set ID，而不是 waveform set number、level set number、DPS set number；公式为 `specset_id = 100 * equation_set_no + specset_no`、level set ID `= 100000 * equation_set_no + 1000 * specset_no + level_set_no`、DPS set ID `= 100000 * equation_set_no + 1000 * specset_no + 1`。

**文档事实** 若指定的部分 set 不存在，SPRM 可能报错，但它始终会存储传给它的值。

## 典型用法

**文档事实** 语法有三种形式：非 equation based（waveform_set_no、timing_set_no、level_set_no/level_set_id、dps_set_no/dps_set_id）；equation based（timing_specset_id、timing_set_no、level set、DPS set）；multiport（`"multi-port_spec"`、timing set 或 timing set list、level set、DPS set，可带 port）。`SPRM?` 返回当前 primary sets。

**文档事实** 示例对含三个 port 的 multiport 规格 spec_ClockP_P1_P2，先用 `SPRM "spec_ClockP_P1_P2","2,1,2",,` 定义各 port 的 primary timing sets，再用 `SPRM?` 查询，返回 `SPRM "spec_ClockP_P1_P2","2,1,2",101002,101003`。

**文档事实** 示例还演示对单个 port 的设置与查询：`SPRM "spec_ClockP_P1_P2",2,,,(port_1.CP_1)`，以及 `SPRM? (port_1.CP_1)` 返回带 `(port_1.CP_1)` 的结果。

**文档事实** Application 段说明其作用是定义 test 的 primary sets，覆盖 AC tests 和 DC measurements（后者见 DC Measurement Commands）。

**建议** 每次需要变更测试条件时用 SPRM 重设 primary sets；注意它不激活硬件，需要硬件生效时应另行执行 APRM。

## 和谁有关

- **文档事实** APRM - (Activate PRiMary sets)，源文明确 SPRM 不在硬件中激活 primary sets，激活由 APRM 完成。
- **文档事实** FTST? - (Functional TeST)、RCLS? - (ReCeive Level Sensitivity)、SQST, SQST? - (SeQuencer STate)、PSST, PSST? - (Power Supply STatus)，源文列为其依赖 SPRM、但无需事先执行 APRM 的命令。
- **文档事实** DSCP, DSCP? - (Define System Control Parameter)，Errors 说明 set number 超过 DSCP 配置的最大值会报错。
- **文档事实** WSUS, WSUS? - (Waveform Sets USed)、TSUS, TSUS? - (Timing Sets USed)、LSUS, LSUS? - (Level Sets USed)、DSUS, DSUS? - (Dps Sets USed)，源文参数表分别用这些命令确定 waveform、timing、level、DPS set 的最大编号。
- **文档事实** Timing Specification File，源文称 wavetable 由 equation_set_no 与 specset_no 在该文件中所引用的 wavetable 决定。

## 版本

**文档事实** Functional changes 仅记载 Introduced before SmarTest 6.3.2，其后无其他条目。

## 出处

- `02_System_reference/02.06_Command_Reference/02.06.05.02.22_SPRM__SPRM__-__Set_PRiMary_sets.htm`，主源，含 intro、Equation Based Testing、SPRM、SPRM?、Parameters、Application、Errors、Example 与 Functional changes。
