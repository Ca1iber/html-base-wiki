---
type: object
title: TESTSET
layer: L2
stage: testmethod
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244_TESTSET.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# TESTSET

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **100,603 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244_TESTSET.htm>` 及其子主题 `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.231.43_SMC_SYNCHRONIZE.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.231.45_SMC_TEST.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.242_TESTNUMBER.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244.01_TESTSET__.addAlarm.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244.02_TESTSET__.combineMultiPortTests.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244.03_TESTSET__.cont.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244.04_TESTSET__.doLog_ShmooTest.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244.05_TESTSET__.hlmFmt.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244.06_TESTSET__.judgeAndLog_DcResultAccessor.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244.07_TESTSET__.judgeAndLog_Dps.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244.08_TESTSET__.judgeAndLog_DpsVfim.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244.09_TESTSET__.judgeAndLog_FunctionalTest.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244.10_TESTSET__.judgeAndLog_ParametricTest.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244.11_TESTSET__.judgeAndLog_PmuIfvm.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244.12_TESTSET__.judgeAndLog_PmuVfim.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244.13_TESTSET__.judgeAndLog_PpmuMeasure.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244.14_TESTSET__.judgeAndLog_PptiaTask.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244.15_TESTSET__.judgeAndLog_ScanTest.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244.16_TESTSET__.judgeAndLog_SpecSearch.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244.17_TESTSET__.judgeAndLog_Spmu.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244.18_TESTSET__.llmFmt.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244.19_TESTSET__.port.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244.20_TESTSET__.reliability.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244.21_TESTSET__.resFmt.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244.22_TESTSET__.suppressTestNameLoopCount.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244.23_TESTSET__.testname.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244.24_TESTSET__.testname_default.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244.25_TESTSET__.testnumber.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244.26_TESTSET__.testnumber_default.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244.27_TESTSET__.testnumber_none.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244.28_TESTSET__.testsuite.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244.29_TESTSET__.testsuite_default.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244.30_TESTSET__.testtext.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244.31_TESTSET__.testtext_none.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244.32_TESTSET__.testtype.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244.33_TESTSET__.testtype_default.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.250_TMLimits.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.99_GET_TESTNUMBER.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.10.01_SmartCalc_multithreading_basics.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.10.05_SmartCalc_recommendations.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.01.08.04_Generating_per-pin_test_numbers.htm>`、`<03_Use_cases_and_application_papers/03.02_How_to_do_Multi-Site_Testing/03.02.02.06.07.02_Use_of_SMC_TEST___with_multibin.htm>`、`<03_Use_cases_and_application_papers/03.02_How_to_do_Multi-Site_Testing/03.02.02.06.07.03_Use_of_TESTSET_and_SMC_TEST___test_suites_with_multibin.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Class definition

This API is defined in the header file

/opt/hp93000/soc/prod_com/include/MAPI/TestSet_r.h
.

You can use the system-prepared class object "TestSet" when using member functions.
You can also create a new class object. If a function sets up a parameter, the
parameter setting is kept until you reset it or return it to a default setting.

System-prepared class object

```
TestSet
```

Note
 The system-prepared object cannot be used within the SMC
framework.

Constructor

```
TESTSET();
```

This constructor creates the class object that contains the settings of
the member functions that define numbering procedures for results in a
given test suite, and is used for specifying all options that relate to
the TEST API and test
methods.

```
TESTSET(bool withContext, INT site);
```

This constructor creates the class object as defined above and
additionally defines the site to be processed. The parameter

withContext
 is to be set to

false
. For more information refer to
`Example 5: Using TESTSET() in SMC background processing`（raw: `58886.htm#_58886__example_TESTSET_in_SMC`）
.

Note

TESTSET
 class objects must not be shared across multiple threads.

If used in SMC background processing,
TESTSET
 class objects should be created
and used only within the

SMC_backgroundProcessing()
 method.

Member functions
[表]
行 1:
  `TESTSET().port()`（raw: `127776.htm`）
    
    `TESTSET().cont()`（raw: `127763.htm`）
    
    `TESTSET().reliability()`（raw: `127778.htm`）
    
    `TESTSET().testnumber()`（raw: `127787.htm`）
    
    `TESTSET().testnumber_default()`（raw: `127782.htm`）
    
    `TESTSET().testnumber_none()`（raw: `127785.htm`）
    
    `TESTSET().testname()`（raw: `127794.htm`）
    
    `TESTSET().testname_default()`（raw: `127792.htm`）
    
    `TESTSET().suppressTestNameLoopCount()`（raw: `142450.htm`）
    
    `TESTSET().testsuite()`（raw: `127796.htm`）
    
    `TESTSET().testsuite_default()`（raw: `127797.htm`）
    
    `TESTSET().testtext()`（raw: `127802.htm`）
    
    `TESTSET().testtext_none()`（raw: `127800.htm`）
    
    `TESTSET().testtype()`（raw: `127806.htm`）
    
    `TESTSET().testtype_default()`（raw: `127804.htm`）
    
    `TESTSET().hlmFmt()`（raw: `127808.htm`）
    
    `TESTSET().llmFmt()`（raw: `127809.htm`）
    
    `TESTSET().resFmt()`（raw: `127810.htm`）
    
    `TESTSET().combineMultiPortTests()`（raw: `132052.htm`）
    
    `TESTSET().addAlarm()`（raw: `345269.htm`）
  `TESTSET().judgeAndLog_FunctionalTest()`（raw: `127824.htm`）
    
    `TESTSET().judgeAndLog_ParametricTest()`（raw: `127827.htm`）
    
    `TESTSET().judgeAndLog_PmuIfvm()`（raw: `127831.htm`）
    
    `TESTSET().judgeAndLog_PmuVfim()`（raw: `127847.htm`）
    
    `TESTSET().judgeAndLog_DpsVfim()`（raw: `127851.htm`）
    
    `TESTSET().judgeAndLog_Spmu()`（raw: `127856.htm`）
    
    `TESTSET().judgeAndLog_PpmuMeasure()`（raw: `127858.htm`）
    
    `TESTSET().judgeAndLog_SpecSearch()`（raw: `127861.htm`）
    
    `TESTSET().judgeAndLog_PptiaTask()`（raw: `127863.htm`）
    
    `TESTSET().judgeAndLog_DcResultAccessor()`（raw: `127868.htm`）
    
    `TESTSET().judgeAndLog_ScanTest()`（raw: `127873.htm`）
    
    `TESTSET().doLog_ShmooTest()`（raw: `127875.htm`）

### Syntax descriptions

Placeholders used

In the syntax descriptions below, placeholders are used for certain
functions:

member_func()

Where

member_func()
 is noted, you can use any
of these member functions, individually or in combination:

`cont()`（raw: `127763.htm`）

`port()`（raw: `127776.htm`）

`reliabilty()`（raw: `127778.htm`）

`testname()`（raw: `127794.htm`）

`testname_default()`（raw: `127792.htm`）

`testnumber()`（raw: `127787.htm`）

`testnumber_default()`（raw: `127782.htm`）

`testnumber_none()`（raw: `127785.htm`）

Because
these member functions are optional, you can also omit
them. For example, when the syntax specifies

TestSet.
member_func()
.judgeAndLog_...()
,
you can use

TestSet.judgeAndLog_...()
.

judgeAndLog_...()

Where

judgeAndLog_...()
 is specified, you can
use any of the functions whose names begin with
"judgeAndLog".

Syntax descriptions

The syntax of the
TESTSET
 API depends on the effect
you want to achieve:

To use a temporary
object:

```
TESTSET().member_func().judgeAndLog_xxx(parameters);
```

To use a temporary object and define the site to be
processed:

```
TESTSET(false, site).member_func().judgeAndLog_xxx(parameters);
```

To use the system-prepared
object:

```
TestSet.member_func().judgeAndLog_xxx(parameters);
```

Note
 The system-prepared object cannot be used within the
SMC framework.

To use a user
object:

```
TESTSET obj;
obj.member_func().judgeAndLog_xxx(parameters);
```

To judge and log a functional test
result:

```
TESTSET().cont(true).judgeAndLog_FunctionalTest();
```

To judge and log the functional test result of a specific
port:

```
TESTSET().port("port").judgeAndLog_FunctionalTest();
```

To retrieve information about binning, test numbers and test names
from
tmLimits
 (see
parametric
tests
), and log the test
name:

```
TESTSET().judgeAndLog_FunctionalTest("[test name]", tmLimits);
```

To suppress the adding of numbers to test names to make them unique
when they conflict with another
name:

```
TESTSET().suppressTestnameLoopCount(true);
```

To judge and log the general parametric test results or to judge and
log the values with a defined limit,
use:

```
bool TESTSET::judgeAndLog_ParametricTest(const STRING &pin, const STRING &testname, DOUBLE value);
bool TESTSET::judgeAndLog_ParametricTest(const STRING &pin, const STRING &testname, const LIMIT& limit, DOUBLE value);
bool judgeAndLog_ParametricTest(const STRING_VECTOR &pins, const STRING &testname, const LIMIT & limit, ARRAY_D& values);
bool judgeAndLog_ParametricTest(const STRING_VECTOR &pins, const STRING &testname, V93kLimits::TMLimits& tmLimit, ARRAY_D& values);
bool judgeAndLog_ParametricTest(const STRING &pinList, const STRING &testname, const LIMIT & limit, ARRAY_D& values);
bool judgeAndLog_ParametricTest(const STRING &pinList, const STRING &testname, V93kLimits::TMLimits& tmLimit, ARRAY_D& values);
bool judgeAndLog_ParametricTest(const STRING_VECTOR& pins, const STRING& testname, ARRAY_D& values);
```

To judge and log the DC test results,
use:

```
bool TESTSET::judgeAndLog_PmuIfvm(const PMU_IFVM &pmuIfvm);
bool TESTSET::judgeAndLog_PmuVfim(const PMU_IFVM &pmuVfim);
bool TESTSET::judgeAndLog_DpsVfim(const DPS_VFIM &dpsVfim);
bool TESTSET::judgeAndLog_Dps(const DPS_TASK &dpsTask);
bool TESTSET::judgeAndLog_Spmu(const SPMU_TASK &spmuTask);
bool TESTSET::judgeAndLog_PpmuMeasure(const PPMU_MEASURE &ppmuMeas);
```

To judge and log the result of a spec search,
use:

```
bool TESTSET::judgeAndLog_SpecSearch(const SPEC_SEARCH &specSearch);
```

To judge and log the result of a ppTIA measurement,
use:

```
bool TESTSET::judgeAndLog_PptiaTask(const PPTIA_TASK &pptiaTask);
```

To judge and log scan test results,
use:

```
bool TESTSET::judgeAndLog_ScanTest(const SCAN_TEST_RESULT& scanTest);
```

To judge and log the result of a shmoo
test:

```
void doLog_ShmooTest(const std::string &testname, const ShmooData& shmooData);
```

### Examples

### Example 1: Using the same condition for multiple tests

If you wish
to use the same condition for multiple TEST member functions, you can program the
condition for the class object of the
TESTSET
. In this example,
the conditions are set in the first line and effective for all the following three
tests.

```
double dIdd1, dIdd2, dIdd3;

TESTNUMBER sdc6 = GET_TESTNUMBER("SDC_6");

TestSet.cont(true).testnumber(sdc6);

TestSet.TEST("Vcc","test1",dIdd1);
TestSet.TEST("Vcc","test2",dIdd2);
TestSet.TEST("Vcc","test3",dIdd3);
```

### Example 2: Generating test numbers

The
TESTSET

class can be used as a programmable interface for generating test numbers for each
test in a test suite by assigning offset and increment values that iterate based on
the number of calls. The examples below use the offset and increment values as shown
in the table below.

[表]
列: Test Name | Offset | Increment
行 1:
  ADC_1
  777
  3
行 2:
  DAC_1
  723
  

Note
 The following
TESTSET
 examples use the term
"subtest Test Number". A "subtest Test Number" refers to the number that is stored
in the EDL. The numbers assigned to a test result can be modified and are affected
by default and user-selectable numbering parameters. In this sense these test
numbers are
temporary.

```
TESTSET adc_1, dac_1;

adc_1.testnumber("ADC_1").TEST(...); // subtest Test Number = 777(777 + 3 * 0)

adc_1.TEST(...); //subtest Test Number = 780 (777 + 3 * 1)
adc_1.TEST(...); //subtest Test Number = 783 (777 + 3 * 2)

dac_1.testnumber("DAC_1")

dac_1.TEST(); //subtest Test Number = 723 (723 + 0 * 0)
dac_1.TEST(); //subtest Test Number = 723 (723 + 0 * 1)
dac_1.TEST(); //subtest Test Number = 723 (723 + 0 * 2)
```

In
this example the adc_1 test suite is assigned an offset of 777 and an increment of
3, which results in assigning every subtest result a distinct subtest Test Number.
The dac _1 test suite is assigned only an offset value, with no increment, which
results in all subtest iterations having a subtest Test Number value of
723.

### Example 3: Test number related methods

The following example shows
how a sequence of tests in a test suite might be numbered using the

TESTSET
 class API with test number member functions.

[表]
列: Test Name | Offset | Increment
行 1:
  DEFAULT FUNCTIONAL TEST
  1000
  20
行 2:
  Func
  2000
  50
[表]
列: | subtest Test Number
行 1:
  TestSet.TEST();
  1000
行 2:
  TestSet.TEST();
  1020
行 3:
  TestSet.TEST();
  1040
行 4:
  
  
行 5:
  TestSet.testnumber("Func").TEST();
  2000
行 6:
  TestSet.TEST();
  2050
行 7:
  TestSet.TEST();
  2100
行 8:
  
  
行 9:
  TestSet.testnumber(3000).TEST();
  3000
行 10:
  TestSet.TEST();
  3000
行 11:
  TestSet.TEST();
  3000
行 12:
  
  
行 13:
  TestSet.testnumber_none().TEST();
  ---
行 14:
  TestSet.TEST();
  ---
行 15:
  TestSet.TEST();
  ---
行 16:
  
  
行 17:
  TESTNUMBER testnumber(4000, 100);
  
行 18:
  TestSet.testnumber(testnumber).TEST();
  4000
行 19:
  TestSet.TEST();
  4100
行 20:
  TestSet.TEST();
  4200
行 21:
  
  
行 22:
  TestSet.testnumber_default().TEST();
  1060
行 23:
  TestSet.TEST();
  1080
行 24:
  TestSet.TEST();
  1100

### Example 4: Judge and Log Examples
```
ON_FIRST_INVOCATION_BEGIN();

FUNCTIONAL_TEST();

ON_FIRST_INVOCATION_END();

TESTSET().judgeAndLog_FunctionalTest();
```

The
first three lines perform a functional test for multi-site parallel, and the last
line performs the judging and logging for each site
respectively.

```
double thd_result, snr_result;

TESTSET().cont(true).judgeAndLog_ParametricTest("dgtz_pin", "THD", thd_result);
TESTSET().judgeAndLog_ParametricTest("dgtz_pin", "SNR", snr_result);
```

The
first
judgeAndLog_ParametricTest()
 judges the

thd_result
 data as pass or fail. Then, the second one judges
the
snr_result
 data as pass or fail because the

TESTSET().cont(true)
 is called in advance. When the result of
the first
judgeAndLog_ParametricTest()
 is pass, the test will
continue even if you do not call the
cont(true)
 member
function.

```
double low_limit, high_limit, thd_result;

TESTSET().judgeAndLog_ParametricTest("Aout", THD",LIMIT(TM::GT, low_limit, TM::LT, high_limit), thd_result);
```

The

