---
type: object
title: HW_STATE
layer: L2
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.117_HW_STATE.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# HW_STATE

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **39,795 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.117_HW_STATE.htm>` 及其子主题 `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.117.01_HW_PIN_STATE.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.117.02_HW_STATE.checkKelvinStatus.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.117.03_HW_STATE.checkKelvinStatusParallel.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.117.04_HW_STATE.checkGangConnection.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.117.05_HW_STATE.checkGangConnectionParallel.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Class definition

This API is defined in the header file

/opt/hp93000/soc/prod_com/include/MAPI/HwState.h
.

Constructor

```
HW_STATE();
```

This constructor creates an object of
HW_STATE
 class.
It contains the hardware setting status. You can retrieve the settings
with the member functions of
`HW_PIN_STATE`（raw: `105632.htm`）
.

Member functions
[表]
行 1:
  `getStatus()`（raw: `105633.htm#_105633__dle_getStatus`）
    
    `pin()`（raw: `105633.htm#_105633__dle_pin`）
    
    `readMaxAbsVdropsParallel`（raw: `105633.htm#_105633__dle_readMaxAbsVdropsParallel`）
    
    `getMaxAbsVdrops`（raw: `105633.htm#_105633__dle_getMaxAbsVdrops`）
  `checkKelvinStatus()`（raw: `105633.htm#_105633__dle_checkKelvinStatus`）
    
    `checkKelvinStatusParallel()`（raw: `105633.htm#_105633__dle_checkKelvinStatusParallel`）
    
    `checkGangConnection()`（raw: `105633.htm#_105633__dle_checkGangConnection`）
    
    `checkGangConnectionParallel()`（raw: `105633.htm#_105633__dle_checkGangConnectionParallel`）

### Member functions

getStatus()

```
void getStatus(const STRING &pinlist);
```

This function queries the status of specified pins for the site in focus.
You need to call this method every time the settings of the hardware are
changed. The read data are stored in
HW_STATE

object.

The member function must be called outside of the
`ON_FIRST_INVOCATION`（raw: `29526.htm`）
 block or within a
`FOR_EACH_SITE...WITH_QUERY`（raw: `116559.htm`）
 block.

The data read from the hardware and stored in the
HW_STATE
 object can be
retrieved per pin and property by the
`pin()`（raw: `105633.htm#_105633__dle_pin`）

function followed by a member function of the subsidiary
`HW_PIN_STATE`（raw: `105632.htm`）
 class.

Parameter
[表]
行 1:
  pinList
  A comma‑separated list of the pins to be
    queried.
    
    If the pinList is empty or
    an invalid pin is specified, an error message will
    be thrown out and the query will not be
    executed.
Return value
There is no return value.
pin()

```
HW_PIN_STATE& pin(const STRING &pinName);
```

This function returns the hardware settings for the specified pin. These settings are the
settings of the hardware at the time you call the
`getStatus()`（raw: `105633.htm#_105633__dle_getStatus`）
 member function. The requested
setting needs to be defined by a member function of the subsidiary
`HW_PIN_STATE`（raw: `105632.htm`）
 class.

Parameter
[表]
行 1:
  pinName
  The pin that will be queried.
    
    If the pinName is empty or is not in the
    pinList of `getStatus()`（raw: `105633.htm#_105633__dle_getStatus`）, an error message
    will be thrown out and no setting will be
    returned.
Return value
A reference to the subsidiary
`HW_PIN_STATE`（raw: `105632.htm`）
 class.
checkKelvinStatus()

```
bool checkKelvinStatus(...);
```

This member function initiates a sense connection test for the site in focus on the defined pins.

For the syntax and more information refer to
`HW_STATE.checkKelvinStatus()`（raw: `150082.htm`）
.

checkKelvinStatusParallel()

```
bool checkKelvinStatusParallel(...);
```

This member function initiates a sense connection test for all active sites on the defined pins.

For the syntax and more information refer to
`HW_STATE.checkKelvinStatusParallel()`（raw: `152227.htm`）
.

checkGangConnection()
```
bool checkGangConnection (...);
```

The function is supported only with the
`DC Scale XPS256 card`（raw: `350661.htm`）
.

For the syntax
and more information refer to
`HW_STATE.checkGangConnection()`（raw: `355895.htm`）
.
checkGangConnectionParallel()
```
bool checkGangConnectionParallel (...);
```

The function is supported only with the
`DC Scale XPS256 card`（raw: `350661.htm`）
.

For the
syntax and more information refer to
`HW_STATE.checkGangConnectionParallel()`（raw: `355896.htm`）
.
readMaxAbsVdropsParallel

```
void readMaxAbsVdropsParallel(const STRING &pinlist, const Boolean reset);
```

This member function reads the latched maximum absolute voltage drop
values from the hardware. The values are read for the given list of pins
for all active sites and are stored in the test method cache. As long as
the test method is loaded, the stored values in the test method cache
are valid and can be retrieved with the
`getMaxAbsVdrops`（raw: `105633.htm#_105633__dle_getMaxAbsVdrops`）
 function.

The
reset
 parameter defines whether the latched values
are then cleared.

The function should be called in the
`ON_FIRST_INVOCATION`（raw: `29526.htm`）
 block and is supported only with the

`DC Scale XPS256 card`（raw: `350661.htm`）
 card.

Parameter
[表]
行 1:
  pinList
  A comma‑separated list of the pins to be
    queried.
    
    If the pinList is empty or
    an invalid pin is specified, an error message will
    be thrown out and the query will not be
    executed.
行 2:
  reset
  Options are:
    
    true (default): Reset after
    readout.
    
    false: Do not reset after
    readout.
