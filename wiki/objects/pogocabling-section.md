---
type: object
title: POGOCABLING section
layer: file
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.04_Model_File_and_Licensing/02.04.01.03.02.02_POGOCABLING_section.htm
  - 02_System_reference/02.04_Model_File_and_Licensing/02.04.01.03.02.02.01_Pogocabling_entries_for_various_card_types.htm
  - 02_System_reference/02.04_Model_File_and_Licensing/02.04.01.03.02.02.02_Conversions__pogo_mapping_file__-__POGOCABLING.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# POGOCABLING section

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **5,464 字符逐字取自** `<02_System_reference/02.04_Model_File_and_Licensing/02.04.01.03.02.02_POGOCABLING_section.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
<physical_location>: pogoblocks = "<pogoblock_list>", type = SD | HD1x256 | HD2x32 | HD4x32 | VHD1x128 | VHD4x32 | REDIRECT, subtype
```
[表] Parameters
行 1:
  <physical_location>
  Specifies the physical channel card position within the test head
    and the respective control segment. For more information regarding
    the control segments refer to `pogo mapping`（raw: `244158.htm`）.
    The format
    of the number is CSS:
    
    C represents the control segment (1 to
    4).
    
    SS represents the control segment slot
    number (01 to 18).
    
    Refer to table `Card cage allocation based on test head type`（raw: `106944.htm#_106944__t_Card_cage_allocation`） below
    for the assignment of the control segment and the control
    segment slot number.
    
    SS=09 and SS=18 address the two slots
    reserved for the legacy DPS cards, such as the
    MS-DPS.
行 2:
  pogoblocks
  Specifies the pogo pin blocks. <pogoblock_list> is a double
    quoted string defining the ordered list of pogo blocks or pogo block
    ranges. Use commas (,) to specify a list, like "101,
    103". Use hyphens (-) to specify a pogo block range,
    like "101-104". You can also mix pogo blocks and
    pogo ranges, like "101, 210-212".
    The total pogo
    block range is N MM, with N=1 to 8, MM=01 to 64. See also topic
    `DUT interface layout`（raw: `20811.htm`）.
    
    The physically addressable
    pogo block range depends on the selected pogo cable.
    
    Note The order of list must correspond to the structure
    of the pogo cable assembly. The first pogo block of the list
    defines always pogo block A of the cable. The last pogo block of
    the list defines always the last pogo block of the cable.
行 3:
  type
  Specifies the pogo cable type.
    
    SD is used for the standard pogo cable with 16 channels per pogo
    block. Depending on the channel card, one SD pogo cable ends in 1-8 pogo blocks with 16
    channels each.
    
    HD2x32 is presently not used by any channel card.
    
    HD4x32 describes a pogo cable with 32 channels per pogo block. One
    HD4x32 pogo cable ends in 4 pogo blocks with 32 channels each.
    
    VHD1x128 describes a PS1600 pogo cable with two VHD pogo blocks and
    64 channels per pogo block that is to be used for special
    configurations only.
    
    VHD4x32 is not yet used. It describes a DPS128 pogo cable with four
    pogo blocks and 32 channels per pogo block.
    
    REDIRECT, subtype is used for special DPS pogo cables which shall
    work also on older software revisions.
    If the software
    detects a "redirect" statement, the software will start,
    even if the information following redirect is unknown to
    this software revision.
    
    The type parameter is optional. If not specified, the system defaults to SD.

The following table shows the location of digital logical boards and DPS card
based on the POGOCABLING syntax.

[表] Card cage allocation based on test head type
列: Control segment | Card cages (cc), physical locations (CSS-CSS) | | Default location for DPS
行 1:
  LTH [跨 2 列]
  STH [跨 2 列]
  CTH [跨 2 列]
  ATH [跨 2 列]
  LTH [跨 2 行]
  STH [跨 2 行]
  CTH [跨 2 行]
  ATH [跨 2 行]
行 2:
  Card cage
  Location
  Card cage
  Location
  Card cage
  Location
  Card cage
  Location
行 3:
  1 [跨 2 行]
  5
  101-109
  1
  101-109
  1
  101-109
  1
  101-109
  
  4
  3
  1
  1
行 4:
  1
  110-118
  3
  110-118
  2
  110-118
  
  
  
  3
  1
  2
  
行 5:
  2 [跨 2 行]
  2
  201-209
  2
  201-209
  
  
  
  
  
  8
  2
  
  
行 6:
  6
  210-218
  4
  210-218
  
  
  
  
  
  7
  8
  
  
行 7:
  3 [跨 2 行]
  3
  301-309
  
  
  
  
  
  
  
  1
  
  
  
行 8:
  7
  310-318
  
  
  
  
  
  
  
  5
  
  
  
行 9:
  4 [跨 2 行]
  8
  401-409
  
  
  
  
  
  
  
  6
  
  
  
行 10:
  4
  410-418
  
  
  
  
  
  
  
  2
  
  
  

