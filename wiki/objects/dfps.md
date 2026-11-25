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

**文档事实** DFPS 即 DeFine Power Supply，用于告诉软件哪个 DPS 通道连接到指定 device pin，以及该通道的 polarity。

**文档事实** DFPS? 查询返回现有的 channel、polarity 与已分配的 pin number。

**文档事实** DFPS 还可用于把一个或多个 DC Scale 通道配置为 DPS mode。

**文档事实** DC Scale 通道在 DPS mode 下的 ganged 配置通过 DFPS 定义，方法是在第一个参数中指定 channel list。

**文档事实** 多 site 配置由 PALS 与 PSTE 命令定义。

**文档事实** 文档 Application 段把该命令归入 Configuration Setup，参见 Configuration Setup Commands。

## 典型用法

**文档事实** 基本调用为 DFPS 11,POS,(Vee)，把 device pin Vee 连接到 DPS board 1 的 channel 1，并设置正极性。

**文档事实** DC Scale 通道 gang 可用逗号分隔列表 DFPS (10101, 10102),POS,(vee) 或范围 DFPS (10101-10102),POS,(vee)，两种写法等价，通道号为五位数。

**文档事实** 跨 board 的 DC Scale UHC4 ganging 需先用 DDIC CONN 启用连接，例如 DDIC CONN, (104GO, 105GI) 后再用 DFPS (10403, 10404, 10501, 10502),POS,(vee) 定义 master/slave 配置。

**文档事实** 文档示例还给出跨三块 board 的 UHC4 配置，以及跨两块 UHC4 card 的 ganging 配置。

**文档事实** DC Scale 通道只允许 POS，NEG 不允许用于 DC Scale 通道。

**文档事实** DFPS? 的 pinlist 可用 @ 字符读取所有已配置的 power supply pins。

**文档事实** DPS128 与 DPS64 的 ganging 只能在同一 card 内连续通道之间进行，不能跨 card，且通道必须同为 HC 或 HV 类型；同时不能超过每个 card 的最大电流。

**文档事实** XPS256 只允许同一 HLA 上的通道 gang；UHC4 与 UHC4T 可在同一 card 内连续通道以及同一 test head 内的任意数量 card 之间 gang，但同一 ganging group 内不支持 UHC4 与 UHC4T 混用。

**文档事实** 外部 device power supply 的 dps_channel 为三或四位整数，前一或两位定义外部 supply，建议使用大于 8 的值以避免与内部 supply 冲突，最大支持 16；后两位定义 DPS 通道号，小于 10 时须加前导 0。

## 和谁有关

- **文档事实** DDIC，本页 Related information 列出它，DC Scale 通道跨 card ganging 前必须用 DDIC 启用连接，示例也先执行 DDIC CONN。
- **文档事实** PALS 与 PSTE，文档在开头说明多 site 配置由这两个命令定义。
- **文档事实** UDPS，其文档说明 UDPS 删除先前由 DFPS 定义的 DPS pin，并解除 gang 配置。
- **文档事实** DPS128 与 DPS64 card，本页参数表分别给出二者的 ganging 限制。
- **文档事实** XPS256、UHC4、UHC4T，本页参数表分别给出它们的 ganging 规则。
- **文档事实** external device power supply，本页参数表说明其 dps_channel 的三或四位编号规则。
- **文档事实** PSSL、PSLV、PSLR、PSLC、PSSR、PSER 与 UHCM 等命令，它们的文档说明 pinlist 或通道必须已由 DFPS 定义。
- **文档事实** CHIN，其文档说明 DPS 通道号格式参见 DFPS；PDMM 与 CSAS 的页面把 DFPS 列为相关命令。
- **文档事实** Configuration Setup Commands，本页 Application 段把 DFPS 归入 Configuration Setup。
- **文档事实** DFPN，DPS128 与 DPS64 功能页把 DFPN 描述为 PMU operating mode 下进行 ganging 的对应命令。

## 版本

**文档事实** Functional changes 记载 Introduced before SmarTest 6.3.2。

**文档事实** SmarTest 6.5.0 新增 DC Scale UHC4 card。

**文档事实** SmarTest 7.3.1 新增 DC Scale PVI8 card。

**文档事实** SmarTest 7.3.2 新增 DC Scale UHC4T card。

**文档事实** SmarTest 7.4.0 新增 DC Scale AVI64 card。

**文档事实** SmarTest 7.5.0 新增 DC Scale FVI16 card。

## 出处

- `02_System_reference/02.06_Command_Reference/02.06.02.02.65_DFPS__DFPS__-__DeFine_Power_Supply.htm`