Return value
There is no return value.
getMaxAbsVdrops
```
void getMaxAbsVdrops(const STRING &pin, DOUBLE maxAbsForceDrop, DOUBLE maxAbsReturnDrop);
```

This function queries the maximum absolute force and return voltage drop values for the defined
pin on the site in focus.

The
`readMaxAbsVdropsParallel`（raw: `105633.htm#_105633__dle_readMaxAbsVdropsParallel`）
 member function must
be called upfront for reading the flags from the hardware into the test
method cache.

The function should be called in a
`FOR_EACH_SITE...WITH_QUERY`（raw: `116559.htm`）

block or outside the
`ON_FIRST_INVOCATION`（raw: `29526.htm`）

block and is supported only with the
`DC Scale XPS256 card`（raw: `350661.htm`）
 card.

Parameter
[表]
行 1:
  pin
  The pin that will be queried.
    
    If the pinName is empty or
    is not in the pinList of
    getStatus(), an error message
    will be thrown out and no setting will be
    returned.
行 2:
  maxAbsForceDrop
  The maximum absolute force voltage drop in
    volts (V) for the queried pin and the site in
    focus.
行 3:
  maxAbsReturnDrop
  The maximum absolute return voltage drop in
    volts (V) for the queried pin and the site in
    focus.
Return value
There is no return value.

### Examples

### Example 1: Query the status outside the ON_FIRST_INVOVATION block

The status is read from the hardware, stored in the
HW_STATE
 object, and
finally retrieved from the
HW_STATE
 object for the site in focus
outside of the
`ON_FIRST_INVOCATION`（raw: `29526.htm`）
 block.

```
HW_STATE hwState;
DOUBLE forcedVoltage;
DOUBLE clampCurrent;

ON_FIRST_INVOCATION_BEGIN();
{
...
...
}
ON_FIRST_INVOCATION_END();

hwState.getStatus ("PMU_pin_1, DPS_pin_1");

forcedVoltage = hwState.pin ("DPS_pin_1").getVoltageForce();
clampCurrent = hwState.pin ("DPS_pin_1").getCurrentClampSource();

cout << "Current site: " << CURRENT_SITE_NUMBER() << ", pin \"DPS_pin_1\"" << endl;

cout << "\tForced voltage: " << forcedVoltage << endl;
cout << "\tCurrent clamp source: " << clampCurrent << endl;
```

### Example 2: Query the status in a FOR_EACH_SITE...WITH_QUERY block

The status is read from the hardware, stored in the
HW_STATE
 object, and
finally retrieved from the
HW_STATE
 object for the site in focus
within a
FOR_EACH_SITE
 block in the
`ON_FIRST_INVOCATION`（raw: `29526.htm`）
 block. The
`FOR_EACH_SITE_BEGIN_WITH_QUERY`（raw: `116559.htm`）
 API must be used
to set the query focus within the
FOR_EACH_SITE
 block.

```
HW_STATE hwState;
DOUBLE forcedVoltage;
DOUBLE clampCurrent;

ON_FIRST_INVOCATION_BEGIN();
{
...
...

FOR_EACH_SITE_BEGIN_WITH_QUERY();
{
hwState.getStatus ("PMU_pin_1, DPS_pin_1");

forcedVoltage = hwState.pin ("PMU_pin_1").getVoltageForce();
clampCurrent = hwState.pin ("PMU_pin_1").getCurrentClampSource();

cout << "Current site: " << CURRENT_SITE_NUMBER() << ", pin \"PMU_pin_1\"" << endl;

cout << "\tForced voltage: " << forcedVoltage << endl;
cout << "\tCurrent clamp source: " << clampCurrent << endl;
}
FOR_EACH_SITE_END();
}
ON_FIRST_INVOCATION_END();
```

### Class definition（取自子主题 HW_PIN_STATE）

This API is defined in the header file

/opt/hp93000/soc/prod_com/include/MAPI/HwPinState.h
.

Constructor

This class has no constructor.

You can access this class object via
the
`pin()`（raw: `105633.htm#_105633__dle_pin`）
 member function of the
`HW_STATE`（raw: `105633.htm`）
 class by specifying the pin name. You cannot
directly construct any objects of this class.

