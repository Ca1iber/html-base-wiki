---
type: object
title: SPMU_TASK
layer: L2
stage: testmethod
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234_SPMU_TASK.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# SPMU_TASK

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **51,836 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234_SPMU_TASK.htm>` 及其子主题 `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.01_SPMU_PIN_TASK.clamp.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.02_SPMU_PIN_TASK.compare.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.03_SPMU_PIN_TASK.connect.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.04_SPMU_PIN_TASK.connectState.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.05_SPMU_PIN_TASK.currentClampTimeToAlarm.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.06_SPMU_PIN_TASK.currentClampTimeToDisconnect.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.07_SPMU_PIN_TASK.disconnect.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.08_SPMU_PIN_TASK.execMode.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.09_SPMU_PIN_TASK.forceDropMax.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.10_SPMU_PIN_TASK.forceDropWarn.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.11_SPMU_PIN_TASK.highAccuracy.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.12_SPMU_PIN_TASK.iClampFilter.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.13_SPMU_PIN_TASK.iFilter.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.14_SPMU_PIN_TASK.iForce.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.15_SPMU_PIN_TASK.iForceRange.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.16_SPMU_PIN_TASK.iMeasureRange.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.17_SPMU_PIN_TASK.iSlewRate.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.18_SPMU_PIN_TASK.limits.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.19_SPMU_PIN_TASK.loadCap.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.20_SPMU_PIN_TASK.loadStepMode.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.21_SPMU_PIN_TASK.max.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.22_SPMU_PIN_TASK.measFilter.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.23_SPMU_PIN_TASK.min.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.24_SPMU_PIN_TASK.mode.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.25_SPMU_PIN_TASK.openLoopProtection.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.26_SPMU_PIN_TASK.preCharge.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.27_SPMU_PIN_TASK.pulldown.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.28_SPMU_PIN_TASK.relay.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.29_SPMU_PIN_TASK.returnDropMax.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.30_SPMU_PIN_TASK.returnDropWarn.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.31_SPMU_PIN_TASK.samples.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.32_SPMU_PIN_TASK.settling.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.33_SPMU_PIN_TASK.vFilter.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.34_SPMU_PIN_TASK.vForce.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.35_SPMU_PIN_TASK.vForceFilter.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.36_SPMU_PIN_TASK.vForceRange.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.37_SPMU_PIN_TASK.vMeasureRange.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.38_SPMU_PIN_TASK.vSlewRate.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01_SPMU_PIN_TASK.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.02_SPMU_TASK.execMode.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.03_SPMU_TASK.execute.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.04_SPMU_TASK.getFunctionalResult.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.05_SPMU_TASK.getPassFail.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.06_SPMU_TASK.getValue.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.07_SPMU_TASK.pin.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.08_SPMU_TASK.preAction.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.09_SPMU_TASK.setup.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.240_TASK_LIST.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
SPMU_TASK();
```

Creates an object to define different
conditions for DC measurements and to execute them concurrently.

Note
 Do not create static objects of the class in the test method and do not
create test method member variables from this class.

List of parameters
There are no parameters.
Return value
The constructor has no return value.

### Example

```
//DC Current Measurement
SPMU_TASK spmuTask;

ON_FIRST_INVOCATION_BEGIN();

spmuTask.pin("pmu1").mode("VFIM").vForce(2000 mV).clamp(200000 uA, 200000 uA).min(-200000 uA)
.max(200000 uA).vForceRange(6500 mV).iForceRange(1000000 uA).compare("I").samples(100).settling(1 ms)
.relay("NT").execMode("SER");

spmuTask.preAction("NPRM").execMode(TM::PVAL).execute();

