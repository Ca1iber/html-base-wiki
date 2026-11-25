---
type: object
title: CHIN? - (CHannel INformation)
layer: L1
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.22_CHIN__-__CHannel_INformation.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# CHIN? - (CHannel INformation)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **2,800 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.22_CHIN__-__CHannel_INformation.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
CHIN? {channel_nr|ALL}
```

returns:

CHIN
 {
channel_nr
}, {
channel_type
},
[
phys_location
], {
board_no
},
[
clk_board
], [
chan_info_1
],
[
chan_info_2
]

### Parameters

[表]
行 1:
  channel_nr
  The number that identifies the channel. [跨 2 列]
    
    Specify ALL if you want information about all channels.
    
    For a digital channel, specify it with the test system channel number, which is five
    digits (see `DFPN, DFPN? - (DeFine Pin Name) for the number)`（raw: `98550.htm`）.
    
    For a DPS channel, specify it with the test system channel number, which is two digits
    (see `DFPS, DFPS? - (DeFine Power Supply)`（raw: `98551.htm`） for the number).
行 2:
  channel_type [跨 10 行]
  Returns the type of the channel. It can [跨 2 列]
    be:
行 3:
  CPIO
  Pin Scale 1600 digital channel
行 4:
  PYIO
  Pin Scale 5000 digital channel
行 5:
  WZ_FDIFF_I
  Fast differential input channel
行 6:
  WZ_FDIFF_O
  Fast differential output channel
行 7:
  PPS
  Precision Parallel Source channel
行 8:
  HVP
  High Voltage PMU
行 9:
  DPS128HC
  DC Scale DPS128-HC or DPS64-HC
行 10:
  XPS256
  DC Scale XPS256
行 11:
  UHC4T
  DC Scale UHC4T
行 12:
  phys_location [跨 5 行]
  The channel's physical location. [跨 2 列]
    
    NOTE: For PS1600 and DPS128 SmarTest returns always "-1"!
    
    This format is TCSSPP.
    
    Where:
行 13:
  T
  test head (1)
行 14:
  C
  card cage (1 - 8)
行 15:
  SS
  slot (01 - 18) in the card cage
行 16:
  PP
  hardware pin number of the digital channel
    
    For DPS, this is the channel number in the DPS board.
行 17:
  board_no
  Board number of the board to which the channel belongs. For the DPS, this is the DPS board [跨 2 列]
    number. For details, see the board_no parameter in `*OPT? - (hardware OPTions)`（raw: `98881.htm`）.
行 18:
  clk_board
  Board number of the clock board in the card [跨 2 列]
    cage to which the channel belongs.
行 19:
  chan_info_1 [跨 4 行]
  First information of the channel. [跨 2 列]
行 20:
  For digital channels: [跨 2 列]
    
    Sequencer memory (SM) depth in blocks of 128k vectors (or 0.125M vectors).
    
    DC Scale DPS channels behave like a digital channel and return the sequencer memory
    depth.
行 21:
  For PPS channels: [跨 2 列]
    
    Pattern memory depth in blocks of 1k words (16 bit).
行 22:
  For HVP channels: [跨 2 列]
    
    DAC/ADC RAM depth in blocks of 1k words (16 bit).
行 23:
  chan_info_2 [跨 2 行]
  Second information of the channel. [跨 2 列]
行 24:
  For digital channels: [跨 2 列]
    
    Sequencer memory (SM) depth in blocks of 128k vectors (or 0.125M vectors).

### Examples

```
CHIN? 10901
```

returns:

```
CHIN 10901,PSIO,120601,109,21,512,0
```

```
CHIN? ALL
```

Return (for example):

```
CHIN 10101,PYIO,110301,101,11,3551,0
CHIN 10102,PYIO,110302,101,11,3551,0

CHIN 21701,DPS128HC,-1,217,31,191,0
CHIN 21702,DPS128HC,-1,217,31,191,0
```

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.22_CHIN__-__CHannel_INformation.htm>` 的 `## Errors` 段。**不是转述。**
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if a wrong value
is given for

channel_nr
.

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