Member functions
Member functions returning DOUBLE:
[表]
行 1:
  `getCompHoldOff()`（raw: `105632.htm#_105632__dle_getCompHoldOff`）
    
    `getCompHysteresis()`（raw: `105632.htm#_105632__dle_getCompHysteresis`）
    
    `getConstCurrTimeToAlarm()`（raw: `105632.htm#_105632__dle_getConstCurrTimeToAlarm`）
    
    `getConstCurrTimeToDisconnect()`（raw: `105632.htm#_105632__dle_getConstCurrTimeToDisconnect`）
    
    `getComplianceValue()`（raw: `105632.htm#_105632__dle_getComplianceValue`）
    
    `getCurrentClampFilter()`（raw: `105632.htm#_105632__dle_getCurrentClampFilter`）
    
    `getCurrentClampMax()`（raw: `105632.htm#_105632__dle_getCurrentClampMax`）
    
    `getCurrentClampMin()`（raw: `105632.htm#_105632__dle_getCurrentClampMin`）
    
    `getCurrentClampSink()`（raw: `105632.htm#_105632__dle_getCurrentClampSink`）
    
    `getCurrentClampSource()`（raw: `105632.htm#_105632__dle_getCurrentClampSource`）
    
    `getCurrentForce()`（raw: `105632.htm#_105632__dle_getCurrentForce`）
  `getCurrentForceMax()`（raw: `105632.htm#_105632__dle_getCurrentForceMax`）
    
    `getCurrentForceMin()`（raw: `105632.htm#_105632__dle_getCurrentForceMin`）
    
    `getCurrentSlew()`（raw: `105632.htm#_105632__dle_getCurrentSlew`）
    
    `getDCPower()`（raw: `105632.htm#_105632__dle_getDCPower`）
    
    `getLoadcap()`（raw: `105632.htm#_105632__dle_getLoadcap`）
    
    `getMeasFilter()`（raw: `105632.htm#_105632__dle_getMeasFilter`）
    
    `getPulseEnergy()`（raw: `105632.htm#_105632__dle_getPulseEnergy`）
    
    `getVoltageClampHigh()`（raw: `105632.htm#_105632__dle_getVoltageClampHigh`）
    
    `getVoltageClampLow()`（raw: `105632.htm#_105632__dle_getVoltageClampLow`）
  `getVoltageClampMax()`（raw: `105632.htm#_105632__dle_getVoltageClampMax`）
    
    `getVoltageClampMin()`（raw: `105632.htm#_105632__dle_getVoltageClampMin`）
    
    `getVoltageDropMaxForce()`（raw: `105632.htm#_105632__dle_getVoltageDropMaxForce`）
    
    `getVoltageDropMaxReturn()`（raw: `105632.htm#_105632__dle_getVoltageDropMaxReturn`）
    
    `getVoltageDropWarnForce()`（raw: `105632.htm#_105632__dle_getVoltageDropWarnForce`）
    
    `getVoltageDropWarnReturn()`（raw: `105632.htm#_105632__dle_getVoltageDropWarnReturn`）
    
    `getVoltageForce()`（raw: `105632.htm#_105632__dle_getVoltageForce`）
    
    `getVoltageForceFilter()`（raw: `105632.htm#_105632__dle_getVoltageForceFilter`）
    
    `getVoltageForceMax()`（raw: `105632.htm#_105632__dle_getVoltageForceMax`）
    
    `getVoltageForceMin()`（raw: `105632.htm#_105632__dle_getVoltageForceMin`）
    
    `getVoltageSlew()`（raw: `105632.htm#_105632__dle_getVoltageSlew`）
Member functions returning INT:

`getActiveChannels()`（raw: `105632.htm#_105632__dle_getActiveChannels`）

`getStackLevel()`（raw: `105632.htm#_105632__dle_getStackLevel`）

Member functions returning STRING:

`getCompSelector()`（raw: `105632.htm#_105632__dle_getCompSelector`）

`getConnectState()`（raw: `105632.htm#_105632__dle_getConnectState`）

`getLoadStepMode()`（raw: `105632.htm#_105632__dle_getLoadStepMode`）

`getOpenLoopProtection()`（raw: `105632.htm#_105632__dle_getOpenLoopProtection`）

`getPulldownState()`（raw: `105632.htm#_105632__dle_getPulldownState`）

`getReferencePin()`（raw: `105632.htm#_105632__dle_getReferencePin`）

`getVoltageClampState()`（raw: `105632.htm#_105632__dle_getVoltageClampState`）

Note
  For all of the member functions, listed above, the
`HW_STATE`（raw: `105633.htm`）
 member function
`getStatus()`（raw: `105633.htm#_105633__dle_getStatus`）
 member function must be called
upfront to retrieve the data from the hardware.

### Member functions returning DOUBLE（取自子主题 HW_PIN_STATE）

getCompHoldOff()

```
DOUBLE getCompHoldOff() const;
```

This function queries the comparator hold off time of the specified pin.
It returns the real value of the hardware. The unit of the returned
value is ns (Nanoseconds).

If this setting of the hardware is not applicable,
NaN

(Not a Number) is returned.

getCompHysteresis()

```
DOUBLE getCompHysteresis() const;
```

This function queries the comparator hysteresis of the specified pin. It
returns the real value of the hardware. The unit of the returned value
is % (Percent).

If this setting of the hardware is not applicable,
NaN

(Not a Number) is returned.

getComplianceValue()

```
DOUBLE getComplianceValue() const;
```

This function queries the compliance voltage of the specified pin. It
returns the real value of the hardware.

If this setting of the hardware is not applicable,
NaN

(Not a Number) is returned.

getConstCurrTimeToAlarm()

```
DOUBLE getConstCurrTimeToAlarm() const;
```

This function queries the time until the "
Constant current
" flag is set for
a channel that is in constant current mode without interruption. It
returns the real value of the hardware.

The function is supported only with DC Scale XPS256 card.

getConstCurrTimeToDisconnect()

```
DOUBLE getConstCurrTimeToDisconnect() const;
```

This function queries the delay time before a channel that is in constant
current mode without interruption is disconnected. It returns the real
value of the hardware.

The function is supported only with DC Scale XPS256 card.

getCurrentClampFilter()

```
DOUBLE getCurrentClampFilter () const;
```

This function queries the clamp current filter setting of the specified
pin. It returns the real value of the hardware. The returned value is
the clamp current filter frequency in Hz.

If this setting of the hardware is not applicable for example, filter
value is set to "OFF" or the hardware does not support the filter),

NaN
 (Not a Number) is returned.

getCurrentClampMax()

```
DOUBLE getCurrentClampMax() const;
```

This function queries the maximum clamp current of the specified pin. It
returns the real value of the hardware.

If this setting of the hardware is not applicable,
NaN

(Not a Number) is returned.

getCurrentClampMin()

```
DOUBLE getCurrentClampMin() const;
```

This function queries the minimum clamp current of the specified pin. It
returns the real value of the hardware.

If this setting of the hardware is not applicable,
NaN

