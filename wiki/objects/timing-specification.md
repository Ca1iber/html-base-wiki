---
type: object
title: Defining the timing specification
layer: file
stage: timing
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.05_Defining_the_timing_specification.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Defining the timing specification

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **3,892 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.06.01.05_Defining_the_timing_specification.htm>` 及其子主题 `<02_System_reference/02.06_Command_Reference/02.06.06.01.05.02_Changing_the_runtime_values_of_base_variables.htm>`、`<02_System_reference/02.06_Command_Reference/02.06.06.01.05.03.01_Global_and_local_scope_of_base_variables.htm>`、`<02_System_reference/02.06_Command_Reference/02.06.06.01.05.03_Multiport_timing_specifications.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example

The following is a simple example of a
`single-port timing specification`（raw: `55262.htm`）
:

```
EQNSET 1 "default"

WAVETBL "table1"
CHECK all

SPECSET 1 "sp1"

# SPECNAME *****ACTUAL***** *****MINIMUM**** *****MAXIMUM**** UNITS COMMENT
f 100 [MHz]
```

This specification uses spec set 1 for equation set 1. It will be identified to the firmware
commands by 101. The base variable f is set to 100. The
`CHECK all statement`（raw: `16942.htm`）
 activates all consistency checks (see
`Consistency checks for edge delays`（raw: `103991.htm`）
).

### Example（取自子主题 Changing the runtime values of base variables）

```
> SVLR? TIM, 1,1,all
< SVLR TIM,1,1,"per1",25
< SVLR TIM,1,1,"per2",50
> DSVS 11, "per", TIM,1,1
> BSVR 11,"per1",30
> BSVR 11,"per2",60
> SVLR? TIM, 1,1,all
< SVLR TIM,1,1,"per1",25
< SVLR TIM,1,1,"per2",50
> BSVE 11
> SVLR? TIM, 1,1,all
< SVLR TIM,1,1,"per1",30
< SVLR TIM,1,1,"per2",60
```

This
example shows how to change the values of the spec (base) variables
per1
 and

per2
 simultaneously by utilizing a spec value set. Note that the values only
change after
BSVE
 has been issued.

### Example（取自子主题 Multiport timing specifications）

The following multiport timing specification corresponds to the schema
above:

```
SPECIFICATION "MultSpec"
{
CHECK all

EQNSET 1 "equation set 1"
WAVETBL "wavetable A"
PORT Port1
SYNC
{
PHASE
SEQUENCE "gr1"
}
var 8

EQNSET 1 "equation set 1"
WAVETBL "wavetable B"
PORT Port2
SYNC
{
PHASE
SEQUENCE "gr2"
}
var 12

EQNSET 2 "equation set 2"
WAVETBL "wavetable B"
PORT Port3
SYNC
{
PHASE
SEQUENCE "gr2"
}
var 10
}
```

Note
the following points in this example:

The
PHASE
 flag is set for all three ports; the first port belongs to
sequencing group
gr1
, the other two to sequencing group
gr2.
 For the implications of this see
`Synchronizing vectors in a multiport setup`（raw: `104317.htm`）
.

A third possible option for the
SYNC
 block is
CLOCK

<
clock_group
>. For details see
`Avoiding rounding problems with different clock groups`（raw: `124792.htm`）
.

Port1
 and
Port2
 use the same equation set, but assign
different values to the base (spec) variable
var
.

The
CHECK all
 statement is placed before the first port block to indicate
that it is to be applied to all three ports.

If the variable
var
 is used to define the period length in timing set 1 of
equation set 1 and 2, then the common period resolution of all ports will be calculated as 4
ns, and the period for
port3
 will be auto-corrected from 10 ns to 12 ns.

`Multi-port burst labels`（raw: `105164.htm`）
 shows how this multiport timing specification can be
combined with a multiport vector setup.

### Example（取自子主题 Global and local scope of base variables）

The following example specification illustrates the
principle:

SPECIFICATION "mu_timing" {

CHECK
all

var 1.3

EQNSET 1 "equation
set 1"

WAVETBL "wavetable 1"

PORT
Port1

var 1.1

EQNSET 1 "equation
set 1"

WAVETBL "wavetable 2"

PORT
Port2

EQNSET 1 "equation set
1"

WAVETBL "wavetable 3"

PORT
Port3

}

In this example, which combines the same equation set with different wavetables for the three
ports, the global assignment 1.3 for the variable
var
 is valid for

Port2
 and
Port3
, but not for
Port1
, which
has the local assignment 1.1.

You can change the
runtime value (not the value in the specification) of the base variables with the
SVLR
 command. If you specify a port in the command, it will modify the
(create a) local assignment for that port. If you do not specify a port, a global assignment
will be created, or the existing global assignment modified.

Note that when a local
assignment is created with
SVLR
, the global assignment will no longer be
valid for the respective port. Thus if the above specification is the primary specification,
issuing the command

