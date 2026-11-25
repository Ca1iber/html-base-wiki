---
type: object
title: DPS_TASK
layer: L2
stage: testmethod
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.50_DPS_TASK.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# DPS_TASK

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **37,557 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.50_DPS_TASK.htm>` 及其子主题 `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.240_TASK_LIST.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.50.01_DPS_PIN_TASK.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Class definition

Constructor

```
DPS_TASK();
```

This API is defined in the header file
/opt/hp93000/soc/prod_com/include/MAPI/DpsTask.h
.

Member functions

`pin()`（raw: `55630.htm#_55630__dle_pin`）

`execMode()`（raw: `55630.htm#_55630__dle_execMode`）

`execute()`（raw: `55630.htm#_55630__dle_execute`）

`measRangeMode()`（raw: `55630.htm#_55630__dle_measRangeMode`）

`preAction()`（raw: `55630.htm#_55630__dle_preAction`）

`primaryActivation()`（raw: `55630.htm#_55630__dle_primaryActivation`）

`samples()`（raw: `55630.htm#_55630__dle_samples`）

`setup()`（raw: `55630.htm#_55630__dle_setup`）

`trigMode()`（raw: `55630.htm#_55630__dle_trigMode`）

`wait()`（raw: `55630.htm#_55630__dle_wait`）

`getFunctionalResult()`（raw: `55630.htm#_55630__dle_getFunctionalResult`）

`getNumberOfUsedChannelsFromLastMeasurement()`（raw: `55630.htm#_55630__dle_getNumberOfUsedChannels`）

`getPassFail()`（raw: `55630.htm#_55630__dle_getPassFail`）

`getValue()`（raw: `55630.htm#_55630__dle_getValue`）

`getValues()`（raw: `55630.htm#_55630__dle_getValues`）

`getVbump()`（raw: `55630.htm#_55630__dle_getVbump`）

`getWaveform()`（raw: `55630.htm#_55630__dle_getWaveform`）

### Member functions

pin()

```
DPS_PIN_TASK & pin(const STRING & pinlist);
```

This function returns the reference to the
`DPS_PIN_TASK`（raw: `55665.htm`）
 class object that represents the measurement conditions for specified DPSs.

Note
 A call to this function must be followed by calls to member functions of
`DPS_PIN_TASK`（raw: `55665.htm`）

class. You cannot call another
DPS_TASK
 member function after calling
pin()
.

[表] Parameter
行 1:
  pinlist
  Target pin name for which the user wants to define measurement conditions.
    You can specify multiple
    pins by separating pin entries with a comma.
execMode()

```
DPS_TASK & execMode(const TM::DCTEST_MODE mode);
DPS_TASK & execMode(const STRING & mode);
```

This member function selects the execution mode.

[表] Parameter
行 1:
  mode [跨 5 行]
  The measurement mode defined as TM::DCTEST_MODE or as string. The following types [跨 2 列]
    are available:
行 2:
  TM::GPF
    
    "GPF"
  This mode executes a global pass/fail measurement. The test will pass if all of the measurements
    pass. The test result can be retrieved with the getPassFail() member
    function.
    
    This is the default value.
行 3:
  TM:PPF
    
    "PPF"
  This mode executes a per-pin pass/fail measurement. The pass/fail result for each measured pin can be
    retrieved with the getPassFail(const STRING & pinlist) member function. In this mode,
    you can also retrieve the global pass/fail result with the getPassFail() member
    function.
行 4:
  TM::PVAL
    
    "PVAL"
  This mode executes a per-pin value measurement. The result value for each measured pin can be retrieved
    with the getValue(const STRING & pin) member function. In this mode, you can also
    retrieve the global pass/fail result and the per-pin pass/fail result by using the
    getPassFail() and getPassFail(const STRING & pinlist) member
    function, respectively.
