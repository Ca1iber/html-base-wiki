---
type: object
title: BWDF, BWDF? - (Break Waveform DeFinition)
layer: L1
stage: timing
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.13_BWDF__BWDF__-__Break_Waveform_DeFinition.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# BWDF, BWDF? - (Break Waveform DeFinition)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,822 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.13_BWDF__BWDF__-__Break_Waveform_DeFinition.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### BWDF

```
BWDF {wvf_set}, {a1}, {a2}, {a3}, {a4}, {a5}, {a6}, {(pinlist)}
```

### BWDF?

```
BWDF? {wvf_set|"wavetable_name"|specset_id|"multiport_spec"}, {(pinlist)}
```

returns:

```
BWDF {wvf_set|"wavetable_name"|specset_id|"multiport_spec"}, {a1}, {a2}, {a3}, {a4}, {a5}, {a6}, {(pinlist)}
```

### Parameters

[表]
行 1:
  wvf_set
  Waveform Set Number. Enter [跨 2 列]
    ALL for all waveform sets, or an integer in the range 1 to the maximum
    number of allowed waveform sets. The maximum number is determined by the command `WSUS, WSUS? - (Waveform Sets USed)`（raw: `98878.htm`）.
行 2:
  specset_id
  Derived as follows: [跨 2 列]
    
    100 * equation_set_no +
    specset_no
行 3:
  wavetable_name
  The wavetable name. Enter a string of up to [跨 2 列]
    40 alphanumeric characters (upper or lower case) enclosed in double quotes.
行 4:
  multiport_spec
  To query a multi-port specification, enter [跨 2 列]
    the name of the specification.
行 5:
  a1..a6 [跨 10 行]
  Edge action. The actions you can define [跨 2 列]
    are:
行 6:
  N
  no action
行 7:
  F0N
  drive 0, no tri-state action
行 8:
  F1N
  drive 1, no tri-state action
行 9:
  FN0
  no drive action, tri-state off
行 10:
  FNZ
  no drive action, tri-state on
行 11:
  F00
  drive 0, tri-state off
行 12:
  F0Z
  drive 0, tri-state on
行 13:
  F10
  drive 1, tri-state off
行 14:
  F1Z
  drive 1, tri-state on
行 15:
  pinlist
  The name of the pin or pins for which break [跨 2 列]
    waveform definitions are to be made or read back. The symbol @ can be used to
    specify all configured input and IO pins. If more than one pin is to be included, the names
    must be separated with a comma.

### Example

```
BWDF 1,N,N,N,F1N,F0N,N,(D0,D1,D2,D3)
```

This example defines a
pulse for waveform set 1, and for pins D0 to D3, driving to 1 at edge action 4 and to 0 at edge
action 5. The tri-state formatter is not used.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.13_BWDF__BWDF__-__Break_Waveform_DeFinition.htm>` 的 `## Errors` 段。**不是转述。**
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

waveform_set
 is greater than the range allowed by the command
`WSUS, WSUS? - (Waveform Sets USed)`（raw: `98878.htm`）
.

There is a mismatch between the edge actions and edge order in the specified waveform.

A tri-state action is defined or implicitly required on edge 2 or 5.

specset_id
 is invalid because
equation_set_no
,

specset_no
, or both are invalid, or because
specset_id
 does not reference a defined wavetable.

<!-- 报错节 end -->

## 是什么

**文档事实** BWDF（Break Waveform DeFinition）为指定 waveform set 定义 break waveform 的动作；只允许 drive actions，break waveform 不得含 data dependent actions，与已定义动作不兼容的边沿延迟会被自动纠正以适配。

**文档事实** BWDF? 查询返回当前 break waveform 的定义。

**文档事实** break waveform 在 sequencer 处于 BREAK 状态时发给 DUT（`Defining the break waveform`，BREAK 状态见 SQST）；该波形不得包含 receive action。若未定义，则使用空定义串的默认 break waveform，即什么都不做。

**文档事实** 从 release 2.1 起，14-edge setup 改用 BWDS/BWDS?；对含多于 6 个 edge 的 pin 与 waveform set，本命令被禁用；查询仍可用，但只返回前 6 个 edge。

**文档事实** Application 为 Timing Setup。

**建议** 新工程直接使用支持 14-edge 的 BWDS/BWDS?；BWDF 只用于维护仍为 6-edge 的旧配置。

## 典型用法

