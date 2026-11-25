---
type: object
title: PCLK, PCLK? - (Pin CLocK)
layer: L1
stage: timing
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.175_PCLK__PCLK__-__Pin_CLocK.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# PCLK, PCLK? - (Pin CLocK)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **3,336 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.175_PCLK__PCLK__-__Pin_CLocK.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### PCLK

Fixed
timing:

```
PCLK{waveform_set}, {timing_set}, {period}, {(pinlist)}
```

Equation-based
timing:

```
PCLK {specset_id|"multi-port_spec"}, {timing_set}, {period}, {(pinlist)}
```

### PCLK?

Fixed
timing:

```
PCLK?{waveform_set},{timing_set},{(pinlist)} [,query_mode]
```

returns:

```
PCLK {waveform_set}, {timing_set}, {period}, {(pinlist)}
```

Equation-based
timing:

```
PCLK? {specset_id|"multi-port_spec"}, {timing_set}, {(pinlist|portlist)} [,query_mode]
```

returns:

```
PCLK {specset_id|"multi-port_spec"}, {timing_set}, {period}, {(pinlist)}
```

### Parameters

[表]
行 1:
  waveform_set
  Waveform Set Number. Enter PRM for the Primary Waveform Set, or an integer in
    the range 1 to the maximum number of allowed waveform sets. The
    maximum number is determined by `WSUS`（raw: `98878.htm`）. For the query command you can also enter
    ALL for all waveform sets.
行 2:
  specset_id
  Used for equation based timing. It is derived as follows:
    
    100 * equation_set_no + specset_no
    
    Note that if you change the period for an equation based timing setup,
    PCLK will only change the runtime value, not the setup value specified
    in the timing set.
行 3:
  multi-port_spec
  In the command, you cannot enter a multi-port specification unless the
    specification is associated with the default port, and no other ports are configured. This
    restriction does not apply to the query.
行 4:
  timing_set
  Timing Set Number. Enter PRM for the Primary Timing Set,
    ALL for all timing sets, or an integer in the range 1 to the maximum
    number of allowed timing sets. The maximum number is determined by `TSUS`（raw: `98817.htm`）.
行 5:
  period
  Enter the test system period in ns. The period range depends on the model. For the Pin Scale 800,
    the range is 2.5 ns to 31250 ns. All values entered (or queried
    regardless of query_mode) are in ns and will
    be rounded to nine digits after the decimal point (atto-seconds)
    according to the accuracy of the firmware. The power-on default
    value for all configured pins also depends on the model.
行 6:
  pinlist
  The name of the pin or pins whose period you want to define or read back. This
    parameter can also include groups previously created by `DFGP`（raw: `98546.htm`）.
    If more than one pin is to be included, the names must be separated with a comma. The
    symbol @ can be used to set or read the periods for all configured pins.
    If you do not use @, the firmware assumes asynchronous operation.
行 7:
  portlist
  In the query, you must specify a list of ports, if you have specified a multi-port
    specification for the first parameter.
行 8:
  query_mode
  In the query, you can specify whether the period specified by the user or the
    corrected period calculated by the system is to be returned. The allowed values are:
    
    WANT: The period defined by the user is returned. This is also the
    default.
    
    EXACT: The period calculated by the system is returned.

### Examples

### Example 1
```
PCLK 101,1,20,(@)
```

This example sets the
test system period for specification 101 to 20 ns.

### Example 2
```
PCLK 101,1,40,(S1)
```

This example sets the
test system period of pin S1 for specification 101 to 40 ns.

The
`VCLK?`（raw: `98844.htm`）
 query checks whether a
PCLK
 command with the specified
parameter values was accepted with or without auto-correction.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.175_PCLK__PCLK__-__Pin_CLocK.htm>` 的 `## Errors` 段。**不是转述。**
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

waveform_set
 is greater than the range allowed by the
`WSUS`（raw: `98878.htm`）
 command.

timing_set
 is greater than the range allowed by the
`TSUS`（raw: `98817.htm`）
 command.

The period lies outside the given range.

<!-- 报错节 end -->

## 是什么

**文档事实** PCLK（Pin CLocK）定义指定 waveform set（equation based timing 下为 equation set）与 timing set 的测试系统周期。pinlist 使用 `@` 时所有已配置 pin 取同一周期，否则按 pin 分别编程周期。

**文档事实** 周期以 ns 为单位输入；不论写入还是查询，值都以 ns 表示，并按固件精度舍入到小数点后 9 位（atto-second）。周期范围与所有已配置 pin 的上电默认周期都取决于机型；文档举例如 Pin Scale 800 为 2.5 ns 至 31250 ns。

**文档事实** equation based timing 下第一个参数是 `specset_id`，由 `100 * equation_set_no + specset_no` 导出。对 equation based timing 用 PCLK 改周期只改运行时值，不改 timing set 中定义的 setup 值。

