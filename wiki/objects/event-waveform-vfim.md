---
type: object
title: EVENT_WAVEFORM_VFIM
layer: L3
stage: testmethod
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.38_EVENT_WAVEFORM_VFIM.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# EVENT_WAVEFORM_VFIM

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **13,935 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.38_EVENT_WAVEFORM_VFIM.htm>` 及其子主题 `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.38.01_EVENT_WAVEFORM_VFIM.vForce.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.38.02_EVENT_WAVEFORM_VFIM.getVForce.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.38.03_EVENT_WAVEFORM_VFIM.sampleVectorDistance.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.38.04_EVENT_WAVEFORM_VFIM.getSampleVectorDistance.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.38.05_EVENT_WAVEFORM_VFIM.getSamples.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.38.06_EVENT_WAVEFORM_VFIM.averages.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.38.07_EVENT_WAVEFORM_VFIM.getAverages.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.38.08_EVENT_WAVEFORM_VFIM.clampChecks.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.38.09_EVENT_WAVEFORM_VFIM.getClampChecks.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.38.10_EVENT_WAVEFORM_VFIM.iClampChecks.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.38.11_EVENT_WAVEFORM_VFIM.getIClampChecks.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.38.12_EVENT_WAVEFORM_VFIM.outOfRangeCheck.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.38.13_EVENT_WAVEFORM_VFIM.getOutOfRangeCheck.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.38.14_EVENT_WAVEFORM_VFIM.getRepeatCount.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.39.01_EVENT_WAVEFORM_VFVM.vForce.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.39.02_EVENT_WAVEFORM_VFIM.getVForce.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.39.03_EVENT_WAVEFORM_VFVM.sampleVectorDistance.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.39.04_EVENT_WAVEFORM_VFVM.getSampleVectorDistance.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.39.05_EVENT_WAVEFORM_VFVM.getSamples.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.39.06_EVENT_WAVEFORM_VFVM.averages.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.39.07_EVENT_WAVEFORM_VFVM.getAverages.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.39.08_EVENT_WAVEFORM_VFVM.vForceCheckLow.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.39.09_EVENT_WAVEFORM_VFVM.vForceCheckHigh.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.39.10_EVENT_WAVEFORM_VFVM.getVForceCheckLow.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.39.11_EVENT_WAVEFORM_VFVM.getVForceCheckHigh.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.39.12_EVENT_WAVEFORM_VFVM.clearVForceCheck.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.39.13_EVENT_WAVEFORM_VFVM.clampChecks.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.39.14_EVENT_WAVEFORM_VFVM.getClampChecks.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.39.15_EVENT_WAVEFORM_VFVM.iClampChecks.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.39.16_EVENT_WAVEFORM_VFVM.getIClampChecks.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.39.17_EVENT_WAVEFORM_VFVM.outOfRangeCheck.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.39.18_EVENT_WAVEFORM_VFVM.getOutOfRangeCheck.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.39.19_EVENT_WAVEFORM_VFVM.getRepeatCount.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.39_EVENT_WAVEFORM_VFVM.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
class EVENT_WAVEFORM_VFIM : public EVENT_BASE

EVENT_WAVEFORM_VFIM(const STRING & id);
EVENT_WAVEFORM_VFIM( INT id);
EVENT_WAVEFORM_VFIM();
```

This constructs an object of the EVENT_WAVEFORM_VFIM class. The class derives from the
`EVENT_BASE`（raw: `116893.htm`）
 class.

When using the EVENT_WAVEFORM_VFIM() constructor, the event ID
is implicitly derived from the name of the assigned ANALOG_WAVEFORM. The event ID will look
like:
WAV_waveformName

[表] Parameter
列: Parameter | Description
行 1:
  id
  Identifier of the event.
    
    The identifier may be defined as integer value or as string.

### Example

Describes the waveform of a voltage
ramp:

```
ANALOG_WAVEFORM rampUp("rampUp");

