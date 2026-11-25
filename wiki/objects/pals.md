---
type: object
title: PALS, PALS? - (Pin ALlocation for multiple Sites)
layer: L1
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.173_PALS__PALS__-__Pin_ALlocation_for_multiple_Sites.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# PALS, PALS? - (Pin ALlocation for multiple Sites)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **3,137 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.173_PALS__PALS__-__Pin_ALlocation_for_multiple_Sites.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### PALS

```
PALS {site}, {channel_1|(DC_scale_channels_list)}, [channel_2], {(pin)}
```

### PALS?

```
PALS? {site}, {(pinlist)}
```

returns:

```
PALS {site}, {channel_1|(DC_scale_channels_list)}, [channel_2], {(pin)}
```

### Parameters

[表]
行 1:
  site
  The site parameter is an integer that defines the number of the site
    where the channels are to be defined.
    
    The integer must be greater than 1 (channels for site 1 are
    defined by the command `DFPN`（raw: `98550.htm`）.
    
    When specified as part of the PALS? query, you
    can use the parameter ALL to read the channel
    allocation for all sites or the parameter
    PEND to read the pending channel
    allocation.
行 2:
  channel_1
  This parameter specifies the test system channel used in the specified site for the
    pin.
    
    For a digital or DC Scale channel, specify it with the test system channel number, which
    is five digits.
    
    See `DFPN, DFPN? - (DeFine Pin Name)`（raw: `98550.htm`） for the channel number.
    
    For utility lines, see `DFUT, DFUT? - (DeFine UTility line)`（raw: `98560.htm`） for the channel
    number.
行 3:
  DC_scale_channels_list
  You can define a Master/Slave configuration for DC Scale channels by specifying a list of
    DC Scale channels, separated by commas and enclosed by
    parentheses. The first channel is the master.
    
    For UHC4 / UHC4T the channels must be physically adjacent on the
    same board, or be the last (the 4th) channel of a board and the
    first of another UHC4 / UHC4T board. You cannot gang UHC4 and
    UHC4T boards. Before ganging between boards can be used, the
    connection must be enabled by `DDIC`（raw: `106906.htm`）.
行 4:
  channel_2
  The optional parameter is currently not used.
行 5:
  pin
  This defines the name of the pin.
行 6:
  pinlist
  The names of the pins to be allocated to the pin.
    
    The query returns the name of the pin allocated to each channel.
    The symbol @ can be used with the
    PALS? command to list all pins previously
    defined by the PALS command. If a list of
    more than one pin is required, the pin names must be separated
    with a comma. If you query a non-existent
    pinlist, the system returns nothing.

### Examples

```
PALS 2,10201,,(Clock)
PALS 2,10202,,(D0)
```

The above example allocates the Clock pin for site 2 to channel 10201 and allocates
pin D0 for site 2 to channel 10202.

```
PALS 2,(10101, 10102),,(dc1)
```

This example defines a master/slave configuration for DC Scale channels. The first
channel is the master.

```
DDIC CONN, (104GO, 105GI)
DDIC CONN, (105GO, 107GI)
PALS 2,(10403, 10404, 10501, 10502, 10503, 10504, 10701, 10702),,(dc1)
```

This example defines a master/slave configuration for DC Scale UHC4 channels across
boards. The first channel is the master.

```
DFAN "MCE231,2,i","",(av8_bbrx_b+)
DFAN "MCE231,6,i","",(av8_bbrx_b-)
PALS 2,"MCE231,1,i",,(av8_bbrx_b+)
PALS 3,"MCE231,3,i",,(av8_bbrx_b+)
PALS 4,"MCE231,4,i",,(av8_bbrx_b+)
PALS 2,"MCE231,5,i",,(av8_bbrx_b-)
PALS 3,"MCE231,7,i",,(av8_bbrx_b-)
PALS 4,"MCE231,8,i",,(av8_bbrx_b-)
```

This example defines a pair of differential pins av8_bbrx_b+ and av8_bbrx_b- using the MCE
card in 4 sites.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.173_PALS__PALS__-__Pin_ALlocation_for_multiple_Sites.htm>` 的 `## Errors` 段。**不是转述。**
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

The specified channel number is not valid;

The specified channel is not installed;

The specified pin name is already used as a group name;

The sequencer is in RUN or BREAK mode.

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
