---
type: object
title: ETIM, ETIM? - (Edge TIMing)
layer: L1
stage: timing
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.118_ETIM__ETIM__-__Edge_TIMing.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# ETIM, ETIM? - (Edge TIMing)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,949 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.118_ETIM__ETIM__-__Edge_TIMing.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### ETIM

```
ETIM {waveform_set},{timing_set}, [t1], [t2], [t3], [t4], [t5], [t6], {(pinlist)}
```

### ETIM?

```
ETIM? {waveform_set}, {timing_set}, {(pinlist)}
```

returns:

```
ETIM {waveform_set},{timing_set}, [t1], [t2], [t3], [t4], [t5], [t6], {(pinlist)}
```

or:

```
ETIM? {specset_id}, {timing_set_no}, {(pinlist)}
```

returns:

```
ETIM {specset_id}, {timing_set_no}, [t1], [t2], [t3], [t4], [t5], [t6],{(pinlist)}
```
[表] Parameters
行 1:
  waveform_set
  Waveform Set Number. Enter PRM for the Primary Waveform Set, or
    an integer in the range 1 to the maximum number of allowed waveform sets. The maximum
    number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `98878.htm`）. For the query command you can also enter
    ALL for all waveform sets.
行 2:
  specset_id
  Derived as follows:
    
    100 *equation_set_no +
    specset_no
行 3:
  timing_set
  Timing Set Number. Enter PRM for the Primary Timing Set,
    ALL for all timing sets, or an integer in the range 1 to the maximum
    number of allowed timing sets. The maximum number is determined by TSUS.
行 4:
  t1..t6
  Edge delay in ns. Note that the positions of some edges may be affected by the use
    and position of previously defined edges as explained in "Restrictions" in `ETIM, ETIM? - (Edge TIMing)`（raw: `98600.htm`）.
行 5:
  pinlist
  The name of the pin or pins for which edge delays are to be set or read back. This
    parameter can also include groups previously created by the DFGP (DeFine
    GrouP) command. The symbol @ can be used to specify all configured pins. If more
    than one pin is to be included, the names must be separated with a comma.

### Example

```
ETIM 1,1,2,4,8,6,10,,(DATA)
```

This example sets the edge delays
for the pin group DATA specified for waveform set 1 and timing set 1. Edges 1 to 5 are set to
2,4,8,6 and 10 ns respectively, edge 6 is unused. If no previous setting for edge 6 exists in
waveform set 1 and timing set 1, then its delay remains at 0.0 ns.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.118_ETIM__ETIM__-__Edge_TIMing.htm>` 的 `## Errors` 段。**不是转述。**
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

`WFDF, WFDF? - (WaveForm DeFinition)`（raw: `98871.htm`）
, or the break waveform definition -
`BWDF, BWDF? - (Break Waveform DeFinition)`（raw: `98497.htm`）
.

Edge placement is outside the allowed range.

All edges of the same direction in the specified timing set do not lie within one period.

specset_id
 does not reference a defined wavetable.

specset_id
 is invalid because
equation_set_no
,

specset_no
, or both are invalid.

<!-- 报错节 end -->

## 是什么

**文档事实** ETIM（Edge TIMing）命令为指定的 waveform set、timing set 与 pin 定义 edge timing；已定义的 waveform set 与 timing set 数量不变。

**文档事实** edge delay 参数可选；缺失的 delay 由系统从数据库提供，此前从未设置过的 delay 默认为 0.0 ns；系统不做自动修正，非法值会被拒绝。省略或未使用的 timing 参数必须留逗号占位。

**文档事实** ETIM? 查询返回所有 event 的 delay；query 中 waveform_set 可写 ALL，timing_set 也可写 ALL，PRM 表示 Primary Waveform Set / Primary Timing Set。

**文档事实** 在 Equation Based Testing 中用 specset_id 代替 waveform set，specset_id = 100 × equation_set_no + specset_no；对应 wavetable 由 Timing Specification File 中 equation_set_no 与 specset_no 所引用的 wavetable 确定。ETIM 会置位 status bit 8，表示 equation based 值已被覆盖（详见 SPST?）。

**文档事实** 对包含多于 6 个 edge 的 pin / waveform set，ETIM 命令被禁用。

**文档事实** 首段称：自 release 2.1 起，使用 14-edge setup 时由 ETDS、ETDS? 取代 ETIM。

**文档事实** 命令配置拥有 setup focus 的 site；同一时刻只有一个 site 处于 focus，SmarTest 只在 Testflow Editor 与 result tools 中显示该 site 的结果，firmware query 也只报告该 site 的 setup 与结果（见 PSFC）。

**文档事实** Restrictions：同一 waveform 中使用同一资源的 action（drive、tri-state 或 window formatter）必须按 WFDF 与 BWDF 规定的顺序排列；用于 window compare 的所有 receive edge 必须物理有序，例如关闭窗口的 edge 必须在打开它的 edge 之后（见 Selecting and ordering edges）。

