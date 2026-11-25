---
type: object
title: APG pattern file
layer: file
stage: pattern
tags: []
related: []
sources:
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.02_APG_pattern_file.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# APG pattern file

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **33,020 字符逐字取自** `<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.02_APG_pattern_file.htm>` 及其子主题 `<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03.01_APG_program_file_syntax.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03_APG_program_file.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.04.01_Device_access_file_syntax.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.04.02_Macros_and_functions_in_device_accesses.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.04.03_Control_instructions_in_device_accesses.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.04_Device_access_file.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.05_Device_architecture_file.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.06.02_Buses.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.06.03_Reference_pins.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.06.04_Copying_vectors.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.06_Pin_mapping_file.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.07_Waveform_mapping_file.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.08_DC_event_file.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.03.01_Setting_up_direct_waveform_mapping.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.03.02_Setting_up_indirect_waveform_mapping.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.03.03_Automatic_waveform_generation.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.12.02_Enabling_and_disabling_maintenance_operations_in_APG_program_file.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.12.04_Reusable_maintenance_operations.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.12_Maintenance_operations.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example

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

### Example（取自子主题 Device access file syntax）

### Pin groups and the :data: column

Lets assume these settings for a device
access (with
PinGroup
 being a properly defined group of four
pins):

```
{ :pin: :states: :data: }
{ PinGroup { 0 1 } 0x5 }
{ ~ { 0 1 } 0x5 }
{ ~ { 0 1 } 0x5 }
{ ~ { 0 1 } 0x5 }
```

The
pins of PinGroup are then set like this:

PinGroup.000 is set to 0.

PinGroup.001 is set to 1.

PinGroup.002 is set to 0.

PinGroup.003 is set to 1.

### Syntax（取自子主题 Macros and functions in device accesses）

These macros are available, listed in alphabetical order.

[表]
列: Keyword | Parameters and descriptions
行 1:
  bitCount(<elements>,
    <bitState>)
  <elements>: The pins of the bus in question that are to be
    monitored. The pseudo-variable e can be used to avoid having to specify
    concrete pins. For example, e[2] refers to the second pin of the bus in
    the current configuration. e[] refers to all pins of the bus.
    
    <bitState>: The bit state that is to be counted; either 0 or 1.
    
    The bitCount function returns the number of bits among the specified
    elements that have the logical bit state given.
    
    The function can be used for specifying the conditions of `dbi`（raw: `103905.htm`） macros.
行 2:
  crc(<configuration>,
    <crcBit>)
  <configuration>: The CRC configuration that the
    crc macro is to use to returns the current CRC result.
    
    <crcBit>: The bit (from the bit list specified in the CRC
    configuration) from which the CRC result is to be calculated.
    
    If the pin list of the bit sequence specified in the chosen configuration includes
    multiple pins in each row, the result of the crc macro has multiple
    bits. You can access individual bits of the result using the `Select operator`（raw: `68467.htm`）.
    
    For example: crc(myConfig,0), crc(myConfig,0)[3],
    crc(myConfig,0)[5,2] (These examples assume that there is a configuration
    named "myConfig" in the :crc: block that is currently specified in the
    APG pattern file.)
    
    The crc macro can be used in the :operation:
    columns of device accesses. If it is used in a device access and CRC is globally enabled,
    the :data: column is ignored in that access.
行 3:
  data(<d>,<x>,<y>,<z>)
  <d>: The unscrambled data word.
    
    <x>: The unscrambled x address.
    
    <y>: The unscrambled y address.
    
    <z>: The unscrambled z address.
    
    The data macro scrambles data words by applying the current bit
    inversion and bit ordering tables specified in the `APG pattern file`（raw: `68403.htm`）.
    
    If fewer than four parameters are specified, the missing ones are considered to be zero.
    For example, data(0xff,1) would be the same as
    data(0xff,1,0,0). You must specify at least two parameters.
    
    Note that all parameters are masked with the respective device parameter from the `Device architecture file`（raw: `68405.htm`）, that is, dBits, xBits, yBits, and zBits. For example, when xBits is 8
    and the value provided as the unscrambled x address is 258, masking would convert it to
    2.
    
    The `Select operator`（raw: `68467.htm`） can be applied to data macro expressions to extract one or
    more individual bits.
    
    The data macro must be used on all pins for which you require `Reconstruction information`（raw: `103883.htm`）.
    
    The data macro can be used in the :data: columns of
    device accesses.
行 4:
  dbi(<configuration>)
  <configuration>: The DBI configuration that the
    dbi macro is to use.
    
    The dbi macro inverts the signals on a bus if a specified condition is
    met, as described in `Dynamic bus inversion`（raw: `103905.htm`）. The signal is inverted for all pins in each
    row in the specified DBI configuration that is completely part of the pins listed in the
    device access row in which the dbi macro is used. (See the DBI examples in the
    Examples section, below.)
    
    Inversion is applied after scrambling; it is applied before or after cyclic redundancy
    checks, depending on the order in which the operations are listed with the
    :operationOrder: keyword.
    
    The dbi macro can be used in the :operation:
    columns of device accesses. However, any device access containing the
    dbi macro cannot be used in padding routines.
行 5:
  xaddr(<x>,<y>,<z>)
  <x>: The unscrambled x address.
    
    <y>: The unscrambled y address.
    
    <z>: The unscrambled z address.
    
    The xaddr macro provides the scrambled x address by applying the
    current scrambling table specified in the `APG pattern file`（raw: `68403.htm`）.
    
    If fewer than three parameters are specified, the missing ones are considered to be zero.
    For example, xaddr(1,1) would be the same as
    xaddr(1,1,0).
    
    If no scrambling is specified, the macro returns the unscrambled x address.
    
    The xaddr macro can be used in the :data: column of the device access
    file. The `Select operator`（raw: `68467.htm`） can be applied to address macro expressions to extract one
    or more individual bits.
行 6:
  yaddr(<x>,<y>,<z>)
  The yaddr macro returns the scrambled y address. It is similar
    to xaddr, described above.
    
    Missing parameters are handled as follows:
    
    If there is only one parameter, that parameter is considered to be the unscrambled y
    address. For example: yaddr(1) is the same as
    yaddr(0,1,0).
    
    If there are two parameters, they are considered to be the unscrambled x and y
    addresses. For example: yaddr(1,2) is the same as
    yaddr(1,2,0).
行 7:
  zaddr(<x>,<y>,<z>)
  The zaddr macro returns the scrambled z address. It is similar
    to xaddr, described above.
    
    Missing parameters are handled as follows:
    
    If there is only one parameter, that parameter is considered to be the unscrambled z
    address. For example: zaddr(1) is the same as
    zaddr(0,0,1).
    
    If there are two parameters, they are considered to be the unscrambled x and z
    addresses. For example: zaddr(1,2) is the same as
    zaddr(1,0,2).

### Example（取自子主题 Macros and functions in device accesses）

### DBI examples

For all examples, the active DBI setup in the device
architecture file is assumed to
be:

```
:dbi:
{
:name: sample_dbi
:configuration:
{
:name: writeDBI
:condition: bitCount(e[], 0) >= 4
:table:
{
:format:
{ :bus: :flag: }
{ DQi[0..7] RDQSi[0] }
{ DQi[8..15] RDQSi[1] }
{ DQi[16..23] RDQSi[2] }
{ DQi[24..31] RDQSi[3] }
}
}
}
```

There
are assumed to be two subgroups of the DQi pin group, one called DQi.subgroup.0_15 (containing
pins 0 through 15), one called DQi.subgroup.4_11 (containing pins 4 through 11).

In the
following example, all DQi pins would be inverted if the condition was met, because all would be
listed in active DBI setup and in the row of the device access in which the

dbi
 macro is
called:

```
:apgAccess:
{
:name: Write
:table:
{
:format:
{:pin: :states: :data: :operation: }
{ DQi {0 1} data(dw,x,y) dbi(writeDBI) }
}
}
```

In
the next example, only pins DQi.000 through DQi.015 would be inverted upon fulfillment of the
condition, because only they are included in the device access'
:pin:

column:

```
:apgAccess:
{
:name: Write
:table:
{
:format:
{:pin: :states: :data: :operation: }
{ DQi.subgroup.0_15 {0 1} data(dw,x,y) dbi(writeDBI) }
}
}
```

In
this example, no pins would be inverted, because the pins included in the

:pins:
 column do not completely cover any of the four rows in the

:bus:
 column of the DBI
definition:

```
:apgAccess:
{
:name: Write
:table:
{
:format:
{:pin: :states: :data: :operation: }
{ DQi.subgroup.4_11 {0 1} data(dw,x,y) dbi(writeDBI) }
}
}
```

### for（取自子主题 Control instructions in device accesses）

A
for
 statement in the

:instruction:
 column causes all statements in the
:data:

and
:operation:
 columns between the
for
 and the

forend
 to be evaluated once for each loop. The number of loop repetitions is
determined by the arguments provided for
for
.

A loop begins with a
C-like statement
for (
<initialization>
;

<test>
;

<increment>
)
, where:

<initialization>
: The setup statement for the loop variable, for
example,
loopCount=1
.

<test>
: The test for continuing the loop, for example,

loopCount<16
. If this test evaluates to true at the beginning of a loop,
another loop iteration is performed.

<increment>
: The instruction to increment the loop counter which is
performed after each loop iteration but before the test for the next iteration. For example,

loopCount+=1
.

A loop ends with
forend
, which must be on a line of its own (that is,
a line that contains
~
 in all other columns).

### delay（取自子主题 Control instructions in device accesses）

A
delay
 statement in the

:instruction:
 column causes the execution of all statements in the

:data:
 and
:operation:
 columns between the

delay
 and the
delayend
 to be delayed for a certain number
of edges when the device access is executed. The amount of the delay is determined by the
parameter provided to
delay
.

A delay block begins with a

delay(
<latency>
)
 statement, where

<latency>
 is the number of edges by which the execution of the block
is to be delayed.

A delay block ends with
delayend
, which must be on a
line of its own (that is, a line that contains
~
 in all other
columns).

There are certain conditions that may must be observed when using delayed
operations; violating these rules will trigger compiler errors:

Device accesses can contain multiple delay blocks, but earlier blocks may not be delayed so
much that they are executed after later blocks.

Blocks may not be delayed beyond the end of the device access.

Device access delays may not be combined with non-transparent x-modes.

Device access delays may not be negative, i.e., it is not possible to use the

delay
 statement to execute operations earlier than normal.

The basic principles of delaying parts of accesses are visualized in these examples:

From left to right:

A simple delay by four edges.

Two delays that do not change the execution order of the delay blocks. (The first block is
still executed before the second one.)

Two delays in which the first block is moved past the original position of the second one.
Still, because the second block is moved as well, their execution order relative to each other
does not change. (The first block is still executed before the second one.)

Two delays in which the blocks change their execution order: The original first block
(orange) is now executed after the original second one (green). This is not permitted and would
create an error.

Note
 You can also delay entire device accesses when you call them
in the APG program file. See
`Device access delays`（raw: `116787.htm`）
 for more information.

### countedMatch（取自子主题 Control instructions in device accesses）

A
countedMatch
 statement in the

:instruction:
 column causes all statements in the
:data:

and
:operation:
 columns between the
countedMatch
 and the

matchend
 to be evaluated once for each loop. The number of loop repetitions
is determined by the arguments provided for
countedMatch
.

A counted
match loop begins with the

countedMatch(
n
)
 statement, where the
integer number
n
 is the number of times that the loop is executed at the
most.

A counted match loop ends with
matchend
, which must be on a line
of its own (that is, a line that contains
~
 in all other columns).

Note
 A counted match loop can also begin with a
countedMatchWithBreak

statement rather than
countedMatch
. For more information on counted match
loops and the difference between
countedMatch
 and

countedMatchWithBreak
, refer to
`Counted match loops`（raw: `114614.htm`）
.

### Example（取自子主题 Control instructions in device accesses）

Example 1,

for
:

```
{ :instruction: :pin: :states: :data: }
{ "for (i=0; i<8; i+=1)" A {L H} 1 }
{ ~ A {L H} 0 }
{ "forend" ~ ~ ~ }
```

Example
2,
delay
:

```
...
:interface: { myDelay }
:table:
{ :instruction: :pin: :states: :data: :operation: }
{ ~ DQi_0 {0 1} 0 dbi(gddr5_DBI) }
{ ~ DQi_1 {0 1} 1 dbi(gddr5_DBI) }
{ ~ DQi_2 {0 1} 0 dbi(gddr5_DBI) }
{ ~ DQi_3 {0 1} 1 dbi(gddr5_DBI) }
{ ~ DQi_4 {0 1} 0 dbi(gddr5_DBI) }
{ ~ DQi_5 {0 1} 1 dbi(gddr5_DBI) }
{ ~ DQi_6 {0 1} 0 dbi(gddr5_DBI) }
{ ~ DQi_7 {0 1} 1 dbi(gddr5_DBI) }
{ ~ DBI.0 {0 1} 0 dbi(gddr5_DBI) }
{ delay(myDelay) EDC.0 {L H} 0 crc(gddr5_crc_write,0) }
{ ~ ~ {L H} 0 crc(gddr5_crc_write,1) }
{ ~ ~ {L H} 0 crc(gddr5_crc_write,2) }
{ ~ ~ {L H} 0 crc(gddr5_crc_write,3) }
{ ~ ~ {L H} 0 crc(gddr5_crc_write,4) }
{ ~ ~ {L H} 0 crc(gddr5_crc_write,5) }
{ ~ ~ {L H} 0 crc(gddr5_crc_write,6) }
{ ~ ~ {L H} 0 crc(gddr5_crc_write,7) }
{ delayend ~ ~ ~ ~ }
```

Example 3,

countedMatch
:

```
apgAccess:
{
:name: "MATCH_WRITE_DQ"
:interface: { "xAddr" "yAddr" "DW"}
:table:
{
:format:
{ :instruction: :pin: :states: :data: }
{ countedMatch(10) XADDR { 0 1 } "xaddr(xAddr,yAddr,0)" }
{ "" YADDR { 0 1 } "yaddr(xAddr,yAddr,0)" }
{ "" DATA { 0 1 } "data(DW,xAddr,yAddr,0)" }
{ "" PrgChk { L H } 1 }
{ matchend ~ ~ ~ }
}
}
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

