---
type: object
title: EQSP, EQSP? - (EQuation SPecification transfer)
layer: L1
stage: timing
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.10_EQSP__EQSP__-__EQuation_SPecification_transfer.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# EQSP, EQSP? - (EQuation SPecification transfer)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,489 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.05.02.10_EQSP__EQSP__-__EQuation_SPecification_transfer.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### EQSP

```
EQSP {spec_type}, {part}, {#spec(data)}
```

### EQSP?

```
EQSP?{spec_type}, {part}
```

returns:

```
EQSP {spec_type}, {part}, {#spec(data)}
```

if
these are not empty, for backward compatibility.

[表] Parameters
行 1:
  spec_type
  The mandatory parameter defines which specification type to use.
    
    Use:
    
    LEV to specify levels
    
    TIM to specify timing
行 2:
  part
  The mandatory parameter defines which part of the specification type to use.
    
    Use:
    
    EQN to specify equations
    
    SPS to specify specs
    
    WVT to specify a wavetable
    
    part can only be set to WVT,
    EQN, or CLK if spec_type is set
    to TIM.
行 3:
  #spec(data)
  An equation based set of data (for example wavetables) in binary format.
    
    This parameter enables you to define the length of the data (in bytes) and the data
    itself to be transferred. It has the following format:
    
    A # to mark the start of the data block.
    
    One digit indicating how many digits make up the data length specifier.
    
    A number of digits indicating the length (in bytes) of the data to follow.
    
    A number of characters which make up the specified equation based testing file. This
    stream of characters must be terminated with a @ character.

### Example

The following example queries the current
wavetables:

```
> EQSP? TIM,WVT
< EQSP TIM,WVT,#9000000127WAVETBL table1 # derived from waveform set 1

PINS Pin1 Pin2
WFDS 0 "d1:D11"
1 0 . . .
2 1 . . .
BWDS ""

@
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
