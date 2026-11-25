---
type: object
title: DC_RESULT_ACCESSOR
layer: L3
stage: testmethod
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.28_DC_RESULT_ACCESSOR.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# DC_RESULT_ACCESSOR

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **20,213 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.28_DC_RESULT_ACCESSOR.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Class definition

The API consists of the central
DC_RESULT_ACCESSOR
 class and following
helper classes:

`RESULT_POINT`（raw: `99164.htm`）

`RESULT_POINT_LIST`（raw: `99163.htm`）

`RESULT_FAIL_INFO`（raw: `99162.htm`）

This API is defined in the header file

/opt/hp93000/soc/prod_com/include/MAPI/DcResultAccessor.h.

Constructor:

```
DC_RESULT_ACCESSOR();
DC_RESULT_ACCESSOR(const STRING& dcResultConfigurationSetName);
```

[表] Parameters
行 1:
  dcResultConfigurationSetName
  Defines the result configuration set to be set before data uploading.

Member Functions:

`uploadResult()`（raw: `99071.htm#_99071__dle_uploadResult`）

`uploadFailedResult()`（raw: `99071.htm#_99071__dle_uploadFailedResult`）

`getRangeOfAvailableResults()`（raw: `99071.htm#_99071__dle_getRangeOfAvailableResults`）

`getNumberOfAvailableResults()`（raw: `99071.htm#_99071__dle_getNumberOfAvailableResults`）

`getFirstResultPoint()`（raw: `99071.htm#_99071__dle_getFirstResultPoint`）

`getLastResultPoint()`（raw: `99071.htm#_99071__dle_getLastResultPoint`）

`getMeasurementType()`（raw: `99071.htm#_99071__dle_getMeasurementType`）

`getPassFail()`（raw: `99071.htm#_99071__dle_getPassFail`）

`getFailInfo()`（raw: `99071.htm#_99071__dle_getFailInfo`）

`getValue()`（raw: `99071.htm#_99071__dle_getValue`）

`getValues()`（raw: `99071.htm#_99071__dle_getValues`）

`getExpectedResult()`（raw: `99071.htm#_99071__dle_getExpectedResult`）

### Member functions

uploadResult()

```
TM::RESULT_RANGE uploadResult(const INT site,
const STRING& pins,
const TM::RESULT_ADDRESSSING_SCHEME& addressingScheme );
```

Uploads all measurement results for the specified pins. The specified
addressing scheme defines the index type with that the results can be
accessed later on. The return value is a

TM::RESULT_RANGE
 object, which specifies the
range of available results.

```
void uploadResult(const INT site,
const STRING& pins,
const TM::RESULT_ADDRESSSING_SCHEME& addressingScheme,
const TM::RESULT_RANGE& requestedResultRange );
```

Uploads all measurement results for the specified pins with a specific
result range.

RESULT_RANGE
 is a struct type
describing a range of results. It consists of the following fields:

addressingScheme
 of type

TM::ADDRESSING_SCHEME,

specifying the addressing scheme of the range. Can be so far
only
TM::RESULT_INDEX
.

first
 of type

RESULT_POINT::IndexType
,

representing
the first result index in the range.

length
 of type

RESULT_INDEX::DistanceType
,

representing
the number of results in the range.

gangIndex

representing the gang index in
case of ganged channels. It is usually used only when the

RESULT_RANGE
 struct is an input
parameter for a function. It is usually not returned (i.e.
always set to '0') by functions returning the

RESULT_RANGE
 struct.

[表] Parameters
行 1:
  site
  The sites to combine in one thread.
行 2:
  pins
  The pins to work with.
行 3:
  addressingScheme
  The index type that the results can be accessed.
    Currently it can only be
    RESULT_INDEX.
行 4:
  requestedResultRange
  The range of results to upload.
uploadFailedResult()

```
TM::RESULT_RANGE uploadFailedResult(const STRING& pins,
const TM::RESULT_ADDRESSSING_SCHEME& addressingScheme );
```