ON_FIRST_INVOCATION_END();
double measuredValue = spmuTask.getValue("pmu1");
```

### Class definition（取自子主题 SPMU_PIN_TASK）

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

### Examples（取自子主题 SPMU_PIN_TASK）

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

### Syntax（取自子主题 SPMU_TASK.execMode()）

```
SPMU_TASK& execMode(const STRING& mode);
SPMU_TASK& execMode(const TM::DCTEST_MODE mode);
SPMU_TASK& execMode(const TM::DCFORCE_MODE mode);
```
Parameter
[表]
列: Parameter | Description
行 1:
  mode
  Default mode is TM:GPF.
    
    Refer to the list of available options of the mode parameter
    below.
[表] Available options of parameter: mode
列: mode | Description
行 1:
  "GPF"
    
    TM::GPF
  Sets the execution mode to return a global
    pass/fail result.
行 2:
  "PPF"
    
    TM::PPF
  Sets the execution mode to return per pin
    pass/fail results.
行 3:
  "PVAL"
    
    TM::PVAL
  Sets the execution mode to return per pin value
    and pass/fail results.
行 4:
  "FORCE_ON"
    
    TM::FORCE_ON
  Sets the instrument to the DC source in force
    mode. It does not perform a measurement. The
    instruments stays in this mode until
    TM::FORCE_OFF or another DC
    execution using this instrument occurs.
行 5:
  "FORCE_OFF"
    
    TM::FORCE_OFF
  Disables the use of the instrument as DC
    source.
行 6:
  "FORCE_AUTO"
    
    TM::FORCE_AUTO
  Sets the mode to use the instrument as a DC
    source. Thus it does not perform a measurement. The
    instruments statys in this mode until the end of the
    test suite execution.
行 7:
  "DCTEST_AUTO"
    
    TM::DCTEST_AUTO
  Sets the execution mode of DC tests to be
    retrieved from the settings of the `test suit flags`（raw: `78943.htm`）.

Note
 Either use the string (i.e.

"GPF"
) or the namespace, (i.e.

TM::GPF
) for setting the mode.

Return value
A reference to the
SPMU_TASK
 object.

Note
 To
retrieve results use the
`SPMU_TASK.getPassFail()`（raw: `131196.htm`）
 or
`SPMU_TASK.getValue()`（raw: `131197.htm`）
 functions.

### Examples（取自子主题 SPMU_TASK.execMode()）

### Example 1
The following example shows equal settings to set the mode to
return per pin pass/fail using the different
interfaces.

```
SPMU_TASK IFtask;

IFtask.execMode("PPF");

// is equal to
// IFtask.execMode(TM::PPF);
```

### Example 2

In this example, a SPMU
VFIM
 per-pin value test on the pin

HMPU1
 is performed via the utility pogo block. The measured current value is
retrieved. The pass/fail result are judged and logged. This approach is useful if you want to
do Kelvin connection type of measurements.

```
SPMU_TASK spmuTask;

ON_FIRST_INVOCATION_BEGIN();

CONNECT();

//
// The pin name determines that the SPMU is connected via the utility pogo block
//
spmuTask.pin("HPMU1").vForce(3 V).clamp(1.5 mA).min(0.5 mA).max(1 mA).relay("NTMBB");

spmuTask.execMode(TM::PVAL).execute();

ON_FIRST_INVOCATION_END();

//
// Upload results and log data
//
double iMeas;

iMeas = spmuTask.getValue("HPMU1");

cout << iMeas << endl;

