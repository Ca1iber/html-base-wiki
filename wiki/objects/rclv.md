---
type: object
title: RCLV, RCLV? - (ReCeive LeVel)
layer: L1
stage: level
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.204_RCLV__RCLV__-__ReCeive_LeVel.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# RCLV, RCLV? - (ReCeive LeVel)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **3,893 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.204_RCLV__RCLV__-__ReCeive_LeVel.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### RCLV

```
RCLV {level_set_no | level_set_id}, [vth | logic_0_level], [logic_1_level], [range,] {(pinlist)}
```

### RCLV?

```
RCLV? {level_set_no | level_set_id}, {(pinlist)}
```

returns:

```
RCLV {level_set | level_set_id}, [vth | logic_0_level], [logic_1_level], [range,] {(pinlist)}
```

### Parameters

[表]
行 1:
  level_set
  The identification number of the level set in which you want the low and high
    threshold levels to be included. The number must not exceed the maximum number of level
    sets allowed (as defined by `DSCP, DSCP? - (Define System Control Parameter)`（raw: `98578.htm`）). If you enter a level set number that
    is outside the used range of sets defined by the LSUS command, a new
    level set is created. Typing ALL in this field sets the low and high
    threshold levels for all existing level sets (except level set 0). Typing
    PRM sets the low and high threshold levels for the primary level
    set.
    
    Standard level sets have a number greater than 0. Level set 0 is a dedicated level set
    for sequencer state OFF. For more information see `Defining a level set for sequencer state OFF`（raw: `119431.htm`）.
行 2:
  level_set_id
  Used in equation based level setup. It is derived as follows:
    
    100000 * equation_set_no + 1000 * specset_no +
    level_set_no
    
    Note that if you use the command for an equation based level setup, you modify only the
    runtime values, not the value in the level set.
行 3:
  vth
  Output threshold for FAST comparator (single threshold as opposed to high and low).
    The expression must define a value in millivolts (mV).
行 4:
  logic_0_level
  An integer (in mV) which sets the logic 0 threshold level of the comparator. This
    parameter represents the point where the comparator distinguishes between logic 0 and an
    intermediate level.
行 5:
  logic_1_level
  An integer (in mV) which sets the logic 1 threshold level of the comparator. This
    parameter represents the point where the comparator distinguishes between logic 1 and an
    intermediate level.
行 6:
  range
  This extra parameter selects the receive range in mV.
    
    This parameter is currently not available.
    
    Ranges of the high-speed voltage comparator:
    
    -8000.0 ... 8000.0 selects the 8 V range
    
    -40000.0 ... 80000.0 selects the -40 V ... +80 V range
    
    Ranges of the high-resolution voltage comparator:
    
    -3000.0 ... 3000.0 selects the 3 V range
    
    -10000.0 ... 10000.0 selects the 10 V range
    
    -30000.0 ... 30000.0 selects the 30 V range
    
    -40000.0 ... 80000.0 selects the -40 V ... +80 V range
    
    If not specified the best fit range will be selected based on
    logic_0_level and logic_1_level if a voltage
    comparator is selected.
    
    Range of the high-resolution current comparator:
    
    A fixed range of 200 mA is set.
    
    The query returns the parameter only if it is defined for the queried level set.
行 7:
  pinlist
  The name of the pin or pins whose threshold level you want to set. This parameter
    can also include groups previously created by the command `DFGP, DFGP? - (DeFine GrouP)`（raw: `98546.htm`）. If more
    than one pin is to be included, the names must be separated with a comma. The symbol
    @ sets or reads the threshold levels for all output pins. You can include O or IO
    pins in pinlist.

For card specifications, like level ranges, see
`Digital Cards`（raw: `132413.htm`）
, for
example:

`Pin Scale 1600`（raw: `126230.htm`）

`Pins Scale 5000`（raw: `351223.htm`）

### Examples

### Example 1
```
RCLV 1,-1300,-750,(Q0)
```

This example sets
the low level compare threshold for pin
Q0
 to -1300 mV and the high level
compare threshold to -750 mV.

### Example 2
```
TERM 1,,,,,,HRV,(avi64Pin1)
RCLV 1,-1300,-750,3000,(avi64Pin1)
```

This
example for an AVI64 pin sets the low level compare threshold to -1300 mV, the high level
compare threshold to -750 mV, and the range to the 3 V range.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.204_RCLV__RCLV__-__ReCeive_LeVel.htm>` 的 `## Errors`、`## Warnings` 段。**不是转述。**
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

The low level threshold is out of range.

The high level threshold is out of range.

The threshold swing is out of range.

The level set number smaller than one.

The level set number is outside the range defined by the
DSCP

command.

For the query the level set number is outside the used range of sets defined by the

LSUS
 command.

The parameter "
range
" exceeds the hardware defined maximum range.

### Warnings

A warning is generated if

Auto-correction of logic 1 or 0 threshold occurs.

A range is defined for the high-resolution current comparator. This range will be
ignored.

<!-- 报错节 end -->

## 是什么

**文档事实**：RCLV（ReCeive LeVel）为比较器定义 logic 1 与 logic 0 阈值电平（mV），可在同一条命令中设置一个或多个引脚，也可用于 `DFGP` 先前定义的 pin 组；阈值写入指定的 level set，`RCLV?` 返回该 level set 与指定引脚的当前阈值。

