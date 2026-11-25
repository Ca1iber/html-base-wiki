---
type: object
title: WAVE, WAVE? - (WAVEform)
layer: L1
stage: timing
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.333_WAVE__WAVE__-__WAVEform.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# WAVE, WAVE? - (WAVEform)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **4,814 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.333_WAVE__WAVE__-__WAVEform.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### WAVE

```
WAVE {wvf_set}, {wfIndex}, [DD1], [DD2], [ED1], [ED2], {pwfIndex}, {(pinlist)}
WAVE {specset_id|"multiport_spec"}, {wfIndex}, [DD1], [DD2], [ED1], [ED2], {pwfIndex}, {(pinlist)}, ALLOW_EQ
```

### WAVE?

```
WAVE? {wvf_set|"wavetable_name"|specset_id|"multi-port_spec"}, {(pinlist)}
```

returns:

```
WAVE {wvf_set|"wavetable_name"|specset_id|"multi-port_spec"}, {wfIndex}, [DD1], [DD2], [ED1], [ED2], {pwfIndex}, {(pinlist)}
```

### Parameters

[表]
行 1:
  wvf_set
  Waveforms set number. Enter an [跨 2 列]
    integer in the range 1 to the maximum number of allowed waveform sets. The maximum number
    is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `98878.htm`）. For the query command you can also enter
    ALL for all waveform sets.
行 2:
  specset_id
  Derived as follows: [跨 2 列]
    
    100 * equation_set_no + specset_no
行 3:
  wavetable_name
  The wavetable name. Enter a [跨 2 列]
    string of up to 40 alphanumeric characters (upper or lower case) enclosed by double
    quotes.
行 4:
  multiport_spec
  To change or query a multiport [跨 2 列]
    specification, enter the name of the specification.
行 5:
  wfIndex
  Logical waveform index. This [跨 2 列]
    index identifies the logical waveform for which a physical waveform is to be created. The
    values specified for the DD1, DD2,
    ED1, and ED2 parameters must be in accordance with
    the format of this logical waveform.
行 6:
  DD1 and [跨 9 行]
    DD2
  First and second drive data [跨 2 列]
    parameter. These are optional parameters and contain values for both drive data and
    tri-state. The values you can define are:
行 7:
  F0N
  drive 0
行 8:
  F1N
  drive 1
行 9:
  FN0
  tri-state off
行 10:
  FNZ
  tri-state on
行 11:
  F00
  drive 0, tri-state off
行 12:
  F0Z
  drive 0, tri-state on
行 13:
  F10
  drive 1, tri-state off
行 14:
  F1Z
  drive 1, tri-state on
行 15:
  ED1 and [跨 9 行]
    ED2
  First and second receive data [跨 2 列]
    parameter. These are optional parameters. The values you can define are:
行 16:
  F0
  compare to 0
行 17:
  F1
  compare to 1
行 18:
  FI
  compare to intermediate
行 19:
  FX
  compare to mask
行 20:
  FU
  compare to unstable
行 21:
  C
  capture digital data
行 22:
  D
  do not capture digital data
行 23:
  The values C [跨 2 列]
    and D are used for selective digital capture. The following rules apply
    to these values:
    
    A waveform that is used for selective digital capture cannot contain more than one
    compare action. Therefore, if you specify C or D for
    one of ED1 or ED2, you cannot specify a value for
    the other Expected Data parameter.
    
    If you issue more than one instance of the WAVE command for the same
    logical waveform, the values you specify for the same Expected Data parameter in these
    different WAVE instances must be homogeneous; that is, either all or
    none of them must be C or D. You cannot, for
    instance, set ED1 to C in one of these WAVE instances, and set it to F1 in another.
行 24:
  pwfIndex
  Physical waveform index. Enter [跨 2 列]
    an integer between 0 and 31 (0 and 255 on the Pin Scale Digital systems) for each physical
    waveform . The index is stored in the vector area and references the physical waveform in
    the physical waveform table.
