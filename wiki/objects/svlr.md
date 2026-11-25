---
type: object
title: SVLR, SVLR? - (Spec VaLues at Runtime)
layer: L1
stage: level
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.24_SVLR__SVLR__-__Spec_VaLues_at_Runtime.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# SVLR, SVLR? - (Spec VaLues at Runtime)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **6,969 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.05.02.24_SVLR__SVLR__-__Spec_VaLues_at_Runtime.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### For single-port specifications

SVLR
```
SVLR {spec_type}, {equation_set_no}, {specset_no}, {"spec_name"}, {value} [,(pinlist)]
```

SVLR?

SVLR?
 {
spec_type
},
{
equation_set_no
}, [
specset_no
],
{"
spec_or_equ_name
"}
[,
MAX
|
MIN
|
UNIT
]

```
SVLR? {spec_type}, {equation_set_no}, [specset_no], {ALL|EQUA|MAX|MIN|SPEC|UNIT}
```

Both
query types
return:

```
SVLR {spec_type}, {equation_set_no}, [specset_no], {"spec_or_equ_name"}, [value]
```

### For multiport specifications

SVLR
```
SVLR {spec_type},, {"multi-port_spec"}, {"spec_name"|"spec_name@port_name"}, {value} [,(pinlist)]
```

SVLR?
```
SVLR? {spec_type},, {"multi-port_spec"}, {"spec_or_equ_name"|"spec_or_equ_name@port_name"} [,MAX|MIN|UNIT]
SVLR?{spec_type},, {"multi-port_spec"}, {ALL|EQUA|MAX|MIN|SPEC|UNIT}
```

Both
query types
return:

```
SVLR {spec_type},, {"multi-port_spec"}, {"spec_or_equ_name"|"spec_or_equ_name@port_name"}, [value]
```

### For both types of specifications

SVLR
```
SVLR {spec_type},PRM,, {"spec_name"|"spec_name@port_name"}, {value} [,(pinlist)]
```

SVLR?
```
SVLR? {spec_type},{ALL|PRM},[ALL|specset_no], {"spec_or_equ_name"|"spec_or_equ_name@port_name"} [,MAX|MIN|UNIT]
SVLR? {spec_type},{ALL|PRM},[ALL|specset_no], {ALL|EQUA|MAX|MIN|SPEC|UNIT}
```

Both
query types
return:

```
SVLR {spec_type},[equation_set_no], ["multi-port_spec"|specset_no], {"spec_or_equ_name"|"spec_or_equ_name@port_name"}, [value]
```

### Parameters

[表]
行 1:
  spec_type [跨 3 行]
  Which specification type to use. [跨 2 列]
    Use:
行 2:
  LEV
  to specify levels, or
行 3:
  TIM
  to specify timing.
行 4:
  equation_set_no
  Equation set number. An integer [跨 2 列]
    in the range 1 to 99.
    
    Use PRM to specify the primary equation set, or, in a multi-port
    setup, the primary specification as defined with SPRM. In this case, the
    specset_no parameter is ignored.
    
    In the query, use ALL to display all equation sets.
    
    This parameter must be omitted if a multi-port specification is specified for the
    thirdparameter.
行 5:
  specset_no
  Specset number. An integer in [跨 2 列]
    the range of 1 to 99. In the query, use ALL to select all defined
    specsets.
    
    If specset_no is not set, and equation_set_no is
    set to ALL or a number, only the spec names in the specified equation
    sets, but no values are returned.
行 6:
  multi-port_spec
  In a multi-port setup, enter the [跨 2 列]
    name of a specification instead of a spec set number. In this case, the secondparameter
    must be left empty.
行 7:
  spec_name
  The name of a base (spec) [跨 2 列]
    variable. In a multi-port setup, the same variable name can occur among the spec variables
    of more than one port within the same specification. In this case, you can qualify the
    variable name by a port name in the following format
    
    <spec_name>@<port_name>,
    
    if you want to modify the variable on that port only.
    
    Note, however, that the scope of the variable will be set to local for the port in
    question after such a modification (even if it is set to global in the setup), until the
    setup is downloaded again.
    
    Note also that in a multi-port setup, you cannot change the value of a variable globally
    (that is, without specifying a port) unless at least one of the variable instances has its
    scope set to global in the setup. For basic information on the local and global scope of
    spec variables in a multi-port setup see `Global and local scope of base variables`（raw: `58766.htm`）.
行 8:
  spec_or_equ_name
  The name of a base (spec) or [跨 2 列]
    derived (equation) variable. An equation variable cannot be specified in the command or in
    a query which uses the extra parameter.
行 9:
  ALL
  Requires that the actual values [跨 2 列]
    of both base and derived variables are returned.
行 10:
  EQUA
  Requires that the actual values [跨 2 列]
    of only the derived (equation) variables are returned.
行 11:
  MAX
  Requires that the maximum values [跨 2 列]
    of all the base (spec) variables are returned.
    
    This keyword can also be specified as an extra parameter in combination with the
    spec_name parameter to retrieve only the maximum value of the specified
    spec variable.
行 12:
  MIN
  Requires that the maximum of all [跨 2 列]
    the base (spec) variables are returned.
    
    This keyword can also be specified as an extra parameter in combination with the
    spec_name parameter to retrieve only the minimum value of the specified
    spec variable.
行 13:
  SPEC
  Requires that the actual values [跨 2 列]
    of only the base (spec) variables are returned.
行 14:
  UNIT
  Requires that the units of all [跨 2 列]
    the base (spec) variables are returned.
    
    This keyword can also be specified as an extra parameter in combination with the
    spec_name parameter to retrieve only the unit of the specified spec
    variable.
行 15:
  value
  Float with 5 possible decimal [跨 2 列]
    places.
行 16:
  pinlist
  By this extra parameter, you can [跨 2 列]
    modify the runtime definitions for an individual pin. Note that you cannot retrieve
    the pin specific values with SVLR?.
    
    Note You can use the pinlist parameter to modify the value
    of a spec variable of an individual pin, temporarily. If you make a new modification
    on a different spec variable, only the last modification is kept while the previous spec
    variable is reset to the setup value defined in the spec file. To make a permanent
    modification on a spec variable, specify all pins (that is, @) as the
    pinlist. Otherwise, to change the value of a spec variable of an
    individual pin permanently, you have to use a specset for each pin and modify the spec
    variable in that specset.

### Examples

### Example 1

The following example queries the values of the spec variable
f in a setup where both single-port and multi-port specifications
occur:

```
> SVLR? TIM,ALL,ALL,"f"
< SVLR TIM,,"spec_p_1_p_2","f@p_1",35
< SVLR TIM,,"spec_p_1_p_2","f@p_2",33
< SVLR TIM,1,1,"f",37
```

### Example 2

The next example queries in which equation sets the spec
variable
f

occurs:

```
> SVLR? TIM,ALL,,"f"
< SVLR TIM,1,,"f",
< SVLR TIM,2,,"f",
```

### Example 3

For this example assume that the primary timing is a
multi-port specification which contains the two ports p_1 and p_2, and that p_1 and p_2 share
the spec variable f in this specification. Assume further that f has been set to scope global
for the port p_1. Now query the current value of f for p_1, change it globally, and query it
again:

```
> SVLR? TIM,PRM,,"f@p_1"
< SVLR TIM,,"spec_p_1_p_2","f@p_1",33
> SVLR TIM,PRM,,"f",43
> SVLR? TIM,PRM,,"f@p_1"
< SVLR TIM,,"spec_p_1_p_2","f@p_1",43
```

Since
f is global for p_1, its value has been modified. Now change the value a second time, but this
time locally, and then try to change it globally
again:

```
> SVLR TIM,PRM,,"f@p_1",53
> SVLR TIM,PRM,,"f",43
> SVLR? TIM,PRM,,"f@p_1"
< SVLR TIM,,"spec_p_1_p_2","f@p_1",53
```

The
second global command has no effect because f has only local scope after issuing the local
command.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.05.02.24_SVLR__SVLR__-__Spec_VaLues_at_Runtime.htm>` 的 `## Errors` 段。**不是转述。**
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

The spec does not exist.

The change to the spec's value results in violations of range, limit, etc.

<!-- 报错节 end -->

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