**文档事实** Application 段把 ETIM 归入 Timing setup，并指向 Timing Setup Commands 页。

**推断** 由于 ETIM 只接受 6 个 edge delay（t1..t6）且对多于 6 个 edge 的 set 禁用，14-edge setup 需要改用 ETDS 的 definition string 形式来表达。

## 典型用法

**文档事实** 设置 edge delay：`ETIM 1,1,2,4,8,6,10,,(DATA)` 为 waveform set 1、timing set 1 的 pin group DATA 设置 edge 1..5 为 2、4、8、6、10 ns，edge 6 不用；若此前 edge 6 无设置，其 delay 保持 0.0 ns。

**文档事实** 查询：`ETIM? {waveform_set}, {timing_set}, {(pinlist)}`；也可写 `ETIM? {specset_id}, {timing_set_no}, {(pinlist)}`，返回 `ETIM ... [t1]..[t6], (pinlist)`。

**文档事实** pinlist 可写单个 pin、逗号分隔的多个 pin、DFGP（DeFine GrouP）创建的 group；`@` 表示所有已配置 pin。

**文档事实** waveform_set 的上限由 WSUS 决定，timing_set 的上限由 TSUS 决定；超出范围会报错。

**建议** 若目标的 edge 数超过 6（尤其是 14-edge setup），按文档首段改用 ETDS、ETDS?，不要依赖 ETIM。

## 和谁有关

- **文档事实** `[[etds]]` — ETIM 首段称自 release 2.1 起、使用 14-edge setup 时由 ETDS/ETDS? 取代 ETIM；ETDS 首段则称自 release 2.0 起对多于 6 个 edge 的 waveform 取代 ETIM。两处关于起始 release 与适用条件的表述不一致，本页并列记录。
- **文档事实** WFDF（WaveForm DeFinition，`02_System_reference/02.06_Command_Reference/02.06.02.02.334_WFDF__WFDF__-__WaveForm_DeFinition.htm`）与 `[[bwdf]]` — ETIM 的 See also 列 WFDF；Restrictions 要求 action 顺序符合 WFDF/BWDF；Errors 把 edge 顺序错误归因于 timing set 与 WFDF/BWDF 定义不匹配。注意 ETIM 源链的是 WFDF，而非 WFDS。
- **文档事实** `[[wave]]` — ETIM 的 See also 与 WFDF 一并列出 WAVE（WAVEform）；文档称 all four commands are required to generate DUT test signal timing（原文未逐一列出这四个命令）。
- **文档事实** `[[wsus]]`、`[[tsus]]` — waveform_set / timing_set 的上限分别由 WSUS / TSUS 决定，超出该范围即报错。
- **文档事实** `[[psfc]]` — 主源说明本命令配置拥有 setup focus 的 site，并在同段链到 PSFC（Parallel Setup FoCus）。
- **文档事实** `[[spst]]` — 主源 Note 称 ETIM 置 status bit 8 表示 equation based 值已被覆盖，并指向 SPST? 查询；SPST 页把 ETIM(ETDS) 与 PCLK、CLKR、DRLV、RCLV、TERM、PSLV 并列为会修改 timing/level 数据的命令。
- **文档事实** `[[dfgp]]` — pinlist 可包含由 DFGP（DeFine GrouP）创建的 group，`@` 表示所有已配置 pin。
- **文档事实** 命令总表 `02.06.02.02_List_of_commands.htm` 与 `02.06.01.05_Site_dependent_firmware_commands.htm` 列出 ETIM、ETIM?（objpack 入边）。

## 版本

**文档事实** Functional changes 记：`Introduced before SmarTest 6.3.2`。

**文档事实** 首段另称：自 release 2.1 起，使用 14-edge setup 时由 ETDS/ETDS? 取代 ETIM；此条不在 Functional changes 中。ETDS 页对取代起点写 release 2.0、条件写多于 6 个 edge，二者不一致（见「和谁有关」）。

## 出处

- `02_System_reference/02.06_Command_Reference/02.06.02.02.118_ETIM__ETIM__-__Edge_TIMing.htm`，主源，含首段、Restrictions、Equation Based Testing、语法/参数、Application、Errors、Example 与 Functional changes，已用 `show.py` 与 `objpack.py` 读取。
- `02_System_reference/02.06_Command_Reference/02.06.02.02.117_ETDS__ETDS__-__Edge_Timing_Definition_String.htm`，用于核对 ETDS 取代 ETIM 的 release 与条件（首段），已用 `show.py` 读取。
- 入边清单（List of commands、Site dependent firmware commands、SPST 等）取自 `extract/objpack.py` 的 `edges.jsonl` 语境。
