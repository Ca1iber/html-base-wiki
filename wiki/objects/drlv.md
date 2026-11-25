---
type: object
title: DRLV, DRLV? - (DRive LeVel)
layer: L1
stage: level
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.89_DRLV__DRLV__-__DRive_LeVel.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# DRLV, DRLV? - (DRive LeVel)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **2,786 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.89_DRLV__DRLV__-__DRive_LeVel.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### DRLV

```
DRLV {level_set_no | level_set_id}, [logic_0_level], [logic_1_level], [v3h_level | range,] {(pinlist)}
```

### DRLV?

```
DRLV? {level_set_no | level_set_id}, {(pinlist)}
```

returns:

```
DRLV {level_set | level_set_id}, [logic_0_level], [logic_1_level], [v3h_level | range,] {(pinlist)}
```

### Parameters

[表]
行 1:
  level_set_no
  The identification number of the level set (fixed levels) in which you want the
    levels to be included. The number must not exceed the maximum number of level sets allowed
    (as defined by the `DSCP`（raw: `98578.htm`） command). Typing ALL in this field sets the levels for all existing level sets. Typing PRM sets the drive voltage levels for the primary level set.
行 2:
  level_set_id
  Used in equation based level setup. It is derived as follows:
    
    100000 * equation_set_no + 1000 * specset_no +
    level_set_no
    
    Note that if you use the command for an equation based level setup, you modify only the
    runtime values, not the value in the level set.
行 3:
  logic_0_level
  An integer (in mV) which sets the low level voltage for the drive amplifier.
行 4:
  logic_1_level
  An integer (in mV) which sets the high level voltage for the drive amplifier.
行 5:
  v3h_level
  Input (drive) 3rd level definition (high level voltage shift). The expression of
    this extra parameter must define a value in millivolts (mV).
    
    This parameter is no longer used.
行 6:
  range
  This extra parameter selects the drive range in mV:
    
     
    
    -8000.0 ... 8000.0 selects the 8 V range
    
    -30000.0 ... 30000.0 selects the 30 V range
    
    all other values select the -40 V ... +80 V range
    
     
    
    If not specified the best fit range will be selected based on
    logic_0_level and logic_1_level.
    
    This parameter is currently not available.
    
    The query returns the parameter only if it is defined for the queried level set.
行 7:
  pinlist
  The name of the pin or pins whose levels you want to set. This parameter can also
    include groups previously created by the `DFGP`（raw: `98546.htm`） (DeFine GrouP)
    command. If more than one pin is to be included, the names must be separated with a comma.
    The symbol @ sets or reads the drive levels of all input pins in the level set. You
    can include I and IO pin types in pinlist.

For card specifications, like level ranges, see
`Digital Cards`（raw: `132413.htm`）
, for
example:

`Pin Scale 1600`（raw: `126230.htm`）

`Pins Scale 5000`（raw: `351223.htm`）

### Examples

### Example 1
```
DRLV 1,-1750,-850,(Q0,Q1,Q2,Q3)
```

This
example sets the driver levels for level set 1 for pins Q0, Q1, Q2 and Q3. The logic 0 level is
set to -1750 mV and the logic 1 level to -850 mV.

### Example 2
```
DRLV 1,-1750,-850,8000,(avi64Pin1)
```

This
example shows how the 8 V drive range of an AVI64 pin is selected.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.89_DRLV__DRLV__-__DRive_LeVel.htm>` 的 `## Errors`、`## Warnings` 段。**不是转述。**
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

The high or low level is out of range;

The swing limitations are exceeded;

The set number is out of range;

The set number is out of the range defined by the
DSCP
command;

The set number is out of the used range of sets (
DRLV?
 only).

The parameter "
range
" exceeds the hardware defined maximum range.

### Warnings

A warning is generated if:

Auto-correction of logic level 1 or 0 occurs.

The logic 1 or 0 level for a pin lies outside the specification.

<!-- 报错节 end -->

## 是什么

**文档事实** DRLV（DRive LeVel）定义 driver amplifier 的低电平与高电平；可在同一条命令中为一个或多个 pin 设 level，也可为 DFGP 先前定义的 pin group 设 drive level；这些 level 被包含在指定的 level set 中。

**文档事实** DRLV? 查询返回指定 set 与 pins 的当前电压 level。

**文档事实** 与 equation based timing 结合时，DRLV 只改 runtime 值，不改 level set 中指定的 setup 值。

**文档事实** 每次 DRLV firmware 命令调用都需要激活 level set，可能增加测试时间，尤其多 site 并行时；此类情况应改用 SVLR firmware 命令。

**文档事实** 该命令配置处于 setup focus 的 site（见 PSFC）；同一时间只有一个 site 在 focus，SmarTest 在 Testflow Editor 与 result tools 中显示 focus site 的结果，firmware 查询也只报告 focus site 的 setup 与结果。

