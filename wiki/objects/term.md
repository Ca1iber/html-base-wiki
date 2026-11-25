---
type: object
title: TERM, TERM? - (TERMination mode)
layer: L1
stage: level
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.257_TERM__TERM__-__TERMination_mode.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# TERM, TERM? - (TERMination mode)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **8,536 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.257_TERM__TERM__-__TERMination_mode.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### TERM

```
TERM {level_set_no | level_set_id}, [term_mode], [term_pulldown,] [param_1], [param_2], [param_3],
[l_range], [h_range], [hr_mode,] {(pinlist)}
```

### TERM?

```
TERM? {level_set_no | level_set_id}, {(pinlist)}
```

returns:

```
TERM {level_set_no | level_set_id}, {term_mode}, [term_pulldown,] [param_1], [param_2], [param_3],
[l_range], [h_range], [hr_mode,] {(pinlist)}
```

### Parameters

[表]
行 1:
  level_set_no
  The identification number of the level set in which you want
    the definitions to be included. The number must not exceed the
    maximum number of level sets allowed (as defined by `DSCP`（raw: `98578.htm`）) and the level sets used (as
    defined by `LSUS`（raw: `98641.htm`）). Entering
    ALL in this field sets the termination
    mode for all existing level sets (except level set 0). Entering
    PRM in this field defines the termination
    mode for the primary level set.
    
    Standard level sets have a number > 0. Level set 0 is a
    dedicated level set for digital pins in high-Z state. For more
    information see `Defining a level set for sequencer state OFF`（raw: `119431.htm`）.
行 2:
  level_set_id
  Derived as follows:
    
    100000 * equation_set_no + 1000 * specset_no +
    level_set_no
行 3:
  term_mode
  The termination mode has dependencies to pin types and to the
    parameters (term_pulldown and
    param_1 to param_3 -
    see the syntax). The allowed combinations are shown in the
    Termination modes table, below.
    
    Level set 0 only supports the termination modes
    OFF (the default), T,
    C, and A.
行 4:
  term_pulldown
  Extra parameter that defines the pull down mode. For more
    information refer to column term_mode of table
    Termination modes below.
    
    The query returns the parameter only if it is defined for the
    queried level set.
行 5:
  param_1
  The use of this parameter depends on the termination mode as
    shown in the Termination modes table, below. When used,
    param_1 gives the termination voltage,
    active load commutation voltage, or the clamp low level voltage.
    The units are mV.
行 6:
  param_2
  The use of this parameter depends on the termination mode as
    shown in the Termination modes table, below. When used,
    param_2 defines the active load Iol
    current, or the clamp high level voltage. The units are mA or mV
    respectively.
    
    When used, param_2 defines either
    
    the active load Iol current in µA,
    
    the clamp high level voltage in mV, or
    
    the receiver swing voltage in mV.
    
    For the NP termination modes SP,
    SM, SEP, or
    SEM, param_2 defines
    the receiver threshold in mV.
行 7:
  param_3
  The use of this parameter depends on the termination mode as
    shown in the Termination modes table, below:
    
    For term_mode = A,
    param_3 defines the active load Ioh
    current. The units are µA.
    
    For term_mode =
    CT,
    param_3 defines the
    receiver offset in mV.
    
    For term_mode =
    bidir_receiver,
    param_3 defines the
    receiver offset in mV.
行 8:
  l_range
  For term_mode =A the low level current range.
    
    This parameter can be
    
    I5E3: Defines the low current range of 0
    to 5 mA.
    
    I3E4: Defines the high current range of 0
    to 30 mA.
    
    AUTO: Lets the firmware automatically
    select the correct range. Whenever possible, the system
    selects the lower range.
    
    This parameter is not supported for AVI64.
行 9:
  h_range
  For term_mode =A the high level current range.
    
    This parameter can be
    
    I5E3: Defines the low current range of 0
    to 5 mA.
    
    I3E4: Defines the high current range of 0
    to 30 mA.
    
    AUTO: Lets the firmware automatically
    select the correct range. Whenever possible, the system
    selects the lower range.
