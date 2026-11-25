---
type: object
title: HW_PIN_STATE
layer: L2
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.117.01_HW_PIN_STATE.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# HW_PIN_STATE

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **17,096 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.117.01_HW_PIN_STATE.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Class definition

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

### Member functions returning DOUBLE

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

### Member functions returning INT

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

### Member functions returning STRING

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

### Example

For an example, refer to

`Example 1: Query the status outside the ON_FIRST_INVOVATION block`（raw: `105633.htm#_105633__ex_Example_ON_FIRST_INVOCATION`）
 and

`Example 2: Query the status in a FOR_EACH_SITE...WITH_QUERY block`（raw: `105633.htm#_105633__ex_Example_FOR_EACH_SITE`）

in
`HW_STATE`（raw: `105633.htm`）
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
