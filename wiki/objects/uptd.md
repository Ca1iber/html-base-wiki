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

（待补）

## 典型用法

（待补）

## 和谁有关

（待补）

## 版本

（待补）

## 出处

（待补）
