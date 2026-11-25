---
type: object
title: PSLV, PSLV? - (Power Supply LeVel)
layer: L1
stage: level
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.195_PSLV__PSLV__-__Power_Supply_LeVel.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# PSLV, PSLV? - (Power Supply LeVel)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **5,670 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.195_PSLV__PSLV__-__Power_Supply_LeVel.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### PSLV

```
PSLV {dps_No|dps_set_id}, [voltage], [source_current], [sink_current,] [impedance], [setup_time], {(pinlist)}
```

Note
 If equation based testing is being used, you specify a DPS set ID instead of a
DPS set number.

Note
PSLV ALL
 only applies changes to all non-equation-based DPS
sets.

### PSLV?

```
PSLV? {dps_No|dps_set_id}, {(pinlist)}
```

returns:

```
PSLV {dps_No|dps_set_id}, [voltage], [source_current], [sink_current,] [impedance], [setup_time], {(pinlist)}
```

Note
PSLV? ALL
 returns information for non-equation-based DPS
sets only.

### Parameters

Note
 The settling time parameter (
setup_time
) of the PSLV command
and the
rise_...
 and
fall_...
 parameters of the
`PSSR, PSSR? -(Power Supply Slew Rate)`（raw: `120504.htm`）
 command exclude each other. This also applies to the
t_ms

equation parameter (see
`DPSPINS`（raw: `16886.htm`）
 and
`DPSPINS resources`（raw: `16887.htm`）
).

[表]
行 1:
  dps_No [跨 5 行]
  Needed for non-equation-based setup. [跨 2 列]
