---
type: object
title: TSUS, TSUS? - (Timing Sets USed)
layer: L1
stage: timing
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# TSUS, TSUS? - (Timing Sets USed)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,774 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### TSUS

```
TSUS {waveform_set},{timing_set}
```

### TSUS?

```
TSUS? {waveform_set}
```

returns:

```
TSUS {waveform_set},{timing_set}
```

Or:

```
TSUS? {specset_id}
```

returns:

```
TSUS {specset_id},{timing_set}
```

Or,
for multiport
specifications:

```
TSUS? {"multiport_spec"}[,(portlist)]
```

returns:

```
TSUS {"multiport_spec"},{timing_set}[,(port)]
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
  Derived as follows: 100 *
    equation_set_no +
    specset_no
行 3:
  multiport_spec
  To query a multiport specification, enter the name of the specification.
行 4:
  timing_set
  Timing set number. This is the highest number currently allocated to a timing set
    or the highest number of timing set you want to associate with a given waveform set. The
    number you enter must be less than or equal to the maximum number of timing sets allowed
    (as defined by the `DSCP`（raw: `98578.htm`） command). This number is automatically
    updated to include any new timing set as it is created. At power-on only one timing set
    (containing the default values and belonging to the single waveform set) is available.
行 5:
  portlist
  For multiport specifications, you can specify a list of the ports for which the
    number of the timing sets used is to be displayed.

### Example

```
TSUS 3,7
```

This example defines a maximum of 7 timing sets in
waveform set 3.

```
TSUS? "spefc",(ARMPort)
TSUS "spefc",3,(ARMPort)
```

This example
queries the number of timing sets defined for port ARMPort in the multiport specification
spefc.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.htm>` 的 `## Errors` 段。**不是转述。**
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

timing_set
 is greater than the range allowed by the
`DSCP`（raw: `98578.htm`）
 command.

waveform_set
 is greater than the range allowed by the
`WSUS`（raw: `98878.htm`）
 command.

waveform_set
 is smaller than 1.

specset_id
 is invalid because
equation_set_no
,

specset_no
, or both are invalid.

specset_id
 does not reference a defined wavetable.

<!-- 报错节 end -->

## 是什么

**文档事实**：TSUS（Timing Sets USed）定义某 waveform set 所含 timing set 的数量；不修改已定义 waveform set 的数量。新值必须是 1 到 CONF 允许的最大 timing set 数之间的整数。DSCP 定义所有 waveform set 的 timing set 总数。

**文档事实**：所有 waveform set 的 timing set 总数上限为 512、默认 256；单个 waveform set 的 timing set 上限为 256；单个 set 的最大数也等于 DSCP 的 timing set 数减去其余 waveform set 已用的 timing set 数。每个 waveform set 至少有一个 timing set，不同 waveform set 可有不同数量（见 Data organization of fixed timing）。

**文档事实**：可用 TSUS 删除 timing set：若当前 waveform set 或要载入硬件的 timing setup 文件所含 timing set 多于需要，TSUS 会删除所有大于指定编号的 set。TSUS? 返回给定 waveform set 当前定义的 timing set 数。

**文档事实**：equation based testing 中以 wavetable 标识，需提供 specset ID：`100 * equation_set_no + specset_no`；对应 wavetable 由 timing specification 文件中 `equation_set_no` 与 `specset_no` 所引用的 wavetable 决定。查询支持 multiport specification 与 portlist。

**文档事实**：Application 归属 Timing setup。

## 典型用法

**文档事实**：`TSUS 3,7` 在 waveform set 3 中定义最多 7 个 timing set（示例）。

**文档事实**：示例给出 `TSUS? "spefc",(ARMPort)` 与 `TSUS "spefc",3,(ARMPort)`，正文说明这是查询 multiport specification spefc 中 ARMPort 端口定义的 timing set 数。

**推断**：示例第二条用的是 `TSUS`（不带 `?`）形式，按语法更像设置而非查询，疑为文档笔误；实际查询应以 `TSUS?` 为准。

**文档事实**：查询全部 waveform set 时可对 `waveform_set` 用 `ALL`；查询单个 waveform set 用 `TSUS? {waveform_set}`，返回 `TSUS {waveform_set},{timing_set}`。

**建议**：用 TSUS 缩小 timing set 数会删除高于指定编号的 set，且总数受 512 上限与 DSCP/CONF 约束，执行前核对；需要保留 TFO 优化出的 timing set 时注意 `TSUS?` 与 `TSUX?` 的差异。

## 和谁有关

- `WSUS`：**文档事实**——`waveform_set` 取值范围由 WSUS 决定；TSUS 参数表链接 WSUS，Errors 写明 `waveform_set` 大于 WSUS 允许范围会报错。
- `DSCP`：**文档事实**——`timing_set` 上界由 DSCP 决定；DSCP 定义所有 waveform set 的 timing set 数；Errors 写明 `timing_set` 超过 DSCP 范围会报错。
- `CONF`：**文档事实**——允许的最大 timing set 数由 CONF 设置。
- `TSUX`：**文档事实**——TSUX 页说明 TFO 优化会生成额外 timing set，`TSUS?` 返回含优化 set 的全部数，`TSUX?` 返回原始数；在特定参数下 TSUS 与 TSUX 的值可互换。
- `Data organization of fixed timing`：**文档事实**——TSUS 正文链接本页说明不同 waveform set 可有不同数量的 timing set。
- 以 TSUS 作为 timing set 上限的命令（`DPRT`、`SPRM`、`PCLK`、`SWNG`、`VCLK`、`VTIM`、`ETDS`、`ETIM`、`FTST`、`TTMD` 等）：**文档事实**——这些页的参数表或 Errors 段写明 timing set 上限/范围由 TSUS 决定（取自 `objpack.py` 入边索引）。
- `List of commands`：**文档事实**——命令总表收录本页。

## 版本

**文档事实**：Functional changes 仅记 "Introduced before SmarTest 6.3.2"；这是哨兵值，表示在本套文档覆盖起点之前已存在，并非 6.3.2 的变更。

## 出处

- `02_System_reference/02.06_Command_Reference/02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.htm`——正文、参数、Errors、Example、Application 与 Functional changes 均取自本篇（已用 `show.py 02.06.02.02.283` 读取）。
- `和谁有关` 的入边关系取自 `extract/objpack.py` 的 `edges_in` 索引。
