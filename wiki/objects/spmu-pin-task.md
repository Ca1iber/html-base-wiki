---
type: object
title: SPMU_PIN_TASK
layer: L2
stage: testmethod
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01_SPMU_PIN_TASK.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# SPMU_PIN_TASK

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **37,165 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01_SPMU_PIN_TASK.htm>` 及其子主题 `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.01_SPMU_PIN_TASK.clamp.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.02_SPMU_PIN_TASK.compare.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.03_SPMU_PIN_TASK.connect.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.04_SPMU_PIN_TASK.connectState.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.05_SPMU_PIN_TASK.currentClampTimeToAlarm.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.06_SPMU_PIN_TASK.currentClampTimeToDisconnect.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.07_SPMU_PIN_TASK.disconnect.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.08_SPMU_PIN_TASK.execMode.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.09_SPMU_PIN_TASK.forceDropMax.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.10_SPMU_PIN_TASK.forceDropWarn.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.11_SPMU_PIN_TASK.highAccuracy.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.12_SPMU_PIN_TASK.iClampFilter.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.13_SPMU_PIN_TASK.iFilter.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.14_SPMU_PIN_TASK.iForce.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.15_SPMU_PIN_TASK.iForceRange.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.16_SPMU_PIN_TASK.iMeasureRange.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.17_SPMU_PIN_TASK.iSlewRate.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.18_SPMU_PIN_TASK.limits.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.19_SPMU_PIN_TASK.loadCap.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.20_SPMU_PIN_TASK.loadStepMode.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.21_SPMU_PIN_TASK.max.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.22_SPMU_PIN_TASK.measFilter.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.23_SPMU_PIN_TASK.min.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.24_SPMU_PIN_TASK.mode.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.25_SPMU_PIN_TASK.openLoopProtection.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.26_SPMU_PIN_TASK.preCharge.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.27_SPMU_PIN_TASK.pulldown.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.28_SPMU_PIN_TASK.relay.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.29_SPMU_PIN_TASK.returnDropMax.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.30_SPMU_PIN_TASK.returnDropWarn.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.31_SPMU_PIN_TASK.samples.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.32_SPMU_PIN_TASK.settling.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.33_SPMU_PIN_TASK.vFilter.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.34_SPMU_PIN_TASK.vForce.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.35_SPMU_PIN_TASK.vForceFilter.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.36_SPMU_PIN_TASK.vForceRange.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.37_SPMU_PIN_TASK.vMeasureRange.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.38_SPMU_PIN_TASK.vSlewRate.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Class definition

This API is defined in the header file

/opt/hp93000/soc/prod_com/include/MAPI/SpmuPinTask.h
.

Constructor

This class has no public constructor. The
SPMU_PIN_TASK
 object can only be
accessed via the
`SPMU_TASK.pin()`（raw: `131191.htm`）
 function of the
`SPMU_TASK`（raw: `55670.htm`）
 class.

List of parameters
There are no parameters.
Return value
There is no return value.

### Examples

### Example 1: Terminated high-impedance measurement with closed AC relay

This example configures and executes a terminated high-impedance
measurement (
VM_HIZ
) with closed AC
relay.

```
//
// Define SPMU_TASK object for high-impedance measurement
//
SPMU_TASK badc_task;

ON_FIRST_INVOCATION_BEGIN();

//
// Configure high-impedance measurement with 1 ms waiting time for "pinName"
// no force values required
//
badc_task.pin("pinName").mode("VM_HIZ").settling(1 ms);

//
// Configure terminated measurement (AC relay closed during measurement)
// and define limits for P/F result
//
badc_task.pin("pinName").relay("TERM").min(0 V).max(5 V);

//
// Define value measurement and execute measurement
//
badc_task.preAction("NONE").execMode("PVAL").execute();

ON_FIRST_INVOCATION_END();

//
// Get results
//
cout << badc_task.getValue("pinName") << endl;
```

### Example 2: Pattern-controlled high impedance voltage measurement with voltage forced by pin PMU

This example shows a pattern-controlled high impedance voltage
measurement. A voltage is forced with pin PMU on
pin_force
.
This pin is cross-connected with
pin_meas
. The

pin_meas
 uses the high impedance measurement path to
measure the voltage of
pin_force
. The measurement path is
configured with
`SPMU_TASK`（raw: `55670.htm`）
.

```
virtual void run()
{
DC_RESULT_ACCESSOR result;
PATTERN_CONTROLLER pc;
SPMU_TASK badcConnect;
static STRING_VECTOR pinList;
static STRING measPins = "pin_meas";

ON_FIRST_INVOCATION_BEGIN();

//
// Connect BADC
//
badcConnect.pin(measPins).mode("VM_HIZ").relay("NT").connect();
badcConnect.execute();

//
// Setup dynamic test, do it only one time
// first_run is a protected variable "Boolean first_run;"
// which is set to 'true' in initialize method
//
if (first_run)
{
PPMU_SETTING ppmuForce;
PPMU_RELAY ppmuOn,ppmuOff;
BADC_SETTING badcSetting;
BADC_MEASURE badcMeasure;
ppmuForce.pin("pin_force")
.vForce(forceVoltage.getValueAsTargetUnit("V"))
.iRange(1 uA).min(0 uA).max(2 uA);
ppmuOn.pin("pin_force").status("PPMU_ON");
ppmuOff.pin("pin_force").status("AC_ON");
badcSetting.pin(measPins).min(0 V).max(5 V);
badcSetting.wait(1 ms);
badcMeasure.pin(measPins).numberOfSamples(16);
badcMeasure.wait(100 us);

pc.label("MeasBADC","@").add(ppmuForce)
.add(ppmuOn)
.add(badcSetting)
.add(badcMeasure)
.add(ppmuOff);
pc.setup();

first_run = false;
}

//
// Execute test
//
FUNCTIONAL_TEST();

result.uploadResult(measPins ,TM::RESULT_INDEX);

pinList = PinUtility.getDigitalPinNamesFromPinList(measPins,TM::ALL_DIGITAL);

ON_FIRST_INVOCATION_END();

//
// Results
//
int numberPins = pinList.size();
for(int i=0; i<numberPins; i++)
{
ARRAY_D values = result.getValues(pinList[i]);
int numberOfResults = values.size();
for (int j = 0; j< numberOfResults; j++)
{
double value = values[j];
cout << "PF: " << result.getPassFail() << endl;
cout << "NumVal: " << result.getNumberOfAvailableResults(pinList[i]) << endl;
cout << "FailInfo: " << result.getFailInfo() << endl;
cout << "PPMU VMHIZ BADC Measurement result: " << value << endl;
}
}

return;
}
```