行 5:
  TM::DCTEST_AUTO
    
    "DCTEST_AUTO"
  This mode executes the DC test according to the test suite flags.
    If the flag `"Pass value"`（raw: `342556.htm#_342556__row_value_on_pass`） or `"Fail value"`（raw: `342556.htm#_342556__row_value_on_fail`） is on, the DC test will execute in the same way as in the
    TM::PVAL mode.
    
    If the flags "Pass value" and "Fail value" are
    off and the flag `"Per pin on pass"`（raw: `342556.htm#_342556__row_per_pin_on_pass`） or `"Per pin on fail"`（raw: `342556.htm#_342556__row_per_pin_on_fail`） is
    on, the DC test will execute in the same way as in the
    TM::PPF mode.
    
    If the flags "Pass value" and "Fail value" are
    off and the flag "Per pin on pass" and "Per pin on fail" are
    off, the DC test will execute in the same way as in the
    TM::GPF mode.
execute()

```
void execute();
```

This function calls the setup() member function if the measurement conditions have
not downloaded to the firmware layer yet. It then executes a DC parametric test based on the measurement conditions
defined in
DPS_TASK
 and
DPS_PIN_TASK
. If this class is added to

TASK_LIST
, the execute() member function of the
TASK_LIST
 class calls this
member function.

When executing the test method, the primaries will be applied.

Note
 The current range defined by the
DPS_PIN_TASK
 minimum
and maximum values remains after the
DPS_TASK
execute()
 member function is called.
The regulation performance of the DPS is negatively affected by the current sense resistor and
therefore the current measurement range should be restored to the highest possible range after a
low current measurement. To reset the current range to the highest possible range, you must
program the
DPS_PIN_TASK
 minimum and maximum values accordingly and then call
the
DPS_TASK
execute()
 member function again.

Using the offline result emulation function:

The
execute()
 method of the
DPS_TASK
 class takes a
measurement name as additional parameter. The name is required to refer to the corresponding
offline measurement result specified in the setup file.

```
virtual void execute(FwStream* = NULL)
```

This function is the existing measurement execution method of

DPS_TASK
.

```
virtual void execute(const string& measurementName)
```

Parameter

[表]
行 1:
  measurementName
  Associate the measurement with offline data.

For more details, see
`Parametric offline result emulation`（raw: `128581.htm`）
 in
`Offline Result Emulation`（raw: `128475.htm`）
.

measRangeMode()

```
DPS_TASK & measRangeMode(const TM::DPS_MEAS_RANGE_MODE& rangeMode);
```

This member function
selects the measurement range mode.
It is no longer supported and silently ignored.

Note
 The regulation performance of the DPS is negatively affected by the current sense resistor. So after a low
current measurement, use this function to restore the current measurement range to the highest possible range.

[表] Parameter
行 1:
  rangemode
  Measurement mode. The following types are available:
    
    TM::KEEP_RANGE: This mode keeps the measurement range of the last measurement
    (default).
    
    TM::RESTORE_RANGE: This mode restores the measurement range after the
    measurement to the highest possible range: 1,5A.
    
    The default value is TM::KEEP_RANGE.
    
    For DPS128 and
    XPS256, the function is silently ignored and the measurement range is restored to the force
    or clamp range.
preAction()

```
DPS_TASK & preAction(const STRING & action);
```

This member function defines the action to be
performed prior to the DC measurement.

[表] Parameter
行 1:
  action
  Action type to be performed prior to the DC measurement. The following types are available:
    
    "NONE": In the internal trigger measurement mode, this option defines no
    pre-action. However, the digital primaries specified in the Testsuite dialog are activated prior
    to the DC measurement.
    Note: In the external trigger measurement mode, a functional test
    is forcibly executed prior to the DC measurement by activating the digital primaries specified
    in the Testsuite dialog. "NONE" is the same as "FTST" in
    the external trigger measurement mode.
    
    To activate the primaries specified with the
    PRIMARY_STATUS API or primary analog set, put the
    FLUSH API prior to this statement.
    
    "FTST": Performs a functional test prior to the DC measurement by activating
    the digital primaries specified in the Testsuite dialog. This option is used to perform a DC
    measurement with applying a break vector defined in the primary set. To activate the primaries
    specified with the PRIMARY_STATUS API or primary analog set, put the
    FLUSH API prior to this statement.
    You can retrieve the result of the
    functional test with the getFunctionalResult() member function of this API.
    
    "FTST_NO_RESULT": Performs a functional test prior to the DC measurement
    without uploading the test result. This option is used when you need to run a preconditioning
    pattern just to put the device in a desired state and Do not care about the test result. This
    option can help save time and optimize the performance.
    
    The default value is "NONE".
