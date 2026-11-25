---
type: object
title: PACT, PACT? - (Parallel ACTivities control)
layer: L1
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.171_PACT__PACT__-__Parallel_ACTivities_control.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# PACT, PACT? - (Parallel ACTivities control)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,583 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.171_PACT__PACT__-__Parallel_ACTivities_control.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### PACT

PACT
 {
control
},
{
site
|
ALL
}

PACT

{"
site_string
"}

### PACT?

```
PACT?
```

returns

```
PACT {control}, {site}
```

Or:

```
PACT?STR
```

returns

```
PACT {"site_string"}
```

### Parameters

[表]
行 1:
  control
  The control parameter [跨 2 列]
    is:
行 2:
  
  ACTIVE
  When a site is ACTIVE it receives all test data, and
    generates results for the tests.
行 3:
  
  MASKED
  When a site is MASKED, it receives all test data, as with the
    ACTIVE parameter. However, the receivers for the site are disabled and
    no result information is available.
行 4:
  site
  A single integer representing a site [跨 2 列]
    number.
行 5:
  site_string
  A string consisting of "0" and "1". One [跨 2 列]
    character must be given for every site that is configured in the pin configuration. "0"
    indicates that the respective site is (to be) masked. "1" indicates that the respective
    site is (to be) activated.
行 6:
  ALL
  means that all configured sites that are [跨 2 列]
    available for testing (that is, do not use a channel that is inactivated in the MCDIgnore
    file) are to be activated or masked.
    
    For the MCDIgnore file see MCDIgnore usage and restrictions in Service Guide Part
    1.
行 7:
  STR
  forces the query to return a site string [跨 2 列]
    instead of a single line for every site.

### Example

```
> PACT ACTIVE, 1
> PACT MASKED, 2
> PACT MASKED, 3
```

This
example masks site 2 and site 3, and makes site 1 active.

```
> PACT?
< PACT ACTIVE,1
< PACT MASKED,2
< PACT MASKED,3
> PACT? STR
< PACT "100"
```

This
example shows the impact of the optional
STR
 parameter for the
query.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.171_PACT__PACT__-__Parallel_ACTivities_control.htm>` 的 `## Errors` 段。**不是转述。**
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if not all pins at the site have had their
channels assigned by the
`PALS`（raw: `98680.htm`）
 command.

<!-- 报错节 end -->

## 是什么

**文档事实**：PACT 是 firmware 命令，用于 mask 或 activate 指定 site；由 Site Control 窗口使用，也在 testflow 被要求串行执行、或分支后各 site 走不同执行路径时使用。`PACT?` 查询当前 site 状态（`02.06.02.02.171`）。

**文档事实**：`control` 取 `ACTIVE`（site 接收全部测试数据并产生测试结果）或 `MASKED`（仍接收全部测试数据，但该 site 的接收器被禁用，没有结果信息）。`site` 是单个整数 site 号；`ALL` 表示 pin configuration 中配置且可用于测试（即不使用 MCDIgnore 文件中 inactivated channel）的所有 site；`{"site_string"}` 用逐 site 的 `"0"`/`"1"` 字符表示 mask/activate，每个已配置 site 必须给一个字符。

**文档事实**：每执行一次 PACT 都会重置所有 site 的结果，即使命令只指定了一个 site。若 site 不可用，PACT 会发出 warning。

**文档事实**（原文 Note）：该命令实现 multisite 测试的 tpi 接口；应使用 tpi 调用而不是此 firmware 命令。**建议**：自动化流程走 tpi，只有在直接操作 firmware/调试时才用 PACT（文档倾向，非机台行为断言）。

## 典型用法

**文档事实**：激活 site 1、mask site 2 和 3：

```text
> PACT ACTIVE, 1
> PACT MASKED, 2
> PACT MASKED, 3
```

**文档事实**：查询与紧凑返回：

```text
> PACT?
< PACT ACTIVE,1
< PACT MASKED,2
< PACT MASKED,3
> PACT? STR
< PACT "100"
```

文档说明该例通过 `STR` 让查询返回单个 site 字符串；示例中 site 1 为 ACTIVE、site 2/3 为 MASKED，对应 `"100"`。

**文档事实**：也可用 `PACT {"site_string"}` 一次性设置多个 site（语法节）。

**建议**：需要保存/恢复 site 状态时，用 `PACT? STR` 取紧凑串、再用 `PACT "…"` 回写；文档给出了字符串格式，但没有给出这一组合的现成示例。

**文档事实**：每次 PACT 都会重置所有 site 的结果，即使只指定一个 site（源首段 Note）。**推断**：因此若在同一 testflow 中先取得结果、后执行 PACT，先前结果会被重置——这是「resets the results of all sites」的直接含义，文档未另给示例。

## 和谁有关

- [[pals]] — **文档事实**：若 site 上并非所有 pin 都经 `PALS` 分配了 channel，PACT 会报错（本页 Errors）。
- [[site-control-window]] — **文档事实**：文档 `Application` 节写明 PACT 应用于 Site Control 窗口（源 `Application`）。
- `EXSR`（`02.06.02.02.121`）— **文档事实**：EXSR 的 active sites 是「上次执行 PACT 命令所激活的 site」；默认只有第一个 site 处于 active（入边语境）。
- testflow 串行执行 / 分支 — **文档事实**：testflow 被要求串行运行，或分支后某些 site 走不同执行路径时，会使用 PACT（源首段）。
- [[pqfc]]、[[psfc]]、[[pste]]、[[stme]] — **文档事实**：与 PACT、PALS 同列为 multisite setup 命令（`02.06.03` 入边语境）。
- `MCDIgnore`（Service Guide Part 1）— **文档事实**：`ALL` 的语义排除 MCDIgnore 文件中 inactivated channel 对应的 site（参数表）。
- TPI — **文档事实**：文档声明 PACT 为 multisite 实现 `tpi` 接口，并建议改用 `tpi` 调用（源首段 Note）。

## 版本

**文档事实**（源 `Functional changes`）：Introduced before SmarTest 6.3.2。
**文档事实**：按本 wiki 规格，`Introduced before …` 是哨兵值，表示在文档集覆盖范围之前已存在，不应理解为 6.3.2 的变更。

## 出处

- `02_System_reference/02.06_Command_Reference/02.06.02.02.171_PACT__PACT__-__Parallel_ACTivities_control.htm`（主文档；语法、Application、Warnings、Errors、示例与 Functional changes 均出自该篇）。
- 关系核对：`02_System_reference/02.06_Command_Reference/02.06.02.02.121_EXSR_-__EXecute_SeaRch.htm`、`02.06.03_Pin_configuration_setup_commands.htm`、`02.06.03.01.01_Introduction.htm`（入边语境）。