Uploads failed measurement results for the specified pins. The specified
addressing scheme defines the index type with that the results can be
accessed later on. The return value is a

TM::RESULT_RANGE
 object, which specifies the
range of available results. The range can be non-continuous (for
example, index 1,3,4,8) or even empty if there were no fails.

```
void uploadFailedResult(const STRING& pins,
const TM::RESULT_ADDRESSSING_SCHEME& addressingScheme,
const TM::RESULT_RANGE& requestedResultRange );
```

Uploads failed measurement results for the specified pins with a specific
result range.

[表] Parameters
行 1:
  pins
  The pins to work with.
行 2:
  addressingScheme
  The index type that the results can be accessed.
    Currently it can only be
    RESULT_INDEX.
行 3:
  requestedResultRange
  The range of results to upload.
getRangeOfAvailableResults()

```
TM::RESULT_RANGE getRangeOfAvailableResults(const STRING& pins,
const TM::RESULT_ADDRESSSING_SCHEME& addressingScheme);
```

Returns a
TM::RESULT_RANGE
 object, which holds the
information about the index of the first available result and the length
of the available result range. The obtained

TM::RESULT_RANGE
 object can be used to specify
the range of results to upload in subsequent

uploadResult()
 or

uploadFailedResult()
 calls.

[表] Parameters
行 1:
  pins
  The pins to work with.
行 2:
  addressingScheme
  The index type that the results can be accessed.
    Currently it can only be
    RESULT_INDEX.
getNumberOfAvailableResults()

```
RESULT_POINT::DistanceType getNumberOfAvailableResults(const STRING& pins);
```

Returns the number of previously uploaded results. If only failed results
have been uploaded, the number of results might be less than the length
of the result range that can be queried with

getRangeOfAvailableResults()
.

[表] Parameters
行 1:
  pins
  The pins to work with.
getFirstResultPoint()

```
RESULT_POINT getFirstResultPoint(const STRING& singlePin);
```

Returns a
RESULT_POINT
 object which references the
first available result for the specified pin on the current site in
focus. Using the increment operator ++ (or other operators) on this

RESULT_POINT
 object allows accessing the
succeeding results for the same pin.

[表] Parameters
行 1:
  singlePin
  The pin to work with.
getLastResultPoint()

```
RESULT_POINT getLastResultPoint(const STRING& singlePin);
```

Returns a
RESULT_POINT
 object which references the
last available result for the specified pin on the current site in
focus. It can be used in an iteration to compare to the actual

RESULT_POINT
 in order to determine the loop stop
condition. Since this
RESULT_POINT
 references an
existing result, loops using it in a comparison should use the

<=
 operator.

[表] Parameters
行 1:
  singlePin
  The pin to work with.
getMeasurementType()

```
TM::PHYSICAL_VALUE getMeasurementType(const STRING& singlePin,
Const RESULT_POINT& resultPoint);
```

Returns the measurement type for a specific result point. So far the
types
TM::VOLTAGE
 and
TM::CURRENT

may be returned.

[表] Parameters
行 1:
  singlePin
  The pin to work with.
行 2:
  resultPoint
  The RESULT_POINT to query.
getPassFail()

```
BOOLEAN getPassFail() const;
BOOLEAN getPassFail(const RESULT_POINT& result) const;
BOOLEAN getPassFail(const RESULT_POINT_LIST& listOfResults) const;
BOOLEAN getPassFail(const RESULT_POINT& result,
const RESULT_POINT::IndexType& resultIndex) const;
BOOLEAN getPassFail(const STRING& pins) const;
BOOLEAN getPassFail(const STRING& pins,
const RESULT_POINT& result,
const RESULT_POINT::IndexType& resultIndex ) const;
BOOLEAN getPassFail(const STRING& pins,
const RESULT_POINT_LIST& listOfResults) const;
```

These functions return
TRUE
 if the specified test
results are PASS; in case of FAIL test results the function returns