primaryActivation()

```
void DPS_TASK::primaryActivation(Boolean primaryActivation);
```

This function allows the user to specify
whether he wants to have the primaries activated primaryActivation(true) or not primaryActivation(false) for a DPS
measurement.

[表] Parameter
行 1:
  primaryActivation
  Specifies whether to have the primaries activated (true) or not
    (false).
samples()
```
DPS_TASK & samples(size_t samples);
```

This function specifies the number of measurements. An
external DPS measurement triggers the pattern for every measurement. After the measurements, the average of the measured
values will be calculated.

[表] Parameter
行 1:
  samples
  The number of measurements to be averaged. This must be a positive integer.
    The default value is
    1.

The real sample number of the measurement may not be the specified
samples
. See details
below.

For DPS128-HC / DPS64-HC the real sample number of the measurement is:
[表]
列: Measurement type | Range | Number of samples
行 1:
  Voltage measurement
  7V
  The maximum between 4 and the specified samples.
行 2:
  Current Measurement [跨 3 行]
  12.5µA - 250µA
  The maximum between 64 and the specified samples.
行 3:
  1.25mA - 200mA
  The maximum between 16 and the specified samples.
行 4:
  1A
  The maximum between 8 and the specified samples.

For UHC4T, the real sample number of the measurement is:
[表]
列: Measurement type | Range | Number of samples
行 1:
  Voltage measurement
  4V
  The maximum between 8 and the specified samples.
行 2:
  Current Measurement [跨 2 行]
  2mA
  The maximum between 256 and the specified samples.
行 3:
  Range larger than or equal to 50mA
  The maximum between 64 and the specified samples.

For XPS256 the real sample number of the measurement is the specified
samples
.

Maximum number of samples:

For DPS128 / DPS64 the maximum number of samples is 8192.

For UHC4T the maximum number of samples is 16384.

For XPS256 the maximum number of samples is 262144.

Real sample number:

For DPS128 / DPS64 and UHC4T, if the real
sample number of the measurement is not power of 2, it will be rounded to the next power of 2.

For
XPS256
 any sample number between 1 and the maximum
value can be set.

setup()

```
void setup();
```

This function downloads the measurement conditions defined in

DPS_TASK
 and
DPS_PIN_TASK
 into the firmware layer, but they will not be applied
to the test card hardware until the execute() member is called. If this class is added to
TASK_LIST
,
the setup() member function of the
TASK_LIST
 class calls this member function.

trigMode()

```
DPS_TASK & trigMode(TM::TrigMode trig_mode);
```

This member function defines the trigger mode.

[表] Parameter
行 1:
  trig_mode [跨 2 行]
  Trigger mode. The following modes are available:
    
    TM::INTERNAL: This mode executes an internal trigger DPS measurement.
    
    TM::EXTERNAL: This mode executes an external trigger DPS measurement. In this
    mode, the measurement continues as long as a trigger is sent to the DPS.
    This option forcibly
    executes a functional test prior to the DC measurement, with activation of the curren digital
    primaries specified in the Testsuite dialog.
    
    To activate the primaries specified with
    the PRIMARY_STATUS API or primary analog set, put the
    FLUSH API prior to this statement.
    
    You can retrieve the results
    of this functional test with the getFunctionalResult() member function of
    the DPS_TASK API. This mode can define multiple limits of the current and
    voltage values for target pins by use of the MULTI_LIMITS API.
行 2:
  The default value is TM::INTERNAL.
wait()

```
DPS_TASK & wait(DOUBLE waitTime_s);
```

Specifies a wait time (in seconds) which is applied right
before the measurement (after any necessary range-switching and/or unganging of channels). For static DPS measurement,
internal settling time exists. But additional settling time may be needed because of load board design or large capacitor
used. For dynamic DPS measurement, no internal settling time exists because it runs together with digital channels. You
need to take care of the settling time within the pattern.

[表] Parameter
行 1:
  waitTime_s
  The wait time in seconds.