**文档事实** period resolution 会影响写入值：若用 `@` 改 timing set 1 的周期，且此前没有显式定义 period resolution（例如用 CLKR），系统会重新计算 period resolution，使新周期成为它的整数倍；这可能连带产生 timing set > 1 的新自动修正。若改的是 timing set > 1 的周期，而该值不是实际 period resolution 的整数倍，则指定值会被修正。

**文档事实** PCLK? 可返回用户指定的值；对 timing set > 1 还可返回实际使用的修正值。`query_mode` 选择返回哪一种：`WANT` 返回用户定义周期（默认），`EXACT` 返回系统计算的周期。

**文档事实** 文档在 fixed timing 下写明：若 timing set 号大于 TSUS 定义的最大允许 timing set 数，会创建新的 timing set；给定 waveform set 大于 WSUS 定义的最大允许 waveform set 数时也会创建新的 waveform set。同一页 Errors 段则把「waveform_set 超出 WSUS 允许范围」「timing_set 超出 TSUS 允许范围」列为报错条件。

**推断** 上一条的「超出即新建」与「超出即报错」两种表述在文档中并存，且文档未说明二者如何分界；实际以机台行为为准，本页不代为判定。

**文档事实** 参数说明还写：命令（非查询）中只有 specification 关联默认 port、且未配置其他 port 时才能输入 multi-port specification；查询不受此限制。Restrictions for multiport setups 页进一步说明不能用 PCLK 改 multi-port specification 内的周期，但可用 PCLK? 查询。

**文档事实** 文档把 PCLK 归入 Timing Setup，指向 Timing Setup Commands 一章。

## 典型用法

**文档事实** `PCLK 101,1,20,(@)` 把 specification 101 的测试系统周期设为 20 ns（作用于所有已配置 pin）。

**文档事实** `PCLK 101,1,40,(S1)` 把 specification 101 下 pin S1 的周期设为 40 ns。

**文档事实** pinlist 可包含 DFGP 先前创建的 pin group；多个 pin 用逗号分隔；`@` 表示所有已配置 pin；不使用 `@` 时固件按 asynchronous operation 处理。

**文档事实** 查询时可附 `query_mode`，用 `EXACT` 可读回系统实际使用的周期，而不只是写入值。

**文档事实** 文档用 VCLK? 检查带相同参数的 PCLK 是否被接受，以及是否经过自动修正。

**建议** 需要区分「我写入的值」与「机台修正后实际使用的值」时，成对使用 PCLK 与 `PCLK? ... EXACT`，并在变更后重新确认 timing set > 1 的周期未被连带修正。

## 和谁有关

- **文档事实** CLKR —— 用 CLKR 定义 period resolution 后，系统在全局（所有 pin）改 timing set 1 周期时不再重算它；CLKR 在 equation based timing 下也只改运行时值。这正是 PCLK 自动重算行为的开关。
- **文档事实** WSUS / TSUS —— 分别给出允许的 waveform set 与 timing set 上限，直接决定 PCLK 的合法参数范围（见 Errors 段）。
- **文档事实** VCLK? —— 专门校验 PCLK 是否被接受、是否发生 auto-correction。
- **文档事实** DFGP —— PCLK 的 pinlist 可引用它创建的 pin group。
- **文档事实** SPST —— 执行 PCLK（连同 ETIM/ETDS、CLKR、DRLV、RCLV、TERM、PSLV）会为受影响的 specset 自动置位，restore 应恢复原 SPST 状态。
- **文档事实** UPTD —— 使用 PCLK 会把 edge attributes setup 的 up-to-date 标志置 0，直到该 setup 被保存或加载。
- **文档事实** VTIM —— 其示例用 PCLK? 对比同一 port 两个 timing set 中 S1_1 与 DS0_1 的周期。
- **文档事实** Defining the global period（`02.06.06.01.04.01.01`）—— 把 PCLK 列为读取和修改周期的命令，并强调只是临时改运行时值、不改 timing set 中的值。
- **文档事实** Restrictions for multiport setups（`02.06.06.01.04.01.01.01`）—— 不能用 PCLK 改 multi-port specification 内的周期，PCLK? 查询可以。
- **建议** 在 [[timing]] 阶段做周期调试时，先用 PCLK? 记录原值再改；改完用 VCLK? 或 SPST 相关状态确认影响面。

## 版本

**文档事实** Functional changes 仅记「Introduced before SmarTest 6.3.2」，未列其他版本差异。

## 出处

- `02_System_reference/02.06_Command_Reference/02.06.02.02.175_PCLK__PCLK__-__Pin_CLocK.htm` —— 主源：正文、Parameters、Application、Errors、Examples、Functional changes。
- `02_System_reference/02.06_Command_Reference/02.06.06.01.04.01.01_Defining_the_global_period.htm` —— 读了其 Related firmware commands 段，确认 PCLK 只临时改运行时值。
- 其余跨页条目（CLKR、WSUS、TSUS、VCLK、DFGP、SPST、UPTD、VTIM、multiport 限制）取自各页被 PCLK 引用的语境句，未整篇通读。
