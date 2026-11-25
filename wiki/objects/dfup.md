---
type: object
title: DFUP, DFUP? - (DeFine Utility Purpose)
layer: L1
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.69_DFUP__DFUP__-__DeFine_Utility_Purpose.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# DFUP, DFUP? - (DeFine Utility Purpose)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **2,727 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.69_DFUP__DFUP__-__DeFine_Utility_Purpose.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### DFUP

```
DFUP {(ch_No_list)}, "{setting}", {(purpose_name)}
```

### DFUP?

```
DFUP? {(purpose_name)}
```

returns

```
DFUP {(ch_No_list)}, "{setting}", {(purpose_name)}
```

### Parameters

[表]
行 1:
  ch_No_list
  Utility line channel numbers to be defined as the members of
    a utility purpose and specified with five digits. The
    channels must be separated with a comma.
    
    In the five‑digit format, the first three digits of the channel numbers specify
    the utility pogo block. For valid pogo blocks, refer to
    `DUT interface layout`（raw: `20811.htm`） and to `Utility pogo block mapping`（raw: `347642.htm#_347642__s_Utility_pogo_block_mapping`） in `Utility pogo block - Utility Card (V93000 EXA Scale systems)`（raw: `347642.htm`）.
    
    The legacy three‑digit format is also supported: The first digit
    (1 ... 8) specifies the utility pogo block
    UTIL‑1 ... UTIL‑8.
    
    The last two digits specify the channel number
    01 ... 32 of the utility line.
    
    On the utility pogo blocks, an offset of -1 is to be
    considered and the channel number is
    URW00 ... URW31.
    
    When reading the defined utility lines with the DFUP? command, the
    data returned always have the five‑digit format. The
    same applies to the `PALS?`（raw: `98680.htm`）
    command.
    
    The channel numbers 16515 and 16516 should not be used. They
    should only be accessed with the `I2CA`（raw: `98637.htm`）or the `BDID`（raw: `98489.htm`）firmware command.
行 2:
  setting
  Output states for each channel in the
    ch_No_list. Specify the setting of each
    utility line with the following specifiers:
    
    0: sets the corresponding (write) channel to high (high
    impedance state)
    
    1: sets the corresponding (write) channel to low
    
    X (x): no action
    
    Specify the setting values corresponding to the definition order of the
    ch_No_list parameter.
    
    The number of characters must be equal to the number of the utility line channels in the
    ch_No_list parameter.
    
    Note that the settings must be explicitly activated with `UPST`（raw: `98833.htm`） and `FLSH`（raw: `99061.htm`）.
行 3:
  purpose_name
  Name of the utility purpose. In the query you can use the
    symbol @ to list all defined utility
    purposes.
    
    This parameter can have up to 16 alphanumeric characters and must
    not contain blank spaces, or any of the following characters:
    # ; ( ' ' ) ? @ ,

### Example

```
> DFUP (16501,16502,16503,16504),"0110",(AWG_CNCT)
> UPST ,(AWG_CNCT)
> FLSH
> UPST? (AWG_CNCT)
< UPST "0110",(AWG_CNCT)
```

This example defines a utility purpose AWG_CNCT
and activates its standard settings.

The members and the setting values are as
follows:

```
Member: 16501 16502 16503 16504
---------------------------------------
Setting: 0 1 1 0
```

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.69_DFUP__DFUP__-__DeFine_Utility_Purpose.htm>` 的 `## Errors` 段。**不是转述。**
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

The channel number is out of range.

The given name is already assigned to a digital pin, analog pin, DPS pin, or
utility name.

The specified channel has already been defined in the DFUT command as READ ONLY
capability.

Incompatible settings are specified for a channel (for example,
DFUP
(101,101),"10", (bad)
).

The setting contains characters other than "0", "1" and "X (or x)".

The number of characters in the setting is not equal to that of the channel
list.

<!-- 报错节 end -->

## 是什么

**文档事实**：DFUP 定义一组 utility line 通道（utility purpose），并为列表中的每个通道指定一个标准输出状态。这些标准设置必须用 `UPST` 激活、再由 `FLSH` 生效。`DFUP?` 按 `purpose_name` 查询已定义的 utility purpose，`@` 可列出全部。

