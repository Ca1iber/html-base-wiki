---
type: object
title: DFPN, DFPN? - (DeFine Pin Name)
layer: L1
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.63_DFPN__DFPN__-__DeFine_Pin_Name.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# DFPN, DFPN? - (DeFine Pin Name)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **4,899 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.63_DFPN__DFPN__-__DeFine_Pin_Name.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### DFPN

```
DFPN ["connectionSet",] {channelNo_1|(list_of_DC_scale_channels)}, ["pinNo"], {(pinName)}
```

### DFPN?

```
DFPN? {(pinlist)}
```

returns:

```
DFPN {channelNo_1|(list_of_DC_scale_channels)}, ["pinNo"], {(pinName)}
```

### Parameters

[表]
行 1:
  connectionSet
  This parameter is currently not used.
    
    This extra string parameter adds the ability to define several
    pins containing the same DC Scale channel in PMU mode. A
    multiple defined DC Scale channel can be sequentially reused as
    single pin or in ganging groups. Note: The documentation for
    supported DC Scale cards knows this feature also as "Ganging on the fly".
    
    Default connection set: The default connection set is defined if
    this extra parameter is not used or if an empty string is
    programmed. A DC Scale pin can be defined in only one default
    connection set.
    
    All traces that are needed for a cross-card ganging group and are
    defined by the `DDIC`（raw: `106906.htm`） command and the
    DFPN command must have the same
    connectionSet defined. Recommendation: If
    the DUT trace can be activated by utility lines, name it like
    the utility line (see DFUP command).
    
    There can be several pin definitions containing the same
    channel:
    
    Adding a different ganging combination (new pin), does not
    invalidate the setups for the existing pins.
    
    The different pins containing the same channel must be part of
    the same ports.
    
    The patterns, events and DC-setups of these pins do not
    overlap.
行 2:
  channelNo_1
  The test system channel number of the channel to which the specified device pin is
    connected (five digits), or the utility block number
    of the specified card cage (three digit).
    
    Digital or DC Scale channel
    
    For a digital channel this is a five digit number. The first three digits
    specify the pogo block number, and the fourth and fifth digits specify the pin number in
    the pogo block. The first digit is 1 to 4, the second and third digits is 01 to 32, and the
    final two digits is 01 to 16. For example, 10105 is the digital channel whose pogo pin
    number is 05 in the pogo block 101.
    
    Each pogo block contains 16 digital channels. The pogo block numbers are determined by the slots in which the channel
    boards are installed.
    
    The first three digits are also called the board number of the
    logical channel board, and the last two digits are a channel number in the logical channel
    board, where each logical channel board contains 16 channels
    
    Utility DC channel
    
    For the utility DC pins, this is a three digit number, specifying the
    utility block of the card cage. The referenced utility pogo must be one which can be
    connected to the DC rail of the card-cage. To get the utility block number, add 164 (264
    for the second utility line card on EXA Scale test systems) to the desired utility line
    block, such that for example utility block 4 has number 168. For compatibility with
    SmarTest 7.6x, "HPMU1" now maps to "UTIDC165" and so on (for Smart Scale test systems
    only).
    
    For more information, see subtopics in `Pogo pin assignment - Utility pogo blocks`（raw: `146933.htm`）.
    
    The hardware knows 4 Utility DC channels (pogo pins): DC-force, DC-sense,
    ground-sense, and guard. But because they are referenced as a group, one pin name is
    sufficient to reflect all 4 channels.
行 3:
  DC_channel_list
  You can define ganging for a set of DC Scale channels in PMU
    mode by specifying a list of DC Scale channels, separated by
    commas and enclosed by parentheses. The channels must be
    physically adjacent on the same board.
    
    Before cross-card ganging can be used, the connection must be
    enabled by command `DDIC`（raw: `106906.htm`）.
行 4:
  pinNo
  This is the device pin number which is allocated to the specified channel. The number must be
    enclosed in double quotes.
行 5:
  pinName
  The name to be allocated to the pin. Maximum number of
    characters is 16 for 32-bit SmarTest and 64 for 64-bit
    SmarTest.
行 6:
  pinlist
  This query parameter specifies the pins whose definitions are
    to be retrieved. The symbol @ can be used
    with the DFPN? query to list all pins
    previously defined by the DFPN command. If a
    list of more than one pin is required, the pin names must be
    separated by a comma. If you query a non-existent pin, the
    system returns nothing.

### Example

### Example 1
```
> DFPN 10101,"1",(Clock)
> DFPN 10102,"2",(D0)
> DFPN? (@)
< DFPN 10101,"1",(Clock)
< DFPN 10102,"2",(CD0)
```

The above example allocates the
Clock
 pin to channel 10101 and allocates pin

D0
 to channel 10102, and then queries these definitions. The
device pin numbers allocated are 1 and 2 respectively.

```
DFPN (11901, 11902),,(vee)
```

This example defines ganging
for DC Scale channels in PMU mode.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.63_DFPN__DFPN__-__DeFine_Pin_Name.htm>` 的 `## Errors` 段。**不是转述。**
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

The specified channel number is not valid.

The specified channel is not installed.

The specified channel has already been allocate.

The specified pin has already been defined.

The specified pin name is already used as a group name.

The sequencer is in RUN or BREAK state.

Ganging is defined for DC Scale channels, and not all specified channels
are
 DC Scale
channels.

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
