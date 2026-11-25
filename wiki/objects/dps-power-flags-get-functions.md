---
type: object
title: DPS power flags - get...() functions
layer: L3
stage: run
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06_DPS_power_flags_-_get...___functions.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# DPS power flags - get...() functions

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **30,660 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06_DPS_power_flags_-_get...___functions.htm>` 及其子主题 `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.01.02_DPS_AUX_PIN_TASK.checkPowerFlags.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06.01_DPS_AUX_TASK.getAllStatus.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06.02_DPS_AUX_TASK.getStatusWithoutConstCur.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06.03_DPS_AUX_TASK.getStatusWithoutConstVol.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06.04_DPS_AUX_TASK.getClampDistanceTooLow.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06.05_DPS_AUX_TASK.getConstantCurrent.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06.06_DPS_AUX_TASK.getConstantCurrentLimitDisconnect.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06.07_DPS_AUX_TASK.getConstantVoltage.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06.08_DPS_AUX_TASK.getCurrentLimiterProtectionDetected.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06.09_DPS_AUX_TASK.getDutBoardDisconnect.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06.10_DPS_AUX_TASK.getLowHeadroom.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06.11_DPS_AUX_TASK.getOvercurrent.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06.12_DPS_AUX_TASK.getOvertemperature.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06.13_DPS_AUX_TASK.getOvervoltage.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06.14_DPS_AUX_TASK.getRangeOverflow.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06.15_DPS_AUX_TASK.getSafetyLine.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06.16_DPS_AUX_TASK.getUnregulated.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06.17_DPS_AUX_TASK.getVoltageDropForce.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06.18_DPS_AUX_TASK.getVoltageDropForceWarn.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06.19_DPS_AUX_TASK.getVoltageDropReturn.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.43.06.20_DPS_AUX_TASK.getVoltageDropReturnWarn.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Member functions

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
