---
type: object
title: EDSP, EDSP? - (EDge SPecification)
layer: L1
stage: timing
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.102_EDSP__EDSP__-__EDge_SPecification.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# EDSP, EDSP? - (EDge SPecification)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **3,886 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.102_EDSP__EDSP__-__EDge_SPecification.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### EDSP

The
edge_spec
parameter specifies a
physical edge (d1 through d8 or r1 through
r8):

```
EDSP [waveform_set|specset_id|"multi-port_spec"], [timing_set], {edge_spec}, , ,[direction], {(pinlist)}
```

The

edge_spec
 parameter is a data parameter (D1, D2, C1, C2, E1, or
E2):

```
EDSP [waveform_set|specset_id|"multi-port_spec"], [timing_set], {edge_spec}, [dev_cyc_name], [dc_ref] ,[direction], {(pinlist)}
```

### EDSP?

```
EDSP? [dc_ref], {(pinlist)}
```

returns:

```
EDSP , , {edge_number}, , {dc_ref}, ,{(pinlist)}
```
[表] Parameters
行 1:
  waveform_set
  Specifies a waveform set number for a fixed timing setup.
行 2:
  specset_id
  Specifies a spec set ID for an equation based setup. The spec set ID is derived
    from an equation set number and a spec set number as follows:
    
    100 * equation_set_no + specset_no
行 3:
  multi-port_spec
  Specifies the name of a multiport specification for a multi-port setup.
    PRM is the default value.
行 4:
  timing_set
  Specifies the number of the a timing set. PRM is the default
    value.
行 5:
  edge_spec
  The edge specifier can either be a physical edge (d1 through d8 or r1 through r8),
    or one of the data parameters D1, D2, C1, C2 (drive parameters) or E1, E2 (receive
    parameters).
行 6:
  edge_number
  In the query reply, this parameter contains the edge that is used as leading or
    trailing edge.
行 7:
  dev_cyc_name
  Specifies the name of a logical device cycle that uses the data parameter given as
    the edge_spec. It must be defined for all pins in
    pinlist. If you do not enter a name in this parameter, the first device
    cycle in the device cycle table is used.
行 8:
  dc_ref
  This parameter specifies the input edge. The input edge determines the algorithm
    according to which the trailing edge is selected. The two options are LE
    (for "leading edge") and TE (for "trailing edge").
    
    The leading edge will always be the first edge that is associated with the specified data
    parameter within the specified device cycle, regardless of whether LE or
    TE is specified.
    
    For the trailing edge the following rules apply:
    
    When you specify LE, trailing and leading edge will be
    identical.
    
    When you specify TE, then drive parameters and receive parameters
    are treated differently.
    
    Drive parameter: The trailing edge will be the first drive edge after the
    leading edge thats performs a data or tri-state action. Note that this trailing edge
    need not be associated in any way with the data parameter of the leading edge.
    
    Receive parameter: If the action of the leading edge is an edge compare,
    leading and trailing edge will be identical. If it is the start action of a window
    compare, then the associated window close edge will be the trailing edge.
    
    For both cases, see the example below.
    
    In the query, you can also specify both. In this case both the
    leading and the trailing edge will be returned for the pins in
    pinlist.
行 9:
  direction
  This parameter can be in or out. If
    in is selected to define an input edge, then the edge_spec
    parameter must be D1, D2, C1, or C2. If out is selected to define a
    receiver edge, then the edge_spec parameter must be E1 or E2. If either
    in or out is selected along with an edge_spec
    parameter of 1,2...6, then a check is performed to ensure that the edges of all pins are in
    the required direction. If no entry is made in this parameter, the measuring edges of the
    pin in pinlist can have any direction or be unused.
行 10:
  pinlist
  The parameters of the EDSP command are applied to all pins named
    in this parameter. If more than one pin is used, the names must be separated by a comma.
    
    In a multi-port setup, all pins must belong to the same port of the specification that
    was entered as the first parameter.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.102_EDSP__EDSP__-__EDge_SPecification.htm>` 的 `## Errors` 段。**不是转述。**
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

