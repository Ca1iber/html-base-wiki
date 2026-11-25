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

**文档事实** DFPN 即 DeFine Pin Name，把 pin name 分配给数字通道或 DC Scale 通道；分配后该 DC Scale 通道处于 PMU mode。pin name 是软件用来识别引脚的名称。

**文档事实** DFPN? 查询返回通道及其已分配的 pin name 列表。

**文档事实** 使用 DFPN 前，sequencer 状态必须为 OFF（见 SQST 命令）。

**文档事实** DFPN 也用于配置 DC Scale 通道在 PMU mode 下的 ganging。

**文档事实** 文档 Application 段把 DFPN 归入 Pin Configuration，参见 Configuration Setup Commands。

**文档事实** 参数表还覆盖 utility DC pins：utility DC 通道用三位 utility block 号；Functional changes 记 SmarTest 7.10.2 增加对 utility DC pins 的支持。

**文档事实** 参数表中 `connectionSet` 目前未使用，但它提供在同一 DC Scale 通道上定义多个 pin 的能力（DC Scale card 文档称其为 “Ganging on the fly”）；未使用该参数或传入空字符串时使用 default connection set，一个 DC Scale pin 只能属于一个 default connection set。

**文档事实** `pinNo` 是分配给指定通道的 device pin number，必须用双引号括起；`pinName` 在 32-bit SmarTest 中最多 16 个字符，在 64-bit SmarTest 中最多 64 个字符。

**推断** DFPN 与 DFPS 是两条并行的引脚分配路径：DFPN 面向数字通道与 DC Scale 的 PMU mode，DFPS 面向 DPS；CONF 只能确认由定义该引脚的 DFPN 或 DFPS 所决定的操作模式。

## 典型用法

**文档事实** 基本分配示例：`DFPN 10101,"1",(Clock)` 把 Clock 引脚分配到通道 10101，device pin number 为 1；`DFPN 10102,"2",(D0)` 把 D0 分配到通道 10102，device pin number 为 2。

**文档事实** 查询示例：`DFPN? (@)` 列出所有先前由 DFPN 定义的引脚，示例返回上述两条定义（文档返回行中的 `CD0` 与输入 `D0` 不一致，疑为文档笔误）。

**文档事实** ganging 示例：`DFPN (11901, 11902),,(vee)` 定义 PMU mode 下 DC Scale 通道的 ganging。

**文档事实** 五位数数字通道号中，前三位是 pogo block/board 号，后两位是 pogo block 内的引脚号（01 到 16）；例如 10105 是 pogo block 101 中 pogo pin 05。

**文档事实** utility DC 通道用三位 utility block 号；utility block number = 目标 utility line block + 164（EXA Scale 上第二个 utility line card 为 +264），例如 utility block 4 对应 168；为兼容 SmarTest 7.6x，HPMU1 映射为 UTIDC165（仅 Smart Scale 系统）。

**文档事实** ganging 时，DC Scale 通道必须在同一 board 上物理相邻；跨 card ganging 前必须用 DDIC 启用连接。

**文档事实** 跨 card ganging 时，由 DDIC 和 DFPN 定义的所有 traces 必须使用相同的 `connectionSet`；如果 DUT trace 能由 utility line 激活，文档建议按 utility line 命名（见 DFUP）。

**文档事实** DFPN? 的 `pinlist` 可用 `@` 列出所有已定义的 pin；多个 pin 名用逗号分隔；查询不存在的 pin 时系统返回空。

**文档事实** `connectionSet` 的多 pin 定义必须满足：新 pin 不使既有 pin 的设置失效；包含同一通道的不同 pin 必须属于同一 ports；这些 pin 的 patterns、events 和 DC-setups 不得重叠。

**建议** 在跨 card ganging 场景中先统一 `connectionSet` 命名，再分别执行 DDIC 与 DFPN，以减少 trace 与 connection set 不匹配的问题。

## 和谁有关

