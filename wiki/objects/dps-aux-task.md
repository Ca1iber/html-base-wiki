---
type: object
title: DPS_AUX_TASK
layer: L2
stage: level
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43_DPS_AUX_TASK.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# DPS_AUX_TASK

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **73,873 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43_DPS_AUX_TASK.htm>` 及其子主题 `<02_System_reference/02.06_Command_Reference/02.06.02.02.183_PRLT__-__request_Parallel_ResuLTs.htm>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.188_PSAS__-__Power_Supply_Accumulated_Status.htm>`、`<02_System_reference/02.06_Command_Reference/02.06.02.02.33_CSAS__-__Channel_Slot_Accumulated_Status.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.240_TASK_LIST.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.01.01_DPS_AUX_PIN_TASK.checkIcHacError.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.01.02_DPS_AUX_PIN_TASK.checkPowerFlags.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.01.03_DPS_AUX_PIN_TASK.checkSetRangeError.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.01.04_DPS_AUX_PIN_TASK.checkSurgeTracker.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.01.05_DPS_AUX_PIN_TASK.selectISensorSetThresholds.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.01.06_DPS_AUX_PIN_TASK.selectVSensorSetThresholds.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.01.07_DPS_AUX_PIN_TASK.setMode.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.01_DPS_AUX_PIN_TASK.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.02_DPS_AUX_TASK.execute.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.03_DPS_AUX_TASK.pin.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.04_DPS_AUX_TASK.setup.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.05_DPS_AUX_TASK.getSurgeTrackerStatus.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06.01_DPS_AUX_TASK.getAllStatus.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06.02_DPS_AUX_TASK.getStatusWithoutConstCur.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06.03_DPS_AUX_TASK.getStatusWithoutConstVol.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06.04_DPS_AUX_TASK.getClampDistanceTooLow.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06.05_DPS_AUX_TASK.getConstantCurrent.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06.06_DPS_AUX_TASK.getConstantCurrentLimitDisconnect.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06.07_DPS_AUX_TASK.getConstantVoltage.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06.08_DPS_AUX_TASK.getCurrentLimiterProtectionDetected.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06.09_DPS_AUX_TASK.getDutBoardDisconnect.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06.10_DPS_AUX_TASK.getLowHeadroom.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06.11_DPS_AUX_TASK.getOvercurrent.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06.12_DPS_AUX_TASK.getOvertemperature.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06.13_DPS_AUX_TASK.getOvervoltage.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06.14_DPS_AUX_TASK.getRangeOverflow.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06.15_DPS_AUX_TASK.getSafetyLine.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06.16_DPS_AUX_TASK.getUnregulated.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06.17_DPS_AUX_TASK.getVoltageDropForce.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06.18_DPS_AUX_TASK.getVoltageDropForceWarn.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06.19_DPS_AUX_TASK.getVoltageDropReturn.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06.20_DPS_AUX_TASK.getVoltageDropReturnWarn.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06_DPS_power_flags_-_get...___functions.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.07.01_DPS_AUX_TASK.getIcHacError.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.07.02_DPS_AUX_TASK.getRangeError.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.07_DPS_status_flags_-_get...___functions.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.88_GET_FUNCTIONAL_RESULT.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
DPS_AUX_TASK();
```

Creates an object of the DPS_AUX_TASK
class.

Note
 Do not create static objects of the class in the test method and do not
create test method member variables from this class.

List of parameters

There are no parameters.

### Return value

The constructor has no return value.

### Examples

### Example 1

The example below sets current thresholds, activates the surge tracker, checks the
status against the current thresholds, and retrieves the result.

```
DPS_AUX_TASK auxTask;

ON_FIRST_INVOCATION_BEGIN();

//
// Set the current thresholds to -1 mA/1 mA and switch on surge tracker
//
auxTask.pin("dps1")
.selectISensorSetThresholds(-1 mA, 1 mA)
.setMode(TM::SURGE_TRACKER);

auxTask.execute();

auxTask.pin("dps1").checkSurgeTracker(TM::AGAINST_BOTH);

ON_FIRST_INVOCATION_END();

//
// Get the result of surge tracker
//
TM::SURGE_TRACKER_STATUS surgeTrackerStatus = auxTask.getSurgeTrackerStatus("dps1");

switch (surgeTrackerStatus)
{
case TM::SURGE_TRACKER_NONE_DETECTED:

cout << "DPS_AUX_TASK::getSurgeTrackerStatus for pin dps1: SURGE_TRACKER_NONE_DETECTED"
<< endl << endl;

break;

case TM::SURGE_TRACKER_HIGH_DETECTED:

cout << "DPS_AUX_TASK::getSurgeTrackerStatus for pin dps1: SURGE_TRACKER_HIGH_DETECTED"
<< endl << endl;

break;

case TM::SURGE_TRACKER_LOW_DETECTED:

cout << "DPS_AUX_TASK::getSurgeTrackerStatus for pin dps1: SURGE_TRACKER_LOW_DETECTED"
<< endl << endl;

break;

case TM::SURGE_TRACKER_BOTH_DETECTED:

cout << "DPS_AUX_TASK::getSurgeTrackerStatus for pin dps1: SURGE_TRACKER_BOTH_DETECTED"
<< endl << endl;

break;

default:

break;
};
```

### Example 2: Site‑specific thresholds for XPS256

The example activates both the voltage surge tracker and the current surge tracker of an
`XPS256`（raw: `350312.htm`）
 pin. Common thresholds are defined in the
`ON_FIRST_INVOCATION`（raw: `29526.htm`）
 block and replaced with
site‑specific thresholds in the
`FOR_EACH_SITE`（raw: `29344.htm`）

loop.

To prevent
`DPS_AUX_PIN_TASK.setMode()`（raw: `141294.htm`）
 from issuing a warning, this function is called only
outside the
FOR_EACH_SITE
 loop.
`RDI_INIT()`（raw: `141275.htm`）
 is used
at the very beginning as a prerequisite of the
`SmartRDI`（raw: `142069.htm`）
 code to be
implemented for the DUT test. The surge tracker results are read within another

FOR_EACH_SITE
 loop to comply with requirements of
SmartRDI.

```
RDI_INIT();

ON_FIRST_INVOCATION_BEGIN();
{
DPS_AUX_TASK auxTask;

//
// Setup surge tracker
//
double vThresholdLow = -0.5 V;
double vThresholdHigh = 3.5 V;
double iThresholdLow = -0.1 A;
double iThresholdHigh = 0.4 A;

auxTask.pin("XPS256_PMU_1")
.setMode (TM::SURGE_TRACKER)
.selectVSensorSetThresholds (vThresholdLow, vThresholdHigh)
.selectISensorSetThresholds (iThresholdLow, iThresholdHigh);

FOR_EACH_SITE_BEGIN();
{
//
// Set site specific thresholds
//
...
...

//
// Apply site specific thresholds
//
auxTask.pin("XPS256_PMU_1")
.selectVSensorSetThresholds (vThresholdLow, vThresholdHigh)
.selectISensorSetThresholds (iThresholdLow, iThresholdHigh);
}
FOR_EACH_SITE_END();

auxTask.execute();

//
// Setup and execute the DUT test
//
...
...

//
// Check the state of the surge tracker for all sites
//
auxTask.pin("XPS256_PMU_1").checkSurgeTracker(TM::AGAINST_BOTH);

FOR_EACH_SITE_BEGIN();
{
TM::SURGE_TRACKER_STATUS statusVoltage, statusCurrent;

auxTask.getSurgeTrackerStatus("XPS256_PMU_1", statusVoltage, statusCurrent);

cout << "Site " << CURRENT_SITE_NUMBER() << ", Voltage surge tracker: " << statusVoltage << endl;
cout << "Site " << CURRENT_SITE_NUMBER() << ", Current surge tracker: " << statusCurrent << endl;
}
FOR_EACH_SITE_END();
}
ON_FIRST_INVOCATION_END();
```

### Syntax（取自子主题 DPS_AUX_PIN_TASK）

This class has no constructor.

List of parameters

There are no parameters.

Return value

There is no return value.

### Example（取自子主题 DPS_AUX_PIN_TASK）

The example below sets current thresholds, activates the surge tracker, checks the
status against the current thresholds, and retrieves the result.

```
DPS_AUX_TASK auxTask;

ON_FIRST_INVOCATION_BEGIN();

//
// Set the current thresholds to -1 mA/1 mA and switch on surge tracker
//
auxTask.pin("dps1")
.selectISensorSetThresholds(-1 mA, 1 mA)
.setMode(TM::SURGE_TRACKER);

auxTask.execute();

auxTask.pin("dps1").checkSurgeTracker(TM::AGAINST_BOTH);

ON_FIRST_INVOCATION_END();

//
// Get the result of surge tracker
//
TM::SURGE_TRACKER_STATUS surgeTrackerStatus = auxTask.getSurgeTrackerStatus("dps1");

switch (surgeTrackerStatus)
{
case TM::SURGE_TRACKER_NONE_DETECTED:

cout << "DPS_AUX_TASK::getSurgeTrackerStatus for pin dps1: SURGE_TRACKER_NONE_DETECTED"
<< endl << endl;

break;

case TM::SURGE_TRACKER_HIGH_DETECTED:

cout << "DPS_AUX_TASK::getSurgeTrackerStatus for pin dps1: SURGE_TRACKER_HIGH_DETECTED"
<< endl << endl;

break;

case TM::SURGE_TRACKER_LOW_DETECTED:

cout << "DPS_AUX_TASK::getSurgeTrackerStatus for pin dps1: SURGE_TRACKER_LOW_DETECTED"
<< endl << endl;

break;

case TM::SURGE_TRACKER_BOTH_DETECTED:

cout << "DPS_AUX_TASK::getSurgeTrackerStatus for pin dps1: SURGE_TRACKER_BOTH_DETECTED"
<< endl << endl;

break;

default:

break;
};
```

### Syntax（取自子主题 DPS_AUX_PIN_TASK.checkIcHacError()）

```
DPS_AUX_PIN_TASK & checkIcHacError();
```

List of parameters

There are no parameters.

### Return value（取自子主题 DPS_AUX_PIN_TASK.checkIcHacError()）

A reference to the corresponding
`DPS_AUX_PIN_TASK`（raw: `141284.htm`）

object.

For retrieving the read result see
`DPS_AUX_TASK.getIcHacError()`（raw: `144799.htm`）
.

### Example（取自子主题 DPS_AUX_PIN_TASK.checkIcHacError()）

```
DPS_AUX_TASK auxTask;

ON_FIRST_INVOCATION_BEGIN();

auxTask.pin("dps2").checkIcHacError();

ON_FIRST_INVOCATION_END();

if ( auxTask.getIcHacError("dps2") == TM::AUX_TASK_STATUS_PASS )
{
cout << "auxTask.getIcHacError(\"dps2\") returned TM::AUX_TASK_STATUS_PASS" << endl;
}
else
{
cout << "auxTask.getIcHacError(\"dps2\") returned TM::AUX_TASK_STATUS_FAIL" << endl;
}
```

### Syntax（取自子主题 DPS_AUX_PIN_TASK.checkPowerFlags()）

```
DPS_AUX_PIN_TASK& checkPowerFlags(TM::POWER_FLAG flags = TM::ALL_FLAGS);
```
[表] Parameter
列: Parameter | Description
行 1:
  flags
  The optional parameter defines a read mask for the power supply
    flags.
    The default value is
    TM::ALL_FLAGS.
[表] Available options of parameter: flags
列: Option | Description
行 1:
  TM::ALL_FLAGS
  Enables all flags for reading.
    This is the default
    value.
行 2:
  TM::CONST_VOLTAGE
    
    TM::CONST_CURRENT
    
    TM::UNREGULATED
    
    TM::OVER_VOLTAGE
    
    TM::OVER_CURRENT
    
    TM::OVER_TEMPERATURE
    
    TM::VOL_DROP_FORCE
    
    TM::VOL_DROP_RETURN
    
    TM::DUTBOARD_DISCON
    
    TM::SAFETY_LINE
    
    TM::CONST_CURR_LIMIT_DISCON
    
    TM::LOW_HEADROOM
    
    TM::CURR_LIMIT_PROTECT_DELE
    
    TM::RANGE_OVERFLOW
    
    TM::CLAMP_DISTANCE_TOO_LOW
    
    TM::VOL_DROP_FORCE_WARN
    
    TM::VOL_DROP_RETURN_WARN
  Enables only the selected flag for reading.
    Refer to `DPS power flags - get...() functions`（raw: `150053.htm`） for more information.

### Return value（取自子主题 DPS_AUX_PIN_TASK.checkPowerFlags()）

A reference to the corresponding
`DPS_AUX_PIN_TASK`（raw: `141284.htm`）
 object.

For retrieving the read result see
`DPS power flags - get...() functions`（raw: `150053.htm`）
.

### Example（取自子主题 DPS_AUX_PIN_TASK.checkPowerFlags()）

The following example reads the actual state of all power flags, clears all
flags and evaluates the state of all flags except the "
Constant
Voltage
" flag. The returned value is set to

TM::POWER_FLAG_STATUS_FAIL
 if minimum one of the checked
flags is set.

```
DPS_AUX_TASK dpsAuxTask_1;