### Example（取自子主题 Reference pins）

From the pin mapping
file:

```
CK1=CK # mapping an MTL pin to a SmarTest pin
VDD(CK)=VDD@(type=dcscale) # mapping the VDD MTL pin to the
# VDD SmarTest pin and aligning it
# to the CK1 pin
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

### Syntax（取自子主题 Buses）

A bus is defined in the
`Pin mapping file`（raw: `67574.htm`）
 using the
configure
bus

keyword:

```
configure bus <busName> (<pinList>)
```

<busName>

is the name of the bus, which you can choose as desired.

<pinList>
 is the list of member pins. Its elements must be
separated by commas. The most significant bit of the bus is listed first, the least significant
bit is listed last.

The pin list can contain:

MTL pin names, as defined in the pin mapping file.

You can include undefined pins; they
are simply ignored.

Other buses defined in the pin mapping file.

If you include a bus in a pin list, all the
pins from that bus are added in their defined order. For
example:

```
configure bus myBus (pin7, pin8)
configure bus myOtherBus (myBus, pin3, pin4)
```

In
this case, myOtherBus contains the pins pin7, pin8, pin3, pin4.

A bus can also be empty:

```
configure bus myBus ()
```

This can be useful,
for example, to support multiple device densities without having to redefine the device access
file.

### Accessing bus pins（取自子主题 Buses）

You can access bus pins by adding a three-digit suffix
to the bus name:

<busname>
.
<nnn>
 is the pin
number
nnn
 from the bus definition.

For
example:

```
configure bus myBus (pin2, pin4, pin6, pin8)
```

In this case,
myBus.000 would be pin2.

### Ambiguities（取自子主题 Buses）

When naming buses and pins, take care not to create
ambiguities.

For example, if you define a bus named data and also define a pin named
data.000, any reference to data.000 could either refer to the individual pin you defined or the
first pin in your bus.

There is an exception to this when both references are actually the
same pin. For example, if there is an individual pin data.000 and you define a bus called data
as (data.000, data.001, data.002, data.003), data.000 always refers to the same pin, since the
individual pin data.000 is the first pin of the bus data.

### Example（取自子主题 Buses）

This example shows how to replace a group with subgroups with a bus.

Groups are
specified in the device access
file:

```
:groups:
{
:format:
{ :name: :size: }
{ DQo 8 }
}

