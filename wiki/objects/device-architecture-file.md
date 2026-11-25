---
type: object
title: Device architecture file
layer: file
stage: pattern
tags: []
related: []
sources:
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.05_Device_architecture_file.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Device architecture file

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **10,838 字符逐字取自** `<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.05_Device_architecture_file.htm>` 及其子主题 `<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.02_APG_pattern_file.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03_APG_program_file.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.04_Device_access_file.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.06_Pin_mapping_file.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.08_DC_event_file.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.12.02_Enabling_and_disabling_maintenance_operations_in_APG_program_file.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.12.04_Reusable_maintenance_operations.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.12_Maintenance_operations.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example

This is an example of a device architecture file for an DRAM device. It contains
address scrambling, bit inversion, cyclic redundancy checks, and device parameter
definitions.

```
:deviceArchitecture:
{
:version: 1.0
:scramble:
{
:name: "address scrambling"
:table:
{
:format:
{ :bit: :expression: }
{ xa0 "not x0" }
}
}
:bitInversion:
{
:name: "bit inversion"
:table:
{
:format:
{ :bit: :expression: }
{ d[0..7] x0 }
}
}
:bitOrdering:
{
:name: "bit ordering"
:table:
{
:format:
{ :bit: :expression: }
{ d[15..0] "not x1" }
{ d[0..15] x1 }
}
}
:crc:
{
:name: "my_crc"
:bitExpression:
{
:name: "my_crc_expression"
:table:
{
:format:
{ :bit: :expression: }
{ "0" "e[0]^e[8]" }
{ "1" "e[1]^e[9]" }
{ "2" "e[2]" }
{ "3" "e[3]" }
{ "4" "e[4]" }
{ "5" "e[5]" }
{ "6" "e[6]" }
{ "7" "e[7]" }
}
}
:bitSequence:
{
:name: "my_crc_bitOrder"
:table:
{
:format:
{ :pinList: :sequence: }
{ DQ.000,DQ.008,DQ.016,DQ.024 [0..1] }
{ DQ.001,DQ.009,DQ.017,DQ.025 [2..3] }
{ DQ.002,DQ.010,DQ.018,DQ.026 [4..5] }
{ DQ.003,DQ.011,DQ.019,DQ.027 [6..7] }
{ DQ.004,DQ.012,DQ.020,DQ.028 [8..9] }
{ DQ.005,DQ.013,DQ.021,DQ.029 [10..11] }
{ DQ.006,DQ.014,DQ.022,DQ.030 [12..13] }
{ DQ.007,DQ.015,DQ.023,DQ.031 [14..15] }
{ dbii.000,dbii.001,dbii.002,dbii.003 [16..17] }
}
}
:configuration:
{
:name: "crcConfig1"
:bitSequence: "my_crc_bitOrder"
:bitExpression: "my_crc_expression"
}
}
:maintenanceOperation:
{
:name: BurstRefresh
:table:
{
:format:
{ :operation: :subroutine: }
{ maintop_a refreshBurst }
}
}
:deviceParam:
{
:format:
{ :name: :value: }
{ xBits 10 }
{ yBits 8 }
{ dBits 16 }
}
}
```

### Example（取自子主题 APG pattern file）

```
:apgPattern:
{
:apgProgram: "refresh_routines.prog"
:deviceAccess: "../../device_defs/access_defs/ddr3_64Mx8_x4.dvac"
:deviceArchitecture: "../../device_defs/arch_defs/ddr3_64Mx8.dvar"

:pinMap: "../../device_defs/pin_maps/ddr3_64Mx8.pmap"
:waveformMap: "../../device_defs/waveform_maps/ddr3_x4.wmap:PreDefined"

:nullData: 0
:scramble: ""
:dataScramble: ""
:bitInversion: ""
:bitOrdering: ""

:maintenanceOperation: "allcore_refresh"

:programParam:
{
:format:
{ :name: :value: }

# tCK based Device timing parameters
# - based on 1066: tCK period 1.875ns.
# - based on 64Mx8 = 512Mb --> tRFC=90ns

{ tRFC 48 }

}
}
```

### Example（取自子主题 APG program file）

```
// solid.prog

#include "../../device_defs/access_defs/ddr3_operations.inc"
#include "../basic_access_sequences.inc"

main ()
{

// for debugging purposes un-comment the next 3 lines for a small core...
#define zStop 4
// #define yStop 64
// #define xstop 128

for (bank=zStart; bank<zStop; bank+=1)
{
WriteBackground(bank,DW1,DW2,DW3,DW4,DW5,DW6,DW7,DW8);
ReadBackground(bank,DW1,DW2,DW3,DW4,DW5,DW6,DW7,DW8);
}

for (bank=zStart; bank<zStop; bank+=1)
{
WriteBackground(bank,IDW1,IDW2,IDW3,IDW4,IDW5,IDW6,IDW7,IDW8);
ReadBackground(bank,IDW1,IDW2,IDW3,IDW4,IDW5,IDW6,IDW7,IDW8);
}

pad(EndProgPad){}
}

//*************************************************/
//**** Subroutines ********************************/
//*************************************************/