ON_FIRST_INVOCATION_BEGIN();
{
//
// Read actual power flag status of two pins
//
dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read latched state & clear all flags
dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read actual state & clear all flags
}
ON_FIRST_INVOCATION_END();

//
// Evaluate the state of the first pin
//
if (dpsAuxTask_1.getStatusWithoutConstVol("dps1") == TM::POWER_FLAG_STATUS_PASS)
{
cout << "dpsAuxTask_1.getStatusWithoutConstVol(\"dps1\") returned TM::POWER_FLAG_STATUS_PASS" << endl;
}
else
{
cout << "dpsAuxTask_1.getStatusWithoutConstVol(\"dps1\") returned TM::POWER_FLAG_STATUS_FAIL" << endl;
}

return;
```

The next example reads, clears and evaluates the latched state
of the "
Low Headroom
" flag. The other flags are not cleared or
evaluated.

```
DPS_AUX_TASK dpsAuxTask_2;

ON_FIRST_INVOCATION_BEGIN();
{
//
// Read and clear latched low headroom flag of two pins
//
dpsAuxTask_2.pin("dps1,dps2").checkPowerFlags(TM::LOW_HEADROOM);
}
ON_FIRST_INVOCATION_END();

//
// Evaluate the state of the first pin
//
if (dpsAuxTask_2.getLowHeadroom("dps1") == TM::POWER_FLAG_STATUS_PASS)
{
cout << "dpsAuxTask_2.getLowHeadroom(\"dps1\") returned TM::POWER_FLAG_STATUS_PASS" << endl;
}
else
{
cout << "dpsAuxTask_2.getLowHeadroom(\"dps1\") returned TM::POWER_FLAG_STATUS_FAIL" << endl;
}

return;
```

### Syntax（取自子主题 DPS_AUX_PIN_TASK.checkSetRangeError()）

```
DPS_AUX_PIN_TASK & checkSetRangeError();
```

List of parameters
There are no parameters.
Return value

A reference to the corresponding
`DPS_AUX_PIN_TASK`（raw: `141284.htm`）
 object.

For retrieving
the read result see
`DPS_AUX_TASK.getRangeError()`（raw: `144800.htm`）
.

### Example（取自子主题 DPS_AUX_PIN_TASK.checkSetRangeError()）

```
DPS_AUX_TASK auxTask;

ON_FIRST_INVOCATION_BEGIN();

auxTask.pin("dps2").checkSetRangeError();

ON_FIRST_INVOCATION_END();

if ( auxTask.getRangeError("dps2") == TM::AUX_TASK_STATUS_PASS )
{
cout << "auxTask.getRangeError(\"dps2\") returned TM::AUX_TASK_STATUS_PASS" << endl;
}
else
{
cout << "auxTask.getRangeError(\"dps2\") returned TM::AUX_TASK_STATUS_FAIL" << endl;
}
```

### Syntax（取自子主题 DPS_AUX_PIN_TASK.checkSurgeTracker()）

```
DPS_AUX_PIN_TASK & checkSurgeTracker(TM::SURGE_TRACKER_CHECK check = TM::AGAINST_BOTH);
```

Parameters
[表]
列: Parameter | Description
行 1:
  check
  Selects the comparator to be checked.
[表] Available options of parameter: check
列: Parameter | Description
行 1:
  TM::AGAINST_BOTH
  Checks if any voltage or current surge goes beyond
    the high and low thresholds.
    This is the default state.
行 2:
  TM::AGAINST_HIGH
  Checks if any voltage or current surge goes beyond
    the high threshold.
行 3:
  TM::AGAINST_LOW
  Checks if any voltage or current surge goes beyond
    the low threshold.
Return value

A reference to the corresponding
`DPS_AUX_PIN_TASK`（raw: `141284.htm`）

object.

For retrieving the read result see
`DPS_AUX_TASK.getSurgeTrackerStatus()`（raw: `141291.htm`）
.

### Example（取自子主题 DPS_AUX_PIN_TASK.checkSurgeTracker()）

The example below sets current thresholds, activates the surge tracker, checks the
status against the current thresholds, and retrieves the result.

```
DPS_AUX_TASK auxTask;

ON_FIRST_INVOCATION_BEGIN();

//
// Set the current thresholds to -1 mA/1 mA and switch on surge tracker
//
auxTask.pin("dps1")
.selectISensorSetThresholds(-1 mA, 1 mA)
.setMode(TM::SURGE_TRACKER);

auxTask.execute();

auxTask.pin("dps1").checkSurgeTracker(TM::AGAINST_BOTH);

ON_FIRST_INVOCATION_END();

//
// Get the result of surge tracker
//
TM::SURGE_TRACKER_STATUS surgeTrackerStatus = auxTask.getSurgeTrackerStatus("dps1");

switch (surgeTrackerStatus)
{
case TM::SURGE_TRACKER_NONE_DETECTED:

cout << "DPS_AUX_TASK::getSurgeTrackerStatus for pin dps1: SURGE_TRACKER_NONE_DETECTED"
<< endl << endl;

break;

case TM::SURGE_TRACKER_HIGH_DETECTED:

cout << "DPS_AUX_TASK::getSurgeTrackerStatus for pin dps1: SURGE_TRACKER_HIGH_DETECTED"
<< endl << endl;

break;

case TM::SURGE_TRACKER_LOW_DETECTED:

cout << "DPS_AUX_TASK::getSurgeTrackerStatus for pin dps1: SURGE_TRACKER_LOW_DETECTED"
<< endl << endl;

break;

case TM::SURGE_TRACKER_BOTH_DETECTED:

cout << "DPS_AUX_TASK::getSurgeTrackerStatus for pin dps1: SURGE_TRACKER_BOTH_DETECTED"
<< endl << endl;

break;

default:

break;
};
```

### Syntax（取自子主题 DPS_AUX_PIN_TASK.selectISensorSetThresholds()）

```
DPS_AUX_PIN_TASK & selectISensorSetThresholds (const DOUBLE& low, const DOUBLE& high)
```

Parameters
[表]
列: Parameter | Description
行 1:
  low
  Low current threshold
行 2:
  high
  High current threshold
Return value
A reference to the corresponding
`DPS_AUX_PIN_TASK`（raw: `141284.htm`）
 object.

### Example（取自子主题 DPS_AUX_PIN_TASK.selectISensorSetThresholds()）

The example below shows the setting of the low and high current thresholds and the
activation of the surge tracker function.

```
DPS_AUX_TASK auxTask;

ON_FIRST_INVOCATION_BEGIN();

//
// Set the current thresholds to -1 mA/1 mA and switch on surge tracker
//
auxTask.pin("dps1")
.selectISensorSetThresholds(-1 mA, 1 mA)
.setMode(TM::SURGE_TRACKER);

auxTask.execute();

ON_FIRST_INVOCATION_END();
```

For an
extended example see
`DPS_AUX_TASK`（raw: `141283.htm`）
.

### Syntax（取自子主题 DPS_AUX_PIN_TASK.selectVSensorSetThresholds()）

```
DPS_AUX_PIN_TASK& selectVSensorSetThresholds (const DOUBLE& low, const DOUBLE& high);
```

Parameters
[表]
列: Parameter | Description
行 1:
  low
  Low voltage threshold
行 2:
  high
  High voltage threshold
Return value
A reference to the corresponding
`DPS_AUX_PIN_TASK`（raw: `141284.htm`）
 object.

### Example（取自子主题 DPS_AUX_PIN_TASK.selectVSensorSetThresholds()）

The example below shows the setting of the low and high voltage thresholds and
the activation of the surge tracker
function.

```
DPS_AUX_TASK auxTask;

ON_FIRST_INVOCATION_BEGIN();

// Set the voltage thresholds to -0.1 V/3.4 V and switch on surge tracker
auxTask.pin("dps1")
.selectVSensorSetThresholds(-0.1 V, 3.4 V)
.setMode(TM::SURGE_TRACKER);

auxTask.execute();

ON_FIRST_INVOCATION_END();
```

For
an extended example see
`DPS_AUX_TASK`（raw: `141283.htm`）
.

### Syntax（取自子主题 DPS_AUX_PIN_TASK.setMode()）

```
DPS_AUX_PIN_TASK & setMode(TM::SURGE_TRACKER_MODE mode);
```

Parameter
[表]
列: Parameter | Description
行 1:
  mode
  Selects the comparator mode.
[表] Available options of parameter: mode
列: Option | Description
行 1:
  TM::DPS_AUX_OFF
  Sets the comparator pair to off.
行 2:
  TM::SURGE_TRACKER
  Sets the surge tracker function to on. The latched
    status flag is reset.
行 3:
  TM::CMP_HIGH
  Used for match loops. Compares against the
    thresholds defined by `DPS_AUX_PIN_TASK.selectVSensorSetThresholds()`（raw: `141292.htm`） or
    `DPS_AUX_PIN_TASK.selectISensorSetThresholds()`（raw: `141293.htm`）.
行 4:
  TM::TO_TMU
  Sets the TMU (Time Measure Unit) function to
    on.
Return value
A reference to the corresponding
`DPS_AUX_PIN_TASK`（raw: `141284.htm`）
 object.

### Example（取自子主题 DPS_AUX_PIN_TASK.setMode()）

The example below shows the setting of the low and high current thresholds and the
activation of the surge tracker function.

```
DPS_AUX_TASK auxTask;

ON_FIRST_INVOCATION_BEGIN();

//
// Set the current thresholds to -1 mA/1 mA and switch on surge tracker
//
auxTask.pin("dps1")
.selectISensorSetThresholds(-1 mA, 1 mA)
.setMode(TM::SURGE_TRACKER);

auxTask.execute();

ON_FIRST_INVOCATION_END();
```

For an
extended example see
`DPS_AUX_TASK`（raw: `141283.htm`）
.

### Syntax（取自子主题 DPS_AUX_TASK.pin()）

```
DPS_AUX_PIN_TASK & pin(const STRING & pinlist);
```
[表] Parameter
列: Parameter | Description
行 1:
  pinlist
  Target pin name for which you want to define measurement conditions.
    
    You can specify multiple pins by separating pin entries with a comma.

### Return value（取自子主题 DPS_AUX_TASK.pin()）

A reference to the corresponding
`DPS_AUX_PIN_TASK`（raw: `141284.htm`）

object.

### Example（取自子主题 DPS_AUX_TASK.pin()）

In this example the pin
dps128pin
 is used to set the high and low
thresholds and to activate the surge
tracker.

```
DPS_AUX_TASK auxTask;

ON_FIRST_INVOCATION_BEGIN();

auxTask.pin(dps128pin)
.selectISensorSetThresholds(-1.0, 2.5)
.setMode("SURGE_TRACKER");

auxTask.execute();