**文档事实**：`ch_No_list` 是 utility line 通道号列表，逗号分隔。五位数格式的前三位指定 utility pogo block，后两位是通道号 01–32；legacy 三位格式的首位 1–8 表示 UTIL-1…UTIL-8。utility pogo block 上有 -1 偏移，通道号写作 URW00…URW31。`DFUP?` 返回的数据始终是五位数格式，`PALS?` 同样。通道 16515 与 16516 不应使用，只能通过 `I2CA` 或 `BDID` firmware 命令访问。

**文档事实**：`setting` 逐字符对应 `ch_No_list` 的定义顺序：`0` 把对应（写）通道置高（高阻态），`1` 置低，`X`（或 `x`）表示不动作；字符数必须等于通道数。`purpose_name` 最多 16 个字母数字字符，不能含空格及 `# ; ( ' ' ) ? @ ,`。

**文档事实**：名称冲突与通道冲突都会报错：给定名字已分配给 digital pin、analog pin、DPS pin 或 utility 名；指定通道已在 `DFUT` 中定义为 READ ONLY；同一通道给出不兼容设置；setting 含 0/1/X 以外字符；setting 长度与通道列表不符。

## 典型用法

**文档事实**：示例定义一个 4 通道的 utility purpose 并激活其标准设置：

```
> DFUP (16501,16502,16503,16504),"0110",(AWG_CNCT)
> UPST ,(AWG_CNCT)
> FLSH
> UPST? (AWG_CNCT)
< UPST "0110",(AWG_CNCT)
```

**文档事实**：成员 16501、16502、16503、16504 依次对应 setting 的 0、1、1、0。

**文档事实**：查询单个 purpose 用 `DFUP? (AWG_CNCT)`，查询全部已定义 purpose 用 `DFUP? (@)`。

**文档事实**：`setting` 只能描述写通道的输出状态；`X` 不改变通道，`0` 是高（高阻态）、`1` 是低电平。文档强调标准设置必须先 `UPST` 再 `FLSH`，单独发 `DFUP` 不会激活输出。

**建议**：把 `DFUP` 当作"定义/命名 + 标准状态"步骤，把 `UPST`/`FLSH` 当作"选择/下载"步骤；在脚本里把两者分开，避免误以为 `DFUP` 已经改变了硬件输出。

## 和谁有关

- `UPST` / `UPST?`、`FLSH`：**文档事实**——DFUP 首段与 `setting` 参数都写明标准设置必须由 `UPST` 激活、`FLSH` 生效；`UPST` 文档还写明省略其 setting 参数时，按 setup focus（由 `PSFC` 设定）使用 DFUP 或 UPAS 命令定义的设置。
- `UPAS`：**文档事实**——UPAS 文档要求 utility purpose 必须已由 DFUP 定义，DFUP 同时设置 site 1 的标准输出状态；UPAS 的 setting 字符数与顺序必须对应 DFUP 的 `ch_No_list`，文档还以 DFUP 的示例作为"同一通道设置不一致"报错的参照。
- `DFUT`：**文档事实**——DFUP 的 Errors 段规定，若指定通道已在 DFUT 中定义为 READ ONLY，DFUP 报错。DFUT 负责单条 utility line 的符号名与操作模式，DFUP 负责通道组与标准状态；**推断**：因此典型顺序是先用 DFUT 定义各条线的名称/方向，再用 DFUP 把可写的线组成 purpose。
- `UTST`：**文档事实**——`Defining a utility line` 页说可以用 `UTST` 逐条设置一条 utility line 的状态，也可以定义 utility purpose（DFUP），用一条命令设置一组线。
- `PALS` / `PALS?`：**文档事实**——DFUP 参数说明说 `DFUP?` 返回五位数格式，并明确 `PALS?` 同样如此，用于多 site 的 utility line 通道号。
- `I2CA`、`BDID`：**文档事实**——DFUP 参数说明规定通道 16515 与 16516 只能通过这两个 firmware 命令访问，不应作为普通 utility line 使用。

## 版本

**文档事实**：Functional changes 记录：Introduced before SmarTest 6.3.2（哨兵值，表示在文档集覆盖起点之前已有，不是 6.3.2 的变更）；SmarTest 7.10.1 在 V93000 EXA Scale 系统上引入三位 utility pogo block 编号（"Three-digit utility pogo block designator on V93000 EXA Scale systems"）。

## 出处

- `02_System_reference/02.06_Command_Reference/02.06.02.02.69_DFUP__DFUP__-__DeFine_Utility_Purpose.htm`——语法、参数、示例、Errors 与 Functional changes 均取自本篇。