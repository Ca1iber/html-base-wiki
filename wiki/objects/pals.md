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

**文档事实**：PALS（Pin ALlocation for multiple Sites）为 site 1 以外的 site 定义 pin 所使用的测试系统通道号；site 1 的通道由 `DFPN` 定义。`site` 必须是大于 1 的整数。

**文档事实**：`channel_1` 是该 site 中该 pin 使用的测试系统通道号：digital 或 DC Scale 通道用五位通道号，utility line 的通道号见 `DFUT`；`channel_2` 在文档中标注为 "currently not used"。

**文档事实**：DC Scale 通道可用括号内的通道列表定义 Master/Slave 配置，列表第一个通道为 master。UHC4/UHC4T 要求通道在同一块板上物理相邻，或是一块板的第 4 通道加另一块板的第 1 通道；不能把 UHC4 与 UHC4T 混在同一组；跨板 ganging 前必须先用 `DDIC` 使能连接。

**文档事实**：`PALS?` 返回每个通道所分配的 pin 名。查询时 `site` 可写 `ALL` 读取所有 site 的通道分配，或写 `PEND` 读取 pending 的通道分配；`@` 可列出 PALS 定义过的全部 pin；查询不存在的 pinlist 时系统不返回内容。

## 典型用法

**文档事实**：`PALS 2,10201,,(Clock)` 与 `PALS 2,10202,,(D0)`——把 site 2 的 Clock 引脚分配到通道 10201、D0 引脚分配到通道 10202。

**文档事实**：`PALS 2,(10101, 10102),,(dc1)`——为 DC Scale 通道定义 master/slave 配置，第一个通道为 master。

**文档事实**：跨板 UHC4 ganging 的示例先执行 `DDIC CONN, (104GO, 105GI)` 与 `DDIC CONN, (105GO, 107GI)`，再用一条 `PALS 2,(10403, 10404, 10501, ..., 10702),,(dc1)` 列出 8 个通道并指定第一个为 master。

**文档事实**：差分引脚示例先用 `DFAN "MCE231,2,i","",(av8_bbrx_b+)` 等定义 MCE231 上的 `av8_bbrx_b+` / `av8_bbrx_b-`，再在 site 2/3/4 上分别用 PALS 把各 site 的 MCE 通道分配给这两个 pin。

**建议**：多 site 配置中先把该 site 所有 pin 的通道分配完，再启用并行测试；PACT 与 PSTE 的 Errors 段都把"该 site 仍有 pin 未由 PALS 分配通道"列为报错条件。

## 和谁有关

- `DFPN`：**文档事实**——PALS 的 `site` 参数说明 site 1 的通道由 DFPN 定义，并让读者到 DFPN 查通道号；PALS 只负责 site > 1。
- `DFUT`：**文档事实**——PALS 的 `channel_1` 说明把 utility line 的通道号指向 DFUT；DFUT 页也说明 `DFUT?` 与 `PALS?` 读回时总是五位格式。
- `DDIC`：**文档事实**——`DC_scale_channels_list` 说明跨板 ganging 前必须由 DDIC 使能连接。
- `PSTE` / `PACT`：**文档事实**——两者的 Errors 段都把 "not all pins at the site have had their channels assigned by the PALS command" 列为报错。
- `DFPS`：**文档事实**——DFPS 页写明多 site 配置由 PALS 和 PSTE 命令定义。
- `DFUP`：**文档事实**——DFUP 页说明 `PALS?` 与 `DFUT?` 一样，读回 utility line 时总是五位格式。
- `DUT interface layout`：**文档事实**——PALS 的 Related information 指向该篇。
- `Pin configuration setup commands`：**文档事实**——PALS 的 Application 段把 PALS 归在 Pin Configuration / Configuration Setup Commands 之下。

## 版本

**文档事实**：Functional changes 记录：Introduced before SmarTest 6.3.2（早于文档集覆盖起点即已存在，不是 6.3.2 的变更）；SmarTest 7.1.3 支持 MBAV8+；SmarTest 7.5.0 为 stacked FVI16 通道新增额外参数 `channel_3`。

**文档事实**：本页语法/参数节仍只列出 `channel_2`（"currently not used"），没有列出 Functional changes 提到的 `channel_3`；两处信息不一致，实际语法应以对应版本文档原文为准。

## 出处

- `02_System_reference/02.06_Command_Reference/02.06.02.02.173_PALS__PALS__-__Pin_ALlocation_for_multiple_Sites.htm`——首段、语法/参数、四个示例、Errors、Related information 与 Functional changes 均取自本篇。