行 25:
  pinlist
  The name of the pin or pins for [跨 2 列]
    which physical waveform states are to be defined or read back. This parameter can also
    include groups previously created by `DFGP, DFGP? - (DeFine GrouP)`（raw: `98546.htm`）. The symbol
    @ can be used to specify all configured pins. If more than one pin is
    to be included, the names must be separated by commas.
行 26:
  ALLOW_EQ
  This extra parameter allows you [跨 2 列]
    to define physical waveforms for an equation based timing. Note that only the runtime
    settings are affected; the definitions in the wavetable are not changed.
    
    Note also the following:
    
    Every runtime change will affect all specifications that use the respective
    wavetable.
    
    Since the new waveform must be evaluated and downloaded for every specification that
    uses the respective wavetable, the change tends to be rather slow.
    
    The runtime definitions are not checked for consistency. It is up to the user to
    ensure this.

### Example

```
> WFDS 1,2,,"d1:D11 d3:0 d4:C11",(pin1,pin2,pin3,pin4)
> WAVE 1,2,F00,,,,4,(pin1,pin2,pin3,pin4)
> WAVE 1,2,F10,,,,5,(pin1,pin2,pin3,pin4)
```

This
example first defines a logical waveform with the index 2 for waveform set 1. The waveform uses
the data parameter
D11
, the fixed action
0
, and the
complement
C11
 of
D11
. Then two physical waveforms are
defined for logical waveform 2, which are referenced by the physical waveform DC/DC power units 4 and 5.
Waveform 4 drives to 0 at edge d1, to 0 at d3, and to 1 at d4. Waveform 5 drives to 1 at edge
d1, to 0 at d3, and to 0 at d4.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.333_WAVE__WAVE__-__WAVEform.htm>` 的 `## Errors` 段。**不是转述。**
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

wvf_set
 is greater than the range allowed by the
`WSUS`（raw: `98878.htm`）
 command.

The logical waveform index is outside the range of 0-31 (for P/C/Ce systems) or 0-255 (Pin
Scale systems).

The physical waveform index is outside the range of 0-31 (0-255 on the Pin Scale Digital
Cards).