**文档事实** 主要参数：level_set_no（不得超过 DSCP 定义的最大 level set 数；ALL 设所有现有 level set，PRM 设 primary level set）；level_set_id（用于 equation based level setup，等于 100000*equation_set_no + 1000*specset_no + level_set_no，且只改 runtime 值）；logic_0_level 与 logic_1_level（mV 整数）；v3h_level（已不再使用）；range（-8000.0…8000.0 选 8 V 范围，-30000.0…30000.0 选 30 V 范围，其他值选 -40 V…+80 V，未指定时按 logic_0/1 选最佳范围，当前不可用，query 仅在 level set 已定义时返回）；pinlist（pin 名或 DFGP group，多个用逗号，@ 设/读该 level set 中所有 input pins，可含 I 与 IO pin 类型）。

**文档事实** Application 段把 DRLV 归入 Level Setup（参见 Level Setup Commands）。

**推断** DRLV 是固定 level set 的驱动电平赋值命令；equation based 场景下它只影响运行期值。

## 典型用法

**文档事实** `DRLV 1,-1750,-850,(Q0,Q1,Q2,Q3)` 为 level set 1 的 Q0–Q3 设 logic 0 = -1750 mV、logic 1 = -850 mV。

**文档事实** `DRLV 1,-1750,-850,8000,(avi64Pin1)` 为 AVI64 pin 选择 8 V drive range（第四参数为 range，而不是已废弃的 v3h_level）。

**文档事实** 用 PRM 设置 primary level set 的 drive 电压；用 ALL 设置所有现有 level set。

**文档事实** 用 @ 设置或读取该 level set 中所有 input pins 的 drive level。

**文档事实** 查询使用 `DRLV? {level_set_no | level_set_id}, {(pinlist)}`。

**文档事实** 多 site 且调用频繁时改用 SVLR，避免 DRLV 每次调用激活 level set 带来的测试时间开销。

**建议** 在 equation based level setup 中若需要持久修改，应改 level set 或 setup 文件，而不能依赖 DRLV，因为它只改 runtime 值。

## 和谁有关

- **文档事实** DSCP，level_set_no 不得超过 DSCP 定义的最大 level set 数，Errors 也提到 set number 超出 DSCP 范围。
- **文档事实** DFGP, DFGP? - (DeFine GrouP)，pinlist 可包含 DFGP 先前创建的 group。
- **文档事实** RCLV, RCLV? - (ReCeive LeVel)，Getting started 的步骤把 DRLV 与 RCLV 并列为修改 drive 与 receive level 的命令。
- **文档事实** SVLR，本页 Note 建议多 site 时改用 SVLR，避免 DRLV 每次调用激活 level set 的测试时间开销。
- **文档事实** PSFC, PSFC?，本页说明该命令配置处于 setup focus 的 site，并指向 PSFC 页。
- **文档事实** DRLS - (DRive Level Sensitivity)，其文档在判定 high threshold 时要求 limit 位于 channel board 最小 drive level（参见 DRLV）与 pass value 之间。
- **文档事实** SPST - (SPecset STatus)，其文档说可用 DRLV 等命令修改 timing/level 数据；执行后受影响 specset 的 bit 自动置位，restore 应恢复原状态。
- **文档事实** UPTD - (UP To Date)，其文档说 PSLV、DRLV、RCLV 可使 DPS 与 LEV 参数状态不同步。
- **文档事实** Create a fixed level set 与 Set fixed driver levels，后者说 DRLV 设置的电压成为所指定 level set 的一部分。
- **文档事实** Level Setup Commands，本页 Application 段把 DRLV 归入 Level Setup。
- **文档事实** Digital Cards（如 Pin Scale 1600、Pins Scale 5000），本页参数说明把 level range 等 card 规格指向该页与具体 card 页。

## 版本

**文档事实** Functional changes 记载 Introduced before SmarTest 6.3.2。

**文档事实** SmarTest 7.0.1：No single-density support。

**文档事实** SmarTest 7.4.0：扩展第四参数用法，v3h_level 改为 v3h_level | range。

## 出处

- `02_System_reference/02.06_Command_Reference/02.06.02.02.89_DRLV__DRLV__-__DRive_LeVel.htm`，主源，含首段、Syntax、Parameters、Application、Errors、Warnings、Examples 与 Functional changes。
- `02_System_reference/02.06_Command_Reference/02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.htm`，DSCP 上限与报错条件的旁证。
- `02_System_reference/02.06_Command_Reference/02.06.05.01.05.01.01_Set_fixed_driver_levels.htm`，DRLV 与 level set 关系的旁证。
- `extract/edges.jsonl` 入边，用于 DFGP、DRLS、SPST、UPTD、RCLV 等旁证。
