---
type: object
title: DFUT, DFUT? - (DeFine UTility line)
layer: L1
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.70_DFUT__DFUT__-__DeFine_UTility_line.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# DFUT, DFUT? - (DeFine UTility line)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **2,306 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.70_DFUT__DFUT__-__DeFine_UTility_line.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### DFUT

```
DFUT {ch_No}, {type}, {(util_name)}
```

### DFUT?

```
DFUT? {(util_name)}
```

returns

```
DFUT {ch_No}, {type}, {(util_name)}
```

### Parameters

[表]
行 1:
  ch_No
  Channel number of the utility line specified
    with five or three digits.
    
    In the five‑digit format, the first three digits
    specify the utility pogo block. For valid pogo blocks, refer
    to `DUT interface layout`（raw: `20811.htm`） and to `Utility pogo block mapping`（raw: `347642.htm#_347642__s_Utility_pogo_block_mapping`） in `Utility pogo block - Utility Card (V93000 EXA Scale systems)`（raw: `347642.htm`）.
    
    In the legacy three‑digit format, the first digit
    (1 ... 8) specifies the utility pogo block
    UTIL‑1 ... UTIL‑8.
    
    The last two digits specify the channel number
    01 ... 32 of the utility line.
    
    On the utility pogo blocks, an offset of -1 is to be
    considered and the channel number is
    URW00 ... URW31.
    
    When reading the defined utility lines with the
    DFUT? command, the data returned
    always have the five‑digit format. The same applies
    to the `PALS?`（raw: `98680.htm`） command.
    
    For more information, see `Utility line assignments`（raw: `59181.htm`） and `DUT interface layout`（raw: `20811.htm`）
行 2:
  type
  Specifies the operating mode of the utility line with the
    following specifiers:
    
    W: Write-Only
    
    R: Read-Only
    
    RW: Read-Write
    
    Utility lines of the optional `Utility Card`（raw: `351250.htm`） can also be configured as safety
    lines or as global shutdown line for
    hardware‑controlled shutdown of XPS256 pins:
    
    TRIGGER_IF_HIGH: Safety line
    
    TRIGGER_IF_LOW: Safety line
    
    TRIGGER_SITE_IF_HIGH: Global shutdown
    line
    
    TRIGGER_SITE_IF_LOW: Global shutdown
    line
    
    For more information, refer to `XPS256 safety line and DUT board disconnect`（raw: `354940.htm`）.
行 3:
  util_name
  Name of the utility line. For the query, it specifies the
    utility line name to be retrieved. @ can be
    used to list all defined utility lines.
    
    This parameter can have up to 16 alphanumeric characters and must
    not contain blank spaces, or any of the following characters:
    # ; ( ' ' ) ? @ ,

### Example

```
DFUT 16504,w,(filter)
```

This
example assigns the name
filter
 and operating mode

w
 to utility line 4 of the first utility pogo
block.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.70_DFUT__DFUT__-__DeFine_UTility_line.htm>` 的 `## Errors` 段。**不是转述。**
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

The channel number is out of range.

The channel number is already used.

The utility line name is out of range.

The utility line name is already assigned to an analog or digital pin.

<!-- 报错节 end -->

## 是什么

**文档事实**：DFUT 为一条 utility line 定义符号名（`util_name`）和操作模式（`type`）。`DFUT?` 按 `util_name` 查询已定义的 utility line，`@` 可列出全部。

**文档事实**：`type` 的常规取值：`W` = Write-Only、`R` = Read-Only、`RW` = Read-Write。可选 `Utility Card` 的 utility line 还可配置为 safety line 或 global shutdown line，用于硬件控制 XPS256 pin 的 shutdown：`TRIGGER_IF_HIGH` / `TRIGGER_IF_LOW` 是 safety line，`TRIGGER_SITE_IF_HIGH` / `TRIGGER_SITE_IF_LOW` 是 global shutdown line。

