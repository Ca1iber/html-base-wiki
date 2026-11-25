---
type: object
title: UPAS, UPAS? - (Utility Purpose ASsignment for multi-site)
layer: L1
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.304_UPAS__UPAS__-__Utility_Purpose_ASsignment_for_multi-site.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# UPAS, UPAS? - (Utility Purpose ASsignment for multi-site)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,759 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.304_UPAS__UPAS__-__Utility_Purpose_ASsignment_for_multi-site.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### UPAS

```
UPAS {site}, ["{setting}"], {(purpose_name)}
```

### UPAS?

```
UPAS? {site}, {(purpose_name)}
```

returns:

```
UPAS {site}, "{setting}", {(purpose_name)}
```

### Parameters

[表]
行 1:
  site
  The site parameter is an integer that defines the number of the site where the
    channels are to be defined.
    
    The integer must be greater than 1.
    
    When specified as part of the UPAS? query, you
    can use the parameter ALL to read the
    standard output states for all sites.
行 2:
  setting
  Output states for each member of the utility purpose on the specified site.
    
    Set the output state of each utility line with the following
    specifiers:
    
    0: Sets the corresponding (write) channel to high (high impedance state)
    
    1: Sets the corresponding (write) channel to low
    
    X (x): No action
    
    The number and order of characters must correspond to the ch_No_list parameter
    of the `DFUP`（raw: `98559.htm`） command.
    
    If this parameter is omitted, the specified site is set to the same states as site 1.
行 3:
  purpose_name
  Name of a utility purpose defined by the `DFUP`（raw: `98559.htm`） command.
    
    In the query, the symbol @ can be used to list all defined
    utility purposes.

### Example

```
> DFUP (101,102,103,104),"11XX",(AWG_CNCT)
> UPAS 2,"XX11",(AWG_CNCT)
> UPST ,(AWG_CNCT)
> FLSH
> UPST? (AWG_CNCT)
< UPST "11XX", (AWG_CNCT)
> PSFC 2
> UPST ,(AWG_CNCT)
> FLSH
> UPST? (AWG_CNCT)
< UPST "XX11", (AWG_CNCT)
```

In
this example, the
`DFUP`（raw: `98559.htm`）
 command defines a utility purpose AWG_CNCT
and output states for site 1. The
UPAS
 command defines the output states of
AWG_CNCT for site 2. First the settings of site 1 are activated. Then the setup focus is
restricted to site 2, and the output states for site 2 are activated.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.304_UPAS__UPAS__-__Utility_Purpose_ASsignment_for_multi-site.htm>` 的 `## Errors` 段。**不是转述。**
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

A multisite setting is not performed with the
`PSTE`（raw: `98711.htm`）
 command.

The specified site number is less than 0 or greater than that of the max site.

The given name is not allocated to any utility purpose.

The given name has already been assigned to a digital pin, analog pin, DPS pin, or utility
name.

Inconsistent settings are specified for one channel (for an example, see the
`DFUP`（raw: `98559.htm`）
 command).

The setting contains characters other than "0", "1" and "X (or x)".

The number of characters in the setting is not equal to that of the channel list in the

`DFUP`（raw: `98559.htm`）
 command.

<!-- 报错节 end -->

## 是什么

**文档事实**：`UPAS` 命令为 site > 1 的同一 utility purpose 分配不同的标准输出状态；该 utility purpose 必须先用 `DFUP` 定义，`DFUP` 同时设置 site 1 的标准输出状态。

**文档事实**：`setting` 中每个字符对应 utility purpose 的一个成员（由 DFUP 的 `ch_No_list` 参数定义）：`0` 把对应（write）channel 置高（高阻态），`1` 置低，`X`（或 `x`）不动作；字符的数量和顺序必须与 DFUP 的 channel 列表一致。省略 `setting` 时，指定 site 被设为与 site 1 相同的状态。

**文档事实**：`site` 是整数，且必须大于 1；在 `UPAS?` 查询中可用 `ALL` 读取所有 site 的标准输出状态。