:subGroups:
{
:format:
{ :baseGroup: :context: :name: :bits: }
{ DQo ALL ALL [7..0] }
{ DQo C1 C1S1 [7..4] }
{ DQo C1 C1S2 [3..0] }
{ DQo C2 C2S1 [7,5,3,1] }
{ DQo C2 C2S2 [6,4,2,0] }
}
```

This
definition in the pin mapping file is equivalent and replaces the above group and
subgroups:

```
/* original group */
configure bus DQo (DQo.000,DQo.001,DQo.002,DQo.003,DQo.004,DQo.005,DQo.006,DQo.007)
/* MSB <-> LSB */

/* original subgroup */
configure bus DQo.ALL.ALL (DQo.007,DQo.006,DQo.005,DQo.004,DQo.003,DQo.002,DQo.001,DQo.000)
/* MSB <-> LSB */
configure bus DQo.C1.C1S1 (DQo.007,DQo.006,DQo.005,DQo.004) /* MSB <-> LSB */
configure bus DQo.C1.C1S2 (DQo.003,DQo.002,DQo.001,DQo.000) /* MSB <-> LSB */
configure bus DQo.C2.C2S1 (DQo.007,DQo.005,DQo.003,DQo.001) /* MSB <-> LSB */
configure bus DQo.C2.C2S2 (DQo.006,DQo.004,DQo.002,DQo.000) /* MSB <-> LSB */
```

### Syntax（取自子主题 Copying vectors）

The attribute is included as a normal pin attribute in the
`Pin mapping file`（raw: `67574.htm`）
:

```
<mtlPinName>(<refPinName>)=<smartestPinName>@(bitseq=copy)
```

The
reference pin (
<refPinName>
) can be:

An MTL pin: The vector is copied from the specified pin.

A reference macro: The macro is defined in the
`APG pattern file`（raw: `68403.htm`）
 and the vector is
copied from the pin named in the macro. See
Reference macros
, below, for more
information.

If no reference pin is specified or if a reference macro is used and an empty string is
specified for it in the APG pattern file, the
bitseq
 attribute is ignored. In
this case, the MTL compiler compiles the vector for the pin normally.

The attributes of
the specified MTL pin must match the attributes of the reference pin from which the vector is
copied.

The reference pin must not itself reference another pin.

### Reference macros（取自子主题 Copying vectors）

A reference macro lets you define the actual reference
pin name in the APG pattern file and include only a macro reference in the pin mapping file.
This allows you to use the same pin mapping file for different purposes and make only changes to
the pattern file.

The syntax in this case
is:

<mtlPinName>
({
<pinNameMacro>
})=
<smartestPinName>
@(bitseq=copy)

The
macro
<pinNameMacro>
 must be defined in the
`APG pattern file`（raw: `68403.htm`）

using the
:define:
 statement, with the name

<pinNameMacro>
 specified in the
:name:
 column and
the pin name you want to associate with it specified in the
:value:

column.

### Examples（取自子主题 Copying vectors）

### MTL pin
```
DQo.003(DQo.000)=DQ_o.03@(bitseq=copy)
```

This statement
instructs the compiler to equate the MTL pin name DQo.003 with the SmarTest pin name DQ_o.03
and, instead of compiling the vector for this pin, copy the vector from the pin with the MTL
name DQo.000.

### Reference macro

In the pin mapping
file:

```
DQo.003({$myRefPin})=DQ_o.03@(bitseq=copy)
```

In the APG pattern
file:

```
:defines:
{
:format:
{ :name: :value: }
{ myRefPin DQo.000 }
}
```

This
statement instructs the compiler to equate the MTL pin name DQo.003 with the SmarTest pin name
DQ_o.03 and, instead of compiling the vector for this pin, copy the vector from the pin that is
specified in the macro myRefPin.

The current value of this macro is DQo.000 (so the
compiler copies the vector from the pin with the MTL name DQo.000), but you could specify a
different pin in the APG pattern file without having to change the pin mapping file at
all.

### Example（取自子主题 Automatic waveform generation）

Consider a pin group DQ_i which contains a pin named DQ_i1 (besides others). The user
supplied wavetable has the following entry for the pins in the DQ_i group:

[表] PINS DQ_i
列: PWF index | Waveform | Device cycle name
行 1:
  0
  11111111
  11111111
行 2:
  1
  00000000
  00000000
行 3:
  2
  11110000
  11110000
行 4:
  3
  00001111
  00001111

If the pattern requires two new waveforms 10101010 and 01010101, the waveforms are
added in the same section. If another pin, for example DQ_i2, in the same group requires the
waveforms 11100011 and 00011100, they will also be added to the waveform definition for the DQ_i
group. The resulting wavetable looks like this:

[表] PINS DQ_i
列: PWF index | Waveform | Device cycle name
行 1:
  0
  11111111
  11111111
行 2:
  1
  00000000
  00000000
行 3:
  2
  11110000
  11110000
行 4:
  3
  00001111
  00001111
行 5:
  4
  10101010
  10101010
行 6:
  5
  01010101
  01010101
行 7:
  6
  11100011
  11100011
行 8:
  7
  00011100
  00011100

If DQ_i2 did not belong to the DQ_i group, the waveforms of DQ_i2 will be created in a
separate pin definition. Assuming that DQ_i2 pins do not belong to any group, the resulting
wavetable would look like this:

[表] PINS DQ_i
列: PWF index | Waveform | Device cycle name
行 1:
  0
  11111111
  11111111
行 2:
  1
  00000000
  00000000
行 3:
  2
  11110000
  11110000
行 4:
  3
  00001111
  00001111
行 5:
  4
  10101010
  10101010
行 6:
  5
  01010101
  01010101
[表] PINS DQ_i2
列: PWF index | Waveform | Device cycle name
行 1:
  0
  11100011
  11100011
行 2:
  1
  00011100
  00011100

Device cycle names for the added waveforms will be automatically generated by the
compiler, which reflect the logical actions of the waveforms. When a non-interruptible waveform
is created, the device cycle name for the waveform will be given the suffix

_ni
.

The compiler adds the minimum number of waveforms that is required
to execute the pattern when it adds waveforms to existing wavetables.

### Example（取自子主题 Setting up direct waveform mapping）



### Example（取自子主题 Setting up indirect waveform mapping）



### Example（取自子主题 Waveform mapping file）

```
# covers clock-like combination only
# [1 ][0 ][1 ][0 ]
PINS CK ()
0 "1010" 1010
80 "1010" 1010_ni