judgeAndLog_ParametricTest()
 compares the thd_result data
with the limit range specified by the LIMIT API, then judges as pass or
fail.

```
TESTSET().judgeAndLog_ParametricTest("I/O0","ft_test",tmLimits,VMeas);
```

In
this example,
Vmeas
 is the variable containing the measured
value. The
judgeAndLog_ParametricTest()
 compares the value of

VMeas
 with the limit range of the test name

ft_test
 in the loaded test table. To use

tmLimits
, add the following two lines to the test
method:

```
#include "TMLimits.h"
using V93kLimits::tmLimits;
```

The
following example illustrates the binning rule of
tmLimits
, which
bins on the first fail.

```
TESTSET().cont(true).judgeAndLog_ParametricTest(pin,"param1",tmLimits,value1);
TESTSET().cont(true).judgeAndLog_ParametricTest(pin,"param2",tmLimits,value2);
```

with

[表]
列: Test name | Bin_s_num | Bin_h_num
行 1:
  param1
  22
  2
行 2:
  param2
  33
  3

Final bin depending on the parameters results:

[表]
列: param1 result | param2 result | Final bin (software / hardware bin)
行 1:
  Pass
  Fail
  33/3
行 2:
  Fail
  Pass
  22/2
行 3:
  Fail
  Fail
  22/2

The following example logs the result of a group of pins in one MPR if the
STDF configuration option
enableMPR
 is set to
True

(See the description of
enableMPR
 in
`Configuring the contents of an STDF file`（raw: `70623.htm`）
).

```
PMU_VFIM pmuVfim(Pins);

ON_FIRST_INVOCATION_BEGIN();

pmuVfim.vForce(Vforce)
.iClamp(IClp*1E-6)
.limits("Idd")
.preAction("NONE")
.settling(SoakT*1E-3)
.execute(TM::PVAL);

ON_FIRST_INVOCATION_END();

TESTSET VfIm;

VfIm.testnumber(505).cont(TRUE).judgeAndLog_PmuVfim(pmuVfim);
```

### Example 5: Using TESTSET() in SMC background processing

The example shows how to implement
TESTSET()
 for SMC background
processing. The example contains the code for two versions of the background
process:

SMC background process per site

Common SMC background process for all active sites

The example requires that the test limits are defined by a CSV file. For more
information refer to
`TMLimits`（raw: `110432.htm`）
 and
`Working with TMLimits`（raw: `118940.htm`）
.

The following definition of test method member variables is required in the

protected
 section of the test method
class:

```
protected:
string mSMCMode;
string mPinList;
string mTestSuite;
string mTestName;
int mMeasurements;
int mOffline;
ARRAY_I mActiveSites;
```

A DC value test is defined in the
run()
 method of the test class.
Result processing is performed in an SMC background process per site or in a common
SMC background process for all active
sites.

```
virtual void run()
{
PATTERN_CONTROLLER patternCtrl;

ON_FIRST_INVOCATION_BEGIN();
{
//
// Prepare
//
mSMCMode = "COMMON_THREAD"; // "THREAD_PER_SITE" or "COMMON_THREAD"
mPinList = "PS1600_1,PS1600_2";
mTestName = "Test 1";
mMeasurements = 1;

GET_SYSTEM_FLAG("offline",&mOffline);
GET_TESTSUITE_NAME(mTestSuite);

RESULT_AREA_CONFIG_SET resultArea(mTestSuite);

resultArea.pin(mPinList).setDcValueResultAreaSize(mMeasurements);

//
// Create setup for DC value measurement
//
...
...

//
// Execute
//
resultArea.setAsPrimary();

CONNECT();

SMC_FUNCTIONAL_TEST();

resultArea.deselectGlobally();

//
// Result processing
//
if (mSMCMode == "THREAD_PER_SITE")
{
//--------------------------------------------------------------
// SMC background thread per site
//--------------------------------------------------------------
FOR_EACH_SITE_BEGIN();
{
SMC_ARM();
}
FOR_EACH_SITE_END();
}
else if (mSMCMode == "COMMON_THREAD")
{
//--------------------------------------------------------------
// Common SMC background thread for all active sites
//
// Note: The array of currently active sites must be stored
// in the member variable mActiveSites.
//--------------------------------------------------------------
GET_ACTIVE_SITES(mActiveSites);

SMC_ARM();
}
else
{
cout << "Invalid SMC mode \"" << mSMCMode << "\"." << endl;
}
}
ON_FIRST_INVOCATION_END();

return;
}
```

The SMC background processing method of the test class is to be defined in the

public

section:

```
//
// The SMC background processing method; armed by SMC_ARM() in the run() method above
//
virtual void SMC_backgroundProcessing()
{
DC_RESULT_ACCESSOR resultAccess(mTestSuite);
STRING_VECTOR pinVector;

//
// Prepare
//
pinVector = PinUtility.getDigitalPinNamesFromPinList(mPinList,TM::ALL_DIGITAL);

cout << "SMC_backgroundProcessing for SMC mode \""
<< mSMCMode << "." << endl << flush;

if (mSMCMode == "THREAD_PER_SITE")
{
//------------------------------------------------------------------
// Thread per site
//------------------------------------------------------------------
TESTSET testSet;

if (!mOffline)
{
resultAccess.uploadResult(mPinList, TM::RESULT_INDEX);
}

for (uint pinIndex = 0; pinIndex < pinVector.size(); pinIndex++)
{
ARRAY_D results = resultAccess.getValues(pinVector[pinIndex]);

for (int resultIndex = 0; resultIndex < mMeasurements; resultIndex++)
{
cout << "\t\tProcessing data for site " << SMC_SITE_NUMBER()
<< ", pin " << pinVector[pinIndex]
<< ", result " << resultIndex + 1 << endl << flush;

testSet.cont(true).judgeAndLog_ParametricTest(pinVector[pinIndex],
mTestName, V93kLimits::tmLimits,
(mOffline) ? 1 : results[resultIndex]);

} // for (int resultIndex ...

} // for (uint pinIndex ...
}
else if (mSMCMode == "COMMON_THREAD")
{
//------------------------------------------------------------------
// Common thread for all active sites
//
// Note: The common thread requires that the array mActiveSites
// has been filled in the calling run() method.
//------------------------------------------------------------------
for (int siteIndex = 0; siteIndex < mActiveSites.size(); siteIndex++)
{
if(!mOffline)
{
resultAccess.uploadResult(mActiveSites[siteIndex],
mPinList,TM::RESULT_INDEX,
TM::RESULT_RANGE(TM::RESULT_INDEX,0,mMeasurements));
}

//
// Create new TESTSET using the current site as parameter
//
TESTSET testSet (false, mActiveSites[siteIndex]);

for (uint pinIndex = 0; pinIndex < pinVector.size(); pinIndex++)
{
ARRAY_D results = resultAccess.getValues(mActiveSites[siteIndex],
pinVector[pinIndex]);

for(int resultIndex = 0; resultIndex < mMeasurements; resultIndex++)
{
cout << "\t\tProcessing data for site " << mActiveSites[siteIndex]
<< ", pin " << pinVector[pinIndex]
<< ", result " << resultIndex + 1 << endl << flush;

testSet.cont(true).judgeAndLog_ParametricTest(pinVector[pinIndex],
mTestName, V93kLimits::tmLimits,
(mOffline) ? 1 : results[resultIndex]);

} // for (int resultIndex ...

} // for (uint pinIndex ...

} // for (int siteIndex ...
}
else
{
cout << "Invalid SMC mode \"" << mSMCMode << "\"." << endl;
}

} // virtual void SMC_backgroundProcessing()
```

Note

The example above contains several calls of
cout
 in function
`SMC_backgroundProcessing()`（raw: `120107.htm#_120107__s_SMC_backgroundProcessing`）
.
cout
 is not
thread safe. In production test
cout
 must never be used in a
background process.

When using
cout
 in a background process,
you have to expect a mix up of the output in the

ui_report
 window and possibly other unwanted
behavior. For more information, refer to
`Thread safety`（raw: `118825.htm`）
.

### Syntax（取自子主题 TESTSET().addAlarm()）

```
TESTSET & addAlarm(const STRING &alarmId);
TESTSET & addAlarm(const STRING &alarmId, const bool setToFail);
```

[表]
列: Parameter | Description
行 1:
  alarmId
  The alarm ID that is stored in the EDL as an `AlarmAttribute`（raw: `345285.htm`）
    for a test result.
行 2:
  setToFail
  If this parameter is true, the test result is
    forced to fail.
    
    If the parameter is false, the test result is
    not changed by this alarm.
    
    This parameter is optional. The default is
    true.

### Example（取自子主题 TESTSET().addAlarm()）

```
TESTSET().cont(true).addAlarm("myAlarmCondition").judgeAndLog_FunctionalTest();
```

### Syntax（取自子主题 TESTSET().combineMultiPortTests()）

```
TESTSET & combineMultiPortTests(bool combine);
```
[表]
列: Parameter | Description
行 1:
  combine
  Whether to combine the result FTR records into one for multiport tests:
    
    true: One combined FTR record is created.
    
    false: A separate FTR record is created for each port.
    
    The default setting is false.

### Syntax（取自子主题 TESTSET().cont()）

```
TESTSET & cont (bool overon);
```
[表]
列: Parameter | Description
行 1:
  overon
  This parameter is used to decide whether or not the test should be continued if a
    test result fails:
    
    If you want to continue the test even if the test fails, set this flag to TRUE. When the
    test result is pass, the test program continues to execute. Instead of the expressions,
    TRUE or FALSE, you can use an enumerator supported by the system.
    
    Note that the API behaves differently for the first site in a multisite setup. In this
    special situation, the test is always continued, even if the test result fails and the
    parameter is set to FALSE. For the following sites, the test is terminated under these
    conditions.

### Example（取自子主题 TESTSET().cont()）

With the following setting, the test will be continued even if the test
fails.

```
TestSet.cont(true);
```

### Syntax（取自子主题 TESTSET().doLog_ShmooTest()）

```
void doLog_ShmooTest(const std::string &testname, const ShmooData& shmooData, int logTestNumber = DEFAULT_LOGTESTNUMBER_VALUE);
void doLog_ShmooTest(const ShmooDataStore &shmooDataStore, int logTestNumber = DEFAULT_LOGTESTNUMBER_VALUE);
```
[表]
列: Parameter | Description
行 1:
  testname
  The test name to log.
    
    Test names can contain any printable ASCII characters, that is, characters with codes from 32
    to 126. This includes the space, digits, lowercase letters, uppercase letters, and these
    punctuation characters: !"#$%&'()*+,-./:;<=>@?[\]^_`{|}~ There is no fixed maximum length
    for the names in SmarTest. However, STDF limits test names to 255 characters, so test names
    should not be longer if STDF data logging is intended.
行 2:
  shmooData
  The `ShmooData`（raw: `110842.htm`） object to log.
行 3:
  shmooDataStore
  
行 4:
  logTestNumber
  An optional test number.
    
    If this test number is provided, it overrides the actual test number. If it is not
    provided, the actual test number is logged.

### Example（取自子主题 TESTSET().doLog_ShmooTest()）

```
ShmooData shmooData;
...
TESTSET().doLog_ShmooTest("shmoo TestMethod", shmooData);
```

### Syntax（取自子主题 TESTSET().hlmFmt()）

```
TESTSET & hlmFmt(const STRING &format);
```
[表]
列: Parameter | Description
行 1:
  format
  A string describing the desired format. The string is a standard ANSI C format
    string, for example, "%7.3f".

### Example（取自子主题 TESTSET().hlmFmt()）

```
TestSet.hlmFmt("%7.3f");
```

### Syntax（取自子主题 TESTSET().judgeAndLog_DcResultAccessor()）

```
bool judgeAndLog_DcResultAccessor(const DC_RESULT_ACCESSOR &dc, INT logTestNumber = DEFAULT_LOGTESTNUMBER_VALUE);
```
[表]
列: Parameter | Description
行 1:
  dc
  The `DC_RESULT_ACCESSOR`（raw: `99071.htm`） object from which the test data is taken.
行 2:
  logTestNumber
  An optional test number.
    
    If this test number is provided, it overrides the actual test number. If it is not
    provided, the actual test number is logged.

Note
  Only the first six digits of values are ensured to be correctly
logged into the STDF file.

### Return Value（取自子主题 TESTSET().judgeAndLog_DcResultAccessor()）

The pass/fail result of the judgment is returned. It can be
true for pass or false for fail.

### Example（取自子主题 TESTSET().judgeAndLog_DcResultAccessor()）

```
DC_RESULT_ACCESSOR dcAccessor;
...
TestSet.judgeAndLog_DcResultAccessor(dcAccessor);
```

### Syntax（取自子主题 TESTSET().judgeAndLog_Dps()）

```
bool judgeAndLog_Dps(const DPS_TASK &dpsTask, INT logTestNumber = DEFAULT_LOGTESTNUMBER_VALUE);
```
[表]
列: Parameter | Description
行 1:
  dpsTask
  Specifies a `DPS_TASK`（raw: `55630.htm`） object to be judged.
行 2:
  logTestNumber
  An optional test number.
    
    If this test number is provided, it overrides the actual test number. If it is not
    provided, the actual test number is logged.

Note
  Only the first six digits of values are ensured to be correctly
logged into the STDF file.

### Return Value（取自子主题 TESTSET().judgeAndLog_Dps()）

The pass/fail result of the judgment is returned. It can be
true for pass or false for fail.

### Example（取自子主题 TESTSET().judgeAndLog_Dps()）

The following example performs a DPS global pass/fail measurement on pin Vcc and Vee
with the current primary
set.

```
DPS_TASK dpsTask;
static STRING tsName;
ON_FIRST_INVOCATION_BEGIN();
CONNECT();
GET_TESTSUITE_NAME(tsName);
dpsTask.pin("Vcc").min(0 A).max(0.1 A);
dpsTask.pin("Vee").min(0 A).max(0.2 A);
dpsTask.execMode(TM::GPF);
dpsTask.trigMode(TM::INTERNAL);
dpsTask.execute();
ON_FIRST_INVOCATION_END();
TESTSET().judgeAndLog_Dps(dpsTask);
```

### Syntax（取自子主题 TESTSET().judgeAndLog_DpsVfim()）

```
bool judgeAndLog_DpsVifm(const DPS_VFIM &dpsVfim, INT logTestNumber = DEFAULT_LOGTESTNUMBER_VALUE);
```
[表]
列: Parameter | Description
行 1:
  dpsVifm
  The `DPS_VIFM`（raw: `28775.htm`） constructor which specifies a DC test to
    be judged.
行 2:
  logTestNumber
  An optional test number.
    
    If this test number is provided, it overrides the actual test number. If it is not
    provided, the actual test number is logged.

Note
  Only the first six digits of values are ensured to be correctly
logged into the STDF file.

### Return Value（取自子主题 TESTSET().judgeAndLog_DpsVfim()）

The pass/fail result of the judgment is returned. It can be
true for pass or false for fail.

### Example（取自子主题 TESTSET().judgeAndLog_DpsVfim()）

```
DPS_VFIM dps("@");
dps.min_current(1).max_current(3).preAction("NONE");
dps.execute();
bool rslt = dps.getPassFail();
if(rslt)
cout << "GPF: PASS" << endl;
else
cout << "GPF: FAIL" << endl;
TESTSET().judgeAndLog_DpsVfim(dps);
```

### Parameters（取自子主题 TESTSET().judgeAndLog_FunctionalTest()）

The supported parameters are listed in the following table:

[表]
列: Parameter | Description
行 1:
  result
  Pass/fail result of functional test to log.