getFunctionalResult()

```
Boolean getFunctionalResult() const;
```

This function returns a global Pass/Fail result for all the
measured pins if the functional pre-test ("FTST" or external trigger measurement) was executed. If not, an error
occurs.

```
Boolean getFunctionalResult(const STRING & pinlist) const;
```

This function returns a Pass/Fail
result for the specified pin if the functional pre-test ("FTST" or external trigger measurement) was executed. If not, an
error occurs.

Users can specify multiple pins by separating pin entries with a comma and obtain Pass/Fail results
for each specified pin.

[表] Parameter
行 1:
  pinlist
  Pin names for which the pass/fail result is to be retrieved.
getNumberOfUsedChannelsFromLastMeasurement()

```
INT getNumberOfUsedChannelsFromLastMeasurement(const STRING & pin) const;
```

This method returns the number of channels contributed to the last measurement if the measurement mode has been set to

TM::MEASURE_CURRENT_UNGANGED
 in member function
`measurementMode()`（raw: `55665.htm#_55665__dle_measurementMode`）
 of the

`DPS_PIN_TASK`（raw: `55665.htm`）
 test method API.

For more information, refer also to
`Number of channels in unganged mode`（raw: `55665.htm#_55665__s_Number_of_channels_unganged`）
 in
`DPS_PIN_TASK`（raw: `55665.htm`）
.

[表] Parameter
行 1:
  pin
  Pin name for which the number of channels is to be retrieved.

Return Value

The number of channels contributed to the last measurement as int value.

getPassFail()

```
Boolean getPassFail() const;
Boolean getPassFail(const STRING & pinlist) const;
```

[表] Parameter
行 1:
  pinlist
  Pin names for which the pass/fail result is to be retrieved.
    
    You can specify multiple pins by separating pin entries with a comma and obtain Pass/Fail results for
    each specified pin.

Return Value

Returns a
Boolean true
 for pass or
false
 for fail
result of the measurement.

getValue()

```
DOUBLE getValue(const STRING & pin) const;
```

This function returns a measured current, or voltage
value (DC-Scale only), for the specified pin in unit [A] and [V], if the appropriate
measurement mode (
PVAL
) is specified. If not, an error occurs.

[表] Parameter
行 1:
  pin
  Pin name for which the measured value is to be retrieved.
getValues()

```
const ARRAY_D getValues(const STRING & pin) const;
```

This function returns the measured values of
all channels of a pin with ganged channels. The measurement values are returned as an array of values in the order of the
gang definition.

[表] Parameter
行 1:
  pin
  Pin name for which the measurement value is to be retrieved.
getVbump()

```
DOUBLE getVbump(const STRING &pin);
```

This function returns the voltage bump value of the specified
pin.

[表] Parameter
行 1:
  pin
  The DPS pin to query.
getWaveform()

```
const ARRAY_D getWaveform(const STRING & pin) const;
```

The first version of the function returns a
series of measured values in external trigger mode, for the specified pin in unit [A], if the appropriate measurement mode
(PVAL) is specified. If not, an error occurs.

```
const ARRAY_D getWaveform(const STRING & pin, INT channelIndex) const;
```

The second version of the
function returns the measured values from one channel of the specified ganging group (
pin
), with the
specified channel index. The index refers to the index of the channel in the ganging group, not the physical channel
number on the board.

[表] Parameter
行 1:
  pin
  Pin name for which the measurement value is to be retrieved.
行 2:
  channelIndex
  Index of the selected pin in the ganging group.

### Examples

### DPS per-pin value measurement
```
DPS_TASK dpsTask;

ON_FIRST_INVOCATION_BEGIN();

//
// Setup the measurement
//
CONNECT();

dpsTask.pin("Vcc").min(0 A).max(0.1 A);
dpsTask.pin("Vee").min(0 A).max(0.2 A);
dpsTask.wait(5 ms); //available in SW6.3.3
dpsTask.execMode(TM::PVAL);
dpsTask.trigMode(TM::INTERNAL);

//
// Execute the measurement
//
FUNCTIONAL_TEST();

dpsTask.execute();

ON_FIRST_INVOCATION_END();

//
// Result upload and datalog
//
double IMeas1, IMeas2;

IMeas1 = dpsTask.getValue("Vcc");
IMeas2 = dpsTask.getValue("Vee");

TEST("Vcc,Vee", "Idd_Test", dpsTask.getPassFail()?TM::Pass:TM::Fail, true);
```

