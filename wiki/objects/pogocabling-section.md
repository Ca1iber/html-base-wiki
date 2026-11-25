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

（待补）

## 典型用法

（待补）

## 和谁有关

（待补）

## 版本

（待补）

## 出处

（待补）