行 10:
  pinlist
  The pin name or names of those power supply outputs which have
    already been defined. If more than one pin is required, the
    names must be separated with a comma. The @
    character can be used to read all configured power supply
    pins.

### Termination modes

The following tables describe the admitted termination modes.

[表] Termination modes
列: term_mode [, term_pulldown] | Description | Pin types | Parameters
行 1:
  OFF
  Off
  o, io
  
行 2:
  OFF,PULLDOWN
  PS1600 and PS5000 only: To switch on the pulldown resistor, use
    OFF,PULLDOWN
  i, o, io
  
行 3:
  OFF,NONE
  PS1600 only: To switch off the pulldown resistor,
    use OFF,NONE
  i, o, io
  
行 4:
  DIFHIZ
  High-impedance unterminated differential
    receiver
  o, io
  
行 5:
  DIFHIZ
  PS1600 only: To switch on the pulldown resistor, use DIFHIZ,PULLDOWN
  
  
行 6:
  DIFHIZ
  PS1600 only: To switch off the pulldown resistor, use DIFHIZ,NONE
  
  
行 7:
  T [跨 3 行]
  Terminated with the specified voltage:
  
  
行 8:
  For the o pin:
    
    The driver is used for the termination.
    
    `Pin Scale 1600 driver`（raw: `126230.htm`）
    
    `Pin Scale 5000 driver`（raw: `351223.htm`）
  o
  param_1:
    
    Termination voltage
行 9:
  For io pin:
    
    The third level of the driver is used for the termination.
    
    For the ranges see the card specifications:
    
    `Pin Scale 1600 driver`（raw: `126230.htm`）
    
    `Pin Scale 5000 driver`（raw: `351223.htm`）
    
    For io pin the driver output is the third
    level, only while high-Z is specified for the driver.
  io
  param_1:
    
    Termination voltage
行 10:
  H
  High terminated (by driver).
    
    The driver is used for the termination.
    term_mode=H (or L) does not control the
    driver; you have to drive a 1 in order to terminate with vih (or
    you have to drive a 0 in order to terminate with vil).
    
    The driver is never set to high-Z in
    term_mode=H (or
    L), even if it is specified.
  io
  
行 11:
  L
  Low terminated (by driver).
  io
  
行 12:
  A
  Active load.
    
    For active load commutation voltage values see the card
    specifications:
    
    `Pin Scale 1600 driver`（raw: `126230.htm`）
    
    `Pin Scale 5000 driver`（raw: `351223.htm`）
    
    For io pin, the active load is enabled, only while the
    driver is set to high-Z. The active load is set to high-Z while
    the driver is set to logic 1 or 0.
    
    Pin Scale 5000:
    
    Active load and highZ is not available in fast mode.
  o, io
  param_1:
    
    Active load commutation voltage
    
    param_2:
    
    Active load Iol current
    
    param_3:
    
    Active load Ioh current
    
    l_range
    
    h_range
行 13:
  CT
  Differential receiver center tap termination with
    the specified termination voltage.
    
     
    
    CT is also used to switch to differential
    receiver (comparator/capture) from single-ended receivers.
    
    The power-on default value of param_2 (swing)
    is 3.2 V, and the power-on default value of
    param_3 (offset) is 1.2 V.
    
    For io pin, the driver output is the third
    level, only while high-Z is specified for the driver.
  o, io
  param_1:
    
    Termination voltage
    
    param_2:
    
    Not currently supported.
    
    param_3:
    
    Not currently supported.
行 14:
  XSE
  Single-ended cross-termination
    
    For the Pin Scale 1600:
    For
    term_mode=X or XSE, the clamps
    are set to off and the driver output is set to
    high-Z.
  o
  
行 15:
  X
  Cross-termination
    
    Currently not in use.
  o
  
