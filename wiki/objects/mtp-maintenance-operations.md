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

（待补）

## 典型用法

（待补）

## 和谁有关

（待补）

## 版本

（待补）

## 出处

（待补）