FALSE
. If you use

getPassFail()
 without parameter, it returns the
global pass/fail result. If you supply the pin name, it returns the
result for the specified pin (all available results for this pin are
ANDed). The same applies if you use a range of results or a combination
of these two access methods.

Use these methods only if the previous
uploadResult()

call specifies to upload ALL results (
uploadAllResults =
TRUE
), otherwise it will always return FAIL.

[表] Parameters
行 1:
  result
  Specifies the test result point for which to return
    the TRUE or FALSE
    result.
行 2:
  listofResults
  Specifies the test result points array for which to
    return the TRUE or
    FALSE result.
行 3:
  resultIndex
  Specifies the result index for example, index of a ganged
    channel).
行 4:
  pins
  Specifies the pins for which to return the
    TRUE or FALSE
    result.
getFailInfo()

```
RESULT_FAIL_INFO getFailInfo() const;
RESULT_FAIL_INFO getFailInfo(const RESULT_POINT& result)const;
RESULT_FAIL_INFO getFailInfo(const RESULT_POINT& result,
const RESULT_POINT::IndexType& resultIndex )
const;
RESULT_FAIL_INFO getFailInfo(const RESULT_POINT_LIST& listofResults)
const;
RESULT_FAIL_INFO getFailInfo(const STRING& pins) const;
RESULT_FAIL_INFO getFailInfo(const STRING& singlePin,
const RESULT_POINT_ARRAY& listofResults)
const;
```

This function returns the fail information object from the status byte of
the specified FAIL results.

[表] Parameters
行 1:
  result
  Specifies the result point of the first pin for which
    a fail should be returned.
行 2:
  listofResult
  Specifies the result point array for which an
    accumulated fail information object (=status byte)
    should be returned.
行 3:
  resultIndex
  Specifies the result index for example, index of a ganged
    channel).
行 4:
  pins
  Specifies the pins for which an accumulated fail
    information object (=status byte) should be
    returned.
行 5:
  singlePin
  Specifies a single pin for which a fail information
    object (=status byte) should be returned.
getValue()

```
DOUBLE getValue( const RESULT_POINT& result)const;
DOUBLE getValue( const RESULT_POINT& result,
const RESULT_POINT::IndexType& resultIndex ) const;
DOUBLE getValue( const STRING& singlePin,
const RESULT_POINT& result)const;
DOUBLE getValue( const STRING& singlepin, const RESULT_POINT& result,
const RESULT_POINT::IndexType& resultIndex ) const;
```

Note
 It is recommended to use the syntax forms with parameter

RESULT_POINT
 or
LIST
 as that
they have the same functionality as those with the parameter

singlePin
.

CAUTION
 The uploaded value can be invalid. Use
`RESULT_FAIL_INFO`（raw: `99162.htm`）
 to check the reported value is valid and not
marked as fail.

This function extracts the measured value of the last uploaded result if
there is any value available. In contrast to the other result extractor
classes it operates only on one single pin. For the specified pin it
returns a single result specified by a result point.

[表] Parameters
行 1:
  result
  The result (RESULT_POINT) to be
    considered.
行 2:
  singlePin
  Specifies a single pin for which to return the
    specified result.
行 3:
  resultIndex
  Specifies the result index for example, index of a ganged
    channel).
行 4:
  resultPoint
  Specifies a test result point for which to return the
    specified result.
getValues()

```
ARRAY_D getValues( const RESULT_POINT_LIST& listOfResult ) const;
void getValues( const RESULT_POINT_LIST& listOfResult, ARRAY_D & values ) const;
ARRAY_D getValues( const INT site, const STRING& singlePin) const;
ARRAY_D getValues( const STRING& singlePin,
const RESULT_POINT_LIST& listofResults)const;
void getValues( const STRING& singlePin, ARRAY_D & values ) const;
```

Note
 It is recommended to use the syntax forms with parameter

RESULT_POINT
 or
LIST
 as that
they have the same functionality as those with the parameter