For more information refer to parameter
`physical_location`（raw: `106944.htm#_106944__row_Physical_location`）
 in table
`Parameters`（raw: `106944.htm#_106944__t_Parameters`）
 above.

For the default
relationship between card cages and groups see:

`Test Head sizes - Compact Test Head`（raw: `98106.htm`）

`Test Head sizes - Small Test Head`（raw: `98109.htm`）

`Test Head sizes - Large Test Head`（raw: `98112.htm`）

`Test Head sizes - A-Test Head`（raw: `134987.htm`）

`Test Head sizes - Compact Test Head with DUT scale interface`（raw: `126650.htm`）

`Test Head sizes - Small Test Head with DUT scale interface`（raw: `98115.htm`）

For drawings of all test heads, see
Mapping physical resources
.

### Error messages

SmarTest startup will terminate with explicit error
messages in the following cases:

an invalid pogo block number is used.

both pogo mapping file and POGOCABLING format are used in one model file.

in online mode, the provided pogo blocks in the model file do not match the
density of the installed card variant.

in offline mode, the density of the used hardware variant in the model file does
not match the provided pogo blocks in the model file.

an S2 pogo block is used to specify the pogo cabling of a UHC4T card.

an S1 pogo block is mapped to a UHC4T card, but
the corresponding S2 pogo block is occupied by another card.

a pogo cable type is specified, which is not supported for the installed channel
card.

### Example

The following example illustrates the pogocabling entry of a double density
digital card. 32 channels (2 logical boards) are routed via two pogo blocks of 16
channels each.

```
101: pogoblocks= "101,102"
```

For further
examples see
`Pogocabling entries for different card types`（raw: `140806.htm`）
.

<!-- 语法节 end -->

## 是什么

**文档事实**：POGOCABLING section 是 model file 的一节，定义 card slot（channel card 在 card cage 中的物理位置，即 control segment 位置）与 DUT interface 上 pogo block 的映射。它允许 card cage slot 与 pogo block 之间灵活走线，并取代早期的 pogo mapping file。语法为 `<physical_location>: pogoblocks = "<pogoblock_list>", type = SD | HD1x256 | HD2x32 | HD4x32 | VHD1x128 | VHD4x32 | REDIRECT, subtype`。

**文档事实**：`<physical_location>` 采用 CSS 格式：C 是 control segment（1–4），SS 是 control segment slot 号（01–18）。SS=09 与 SS=18 是保留给 legacy DPS 卡（如 MS-DPS）的两个 slot。`pogoblocks` 是双引号字符串，逗号分隔块、连字符表示范围、两者可混用（如 "101, 210-212"）；总块范围 N MM（N=1–8，MM=01–64），实际可寻址范围取决于所选 pogo cable，且列表顺序必须与 pogo cable assembly 的结构一致——列表第一个块始终是 cable 的 pogo block A，最后一个块是 cable 的最后一个块。

**文档事实**：`type` 指定 pogo cable 类型：`SD` 是标准 pogo cable，16 通道/块，按卡不同一条 cable 终止于 1–8 个块；`HD4x32` 为 32 通道/块、一条 cable 4 个块；`VHD1x128` 是 PS1600 的 pogo cable（2 个 VHD 块、64 通道/块），仅用于特殊配置；`VHD4x32` 是 DPS128 的 pogo cable（4 块 × 32 通道），文档写"尚未使用"；`HD2x32` 目前没有卡使用；`REDIRECT, subtype` 用于特殊 DPS pogo cable，使旧软件版本也能启动——软件一旦识别到 "redirect" 语句，即使后面的信息该版本不认识也会继续启动。`type` 可省略，默认 `SD`。

**文档事实**：语法行还列出 `HD1x256`，但 `type` 参数说明没有对它作任何解释（只解释了 SD、HD2x32、HD4x32、VHD1x128、VHD4x32、REDIRECT）。这是文档自身的空档，不是本页省略。

**文档事实**：同一 model file 同时使用 pogo mapping file 与 POGOCABLING 格式会导致 SmarTest 启动终止；此外以下情况也会终止启动并给出错误：pogo block 号非法；online 模式下 model file 给出的 pogo block 与所装卡变体的密度不匹配；offline 模式下 model file 所用硬件变体的密度与给出的 pogo block 不匹配；用 S2 pogo block 指定 UHC4T 的 pogo cabling；S1 映射到 UHC4T 但对应 S2 被其它卡占用；指定了所装 channel card 不支持的 pogo cable 类型。

**文档事实**：SmarTest 6.5.x 同时支持 pogo mapping file 与 POGOCABLING 格式；SmarTest 7.0 及以后只支持 POGOCABLING 格式。

## 典型用法

**文档事实**：最小示例 `101: pogoblocks= "101,102"`——双密度数字卡的 32 通道（2 个 logical board）经 2 个 16 通道的 pogo block 引出。