In this example, a DPS per-pin value measurement is
performed on the pin "Vcc" and "Vee". The measured current values are retrieved. The pass/fail result is judged and
logged.

### DPS measurement with different settings for different sites
```
DPS_TASK dpsTask;

ON_FIRST_INVOCATION_BEGIN();

CONNECT();

//
// Dummy initialization of a testflow variable
//
FOR_EACH_SITE_BEGIN();

SET_USER_FLAG("DPS_DUMMY_VAR", CURRENT_SITE_NUMBER());

FOR_EACH_SITE_END();

dpsTask.pin("Vcc").min(0 A).max(0.1 A);

dpsTask.execMode(TM::GPF);

dpsTask.trigMode(TM::INTERNAL);

//
// The task will be changed.
//
dpsTask.setup();

FOR_EACH_SITE_BEGIN();

INT current;

GET_USER_FLAG("DPS_DUMMY_VAR",&current);

dpsTask.pin("Vcc").max(current A);

FOR_EACH_SITE_END();

dpsTask.execute();

ON_FIRST_INVOCATION_END();

//
// Result upload and datalog
//
TEST( "Vcc", "multiDeltaDps", dpsTask.getPassFail()?TM::Pass:TM::Fail, true);
```

In this example, different settings are defined
for different sites through the user flag "DPS_DUMMY_VAR". Then a global pass/fail measurement is performed on all the sites in
parallel. The measurement result is retrieved and logged.

### DPS measurement with external trigger
```
DPS_TASK dpsTask;
ARRAY_D valueArrayVcc, valueArrayVdd;
INT i;
static LIMIT limit;
MULTI_LIMITS templ;

ON_FIRST_INVOCATION_BEGIN();

CONNECT();

//
// Create a Limit for each measurement
//
limit.unit("A");
limit.low(TM::GE, -4 uA);
limit.high(TM::LE, 175 uA);
templ.add(limit,8);

//
// Make sure that your pattern issues 8 triggers,
// otherwise you will get an error message
//
dpsTask.pin("Vcc").limits(templ);
dpsTask.trigMode(TM::EXTERNAL).execMode(TM::PVAL);

//
// Execute the primary pattern
//
dpsTask.execute();

ON_FIRST_INVOCATION_END();

//
// Result upload and datalog
//
valueArrayVcc = dpsTask.getWaveform("Vcc");

for ( i = 0 ; i < valueArrayVdd.size(); i++ )
{
TEST("Vcc", "extTrigDps", limit, valueArrayVcc[i], TRUE);
}
```

In this example, a DPS per-pin value test is performed on the pin "Vcc". The test is triggered by an external digital pin.
Eight times of measurements are performed. Each measurement result is retrieved, judged and logged.

### Class definition（取自子主题 DPS_PIN_TASK）

This API is defined in the header file

/opt/hp93000/soc/prod_com/include/MAPI/DpsPinTask.h
.

Constructor
You cannot directly construct any objects of this class. The

DPS_PIN_TASK
 class is a subsidiary data container of
the
`DPS_TASK`（raw: `55630.htm`）
 class. You can access this class object via the

`pin()`（raw: `55630.htm#_55630__dle_pin`）
 member function of the

DPS_TASK
 class by specifying the target DPS
names.
Member functions
[表]
行 1:
  `min()`（raw: `55665.htm#_55665__dle_min`）
    
    `max()`（raw: `55665.htm#_55665__dle_max`）
    
    `measurementMode()`（raw: `55665.htm#_55665__dle_measurementMode`）
    
    `switchableCap()`（raw: `55665.htm#_55665__dle_switchableCap`）
    
    `targetCap()`（raw: `55665.htm#_55665__dle_targetCap`）
  `limits(STRING)`（raw: `55665.htm#_55665__dle_limits_1`）
    
    `limits(LIMIT)`（raw: `55665.htm#_55665__dle_limits_2`）
    
    `limits(V93kLimits::TMLimits, STRING)`（raw: `55665.htm#_55665__dle_limits_3`）
    
    `limits(MULTI_LIMITS)`（raw: `55665.htm#_55665__dle_limits_4`）

