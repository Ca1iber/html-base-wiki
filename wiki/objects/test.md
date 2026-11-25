---
type: object
title: TEST
layer: L2
stage: testmethod
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.241_TEST.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# TEST

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **16,005 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.241_TEST.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

For functional
tests:

```
Boolean TEST(Boolean continue = FALSE);
Boolean TEST(Boolean continue, TM::RELIABILITY reliability);
```

Note
 It can only retrieve and log the latest functional test result when no other
sequencer based tests have been executed between
FUNCTIONAL_TEST
 and

TEST
.

The following is also available for multiport testing
only:

```
Boolean TEST(const STRING& port, Boolean continue = FALSE);
Boolean TEST(const STRING& port, Boolean continue, TM::RELIABILITY reliability);
```

For
AC tests or any
tests:

```
Boolean TEST(const STRING& pin, const STRING& testname, DOUBLE value, Boolean continue = FALSE);
Boolean TEST(const STRING& pin, const STRING& testname, DOUBLE value, Boolean continue, TM::RELIABILITY reliability);
Boolean TEST(const STRING& pin, const STRING& testname, DOUBLE value, INT logTestNumber = DEFAULT_LOGTESTNUMBER_VALUE, char* softBin = "", INT hardbin = -1, Boolean continue = FALSE);
Boolean TEST(const STRING& pin, const STRING& testname, const LIMIT& limit, DOUBLE value, Boolean continue = FALSE);
Boolean TEST(const STRING& pin, const STRING& testname, const LIMIT& limit, DOUBLE value, Boolean continue, TM::RELIABILITY reliability);
Boolean TEST(const STRING& pin, const STRING& testname, const LIMIT& limit, DOUBLE value, INT logTestNumber = DEFAULT_LOGTESTNUMBER_VALUE, char* softBin = "", INT hardbin = -1, Boolean continue = FALSE);
Boolean TEST(const STRING& pin, const STRING& testname, V93kLimits::TMLimits& tmLimit, DOUBLE value, Boolean continue = FALSE);
Boolean TEST(const STRING& pin, const STRING& testname, V93kLimits::TMLimits& tmLimit, DOUBLE value, Boolean continue, TM::RELIABILITY reliability);
Boolean TEST(const STRING& pin, const STRING& testname, V93kLimits::TMLimits& tmLimit, DOUBLE value, INT logTestNumber = DEFAULT_LOGTESTNUMBER_VALUE, char* softBin = "", INT hardbin = -1, Boolean continue = FALSE);
```

The
following are also available for multiport testing
only:

```
Boolean TEST(const STRING& port, const STRING& pin, const STRING& testname, DOUBLE value, Boolean continue = FALSE);
Boolean TEST(const STRING& port, const STRING& pin, const STRING& testname, DOUBLE value, Boolean continue, TM::RELIABILITY reliability);
Boolean TEST(const STRING& port, const STRING& pin, const STRING& testname, const LIMIT& limit, DOUBLE value, Boolean continue = FALSE);
Boolean TEST(const STRING& port, const STRING& pin, const STRING& testname, const LIMIT& limit, DOUBLE value, Boolean continue, TM::RELIABILITY reliability);
Boolean TEST(const STRING& port, const STRING& pin, const STRING& testname, V93kLimits::TMLimits& tmLimit, DOUBLE value, Boolean continue = FALSE);
Boolean TEST(const STRING& port, const STRING& pin, const STRING& testname, V93kLimits::TMLimits& tmLimit, DOUBLE value, Boolean continue, TM::RELIABILITY reliability);
```

For
DC
tests:

```
Boolean TEST(const PMU_IFVM& dc, Boolean continue = FALSE);
Boolean TEST(const PMU_IFVM& dc, Boolean continue, TM::RELIABILITY reliability);
Boolean TEST(const PMU_VFIM& dc, Boolean continue = FALSE);
Boolean TEST(const PMU_VFIM& dc, Boolean continue, TM::RELIABILITY reliability);
Boolean TEST(const DPS_VFIM& dps, Boolean continue = FALSE);
Boolean TEST(const DPS_VFIM& dps, Boolean continue, TM::RELIABILITY reliability);
```

For
flexible DC
tests:

```
Boolean TEST(const PPMU_MEASURE& dc, Boolean continue = FALSE);
Boolean TEST(const PPMU_MEASURE& dc, Boolean continue, TM::RELIABILITY reliability);
Boolean TEST(const PPMU_MEASURE& dc, INT logTestNumber = DEFAULT_LOGTESTNUMBER_VALUE, char* softBin = "", INT hardbin = -1, Boolean continue = FALSE);
Boolean TEST(const PPMU_MEASURE& dc, INT logTestNumber = DEFAULT_LOGTESTNUMBER_VALUE, char* softBin = "", INT hardbin = -1, Boolean continue, TM::RELIABILITY reliability);
Boolean TEST(const STRING& port, const PPMU_MEASURE& dc, Boolean continue, TM::RELIABILITY reliability);
```

For
DC dynamic
tests:

```
Boolean TEST(DC_RESULT_ACCESSOR& dcResultAccessor, Boolean continue = FALSE);
```

For
spec
searches:

```
Boolean TEST(const SPEC_SEARCH& specSearch, INT logTestNumber = DEFAULT_LOGTESTNUMBER_VALUE, char* softBin = "", INT hardbin = -1, Boolean continue = FALSE);
Boolean TEST(const SPEC_SEARCH& specSearch, INT logTestNumber = DEFAULT_LOGTESTNUMBER_VALUE, char* softBin = "", INT hardbin = -1, Boolean continue, TM::RELIABILITY reliability);
```

For
ppTIA
measurements:

```
Boolean TEST(const PPTIA_TASK& pptia, INT logTestNumber = DEFAULT_LOGTESTNUMBER_VALUE, char* softBin = "", INT hardbin = -1, Boolean continue = FALSE);
Boolean TEST(const PPTIA_TASK& pptia, INT logTestNumber = DEFAULT_LOGTESTNUMBER_VALUE, char* softBin = "", INT hardbin = -1, Boolean continue, TM::RELIABILITY reliability);
Boolean TEST(const STRING& port, const PPTIA_TASK& pptia, Boolean continue = FALSE);
Boolean TEST(const STRING& port, const PPTIA_TASK& pptia, Boolean continue, TM::RELIABILITY reliability);
```
[表] Parameters
列: I/O | Parameter | Description / Range
行 1:
  I
  continue
  (Option.) This parameter controls whether the test should be continued if the
    TEST API returns FAIL. If it is set to
    TRUE, the test is continued in spite of a
    FAIL result. If it is set to FALSE (this is
    the default), the test is terminated. Instead of
    TRUE or FALSE, you can
    also use the enumerator TM::CONTINUE. If the
    TEST API returns PASS, the test is always
    continued.
    
    Note that the API behaves differently for the first site in a multi-site setup. In this
    special situation, the test is always continued, even if the
    TEST API returns FAIL and the continue
    parameter is set to FALSE. For the following
    sites, the test is terminated under these conditions.
    
    You can omit this parameter. However, you must specify it if you also specify the
    reliability parameter.
行 2:
  I
  reliability
  (Option.) This parameter is used to indicate the reliability of the test result for data logging.
    To indicate the test is reliable, specify
    TM::RELIABLE. To indicate the test is
    unreliable, specify TM::UNRELIABLE.
    
    You can omit this parameter. If so, use the syntax without this parameter. At that time,
    it is the same as specifying
    TM::RELIABLE.
行 3:
  I
  port
  For multi-port testing only. The port name whose functional test result or Flexible DC test
    result is judged and logged. Note that any pin group cannot be
    specified in the TEST API.
行 4:
  I
  pin
  The pin name (single pin name).
行 5:
  I
  testname
  The test name that can be referred from the Properties view. Test names can
    reference limits on the `Tests`（raw: `99276.htm`） page.
行 6:
  I
  value
  The test result value.
行 7:
  I
  limit
  The optional limit value to be used for the judgment. This parameter is a `LIMIT`（raw: `29504.htm`） API's class object. Hence, you can specify TM::Pass or
    TM::Fail to make the test result pass or fail intentionally.
    
    You can omit this parameter.
行 8:
  I
  logTestNumber
  An optional test number.
    
    If this test number is provided, it overrides the actual test number. If it is not
    provided, the actual test number is logged.
行 9:
  I
  softBin
  The software bin number of the multibin. For details see the `SET_MULTIBIN`（raw: `100114.htm`）
    API.
行 10:
  I
  hardBin
  The hardware bin number of the multibin. For details see the `SET_MULTIBIN`（raw: `100114.htm`）
    API.