**文档事实** 定义脉冲：`BWDF 1,N,N,N,F1N,F0N,N,(D0,D1,D2,D3)` 为 waveform set 1 的 D0..D3 定义 break waveform，在第 4 个 edge action 驱动 1、第 5 个驱动 0，不使用 tri-state formatter。

**文档事实** `wvf_set` 可填 ALL（所有 waveform set）或 1 到允许的最大 waveform set 数；该上限由 WSUS 决定。

**文档事实** `BWDF?` 的第一个参数可为 `wvf_set`、`"wavetable_name"`（双引号内最多 40 个字母数字字符）、`specset_id`（`100 * equation_set_no + specset_no`）或 `"multiport_spec"`。

**文档事实** 动作码共九种：`N`（无动作）、`F0N`/`F1N`（驱动 0/1，无 tri-state 动作）、`FN0`/`FNZ`（不驱动，tri-state 关/开）、`F00`/`F0Z`（驱动 0，tri-state 关/开）、`F10`/`F1Z`（驱动 1，tri-state 关/开）。

**文档事实** `pinlist` 可写单个 pin 或多个逗号分隔的 pin；`@` 表示所有已配置的 input 与 IO pin。

**文档事实** 报错节限定：edge 2 或 edge 5 上定义或隐含要求 tri-state action 会报错；edge actions 与 waveform 的 edge order 不匹配也会报错。

**建议** 用 `BWDF?` 回读后再改，避免 edge order 与 tri-state 位置踩到报错条件。

## 和谁有关

- **文档事实** BWDS, BWDS?：主源称 release 2.1 起 14-edge setup 由 BWDS/BWDS? 取代 BWDF/BWDF?；BWDS 页也写本命令取代 BWDF，用于 14 个或更多 edge 的 setup。
- **文档事实** WSUS, WSUS?：`wvf_set` 的允许上限由 WSUS 决定，报错节也以 WSUS 范围为判据。
- **文档事实** ETIM, ETIM? 与 WFDF：ETIM 页要求同一 waveform 中使用同一资源（drive、tri-state、window formatter）的动作按 WFDF 与 BWDF 的规格排序；其错误说明提到选定 timing set 的 edge 延迟与波形不匹配。
- **文档事实** VWFG?：检查 waveform definitions 时把 WFDF、WAVE、BWDF 的参数（waveform set number、edge actions、data parameters）计入比较。
- **文档事实** Defining the break waveform：说明 break waveform 在 BREAK 状态发出、不得含 receive action、未定义时默认空；其 Related firmware commands 指向 BWDS? 查询。
- **文档事实** DUT Input Stability：用 PMU 做 DC 测量时 DUT 必须稳定，多数测量在 break state 进行，因此必须确保 active waveform set 的 break waveform 不引起 toggling；该页明确说 break waveform 由 BWDF 设置。
- **文档事实** SQST：BREAK 状态的定义见 SQST（`Defining the break waveform` 的指引）。
- **文档事实** Data Queue：其 FLQU「fill break vectors」说明引用了 BWDF（入边）。
- **文档事实** List of commands / Timing Setup Commands：BWDF 列在命令参考总表，Application 指向 Timing Setup。

## 版本

**文档事实** Functional changes 记：Introduced before SmarTest 6.3.2。

**文档事实** 主源另记版本相关变更：release 2.1 起 14-edge setup 由 BWDS/BWDS? 取代；含多于 6 个 edge 的 pin/waveform set 禁用 BWDF，查询只返回前 6 个 edge。

## 出处

- `02_System_reference/02.06_Command_Reference/02.06.02.02.13_BWDF__BWDF__-__Break_Waveform_DeFinition.htm`，主源，含概览、Syntax、Parameters、Application、Errors、Example 与 Functional changes，已用 `show.py` 读取。
- `02_System_reference/02.06_Command_Reference/02.06.02.02.14_BWDS__BWDS__-__Break_Waveform_Definition_String.htm`、`02.06.02.02.118_ETIM__ETIM__-__Edge_TIMing.htm`、`02.06.02.02.330_VWFG__-__Verify_WaveForms_in_Groups.htm`，用于取代关系与 edge/波形检查关系，已用 `show.py` 读取。
- `02_System_reference/02.06_Command_Reference/02.06.06.01.03.03_Defining_the_break_waveform.htm`、`02.06.10.01.02.01_DUT_Input_Stability.htm`，用于 break waveform 概念与 PMU 稳定度关系，已用 `show.py` 读取。
- 入边语境取自 `extract/objpack.py` / `edges.jsonl`。