rampUp.definition(TM::RAMP)
.direction(TM::POS)
.samples(4)
.min(0.1).max(1.6);
```

Defines a force voltage ramp
waveform:

```
EVENT_WAVEFORM_VF rampUpEvent;
rampUpEvent.vForce(rampUp);
rampUpEvent.sampleVectorDistance(64);
```

### Syntax（取自子主题 EVENT_WAVEFORM_VFIM.vForce()）

```
EVENT_WAVEFORM_VFIM & vForce(const ANALOG_WAVEFORM & waveform);
```
[表] Parameter
列: Parameter | Description
行 1:
  waveform
  Waveform definition object

Return value

There is no return value.

### Example（取自子主题 EVENT_WAVEFORM_VFIM.vForce()）

For an example see
`EVENT_WAVEFORM_VFIM`（raw: `116927.htm`）
.

### Syntax（取自子主题 EVENT_WAVEFORM_VFIM.getVForce()）

```
void getVForce(ARRAY_D & waveform) const;
```
[表] Parameter
列: Parameter | Description
行 1:
  waveform
  Waveform definition object

Return value

There is no return value.

### Example（取自子主题 EVENT_WAVEFORM_VFIM.getVForce()）

For an example see
`EVENT_WAVEFORM_VFIM`（raw: `116927.htm`）
.

### Syntax（取自子主题 EVENT_WAVEFORM_VFIM.sampleVectorDistance()）

```
EVENT_WAVEFORM_VFIM & sampleVectorDistance(INT vectors);
```
[表] Parameter
列: Parameter | Description
行 1:
  vectors
  Number of vectors defining the distance. Minimum is 32 vectors.

### Return value（取自子主题 EVENT_WAVEFORM_VFIM.sampleVectorDistance()）

A reference to the corresponding
`EVENT_WAVEFORM_VFIM`（raw: `116927.htm`）

object.

### Example（取自子主题 EVENT_WAVEFORM_VFIM.sampleVectorDistance()）

For an example see
`EVENT_WAVEFORM_VFIM`（raw: `116927.htm`）
.

### Syntax（取自子主题 EVENT_WAVEFORM_VFIM.getSampleVectorDistance()）

```
void getSampleVectorDistance(INT & vectors) const;
```
[表] Parameter
列: Parameter | Description
行 1:
  vectors
  Number of vectors defining the distance. Minimum is 32 vectors.

### Return value（取自子主题 EVENT_WAVEFORM_VFIM.getSampleVectorDistance()）

The sample vector distance as an INT.

### Example（取自子主题 EVENT_WAVEFORM_VFIM.getSampleVectorDistance()）

For an example see
`EVENT_WAVEFORM_VFIM`（raw: `116927.htm`）
.

### Syntax（取自子主题 EVENT_WAVEFORM_VFIM.getSamples()）

```
void getSamples(INT & samples) const;
```
[表] Parameter
列: Parameter | Description
行 1:
  samples
  Number of samples

### Return value（取自子主题 EVENT_WAVEFORM_VFIM.getSamples()）

The number of samples of the waveform.

### Example（取自子主题 EVENT_WAVEFORM_VFIM.getSamples()）

For an example see
`EVENT_WAVEFORM_VFIM`（raw: `116927.htm`）
.

### Syntax（取自子主题 EVENT_WAVEFORM_VFIM.averages()）

```
EVENT_WAVEFORM_VFIM & averages(const EVENT_VALUE_INT & samples);
```
[表] Parameter
列: Parameter | Description
行 1:
  samples
  Number of internal samples from which the average is created.
    
    For DC Scale channels, with exception of XPS256,
    the number of samples must be a power of 2.

Return value

There is no return value.

### Example（取自子主题 EVENT_WAVEFORM_VFIM.averages()）

For an example see
`EVENT_WAVEFORM_VFIM`（raw: `116927.htm`）
.

### Syntax（取自子主题 EVENT_WAVEFORM_VFIM.getAverages()）

```
void getAverages(EVENT_VALUE_INT & samples) const;
```
[表] Parameter
列: Parameter | Description
行 1:
  samples
  Number of internal samples from which the average is
    created.

### Return value（取自子主题 EVENT_WAVEFORM_VFIM.getAverages()）

Returns EVENT_VALUE_INT as reference.

### Example（取自子主题 EVENT_WAVEFORM_VFIM.getAverages()）

For an example see
`EVENT_WAVEFORM_VFIM`（raw: `116927.htm`）
.

### Syntax（取自子主题 EVENT_WAVEFORM_VFIM.clampChecks()）

```
EVENT_WAVEFORM_VFIM & clampChecks(bool failOnLow = true, bool failOnHigh = true);
```
[表] Parameters
列: Parameter | Description
行 1:
  failOnLow
  Enables or disables the lower clamp check.
    
    true: The lower clamp check is enabled.
    
    false: The lower clamp check is disabled.
    
    Default value: The clamp check is disabled.
行 2:
  failOnHigh
  Enables or disables the upper clamp check.
    
    true: The upper clamp check is enabled.
    
    false: The upper clamp check is disabled.
    
    Default value: The clamp check is disabled.

### Return value（取自子主题 EVENT_WAVEFORM_VFIM.clampChecks()）

A reference to the corresponding
`EVENT_WAVEFORM_VFIM`（raw: `116927.htm`）

object.

### Example（取自子主题 EVENT_WAVEFORM_VFIM.clampChecks()）

For an example, see
`EVENT_WAVEFORM_VFIM`（raw: `116927.htm`）
.

### Syntax（取自子主题 EVENT_WAVEFORM_VFIM.getClampChecks()）

```
void getClampChecks(bool & failOnLow, bool & failOnHigh) const;
```
[表] Parameters
列: Parameter | Description
行 1:
  failOnLow
  The programmed value of the lower clamp check.
    
    true: The lower clamp check is enabled.
    
    false: The lower clamp check is disabled.
行 2:
  failOnHigh
  The programmed value of the upper clamp check.
    
    true: The upper clamp check is enabled.
    
    false: The upper clamp check is disabled.

Return value

There is no return value.

### Example（取自子主题 EVENT_WAVEFORM_VFIM.getClampChecks()）

For an example, see
`EVENT_WAVEFORM_VFIM`（raw: `116927.htm`）
.

### Syntax（取自子主题 EVENT_WAVEFORM_VFIM.iClampChecks()）

```
EVENT_WAVEFORM_VFIM & iClampChecks(bool failOnLow = true, bool failOnHigh = true);
```
[表] Parameters
列: Parameter | Description
行 1:
  failOnLow
  Enables or disables the lower clamp check.
    
    true: The lower clamp check is enabled.
    
    false: The lower clamp check is disabled.
    
    Default value: The clamp check is disabled.
行 2:
  failOnHigh
  Enables or disables the upper clamp check.
    
    true: The upper clamp check is enabled.
    
    false: The upper clamp check is disabled.
    
    Default value: The clamp check is disabled.

### Return value（取自子主题 EVENT_WAVEFORM_VFIM.iClampChecks()）

A reference to the corresponding
`EVENT_WAVEFORM_VFIM`（raw: `116927.htm`）

object.

### Example（取自子主题 EVENT_WAVEFORM_VFIM.iClampChecks()）

For an example, see
`EVENT_WAVEFORM_VFIM`（raw: `116927.htm`）
.

### Syntax（取自子主题 EVENT_WAVEFORM_VFIM.getIClampChecks()）

```
void getIClampChecks(bool & failOnLow, bool & failOnHigh) const;
```
[表] Parameters
列: Parameter | Description
行 1:
  failOnLow
  The programmed value of the lower clamp check.
    
    true: The lower clamp check is enabled.
    
    false: The lower clamp check is disabled.
行 2:
  failOnHigh
  The programmed value of the upper clamp check.
    
    true: The upper clamp check is enabled.
    
    false: The upper clamp check is disabled.

Return value

There is no return value.

### Example（取自子主题 EVENT_WAVEFORM_VFIM.getIClampChecks()）

For an example, see
`EVENT_WAVEFORM_VFIM`（raw: `116927.htm`）
.

### Syntax（取自子主题 EVENT_WAVEFORM_VFIM.outOfRangeCheck()）

```
EVENT_WAVEFORM_VFIM & outOfRangeCheck(bool failOnOutOfRange = true);
```
[表] Parameter
列: Parameter | Description
行 1:
  failOnOutOfRange
  Possible values are: true | false

Return value

There is no return value.

### Example（取自子主题 EVENT_WAVEFORM_VFIM.outOfRangeCheck()）

For an example see
`EVENT_WAVEFORM_VFIM`（raw: `116927.htm`）
.

### Syntax（取自子主题 EVENT_WAVEFORM_VFIM.getOutOfRangeCheck()）

```
void getOutOfRangeCheck(bool & failOnOutOfRange) const;
```
[表] Parameter
列: Parameter | Description
行 1:
  failOnOutOfRange
  Possible values are: true | false

### Return value（取自子主题 EVENT_WAVEFORM_VFIM.getOutOfRangeCheck()）

The setting of the
failOnOutOfRange

parameter.

### Example（取自子主题 EVENT_WAVEFORM_VFIM.getOutOfRangeCheck()）

For an example see
`EVENT_WAVEFORM_VFIM`（raw: `116927.htm`）
.

### Syntax（取自子主题 EVENT_WAVEFORM_VFIM.getRepeatCount()）

```
EVENT_WAVEFORM_VFIM & getRepeatCount(INT & repeats) const;
void getRepeatCount (INT & repeats) const;
```
[表] Parameter
列: Parameter | Description
行 1:
  repeats
  The number of times the waveform is repeated.
    
    Note: The getRepeatCount() member function of DC events returns always 1 as repeat
    count.

### Return value（取自子主题 EVENT_WAVEFORM_VFIM.getRepeatCount()）

Number of repeats of the waveform.

### Example（取自子主题 EVENT_WAVEFORM_VFIM.getRepeatCount()）

For an example see
`EVENT_WAVEFORM_VFIM`（raw: `116927.htm`）
.

### Syntax（取自子主题 EVENT_WAVEFORM_VFVM）

```
class EVENT_WAVEFORM_VFVM : public EVENT_BASE