### Syntax（取自子主题 SPMU_PIN_TASK.clamp()）

```
SPMU_PIN_TASK& clamp(DOUBLE clamp);
SPMU_PIN_TASK& clamp(DOUBLE sink, DOUBLE source);
SPMU_PIN_TASK& clamp(DOUBLE clampLow, DOUBLE clampHigh);
```

Note
 The syntax with two parameters is supported only by the
`DC Scale DPS128/64 cards`（raw: `138572.htm`）

and the
`DC Scale XPS256 card`（raw: `350661.htm`）
.

[表] Parameters
列: Parameter | Description
行 1:
  clamp
  Clamp value:
    
    "IF..." and "CF..."
    modes: Sets the clamp voltage in Volt.
    
    "VF..." modes: Sets the clamp current in
    Ampere.
行 2:
  sink
  Sets the sinking clamp current in Ampere for the "VF..." modes.
    Supported only
    by the DC Scale DPS128/64 cards and the DC Scale XPS256
    card.
行 3:
  source
  Sets the sourcing clamp current in Ampere for the "VF..." modes.
    Supported only
    by the DC Scale DPS128/64 cards and the DC Scale XPS256
    card.
行 4:
  clampLow
  Sets the lower clamp voltage in Volt for the "IF..." and
    "CF..." modes.
    Supported only by the DC Scale
    DPS128/64 cards and the DC Scale XPS256 card.
行 5:
  clampHigh
  Sets the upper clamp voltage in Volt for the "IF..." and
    "CF..." modes.
    Supported only by the DC Scale
    DPS128/64 cards and the DC Scale XPS256 card.

### Return value（取自子主题 SPMU_PIN_TASK.clamp()）

A reference to the
`SPMU_PIN_TASK`（raw: `55669.htm`）

object.

### Syntax（取自子主题 SPMU_PIN_TASK.compare()）

```
SPMU_PIN_TASK& compare(const STRING& compare);
```
[表] Parameter
列: Parameter | Description
行 1:
  compare
  Default mode is "I".
    
    The test results will be evaluated pass, if the following condition per mode is met:
    
    "I" - Intermediate - the measured value is between the low and the
    high threshold.
    
    "L" - low - the measured value is below the low threshold.
    
    "H" - high - the measured value is above the high threshold.

### Return value（取自子主题 SPMU_PIN_TASK.compare()）

A reference to the
`SPMU_PIN_TASK`（raw: `55669.htm`）

object.

### Syntax（取自子主题 SPMU_PIN_TASK.connect()）

```
void connect();
```

List of parameters

There are no parameters.

Return value

There is no return value.

### Example（取自子主题 SPMU_PIN_TASK.connect()）

Note
 Every other function called before the

connect()
 or
disconnect()
 function inside the same task
is not taken into account.

Note
 When using two or more pins in one
SPMU_TASK object, where some pins need to be connected (
connect()
) and other
pins need to be disconnected (
disconnect()
), you must specify two separate
tasks and execute the tasks individually.

```
SPMU_TASK tsk1, tsk2;
ON_FIRST_INVOCATION_BEGIN();
tsk1 .pin("VI32_1") .relay("NT").connect();
tsk2 .pin("VI32_2") .relay("NT").disconnect();
tsk1 .execute();
tsk2 .execute();
ON_FIRST_INVOCATION_END();
```

### Syntax（取自子主题 SPMU_PIN_TASK.connectState()）

```
SPMU_PIN_TASK& connectState (const STRING& DPS128_connectionState);
SPMU_PIN_TASK& connectState (const STRING& XPS256_connectionState);
```
Parameters
[表]
列: Parameter | Description
行 1:
  `DPS128_connectionState`（raw: `144095.htm#_144095__t_DPS128_connectionState_options`）
  The parameter defines some special measurement modes
    or (for compatibility) connection states.
    This
    parameter is supported only for the HC variant of
    DPS128.
    
    For the available options, refer to
    table `DPS128_connectionState`（raw: `144095.htm#_144095__t_DPS128_connectionState_options`）.
行 2:
  `XPS256_connectionState`（raw: `144095.htm#_144095__t_XPS256_connectionState_options`）
  The parameter defines some special measurement
    modes or (for compatibility) connection states.
    
    This parameter is supported only for XPS256 pins.
    
    For the available options, refer to table `XPS256_connectionState`（raw: `144095.htm#_144095__t_XPS256_connectionState_options`）.
