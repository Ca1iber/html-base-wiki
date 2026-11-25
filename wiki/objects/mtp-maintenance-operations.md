---
type: object
title: Maintenance operations
layer: n/a
stage: testmethod
tags: []
related: []
sources:
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.12_Maintenance_operations.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Maintenance operations

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **4,677 字符逐字取自** `<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.12_Maintenance_operations.htm>` 及其子主题 `<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.12.02_Enabling_and_disabling_maintenance_operations_in_APG_program_file.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.12.04_Reusable_maintenance_operations.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Examples

### Structure example

This example assumes a maintenance operation period
taken from the data sheet of a memory device with a maintenance operation period of 300 ns. The
test system cycle period is 100 ns. This causes a maintenance operation subroutine to be called
on test system cycles 3, 6, ... as shown in the example below.

If the test system cycle period is reduced to 50 ns and the maintenance operation
period remains 300 ns long, the maintenance operation subroutine is called on test system cycle
number 6 as shown in the example below.

Note
 The maintenance operation period numbers in the above examples
differ from the numbers for common memory devices. They are used just to explain the maintenance
operation concept.

### Code example
```
main ()
{
// write device
for (rowAddr=0 ; rowAddr<rowMax; rowAddr+=1)
{
// no maintenance operation allowed during full device write
is {}
for (colAddr=0 ; colAddr<colMax ; colAddr+=1)
{
write (rowAddr, colAddr, data);
}
}

// read device
for (rowAddr=0 ; rowAddr<rowMax; rowAddr+=1)
{
// no maintenance operation allowed during burst read
// maintenance operation can occur in between bursts
for (colAddr=0 ; colAddr<colMax ; colAddr+=burstLength)
{
is {}
read_burst (rowAddr, colAddr, data);
}
}
}
```

### Examples（取自子主题 Enabling and disabling maintenance operations in APG program file）

### Example 1

Set up a single dynamic refresh maintenance operation. It is
requested to enable and disable the refresh manually in the program.

In the
`Device architecture file`（raw: `68405.htm`）
:

```
:maintenanceOperation:
{
:name: dynamic_compensated_refresh
:table:
{
:format:
{ :operation: :subroutine: :timerMode: :intervalMode: }
{ maintop_time_a dynamic_refresh dynamic compensated }
}
}
```

In
the
`APG pattern file`（raw: `68403.htm`）
:

```
...
:maintenanceOperation: dynamic_compensated_refresh
...
```

In
the
`Timing file`（raw: `101980.htm`）
:

```
SPECS
cycleTime [ns]
refreshTime [ns]
TIMINGSET 1 "withRefresh
period = cycleTime
maintop_time_a = refreshTime
PINS
...
```

In
the
`program file`（raw: `67572.htm`）
:

```
dynamic_refresh()
{
...
}
main()
{
REFRESH_CTRL(STOP);
for(i=0;i<loopSize;i++)
{
WriteBackground();
}
REFRESH_CTRL(START);
...
...
}
```

### Example 2

Set up a multiple static refreshes maintenance
operation.

In the
`Device architecture file`（raw: `68405.htm`）
:

```
:maintenanceOperation:
{
:name: static_multiple_refreshes
:table:
{
:format:
{ :operation: :subroutine: :timerMode: :intervalMode: }
{ static_maintop_time_a static_routine_a static accumulated }
{ static_maintop_time_b static_routine_b static accumulated }
}
}
```

In
the
`APG pattern file`（raw: `68403.htm`）
:

```
...
:maintenanceOperation: static_multiple_refreshes
...
...
...
:timing:
{
:file: "../../../timing/staticRefTest_x6.tim"
:eqns: "functional-refresh"
:tims: "standard"
:spec: "1333-999_32ms"
}
...
```

In
the
`Timing file`（raw: `101980.htm`）
:

```
SPECS
cycleTime [ns]
refreshTime_a [ns]
refreshTime_b [ns]
TIMINGSET 1 "standard"
period = cycleTime
static_maintop_time_a = refreshTime_a
static_maintop_time_b = refreshTime_b
PINS
...
```

In
the
`program file`（raw: `67572.htm`）
:

```
static_routine_a()
{
...
}
static_routine_b()
{
...
}
main{)
{
REFRESH_CTRL(START, static_maintop_time_a); //Enable maintenance operation by enabling the static_a refresh
writeBackground();

readBackground();

REFRESH_CTRL(SWITCH, static_maintop_time_b); //Disable static_a and enable static_b, reset refreshCount() to 0.

readBackgroundB();

REFRESH_CTRL(SWITCH, static_maintop_time_a, refreshCount()%4 == 0);
//If the refresh insertion count of static_b is multiple of 4, disable static_b and enable static_a,
//and reset refreshCount() to 0.
//If the refresh insertion count of static_b is not multiple of 4, this switch action becomes pending.

readBackgroundB();
//If the above switch action has been pending, the static_b refresh is still enabled.
//Once the static_b refresh insertion count recorded by refreshCount() reaches multiple of 4,
//this pending switch action will be executed, which disables static_b and enables static_a,
//and resets refreshCount() to 0.

REFRESH_CTRL(STOP, refreshCount()%4 == 0);
//If the refresh insertion count of static_a is multiple of 4, disable maintenance operation immediately.
//If the refresh insertion count of static_a is not multiple of 4, MTL throws an error here because
//a pending disabling action exits after a pattern ends.

// MTL compiler will show a warning if the condition is never met before the pattern ends.

}
```

### Example（取自子主题 Reusable maintenance operations）

```
#include "../../device_defs/access_defs/ddr3_operations.inc"

