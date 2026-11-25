---
type: object
title: CLKR, CLKR? - (CLocK Resolution)
layer: L1
stage: timing
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.24_CLKR__CLKR__-__CLocK_Resolution.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# CLKR, CLKR? - (CLocK Resolution)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,973 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.24_CLKR__CLKR__-__CLocK_Resolution.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### CLKR

```
CLKR {waveform_set|specset_id|"multi-port_spec"}, [ref_period],{period_res}
```

### CLKR?

```
CLKR?[type,] {waveform_set|specset_id|"multi-port_spec"}
```

returns:

```
CLKR {waveform_set|specset_id|"multi-port_spec"}, [ref_period],{period_res|clock_res}
```

### Parameters

[表]
行 1:
  waveform_set
  Waveform Set Number. Enter an integer in the range 1 to the maximum number of
    allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `98878.htm`）. For the
    query command you can also enter ALL for all waveform sets.
行 2:
  specset_id
  Derived as follows:
    
    100 * equation_set_no +
    specset_no
行 3:
  multi-port_spec
  To set or query the resolution of a multi-port timing specification, specify the
    name of the specification.
行 4:
  ref_period
  Not used. (Ignored)
行 5:
  period_res
  The period resolution (in ns) for the specified specification or waveform set.
    
    If necessary, period_res is rounded to nine digits after the decimal
    point. The allowable maximum period resolution is the maximum tester period value. The
    minimum period resolution is determined by the hardware (see `Automatic calculation of period resolution for single-port setups`（raw: `98092.htm`）).
行 6:
  type
  In the query, the type parameter specifies which resolution is queried. The
    allowed values are:
    
    VIRTUAL: The period resolution (period_res) is
    queried. This is the default.
    
    EXACT: The clock resolution (clock_res) is
    queried.
行 7:
  clock_res
  In the answer to the query, the clock resolution is returned if type is set to
    EXACT in the query.

### Example

```
> CLKR 1,,10
> CLKR? 1
< CLKR 1,1000,10
```

This example sets and queries the period resolution (10 ns) for waveform set 1. Ignore
the returned value of the
ref_period
 parameter.

```
> CLKR? "spec_port_1_port_2"
< CLKR "spec_port_1_port_2",50,5.555555556
```

This
example queries the period resolution for the multi-port specification

spec_port_1_port_2
.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.24_CLKR__CLKR__-__CLocK_Resolution.htm>` 的 `## Errors` 段。**不是转述。**
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

waveform_set
 is less than 1.

waveform_set
 is greater than the range allowed by the
`WSUS`（raw: `98878.htm`）
 command.

period_res
 is outside the allowed range.

<!-- 报错节 end -->

## 是什么

**文档事实**：`CLKR` 为 single-port 或 multi-port timing specification，或为 waveform set 定义 period resolution。

**文档事实**：`Postdependencies`：一旦用 `CLKR` 定义 period resolution，系统就不再在用 `PCLK` 全局（所有 pin）修改 timing set 1 的 tester period 时自动重算它。与 equation based timing 联用时，`CLKR` 只改 period resolution 的运行时值；equation set 内用 `period_res` 关键字的定义不会被改。

**文档事实**：`waveform_set` 取 1 到 `WSUS` 决定的最大 waveform set 数；查询时可写 `ALL`。

**文档事实**：equation based timing 的 `specset_id = 100 * equation_set_no + specset_no`。

**文档事实**：multi-port timing specification 用带引号的名称 `"multi-port_spec"` 指定。

**文档事实**：`ref_period` 不使用（被忽略）。

**文档事实**：`period_res` 单位 ns；必要时舍入到小数点后 9 位；允许的最大 period resolution 是最大 tester period，最小值由硬件决定（见 `Automatic calculation of period resolution for single-port setups`）。

**文档事实**：查询的 `type` 取 `VIRTUAL`（默认，查询 period resolution，返回 `period_res`）或 `EXACT`（查询 clock resolution，返回 `clock_res`）。