# covers nClock-like combination only
# [0 ][1 ][0 ][1 ]
PINS CKn ()
0 "0101" 0101
80 "0101" 0101_ni

# covers all possible combinations
# [01][01][01][01]
PINS Address_Bus Bank_Addr_Bus CASn CKE CSn RASn WEn ODT RESETn DM_Bus ()
0 "0000" 0000
1 "0001" 0001
2 "0010" 0010
3 "0011" 0011
...
f "1111" 1111
80 "0000" 0000_ni
...
8f "1111" 1111_ni

# covers tCK-based combinations only
# [01][01][01][01]
# [01][01][i ][i ]
# [i ][i ][01][01]
# [i ][i ][i ][i ]
PINS DQi_Bus DQSi_DiffBus ()
0 "iiii" iiii
1 "ii00" ii00
2 "ii01" ii01
3 "ii10" ii10
...
18 "11ii" 11ii
80 "iiii" iiii_ni
...
98 "11ii" 11ii_ni

# covers all possible combinations
# [LHX][LHX][LHX][LHX]
PINS DQ_Bus DQS_DiffBus ()
0 "LLLL" LLLL
1 "LLLH" LLLH
2 "LLLX" LLLX
3 "LLHL" LLHL
...
50 "XXXX" XXXX
80 "LLLL" LLLL_ni
...
d0 "XXXX" XXXX_ni
```

Note
 If
`Transparent x-modes`（raw: `67809.htm`）
 are used, no names are permitted within the parentheses.
The correct syntax in this case is, for example,
PINS clock ()
.

Note
 An unmodified SmarTest timing file can be used in place of the waveform mapping file
for indirect waveform mapping. This requires copying the timing file and referencing it from the
APG pattern file using the syntax for direct waveform mapping. (That is, giving both file name
and wavetable name arguments for the
:waveformMap:
 keyword.)

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