**文档事实**：`ch_No` 支持五位数与 legacy 三位格式：五位格式前三位是 utility pogo block，三位格式首位 1–8 表示 UTIL-1…UTIL-8；后两位是通道号 01–32。utility pogo block 上有 -1 偏移，通道号为 URW00…URW31。`DFUT?` 返回始终是五位数格式，`PALS?` 同样。

**文档事实**：`util_name` 最多 16 个字母数字字符，不能含空格及 `# ; ( ' ' ) ? @ ,`。报错条件：通道号超范围、通道号已被使用、utility line 名字超范围、名字已分配给 analog 或 digital pin。

## 典型用法

**文档事实**：`DFUT 16504,w,(filter)`——把第一个 utility pogo block 的第 4 号 utility line 命名为 `filter`，操作模式为 Write-Only（`w`）。

**文档事实**：查询单条线用 `DFUT? (filter)`；查询全部已定义 utility line 用 `DFUT? (@)`。

**文档事实**：需要把 utility line 用作 XPS256 的硬件安全关机时，`type` 选 `TRIGGER_IF_HIGH` / `TRIGGER_IF_LOW`（safety line）或 `TRIGGER_SITE_IF_HIGH` / `TRIGGER_SITE_IF_LOW`（global shutdown line）；具体行为见 `XPS256 safety line and DUT board disconnect`。

**建议**：命名前先 `DFUT? (@)` 或 `PALS?` 全量回读查重。文档规定同一通道不能被重复使用、名字不能与 analog/digital pin 冲突，先用 `@` 回读是最直接的查重方式。

## 和谁有关

- `UTST` / `UTST?`：**文档事实**——UTST 文档说被查询的 utility line 必须由 DFUT 定义。**推断**：因此 DFUT 的命名是 UTST 按名称操作该线的前置；文档只写了"必须先定义"，没有展开顺序示例。
- `PALS` / `PALS?`：**文档事实**——PALS? 文档就 utility line 的通道号写 "see DFUT, DFUT? - (DeFine UTility line) for the channel number"；DFUT 的 `ch_No` 说明也明确 `PALS?` 与 `DFUT?` 一样返回五位数格式。
- `DFUP`：**文档事实**——DFUP 的 Errors 段规定，若通道已在 DFUT 中定义为 READ ONLY，DFUP 报错；DFUP 定义 utility purpose（通道组加标准状态），DFUT 定义单条线的符号名与方向。**推断**：两者是"线"与"线的组"的分工，先 DFUT 后 DFUP 是自然顺序，但文档没有强制先后。
- `Utility Card`：**文档事实**——`type` 参数说明把 `TRIGGER_*` 关键字限定为可选 Utility Card 的 utility line，并链接到 Utility Card 主题。
- `XPS256 safety line and DUT board disconnect`：**文档事实**——`type` 参数说明在给出 `TRIGGER_IF_HIGH` / `TRIGGER_IF_LOW` / `TRIGGER_SITE_IF_HIGH` / `TRIGGER_SITE_IF_LOW` 后直接让读者参考本篇，用于 XPS256 pin 的硬件控制 shutdown。
- `Utility line assignments`、`DUT interface layout`：**文档事实**——DFUT 的 `ch_No` 参数与 Related information 直接指向这两篇，用于确定 utility pogo block 与通道编号。

## 版本

**文档事实**：Functional changes 记录：Introduced before SmarTest 6.3.2（哨兵值，表示在文档集覆盖起点之前已有，不是 6.3.2 的变更）；SmarTest 7.10.1 在 V93000 EXA Scale 系统上引入三位 utility pogo block 编号；SmarTest 7.10.2 为 `type` 参数新增关键字，用 utility line 配置 XPS256 pin 的 shutdown（"New keywords for the type parameter to configure shutdown of XPS256 pins using utility lines"）。

## 出处

- `02_System_reference/02.06_Command_Reference/02.06.02.02.70_DFUT__DFUT__-__DeFine_UTility_line.htm`——语法、参数、示例、Errors、Related information 与 Functional changes 均取自本篇。