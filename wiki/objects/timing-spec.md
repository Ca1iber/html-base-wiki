---
type: object
title: TIMING_SPEC
layer: L2
stage: timing
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.249_TIMING_SPEC.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# TIMING_SPEC

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **5,445 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.249_TIMING_SPEC.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Class definition

This API is defined in the header file

/opt/hp93000/soc/prod_com/include/MAPI/TimingSpec.h
.

Constructor

```
TIMING_SPEC(INT eqnset, INT specset)
```

This constructor creates the
TIMING_SPEC
 API's class
object that represents the contents of an existing timing spec set in an
equation set.

[表] Parameters
行 1:
  eqnset
  Equation set number
行 2:
  specset
  Spec set number
Member functions

`getEquation()`（raw: `29809.htm#_29809__dle_getEquation`）

`getSpec()`（raw: `29809.htm#_29809__dle_getSpec`）

`getSpecValue()`（raw: `29809.htm#_29809__dle_getSpecValue`）

`change()`（raw: `29809.htm#_29809__dle_change`）

`restore()`（raw: `29809.htm#_29809__dle_restore`）

### Member functions

getEquation()
```
INT getEquation();
```

This member function returns the
equation set number.

There are no parameters in this member
function.

getSpec()
```
INT getSpec();
```

This member function returns the
spec set number.

There are no parameters in this member
function.

getSpecValue()
```
DOUBLE getSpecValue(const STRING& spec);
```

This
member function returns the value of the specified timing
spec.

[表] Parameter
行 1:
  spec
  Name of the spec whose value will be queried.
    
    For multiport timing, the parameter is to be defined
    as "spec@port" with
    
    spec = Spec whose value
    will be queried
    
    port = Selected port
change()
```
void change(const STRING& spec, DOUBLE value);
```

This
member function changes the value of the specified spec.

[表] Parameters
行 1:
  spec
  Name of the spec whose value will be changed.
行 2:
  value
  Value applied to spec.
    
    The value must be within the range between the
    minimum and maximum values specified in the spec
    set.

Note
 In SmarTest, all timing values are in

nanoseconds
 by default.

CAUTION
 Never mix the
LEVEL_SPEC
 or

TIMING_SPEC
 API and firmware commands modifying values for other
reasons than debugging purposes (see note below)!
LEVEL_SPEC
 and

TIMING_SPEC
 test method APIs cache values in order to enable the
.restore() functionality. This caching is not available on the firmware level. In both
cases, changing spec values takes effect without changing the level or timing file! If
you want to change spec values permanently you must do so in the corresponding setup
file itself.

Note
 For debug purpose only: If you want to change the spec value while the
application model is running without having to abort the execution, you can pause the application
model, change the spec value with the firmware command
`SVLR`（raw: `98764.htm`）
 directly
from hpt and then resume the running of the application model.

restore()
```
void restore();
```

This member function resets the
values of all specs to the ones when the test method program in the
current test suite is started.

There are no parameters in this
member function.

### Examples

### Example 1: Change primary timing set
```
TIMING_SPEC spec1(1, 2);
Primary.timing(spec1);
Primary.timing(1);
```

spec1

is an object of the
TIMING_SPEC
 class. The

timing()
 member function of the

PRIMARY_STATUS
 API sets timing equation set "1" and spec set
"2" as the primary timing specification. The timing equation and spec set numbers
must be specified using the corresponding object name

spec1
.

The second
timing()
 member
function defines the timing set "1" as the primary.

### Example 2: Change a primary timing spec value
```
TIMING_SPEC spec1(1, 2);
Primary.getTimingSpec().change("Tp", 10);
```

The

change()
 member function changes the value of spec variable
"Tp" to 10 nanoseconds. The
Primary.getTimingSpec()
 statement
returns the
TIMING_SPEC
 API's class object, namely

spec1
, that defines the current primary timing
specification.

```
TIMING_SPEC& ts_obj= Primary.getTimingSpec();
ts_obj.change("Tp", 10);
```

The

change()
 member function changes the spec variable "Tp" to10
nanoseconds. By the ampersand (&) in the first statement,

ts_obj
 is created as a reference to the class object returned
by
Primary.getTimingSpec()
 without copying the contents
object.

```
TIMING_SPEC spec1(1, 2);
Primary.getTimingSpec().change("Tp", 10 ns);
```

In
this example, with "ns" in the second parameter of the
change()

member function, the spec variable "Tp" is changed into 10
-9
 seconds.
This is more convenient when you want your timing in
nanoseconds
 be
represented in
seconds
 basis.

### Example 3: Retrieve a primary timing spec value
```
DOUBLE specValue = Primary.getTimingSpec().getSpecValue("Tp");
```

The

getSpecValue()
 member function returns the value of the "Tp"
spec variable in the currently defined primary specification. The

Primary.getTimingSpec()
 statement returns the

TIMING_SPEC
 API's class object that represents the spec set
and equation set that are currently defined as the primary.

### Example 4: Retrieve a primary timing spec value for a multiport specification
```
DOUBLE specValue = Primary.timing(SPECIFICATION("spec")).getSpecification().getSpecValue("specValue@port");
```

The

`getSpecValue()`（raw: `29809.htm#_29809__dle_getSpecValue`）
 member function returns a spec value for
a single port of a multiport timing specification. The spec value and the port are
defined by
"specValue@port"
. The multiport timing specification is
selected by the
`SPECIFICATION`（raw: `29771.htm`）
 API.

### Example 5: Retrieve the timing equation set
```
INT tmg_eq;
:
tmg_eq = Primary.getTimingSpec().getEquation();
```

The

getEquation()
 member function returns the timing equation set
number currently defined as the primary.

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