TEST( "I/O1", "simpleSpmu", spmuTask.getPassFail("HPMU1")?TM::Pass:TM::Fail, TRUE);
```

### Syntax（取自子主题 SPMU_TASK.execute()）

```
void execute();
virtual void execute(const string& measurementName)
```
[表] Parameter
列: Parameter | Description
行 1:
  measurementName
  The measurementName is used with the Offline Result Emulation
    (ORE) feature of SmarTest. It refers to the corresponding offline measurement result
    specified in the ORE setup file.

Return value

There is no return value.

Note
 To retrieve results
use the
`SPMU_TASK.getPassFail()`（raw: `131196.htm`）
 or
`SPMU_TASK.getValue()`（raw: `131197.htm`）
 functions.

### Syntax（取自子主题 SPMU_TASK.getFunctionalResult()）

```
Boolean getFunctionalResult() const;
Boolean getFunctionalResult(const STRING& pinlist) const;
```
[表] Parameter
列: Parameter | Description
行 1:
  pinlist
  List of pins for which per pin pass/fail result should be retrieved.

Note
 Apply the corresponding mode with
`SPMU_TASK.execMode()`（raw: `131193.htm`）
 to retrieve
per pin value results.

Return Value

Returns a
Boolean true
 for pass or
false
 for fail
result of the measurement.

### Syntax（取自子主题 SPMU_TASK.getPassFail()）

```
Boolean getPassFail() const;
Boolean getPassFail(const STRING& pinlist) const;
```
[表] Parameter
列: Parameter | Description
行 1:
  pinlist
  List of pins for which the a per pin pass/fail result should be retrieved.

Return Value

Returns a
Boolean true
 for pass or
false
 for fail
result of the measurement.

### Syntax（取自子主题 SPMU_TASK.getValue()）

```
DOUBLE getValue(const STRING& pin) const;
```
[表] Parameter
列: Parameter | Description
行 1:
  pin
  Pins for which per pin value result should be retrieved.

Note
 Apply the corresponding mode with
`SPMU_TASK.execMode()`（raw: `131193.htm`）
 to retrieve
per pin value results.

### Return value（取自子主题 SPMU_TASK.getValue()）

The result of the measurement as data type

DOUBLE
 in either Ampere or Volt.

In case the result is out of range
999999999 is returned when used with DC Scale cards.

### Syntax（取自子主题 SPMU_TASK.pin()）

```
SPMU_PIN_TASK& SPMU_TASK::pin(const STRING& pinlist);
```
Parameter
[表]
列: Parameter | Description/Range
行 1:
  pinlist
  Target pin name for digital pin for which the user wants to define
    measurement conditions.
    
    Users can specify multiple pins by separating pin
    entries with a comma.
Return value
A reference to the
`SPMU_PIN_TASK`（raw: `55669.htm`）
 object.

### Example（取自子主题 SPMU_TASK.pin()）

In this example, the pin
I/O0
 is used as DC source to provide

10 uA
 current for the connected DUT
pin.

```
SPMU_TASK spmuTask;

ON_FIRST_INVOCATION_BEGIN();

CONNECT();

//
// Setup
//
spmuTask.pin("I/O0").iForce(10 uA).clamp(3.5 V).min(1.5 V).max(3 V).relay("NTMBB");

//
// Force 10uA
//
spmuTask.execMode(TM::FORCE_ON).execute();

ON_FIRST_INVOCATION_END();
```

### Syntax（取自子主题 SPMU_TASK.preAction()）

```
SPMU_TASK& preAction(const STRING& action);
```
[表] Parameter
列: Parameter | Description
行 1:
  action
  The following actions are available:
    
    "NONE" - Default. Conditional primary
    activation.
    
    The currently loaded digital primary settings will be
    activated if it is not active already.
    
    "NPRM" - No primary activation!
    
    "FTST" - Performs a functional test
    after activating the currently loaded digital primary
    settings.

Note
 To activate primary settings specified with
`PRIMARY_STATUS`（raw: `29640.htm`）
 execute a
`FLUSH()`（raw: `29338.htm`）
 before calling this function.

### Return value（取自子主题 SPMU_TASK.preAction()）

A reference to the
SPMU_TASK

object.

Note
 To retrieve the result of the functional test use
`SPMU_TASK.getFunctionalResult()`（raw: `131198.htm`）
.

### Syntax（取自子主题 SPMU_TASK.setup()）

```
void setup();
```

List of parameters

There are no parameters.

Return value

There is no return value.

### Example（取自子主题 SPMU_TASK.setup()）

The following example performs two measurements,
spmuVMeas
 and

spmuIMeasa
. The
spmuVMeas
 is setup and executed on all
sites first. Then
spmuIMeasa
 is defined and downloaded to the HW using

SPMU_TASK.setup()
. The per site value of the voltage measured is set as
parameter of
`SPMU_PIN_TASK.vForce()`（raw: `131353.htm`）
 before the
spmuIMeasa
 measurement is
performed on all sites.

```
SPMU_TASK spmuVMeas, spmuIMeas;

ON_FIRST_INVOCATION_BEGIN();
// Measure Voltage
spmuVMeas.pin("dc_pin").iForce(1 mA).min(1 V).max(2 V).mode("IFVM").relay("NTMBB");
spmuVMeas.execMode("PVAL").execute();

