---
type: object
title: UPTD, UPTD? - (UP To Date)
layer: L1
stage: level
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.26_UPTD__UPTD__-__UP_To_Date.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# UPTD, UPTD? - (UP To Date)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **6,601 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.05.02.26_UPTD__UPTD__-__UP_To_Date.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### UPTD

```
UPTD {status}, {flag}
```

### UPTD?

```
UPTD? {status}
```

returns:

```
UPTD {status}, {flag}
```

### Parameters



### status

This parameter sets or returns the current status of the
hardware.

[表] Options for the status parameter
列: Option | Description
行 1:
  ALL
  The status of all options is returned. Use of the PATR (`PADS`（raw: `98679.htm`）for 14 edge setups), `DFPN (DeFine Pin Name)`（raw: `98550.htm`）, or `CONF (CONFiguration)`（raw: `98510.htm`） commands sets the flag
    to 0 until the setup is saved or loaded.
行 2:
  ANA
  The status of the analog control data is returned. When analog control data has
    changed the flag is set to 0 until the changed data is saved or loaded.
行 3:
  APPL
  The status of the production test application data file is returned. When
    application data is changed, the flag is set to 0 until the changed data is saved or
    loaded.
行 4:
  ATR
  The status of the edge attributes setup is returned. Use of the commands `PCLK (Pin CLocK)`（raw: `98682.htm`）, `DFPN (DeFine Pin Name)`（raw: `98550.htm`）, or `CONF (CONFiguration)`（raw: `98510.htm`） sets the flag to 0 until
    the setup is saved or loaded.
行 5:
  CAL
  The status of the calibration data is returned. When the calibration data is
    changed, the flag is set to 0 until the changed data is saved or loaded.
行 6:
  CNFG
  The status of the production test configuration is returned. When the data is
    changed, the flag is set to 0 until the changed data is saved or loaded.
行 7:
  CONF
  The status of the pin configuration setup is returned. Use of any of the `Pin configuration setup commands`（raw: `10649.htm`） sets the flag to 0 until the setup is saved or loaded.
行 8:
  DFRM
  The status of the Data Bridge Command Set is returned. When the Command Set name is
    changed, the flag is set to 0. When the Command Set process is successfully loaded and
    running, the flag is set to 1.
行 9:
  DPS
  The status of the power supply setup is returned. Use of `equation based level setup`（raw: `56938.htm`）, the `PSLV`（raw: `98702.htm`）`(Power Supply LeVel)`（raw: `98702.htm`） command, or any of the `Pin configuration setup commands`（raw: `10649.htm`）
    sets both the DPS and LEV flags to 0 until the setup is saved or loaded (see Note
    below).
行 10:
  DSET
  The status of the data set is returned. When the data set is changed, the flag is
    set to 0 until the changed data is saved or loaded.
行 11:
  EDA
  The status of the CAE link files is returned. When the CAE link data is changed,
    the flag is set to 0 until the changed data is saved or loaded.
行 12:
  ERMP
  The status of the Error Map files is returned. When the Error Map data is changed,
    the flag is set to 0 until the changed data is saved or loaded.
行 13:
  FLOW
  The status of the production testflow file is returned. When testflow data is
    changed, the flag is set to 0 until the changed data is saved or loaded.
行 14:
  LEV
  The status of the level setup is returned. Use of `equation based level setup`（raw: `56938.htm`）, any of the `Pin configuration setup commands`（raw: `10649.htm`）, or any of the `Level Setup Commands`（raw: `10637.htm`） sets both the DPS and LEV flags to 0 until the setup is saved or loaded
    (see Note below).
行 15:
  PDL
  The status of the path delay data is returned. Use of the commands `SATR (System ATtRibutes)`（raw: `98727.htm`）, or `FXDL (FiXture DeLay)`（raw: `98609.htm`）, as well as `DFPN (DeFine Pin Name)`（raw: `98550.htm`） or `CONF (CONFiguration)`（raw: `98510.htm`） sets the flag to 0 until the changed data is
    saved or loaded.
行 16:
  PRBH
  The status of the Prober/Handler Command Set is returned. When the Command Set name
    is changed, the flag is set to 0. When the Command Set process is successfully loaded and
    running, the flag is set to 1.