## 典型用法

**文档事实**：为 waveform set 1 设置并查询 period resolution（10 ns）：

```
> CLKR 1,,10
> CLKR? 1
< CLKR 1,1000,10
```

**文档事实**：源文说明 `ref_period` 位置留空；返回的 `1000` 是 `ref_period`，应忽略。

**文档事实**：查询 multi-port specification `spec_port_1_port_2` 的 period resolution：

```
> CLKR? "spec_port_1_port_2"
< CLKR "spec_port_1_port_2",50,5.555555556
```

**文档事实**：查询时把 `type` 设为 `EXACT` 会返回 clock resolution（`clock_res`），而不是 period resolution。

**文档事实**：查询 waveform set 时可在 `waveform_set` 位置写 `ALL`，覆盖所有 waveform set。

## 和谁有关

**文档事实**：以下关系都有源文正文、参数说明或入边支撑；每条注明为什么相关。

- [[wsus]]：`waveform_set` 的上限由 `WSUS` 决定；`Errors` 中“waveform_set 超出 `WSUS` 允许范围”也点名它。
- [[pclk]]：`Postdependencies` 说明用 `CLKR` 定义 period resolution 后，`PCLK` 全局改 timing set 1 的 tester period 时系统不再重算。
- [[spst]]：`SPST?` 文档说 `ETIM`/`PCLK`/`CLKR`/`DRLV` 等修改 timing 或 level data 时，受影响 specset 的 `SPST` 位会被自动置位。为什么：`CLKR` 是修改 timing data 的命令之一。
- `Clock domain per pin`（`02_System_reference/02.05_Test_Head_Cards/02.05.04.03.01_Clock_domain_per_pin.htm`）：该页说 multiport setup 的 period resolution 细节见本页。
- `Determining the period resolution`（`02_System_reference/02.06_Command_Reference/02.06.06.01.04.01.02_Determining_the_period_resolution.htm`）：本页 `Related information` 指向它。
- `Automatic calculation of period resolution for single-port setups`（`02_System_reference/02.06_Command_Reference/02.06.06.01.04.01.02.01_Automatic_calculation_of_period_resolution_for_single-port_setups.htm`）：本页说 period resolution 最小值由硬件决定并指向它。
- `Period resolution, clock resolution, and master clock period`（`02_System_reference/02.06_Command_Reference/02.06.06.01.04.01.02.03_Period_resolution__clock_resolution__and_master_clock_period.htm`）：该页说可用 `CLKR? EXACT` 取 clock resolution，并以 PS1600 为例给出算法。
- `Timing Setup Commands`（`02_System_reference/02.06_Command_Reference/02.06.06_Timing_Setup_Commands.htm`）：本页 `Application` 指到该章。
- `Executing Firmware Commands from the Prompt`（`02_System_reference/02.06_Command_Reference/02.06.01.03.02_Executing_Firmware_Commands_from_the_Prompt.htm`）：回链本页，作为语法细节参考。

## 版本

**文档事实**：`Functional changes` 只有 `Introduced before SmarTest 6.3.2`，没有其他版本记录。

**推断**：这一写法是文档集的哨兵，表示该内容在 6.3.2 之前已存在，不能当作 6.3.2 引入。

## 出处

- 主源：`02_System_reference/02.06_Command_Reference/02.06.02.02.24_CLKR__CLKR__-__CLocK_Resolution.htm`（正文、Postdependencies、Parameters、Application、Errors、Example、Related information、Functional changes）。
- 关系证据：`extract/objpack.py` 的入边（`02.06.02.02_List_of_commands`、`02.06.01.03.02_Executing_Firmware_Commands_from_the_Prompt`、`02.05.04.03.01_Clock_domain_per_pin`、`02.06.06.01.04.01.02.03_Period_resolution...`、`SPST` 页等）。