ON_FIRST_INVOCATION_END();
```

For
an extended example see
`DPS_AUX_TASK`（raw: `141283.htm`）
.

### Syntax（取自子主题 PRLT? - (request Parallel ResuLTs)）

```
PRLT? ["exec_context",] {site}
```

returns:

```
PRLT {site}, {"result"}
```

### Parameters（取自子主题 PRLT? - (request Parallel ResuLTs)）

[表]
行 1:
  exec_context
  An execution context. For more information
    on execution contexts see `Using execution contexts`（raw: `135848.htm`）.
行 2:
  site
  The site parameter is
    
    number
    A single integer representing the site number.
    
    ALL
    Means that all the results of all configured sites are
    returned.
行 3:
  result
  The result parameter is a string containing one character for every
    site. The nth character stands for
    site n. Possible characters are:
    
    P
    If the last test passed on all pins.
    
    F
    If the last test failed at any pin.
    
    0
    If the site was masked during the last test.

### Example（取自子主题 PRLT? - (request Parallel ResuLTs)）

```
PRLT? ALL
```

returns:

```
PRLT ALL, "PF0"
```

In
this example, site 1 passed the last test, site 2 failed it, and site 3 was masked during the
test.

### Syntax（取自子主题 CSAS? - (Channel Slot Accumulated Status)）

```
CSAS? [msMode,] {mask}, {(pinlist)}
```

returns:

```
CSAS {status}, {(pinlist)}
```

### Parameters（取自子主题 CSAS? - (Channel Slot Accumulated Status)）

[表]
行 1:
  msMode
  The extra parameter controls how the return value is created.
    The value of the
    parameter can be PQFC:
    
    PQFC specified: The current query focus is respected and allows
    status query per site without affecting status bits of other sites.
    
    PQFC not specified: The command reads (and clears) status bits of
    all enabled and active sites at a glance, ignoring the actual query focus.
    
    The parameter applies only to use of parameter mask as integer
    value.
行 2:
  mask
  Integer bit mask or ALL.
    
    Integer bit mask: Integer value is used to mask out individual status bits. Each bit of mask is logically
    AND-ed with the corresponding bit of the DPS status. If one of the resulting bits is set, then
    F (Fail) is returned, otherwise P (Pass).
    
    It is used to check for an error condition. All bit positions of the status flags that should be checked,
    must be set to 1 in mask. If one of the selected status bits is set, then CSAS? returns
    F.
    
    ALL: Hex value (hexadecimal representation of all status bits) is returned.
    
    For setting the integer bit mask or interpreting a returned hex value, refer to the `status`（raw: `144688.htm#_144688__r_status`） parameter below.
行 3:
  pinlist
  Comma separated list of DPS128/64 or XPS256 pins. The @ character can be
    used to read the status for all DPS pins.
行 4:
  status
  If mask is ALL, you need to translate the hex
    value (hexadecimal representation of the status bits) to its binary form as
    follows:
    
      [子表]
      子行 1:
        Bit 0:
        High voltage or current
          of surge tracker exceeded
      子行 2:
        Bit 1:
        Low voltage or current
          of surge tracker exceeded
      子行 3:
        Bit 2:
        0
      子行 4:
        Bit 3:
        Measurement range change
          failed
      子行 5:
        Bit 4:
        Clamp current
          correction failed
      子行 6:
        Bit 5:
        Battery full
      子行 7:
        Bit 6:
        Power budget 1
      子行 8:
        Bit 7:
        Power budget 2
      子行 9:
        Bit 8:
        Power budget
          3
      子行 10:
        Bit 9:
        High voltage
          of surge tracker reached
      子行 11:
        Bit 10:
        Low voltage
          of surge tracker reached
      子行 12:
        Bit 11:
        High current of surge tracker
          reached
      子行 13:
        Bit 12:
        Low current of surge tracker reached
    
    If mask is specified as an integer bit-mask:
    
    Pass: P
    
    Fail: F

### Examples（取自子主题 CSAS? - (Channel Slot Accumulated Status)）

### Example 1:

```
CSAS? 3,(VCC)
```

returns either

```
CSAS P,(VCC)
```

or

```
CSAS F,(VCC)
```

The example uses the integer bitmask and checks whether a spike on the
VCC

pin exceeded the low or high limit.

P
 = Pass

No spike occurred since the last
CSAS?

query.

F
 = Fail

Either the low or high limit or both were exceeded.

### Example 2:

```
CSAS? ALL,(Vaux)
```

returns

```
CSAS #H10,(Vaux)
```

The example uses the
ALL
 specifier and checks for an error condition on the

Vaux
 pin.

Bit 3 = 0

No "
Measurement range change
failed
" error. All set
current measurement range requests were successful.

Bit 4 = 1

The "
Clamp current
correction failed
". A
high-accuracy clamp current correction for a
DCVH
 setup with execution mode

SER_HAC
 or
PAR_HAC
 was not successful.

### Syntax（取自子主题 PSAS? - (Power Supply Accumulated Status)）

```
PSAS? [msMode ,] {mask}, {(pinlist)}
```

returns

```
PSAS {status}, {(pinlist)}
```

[表] Parameters
行 1:
  msMode
  The extra parameter controls how the return value is
    created.
    The value of the parameter can be
    PQFC:
    
    PQFC specified: The current query focus
    is respected and allows status query per site without
    affecting status bits of other sites.
    
    PQFC not specified: The command reads
    (and clears) status bits of all enabled and active sites at
    a glance, ignoring the actual query focus.
    
    The parameter applies only to use of parameter
    mask as integer value.
行 2:
  mask
  Integer bit mask or ALL.
    
    Integer bit mask: Integer value is used to mask out individual status bits. Each bit of mask is logically
    AND-ed with the corresponding bit of the DPS status. If one of the resulting bits is set, then
    F (Fail) is returned, otherwise P (Pass).
    
    It is used to check for an error condition. All bit positions of the status flags that should be checked,
    must be set to 1 in mask. If one of the selected status bits is set, then PSAS? returns
    F.
    
    ALL: Hex value (hexadecimal representation of all status bits) is returned.
    
    For setting the integer bit mask or interpreting a returned hex value, refer to the `status`（raw: `98691.htm#_98691__r_status`） parameter below.
行 3:
  pinlist
  Comma separated list of DPS128/64 or XPS256
    pins. The @ character can be used to read the status for all DPS
    pins.
行 4:
  status
  If parameter mask is
    ALL, you need to translate the hex value
    (hexadecimal representation of the status bits) to its binary form
    as follows:
    
      [子表]
      子行 1:
        Bit 0 (LSB):
        Constant voltage [跨 2 列]
      子行 2:
        Bit 1:
        Constant current [跨 2 列]
      子行 3:
        Bit 2:
        Unregulated [跨 2 列]
      子行 4:
        Bit 3:
        Overvoltage [跨 2 列]
      子行 5:
        Bit 4:
        Overpower / Overcurrent / Power [跨 2 列]
          budget exceeded
      子行 6:
        Bit 5:
        Overtemperature [跨 2 列]
      子行 7:
        Bit 6:
        Voltage drop force [跨 2 列]
      子行 8:
        Bit 7:
        Voltage drop return [跨 2 列]
      子行 9:
        Bit 8:
        DUT board disconnect
        For the special mapping of bit [跨 2 行]
          9 and 8 on UHC4 and UHC4T, refer to table `DPS flag description`（raw: `98691.htm#_98691__s_DPS_flag_description`）
          below.
      子行 10:
        Bit 9:
        Safety line
      子行 11:
        Bit 10:
        Current limit [跨 2 列]
          disconnect
      子行 12:
        Bit 11:
        Low headroom [跨 2 列]
      子行 13:
        Bit 12:
        Current limiter protection [跨 2 列]
          detected
      子行 14:
        Bit 13:
        Range overflow [跨 2 列]
      子行 15:
        Bit 14 (MSB):
        Clamp distance too [跨 2 列]
          low
      子行 16:
        Bit 15:
        Voltage drop force [跨 2 列]
          warning
      子行 17:
        Bit 16:
        Voltage drop return [跨 2 列]
          warning
    
    If parameter mask is specified as an integer
    bit-mask:
    
    Pass: P
    
    Fail: F
    
    Refer to table `DPS flag implementation`（raw: `98691.htm#_98691__s_DPS_flag_implementation_710`） below for information regarding the
    card specific implementation of the bits or flags.

### Examples（取自子主题 PSAS? - (Power Supply Accumulated Status)）

### Description

For the following examples (1 to 4), the assumed binary value of the status of the
UHC4 pin Vcc is 10000110 (Voltage drop return, Unregulated, Constant Current).

### Example 1

To get all flags:

```
PSAS? ALL,(Vcc)
```

returns

```
PSAS #86,(Vcc)
```

### Example 2

To check if Unregulated (bit 2) is set:

```
PSAS? 4,(Vcc)
```

returns

```
PSAS F,(Vcc)
```

### Example 3

To check if Constant Current (bit 1) or Overpower (bit 4) is set:

```
PSAS? 18,(Vcc)
```

returns

```
PSAS F,(Vcc)
```

### Example 4

To check if Voltage Drop Force (bit 6) or DUT Board Disconnect (bit 8) is set:

```
PSAS? 320,(Vcc)
```

returns

```
PSAS P,(Vcc)
```

### Example 5

```
PSAS? ALL,(Vee)
```

returns

```
PSAS 2,(Vee)
```

This example for device pin Vee shows the DPS is working in constant current mode.

### Example 6

```
PSAS? ALL,(Vee)
```

returns

```
PSAS 64,(Vee)
```

This example for device pin Vee shows the DPS has hit the voltage drop force
threshold.

### Syntax（取自子主题 GET_FUNCTIONAL_RESULT()）

Note
GET_FUNCTIONAL_RESULT()
 should reside outside the

`ON_FIRST_INVOCATION block`（raw: `29526.htm`）
. Any action which restarts
the sequencers will erase the functional results.

Functions returning
Boolean
:

```
Boolean GET_FUNCTIONAL_RESULT(void);
Boolean GET_FUNCTIONAL_RESULT(const STRING& pin);
Boolean GET_FUNCTIONAL_RESULT(const STRING& pin, const STRING& context);
Boolean GET_FUNCTIONAL_RESULT(const STRING& port, const STRING& labelName, TM::FUNCIONAL_RESULT_TYPE type);
```

Note
 To retrieve the result of specified label and port, the
`TM::FUNCIONAL_RESULT_TYPE`（raw: `29400.htm#_29400__div_FUNCIONAL_RESULT_TYPE`）
 type must be set to

TM::FTST_BURST
.

Functions returning the result as
`FUNC_TEST_BURST_RESULT`（raw: `29400.htm#_29400__p_FUNC_TEST_BURST_RESULT`）
:

```
void GET_FUNCTIONAL_RESULT(const STRING& port,
std::vector<FUNC_TEST_BURST_RESULT>& ret, bool bReadPinFailCycles = false);

void GET_FUNCTIONAL_RESULT(const STRING_VECTOR& portlist,
const STRING& sequencer_execution_context,
std::vector<FUNC_TEST_BURST_RESULT>& ret, bool bReadPinFailCycles = false);

void GET_FUNCTIONAL_RESULT(const STRING& port,
const STRING& sequencer_execution_context,
std::vector<FUNC_TEST_BURST_RESULT>& ret, bool bReadPinFailCycles = false);
```

This API is defined in the header file

/opt/hp93000/soc/prod_com/include/MAPI/Execute.h
.

Parameters
[表]
列: Parameter | Description
行 1:
  pin
    port
  Defines the pin name of which the functional test
    result shall be retrieved.
    For multiport testing, a
    port name can be specified instead of a single
    pin.
    
    If this parameter is omitted (first
    syntax only), TRUE is returned
    only if all pins have passed, else
    FALSE is returned.
行 2:
  portlist
  List of string elements defining ports and set up as
    `STRING_VECTOR`（raw: `131095.htm`）.
    The
    portlist is to be used if the
    functional test results for more than one port shall
    be retrieved.
