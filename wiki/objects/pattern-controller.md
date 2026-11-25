---
type: object
title: PATTERN_CONTROLLER
layer: L2
stage: pattern
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.142_PATTERN_CONTROLLER.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# PATTERN_CONTROLLER

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **14,071 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.142_PATTERN_CONTROLLER.htm>` 及其子主题 `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.142.01_PATTERN.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Class definition

Constructor:

```
PATTERN_CONTROLLER();
```

Member
functions:

`label(...)`（raw: `71357.htm#_71357__dlentry_label`）

`execMode(...)`（raw: `71357.htm#_71357__dlentry_execMode`）

`setup()`（raw: `71357.htm#_71357__dlentry_setup`）

`execute()`（raw: `71357.htm#_71357__dlentry_execute`）

`getPassFail(...)`（raw: `71357.htm#_71357__dlentry_getPassFail`）

### Syntax

The general format for setting up a DC subpattern
is

```
obj.label().add(dc_task_1).add(dc_task_2)...add(dc_task_n);
```

The
general format for downloading or executing a DC subpattern, or retrieving test
results,
is

```
obj.func();
```

The
parameters have the following meaning:

[表]
行 1:
  obj
  Object of the PATTERN_CONTROLLER class
行 2:
  func()
  Member function of the PATTERN_CONTROLLER
    class
行 3:
  add()
  Member function of the PATTERN class

### Member functions

label(...)
```
PATTERN & label(const STRING& subpattern_name, STRING& port = "@");
```

This
member function returns the reference to the
`PATTERN`（raw: `78536.htm`）

object holding the DC tasks for the specified label.

Note
 A call of this function must be followed by calls of member
functions of the
PATTERN
 class. You cannot call
another member function of the
PATTERN_CONTROLLER

class after calling
label()
.

[表] Parameters
行 1:
  subpattern_name
  The subpattern for which the DC task are to be
    specified. Note that the subpattern must already
    exist.
    
    For PPMU BADC tests with digital cards you must use
    an empty subpattern.
    
    For DC tests with DC Scale DPS cards it can also be a
    MAIN or SVEC pattern.
行 2:
  port
  The port for which the subpattern has been defined.
    If this parameter is omitted, the default port
    @ will be assumed.
execMode(...)
```
PATTERN_CONTROLLER & execMode(const TM::DCTEST_MODE mode);
PATTERN_CONTROLLER & execMode(const STRING& mode_string);
```

This
member function specifies the execution mode for the DC test.

Note
 It is the
execMode()
 function of the

PATTERN_CONTROLLER
 API that determines the
execution mode. The execution mode of the

PPMU_MEASURE
 API is ignored. But it must be
specified nonetheless, since otherwise no measurement would be
performed.

[表] Parameters
行 1:
  mode [跨 4 行]
  Execution mode. Possible [跨 2 列]
    values are:
行 2:
  TM::GPF
  Global PASS/FAIL The test will pass if it passes for
    all measured pins. This is the default.
行 3:
  TM::PPF
  Per pin PASS/FAIL. With this execution mode, the
    result can be retrieved for every measured pin.
行 4:
  TM::DCTEST_AUTO
  Executes the DC test according to the test suite
    flags.
    
    If the flag `Per pin on pass`（raw: `342556.htm#_342556__row_per_pin_on_pass`） or `Per pin on fail`（raw: `342556.htm#_342556__row_per_pin_on_fail`） is on, the DC test will
    executes in the same way as the mode
    TM::PPF.
    
    If the flag `Per pin on pass`（raw: `342556.htm#_342556__row_per_pin_on_pass`） and `Per pin on fail`（raw: `342556.htm#_342556__row_per_pin_on_fail`） are off, the DC test will
    executes in the same way as the mode
    TM::GPF.
行 5:
  mode_string [跨 4 行]
  Execution mode, [跨 2 列]
    specified as a string. Possible values are:
行 6:
  "GPF"
  Global PASS/FAIL. This is the default.
行 7:
  "PPF"
  Per pin PASS/FAIL
行 8:
  "DCTEST_AUTO"
  Executes the DC test according to the test suite
    flags. This is the same with the mode
    TM::DCTEST_AUTO.
setup()
```
void setup();
```

This member function serves to
download the previously defined DC tasks and to insert the corresponding

MEAS
 instructions into the specified
predefined subpattern. If the subpattern already contains any
instructions, these are removed.

For performance reasons, the
instructions are written into the subpattern only once within one
testflow execution; that is, the API will not modify them later on.
Therefore, if the same subpattern is used by more than one class object
of the
PATTERN_CONTROLLER
 API within one testflow, or
if the testflow is executed in a loop,
setup()

expects that the same measurement sets can be used for the subpattern
every time. If this is not the case (because the measurement parameters
depend on variables so that they change from one loop repetition to the
next, or because they are different for two class objects), it will
issue an error message.

setup()
 can also
temporarily modify a previous parameter definition within the same class
object. This is exploited for measurement parameters that contain
variables. For details, see
`Managing DC Tests with Variable Parameters`（raw: `75890.htm`）
.

There are no
parameters in this member function.

execute()
```
void execute();
```

This member function executes the
current primary sets. If the actual measurement parameters have not yet
been downloaded, and the predefined subpattern is still empty,

execute()
 first calls
setup()

to download the parameters and insert the
MEAS

instructions.

There are no parameters in this member
function.

getPassFail(...)
```
Boolean getPassFail() const;
Boolean getPassFail(const STRING & pinlist) const;
```

If
no parameter is specified, this member function returns the global
PASS/FAIL result of the test.

If a pin list is specified, the
function returns a single PASS/FAIL result for these pins. PASS is only
returned if all specified pins passed.

[表] Parameter
行 1:
  pinlist
  List of pins for which a global result is to be
    retrieved
[表] Return value
行 1:
  true
  Value for pass result of the measurement.
行 2:
  false
  Value for fail result of the measurement.

### Examples

### PPMU IVFM test

In this example, a PPMU IVFM test on the pin

S0
 and a PPMU VFIM test on the pin
S1
 are
performed from the pattern. The subroutine label
DC_Sub_Q0
 is used
for the execution of DC
test.

```
PPMU_SETTING setting, precharge;
PPMU_RELAY relay_on, relay_off;
PPMU_MEASURE meas1;
PPMU_CLAMP clamp_on, clamp_off;
PATTERN_CONTROLLER controller;

ON_FIRST_INVOCATION_BEGIN();

//
// Setups for PPMU
//
setting.pin("S0").iRange(1 mA).min(0 V).max(4.3 V).iForce(10 uA);
setting.pin("S1").iRange(10 mA).min(-10 uA).max(30 uA).vForce(3.3 V);

precharge.pin("S0").iRange(20 mA).min(0 mA).max(30 mA) .vForce(2.8 V);

//
// Relay setups
//
relay_on.pin("S0,S1").status("PPMU_ON");
relay_on.wait(1.3 ms);
relay_off.pin("S0,S1").status("AC_ON");

//
// Measurement setups
//
meas1.pin("S0,S1").execMode(TM::PVAL);

//
// Hardware specific programming to avoid hot switching
// on the Current Force setup
//
if(GET_TESTER_CLASS()==TM::PINSCALE)
{
clamp_on.pin("S0").status("CLAMP_ON").low(2.6 V).high(2.9 V);
clamp_off.pin("S1").status("CLAMP_OFF");
}

//
// Set up the controller
//
if(GET_TESTER_CLASS()==TM::PINSCALE)
controller.label("DC_Sub_Q0","Q0_Port").add(setting).add(clamp_on)
.add(relay_on).add(clamp_off).add(meas1).add(relay_off);
else
controller.label("DC_Sub_Q0","Q0_Port").add(precharge)
.add(relay_on).add(setting).add(meas1).add(relay_off);

controller.execMode("PPF").execute();

ON_FIRST_INVOCATION_END();

//
// Result upload and datalog
//
TEST("S0", "DC_TEST", controller.getPassFail("S0")?TM::Pass:TM::Fail,TRUE);
TEST("S1", "DC_TEST", controller.getPassFail("S1")?TM::Pass:TM::Fail,TRUE);
```