### Member functions（取自子主题 DPS_PIN_TASK）

min()

```
DPS_PIN_TASK & min(DOUBLE val);
```

This function sets the lower current or voltage limit for pass/fail
judgment. Both the minimum and maximum limit must be specified by the
min and max functions. If not, an error occurs when the measurement
program is started. Both the minimum and maximum limit values are used
to set the DPS measurement range. See also the
`note`（raw: `55665.htm#_55665__n1`）
 below.

[表] Parameter
行 1:
  val
  Lower limit. The unit is [A] or [V].
max()

```
DPS_PIN_TASK & max(DOUBLE val);
```

This function sets the upper current or voltage limit for pass/fail
judgment. Both the minimum and maximum limit must be specified by the
min and max functions. If not, an error occurs when the measurement
program is started. Both the minimum and maximum limit values are used
to set the DPS measurement range. See also the
`note`（raw: `55665.htm#_55665__n1`）
 below.

[表] Parameter
行 1:
  val
  Upper limit. The unit is [A] or [V].
limits(STRING)

```
DPS_PIN_TASK & limits(const STRING & testname);
```

This function sets the lower and upper limit values for pass/fail
judgment by using a test flow limit name.

[表] Parameter
行 1:
  testname
  Test name that can be referred to from the parameter
    dialog.
limits(LIMIT)

```
DPS_PIN_TASK & limits(const LIMIT & limitobj);
```

This function sets the lower and upper limit values for pass/fail
judgment, by using a LIMIT class object.

If
measurementMode()
 is set to

TM::VOLTAGE_WAVEFORM
,

TM::CURRENT_WAVEFORM
 or

TM::VOLTAGE_WAVEFORM_HDIG
, you must specify a

MULTI_LIMITS
 object instead of LIMIT.

[表] Parameter
行 1:
  limitobj
  Name of an object of the `LIMIT`（raw: `29504.htm`）
    class
limits(V93kLimits::TMLimits, STRING)

```
DPS_PIN_TASK & limits(V93kLimits::TMLimits & lim, const STRING & limitParamName);
```

This function sets the lower and upper limit values for pass/fail
judgment, by using a
TMLimits
 class object.

[表] Parameter
行 1:
  lim
  Name of an object of the `TMLimits`（raw: `110432.htm`） class
行 2:
  limitParamName
  Name of the test whose limits are to be used.
    This
    parameter corresponds to the value of the
    limitParamName parameter of the
    `getLimitObj()`（raw: `110432.htm#_110432__dle_getLimitObj`） member
    function of `TMLimits`（raw: `110432.htm`）.
limits(MULTI_LIMITS)

```
DPS_PIN_TASK & limits(const MULTI_LIMITS & multi_limitsobj);
```

This function creates multiple sets of the lower and upper limit values
for pass/fail judgments by using a
MULTI_LIMITS
 class
object. This function can be used only in the external trigger DPS
measurement. The current limit values in the
n
th element of the

MULTI_LIMITS
 class object are used in the

n
th measurement in the external trigger DPS measurement.

If
measurementMode()
 is set to

TM::VOLTAGE_WAVEFORM
,

TM::CURRENT_WAVEFORM
 or

TM::VOLTAGE_WAVEFORM_HDIG
, you must specify a

MULTI_LIMITS
 object instead of LIMIT.

[表] Parameter
行 1:
  multi_limitsobj
  Object name of the `MULTI_LIMITS`（raw: `55668.htm`）
    class.
measurementMode()
```
DPS_PIN_TASK & measurementMode(TM::DC_MEASURE_TYPE mode);
```

This
member function defines the measurement mode. (Default:

TM::MEASURE_CURRENT
)