行 2:
  site
  Site number to log.
行 3:
  testname
  Test name defined in the test table.
    
    Test names can contain any printable ASCII characters, that is, characters with codes from 32
    to 126. This includes the space, digits, lowercase letters, uppercase letters, and these
    punctuation characters: !"#$%&'()*+,-./:;<=>@?[\]^_`{|}~ There is no fixed maximum length
    for the names in SmarTest. However, STDF limits test names to 255 characters, so test names
    should not be longer if STDF data logging is intended.
行 4:
  tmLimit
  Object of `TMLimits`（raw: `110432.htm`） for the loaded test table. You can use the default
    instance tmLimits.
行 5:
  label
  Label to log.

The following function calls can be used within the SMC framework:

bool judgeAndLog_FunctionalTest(bool result, const STRING& label);

bool judgeAndLog_FunctionalTest(const STRING& testname, V93kLimits::TMLimits&
tmLimit, bool result, const STRING& label);

### Return Value（取自子主题 TESTSET().judgeAndLog_FunctionalTest()）

The pass/fail result of the judgment, where true is returned
for pass and false for fail.

### Example（取自子主题 TESTSET().judgeAndLog_FunctionalTest()）

```
ON_FIRST_INVOCATION_BEGIN();
FUNCTIONAL_TEST();
ON_FIRST_INVOCATION_END();
TESTSET().cont(true).judgeAndLog_FunctionalTest("funcTest1", tmLimits);
```

### Syntax（取自子主题 TESTSET().judgeAndLog_ParametricTest()）

```
bool judgeAndLog_ParametricTest(const STRING& pin, const STRING& testname, double value, INT logTestNumber = DEFAULT_LOGTESTNUMBER_VALUE, char* softBin = "", INT hardbin = -1);
bool judgeAndLog_ParametricTest(const STRING& pin, const STRING& testname, const LIMIT& limit, double value, INT logTestNumber = DEFAULT_LOGTESTNUMBER_VALUE, char* softBin = "", INT hardbin = -1);
bool judgeAndLog_ParametricTest(const STRING& pin, const STRING& testname, V93kLimits::TMLimits& tmLimit, double value, INT logTestNumber = DEFAULT_LOGTESTNUMBER_VALUE, char* softBin = "", INT hardbin = -1);
bool judgeAndLog_ParametricTest(const STRING& pinList, const STRING& testname, const LIMIT& limit, ARRAY_D& values, INT logTestNumber = DEFAULT_LOGTESTNUMBER_VALUE, char* softBin = "", INT hardbin = -1);
bool judgeAndLog_ParametricTest(const STRING& pinList, const STRING& testname, V93kLimits::TMLimits& tmLimit, ARRAY_D& values, INT logTestNumber = DEFAULT_LOGTESTNUMBER_VALUE, char* softBin = "", INT hardbin = -1);
bool judgeAndLog_ParametricTest(const STRING_VECTOR& pins, const STRING& testname, ARRAY_D& values, INT logTestNumber = DEFAULT_LOGTESTNUMBER_VALUE, char* softBin = "", INT hardbin = -1);
bool judgeAndLog_ParametricTest(const STRING_VECTOR& pins, const STRING& testname, const LIMIT& limit, ARRAY_D& values, INT logTestNumber = DEFAULT_LOGTESTNUMBER_VALUE, char* softBin = "", INT hardbin = -1);
bool judgeAndLog_ParametricTest(const STRING_VECTOR& pins, const STRING& testname, V93kLimits::TMLimits& tmLimit, ARRAY_D& values, INT logTestNumber = DEFAULT_LOGTESTNUMBER_VALUE, char* softBin = "", INT hardbin = -1);
```
[表] Parameters
列: Parameter | Description
行 1:
  pin
  The name for a single pin.
行 2:
  pinList
  The list of pins to be measured, separated with commas.
行 3:
  pins
  The pins to be measured.
行 4:
  testname
  For bool TEST(const STRING& pin, const STRING& testname, double
    value);: The test name that is referred from the Properties view.
    
    For bool TEST(const STRING& pin, const STRING& testname, const LIMIT&
    limit, double value);: The test name that is used to create a `TestNameAttr`（raw: `34701.htm`）.
    
    Test names can contain any printable ASCII characters, that is, characters with codes from 32
    to 126. This includes the space, digits, lowercase letters, uppercase letters, and these
    punctuation characters: !"#$%&'()*+,-./:;<=>@?[\]^_`{|}~ There is no fixed maximum length
    for the names in SmarTest. However, STDF limits test names to 255 characters, so test names
    should not be longer if STDF data logging is intended.
行 5:
  value
  The test result value.
行 6:
  limit
  The limit value to be used for the judgment. This parameter is a `LIMIT`（raw: `29504.htm`） API class object. Hence, you can specify TM::Pass
    or TM::Fail to make the test result pass or fail intentionally.
    
    This parameter is optional, except in the case of bool TEST(const STRING&
    pin, const STRING& testname, const LIMIT& limit, double value);.
行 7:
  tmLimit
  Specifies the `TMLimits`（raw: `110432.htm`） object from which the limit data are taken.
行 8:
  logTestNumber
  An optional test number.
    
    If this test number is provided, it overrides the actual test number. If it is not
    provided, the actual test number is logged.
行 9:
  hardBin
  The hardware bin number of the multibin. For details see the `SET_MULTIBIN`（raw: `100114.htm`）
    API.
行 10:
  softBin
  The software bin number of the multibin. For details see the `SET_MULTIBIN`（raw: `100114.htm`）
    API.

Note
 Only the first six digits of values are ensured to be logged to the
STDF file correctly.

The following function calls can be used within the SMC
framework:

bool judgeAndLog_ParametricTest(const STRING& pin, const
STRING& testname, double value);

bool
judgeAndLog_ParametricTest(const STRING& pin, const STRING& testname, const LIMIT&
limit, double value);

bool judgeAndLog_ParametricTest(const STRING&
pin, const STRING& testname, V93kLimits::TMLimits& tmLimit, double
value);

bool judgeAndLog_ParametricTest(const STRING_VECTOR& pins,
const STRING& testname, ARRAY_D& values);

bool
judgeAndLog_ParametricTest(const STRING_VECTOR& pins, const STRING& testname, const
LIMIT& limit, ARRAY_D& values);

bool
judgeAndLog_ParametricTest(const STRING_VECTOR& pins, const STRING& testname,
V93kLimits::TMLimits& tmLimit, ARRAY_D& values);

### Return Value（取自子主题 TESTSET().judgeAndLog_ParametricTest()）

The pass/fail result of the judgment, where true is returned
for pass and false for fail.

### Examples（取自子主题 TESTSET().judgeAndLog_ParametricTest()）

### Limit
```
LIMIT limit;
DOUBLE value1;
...
TESTSET().judgeAndLog_ParametricTest("Vcc", "Leakage",limit, value1);
```

### tmLimit binning rule
```
TESTSET().cont(true).judgeAndLog_ParametricTest(pin,"param1",tmLimits,value1);
TESTSET().cont(true).judgeAndLog_ParametricTest(pin,"param2",tmLimits,value2);
```

with

[表]
列: Test name | Bin_s_num | Bin_h_num
行 1:
  param1
  22
  2
行 2:
  param2
  33
  3

Final bin depending on the parameters results:

[表]
列: param1 result | param2 result | Final bin (software / hardware bin)
行 1:
  Pass
  Fail
  33/3
行 2:
  Fail
  Pass
  22/2
行 3:
  Fail
  Fail
  22/2

### Syntax（取自子主题 TESTSET().judgeAndLog_PmuIfvm()）

```
bool judgeAndLog_PmuIfvm(const PMU_IFVM &pmuIfvm, INT logTestNumber = DEFAULT_LOGTESTNUMBER_VALUE);
```
[表]
列: Parameter | Description
行 1:
  pmuIfvm
  The `PMU_IFVM`（raw: `29543.htm`） constructor which specifies a DC test to be judged.
行 2:
  logTestNumber
  An optional test number.
    
    If this test number is provided, it overrides the actual test number. If it is not
    provided, the actual test number is logged.

Note
  Only the first six digits of values are ensured to be correctly
logged into the STDF file.

### Return Value（取自子主题 TESTSET().judgeAndLog_PmuIfvm()）

The pass/fail result of the judgment is returned. It can be
true for pass or false for fail.

### Syntax（取自子主题 TESTSET().judgeAndLog_PmuVfim()）

```
bool judgeAndLog_PmuVfim(const PMU_VFIM &pmuVfim, INT logTestNumber = DEFAULT_LOGTESTNUMBER_VALUE);
```
[表]
列: Parameter | Description
行 1:
  pmuVfim
  The `PMU_VFIM`（raw: `29563.htm`） constructor which specifies a DC test to be judged.
行 2:
  logTestNumber
  An optional test number.
    
    If this test number is provided, it overrides the actual test number. If it is not
    provided, the actual test number is logged.

Note
  Only the first six digits of values are ensured to be correctly
logged into the STDF file.

### Return Value（取自子主题 TESTSET().judgeAndLog_PmuVfim()）

The pass/fail result of the judgment is returned. It can be
true for pass or false for fail.

### Syntax（取自子主题 TESTSET().judgeAndLog_PpmuMeasure()）

```
bool judgeAndLog_PpmuMeasure(const PPMU_MEASURE &ppmuMeas, INT logTestNumber = DEFAULT_LOGTESTNUMBER_VALUE);
```
[表]
列: Parameter | Description
行 1:
  ppmuMeas
  The `PPMU_MEASURE`（raw: `29585.htm`） constructor specifies a flexible DC test to be
    judged.
行 2:
  logTestNumber
  An optional test number.
    
    If this test number is provided, it overrides the actual test number. If it is not
    provided, the actual test number is logged.

Note
  Only the first six digits of values are ensured to be correctly
logged into the STDF file.

### Return Value（取自子主题 TESTSET().judgeAndLog_PpmuMeasure()）

The pass/fail result of the judgment is returned. It can be
true for pass or false for fail.

### Example（取自子主题 TESTSET().judgeAndLog_PpmuMeasure()）

```
PPMU_MEASURE ppmuMeasure;
ON_FIRST_INVOCATION_BEGIN();
PPMU_SETTING ppmuSetting;
PPMU_RELAY ppmuRelayOn, acRelayOn;
TASK_LIST simpleFlexDc;
ppmuSetting.pin("I/O1").vForce(0 V).iRange(1 uA).max(1 uA).min(-1 uA);
ppmuSetting.pin("I/O2").iForce(1 uA).iRange(1 uA).max(0.5 V).min(1 V);
ppmuRelayOn.pin("I/O1,I/O2").status("PPMU_ON");
ppmuRelayOn.wait(1.3 ms);
ppmuMeasure.pin("I/O1").execMode(TM::PPF);
ppmuMeasure.pin("I/O2").execMode(TM::PVAL);
acRelayOn.pin("I/O1,I/O2").status("AC_ON");
simpleFlexDc.add(ppmuSetting).add(ppmuRelayOn).add(ppmuMeasure).add(acRelayOn);
simpleFlexDc.execute();
ON_FIRST_INVOCATION_END();
TESTSET().judgeAndLog_PpmuMeasure(ppmuMeasure);
```

### Syntax（取自子主题 TESTSET().judgeAndLog_PptiaTask()）

```
bool judgeAndLog_PptiaTask(const PPTIA_TASK & pptiaTask, INT logTestNumber = DEFAULT_LOGTESTNUMBER_VALUE);
```
[表]
列: Parameter | Description
行 1:
  pptiaTask
  The `PPTIA_TASK`（raw: `86641.htm`） object from which the test data is taken.
行 2:
  logTestNumber
  An optional test number.
    
    If this test number is provided, it overrides the actual test number. If it is not
    provided, the actual test number is logged.

Note
  Only the first six digits of values are ensured to be correctly
logged into the STDF file.

### Return Value（取自子主题 TESTSET().judgeAndLog_PptiaTask()）

The pass/fail result of the judgment is returned. It can be
true for pass or false for fail.

### Example（取自子主题 TESTSET().judgeAndLog_PptiaTask()）

```
INT debug;
PPTIA_TASK task1;
GET_TESTFLOW_FLAG ("debug_analog", &debug);
ON_FIRST_INVOCATION_BEGIN();
task1.pin(tia_pin).eventASlope(TM::RISE).eventAThreshold(1000 mV).eventACount(0) ;
task1.pin(tia_pin).eventBSlope(TM::RISE).eventBThreshold(1000 mV).eventBCount(N) ;
task1.pin(tia_pin).armingMethod(TM::EVENT_A_FIRST) ;
task1.pin(tia_pin).limits("per_s",TM::MEAN) ;
task1.preAction(TM::SET_TIA_MODE).execute() ;
ON_FIRST_INVOCATION_END();
TESTSET().judgeAndLog_PptiaTask(task1);
```

This
example performs a period measurement with PPTIA on
tia_pin
.

tia_pin
 is the test method parameter holding the pin(s) to be measured.

N
 is the test method parameter holding the number of events.

### Syntax（取自子主题 TESTSET().judgeAndLog_ScanTest()）

```
bool judgeAndLog_ScanTest(const SCAN_TEST_RESULT& scanTest);
```
[表]
列: Parameter | Description
行 1:
  scanTest
  The `SCAN_TEST_RESULT`（raw: `117961.htm`） object from which the scan test result is taken.

Note
 Only the first six digits of values are ensured to be logged to the
STDF file correctly.

### Return Value（取自子主题 TESTSET().judgeAndLog_ScanTest()）

The pass/fail result of the judgment, where true is returned
for pass and false for fail.

### Example（取自子主题 TESTSET().judgeAndLog_ScanTest()）

In the following example, scanPins, maxFailsPerPin, cycleBased, includeExpectedData
and testerCycleMode are input parameters defined for the test
method.

```
ERROR_MAP_TEST emap(testerCycleMode ? TM::TESTER_CYCLES : TM::XMODE_CYCLES);
SCAN_TEST_RESULT log(cycleBased ? TM::CYCLE_BASED_LOGGING : TM::PATTERN_BASED_LOGGING);

ON_FIRST_INVOCATION_BEGIN();
/* Setup the error map */
emap.pin(scanPins).setLocation(TM::RAM)
.setRecordingMode(TM::PF).setStartCycle(0);
/* Execute functional test */
CONNECT();
FUNCTIONAL_TEST();
ON_FIRST_INVOCATION_END();

/* If functional test has passed, no further processing has to be done */
if(GET_FUNCTIONAL_RESULT())
{
return S_OK;
}

/* Retrieve the overall failures for this site */
log.totalFailures(emap.getErrorCount());
log.totalCyclesExecuted(emap.getLastCycleExecuted());

STRING_VECTOR pins =
PIN_UTILITY::getDigitalPinNamesFromPinList(scanPins,TM::O_PIN | TM::IO_PIN);

/* Retrieve the failing cycles per pin for this site */
for(int i=0; i<pins.size(); i++)
{
INT failsToUpload = 1;
if(-1 == maxFailsPerPin)
{
failsToUpload = emap.pin(pins[i]).getErrorCount();
}
else {
failsToUpload = maxFailsPerPin;
}

ARRAY_LL cycles;
emap.pin(pins[i]).getFirstFailingCycles(0, failsToUpload, cycles);
log.pin(pins[i]).failingCycles(cycles);

if(includeExpectedData)
{
ARRAY_CHAR expected;
emap.pin(pins[i]).getExpectedDataForCycles(cycles, expected);
log.pin(pins[i]).expectedData(expected);
}
}
/* Push the failures to datalog */
TESTSET().cont(true).judgeAndLog_ScanTest(log);
```

