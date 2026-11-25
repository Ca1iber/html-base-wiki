---
type: object
title: LIMIT
layer: L2
stage: testmethod
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.126_LIMIT.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# LIMIT

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **5,985 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.126_LIMIT.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Class definition

This API is defined in the header file

/opt/hp93000/soc/prod_com/include/MAPI/Limit.h
.

Constructor
```
LIMIT();
```

The default constructor
LIMIT()
 creates an empty class object of the LIMIT
API.

```
LIMIT(TM::COMPARE opl, DOUBLE low, TM::COMPARE oph, DOUBLE high);
```

This
constructor creates the class object that contains the specified limit
values and comparison operators. For the parameter, see the description
of member functions
`low()`（raw: `29504.htm#_29504__dle_low`）
 and
`high()`（raw: `29504.htm#_29504__dle_high`）
.

Comparison operator
The API supports the enumerator
TM::COMPARE
 as follows:

LT
: Less than the limit value

LE
: Less than or equal to the limit value

GT
: Greater than the limit value

GE
: Greater than or equal to the limit value

NA
: No compare

Constant objects of the LIMIT() API
The following constant objects of the
LIMIT()
 API can
control the test result judgment in the
TEST()
 API
regardless of the actual measurement.

TM::Pass
: Always pass

TM::Fail
: Always fail

Member functions:

`low()`（raw: `29504.htm#_29504__dle_low`）

`high()`（raw: `29504.htm#_29504__dle_high`）

`unit()`（raw: `29504.htm#_29504__dle_unit`）

`get()`（raw: `29504.htm#_29504__dle_get`）

`getLow()`（raw: `29504.htm#_29504__dle_getLow`）

`getHigh()`（raw: `29504.htm#_29504__dle_getHigh`）

### Member functions

low()
```
DOUBLE low(TM::COMPARE op, DOUBLE value);
```

This
member function sets the comparison operator and lower limit value of
the class object.

[表] Parameters
行 1:
  op
  The comparison operator of type
    TM::COMPARE to be set. Applicable
    operators are
    
    GT: Greater than the limit
    value,
    
    GE: Greater than or equal to
    the limit value), and
    
    NA: No compare.
行 2:
  value
  The lower limit value to be set.
high()
```
DOUBLE high(TM::COMPARE op, DOUBLE value);
```

This
member function sets the comparison operator and upper limit value of
the class object.

[表] Parameters
行 1:
  op
  The comparison operator of type
    TM::COMPARE to be set. Applicable
    operators are
    
    LT: Less than the limit
    value,
    
    LE: Less than or equal to the
    limit value, and
    
    NA: No compare.
行 2:
  value
  The upper limit value to be set.
unit()

```
const STRING& unit(const STRING& unit);
```

This member function sets the unit for the class object. The unit is used
for data logging purposes and will not affect the Pass/Fail result of
the test.

[表] Parameters
行 1:
  unit
  The unit of the limit value. The format of this
    parameter can be:
    
    "limit_unit"
    
    "lower_unit;lower_power;upper_unit;upper_power".
    This
    format is used to scale the values in data
    logging:
    
    lower_unit is the unit
    specified for lower limit
    
    lower_power is power of 10
    matching with lower_unit
    
    upper_unit is the unit
    specified for upper limit
    
    upper_power is power of 10
    matching with upper_unit.
    
    The unit with smaller value of power will be
    used in the data logging. The value should be
    specified like "mV;-3;uV;-6".
    
    SmarTest will
    not check whether the specified
    lower_unit/upper_unit
    matches with the
    lower_power/upper_power.
    It just copies the string specified for
    lower_unit or
    upper_unit as the unit to data
    log.

Example:

If the unit is specified in the format "
limit_unit
", the
unit of values in data log is
limit_unit
.

If the unit is specified in the format
"
lower_unit;lower_power;upper_unit;upper_power
", the
values in data log will be scaled by the smaller one of

lower_power
 and
upper_power
: The unit of
values in data log is

lower_unit
 if
lower_power
 used or

upper_unit
 if
upper_power
 used.

Assuming the lower limit is 1, upper limit is 5 and the measured value is
3, the values printed in the data log will be as follows:

[表]
列: Unit specified | Lower limit | Upper limit | Measured value | Unit
行 1:
  No unit specified
  1
  5
  3
  
行 2:
  "V"
  1
  5
  3
  V
行 3:
  "mV;-3;V;0"
  1000
  5000
  3000
  mV
行 4:
  "uV;-4;V;0"
  10000
  50000
  30000
  uV
行 5:
  "mV;-3;uV;-6"
  1000000
  5000000
  3000000
  uV
get()
```
void get(TM::COMPARE &opl, double &low, TM::COMPARE &oph, double &high) const;
```

This
member function retrieves the limit values and limit comparison
types.

[表] Parameters
行 1:
  opl
  The low limit comparison type. It can be
    TM::GT,
    TM::GE, or
    TM::NA.
行 2:
  low
  The low limit value.
行 3:
  oph
  The high limit comparison type. It can be
    TM::LT,
    TM::LE, or
    TM::NA.
行 4:
  high
  The high limit value.
getLow()
```
TM::COMPARE getLow(double *) const;
```

This member
function retrieves the low limit value and returns the comparison
type.

[表] Parameter
行 1:
  low
  The low limit value.
getHigh()
```
TM::COMPARE getHigh(double *) const;
```

This member
function retrieves the high limit value and returns the comparison
type.

[表]
行 1:
  high
  The high limit value.

### Examples

### Example 1

```
double low_limit, high_limit, thd_result;

TEST("Aout", "THD", LIMIT(TM::GT, low_limit, TM::LT, high_limit), thd_result);
```

The

TEST()
 API judges the test result

thd_result
 with the limit values specified by the

LIMIT()
 API. Within the
TEST()
 API
notation, you can use the
LIMIT()
 API to define the limit values
for the judgment.

### Example 2

```
double thd_result;

TEST("Aout", "THD", TM::Pass, thd_result);
```

The
TEST()
 API judges the test result
thd_result
 and always
returns a pass result because
TM::Pass
 is described as the
parameter.

### Example 3

```
double low_limit, high_limit, thd_result;
LIMIT lmt_obj;

lmt_obj.low(TM::GT, low_limit);
lmt_obj.high(TM::LT, high_limit);
lmt_obj.unit("dB");

TEST("Aout", "THD", lmt_obj, thd_result);
```

The
LIMIT()
 API's class object
lmt_obj
 is created. The
member functions
low()
 and
high()
 of the

LIMIT()
 API set the low and high limit values to that object.
The member function
unit()
 sets the unit of

low_limit
 and
high_limit
 to "dB". Then,

TEST()
 API uses these limit values to judge the test.

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
