---
type: object
title: ETDS, ETDS? - (Edge Timing Definition String)
layer: L1
stage: timing
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.117_ETDS__ETDS__-__Edge_Timing_Definition_String.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# ETDS, ETDS? - (Edge Timing Definition String)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **6,920 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.117_ETDS__ETDS__-__Edge_Timing_Definition_String.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### ETDS

ETDS

{
waveform_set
|
specset_id
|"
multi-port_spec
"},
{
timing_set
}, [
mode
],
{
definition_string
}, {(
pinlist
)}

### ETDS?

ETDS?

{
waveform_set
|
specset_id
|"
multi-port_spec
"},
{
timing_set
}, [
mode
],
{(
pinlist
)}

returns:

ETDS

{
waveform_set
|
specset_id
|"
multi-port_spec
"},
{
timing_set
}, [
mode
],
{
definition_string
}, {(
pinlist
)}

### Parameters

[表]
行 1:
  waveform_set
  Waveform Set Number. Enter PRM for the Primary Waveform Set, or
    an integer in the range 1 to the maximum number of allowed waveform sets. The maximum
    number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `98878.htm`）. For the query, you can also enter
    ALL for all waveform sets.
行 2:
  specset_id
  Derived as follows:
    
    100 *equation_set_no +
    specset_no
行 3:
  multi-port_spec
  For a multi-port setup, specify the name of a multi-port specification.
    
    Note that the multi-port specification uniquely determines an equation set for every pin
    of pinlist, because no pin can belong to more than one port within a
    multi-port specification.
行 4:
  timing_set
  Timing Set Number. Enter PRM for the Primary Timing Set,
    ALL for all timing sets, or an integer in the range 1 to the maximum
    number of allowed timing sets. The maximum number is determined by
    TSUS.
行 5:
  mode
  The operating mode. For the query, you can enter ALL for all modes
    or BIDIR for bidirectional mode, that is, for edges that serve both as
    drive and receive edges.
    
    With fast pins, you can specify the mode DELTA for both the command
    and the query. In this mode, the delays specified for edges with an index > 1 are
    interpreted as offsets from the calculated default values.
行 6:
  definition_string
  The definition string consists of a sequence of items each of which associates a
    delay with a drive or compare edge. On Pin Scale 800/3600 boards, drive edges are denoted
    by dn. On Pin Scale 9G boards, there
    are two kinds of drive edges, which are denoted by fn
    and sn, respectively; for details see `Defining waveforms for Pin Scale 9G pins`（raw: `113740.htm`）. You can also use the dn notation
    for Pin Scale 9G channels, but mixing both notations in one string is not
    allowed. Receive edges are always denoted by rn.
    
    Unless you employ the pdiv statement for fast pins (see below), all
    edges which are not explicitly set remain unchanged.
    
    The range of the edge delay is -8000 ns to +24000 ns (or -4 to +12 test system periods)
    for the Pin Scale 3600/800.
    
    On Pin Scale 800/3600 boards, the restrictions for edge ordering must be observed both in
    fixed and equation based timing. For example, you cannot assign a greater delay to d1 than to d3 if d1 precedes
    d3 in a waveform definition. For more information, see `Selecting and ordering edges`（raw: `10608.htm`）.
    
    Note that with equation based timing, ETDS returns no error message
    when the edge order restrictions are violated.
    
    On Pin Scale 9G boards, ordering of drive edges is not restricted in any
    way.
行 7:
  
  Special Rules for Fast Pins:
    
    If a pin is configured as a fast pin in the context of the specification given by the
    first parameter, you can specify the period divider at the start of the definition string.
    The format is pdiv:n, where n must
    be the same value as the period_div value of the pins in
    pinlist within the timing set specified by the timing_set parameter.
    
    If you specify pdiv:nand a delay for the
    first edge, ETDS calculates delays for the following
    n-1 edges except those that are specified explicitly in the string.
    Note that for n = 3, the edges with index 1, 3, 5 are used for internal
    reasons.
    
    If you omit either pdiv or the first edge, only the specified edges
    are modified. However, with receive edges this is only possible for
    r1.
    
    The calculated delays are determined for the ith edge by the following
    formula:
    
     1st_edge_delay + (i-1) *
    (period/pdiv)
    
    1st_edge_delay is the delay specified for the first edge
    (d1 or r1; the generic notation
    e1 is not allowed for fast pins). If the first edge is not
    specified in the string, its delay is set to 0. An example for the calculation will be
    given below.
    
    Note that when both the period divider and a delay for the first edge are present in the
    definition string, then the delays for all the edges required by the period divider will be
    overwritten.
    
    When a delay is explicitly specified for one of the edges, this delay overrides the
    calculated default. There are two formats to specify overrides. You can either define
    absolute delays or the offsets from the default delays.
    
    If you want to use the second, relative format, you must specify DELTA for the modeparameter. Note that you can also specify negative
    offsets in the DELTA mode.
行 8:
  pinlist
  The name of the pin or pins for which edge delays are to be set or read back. This
    parameter can also include groups previously created by the DFGP (DeFine
    GrouP) command. The symbol @ can be used to specify all configured pins.
    If more than one pin is to be included, the names must be separated with a comma.
    
    In a multi-port setup, every pin must belong to a port of the specified
    specification.

### Examples

### Example 1
```
> ETDS 1,1,,"e1:0 e2:2 e3:6 e4:4",(io)
> ETDS 1,1,,"d1:0 d2:1 d3:2 d4:3 d5:4 d6:5 d7:6 d8:7",(clk)
> ETDS? 1,1,,(@)
< ETDS 1,1,,"d1:0 d2:2 d3:6 d4:4 r1:0 r2:2 r3:6 r4:4",(io)
< ETDS 1,1,,"d1:0 d2:1 d3:2 d4:3 d5:4 d6:5 d7:6 d8:7",(clk)
```

### Example 2

The following example shows the various possibilities for
using
ETDS
 with fast
pins:

```
> ETDS? 401,1,,(CP)
< ETDS 401,1,,"pdiv:4 d1:0 d2:5 d3:10 d4:15",(CP)
> ETDS 401,1,,"d2:5.5",(CP)
> ETDS? 401,1,,(CP)
< ETDS 401,1,,"pdiv:4 d1:0 d2:5.5 d3:10 d4:15",(CP)
> ETDS 401,1,,"pdiv:4 d1:3 d3:14",(CP)
> ETDS? 401,1,,(CP)
< ETDS 401,1,,"pdiv:4 d1:3 d2:8 d3:14 d4:18",(CP)
> ETDS 401,1,DELTA,"d3:-1",(CP)
> ETDS? 401,1,,(CP)
< ETDS 401,1,,"pdiv:4 d1:3 d2:8 d3:12 d4:18",(CP)
> ETDS 401,1,DELTA,"pdiv:4 d1:0 d2:1 d4:-1",(CP)
> ETDS? 401,1,,(CP)
< ETDS 401,1,,"pdiv:4 d1:0 d2:6 d3:10 d4:14",(CP)
```

Note
in particular the effect of the first instance of the command in
DELTA
 mode.
The negative offset is not applied to the actual value of d3, which is 14, but to the calculated
default value, which is 13.

### Example 3

This example shows how to set and retrieve a delay of a
multi-port
specification:

```
> ETDS? "mu_timing",2,,(In1)
< ETDS ETDS "mu_timing",2,,"d1:0",(In1)
> ETDS "mu_timing",2,,"d1:0.5",(In1)
> ETDS? "mu_timing",2,,(In1)
< ETDS "mu_timing",2,,"d1:0.5",(In1)
```

The
specification name and the pin name identify the port (no pin may occur in more than one port
within the same specification). Then the port and the specification identify the equation
set.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.117_ETDS__ETDS__-__Edge_Timing_Definition_String.htm>` 的 `## Errors` 段。**不是转述。**
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

waveform_set
 is greater than the range allowed by the
`WSUS`（raw: `98878.htm`）
command.

timing_set
 is greater than the range allowed by the
`TSUS`（raw: `98817.htm`）
command.

The selected primary timing set is not defined for the specified waveform set.

The edge order is wrong; for instance a window open must come before a window close - a
mismatch exists between edge delays of the selected timing set and the waveform definition -

`WFDS, WFDS? - (WaveForm Definition String)`（raw: `98872.htm`）
, or the break waveform definition -
`BWDS, BWDS? - (Break Waveform Definition String)`（raw: `98498.htm`）
.

 Eplacement is outside the allowed range.

 All edges of the same direction in the specified timing set do not lie within one period.

<!-- 报错节 end -->

## 是什么

**文档事实** ETDS（Edge Timing Definition String）命令在已存在的 waveform set/specification 内，为选定的 pin 与 timing set 定义或修改 edge delay。

**文档事实** ETDS? 查询返回当前值，但只返回指定 waveform set/specification 的 wavetable 中用到的 edge，或值不为 0 的 edge。

**文档事实** 该命令配置拥有 setup focus 的 site 的 setup；对处于 focus 的 site，SmarTest 在 Testflow Editor 与 result tool 中显示结果，firmware query 也仅报告当前 focus site 的 setup 与结果。

**文档事实** Mode of operation：edge delay 不必为所有 edge 定义，缺失的 delay 由系统从数据库提供，未设置过的 delay 默认为 0.0 ns；不做自动修正，非法值会被拒绝。与 equation based timing 一起使用时，ETDS 只改运行时值，不改 timing set 中指定的 setup 值。

**文档事实** Postdependencies：命令执行后，primary set 会在下一个 functional test 开始时以新值重新激活。

**文档事实** definition_string 中，drive edge 用 `dn` 表示，receive edge 用 `rn` 表示；Pin Scale 800/3600 板用 `dn`，Pin Scale 9G 板有两类 drive edge（`fn`、`sn`），也可使用 `dn` 写法，但同一字符串中不得混用两种写法。

**文档事实** Fast pin 可在 definition string 开头写 period divider `pdiv:n`；同时给出 `pdiv:n` 和第一个 edge 的 delay 时，ETDS 会计算其后 n-1 个 edge 的 delay（显式指定的除外）；在 `DELTA` 模式下，指定的 delay 被解释为相对默认值的偏移，且允许负偏移。

## 典型用法

**文档事实** 设置后再读回：`ETDS 1,1,,"d1:0 d2:1 d3:2 d4:3 d5:4 d6:5 d7:6 d8:7",(clk)`，用 `ETDS? 1,1,,(@)` 读回（`@` 表示全部已配置 pin）。文档示例中 io 用 `e1:0 e2:2 e3:6 e4:4` 设置后，查询结果显示为 drive 与 receive 两组展开的 `d1:0 d2:2 d3:6 d4:4 r1:0 r2:2 r3:6 r4:4`。

**文档事实** Fast pin 示例：`ETDS? 401,1,,(CP)` 得到 `pdiv:4 d1:0 d2:5 d3:10 d4:15`；`ETDS 401,1,,"d2:5.5",(CP)` 只覆盖 d2；`ETDS 401,1,DELTA,"d3:-1",(CP)` 把 -1 应用到计算出的默认值（13）而不是当前实际值（14）。

**文档事实** Multi-port 示例：`ETDS? "mu_timing",2,,(In1)` 读回，`ETDS "mu_timing",2,,"d1:0.5",(In1)` 设置；specification 名与 pin 名确定 port，port 与 specification 再确定 equation set。

## 和谁有关

- **文档事实** `[[etim]]` — ETDS 首段称此命令从 release 2.0 起，对 edge 数超过 6 的 waveform 取代 ETIM；ETIM 页则称从 release 2.1 起，在 14-edge setup 中使用 ETDS 取代 ETIM。两处关于起始 release 与适用条件的说法不一致，此处并列记录，不自行取舍。
- **文档事实** `[[wfds]]`、`[[bwds]]` — Errors 段把 edge order 错误（例如 window open 必须先于 window close）列为 timing set 的 edge delay 与 waveform definition（WFDS）或 break waveform definition（BWDS）不匹配。
- **文档事实** `[[tsus]]`、`[[wsus]]` — timing_set 与 waveform_set 的上限分别由 TSUS、WSUS 决定；超出该范围会报错。
- **文档事实** `[[vtim]]` — VTIM 页用 `ETDS?` 的结果比较不同 pin 在不同 timing set 中的 edge timing，并用 `ETDS` 修改后再验证。
- **文档事实** `[[spst]]` — SPST 页把 ETIM(ETDS) 与 PCLK、CLKR、DRLV、RCLV、TERM、PSLV 并列为会修改 timing/level 数据并自动置位受影响 specset 的命令。
- **文档事实** `[[psfc]]` — ETDS 页说明命令配置拥有 setup focus 的 site，并在同一段链到 PSFC（Parallel Setup Focus）。
- **文档事实** `DFGP`（`02_System_reference/02.06_Command_Reference/02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.htm`）— pinlist 可包含由 DFGP（DeFine GrouP）创建的 group，`@` 表示所有已配置 pin。
- **文档事实** 命令清单（`02_System_reference/02.06_Command_Reference/02.06.02.02_List_of_commands.htm`、`02_System_reference/02.06_Command_Reference/02.06.01.05_Site_dependent_firmware_commands.htm`）— 这些页面列出 ETDS、ETDS?。

## 版本

**文档事实** Functional changes 只记载 `Introduced before SmarTest 6.3.2`（哨兵值，表示在文档集覆盖范围开始前就已存在）。

**文档事实** 关于取代 ETIM 的起始 release 另有不同说法（见「和谁有关」），它不属本页 Functional changes 的条目。

## 出处

- `02_System_reference/02.06_Command_Reference/02.06.02.02.117_ETDS__ETDS__-__Edge_Timing_Definition_String.htm`，主源，含用途、Mode of operation、Postdependencies、参数表、三个 Example、Errors 与 Functional changes。
- 关系与版本佐证另读 ETIM（`02_System_reference/02.06_Command_Reference/02.06.02.02.118_ETIM__ETIM__-__Edge_TIMing.htm`）、VTIM（`02_System_reference/02.06_Command_Reference/02.06.02.02.329_VTIM__-__Verify_TIMing.htm`）、SPST（`02_System_reference/02.06_Command_Reference/02.06.02.02.229_SPST__-__SPecset_STatus.htm`）、WFDS（`02_System_reference/02.06_Command_Reference/02.06.02.02.335_WFDS__WFDS__-__WaveForm_Definition_String.htm`）、BWDS（`02_System_reference/02.06_Command_Reference/02.06.02.02.14_BWDS__BWDS__-__Break_Waveform_Definition_String.htm`）、TSUS（`02_System_reference/02.06_Command_Reference/02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.htm`）与 WSUS（`02_System_reference/02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.htm`）。