行 3:
  context
  The `execution context`（raw: `135848.htm`） of
    the last executed test for that context.
行 4:
  sequencer_execution_context
  The sequencer execution context, see `SEQUENCER_CONTEXT`（raw: `136815.htm`） and `SEQUENCER_CONTEXT_ITEM`（raw: `137373.htm`）.
行 5:
  labelName
  Specifies the label of which the functional test
    result will be retrieved.
行 6:
  type
  The value type FUNCIONAL_RESULT_TYPE defines the type of the
    functional result.
    Currently the type can only be
    TM::FTST_BURST for retrieving the burst result of the multiport
    test.
    
    ```
    namespace TM
    
    typedef enum
    {
    FTST_BURST
    
    }FUNCTIONAL_RESULT_TYPE;
    ```
行 7:
  ret
  The result of type
    FUNC_TEST_BURST_RESULT containing
    the executed label, the start cycle, the pass/fail
    result and the optional fail cycles map of the
    execution.
    ret is an already
    defined vector of type
    TM::FUNC_TEST_BURST_RESULT that
    is handled as
    reference.
    
    TM::FUNC_TEST_BURST_RESULT
    is defined as follows:
    
    ```
    typedef struct
    {
    STRING labelname;
    int id;
    int startCyc;
    int numberOfCycles;
    bool result;
    std::map<std::string, int> failCyclesMap;
    int isFailCyclesValid;
    
    } FUNC_TEST_BURST_RESULT;
    ```
    
      [子表]
      列: Return value | Description
      子行 1:
        labelname
        The name of the executed label.
      子行 2:
        id
        Index of the label within the burst.
          id is set to 0 for the first
          label.
      子行 3:
        startCyc
        The start cycle of the label within the
          burst.
      子行 4:
        numberOfCycles
        The number of cycles of the label.
      子行 5:
        result
        Returns a TRUE or
          FALSE.
          
          If multiple pins or a port has been passed all
          containing pins must pass to return a
          TRUE. If any of the pins fail a
          FALSE is returned.
      子行 6:
        failCyclesMap
        A map containing the name of failing pins
          as string and the number of
          fail cycles as int.
          The map
          is filled only if parameter `bReadPinFailCycles`（raw: `29400.htm#_29400__r_bReadPinFailCycles`） has been set to
          TRUE.
      子行 7:
        isFailCyclesValid
        The parameter shows the state of filling the
          failCyclesMap:
          
          -1: The pin fail cycles were not read. The
          function was called with parameter
          bReadPinFailCycles set to
          FALSE.
          
          0: The pin fail cycles were read but are not
          valid (`ERCC?`（raw: `98594.htm`）
          valid_code flag was
          OVFL or
          LESS).
          
          1: The pin fail cycles were read
          successfully.
行 8:
  bReadPinFailCycles
  The optional parameter initiates filling the
    failCyclesMap of parameter `ret`（raw: `29400.htm#_29400__r_ret`） if set to
    TRUE.
    The default value is
    FALSE.
    Note Use
    this parameter with caution. Filling the fail
    cycles map with data that must be read from the
    hardware may significantly increase the test
    time.
Return value
There are two types of functions for this API:

Boolean

The pass/fail result is returned as

Boolean
:

TRUE
 if the selected pin or all pins of
the selected ports have passed the functional test or

FALSE
 if any of the selected pins or any
pin of the selected ports has failed the functional
test.

void

These functions have no return value. The requested data is
returned by a parameter of type

FUNC_TEST_BURST_RESULT
 that is to be
defined in the calling function and transferred as reference.
For more information refer to parameter
`ret`（raw: `29400.htm#_29400__r_ret`）
 and
`Example 3`（raw: `29400.htm#_29400__Example_3`）
.

### Examples（取自子主题 GET_FUNCTIONAL_RESULT()）

### Example 1

In the following example the result of
PIN1
 will be retrieved and
stored in the
result
 variable after executing
`FUNCTIONAL_TEST()`（raw: `29356.htm`）
.

```
ON_FIRST_INVOCATION_BEGIN();

FUNCTIONAL_TEST();

ON_FIRST_INVOCATION_END();

Boolean result = GET_FUNCTIONAL_RESULT("PIN1");
```

### Example 2

This example retrieves the result of all pins involved in that PPMU measurement.

```
TASK_LIST Ppmu_task;

//
// Add the measurement settings to Ppmu_task;
//

ON_FIRST_INVOCATION_BEGIN();

Ppmu_task.execute();

ON_FIRST_INVOCATION_END();

Boolean result = GET_FUNCTIONAL_RESULT();
```

### Example 3

The following example returns the result of all executed patterns.

```
std::vector<FUNC_TEST_BURST_RESULT> mpResult;

ON_FIRST_INVOCATION_BEGIN();

FW_TASK("DCRM OVEM,LMAP,,(@@)");

FUNCTIONAL_TEST();

FW_TASK("DCRM OVEM,FCM,,(@@)");

ON_FIRST_INVOCATION_END();

GET_FUNCTIONAL_RESULT("dig12_dc1Port", mpResult);

for ( uint i = 0; i < mpResult.size(); i++ )
{
FUNC_TEST_BURST_RESULT funcTestRes = mpResult[i];

cout << "Result for label " << funcTestRes.labelname << ": "
<< (funcTestRes.result==true ? "true" : "false" ) << endl;
}
```

### Example 4

The following example illustrates how to retrieve a functional result of a test
executed using
`GET_FUNCTIONAL_RESULT()`（raw: `29400.htm`）
 on a special sequencer context.

```
STRING sContext = "global";

ON_FIRST_INVOCATION_BEGIN();

SEQUENCER_CONTEXT_ITEM context1(sContext);

context1.setPorts("port1");

SEQUENCER_CONTEXT context;

context.add(context1).apply();

CONNECT();

FW_TASK("DCRM OVEM,LMAP,,(@@)");

START_TEST(sContext);

int a, b;

WAIT_TEST_DONE(36000, &a, &b ,sContext);

FW_TASK("DCRM OVEM,FCM,,(@@)");

ON_FIRST_INVOCATION_END();

std::vector<FUNC_TEST_BURST_RESULT> result;

GET_FUNCTIONAL_RESULT("port1", sContext, result);

cout << endl << "*** Current Site number: " << CURRENT_SITE_NUMBER() << " ***" << endl;

for ( uint i = 0; i < result.size(); i++ )
{
FUNC_TEST_BURST_RESULT funcTestRes = result[i];

cout << "Result for label " << funcTestRes.labelname << ": "
<< (funcTestRes.result==true ? "TRUE" : "FALSE" ) << endl;

cout << "startCycle: " << funcTestRes.startCyc << endl << "numberOfCycles: "
<< funcTestRes.numberOfCycles << endl << "----------------------------------------------------" << endl;
}

DISCONNECT();
```

### Example 5: Reading the number of fail cycles per pin
The following
example shows how to read the number of fail cycles per pin.

Note
 Use parameter
bReadPinFailCycles
 with caution.
Filling the fail cycles map with data that must be read from the hardware may
significantly increase the test time.

```
ON_FIRST_INVOCATION_BEGIN();
{
...
...

FW_TASK("DCRM OVEM,LMAP,,(@@)");

FUNCTIONAL_TEST();
}
ON_FIRST_INVOCATION_END();

vector<FUNC_TEST_BURST_RESULT> mpResult;

GET_FUNCTIONAL_RESULT("Port_1", mpResult, true);

for (uint labelIndex = 0; labelIndex < mpResult.size(); labelIndex++)
{
FUNC_TEST_BURST_RESULT funcTestRes = mpResult[labelIndex];

cout << "Label " << funcTestRes.labelname << endl;
cout << endl;
cout << "\tResult:\t\t\t" << (funcTestRes.result==true ? "true" : "false" ) << endl;
cout << "\tisValidFailCycles:\t" << funcTestRes.isFailCyclesValid << endl;
cout << endl;
cout << "\tfailCyclesMap:" << endl;
cout << endl;

map<string, int>::iterator iterator;

for (iterator = funcTestRes.failCyclesMap.begin(); iterator != funcTestRes.failCyclesMap.end(); ++iterator)
{
cout << "\t\tFail cycles for pin " << iterator->first << " : " << iterator->second << endl;
}

cout << endl;
}
```

The
code above results in the following output if failing pins have been
found:

```
Label ...

Result: false
isValidFailCycles: 1

failCyclesMap:

Fail cycles for pin ... : ...
Fail cycles for pin ... : ...
...
```

### Syntax（取自子主题 DPS_AUX_TASK.execute()）

```
void execute();
```

List of parameters

There are no parameters.

Return value

There is no return value.

### Example（取自子主题 DPS_AUX_TASK.execute()）

The example below shows the surge tracker activation and execution.

The example below shows the setting of the low and high current thresholds and the
activation of the surge tracker function.

```
DPS_AUX_TASK auxTask;

ON_FIRST_INVOCATION_BEGIN();

//
// Set the current thresholds to -1 mA/1 mA and switch on surge tracker
//
auxTask.pin("dps1")
.selectISensorSetThresholds(-1 mA, 1 mA)
.setMode(TM::SURGE_TRACKER);

auxTask.execute();

ON_FIRST_INVOCATION_END();
```

For an extended example see

`DPS_AUX_TASK`（raw: `141283.htm`）
.

### Syntax（取自子主题 DPS_AUX_TASK.setup()）

```
void setup();
```

List of parameters

There are no parameters.

Return value

There is no return value.

### Example（取自子主题 DPS_AUX_TASK.setup()）

For an example see
`DPS_AUX_TASK`（raw: `141283.htm`）
.

### Syntax（取自子主题 DPS_AUX_TASK.getSurgeTrackerStatus()）

```
TM::SURGE_TRACKER_STATUS getSurgeTrackerStatus(const string& pinlist);
```

The second syntax is supported only for
`XPS256`（raw: `350661.htm`）
. For
this syntax, you must set both the
`voltage thresholds`（raw: `141292.htm`）
 and the
`current thresholds`（raw: `141293.htm`）
 to get valid
results:

```
virtual void getSurgeTrackerStatus(const STRING& pinlist,
TM::SURGE_TRACKER_STATUS& voltageSurgeTracker,
TM::SURGE_TRACKER_STATUS& currentSurgeTracker);
```

Parameter
s
[表]
列: Parameter | Description
行 1:
  pinlist
  List of pins for which the surge tracker status
    should be retrieved.
行 2:
  voltageSurgeTracker
  Voltage surge tracker status of type TM::SURGE_TRACKER_STATUS.
    
    Supported only for `XPS256`（raw: `350661.htm`）.
行 3:
  currentSurgeTracker
  Current surge tracker status of type TM::SURGE_TRACKER_STATUS.
    
    Supported only for `XPS256`（raw: `350661.htm`）.
Return value

The first syntax of the member function returns the status of the surge tracker as enum of
the type
TM::SURGE_TRACKER_STATUS
.

The second syntax of the member function has no return value.

Type
TM::SURGE_TRACKER_STATUS

The surge tracke status can be one of the following values:

TM::SURGE_TRACKER_NONE_DETECTED

TM::SURGE_TRACKER_HIGH_DETECTED

TM::SURGE_TRACKER_LOW_DETECTED

TM::SURGE_TRACKER_BOTH_DETECTED

### Examples（取自子主题 DPS_AUX_TASK.getSurgeTrackerStatus()）

### Example 1

The example below sets current thresholds, activates the surge tracker, checks the
status against the current thresholds, and retrieves the result.