(Not a Number) is returned.

getCurrentClampSink()

```
DOUBLE getCurrentClampSink() const;
```

This function queries the sink current clamp of the specified pin. It
returns the real value of the hardware.

If this setting of the hardware is not applicable,
NaN

(Not a Number) is returned.

getCurrentClampSource()

```
DOUBLE getCurrentClampSource() const;
```

This function queries the source current clamp of the specified pin. It
returns the real value of the hardware.

If this setting of the hardware is not applicable,
NaN

(Not a Number) is returned.

getCurrentForce()

```
DOUBLE getCurrentForce() const;
```

This function queries the force current of the specified pin. It returns
the real value of the hardware.

If the force current of the hardware is not applicable,

NaN
 (Not a Number) is returned.

getCurrentForceMax()

```
DOUBLE getVoltageForceMax() const;
```

This function queries the maximum force current of the specified pin. It
returns the real value of the hardware.

If the maximum force current of the hardware is not applicable,

NaN
 (Not a Number) is returned.

getCurrentForceMin()

```
DOUBLE getCurrentForceMin() const;
```

This function queries the minimum force current of the specified pin. It
returns the real value of the hardware.

If the force current of the hardware is not applicable,

NaN
 (Not a Number) is returned.

getCurrentSlew()

```
DOUBLE getCurrentSlew() const;
```

This function queries the current slew rate of the specified pin. It
returns the real value of the hardware. The unit of the returned value
is A / s (Ampere per second).

If this setting of the hardware is not applicable for example, the slew
rate is not defined and therefore set to the maximum value or the
hardware does not support the slew rate setting),
NaN

(Not a Number) is returned.

getDCPower()

```
DOUBLE getDCPower() const;
```

This function queries the assigned power budget for DC tests. It returns
the real value of the hardware. The unit of the returned value is mW
(Milliwatt).

If this setting of the hardware is not applicable for example, the
assigned power budget is not defined and therefore set to the default
value or the hardware does not support the assigned power budget
setting),
NaN
 (Not a Number) is returned.

getLoadcap()

```
DOUBLE getLoadcap() const;
```

This function queries the specified load capacitance of the specified
pin. It returns the real value of the hardware. The unit of the returned
value is µF (Microfarad).

If the load capacitance is not applicable,
NaN
 (Not a
Number) is returned.

getMeasFilter()

```
DOUBLE getMeasFilter() const;
```

This function queries the measure filter of the specified pin. It returns
the real value of the hardware. The unit of the returned value is Hz
(Hertz).

If this setting of the hardware is not applicable or if the measure
filter is not defined,
NaN
 (Not a Number) is
returned.

getPulseEnergy()

```
DOUBLE getPulseEnergy() const;
```

This function queries the assigned energy budget for pulsed tests. It
returns the real value of the hardware. The unit of the returned value
is mJ (Millijoule)
`1)`（raw: `#fntarg_1`）
.

If this setting of the hardware is not applicable for example, the
assigned energy budget is not defined and therefore set to the default
value or the hardware does not support the assigned energy budget
setting),
NaN
 (Not a Number) is returned.

getVoltageClampHigh()

```
DOUBLE getVoltageClampHigh() const;
```

This function queries the high clamp voltage of the specified pin. It
returns the real value of the hardware.

If this setting of the hardware is not applicable,
NaN

(Not a Number) is returned.

getVoltageClampLow()

```
DOUBLE getVoltageClampLow() const;
```

This function queries the low clamp voltage of the specified pin. It
returns the real value of the hardware.

If this setting of the hardware is not applicable,
NaN

(Not a Number) is returned.

getVoltageClampMax()

```
DOUBLE getVoltageClampMax() const;
```

This function queries the maximum clamp voltage of the specified pin. It
returns the real value of the hardware.

If this setting of the hardware is not applicable,
NaN

(Not a Number) is returned.

getVoltageClampMin()

```
DOUBLE getVoltageClampMin() const;
```

This function queries the minimum clamp voltage of the specified pin. It
returns the real value of the hardware.

If this setting of the hardware is not applicable,
NaN

(Not a Number) is returned.

getVoltageDropMaxForce()

```
DOUBLE getVoltageDropMaxForce() const;
```

This function queries the maximum force drop voltage of the specified
pin. It returns the real value of the hardware.

If this setting of the hardware is not applicable,
NaN

(Not a Number) is returned.

getVoltageDropMaxReturn()

```
DOUBLE getVoltageDropMaxReturn() const;
```

This function queries the maximum return drop voltage of the specified
pin. It returns the real value of the hardware.

If this setting of the hardware is not applicable,
NaN

(Not a Number) is returned.

getVoltageForce()

```
DOUBLE getVoltageForce() const;
```

This function queries the force voltage of the specified pin. It returns
the real value of the hardware.

If the force voltage of the hardware is not applicable,

NaN
 (Not a Number) is returned.

getVoltageForceFilter()

```
DOUBLE getVoltageForceFilter () const;
```

This function queries the force voltage filter setting of the specified
pin. It returns the real value of the hardware. The returned value is
the voltage source filter frequency in Hz.

 If this setting of the hardware is not applicable for example, filter
value is set to
"OFF"
 or the hardware does not
support the filter),
NaN
 (Not a Number) is returned.

getVoltageForceMax()

```
DOUBLE getVoltageForceMax() const;
```

This function queries the maximum force current of the specified pin. It
returns the real value of the hardware.

If the maximum force current of the hardware is not applicable,

NaN
 (Not a Number) is returned.

getVoltageForceMin()

```
DOUBLE getVoltageForceMin() const;
```

This function queries the minimum force voltage of the specified pin. It
returns the real value of the hardware.