singlePin
.

CAUTION
 The uploaded values can be invalid. Use
`RESULT_FAIL_INFO`（raw: `99162.htm`）
 to check the reported values are valid and not
marked as fail.

This function extracts the measured value of the last uploaded results if
there are any values available. In contrast to the other result
extractor classes it operates only on one single pin. For the specified
pin it returns a range of results specified by an array of result
points, or all available results for this pin if no result points are
specified.

[表] Parameters
行 1:
  site
  Specifies the site
行 2:
  singlePin
  Specifies a single pin for which to return the
    measured value.
行 3:
  listofResults
  Specifies a test result point array for which to
    return the measured value.
getExpectedResult()

```
EXPECTED_RESULT getExpectedResult( const RESULT_POINT& result ) const;
```

This function gets the test limits for the specified pin in the specified
result. The function returns an
EXPECTED_RESULT

object containing the specified limits and status information. Please
refer to
`RESULT_POINT`（raw: `99164.htm`）
 and
`LIMIT`（raw: `29504.htm`）
 for more
information.

[表] Parameters
行 1:
  result
  The result (RESULT_POINT) to
    be considered.

### Examples

### Note

The examples provide various approaches for the use of the
upload function
uploadResult()
. In the last example below, the

uploadResult()
 is called inside the ON_FIRST_BLOCK. This
reduces the test time considerably and, therefore, is the recommended
approach.

### Example 1
```
virtual void run()
{
ON_FIRST_INVOCATION_BEGIN();

// a) Measurement setup
// ...

// b) Measurement execution
// ...

ON_FIRST_INVOCATION_END();

// c) upload the results ...
// ...
STRING pin("dps1");

// Declare a DC_RESULT_ACCESSOR object to access the results
DC_RESULT_ACCESSOR results;

// Which results are available?
//
// NOTE:
// The returned result range contains the information about
// available number of results for the pin. If more than
// one pin is used for example, a group) the smallest common result
// range for both pins is returned.

TM::RESULT_RANGE resultRange =
results.getRangeOfAvailableResults(pin, TM::RESULT_INDEX);

if (resultRange.length > 0)
{
// Now upload the available results
//
// NOTE:
// results.uploadResult(pin, TM::RESULT_INDEX);
// would have the same effect, but calls
// getRangeOfAvailablResults() internally again.
// As this reduces performance, avoid this form of
// uploadResult() if you already have determined
// the range of available results.
// Instead specify the range explicitly.

results.uploadResult(pin, resultRange);

// d) process the results ...

// loop over the results ...
// Note that both first and last represent valid RESULT_POINTS.
// You must use "less or equal" (<=) in the comparison to include also the last
// RESULT_POINT. Using a "<" or "!=" operator in the comparison would drop the
// last result.

RESULT_POINT currentPoint = results.getFirstResultPoint(pin);
RESULT_POINT lastPoint = results.getLastResultPoint(pin);

while (currentPoint <= lastPoint)
{
// check for pass/fail at the current RESULT_POINT
// As this example uploaded only fails, this condition
// will always be true.

if (! results.getPassFail(currentPoint))
{
// test at RESULT_POINT failed ...
// obtain more information on the failed result ...
// get the measurement value
DOUBLE val = results.getValue(currentPoint);

// obtain fail status information
RESULT_FAIL_INFO status = results.getFailInfo(currentPoint);
if (status.hasHighLimitFailed())
{
// measure value is higher than the high limit
// ...

}
else if (status.hasLowLimitFailed())
{
// ...

}
else if (status.hasMeasurementRangeViolation())
{
// ...

} // etc..

// go to next result
++currentPoint;
} // if
} // while
}

// pass/fail judgment and datalog
TEST(results);
}
```

### Example 2

Same as Example 1 above, except in block "c) upload the
results":

