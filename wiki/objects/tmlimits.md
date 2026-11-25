---
type: object
title: TMLimits
layer: L3
stage: testmethod
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.250_TMLimits.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# TMLimits

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **25,124 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.250_TMLimits.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Class definition

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

### Member functions

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

### Examples

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
