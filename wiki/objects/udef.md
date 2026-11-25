---
type: object
title: UDEF - (UnDEFine pin)
layer: L1
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.295_UDEF_-__UnDEFine_pin.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# UDEF - (UnDEFine pin)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **434 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.295_UDEF_-__UnDEFine_pin.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
UDEF {(pinlist)}
```

### Parameters

[表]
行 1:
  pinlist
  Consists of single or multiple pin names or the symbol @ which removes all pins. If
    more than one pin is required, the names must be separated with a comma.

### Example

```
UDEF (Q3)
```

This example causes pin Q3 to be removed from the
current configuration. If you subsequently redefine the channel using the same or a different
name, it assumes its former operating mode and the pin type

OFF
.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.295_UDEF_-__UnDEFine_pin.htm>` 的 `## Errors` 段。**不是转述。**
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if you attempt to undefine pins while the
sequencer is in the run or the break state. See the command
`SQST, SQST? - (SeQuencer STate)`（raw: `98752.htm`）
 for
details.

<!-- 报错节 end -->

## 是什么

**文档事实** UDEF（UnDEFine pin）从当前配置中删除已定义的 pin。

**文档事实** 参数 `pinlist` 可给单个或多个 pin 名称；多个名称用逗号分隔，符号 `@` 删除全部 pin。

**文档事实** 示例 `UDEF (Q3)` 把 pin Q3 从当前配置移除；若之后用相同或不同名称重新定义该 channel，它沿用之前的 operating mode，pin type 为 `OFF`。

**文档事实** Application 段把 UDEF 归入 Pin configuration，并指向 Configuration Setup Commands。

## 典型用法

**文档事实** 语法为 `UDEF {(pinlist)}`；示例 `UDEF (Q3)` 删除单个 pin。

**文档事实** 删除全部 pin 用 `UDEF (@)`（参数说明）。

**文档事实** sequencer 处于 run 或 break 状态时不能 undefine pins，否则报错；需先用 SQST 确认状态。

**推断** 由于被删 pin 的 channel 会记住原 operating mode、重定义时 pin type 回到 `OFF`，UDEF 可与 `DFPN` 搭配用于改名或把同一 channel 重新分配给另一个 pin 名；文档未给出该组合的完整流程。

## 和谁有关

- **文档事实** `[[dfpn]]` — 两者是 pin 定义的相反操作：DFPN 给数字 channel 或 DC Scale channel 分配 pin name，UDEF 把 pin 从当前配置移除。Pin configuration setup commands 的数字 pin 组列为 DFPN、CONF、UDEF，DC Scale 组列为 DFPN、UDEF、DFPS、UDPS、PSSL。
- **文档事实** `[[conf]]` — 与 UDEF 同属数字 pin 命令组 DFPN、CONF、UDEF。
- **文档事实** `[[dfps]]`、`[[udps]]`、`[[pssl]]` — 与 UDEF 同属 DC Scale pin 命令组 DFPN、UDEF、DFPS、UDPS、PSSL。
- **文档事实** `[[sqst]]` — Errors 段要求用 SQST 判断 sequencer 是否处于 run/break；DFPN 页同样要求使用前 sequencer 为 OFF（见 SQST）。
- **文档事实** `[[pin-configuration-file]]` — `02.04.05.08.02 Disabling a pin configuration license lock` 把 UDEF 列为会使 device-specific license signature 失效、禁用 setup 相关命令（VECC、VECD、SQLB、DMAS）的命令之一。
- **文档事实** `[[rset]]` — `DCCH`/`DCVH` 页把 UDEF 与 `DCCH`、`DCVH`、`*RST`、`RSET DC` 一起列为会使既有 DC 测量失效的 reset 条件。

## 版本

**文档事实** Functional changes 记载 “Introduced before SmarTest 6.3.2”。

## 出处

- `02_System_reference/02.06_Command_Reference/02.06.02.02.295_UDEF_-__UnDEFine_pin.htm`，主源，含用途、参数、Application、Errors、示例与 Functional changes。
- `02_System_reference/02.04_Model_File_and_Licensing/02.04.05.08.02_Disabling_a_pin_configuration_license_lock.htm`，用于确认 UDEF 对 license lock 的影响。
- `02_System_reference/02.06_Command_Reference/02.06.02.02.40_DCCH_-__DC_Current_measurement_High_precision_pmu.htm`，用于确认 UDEF 与 DC 测量 reset 的关系。