行 16:
  C
  Clamp.
    
    Note that this sets clamps as termination mode of the specified pins. Only the latest
    setting of term_mode for the specified pins is used. To use both the
    clamps and termination, or to set clamps independently from termination mode, use the
    CLMP command.
  o, io
  param_1:
    
    Clamp low voltage
    
    param_2:
    
    Clamp high voltage

### Examples

### Example 1
```
TERM 1,T,-1500,,,,,(Q1)
```

This
example terminates the output pin Q1 to -1500 mV in level set 1.

### Example 2
```
TERM 3,A,3000,1500,1000,I3E4,I3E4,(out)
```

This
example sets the active load level of the pin group out to 3V, and sets Iol and Ioh
current to 1.5 and 1.0 mA respectively. The 0 to 30 mA range is used for both the
low and the high range.

### Example 3
```
TERM 1,CT,2000,,,,,(o1,o1-)
```

This
example terminates the differential output pair (the o1 and o1- pins) to 2000 mV
with center tap termination in level set 1.

### Example 4
```
TERM 1,OFF,PULLDOWN,,,,,,(Q1,Q2)
```

On a PS1600 card,
this example switches
on
 the pulldown resistor on the specified
pins.

```
TERM 1,OFF,NONE,,,,,,(Q1,Q2)
```

On a PS1600 card,
this example switches
off
 the pulldown resistor on the specified
pins.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.257_TERM__TERM__-__TERMination_mode.htm>` 的 `## Errors`、`## Warnings` 段。**不是转述。**
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

You use the wrong current range for the selected current.

You use an incorrect parameter combination.

You use too many parameters for the selected mode.

The clamp voltage is out of range.

The active load voltage is out of range.

The active load current is out of range.

The termination voltage is out of range.

The low level voltage is higher than the high level voltage in clamp mode.

You use the termination mode
H
 or
L
 for an

o
 pin. Use the termination mode

T
.

Parameter
hr_mode
 is used for instruments other than
AVI64.

### Warnings

A warning is generated if:

Auto-correction of high or low level clamp voltage occurs.

The range is auto-corrected due to an incompatible range and current
combination.

You enter too many parameters for the selected termination mode (see the table
above).

<!-- 报错节 end -->

## 是什么

**文档事实**：TERM 设置 output 与 IO pin 的 termination mode（终接模式）。

**文档事实**：它配置处于 setup focus 的 site 的 setup（参见 PSFC）；该命令一次只能聚焦一个 site，SmarTest 在 Testflow Editor 与 result tools 中按焦点 site 显示结果，firmware 查询也只报告当前焦点 site 的 setup 与结果。

**文档事实**：equation based testing 中要以 level set ID 标识 level set，算法为 `100000 * equation_set_no + 1000 * specset_no + level_set_no`。TERM 会置位状态位的 bit 8，表示 equation based 值已被覆盖（见 SPST?）。

**文档事实**：`level_set_no` 可填 `ALL`（对除 level set 0 外的所有现有 level set 设置）或 `PRM`（primary level set）；标准 level set 编号 > 0；level set 0 专供数字 pin 的 high-Z 状态使用，只支持 OFF（默认）、T、C、A 四种 termination mode。

**文档事实**：`term_mode` 与 pin 类型及参数（`term_pulldown`、`param_1`~`param_3`）有依赖；文档 Termination modes 表列出 OFF、OFF,PULLDOWN、OFF,NONE、DIFHIZ、T、H、L、A、CT、XSE、X、C。要点：T 用指定电压终接；H/L 由 driver 做高/低终接（H/L 不控制 driver，需驱动 1 才以 vih 终接、驱动 0 才以 vil 终接，且 H/L 下 driver 永不进入 high-Z）；A 为 active load（io pin 仅在 driver high-Z 时使能；PS5000 在 fast mode 下不支持 active load 与 highZ）；CT 为差分接收器中心抽头终接，也用于从单端接收器切到差分接收器；XSE 为单端交叉终接；X 当前未使用；C 只把 clamp 设为指定 pin 的 termination mode，且只保留最近一次设置，若要同时用 clamp 与终接、或独立设置 clamp，应使用 CLMP。