EVENT_WAVEFORM_VFVM(const STRING & id);
EVENT_WAVEFORM_VFVM( INT id);
EVENT_WAVEFORM_VFVM();
```

This
constructs an object of the EVENT_WAVEFORM_VFVM class. The class derives from the
`EVENT_BASE`（raw: `116893.htm`）
 class.

When using the EVENT_WAVEFORM_VFVM() constructor, the event ID
is implicitly derived from the name of the assigned ANALOG_WAVEFORM. The event ID will look
like:
WAV_waveformName

[表] Parameter
列: Parameter | Description
行 1:
  id
  Identifier of the event.
    
    The identifier may be defined as integer value or as string.

### Example（取自子主题 EVENT_WAVEFORM_VFVM）

Describes the waveform of a voltage
ramp:

```
ANALOG_WAVEFORM rampUp("rampUp");

rampUp.definition(TM::RAMP)
.direction(TM::POS)
.samples(4)
.min(0.1).max(1.6);
```

Defines a force voltage ramp
waveform:

```
EVENT_WAVEFORM_VF rampUpEvent("ramp_0.1V_1.6V");
rampUpEvent.vForce(rampUp);
rampUpEvent.sampleVectorDistance(64);
```

Requests validation of reached force voltage for each step. The allowed low voltage
deviation is -10 mV. The upper value is not
checked.

```
rampUpEvent.vForceCheckLow(-10 mV);
rampUpEvent.iClampChecks(false, true);
```

### Syntax（取自子主题 EVENT_WAVEFORM_VFVM.vForce()）

```
EVENT_WAVEFORM_VFIM & vForce(const ANALOG_WAVEFORM & waveform);
```
[表] Parameter
列: Parameter | Description
行 1:
  waveform
  Waveform definition object

Return value

There is no return value.

### Example（取自子主题 EVENT_WAVEFORM_VFVM.vForce()）

For an example see
`EVENT_WAVEFORM_VFVM`（raw: `116926.htm`）
.

### Syntax（取自子主题 EVENT_WAVEFORM_VFIM.getVForce()）

```
void getVForce(ARRAY_D & waveform) const;
```
[表] Parameter
列: Parameter | Description
行 1:
  waveform
  Waveform definition object

Return value

There is no return value.

### Example（取自子主题 EVENT_WAVEFORM_VFIM.getVForce()）

For an example see
`EVENT_WAVEFORM_VFIM`（raw: `116927.htm`）
.

### Syntax（取自子主题 EVENT_WAVEFORM_VFVM.sampleVectorDistance()）

```
EVENT_WAVEFORM_VFIM & sampleVectorDistance(INT vectors);
```
[表] Parameter
列: Parameter | Description
行 1:
  vectors
  Number of vectors defining the distance. Minimum is 32 vectors.

### Return value（取自子主题 EVENT_WAVEFORM_VFVM.sampleVectorDistance()）

A reference to the corresponding
`EVENT_WAVEFORM_VFVM`（raw: `116926.htm`）

object.

### Example（取自子主题 EVENT_WAVEFORM_VFVM.sampleVectorDistance()）

For an example see
`EVENT_WAVEFORM_VFVM`（raw: `116926.htm`）
.

### Syntax（取自子主题 EVENT_WAVEFORM_VFVM.getSampleVectorDistance()）

```
void getSampleVectorDistance(INT & vectors) const;
```
[表] Parameter
列: Parameter | Description
行 1:
  vectors
  Number of vectors defining the distance. Minimum is 32 vectors.

Return value

There is no return value.

### Example（取自子主题 EVENT_WAVEFORM_VFVM.getSampleVectorDistance()）

For an example see
`EVENT_WAVEFORM_VFVM`（raw: `116926.htm`）
.

### Syntax（取自子主题 EVENT_WAVEFORM_VFVM.getSamples()）

```
void getSamples(INT & samples) const;
```
[表] Parameter
列: Parameter | Description
行 1:
  samples
  Number of samples

Return value

There is no return value.

### Example（取自子主题 EVENT_WAVEFORM_VFVM.getSamples()）

For an example see
`EVENT_WAVEFORM_VFVM`（raw: `116926.htm`）
.

### Syntax（取自子主题 EVENT_WAVEFORM_VFVM.averages()）

```
EVENT_WAVEFORM_VFVM & averages(const EVENT_VALUE_INT & samples);
```
[表] Parameter
列: Parameter | Description
行 1:
  samples
  Number of internal samples from which the average is created.
    
    For DC Scale channels, with exception of XPS256,
    the number of samples must be a power of 2.

Return value

There is no return value.

### Example（取自子主题 EVENT_WAVEFORM_VFVM.averages()）

For an example see
`EVENT_WAVEFORM_VFVM`（raw: `116926.htm`）
.

### Syntax（取自子主题 EVENT_WAVEFORM_VFVM.getAverages()）

```
void getAverages(EVENT_VALUE_INT & samples) const;
```
[表] Parameter
列: Parameter | Description
行 1:
  samples
  Number of internal samples from which the average is
    created.

### Return value（取自子主题 EVENT_WAVEFORM_VFVM.getAverages()）

Returns EVENT_VALUE_INT as reference.

### Example（取自子主题 EVENT_WAVEFORM_VFVM.getAverages()）

For an example see
`EVENT_WAVEFORM_VFVM`（raw: `116926.htm`）
.

### Syntax（取自子主题 EVENT_WAVEFORM_VFVM.vForceCheckLow()）

```
EVENT_WAVEFORM_VFVM & vForceCheckLow (DOUBLE lowOffset);
```
[表] Parameter
列: Parameter | Description
行 1:
  lowOffset
  Voltage value defining the offset

Return value

There is no return value.

### Example（取自子主题 EVENT_WAVEFORM_VFVM.vForceCheckLow()）

For an example see
`EVENT_WAVEFORM_VFVM`（raw: `116926.htm`）
.

### Syntax（取自子主题 EVENT_WAVEFORM_VFVM.vForceCheckHigh()）

```
EVENT_WAVEFORM_VFVM & vForceCheckHigh(DOUBLE highOffset);
```
[表] Parameter
列: Parameter | Description
行 1:
  highOffset
  Voltage value defining the offset

Return value

There is no return value.

### Example（取自子主题 EVENT_WAVEFORM_VFVM.vForceCheckHigh()）

For an example see
`EVENT_WAVEFORM_VFVM`（raw: `116926.htm`）
.

### Syntax（取自子主题 EVENT_WAVEFORM_VFVM.getVForceCheckLow()）

```
bool getVForceCheckLow (DOUBLE & lowOffset) const;
```
[表] Parameter
列: Parameter | Description
行 1:
  lowOffset
  Voltage value defining the offset

### Return value（取自子主题 EVENT_WAVEFORM_VFVM.getVForceCheckLow()）

The value of the forced voltage.

### Example（取自子主题 EVENT_WAVEFORM_VFVM.getVForceCheckLow()）

For an example see
`EVENT_WAVEFORM_VFVM`（raw: `116926.htm`）
.

### Syntax（取自子主题 EVENT_WAVEFORM_VFVM.getVForceCheckHigh()）

```
bool getVForceCheckHigh(DOUBLE & highOffset) const;
```
[表] Parameter
列: Parameter | Description
行 1:
  highOffset
  Voltage value defining the offset

### Return value（取自子主题 EVENT_WAVEFORM_VFVM.getVForceCheckHigh()）

The value of the forced voltage.

### Example（取自子主题 EVENT_WAVEFORM_VFVM.getVForceCheckHigh()）

For an example see
`EVENT_WAVEFORM_VFVM`（raw: `116926.htm`）
.

### Syntax（取自子主题 EVENT_WAVEFORM_VFVM.clearVForceCheck()）

```
void clearVForceCheck();
```

List of parameters

There are no parameters.

Return value

There is no return value.

### Example（取自子主题 EVENT_WAVEFORM_VFVM.clearVForceCheck()）

For an example see
`EVENT_WAVEFORM_VFVM`（raw: `116926.htm`）
.

### Syntax（取自子主题 EVENT_WAVEFORM_VFVM.clampChecks()）

```
EVENT_WAVEFORM_VFVM & clampChecks(bool failOnLow = true, bool failOnHigh = true);
```
[表] Parameters
列: Parameter | Description
行 1:
  failOnLow
  Enables or disables the lower clamp check.
    
    true: The lower clamp check is enabled.
    
    false: The lower clamp check is disabled.
    
    Default value: The clamp check is disabled.
行 2:
  failOnHigh
  Enables or disables the upper clamp check.
    
    true: The upper clamp check is enabled.
    
    false: The upper clamp check is disabled.
    
    Default value: The clamp check is disabled.

### Return value（取自子主题 EVENT_WAVEFORM_VFVM.clampChecks()）

A reference to the corresponding
`EVENT_WAVEFORM_VFVM`（raw: `116926.htm`）

object.

### Example（取自子主题 EVENT_WAVEFORM_VFVM.clampChecks()）

For an example, see
`EVENT_WAVEFORM_VFVM`（raw: `116926.htm`）
.

### Syntax（取自子主题 EVENT_WAVEFORM_VFVM.getClampChecks()）

```
void getClampChecks(bool & failOnLow, bool & failOnHigh) const;
```
[表] Parameter
列: Parameter | Description
行 1:
  failOnLow
  The programmed value of the lower clamp check.
    
    true: The lower clamp check is enabled.
    
    false: The lower clamp check is disabled.
行 2:
  failOnHigh
  The programmed value of the upper clamp check.
    
    true: The upper clamp check is enabled.
    
    false: The upper clamp check is disabled.

Return value

There is no return value.

### Example（取自子主题 EVENT_WAVEFORM_VFVM.getClampChecks()）

For an example, see
`EVENT_WAVEFORM_VFVM`（raw: `116926.htm`）
.

### Syntax（取自子主题 EVENT_WAVEFORM_VFVM.iClampChecks()）

```
EVENT_WAVEFORM_VFVM & iClampChecks(bool failOnLow = true, bool failOnHigh = true);
```
[表] Parameters
列: Parameter | Description
行 1:
  failOnLow
  Enables or disables the lower clamp check.
    
    true: The lower clamp check is enabled.
    
    false: The lower clamp check is disabled.
    
    Default value: The clamp check is disabled.
行 2:
  failOnHigh
  Enables or disables the upper clamp check.
    
    true: The upper clamp check is enabled.
    
    false: The upper clamp check is disabled.
    
    Default value: The clamp check is disabled.

### Return value（取自子主题 EVENT_WAVEFORM_VFVM.iClampChecks()）

A reference to the corresponding
`EVENT_WAVEFORM_VFVM`（raw: `116926.htm`）

object.

### Example（取自子主题 EVENT_WAVEFORM_VFVM.iClampChecks()）

For an example, see
`EVENT_WAVEFORM_VFVM`（raw: `116926.htm`）
.

### Syntax（取自子主题 EVENT_WAVEFORM_VFVM.getIClampChecks()）

```
void getIClampChecks(bool & failOnLow, bool & failOnHigh) const;
```
[表] Parameters
列: Parameter | Description
行 1:
  failOnLow
  The programmed value of the lower clamp check.
    
    true: The lower clamp check is enabled.
    
    false: The lower clamp check is disabled.
行 2:
  failOnHigh
  The programmed value of the upper clamp check.
    
    true: The upper clamp check is enabled.
    
    false: The upper clamp check is disabled.

Return value

There is no return value.

### Example（取自子主题 EVENT_WAVEFORM_VFVM.getIClampChecks()）

For an example, see
`EVENT_WAVEFORM_VFVM`（raw: `116926.htm`）
.

### Syntax（取自子主题 EVENT_WAVEFORM_VFVM.outOfRangeCheck()）

```
EVENT_WAVEFORM_VFVM & outOfRangeCheck(bool failOnOutOfRange = true);
```
[表] Parameter
列: Parameter | Description
行 1:
  failOnOutOfRange
  Possible values are: true | false

Return value

There is no return value.

### Example（取自子主题 EVENT_WAVEFORM_VFVM.outOfRangeCheck()）

For an example see
`EVENT_WAVEFORM_VFVM`（raw: `116926.htm`）
.

### Syntax（取自子主题 EVENT_WAVEFORM_VFVM.getOutOfRangeCheck()）

```
void getOutOfRangeCheck(bool & failOnOutOfRange) const;
```
[表] Parameter
列: Parameter | Description
行 1:
  failOnOutOfRange
  Possible values are: true | false

### Return value（取自子主题 EVENT_WAVEFORM_VFVM.getOutOfRangeCheck()）

The setting of the
failOnOutOfRange

parameter.

### Example（取自子主题 EVENT_WAVEFORM_VFVM.getOutOfRangeCheck()）

For an example see
`EVENT_WAVEFORM_VFVM`（raw: `116926.htm`）
.

### Syntax（取自子主题 EVENT_WAVEFORM_VFVM.getRepeatCount()）

```
EVENT_WAVEFORM_VFVM & getRepeatCount(INT & repeats) const;
void getRepeatCount (INT & repeats) const;
```
[表] Parameter
列: Parameter | Description
行 1:
  repeats
  The number of times the waveform is repeated.
    
    Note: The getRepeatCount() member function of DC events returns always 1 as repeat
    count.

### Return value（取自子主题 EVENT_WAVEFORM_VFVM.getRepeatCount()）

Number of repeats of the waveform.

### Example（取自子主题 EVENT_WAVEFORM_VFVM.getRepeatCount()）

For an example see
`EVENT_WAVEFORM_VFVM`（raw: `116926.htm`）
.

<!-- 语法节 end -->

## 是什么

**文档事实** EVENT_WAVEFORM_VFIM 是组合式 force/measure waveform 类，名称含义为 Voltage Force / Current Measure Waveform；它继承 EVENT_BASE，用于定义产生波形的事件，并在采样加到 frontend 的同一时间点进行测量。

**文档事实** 文档把 EVENT_WAVEFORM_VFIM 与 EVENT_WAVEFORM_VFVM 并列为 specialized force/measure waveform classes，后者是 Voltage Force / Voltage Measure Waveform。

**文档事实** API 定义在 /opt/hp93000/soc/prod_com/include/MAPI/Events.h。

**文档事实** 构造函数可接受字符串 id 或整数 id；使用无参构造函数时，事件 ID 由所赋 ANALOG_WAVEFORM 的名称隐式派生，形如 WAV_waveformName。

**文档事实** 文档为该类提供的成员包括 vForce 与 getVForce、sampleVectorDistance 与 getSampleVectorDistance、getSamples、averages 与 getAverages、clampChecks 与 getClampChecks、iClampChecks 与 getIClampChecks、outOfRangeCheck 与 getOutOfRangeCheck、getRepeatCount。

## 典型用法

**文档事实** 文档示例先构造 ANALOG_WAVEFORM rampUp，用 definition(TM::RAMP)、direction(TM::POS)、samples(4)、min(0.1)、max(1.6) 描述电压斜坡波形，再声明事件对象并用 vForce(rampUp) 绑定波形、用 sampleVectorDistance(64) 设置采样向量距离。

**文档事实** vForce 接受 const ANALOG_WAVEFORM 引用作为波形定义对象。

**文档事实** sampleVectorDistance 的参数 vectors 是定义距离的向量数，最小为 32 vectors。

**文档事实** averages 指定用于求平均的内部采样数；对 DC Scale 通道，XPS256 除外，该采样数必须是 2 的幂。

**文档事实** clampChecks 与 iClampChecks 的 failOnLow 和 failOnHigh 分别启用或禁用低端与高端钳位检查；参数表写默认为 clamp check 禁用，而函数签名给出的默认实参是 true。

**文档事实** getRepeatCount 返回波形重复次数；文档注明 DC event 的 getRepeatCount 成员函数总是返回 1。

**文档事实** 文档示例中事件对象实际声明为 EVENT_WAVEFORM_VF rampUpEvent，与本页标题的 EVENT_WAVEFORM_VFIM 不同，阅读示例时需注意。

## 和谁有关

- **文档事实** EVENT_BASE，语法节说明 EVENT_WAVEFORM_VFIM 派生自它。
- **文档事实** EVENT_WAVEFORM_VFVM，首页把二者并列为 specialized force/measure waveform classes，且本页语法节跟随了 VFVM 的子主题，二者共用 vForce、getVForce 等同名方法。
- **文档事实** ANALOG_WAVEFORM，vForce 的参数类型是 const ANALOG_WAVEFORM 引用，示例先构造 ANALOG_WAVEFORM 再绑定。
- **文档事实** EVENT_VALUE_INT，averages 与 getAverages 使用它作为采样数参数和返回值。
- **文档事实** EVENT_WAVEFORM_VF 与 EVENT_WAVEFORM_IM，列在本页 Related information，文档示例实际使用了 EVENT_WAVEFORM_VF。

## 版本

**文档事实** Functional changes 记载 Introduced in SmarTest 6.5.2。

**文档事实** SmarTest 7.4.0 新增成员函数 clampChecks() 与 getClampChecks()。

## 出处

- `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.38_EVENT_WAVEFORM_VFIM.htm`