### PS1600 DC measurement examples

For DC value measurement examples
using the PS1600 pin PMU (PPMU) and board ADC (BADC) see
`PS1600 DC value measurements`（raw: `126336.htm`）
.

### Class definition（取自子主题 PATTERN）

Member functions:

`add(TASK)`（raw: `78536.htm#_78536__dlentry_add_TASK`）

`add(PPMU_TASK)`（raw: `78536.htm#_78536__dlentry_add_PPMU_TASK`）

`add(BADC_TASK)`（raw: `78536.htm#_78536__dlentry_add_BADC_TASK`）

`add(DC_WAVEFORM)`（raw: `78536.htm#_78536__dlentry_add_DC_WAVEFORM`）

`vecEvents(...)`（raw: `78536.htm#_78536__dlentry_vecEvents`）

`getClampHighCurrent(...) and getClampLowCurrent(...)`（raw: `78536.htm#_78536__dlentry_getClampHighCurrent`）

`getForceVoltage(...)`（raw: `78536.htm#_78536__dlentry_getForceVoltage`）

### Member functions（取自子主题 PATTERN）

add(TASK)
```
PATTERN & add(TASK & task));
```

This member function
allows to execute Board ADC tests in parallel with digital test for
different ports, and also to alternate (switch) between digital tests,
PinPMU tests, and Board ADC tests in one pattern run without the need to
stop the sequencer. The API

downloads measurement sets defined with the

PPMU_
xxx
 and

BADC_
xxx
 APIs.

inserts instructions (which will execute these sets) into a
predefined subpattern.

executes the current primary sets.

[表] Parameter
行 1:
  task
  A class object of one of the
    PPMU_xxx or
    BADC_xxx classes. The
    pins for which the task is defined must be a subset of
    the pins of the port to which the subpattern
    belongs.
add(PPMU_TASK)
```
PATTERN & add(PPMU_TASK & task);
```

This
member function assigns a class object of one of the

PPMU_SETTING
,

PPMU_RELAY
,

PPMU_MEASURE
, or

PPMU_CLAMP
 API's to a subpattern. The
measurement sets generated from these objects will be executed from
within the specified subpattern.

[表] Parameter
行 1:
  task
  A class object of one of the
    PPMU_xxx classes. The
    pins for which the task is defined must be a subset of
    the pins of the port to which the subpattern
    belongs.
add(BADC_TASK)
```
PATTERN & add(BADC_TASK & task);
```

This
member function assigns a class object of one of the
`BADC_SETTING`（raw: `126272.htm`）
 and
`BADC_MEASURE`（raw: `126248.htm`）
 API's to a subpattern.
The measurement sets generated from these objects will be executed from
within the specified subpattern.

[表] Parameter
行 1:
  task
  A class object of one of the
    BADC_xxx classes. The
    pins for which the task is defined must be a subset of
    the pins of the port to which the subpattern
    belongs.
add(DC_WAVEFORM)
```
PATTERN & add(DC_WAVEFORM & waveform);
```

This
member function assigns a DC waveform to the pattern.

[表] Parameter
行 1:
  waveform
  An object of the DC_WAVEFORM class.
vecEvents(...)
```
VEC_EVENTS & vecEvents(const STRING & pinlist);
```

This member function returns the vector event editing interface for the specified pins. Using the

`VEC_EVENTS`（raw: `116944.htm`）
, you can define events on DC Scale channels
in the vectors of a pattern.

