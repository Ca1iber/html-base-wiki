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

（待补）

## 典型用法

（待补）

## 和谁有关

（待补）

## 版本

（待补）

## 出处

（待补）
