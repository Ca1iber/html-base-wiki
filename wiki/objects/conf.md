---
type: object
title: CONF, CONF? - (CONFiguration)
layer: L1
stage: project
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.31_CONF__CONF__-__CONFiguration.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# CONF, CONF? - (CONFiguration)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **3,398 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.31_CONF__CONF__-__CONFiguration.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### CONF

```
CONF ["context",]{pin_type},[pin_oper_mode],{(pinlist)}
```

### CONF?

```
CONF? ["context"|ALL,] {(pinlist)}
```

returns:

```
CONF ["context",]{pin_type},{pin_oper_mode},{(pinlist)}
```

### Parameters

[表]
行 1:
  context
  This extra parameter specifies a mode context. If it is omitted, the default mode context
    DEFAULT is set or read. If
    DEFAULT is the only context defined, the
    parameter is omitted in the query reply.
    
    The default mode context is predefined. All other mode contexts
    must be defined with the CTXT command.
    
    If you specify ALL in the query,
    CONF? will display all mode contexts.
行 2:
  pin_type
  The mandatory parameter assigns channel resources to the pin. This can be:
    
      [子表]
      子行 1:
        I
        Configures a drive pin.
      子行 2:
        O
        Configures a receive pin.
      子行 3:
        IO
        Configures a bidirectional pin.
      子行 4:
        DC
        Configures a pin for DC measurements.
          The pin is only connected to the PMU, and no
          driver or receiver resources are allocated to it.
          
          For DC Scale channels (power or signal pins)
          the mode is always DC.
          
          This option is not allowed for Smart Scale
          pins.
      子行 5:
        OFF
        The pin is not available for measurements.
行 3:
  pin_oper_mode
  The mandatory parameter defines or indicates the operating mode of the pins in
    pinlist. The operation mode can be:
    
      [子表]
      子行 1:
        DCSIGNAL
        In the query this indicates that the pin is
          associated with a DC Scale channel and has been
          configured in PMU mode with
          DFPN.
      子行 2:
        POWER
        In the query this indicates that the pin is
          associated with a DC Scale channel and has been
          configured in DPS mode with
          DFPS.
      子行 3:
        CMON
        Configures the pin as current monitor
          output. For more information, refer to `XPS256 current monitor`（raw: `354977.htm`）.
      子行 4:
        F160
        Specifies Standard operating mode. This
          is the default. It must be selected for pins on
          PS1600 boards.
      子行 5:
        F330
        Not valid.
      子行 6:
        FAST
        This operation mode must be selected for
          fast pins. Note that no pin can be set to
          FAST in the default mode
          context DEFAULT, and that no
          IO pin can be set to
          FAST.
          
          For Smart Scale pins this mode will be mapped
          to F160.
行 4:
  pinlist
  The name of the pin or pins to be configured or listed. If
    more than one pin is to be included, the names must be separated
    with a comma.
    
    The symbol @ can be used in the query to list all pins that were
    previously either explicitly configured with the
    CONF command, or (in the case of DC Scale
    pins) implicitly with the DFPN or
    DFPS command.

### Examples

### Example 1
```
> CONF IO,F160,(D0,D1)
```

This
example configures pins
D0
 and
D1
 as bidirectional
pins operating in Standard Mode for the default mode context.

### Example 2
```
> CONF? (sdd,vdd)
< CONF DC,DCSIGNAL,(sdd)
< CONF DC,POWER,(vdd)
```

This example queries the DC Scale channels

sdd
 and
vdd
, which were set with
`DFPN`（raw: `98550.htm`）
 to PMU mode (
DCSIGNAL
) and with

`DFPS`（raw: `98551.htm`）
 to DPS mode (
POWER
),
respectively.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.31_CONF__CONF__-__CONFiguration.htm>` 的 `## Errors` 段。**不是转述。**
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if you attempt to configure pins while
the sequencer is in the run or the break state (see the
SQST

command).

<!-- 报错节 end -->

## 是什么

**文档事实**：`CONF` 在指定的 mode context 内给 pin 赋予 pin type 和 operating mode；`CONF?` 返回指定 pin 的当前设置。

**文档事实**：`CONF` 也适用于 power pin / signal pin（即关联 DC Scale channel 的 pin），但只能确认由 `DFPN` 或 `DFPS` 定义的 operation mode（power 还是 signal）；查询可取回该 operation mode。power/signal pin 的 operation mode 在所有 mode context 中都相同。

**文档事实**：`context` 省略时使用预定义默认 context `DEFAULT`；其他 mode context 必须用 `CTXT` 定义。`CONF?` 中写 `ALL` 会显示所有 mode context。

**文档事实**：`pin_type` 取 `I`（drive pin）、`O`（receive pin）、`IO`（bidirectional pin）、`DC`（只接 PMU，不分配 driver/receiver；DC Scale channel 恒为 `DC`，Smart Scale pin 不允许此选项）或 `OFF`（该 pin 不用于测量）。

