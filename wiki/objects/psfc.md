---
type: object
title: PSFC, PSFC? - (Parallel Setup FoCus)
layer: L1
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.191_PSFC__PSFC__-__Parallel_Setup_FoCus.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# PSFC, PSFC? - (Parallel Setup FoCus)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,556 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.191_PSFC__PSFC__-__Parallel_Setup_FoCus.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### PSFC

```
PSFC {site|"site_string"|ALL}
```

### PSFC?

```
PSFC? [STR]
```

returns

```
PSFC {"site_string"|ALL}
```

### Parameters

[表]
行 1:
  site
  A single integer representing the site number.
行 2:
  site_string
  A string of characters ("0" or "1"). The length of the string
    corresponds to the number of the configured sites. The
    nth character of this string
    stands for site n.
    
    1 means that the site is (to be) addressed by any
    subsequent commands that take the setup focus into
    account.
    
    0 means that the site is not (to be) addressed by any
    subsequent commands.
    
    If some of the sites that are required to get the setup focus are
    not available (because they use a channel that is inactivated in
    the MCDIgnore file) the setup status of
    these sites will not be changed.
行 3:
  ALL
  In the command, this means that all sites that are available for testing
    (that is, do not use a channel that is inactivated in the MCDIgnore
    file) are to be addressed by subsequent (setup focus aware) commands.
    
    ALL is returned in the query reply, if the query is issued without the
    STR parameter, and if all available sites have the setup focus.
行 4:
  STR
  forces the query to return a site string even if all available sites
    have the setup focus. This can be used to check if some sites are not available.

### Example

```
PSFC "11111110"
```

In this example, 8 sites are defined. The

PSFC
 command unsets the setup focus for the last site. The setup data of
this site will not be changed by any subsequent command execution.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.191_PSFC__PSFC__-__Parallel_Setup_FoCus.htm>` 的 `## Errors` 段。**不是转述。**
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if not all pins at the site have had their channels assigned by the

PALS
 command.

<!-- 报错节 end -->

## 是什么

**文档事实**：`PSFC` 把 setup 数据的修改限制在可用 site 的一个真子集上——它为各个 site 设置或取消 setup focus；默认所有 site 都拥有 setup focus。`PSFC?` 查询当前拥有 setup focus 的 site。

**文档事实**：并非所有 setup 命令都遵守 setup focus。timing 和 level 的 setup 命令遵守；大多数 vector setup 命令不遵守，但 `VECD` 与 `VECC` 是例外。

**文档事实**：源文的 CAUTION 指出，直接使用 `PSFC` 可能使 site control 窗口显示的 site active/inactive 信息不正确，从而让原本以为 inactive 的 site 被 site control 固件命令更新，造成不期望的结果甚至损坏；正常应通过 site control 窗口或 test method API 做 site control。

**文档事实**：pin configuration 中配置的 site 不一定都可用于测试；若某 site 使用在 MCDIgnore 文件中被停用的 channel，则该 site 不能用于测试。参数说明补充：若需要取得 setup focus 的 site 中有不可用的，这些 site 的 setup 状态不会被改变；`ALL` 也只覆盖可用 site。

**文档事实**：源文 `Application` 段把用途标为 site control window；`Related information` 指向 MCDIgnore usage and restrictions。

**推断**：因此 `PSFC` 是 site 级「写作用域」开关，不是 site 激活/屏蔽开关；它不改变 site 是否可用。

## 典型用法

**文档事实**：源文示例是 `PSFC "11111110"`：定义了 8 个 site，site string 最后一位为 0，命令取消最后一个 site 的 setup focus；之后任何命令执行都不会改变该 site 的 setup 数据。

**文档事实**：`PSFC ALL` 把所有可用于测试的 site 纳入后续遵守 setup focus 的命令；`PSFC?` 返回 site string 或 `ALL`；加 `STR` 可强制返回 site string，即使所有可用 site 都有 focus，用于检查是否有 site 不可用。

**文档事实**（`02.06.03.01.10.02`）：一个典型应用是断开单个 site——先用 `PSFC` 把 setup focus 限制到该 site，再用 disconnect sequence 对应的固件命令断开。`03.04.01.03.02` 写明 SmarTest 会在用户自定义 disconnect sequence 前自动加一条 `PSFC` 来定义 site focus。

**文档事实**（`03.02.02.06.08`）：编程提示可用用户过程或 test method 在 `RLYC` 之前用 `PSFC` 只选已使能 site，随后切回 `PSFC ALL`，以替代 `FW_escape` 命令。

**建议**（转述源文 CAUTION）：不要绕过 site control 窗口或 test method API 直接随意下发 `PSFC`；先确认窗口状态与实际 focus 一致。

## 和谁有关

- **`PALS`**：报错条件写明，若 site 上并非所有 pin 的 channel 都已由 `PALS` 分配，`PSFC` 会报错——`PSFC` 之前必须先完成通道分配。（文档事实）
- **遵守 setup focus 的 timing/level setup 命令与 `VECD`/`VECC`**：源文点名它们遵守 setup focus，其余大多数 vector setup 命令不遵守；因此 `PSFC` 的实际影响面取决于后续下发的命令类型。（文档事实）
- **一批 setup 配置命令**：`DFTD`、`TPSP`、`UHCM`、`TTCF`、`JSCF`、`CFCF`、`PRCF`、`BSVR`、`JSWF`、`DFSP`、`ENSP`、`TORC`、`TORN`、`TOUD`、`TOCR`、`TSCF`、`TORR`、`DCEL`、`CLMP`、`DCCH`、`DCVH`、`DPSE`、`DPSR` 等页面的入边语境都写着「configure setups of those sites that have the setup focus」或「on all sites that have the setup focus (defined with PSFC)」。它们是 `PSFC` 的直接消费者。（文档事实）
- **`PQFC`**：`TOCF` 页面把 query focus 归给 `PQFC`，而 setup focus 由 `PSFC` 定义；两者成对出现于多 site 描述。**推断**：`PSFC` 管写、`PQFC` 管读，但本页没有解释两者交互，不能据此推断实机细节。
- **Site control window**：源文 `Application` 段指定 site control window 为用途场景；CAUTION 又说直接使用 `PSFC` 会让该窗口显示不正确。（文档事实）
- **MCDIgnore 文件**：它决定哪些 site 可用；不可用 site 的 setup focus 状态不会被改变，`ALL` 也不包含它们。（文档事实）
- **`PACT` / `PALS` / `PSTE` 等多 site 命令**：`02.06.03` 与 `02.06.03.01.01` 把 `PACT`、`PALS`、`PQFC`、`PSFC`、`PSTE`、`STME` 并列为 multi-site setup 命令。**推断**：同族但职责不同，`PSFC` 不负责激活 site。
- **disconnect 流程**：单 site disconnect 的典型做法以 `PSFC` 限定 focus；用户自定义 disconnect sequence 前也会自动插入 `PSFC`。（文档事实）

## 版本

**文档事实**：`Functional changes` 只写 “Introduced before SmarTest 6.3.2”，没有列出本命令的后续变更。

## 出处

- 主源：`02_System_reference/02.06_Command_Reference/02.06.02.02.191_PSFC__PSFC__-__Parallel_Setup_FoCus.htm`（正文、Parameters、Errors、Example、Application、Related information、Functional changes）。
- 关系证据：`extract/objpack.py` 入边，主要来自 `02.06.03.01.10.02`、`02.06.03.01.01`、`02.06.03`、`03.04.01.03.02`、`03.02.02.06.08`，以及上述各 setup 命令页。