**文档事实**：`vth` 是 FAST 比较器的单阈值（代替分别给出的高、低阈值）；`logic_0_level` / `logic_1_level` 分别是比较器区分 logic 0 / logic 1 与中间电平的阈值点。

**文档事实**：普通 level set 编号大于 0；level set 0 是 sequencer state OFF 专用的 level set。`ALL` 设置除 level set 0 外的所有已有 level set，`PRM` 设置 primary level set。若写入的编号超出 `LSUS` 已使用的 level set 范围，会新建一个 level set。

**文档事实**：DUT 板上若使用串联电阻（resistive divider），接收电平会自动调整，以补偿串联电阻上的压降。

**文档事实**：equation based level setup 使用 `level_set_id`，导出式为 `100000*equation_set_no + 1000*specset_no + level_set_no`；此时只修改运行值，不修改 level set 中的值。

**文档事实**：Warnings 段记录：若发生 logic 1 或 logic 0 阈值的自动校正，会产生 warning；若为高分辨率电流比较器定义 `range`，该 `range` 会被忽略。

**文档事实**：`range` 选择接收量程（mV）：高速电压比较器可选 8 V（-8000.0…8000.0）或 -40 V…+80 V（-40000.0…80000.0）；高分辨率电压比较器可选 3 V、10 V、30 V 或 -40 V…+80 V；高分辨率电流比较器固定 200 mA。未指定时，若选择的是电压比较器，则按 `logic_0_level` / `logic_1_level` 选最佳量程。参数说明同时标注 "This parameter is currently not available."，而功能变更记录写明 `range` 是 SmarTest 7.4.0 新增的参数，两处表述不一致。

## 典型用法

**文档事实**：`RCLV 1,-1300,-750,(Q0)`——把 pin Q0 的 logic 0 比较阈值设为 -1300 mV、logic 1 阈值设为 -750 mV。

**文档事实**：AVI64 示例先执行 `TERM 1,,,,,,HRV,(avi64Pin1)`，再执行 `RCLV 1,-1300,-750,3000,(avi64Pin1)`；文档说明该例把低、高阈值设为 -1300/-750 mV，并把量程设为 3 V range。

**文档事实**：查询语法为 `RCLV? {level_set_no | level_set_id}, {(pinlist)}`，返回一条与设置命令同参数形式的 `RCLV ...` 行。

**文档事实**：`pinlist` 可包含 `DFGP` 定义的 pin 组；`@` 用于设置或读取全部 output pin 的阈值；pinlist 中可包含 O 或 IO 引脚。

**建议**：批量设置前先对目标引脚与 level setup 用 `SPEC?` 查 RCLV 允许的最小 logic 0 / 最大 logic 1 阈值，避免越界报错。

## 和谁有关

- `DRLV`：**文档事实**——DRLV 是驱动电平的对应命令；入门文档在同一处要求 "Change the drive and receive levels (DRLV and RCLV)"。
- `DFGP`：**文档事实**——RCLV 首段与 `pinlist` 参数都写明可使用 `DFGP` 定义的 pin 组。
- `TERM`：**文档事实**——RCLV 的 Example 2 先用 TERM 选择比较器，再设置阈值；SPST? 页也把 TERM 与 RCLV 并列为会修改 level 数据的命令。
- `RCLS?`：**文档事实**——RCLS? 页要求 `pass_value` 落在通道板比较器阈值范围内，并让读者参考 RCLV。
- `SPEC?`：**文档事实**——SPEC? 查询指定引脚与 level setup 下 RCLV 可指定的最小 logic 0 与最大 logic 1 阈值。
- `DSCP`：**文档事实**——level set 数不得超过 DSCP 定义的最大 level set 数；RCLV 的 Errors 段以 DSCP 范围作为越界判据。
- `LSUS`：**文档事实**——写入编号超出 LSUS 已用范围时新建 level set；查询时编号超出 LSUS 已用范围会报错。
- `SPST?` / `UPTD`：**文档事实**——SPST? 页把 RCLV 列为会修改 level 数据、从而置位受影响 specset 状态位的命令；UPTD 页在 DPS/LEV 状态同步的说明中把 PSLV、DRLV、RCLV 等命令并列。
- `Defining a level set for sequencer state OFF`：**文档事实**——`level_set` 参数说明引用该篇，用于 level set 0 的专用性。
- `Digital Cards`（如 Pin Scale 1600、Pins Scale 5000）：**文档事实**——RCLV 末尾让读者到这些卡页查 level range 等规格。
- `Set fixed receiver levels` / `Create a fixed level set`：**文档事实**——这两篇 how-to 都以 RCLV 作为设置接收阈值的命令。

## 版本

**文档事实**：Functional changes 记录：Introduced before SmarTest 6.3.2（早于文档集覆盖起点即已存在，不是 6.3.2 的变更）；SmarTest 7.4.0 新增额外参数 `range`。

## 出处

- `02_System_reference/02.06_Command_Reference/02.06.02.02.204_RCLV__RCLV__-__ReCeive_LeVel.htm`——首段、语法/参数、两个示例、Errors/Warnings、Related information 与 Functional changes 均取自本篇。
