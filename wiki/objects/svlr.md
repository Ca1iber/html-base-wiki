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

**文档事实**：SVLR 把 base（spec）variable 设为给定值，并重新计算 timing 或 levels。给定值必须落在相应 spec set 规定的 minimum 与 maximum 范围内；新值在下一个 functional test 开始时生效。

**文档事实**：SVLR 不改变 spec variable 的 setup value；做出新的修改时，之前的修改会被重置为 setup values。

**文档事实**：SVLR? 查询返回一个或多个 base 或 derived（spec 或 equation）variable 的当前 runtime value，或返回变量与 equation sets 之间的关联。

**文档事实**：spec_type 取 LEV（levels）或 TIM（timing）。equation_set_no 为 1–99，可用 PRM 表示 primary equation set（multi-port 下为 SPRM 定义的 primary specification），查询中可用 ALL。specset_no 为 1–99，查询中可用 ALL；未给 specset_no 时只返回 spec 名而不返回值。

**文档事实**：multi-port specification 在第三个参数给出 specification 名，此时第二个参数必须留空。spec_name 可用 `<spec_name>@<port_name>` 限定到某端口；这样修改后该端口的变量 scope 会变为 local（即使 setup 中为 global），直到 setup 再次下载。

**文档事实**：pinlist 参数可临时修改单个 pin 的 runtime definition，但 SVLR? 不能取回 pin-specific values。在另一个 spec variable 上做新修改时只保留最后一次修改，之前的 spec variable 会重置为 spec file 中的 setup value。要永久修改某个 spec variable，应把全部 pin（即 @）作为 pinlist；若要永久修改单个 pin 的值，则需为每个 pin 使用 specset 并在该 specset 中修改。

**文档事实**：CAUTION 指出，不应把 LEVEL_SPEC 或 TIMING_SPEC API 与非调试目的的 firmware 命令混用：这两个 test method API 会缓存值以支持 `.restore()`，而 firmware 层没有这种缓存。两种方式改 spec 值都不会改变 level 或 timing 文件；永久修改必须改对应的 setup 文件。

**文档事实**：SVLR 不会把 Test Program Explorer 置为 out of date，但会设置受影响 spec set 的 status bit 10；status bits 可用 SPST? 查询。

**文档事实**：该命令配置拥有 setup focus 的 sites（见 PSFC），同一时间只能有一个 site 在 focus。

**文档事实**：Application 段把 SVLR/SVLR? 的应用场景记为 testflow 中的 assign value node，并注明 multi-site 环境下每个 site 可设置自己的值。

## 典型用法

**文档事实**：Example 1 在同时存在 single-port 与 multi-port specifications 的 setup 中查询 spec variable f 的值：

```
> SVLR? TIM,ALL,ALL,"f"
< SVLR TIM,,"spec_p_1_p_2","f@p_1",35
< SVLR TIM,,"spec_p_1_p_2","f@p_2",33
< SVLR TIM,1,1,"f",37
```

**文档事实**：Example 2 查询 spec variable f 出现在哪些 equation sets；不返回数值：

```
> SVLR? TIM,ALL,,"f"
< SVLR TIM,1,,"f",
< SVLR TIM,2,,"f",
```

**文档事实**：Example 3 假设 primary timing 是含 p_1、p_2 两个端口的 multi-port specification，且两端口共享变量 f，f 对 p_1 的 scope 为 global。查询 p_1 的值、全局修改、再查询：

```
> SVLR? TIM,PRM,,"f@p_1"
< SVLR TIM,,"spec_p_1_p_2","f@p_1",33
> SVLR TIM,PRM,,"f",43
> SVLR? TIM,PRM,,"f@p_1"
< SVLR TIM,,"spec_p_1_p_2","f@p_1",43
```

**文档事实**：随后先做 local 修改，再尝试 global 修改：

```
> SVLR TIM,PRM,,"f@p_1",53
> SVLR TIM,PRM,,"f",43
> SVLR? TIM,PRM,,"f@p_1"
< SVLR TIM,,"spec_p_1_p_2","f@p_1",53
```

**文档事实**：第二次 global 命令无效，因为执行 local 命令后 f 只有 local scope。

**文档事实**：修改单点值的基本形式为 `SVLR {spec_type}, {equation_set_no}, {specset_no}, {"spec_name"}, {value} [,(pinlist)]`；文档给出的出错条件是 spec 不存在，或修改后的值违反 range、limit 等。

## 和谁有关

**文档事实**：以下关系均有本页正文或回链证据支撑。

- [[psfc]]：本页说明 SVLR 配置拥有 setup focus 的 sites，并直接链接 PSFC/PSFC?（Parallel Setup FoCus）。
- [[spst]]：本页说明 SVLR 会设置受影响 spec set 的 status bit 10，并可用 SPST? 查询。
- [[assign-value-node]]：本页 Application 段把 assign value node 列为 SVLR 的应用场景，并说明每个 site 可设自己的值。
- [[spec-set]]：SVLR/SVLR? 的 specset_no 指向 spec set；查询中 ALL 选择所有已定义的 specsets。
- [[level-spec]]、[[timing-spec]]：本页 CAUTION 直接提到 LEVEL_SPEC 与 TIMING_SPEC test method API，并比较其缓存行为与 firmware 层 SVLR 的差异。
- `List of level setup commands`（`02_System_reference/02.06_Command_Reference/02.06.05.02_List_of_level_setup_commands.htm`）：回链证据把 SVLR/SVLR? 列入 level setup 命令。
- `Global and local scope of base variables`（`02_System_reference/02.06_Command_Reference/02.06.06.01.05.03.01_Global_and_local_scope_of_base_variables.htm`）：本页参数说明 multi-port 下 spec variable 的 local/global scope 时直接链接该页。

## 版本

**文档事实**：本页 Functional changes 仅记载 Introduced before SmarTest 6.3.2——这是哨兵值，表示文档集覆盖范围之前已有，不能理解为 6.3.2 的新增或变更。

**文档事实**：本页 Functional changes 未记载任何后续版本变更，后续变更文档未覆盖。

## 出处

- 主源（「语法 / 参数」与「报错条件」的逐字来源）：`02_System_reference/02.06_Command_Reference/02.06.05.02.24_SVLR__SVLR__-__Spec_VaLues_at_Runtime.htm`（正文、单端口/多端口/两种 setup 的语法、Parameters、Application、Errors、Examples、Functional changes）。
