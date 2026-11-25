---
type: object
title: PSTE, PSTE? - (Parallel SiTe Enable)
layer: L1
stage: run
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.199_PSTE__PSTE__-__Parallel_SiTe_Enable.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# PSTE, PSTE? - (Parallel SiTe Enable)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,365 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.199_PSTE__PSTE__-__Parallel_SiTe_Enable.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### PSTE

```
PSTE {sites}
```

### PSTE?

```
PSTE? [STR]
```

returns

```
PSTE {sites|"site_string"}
```

### Parameters

[表]
行 1:
  sites
  The sites parameter is an integer that
    specifies the number of sites (to be) configured. The maximum is
    1024.
    
    For more information, refer to `Number of sites`（raw: `116532.htm#_116532__r_numberOfSites`） in
    `SmarTest system parameters - default values and limits`（raw: `116532.htm`）.
行 2:
  site_string
  A string consisting of "0" and "1". The length of the string corresponds to the
    number of the configured sites. The nth character of this
    string stands for site n.
    
    "0" indicates that the respective site uses a channel that is listed in the
    MCDIgnore file, and that this site therefore cannot be used for
    testing. "1" indicates that the site can be used.
行 3:
  STR
  If you specify this optional keyword in the query, PSTE? will return a site
    string.
    
    If this parameter is omitted, PSTE? will return the number of sites
    that are configured in the pin configuration.

### Example

```
> PSTE 3
```

This example configures three sites (site 1, site 2,
and site 3).

```
> PSTE? STR
< PSTE "101"
```

This example says that
three sites are configured, but that only two of them (site 1 and site 3) are available for
testing. Site 2 uses a channel that is listed in the
MCDIgnore
 file, and
therefore cannot be used for testing.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.199_PSTE__PSTE__-__Parallel_SiTe_Enable.htm>` 的 `## Errors` 段。**不是转述。**
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

Not all pins at the site have had their channels assigned by the
`PALS`（raw: `98680.htm`）
 command.

All channels are listed in the
MCDIgnore
 file and therefore not
available for testing.

<!-- 报错节 end -->

## 是什么

**文档事实** PSTE 定义 pin configuration 中要配置多少个 site；`sites` 是整数，最大 1024。配置的 site 不一定都能实际用于测试。

**文档事实** 若某个 site 使用的通道之一在 MCDIgnore 文件（服务指南第 1 部分）中被停用，该 site 就不能用于测试。

**文档事实** `PSTE?` 不带 `STR` 时返回 pin configuration 中已配置的 site 数；带 `STR` 时返回由 "0"/"1" 组成的 site 字符串，长度等于已配置 site 数，第 n 个字符对应 site n。`0` 表示该 site 使用了 MCDIgnore 中列出的通道因而不可测，`1` 表示可用。

**文档事实** 不要把 PSTE 的效果与 Site Control 窗口的 enabled 状态混为一谈：后者在固件中没有对应项。PSTE 决定 Site Control 窗口中显示多少个 site，而窗口中只有可用 site 才能被置为 enabled。

**文档事实** 该命令不支持 HV 模式下的 pin。

**文档事实** 文档把 multi-site 配置表述为「由 PALS 与 PSTE 命令定义」（DFPS 页）。

## 典型用法

**文档事实** `PSTE 3` 配置三个 site（site 1、site 2、site 3）。

**文档事实** `PSTE? STR` 返回 `PSTE "101"`，表示三个 site 已配置，但只有 site 1 与 site 3 可用于测试；site 2 使用了 MCDIgnore 文件中的通道。

**文档事实** 报错条件：某个 site 上并非所有 pin 都已由 PALS 分配通道；或所有通道都列在 MCDIgnore 中，因而没有可用于测试的通道。

**建议** 加载 pin configuration 后先用 `PSTE? STR` 读出可用 site 位图，再决定 site 数量、site 列表与并测策略；只看 `PSTE?` 的数字会把不可用 site 也算进去。

## 和谁有关

- **文档事实** [[pals]] —— PSTE 的报错条件之一是「site 上并非所有 pin 都已由 PALS 分配通道」；DFPS 页称 multi-site 配置由 PALS 与 PSTE 定义。
- **文档事实** [[stme]] —— 同属 `02.06.03` 的多 site 设置命令族 PACT、PALS、PQFC、PSFC、PSTE、STME。
- **文档事实** [[pqfc]] —— 加载 pin configuration 后 query focus 指向第一个可用 site（可能不是 site 1），可用 site 由 `PSTE? STR` 回复中的 "1" 表示。
- **文档事实** [[upas]] —— 其文档明写「A multisite setting is not performed with the PSTE command」，即 UPAS 的多 site 分配不走 PSTE。
- **文档事实** [[site-control-window]] —— PSTE 决定该窗口显示的 site 数；只有可用 site 能在窗口中被 enabled。
- **文档事实** [[dfps]] —— 其文档把 multi-site 配置归为 PALS 与 PSTE。
- **文档事实** MCDIgnore 文件 —— 决定哪些通道被停用、从而哪些 site 不可测；PSTE 的 Related information 指向「MCDIgnore usage and restrictions」。
- **文档事实** 用例文档 `03.02_How_to_do_Multi-Site_Testing` —— 多 site 测试用例章节。

## 版本

**文档事实** Functional changes 仅记「Introduced before SmarTest 6.3.2」，未列其他版本差异。

## 出处

- `02_System_reference/02.06_Command_Reference/02.06.02.02.199_PSTE__PSTE__-__Parallel_SiTe_Enable.htm` —— 主源：正文、Parameters、Note、Errors、Example、Related information、Functional changes。
- 其余跨页条目（PALS、PQFC、DFPS、UPAS、STME 命令族、03.02 用例）取自各页被 PSTE 引用的语境句，未整篇通读。