```
virtual void run()
{
STRING pin("dps1");
DC_RESULT_ACCESSOR results;

// This example uses the version of uploadResult() that returns the
// result range. Hence it is not necessary to call
// result.getRangeOfAvailablResults().
// This simplifies the code example above to:

TM::RESULT_RANGE resultRange = results.uploadResult(pin, TM::RESULT_INDEX);
if (resultRange.length > 0)
{
// similar as in Example 1

}
}
```

### Example 3

In this example, the upload function

uploadResult()
 is used and hence all available results
will be uploaded. The functions
getFirstResultPoint()
 and

getLastResultPoint()
 are used to obtain valid
RESULT_POINTs, which are then used in a "for" loop to iterate over all uploaded
results. In the "for" loop different extractor functions are used on the actual
result in order to obtain pass/fail information, measured value, and status byte
information.

```
virtual void run()
{
// ...
// Perform DC Dynamic measurement ....
ON_FIRST_INVOCATION_BEGIN();

// settings and relay switching ...
FUNCTIONAL_TEST();

ON_FIRST_INVOCATION_END();

// ...

STRING pin("dps1");

// upload the results
//
// Define a result accessor object
DC_RESULT_ACCESSOR allResults;

// Upload all available results for the pin in RESULT_INDEX addressing scheme.
// The variable "range" will contain the start index and the length of the uploaded
// result range. For uploadResult() the length is equal to the number of uploaded
// results but for uploadFailedResults() it is usually larger than the number of
// failed results.
// Before the result data can be accessed, they always first need to be uploaded from
// hardware/firmware. Each uploadResult() will overwrite the last uploaded results.
// (independent of the particular DC_RESULT_ACCESSOR object!).

const TM::RESULT_RANGE range(allResults.uploadResult(pin, TM::RESULT_INDEX));
if (range.length > 0)
{
// Use result accessor member functions getFirstResultPoint() and
// getLastResultPoint() to obtain iterators (RESULT_POINT objects) to the
// first and last uploaded results.

const RESULT_POINT first(allResults.getFirstResultPoint(pin));
const RESULT_POINT end (allResults.getLastResultPoint(pin));

// process the results

// Loop over the uploaded results using the first and end iterators (RESULT_POINTs)
// and the increment ("++") operator on an iterator (decrement is not supported).
for ( RESULT_POINT p = first; p <= end; ++p )
{
const bool testPassed = allResults.getPassFail(p);
const TM::PHYSICAL_VALUE type = allResults.getMeasurementType(p);

std::cout << "Test " << (testPassed ? " PASSED " : " FAILED ");
std::cout << ", Measured value " << allResults.getValue(p);
std::cout << ((type == TM::VOLTAGE) ? " V " : " A ");
std::cout << " at point " << p.getIndex();
std::cout << " at site " << CURRENT_SITE_NUMBER() << endl;

if (! testPassed)
{
// test has failed at this point
// obtain the status info to examine the fail reason...
const RESULT_FAIL_INFO failInfo = allResults.getFailInfo(p);

// print out the status bits ...
std::cout << " HighLimitFailed : " << failInfo.hasHighLimitFailed();

// ...
}
}
}

// set the test result and send data to datalog ...
TEST(allResults, TRUE);
}
```

### Example 4

This example shows how to use the
uploadResult()
 function in a

FOR_EACH_SITE_...
 block to upload the result of multiple sites. It utilizes
the
DC_RESULT_ACCESSOR
 constructor with string parameter, in order for

RESULT_AREA_CONFIG_SET
 to reference it.

