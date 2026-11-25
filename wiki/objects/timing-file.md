---
type: object
title: Data organization of equation based timing
layer: file
stage: timing
tags: []
related: []
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.04.03.01_Data_organization_of_equation_based_timing.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.04.04_Example_of_the_equation_based_timing_setup_file.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Data organization of equation based timing

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **6,314 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.04.03.01_Data_organization_of_equation_based_timing.htm>` 及其子主题 `<02_System_reference/02.06_Command_Reference/02.06.06.01.03.01_Defining_waveform_shapes_for_Pin_Scale_standard_pins.htm>`、`<02_System_reference/02.06_Command_Reference/02.06.06.01.03.02_Defining_waveform_shapes_for_Smart_Scale_pins.htm>`、`<02_System_reference/02.06_Command_Reference/02.06.06.01.05.02_Changing_the_runtime_values_of_base_variables.htm>`、`<02_System_reference/02.06_Command_Reference/02.06.06.01.05.03_Multiport_timing_specifications.htm>`、`<02_System_reference/02.06_Command_Reference/02.06.06.01.05_Defining_the_timing_specification.htm>`、`<02_System_reference/02.06_Command_Reference/02.06.07.01.08.03.01_Changing_the_timing_set__CTIM.htm>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.04.03.01.01_Multiport_timing_specifications.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example

The following figure exemplifies the structure of equation based timing by a schematic
setup:

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

### Example（取自子主题 Defining the timing specification）

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

### Example（取自子主题 Changing the timing set (CTIM)）

The example:

```
SQPG 0,STVA,0,,(@)
....
SQPG 4,CTIM,2,,(@)
SQPG 5,GENV,400,,(@)
SQPG 6,CTIM,1,,(@)
SQPG 7,GENV,200,,(@)
SQPG 8,STOP,,,(@)
```

changes
the timing to set 2 at the start of the test before the device is initialized. At the end of
vector 400 the timing is changed to set 1.

For binning tests, the
CTIM

instruction allows you to change to the primary timing set as shown in the following listing:

```
SQPG 0,STVA,0,,(@)
SQPG 1,STSA,,,(@)
....
SQPG 4,CTIM,2,,(@)
SQPG 5,GENV,400,,(@)
SQPG 6,CTIM,PRM,,(@)
SQPG 7,GENV,200,,(@)
SQPG 8,STOP,,,(@)
```

Each
time you execute a functional test with this test sequence, the timing is changed to the primary
timing set. If you use the
`SPRM`（raw: `98742.htm`）
 command to change the primary set
for each test run, you can repeat the test and vary the parameters without changing your
setup.

### Example（取自子主题 Defining waveform shapes for Pin Scale standard pins）

```
WAVETBL "std"

PINS IN1
0 "d1:0" ZERO
1 "d1:0 d2:1 d3:0" ONE

PINS O1
0 "r1:L" LOW
1 "r1:H" HIGH
```

ZERO

and
ONE
 are the names for the waveforms 0 and 1 for pin

IN1
. These names will be displayed by the Pattern Debug tool.

### Example（取自子主题 Defining waveform shapes for Smart Scale pins）

The following example shows a wavetable fragment for a Smart Scale pin in its native
format:

```
WAVETBL "wavetable 1"

PINS DS0
0 "10" "0." 110
1 "101" "0.." 101

PINS DS1
0 "0" "0" 0

PINS Q0
0 "XXL" "..." XXL
1 "HLH" "..." HLH
2 "XLH" "..." XLH
3 "H.H" "10." HCMP

PINS IO1
TTMODE X4
0 "...." "...." "LHLH" LHLH
1 "...." "...." "XLXH" XLXH
2 "0110" "0..." "XXXX" 0110
```

The
dots stand for "no action".

If you retrieve these definitions with

WFDS?
, the reply will look as
follows:

```
> wfds? 101,all,,(DS0)
< WFDS 101,0,,"f1:1 f2:0 s1:0",(DS0)
< WFDS 101,1,,"f1:1 f2:0 f3:1 s1:0",(DS0)

> wfds? 101,all,,(DS1)
< WFDS 101,0,,"f1:0 s1:0",(DS1)

> wfds? 101,all,,(Q0)
< WFDS 101,0,,"r1:EX r2:EX r3:E0",(Q0)
< WFDS 101,1,,"r1:E1 r2:E0 r3:E1",(Q0)
< WFDS 101,2,,"r1:EX r2:E0 r3:E1",(Q0)
< WFDS 101,3,,"r1:W1 r2:WC r3:E1",(Q0)

> wfds? 101,all,,(IO1)
< WFDS 101,0,,"r1:E0 r2:E1 r3:E0 r4:E1",(IO1)
< WFDS 101,1,,"r1:EX r2:E0 r3:EX r4:E1",(IO1)
< WFDS 101,2,,"f1:0 f2:1 f3:1 f4:0 s1:0 r1:EX r2:EX r3:EX r4:EX",(IO1)
```

Note
that waveform 3 for pin
Q0
 contains a window compare. Note also that the
waveforms are returned in the modified standard format although they are coded in the pure Smart
Scale format in the wavetable.

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