### Syntax（取自子主题 TESTSET().judgeAndLog_SpecSearch()）

```
bool judgeAndLog_SpecSearch(const SPEC_SEARCH &specSearch, INT logTestNumber = DEFAULT_LOGTESTNUMBER_VALUE);
```
[表]
列: Parameter | Description
行 1:
  specSearch
  The `SPEC_SEARCH`（raw: `29753.htm`） API class object that specifies a spec search
    measurement to be judged.
行 2:
  logTestNumber
  An optional test number.
    
    If this test number is provided, it overrides the actual test number. If it is not
    provided, the actual test number is logged.

Note
  Only the first six digits of values are ensured to be correctly
logged into the STDF file.

### Return Value（取自子主题 TESTSET().judgeAndLog_SpecSearch()）

The pass/fail result of the judgment is returned. It can be
true for pass or false for fail.

### Example（取自子主题 TESTSET().judgeAndLog_SpecSearch()）

```
SPEC_SEARCH search_1("freq",TM::TIM);
search_1.specPins("CPandMR").method(TM::Linear).unit("Hz").start(50).stop(70).numberOfSteps(20).resolution(0.01);
search_1.execute();
TESTSET().judgeAndLog_SpecSearch(search_1);
```

This
function executes a spec search test on the pin "
CPandMR
". The test result is
judged and logged with TESTSET API.

### Syntax（取自子主题 TESTSET().judgeAndLog_Spmu()）

```
bool judgeAndLog_Spmu(const SPMU_TASK &spmuTask, INT logTestNumber = DEFAULT_LOGTESTNUMBER_VALUE);
```
[表]
列: Parameter | Description
行 1:
  spmuTask
  Specifies an `SPMU_TASK`（raw: `55670.htm`） object to be judged.
行 2:
  logTestNumber
  An optional test number.
    
    If this test number is provided, it overrides the actual test number. If it is not
    provided, the actual test number is logged.

Note
  Only the first six digits of values are ensured to be correctly
logged into the STDF file.

### Return Value（取自子主题 TESTSET().judgeAndLog_Spmu()）

The pass/fail result of the judgment is returned. It can be
true for pass or false for fail.

### Example（取自子主题 TESTSET().judgeAndLog_Spmu()）

```
SPMU_TASK spmuTask;
ON_FIRST_INVOCATION_BEGIN();
CONNECT();
spmuTask.pin("I/O0").iForce(10 uA).clamp(3.5 V).min(1.5 V).max(3 V).relay("NTMBB");
spmuTask.pin("I/O1").vForce(3 V).clamp(1.5 mA).min(0.5 mA).max(1 mA).relay("NTMBB");
spmuTask.execMode(TM::PPF).execute();
ON_FIRST_INVOCATION_END();
TESTSET().judgeAndLog_Spmu(spmuTask);
```

This
example performs voltage measurement on pin
"I/O0"
 and
"I/O1"
.
The test result is judged and logged with the TESTSET API.

### Syntax（取自子主题 TESTSET().llmFmt()）

```
TESTSET & llmFmt(const STRING &format);
```
[表]
列: Parameter | Description
行 1:
  format
  A string describing the desired format. The string is a standard ANSI C format
    string, for example, "%7.3f".
    
    To indicate a hex result, use TESTSET().resFmt("%x").

### Example（取自子主题 TESTSET().llmFmt()）

Code example for result in hex
format:

```
LIMIT lim1;
lim1.low(TM::GE, 0x0001);
lim1.high(TM::LE, 0xFFFE);
lim1.unit(" ");
TESTSET hex_test;
hex_test.resFmt("%x").hlmFmt("%x").llmFmt("%x");
hex_test.testtext("TEST TEXT HERE");
hex_test.cont(1).testnumber(1000).judgeAndLog_ParametricTest("tdo", "dummy", lim1, 100);
```

### Syntax（取自子主题 TESTSET().port()）

```
TESTSET & port(const STRING &name);
```
[表]
列: Parameter | Descriptions
行 1:
  name
  The port name defined in the pin configuration whose functional test result is
    judged and logged.

### Example（取自子主题 TESTSET().port()）

```
TestSet.port("port1");
```

### Syntax（取自子主题 TESTSET().reliability()）

```
TESTSET & reliability(TM::RELIABILITY rel);
```
[表]
列: Parameter | Descriptions
行 1:
  rel
  This parameter enables you to indicate the reliability of the test result for data
    logging. To indicate the test is reliable, specify TM::RELIABLE. To indicate the test is
    unreliable, specify TM::UNRELIABLE.
    
    This parameter is optional. If you omit it, it is the same as specifying
    TM::RELIABLE.

### Example（取自子主题 TESTSET().reliability()）

```
TestSet.reliability(TM::RELIABLE);
```

### Syntax（取自子主题 TESTSET().resFmt()）

```
TESTSET & resFmt(const STRING &format);
```
[表]
列: Parameter | Description
行 1:
  format
  A string describing the desired format. The string is a standard ANSI C format
    string, for example, "%7.3f".

### Example（取自子主题 TESTSET().resFmt()）

```
TestSet.resFmt("%7.3f");
```

### Syntax（取自子主题 TESTSET().suppressTestNameLoopCount()）

```
TESTSET & suppressTestNameLoopCount(bool suppress);
```
[表]
列: Parameter | Description
行 1:
  suppress
  A If this parameter is true, no numbers are added to test names
    to make them unique.
    
    If the parameter is false (the default), numbers are added to a test
    name that is the same as that of another test to make sure that both tests have different
    names.

### Examples（取自子主题 TESTSET().suppressTestNameLoopCount()）

### Test names are made unique
```
TestSet.suppressTestNameLoopCount(false);
```

If the test
"myTest" is executed three times in a loop with this setting active, the logged test names would
be: "myTest[1]", "myTest[2]", and "myTest[3]".

### Test names are not made unique
```
TestSet.suppressTestNameLoopCount(true);
```

If the test
"myTest" is executed three times in a loop with this setting active, the logged test names would
be: "myTest", "myTest", and "myTest".

### Syntax（取自子主题 TESTSET().testname()）

```
TESTSET & testname(const STRING &name);
TESTSET & testname(const STRING &name, const bool forceSTDFTestName);
```
[表]
列: Parameter | Description
行 1:
  name
  The test name that is stored in the EDL as a `TestNameAttribute`（raw: `34701.htm`） for a test result. Used when one of the `TEST`（raw: `29803.htm`）
    methods is subsequently called.
    
    Test names can contain any printable ASCII characters, that is, characters with codes from 32
    to 126. This includes the space, digits, lowercase letters, uppercase letters, and these
    punctuation characters: !"#$%&'()*+,-./:;<=>@?[\]^_`{|}~ There is no fixed maximum length
    for the names in SmarTest. However, STDF limits test names to 255 characters, so test names
    should not be longer if STDF data logging is intended.
行 2:
  forceSTDFTestName
  If this parameter is true, the data formatter writes the
    name value name directly into the TEST_NAM field of the `TSR record`（raw: `69139.htm`）.
    
    If the parameter is false, the data formatter calculates the content
    of the TEST_NAM field from the test suite name, test name, and pin name.
    
    This parameter is optional. The default is false.

### Example（取自子主题 TESTSET().testname()）

```
TESTSET().testname("Sample_test");
```

### Syntax（取自子主题 TESTSET().testname_default()）

```
TESTSET & testname_default();
```

### Example（取自子主题 TESTSET().testname_default()）

```
TestSet.testname_default();
```

### Syntax（取自子主题 TESTSET().testnumber()）

```
TESTSET & testnumber(const STRING &name, bool logname = false);
```

This
form of the function assigns a test number to a test result from the test number
values entered in the
`Properties view`（raw: `99279.htm`）
 for the specified
test name, and the number of calls for the
`TEST`（raw: `29803.htm`）
 member function
with that test name. You can use this member function to assign a test number to a
test result that does not have a test name, such as the result of a functional test.
In this case, you must enter a test name in the Properties view, even if you have
selected a functional test.

If you wish to log the specified test name, set
the
logname
 parameter to
TRUE
. The name is
stored into the EDL as a
`TestNameAttr`（raw: `34701.htm`）
. The values of the
test number offset and test number increment named "name" are searched from the test
number table whose values are input through the Properties view. If "name" and the
corresponding values are found, when one of the
TEST()
 methods is
called, these values are used to generate a subtest test number. The subtest test
number return value is stored into the EDL as a
TestId

attribute.

```
TESTSET & testnumber(int number);
```

If the
`test_number_enable`（raw: `342556.htm#_342556__row_test_number_enable`）
 testflow flag is
enabled, this form of the function stores the number integer value in the EDL as a
TestId attribute.

```
TESTSET & testnumber(int number, const bool forceSTDFTestName);
```

If the
`test_number_enable`（raw: `342556.htm#_342556__row_test_number_enable`）
 testflow flag is
enabled, this form of the function stores the number integer value in the EDL as a TestId
attribute.

If
forceSTDFTestName
 is
true
, the data formatter writes
the
name
 value of the test directly into the TEST_NAM field of the
`TSR record`（raw: `69139.htm`）
, instead of calculating it from the test suite name, test
name, and pin name. If this parameter is
false
, it results in the same
behavior as using
TESTSET & testnumber(int number)
.

```
TESTSET & testnumber(TESTNUMBER &testnumber);
```

This form of the function assigns a test number for a test result from the offset and increment
values defined by the
`TESTNUMBER`（raw: `58917.htm`）
 API. When the
`test_number_enable`（raw: `342556.htm#_342556__row_test_number_enable`）
 testflow flag
is enabled and one of the
`TEST()`（raw: `29803.htm`）
 methods is called, the
integer value returned by
testnumber.applyTestNumber()
 is stored in
the EDL as a TestId attribute.

```
TESTSET & testnumber(TESTNUMBER &testnumber, const bool forceSTDFTestName);
```

This form of the function has the same effect as
TESTSET & testnumber(TESTNUMBER
&testnumber)
, above. In addition, it lets you specify that the name of the test is
put into the TEST_NAM field of the
`TSR record`（raw: `69139.htm`）
 (as described for

TESTSET & testnumber(int number, const bool forceSTDFTestName)
,
above).

Note
 The
TEST()
 methods have to be called within the scope of the

testnumber
 variable after this method is called. If one of
the
TEST()
 methods is called outside of the

testnumber
 variable scope, an error occurs and the test
method stops running. After you set the
testnumber
 variable, one
of the other
testnumber()
 methods must be called before exiting
the scope of the variable.

[表]
列: Parameter | Description
行 1:
  name
  The name you assign to a result that has not been previously
    assigned a name. The name assigned through the Properties view
    will reference corresponding test number in the Properties
    view.
行 2:
  logname
  A Boolean value that indicates whether the name is stored in
    the EDL.
行 3:
  number
  An integer value that you assign to directly generate a
    subtest test number in the EDL.
行 4:
  testnumber
  The `TESTNUMBER`（raw: `58917.htm`） object you assign to a test
行 5:
  forceSTDFTestName
  If this parameter is true, the data formatter writes the
    name value name directly into the TEST_NAM field of the `TSR record`（raw: `69139.htm`）.
    
    If the parameter is false, the data formatter calculates the content
    of the TEST_NAM field from the test suite name, test name, and pin name.

### Examples（取自子主题 TESTSET().testnumber()）

### Example 1

This example assigns the test number defined in
limit1
 to the
current test. The specified test name is logged to EDL stream.

```
TestSet.testnumber("limit1",true);
```

### Example 2

This example assigns
100
 as the test number to the current test.

```
TestSet.testnumber(100);
```

### Example 3

This example assigns the test number in
tm1
 to the current test.

```
TESTNUMBER tm1;
...
TestSet.testnumber(tm1);
```

### Syntax（取自子主题 TESTSET().testnumber_default()）

```
TESTSET & testnumber_default();
```

### Example（取自子主题 TESTSET().testnumber_default()）

```
TestSet.testnumber_default();
```

### Syntax（取自子主题 TESTSET().testnumber_none()）

```
TESTSET & testnumber_none();
```

### Example（取自子主题 TESTSET().testnumber_none()）

```
TestSet.testnumber_none();
```

### Syntax（取自子主题 TESTSET().testsuite()）

```
TESTSET & testsuite(const STRING &name);
```
[表]
列: Parameter | Description
行 1:
  name
  The name of the test suite that you wish to use as the source for test limits and
    test numbers and include in the data log.
    
    Note that the test suite name must be listed in the test table.

### Example（取自子主题 TESTSET().testsuite()）

```
TestSet.testsuite("Functional_test");
```

### Syntax（取自子主题 TESTSET().testsuite_default()）

```
TESTSET & testsuite_default();
```

### Example（取自子主题 TESTSET().testsuite_default()）

```
TestSet.testsuite_default();
```

### Syntax（取自子主题 TESTSET().testtext()）

```
TESTSET & testtext(const STRING &text);
```
[表]
列: Parameter | Description
行 1:
  text
  String of text stored in the EDL as a `TestDescriptionAttrType`（raw: `57547.htm`）.

### Example（取自子主题 TESTSET().testtext()）

The following example appends the comment '
trail_test
' to
`TEST_TXT`（raw: `123927.htm`）
 if the
`disableTestTxtOverride`（raw: `70623.htm`）
 is
set to

true
.

```
{
...
TestSet.testtext("trial_test").testnumber(50).judgeAndLog_ParametricTest("pin1", "limit1", TM::Pass, 0);
...
}
```

### Syntax（取自子主题 TESTSET().testtext_none()）

```
TESTSET & testtext_none();
```

### Example（取自子主题 TESTSET().testtext_none()）

```
TestSet.testtext_none();
```

### Syntax（取自子主题 TESTSET().testtype()）

```
TESTSET & testtype(TM::TEST_TYPE type);
```
[表]
列: Parameter | Description
行 1:
  type
  The test type can be TM::FUNCTIONAL,
    TM::PARAMETRIC, or TM::SCAN.

### Example（取自子主题 TESTSET().testtype()）

```
TestSet.testtype(TM::PARAMETRIC);
```

### Syntax（取自子主题 TESTSET().testtype_default()）

```
TESTSET & testtype_default();
```

### Example（取自子主题 TESTSET().testtype_default()）

```
TestSet.testtype_default();
```

### Class definition（取自子主题 TESTNUMBER）

Constructor

```
TESTNUMBER(int offset, int increment);
```

Member
Functions

```
int applyTestNumber();
int getTestNumber() const;
int getOffset() const;
int getIncrement() const;
int getNumberOfCalls() const;
int setOffset(int offset);
int setIncrement(int increment);
int setNumberOfCalls(int numberofcalls);
```

### Syntax（取自子主题 TESTNUMBER）

In the case of TESTNUMBER, there is no use case to use a
temporary object. You will assign your own object when using
TESTNUMBER.

```
User object (TESTNUMBER obj(offset,increment));
obj.member_func();
```

Users
can use obj as an argument of
TESTSET.testnumber() member_func()
; or call

obj.method()
;

### Member functions（取自子主题 TESTNUMBER）

Some of the following TESTNUMBER member function
descriptions use the term "subtest test number". This is a subtest number assigned to each test
in a test suite (or a test method) that is passed to the Test Number Generator, and is based on
the following calculation:

```
subtest test number = offset + increment * (number of calls)
```

The
numbers assigned to a test result can be modified and are affected by default and
user-selectable numbering parameters.

### Example（取自子主题 TESTNUMBER）

The example below demonstrates how the TESTNUMBER class can be used with the TESTSET
class, and specifically illustrates the use of the
getOffset
,