```
virtual void run()
{
DC_RESULT_ACCESSOR result("dpsCurr");

ON_FIRST_INVOCATION_BEGIN();

RESULT_AREA_CONFIG_SET resSet("dpsCurr");
resSet.pin("dps1").setDcValueResultAreaSize(8192);
resSet.setAsPrimary();
FUNCTIONAL_TEST();
resSet.deselectGlobally();

FOR_EACH_SITE_BEGIN();

cout << "***Getting results for site: " << CURRENT_SITE_NUMBER() << endl;
TM::RESULT_RANGE resultRange = result.uploadResult("dps1",TM::RESULT_INDEX);

const RESULT_POINT first( result.getFirstResultPoint("dps1") );
const RESULT_POINT end ( result.getLastResultPoint("dps1") );
DOUBLE mea;
for (RESULT_POINT p = first; p <= end; p++)
{
mea = result.getValue("dps1", p);
cout << "*** Result on site "
<< CURRENT_SITE_NUMBER()
<< ": " << mea << endl;
cout << "*** P/F: " << result.getPassFail("dps1", p) << endl;
}

cout << "### P/F: " << result.getPassFail("dps1") << endl;

cout << "All results array: " << result.getValues("dps1") << endl << endl;

FOR_EACH_SITE_END();

ON_FIRST_INVOCATION_END();

return;
}
```

### Example 5

In this example
the
uploadResult()
 function is called inside the

ON_FIRST_INVOCATION...
 block. This reduces the test time
considerably and, therefore, is the recommended
approach.

```
virtual void run()
{
DC_RESULT_ACCESSOR result("dpsCurr");

ON_FIRST_INVOCATION_BEGIN();

FUNCTIONAL_TEST();

TM::RESULT_RANGE range;
range.first = 0;
range.length = 200;
result.uploadResult("dps1", TM::RESULT_INDEX, range);

ON_FIRST_INVOCATION_END();

const RESULT_POINT first( result.getFirstResultPoint("dps1") );
const RESULT_POINT end ( result.getLastResultPoint("dps1") );
DOUBLE measuredValue;
INT resPointNr = 1;

cout << "Results for site " << CURRENT_SITE_NUMBER() << endl;

for (RESULT_POINT p = first; p <= end; p++, resPointNr++)
{
measuredValue = result.getValue("dps1", p);
cout << "*** Result point: " << resPointNr << endl;
cout << "*** Measured value on dps1: "
<< measuredValue << endl;
cout << "*** P/F: " << result.getPassFail("dps1", p) << endl;
}

cout << "P/F: " << result.getPassFail("dps1") << endl;
cout << "All results: " << result.getValues("dps1") << endl << endl;

return;
}
```

<!-- 语法节 end -->

## 是什么

**文档事实** DC_RESULT_ACCESSOR 是 Test Method API，用于以一致的方式处理不同 pin 类型与不同测量类型的测量结果（原文：allows the consistent handling of measurement results for different pin types and measurement types）。

**文档事实** 它支持 DPS operating mode pin（用 DPS Pins editor 定义）与 PMU operating mode pin（用 Digital Pins editor 定义），可取得由 `DPS_TASK` 与 `SPMU_TASK` 建立的测量结果。支持的卡/模式：DC Scale DPS128 与 XPS256 的 DPS 和 PMU operating mode；DC Scale UHC4T pin 的 DPS operating mode。它不支持 legacy DPS pin（同样由 DPS Pins editor 定义）与数字通道 pin。

**文档事实** 它也支持由 `PPMU_...` 与 `BADC_...` API 定义的测量；DC Dynamic 测量主要由 DC event API 设置。文档提醒：DC profiling 期间每 pin 捕获的 sample 数可能略有差异，原因是 profiling 的内部触发不是 vector exact。

**文档事实** API 由中心类 `DC_RESULT_ACCESSOR` 与三个 helper 类 `RESULT_POINT`、`RESULT_POINT_LIST`、`RESULT_FAIL_INFO` 组成；头文件为 `/opt/hp93000/soc/prod_com/include/MAPI/DcResultAccessor.h`。构造函数可带 `dcResultConfigurationSetName`，用于在上传数据前设定 result configuration set。

