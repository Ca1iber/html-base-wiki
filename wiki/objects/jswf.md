---
type: object
title: JSWF? - (Jitter Set WaveForm)
layer: L1
stage: timing
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.16.02.06_JSWF__-__Jitter_Set_WaveForm.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# JSWF? - (Jitter Set WaveForm)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,802 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.16.02.06_JSWF__-__Jitter_Set_WaveForm.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
JSWF? {"jitter_set_name"}, {clock_resolution}, {(pinlist)}
```

returns:

```
JSWF {"jitter_set_name"}, {"offset_sequence"}, {(pinlist)}
```

### Parameters

[表]
行 1:
  jitter_set_name
  Specifies the name of a jitter set that must have been defined with
    JSDF.
行 2:
  clock_resolution
  Specifies the clock resolution on which the calculation will be based. The admitted
    range is between 880 and 1750 ps.
    
    You can retrieve the clock resolution for a specification with the CLKR?
    EXACT query.
    
    Note that the unit is pico seconds, not nano seconds.
行 3:
  offset_sequence
  The list of the calculated offsets that is returned.
行 4:
  pinlist
  Specifies the pins for which the offset sequence is calculated.

### Examples

### Example 1
```
> jscf? "test",,(IO0)
< JSCF "test",WAVEFORM,SINUS,(IO0)
< JSCF "test",PERIOD,20,(IO0)
< JSCF "test",AMPLITUDE,100,(IO0)
> CLKR? EXACT,101,(@)
< CLKR 101,2.4,1.2,(@)
> jswf? "test",1200,(IO0)
< JSWF "test","0,29,47,47,29,0,-30,-48,-48,-30,-1,29,47,47,29,0,
. . .
-1,-30,-48,-48,-30,0,29,47,47,29,0,-30,-48,-48,-30",(IO0)
```

This
example first queries the jitter waveform for pin
IO0
, and also the clock
resolution for timing specification 101. It then calculates the offset sequence for this
waveform and clock resolution. Note that
CLKR?
 returns the clock resolution
as nano seconds, but that
JSWF?
 expects it to be specified as pico seconds.
The reply is displayed in abbreviated form. The total length of the sequence is about 500 items.

### Example 2
```
> JSCF? "test",WAVEFORM,(IO1)
< JSCF "test",WAVEFORM,"150,110,80,70,0"
> JSWF? "test",880,(IO1)
< JSWF "test","150,120,90,70,40",(IO1)
```

This
example shows how
JSWF?
 corrects the offset list if the second of two
consecutive items is smaller than the first, and the maximum difference is exceeded.

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