getIncrement
,
setOffset
,
setIncrement
,
and
applyTestNumber
 member functions.

The test name "SDC_6" is defined.
Its offset is set to 3000 and increment is set to
50.

```
TESTNUMBER sdc6 = GET_TESTNUMBER("SDC_6");
if (sdc6.getOffset()<=0){
sdc6.setOffset(1000);
}
if(sdc6.getIncrement()<=100{
sdc6.setIncrement(250);
}
TestSet.testnumber(sdc6.applyTestNumber()).TEST();//3000+250*0=3000
TestSet.testnumber(sdc6.applyTestNumber()).TEST();//3000+250*1=3250
TestSet.testnumber(sdc6).TEST();//3000+250*2=3500
TestSet.TEST();//3000+250*3=3750
```

In
this example, the
getOffset
 and
getIncrement
 commands
retrieve the offset and increment values that have been assigned for SDC_6. The increment value
of 250, implemented through the
setIncrement
 command, is applied. The

applyTestNumber
 member function initiates an iteration based on the number
of calls, and returns the resulting test number value.

Note
 The

TESTNUMBER()
 class can be used with the
TESTSET()
 class
to work as an API for executing test numbering procedures, such as assigning default values,
assigning offset and increment values, and deactivating test numbering for a tes tsuite. See the

`TESTSET()`（raw: `58886.htm`）
 examples section for a set of examples that show the use
of
TESTNUMBER
 member functions with
`TESTSET()`（raw: `58886.htm`）
.
You may also want to look at the
`GET_TESTNUMBER()`（raw: `59051.htm`）
 API examples
section to learn how
GET_TESTNUMBER()
 can be used with the

TESTNUMBER()
.

### Syntax（取自子主题 GET_TESTNUMBER）

```
const TESTNUMBER & GET_TESTNUMBER(const char * testname);
```
[表] Parameter
行 1:
  testname
  The test name that is referenced from the
    
    `Properties view`（raw: `99279.htm`）.

### Example（取自子主题 GET_TESTNUMBER）