```
DPS_AUX_TASK auxTask;

ON_FIRST_INVOCATION_BEGIN();

//
// Set the current thresholds to -1 mA/1 mA and switch on surge tracker
//
auxTask.pin("dps1")
.selectISensorSetThresholds(-1 mA, 1 mA)
.setMode(TM::SURGE_TRACKER);

auxTask.execute();

auxTask.pin("dps1").checkSurgeTracker(TM::AGAINST_BOTH);

ON_FIRST_INVOCATION_END();

//
// Get the result of surge tracker
//
TM::SURGE_TRACKER_STATUS surgeTrackerStatus = auxTask.getSurgeTrackerStatus("dps1");

switch (surgeTrackerStatus)
{
case TM::SURGE_TRACKER_NONE_DETECTED:

cout << "DPS_AUX_TASK::getSurgeTrackerStatus for pin dps1: SURGE_TRACKER_NONE_DETECTED"
<< endl << endl;

break;

case TM::SURGE_TRACKER_HIGH_DETECTED:

cout << "DPS_AUX_TASK::getSurgeTrackerStatus for pin dps1: SURGE_TRACKER_HIGH_DETECTED"
<< endl << endl;

break;

case TM::SURGE_TRACKER_LOW_DETECTED:

cout << "DPS_AUX_TASK::getSurgeTrackerStatus for pin dps1: SURGE_TRACKER_LOW_DETECTED"
<< endl << endl;

break;

case TM::SURGE_TRACKER_BOTH_DETECTED:

cout << "DPS_AUX_TASK::getSurgeTrackerStatus for pin dps1: SURGE_TRACKER_BOTH_DETECTED"
<< endl << endl;

break;

default:

break;
};
```

### Example 2: Surge tracker of XPS256

```
DPS_AUX_TASK auxTask;

ON_FIRST_INVOCATION_BEGIN();
{
auxTask.pin("XPS256")
.setMode (TM::SURGE_TRACKER)
.selectVSensorSetThresholds (-0.5 V, 3.5 V)
.selectISensorSetThresholds (-0.1 A, 0.4 A);

auxTask.execute();

auxTask.pin("XPS256").checkSurgeTracker(TM::AGAINST_BOTH);
}
ON_FIRST_INVOCATION_END();

TM::SURGE_TRACKER_STATUS statusVoltage, statusCurrent;

auxTask.getSurgeTrackerStatus("XPS256", statusVoltage, statusCurrent);

cout << "Voltage surge tracker: " << statusVoltage << endl;
cout << "Current surge tracker: " << statusCurrent << endl;
```

### Member functions（取自子主题 DPS power flags - get...() functions）

Several get...() member functions are documented
in this section. These member functions retrieve the value of all flags or of a
single flag from the test method cache. The
`DPS_AUX_PIN_TASK.checkPowerFlags()`（raw: `150021.htm`）
 member function
must be called upfront for reading the flags from the hardware into the test method
cache.

The member functions return one of the following values of the
enumerated type
DPS_POWER_FLAG_STATUS
:

[表]
列: Keyword | Value | State of the checked flags
行 1:
  TM::POWER_FLAG_STATUS_PASS
  0
  The checked single flag is not set or none of multiple checked
    flags is set.
行 2:
  TM::POWER_FLAG_STATUS_FAIL
  1
  The checked single flag is set or minimum one of multiple checked
    flags is set.

### Syntax（取自子主题 DPS_AUX_TASK.getAllStatus()）

```
TM::DPS_POWER_FLAG_STATUS getAllStatus(const STRING& pin);
```
[表] Parameter
列: Parameter | Description/Range
行 1:
  pin
  Single pin for which the status flags should be retrieved.

### Return value（取自子主题 DPS_AUX_TASK.getAllStatus()）

The member function returns one of the following
values of the enumerated type
DPS_POWER_FLAG_STATUS
:

[表]
列: Keyword | Value | State of the checked flags
行 1:
  TM::POWER_FLAG_STATUS_PASS
  0
  None of the checked flags is set.
行 2:
  TM::POWER_FLAG_STATUS_FAIL
  1
  Minimum one of the checked flags is set.

Note
 In offline mode, the "
Constant voltage
"
accumulated power supply status flag is always set and this member function returns
therefore
TM::POWER_FLAG_STATUS_FAIL
.

### Example（取自子主题 DPS_AUX_TASK.getAllStatus()）

The following example reads the actual state of all power flags, clears all
flags and evaluates the state of all flags. The returned value is

TM::POWER_FLAG_STATUS_FAIL
 if minimum one of the checked
flags is
set.

```
DPS_AUX_TASK dpsAuxTask_1;

ON_FIRST_INVOCATION_BEGIN();
{
//
// Read actual power flag status of two pins
//
dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read latched state & clear all flags
dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read actual state & clear all flags
}
ON_FIRST_INVOCATION_END();

//
// Evaluate the state of the first pin
//
if (dpsAuxTask_1.getAllStatus("dps1") == TM::POWER_FLAG_STATUS_PASS)
{
cout << "dpsAuxTask_1.getAllStatus(\"dps1\") returned TM::POWER_FLAG_STATUS_PASS" << endl;
}
else
{
cout << "dpsAuxTask_1.getAllStatus(\"dps1\") returned TM::POWER_FLAG_STATUS_FAIL" << endl;
}
```

### Syntax（取自子主题 DPS_AUX_TASK.getStatusWithoutConstCur()）

```
TM::DPS_POWER_FLAG_STATUS getStatusWithoutConstCur(const STRING& pin);
```

[表] Parameter
列: Parameter | Description/Range
行 1:
  pin
  Single pin for which the status flags should be
    retrieved.

### Return value（取自子主题 DPS_AUX_TASK.getStatusWithoutConstCur()）

The member function returns one of the following
values of the enumerated type
DPS_POWER_FLAG_STATUS
:

[表]
列: Keyword | Value | State of the checked flags
行 1:
  TM::POWER_FLAG_STATUS_PASS
  0
  None of the checked flags is set.
行 2:
  TM::POWER_FLAG_STATUS_FAIL
  1
  Minimum one of the checked flags is set.

Note
 In offline mode, the "
Constant voltage
"
accumulated power supply status flag is always set and this member function returns
therefore
TM::POWER_FLAG_STATUS_FAIL
.

### Example（取自子主题 DPS_AUX_TASK.getStatusWithoutConstCur()）

The following example reads the actual state of all power flags, clears all flags and evaluates
the state of the read flags except the "
Constant current
" flag. The returned value is

TM::POWER_FLAG_STATUS_FAIL
 if minimum one of the checked
flags is set.

```
DPS_AUX_TASK dpsAuxTask_1;

ON_FIRST_INVOCATION_BEGIN();
{
//
// Read actual power flag status of two pins
//
dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read latched state & clear all flags
dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read actual state & clear all flags
}
ON_FIRST_INVOCATION_END();

//
// Evaluate the state of the first pin
//
if (dpsAuxTask_1.getStatusWithoutConstCur("dps1") == TM::POWER_FLAG_STATUS_PASS)
{
cout << "dpsAuxTask_1.getStatusWithoutConstCur(\"dps1\") returned TM::POWER_FLAG_STATUS_PASS" << endl;
}
else
{
cout << "dpsAuxTask_1.getStatusWithoutConstCur(\"dps1\") returned TM::POWER_FLAG_STATUS_FAIL" << endl;
}
```

### Syntax（取自子主题 DPS_AUX_TASK.getStatusWithoutConstVol()）

```
TM::DPS_POWER_FLAG_STATUS getStatusWithoutConstVol(const STRING& pin);
```

[表] Parameter
列: Parameter | Description/Range
行 1:
  pin
  Single pin for which the status flags should be
    retrieved.

### Return value（取自子主题 DPS_AUX_TASK.getStatusWithoutConstVol()）

The member function returns one of the following
values of the enumerated type
DPS_POWER_FLAG_STATUS
:

[表]
列: Keyword | Value | State of the checked flags
行 1:
  TM::POWER_FLAG_STATUS_PASS
  0
  None of the checked flags is set.
行 2:
  TM::POWER_FLAG_STATUS_FAIL
  1
  Minimum one of the checked flags is set.

Return value in offline mode is
TM::POWER_FLAG_STATUS_PASS
.

### Example（取自子主题 DPS_AUX_TASK.getStatusWithoutConstVol()）

The following example reads the actual state of all power flags, clears all flags and evaluates
the state of the read flags except the "
Constant voltage
" flag. The returned value is

TM::POWER_FLAG_STATUS_FAIL
 if minimum one of the checked
flags is set.

```
DPS_AUX_TASK dpsAuxTask_1;

ON_FIRST_INVOCATION_BEGIN();
{
//
// Read actual power flag status of two pins
//
dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read latched state & clear all flags
dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read actual state & clear all flags
}
ON_FIRST_INVOCATION_END();

//
// Evaluate the state of the first pin
//
if (dpsAuxTask_1.getStatusWithoutConstVol("dps1") == TM::POWER_FLAG_STATUS_PASS)
{
cout << "dpsAuxTask_1.getStatusWithoutConstVol(\"dps1\") returned TM::POWER_FLAG_STATUS_PASS" << endl;
}
else
{
cout << "dpsAuxTask_1.getStatusWithoutConstVol(\"dps1\") returned TM::POWER_FLAG_STATUS_FAIL" << endl;
}
```

### Syntax（取自子主题 DPS_AUX_TASK.getClampDistanceTooLow()）

```
TM::DPS_POWER_FLAG_STATUS getClampDistanceTooLow(const STRING& pin);
```

[表] Parameter
列: Parameter | Description/Range
行 1:
  pin
  Single pin for which the status flags should be
    retrieved.

### Return value（取自子主题 DPS_AUX_TASK.getClampDistanceTooLow()）

The member function returns one of the following
values of the enumerated type
DPS_POWER_FLAG_STATUS
:

[表]
列: Keyword | Value | State of the checked flags
行 1:
  TM::POWER_FLAG_STATUS_PASS
  0
  The checked flag is not set.
行 2:
  TM::POWER_FLAG_STATUS_FAIL
  1
  The checked flag is set.

Return value in offline mode is
TM::POWER_FLAG_STATUS_PASS
.

### Example（取自子主题 DPS_AUX_TASK.getClampDistanceTooLow()）

The following example reads the actual state of all power flags, clears all flags and evaluates
the state of the "
Clamp distance too
low
" flag. The
returned value is
TM::POWER_FLAG_STATUS_FAIL
 if the checked flag
is set.

```
DPS_AUX_TASK dpsAuxTask_1;

ON_FIRST_INVOCATION_BEGIN();
{
//
// Read actual power flag status of two pins
//
dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read latched state & clear all flags
dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read actual state & clear all flags
}
ON_FIRST_INVOCATION_END();

//
// Evaluate the state of the first pin
//
if (dpsAuxTask_1.getClampDistanceTooLow("dps1") == TM::POWER_FLAG_STATUS_PASS)
{
cout << "dpsAuxTask_1.getClampDistanceTooLow(\"dps1\") returned TM::POWER_FLAG_STATUS_PASS" << endl;
}
else
{
cout << "dpsAuxTask_1.getClampDistanceTooLow(\"dps1\") returned TM::POWER_FLAG_STATUS_FAIL" << endl;
}
```

### Syntax（取自子主题 DPS_AUX_TASK.getConstantCurrent()）

```
TM::DPS_POWER_FLAG_STATUS getConstantCurrent(const STRING& pin);
```

[表] Parameter
列: Parameter | Description/Range
行 1:
  pin
  Single pin for which the status flags should be
    retrieved.

### Return value（取自子主题 DPS_AUX_TASK.getConstantCurrent()）

The member function returns one of the following
values of the enumerated type
DPS_POWER_FLAG_STATUS
:

[表]
列: Keyword | Value | State of the checked flags
行 1:
  TM::POWER_FLAG_STATUS_PASS
  0
  The checked flag is not set.
行 2:
  TM::POWER_FLAG_STATUS_FAIL
  1
  The checked flag is set.

Return value in offline mode is
TM::POWER_FLAG_STATUS_PASS
.

### Example（取自子主题 DPS_AUX_TASK.getConstantCurrent()）

The following example reads the actual state of all power flags, clears all flags and evaluates
the state of the "
Constant current
" flag. The
returned value is
TM::POWER_FLAG_STATUS_FAIL
 if the checked flag
is set.