If the minimum force voltage of the hardware is not applicable,

NaN
 (Not a Number) is returned.

getVoltageSlew()

```
DOUBLE getVoltageSlew() const;
```

This function queries the voltage slew rate of the specified pin. It
returns the real value of the hardware. The unit of the returned value
is mV / µs (Millivolt per microsecond).

If this setting of the hardware is not applicable for example, the slew
rate is not defined and therefore set to the maximum value or the
hardware does not support the slew rate setting),
NaN

(Not a Number) is returned.

getVoltageDropWarnForce()

```
DOUBLE getVoltageDropWarnForce() const;
```

This function queries the force drop voltage threshold (above which the
"
Voltage drop force
warning
" status
flag is set), of the specified pin. It returns the real value of the
hardware.

The function is supported only for the DC Scale XPS256 card.

getVoltageDropWarnReturn()

```
DOUBLE getVoltageDropWarnReturn() const;
```

This function queries the return drop voltage threshold (above which the
"
Voltage drop return
warning
"
status flag is set), of the specified pin. It returns the real value of
the hardware.

The function is supported only for the DC Scale XPS256 card.

### Member functions returning INT（取自子主题 HW_PIN_STATE）

getActiveChannels()

```
INT getActiveChannels(void) const;
```

This function queries the number of active channels of the specified
pin.

If this setting of the hardware is not applicable,
NaN

(Not a Number) is returned.

getStackLevel()

```
INT getStackLevel(void) const;
```

This function queries the number of stack level of the specified pin.

If this setting of the hardware is not applicable,
NaN

(Not a Number) is returned.

### Member functions returning STRING（取自子主题 HW_PIN_STATE）

getCompSelector()
```
STRING getCompSelector() const;
```

This function
queries the comparator selector of the specified pin. It returns the
real value of the hardware.

[表]
列: Returned value | Meaning | Supported pin types
行 1:
  "na"
  The comparator selector is not applicable or not
    defined.
  DPS, SIG
行 2:
  "LS"
  The high-resolution voltage or current comparator.
    
    This is the default comparator for an AVI64
    channel in the PMU operating mode.
  SIG (AVI64 only)
行 3:
  "LS_DIFFVM"
  High-resolution voltage comparator of the
    differential voltmeter.
  SIG (AVI64 only)
行 4:
  "HS"
  High-speed digital voltage comparator.
  SIG (AVI64 only)
行 5:
  "HS_TERM"
  Terminated high-speed digital voltage comparator.
    Input signal is terminated to ground via 50 O.
  SIG (AVI64 only)
行 6:
  "HS_DIFFERENTIAL"
  Differential high-speed digital voltage
    comparator.
  SIG (AVI64 only)
getConnectState()
```
STRING getConnectState() const;
```

This function
queries the connection state setting of the specified pin. It returns
the real value of the hardware.

[表]
列: Returned value | Meaning | Supported pin types
行 1:
   [跨 3 行]
  "FAST"
  The fast VI mode.
  SIG
行 2:
  "NORMAL"
  The default mode for DPS application.
  DPS, SIG
行 3:
  "PULSE"
  The high-current mode.
  DPS, SIG
getLoadStepMode()
```
STRING getLoadStepMode() const;
```

This function
queries the loadstep mode of the specified pin. It returns the real
value of the hardware.

Possible return values are "
STD
" or
"
FAST
".

The function is supported only for the DC Scale XPS256 card.

If this setting of the hardware is not applicable,

"na"
 is returned.

getOpenLoopProtection()
```
STRING getOpenLoopProtection() const;
```

This
function queries the setting of the open loop protection for the
specified pin. It returns the real value of the hardware.

Possible return values are "
DIODE
" or
"
NONE
".

The function is supported only for the DC Scale XPS256 card.

If this setting of the hardware is not applicable,

"na"
 is returned.

getPulldownState()
```
STRING getPulldownState() const;
```

This function
queries the pulldown state of the specified pin. It returns the real
value of the hardware.

Possible return values are "
ON
" or
"
OFF
".

The function is supported only for the DC Scale XPS256 card.

If this setting of the hardware is not applicable,

"na"
 is returned.

getReferencePin()
```
STRING getReferencePin() const;
```

This function
queries the reference pin of the specified pin. It returns the real
value of the hardware. The function returns
"GND"
 if
the reference pin is not defined or is defined as

TM::REF_GND
 for measure modes that support a
reference pin.

If this setting of the hardware is not applicable,

"na"
 is returned.

getVoltageClampState()
```
STRING getVoltageClampState() const;
```

This function
queries the clamp status. It returns
"ON"
 or

"OFF"
.

### Example（取自子主题 HW_PIN_STATE）

For an example, refer to

`Example 1: Query the status outside the ON_FIRST_INVOVATION block`（raw: `105633.htm#_105633__ex_Example_ON_FIRST_INVOCATION`）
 and

`Example 2: Query the status in a FOR_EACH_SITE...WITH_QUERY block`（raw: `105633.htm#_105633__ex_Example_FOR_EACH_SITE`）

in
`HW_STATE`（raw: `105633.htm`）
.

### Syntax（取自子主题 HW_STATE.checkKelvinStatus()）

```
bool checkKelvinStatus(const STRING pinList, ARRAY_I & statusPos, ARRAY_I & statusNeg);
bool checkKelvinStatus(const STRING pinlist, const INT samples, ARRAY_I &statusPos, ARRAY_I &statusNeg);
```

The following syntax is supported only for the
`DC Scale XPS256 card`（raw: `350661.htm`）
:

```
bool checkKelvinStatus(const STRING pinlist, const INT samples,
const DOUBLE maxResistance, ARRAY_I &statusPos, ARRAY_I &statusNeg);

bool checkKelvinStatus(const STRING pinlist, const INT samples,
const DOUBLE maxResistancePos, const DOUBLE maxResistanceNeg, ARRAY_I &statusPos, ARRAY_I &statusNeg);
```

[表] Parameters
列: Parameter | Description/Range
行 1:
  pinList
  The pins connected to the DUT board that will be queried. The pins are separated with commas. If the
    pinList is empty or an invalid pin is specified, an error message will be thrown out and the
    test will not be executed.
行 2:
  samples
  The optional parameter defines the number of averaged measurements to be performed.
    The valid range of the
    integer parameter is 1 … 128.
    
    The default value is 1.
行 3:
  maxResistance
    
    maxResistancePos
    
    maxResistanceNeg
  The threshold for the pass/fail decision in ohms (Ω).
    
    The programmable range is 0 ... 5000 Ω.
    
    The three parameters are supported only for the `DC Scale XPS256 card`（raw: `350661.htm`）.
    
    According to the selected syntax, the threshold value can be set together for the positive power lines and negative
    power lines or can be set separately for positive and negative power lines.
    
    For the default value if another syntax is selected and no threshold is defined, refer to `XPS256 programming - Kelvin test / sense connection test`（raw: `354645.htm`）.
行 4:
  statusPos
  Integer array that is filled with the results of the Kelvin test on the positive power lines.
    The size of the
    array is defined by the number of defined pins. The first element of the array corresponds to the first pin in
    pinList.
    
    The returned integer values are to be interpreted as follows:
    
    0:
    The Kelvin test has failed on the corresponding pin.
    
    1:
    The Kelvin test has passed on the corresponding pin.
行 5:
  statusNeg
  Integer array that is filled with the results of the Kelvin test on the negative power lines.
    The size of the
    array is defined by the number of defined pins. The first element of the array corresponds to the first pin in
    pinList.
    
    The returned integer values are to be interpreted as follows:
    
    0:
    The Kelvin test has failed on the corresponding pin.
    
    1:
    The Kelvin test has passed on the corresponding pin.

### Return value（取自子主题 HW_STATE.checkKelvinStatus()）

The returned
bool
 value indicates the state of the conversion from the read data to
the data in the arrays:

true
: No error found

false
: Invalid data read

### Example（取自子主题 HW_STATE.checkKelvinStatus()）

The following example performs a sense connection test on three pins "pin1", "pin2", "pin3" in parallel on all active sites. Failing
sites are re-tested in the
`FOR_EACH_SITE`（raw: `116559.htm`）
 block to identify the failing pins and lines. Note that the

FOR_EACH_SITE_BEGIN_WITH_QUERY()
 API must be used to set the query focus within the block.

```
SPMU_TASK spmuTask;
HW_STATE hwState;
ARRAY_I goNogoResult;
ARRAY_I statusPosArray;
ARRAY_I statusNegArray;
STRING pinlist = "pin1, pin2, pin3";

ON_FIRST_INVOCATION_BEGIN();
{
//
// Disconnect the tested pins
//
spmuTask.pin(pinlist).vForce(0.0 V).min(-1.0 A).max(1.0 A).relay("NT");

spmuTask.execMode(TM::FORCE_OFF).execute();

//
// Perform the Kelvin test in parallel on all active sites
//
hwState.checkKelvinStatusParallel(pinlist, goNogoResult);

//
// Evaluate the go/no-go results, re-test failing sites
//
cout << "Parallel Kelvin tests GoNogo results per site:" << endl << endl;

FOR_EACH_SITE_BEGIN_WITH_QUERY();
{
cout << "\tSite " << CURRENT_SITE_NUMBER() << ": ";

if (goNogoResult[CURRENT_SITE_NUMBER() -1] == 1)
{
cout << "PASS" << endl;
}
else
{
cout << "FAIL, serial test on site " << CURRENT_SITE_NUMBER() << endl << endl;

//
// Serial test identifies failing pins
//
hwState.checkKelvinStatus(pinlist, statusPosArray, statusNegArray);

for (int arrayIndex = 0; arrayIndex < statusPosArray.size(); arrayIndex++)
{
cout << "\t\tPin " << arrayIndex + 1
<< ": positive = " << statusPosArray[arrayIndex]
<< ", negative = " << statusNegArray[arrayIndex] << endl;
}

cout << endl;
}
}
FOR_EACH_SITE_END();

cout << endl;
}
ON_FIRST_INVOCATION_END();
```

### Syntax（取自子主题 HW_STATE.checkKelvinStatusParallel()）

```
bool checkKelvinStatusParallel(const STRING pinlist, ARRAY_I &result);
bool checkKelvinStatusParallel(const STRING pinlist, const INT samples, ARRAY_I &result);
```

The following syntax is supported only for the
`DC Scale XPS256 card`（raw: `350661.htm`）
:

```
bool checkKelvinStatusParallel(const STRING pinlist, const INT samples,
const DOUBLE maxResistance, ARRAY_I &result);

bool checkKelvinStatusParallel(const STRING pinlist, const INT samples,
const DOUBLE maxResistancePos, const DOUBLE maxResistanceNeg, ARRAY_I &result);
```

[表] List of parameters
列: Parameter | Description
行 1:
  pinList
  The pins connected to the DUT board that will be queried. The pins are separated with commas. If the
    pinList is empty or an invalid pin is specified, an error message will be thrown out and the
    test will not be executed.
行 2:
  samples
  The optional parameter defines the number of averaged measurements to be performed.
    
    The valid range of the integer parameter is 1 … 128.
    
    The default value is 1.