行 17:
  PRCS
  The status of the Execution Input Command Set is returned. When the Command Set
    name is changed, the flag is set to 0. When the Command Set process is successfully loaded
    and running, the flag is set to 1.
行 18:
  PROG
  The status of the production test program file is returned. When production test
    data is changed, the flag is set to 0 until the changed data is saved or loaded.
行 19:
  REP
  The status of the report window data is returned. When the data in the report
    window changes, the flag is set to 0 until the changed data is saved or loaded.
行 20:
  ROUT
  The status of the routing setup is returned. When routing definition data has
    changed the flag is set to 0 until the changed data is saved or loaded.
行 21:
  SLST
  The status of the state list files is returned. When the state list data is
    changed, the flag is set to 0 until the changed data is saved or loaded.
行 22:
  TIM
  The status of the timing setup is returned. Use of the commands `CONF (CONFiguration)`（raw: `98510.htm`）, `DFPN (DeFine Pin Name)`（raw: `98550.htm`）, or any of the `Timing Setup Commands`（raw: `10585.htm`） set the flag to 0 until the setup is
    saved or loaded.
行 23:
  TMDG
  The status of the timing diagram files is returned. When the timing diagram is
    changed, the flag is set to 0 until the changed data is saved or loaded.
行 24:
  USRP
  The status of the User Procedure Command Set is returned. When the Command Set name
    is changed, the flag is set to 0. When the Command Set process is successfully loaded and
    running, the flag is set to 1.
行 25:
  VEC
  The status of the vector and sequencer setup is returned. Use of the commands `DFPN (DeFine Pin Name)`（raw: `98550.htm`）, `CONF (CONFiguration)`（raw: `98510.htm`）, or any of the `Vector Setup Commands`（raw: `10523.htm`） set the flag to 0 until the
    setup is saved or loaded.
行 26:
  WAFR
  The status of the wafer description file is returned. When description data is
    changed, the flag is set to 0 until the changed data is saved or loaded.
行 27:
  WAVE
  The status of the waveform definition data is returned. When waveform definition
    data has changed the flag is set to 0 until the changed data is saved or loaded.

Note
 The status of the DPS and LEV parameters is kept synchronized when
modified via the pin configuration tool or by
`equation based level setup`（raw: `56938.htm`）
. Only the commands
`PSLV`（raw: `98702.htm`）
`(Power Supply LeVel)`（raw: `98702.htm`）
,
`DRLV (DRive LeVel)`（raw: `98577.htm`）
, or
`RCLV, RCLV? - (ReCeive LeVel)`（raw: `98717.htm`）

allow to unsychronize their status.

### flag

Sets or returns the up-to-date status:

1: The specified device file is identical to the data currently used in hardware.

0: The specified device file differs from the data currently used in hardware.

### Example

```
UPTD? CONF
```

This example requests if the pin configuration data
has been changed since the file was last loaded or saved. If the data has not changed, the
response is:

```
UPTD CONF,1
```

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.05.02.26_UPTD__UPTD__-__UP_To_Date.htm>` 的 `## Errors` 段。**不是转述。**
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if you specify a flag other than 0 or
1.

<!-- 报错节 end -->

## 是什么

**文档事实** UPTD（UP To Date）命令用于把一个给定的 setup、result 或 command set 声明为 up to date 或 out of date；`UPTD?` 查询用于读取“自当前 device file 最近一次保存或加载以来，硬件中的数据是否被改动过”，返回 1 或 0。

**文档事实** 在 power-on 之后，或执行 `*RST`（ReSeT）或 `[[dscp]]`（DSCP）之后，所有 flag 都置为 0。

**文档事实** `status` 指定要设置或查询哪类数据的状态；文档的 status 选项表列出 27 项：`ALL`、`ANA`、`APPL`、`ATR`、`CAL`、`CNFG`、`CONF`、`DFRM`、`DPS`、`DSET`、`EDA`、`ERMP`、`FLOW`、`LEV`、`PDL`、`PRBH`、`PRCS`、`PROG`、`REP`、`ROUT`、`SLST`、`TIM`、`TMDG`、`USRP`、`VEC`、`WAFR`、`WAVE`；`ALL` 返回所有选项的状态。

**文档事实** `flag` 的语义：1 表示指定的 device file 与硬件当前使用的数据一致；0 表示二者不一致。

