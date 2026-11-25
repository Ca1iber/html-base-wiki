---
type: object
title: SMC_TEST()
layer: L2
stage: testmethod
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.231.45_SMC_TEST.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# SMC_TEST()

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **15,909 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.231.45_SMC_TEST.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

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

### Examples

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
