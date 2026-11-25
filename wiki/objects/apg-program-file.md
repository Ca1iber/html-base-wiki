---
type: object
title: APG program file
layer: file
stage: pattern
tags: []
related: []
sources:
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03_APG_program_file.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# APG program file

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **14,708 字符逐字取自** `<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03_APG_program_file.htm>` 及其子主题 `<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.02_APG_pattern_file.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01.01.01_Data_types_relevant_to_operators.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01.01.02_Index_operator.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01.01.03_Select_operator.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01.02_Loops.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01.03_Conditional_execution.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01.04_Other_control_structures.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01.08_Macros_and_functions_in_program_files.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01_APG_program_file_syntax.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.04_Device_access_file.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.05_Device_architecture_file.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.06_Pin_mapping_file.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.08_DC_event_file.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.12_Maintenance_operations.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example

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

### Syntax（取自子主题 APG program file syntax）

The APG program file syntax supports a subset of the C syntax. All supported syntax
elements are identical to the corresponding elements of C.

In particular, you can use in
APG program files:

All pre-processor statements (such as
#include
) supported by C

The operators listed in
`Operators`（raw: `101459.htm`）
.

For
 loops and
if
 statements

Subroutine definitions and calls

Arrays

`DC_EVENT() and DC_EVENT_RANGE()`（raw: `102814.htm`）
, predefined calls similar to
subroutine calls

Macros, function-like constructs that process data based on the current settings in the

`APG pattern file`（raw: `68403.htm`）

Some prominent elements of the C language that are not available:

Data typing exclude the array data type

Pointers and addresses

Loops other than
for
 loops

Functions returning values

### Syntax（取自子主题 Loops）

For
 loops and counted match loops in MTL use the standard C
syntax.

### Examples（取自子主题 Loops）

### for loops
```
for (i = 0; i < maxTest; i += 2)
{
... # any code here
}
```

Correct
nested
loop:

```
for (i = 0; i < 100; i += 1)
{
for (j = 0; j < 10; j += 1)
{
...
}
}
```

Incorrect
nested
loop:

```
for (i = 0; i < 100; i += 1)
{
for (j = 0; j < i; j += 1) # Incorrect code: the inner
{ # loop variable is compared
... # with the outer loop variable
}
}
```

### Counted match loops
```
countedMatch (10) // countedMatchWithBreak(n) for counted match loops with a break.
{
MATCH_WRITE_DQ (xAddr, yAddr, DW);
}
```

Note
 Do not use counted match loops in the APG program file and device access file at the
same time.

### Examples（取自子主题 Conditional execution）

### Example 1

This example demonstrates permitted and non-permitted uses of
the
if
 statement. See the program comments for
details.

```
v1 = 1;
v2 = 2;
v3 = 3;
for (x=0; x<100; x += 1)
{
if (x < 3) {NOP();} # Incorrect: x is the loop variable
v1 += 2;
if (v1 > 100) {NOP();} # Incorrect: v1 changes within the loop
if (v3 < 5) {NOP();} # Incorrect: v3 changes within the inner loop (below)
if (v2 == 1) {NOP();} # OK
for (y = 0; y < 32; y += 2)
{
v3 += 3;
if (x < 4) {NOP();} # Incorrect: x is the loop variable of the outer loop
if (v1 > 100) {NOP();} # Incorrect: v1 changes in the outer loop
if (v2 == 1) {NOP();} # OK
}
}
if (v1 < 50) {NOP();} # OK: v1 is used outside of any loop
```

### Example 2

When 'if' statements in subroutines, the
if

statement still have the same the limitations. For
example:

```
sub(var)
{
if (var > 0) {NOP();}
}