```
DPS_AUX_TASK dpsAuxTask_1;

ON_FIRST_INVOCATION_BEGIN();
{
//
// Read actual power flag status of two pins
//
dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read latched state & clear all flags
dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read actual state & clear all flags
}
ON_FIRST_INVOCATION_END();

//
// Evaluate the state of the first pin
//
if (dpsAuxTask_1.getConstantCurrent("dps1") == TM::POWER_FLAG_STATUS_PASS)
{
cout << "dpsAuxTask_1.getConstantCurrent(\"dps1\") returned TM::POWER_FLAG_STATUS_PASS" << endl;
}
else
{
cout << "dpsAuxTask_1.getConstantCurrent(\"dps1\") returned TM::POWER_FLAG_STATUS_FAIL" << endl;
}
```

### Syntax（取自子主题 DPS_AUX_TASK.getConstantCurrentLimitDisconnect()）

```
TM::DPS_POWER_FLAG_STATUS getConstantCurrentLimitDisconnect(const STRING& pin);
```

[表] Parameter
列: Parameter | Description/Range
行 1:
  pin
  Single pin for which the status flags should be
    retrieved.

### Return value（取自子主题 DPS_AUX_TASK.getConstantCurrentLimitDisconnect()）

The member function returns one of the following values of the enumerated type

DPS_POWER_FLAG_STATUS
:

[表]
列: Keyword | Value | State of the checked flags
行 1:
  TM::POWER_FLAG_STATUS_PASS
  0
  The checked flag is not set.
行 2:
  TM::POWER_FLAG_STATUS_FAIL
  1
  The checked flag is set.

Return value in offline mode is
TM::POWER_FLAG_STATUS_PASS
.

### Example（取自子主题 DPS_AUX_TASK.getConstantCurrentLimitDisconnect()）

The following example reads the actual state of all power flags, clears all flags and
evaluates the state of the
Current limit
disconnect
" flag. The returned
value is
TM::POWER_FLAG_STATUS_FAIL
 if the checked flag is
set.

```
DPS_AUX_TASK dpsAuxTask_1;

ON_FIRST_INVOCATION_BEGIN();
{
//
// Read actual power flag status of two pins
//
dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read latched state & clear all flags
dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read actual state & clear all flags
}
ON_FIRST_INVOCATION_END();

//
// Evaluate the state of the first pin
//
if (dpsAuxTask_1.getConstantCurrentLimitDisconnect("dps1") == TM::POWER_FLAG_STATUS_PASS)
{
cout << "dpsAuxTask_1.getConstantCurrentLimitDisconnect(\"dps1\") returned TM::POWER_FLAG_STATUS_PASS" << endl;
}
else
{
cout << "dpsAuxTask_1.getConstantCurrentLimitDisconnect(\"dps1\") returned TM::POWER_FLAG_STATUS_FAIL" << endl;
}
```

### Syntax（取自子主题 DPS_AUX_TASK.getConstantVoltage()）

```
TM::DPS_POWER_FLAG_STATUS getConstantVoltage(const STRING& pin);
```

[表] Parameter
列: Parameter | Description/Range
行 1:
  pin
  Single pin for which the status flags should be
    retrieved.

### Return value（取自子主题 DPS_AUX_TASK.getConstantVoltage()）

The member function returns one of the following values of the enumerated type

DPS_POWER_FLAG_STATUS
:

[表]
列: Keyword | Value | State of the checked flags
行 1:
  TM::POWER_FLAG_STATUS_PASS
  0
  The checked flag is not set.
行 2:
  TM::POWER_FLAG_STATUS_FAIL
  1
  The checked flag is set.

Note
 In offline mode, the "
Constant voltage
"
accumulated power supply status flag is always set and this member function returns
therefore
TM::POWER_FLAG_STATUS_FAIL
.

### Example（取自子主题 DPS_AUX_TASK.getConstantVoltage()）

The following example reads the actual state of all power flags, clears all flags and
evaluates the state of the "
Constant voltage
"
flag. The returned value is
TM::POWER_FLAG_STATUS_FAIL
 if the
checked flag is set.

```
DPS_AUX_TASK dpsAuxTask_1;

ON_FIRST_INVOCATION_BEGIN();
{
//
// Read actual power flag status of two pins
//
dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read latched state & clear all flags
dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read actual state & clear all flags
}
ON_FIRST_INVOCATION_END();

//
// Evaluate the state of the first pin
//
if (dpsAuxTask_1.getConstantVoltage("dps1") == TM::POWER_FLAG_STATUS_PASS)
{
cout << "dpsAuxTask_1.getConstantVoltage(\"dps1\") returned TM::POWER_FLAG_STATUS_PASS" << endl;
}
else
{
cout << "dpsAuxTask_1.getConstantVoltage(\"dps1\") returned TM::POWER_FLAG_STATUS_FAIL" << endl;
}
```

### Syntax（取自子主题 DPS_AUX_TASK.getCurrentLimiterProtectionDetected()）

```
TM::DPS_POWER_FLAG_STATUS getCurrentLimiterProtectionDetected(const STRING& pin);
```

[表] Parameter
列: Parameter | Description/Range
行 1:
  pin
  Single pin for which the status flags should be
    retrieved.

### Return value（取自子主题 DPS_AUX_TASK.getCurrentLimiterProtectionDetected()）

The member function returns one of the following
values of the enumerated type
DPS_POWER_FLAG_STATUS
:

[表]
列: Keyword | Value | State of the checked flags
行 1:
  TM::POWER_FLAG_STATUS_PASS
  0
  The checked flag is not set.
行 2:
  TM::POWER_FLAG_STATUS_FAIL
  1
  The checked flag is set.

Return value in offline mode is
TM::POWER_FLAG_STATUS_PASS
.

### Example（取自子主题 DPS_AUX_TASK.getCurrentLimiterProtectionDetected()）

The following example reads the actual state of all power flags, clears all flags and evaluates
the state of the "
Current limiter protection
detected
" flag. The
returned value is
TM::POWER_FLAG_STATUS_FAIL
 if the checked flag
is set.

```
DPS_AUX_TASK dpsAuxTask_1;

ON_FIRST_INVOCATION_BEGIN();
{
//
// Read actual power flag status of two pins
//
dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read latched state & clear all flags
dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read actual state & clear all flags
}
ON_FIRST_INVOCATION_END();

//
// Evaluate the state of the first pin
//
if (dpsAuxTask_1.getCurrentLimiterProtectionDetected("dps1") == TM::POWER_FLAG_STATUS_PASS)
{
cout << "dpsAuxTask_1.getCurrentLimiterProtectionDetected(\"dps1\") returned TM::POWER_FLAG_STATUS_PASS" << endl;
}
else
{
cout << "dpsAuxTask_1.getCurrentLimiterProtectionDetected(\"dps1\") returned TM::POWER_FLAG_STATUS_FAIL" << endl;
}
```

### Syntax（取自子主题 DPS_AUX_TASK.getDutBoardDisconnect()）

```
TM::DPS_POWER_FLAG_STATUS getDutBoardDisconnect(const STRING& pin);
```

[表] Parameter
列: Parameter | Description/Range
行 1:
  pin
  Single pin for which the status flags should be
    retrieved.

### Return value（取自子主题 DPS_AUX_TASK.getDutBoardDisconnect()）

The member function returns one of the following
values of the enumerated type
DPS_POWER_FLAG_STATUS
:

[表]
列: Keyword | Value | State of the checked flag
行 1:
  TM::POWER_FLAG_STATUS_PASS
  0
  The checked flag is not set.
行 2:
  TM::POWER_FLAG_STATUS_FAIL
  1
  The checked flag is set.

Return value in offline mode is
TM::POWER_FLAG_STATUS_PASS
.

### Example（取自子主题 DPS_AUX_TASK.getDutBoardDisconnect()）

The following example reads the actual state of all power flags, clears all flags and evaluates
the state of the "
DUT board disconnect
" flag. The
returned value is
TM::POWER_FLAG_STATUS_FAIL
 if the checked flag
is set.

```
DPS_AUX_TASK dpsAuxTask_1;

ON_FIRST_INVOCATION_BEGIN();
{
//
// Read actual power flag status of two pins
//
dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read latched state & clear all flags
dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read actual state & clear all flags
}
ON_FIRST_INVOCATION_END();

//
// Evaluate the state of the first pin
//
if (dpsAuxTask_1.getDutBoardDisconnect("dps1") == TM::POWER_FLAG_STATUS_PASS)
{
cout << "dpsAuxTask_1.getDutBoardDisconnect(\"dps1\") returned TM::POWER_FLAG_STATUS_PASS" << endl;
}
else
{
cout << "dpsAuxTask_1.getDutBoardDisconnect(\"dps1\") returned TM::POWER_FLAG_STATUS_FAIL" << endl;
}
```

### Syntax（取自子主题 DPS_AUX_TASK.getLowHeadroom()）

```
TM::DPS_POWER_FLAG_STATUS getLowHeadroom(const STRING& pin);
```

[表] Parameter
列: Parameter | Description/Range
行 1:
  pin
  Single pin for which the status flags should be
    retrieved.

### Return value（取自子主题 DPS_AUX_TASK.getLowHeadroom()）

The member function returns one of the following
values of the enumerated type
DPS_POWER_FLAG_STATUS
:

[表]
列: Keyword | Value | State of the checked flags
行 1:
  TM::POWER_FLAG_STATUS_PASS
  0
  The checked flag is not set.
行 2:
  TM::POWER_FLAG_STATUS_FAIL
  1
  The checked flag is set.

Return value in offline mode is
TM::POWER_FLAG_STATUS_PASS
.

### Example（取自子主题 DPS_AUX_TASK.getLowHeadroom()）

The following example reads the actual state of all power flags, clears all flags and evaluates
the state of the "
Low headroom
" flag. The
returned value is
TM::POWER_FLAG_STATUS_FAIL
 if the checked flag
is set.

```
DPS_AUX_TASK dpsAuxTask_1;

ON_FIRST_INVOCATION_BEGIN();
{
//
// Read actual power flag status of two pins
//
dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read latched state & clear all flags
dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read actual state & clear all flags
}
ON_FIRST_INVOCATION_END();

//
// Evaluate the state of the first pin
//
if (dpsAuxTask_1.getLowHeadroom("dps1") == TM::POWER_FLAG_STATUS_PASS)
{
cout << "dpsAuxTask_1.getLowHeadroom(\"dps1\") returned TM::POWER_FLAG_STATUS_PASS" << endl;
}
else
{
cout << "dpsAuxTask_1.getLowHeadroom(\"dps1\") returned TM::POWER_FLAG_STATUS_FAIL" << endl;
}
```

### Syntax（取自子主题 DPS_AUX_TASK.getOvercurrent()）

```
TM::DPS_POWER_FLAG_STATUS getOvercurrent(const STRING& pin);
```

[表] Parameter
列: Parameter | Description/Range
行 1:
  pin
  Single pin for which the status flags should be
    retrieved.

### Return value（取自子主题 DPS_AUX_TASK.getOvercurrent()）

The member function returns one of the following
values of the enumerated type
DPS_POWER_FLAG_STATUS
:

[表]
列: Keyword | Value | State of the checked flags
行 1:
  TM::POWER_FLAG_STATUS_PASS
  0
  The checked flag is not set.
行 2:
  TM::POWER_FLAG_STATUS_FAIL
  1
  The checked flag is set.

Return value in offline mode is
TM::POWER_FLAG_STATUS_PASS
.

### Example（取自子主题 DPS_AUX_TASK.getOvercurrent()）

The following example reads the actual state of all power flags, clears all flags and evaluates
the state of the "
Overpower / Overcurrent / Power
budget exceeded
" flag. The
returned value is
TM::POWER_FLAG_STATUS_FAIL
 if the checked flag
is set.