**文档事实** 对多数 setup 类状态，相关数据一经改动 flag 即置 0，直到改动被保存或加载；对 command set 类状态（`DFRM`、`PRBH`、`PRCS`、`USRP`），command set 名称改变时 flag 置 0，command set 进程成功加载并运行时置 1。

**文档事实** `DPS` 与 `LEV` 的状态在通过 pin configuration tool 或 equation based level setup 修改时保持同步；只有 `[[pslv]]`、`[[drlv]]`、`[[rclv]]` 允许二者状态不同步。

**推断** 因此 UPTD 读写的是“硬件中数据相对已存 device file 的脏标记”，不是文件内容比较；文档没有说明 UPTD 自身会触发保存或加载。

## 典型用法

**文档事实** 查询用 `UPTD? {status}`；文档示例 `UPTD? CONF` 询问 pin configuration 数据自上次加载或保存后是否改变，若未改变则响应 `UPTD CONF,1`。

**文档事实** 设置用 `UPTD {status}, {flag}`；示例中的 `UPTD CONF,1` 是上述查询的响应，文档未给出设置形式的输入示例。

**文档事实** `flag` 只允许 0 或 1，指定其他值会报错（见报错节）。

**文档事实** 要读取所有选项的状态，可将 status 设为 `ALL`（status 表 `ALL` 条目）。

**文档事实** Application 段只给出 Test Program Explorer（`01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02_Test_Program_Explorer.htm`）作为应用环境。

**建议** 在切换 setup 或执行保存/加载前后，先用 `UPTD? <status>` 确认目标数据为 1（无未保存改动）；检查 `DPS`/`LEV` 时注意二者可能因 `PSLV`、`DRLV`、`RCLV` 而状态不同步。

## 和谁有关

- **文档事实** `*RST`（`02_System_reference/02.06_Command_Reference/02.06.02.02.345_RST_-__ReSeT.htm`）与 `[[dscp]]`（DSCP）— 文档开头说明 power-on 或执行这两个命令后所有 flag 置 0。
- **文档事实** `[[dfpn]]`、`[[conf]]`、`[[pclk]]` — 这些命令的使用会把相应选项的 flag 置 0：`CONF`、`DFPN` 出现在 `ALL`、`ATR`、`PDL`、`TIM`、`VEC` 条目，`PCLK` 出现在 `ATR` 条目。
- **文档事实** `[[pslv]]`、`[[drlv]]`、`[[rclv]]` — 文档 Note 说明只有这三个命令允许 DPS 与 LEV 的状态不同步。
- **文档事实** PATR/PADS、SATR、FXDL — 文档在 `ALL`、`PDL` 条目中说明使用它们会把 flag 置 0；这些对象在本 wiki 无独立页。
- **文档事实** Pin configuration setup commands、Level Setup Commands、Timing Setup Commands、Vector Setup Commands、equation based level setup — 文档在 `CONF`、`LEV`、`TIM`、`VEC`、`DPS` 等条目中把它们列为会置 flag 0 的命令族/机制；主源也把 `DPS` 与 `LEV` 的同步关系归因于 equation based level setup。
- **文档事实** `[[test-program-explorer]]` — 主源 Application 段指向 Test Program Explorer。
- **文档事实** List of level setup commands（`02_System_reference/02.06_Command_Reference/02.06.05.02_List_of_level_setup_commands.htm`）— 入边显示 UPTD 被列在该页，说明它属于 level setup commands 家族。

## 版本

**文档事实** Functional changes 记：

- Introduced before SmarTest 6.3.2
- SmarTest 7.0.3：BIT 与 FAM 不再支持（"BIT and FAM are no longer supported"）
- SmarTest 7.0.3：由于 standard test functions 被废弃，TSTF 不再支持
- SmarTest 7.2.0：移除 `SHMO` 参数

## 出处

- `02_System_reference/02.06_Command_Reference/02.06.05.02.26_UPTD__UPTD__-__UP_To_Date.htm`，主源，含概览、UPTD/UPTD? 语法、status 表与 Note、flag、Application、Errors、Example 与 Functional changes，已用 `show.py 02.06.05.02.26` 读取。
- List of level setup commands 关系取自 `extract/objpack.py` / `edges.jsonl` 的入边，该页未单独读取。

