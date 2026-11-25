---
type: object
title: Wavetable file
layer: file
stage: timing
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.11.01.05.03_Wavetable_file.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Wavetable file

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,086 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.11.01.05.03_Wavetable_file.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

USE_PROTOCOL

"<
protocolName
>"
[<
portList
>]
 for
wavetables

[表] Parameter
列: Parameter | Description/Range
行 1:
  protocolName
  The name of the protocol to use.
行 2:
  portList
  (optional) List of protocol ports.
    
    If omitted, all ports assigned to the protocol specified by
    protocolName. will be used..

### Example

The following except shows how to use the
USE_PROTOCOL
 statement
within a device timing setup
file.

```
hp93000,timing,0.1
...

EQSP TIM,WVT,#9000015411

WAVETBL "wavetable 1"
DEFINES parallel

PINS xmit std_ins wse_gen reset_b
0 "d1:!Z d2:F0N" 0
...

# Note, that only one wavetable is supported per protocol. Therefore no segment is given
WAVETBL "wavetable 1"
DEFINES mdio_port

#USE_PROTOCOL "<protocolName>" <protocolPort>
USE_PROTOCOL "MyMDIO" PoMDIO

EQSP TIM,CLK,#9000000278
...

EQSP TIM,EQN,#9000011543
EQNSET 1 "equation set 1"
DEFINES mdio_port

SPECS
TSetup [ns]
...
TIMINGSET 1 "eq 1 ts 1"
period=TPer

#USE_PROTOCOL "<protocolName>:<timingSegmentName>" <protocolPort>
USE_PROTOCOL "MyMDIO:DefaultTiming" PoMDIO
...

EQSP TIM,SPS,#9000006739
...
```

<!-- 语法节 end -->

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