The
edge_spec
parameter specifies a drive edge, but the

direction
parameter specifies a compare edge, or the other way
round.

Pins of different periods are included in the pin list.

You select an unused edge.

The edge direction of the selected edge is not the same for all pins in the pin list.

<!-- 报错节 end -->

## 是什么

**文档事实** EDSP（EDge SPecification）命令定义 timing search 所用的 search edge。概念上始终有两个 search edge，称为 leading edge 与 trailing edge；部分 AC test 使用 leading edge，另一些（例如 data hold time test）使用 trailing edge 作为 search edge。命令只指定其中一个，称为 input edge，另一个由 EDSP 推断。

**文档事实** input edge 可以显式指定，也可以由 data parameter 与 logical device cycle 的组合隐式指定；隐式方式要求 wavetable 使用 logical waveform。

**文档事实** 显式指定 input edge 时，leading 与 trailing edge 在物理上相同；用 data parameter 与 logical device cycle 定义时，EDSP 通常会为 leading 与 trailing 选出不同的物理 edge。

**文档事实** EDSP? 查询返回当前设置。

**文档事实** 命令配置拥有 setup focus 的 site；同一时刻只有一个 site 处于 focus，SmarTest 只在 Testflow Editor 与 result tools 中显示该 site 的结果，firmware query 也只报告该 site 的 setup 与结果（见 PSFC）。

**文档事实** 第一个参数三选一：waveform_set（fixed timing 的 waveform set 号）、specset_id（equation based setup，specset_id = 100 × equation_set_no + specset_no）或 `"multi-port_spec"`（multi-port setup 的 specification 名称，PRM 为默认值）；timing_set 默认值也是 PRM。

**文档事实** edge_spec 可以是物理 edge（d1 到 d8 或 r1 到 r8），也可以是 data parameter：D1、D2、C1、C2 为 drive parameter，E1、E2 为 receive parameter。

**文档事实** dc_ref 指定 input edge，决定 trailing edge 的选取算法，取 LE（leading edge）或 TE（trailing edge）。leading edge 始终是指定 device cycle 内与该 data parameter 关联的第一个 edge，无论选 LE 还是 TE。选 LE 时 trailing 与 leading 相同；选 TE 时 drive 与 receive 参数分别处理：drive 的 trailing edge 是 leading edge 之后第一个执行 data 或 tri-state 动作的 drive edge（该 edge 不必与 leading 的 data parameter 有关联），receive 的 leading 若为 edge compare 则两者相同、若为 window compare 的 start action 则关联的 window close edge 为 trailing edge。query 可同时指定两者，此时返回 leading 与 trailing。

**文档事实** direction 取 in 或 out：in 定义 input edge 时 edge_spec 必须为 D1、D2、C1、C2；out 定义 receiver edge 时 edge_spec 必须为 E1、E2；若 in/out 与编号 edge（1..6）一起使用，则检查所有 pin 的 edge 是否处于要求方向；若该参数留空，pinlist 中 pin 的 measuring edge 可为任意方向或未使用。

**文档事实** 在 multi-port setup 中，pinlist 的所有 pin 必须属于第一个参数所给 specification 的同一 port。

**文档事实** 源页在 dc_ref 与 direction 的描述中两处写 “see the example below”，但本页源文件没有独立的 Example 段。

## 典型用法

**文档事实** 指定物理 edge 的形式：`EDSP [waveform_set|specset_id|"multi-port_spec"], [timing_set], {edge_spec}, , ,[direction], {(pinlist)}`，其中第 4、5 个参数留空。

**文档事实** 指定 data parameter 的形式：`EDSP [waveform_set|specset_id|"multi-port_spec"], [timing_set], {edge_spec}, [dev_cyc_name], [dc_ref], [direction], {(pinlist)}`。