SVLR TIM,PRM,,"var@Port2",2.1

will
create an (internal) local assignment of 2.1 for
var
 in
Port2
.
If you subsequently change the global assignment with

SVLR
TIM,PRM,,"var",1.9

this will have no effect on
Port2
 (or
Port1
). Also, as before,
this change of the scope will not affect the specification, but only the runtime settings.

<!-- 语法节 end -->

## 是什么

**文档事实** 在 equation based timing 中，timing specification 把 wavetable 定义的 waveform shape 与 equation set 定义的 period length、edge delay 组合成一次测试的完整 timing；它同时包含一个 spec set，为 equation set 的 base variables 赋值，并规定要对 edge delays 执行哪些检查。

**文档事实** timing specification 文件位于 `<device_folder>/timing`，文件名可任意取，例如 `timingSpec1`。

**文档事实** 通常用 spec tool 定义 specification；如果要用 EQFS 或 EQSP 下载，必须按 timing setup file 中的编码原样提供。

**文档事实** `SVLR?` 可查询 base 与 derived（spec 与 equation）变量的当前值；`SVLR` 可修改 base variables 的 runtime 值（不是 spec set 中的定义），此时整个 timing equation system 会重新计算。

**文档事实** 本文档的子主题为 Consistency checks for edge delays、Changing the runtime values of base variables、Multiport timing specifications。

## 典型用法

**文档事实** 单端口示例：`EQNSET 1 "default"`、`WAVETBL "table1"`、`CHECK all`、`SPECSET 1 "sp1"`，再给 `f 100 [MHz]`。该 spec set 1 属于 equation set 1，固件命令用 101 标识；`CHECK all` 打开全部一致性检查。

**文档事实** 运行时修改 base variables 用 spec value set：`SVLR? TIM,1,1,all` 先读值，`DSVS` 建立 set，`BSVR` 写 `per1`/`per2`，`BSVE` 应用；在 `BSVE` 之前值不变。

**文档事实** 多端口示例用 `SPECIFICATION "MultSpec" { ... }` 包住多个 `PORT`；每个 port 指定 `EQNSET`、`WAVETBL`、`SYNC { PHASE SEQUENCE "grX" }` 与 `var`。`CHECK all` 放在首个 port 块之前即对所有 port 生效；示例中公共 period resolution 为 4 ns，port3 的 period 由 10 ns 自动修正为 12 ns。

**文档事实** global/local scope：顶层的 `var 1.3` 对未做 local 赋值的 Port2、Port3 有效，Port1 的 `var 1.1` 覆盖全局。`SVLR TIM,PRM,,"var@Port2",2.1` 会为该 port 创建 local assignment，之后修改全局 `var` 不再影响 Port2；这类修改只改变 runtime settings，不改 specification。

## 和谁有关

- **文档事实** `[[timing-equation-set]]` — equation set 的 SPECS 只声明 base variables、不给值，值在 timing specification 中指定；Timing equation set reference 与 Data organization 页都这样交叉引用本文档。
- **文档事实** `[[spec-set]]` — spec set 给 base variables 赋固定值；本文档示例用 `SPECSET 1 "sp1"` 赋值，Data organization 页说明 spec set 只存在于 timing specification 内。
- **文档事实** `[[wavetable]]` — timing specification 组合 wavetable 的 waveform shape 与 equation set 的 period/edge delay。
- **文档事实** `[[timing-file]]` — timing specification 是 `<device_folder>/timing` 下的文件内容；Data organization 页说明一个 timing setup file 可含多个 equation set、wavetable 与 timing specification。
- **文档事实** `[[eqfs]]`、`[[eqsp]]` — Related information 与正文都说明可用 EQFS/EQSP 下载 specification，且须按 timing setup file 的编码写法提供。
- **文档事实** `[[svlr]]` — Related firmware commands 段专门说明 `SVLR?` 查询、`SVLR` 运行时修改；子主题示例也用 SVLR/DSVS/BSVR/BSVE。
- **文档事实** `[[spec-tool]]` — 正文说 specification 通常用 spec tool 定义。
- **文档事实** 子主题 `Multiport timing specifications` 与 `Changing the runtime values of base variables` 是本页的下级主题，示例分别来自这两页。

## 版本

**文档事实** Functional changes 记载 “Introduced before SmarTest 6.3.2”。

## 出处

- `02_System_reference/02.06_Command_Reference/02.06.06.01.05_Defining_the_timing_specification.htm`，主源，含定义、文件位置、Related firmware commands、单端口示例、子主题与 Functional changes。
- `02_System_reference/02.06_Command_Reference/02.06.06.01.05.02_Changing_the_runtime_values_of_base_variables.htm`，运行时修改示例。
- `02_System_reference/02.06_Command_Reference/02.06.06.01.05.03_Multiport_timing_specifications.htm` 与 `02.06.06.01.05.03.01_Global_and_local_scope_of_base_variables.htm`，多端口与 global/local scope 示例。