**文档事实** 成员函数覆盖：上传全部结果（`uploadResult`）、只上传失败结果（`uploadFailedResult`）、查询可用结果范围/数量（`getRangeOfAvailableResults`、`getNumberOfAvailableResults`）、取首/末结果点（`getFirstResultPoint`、`getLastResultPoint`）、取测量类型（`getMeasurementType`）、取 pass/fail（`getPassFail`）、取失败状态字节（`getFailInfo`）、取单个/批量测量值（`getValue`、`getValues`）、取期望结果/限值（`getExpectedResult`）。当前结果寻址方案只有 `TM::RESULT_INDEX`。

**推断** 从“结果必须先上传”“测量由 DPS_TASK/SPMU_TASK 建立”可以看出，DC_RESULT_ACCESSOR 是测量执行之后的“结果上传与读取”层，而不是测量条件设置 API；这由文档的 upload 语义与支持的 setup API 列表归纳。

## 典型用法

**文档事实** 基本流程：建立并执行测量（由 `DPS_TASK`/`SPMU_TASK` 或 DC event/PPMU/BADC API）→ 用 `uploadResult()` 上传结果（可先 `getRangeOfAvailableResults()` 获取范围）→ 用 `getFirstResultPoint()`/`getLastResultPoint()` 取得 `RESULT_POINT` 迭代器 → 逐点用 `getPassFail()`、`getValue()`、`getMeasurementType()`、`getFailInfo()` 读取 → 用 `TEST(...)` 或 `TESTSET.judgeAndLog(DcResultAccessor)` 记录结果。

**文档事实** 上传全部结果可用 `uploadResult(pin, TM::RESULT_INDEX)`（返回 `TM::RESULT_RANGE`）或带显式范围的 `uploadResult(pin, TM::RESULT_INDEX, range)`；只上传失败结果用 `uploadFailedResult(...)`，其范围可能不连续（如 1,3,4,8），无失败时甚至为空。每次 `uploadResult()` 都会覆盖上一次上传的结果，且与具体 accessor 对象无关。若先后两个 pin，返回的是两 pin 的“最小公共结果范围”。

**文档事实** 迭代时必须包含最后一个 `RESULT_POINT`：文档明确要求用 `<=`，用 `<` 或 `!=` 会漏掉最后一条结果；`RESULT_POINT` 只支持 `++`，不支持 decrement。若已知范围，直接传 `range` 可避免 `uploadResult()` 内部再次调用 `getRangeOfAvailableResults()`，文档称这样可提升性能。

**文档事实** `getPassFail()` 无参数返回全局 pass/fail；给 pin 名时返回该 pin 所有可用结果的 AND；给结果范围或两者组合时同理。文档警告：只有在之前的 `uploadResult()` 指定上传 ALL results（`uploadAllResults = TRUE`）时才应使用这些方法，否则总是返回 FAIL。`getValue()` 取最后一个已上传结果的值；文档提示上传值可能无效，应先用 `RESULT_FAIL_INFO` 确认有效且未被标记为 fail。`getValues()` 对单 pin 返回值数组，不指定结果点时返回该 pin 全部可用结果；文档同样建议使用 `RESULT_POINT_LIST` 形式。

**文档事实** 多 site 示例：用 `DC_RESULT_ACCESSOR result("dpsCurr")` 绑定 result configuration set，配合 `RESULT_AREA_CONFIG_SET resSet("dpsCurr")`、`resSet.pin("dps1").setDcValueResultAreaSize(8192)`、`resSet.setAsPrimary()`，在 `FOR_EACH_SITE_BEGIN()` 中对每 site 调 `uploadResult` 并逐点读取。

**文档事实** 文档把在 `ON_FIRST_INVOCATION...` 块内调用 `uploadResult()`（Example 5）称为推荐做法，可显著减少测试时间。

**建议** 优先使用文档推荐的 `RESULT_POINT`/`LIST` 形式（而非 `singlePin` 形式）；读取 value 前用 `RESULT_FAIL_INFO` 校验；迭代用 `<=` 且只 `++`；若已取得范围就显式传入，避免重复查询。

## 和谁有关