distributed_refresh_routine()
{
// Issue a Refresh command.
Refresh();
Idle(tRFC-1);
}

allcore_refresh_routine()
{
for (x = xStart ; x < xStop; x+=1)
{
// Issue a Refresh command.
Refresh();
Idle(tRFC-1);
}
}
```

<!-- 语法节 end -->

## 是什么

- **文档事实** — Maintenance operations 是器件测试期间需要定期执行的程序，最常见的是 refresh；由一系列 vectors（由 device accesses 与其他指令编译而来）和一个执行 interval 组成，MTP 据此自动调度，不需要手工插入 test pattern。
- **文档事实** — 维护周期在 Timing file 中用 `maintop_time_a`（single refresh）或 `static_maintop_time_x`（x 可为任意字母，multiple refreshes）指定；最长 9.2 秒（228 倍 test system period），最短 16 倍 test system period。
- **文档事实** — 类型分 single refresh（static 与 dynamic timer mode 都支持；static 支持 single-port 与 multiport）和 multiple refreshes（只有 static 支持；同一时刻只允许一个 refresh，可在 refresh 之间 switch）。
- **文档事实** — 是否插入由波形类型决定：refresh counter 到 0 后，refresh 在 pattern stream 中下一个 interruptible waveform（index 小于 0x80）执行；这要求 replicated wavetables，即每个 waveform 各出现两次（normal/interruptible 与 non-interruptible）。
- **文档事实** — 用 `is{}` 或 `nis{}` 标记可/不可中断位置：`is{}` 表示程序整体不可中断、只在 `is{}` 处可中断（花括号必须为空）；`nis{}` 表示整体可中断、只在花括号内不可中断；同一程序只能二选一，sequencer mode 的 pins 只能含 `is{}`。
- **文档事实** — Timer mode 分 static 与 dynamic：static 编译进 pattern，可在 tester cycle 边界之间执行，但周期/间隔改动需重新编译，不能与 accumulated interval mode 同用；dynamic 由硬件 counter 在 runtime 执行，只在 tester cycle 边界执行、改设置无需重编译，但只支持 single refresh，且不支持 DC Scale card DPS128/64。
- **文档事实** — Interval mode 分 compensated（从 memory pattern 起点按周期累加）与 accumulated（从上次实际执行点起算）；accumulated 与 static refresh 同用需要 HSM3G 或 HSM6800 卡。
- **文档事实** — 使用 vector mode 需要在 pin mapping file 的 `interruptCtrl` 语句中指定 `VEC`，或把 `interrupCtrl` pin attribute 设为 `VEC`（原文两处拼写不一致）。
- **文档事实** — PMU 类型 DC events 会中断 pattern 执行，中断可达 1.3 ms，可能超过 DUT 的最大 refresh interval；使用这类事件时写 pattern 要考虑该影响。

## 典型用法

- **文档事实** — 结构示例：maintenance period 300 ns、test system cycle 100 ns 时，维护子程序在第 3、6、… 个 test system cycle 被调用；若 cycle 缩短为 50 ns、周期仍 300 ns，则在第 6 个 cycle 调用。
- **文档事实** — 代码示例用 `is {}` 标出 full device write 与 burst read 期间允许维护的位置（burst 之间）。
- **文档事实** — 启用 single dynamic refresh：Device architecture file 的 `:maintenanceOperation:` 表给出 `:name:` 与 operation/subroutine/timerMode/intervalMode；APG pattern file 用 `:maintenanceOperation:` 引用；Timing file 设 `maintop_time_a = refreshTime`；program file 用 `REFRESH_CTRL(STOP)` / `REFRESH_CTRL(START)` 手动开关。
- **文档事实** — 多个 static refresh：Device architecture file 定义多条 `static_maintop_time_a/b` 记录；Timing file 分别赋 `refreshTime_a/b`；program 用 `REFRESH_CTRL(START, ...)`、`REFRESH_CTRL(SWITCH, ...)`、`REFRESH_CTRL(STOP, ...)` 与 `refreshCount()` 控制切换和计数。
- **文档事实** — Reusable maintenance operations 示例把 refresh 例程写成普通子程序（`distributed_refresh_routine`、`allcore_refresh_routine`），通过 include 复用。

## 和谁有关

- [[timing-file]] — 维护周期 `maintop_time_a` / `static_maintop_time_x` 在此定义。
- [[device-architecture-file]] — `:maintenanceOperation:`、`:timerMode:`、`:intervalMode:` 在此配置。
- [[apg-pattern-file]] — 用 `:maintenanceOperation:` 引用维护操作，并可用 `:timing:` 指定 timing。
- [[apg-program-file]] — maintenance routines 是普通子程序；`is{}`/`nis{}` 与 `REFRESH_CTRL` 在此使用。
- [[pin-mapping-file]] — vector mode 的 `interruptCtrl` / `VEC` 在此指定。
- [[wavetable-file]] 与 [[wavetable]] — 维护操作依赖 replicated wavetables，non-interruptible sequence 的 waveform index 需在 0x80–0xFF。
- [[dps128-dps64-cards]] — dynamic mode 不支持 DC Scale DPS128/64。
- [[mtp-memory-test]] — 本页位于 Memory Test Plus（MTP）7.10.2 章，是该章文档树的一部分。

## 版本

- **文档事实** — "Introduced before SmarTest 6.3.2"；这是哨兵值，表示文档集覆盖范围之前已存在，不是 6.3.2 的变更。
- **文档事实** — "MTP 3.0.1: New mode for dynamic refresh: sequencer"。
- **文档事实** — "MTP 3.0.1: PMU type DC events may prevent timely refreshes"。
- **文档事实** — "MTP 3.0.1: Maintenance operation can be enabled and disabled under program control"。
- **文档事实** — "MTP 3.0.3: (MTP on SOC 103.0.0) The sequencer mode is now available in both MTP on HSM and MTP on SOC"。
- **文档事实** — "MTP 3.1.6: (MTP on SOC 103.3.0) Multiple static refreshes maintenance operation is available in both MTP on HSM and MTP on SOC"。
- **文档事实** — "MTP 3.1.6: (MTP on SOC 103.3.0) The static refresh supports multiport operation"。
- **文档事实** — "MTP 3.1.6: (MTP on SOC 103.3.0) New keyword: static_maintop_time_x (x can be any given letter) is added for the multiple refreshes maintenance operation periods."

## 出处

- 主文档 `02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.12_Maintenance_operations.htm`（`show.py 02.12.03.04.12` / `objpack.py`）。
- 语法节的 Example 另取自 `02.12.03.04.12.02_Enabling_and_disabling_maintenance_operations_in_APG_program_file.htm` 与 `02.12.03.04.12.04_Reusable_maintenance_operations.htm`。