// Define measurement placeholder
spmuIMeas.pin("dc_pin").vForce(1 V).min(-1 mA).max(1 mA).mode("VFIM").relay("NTMBB");
spmuIMeas.execMode(TM::FORCE_ON);
// write measurement definition to HW
spmuIMeas.setup();

// setup force voltage per site
FOR_EACH_SITE_BEGIN();
spmuIMeas.pin("dc_pin").vForce(spmuVMeas.getValue("dc_pin"));
FOR_EACH_SITE_END();

// force voltage per site
spmuIMeas.execute();

ON_FIRST_INVOCATION_END();
```

### Class definition（取自子主题 TASK_LIST）

This API is defined in the header file

/opt/hp93000/soc/prod_com/include/MAPI/TaskList.h
.

Constructor

```
TASK_LIST();
```

This constructor defines a task list that holds task names to be
executed.

Parameters

There are no parameters associated with this function.

Member functions:

`add()`（raw: `29792.htm#_29792__dle_add`）

`setup()`（raw: `29792.htm#_29792__dle_setup`）

`execute()`（raw: `29792.htm#_29792__dle_execute`）

### Usage（取自子主题 TASK_LIST）

For creating an object:

```
TASK_LIST <object>;
```

For setting up tasks to be performed:

```
<object>.add(task1).add(task2)...add(taskN);
```

For downloading the settings in tasks:

```
<object>.setup();
```

For downloading the settings in tasks and performing the tasks:

```
<object>.execute();
```

[表]
行 1:
  <object>
  Object name to be defined
行 2:
  task1-N
  Object name of the PPMU_SETTING, PPMU_RELAY or
    PPMU_MEASURE class to specify a task to
    be performed. A task list can contain up to 10 tasks.

### Member functions（取自子主题 TASK_LIST）

add()

```
TASK_LIST & add(const TASK& task);
```

This function adds the specified task to the task list. Added tasks are
performed sequentially.

Note
 If you define a
TASK_LIST
 object as
global, the object will not be destroyed when the test method is
completed. This will have the effect that the list grows longer with
every testflow repetition, so that the test time is increased with every
repetition.

[表] Parameter
行 1:
  task
  Object name of the PPMU_SETTING, PPMU_RELAY or
    PPMU_MEASURE class to specify a
    task be performed.

Using the offline result emulation function:

Measurements can be made by using
`DPS_TASK`（raw: `55630.htm`）
,
`SPMU_TASK`（raw: `55670.htm`）
, and

`PPMU_MEASURE`（raw: `29585.htm`）
 objects directly (by calling their

execute()
 member functions) or be put in a

TASK_LIST
 object which queues up tasks to be executed (by calling
the
execute()
 method on the
TASK_LIST
 object
rather than on the task objects themselves). This requires an enhancement also on the

TASK_LIST add()
 method which takes a measurement name as
additional parameter.

```
TASK_LIST& add(const TASK& task)
```

This is the existing function which adds the specified task to the task list.

```
TASK_LIST& add(const TASK& task, const string& measurementName)
```

This function adds the specified task to the task list.

Parameter

[表]
行 1:
  measurementName
  Associate the measurement that will be executed by calling
    task_list.execute() with offline data.

For more details, see
`Parametric offline result emulation`（raw: `128581.htm`）
 in
`Offline Result Emulation`（raw: `128475.htm`）
.

setup()

```
void setup();
```

This function downloads settings defined in the task list. The tasks of
the task list are executed sequentially in the registered order. It is
used when the input parameters of the task are changed during the test
method execution. It can change the parameters of an exisiting MSET and
reuse it to avoid running out of MSETs. (Refer to
`FlexDC`（raw: `122087.htm`）
 and
`Managing DC Tests with Variable Parameters`（raw: `75890.htm`）
 for details.)

Parameters

There are no parameters associated with this function.

execute()

```
void execute();
```

This function performs a test by executing the task list. The tasks of
the task list are executed sequentially in the registered order.

Parameters

There are no parameters associated with this function.

Note
 After the
