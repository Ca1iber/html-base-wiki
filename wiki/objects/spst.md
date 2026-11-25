---
type: object
title: SPST? - (SPecset STatus)
layer: L1
stage: level
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.23_SPST__-__SPecset_STatus.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# SPST? - (SPecset STatus)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **3,274 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.05.02.23_SPST__-__SPecset_STatus.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
SPST? {spec_type}, {equation_set_no}, {specset_no}
```

returns:

```
SPST {spec_type}, {equation_set_no}, {specset_no}, {status}
```

or,
for multiport
specifications:

```
SPST? {spec_type}, , {"multi-port_spec"}
```

or

```
SPST? {spec_type}, PRM,
```

returns:

```
SPST {spec_type},, {"multi-port_spec"}, {status}
```

### Parameters

[表]
行 1:
  spec_type [跨 3 行]
  Which specification type to use. Use: [跨 2 列]
行 2:
  LEV
  to specify levels, or
行 3:
  TIM
  to specify timing.
行 4:
  equation_set_no
  Equation set number. An integer in the [跨 2 列]
    range 0 to 256.
    
    Use ALL to refer to all defined equation sets. Use PRM to specify the primary equation set. In the latter case, the specset_no parameter is ignored.
    
    Equation set 0 is used for compatibility with a non-equation based testing environment.
    In this case, when equation set 0 is used and spec_type is
    LEV, specset_no is meaningless, while when equation
    set 0 is used and spec_type is TIM,
    specset_no is interpreted as the number of a waveform set.
行 5:
  specset_no
  Spec set number. An integer in the range 1 [跨 2 列]
    to 99. Use ALL to refer to all defined spec sets.
行 6:
  multi-port_spec
  In a multi-port setup, enter the name of a [跨 2 列]
    specification instead of a spec set number. In this case, the equation_set_no parameter must be left empty.
行 7:
  status
  An integer that indicates the settings of the status [跨 2 列]
    bits. Every set bit is represented by a power of 2, as described in the table below. The
    integer is the sum of these powers.
    
    For example, if 768 = 512 + 256 is returned, then bits 8 and 9 are set, and all other
    bits are cleared.
[表] Status bits for the status parameter
列: Bit | Description | Value
行 1:
  0
  Not available/defined.
  1
行 2:
  1
  Drive 1 period limit violation.
  2
行 3:
  2
  Receive 1 period limit violation.
  4
行 4:
  3
  Drive 2 period limit violation.
  8
行 5:
  4
  Receive 2 period limit violation.
  16
行 6:
  5
  Drive edge order violation.
  32
行 7:
  6
  Tri-state edge order violation.
  64
行 8:
  7
  Window edge order violation.
  128
行 9:
  8
  It is possible to modify the timing or level data with `ETIM`（raw: `98600.htm`）(`ETDS`（raw: `98599.htm`）), `PCLK`（raw: `98682.htm`）, `CLKR`（raw: `98504.htm`）, `DRLV`（raw: `98577.htm`）, `RCLV`（raw: `98717.htm`）, `TERM`（raw: `98771.htm`）,
    and `PSLV`（raw: `98702.htm`）. If any of these commands are executed, this bit is set
    automatically for the affected specset, and the restore should bring back the original
    SPST status.
  256
行 10:
  9
  Modified with `SHVL`（raw: `98733.htm`）.
  512
行 11:
  10
  Modified with `SVLR`（raw: `98764.htm`）.
  1024
行 12:
  12
  Absolute range violation.
  2048
行 13:
  13
  Relative range violation
  4096
行 14:
  14
  Drive 10 period limit violation
  8192
行 15:
  15
  Receive 10 period limit violation
  16384

### Examples

### Example 1
```
> SPST? lev,all,all
< SPST LEV,1,1,0
```

### Example 2
```
> SPST? tim,all,all
< SPST TIM,1,1,0
< SPST TIM,2,22,0
```

### Example 3
```
> SPST? TIM,,"mu_burst"
< SPST TIM,,"mu_burst",6
```

In this
last example, a multi-port specification is queried. The answer says that bits 1 and 2 have been
set. This has the effect that a drive or receive period 1 limit violation will be ignored, and
only a period 2 limit violation will be recorded.

<!-- 语法节 end -->

## 是什么

**文档事实** `SPST?` 返回当前 status bit 的设置。多数 bit 决定测试执行时对 edge order 与 period 做哪类 violation check：关联 bit 被清除时执行检查，被置位时省略检查；其余 bit 表示 timing 是否被特定固件命令修改过。

**文档事实** 该命令可取得 site-specific 信息，但同一时刻只能有一个 site 处于 focus。对 focus 中的 site，SmarTest 在 Testflow Editor 与 result tools 中显示结果；任何固件查询也只报告当前 focus site 的 setup 与结果。

**文档事实** `spec_type` 取 `LEV`（levels）或 `TIM`（timing）；`equation_set_no` 为 0–256，可用 `ALL`、`PRM`（primary equation set，此时忽略 `specset_no`）；`specset_no` 为 1–99，可用 `ALL`。

**文档事实** equation set 0 用于与非 equation based 测试环境兼容：`spec_type` 为 `LEV` 时 `specset_no` 无意义；为 `TIM` 时 `specset_no` 被解释为 waveform set 编号。

**文档事实** 多端口时用 `SPST? {spec_type}, , {"multi-port_spec"}` 查询，此时 `equation_set_no` 必须留空；也支持 `SPST? {spec_type}, PRM,` 形式。

**文档事实** `status` 是各置位 bit 对应 2 的幂之和；例如 768 = 512 + 256 表示 bit 8 与 bit 9 置位、其余清零。bit 8 表示 timing/level 数据被 ETIM/ETDS/PCLK/CLKR/DRLV/RCLV/TERM/PSLV 修改过（restore 应带回原 SPST 状态），bit 9 对应 SHVL，bit 10 对应 SVLR；bit 12/13 为 absolute/relative range violation，bit 14/15 为 drive/receive 10 period limit violation。

## 典型用法

**文档事实** `SPST? lev,all,all` 返回 `SPST LEV,1,1,0`。

**文档事实** `SPST? tim,all,all` 返回 `SPST TIM,1,1,0` 与 `SPST TIM,2,22,0`。

**文档事实** `SPST? TIM,,"mu_burst"` 返回 `SPST TIM,,"mu_burst",6`。6 = bit 1 + bit 2，表示 drive 或 receive 的 period 1 limit violation 被忽略，只记录 period 2 limit violation。

**文档事实** Application 段列出四个使用场景：Level setup、Timing setup、Testflow、Spec tool。

## 和谁有关

- **文档事实** `[[etim]]`、`[[etds]]`、`[[pclk]]`、`[[clkr]]`、`[[drlv]]`、`[[rclv]]`、`[[term]]`、`[[pslv]]` — status bit 8 的说明把这些命令列为会修改 timing/level 数据的命令；执行其中任一命令会自动为受影响的 specset 置该 bit，restore 应恢复原 SPST 状态。
- **文档事实** `[[svlr]]` — status bit 10 的说明是 “Modified with SVLR”。
- **文档事实** `SHVL` — status bit 9 的说明是 “Modified with SHVL”；该命令没有独立对象页。
- **文档事实** `[[spec-set]]` — 参数 `specset_no` 指向 spec set（1–99，ALL），SPST? 查询的就是该 specset 的 status；`spec_type` 区分 LEV 与 TIM。
- **文档事实** `[[timing-specification]]` — 多端口查询参数是 `multi-port_spec`（specification 名）；本命令按 equation set/spec set 或 multiport specification 两种方式定位查询对象。
- **推断** Application 段列的 Level setup、Timing setup、Testflow、Spec tool 分别对应 `[[level-setup-tool]]`、`[[timing-setup-tool]]`、`[[testflow-tool]]`、`[[spec-tool]]`；文档没有逐项点名工具页。

## 版本

**文档事实** Functional changes 记载 “Introduced before SmarTest 6.3.2”。

## 出处

- `02_System_reference/02.06_Command_Reference/02.06.05.02.23_SPST__-__SPecset_STatus.htm`，主源，含 status bit 行为、site focus 说明、语法/参数、Application、三个示例与 Functional changes。