main()
{
v1 = 1;
for (x=0; x<100; x +=1)
{
sub(x); # Incorrect: x is the loop variable and is
# used in an if statement in the subroutine
sub(v1); # Correct: v1 does not change in the loop
}
}
```

### Example 3

This example shows using the conditional operator (
:
?
) with loop variables to develop a diagonal-like
pattern.

```
for(y=yStart;y<yStop;y++)
{
for(x=xStart; x < xStop; x++)
{
data = (x==y) ? 0:1;
write(data);
}
}
```

### Syntax（取自子主题 Other control structures）

```
is{}
nis{}
```

### Examples（取自子主题 Other control structures）

### Example 1
```
for (z=0; z<zMax; z+=1)
{
for (x=0; x<xMax; x+=1)
{
for (y=0; y<yMax; y+=burstLength)
{
WriteTransaction (0, x, y, z));
is {} /* device maintenance insertion point */
}
}
}
```

### Example 2
```
main ()
{
// write device
for (rowAddr=0 ; rowAddr<rowMax; rowAddr+=1)
{
// no maintenance operation allowed during full device write
nis {
nop(); // Note the nis body cannot start with a for loop
for (colAddr=0 ; colAddr<colMax ; colAddr+=1)
{
write (rowAddr, colAddr, data);
}
}
}

// read device
for (rowAddr=0 ; rowAddr<rowMax; rowAddr+=1)
{
// no maintenance operation allowed during burst read
// maintenance operation can occur in between bursts
for (colAddr=0 ; colAddr<colMax ; colAddr+=burstLength)
{
nis {
read_burst (rowAddr, colAddr, data);
}
}
}
}
```

### Syntax（取自子主题 Macros and functions in program files）

These functions and macros are available, listed in alphabetical order.

[表]
列: Keyword | Parameters and descriptions
行 1:
  DC_EVENT(<event>)
    
     .delay(<edges>)
  <event>: The name of the event that is to be executed. The
    event must be defined in the `DC event file`（raw: `99152.htm`）.
    
    <edges>: The delay of the event, measured in waveform edges. The
    delay() function property is optional.
    
    The delay is the time difference between the scheduled time of the event in the pattern
    and its actual execution. If the delay is negative, the event is executed before its
    scheduled time. The value is an expression; the expression may contain normal variables but
    not loop-dependent variables (that is, variables that change during a loop iteration).
    
    The delay() property cannot be used with pmu type
    DC events.
    
    The DC_EVENT function executes the specified DC event. It can be used
    in the `APG program file`（raw: `67572.htm`）.
行 2:
  DC_EVENT_RANGE(
    
     <sequence>,
    
     <parameters>)
    
     .maxRepeats(<num>)
    
     .initialDelay(<d>)
    
     {
    
     <instructions>
    
     }
  <sequence>: The name of the sequence that is to be
    executed. The event must be defined in the `DC event file`（raw: `99152.htm`） using the
    :dcSequence: keyword.
    
    <parameters>: The parameters that are passed to the sequence.
    Parameters are separated by commas.
    
    <num>: The maximum number of times that the specified sequence
    is to be executed. The maxRepeats() function property is optional.
    
    <d>: The amount by which the start of the sequence is delayed
    (relative to the beginning of the execution of the instructions in the macro body),
    measured in waveform edges. The initialDelay() function property is
    optional.
    
    <instructions>: Standard MTL program statements. While these
    statements are being executed, the specified sequence is executed on the DC Scale card
    (subject to the limit set in maxRepeats(), if that property is used.
    
    The DC_EVENT_RANGE function executes the specified sequence of DC
    events alongside the instructions in its body. It can be used in the `APG program file`（raw: `67572.htm`）.
行 3:
  pad(<paddingRoutine>)
    {}
  <paddingRoutine>: The name of the padding routine that is
    to be used. The routine must be specified as a subroutine in the `APG program file`（raw: `67572.htm`）
    without any arguments.
    
    The pad() {} macro applies padding in the location where it occurs, if
    such padding is needed. It can be used in the `APG program file`（raw: `67572.htm`）.
行 4:
  REFRESH_CTRL(<command>)
  Manually Enables or disables maintenance operations (refreshes) in the `program file`（raw: `67572.htm`）.
    
    <command>: Either START,
    STOP or SWITCH.
    
    See details in `Enabling and disabling maintenance operations`（raw: `118570.htm`）.

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

### Example（取自子主题 Device architecture file）

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

### Example（取自子主题 Data types relevant to operators）

The following examples demonstrates you data types for variables in the APG program
file.

```
a="hello"; //The data type for a is string.
a=5; //Error, because a has been a string variable and cannot be assigned with an integer value.

b="hello"; //The data type for b is string
b=b+1; //The value for b becomes to "hello1"

c=(1==1); //The data type for c is Boolean.
d=c?1:0; //The value for d is 1, and the data type for d is integer.

arr[3]={1,2,"hello"}; //Error, because the array is assigned with values of different data types (integers and string).
```

### Example（取自子主题 Index operator）

```
myVar = 0x55[2] # myVar is assigned the value 1
```

### Example（取自子主题 Select operator）

value[3]
: The third bit of
value
.

value[1,2,5]
: The first, second, and fifth bits of

value
.

value[6..8]
: The sixth, seventh, and eighth bits of

value
.

value[1..3,6,8]
: Bits one, two, three, six, and eight of

value
.

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