行 11:
  I
  tmLimit
  Specifies the optional `TMLimits`（raw: `110432.htm`）`object`（raw: `110432.htm`） from which the
    limit data are taken.
行 12:
  I
  dc
  `PMU_IFVM`（raw: `29543.htm`） or `PMU_VFIM`（raw: `29563.htm`） constructor which specifies a DC
    test to be judged, or an object of `PPMU_MEASURE`（raw: `29585.htm`） API which specifies a Flexible DC
    test to be judged and logged.
行 13:
  I
  dcResultAccessor
  The `DC_RESULT_ACCESSOR`（raw: `99071.htm`） object from which the test data is taken.
行 14:
  I
  dps
  `DPS_VFIM`（raw: `28775.htm`） constructor which specifies a DC test to be judged.
行 15:
  I
  specSearch
  The `SPEC_SEARCH`（raw: `29753.htm`） API's class object to specify a spec search measurement
    to be judged.
行 16:
  I
  pptia
  `PPTIA_TASK`（raw: `86641.htm`） object from which the test data is taken

### Important points

You can get the latest functional test result with the following
syntax:

```
Boolean TEST(Boolean continue = FALSE);
```

To get the pass/fail
result in a specific pin, use the
`GET_FUNCTIONAL_RESULT`（raw: `29400.htm`）
 API.

The functional test can be executed by the
`FUNCTIONAL_TEST`（raw: `29356.htm`）
,

`DIGITAL_CAPTURE_TEST`（raw: `28758.htm`）
,
`NB_DIGITAL_CAPTURE_START`（raw: `29520.htm`）
,
`PMU_VFIM`（raw: `29563.htm`）
,
`PMU_IFVM`（raw: `29543.htm`）
, or
`DPS_VFIM`（raw: `28775.htm`）
 APIs.

For multi-port testing, you can get the functional test result of the specified port in the

TEST
 API by specifying the port name as
follows:

```
Boolean TEST(const STRING& port,
Boolean continue = FALSE);
```

For AC or any test in multi-port testing, you can log the port name of the specified port in
the
TEST
 API by specifying the port name as
follows:

```
Boolean TEST(const STRING& port,
const STRING& pin,
const STRING& testname,
DOUBLE value,
Boolean continue = FALSE);
Boolean TEST(const STRING& port,
const STRING& pin,
const STRING& testname,
const LIMIT& limit,
DOUBLE value,
Boolean continue = FALSE);
```

If
you will be converting the test data from the event data log to Standard
Test Data Format (STDF) for test data analysis, the entry for the pin
parameter specified for AC Test or Any test and for DC Test must be an
existing, defined pin name. To ensure that the string entered for the pin
parameter is an existing pin name, set the
`Check Testmethod API flag`（raw: `342556.htm#_342556__row_check_testmethod_api`）
 to "on". With the Check Testmethod API flag set to "on", a
fatal error will occur at runtime if the pin parameter is not an existing,
defined pin name.

If the parameter
limit
 is not specified, the limit values specified in
the Properties view will be used. If you specify the
Pass
 class object of
the
`LIMIT`（raw: `29504.htm`）
 API, the pass is always returned regardless of the actual test
result. If you specify the
Fail
 class object for the

LIMIT
 API, fail is always returned regardless of the actual result.

Whenever the limit parameter is supported, you can also supply a
`TMLimits object`（raw: `110432.htm`）
, as noted above in the AC test syntax descriptions.

You can use the continue parameter to call the TEST API several times in succession and
return an overall result of all these calls. The final return value to the testflow is computed
as the logical conjunction (AND) of all TEST calls; so, if at least one call returns FAIL, the
overall result will be FAIL. This computation is performed at the end of all of the remaining
statements.

If you call the
TEST
 API repeatedly in a multi-site setup,
you must take into account that for the
first
 site, the test will be continued after
every
TEST
 call, even if it has the
continue
 parameter
set to
FALSE
 and returns FAIL. Thus
all
TEST
 calls
will be executed for the first site. regardless of their
continue
 settings
and return values.

If you need the test result of pass or fail in your program, you can obtain it by the return
value of the
TEST
 API as either of boolean values.

If you need to make a test result fail intentionally, you can use the statement
TEST
("","",TM::Fail,0)
. This statement makes a test result fail forcedly. In contrast to
this, if you need to pass, you can use the statement
TEST ("","",TM::Pass,0)
.
Where,
TM::Fail
 and