**文档事实**：`pin_oper_mode` 取 `DCSIGNAL`（查询结果表示该 pin 属 DC Scale channel，已用 `DFPN` 配成 PMU 模式）、`POWER`（查询结果表示属 DC Scale channel，已用 `DFPS` 配成 DPS 模式）、`CMON`（配成 current monitor 输出，见 XPS256 current monitor）、`F160`（Standard，默认；PS1600 board 上的 pin 必须选它）、`F330`（Not valid）、`FAST`（fast pin 必须选；`DEFAULT` 下任何 pin 都不能设 `FAST`，`IO` pin 不能设 `FAST`；Smart Scale pin 的该模式会映射为 `F160`）。

**文档事实**：`pinlist` 为逗号分隔的 pin 名；查询时可用 `@` 列出所有此前用 `CONF` 显式配置过、或对 DC Scale pin 用 `DFPN`/`DFPS` 隐式配置过的 pin。

## 典型用法

**文档事实**：把 `D0`、`D1` 配成默认 context 下的双向 pin，工作在 Standard Mode：

```
> CONF IO,F160,(D0,D1)
```

**文档事实**：查询 DC Scale channel `sdd`、`vdd` 的当前配置：

```
> CONF? (sdd,vdd)
< CONF DC,DCSIGNAL,(sdd)
< CONF DC,POWER,(vdd)
```

**文档事实**：查询时 `context` 可写 `ALL` 以列出所有 mode context，`pinlist` 可写 `@` 以列出所有已配置 pin。`CONF` 不能在 sequencer 处于 run 或 break 状态时执行（见 `SQST`）。

## 和谁有关

**文档事实**：以下关系均有来源文档中的正文、参数说明或回链证据支撑。

- [[dfpn]]、[[dfps]]：DC Scale pin 的 operation mode 由它们定义，`CONF`/`CONF?` 只能确认或查询；`CONF?` 的 `@` 也会列出被它们隐式配置的 pin。为什么：本页 Parameters 与 Example 2 明确写出。
- [[ctxt]]：非 `DEFAULT` 的 mode context 必须由 `CTXT` 定义，`CONF`/`CONF?` 的 `context` 参数依赖它（本页 Parameters 明确写出）。
- [[sqst]]：本页 `Errors` 说明 sequencer 在 run/break 状态时配置 pin 会报错，并指向 `SQST`。
- [[pals]]：`PALS` 文档要求它在包括 `CONF` 在内的任何其他 setup command 之前使用（回链证据）。
- [[uptd]]：`UPTD` 文档说使用 `CONF` 会把对应 setup 的 up-to-date 标志置 0，直到保存或加载（回链证据）。
- [[dsus]]、[[lsus]]、[[tsus]]：这几篇文档都称允许的 DPS / level / timing set 数 `as set by CONF, CONF? - (CONFiguration)`（回链证据）；本页正文没有展开这些上限。
- `XPS256 current monitor`（`02_System_reference/02.05_Test_Head_Cards/02.05.05.03.03.02_XPS256_current_monitor.htm`）：`CMON` 模式的说明直接指到这里。
- `Configuration Setup Commands`（`02_System_reference/02.06_Command_Reference/02.06.03_Pin_configuration_setup_commands.htm`）：本页 `Application` 指向该章，作为 pin configuration 的上文。

## 版本

**文档事实**：`Functional changes` 记录：

- `Introduced before SmarTest 6.3.2`——这是哨兵值，表示文档集覆盖范围之前已有，不能当作 6.3.2 的变更；
- SmarTest 7.1.3：`pin_oper_mode` 增加 `HV` 选项；
- SmarTest 7.3.1：新增 operating mode `STDDIFF`、`FASTDIFF`；
- SmarTest 7.10.2：新增 operating mode `CMON`。

**文档事实**：本页 `Parameters` 的 `pin_oper_mode` 列表只列出 `DCSIGNAL`、`POWER`、`CMON`、`F160`、`F330`、`FAST`，没有列 `HV`、`STDDIFF`、`FASTDIFF`；两处内容不一致，此处照原样记录。

## 出处

- 主源（「语法 / 参数」与「报错条件」的逐字来源）：`02_System_reference/02.06_Command_Reference/02.06.02.02.31_CONF__CONF__-__CONFiguration.htm`（正文、CONF/CONF?、Parameters、Application、Errors、Examples、Functional changes）。
- 回链证据：`02_System_reference/02.06_Command_Reference/02.06.03_Pin_configuration_setup_commands.htm`、`02.06.03.01.01_Introduction.htm`、`02.06.02.02.63_DFPN__DFPN__-__DeFine_Pin_Name.htm`、`02.06.02.02.65_DFPS__DFPS__-__DeFine_Power_Supply.htm`、`02.06.02.02.173_PALS__PALS__-__Pin_ALlocation_for_multiple_Sites.htm`、`02.06.02.02.306_UPTD__UPTD__-__UP_To_Date.htm`、`02.06.02.02.91_DSUS__DSUS__-__Dps_Sets_USed.htm`、`02.06.02.02.155_LSUS__LSUS__-__Level_Sets_USed.htm`、`02.06.02.02.283_TSUS__TSUS__-__Timing_Sets_USed.htm`。
