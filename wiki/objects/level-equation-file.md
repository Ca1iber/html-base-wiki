---
type: object
title: Level equation file
layer: file
stage: level
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.11.01.05.01_Level_equation_file.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Level equation file

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **947 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.11.01.05.01_Level_equation_file.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

USE_PROTOCOL

"<
protocolName
:<
levelSegmentName
>"
[<
portList
>]

[表] Parameter
列: Parameter | Description/Range
行 1:
  protocolName
  The name of the protocol to use.
行 2:
  levelSegmentName
  Name of the level segment to be used.
    
    Must be defined for the protocol specified by protocolName.
行 3:
  portList
  (optional) List of protocol ports.
    
    If omitted, all ports assigned to the protocol specified by
    protocolName. will be used.

### Example

The following except shows how to use the
USE_PROTOCOL
 statement
within a device level setup
file.

```
hp93000,level,0.1
...
EQSP LEV,EQN,#9000005436
EQNSET 1 "levels equation set"

SPECS # starts the declaration of the specs
v_il_ctl [V]
...
EQUATIONS
# put here depend specs, resources in [V] and [mA]
...

LEVELSET 1 "normal"
#USE_PROTOCOL "<protocolName>:<levelSegmentName>" <portList>
USE_PROTOCOL "MDIO:DefaultPowerLevels" PoMDIO

PINS std_ins reset_b wse_gen
vil= v_il_ctl

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