TM::Pass
 are the

LIMIT
 API class objects and 0 is a dummy value of the test result.

To log test data by using the
TEST
 API and display the test report by
using the logged data, you must set the report formatter to the
`EventFormatter`（raw: `34891.htm`）
 and enable the required flags. For details, see
`Logging Data`（raw: `20894.htm`）
.

If you develop original report formatter for event data logging, you should understand that
the
TEST
 API produces a data log event of the type "TestEventType". For
details, see the
`Event Data Logging`（raw: `34872.htm`）
 manual.

For judgment of spec search, the
TEST
 API judges the last spec search
test result and produce a data log event. If a pass/fail or fail/pass transition is found the
return value is TRUE else it returns FALSE. If the spec search is not performed prior to this
API call, an error occurs.

Sometimes an error occurs in your program or an unpredictable trouble on the tester hardware
occurs at runtime, during testing. In such cases, the test should be indicated as unreliable.
You can indicate that the test is unreliable using the reliability parameter of the TEST
API.

If the reliability parameter is set to
TM::UNRELIABLE
, the

TEST
 API can also log the unreliable state to the event data log stream
with the test data such as pass/fail, result values, and so on. Note that the

TEST
 API does not log the reliable state even if the reliability parameter
is set to
TM::RELIABLE
.

The system-supplied
`Event Formatter`（raw: `34891.htm`）
 does not write the unreliable state on the event
data log stream to the report window. However, the pass/fail result for each test on the
displayed data log indicates a blank for an unreliable result. It is available for the global
pass/fail result only of a DC test or functional test. To write the unreliable state, you need
to develop an original report formatter.

For a DC test or functional test, the TEST API logs the unreliable state for the global
pass/fail result only, not for the per-pin results.

For the spec search test, only if a pass/fail or fail/pass transition is not found, the TEST
API
without
 using the reliability parameter logs the unreliable state. To indicate the
unreliable state from other reasons, use the reliability parameter.

TEST API for Flexible DC judges the test result based on the Global Pass Fail (GPF) result.
A Flexible DC test allows the user to define a different limit condition for each pin, so the
test may have multiple limit conditions. However, only one multiple-limit condition is allowed
in a Multiple Result Parametric (MPR) Record. Therefore, TEST API for Flexible DC creates a
test event for each limit condition, and outputs the test results of each test event for each
limit condition to the Event Data Log stream (EDL). Then the test results of the Flexible DC
test are placed into the MPR record for each limit condition and are recorded in converted
STDF.

### Examples

### Example 1
```
double thd_result;
TEST("dgtz_pin", "THD", thd_result);
```

The

TEST
 API compares the
thd_result
 data with the limit
range specified in the Properties view, then judges it as pass or fail.

### Example 2
```
double thd_result;
double snr_result;
TEST("dgtz_pin", "THD", thd_result,TM::CONTINUE);
TEST("dgtz_pin", "SNR", snr_result);
```

The
first
TEST
 API judges the
thd_result
 data as pass or fail.
Then the second
TEST
 API judges the
snr_result
 data as
pass or fail because the
TM::CONTINUE
 is described in the last parameter of
the first notation. When the result of the first
TEST
 is pass, the test will
continue even if the you do not set the continue flag to
TRUE
.

### Example 3
```
double thd_result;
double low_limit, high_limit;
TEST("Aout", "THD", LIMIT(TM::GT, low_limit,TM::LT, high_limit), thd_result);
```

First
of all, the
TEST
 API compares the
thd_result
 data with the
limit range specified by the
LIMIT
 API, then judges as pass or
fail.

### Example 4
```
TEST(PMU_VFIM("PIN1"));
```

The

TEST
 API retrieves the pass/fail judgment of the

PMU_VFIM("PIN1")
 which specifies the limits and result of the current
measurement test using Pin PMU connected to
PIN1
.

### Example 5
```
int Time_out,Trig_state;
START_TEST();
WAIT_TEST_DONE(1 sec, &Time_out, &Trig_state);

if(Trig_state == 1){
cout << "One or more digitizers has not received any trigger." << endl;
TEST("","",TM::Fail,0,TM::CONTINUE,TM::UNRELIABLE);
}
```

If
the used digitizers cannot receive the predictable starting trigger correctly, the

TEST
 API always judges the dummy result "0" as "Fail" by indicating the
"unreliable" state.

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