**文档事实**：A 的 `l_range` / `h_range` 可选 I5E3（0–5 mA）、I3E4（0–30 mA）、AUTO；`l_range` 不支持 AVI64。C 模式下 param_1/param_2 分别是 clamp 低/高电压。Application 归属 Level setup；Related information 列出 IO PINS resources。

## 典型用法

**文档事实**（示例）：
- `TERM 1,T,-1500,,,,,(Q1)`：把 output pin Q1 在 level set 1 终接到 −1500 mV。
- `TERM 3,A,3000,1500,1000,I3E4,I3E4,(out)`：把 pin 组 out 的 active load 设为 3 V，Iol/Ioh 分别 1.5/1.0 mA，低/高电流范围都用 0–30 mA。
- `TERM 1,CT,2000,,,,,(o1,o1-)`：对差分输出对 o1/o1- 用中心抽头终接到 2000 mV（level set 1）。
- `TERM 1,OFF,PULLDOWN,,,,,,(Q1,Q2)` 在 PS1600 上打开指定 pin 的下拉电阻；`TERM 1,OFF,NONE,,,,,,(Q1,Q2)` 关闭。

**文档事实**：查询用 `TERM? {level_set_no | level_set_id}, {(pinlist)}`，返回含 `term_mode` 与已定义的可选参数（`term_pulldown` 仅在该 level set 已定义时才返回）。

**建议**：参数个数与模式强相关——参数过多会报错/警告；设置前按 Termination modes 表核对 pin 类型与参数组合，电流范围要与电流值匹配，clamp 模式下低电压不得高于高电压。

## 和谁有关

- `DSCP`、`LSUS`：**文档事实**——`level_set_no` 不得超过 DSCP 允许的最大 level set 数，也不得超过 LSUS 定义的已用 level set 数。
- `PSFC`：**文档事实**——TERM 配置处于 setup focus 的 site 的 setup，正文链接 PSFC。
- `SPST?`：**文档事实**——正文说 TERM 置位状态位 bit 8 以表示 equation based 值被覆盖，并让读者参考 SPST?；入边显示 SPST 页把 TERM 列为会修改 level/timing data 从而自动置位的命令之一。
- `CLMP`：**文档事实**——C 模式只设 clamp；要同时用 clamp 与终接、或独立设 clamp 需用 CLMP；入边显示 CLMP 页指向 TERM。
- `SPEC`：**文档事实**——入边显示 SPEC 命令可查询某 pin 与 level setup 下 TERM 允许的 termination mode。
- level set 0 / `Defining a level set for sequencer state OFF`：**文档事实**——level set 0 专供 high-Z；正文链接该用法，入边另有 level set 0 保护敏感 DUT 的应用页。
- `PS1600 driver` / `Pin Scale 5000 driver`：**文档事实**——T、A 等模式的范围与行为参考这两份卡规格；OFF,PULLDOWN 需 PS1600/PS5000，OFF,NONE 与 DIFHIZ,PULLDOWN/NONE 仅 PS1600。
- `IO PINS resources`、`Level Setup Commands`：**文档事实**——Related information 与 Application 所列。

## 版本

**文档事实**：Functional changes 记：Introduced before SmarTest 6.3.2（哨兵值）；SmarTest 7.1.0 新增 PS1600 的 `OFF,PULLDOWN` 与 `OFF,NONE` 参数；7.1.4 支持 DIFHIZ；7.4.0 新增额外参数 `hr_mode`，并为 DC Scale AVI64 增加 termination mode。

## 出处

- `02_System_reference/02.06_Command_Reference/02.06.02.02.257_TERM__TERM__-__TERMination_mode.htm`——正文、参数、Termination modes 表、Errors/Warnings、示例、Related information 与 Functional changes 均取自本篇（已用 `show.py 02.06.02.02.257` 读取）。
- 入边关系取自 `extract/objpack.py` 的 `edges_in`；`PS1600 driver` / `Pin Scale 5000 driver` 的具体电气范围以正文所链卡规格页为准。