**文档事实** 查询形式：`EDSP? [dc_ref], {(pinlist)}`，返回 `EDSP , , {edge_number}, , {dc_ref}, ,{(pinlist)}`；`edge_number` 是实际用作 leading 或 trailing 的 edge。

**文档事实** `dev_cyc_name` 指定使用该 data parameter 的 logical device cycle 名，必须对 pinlist 中所有 pin 都已定义；若省略，则使用 device cycle 表中的第一个 device cycle。

**文档事实** 用 `direction` 做方向校验：in 只接受 D1/D2/C1/C2，out 只接受 E1/E2；与编号 edge 一起用时检查 pinlist 中所有 pin 的 edge 是否处于要求的方向。

**文档事实** 查询时 `dc_ref` 可写 LE、TE 或两者；写两者时返回 leading 与 trailing 两个 edge。

**推断** 由于 query 会返回实际选中的 `edge_number`，可用 `EDSP?` 核对 EDSP 对 trailing edge 的推断结果，尤其是在 drive/receive 与 window compare 场景下。源页没有给出可直接套用的数值示例。

**文档事实** 报错条件包括：edge_spec 指 drive edge 但 direction 指 compare edge（或反之）、pinlist 混入不同 period 的 pin、选择了未使用的 edge、所选 edge 的方向在 pinlist 各 pin 上不一致。

## 和谁有关

- **文档事实** `[[psfc]]` — 主源说明本命令配置拥有 setup focus 的 site，并在同段链到 PSFC（Parallel Setup FoCus）；两者的 site focus 语义一致。
- **文档事实** `02_System_reference/02.06_Command_Reference/02.06.02.02.100_EDDC__-__EDge_in_Device_Cycle.htm` — 该页 Note 称 EDDC? 查询与 EDSP 的定义完全独立，而 EDSP 决定 timing search 的 leading 与 trailing search edge（objpack 入边）。
- **文档事实** `02_System_reference/02.06_Command_Reference/02.06.02.02.291_TTRS__-__Time_TRansition_Search.htm` — 该页称 search 所用 edge 由 EDSP/EDSP? 选择，且 EDSP 选出的 edge 必须一致：对 pin list 中所有 pin 使用相同的 edge number、edge type 与 edge direction（objpack 入边）。
- **推断** `[[etim]]`、`[[etds]]` — EDSP 的 edge_spec 引用物理 edge 编号（d1..d8、r1..r8）与 timing set，而 edge 的位置由 edge timing 命令定义（ETIM/ETDS 页）；EDSP 主源本身没有直接链接这两个命令，故此关系标为推断。
- **文档事实** `02.06.02.02_List_of_commands.htm` 与 `02.06.01.05_Site_dependent_firmware_commands.htm` — 这些页面列出 EDSP、EDSP?（objpack 入边）。
- **文档事实** Application 段只有 AC Tests 一项；源页未给出更具体的 AC test 名称，也未列出独立的 AC test 文档。

## 版本

**文档事实** Functional changes 记：`Introduced before SmarTest 6.3.2`。

## 出处

- `02_System_reference/02.06_Command_Reference/02.06.02.02.102_EDSP__EDSP__-__EDge_SPecification.htm`，主源，含首段、两种 EDSP 形式、EDSP? 形式、参数表、Application、Errors 与 Functional changes（无 Example 段），已用 `show.py` 与 `objpack.py` 读取。
- `02_System_reference/02.06_Command_Reference/02.06.02.02.118_ETIM__ETIM__-__Edge_TIMing.htm` 与 `02.06.02.02.117_ETDS__ETDS__-__Edge_Timing_Definition_String.htm`，用于核对物理 edge 与 timing set 的定义来源（推断关系），已用 `show.py` 读取。
- EDDC、TTRS 与命令总表的引用语境取自 `extract/objpack.py` 的 `edges.jsonl`。