execute()
 function is performed, you cannot
define any tasks for the digital pin that is not included to the
performed task. For example, the following program defines and executes
the "tasks" task list.

```
PPMU_SETTING setting1;
TASK_LIST tasks;

tasks.add(setting1);

setting1.pin("pin1").vForce(2.1 mV);
setting1.pin("pin1").iRange("10uA");
setting1.pin("pin1").min(0.1 uA).max(5.0 uA);

tasks.execute();
```

After that, you can modify or define tasks for "pin1" as shown below:

```
setting1.pin("pin1").vForce(2.5 mV); // OK
```

However, error occurs if the following program is performed because tasks
for "pin2" is not defined in the "tasks" task list.

```
setting1.pin("pin2").vForce(2.1 mV); // error
```

### Example（取自子主题 TASK_LIST）

In the following example, the task
setting
,
precharge
,

relay_on
,
relay_off
,

ppmuMeasure
,
clamp_on
 and

clamp_off
 are defined and added to the task list. Then a PPMU
measurement is performed by executing the task list.

```
PPMU_SETTING ppmuSetting;
PPMU_RELAY ppmuRelay_on, ppmuRelay_off;
PPMU_MEASURE ppmuMeasure;
PPMU_CLAMP ppmuClamp_on, ppmuClamp_off;
TASK_LIST taskList_1;

ON_FIRST_INVOCATION_BEGIN();

//
// Setups for PPMU
//
ppmuSetting.pin("S0").iRange(1 mA).min(0 V).max(4.3 V).iForce(10 uA);
ppmuSetting.pin("S1").iRange(10 mA).min(-10 uA).max(30 uA).vForce(3.3 V);

//
// Relay setups
//
ppmuRelay_on.pin("S0,S1").status("PPMU_ON");
ppmuRelay_on.wait(1.3 ms);
ppmuRelay_off.pin("S0,S1").status("AC_ON");

//
// Measurement setups
//
ppmuMeasure.pin("S0,S1").execMode(TM::PVAL);

//
// Hardware specific programming to avoid hot switching on the current force setup
//
ppmuClamp_on.pin("S0").status("CLAMP_ON").low(2.6 V).high(2.9 V);
ppmuClamp_off.pin("S0").status("CLAMP_OFF");

//
// Build and execute the task list
//
taskList_1.add(ppmuSetting)
.add(ppmuClamp_on)
.add(ppmuRelay_on)
.add(ppmuClamp_off)
.add(ppmuMeasure)
.add(ppmuRelay_off);

taskList_1.execute();

ON_FIRST_INVOCATION_END();

//
// Result upload and Datalog
//
double VMeas, IMeas;

VMeas = ppmuMeasure.getValue("S0");
IMeas = ppmuMeasure.getValue("S1");

TEST("DC_Test",ppmuMeasure, true);
```

The following example shows how to measure a current on a device pin and then use it
as a force value for a following measurement for multi-sites. The result value of
the first measurement differs from site to site.

```
PPMU_MEASURE ppmuMeasure2;

ON_FIRST_INVOCATION_BEGIN();

PPMU_MEASURE ppmuMeasure1;
PPMU_SETTING ppmuSetting1,ppmuSetting2;
PPMU_RELAY ppmuRelayOn, acRelayOn;
TASK_LIST multiDeltaFlexDc1, multiDeltaFlexDc2;

// 1st measurement
ppmuSetting1.pin("I/O1").vForce(0 V).iRange(1 uA).max(1 uA).min(-1 uA);
ppmuRelayOn.pin("I/O1").status("PPMU_ON");
ppmuRelayOn.wait(1.3 ms);
ppmuMeasure1.pin("I/O1").execMode(TM::PVAL);
acRelayOn.pin("I/O1").status("AC_ON");
multiDeltaFlexDc1.add(ppmuSetting1).add(ppmuRelayOn).add(ppmuMeasure1);
multiDeltaFlexDc1.execute();

// dummy setting for avoiding DC set run out
ppmuSetting2.pin("I/O1").iForce(0 uA).iRange(1 mA).max(0.5 V).min(-0.5 V);
ppmuSetting2.wait(1 ms);
ppmuMeasure2.pin("I/O1").execMode(TM::PVAL);
multiDeltaFlexDc2.add(ppmuSetting2).add(ppmuMeasure2).add(acRelayOn);
multiDeltaFlexDc2.setup();

// 2nd measurement
FOR_EACH_SITE_BEGIN();

ppmuSetting2.pin("I/O1")
.iForce(ppmuMeasure1.getValue("I/O1"))
.iRange(ppmuMeasure1.getValue("I/O1"))
.max(0.5 V)
.min(-0.5 V);

FOR_EACH_SITE_END();

multiDeltaFlexDc2.execute();

ON_FIRST_INVOCATION_END();

TEST("I/O1",
"multi_delta",
ppmuMeasure2.getPassFail("I/O1")?TM::Pass:TM::Fail,
ppmuMeasure2.getValue("I/O1"),
true );
```