**文档事实**：`purpose_name` 必须是由 `DFUP` 定义的 utility purpose 名；查询中可用 `@` 列出所有已定义的 utility purpose。

**文档事实**：要激活输出状态，需先用 `PSFC` 把 setup focus 限制到目标 site，再用 `UPST` 和 `FLSH` 激活。本命令配置的是具有 setup focus 的那些 site。

**文档事实**：多 site 设置必须用 `PSTE` 命令完成，否则报错（见 `Errors`）。

## 典型用法

**文档事实**：示例命令序列：

```
> DFUP (101,102,103,104),"11XX",(AWG_CNCT)
> UPAS 2,"XX11",(AWG_CNCT)
> UPST ,(AWG_CNCT)
> FLSH
> UPST? (AWG_CNCT)
< UPST "11XX", (AWG_CNCT)
> PSFC 2
> UPST ,(AWG_CNCT)
> FLSH
> UPST? (AWG_CNCT)
< UPST "XX11", (AWG_CNCT)
```

**文档事实**：示例先用 `DFUP` 定义 utility purpose `AWG_CNCT` 及 site 1 的输出状态，再用 `UPAS` 定义 site 2 的 `AWG_CNCT` 输出状态；先激活 site 1 的设置，然后把 setup focus 限制到 site 2 并激活 site 2 的输出状态。

**文档事实**：查询形式为 `UPAS? {site}, {(purpose_name)}`，返回 `UPAS {site}, "{setting}", {(purpose_name)}`；用 `@` 可列出所有已定义的 utility purpose。

## 和谁有关

**文档事实**：以下关系均由来源文档的正文、参数说明或回链证据支撑。

- [[dfup]]：定义 utility purpose 和 site 1 的输出状态；`UPAS` 的 `purpose_name`、`setting` 的长度与顺序都依赖它（本页正文与 Parameters 明确写出）。
- [[psfc]]：激活前必须用它把 setup focus 限制到目标 site；`UPAS` 配置的是具有 setup focus 的各 site（本页正文明确写出）。
- [[flsh]]：激活输出状态需在 `UPST` 之后调用 `FLSH`（本页正文明确写出）。
- [[pste]]：本页 `Errors` 说明多 site 设置未用 `PSTE` 完成会报错。
- [[dfut]]、[[udut]]、[[udup]]：Pin configuration setup commands 文档把 `DFUT`、`UDUT`、`DFUP`、`UPAS`、`UDUP` 并列为 utility line 命令（回链证据）。
- `UPST`（`02_System_reference/02.06_Command_Reference/02.06.02.02.305_UPST__UPST__-__Utility_Purpose_STate.htm`）：本页要求先用 `PSFC` 限定 focus，再用 `UPST` 和 `FLSH` 激活输出状态；本 wiki 无该对象页。
- `Defining a utility purpose`（`02_System_reference/02.06_Command_Reference/02.06.03.01.08_Defining_a_utility_purpose.htm`）、`Accessing Utility Lines`（`02_System_reference/02.06_Command_Reference/02.06.12.01_Accessing_Utility_Lines.htm`）：本页 `Application` 指向它们作为 utility purpose 的上文，后者以本页命令为例（回链证据）。

## 版本

**文档事实**：`Functional changes` 只记录 `Introduced before SmarTest 6.3.2`。这是哨兵值，表示文档集覆盖范围之前已有，不能当作 6.3.2 的变更；文档未记录更晚变更。

## 出处

- 主源：`02_System_reference/02.06_Command_Reference/02.06.02.02.304_UPAS__UPAS__-__Utility_Purpose_ASsignment_for_multi-site.htm`（正文、UPAS/UPAS?、Parameters、Application、Errors、Example、Functional changes）。
- 回链证据：`02_System_reference/02.06_Command_Reference/02.06.02.02_List_of_commands.htm`、`02.06.03_Pin_configuration_setup_commands.htm`、`02.06.03.01.01_Introduction.htm`、`02.06.12.01_Accessing_Utility_Lines.htm`、`02.06.01.05_Site_dependent_firmware_commands.htm`、`02.06.02.02.01_Site_dependent_firmware_commands.htm`。
