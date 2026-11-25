---
type: object
title: DFPS, DFPS? - (DeFine Power Supply)
layer: L1
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.65_DFPS__DFPS__-__DeFine_Power_Supply.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# DFPS, DFPS? - (DeFine Power Supply)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **3,847 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.65_DFPS__DFPS__-__DeFine_Power_Supply.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### DFPS

```
DFPS {dps_channel|(DC_scale_channel_list)}, {polarity}, {(pin)}
```

### DFPS?

```
DFPS? {(pinlist)}
```

returns:

```
DFPS {dps_channel|(DC_scale_channel_list)}, {polarity}, {(pin)}
```

### Parameters

[表]
行 1:
  dps_channel
  The test system channel number of the DPS channel to be configured. [跨 2 列]
    
    The channel is to be defined as follows:
    
    For `external device power supplies`（raw: `130769.htm`）, this is a
    three‑digit or four‑digit integer.
    The first
    one or two digits define an external supply. To avoid a
    conflict with the internal supplies, we recommend using
    values above 8. The maximum supported value is
    16.
    
    The last two digits define the channel number
    of the DPS. If the channel number is less than 10, a
    leading "0" must be used.
    
    For DC Scale channels (in DPS mode) this is a five digit
    number in the same format as for digital I/O
    channels.
行 2:
  DC_scale_channel_list
  To gang DC Scale channels, you must specify a consecutive number of channels enclosed by [跨 2 列]
    parentheses, either as comma separated list or as range, for
    example 10105-10106.
    
    DPS128/64: Ganging is possible for any number of successive channels
    within a card, but not across cards.
    DPS128/DPS64 channels
    must be of the same type (HC or HV).
    
    The maximum
    number of ganging groups per DPS128/64
    is half the number of channels. The maximum current per
    card cannot be exceeded.
    
    XPS256: Only channels on the same HLA can be ganged.
    
    UHC4, UHC4T: For UHC4 or UHC4T ganging is possible for any number of successive
    channels within a card and any number of cards within a test
    head. The combination of UHC4 and UHC4T within the same
    ganging group is not supported. The maximum current per card
    cannot be exceeded.
    
    Before cross-card ganging can be used, the connection must be enabled by command
    `DDIC`（raw: `106906.htm`）.
行 3:
  polarity [跨 3 行]
  Gives the polarity of the DPS which has to be applied [跨 2 列]
    to the selected channel.
行 4:
  POS
  Enter POS only if the DPS connections on the DUT board are as follows: The
    force is connected to power; the sink is connected to ground. The voltage supplied to the
    device will then be exactly as entered in the Level Setup, but the entry made there must be
    positive, otherwise the system returns an error.
    
    For DC scale channels, only POS is allowed.
行 5:
  NEG
  NEG is not allowed for DC Scale channels.
行 6:
  pin
  Defines the pin name for the DPS channel. [跨 2 列]
行 7:
  pinlist
  The pin name or names of those power supply outputs which have already been defined. If more than [跨 2 列]
    one pin is required, the names must be separated with a comma.
    The @ character can be used to read all configured power
    supply pins.

### Examples

### Example 1
```
DFPS 11,POS,(Vee)
```

This example connects
device pin Vee to channel 1 of DPS board 1. The DPS output polarity is positive.

### Example 2
[表]
行 1:
  ```
    DFPS (10101, 10102),POS,(vee)
    ```
行 2:
  ```
    DFPS (10101-10102),POS,(vee)
    ```

Both lines define the same master/slave configuration for DC Scale channels in DPS
mode. They just use different notations. Note the five digit channel numbers.

### Example 3
```
DDIC CONN, (104GO, 105GI)
DFPS (10403, 10404, 10501, 10502),POS,(vee)
```

This
example defines a master/slave configuration for DC Scale UHC4 channels in DPS mode across two
boards.

### Example 4
```
DDIC CONN, (104GO, 105GI, 105GO, 106GI)
DFPS (10403, 10404, 10502, 10503, 10504, 10601),POS,(vee)
```

This
example defines a master/slave configuration for DC Scale UHC4 channels in DPS mode across three
boards.

### Example 5
```
DDIC CONN,(230GO, 227GI)
DFPS (23004, 22701),POS,(VDDCI)
```

This
example specifies the ganging of channels across two DC Scale UHC4 cards.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.65_DFPS__DFPS__-__DeFine_Power_Supply.htm>` 的 `## Errors` 段。**不是转述。**
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

 You define more than the number of installed DPS pins.

 The requested DPS channel has already been allocated.

 The requested DPS channel is not installed.

 The addressed DPS is not installed.

 The requested DPS channel number is not valid.

 The requested DPS pin has already been defined.

 You try to assign DPS channels in the connected state.

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
