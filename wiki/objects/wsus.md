---
type: object
title: WSUS, WSUS? - (Waveform Sets USed)
layer: L1
stage: timing
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# WSUS, WSUS? - (Waveform Sets USed)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **644 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### WSUS

```
WSUS {waveform_set}
```

### WSUS?

```
WSUS?
```

returns:

```
WSUS {waveform_set}
```

### Parameters

[表]
行 1:
  waveform_set
  Waveform set number. This is the highest number currently allocated to a waveform
    set or the highest number of a set you want to load. The number you enter must not exceed
    the maximum number of waveform sets allowed (defined by the `DSCP`（raw: `98578.htm`） command).
    
    This number is automatically updated to include any new waveform set as it is created. At
    power-on, only one waveform set (containing one timing set and default values) is
    available.

### Example

```
WSUS 3
```

This example sets the number of used waveform sets to
3.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.htm>` 的 `## Errors` 段。**不是转述。**
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

waveform_set
 is greater than the range allowed by the

DSCP
 command.

waveform_set
 is smaller than one.

<!-- 报错节 end -->

## 是什么

**文档事实**：WSUS（Waveform Sets USed）把已定义的 waveform set 数量设为给定值；新值必须是 1 到 DSCP 允许的最大 waveform set 数之间的整数（默认 16、最大 16）。可用 WSUS 删除 set：若准备载入硬件的 timing setup 文件含有多于所需的 waveform set，WSUS 会删掉所有大于指定编号的 set。WSUS? 查询当前已定义的 waveform set 数。

**文档事实**：参数 `waveform_set` 是当前已分配的最高编号，或想载入的 set 的最高编号；新 waveform set 创建时该数会自动更新。上电时只有一个 waveform set（含一个 timing set 与默认值）可用。

**文档事实**：Application 归属 Timing setup。

## 典型用法

**文档事实**：`WSUS 3` 把已用 waveform set 数设为 3（示例）。

**文档事实**：`WSUS?` 返回 `WSUS {waveform_set}`，给出当前定义的 waveform set 数。

**建议**：载入比实际需要更大的 timing setup 后，可用 WSUS 指定较小编号来删掉多余 set；删除不可恢复，执行前先确认编号。

## 和谁有关

- `DSCP`：**文档事实**——正文与 Errors 均以 DSCP 定义的最大 waveform set 数为上界（默认 16、最大 16）；`waveform_set` 超过 DSCP 允许范围、或小于 1 都会报错。
- `TSUS`：**文档事实**——TSUS 的 `waveform_set` 取值范围由 WSUS 决定，参数表直接链接 WSUS；TSUS 的 Errors 写明 `waveform_set` 大于 WSUS 允许范围会报错。
- 以 WSUS 作为 waveform set 上限的命令（`PRMD`、`LBMD`、`TORC`、`TORS`、`TORR`、`APTS`、`ASWE`、`BWDF`、`BWDS`、`CLKR`、`DCDT`、`DCUD`、`ETDS`、`ETIM`、`EUDS`、`FTST` 等）：**文档事实**——这些页的参数表或 Errors 段写明 waveform set 上限由 WSUS 决定（取自 `objpack.py` 入边索引）。
- `List of commands`：**文档事实**——命令总表收录本页。

## 版本

**文档事实**：Functional changes 仅记 "Introduced before SmarTest 6.3.2"；这是哨兵值，表示在本套文档覆盖起点之前已存在，并非 6.3.2 的变更。

## 出处

- `02_System_reference/02.06_Command_Reference/02.06.02.02.342_WSUS__WSUS__-__Waveform_Sets_USed.htm`——正文、参数、Errors、Example、Functional changes 均取自本篇（已用 `show.py 02.06.02.02.342` 读取）。
- `和谁有关` 的入边关系取自 `extract/objpack.py` 的 `edges_in` 索引。
