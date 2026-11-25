---
type: object
title: Timing equation set reference
layer: file
stage: timing
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.02.01_Timing_equation_set_reference.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Timing equation set reference

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

**没有加标记的语法段。** 定义文档里没有 `Syntax` / `Parameters` / `Example`
这类**段标记**。本脚本一个字都不收录——没有段标记时「哪一段是语法」是猜，
而猜就是编。要看原文：`python show.py <分类号>`。

<!-- 语法节 end -->

## 是什么

**文档事实** 本页是 timing equation set 的文件结构参考。equation set 由以下头部标识：

`EQNSET <equation_set_number> [["]<equation_set_description>["]]`

**文档事实** equation_set_number 是大于 0 的数，在 timing setup file 内标识 equation set；一个 setup file 最多可定义 256 个 timing equation set；description 可选、最多 60 字符，含空格时须用双引号，不允许分号。

**文档事实** 一个 timing equation set 按以下顺序包含：

1. 可选 `MODECONTEXT "<mode_context>"`；未定义时假定为 default mode context，即所有 pin 配置为标准 pin。
2. 可选 `DEFINES <port_1> [<port_2> ... <port_n>]`；SmarTest 用它检查 equation set 是否为指定 ports 的所有 pins 提供所需信息。
3. 可选 SPECS 基变量（spec 变量）列表；变量只在这里声明、不赋值，值在 timing specification 中指定；方括号中的单位可选且仅用于 spec tool 显示；变量名大小写敏感；变量名不得以 level 或 timing setup 文件的关键字开头，文档列出的关键字有 ADJUST、LEVELSET、period_res、CHECK、master_clock、SPECIFICATION、CLKSET、MODECONTEXT、SPECS、clockSrc、MODULATION、SPECSET、DEFINES、PDC、SYNC、DPSPINS、PHYDVCTBL、TIMINGSET、EQNSET、PINS、v3_delay_register_value、EQUATIONS、PORT、WAVETBL、fract、period_div。
4. 可选 EQUATIONS 派生变量（equation 变量）定义；形式为 `var_name = expression`，表达式可引用基变量和已定义的派生变量；基变量与派生变量总数最多 4096。
5. 可选 master clock period（仅 Smart Scale）、tester period resolution 与 clock source；period_res 可用常量或表达式；clocksrc 取 INT（内部时钟，默认）或 AMC（alternate master clock）；master clock period 在 SmarTest 7.10 固定，多个 clock domain 应使用不同 period_res。
6. 强制的一个或多个 timing set；timing set 号在给定 equation set 内对所有 timing set 计数，用表达式为 edge 赋 delay 与 period。

**文档事实** timing set 通用格式为 `TIMINGSET <timing_set_number> [["]<timing_set_description>["]]`，随后是 `period = <expression>|fract(<spec_var1>,<spec_var2>,<spec_var3>)`、`PINS <pin list> [-(<exclude pin list>)]`、可选 `period_div = <number>`，以及 `(f|s|d|r)<edge_no> = <expression>` 形式的 edge delay。d 是 Pin Scale card 的 drive edge，f 与 s 是 Pin Scale 9G card 的 drive edge，r 是两类 card 的 receive edge；edge 号从 1 起，drive 与 receive 各自最多 8。

**文档事实** 所有 equation set 与 waveform set 中所有 timing set 的总数上限由 DSCP 命令定义。

**推断** 本页描述 setup 文件语法而非可执行命令（与 frontmatter 的 layer: file 一致）。

## 典型用法

**文档事实** 用 `EQNSET <number> ["description"]` 在 timing setup file 中开始一个 equation set。

**文档事实** 在 SPECS 中声明基变量，例如 `f [MHz]`、`D [ns]`；单位只影响 spec tool 显示，没有其他作用。

**文档事实** 在 EQUATIONS 中用已声明变量定义派生变量，例如 `p = 1/f*1000`。

**文档事实** 用 `period_res = 4` 指定 period resolution；用 clocksrc 选择 INT 或 AMC。

**文档事实** 文档给出的 timing set 片段为 `TIMINGSET 1 "example"`、`period= p`、`PINS mode -( S0 )`、`d1= 0`、`d2= p/3`、`d3= p/2 + D`，表示对 pin group mode（排除 S0）定义 edge delay。

**文档事实** PINS 后可用 `period_div = <number>` 指定 Pin Scale fast pins 与 Smart Scale pins 的 edge 数。

**建议** SPECS 只声明变量而不赋值，实际数值应在 timing specification 中给出；equation set 中保持表达式与结构，便于按 spec 重用。

## 和谁有关

- **文档事实** Data organization of equation based timing，其页说 “For detailed reference information on equation sets see Timing equation set reference.”，把本页作为 equation sets 的详细参考。
- **文档事实** Specifying the Period Resolution，其页说 equation based timing 可在 equation set 中用 period_res 指定 period resolution，并参见本页；本页也定义 period_res。
- **文档事实** Mode contexts，本页 MODECONTEXT 指向该页；未定义 mode context 时使用 default mode context。
- **文档事实** Defining the timing specification，本页 SPECS 说明值在 timing specification 中赋，并链接该页。
- **文档事实** Pin exclusion，本页 PINS 的可选 exclude list 链接该页，该页也链接回本页；Pin exclusion 在 7.0.3 引入。
- **文档事实** Period divisor (period_div)，本页 period_div 语句链接该页，该页也链接回本页。
- **文档事实** Defining the global period 与 Setting the edge delays，本页 Related information 列出这两个主题。
- **文档事实** Avoiding rounding problems with the fract() function，本页 period 的 fract() 用法链接该页。
- **文档事实** Pin Scale standard pins、Smart Scale pins、Pin Scale 3600 fast pins 的 edge delay 页面，本页 d、f、s、r 与 period_div 的说明分别指向它们。
- **文档事实** DPSPINS 与 DPSPINS resources，本页关键字说明把不属于 timing equation set 的关键字指向这些 level setup 页面。
- **文档事实** DSCP，本页说所有 equation set 与 waveform set 的 timing set 总数上限由 DSCP 定义。
- **文档事实** Timing Equations - Reference、Level sets、Additional pin qualifier (diff)，这些页面在入边中链接本页作参考。

## 版本

**文档事实** Functional changes 记载 Introduced before SmarTest 6.3.2。

**文档事实** SmarTest 7.0.3：Pin exclusion introduced。

**文档事实** SmarTest 7.2.0：Obsoletes the soc_mts keyword。

**文档事实** 脚注记载 SmarTest 7.10 起 master clock 固定为 375 MHz。

**文档事实** 脚注说明 PDC、PHYDVCTBL、v3_delay_register_value 所属功能已废弃，但这些关键字仍不能使用。

## 出处

- `02_System_reference/02.06_Command_Reference/02.06.06.01.02.01_Timing_equation_set_reference.htm`，主源，含全文、Related information、脚注与 Functional changes。
- `02_System_reference/02.06_Command_Reference/02.06.06.01.02_Data_organization_of_equation_based_timing.htm`，上位主题，说明本页是 equation sets 的详细参考。
- `extract/edges.jsonl` 入边，用于 Specifying the Period Resolution、Pin exclusion、Period divisor、Mode contexts 等旁证。