<!-- 语法节 end -->

## 是什么

**文档事实** `SPMU_TASK` 是 MAPI 的 test method API，用于定义并执行并行 DC 测量：既覆盖 PMU 模式下的 DC Scale 卡，也覆盖数字卡的 BADC（board ADC）。该 API 定义在 `/opt/hp93000/soc/prod_com/include/MAPI/SpmuTask.h`。

**文档事实** 文档明确 `SPMU_TASK` 是历史遗留名称（legacy name），并注明 SmarTest 7.10 不支持 High Precision PMU（System PMU）。

**文档事实** 与其他 API 的配合方式由文档给出：与 `TASK_LIST` 联用时，可定义多个 DC 测量并按顺序执行；与 `SPMU_PIN_TASK` 联用时，可更改测量所需的 relay 设置。

**文档事实** 该类对象用于为 DC 测量定义条件并并发执行这些测量；每个 pin 的测量条件由 `pin()` 返回的 `SPMU_PIN_TASK&` 对象承载。成员函数包括 `pin()`、`execMode()`、`preAction()`、`setup()`、`execute()`、`getValue()`、`getPassFail()`、`getFunctionalResult()`。

**文档事实** 构造函数无参数、无返回值。文档 Note 明确：不要在 test method 中创建该类的静态对象，也不要创建该类的 test method 成员变量。

**文档事实** `execMode()` 的执行模式包括 `"GPF"`（默认，`TM::GPF`）、`"PPF"`、`"PVAL"`、`"FORCE_ON"`、`"FORCE_OFF"`、`"FORCE_AUTO"`、`"DCTEST_AUTO"`；`preAction()` 的动作包括 `"NONE"`（默认）、`"NPRM"`、`"FTST"`。

## 典型用法

**文档事实** 主文档的 DC Current Measurement 示例展示了完整链式流程：`pin("pmu1")` 后依次设置 `mode("VFIM")`、`vForce()`、`clamp()`、`min()`/`max()`、`vForceRange()`、`iForceRange()`、`compare()`、`samples()`、`settling()`、`relay()`、per-pin `execMode("SER")`；随后 `preAction("NPRM").execMode(TM::PVAL).execute()`；最后在 `ON_FIRST_INVOCATION_END()` 之后用 `getValue("pmu1")` 读取结果。

**文档事实** 高阻测量示例使用 `mode("VM_HIZ")`、`settling(1 ms)`、`relay("TERM")`、`min()`/`max()` 配置端接高阻测量，再以 `preAction("NONE").execMode("PVAL").execute()` 执行，并在 first-invocation block 之外读取 `getValue("pinName")`。

**文档事实** `execute()` 在测量条件尚未下载到 firmware 时会先执行 `SPMU_TASK.setup()`。`getValue()` 返回 `DOUBLE`，单位按测量模式为 A 或 V；文档注明使用 DC Scale 卡时，结果超出范围会返回 `999999999`。

**文档事实** `setup()` 示例展示“先测量、再按 site 设置 force 值”的两步流程：`spmuVMeas` 配置并 `execute()` 测电压；`spmuIMeas` 配置后先 `setup()` 把定义写入 HW；随后在 `FOR_EACH_SITE_BEGIN()` / `FOR_EACH_SITE_END()` 中用 `spmuVMeas.getValue("dc_pin")` 逐 site 设置 `vForce()`；最后 `spmuIMeas.execute()`。

