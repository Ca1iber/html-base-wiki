---
type: object
title: CLMP, CLMP? - (CLaMP level)
layer: L1
stage: level
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.26_CLMP__CLMP__-__CLaMP_level.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# CLMP, CLMP? - (CLaMP level)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **2,496 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.26_CLMP__CLMP__-__CLaMP_level.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### CLMP

```
CLMP {level_set|level_set_id}, [clamp_mode], [low_clamp_level], [high_clamp_level], {(pinlist)}
```

### CLMP?

```
CLMP? {level_set|level_set_id}, {(pinlist)}
```

returns:

```
CLMP {level_set|level_set_id}, [clamp_mode], [low_clamp_level], [high_clamp_level], {(pinlist)}
```

### Parameters

[表]
行 1:
  level_set
  The identification number of the level set in which you want the levels to be
    included. The number must not exceed the maximum number of level sets allowed (as defined
    by the DSCP command). Specifying ALL sets the clamp
    levels for all existing level sets (except level set 0). Specifying PRM
    sets the clamp levels for the primary level set.
    
    Standard level sets have a number > 0. Level set 0 is a dedicated level set for the
    high-Z state of digital pins. For more information see `Defining a level set for sequencer state OFF`（raw: `119431.htm`）.
行 2:
  level_set_id
  Used in equation based level setup. It is derived as follows:
    
    100000 * equation_set_no + 1000 * specset_no +
    level_set_no
    
    Note that if you use the command for an equation based level setup, you modify only the
    runtime values, not the value in the level set.
行 3:
  clamp_mode
  ON | OFF
    
    For the Pin Scale 3600, the clamps can be set to ON when std/fast mode is set to std, and
    termination mode is set to OFF or A (active load).
    
    Pin Scale 9G cards do not have clamps. Setting clamp levels will be ignored.
    
    For termination mode, see `TERM, TERM? - (TERMination mode)`（raw: `98771.htm`）.
行 4:
  low_clamp_level
  An integer (in mV) which sets the low clamp level.
    
    For the Pin Scale 800, the range is -1800 to 6800. At power-on this parameter assumes a
    default value of -250.
行 5:
  high_clamp_level
  An integer (in mV) which sets the high clamp level. For the Pin Scale 800, the
    range is -1800 to 6800, and the difference of high_clamp_level -
    low_clamp_level must be in the range 0 to 8.6 V.
行 6:
  pinlist
  The name of the pins for which the clamp levels are to be set. This parameter can
    also include groups previously created by the DFGP (DeFine GrouP)
    command. If more than one pin is to be included, the names must be separated by a comma.
    The symbol @ refers to all pins. You can include O and IO pin types in
    pinlist.

### Example

```
CLMP 1,ON,-10,5100,(Q0,Q1,Q2,Q3)
```

This example sets the clamp
levels for level set 1 for pins Q0, Q1, Q2 and Q3. The low clamp level is set to -10 mV, and the
high clamp level is set to 5100 mV.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.26_CLMP__CLMP__-__CLaMP_level.htm>` 的 `## Errors` 段。**不是转述。**
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

The high or low clamp level is out of range.

The swing limitations are exceeded.

The set number is out of range.

The set number is out of the range defined by the
DSCP
 command.

The set number is out of the used range of sets (
CLMP?
 only).

<!-- 报错节 end -->

## 是什么

**文档事实**：`CLMP`（CLaMP level）为指定 pin 设定低、高 clamp 电压，并开关 clamp；这些电平包含在指定的 level set 中。`CLMP?` 返回指定 level set 和 pin 的实际 clamp 电平，以及 clamp mode（on/off）。

**文档事实**：与 equation based timing/level setup 联用时，`CLMP` 只改运行时值，不改 level set 中保存的 setup 值。源文正文写 `equation based timing`，参数表写 `equation based level setup`，两处措辞不一致。

**文档事实**：本命令配置的是处于 setup focus 的 site；一次只有一个 site 在 focus，`CLMP` 的设置与 `CLMP?` 的返回也都是该 site 的信息（源文指向 `PSFC`）。

**文档事实**：`level_set` 不得超过 `DSCP` 定义的最大 level set 数；`ALL` 表示除 level set 0 外的所有已有 level set，`PRM` 表示 primary level set。标准 level set 编号 > 0，level set 0 是数字 pin high-Z 状态的专用 level set。

**文档事实**：equation based level setup 的 `level_set_id` 按 `100000 * equation_set_no + 1000 * specset_no + level_set_no` 推导。