[表] Parameter
行 1:
  mode
  Measurement mode. [跨 2 列]
    The following measurement modes are
    available:
      [子表]
      列: Keyword | Description | Supported by
      子行 1:
        TM::MEASURE_VOLTAGE
        Voltage measurement
        DC
          Scale cards
      子行 2:
        TM::MEASURE_CURRENT
        Single current measurement
          
          This is the default measurement mode.
        DC
          Scale cards
      子行 3:
        TM::MEASURE_CURRENT_UNGANGED
        Unganged single current measurement (see
          also section `Number of channels in unganged mode`（raw: `55665.htm#_55665__s_Number_of_channels_unganged`）
          below)
          Note that on DPS128/64 and XPS256 you cannot execute a current
          compare on a ganged group of channels in unganged mode. Already activated
          comparators are silently disabled in unganged mode. A user notification (Error or
          warning) is omitted in this case, to avoid any interrupt in the testflow. The
          previous state of the comparators is automatically restored after the ganged group
          has been restored.
        DC Scale cards
      子行 4:
        TM::VOLTAGE_WAVEFORM
        Voltage waveform measurement
        DC Scale cards.
          
          Must be specified with a
          MULTI_LIMITS object instead of
          LIMIT.
      子行 5:
        TM::CURRENT_WAVEFORM
        Current waveform measurement
        DPS-slot DPS, DC Scale cards.
          
          Must be specified with a
          MULTI_LIMITS object instead of
          LIMIT.
      子行 6:
        TM::CONSTANT_VOLTAGE
        Multiple measurements on a voltage expected
          to be constant
        DC Scale cards
      子行 7:
        TM::CONSTANT_CURRENT
        Multiple measurements on a current expected
          to be constant
        DC Scale cards
      子行 8:
        TM::VOLTAGE_WAVEFORM_HDIG
        High-speed sampler voltage waveform
          measurement
          (For the binary data string
          description see `DPSE, DPSE? - (Define Power Supply External trigger measurement)`（raw: `98572.htm`）)
        DC Scale UHC4 / UHC4T
          
          Must be specified with a
          MULTI_LIMITS object instead of
          LIMIT.
      子行 9:
        TM::CONSTANT_VOLTAGE_HDIG
        High-speed sampler multiple voltage
          measurement
          (For the binary data string
          description see `DPSE, DPSE? - (Define Power Supply External trigger measurement)`（raw: `98572.htm`）)
        DC Scale UHC4T
      子行 10:
        TM::MEASURE_VOLTAGE_HDIG
        High-speed sampler voltage measurement (For
          the binary data string description see `DPSE, DPSE? - (Define Power Supply External trigger measurement)`（raw: `98572.htm`）)
        DC Scale UHC4T
      子行 11:
        TM::VOLTAGE_DROP_FORCE
        Voltage drop measurement on force line.
          
          For more information, refer to
          
          `Voltage drop measurement`（raw: `140638.htm#_140638__s_Voltage_drop_measurement`） in
          `DPS128 / DPS64 functionality and features`（raw: `140638.htm`）
          
          `UHC4T features`（raw: `107325.htm`）
          
          `XPS256 voltage drop measurement`（raw: `353409.htm`）
        HC variant of DC Scale
          DPS128 / DPS64,
          
          DC Scale XPS256, and
          
          DC Scale UHC4T
      子行 12:
        TM::VOLTAGE_DROP_RETURN
        Voltage drop measurement on return line.
          
          For more information, refer to
          
          `Voltage drop measurement`（raw: `140638.htm#_140638__s_Voltage_drop_measurement`） in
          `DPS128 / DPS64 functionality and features`（raw: `140638.htm`）
          
          `UHC4T features`（raw: `107325.htm`）
          
          `XPS256 voltage drop measurement`（raw: `353409.htm`）
        HC variant of DC Scale
          DPS128 / DPS64,
          
          DC Scale XPS256, and
          
          DC Scale UHC4T
    
    DC Scale cards include:
    DPS64, DPS128, XPS256, UHC4T

Note
 The current range defined by the
DPS_PIN_TASK
 minimum
and maximum values remains after the
DPS_TASK
execute()
 member function is called.
The regulation performance of the DPS is negatively affected by the current sense resistor and
therefore the current measurement range should be restored to the highest possible range after a
low current measurement. To reset the current range to the highest possible range, you must
program the
DPS_PIN_TASK
 minimum and maximum values accordingly and then call
