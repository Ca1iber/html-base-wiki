---
type: object
title: UDPS - (Undefine DPS pin)
layer: L1
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.298_UDPS_-__Undefine_DPS_pin.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# UDPS - (Undefine DPS pin)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **464 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.298_UDPS_-__Undefine_DPS_pin.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
UDPS {(pinlist)}
```

### Parameters

[表]
行 1:
  pinlist
  Consists of single or multiple pin names or the symbol @ which undefines all
    DPS pins. If more than one pin is to be removed, the names must be separated with a comma.

### Example

```
UDPS (Vee)
```

This example removes pin Vee from the setup. The
software saves the level data associated with the DPS channel. Therefore if you redefine the
channel using the same or a different name, the DPS settings are immediately restored.

<!-- 语法节 end -->

## 是什么

**文档事实** UDPS（Undefine DPS pin）从当前 setup 中移除指定的 DPS pin；这些 pin 此前由 `[[dfps]]`（DFPS, DFPS? - DeFine Power Supply）定义。

**文档事实** 文档写明 gang（master/slave）配置也一并被 resolved（原句：the gang (master/slave) configuration is also resolved）。

**文档事实** `pinlist` 可为单个或多个 pin 名，多个名称以逗号分隔；符号 `@` 取消定义全部 DPS pin。

**文档事实** 软件会保存与该 DPS channel 关联的 level 数据；因此之后用相同或不同名称重新定义该 channel 时，DPS 设置立即恢复。

**文档事实** Application 段把 UDPS 归入 Pin configuration，并指向 Configuration Setup Commands。

**推断** 因此 UDPS 解除的是 pin 到 DPS 通道的当前 assignment，并不清除该通道已保存的 level 设置；重新定义会把原设置带回。

## 典型用法

**文档事实** 示例 `UDPS (Vee)` 把 pin Vee 从 setup 中移除。

**文档事实** 一次移除多个 DPS pin 时用逗号分隔名称；取消定义全部 DPS pin 用 `UDPS (@)`（参数说明）。

**文档事实** 若之后用同名或不同名重新定义该 channel，之前保存的 DPS 设置会立即恢复。

**建议** 若只是临时取消某个 DPS pin 并打算恢复，可用 UDPS 移除后再用 `[[dfps]]` 重新定义；文档说明通道的 level 数据会被保留并立即恢复。

## 和谁有关

- **文档事实** `[[dfps]]` — DFPS/DFPS? 定义 DPS pin；本命令移除的正是它先前定义的 pin，文档还说 gang 配置一并被 resolved。
- **文档事实** `[[udef]]` — 两者都是 undefine 类命令：UDEF 删除已定义 pin，UDPS 专门移除 DPS pin；02.06.03 的 DC Scale pin 命令组把 DFPN、UDEF、DFPS、UDPS、PSSL 列在一起。
- **文档事实** `[[pssl]]`、`[[dfpn]]` — 与 DFPS、UDEF、UDPS 同属 02.06.03 列出的 “Commands for DC Scale pins: DFPN, UDEF, DFPS, UDPS, PSSL”。
- **文档事实** `[[pin-configuration-file]]` — `02.04.05.08.02 Disabling a pin configuration license lock` 把 UDPS 列为可使 DSL 锁失效的命令之一：执行后会 invalidate device-specific-license signature，并禁用 setup 相关命令（VECC、VECD、SQLB、DMAS），需重新加载 pin configuration 才能恢复。
- **文档事实** `[[conf]]`、`[[ctxt]]`、`[[dfpn]]`、`[[dfps]]`、`[[dfut]]`、`[[dfup]]`、`[[pals]]` — license lock 页说明执行 UDPS 后这些 pin configuration 相关命令重新启用；同一段还列出 DDSL、DFAN（本 wiki 无独立页）。
- **文档事实** Pin configuration setup commands（`02.06.03`）与 Introduction（`02.06.03.01.01`）— 入边显示 UDPS 被列入 “Commands for DPS pins: DFPS, UDPS” 与 “Commands for DC Scale pins: DFPN, UDEF, DFPS, UDPS, PSSL”。
- **文档事实** List of commands — 入边显示 UDPS 列在命令参考总表。

## 版本

**文档事实** Functional changes 记：Introduced before SmarTest 6.3.2。

## 出处

- `02_System_reference/02.06_Command_Reference/02.06.02.02.298_UDPS_-__Undefine_DPS_pin.htm`，主源，含概览、Syntax、Parameters、Application、Example 与 Functional changes，已用 `show.py 02.06.02.02.298` 读取。
- `02_System_reference/02.04_Model_File_and_Licensing/02.04.05.08.02_Disabling_a_pin_configuration_license_lock.htm`，用于确认 UDPS 对 DSL 锁与 setup 相关命令的影响，已用 `show.py 02.04.05.08.02` 读取。
- 命令族与入边关系取自 `extract/objpack.py` / `edges.jsonl`。
