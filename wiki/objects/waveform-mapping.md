---
type: object
title: Waveform mapping
layer: n/a
stage: pattern
tags: []
related: []
sources:
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.03_Waveform_mapping.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Waveform mapping

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **21,450 字符逐字取自** `<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.03_Waveform_mapping.htm>` 及其子主题 `<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.02_APG_pattern_file.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.03_APG_program_file.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.04.01_Device_access_file_syntax.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.04.02_Macros_and_functions_in_device_accesses.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.04.03_Control_instructions_in_device_accesses.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.04_Device_access_file.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.07.01_Waveform_mapping_file_syntax.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.07_Waveform_mapping_file.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.03.01.01_Wavetable_syntax.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.03.01_Setting_up_direct_waveform_mapping.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.03.02_Setting_up_indirect_waveform_mapping.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.03.03_Automatic_waveform_generation.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Setting up direct waveform mapping）



### Common syntax（取自子主题 Wavetable syntax）

```
WAVETBL "<wavetable_name>"

PINS <dutPinName>
<waveform_specification>
...

...
```

These
are the keywords and parameters in alphabetical order:

[表]
列: Keyword | Parameters and descriptions
行 1:
  PINS
  <dutPinName>: The pin or pin group to be defined with
    waveform, which must have been already defined in the SmarTest pin configuration file and
    mapped into the MTL `Pin mapping file`（raw: `67574.htm`）.
    
    Up to 256 DUT pin names can be after a PINS keyword, separated by
    spaces.
    
    <waveform_specification>: The detailed description for the waveform.
    
    If maintenance operations are used, waveforms for non-interruptible sequences on pins
    in the VEC refresh mode must be applied with indexes between
    (hexadecimal) 80 and FF. (See `Maintenance operations`（raw: `75895.htm`） for details.)
行 2:
  WAVETBL
  <wavetableName>: A wavetable name. The name can be any
    string complying with the `naming conventions`（raw: `73015.htm`）.

### Compatible format（取自子主题 Wavetable syntax）

There are two ways to specify a waveform,
standard
 and
fast
.

In both modes, a
waveform is specified as:

```
<phyWfIndex><edgeActions><deviceCycleName>
```

<phyWIndex>
: A physical waveform index, integer from 0 to
255.

Note that the numbers do not need to be prefixed with 0x.

<edgeAction>
:

For the
standard
 mode, each edge in this description is prefixed with
the name of the edge (for example, "d1:0 d2:1").

For the
fast
 mode, the description consists simply of the sequence of
level (for example, "01").

<deviceCycleName>
: The name to be displayed in Pattern View.

### Example（取自子主题 Wavetable syntax）

### Compatible syntax

In the
`Pin mapping file`（raw: `67574.htm`）
:

```
...
using defaultxmode 3
...
```

In
the wavetable
file:

```
WAVETBL "Compatible"
PINS pin1 # fast-mode
0 "000" 000
1 "001" 001
2 "011" 011
...
PINS pin1 # std-mode
0 "d1:0 d2:0 d3:0" 000
1 "d1:0 d2:0 d3:1" 001
2 "d1:0 d2:1 d3:1" 011
...
```

### Example（取自子主题 Setting up indirect waveform mapping）



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

### Examples（取自子主题 Waveform mapping file syntax）

### Compatible syntax

In the
`Pin mapping file`（raw: `67574.htm`）
:

```
...
using defaultxmode 3
...
```

In
the wavetable
file:

```
WAVETBL "Compatible"
PINS pin1 # fast-mode
"000" 000
"001" 001
"011" 011
...
PINS pin1 # std-mode
"d1:0 d2:0 d3:0" 000
"d1:0 d2:0 d3:1" 001
"d1:0 d2:1 d3:1" 011
...
```

### Native syntax

In the
`Pin mapping file`（raw: `67574.htm`）
:

```
...
using defaultxmode 3
...
```

In
the wavetable
file:

```
WAVETBL "Native"
PINS pin_i
# idx fast slow name
0 "000" "000" 000
1 "001" "000" 001
2 "001" "001" 00Z
3 "011" "000" 011
...
PINS pin_o
# idx rec win name
0 "LLL" "000" LLL
1 "LLH" "000" LLH
2 "LHL" "000" LHL
3 "LHH" "000" LHH
...
PINS pin_io
# idx fast slow rec win name
0 "000" "000" "..." "000" 000
1 "001" "000" "..." "000" 001
2 "001" "001" "..." "000" 00Z
3 "111" "111" "LLX" "000" LL
...
```

### Native standard syntax

In the
`Pin mapping file`（raw: `67574.htm`）
:

```
...
using defaultxmode 3
...
```

In
the wavetable
file:

```
WAVETBL "Native_std"
PINS pin_i
# idx fast&slow name
0 "s1:0 f1:0 s2:0 f2:0 s3:0 f3:0" 000
1 "s1:0 f1:0 s2:0 f2:0 s3:0 f3:1" 001
2 "s1:0 f1:0 s2:0 f2:0 s3:1 f3:1" 00Z
...