行 3:
  maxResistance
    
    maxResistancePos
    
    maxResistanceNeg
  The threshold for the pass/fail decision in ohms (Ω).
    
    The programmable range is 0 ... 5000 Ω.
    
    The three parameters are supported only for the `DC Scale XPS256 card`（raw: `350661.htm`）.
    
    According to the selected syntax, the threshold value can be set together for the positive power lines and negative
    power lines or can be set separately for positive and negative power lines.
    
    For the default value if another syntax is selected and no threshold is defined, refer to `XPS256 programming - Kelvin test / sense connection test`（raw: `354645.htm`）.
行 4:
  result
  Integer array that is filled with the go/no-go results of the Kelvin test of all tested sites.
    The size of the array is defined by the
    number of configured sites. The first element of the array corresponds to site 1.
    
    The returned integer
    values are to be interpreted as follows:
    
    -1:
    No test performed: The corresponding site is not active.
    
    0:
    The Kelvin test has failed on the corresponding site.
    
    1:
    The Kelvin test has passed on the corresponding site.

### Return value（取自子主题 HW_STATE.checkKelvinStatusParallel()）

The returned
bool
 value indicates the state of the conversion from the read data to the data in the array:

true
No error found
false
Invalid data read

### Example（取自子主题 HW_STATE.checkKelvinStatusParallel()）

The following example performs a sense connection test on three pins "pin1", "pin2", "pin3" in parallel on all active sites. Failing
sites are re-tested in the
`FOR_EACH_SITE`（raw: `116559.htm`）
 block to identify the failing pins and lines. Note that the

FOR_EACH_SITE_BEGIN_WITH_QUERY()
 API must be used to set the query focus within the block.

```
SPMU_TASK spmuTask;
HW_STATE hwState;
ARRAY_I goNogoResult;
ARRAY_I statusPosArray;
ARRAY_I statusNegArray;
STRING pinlist = "pin1, pin2, pin3";

ON_FIRST_INVOCATION_BEGIN();
{
//
// Disconnect the tested pins
//
spmuTask.pin(pinlist).vForce(0.0 V).min(-1.0 A).max(1.0 A).relay("NT");

spmuTask.execMode(TM::FORCE_OFF).execute();

//
// Perform the Kelvin test in parallel on all active sites
//
hwState.checkKelvinStatusParallel(pinlist, goNogoResult);

//
// Evaluate the go/no-go results, re-test failing sites
//
cout << "Parallel Kelvin tests GoNogo results per site:" << endl << endl;

FOR_EACH_SITE_BEGIN_WITH_QUERY();
{
cout << "\tSite " << CURRENT_SITE_NUMBER() << ": ";

if (goNogoResult[CURRENT_SITE_NUMBER() -1] == 1)
{
cout << "PASS" << endl;
}
else
{
cout << "FAIL, serial test on site " << CURRENT_SITE_NUMBER() << endl << endl;

//
// Serial test identifies failing pins
//
hwState.checkKelvinStatus(pinlist, statusPosArray, statusNegArray);

for (int arrayIndex = 0; arrayIndex < statusPosArray.size(); arrayIndex++)
{
cout << "\t\tPin " << arrayIndex + 1
<< ": positive = " << statusPosArray[arrayIndex]
<< ", negative = " << statusNegArray[arrayIndex] << endl;
}

cout << endl;
}
}
FOR_EACH_SITE_END();

cout << endl;
}
ON_FIRST_INVOCATION_END();
```

### Syntax（取自子主题 HW_STATE.checkGangConnection()）

```
bool checkGangConnection (const STRING& pinList, ARRAY_I &result);
bool checkGangConnection (const STRING& pinlist, const INT samples, ARRAY_I &result);
bool checkGangConnection (const STRING pinlist, const INT samples, const DOUBLE maxResistance, ARRAY_I &result);
```

[表] Parameters
列: Parameter | Description/Range
行 1:
  pinList
  The pins connected to the DUT board that will be queried. The pins are separated with commas. If the
    pinList is empty or an invalid pin is specified, an error message will be thrown out and the
    test will not be executed.
行 2:
  samples
  The optional parameter defines the number of averaged measurements to be performed.
    The valid range of the
    integer parameter is 1 … 128.
    
    The default value is 1.
行 3:
  maxResistance
  The optional threshold for the pass/fail decision in ohms (Ω).
    
    The programmable range is 0 ... 100 Ω.
    
    The default value if another syntax is selected and no threshold is defined is 20 Ω.
行 4:
  result
  Integer array that is filled with the results of the gang connection test.
    The size of the array is defined by the number of defined
    pins. The first element of the array corresponds to the first pin in pinList.
    
    The
    returned integer values are to be interpreted as follows:
    
    0:
    The gang connection test has failed on the corresponding pin.
    
    1:
    The gang connection test has passed on the corresponding pin.

### Return value（取自子主题 HW_STATE.checkGangConnection()）

The returned
bool
 value indicates the state of the conversion from the read data to
the data in the arrays:

true
: No error found

false
: Invalid data read

### Example（取自子主题 HW_STATE.checkGangConnection()）

The following example performs a gang connection test on three pins "pin1", "pin2", "pin3". The test is implemented into the
`ON_FIRST_INVOCATION`（raw: `29526.htm`）
 block but a
`FOR_EACH_SITE`（raw: `116559.htm`）
 block is used for the serial
sense connection test. Note that the
FOR_EACH_SITE_BEGIN_WITH_QUERY()
 API must be used to set the query focus
within the block.