Note
 The interface is valid for only one pinlist at a time. It is valid as long as the
pattern is not changed via
label()
, or until the next
call to
vecEvents()
. Each call to

vecEvents()
 will invalidate a previously
retrieved VEC_EVENTS reference.

[表] Parameter
行 1:
  pinlist
  The pin list to work with.
getClampHighCurrent(...) and getClampLowCurrent(...)
```
bool getClampHighCurrent(const STRING & singlePin,
INT refVector,
DOUBLE & current) const;

bool getClampLowCurrent(const STRING & singlePin,
INT refVector,
DOUBLE & current) const;
```

These
member functions find the last current clamp that is defined before or
at the specified vector in this pattern. Also samples generated by a
waveform will be analyzed. If the force current cannot be determined,
false is returned. This might for instance happen if no force event
exists or an equation variable is referenced that cannot be resolved to
a value.

[表] Parameters
行 1:
  singlePin
  The pin to be analyzed.
行 2:
  refVector
  The vector for which the currently active force
    voltage will be searched.
行 3:
  current
  The found force current value. If no value is set,
    return value is 999999 for iClampHigh and -999999 for
    iClampLow.
[表] Return value
行 1:
  true
  The force current was successfully resolved.
行 2:
  false
  No force current between pattern start and refVector
    was found.
getForceVoltage(...)
```
bool getForceVoltage(const STRING & singlePin, INT refVector,
DOUBLE & voltage) const;
```

This
member function finds the force voltage that is defined before or at the
specified vector in this pattern. Also samples generated by a waveform
will be analyzed. If the force voltage cannot be determined, false is
returned. This might for instance happen if no force event exists, or if
an equation variable is referenced that cannot be resolved to a
value.

Note that this function operates on setup data only! It may
be used for fast setup backtracking, for example, to lookup the force
voltage at a specific cycle. Be aware that this function operates on
vectors, not cycles!

[表] Parameters
行 1:
  singlePin
  The pin to work with.
行 2:
  refVector
  Reference vector.
行 3:
  voltage
  Voltage at reference vector.

### Examples（取自子主题 PATTERN）

### Example 1
 The example shows how to lookup the force voltage at a
specific vector in the "myRamp"
pattern.

```
// Get the PATTERN the events will be placed on
PATTERN_CONTROLLER patternController;
PATTERN & pattern(patternController.label("myRamp"));

// Get the force voltage at vector 100
DOUBLE voltage;

if (pattern.getForceVoltage("Vdd", 100, voltage))
{
cout << "Voltage at vector 100: " << voltage << " V" << endl;
}
```

### Example 2

The example shows how to add a DC waveform to the designated
label.

```
//
// Define an analog waveform
//
ANALOG_WAVEFORM ramp("ramp");
ramp.definition(TM::RAMP)
.direction(TM::POS)
.min(-1 V)
.max(5.5 V)
.samples(2048);

//
// Integrate the analog waveform into the DC waveform
//
DC_WAVEFORM dcWaveform;

dcWaveform.vForce(ramp)
.vRange(6 V)
.iRange(1 mA)
.sampleVectorDistance(1024);

//
// Add the DC waveform to a label
//
PATTERN_CONTROLLER patternControllerDcWaveForm;
patternControllerDcWaveForm.label("ppmuSubRamp","portPpmu").add(dcWaveform);
patternControllerDcWaveForm.setup(); //This function is only needed for the first run.
```

### Example 3

The example below shows how to get the last current clamp that
was defined before or at the specified vector in a
pattern.