PINS pin_o
# idx receive name
0 "r1:L r2:L r3:L" LLL
1 "r1:L r2:L r3:H" LLH
2 "r1:L r2:H r3:L" LHL
...
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

<!-- 语法节 end -->

## 是什么

**文档事实** Waveform mapping 是把 APG 程序产生的逻辑 0/1 pattern 转换为送往测试机引脚的物理波形的过程。

**文档事实** MTL 中有两种映射方式，二者都把编译器产生的逻辑 pattern 转换为 timing file 中的索引：direct waveform mapping 使用标准 SmarTest Timing file；indirect waveform mapping 使用 MTP Waveform mapping file。

**文档事实** direct 方式的设置是在 APG pattern file 的 `:waveformMap:` 关键字参数中给出 timing file 与所需 wavetable；indirect 方式则给出 waveform mapping file。

**文档事实** 必须始终使用某种 waveform mapping；源页建议除非有特定理由，否则使用 direct waveform mapping。特定理由包括：使用 Device access file 中的 `:devCyc:` 关键字（源页建议不再这样做）；测试在高数据率下需要第三 level 的器件，或更一般地需要把多个逻辑波形映射到一个物理波形（direct 方式无法做到）。

## 典型用法

**文档事实** wavetable 用 `WAVETBL "<wavetable_name>"` 与 `PINS <dutPinName>` 定义；每条波形写作 `<phyWfIndex><edgeActions><deviceCycleName>`，物理索引为 0–255，device cycle name 显示在 Pattern View。standard 模式每个 edge 带名称（如 `d1:0 d2:1`），fast 模式只写电平序列（如 `01`）。

**文档事实** 一个 PINS 后可跟最多 256 个 DUT 引脚名，以空格分隔；若使用 maintenance operations，VEC refresh 模式下不可中断序列的波形必须使用 80–FF（十六进制）索引。

**文档事实** Automatic waveform generation：编译器向已有 wavetable 增补波形时只添加执行 pattern 所需的最少波形，并自动生成反映逻辑动作的 device cycle name；不可中断波形的名字带 `_ni` 后缀。

**文档事实** 源页的 Waveform mapping file 示例按引脚组分节（如 CK、CKn、Address_Bus、DQi_Bus、DQ_Bus），普通波形从 0 起编号、不可中断波形从 0x80 起并带 `_ni` 后缀；若使用 Transparent x-modes，PINS 后的括号内不允许写名字，正确写法如 `PINS clock ()`。

**文档事实** 源页注明：indirect waveform mapping 可用未修改的 SmarTest timing file 代替 waveform mapping file，做法是复制该 timing file，并在 APG pattern file 中以 direct waveform mapping 的语法（同时给文件名与 wavetable 名参数）引用它。

## 和谁有关

- **文档事实** APG pattern file：`:waveformMap:` 关键字在此文件中指定 waveform mapping 的来源（timing file 或 waveform mapping file），是两种映射方式的入口。
- **文档事实** Timing file：direct waveform mapping 直接使用标准 SmarTest timing file 作为转换来源；本页 Related information 同时指向该页。
- **文档事实** Waveform mapping file：indirect waveform mapping 使用 MTP waveform mapping file；本页 Related information 同时指向该页。
- **文档事实** Wavetable syntax（WAVETBL / PINS）：本页语法节从 Wavetable syntax 子主题逐字抽取，定义 wavetable 的关键字与写法。
- **文档事实** APG program file 与编译器：源页说明 waveform mapping 转换的是 APG 程序产生、由编译器生成的逻辑 pattern；Automatic waveform generation 由编译器增补波形与生成名字。
- **文档事实** Device access file：源页把使用 `:devCyc:` 关键字列为选择 indirect waveform mapping 的理由之一。
- **文档事实** Maintenance operations：源页规定 VEC refresh 模式下不可中断序列的波形索引必须落在 80–FF。
- **文档事实** Transparent x-modes：源页规定使用该模式时 PINS 括号内不得写名字。
- **文档事实** Setting up direct waveform mapping、Setting up indirect waveform mapping、Automatic waveform generation：这三个子主题分别给出两种映射的设置步骤与自动波形生成说明。
- **文档事实** Pattern View：device cycle name 是显示在 Pattern View 中的名字。

## 版本

**文档事实** Functional changes 记 Introduced before SmarTest 6.3.2。

## 出处

- `02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.03_Waveform_mapping.htm`，主源，含定义、direct/indirect 对比、选择建议、Related information 与 Functional changes。
- `02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.04.03.01_Setting_up_direct_waveform_mapping.htm`、`...03.02_Setting_up_indirect_waveform_mapping.htm`、`...03.03_Automatic_waveform_generation.htm`、`...03.01.01_Wavetable_syntax.htm`，以及 APG pattern file、APG program file、Device access file、Waveform mapping file 等子主题，语法节逐字抽取来源。