the
DPS_TASK
execute()
 member function again.

The DPS measurement range will
be adjusted according to the limits you set. For details of DPS measurement
range specification, see
`DC Scale Device Power Supplies`（raw: `130532.htm`）
.
switchableCap()

```
DPS_PIN_TASK& switchableCap( const STRING & utilityPinName, TM::SWITCHABLE_CAP_STATE state );
```

This function is used to switch the state for the specified utility pin
in order to set the load capacitance to the value specified by member
function
`targetCap()`（raw: `55665.htm#_55665__dle_targetCap`）
.

The target state of the utility pin is defined by parameter

state
. The selected state is applied for
measurement only. The original state is automatically restored after the
measurement.

The function is only supported with the
`XPS256 specifications`（raw: `350908.htm`）
 in
`DPS operating mode`（raw: `354249.htm`）
.

[表] Parameter
行 1:
  utilityPinName
  The name of the utility pin that switches the
    capacitor on or off and is defined in the `Utility Pins editor`（raw: `105637.htm`）.
    
    Multiple utility pins can be defined as comma
    separated list.
行 2:
  state
  The state of type
    TM::SWITCHABLE_CAP_STATE to be
    set for the measurement.
    
    Programmable values:
    
    TM::CAP_STATE_OFF
    
    TM::CAP_STATE_ON
    
    The original state of the utility pin is
    automatically restored after the measurement.

targetCap()

```
DPS_PIN_TASK & targetCap (const DOUBLE & capFarad);
```

This function sets the target load capacitance for member function
`switchableCap()`（raw: `55665.htm#_55665__dle_switchableCap`）
.

The defined load capacitance is set only for the measurement. The
original capacitance value, which has been defined in the
`DPS Pins editor`（raw: `105636.htm`）
 or by the
`capacitance`（raw: `16887.htm#_16887__capacitance`）
 parameter of the
`DPSPINS resources`（raw: `16887.htm`）
, is automatically
restored after the measurement. This is needed to, for example, measure
the quiescent power supply current for high current XPS256
applications.

The target state of the utility pin is defined by parameter

state
. The selected state is applied for
measurement only. The original state is automatically restored after the
measurement.

The function is only supported with the DC Scale XPS256 card.
[表] Parameter
行 1:
  capFarad
  The load capacitance in µF (Microfarad).

### Example（取自子主题 DPS_PIN_TASK）

```
DPS_TASK dpsTask;

ON_FIRST_INVOCATION_BEGIN();

CONNECT();

dpsTask.pin("dps1")
.measurementMode(TM::MEASURE_CURRENT)
.min(0 mA)
.max(200 mA);

dpsTask.pin("dps2")
.measurementMode(TM::MEASURE_VOLTAGE)
.min(2 V)
.max(4 V);

dpsTask.pin("dps_gang_of_10-A")
.measurementMode(TM::MEASURE_CURRENT_UNGANGED)
.min(0 mA)
.max(10 mA);

dpsTask.pin("dps_gang_of_10-B")
.measurementMode(TM::MEASURE_CURRENT_UNGANGED)
.min(0 mA)
.max(750 mA);

dpsTask.samples(5).execMode(TM::PVAL).execute();

ON_FIRST_INVOCATION_END();

cout << "dps1:" << dpsTask.getValue("dps1") << " A" << endl;
cout << "dps2:" << dpsTask.getValue("dps2") << " V" << endl;

cout << "dps_gang_of_10-A:" << dpsTask.getValue("dps_gang_of_10-A") << " A" << endl;
cout << "dps_gang_of_10-B:" << dpsTask.getValue("dps_gang_of_10-B") << " A" << endl;
```

The example executes first a current measurement, then a voltage measurement.

In a third step it executes two single unganged current measurements on the two
10-channel-gangs, for "dps_gang_of_10A" with one remaining channel (see
Case
A
 above) and for "dps_gang_of_10B" with two ganged remaining channels (see

Case B
 above). Finally the measured current and voltage values are
retrieved.

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

（待补）

## 典型用法

（待补）

## 和谁有关

（待补）

## 版本

（待补）

## 出处

（待补）