**文档事实** `SPMU_PIN_TASK` 的 `connect()` / `disconnect()` 文档指出：同一 task 内，在 `connect()` 或 `disconnect()` 之前调用的其他函数不会被考虑；若同一 `SPMU_TASK` 中有的 pin 要 connect、有的要 disconnect，必须拆成两个 task 分别 `execute()`。

**建议** 需要复用测量定义或按序执行多个 DC 测量时，把 `SPMU_TASK` 放入 `TASK_LIST`；单次测量则可直接调用 `execute()`（`TASK_LIST` 文档说明这两种方式都存在）。

## 和谁有关

- **文档事实** 与 `SPMU_PIN_TASK`：文档说明 `SPMU_PIN_TASK` 对象只能通过 `SPMU_TASK.pin()` 取得；主文档同时说明与 `SPMU_PIN_TASK` 联用时可更改测量所需的 relay 设置。`pin()` 因此是进入 per-pin 设置的入口。
- **文档事实** 与 `TASK_LIST`：主文档说明与 `TASK_LIST` 联用可定义多个 DC 测量并按顺序执行；`TASK_LIST` 文档说明 `SPMU_TASK` 等任务对象既可直接 `execute()`，也可放入 `TASK_LIST` 由它排队执行。
- **文档事实** 与本类成员子主题：`02.07.04.01.234.02`–`.09` 分别记录 `SPMU_TASK.execMode()`、`execute()`、`getFunctionalResult()`、`getPassFail()`、`getValue()`、`pin()`、`preAction()`、`setup()`；主文档 `Subtopics` 列出这些入口。
- **文档事实** 与 DC Scale 卡（DPS128/64、XPS256）：多个 `SPMU_PIN_TASK` 成员注明仅特定卡支持（如 `clamp()` 双参数形式、`connectState()`、`forceDropMax()`/`returnDropMax()`、`loadCap()`、`openLoopProtection()`、`preCharge()` 的 `"SAFE_CON"` 等）；入边还显示 XPS256 文档称 PMU operating mode 的 force/clamp/measure 与电压降测量由 `SPMU_TASK`/`SPMU_PIN_TASK` 覆盖。
- **文档事实** 与 PS1600 / Pin Scale 5000 的 DC value measurements：入边说明 BADC 的 AMUX 可在功能测试前通过 `FLEX_RELAY` 或 `SPMU_TASK` API 设置。
- **文档事实** 与 `PPMU_SETTING`、`PPMU_RELAY`、`BADC_SETTING`、`BADC_MEASURE`、`PATTERN_CONTROLLER`、`DC_RESULT_ACCESSOR`：主文档 Example 2 用它们搭建 pattern-controlled 高阻电压测量并读取结果（示例级关系）。
- **文档事实** 与 `DC Test Programming`、`Offline Result Emulation`：主文档 `Related information` 列出这两个主题；入边另有 `Offline result emulation for Class SPMU_TASK`，以及 `TESTSET::judgeAndLog_Spmu`（其说明为“指定要判定的 `SPMU_TASK` 对象”）。

## 版本

**文档事实** `Functional changes` 原文记录：
- Introduced before SmarTest 6.3.2

**文档事实** 该节未列出后续版本新增项；本页语法节中出现的 `connectState()`、`forceDropMax()`、`returnDropMax()`、`highAccuracy()` 等成员，其引入版本未在本页 `Functional changes` 中给出。

## 出处

- 主文档：`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234_SPMU_TASK.htm`（Subtopics、Syntax、Example、Related information、Functional changes）。
- 语法/参数材料另取自其子主题 `02.07.04.01.234.01_SPMU_PIN_TASK.htm` 及 `02.07.04.01.234.01.01`–`.38`、`02.07.04.01.234.02`–`.09`、`02.07.04.01.240_TASK_LIST.htm`（objscaffold 逐字汇总，已读）。
- 「和谁有关」另参考 `extract/edges.jsonl` 中指向/离开该页的边记录。