[表] Available options of parameter: DPS128_connectionState
列: Option | Description
行 1:
  "MEAS_KELVIN_HIGH"
  This connection state selects a voltage drop
    measurement.
    The voltage drop is measured from the
    high force pogo pins (P#) of the channel to the high
    sense pogo pin (PS#).
    
    For ganged channels, the
    voltage drop is measured on the master
    channel.
  These connection states require that a voltage [跨 2 行]
    measurement mode like "IFVM" or "VFVM" has been
    selected by function `SPMU_PIN_TASK.mode()`（raw: `131275.htm`）.
    
    These connection states are available only for the HC
    variant of DPS128 / DPS64. For more
    information, refer to `Voltage drop measurement`（raw: `140638.htm#_140638__s_Voltage_drop_measurement`） in
    `DPS128 / DPS64 functionality and features`（raw: `140638.htm`）.
行 2:
  "MEAS_KELVIN_LOW"
  This connection state selects a voltage drop
    measurement.
    The voltage drop is measured from the
    ground sense pogo pin (GS#) to the common ground
    (GND) pins of the channel.
    
    For ganged
    channels, the voltage drop is measured on the master
    channel.
[表] Available options of parameter: XPS256_connectionState
列: Option | Description
行 1:
  "MEAS_KELVIN_HIGH"
  This connection state selects a voltage drop
    measurement.
    The voltage drop is measured from the
    high force pogo pins (P#) of the channel to the high
    sense pogo pin (PS#).
    
    For ganged channels, the
    voltage drop is measured on the master
    channel.
  These connection states require that a voltage [跨 2 行]
    measurement mode like "CFVM" or "VFVM" has been
    selected by function `SPMU_PIN_TASK.mode()`（raw: `131275.htm`）.
    
    For more information, refer to `XPS256 voltage drop measurement`（raw: `353409.htm`） and `XPS256 programming - Voltage drop measurement`（raw: `354548.htm`）.
行 2:
  "MEAS_KELVIN_LOW"
  This connection state selects a voltage drop
    measurement.
    The voltage drop is measured from the
    ground sense pogo pin (GS#) to the common ground
    (GND) pins of the channel.
    
    For ganged
    channels, the voltage drop is measured on the master
    channel.
Return value
A reference to the
`SPMU_PIN_TASK`（raw: `55669.htm`）
 object.

### Example（取自子主题 SPMU_PIN_TASK.connectState()）

The following example shows how to set the connection
state.

```
SPMU_TASK spmuTask;

spmuTask.pin("...")
...
...
.connectState("...")
;
```

Note: The example concentrates on the function described in this
topic. More settings are required for an executable SPMU_TASK object.

### Syntax（取自子主题 SPMU_PIN_TASK.currentClampTimeToAlarm()）

```
SPMU_PIN_TASK & currentClampTimeToAlarm(DOUBLE currClampTimeToAlarm);
```
Parameter
[表]
列: Parameter | Description
行 1:
  currClampTimeToAlarm
  The delay time in milliseconds (ms) to be set.
Return value
A reference to the
`SPMU_PIN_TASK`（raw: `55669.htm`）
 object.

### Syntax（取自子主题 SPMU_PIN_TASK.currentClampTimeToDisconnect()）

```
SPMU_PIN_TASK & currentClampTimeToDisconnect(DOUBLE currClampTimeToDisconnect);
```
Parameter
[表]
列: Parameter | Description
行 1:
  currClampTimeToDisconnect
  The delay time in milliseconds (ms) to be set.
Return value
A reference to the
`SPMU_PIN_TASK`（raw: `55669.htm`）
 object.

### Syntax（取自子主题 SPMU_PIN_TASK.disconnect()）

```
void disconnect();
```

List of parameters

There are no parameters.

Return value

There is no return value.

### Example（取自子主题 SPMU_PIN_TASK.disconnect()）

Note
 Every other function called before the

connect()
 or
disconnect()
 function inside the same task
is not taken into account.

Note
 When using two or more pins in one
SPMU_TASK object, where some pins need to be connected (
connect()
) and other
pins need to be disconnected (
disconnect()
), you must specify two separate
tasks and execute the tasks individually.

```
SPMU_TASK tsk1, tsk2;
ON_FIRST_INVOCATION_BEGIN();
tsk1 .pin("VI32_1") .relay("NT").connect();
tsk2 .pin("VI32_2") .relay("NT").disconnect();
tsk1 .execute();
tsk2 .execute();
ON_FIRST_INVOCATION_END();
```

### Syntax（取自子主题 SPMU_PIN_TASK.execMode()）

```
SPMU_PIN_TASK& execMode(const STRING& mode);
```
[表] Parameter
列: Parameter | Description
行 1:
  mode
  The parameter defines the execution mode:
    
    "PAR" - Parallel measurement mode.
    
    "SER" - Serial measurement mode, not for
    HIZ measurement on digital pins.
    
    "PAR_HAC" - Parallel measurement mode
    with high accuracy force current.
    
    "SER_HAC" - Serial measurement mode with
    high accuracy force current, not for HIZ measurement on
    digital pins.
    
    Default mode is "PAR".
    
    "PAR_HAC" and "SER_HAC" are not supported for
    ganged DPS128 channels.

### Return value（取自子主题 SPMU_PIN_TASK.execMode()）

A reference to the
`SPMU_PIN_TASK`（raw: `55669.htm`）

object.

### Syntax（取自子主题 SPMU_PIN_TASK.forceDropMax()）

```
SPMU_PIN_TASK & forceDropMax(DOUBLE forceDrop);
```
Parameter
[表]
列: Parameter | Description
行 1:
  forceDrop
  The maximum voltage drop in Volts (V) to be set.
    
    A positive voltage has to be set regardless of the
    polarity of the actual or programmed current.
    
    Valid range and default value:
    
    XPS256:
    
    For the specification, refer to `Voltage drop protection / measurement`（raw: `350739.htm#_350739__s_Voltage_drop_protection`） in `XPS256 other performance characteristics`（raw: `350739.htm`）.
    
    The programmable range is 0.0 … 1.0 V for the force line and for the return
    line but, the total for the two lines must not exceed 1.0 V.
    
    Default value: 150 mV
    
    For a maximum
    voltage drop > 0.5 V, the open loop
    protection must be set to
    "NONE" by function `openLoopProtection()`（raw: `355803.htm`） and in
    the `DC Scale Safety editor`（raw: `354611.htm#_354611__s_DC_Scale_Safety_editor`） the `Vdrop Disco`（raw: `354611.htm#_354611__r_Vdrop_Disco`） parameter must be set to
    ON.
Return value
A reference to the
`SPMU_PIN_TASK`（raw: `55669.htm`）
 object.

### Example（取自子主题 SPMU_PIN_TASK.forceDropMax()）

### Maximum voltage drop of XPS256
```
SPMU_TASK spmuTask_1;

spmuTask_1.pin("...")
.mode("VFIM")
...
...
.forceDropMax (300 mV)
.returnDropMax (200 mV)
;
```

Note:
The example concentrates on the function described in this topic. More settings are
required for an executable SPMU_TASK object.

### Syntax（取自子主题 SPMU_PIN_TASK.forceDropWarn()）

```
SPMU_PIN_TASK & forceDropWarn(DOUBLE forceDropWarn);
```
Parameter
[表]
列: Parameter | Description
行 1:
  forceDropWarn
  The warning threshold in millivolt (mV) to be set.
    
    A positive voltage has to be set regardless of the
    polarity of the actual or programmed current.
    
    For the valid range refer to `Voltage drop protection / measurement`（raw: `350739.htm#_350739__s_Voltage_drop_protection`） in `XPS256 other performance characteristics`（raw: `350739.htm`）
Return value
A reference to the
`SPMU_PIN_TASK`（raw: `55669.htm`）
 object.

### Syntax（取自子主题 SPMU_PIN_TASK.highAccuracy()）

```
SPMU_PIN_TASK & highAccuracy();
```

List of parameters
There are no parameters.
Return value
A reference to the
`SPMU_PIN_TASK`（raw: `55669.htm`）
 object.
Errors
An error message is displayed in the UI report window if the high‑accuracy license
is missing or is not enabled in the
`DC Scale Extensions editor`（raw: `150670.htm`）
:

```
Connection state HC_HAC not supported or no license for pin ...
```

### Syntax（取自子主题 SPMU_PIN_TASK.iClampFilter()）

```
SPMU_PIN_TASK& iClampFilter (DOUBLE filterFrequency);
SPMU_PIN_TASK& iClampFilter (const STRING & filterFrequency);
```

[表] Parameter
列: Parameter | Description
行 1:
  filterFrequency
  Sets the filter to the given frequency in Hertz (Hz) or switches the filter off. The
    parameter can be defined as double value or as
    string.
    Programmable double values or strings are
    
    Value between the card-specific minimum and maximum value:
    The filter is switched on and set to the defined value.
    
    0.0: The filter is set to the card-specific default
    value.
    
    Programmable strings are
    
    "OFF": The filter is set to the card-specific default
    value.
    
    Card-specific range and default value:
    
    XPS256: Refer to section `Dynamic behavior`（raw: `354306.htm#_354306__s_Dynamic_behavior`） in `XPS256 programming - Force and clamp currents`（raw: `354306.htm`）.

### Return value（取自子主题 SPMU_PIN_TASK.iClampFilter()）

A reference to the
`SPMU_PIN_TASK`（raw: `55669.htm`）
 object.

### Example（取自子主题 SPMU_PIN_TASK.iClampFilter()）

The following example shows how to set the force voltage filter and the clamp current
filter.

```
SPMU_TASK spmuTask;

spmuTask.pin("###")
...
...
.vForceFilter(0) // Switch the force voltage filter off
.iClampFilter(1000) // Set the clamp current filter to 1 kHz
;
```

Note: The example concentrates on the function described in this topic. More settings
are required for an executable SPMU_TASK object.

### Syntax（取自子主题 SPMU_PIN_TASK.iFilter()）

```
SPMU_PIN_TASK& iFilter(DOUBLE filterFrequency);
SPMU_PIN_TASK& iFilter(const STRING & filterFrequency);
```
[表] Parameter
列: Parameter | Description
行 1:
  filterFrequency
  Sets the filter to the given frequency in Hertz (Hz) or switches the filter off. The
    parameter can be defined as double value or as
    string.
    Programmable double values or strings are
    
    Value between the card-specific minimum and maximum value:
    The filter is switched on and set to the defined value.
    
    0.0: The filter is set to the card-specific default
    value.
    
    Programmable strings are
    
    "OFF": The filter is set to the card-specific default
    value.
    
    Card-specific range and default value:
    
    XPS256: Refer to section `Dynamic behavior`（raw: `354306.htm#_354306__s_Dynamic_behavior`） in `XPS256 programming - Force and clamp currents`（raw: `354306.htm`）.

### Return value（取自子主题 SPMU_PIN_TASK.iFilter()）

A reference to the
`SPMU_PIN_TASK`（raw: `55669.htm`）

object.

### Example（取自子主题 SPMU_PIN_TASK.iFilter()）

The following example shows how to set the voltage filter and the current
filter.

```
SPMU_TASK spmuTask_1;

spmuTask_1.pin("...")
...
...
.vFilter("OFF") // Switch the voltage filter off
.iFilter(1000) // Set the current filter to 1 kHz
;
```

Note:
The example concentrates on the function described in this topic. More settings are
required for an executable SPMU_TASK object.

### Syntax（取自子主题 SPMU_PIN_TASK.iForce()）

```
SPMU_PIN_TASK& iForce(DOUBLE current);
```
[表] Parameter
列: Parameter | Description
行 1:
  current
  Forced current in Ampere.

### Return value（取自子主题 SPMU_PIN_TASK.iForce()）

A reference to the
`SPMU_PIN_TASK`（raw: `55669.htm`）

object.

### Syntax（取自子主题 SPMU_PIN_TASK.iForceRange()）

```
SPMU_PIN_TASK& iForceRange(DOUBLE rangeValue);
```

Parameter
[表]
列: Parameter | Description
行 1:
  rangeValue
  Expected value in Ampere (A).
    
    SmarTest determines the current range automatically
    from the programmed force- or clamp-current if the
    range has not been defined by this API.
    
    Note The current range depends on the
    underlying hardware.
Return value
A reference to the
`SPMU_PIN_TASK`（raw: `55669.htm`）
 object.

### Syntax（取自子主题 SPMU_PIN_TASK.iMeasureRange()）

```
SPMU_PIN_TASK& iMeasureRange(DOUBLE rangeValue);
```

Parameter
[表]
列: Parameter | Description
行 1:
  rangeValue
  Expected value in Ampere (A).
    
    SmarTest determines the current range automatically
    from the pass/fail thresholds `min()`（raw: `131359.htm`） and `max()`（raw: `131360.htm`） if the expected value has not been
    defined by this API.
    Note The current
    range depends on the underlying
    hardware.
Return value
A reference to the
`SPMU_PIN_TASK`（raw: `55669.htm`）
 object.

### Syntax（取自子主题 SPMU_PIN_TASK.iSlewRate()）

```
SPMU_PIN_TASK& iSlewRate (const DOUBLE iSlewRate);
```
[表] Parameter
列: Parameter | Description
行 1:
  iSlewRate
  Defines the current slew rate in Ampere per microsecond (A / µsec).
    Programmable
    double values are
    
    Value between the card-specific minimum and maximum value:
    The filter is switched on and set to the defined filter
    frequency.
    
    0.0: The filter is set to the card-specific default
    value.
    
    Card-specific range and default value:
    
    XPS256: Refer to section `Dynamic behavior`（raw: `354306.htm#_354306__s_Dynamic_behavior`） in `XPS256 programming - Force and clamp currents`（raw: `354306.htm`）.

### Return value（取自子主题 SPMU_PIN_TASK.iSlewRate()）

A reference to the
`SPMU_PIN_TASK`（raw: `55669.htm`）

object.

### Example（取自子主题 SPMU_PIN_TASK.iSlewRate()）

The following example shows how to set the force current slew
rate.

```
SPMU_TASK spmuTask_1;

spmuTask_1.pin("...")
.mode("CFVM")
...
...
.iSlewRate(20 mA) // [A/us]
;
```

Note:
The example concentrates on the function described in this topic. More settings are
required for an executable SPMU_TASK object.

### Syntax（取自子主题 SPMU_PIN_TASK.limits()）

```
SPMU_PIN_TASK& limits(const STRING& limits);
SPMU_PIN_TASK& limits(const LIMIT& limits);
```
[表] Parameter
列: Parameter | Description
行 1:
  limits
  The Name of the `LIMIT`（raw: `29504.htm`） object or the limit's name from the test
    suite as STRING.

### Return value（取自子主题 SPMU_PIN_TASK.limits()）

A reference to the
`SPMU_PIN_TASK`（raw: `55669.htm`）

object.

### Syntax（取自子主题 SPMU_PIN_TASK.loadCap()）

```
SPMU_PIN_TASK& loadCap (DOUBLE capacitance);
```
[表] Parameter
列: Parameter | Description
行 1:
  capacitance
  External load capacitance in F.
    Card-specific default value and range:
    
    DPS128 / 64:
    
    Range:
    
    0.0 μF: Enables the cap-less mode
    
    > 0.0 μF: Enables the standard mode that supports a load capacitance of up to 470 μF
    per channel`1)`（raw: `#_148944__d2708e1305`）.
    
    Default value after reset: 1.0 μF - standard mode with load
    capacitance.
    
    Default value if not programmed: The last programmed value or the
    reset value of 1 μF
    
    XPS256: Refer to section `Dynamic behavior`（raw: `354305.htm#_354305__s_Dynamic_behavior`） in `XPS256 programming - Force and clamp voltages`（raw: `354305.htm`）.

### Return value（取自子主题 SPMU_PIN_TASK.loadCap()）

A reference to the
`SPMU_PIN_TASK`（raw: `55669.htm`）

object.

### Example（取自子主题 SPMU_PIN_TASK.loadCap()）

```
SPMU_TASK spmuTask_1;

spmuTask_1.pin("...")
.mode("VFIM")
...
...
.loadCap(10.0 nF)
;
```

Note:
The example concentrates on the function described in this topic. More settings are
required for an executable SPMU_TASK object.

### Syntax（取自子主题 SPMU_PIN_TASK.loadStepMode()）

```
SPMU_PIN_TASK & loadStepMode(const STRING& mode);
```
Parameter
[表]
列: Parameter | Description
行 1:
  mode
  Load step mode to be defined as string.
    
    Valid strings are
    
    "STD" (default) or
    
    "FAST"
    
    See also `XPS256 programming - Load step response`（raw: `352356.htm`）.
Return value
A reference to the
`SPMU_PIN_TASK`（raw: `55669.htm`）
 object.

### Syntax（取自子主题 SPMU_PIN_TASK.max()）

```
SPMU_PIN_TASK& max(DOUBLE max);
```
[表] Parameter
列: Parameter | Description
行 1:
  max
  High threshold value.
    
    The unit depends on the selected `measurement mode`（raw: `131275.htm`）:
    
    "IFVM" mode and other
    VM modes: The high threshold
    voltage in Volt.
    
    "VFIM" mode and other
    IM modes::The high threshold
    current in Ampere.

### Return value（取自子主题 SPMU_PIN_TASK.max()）

A reference to the
`SPMU_PIN_TASK`（raw: `55669.htm`）

object.

### Syntax（取自子主题 SPMU_PIN_TASK.measFilter()）

```
SPMU_PIN_TASK& measFilter(double filterFrequency);
```

Paameter
[表]
列: Parameter | Description
行 1:
  filterFrequency
  Sets the filter to the given frequency in Hz or
    switches the filter off.
    
    Programmable double values are
    
    Value between the card-specific minimum and
    maximum value: The filter is set to the defined
    value.
    
    0.0: The filter is set to the card-specific
    default value.
    
    Card-specific range and default value:
    
    XPS256: Refer to section
    
    `Measurement filters`（raw: `354459.htm#_354459__s_Measure_filters`） in `XPS256 programming - Measure voltages`（raw: `354459.htm`）
    or to section
    
    `Measurement filters`（raw: `354458.htm#_354458__s_Measure_filters`） in `XPS256 programming - Measure currents`（raw: `354458.htm`）.
Return value
A reference to the
`SPMU_PIN_TASK`（raw: `55669.htm`）
 object.

### Example（取自子主题 SPMU_PIN_TASK.measFilter()）

The following example shows how to set the measure
filter.

```
SPMU_TASK spmuTask_1;

spmuTask_1.pin("...")
...
...
.measFilter(100 kHz) // Set the measure filter to 100 kHz
;
```

Note: The example concentrates on the function described in this
topic. More settings are required for an executable SPMU_TASK object.

### Syntax（取自子主题 SPMU_PIN_TASK.min()）

```
SPMU_PIN_TASK& min(DOUBLE min);
```
[表] Parameter
列: Parameter | Description
行 1:
  min
  Low threshold value.
    
    The unit depends on the selected `measurement mode`（raw: `131275.htm`）:
    
    "IFVM" mode and other
    VM modes: The high threshold
    voltage in Volt.
    
    "VFIM" mode and other
    IM modes::The high threshold
    current in Ampere.

### Return value（取自子主题 SPMU_PIN_TASK.min()）

A reference to the
`SPMU_PIN_TASK`（raw: `55669.htm`）

object.

### Syntax（取自子主题 SPMU_PIN_TASK.mode()）

```
SPMU_PIN_TASK& mode(const STRING& mode);
```
[表] Parameter
列: Parameter | Description
行 1:
  mode
  Default mode is "IFVM".
    Refer to the list of
    available options of the mode parameter
    below.
[表] Available options of parameter: mode
列: mode | Description
行 1:
  "IFVM"
  Force current and measure voltage.
    
    This mode is set so that voltage is forced and the required
    current is defined via symmetrical set current clamp values.
    Therefore, you must observe the minimum clamp current distance
    for setting the forced current in the "IFVM"
    mode.
    
    AVI64 and FVI16 support the real current forcing modes `"CFVM" and "CFIM"`（raw: `131275.htm#_131275__r_AVI64_FVI16`） in
    which the minimum clamp distance does not have to be
    observed.
行 2:
  "VFIM"
  Force voltage and measure current.
行 3:
  "VM_HIZ"
  High impedance voltage measurement.
行 4:
  "VM_HIZ_HAC"
  High impedance voltage measure with high accuracy. The voltage
    range is selected via `SPMU_PIN_TASK.min()`（raw: `131359.htm`） and `SPMU_PIN_TASK.max()`（raw: `131360.htm`）.
行 5:
  "IFVM_UNGANGED"
  Force current and measure voltage by temporarily separating
    ganged channels for this measurement.
    The ganged channels are
    temporarily unganged to the minimum number of channels that is
    required to force the programmed current. The voltage
    measurement is always performed on the first channel of the
    ganged group. Temporarily unganging for voltage measurements
    will improve the stability of the forced current and therefore
    improve the stability of the voltage measurement.
行 6:
  "VFIM_UNGANGED"
  Force voltage and measure current by temporarily separating
    ganged channels for this measurement.
    See also `Number of channels in unganged mode`（raw: `131275.htm#_131275__s_Number_of_channels_unganged`） below.
    
    Note that on DPS128/64 and XPS256 you cannot execute a current
    compare on a ganged group of channels in unganged mode. Already activated
    comparators are silently disabled in unganged mode. A user notification (Error or
    warning) is omitted in this case, to avoid any interrupt in the testflow. The
    previous state of the comparators is automatically restored after the ganged group
    has been restored.
行 7:
  "PPMU_BADC"
  Connects the board ADC (BADC) with the pin PMU (PPMU) for static
    measurements.
    
    Mapped to "IFVM" for DC Scale cards without a
    separate board ADC.
行 8:
  The following [跨 2 列]
    measurement modes are supported only for the `DC Scale XPS256 card`（raw: `350661.htm`）.
行 9:
  "VFVM"
  Force voltage and measure voltage.
行 10:
  "CFVM"
  Force current directly and measure voltage or current. [跨 2 行]
    
    Both the lower and the upper clamp must be set by function `SPMU_PIN_TASK.clamp()`（raw: `131358.htm`） if these modes are selected.
行 11:
  "CFIM"

Note
 If the
`SPMU_PIN_TASK.iForce()`（raw: `131352.htm`）
 or
`SPMU_PIN_TASK.vForce()`（raw: `131353.htm`）
 is
used, the corresponding mode(
"IFVM"
 or
"VFIM"
)
is set automatically.

### Return value（取自子主题 SPMU_PIN_TASK.mode()）

A reference to the
`SPMU_PIN_TASK`（raw: `55669.htm`）

object.

### Example（取自子主题 SPMU_PIN_TASK.mode()）

In the example below
"VM_HIZ"
 selects the Board ADC for a
voltage
measurement.

```
SPMU_TASK badc_task;

ON_FIRST_INVOCATION_BEGIN();
badc_task.pin("pinName").mode("VM_HIZ");
badc_task.pin("pinName").settling(1 ms).samples(1);
badc_task.pin("pinName").relay("TERM");
badc_task.pin("pinName").min(0 V).max(5 V);
badc_task.preAction("NONE").execMode("PVAL").execute();
ON_FIRST_INVOCATION_END();

cout << badc_task.getValue("pinName") << endl;
```

### Syntax（取自子主题 SPMU_PIN_TASK.openLoopProtection()）

```
SPMU_PIN_TASK & openLoopProtection(const STRING & openLoopProtection);
```
Parameter
[表]
列: Parameter | Description
行 1:
  openLoopProtection
  Mode of the open loop
    protection to be defined as string.
    
    Valid strings are
    
    "DIODE" (default)
    The internal force to sense connections are made via anti‑parallel diodes.
    
    This is the
    default state if the parameter is not defined.
    
    This is the recommended setting if
    both parameters the `maximum force drop`（raw: `344345.htm`） and the `maximum return drop`（raw: `344346.htm`） are set to a
    value < 0.5 V.
    
    "NONE"
    The internal force to sense connections are open.
    
    The output stage no longer has any voltage feedback if the force to
    sense connection on the DUT or the DUT board is (unintentionally) open.
    
    The
    following rules apply to this option:
    
    The `Vdrop Disco`（raw: `354611.htm#_354611__r_Vdrop_Disco`） parameter must be set
    to ON in the `DC Scale Safety editor`（raw: `354611.htm#_354611__s_DC_Scale_Safety_editor`）.
    
    This is the required setting if one of the parameters `maximum force drop`（raw: `344345.htm`） or `maximum return drop`（raw: `344346.htm`）
    is set to a value ≥ 0.5 V.
    
    See also `XPS256 programming - Voltage drop measurement`（raw: `354548.htm`）.
Return value
A reference to the
`SPMU_PIN_TASK`（raw: `55669.htm`）
 object.

### Syntax（取自子主题 SPMU_PIN_TASK.preCharge()）

```
SPMU_PIN_TASK& preCharge(DOUBLE voltage);
```

[表] Parameters
列: Parameter | Description
行 1:
  voltage
  Precharge voltage of the SPMU pin in Volt.
行 2:
  safe_con
  Enables the safe connecting mode.
    
    The string parameter safe_con is supported only by the `DC Scale XPS256 card`（raw: `350661.htm`）. The
    following value is available:
    
    "SAFE_CON"

### Return value（取自子主题 SPMU_PIN_TASK.preCharge()）

A reference to the
`SPMU_PIN_TASK`（raw: `55669.htm`）

object.

### Syntax（取自子主题 SPMU_PIN_TASK.pulldown()）

```
SPMU_PIN_TASK & pulldown(const STRING& pulldown);
```
Parameter
[表]
列: Parameter | Description
行 1:
  pulldown
  Options are
    
    "ON" (default) to enable the pull‑down circuit or
    
    "OFF" to disable it.
Return value
A reference to the
`SPMU_PIN_TASK`（raw: `55669.htm`）
 object.

### Syntax（取自子主题 SPMU_PIN_TASK.relay()）

```
SPMU_PIN_TASK& relay(const STRING& relay);
```
[表] Parameters
列: Parameter | Description
行 1:
  relay
  Default mode is "NO".
    
    Refer to the list of available options of the relay parameter below.

Note
 DC Scale cards do not support
TERM
,

NTBMM
 and
NTMBB
 modes!

[表] Available options of parameter: relay
列: Relay switching mode and description | DC Scale | High impedance (HIZ) measurements with BADC`1)`（raw: `#fntarg_1`）
行 1:
  "NO"
    
    The termination state and the relay state remain
    unchanged.
  The connection state is not changed.
  The connection state is not changed.
行 2:
  "NTBBM"
    
    No-Termination-Break-Before-Measure.
    
    Digital front-end (driver, receiver & active load) will
    be disconnected before the DC instrument is connected.
  n/a
  Open AC relay
    
    Close DC and BADC relay and switch MUX to DC rail
    
    Measure
    
    Open BADC and DC relay
    
    Close AC relay
行 3:
  "NTMBB"
    
    No-Termination-Measure-Before-Break.
    
    DC instrument will be connected before the digital frontend
    (driver, receiver & active load) is disconnected.
  n/a
  Close DC and BADC relay and switch MUX to DC rail
    
    Open AC relay
    
    Measure
    
    Close AC relay
    
    Open BADC and DC relay
行 4:
  "TERM"
    
    Terminated measurement.
    
    AC relay state is not changed.
  n/a
  Close DC and BADC relay and switch MUX to DC rail
    
    Measure
    
    Open BADC and DC relay
行 5:
  "NT"
    
    No termination.
  Supported only in PMU operating mode of DC Scale pins.
    
    Relay actions depend on the settings of `SPMU_PIN_TASK.mode()`（raw: `131275.htm`）
    with `SPMU_TASK.execMode()`（raw: `131193.htm`） set to
    "FORCE_ON":
    
    mode() set to "IFVM",
    "VFIM":
    
    Connect DC Scale card by closing AC_Force, H_IMP and
    AC_Sense relays.
    
    Measure
    
    Open AC_Force, H_IMP and AC_Sense relays.
    
    mode() set to
    "VM_HIZ":
    
    Connect DC Scale card by closing H_IMP and AC_Sense
    relays.
    
    Measure
    
    Open H_IMP and AC_Sense relays.
    
    mode() set to
    "VFIM_UNGANGED":
    
    Connect DC Scale card by closing AC_Force, H_IMP and
    AC_Sense relays.
    
    Measure (not needed pins will be disconnected)
    
    Open AC_Force, H_IMP and AC_Sense relays.

### Return value（取自子主题 SPMU_PIN_TASK.relay()）

A reference to the
`SPMU_PIN_TASK`（raw: `55669.htm`）

object.

### Syntax（取自子主题 SPMU_PIN_TASK.returnDropMax()）

```
SPMU_PIN_TASK & returnDropMax(DOUBLE returnDrop);
```

Parameter
[表]
列: Parameter | Description
行 1:
  returnDrop
  The maximum voltage drop in Volts (V) to be set.
    
    A positive voltage has to be set regardless of the
    polarity of the actual or programmed current.
    
    Valid range and default value:
    
    XPS256:
    
    For the specification, refer to `Voltage drop protection / measurement`（raw: `350739.htm#_350739__s_Voltage_drop_protection`） in `XPS256 other performance characteristics`（raw: `350739.htm`）.
    
    The programmable range is 0.0 … 1.0 V for the force line and for the return
    line but, the total for the two lines must not exceed 1.0 V.
    
    Default value: 50 mV
    
    For a maximum
    voltage drop > 0.5 V, the open loop
    protection must be set to
    "NONE" by function `openLoopProtection()`（raw: `355803.htm`） and in
    the `DC Scale Safety editor`（raw: `354611.htm#_354611__s_DC_Scale_Safety_editor`） the `Vdrop Disco`（raw: `354611.htm#_354611__r_Vdrop_Disco`） parameter must be set to
    ON.
Return value
A reference to the
`SPMU_PIN_TASK`（raw: `55669.htm`）
 object.

### Example（取自子主题 SPMU_PIN_TASK.returnDropMax()）

### Maximum voltage drop of XPS256
```
SPMU_TASK spmuTask_1;

spmuTask_1.pin("...")
.mode("VFIM")
...
...
.forceDropMax (300 mV)
.returnDropMax (200 mV)
;
```

Note:
The example concentrates on the function described in this topic. More settings are
required for an executable SPMU_TASK object.

### Syntax（取自子主题 SPMU_PIN_TASK.returnDropWarn()）

```
SPMU_PIN_TASK & returnDropWarn(DOUBLE returnDropWarn);
```
Parameter
[表]
列: Parameter | Description
行 1:
  returnDropWarn
  The warning threshold in millivolt (mV) to be set.
    
    A positive voltage has to be set regardless of the
    polarity of the actual or programmed current.
    
    For the valid range refer to `Voltage drop protection / measurement`（raw: `350739.htm#_350739__s_Voltage_drop_protection`） in `XPS256 other performance characteristics`（raw: `350739.htm`）
Return value
A reference to the
`SPMU_PIN_TASK`（raw: `55669.htm`）
 object.

### Syntax（取自子主题 SPMU_PIN_TASK.samples()）

```
SPMU_PIN_TASK& samples(INT numOfSamples);
```
[表] Parameter
列: Parameter | Description
行 1:
  numOfSamples
  The number of samples, only used for averaging, if omitted the HW required minimum sample is
    used.
    
    For DC Scale channels, with exception of XPS256, the number of
    samples must be a power of 2.

### Return value（取自子主题 SPMU_PIN_TASK.samples()）

A reference to the
`SPMU_PIN_TASK`（raw: `55669.htm`）

object.

### Syntax（取自子主题 SPMU_PIN_TASK.settling()）

```
SPMU_PIN_TASK& settling(DOUBLE time);
```
[表] Parameter
列: Parameter | Description
行 1:
  time
  Settling time in seconds (s).
    
    Default is 0 seconds.
    
    Valid range is 0 s to 2 s.

### Return value（取自子主题 SPMU_PIN_TASK.settling()）

A reference to the
`SPMU_PIN_TASK`（raw: `55669.htm`）

object.

### Syntax（取自子主题 SPMU_PIN_TASK.vFilter()）

```
SPMU_PIN_TASK& vFilter(DOUBLE filterFrequency);
SPMU_PIN_TASK& vFilter(const STRING & filterFrequency);
```
[表] Parameter
列: Parameter | Description
行 1:
  filterFrequency
  Defines the filter frequency in Hertz (Hz) or switches the
    filter off. The parameter can be defined as double value or as
    string.
    
    Programmable double values are
    
    Value between the card-specific minimum and maximum value:
    The filter is switched on and set to the defined value.
    
    0.0: The filter is set to the card-specific default
    value.
    
    Programmable strings are
    
    "OFF": The filter is set to the card-specific default
    value.
    
    Card-specific range and default value:
    
    XPS256: Refer to section `Dynamic behavior`（raw: `354305.htm#_354305__s_Dynamic_behavior`） in `XPS256 programming - Force and clamp voltages`（raw: `354305.htm`）.

### Return value（取自子主题 SPMU_PIN_TASK.vFilter()）

A reference to the
`SPMU_PIN_TASK`（raw: `55669.htm`）

object.

### Example（取自子主题 SPMU_PIN_TASK.vFilter()）

The following example shows how to set the voltage filter and the current
filter.

```
SPMU_TASK spmuTask_1;

spmuTask_1.pin("...")
...
...
.vFilter("OFF") // Switch the voltage filter off
.iFilter(1000) // Set the current filter to 1 kHz
;
```

Note:
The example concentrates on the function described in this topic. More settings are
required for an executable SPMU_TASK object.

### Syntax（取自子主题 SPMU_PIN_TASK.vForce()）

```
SPMU_PIN_TASK& vForce(DOUBLE voltage);
```
[表] Parameter
列: Parameter | Description
行 1:
  voltage
  Forced voltage in Volt.

### Return value（取自子主题 SPMU_PIN_TASK.vForce()）

A reference to the
`SPMU_PIN_TASK`（raw: `55669.htm`）

object.

### Syntax（取自子主题 SPMU_PIN_TASK.vForceFilter()）

```
SPMU_PIN_TASK& vForceFilter (DOUBLE filterFrequency);
SPMU_PIN_TASK& vForceFilter (const STRING & filterFrequency);
```
[表] Parameter
列: Parameter | Description
行 1:
  filterFrequency
  Sets the filter to the given frequency in Hertz (Hz) or switches the filter off. The
    parameter can be defined as double value or as
    string.
    Programmable double values are
    
    Value between the card-specific minimum and maximum value:
    The filter is switched on and set to the defined value.
    
    0.0: The filter is set to the card-specific default
    value.
    
    Programmable strings are
    
    "OFF": The filter is set to the card-specific default
    value.
    
    Card-specific range and default value:
    
    XPS256: Refer to section `Dynamic behavior`（raw: `354305.htm#_354305__s_Dynamic_behavior`） in `XPS256 programming - Force and clamp voltages`（raw: `354305.htm`）.

### Return value（取自子主题 SPMU_PIN_TASK.vForceFilter()）

A reference to the
`SPMU_PIN_TASK`（raw: `55669.htm`）

object.

### Example（取自子主题 SPMU_PIN_TASK.vForceFilter()）

The following example shows how to set the force voltage filter and the clamp
current
filter.

```
SPMU_TASK spmuTask;

spmuTask.pin("###")
...
...
.vForceFilter(0) // Switch the force voltage filter off
.iClampFilter(1000) // Set the clamp current filter to 1 kHz
;
```

Note:
The example concentrates on the function described in this topic. More settings are
required for an executable SPMU_TASK object.

### Syntax（取自子主题 SPMU_PIN_TASK.vForceRange()）

```
SPMU_PIN_TASK& vForceRange(DOUBLE rangeValue);
```
[表] Parameter
列: Parameter | Description
行 1:
  rangeValue
  Expected value in Volt.
    
    SmarTest determines the voltage range automatically from the programmed force- or
    clamp-voltage if the range has not been defined by this API.

Note
 The voltage range depends on the underlying hardware.

### Return value（取自子主题 SPMU_PIN_TASK.vForceRange()）

A reference to the
`SPMU_PIN_TASK`（raw: `55669.htm`）

object.

### Syntax（取自子主题 SPMU_PIN_TASK.vMeasureRange()）

```
SPMU_PIN_TASK& vMeasureRange(DOUBLE rangeValue);
```
[表] Parameter
列: Parameter | Description
行 1:
  rangeValue
  Expected value in Volt.
    
    SmarTest determines the voltage range automatically from the pass/fail thresholds `min()`（raw: `131359.htm`） and `max()`（raw: `131360.htm`） if the expected value has not been defined by
    this API.

Note
 The voltage range depends on the underlying hardware.

### Return value（取自子主题 SPMU_PIN_TASK.vMeasureRange()）

A reference to the
`SPMU_PIN_TASK`（raw: `55669.htm`）

object.

### Syntax（取自子主题 SPMU_PIN_TASK.vSlewRate()）

```
SPMU_PIN_TASK& vSlewRate (const DOUBLE vSlewRate);
```
[表] Parameter
列: Parameter | Description
行 1:
  vSlewRate
  Defines the voltage slew rate in Volts per microsecond (V / µsec).
    Programmable
    double values are
    
    Value between the card-specific minimum and maximum value:
    The slew rate is set to the defined value.
    
    0.0: The slew rate is set to the card-specific default
    value.
    
    Card-specific range and default value:
    
    XPS256: Refer to section `Dynamic behavior`（raw: `354305.htm#_354305__s_Dynamic_behavior`） in `XPS256 programming - Force and clamp voltages`（raw: `354305.htm`）.

### Return value（取自子主题 SPMU_PIN_TASK.vSlewRate()）

A reference to the
`SPMU_PIN_TASK`（raw: `55669.htm`）

object.

### Example（取自子主题 SPMU_PIN_TASK.vSlewRate()）

The following example shows how to set the force voltage slew
rate.

```
SPMU_TASK spmuTask_1;

spmuTask_1.pin("...")
.mode("VFIM")
...
...
.vSlewRate(20 mV) // [V/us]
;
```

Note:
The example concentrates on the function described in this topic. More settings are
required for an executable SPMU_TASK object.

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