```
SPMU_TASK spmuTask;
HW_STATE hwState;
STRING pinlist = "pin1, pin2, pin3";
int samples = 10;
double maxResistance = 30.0 Ohm;
ARRAY_I goNogoResult;
ARRAY_I perPinResult;

ON_FIRST_INVOCATION_BEGIN();
{
//
// Disconnect the tested pins
//
spmuTask.pin(pinlist).vForce(0.0 V).min(-1.0 A).max(1.0 A).relay("NT");

spmuTask.execMode(TM::FORCE_OFF).execute();

//
// Perform the gang connection test in parallel on all active sites
//
ARRAY_I goNogoResult;

hwState.checkGangConnectionParallel(pinlist, samples, maxResistance, goNogoResult);

//
// Evaluate the go/no-go results, re-test failing sites
//
cout << "Parallel gang connection test GoNogo results per site:" << endl << endl;

FOR_EACH_SITE_BEGIN_WITH_QUERY();
{
cout << "\tSite " << CURRENT_SITE_NUMBER() << ": ";

if (goNogoResult[CURRENT_SITE_NUMBER() -1] == 1)
{
cout << "PASS" << endl;
}
else
{
cout << "FAIL, serial test on site " << CURRENT_SITE_NUMBER() << endl << endl;

//
// Serial test identifies failing pins
//
hwState.checkGangConnection(pinlist, samples, maxResistance, perPinResult);

for (int arrayIndex = 0; arrayIndex < perPinResult.size(); arrayIndex++)
{
cout << "\t\tPin " << arrayIndex + 1 << " = " << perPinResult[arrayIndex] << endl;
}

cout << endl;
}
}
FOR_EACH_SITE_END();

cout << endl;
}
ON_FIRST_INVOCATION_END();
```

### Syntax（取自子主题 HW_STATE.checkGangConnectionParallel()）

```
bool checkGangConnectionParallel (const STRING& pinList, ARRAY_I &result);
bool checkGangConnectionParallel (const STRING& pinlist, const INT samples, ARRAY_I &result);
bool checkGangConnectionParallel (const STRING pinlist, const INT samples, const DOUBLE maxResistance, ARRAY_I &result);
```

[表] List of parameters
列: Parameter | Description
行 1:
  pinList
  The pins connected to the DUT board that will be queried. The pins are separated with commas. If the
    pinList is empty or an invalid pin is specified, an error message will be thrown out and the
    test will not be executed.
行 2:
  samples
  The optional parameter defines the number of averaged measurements to be performed.
    
    The valid range of the integer parameter is 1 … 128.
    
    The default value is 1.
行 3:
  maxResistance
  The optional threshold for the pass/fail decision in ohms (Ω).
    
    The programmable range is 0 ... 100 Ω.
    
    The default value if another syntax is selected and no threshold is defined is 20 Ω.
行 4:
  result
  Integer array that is filled with the go/no-go results of the gang connection test of all tested sites.
    The size of the array is
    defined by the number of configured sites. The first element of the array corresponds to site 1.
    
    The
    returned integer values are to be interpreted as follows:
    
    -1:
    No test performed: The corresponding site is not active.
    
    0:
    The Kelvin test has failed on the corresponding site.
    
    1:
    The Kelvin test has passed on the corresponding site.

### Return value（取自子主题 HW_STATE.checkGangConnectionParallel()）

The returned
bool
 value indicates the state of the conversion from the read data to the data in the array:

true
No error found
false
Invalid data read

### Example（取自子主题 HW_STATE.checkGangConnectionParallel()）

The following example performs a gang connection test on three pins "pin1", "pin2", "pin3". The test is implemented into the
`ON_FIRST_INVOCATION`（raw: `29526.htm`）
 block but a
`FOR_EACH_SITE`（raw: `116559.htm`）
 block is used for the serial
sense connection test. Note that the
FOR_EACH_SITE_BEGIN_WITH_QUERY()
 API must be used to set the query focus
within the block.

```
SPMU_TASK spmuTask;
HW_STATE hwState;
STRING pinlist = "pin1, pin2, pin3";
int samples = 10;
double maxResistance = 30.0 Ohm;
ARRAY_I goNogoResult;
ARRAY_I perPinResult;

ON_FIRST_INVOCATION_BEGIN();
{
//
// Disconnect the tested pins
//
spmuTask.pin(pinlist).vForce(0.0 V).min(-1.0 A).max(1.0 A).relay("NT");

spmuTask.execMode(TM::FORCE_OFF).execute();

//
// Perform the gang connection test in parallel on all active sites
//
ARRAY_I goNogoResult;

hwState.checkGangConnectionParallel(pinlist, samples, maxResistance, goNogoResult);

//
// Evaluate the go/no-go results, re-test failing sites
//
cout << "Parallel gang connection test GoNogo results per site:" << endl << endl;

FOR_EACH_SITE_BEGIN_WITH_QUERY();
{
cout << "\tSite " << CURRENT_SITE_NUMBER() << ": ";

if (goNogoResult[CURRENT_SITE_NUMBER() -1] == 1)
{
cout << "PASS" << endl;
}
else
{
cout << "FAIL, serial test on site " << CURRENT_SITE_NUMBER() << endl << endl;

//
// Serial test identifies failing pins
//
hwState.checkGangConnection(pinlist, samples, maxResistance, perPinResult);

for (int arrayIndex = 0; arrayIndex < perPinResult.size(); arrayIndex++)
{
cout << "\t\tPin " << arrayIndex + 1 << " = " << perPinResult[arrayIndex] << endl;
}

cout << endl;
}
}
FOR_EACH_SITE_END();

cout << endl;
}
ON_FIRST_INVOCATION_END();
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