- **文档事实** DDIC，本页 Related information 列出它；跨 card ganging 前必须用 DDIC 启用连接，且 DDIC 与 DFPN 定义的所有 traces 必须具有相同 `connectionSet`。
- **文档事实** DFPS，DFPS 页说明 DC Scale 通道在 DPS mode 下的 ganging 由 DFPS 定义；DPS128/DPS64 功能页说明 PMU operating mode 的 ganging 用 DFPN、DPS operating mode 用 DFPS。
- **文档事实** CONF，CONF 页说明只能确认由定义该引脚的 DFPN 或 DFPS 所决定的操作模式（power pin 或 signal pin），并用 DFPN 设 PMU mode、DFPS 设 DPS mode 作示例。
- **文档事实** SQST，本页开头要求 DFPN 使用前 sequencer 状态必须为 OFF，并指向 SQST。
- **文档事实** PALS，PALS 页说明多 site 时 site 1 的通道由 DFPN 定义，通道号格式参见 DFPN。
- **文档事实** UDEF，Pin configuration setup commands 页把 DFPN、CONF、UDEF 并列为数字引脚命令，把 DFPN、UDEF、DFPS、UDPS、PSSL 并列为 DC Scale 引脚命令；UDEF 用于删除已定义的 pin。
- **文档事实** DFUP，本页在 `connectionSet` 命名建议中指向 DFUP，用于按 utility line 命名 DUT trace。
- **文档事实** PSSL，PSSL 页说明其引脚列表包含由 DFPN 定义的 DC signal（PMU）pins，并可为这些引脚设置 force voltage 与电流钳位的安全限值。
- **文档事实** CHIN、PDMM、CSAS、UPTD，这些页的 objpack 入边引文把 DFPN 列为相关命令：CHIN 指向其五位通道号定义，PDMM 与 CSAS 列入相关命令，UPTD 说明使用 DFPN 会把 up-to-date flag 置 0 直到保存或加载。
- **文档事实** Pogo pin assignment - Utility pogo blocks，参数表链接该页以说明 utility block 号。
- **文档事实** Control of the Pin Electronics Relays and the Relay Switching Method，objpack 入边引文说明 AC relay 把 DUT pin 连接到先前由 DFPN 定义的 test system channel。
- **文档事实** DPS128/DPS64 in PMU operating mode，objpack 入边引文把 DFPN 列为该工作模式的相关命令。
- **文档事实** List of commands 与 Pin configuration setup commands，索引页把 DFPN 列入命令清单。
- **推断** 综合 DDIC、DFPS、CONF 的说明，DFPN 是 PMU/DC Scale 侧“通道到 pin name”的主定义命令，DFPS 则负责 DPS 侧；两者共同决定后续 CONF 能确认的操作模式。

## 版本

**文档事实** Functional changes 记载：Introduced before SmarTest 6.3.2。

**文档事实** SmarTest 7.1.2：64-bit 系统上 pinName 的字符数扩展。

**文档事实** SmarTest 7.3.1：扩展支持 DC Scale PVI8；新增额外参数 `connectionSet`。

**文档事实** SmarTest 7.4.0：新增对 DC Scale AVI64 card 的支持。

**文档事实** SmarTest 7.5.0：新增对 DC Scale FVI16 card 的支持，并新增额外参数 `channelNo_2` 与 `channelNo_3`。

**文档事实** SmarTest 7.10.2：新增对 utility DC pins 的支持。

**文档事实** 与语法节的差异：Functional changes 提到 `channelNo_2` 与 `channelNo_3`，但本页语法节只列出 `channelNo_1`；语法节按脚本规则未改动。

## 出处

- `02_System_reference/02.06_Command_Reference/02.06.02.02.63_DFPN__DFPN__-__DeFine_Pin_Name.htm`，主源，含概述、Syntax、Parameters、Application、Errors、Examples、Related information 与 Functional changes。
- `02_System_reference/02.06_Command_Reference/02.06.02.02.54_DDIC__DDIC__-__Define_DUT_Interface_Connection.htm`、`02_System_reference/02.06_Command_Reference/02.06.02.02.65_DFPS__DFPS__-__DeFine_Power_Supply.htm`、`02_System_reference/02.06_Command_Reference/02.06.02.02.31_CONF__CONF__-__CONFiguration.htm`、`02_System_reference/02.06_Command_Reference/02.06.02.02.241_SQST__SQST__-__SeQuencer_STate.htm`、`02_System_reference/02.06_Command_Reference/02.06.02.02.173_PALS__PALS__-__Pin_ALlocation_for_multiple_Sites.htm`、`02_System_reference/02.06_Command_Reference/02.06.02.02.295_UDEF_-__UnDEFine_pin.htm`、`02_System_reference/02.06_Command_Reference/02.06.02.02.69_DFUP__DFUP__-__DeFine_Utility_Purpose.htm`、`02_System_reference/02.06_Command_Reference/02.06.02.02.196_PSSL__PSSL___Power_Supply_Safety_Limits.htm`，用于核对命令间关系（已用 show.py 读取）。
- CHIN、PDMM、CSAS、UPTD、DPS128/DPS64、Pogo pin assignment、Control of the Pin Electronics Relays、List of commands、Pin configuration setup commands 等引文取自 `extract/objpack.py` 入边索引。