```
DPS_AUX_TASK dpsAuxTask_1;

ON_FIRST_INVOCATION_BEGIN();
{
//
// Read actual power flag status of two pins
//
dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read latched state & clear all flags
dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read actual state & clear all flags
}
ON_FIRST_INVOCATION_END();

//
// Evaluate the state of the first pin
//
if (dpsAuxTask_1.getOvercurrent("dps1") == TM::POWER_FLAG_STATUS_PASS)
{
cout << "dpsAuxTask_1.getOvercurrent(\"dps1\") returned TM::POWER_FLAG_STATUS_PASS" << endl;
}
else
{
cout << "dpsAuxTask_1.getOvercurrent(\"dps1\") returned TM::POWER_FLAG_STATUS_FAIL" << endl;
}
```

### Syntax（取自子主题 DPS_AUX_TASK.getOvertemperature()）

```
TM::DPS_POWER_FLAG_STATUS getOvertemperature(const STRING& pin);
```

[表] Parameter
列: Parameter | Description/Range
行 1:
  pin
  Single pin for which the status flags should be
    retrieved.

### Return value（取自子主题 DPS_AUX_TASK.getOvertemperature()）

The member function returns one of the following
values of the enumerated type
DPS_POWER_FLAG_STATUS
:

[表]
列: Keyword | Value | State of the checked flags
行 1:
  TM::POWER_FLAG_STATUS_PASS
  0
  The checked flag is not set.
行 2:
  TM::POWER_FLAG_STATUS_FAIL
  1
  The checked flag is set.

Return value in offline mode is
TM::POWER_FLAG_STATUS_PASS
.

### Example（取自子主题 DPS_AUX_TASK.getOvertemperature()）

The following example reads the actual state of all power flags, clears all flags and evaluates
the state of the "
Overtemperature
" flag. The
returned value is
TM::POWER_FLAG_STATUS_FAIL
 if the checked flag
is set.

```
DPS_AUX_TASK dpsAuxTask_1;

ON_FIRST_INVOCATION_BEGIN();
{
//
// Read actual power flag status of two pins
//
dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read latched state & clear all flags
dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read actual state & clear all flags
}
ON_FIRST_INVOCATION_END();

//
// Evaluate the state of the first pin
//
if (dpsAuxTask_1.getOvertemperature("dps1") == TM::POWER_FLAG_STATUS_PASS)
{
cout << "dpsAuxTask_1.getOvertemperature(\"dps1\") returned TM::POWER_FLAG_STATUS_PASS" << endl;
}
else
{
cout << "dpsAuxTask_1.getOvertemperature(\"dps1\") returned TM::POWER_FLAG_STATUS_FAIL" << endl;
}
```

### Syntax（取自子主题 DPS_AUX_TASK.getOvervoltage()）

```
TM::DPS_POWER_FLAG_STATUS getOvervoltage(const STRING& pin);
```

[表] Parameter
列: Parameter | Description/Range
行 1:
  pin
  Single pin for which the status flags should be
    retrieved.

### Return value（取自子主题 DPS_AUX_TASK.getOvervoltage()）

The member function returns one of the following values of
the enumerated type
DPS_POWER_FLAG_STATUS
:

[表]
列: Keyword | Value | State of the checked flags
行 1:
  TM::POWER_FLAG_STATUS_PASS
  0
  The checked flag is not set.
行 2:
  TM::POWER_FLAG_STATUS_FAIL
  1
  The checked flag is set.

Return value in offline mode is
TM::POWER_FLAG_STATUS_PASS
.

### Example（取自子主题 DPS_AUX_TASK.getOvervoltage()）

The following example reads the actual state of all power flags, clears all flags and evaluates
the state of the "
Overvoltage
" flag. The
returned value is
TM::POWER_FLAG_STATUS_FAIL
 if the checked flag
is set.

```
DPS_AUX_TASK dpsAuxTask_1;

ON_FIRST_INVOCATION_BEGIN();
{
//
// Read actual power flag status of two pins
//
dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read latched state & clear all flags
dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read actual state & clear all flags
}
ON_FIRST_INVOCATION_END();

//
// Evaluate the state of the 1st pin
//
if (dpsAuxTask_1.getOvervoltage("dps1") == TM::POWER_FLAG_STATUS_PASS)
{
cout << "dpsAuxTask_1.getOvervoltage(\"dps1\") returned TM::POWER_FLAG_STATUS_PASS" << endl;
}
else
{
cout << "dpsAuxTask_1.getOvervoltage(\"dps1\") returned TM::POWER_FLAG_STATUS_FAIL" << endl;
}
```

### Syntax（取自子主题 DPS_AUX_TASK.getRangeOverflow()）

```
TM::DPS_POWER_FLAG_STATUS getRangeOverflow(const STRING& pin);
```

[表] Parameter
列: Parameter | Description/Range
行 1:
  pin
  Single pin for which the status flags should be
    retrieved.

### Return value（取自子主题 DPS_AUX_TASK.getRangeOverflow()）

The member function returns one of the following
values of the enumerated type
DPS_POWER_FLAG_STATUS
:

[表]
列: Keyword | Value | State of the checked flags
行 1:
  TM::POWER_FLAG_STATUS_PASS
  0
  The checked flag is not set.
行 2:
  TM::POWER_FLAG_STATUS_FAIL
  1
  The checked flag is set.

Return value in offline mode is
TM::POWER_FLAG_STATUS_PASS
.

### Example（取自子主题 DPS_AUX_TASK.getRangeOverflow()）

The following example reads the actual state of all power flags, clears all flags and evaluates
the state of the "
Range overflow
" flag. The
returned value is
TM::POWER_FLAG_STATUS_FAIL
 if the checked flag
is set.

```
DPS_AUX_TASK dpsAuxTask_1;

ON_FIRST_INVOCATION_BEGIN();
{
//
// Read actual power flag status of two pins
//
dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read latched state & clear all flags
dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read actual state & clear all flags
}
ON_FIRST_INVOCATION_END();

//
// Evaluate the state of the first pin
//
if (dpsAuxTask_1.getRangeOverflow("dps1") == TM::POWER_FLAG_STATUS_PASS)
{
cout << "dpsAuxTask_1.getRangeOverflow(\"dps1\") returned TM::POWER_FLAG_STATUS_PASS" << endl;
}
else
{
cout << "dpsAuxTask_1.getRangeOverflow(\"dps1\") returned TM::POWER_FLAG_STATUS_FAIL" << endl;
}
```

### Syntax（取自子主题 DPS_AUX_TASK.getSafetyLine()）

```
TM::DPS_POWER_FLAG_STATUS getSafetyLine(const STRING& pin);
```

[表] Parameter
列: Parameter | Description/Range
行 1:
  pin
  Single pin for which the status flags should be
    retrieved.

### Return value（取自子主题 DPS_AUX_TASK.getSafetyLine()）

The member function returns one of the following
values of the enumerated type
DPS_POWER_FLAG_STATUS
:

[表]
列: Keyword | Value | State of the checked flags
行 1:
  TM::POWER_FLAG_STATUS_PASS
  0
  The checked flag is not set.
行 2:
  TM::POWER_FLAG_STATUS_FAIL
  1
  The checked flag is set.

Return value in offline mode is
TM::POWER_FLAG_STATUS_PASS
.

### Example（取自子主题 DPS_AUX_TASK.getSafetyLine()）

The following example reads the actual state of all power flags, clears all flags and evaluates
the state of the "
Safety line
" flag. The
returned value is
TM::POWER_FLAG_STATUS_FAIL
 if the checked flag
is set.

```
DPS_AUX_TASK dpsAuxTask_1;

ON_FIRST_INVOCATION_BEGIN();
{
//
// Read actual power flag status of two pins
//
dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read latched state & clear all flags
dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read actual state & clear all flags
}
ON_FIRST_INVOCATION_END();

//
// Evaluate the state of the first pin
//
if (dpsAuxTask_1.getSafetyLine("dps1") == TM::POWER_FLAG_STATUS_PASS)
{
cout << "dpsAuxTask_1.getSafetyLine(\"dps1\") returned TM::POWER_FLAG_STATUS_PASS" << endl;
}
else
{
cout << "dpsAuxTask_1.getSafetyLine(\"dps1\") returned TM::POWER_FLAG_STATUS_FAIL" << endl;
}
```

### Syntax（取自子主题 DPS_AUX_TASK.getUnregulated()）

```
TM::DPS_POWER_FLAG_STATUS getUnregulated(const STRING& pin);
```

[表] Parameter
列: Parameter | Description/Range
行 1:
  pin
  Single pin for which the status flags should be
    retrieved.

### Return value（取自子主题 DPS_AUX_TASK.getUnregulated()）

The member function returns one of the following
values of the enumerated type
DPS_POWER_FLAG_STATUS
:

[表]
列: Keyword | Value | State of the checked flags
行 1:
  TM::POWER_FLAG_STATUS_PASS
  0
  The checked flag is not set.
行 2:
  TM::POWER_FLAG_STATUS_FAIL
  1
  The checked flag is set.

Return value in offline mode is
TM::POWER_FLAG_STATUS_PASS
.

### Example（取自子主题 DPS_AUX_TASK.getUnregulated()）

The following example reads the actual state of all power flags, clears all flags and evaluates
the state of the "
Unregulated
" flag. The
returned value is
TM::POWER_FLAG_STATUS_FAIL
 if the checked flag
is set.

```
DPS_AUX_TASK dpsAuxTask_1;

ON_FIRST_INVOCATION_BEGIN();
{
//
// Read actual power flag status of two pins
//
dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read latched state & clear all flags
dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read actual state & clear all flags
}
ON_FIRST_INVOCATION_END();

//
// Evaluate the state of the first pin
//
if (dpsAuxTask_1.getUnregulated("dps1") == TM::POWER_FLAG_STATUS_PASS)
{
cout << "dpsAuxTask_1.getUnregulated(\"dps1\") returned TM::POWER_FLAG_STATUS_PASS" << endl;
}
else
{
cout << "dpsAuxTask_1.getUnregulated(\"dps1\") returned TM::POWER_FLAG_STATUS_FAIL" << endl;
}
```

### Syntax（取自子主题 DPS_AUX_TASK.getVoltageDropForce()）

```
TM::DPS_POWER_FLAG_STATUS getVoltageDropForce(const STRING& pin);
```

[表] Parameter
列: Parameter | Description/Range
行 1:
  pin
  Single pin for which the status flags should be
    retrieved.

### Return value（取自子主题 DPS_AUX_TASK.getVoltageDropForce()）

The member function returns one of the following
values of the enumerated type
DPS_POWER_FLAG_STATUS
:

[表]
列: Keyword | Value | State of the checked flags
行 1:
  TM::POWER_FLAG_STATUS_PASS
  0
  The checked flag is not set.
行 2:
  TM::POWER_FLAG_STATUS_FAIL
  1
  The checked flag is set.

Return value in offline mode is
TM::POWER_FLAG_STATUS_PASS
.

### Example（取自子主题 DPS_AUX_TASK.getVoltageDropForce()）

The following example reads the actual state of all power flags, clears all flags and evaluates
the state of the "
Voltage drop force
" flag.
The returned value is
TM::POWER_FLAG_STATUS_FAIL
 if the checked
flag is set.

```
DPS_AUX_TASK dpsAuxTask_1;

ON_FIRST_INVOCATION_BEGIN();
{
//
// Read actual power flag status of two pins
//
dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read latched state & clear all flags
dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read actual state & clear all flags
}
ON_FIRST_INVOCATION_END();

//
// Evaluate the state of the first pin
//
if (dpsAuxTask_1.getVoltageDropForce("dps1") == TM::POWER_FLAG_STATUS_PASS)
{
cout << "dpsAuxTask_1.getVoltageDropForce(\"dps1\") returned TM::POWER_FLAG_STATUS_PASS" << endl;
}
else
{
cout << "dpsAuxTask_1.getVoltageDropForce(\"dps1\") returned TM::POWER_FLAG_STATUS_FAIL" << endl;
}
```

### Syntax（取自子主题 DPS_AUX_TASK.getVoltageDropForceWarn()）

```
TM::DPS_POWER_FLAG_STATUS getVoltageDropForceWarn(const STRING& pin);
```