行 2:
  dps_No
  The identification number of the DPS set which you want to modify. The number must not
    exceed the maximum number allowed (as defined by the DSCP (Define System
    Control Parameter) command.
行 3:
  ALL
  Modifies all the existing fixed DPS sets.
行 4:
  PRM
  Modifies the primary DPS set.
行 5:
  ACT
  (Only for PSLV?) Displays the settings of the actual enabled DPS
    set.
行 6:
  dps_set_id
  Needed for equation-based setup. [跨 2 列]
    
    This parameter is derived as follows:
    
    100000*equation_set_no + 1000*specset_no+1
行 7:
  voltage
  The optional parameter voltage defines the output voltage (in V) of [跨 2 列]
    the DPS. Applicable value depends on the DPS type.
行 8:
  source_current
  The optional parameter defines the source current limit (ilimit_source) in [A]. The [跨 2 列]
    applicable value depends on the DPS type.
    
    The parameter defines the source and the sink current limit if both values are equal.
    
    The parameter defines only the source current limit if the
    sink_current parameter is used.
行 9:
  sink_current
  The extra parameter defines the sink current limit (ilimit_sink) in [A]. [跨 2 列]
    
    The parameter is required only if the source and sink current limits are set to different
    values. This parameter defines then the sink current limit while the source current limit
    is defined by the above source_current parameter.
    
    The parameter is not required if the current limits are programmed symmetrically to the
    same (absolute) value. Both, the source and the sink value are then defined by the
    source_current parameter.
    
    The query answer shows the sink_current parameter only if the
    programmed sink current limit is not symmetrical to the source current limit.
行 10:
  impedance
  The optional parameter sets the DPS output impedance. You can select: [跨 2 列]
    
    LOZ sets the DPS output impedance to low when the test system is in
    the disconnect state. The current limit remains at the same level as in the active state,
    while the force voltage is set to 0 V.
    
    HIZ sets the DPS output to high impedance when the test system is in
    the disconnect state. This sets the channel to the minimum possible current limit.
    HIZ is the default state for DPS-slot types. If it is applied to DC
    Scale cards, HIZ_R is used instead of HIZ.
    
    HIZ_R sets the DPS output to high impedance by switching the output
    relay off when the test system is in the disconnect state.
    
    Note that relay switching is slower than with HIZ.
    
    LOZ_HIZ combines LOZ with HIZ.
    First, the DPS is switched to 0 V with an unchanged current limit (just like in
    LOZ mode). After the output voltage has reached 0 V (±50 mV) or after
    a timeout of 1 second, the DPS pin is switched to high impedance. This combines the
    advantages of both modes. A capacitor on the load board is quickly discharged and then the
    DPS pin is switched to high impedance. This is safer when changing the DUT or DUT board
    after a disconnect.
    
    LOZ_HIZ_R combines LOZ with
    HIZ_R. First, the DPS is switched to 0 V with an unchanged current
    limit (just like in LOZ mode). After the output voltage has reached 0 V
    (±50mV) or after a timeout of 1 second, the DPS pin is switched to open. This combines the
    advantages of both modes. A capacitor on the DUT board is quickly discharged and then the
    DPS pin is switched to high impedance. This is safer when changing the DUT or the DUT
    board after a disconnect.
行 11:
  setup_time
  The optional parameter is an integer which specifies the settling time (in ms) of the [跨 2 列]
    DPS. All DPS's are synchronized so that they finish their settling periods at the same
    point in time. This is the point when the system is switched to the connect state. If there
    are, for example, two DPS's, one with a settling time of 10 ms, and the other with a
    settling time of 4 ms, then the second DPS will be started 6 ms after the first:
    
    The range is from -2147483647 up to 2147483646 ms.
    
    The default value is 0.
    Note setup_time has a resolution
    of ms (floating point values are rounded to nearest integer).
行 12:
  pinlist
  pinlist must contain the names of pins previously defined by the `DFPS`（raw: `98551.htm`） command. If more than one pin is specified, the names must be separated by commas. [跨 2 列]
    The character @ can be used to set the levels for all DPS pins.

### Example

```
PSLV 1,5.2,0.5,HIZ,15,(Vee)
```

This example sets the following parameters for device pin Vee:

DPS set 1

A voltage of 5.2 V

A current limit of 0.5 A

Minimum current limit when the test system is disconnected

A setup time of 15 ms

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.195_PSLV__PSLV__-__Power_Supply_LeVel.htm>` 的 `## Errors` 段。**不是转述。**
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

The DPS set number is out of range.

The programmed voltage is out of range.

The programmed current is out of range.

A communication error with the DPS occurs.

The programmed voltage reaches the overvoltage limit.

<!-- 报错节 end -->

## 是什么

**文档事实**：PSLV（Power Supply LeVel）为先前的 `DFPS` 命令定义过的通道设置 DPS 参数；`PSLV?` 返回已有设置。可设置的量包括输出电压（V）、source/sink 电流限值（A）、断开状态下的输出阻抗模式，以及 settle 时间（ms）。

**文档事实**：`voltage` 与电流限值的可取值取决于 DPS 类型。`source_current` 在 source 与 sink 限值相等时同时定义两者；若使用 `sink_current`，则 `source_current` 只定义 source 限值，`sink_current` 定义 sink 限值。查询只在 sink 限值与 source 限值不对称时输出 `sink_current`。

**文档事实**：非方程化（fixed）setup 用 DPS set 号；方程化 setup（equation based testing）用 `dps_set_id`，其导出式为 `100000*equation_set_no + 1000*specset_no+1`。`ALL` 只作用于全部非方程化的 fixed DPS set，`PSLV? ALL` 也只返回非方程化 DPS set 的信息；`PSLV? ACT` 显示实际启用的 DPS set 的设置。

**文档事实**：`setup_time` 是 DPS 的 settling 时间；所有 DPS 被同步为在同一时间点结束 settling，即系统切换到 connect 状态的那一刻。若两个 DPS 分别设 10 ms 和 4 ms，后者会比前者晚 6 ms 启动。取值 -2147483647…2147483646 ms，默认 0，分辨率为 ms（浮点值四舍五入）。

**文档事实**：`impedance` 决定 disconnect 状态下输出的处置方式：`LOZ` 把输出电压拉到 0 V 并保持电流限；`HIZ` 切到最小可能电流限（DPS-slot 类型的默认值，用于 DC Scale 卡时改用 `HIZ_R`）；`HIZ_R` 通过断开输出继电器实现高阻（比 HIZ 慢）；`LOZ_HIZ` / `LOZ_HIZ_R` 先按 LOZ 降到 0 V（±50 mV 或超时 1 s），再分别切到 HIZ / 断开。

**文档事实**：`PSLV` 的 `setup_time` 与 `PSSR` 的 `rise_...` / `fall_...` 参数互斥，也与 `DPSPINS` 的 `t_ms` 方程参数互斥。

## 典型用法

**文档事实**：`PSLV 1,5.2,0.5,HIZ,15,(Vee)`——对器件引脚 Vee 使用 DPS set 1，输出电压 5.2 V、限流 0.5 A、断开时 HIZ、setup time 15 ms。

**文档事实**：查询语法为 `PSLV? {dps_No|dps_set_id}, {(pinlist)}`，返回一条与设置命令同参数形式的 `PSLV ...` 行。

**文档事实**：`pinlist` 中的引脚必须先用 `DFPS` 定义；多个引脚用逗号分隔；字符 `@` 表示对所有 DPS 引脚设置。

**建议**：若同一 DPS 还要用 PSSR 配置上升/下降斜率，不要同时设置 PSLV 的 `setup_time`；文档规定二者互斥。

## 和谁有关

- `DFPS`：**文档事实**——PSLV 的 `pinlist` "must contain the names of pins previously defined by the DFPS command"；PSLV 只改已存在的 DPS 通道，不自己定义引脚。
- `DSCP`：**文档事实**——`dps_No` 不得超过 DSCP 定义的最大允许 DPS set 数。
- `PSSR`：**文档事实**——PSLV 与 PSSR 两篇都写明 PSLV 的 `setup_time` 与 PSSR 的 `rise_...`/`fall_...` 互斥；PSLV 的 Related information 也指向 PSSR。
- `DPSPINS` / `DPSPINS resources`：**文档事实**——`t_ms` 方程参数与 PSLV 的 `setup_time` 互斥；DPSPINS resources 页把 "HIZ in the PSLV command" 作为最小电流（min）的用法。
- `PSSL`：**文档事实**——PSSL 页说明，当 PSSL 设定的安全限被其他固件命令（例如 PSLV）超过时，固件报错。
- `PSLR`：**文档事实**——PSLR 页说明其设定的最大输出电压就是之后 PSLV 可编程的最大电压。
- `PSST`：**文档事实**——PSST 页说明 DPS 的 ON/OFF 状态由 PSLV 指定；断开时输出阻抗取当前 active DPS set 中的 `HIZ_R`、`HIZ` 或 `LOZ`。
- `SPST?` / `UPTD`：**文档事实**——SPST? 页把 PSLV 列为会修改 level 数据、从而置位受影响 specset 状态位的命令；UPTD 页说明使用 PSLV 会把 DPS 与 LEV 标志清 0，直到重新 setup。

## 版本

**文档事实**：Functional changes 记录：Introduced before SmarTest 6.3.2（早于文档集覆盖起点即已存在，不是 6.3.2 的变更）；SmarTest 6.5.3 解除与 PSSR 命令的依赖（"Excluding dependency with PSSR command"）；SmarTest 7.1.3 新增阻抗模式 `LOZ_HIZ` 与 `LOZ_HIZ_R`；SmarTest 7.2.0 新增 `sink_current` 参数。

## 出处

- `02_System_reference/02.06_Command_Reference/02.06.02.02.195_PSLV__PSLV__-__Power_Supply_LeVel.htm`——首段、语法/参数、示例、Errors、Related information 与 Functional changes 均取自本篇。