[表]
行 1:
  TESTNUMBER tn=GET_TESTNUMBER ("Funcd1");
  /*Retrieve and copy the constant reference of the corresponding
    TESTNUMBER object
行 2:
  tn.setOffset(200);
  /*Change the offset value in the object using the setOffset member
    function
行 3:
  TestSet.testnumber (tn).TEST ();
  /*Assigns a test number using the new offset and increment values to a
    test result which is judged and logged using the TEST API.

### Examples（取自子主题 Generating per-pin test numbers）

### Writing the test method
```
virtual void run()
{
STRING_VECTOR Pin_List;
STRING Test_Name;
int Pin_Num;
int Pin_List_No;

Pin_List = PinUtility.getDigitalPinNamesFromPinList(mPins,TM::IO_PIN,true,true);
Pin_Num = Pin_List.size();

Test_Name = "passCurrLimit_uA";

ARRAY_D values(Pin_Num);
for (int i = 0; i < Pin_Num; i++){
values[i] = (i+100);
}

STRING pinstr = PIN_UTILITY::createPinListFromPinNames(Pin_List);
TEST(pinstr.c_str(), Test_Name.c_str(), V93kLimits::tmLimits,values,TM::CONTINUE);
// If this feature is disabled, only one test number is generated in the execution. Otherwise, 100 test numbers are generated.
```

### Creating a testflow by using the above-defined test method.

At the Start, the testflow reads the value of

PerPinTestNumberAutoGenEnable
 in the testflow variable table, which is 1 to
enable the per-pin test numbering feature.

Set the value of
PerPinTestNumberAutoGenEnable
 to 0 to disable the
per-pin test numbering feature for the following test suites.

Set the value of
PerPinTestNumberAutoGenEnable
 to 1 to enable the per-pin
test numbering for the following test suites.

Since

PerPinTestNumberAutoGenEnable
 is a global testflow variable, changing it
in the source code may lead to an unsafe thread issue. We do not recommend to change it in the
source code.

### Class definition（取自子主题 TMLimits）

Note
 If you want to use the SmarTest implementation of TMLimits described
herein, declare the V93kLimits namespace in your test method with the statement

using namespace V93kLimits;
.

This API is defined in the header file

/opt/hp93000/soc/prod_com/include/MAPI/TMLimits.h
.

Constructor

There is no constructor available for this class. You cannot create any
object of this class:

To use the
TMLimits
 class, you must always use
the system-prepared class object
tmLimits
.

To use the API, you need also to declare the using of

V93kLimits
 namespace in your test method:

```
using namespace V93kLimits;
```

Member functions

`clear()`（raw: `110432.htm#_110432__dle_clear`）

`getInstance()`（raw: `110432.htm#_110432__dle_getInstance`）

`getLimit()`（raw: `110432.htm#_110432__dle_getLimit`）

`getLimitRef()`（raw: `110432.htm#_110432__dle_getLimitRef`）

`getLimitObj()`（raw: `110432.htm#_110432__dle_getLimitObj`）

`load()`（raw: `110432.htm#_110432__dle_load`）

`setTestMode()`（raw: `110432.htm#_110432__dle_setTestMode`）

`getTestMode()`（raw: `110432.htm#_110432__dle_getTestMode`）

`loadOnDemandAndReturnStatus()`（raw: `110432.htm#_110432__dle_loadOnDemandAndReturnStatus`）

`setLookupKey()`（raw: `110432.htm#_110432__dle_setLookupKey`）

`setDefaultLookupKeys`（raw: `110432.htm#_110432__dle_setDefaultLookupKeys`）

`getLookupKey()`（raw: `110432.htm#_110432__dle_getLookupKey`）

TMLimits::LimitInfo

TMLimits::LimitInfo
 is a struct for limit
data:

[表]
行 1:
  SuiteName
  string
  The name of the test suite
行 2:
  TestName
  string
  The name of the test
行 3:
  PinName
  string
  The pins to which the test applies
行 4:
  TestNumber
  int
  The test number of the test
行 5:
  PassRegion
  char
  The pass region, used for part average testing: L, I,
    H, or X
行 6:
  LslTyp
  string
  The type of lower limit: GT, GE, or NA
行 7:
  UslTyp
  string
  The type of upper limit: LT, LE, or NA
行 8:
  Lsl
  double
  The lower spec limit
行 9:
  Usl
  double
  The upper spec limit
行 10:
  Units
  string
  The units for test results and spec limits
行 11:
  OffSet
  DOUBLE
  A value that is added to the test results before they
    are compared to the limits
行 12:
  BinhNum
  int
  The hardware bin number for failed tests
行 13:
  BinhName
  string
  The name of the hardware bin specified by
    BinhNum
行 14:
  BinsNum
  int
  The software bin number for failed tests
行 15:
  BinsNumString
  string
  The software bin number for failed tests in the type of
    string.
行 16:
  BinsName
  string
  The name of the software bin specified by BinsNum
行 17:
  TestRmrks
  string
  Optional comments for explaining this test
行 18:
  TEST_API_LIMIT
  `LIMIT`（raw: `29504.htm`）
  The SmarTest object for this test
行 19:
  Exec
  char
  Whether this test is to be executed
    (Y) or not
    (N)
行 20:
  ParamString
  map <string, string>
  The calling parameter string, for accessing
    user-defined columns
行 21:
  ParamDouble
  map <string, double>
  The calling parameter doubles, for accessing
    user-defined columns

Most of the elements of
LimitInfo
 correspond
to columns in
`TMLimits CSV files`（raw: `112490.htm`）
.

### Member functions（取自子主题 TMLimits）

clear()
```
void clear()
```

Clears all values from the limit table
in the TMLimits object.

getInstance()
```
static TMLimits& getInstance()
```

This function is
used for internal purposes only.

getLimit()

Note
 For performance reasons, we recommend that you use
`getLimitRef()`（raw: `110432.htm#_110432__dle_getLimitRef`）
, described below, instead of this
function unless you want to modify the test limits it
returns.

```
LimitInfo& getLimit(const std::string& key);
LimitInfo& getLimit(const std::string& testSuiteName, const std::string & limitParamName);
LimitInfo& getLimit(const std::string& testSuiteName, const std::string & limitParamName, const std::string & pinName);
LimitInfo& getLimit(const std::string& testSuiteName, const std::string & limitParamName, const std::string & pinName, int testNumber);
```

Returns
a reference to an internal
`LimitInfo`（raw: `110432.htm#_110432__LimitInfo`）
 object of the system-prepared class object

tmLimits
 describing an individual test for use
with
TMLimits
 functions. Data of the requested test
are copied from the TMLimits table into the internal

LimitInfo
 object.

The internal
LimitInfo
 object is available once per
thread, meaning there is one object for the main thread of SmarTest and
one more internal
LimitInfo
 object for each SMC
background thread.

You can change the contents of the internal
LimitInfo

object but changes apply only to the object that is assigned to the
current thread.

Multiple calls of this function within one thread refer always to the
same internal
LimitInfo
 object. You must therefore
immediately process the retrieved data before the next call is issued or
you must create a local copy of the data.

Depending on the
structure of the CSV file you use, there are four variants of the
function:

If the CSV file contains a unique key for each test in the first
column, use the first variant.

If the CSV file contains the test suite name in the first column and
the test name in the second, use the second variant of the
function.

If the CSV file contains additional a dedicated pin name in the
third column use the third variant of the function and use the
fourth variant if the fourth column contains a test number.

Parameters
[表]
行 1:
  key
  The unique test key describing the test in
    the returned object.
行 2:
  testSuiteName
  The name of the test suite that contains
    the described test.
行 3:
  limitParamName
  The name of the test that is described in
    the returned object.
行 4:
  pinName
  The name of a pin used by a test for which you
    want to read the limits.
    
    The provided pin name is matched against the
    Pins column in the limits:
    
    If a test matching pin (and
    the other provided parameters) is found, the
    corresponding limits are returned. This includes
    tests where the Pins column
    contains a pin group that includes
    pin.
    
    If there is a Pins column in
    the limits but no test matches
    pin, the execution will lead to
    an error:
    
    Error: no limit found for
    testsuite=..., testname=..., pin=...,
    testnumber=...
    
    If no Pins column exists,
    pin is ignored.
    
    This parameter is optional. If you omit it, the
    pin name is not considered for finding the test
    limits.
行 5:
  testNumber
  The number of the test for which you want to
    read the limits.
    
    This parameter is optional. If you omit it, the
    test number is not considered for finding the test
    limits.
Return value
A reference to an internal
`LimitInfo`（raw: `110432.htm#_110432__LimitInfo`）
 object of the system-prepared class object

tmLimits
. This internal object holds the
data of the requested test.
Using the function

The following code creates a reference to the internal
`LimitInfo`（raw: `110432.htm#_110432__LimitInfo`）
 object of the
system-prepared class object
tmLimits
.
The object is available once for the current
thread:

```
TMLimits::LimitInfo & limitInfo_1 = tmLimits.getLimit("testSuite_1","test_1");
```

Variable

limitInfo_1
 refers to an internal

LimitInfo
 object that is filled with
the requested data. Rerunning the function immediately using
another variable and other parameters will override the data
that
limitInfo_1
 refers: Both variables
refer to the same internal
LimitInfo

object of the system-prepared class object

tmLimits
. In this case you must
create a local copy of the internal

LimitInfo

object:

```
TMLimits::LimitInfo limitInfo_1 = tmLimits.getLimit("testSuite_1","test_1");
TMLimits::LimitInfo limitInfo_2 = tmLimits.getLimit("testSuite_1","test_2");
```
getLimitRef()
```
const LimitInfo& getLimitRef(const string& key)
const LimitInfo& getLimitRef(const string& testsuite, const string& testname, const string& pin = "", int testnumber = -1, int sbin = -1)
```

Returns
a reference to a
`LimitInfo`（raw: `110432.htm#_110432__LimitInfo`）
 object
that represents directly the requested test in the TMLimits table.
Unlike
`getLimit()`（raw: `110432.htm#_110432__dle_getLimit`）
, the content of the
referenced object cannot be modified.

The referenced

LimitInfo
 object holds the data for the first
test that matches all specified criteria. In the second variant of the
function, you must always specify the test suite and test name. The
other criteria are optional and are ignored if you do not specify
them.

This function is significantly faster than
`getLimit()`（raw: `110432.htm#_110432__dle_getLimit`）
 and should be preferred. If you do
not need to modify the
LimitInfo
 object, use this
function for maximum performance.

Parameters
[表]
行 1:
  key
  The unique test key describing the test in
    the returned object.
行 2:
  pin
  The name of a pin used by a test for
    which you want to read the limits.
    
    The provided pin name is matched against the
    Pins column in the limits:
    
    If a test matching pin (and
    the other provided parameters) is found, the
    corresponding limits are returned. This includes
    tests where the Pins column
    contains a pin group that includes
    pin.
    
    If there is a Pins column in
    the limits but no test matches
    pin, the execution will lead to
    an error:
    
    Error: no limit found for
    testsuite=..., testname=..., pin=...,
    testnumber=...
    
    If no Pins column exists,
    pin is ignored.
    
    This parameter is optional. If you omit
    it, the pin name is not considered for finding the
    test limits.
行 3:
  sbin
  The software bin number of the test for
    which you want to read the limits.
    
    This parameter is optional. If you omit it, the
    software bin number is not considered for finding the
    test limits.
行 4:
  testname
  The name of the test for which you want to
    read the limits.
行 5:
  testnumber
  The number of the test for which you
    want to read the limits.
    
    This parameter is optional. If you omit it, the
    test number is not considered for finding the test
    limits.
行 6:
  testsuite
  The name of the test suite that contains
    the described test.
Return value
A reference to an internal
`LimitInfo`（raw: `110432.htm#_110432__LimitInfo`）
 object of the system-prepared class object

tmLimits
. This internal object holds the
data of the requested test.
Using the function

The following code returns a reference to a
`LimitInfo`（raw: `110432.htm#_110432__LimitInfo`）
 object that
represents directly the requested test in the TMLimits
table:

```
const TMLimits::LimitInfo & limitInfoRef = tmLimits.getLimitRef("testSuite_1","test_1");
```

The

LimitInfo
 object referenced by the

limitInfoRef
 variable, cannot be
modifed. However this version is significantly faster than

`getLimit()`（raw: `110432.htm#_110432__dle_getLimit`）
.

If you need
to modify the requested
limitInfoRef
, you
must create a local copy of the object as
follows:

```
TMLimits::LimitInfo limitInfoCopy = tmLimits.getLimitRef("testSuite_1","test_1");
```

The
local object
limitInfoCopy
 of type

LimitInfo
 can by modified and does not
have the limitation of internal object referenced by
`getLimit()`（raw: `110432.htm#_110432__dle_getLimit`）
. However, creating the local
object and filling it with the data from the TMLimits table
needs about the same amount of test time as

getLimit()
.

These are some sample calls to

getLimitRef()
 and the test number for
which it returns the limits, given the example test table
below:

tmLimits.getLimitRef("a","test","Pin1")

returns the limits for test number 301.

tmLimits.getLimitRef("a","test","Pin2")

returns the limits for test number 302.

tmLimits.getLimitRef("a","test","Pin3")

returns the limits for test number 303.

tmLimits.getLimitRef("a","test","PinNew")

returns the limits for test number 300.

tmLimits.getLimitRef("a","test","PortOdd")

returns the limits for test number 303.

[表]
行 1:
  
  Test suite name
  Test name
  Pins
  Test number
行 2:
  
  a
  test
  Pin1
  301
行 3:
  
  a
  test
  Pin2
  302
行 4:
  
  a
  test
  
  300
行 5:
  
  a
  test
  PortOdd
  303
行 6:
  
  Note: PortOdd contains the pins Pin1 [跨 4 列]
    and Pin3.
getLimitObj()
```
LIMIT& getLimitObj(const string& LimitParamName)
LIMIT& getLimitObj(const string& LimitParamName, const string& PinName)
```

Returns a reference to an internal
`LIMIT`（raw: `29504.htm`）
 object of the system-prepared
class object
tmLimits
. Data of the requested test are
copied from the TMLimits table into the internal

LIMIT
 object.

The internal
LIMIT
 object is available once per thread, meaning there is
one object for the main thread of SmarTest and one more internal

LIMIT
 object for each SMC background thread.

You can change the contents of the internal
LIMIT
 object but changes
apply only to the object that is assigned to the current thread.

Multiple calls of this function within one thread refer always to the same internal

LIMIT
 object. You must therefore immediately
process the retrieved data before the next call is issued or you must
create a local copy of the data.

Parameters
[表]
行 1:
  limitParamName
  The name of the test that is described in the
    returned object
    
    In contrast to functions `getLimit()`（raw: `110432.htm#_110432__dle_getLimit`） and `getLimitRef()`（raw: `110432.htm#_110432__dle_getLimitRef`）, the test suite
    name is derived from the function call itself and
    must therefore also match. Otherwise the test
    defined by limitParamName will
    not been found in the limit table.
行 2:
  PinName
  The name of the pin to which the particular
    set of limits applies that is defined for the test
    described in the returned object
Return value
A reference to an internal
`LIMIT`（raw: `29504.htm`）
 object of the system-prepared class
object
tmLimits
. This internal object holds
the data of the requested test.
Using the function

The following code creates a reference to the internal
`LIMIT`（raw: `29504.htm`）
 object
of the system-prepared class object

tmLimits
. The object is available
once for the current
thread:

```
LIMIT & limit_1 = tmLimits.getLimitObj("testname_1");
```

Variable

limit_1
 refers to an internal

LIMIT
 object that is filled with the
requested data. Rerunning the function immediately using
another variable and other parameters will override the data
that
limit_1
 refers: Both variables refer
to the same internal
LIMIT
 object of the
system-prepared class object
tmLimits
. In
this case you must create a local copy of the internal

LIMIT

object:

```
LIMIT limit_1 = tmLimits.getLimitObj("testname_1");
LIMIT limit_2 = tmLimits.getLimitObj("testname_2");
```

There
are two ways to specify the object:

By specifying the parameter name

By specifying the parameter name and the pin name

Note
 If you specify just a parameter name for
a test that defines different limits for different
pins, the function returns the first limit set for
the test.

In contrast to functions
`getLimit()`（raw: `110432.htm#_110432__dle_getLimit`）
 and
`getLimitRef()`（raw: `110432.htm#_110432__dle_getLimitRef`）
, the test suite
name is derived from the function call itself and must therefore
also match. Otherwise the test defined by

limitParamName
 will not been found in the
limit table.

This function sets multibin to the values
contained in the TMLimits object. If multibin is used in the
testflow, do not use getLimitObj() to access the TMLimits
object. Instead, use getLimit() or, if you use a
`judgeAndLog_xxx`（raw: `58886.htm`）
 or
`TEST()`（raw: `29803.htm`）
 function, use a variant
that directly accesses TMLimits (instead of through a member
function).

For example, instead of code like
this:

```
TestSet.cont(true).TEST("DC_Test", "lim1", tmLimits.getLimitObj("lim1"), mLim1);
```

use
code like
this:

```
TestSet.cont(true).TEST("DC_Test", "lim1", tmLimits, mLim1);
```
load()
```
int load()
int load(const string& limitfile)
int load(const string& limitfile, const string& mode)
int load(TM::LIMIT_WARNING_LEVEL = TM::LIMIT_DEFAULT_WARNING)
```

Loads
a CSV file into the TMLimits object. There are three ways to specify the
desired file:

If you call
load()
 without any parameters, it
uses the
TMLimit_FileName
 testflow variable to
determine the file to load and the current value of the

TMLimit_TestMode
 variable for the desired
mode.

Note that this variant is subject to the restrictions
outlined above. The test mode of the variable will only be used
if it has changed since the last call of one of the member
functions specified above.

If you specify a file when calling
load()
 but no
mode, it loads the specified file and uses the mode "Default". With
the "Default" test mode, the first test mode occurring in the
specified test table is selected.

If you call
load()
 with both a file name and a
mode, it loads the specified file and sets the specified mode.

[表] Parameters
行 1:
  limitfile
  The CSV file to load.
    
    The specified name can include a path, which must be
    relative to the testtable/
    directory within the current device directory. If
    just a file name is given, the file must be located
    in the testtable/
    directory.
    
    The file must confirm to the TMLimits data format,
    such as files written by saving the test table from
    the test program explorer. This is described in
    `Saving test numbers as TMLimits CSV files`（raw: `110093.htm`）.
行 2:
  mode
  The mode (or test stage) from the testflow to
    use.
    
    A TMLimits CSV file can contain multiple versions of
    any of the parameters (such as upper and lower test
    limits) except the key columns, with each version
    being assigned to a test mode. Test modes can also
    be specified for user-defined columns.
    
    These modes, such as quality assurance, are user
    definable; a CSV file can include an unlimited
    number of modes.
行 3:
  LIMIT_WARNING_LEVEL
  Warning level of type
    TM::LIMIT_WARNING_LEVEL.
    
    Enables you to set the verbosity of warnings
    displayed to the system console and report UI
    window.
    
    Available options are:
    
    LIMIT_DEFAULT_WARNING
    Default.
    
    Use this if you want to reset the warning to
    default. This is, all warnings are outputted to
    the system console and report UI window.
    
    LIMIT_NO_DUPLICATE_KEY_WARNING
    Optional.
    
    Sets the verbosity of reported warnings not to
    show duplicate keys. This is, duplicate keys will
    only be outputted once to the system console and
    report UI window.
    
    LIMIT_NO_DUPLICATE_TEST_WARNING
    Optional.
    
    Sets the verbosity of reported warnings not to
    show duplicate test numbers. This is, duplicate
    test numbers will only be outputted once to the
    system console and report UI window.
    
    LIMIT_NO_WARNING
    Optional.
    
    Sets the verbosity of reported warnings not to
    show any warnings. This is, no warning will be
    outputted to the system console and report UI
    window.
    
    Use this with caution, because no warnings will
    be displayed at all.
setTestMode()
```
int setTestMode(const string& mode)
```

Sets the
test mode for the TMLimits object.

[表] Parameter
行 1:
  mode
  The mode (or test stage) from the testflow to
    use.
    
    See the description of this parameter in `load()`（raw: `110432.htm#_110432__dle_load`）, above.
getTestMode()
```
string getTestMode();
```

This function returns the
currently configured test mode.

loadOnDemandAndReturnStatus()
```
bool loadOnDemandAndReturnStatus();
```

This function
returns whether a test table exists and can be loaded or is already
loaded.

If a test table is already loaded in the test method or in the Test
Program Explorer, true will be returned.

If a test table exists and is used in the testflow but not loaded,
the function will load the test table and return true.

If no test table exists or a test table exists but not loaded and
not used in the testflow, false will be returned.

setLookupKey()
```
void setLookupKey(const std::string& lookupkey);
```

Sets
the key(s) to look up for a limit in the test table.

[表] Parameter
行 1:
  lookupkey
  The name of the columns in the test table
    separated by colons.
    
    To retrieve the limits with
    getLimitRef(), you can specify
    any combinations of columns in the test table as the
    lookup key.
    
    To directly use the tmLimits as an
    input parameter of `TESTSET().judgeAndLog_ParametricTest()`（raw: `127827.htm`）, only the
    combinations of Suite name, Test name, Pins or Test
    number can be used as the lookup key.
setDefaultLookupKeys
```
void setDefaultLookupKeys();
```

Reset the lookup keys
of the test table. The default lookup keys can be the four combinations
below.

Suite name, Test name, Pins

Suite name, Test name

Limit key, Pins

Limit key

getLookupKey()
```
const std::string& getLookupKey();
```

Returns the
current lookup key.

### Examples（取自子主题 TMLimits）

### Example 1: Declare namespace

To use the TMLimits API, you need to
declare the using of V93kLimits namespace in your test
method:

```
using namespace V93kLimits;
```

### Example 2: Setting the test mode and performing a test
```
tmLimits.setTestMode("FT");
TestSet.TEST("pinName", "myTestName", tmLimits, 4);
```

### Example 3: Performing a test for testflow using multibin

Use

```
TestSet.cont(true).TEST("DC_Test", "myTestName", tmLimits, mLim1);
```

instead
of

```
TestSet.cont(true).TEST("DC_Test", "myTestName", tmLimits.getLimitObj("myTestName"), mLim1);
```

### Example 4: Using the test table bins

Test table bins with TMLImits
support different bins for one test suite.

Several tmLimits API calls remember
the first failing bins, see Behavior example in
`TESTSET().judgeAndLog_ParametricTest()`（raw: `127827.htm`）
.

Requirements:

Testflow: Multibin icon in the fail branch of test suite

Test table: Bins of the corresponding limit keys are
defined

```
TESTSET().cont(true).judgeAndLog_ParametricTest(pin, <testname>, , V93kLimits::tmLimits, <singlevalue>);
```

### Example 5: Accessing a value from LimitInfo

This code reads the
limits from the test "myTestName" of the current test suite into a LimitInfo struct
and retrieves the value for the units, storing it in a string
variable.

```
using namespace V93kLimits;

string sTestsuiteName;
GET_TESTSUITE_NAME( sTestsuiteName );
string sTestName = "myTestName";

TMLimits::LimitInfo strLimitInfo;
strLimitInfo = tmLimits.getLimit( sTestsuiteName, sTestName );
string sTestTableTestModeUnit = strLimitInfo.Units;
```

### Example 6: Changing the values of a TMLimits object
```
LimitInfo& MyInfo = tmlimits.getLimit(testsuiteName, testname);
MyInfo.Lsl = 4;
```

This
example creates a reference to a
`LimitInfo object`（raw: `110432.htm#_110432__LimitInfo`）
 for the specified testsuite and test, and changes the

Lsl
 value of the object to 4. Note that a reference is needed
for this to work.

### Example 7: Using the lookup key to manually retrieve the limit with getLimitRef()
```
STRING_VECTOR string_vector_odd;
PPMU_MEASURE ppmu_measure_odd;
DOUBLE resultValue = 0.0;
//test setup and execution
....
//get the limit with the Limit key of ContactShort
tmLimits.setLookupKey("Limit key");
TMLimits::LimitInfo limitInfoContactShort = tmLimits.getLimitRef("ContactShort");
for (int i = 0; i < string_vector_odd.size(); i++)
{
if (string_vector_odd[i] == "BBIOI_N_ch0")
{
//get the limit with the Limit key of ContactShort and with the pin of BBIOI_N_ch0
tmLimits.setLookupKey("Limit key:Pins");
TMLimits::LimitInfo limitInfoContactShortPin = tmLimits.getLimitRef("ContactShort:" + string_vector_odd[i]);
resultValue=ppmu_measure_odd.getValue(string_vector_odd[i]);
TestSet.cont(true).testnumber(limitInfoContactShortPin.TestNumber).judgeAndLog_ParametricTest(string_vector_odd[i],"Contact_Short",limitInfoContactShortPin.TEST_API_LIMIT, resultValue);
}
else
{
resultValue=ppmu_measure_odd.getValue(string_vector_odd[i]);
TestSet.cont(true).testnumber(limitInfoContactShort.TestNumber).judgeAndLog_ParametricTest(string_vector_odd[i],"Contact_Short",limitInfoContactShort.TEST_API_LIMIT, resultValue);
}
}
```

### Example 8: Using the lookup key to automatically retrieve the limit in judgeAndLog_ParametricTest()
```
tmLimits.setLookupKey("Test number");
// use the limit with the test number of 555:
TESTSET().testnumber(555).judgeAndLog_ParametricTest("io1","test12",tmLimits,-12);
tmLimits.setDefaultLookupKeys();
// use the limit with the Pins of "io1" and with the Test name of "test12"
TESTSET().judgeAndLog_ParametricTest("io1","test12",tmLimits,-12);
```

### Example 9: Limiting displayed warnings when loading a limits file.

This example shows all available parameter. However, it will
suppress duplicate test
numbers.

```
virtual void run()
{
ON_FIRST_INVOCATION_BEGIN();

tmLimits.setLookupKey("Test number:Limit_type");
cout << "default usage" << endl;
tmLimits.load();

// use this to re-/set to default
// tmLimits.load(TM::LIMIT_DEFAULT_WARNING);

// use this to suppress duplicate key warnings
// tmLimits.load(TM::LIMIT_NO_DUPLICATE_KEY_WARNING);

// use this to suppress duplicate test number warnings
tmLimits.load(TM::LIMIT_NO_DUPLICATE_TEST_WARNING);

// use this to suppress all warnings
// use this carefully!
// tmLimits.load(TM::LIMIT_DEFAULT_WARNING);

ON_FIRST_INVOCATION_END();

return;
}
```

### Example（取自子主题 SmartCalc multithreading basics）

The following section shows a truncated output of the

/proc/cpuinfo
 of a XW4400 system
controller:

```
processor: 0
vendor_id: GenuineIntel
cpu family: 6
model: 15
model name: Intel(R) Core(TM)2 CPU 6700 @ 2.66GHz
stepping: 6
cpu MHz: 1596.000
cache size: 4096 KB
physical id: 0
siblings: 2
core id: 0
cpu cores: 2
....
processor: 1
vendor_id: GenuineIntel
cpu family: 6
model: 15
model name: Intel(R) Core(TM)2 CPU 6700 @ 2.66GHz
stepping: 6
cpu MHz: 1596.000
cache size: 4096 KB
physical id: 0
siblings: 2
core id: 1
cpu cores: 2
```

### Example（取自子主题 SmartCalc recommendations）

### Exception handling

The following example shows how a customized
exception handling can be coded in the
`SMC_backgroundProcessing()`（raw: `120107.htm#_120107__s_SMC_backgroundProcessing`）
 method using

catch()
.

```
void SMC_backgroundProcessing()
{
...
try
{
...
call my_function_that_throws();
...
}
catch(myException& e)
{
//
// Always catch user-defined exceptions
// and do what is needed in this specific error.
...
}
...
}

class myException {};

void my_function_that_throws()
{
if (...)
{
throw myException();
}
}
```

### Syntax（取自子主题 SMC_TEST()）

```
void SMC_TEST(const STRING& pin, const STRING& testname, DOUBLE value, Boolean Continue = FALSE, INT testNumber = -1, const STRING& softbin= "", INT hardbin = -1, const STRING& testtext= "");
void SMC_TEST(const STRING& pin, const STRING& testname, DOUBLE value, Boolean Continue, TM::RELIABILITY reliability, INT testNumber = -1, const STRING& softbin= "", INT hardbin = -1, const STRING& testtext= "");
void SMC_TEST(const STRING& pin, const STRING& testname, const LIMIT& limit, DOUBLE value, Boolean Continue = FALSE, INT testNumber = -1, const STRING& softbin= "", INT hardbin = -1, const STRING& testtext= "");
void SMC_TEST(const STRING& pin, const STRING& testname, const LIMIT& limit, DOUBLE value, Boolean Continue, TM::RELIABILITY reliability, INT testNumber = -1, const STRING& softbin= "", INT hardbin = -1, const STRING& testtext= "", INT logTestNumber = -1);
void SMC_TEST(const STRING& pin, const STRING& testname, V93kLimits::TMLimits& limits, DOUBLE value, const STRING& testtext);
void SMC_TEST(const STRING& pin, const STRING& testname, V93kLimits::TMLimits& limits, DOUBLE value, Boolean Continue = FALSE, const STRING& testtext= "");
void SMC_TEST(const STRING& pin, const STRING& testname, V93kLimits::TMLimits& limits, DOUBLE value, Boolean Continue, TM::RELIABILITY reliability, INT logTestNumber = -1, const STRING& softbin = "", INT hardbin = -1);
void SMC_TEST(const STRING& pin, const STRING& testname, V93kLimits::TMLimits& limits, DOUBLE value, Boolean Continue, TM::RELIABILITY reliability, const STRING& testtext);
```

Additional interface which allows specifying the site:

```
void SMC_TEST(INT site, const STRING& pin, const STRING& testname, DOUBLE value, Boolean Continue = FALSE, INT testNumber = -1, const STRING& softbin= "", INT hardbin = -1, const STRING& testtext= "");
void SMC_TEST(INT site, const STRING& pin, const STRING& testname, DOUBLE value, Boolean Continue, TM::RELIABILITY reliability, INT testNumber = -1, const STRING& softbin= "", INT hardbin = -1, const STRING& testtext= "");
void SMC_TEST(INT site, const STRING& pin, const STRING& testname, const LIMIT& limit, DOUBLE value, Boolean Continue = FALSE, INT testNumber = -1, const STRING& softbin= "", INT hardbin = -1, const STRING& testtext= "");
void SMC_TEST(INT site, const STRING& pin, const STRING& testname, const LIMIT& limit, DOUBLE value, Boolean Continue, TM::RELIABILITY reliability, INT testNumber = -1, const STRING& softbin= "", INT hardbin = -1, const STRING& testtext= "");
void SMC_TEST(INT site, const STRING& pin, const STRING& testname, V93kLimits::TMLimits& limits, DOUBLE value, const STRING& testtext);
void SMC_TEST(INT site, const STRING& pin, const STRING& testname, V93kLimits::TMLimits& limits, DOUBLE value, Boolean Continue = FALSE, const STRING& testtext= "");
void SMC_TEST(INT site, const STRING& pin, const STRING& testname, V93kLimits::TMLimits& limits, DOUBLE value, Boolean Continue, TM::RELIABILITY reliability, const STRING& testtext= "");
```

To avoid ambiguity when a
const char *
 (string) is given as

testtext
 parameter we provide explicit versions of all of
those signatures with default parameters as well (as the compiler would otherwise
prefer conversion to a
Boolean
 (i.e.
Continue

parameter), over conversion via
STRING
 constructor with

const char *
):

```
void SMC_TEST(const STRING& pin, const STRING& testname, DOUBLE value, Boolean Continue, INT testNumber, const STRING& softbin, INT hardbin, const char * testtext);
void SMC_TEST(const STRING& pin, const STRING& testname, DOUBLE value, Boolean Continue, TM::RELIABILITY reliability, INT testNumber, const STRING& softbin, INT hardbin, const char * testtext);
void SMC_TEST(const STRING& pin, const STRING& testname, const LIMIT& limit, DOUBLE value, Boolean Continue, INT testNumber, const STRING& softbin, INT hardbin, const char * testtext);
void SMC_TEST(const STRING& pin, const STRING& testname, const LIMIT& limit, DOUBLE value, Boolean Continue, TM::RELIABILITY reliability, INT testNumber, const STRING& softbin, INT hardbin, const char * testtext);
void SMC_TEST(const STRING& pin, const STRING& testname, V93kLimits::TMLimits& limits, DOUBLE value, Boolean Continue, const char * testtext);
void SMC_TEST(const STRING& pin, const STRING& testname, V93kLimits::TMLimits& limits, DOUBLE value, const char * testtext);
void SMC_TEST(const STRING& pin, const STRING& testname, V93kLimits::TMLimits& limits, DOUBLE value, Boolean Continue, TM::RELIABILITY reliability, const char * testtext);
```

Additional interface which allows specifying the site:

```
void SMC_TEST(INT site, const STRING& pin, const STRING& testname, DOUBLE value, Boolean Continue, INT testNumber, const STRING& softbin, INT hardbin, const char * testtext);
void SMC_TEST(INT site, const STRING& pin, const STRING& testname, DOUBLE value, Boolean Continue, TM::RELIABILITY reliability, INT testNumber, const STRING& softbin, INT hardbin, const char * testtext);
void SMC_TEST(INT site, const STRING& pin, const STRING& testname, const LIMIT& limit, DOUBLE value, Boolean Continue, INT testNumber, const STRING& softbin, INT hardbin, const char * testtext);
void SMC_TEST(INT site, const STRING& pin, const STRING& testname, const LIMIT& limit, DOUBLE value, Boolean Continue, TM::RELIABILITY reliability, INT testNumber, const STRING& softbin, INT hardbin, const char * testtext);
void SMC_TEST(INT site, const STRING& pin, const STRING& testname, V93kLimits::TMLimits& limits, DOUBLE value, Boolean Continue, const char * testtext);
void SMC_TEST(INT site, const STRING& pin, const STRING& testname, V93kLimits::TMLimits& limits, DOUBLE value, const char * testtext);
void SMC_TEST(INT site, const STRING& pin, const STRING& testname, V93kLimits::TMLimits& limits, DOUBLE value, Boolean Continue, TM::RELIABILITY reliability, const char * testtext);
```

This API is defined in the header file

/opt/hp93000/soc/prod_com/include/MAPI/SMART_CALC2.h
.

Parameters
[表]
列: Parameter | Description
行 1:
  site
  The site number
行 2:
  pin
  The pin name (single pin name).
行 3:
  testname
  The test name that can be referred from the
    Properties view.
行 4:
  tmLimit
  Specifies the `TMLimits`（raw: `110432.htm`）`object`（raw: `110432.htm`） which will be used to
    extract the data for testNumber,
    softbin, hardbin as well as the limit data.
行 5:
  limit
  The (optional) limit value to be used for the
    judgment. This parameter is a `LIMIT`（raw: `29504.htm`）
    API's class object. Hence, you can specify
    TM::Pass or
    TM::Fail to make the test
    result pass or fail intentionally.
    
    If the parameter limit is not
    specified, the limit values specified in the
    properties view of the test suite containing `SMC_SYNCHRONIZE()`（raw: `120088.htm`） will be used.
    
    If you specify TM:Pass within the
    `LIMIT`（raw: `29504.htm`） class, the test alway will
    pass, regardless of the actual test result.
    
    If you specify TM:Fail within the
    `LIMIT`（raw: `29504.htm`） class, the test always will
    fail, regardless of the actual result.
行 6:
  value
  The test result value.
行 7:
  Continue
  This optional parameter controls whether the test
    should be continued if SMC_TEST()
    evaluates to FAIL. If it is set to
    TRUE, the test is continued in
    spite of a real FAIL result. If it is set to
    FALSE (default), the test is
    terminated.
    
    Note The API behaves differently for the
    first site in a multi-site setup. In this special
    situation, the test is always continued, even if the
    TEST API returns FAIL and the continue parameter is
    set to FALSE. For the following
    sites, the test is terminated under these
    conditions.
行 8:
  reliability
  This optional parameter is used to indicate the
    reliability of the test result for data logging.
    
    To indicate the test is reliable, specify
    TM::RELIABLE.
    
    To indicate the test is unreliable, specify
    TM::UNRELIABLE.
    
    You can omit this parameter. If so, use the syntax
    without this parameter. At that time, it is the same
    as specifying TM::RELIABLE.
    
    Note SMC_TEST() does not
    log the reliable state even if the parameter is set
    to TM::RELIABLE.
行 9:
  testNumber
  An integer value that you assign to directly generate
    a subtest test number in the EDL. Value must be >=
    0.
行 10:
  softbin
  The software bin number of the multibin. For details
    see the `SET_MULTIBIN`（raw: `100114.htm`） API.
行 11:
  hardbin
  The hardware bin number of the multibin. For details see the `SET_MULTIBIN`（raw: `100114.htm`） API.
行 12:
  logTestNumber
  An optional test number.
    
    If this test number is provided, it overrides the actual test number. If it is not
    provided, the actual test number is logged.
行 13:
  testtext
  Text be added to the data log stream for this
    SMC_TEST() call.
Return value
There is no return value.

### Examples（取自子主题 SMC_TEST()）

### Example 1: General usage

SMC_TEST()
 compares
the
thd_result
 data with the limit range specified in the
parameter dialog of
`SMC_SYNCHRONIZE()`（raw: `120088.htm`）
, then judges it as pass or
fail.

```
SMC_TEST("dgtz_pin", "THD", thd_result);
```

The first

SMC_TEST()
 call judges the
thd_result
 data
as pass or fail. Then the second
SMC_TEST()
 judges the

snr_result
 data as pass or fail because the

TM::CONTINUE
 is set int the first

SMC_TEST()
. When the result of the first

SMC_TEST()
 is pass, the test will continue even if you do not
set the
Continue
 parameter to

TRUE
.

```
SMC_TEST("dgtz_pin", "THD", thd_result, TM::CONTINUE);
SMC_TEST("dgtz_pin", "SNR", snr_result);
```

SMC_TEST()

compares the
thd_result
 data with the limit range specified by
the
`LIMIT`（raw: `29504.htm`）
 API, then judges as pass or
fail.

```
SMC_TEST("Aout", "THD", LIMIT(TM::GT, low_limit,TM::LT, high_limit), thd_result);
```

SMC_TEST()

compares the
thd_result
 data with the limit range specified by
the
`LIMIT`（raw: `29504.htm`）
 API, then judges as pass or fail. In fail case it will
bin into the specified
softbin
 and

hardbin
.

```
SMC_TEST("Aout", "THD", LIMIT(TM::GT, low_limit,TM::LT, high_limit), thd_result, false, testNumber, "softbin", hardbin);
```

### Example 2: Using hidden data logging

The following example shows
how hidden data logging can be implemented using the
`LIMIT`（raw: `29504.htm`）
 class,
without having the
hidden_datalog_mode
 testflow flag enabled.

```
#include "testmethod.hpp"
#include "mapi.hpp"

using namespace std;

class hiddenDatalogWLimit: public testmethod::TestMethod
{
protected:

virtual void initialize()
{
addLimit("TestName");
}

virtual void run()
{
ON_FIRST_INVOCATION_BEGIN();
{
SMC_EXECUTE_TEST( 1.0 );

LIMIT lim = GET_LIMIT_OBJECT("TestName");

FOR_EACH_SITE_BEGIN()
{
SMC_ARM(lim);
}
FOR_EACH_SITE_END();
}
ON_FIRST_INVOCATION_END();

return;
}

public:

void SMC_backgroundProcessing(LIMIT lim)
{
INT site = SMC_SITE_NUMBER();
double result = ...;

cout << "Site: <" << site << "> " << endl;

SMC_TEST(site, "PinName","TestName", lim, result);
}
};
REGISTER_TESTMETHOD("hiddenDatalogWLimit", hiddenDatalogWLimit);
```

Note

The example above contains a call of
cout
 in function
`SMC_backgroundProcessing()`（raw: `120107.htm#_120107__s_SMC_backgroundProcessing`）
.
cout
 is not
thread safe. In production test
cout
 must never be used in a
background process.

When using
cout
 in a background process,
you have to expect a mix up of the output in the

ui_report
 window and possibly other unwanted
behavior. For more information, refer to
`Thread safety`（raw: `118825.htm`）
.

### Example 3: Using test tables

The following two examples show how
to use the limits and bins that a user has defined in a test table ( *.csv file).

tmLimits
 causes
SMC_TEST()
 to look at the
loaded test table file and to compare the value contained in

result
 to the limits of "PowerOut0" and to bin the result
accordingly.

```
SMC_TEST("dgtPinName", "PowerOut0", tmLimits, result, true);
SMC_TEST("dgtPinName", "PowerOut0", V93kLimits::tmLimits, result, true);
```

Do
not use the following code for background processing, because this will use the
system prepared
TestSet
 object, which is not thread
safe!

```
SMC_TEST("dgtPinName", "PowerOut0", tmLimits.getLimitObj("PowerOut0"), result, true);
```

### Example 4: Handling large numbers of sites

The following example shows
how to speed up the
SMC_TEST()
 execution when the large numbers
of sites increase the total computing time.

The transfer of the required data
from function
run()
 to function

backgroundProcessing()
 is done via member variables

mResultArray
 and
mActiveSitesArray
.
Transferring the data as parameter of
SMC_ARM()
 is also supported
but this will increase the test time because all data that are transferred to the
background process must be copied by
SMC_ARM()
. The array

mActiveSitesArray
 must be updated in function

run()
 before function

SMC_backgroundProcessing()
 is called to ensure that only
activated sites are
processed.

```
#include "testmethod.hpp"
#include "mapi.hpp"

using namespace std;

class hiddenDatalogSequential: public testmethod::TestMethod
{
protected:

ARRAY_D mResultArray;
ARRAY_I mActiveSitesArray;

virtual void initialize()
{
}

virtual void run()
{
ON_FIRST_INVOCATION_BEGIN();
{
//
// Initialize the result array for all configured sites
//
ARRAY_I configuredSitesArray;

mResultArray.resize (GET_CONFIGURED_SITES(configuredSitesArray));
mResultArray.init (-1.0);

//
// Start functional test and retrieve the result for active sites
//
FUNCTIONAL_TEST();

FOR_EACH_SITE_BEGIN()
{
Boolean result = GET_FUNCTIONAL_RESULT();

mResultArray[CURRENT_SITE_NUMBER()-1] = (double) result;
}
FOR_EACH_SITE_END();

//
// Show the result array
//
cout << "Result array:";

for (int index = 0; index < mResultArray.size(); index++)
{
cout << " " << mResultArray[index];
}

cout << endl;

//
// Get and show active sites
//
GET_ACTIVE_SITES(mActiveSitesArray);

cout << "Active sites:";

for (int index = 0; index < mActiveSitesArray.size(); index++)
{
cout << " " << mActiveSitesArray[index];
}

cout << endl;

//
// Arm the SMC_backgroundProcessing() method
//
// Note: Data are transferred by member variables mResultArray[] and mActiveSitesArray[].
//
SMC_ARM();
}
ON_FIRST_INVOCATION_END();

} // virtual void run()

public:

void SMC_backgroundProcessing()
{
//
// Parse the resultArray array for all active sites
//
for (int index = 0; index < mActiveSitesArray.size(); index++)
{
double result = mResultArray[mActiveSitesArray[index] - 1];

cout << "SMC - Processing site " << mActiveSitesArray[index] << " - Result = " << result << endl;

SMC_TEST(mActiveSitesArray[index], "PinName", "TestName", result);
}

} // void SMC_backgroundProcessing ...

}; // class hiddenDatalogSequential: public testmethod::TestMethod

REGISTER_TESTMETHOD("hiddenDatalogSequential", hiddenDatalogSequential);
```

Note

The example above contains a call of
cout
 in function
`SMC_backgroundProcessing()`（raw: `120107.htm#_120107__s_SMC_backgroundProcessing`）
.
cout
 is not
thread safe. In production test
cout
 must never be used in a
background process.

When using
cout
 in a background process,
you have to expect a mix up of the output in the

ui_report
 window and possibly other unwanted
behavior. For more information, refer to
`Thread safety`（raw: `118825.htm`）
.

In offline mode, the example above results in the following output in the

ui_report
 window if eight sites are configured, sites 3 and 7
are
deactivated:

```
Result array: 1 1 -1 1 1 1 -1 1
Active sites: 1 2 4 5 6 8
SMC - Processing site 1 - Result = 1
Testsuite: Test_2 PASSED on site 1
SMC - Processing site 2 - Result = 1
SMC - Processing site 4 - Result = 1
SMC - Processing site 5 - Result = 1
SMC - Processing site 6 - Result = 1
SMC - Processing site 8 - Result = 1
Testsuite: Test_2 PASSED on site 2
Testsuite: Test_2 PASSED on site 4
Testsuite: Test_2 PASSED on site 5
Testsuite: Test_2 PASSED on site 6
Testsuite: Test_2 PASSED on site 8
```

### Syntax（取自子主题 SMC_SYNCHRONIZE()）

```
Boolean SMC_SYNCHRONIZE(DOUBLE timeout = 0);
Boolean SMC_SYNCHRONIZE(DOUBLE timeout, Boolean forceErrorExitOnFail);
Boolean SMC_SYNCHRONIZE(INT *noOfSMCExecutedTests, DOUBLE timeout = 0);
Boolean SMC_SYNCHRONIZE(INT *noOfSMCExecutedTests, DOUBLE timeout, Boolean forceErrorExitOnFail);
```

This
API is defined in the header file

/opt/hp93000/soc/prod_com/include/MAPI/SMART_CALC2.h
.

Parameters
[表]
列: Parameter | Description/Range
行 1:
  timeout
  The time in seconds after which a thread should be
    canceled and SMC_SYNCHRONIZE()
    should not wait for its completion.
    
    Resolution: 1 µs
    
    The accuracy of this parameter is influenced by the
    overhead time of the operating system.
    
    The default value is 0.0 seconds which means that no timeout is set.
行 2:
  noOfSMCExecutedTests
  References a pointer to store the number of `SMC_TEST()`（raw: `120084.htm`） statements
    which have been executed during this synchronize operation per site.
    
    Note
    
    When using the class SMC_ARM_FOR_SITES() or
    SMC_ARM_OTHER_TS_FOR_SITES(),
    SMC_SYNCHRONIZE() does not not return a test count. As a result,
    noOfSMCExecutedTests is not incremented and does not count the
    number of calls to SMC_TEST().
行 3:
  forceErrorExitOnFail
  Enables a forced exit on an error. If set to
    
    true - it causes an
    exception in case a calculation routine had to be
    aborted.
    
    false - it causes
    SMC_SYCHRONIZE() to return
    false in case a calculation
    routine had to be aborted.
Return value

Returns
false
 in case threads had to be terminated or an invocation error
occurred, else
true
 is returned.

If the
noOfSMCExecutedTests
 parameter is used, the number of
`SMC_TEST()`（raw: `120084.htm`）
 statements which have been executed during this
synchronize operation per site will be stored in the integer variable
referenced by the pointer.

### Example（取自子主题 SMC_SYNCHRONIZE()）

Waits for all calculations to be finished within 100 ms. After the timeout of
100 ms all other still running calculation threads will be
terminated!

```
SMC_SYNCHRONIZE(100 ms);
```

Waits for all
calculations to be finished within 10 ms. After the timeout of 10 ms all other still
running calculation threads will be terminated! In case a calculation had to
terminated,
SMC_SYNCRONIZE()
 throws an
exception.

```
SMC_SYNCHRONIZE(10 ms, true);
```

### Examples（取自子主题 Use of SMC_TEST() with multibin）

### Example 1: Single SMC test

The first failing test of SMC_TEST_5 logs to the multibin.

[表]
行 1:
  
  Code snippet from
    SMC_TEST_5:
    
    ```
    Virtual void run()
    {
    SMC_TEST("cx0","test",V93kLimits::tmLimits,0,true);
    SMC_TEST("cx1","test",V93kLimits::tmLimits,0,true);
    
    return;
    }
    ```
    
    If
    both tests fail, the first one (failing cx0) will be logged into
    the multibin.

### Example 2: Multiple SMC tests

The first failing test of
SMC_TEST_5
 and
SMC_TEST_6

logs to the multibin.

[表]
行 1:
  
  If all tests fail, the first one of
    SMC_TEST_5 will be logged into the
    multibin.
    
    If all tests of SMC_TEST_5 pass, the first one
    of SMC_TEST_6 will be logged into the
    multibin.

### Examples（取自子主题 Use of TESTSET and SMC_TEST() test suites with multibin）

### Example 1: Failing non-SMC test followed by failing SMC test
[表]
行 1:
  
  In a testflow a test of the non-SMC test suite
    TESTSET_6 fails before a test of
    SMC_TEST_4 fails and before
    SMC_SYNCHRONIZE is called.
    
      [子表]
      列: Test suite | Type | State | Bin
      子行 1:
        TESTSET_6
        non-SMC
        Fail
        Logged
      子行 2:
        SMC_TEST_4
        SMC
        Fail
        
      子行 3:
        SMC_TEST_5
        SMC
        Fail
        
      子行 4:
        SMC_SYNCHRONIZE
        SMC
        n.a.
        
    
    The failing test of non-SMC test suite TESTSET_6
    is logged to the multibin.

### Example 2: Failing SMC test followed by failing non-SMC test
[表]
行 1:
  
  In a testflow a test of the non-SMC test suite
    TESTSET_6 fails after a test of
    SMC_TEST_4 fails but before
    SMC_SYNCHRONIZE is called.
    
      [子表]
      列: Test suite | Type | State | Bin
      子行 1:
        SMC_TEST_4
        SMC
        Fail
        
      子行 2:
        TESTSET_6
        non-SMC
        Fail
        Logged
      子行 3:
        SMC_TEST_5
        SMC
        Fail
        
      子行 4:
        SMC_SYNCHRONIZE
        SMC
        n.a.

### Example 3: Failing SMC test followed by multiple failing non-SMC test using temporary TESTSET() objects
[表]
行 1:
  
  In a testflow a test of both the non-SMC test suites
    TESTSET_6 and TESTSET_7
    fails after a test of SMC_TEST_4 fails but
    before SMC_SYNCHRONIZE is called. Both non-SMC
    testsuites are using temporary TESTSET()
    objects. All tests fail before SMC_SYNCHRONIZE
    is called.
    
    Additional to the rule explained above, the rule for multiple
    test suites with temporary TESTSET objects
    applies (see `Multiple usage of the temporary object`（raw: `145088.htm#_145088__dle_Multiple_usage_of_the_temporary_object`） in `Use of TESTSET with multibin`（raw: `145088.htm`）).
    
    The failing test of TESTSET_7 is logged to the
    multibin.
    
      [子表]
      列: Test suite | Type | State | Bin
      子行 1:
        SMC_TEST_4
        SMC
        Fail
        
      子行 2:
        TESTSET_6
        non-SMC
        Fail
        
      子行 3:
        TESTSET_7
        non-SMC
        Fail
        Logged
      子行 4:
        SMC_TEST_5
        SMC
        Fail
        
      子行 5:
        SMC_SYNCHRONIZE
        SMC
        n.a.

### Example 4: System prepared TestSet object in combination with temporary TESTSET object
[表]
行 1:
  
  In a testflow all tests of the test suite
    TestSet (using the system-prepared
    TestSet object) and test suite
    TESTSET_temporary (using a temporary
    TESTSET() object) fail after a test of
    SMC_TEST_4 fails but before
    SMC_SYNCHRONIZE is called.
    
    Additional to the rule explained above, the rule for multiple
    test suites using temporary TESTSET() objects
    applies (see Multiple test suites section in `Use of TESTSET with multibin`（raw: `145088.htm`）).
    
    The failing test of TESTSET_temporary is logged
    to the multibin.
    
      [子表]
      列: Test suite | Type | State | Bin
      子行 1:
        SMC_TEST_4
        SMC
        Fail
        
      子行 2:
        TestSet
        non-SMC
        Fail
        
      子行 3:
        TESTSET_temporary
        non-SMC
        Fail
        Logged
      子行 4:
        SMC_TEST_5
        SMC
        Fail
        
      子行 5:
        SMC_SYNCHRONIZE
        SMC
        n.a.

<!-- 语法节 end -->

## 是什么

**文档事实** TESTSET 是测试方法 API 中的一个类，文档称它访问一个数据容器，该容器保存“某个 test suite 中结果的编号过程（numbering procedures）”所需信息，并用于指定与 TEST API 及 test method 相关的全部选项。

**文档事实** 构造函数：
- `TESTSET()` 创建上述类对象。
- `TESTSET(bool withContext, INT site)` 额外指定要处理的 site；文档要求 `withContext` 必须设为 `false`。

**文档事实** 文档给出的对象形式与限制：
- 系统预制对象为 `TestSet`，该预制对象不能在 SMC 框架内使用。
- 也可以创建临时对象或用户对象。
- `TESTSET` 对象不得跨多个线程共享；若用于 SMC 后台处理，应只在 `SMC_backgroundProcessing()` 方法内创建和使用。
- 成员函数设置的参数会一直保持，直到被重置或恢复为默认设置。
- 头文件：`/opt/hp93000/soc/prod_com/include/MAPI/TestSet_r.h`。

## 典型用法

**文档事实** 文档给出的对象用法：
- 临时对象：`TESTSET().member_func().judgeAndLog_xxx(parameters);`
- 指定 site 的临时对象：`TESTSET(false, site).member_func().judgeAndLog_xxx(parameters);`
- 系统预制对象：`TestSet.member_func().judgeAndLog_xxx(parameters);`（SMC 框架内不可用）
- 用户对象：`TESTSET obj; obj.member_func().judgeAndLog_xxx(parameters);`

**文档事实** 常见组合是先调用 `cont()`、`port()`、`testnumber()` 等设置条件，再调用 `judgeAndLog_*` 进行判定和记录，例如：
- `TESTSET().cont(true).judgeAndLog_ParametricTest("dgtz_pin", "THD", thd_result);`
- `TESTSET().port("port").judgeAndLog_FunctionalTest();`
- `TESTSET().judgeAndLog_Dps(dpsTask);`

**文档事实** 编号方面，`testnumber()` 支持按 Properties view 中的 test name 取 offset/increment、直接给整数编号，或传入 `TESTNUMBER` 对象；`testnumber_default()` 生成默认 test ID（test table 编号与 Properties view 的 Flags 区编号之和；若不用 test table，则为 Limits 区编号与 Flags 区编号之和），`testnumber_none()` 不为当前测试写 test number（即使 `test_number_enable` 已启用）。文档 Example 1 中 `TestSet.cont(true).testnumber(sdc6);` 之后的多次 `TEST()` 共用同一编号条件。

**文档事实** 文档 Example 4 在高阻/功能测量后，于 `ON_FIRST_INVOCATION_END();` 之后调用 `TESTSET().judgeAndLog_FunctionalTest();`，即先测量、再判定并记录。

## 和谁有关

以下关系均来自文档正文、子主题或入边语境：

- 与 TESTNUMBER、GET_TESTNUMBER：Related information 明确列出。`testnumber(TESTNUMBER&)` 使用 TESTNUMBER 的 offset/increment 生成 subtest test number；`GET_TESTNUMBER("name")` 返回的 TESTNUMBER 可直接传给 `testnumber()`。
- 与 TEST()：`testname()`、`testnumber()` 的设置作用于随后调用的 `TEST()` 方法；文档警告 `TEST()` 必须在 TESTNUMBER 变量作用域内调用，否则出错并停止测试方法。
- 与 TMLimits（`V93kLimits::TMLimits`）：多个 `judgeAndLog_*` 重载直接接收 `tmLimits`，按测试表中的 limit/bin 信息判定；文档给出了 tmLimits 的 first-fail 分 bin 规则。
- 与各类测量/结果对象：`judgeAndLog_FunctionalTest()`、`judgeAndLog_ParametricTest()`、`judgeAndLog_PmuIfvm()`、`judgeAndLog_PmuVfim()`、`judgeAndLog_Dps()`、`judgeAndLog_DpsVfim()`、`judgeAndLog_Spmu()`、`judgeAndLog_PpmuMeasure()`、`judgeAndLog_SpecSearch()`、`judgeAndLog_PptiaTask()`、`judgeAndLog_ScanTest()`、`judgeAndLog_DcResultAccessor()`、`doLog_ShmooTest()` 分别以 PMU_IFVM、PMU_VFIM、DPS_TASK、DPS_VFIM、SPMU_TASK、PPMU_MEASURE、SPEC_SEARCH、PPTIA_TASK、SCAN_TEST_RESULT、DC_RESULT_ACCESSOR、ShmooData 等对象为输入。
- 与 ON_FIRST_INVOCATION_BEGIN/END：TESTSET 的示例把测量放在 first-invocation block 内、把 `judgeAndLog_*` 放在 block 外；ON_FIRST_INVOCATION_BEGIN 页面也明确禁止在 first-invocation block 内使用 TEST()、LIMIT() 和 judgeAndLog_* 语句（入边证据）。
- 与 SMC / SmartCalc：系统预制 `TestSet` 非线程安全，不能用于 SMC；SMC 中应使用 `SMC_TEST()` 或动态创建的 `TESTSET().judgeAndLog_*()`；文档示例用 `TESTSET(false, mActiveSites[siteIndex])` 在 SMC 后台按 site 处理。`judgeAndLog_ParametricTest()` 自 7.1.4 起可在 SMC 框架内使用（版本记录）。
- 与 SET_MULTIBIN：`judgeAndLog_ParametricTest()` 的 `softBin` / `hardBin` 参数文档中指向 `SET_MULTIBIN` API。
- 与数据记录（EDL/STDF）：参数表与示例说明判定结果写入 EDL/STDF；`doLog_ShmooTest()` 可指定 log test number；文档提醒 STDF 只保证前 6 位数值被正确记录。

## 版本

`Functional changes` 原文记录：
- Introduced before SmarTest 6.3.2
- SmarTest 6.5.0: New member function judgeAndLog_ScanTest()
- SmarTest 6.5.1: testtext() text can replace the content of Test_TXT or be appended to it
- SmarTest 6.5.2: New member function doLog_ShmooTest()
- SmarTest 6.5.2: New member function judgeAndLog_Dps()
- SmarTest 6.5.2: New member function judgeAndLog_Spmu()
- SmarTest 6.5.3: New member functions hlmfmt(), llmfmt(), resfmt()
- SmarTest 7.0.3: Removed test number manager
- SmarTest 7.1.0: Added specifications for judgeAndLog_FunctionalTest()
- SmarTest 7.1.4: Enhanced judgeAndLog_ParametricTest() function can be used within SMC framework.
- SmarTest 7.1.4: New member function combineMultiPortTests().
- SmarTest 7.2.0: Removed test_number_manager flag
- SmarTest 7.2.1: New member function suppressTestnameLoopCount().
- SmarTest 7.2.2: Enhanced judgeAndLog_FunctionalTest() and judgeAndLog_ScanTest() functions can be used within SMC framework.
- SmarTest 7.5.0: New member function addAlarm()
- SmarTest 7.5.1: New signatures for testnumber()
- SmarTest 7.5.2: Renamed forceSTDFTestNam parameter to forceSTDFTestName

## 出处

- 主文档：`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244_TESTSET.htm`（Class definition、Syntax descriptions、Examples、Subtopics、Related information、Functional changes）。
- 语法/参数材料另取自其子主题 `02.07.04.01.244.01`–`02.07.04.01.244.33`（`TESTSET().*.htm`），以及 `02.07.04.01.250_TMLimits.htm`、`02.07.04.01.99_GET_TESTNUMBER.htm` 等（objscaffold 逐字汇总，已读）。