EndProgPad()
{
CLK(); CTRL(1,1); DES(); DBUS_IDLE();
}
```

### Example（取自子主题 Device access file）

```
:deviceAccess:
{
:version: 1.0
:deviceParam:
{ xBits yBits dBits }
:groups:
{
:format:
{ :name: :size: }
{ x_address 10 }
{ y_address 8 }
{ data 16 }
}

:apgAccess:
{
:name: write_access
:interface:
{ xAddr yAddr dataw }
:table:
{
:format:
{ :pin: :states: :data: }
{ CS_ {0 1} 0 }
{ OE_ {0 1} 1 }
{ WE_ {0 1} 0 }
{ BHE_ {0 1} 0 }
{ BLE_ {0 1} 0 }
{ x_address (0 1} xaddr(xAddr,yAddr) }
{ y_address {0 1} yaddr(xAddr,yAddr) }
{ data {L H} data(dataw,xAddr,yAddr) }
}
}

:apgAccess:
{
:name: read_access
:interface:
{ xAddr yAddr dataw }
:table:
{
:format:
{ :pin: :states: :data: }
{ CS_ {0 1} 0 }
{ OE_ {0 1} 0 }
{ WE_ {0 1} 1 }
{ BHE_ {0 1} 0 }
{ BLE_ {0 1} 0 }
{ x_address {0 1} xaddr(xAddr,yAddr) }
{ y_address {0 1} yaddr(xAddr,yAddr) }
{ data {L H} data(dataw,xAddr,yAddr) }
}
}

:apgAccess:
{
:name: "NMT_Rx6"
:interface: { ... }
:table:
{
:format:
{ :pin: :states: :data: :operation: }
{ Rx6.000 {0 1} 0 ~ }
{ ~ {0 1} 0 crc(NMT_Rx6_crc,6)[0] }
{ ~ {0 1} 0 crc(NMT_Rx6_crc,5)[0] }
}
}
}
```

### Example（取自子主题 DC event file）

```
:dcTest:
{
:dcSet:
{
:name: vBump
:table:
{
:format:
{ :dcEvent: :pinList: :dcSetup: :type: }
{ forceLow VDD,VDDQ vBump,1 dcscale }
{ forceHigh VDD,VDDQ vBump,2 dcscale }
{ forceDefault VDD,VDDQ vBump,3 dcscale }
}
}

:dcSet:
{
:name: IDD
:table:
{
:format:
{ :dcEvent: :pinList: :dcSetup: :type: }
{ setRange VDD IDD,0 dcscale }
{ measure VDD IDD,1 dcscale }
}
}

:dcSet:
{
:name: forceMeasure
:table:
{
:format:
{ :dcEvent: :pinList: :dcSetup: :type: }
{ setRange VDD,VDDQ forceMeasure,0 dcscale }
{ forceLow VDD,VDDQ forceMeasure,1 dcscale }
{ forceDefault VDD,VDDQ forceMeasure,2 dcscale }
{ measureLow VDD,VDDQ forceMeasure,3 dcscale }
{ measureDefault VDD,VDDQ forceMeasure,4 dcscale }
}
}

:dcSet:
{
:name: randomPowerUp
:table:
{
:format:
{ :dcEvent: :pinList: :dcSetup: :type: }
{ force0 VDD,VDDQ powerUp,0 dcscale }
{ force1 VDD,VDDQ powerUp,1 dcscale }
{ force2 VDD,VDDQ powerUp,2 dcscale }
{ force3 VDD,VDDQ powerUp,3 dcscale }
{ force4 VDD,VDDQ powerUp,4 dcscale }
}
}

:dcSet:
{
:name: modulation
:table:
{
:format:
{ :dcEvent: :pinList: :dcSetup: :type: }
{ force1400 VDD,VDDQ modulation,1 dcscale }
{ force1450 VDD,VDDQ modulation,2 dcscale }
{ force1475 VDD,VDDQ modulation,3 dcscale }
{ force1500 VDD,VDDQ modulation,4 dcscale }
{ force1550 VDD,VDDQ modulation,5 dcscale }
{ force1600 VDD,VDDQ modulation,6 dcscale }
}
}
}
```

### Example（取自子主题 Pin mapping file）

```
DM.000=DM
DM=DM_Bus

DQi.007=DQ_i.07
DQi.006=DQ_i.06
DQi.005=DQ_i.05
DQi.004=DQ_i.04
DQi.003=DQ_i.03
DQi.002=DQ_i.02
DQi.001=DQ_i.01
DQi.000=DQ_i.00
DQi=DQi_Bus

DQo.007=DQ_o.07
DQo.006=DQ_o.06
DQo.005=DQ_o.05
DQo.004=DQ_o.04
DQo.003=DQ_o.03
DQo.002=DQ_o.02
DQo.001=DQ_o.01
DQo.000=DQ_o.00
DQo=DQ_Bus

DQSi.001=DQS_i
DQSi.000=DQSn_i
DQSi=DQSi_DiffBus

DQSo.001=DQS_o
DQSo.000=DQSn_o
DQSo=DQS_DiffBus

Bank.002=BA.2
Bank.001=BA.1
Bank.000=BA.0
Bank=Bank_Addr_Bus

Address.012=A.12
Address.011=A.11
Address.010=A.10
Address.009=A.09
Address.008=A.08
Address.007=A.07
Address.006=A.06
Address.005=A.05
Address.004=A.04
Address.003=A.03
Address.002=A.02
Address.001=A.01
Address.000=A.00
Address=Address_Bus

CK=CK
CKn=CKn
CKE=CKE
CSn=CSn
RASn=RASn
CASn=CASn
WEn=WEn

RESETn=RESETn
ODT=ODT
```

### Examples（取自子主题 Maintenance operations）

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