```
PATTERN_CONTROLLER pc;
PATTERN & pattern(pc.label("patEvents", "@"));

EVENT_IC iClampEvent1("iClampEvent1");
EVENT_RANGE_RESTORE eventRangeRestore("eventRangeRestore");

ON_FIRST_INVOCATION_BEGIN();

iClampEvent1.iClampLow(1 mA);

pattern.vecEvents("dps1").clearAll().setup();

pattern.vecEvents("dps1")
.insert(32, iClampEvent1)
.insert(150, eventRangeRestore);

pc.setup();

ON_FIRST_INVOCATION_END();

DOUBLE current = 0.;

if ( pattern.getClampHighCurrent("dps1", 32, current) )
{
cout << "High current clamp at vector 32 (expect 999999): " << current << " A" << endl;
}

if ( pattern.getClampLowCurrent("dps1", 32, current) )
{
cout << "Low current clamp at vector 32 (expect 0.001): " << current << " A" << endl;
}
```

<!-- 语法节 end -->

## 是什么

**文档事实** PATTERN_CONTROLLER 用于在 pattern 内执行 DC Scale 的 DC 测试与 PPMU BADC 测试：它下载由 `PPMU_...` / `BADC_...` API 定义的测量集，把执行这些集合的指令插入预定义 subpattern，并执行当前 primary sets，还可取回全局 pass/fail；由此可在同一 pattern run 中让不同端口上的 digital 与 DC 测试并行或交替，而无需停止 / 启动 sequencer。
**文档事实** 它调用 PATTERN 类对象（保存各 subpattern 的测量数据）。对 digital 卡的 PPMU BADC 测试，subpattern 必须为空，因为测量会按 add 顺序动态链接进去，且使用随 test suite / testflow 执行而变化的内部 ID，链接后的 subpattern 不能永久保存。定义于 `/opt/hp93000/soc/prod_com/include/MAPI/PatternController.h`。

## 典型用法

**文档事实** 设置格式为 `obj.label().add(dc_task_1)...add(dc_task_n);`，执行或取值格式为 `obj.func();`。示例先 `controller.label("DC_Sub_Q0","Q0_Port")` 逐个 `add(...)` PPMU task，再 `controller.execMode("PPF").execute();`，最后用 `controller.getPassFail("S0")` 上传结果。
**文档事实** `label()` 之后必须接 PATTERN 的成员函数，不能在同一对象上再调 PATTERN_CONTROLLER 的其他成员；执行模式由 PATTERN_CONTROLLER 的 `execMode()` 决定，`PPMU_MEASURE` 的 execMode 被忽略但仍须指定。也可通过 `PATTERN::vecEvents()` 在 pattern 向量上编辑 DC event。
**文档事实** 示例代码把 setup、execute 与结果取回放在 `ON_FIRST_INVOCATION_BEGIN()` / `ON_FIRST_INVOCATION_END()` 块内。

## 和谁有关

- PATTERN：本页子主题；`label()` 返回 PATTERN 引用，PATTERN 提供 `add(TASK)`、`add(PPMU_TASK)`、`add(BADC_TASK)`、`add(DC_WAVEFORM)`、`vecEvents()` 等。
- PPMU_SETTING / PPMU_RELAY / PPMU_MEASURE / PPMU_CLAMP 与 BADC_SETTING / BADC_MEASURE：`add()` 接收这些 task；`BADC_MEASURE` / `BADC_SETTING` 的入边明确写其测量由 PATTERN_CONTROLLER 执行。
- VEC_EVENTS：`PATTERN_CONTROLLER` 页引用 `VEC_EVENTS`，用于在向量中定义 DC event（入边 `02.07.04.01.267_VEC_EVENTS`）。
- EVENT_*（DC event 类）：多份入边写 "has to be assigned to the PATTERN_CONTROLLER which is responsible for further handling"。
- SPMU_TASK / DC_RESULT_ACCESSOR / FLEX_RELAY / PS1600 DC value measurements：Related information 明列。

## 版本

**文档事实** Functional changes 记为 "Introduced before SmarTest 6.3.2"。

## 出处

- `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.142_PATTERN_CONTROLLER.htm`（主语料；语法节含子主题 `02.07.04.01.142.01_PATTERN.htm`）。