**文档事实**：`clamp_mode` 取 `ON`/`OFF`。Pin Scale 3600 只有在 std/fast mode 为 `std`、termination mode 为 `OFF` 或 `A`（active load）时才能把 clamp 设为 `ON`；Pin Scale 9G 卡没有 clamp，设置 clamp 电平会被忽略。termination mode 见 `TERM`。

**文档事实**：`low_clamp_level`、`high_clamp_level` 为整数（mV）。Pin Scale 800 的范围是 -1800 至 6800，上电时 `low_clamp_level` 默认 -250；`high_clamp_level - low_clamp_level` 必须在 0 至 8.6 V。

**文档事实**：`pinlist` 可包含 `DFGP` 已创建的 group，多个 pin 名用逗号分隔，`@` 表示所有 pin，可包含 `O` 与 `IO` pin 类型。

## 典型用法

**文档事实**：为 level set 1 的 Q0–Q3 设 clamp，低 clamp 为 -10 mV、高 clamp 为 5100 mV：

```
CLMP 1,ON,-10,5100,(Q0,Q1,Q2,Q3)
```

**文档事实**：查询用 `CLMP? {level_set|level_set_id}, {(pinlist)}`，返回与设置同形的行：`CLMP {level_set|level_set_id}, [clamp_mode], [low_clamp_level], [high_clamp_level], {(pinlist)}`。

**文档事实**：设置时 `level_set` 写 `ALL` 可作用于除 level set 0 外的所有已有 level set，写 `PRM` 可作用于 primary level set。

**文档事实**：equation based level setup 下命令只改运行时值；`CLMP?` 的报错还包括 set number 超出已使用 set 范围。

## 和谁有关

**文档事实**：以下关系都有源文正文、参数说明或入边支撑；每条注明为什么相关。

- [[dscp]]：`level_set` 的上限由 `DSCP` 定义，`Errors` 也把“set number 超出 `DSCP` 定义范围”列为报错。为什么：参数与报错都点名 `DSCP`。
- [[term]]：clamp 能否为 `ON` 取决于 termination mode（`OFF`/`A`），本页明确指到 `TERM`；`TERM` 页说明 `C` 模式只设 clamp，要同时用 clamp 与终接、或独立设 clamp 需用 `CLMP`。
- [[dfgp]]：`pinlist` 可包含 `DFGP` 创建的 group。为什么：本页 `pinlist` 说明直接点名 `DFGP`。
- [[psfc]]：本命令只作用于有 setup focus 的 site；本页指向 `PSFC`，`PSFC` 页也把 `CLMP` 列入受 focus 影响的 setup 命令。
- `Defining a level set for sequencer state OFF`（`02_System_reference/02.06_Command_Reference/02.06.05.01.05.05_Controlling_high-Z_behavior_of_digital_pins_while_the_sequencers_are_OFF.htm`）：level set 0 是 high-Z 专用 level set，本页的 `level_set` 说明指到该文。
- `Create a fixed level set`（`02.06.05.01.05.01_Create_a_fixed_level_set.htm`）与 `Set fixed clamping levels`（`02.06.05.01.05.01.03_Set_fixed_clamping_levels.htm`）：前者把 `CLMP` 列为创建 level set 的命令之一；后者说可用 `CLMP` 或 `TERM` 设 clamp，若要独立于 termination mode 设 clamp 则用 `CLMP`。
- `Site dependent firmware commands`（`02.06.02.02.01_Site_dependent_firmware_commands.htm`）：命令表中 `CLMP` 的 “Command site focus” 与 “Query site focus” 两列均为 Yes。
- `Level Setup Commands`（`02_System_reference/02.06_Command_Reference/02.06.05_Level_Setup_Commands.htm`）：本页 `Application` 指到该章。
- `Level set 0` application paper（`03_Use_cases_and_application_papers/03.14_Application_Papers/03.14.03.07_Level_set_0__Protecting_sensitive_DUTs_and_DUT_board_circuitries_from_tr.htm`）：该文讲 level set 0 的 high-Z 保护定制，可按 pin 修改 clamp 值，并链接到本页。

## 版本

**文档事实**：源文没有 `Functional changes` 段，版本信息文档未覆盖。

## 出处

- 主源：`02_System_reference/02.06_Command_Reference/02.06.02.02.26_CLMP__CLMP__-__CLaMP_level.htm`（正文、CLMP/CLMP?、Parameters、Application、Errors、Example）。
- 关系证据：`extract/objpack.py` 的入边（`02.06.02.02_List_of_commands`、`02.06.05.01.05.01_Create_a_fixed_level_set`、`02.06.05.01.05.01.03_Set_fixed_clamping_levels`、`02.06.02.02.01_Site_dependent_firmware_commands`、level set 0 application paper 等）与 `TERM` 页正文。