[表] Parameter
列: Parameter | Description/Range
行 1:
  pin
  Single pin for which the status flags should be
    retrieved.

### Return value（取自子主题 DPS_AUX_TASK.getVoltageDropForceWarn()）

The member function returns one of the following
values of the enumerated type
DPS_POWER_FLAG_STATUS
:

[表]
列: Keyword | Value | State of the checked flags
行 1:
  TM::POWER_FLAG_STATUS_PASS
  0
  The checked flag is not set.
行 2:
  TM::POWER_FLAG_STATUS_FAIL
  1
  The checked flag is set.

### Syntax（取自子主题 DPS_AUX_TASK.getVoltageDropReturn()）

```
TM::DPS_POWER_FLAG_STATUS getVoltageDropReturn(const STRING& pin);
```

[表] Parameter
列: Parameter | Description/Range
行 1:
  pin
  Single pin for which the status flags should be
    retrieved.

### Return value（取自子主题 DPS_AUX_TASK.getVoltageDropReturn()）

The member function returns one of the following
values of the enumerated type
DPS_POWER_FLAG_STATUS
:

[表]
列: Keyword | Value | State of the checked flags
行 1:
  TM::POWER_FLAG_STATUS_PASS
  0
  The checked flag is not set.
行 2:
  TM::POWER_FLAG_STATUS_FAIL
  1
  The checked flag is set.

Return value in offline mode is
TM::POWER_FLAG_STATUS_PASS
.

### Example（取自子主题 DPS_AUX_TASK.getVoltageDropReturn()）

The following example reads the actual state of all power flags, clears all flags and evaluates
the state of the "
Voltage drop return
" flag.
The returned value is
TM::POWER_FLAG_STATUS_FAIL
 if the checked
flag is set.

```
DPS_AUX_TASK dpsAuxTask_1;

ON_FIRST_INVOCATION_BEGIN();
{
//
// Read actual power flag status of two pins
//
dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read latched state & clear all flags
dpsAuxTask_1.pin("dps1,dps2").checkPowerFlags(); // Read actual state & clear all flags
}
ON_FIRST_INVOCATION_END();

//
// Evaluate the state of the first pin
//
if (dpsAuxTask_1.getVoltageDropReturn("dps1") == TM::POWER_FLAG_STATUS_PASS)
{
cout << "dpsAuxTask_1.getVoltageDropReturn(\"dps1\") returned TM::POWER_FLAG_STATUS_PASS" << endl;
}
else
{
cout << "dpsAuxTask_1.getVoltageDropReturn(\"dps1\") returned TM::POWER_FLAG_STATUS_FAIL" << endl;
}
```

### Syntax（取自子主题 DPS_AUX_TASK.getVoltageDropReturnWarn()）

```
TM::DPS_POWER_FLAG_STATUS getVoltageDropReturnWarn(const STRING& pin);
```

[表] Parameter
列: Parameter | Description/Range
行 1:
  pin
  Single pin for which the status flags should be
    retrieved.

### Return value（取自子主题 DPS_AUX_TASK.getVoltageDropReturnWarn()）

The member function returns one of the following
values of the enumerated type
DPS_POWER_FLAG_STATUS
:

[表]
列: Keyword | Value | State of the checked flags
行 1:
  TM::POWER_FLAG_STATUS_PASS
  0
  The checked flag is not set.
行 2:
  TM::POWER_FLAG_STATUS_FAIL
  1
  The checked flag is set.

### Member functions（取自子主题 DPS status flags - get...() functions）

Several get...() member functions are documented
in this section. These member functions retrieve the value of all flags or of a
single status flag from the test method cache. The related
`DPS_AUX_PIN_TASK.check...()`（raw: `141284.htm`）
 member function must be called upfront for
reading the flags from the hardware into the test method cache.

The member
functions return one of the following values of the enumerated type

DPS_AUX_TASK_STATUS
:

[表]
列: Keyword | Value | State of the checked flags
行 1:
  TM::AUX_TASK_STATUS_PASS
  0
  The checked single flag is not set or none of multiple checked
    flags is set.
行 2:
  TM::AUX_TASK_STATUS_FAIL
  1
  The checked flag is set or minimum one of multiple checked flags
    is set.

### Syntax（取自子主题 DPS_AUX_TASK.getIcHacError()）

```
TM::DPS_AUX_TASK_STATUS getIcHacError(const STRING& pin);
```

[表] Parameter
列: Parameter | Description/Range
行 1:
  pin
  Single pin for which the status flags should be
    retrieved.

### Return value（取自子主题 DPS_AUX_TASK.getIcHacError()）

The member function returns one of the following
values of the enumerated type
DPS_POWER_FLAG_STATUS
:

[表]
列: Keyword | Value | State of the checked flags
行 1:
  TM::AUX_TASK_STATUS_PASS
  0
  The checked flag is not set.
行 2:
  TM::AUX_TASK_STATUS_FAIL
  1
  The checked flag is set.

Return value in offline mode is
TM::AUX_TASK_STATUS_PASS
.

### Example（取自子主题 DPS_AUX_TASK.getIcHacError()）

```
DPS_AUX_TASK auxTask;

ON_FIRST_INVOCATION_BEGIN();

auxTask.pin("dps2").checkIcHacError();

ON_FIRST_INVOCATION_END();

if ( auxTask.getIcHacError("dps2") == TM::AUX_TASK_STATUS_PASS )
{
cout << "auxTask.getIcHacError(\"dps2\") returned TM::AUX_TASK_STATUS_PASS" << endl;
}
else
{
cout << "auxTask.getIcHacError(\"dps2\") returned TM::AUX_TASK_STATUS_FAIL" << endl;
}
```

### Syntax（取自子主题 DPS_AUX_TASK.getRangeError()）

```
TM::DPS_AUX_TASK_STATUS getRangeError(const STRING & pin);
```

Parameter
[表]
列: Parameter | Description/Range
行 1:
  pin
  Single pin for which the status flags should be
    retrieved.
Return value

The member function returns one of the following values of the enumerated
type
DPS_POWER_FLAG_STATUS
:

[表]
列: Keyword | Value | State of the checked flags
行 1:
  TM::AUX_TASK_STATUS_PASS
  0
  The checked flag is not set.
行 2:
  TM::AUX_TASK_STATUS_FAIL
  1
  The checked flag is set.

Return value in offline mode is

TM::AUX_TASK_STATUS_PASS
.

### Example（取自子主题 DPS_AUX_TASK.getRangeError()）

```
DPS_AUX_TASK auxTask;

ON_FIRST_INVOCATION_BEGIN();

auxTask.pin("dps2").checkSetRangeError();

ON_FIRST_INVOCATION_END();

if ( auxTask.getRangeError("dps2") == TM::AUX_TASK_STATUS_PASS )
{
cout << "auxTask.getRangeError(\"dps2\") returned TM::AUX_TASK_STATUS_PASS" << endl;
}
else
{
cout << "auxTask.getRangeError(\"dps2\") returned TM::AUX_TASK_STATUS_FAIL" << endl;
}
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

**文档事实** DPS_AUX_TASK 类控制 DC Scale 卡的 surge tracker 与 TMU（Time Measure Unit）。

**文档事实** 源页列出的支持情况是：surge tracker 支持 DPS128/DPS64 与 XPS256；TMU 目前不被任何卡支持。

**文档事实** DPS_AUX_TASK 可加入 TASK_LIST，并与其他 TASK 类型类协同工作；其 API 定义在头文件 `/opt/hp93000/soc/prod_com/include/MAPI/DpsAuxTask.h`。

**文档事实** 源页注明不要在 test method 中创建该类的静态对象，也不要创建该类的 test method 成员变量。

**文档事实** 该类通过 pin() 取得 DPS_AUX_PIN_TASK，再链式调用 setMode()、selectISensorSetThresholds()、selectVSensorSetThresholds() 等方法；用 execute() 执行，用 checkSurgeTracker()、checkPowerFlags() 等把硬件状态读入 test method cache，再用 get...() 取结果。

## 典型用法

**文档事实** 源页示例流程为：在 ON_FIRST_INVOCATION 块中创建 DPS_AUX_TASK，用 `pin("dps1").selectISensorSetThresholds(-1 mA, 1 mA).setMode(TM::SURGE_TRACKER)` 设阈值并开启 surge tracker，调用 execute()，再调用 `pin("dps1").checkSurgeTracker(TM::AGAINST_BOTH)`，最后用 getSurgeTrackerStatus("dps1") 取回状态。

**文档事实** pin() 的 pinlist 可用逗号分隔多个引脚；checkPowerFlags() 可带 flags 掩码（默认 TM::ALL_FLAGS），其 get...() 系列函数从 test method cache 读取标志值，因此必须先调用 checkPowerFlags() 才能把硬件标志读入 cache。

**文档事实** 对 XPS256，getSurgeTrackerStatus() 有第二种语法，可分别返回电压与电流 surge tracker 状态；该语法要求同时设置电压阈值与电流阈值才有效。

**文档事实** XPS256 的 site 级阈值示例在 ON_FIRST_INVOCATION 中设公共阈值、在 FOR_EACH_SITE 中替换为各 site 阈值，并在另一个 FOR_EACH_SITE 中读取结果；示例用 RDI_INIT() 与 SmartRDI 配合，并说明 setMode() 只在 FOR_EACH_SITE 外调用以避免告警。

**文档事实** 源页的 offline mode 说明：getAllStatus() 因 "Constant voltage" 标志在 offline 下恒置位而返回 TM::POWER_FLAG_STATUS_FAIL；getStatusWithoutConstVol() 及其他单个标志 get...() 在 offline 下返回 TM::POWER_FLAG_STATUS_PASS。

## 和谁有关

- **文档事实** DPS_AUX_PIN_TASK：本页 Related information 与 Subtopics 直接指向它；它是 DPS_AUX_TASK 的附属数据容器，pin() 返回该类型引用，setMode/select.../check... 等方法定义在它上面。
- **文档事实** TASK_LIST：本页 Related information 与 Subtopics 指向它；DPS_AUX_TASK 可加入 TASK_LIST，加入后由 TASK_LIST 的 execute() 调用其 execute()。
- **文档事实** DPS128/DPS64 与 XPS256：本页明确列出它们是 surge tracker 支持的 DC Scale 卡；示例分别用 dps1 与 XPS256 引脚演示。
- **文档事实** ON_FIRST_INVOCATION 与 FOR_EACH_SITE：源页示例在 ON_FIRST_INVOCATION_BEGIN/END 内配置与执行；XPS256 site 级阈值示例用 FOR_EACH_SITE 循环设置和读取阈值。
- **文档事实** RDI_INIT 与 SmartRDI：XPS256 示例以 RDI_INIT() 作为 SmartRDI 代码的前置，并按 SmartRDI 要求在 FOR_EACH_SITE 中读取结果。
- **文档事实** XPS256 programming - Surge tracker / Force and clamp voltages / Force and clamp currents：这些卡编程页指向 DPS_AUX_TASK 与 DPS_AUX_PIN_TASK，说明 surge tracker 的完整功能由这两类 API 覆盖。

## 版本

**文档事实** Functional changes 记 Introduced in SmarTest 7.2.1；SmarTest 7.3.1 新增 DC Scale PVI8 卡；SmarTest 7.4.0 新增 DC Scale AVI64 卡，并新增 getBatteryFull()、getPowerBudgetWarningAll()、getPowerBudgetWarning1()/...Warning2()/...Warning3() 以及返回 DPS_POWER_FLAG_STATUS 的成员函数；SmarTest 7.5.0 新增 DC Scale FVI16 卡。

## 出处

- `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43_DPS_AUX_TASK.htm`，主源，含类说明、支持卡、头文件、构造/示例、Related information 与 Functional changes。
- 语法节还逐字取自其子主题 DPS_AUX_PIN_TASK、execute、pin、setup、getSurgeTrackerStatus，以及 DPS power flags / DPS status flags 的 get...() 函数与被引用页面。