**文档事实**：不同卡型有不同条目，见子主题 `Pogocabling entries for various card types`。例如 DC Scale UHC4T 的 4 个通道被路由到合并为一个单元的 2 个 pogo block（占用 S1/S2 对），model file 只填 S1 位置，软件自动封锁相邻 S2。

**文档事实**：从旧的 pogo mapping file 迁移时，需先在 SmarTest 6.5.x（不是 7.x）启动，生成 `/opt/hp93000/soc/system/log` 下的 `PogoCabling.log`，其中含当前 pogo mapping；再按 `Conversions: pogo mapping file <-> POGOCABLING` 转换。SmarTest 7.0+ 不接受 pogo mapping file。

**建议**：写 `pogoblocks` 列表时按实际 cable assembly 的物理顺序排列，不要按块号"排序"——文档明确列表顺序决定 cable 的 A 块到末块，重排会改变映射。这是建议；文档只规定顺序必须对应 cable 结构。

## 和谁有关

- `DPS section`：**文档事实**——DPS section 文档说，DPS-slot 器件电源要指定 slot 号；DC Scale 卡要使用 POGOCABLING section 中指定的 pogo block 的六位数 channel 号；在该 section 里所有卡都必须指定类型。两个 section 需配套填写。
- `GLOBAL section` / `Model file reference (model legacy)`：**文档事实**——GLOBAL section 与 legacy model file 参考都把 POGOCABLING 列为 model file 的一节；legacy 参考列出的 section 顺序包含 GLOBAL、POGOCABLING、IOCHANNEL、INTERFACE_SECTION、ETC、DPS、DMM。
- `Pogo mapping`：**文档事实**——该页说 `CARD_CONFIGURATION` section of the tester.model file 把卡的物理位置映射到 DUT interface 的 pogo block 编号，并明确 "In the legacy model file, mapping is made in the POGOCABLING section"。
- `DUT interface layout`：**文档事实**——该页说 POGOCABLING section（SmarTest 7）与 CARD_CONFIGURATION section（SmarTest 8）把卡的 card cage 位置映射到 DUT interface 的 pogo block 位置；POGOCABLING 的 `pogoblocks` 参数也直接引用该页。
- `UHC4T specific setup tasks`：**文档事实**——该页要求 UHC4T 必须同时在 DPS section 与 POGOCABLING section 中定义（或写在 tester.model 的 CARD_CONFIGURATION section），软件标识为 `DCS-UHC4T`。**推断**：这与本页 Error messages 中的 S1/S2 pogo block 限制相互印证。
- `Pogocabling entries for various card types`、`Conversions: pogo mapping file <-> POGOCABLING`：**文档事实**——本页 Subtopics 与 Related information 直接列出这两篇子主题；前者给各卡型的条目写法，后者给迁移步骤与日志。
- `DUT Scale interface`：**文档事实**——该页入边写 "The POGOCABLING section in the model file maps the physical position of a card with the pogo block numbering of the DUT interface"，即把本页当作 DUT Scale 接口映射的定义处。
- `SE-UDPS`：**文档事实**——该页入边写 SE-UDPS "is to be defined in the DPS section of the model file and in the POGOCABLING section of the file"，并给出 `POGOCABLING <physical_card_location>: pogoblocks = "<pogoblock_list>"` 的写法。
- `DPS128/DPS64 pogo cable assemblies and pogo pin assignments`、`PS1600 pogo pin assignment`、`Concepts of logical boards`：**文档事实**——这三篇的入边都只是链接到本页（PS1600 篇的语境写作 "SmarTest 7: POGOCABLING section"），未给出更具体的用途句。

## 版本

**文档事实**：Functional changes 记录：Introduced in SmarTest 6.5.0；SmarTest 7.0.1 新增 pogo cable 参数 `type` 与 `subtype`，并新增 Pin Scale 9G 卡的 pogo block 计算；SmarTest 7.1.0 新增 PS1600 的 pogo cable 参数与 PS1600 卡的 pogo block 计算；SmarTest 7.1.3 把 MCE 加入 analog hardware types。

**文档事实**：SmarTest 7.0 起只支持 POGOCABLING 格式，pogo mapping file 不再被接受；6.5.x 是两种格式并存的最后版本（见 Conversions 子主题）。

## 出处

- `02_System_reference/02.04_Model_File_and_Licensing/02.04.01.03.02.02_POGOCABLING_section.htm`——语法、参数、Card cage allocation 表、错误信息、示例与 Functional changes 均取自本篇。
- `02_System_reference/02.04_Model_File_and_Licensing/02.04.01.03.02.02.01_Pogocabling_entries_for_various_card_types.htm`——各卡型条目（含 UHC4T 的 S1/S2 用法）取自本篇。
- `02_System_reference/02.04_Model_File_and_Licensing/02.04.01.03.02.02.02_Conversions__pogo_mapping_file__-__POGOCABLING.htm`——6.5.x/7.0 支持差异、`PogoCabling.log` 与迁移步骤取自本篇。