- **文档事实** `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.50_DPS_TASK.htm`、`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234_SPMU_TASK.htm`：文档明确本 API 取得由这两个 API 建立的测量结果，因此 DPS/PMU 测量设置与结果读取通过它衔接。
- **文档事实** `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.193_RESULT_POINT.htm`、`.../02.07.04.01.194_RESULT_POINT_LIST.htm`、`.../02.07.04.01.192_RESULT_FAIL_INFO.htm`：三个 helper 类；其中 RESULT_FAIL_INFO 保存每个 pin 在指定 result point 的状态字节，并提供访问各 fail 位的 getter。
- **文档事实** `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.08_BADC_MEASURE.htm`：BADC_MEASURE 的测量结果通过 DC_RESULT_ACCESSOR 获取。
- **文档事实** `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.142_PATTERN_CONTROLLER.htm`：PATTERN_CONTROLLER 只能取全局 pass/fail，逐 pin 的 Board ADC 测量结果必须用 DC_RESULT_ACCESSOR 上传。
- **文档事实** `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.26_DC_PROFILING_OFF.htm`：该页说明 profiling 得到的测量值由 DC_RESULT_ACCESSOR 取得，因此它也是 DC profiling 结果的读取入口。
- **文档事实** `02_System_reference/02.05_Test_Head_Cards/02.05.04.01.03.04_PS1600_DC_value_measurements.htm`、`02_System_reference/02.05_Test_Head_Cards/02.05.04.02.07.02_Pin_Scale_5000_DC_value_measurements.htm`：两页均用 DC_RESULT_ACCESSOR 读取 DC 测量结果。
- **文档事实** `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.06_XPS256_programming_-_DGT.htm`、`.../02.05.05.03.10.13_XPS256_programming_-_Measure_currents.htm`、`.../02.05.05.03.10.14_XPS256_programming_-_Measure_voltages.htm`、`.../02.05.05.03.10.19_XPS256_programming_-_Voltage_drop_measurement.htm`：XPS256 的采样数据/电流/电压/电压降结果通过 DC_RESULT_ACCESSOR 上传，或与 `SPMU_TASK.getValue()`/`DPS_TASK.getValue()` 配合读取。
- **文档事实** `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.241_TEST.htm`、`.../02.07.04.01.244.06_TESTSET__.judgeAndLog_DcResultAccessor.htm`：`TEST` 与 `TESTSET.judgeAndLog` 可直接以 DC_RESULT_ACCESSOR 对象作为测试数据来源。
- **文档事实** `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.231.50_SMC_UPLOAD_DC_RESULTS.htm`：SMC_UPLOAD_DC_RESULTS 使用 DC_RESULT_ACCESSOR 上传指定测量结果，并可带 `TM::RESULT_RANGE`。
- **文档事实** 本页 Related information 还列出 `ERRE?`、`DFTD`、`VALR?` 三个命令页（`02_System_reference/02.06_Command_Reference/02.06.02.02.115_ERRE__-__Expected_and_Received_Results_of_Events.htm`、`.../02.06.02.02.68_DFTD__DFTD___DeFine_Test_Data.htm`、`.../02.06.02.02.317_VALR__-__VALid_Range.htm`）。

## 版本

**文档事实** 本页 `Functional changes` 记录：
- Introduced before SmarTest 6.3.2
- SmarTest 7.3.1: New function getExpectedResult().
- SmarTest 7.3.1: New parameter site.
- SmarTest 7.3.1: DC Scale PVI8 card added.
- SmarTest 7.4.0: DC Scale AVI64 card added.
- SmarTest 7.10.1: DC Scale XPS256 card added.

**文档事实** 正文称支持 UHC4T 的 DPS operating mode，但 `Functional changes` 未记录 UHC4T 支持是在哪个版本加入的。

## 出处

- `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.28_DC_RESULT_ACCESSOR.htm`（主源：简介、Class definition、Member functions、Examples、Related information、Functional changes）。
- 关联判断另参考 `extract/edges.jsonl` 中指向本页的入边；本页语法节逐字取自同页，无语法子主题。