You try to define a physical waveform for which no logical waveform exists. Define the
waveform first with (
`WFDS, WFDS? - (WaveForm Definition String)`（raw: `98872.htm`）
.

There is a mismatch of action between the data parameter in the
`WFDF`（raw: `98871.htm`）
 or
`WFDS`（raw: `98872.htm`）
 definition and the corresponding fixed action
as specified by
WAVE
.

You try to redefine a physical waveform for a waveform. Delete the waveform and any
associated physical waveforms first with
`WFUD - (WaveForm UnDefine)`（raw: `98875.htm`）
.

specset_id
 is invalid because
equation_set_no
,

specset_no
, or both are invalid.

specset_id
 does not reference a defined wavetable.

wavetable_name
 does not reference a defined wavetable.

<!-- 报错节 end -->

## 是什么

**文档事实**：WAVE 在 fixed timing 下定义一个 physical waveform：为某个 logical waveform 的 data parameter 指定具体取值，并给这组取值分配 physical waveform index（`pwfIndex`）。只有 physical waveform 会下载到硬件并由 sequencer 执行，因此每个 logical waveform 至少要发一条 WAVE，即使它不含任何 data parameter。

**文档事实**：logical waveform 中由固定状态给出的 drive / receive action 直接决定物理状态；由 data parameter 给出的部分则在 WAVE 中补齐——驱动侧用 `DD1`/`DD2`，接收侧用 `ED1`/`ED2`。文档的 Mode of operation 给出 data parameter 形式与允许的 fixed action 的对应表；若 logical waveform 不含 data parameter，WAVE 的 `DD1`…`ED2` 必须留空。

**文档事实**：`pwfIndex` 范围为 0–31（Pin Scale Digital 系统为 0–255），该索引存入 vector 区并引用 physical waveform 表。WAVE 也可为 equation based timing 创建 physical waveform 的运行时定义（第二语法形式带 `ALLOW_EQ`，只影响 runtime，不改 wavetable）。

**文档事实**：对同一 logical waveform 的多条 WAVE，同一 Expected Data 参数在不同实例中的 `C`/`D`（selective digital capture）取值必须同质：要么全为 C/D，要么全不为；且用于 selective digital capture 的波形最多只能有一个 compare action。

**推断**：由此 WAVE 与 WFDS/WFDF 构成"logical waveform 定义 / physical waveform 落地"两级分工，WAVE 是让波形真正可被 sequencer 执行的一步；文档"Only physical waveforms are downloaded to the hardware"直接支持这一分工。

## 典型用法

**文档事实**：文档示例先用 `WFDS 1,2,,"d1:D11 d3:0 d4:C11",(pin1,pin2,pin3,pin4)` 为 waveform set 1 定义 logical waveform 索引 2（使用 DD1、固定 0、DD1 的补码 C11），再用 `WAVE 1,2,F00,,,,4,(pin1,pin2,pin3,pin4)` 与 `WAVE 1,2,F10,,,,5,(pin1,pin2,pin3,pin4)` 定义两个 physical waveform：4 号在 d1/d3 驱动 0、d4 驱动 1；5 号在 d1 驱动 1、d3/d4 驱动 0。

**文档事实**：查询语法为 `WAVE? {wvf_set|"wavetable_name"|specset_id|"multi-port_spec"}, {(pinlist)}`，返回 physical waveform 定义；`wvf_set` 也可写 `ALL`。

**文档事实**：`wvf_set` 的上限由 `WSUS` 决定；`pinlist` 可使用 `DFGP` 定义的组，`@` 表示全部已配置引脚。

**建议**：重定义已存在的 physical waveform 前先用 `WFUD` 删除原 waveform 及其关联 physical waveform；WAVE 的 Errors 段明确把"重定义已有 physical waveform"列为报错条件。

## 和谁有关

- `WFDS` / `WFDF`：**文档事实**——WAVE 的 Prerequisites 要求待建 physical waveform 的 logical waveform 已由 WFDS 或 WFDF 定义；Errors 段也把"为不存在的 logical waveform 定义 physical waveform"列为报错，并要求先用 WFDS 定义。
- `WFUD`：**文档事实**——WFUD 页说明它删除由 WFDF/WFDS 定义的 logical waveform 及其由 WAVE 定义的全部 physical waveform；WAVE 的 Errors 段要求重定义前先用 WFUD 删除。
- `ETIM` / `ERCY?`：**文档事实**——ETIM 页把 WAVE 列在相关命令中；ERCY? 页让读者参考 WAVE 以理解 expected data 参数。
- `VWFS?` / `VWFG?`：**文档事实**——这两个校验命令把 WFDF、WAVE、BWDF 等命令定义的波形与数据参数纳入一致性/兼容性检查。
- `VDCP`：**文档事实**——VDCP 页说明其 data parameter 与 WAVE 使用的 data parameter 相同，称为 direction parameter。
- `WSUS`：**文档事实**——`wvf_set` 的最大值由 WSUS 决定；WAVE 的 Errors 段以 WSUS 允许范围作为越界判据。
- `WFDS` 的 Postdependencies：**文档事实**——WFDS 页要求定义 logical waveform 后必须用 WAVE 指定其 physical waveform，即使 logical waveform 不含 data parameter。
- `Edge action` / `Specifying the actions`：**文档事实**——WAVE 的 Related information 指向这两篇，用于 fixed action / edge action 取值的说明。

## 版本

**文档事实**：Functional changes 仅记录 "Introduced before SmarTest 6.3.2"，即该命令早于文档集覆盖起点即已存在；文档未列出更细的版本变更。

## 出处

- `02_System_reference/02.06_Command_Reference/02.06.02.02.333_WAVE__WAVE__-__WAVEform.htm`——首段、Prerequisites、Mode of operation、语法/参数、示例、Errors、Related information 与 Functional changes 均取自本篇。
