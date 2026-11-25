---
type: object
title: SPEC_SEARCH
layer: L2
stage: level
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.233_SPEC_SEARCH.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# SPEC_SEARCH

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **8,046 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.233_SPEC_SEARCH.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Class definition

Constructor:

```
SPEC_SEARCH(const STRING& specName, TM::SPEC_TYPE specType);
```

Member
Functions:

```
SPEC_SEARCH& specPins(const STRING& pins);
SPEC_SEARCH& method(TM::SPEC_METHOD method);
SPEC_SEARCH& start(DOUBLE min);
SPEC_SEARCH& stop(DOUBLE max);
SPEC_SEARCH& stepWidth(DOUBLE step);
SPEC_SEARCH& numberOfSteps(INT step);
SPEC_SEARCH& resolution(DOUBLE resolution);
SPEC_SEARCH& resultPins(const STRING& r_pins);
SPEC_SEARCH& limits(STRING testname);
SPEC_SEARCH& limits(LIMIT limit);
SPEC_SEARCH& unit(const STRING& unit_v);
void execute();
TM::SPEC_RESULT getResultSpec();
DOUBLE getPassVal();
DOUBLE getFailVal();
```

### Syntax

For creating a class
object:

```
SPEC_SEARCH object("specName", specType);
```

For setting up a
spec search test:

```
object.func1.func2 . . .funcN
```

For executing a spec
search test:

```
object.execute();
```

For retrieving a result of the spec
search test:

```
variable = object.getXXX();
```
[表]
行 1:
  object
  Class object name to be defined
行 2:
  specName
  Target spec name
行 3:
  specType
  Specifies whether timing or level spec
行 4:
  func1 to funcN
  Member functions of the SPEC_SEARCH API
行 5:
  variable
  Variable to hold a result
行 6:
  getXXX()
  Member functions of the SPEC_SEARCH API for retrieving a
    result

### Member functions

### specPins()
```
SPEC_SEARCH& specPins(const STRING& pins);
```

Specify
a pin or a list of pins/pin groups. You can specify multiple pins by separating with a comma.
The spec is shifted for these pins.

[表] Parameter
行 1:
  pins
  Name of a pin, pins or pin group

### method()
```
SPEC_SEARCH& method(TM::SPEC_METHOD method);
```

This
member function specifies a search method. The definition of SPEC_METHOD
is:

```
enum SPEC_METHOD{Linear, Binary, LinBin};
```
[表] Parameter
行 1:
  method
  Search method. The following specifiers can be set:
    
    TM::Linear A linear search from the start value to the
    stop value, with a test interval of resolution.
    
    TM::Binary A binary search from start to stop. The
    minimum interval is set with the resolution.
    
    TM::LinBin A linear search from start to stop with
    an interval resolution, followed by a binary search between the last passed and
    first failed linear measured values, using the maximum resolution of the test system
    hardware.

### start()
```
SPEC_SEARCH& start(DOUBLE min);
```

This
member function defines a start values of the spec search.

If start and stop value are not
specified, the "minimum" and "maximum" values defined in the spec window of the timing or level
spec will be used as start and stop values for the spec search.

[表] Parameter
行 1:
  min
  Start value of the spec search

### stop()
```
SPEC_SEARCH& stop(DOUBLE max);
```

This
member function defines a stop value of the spec search.

[表] Parameter
行 1:
  max
  Stop value of the spec search

### stepWidth()
```
SPEC_SEARCH& stepWidth(DOUBLE width);
```

This
member function defines the step width of the spec search in the unit specified with the
corresponding spec. This is optional if the mode is
Binary
. This value
will be overridden when the
numberOfSteps
 member function is used after
this member function.

[表] Parameter
行 1:
  width
  Step width of the spec search

### numberOfSteps()
```
SPEC_SEARCH& numberOfSteps(INT num);
```

This
member function defines the number of steps of the spec search. This is optional if the mode is
Binary. This value will be overridden when the stepWidth member function is used after this
member function.

[表] Parameter
行 1:
  num
  Number of steps of the spec search

### resolution()
```
SPEC_SEARCH& resolution(DOUBLE resolution);
```

This
member function defines the smallest step size to be used in the binary search. This parameter
is required for all the spec search method,
Linear
,

Binary
 and
LinBin
. The unit must be the same as
the one defined with the spec.

Note that this setting rounds off the value specified with
the start, stop, stepWidth and numberOfSteps member function. For example, if resolution is set
to 0.01 and start value is set to 1.555, start value will be rounded off and assumed to be
1.56.

[表] Parameter
行 1:
  resolution
  For binary search, this parameter is the smallest step size.
    
    For linear search, this parameter is the resolution of the step width.

### resultPins()
```
SPEC_SEARCH& resultPins(const STRING& r_pins);
```

This
member function defines a name of a pin, pins or pin group that contribute to the pass/fail
result You can specify multiple pins by separating with a comma. This parameter is optional and
overrides the settings of the
specPins
 member functions.

[表] Parameter
行 1:
  r_pins
  A name of a pin, pins or pin group that contribute to the pass/fail result.

### limits()
```
SPEC_SEARCH& limits(STRING testname);
SPEC_SEARCH& limits(LIMIT limit);
```

This
member function sets the start and stop values using a test name or
LIMIT

API's class object. This parameter is optional and overrides the settings of the

start
 and
stop
 member functions.

[表] Parameter
行 1:
  testname
  Test name that can be referred from the Properties view.
行 2:
  limit
  Class object name of the LIMIT API.

### unit()
```
SPEC_SEARCH& unit(const STRING& unit_v);
```

This
member function specifies the unit to be used for displaying results in data logging. This
parameter is optional.

[表] Parameter
行 1:
  unit_v
  Unit string to be added to the data log

### execute()
```
void execute();
```

This member function
executes a spec search test.

There are no parameters in this member
function.

### getResultSpec()
```
TM::SPEC_RESULT getResultSpec();
```

This
member function returns the result of the spec search test with the following

TM::SPEC_RESULT
 type specifiers:

[表]
行 1:
  TransitionPassFail
  A pass to fail transition is found.
行 2:
  TransitionFailPass
  A fail to pass transition is found.
行 3:
  AllPass
  All the functional tests are passed.
行 4:
  AllFail
  All the functional tests are failed.

From the returned specifier, you can determine which member function is applicable to
retrieve the transition value of the spec search test. See Example.

There are no
parameters in this member function.

### getPassVal()
```
DOUBLE getPassVal();
```

This member
function returns a maximum pass value when a pass to fail transition is found or a minimum pass
value when a fail to pass transition is found in the spec search.

If a pass/fail
transition does not occur in the spec search (
AllPass
 or

AllFail
), the
getPassVal
 member function does not
return a valid value.

There are no parameters associated with this member
function.

### getFailVal()
```
DOUBLE getFailVal();
```

This member
function returns a minimum fail value when a pass to fail transition is found or a maximum fail
value when a fail to pass transition is found in the spec search.

If a pass/fail
transition does not occur in the spec search (
AllPass
 or

AllFail
), the
getFailVal
 member function does not
return a valid value.

There are no parameters associated with this member
function.

### Example

```
SPEC_SEARCH search_1("freq",TM::TIM);
search_1.specPins("CPandMR").method(TM::Linear).
unit("Hz").start(50).stop(70).numberOfSteps(20).
resolution(0.01);

search_1.execute();
DOUBLE Pval, Fval;
switch(search_1.getResultSpec()){
case TM::TransitionPassFail :
case TM::TransitionFailPass :
Pval = search_1.getPassVal();
Fval = search_1.getFailVal();
break;
case TM::AllPass :
case TM::AllFail :
cout << "No transition found within the search interval" << endl;
break;
}
```

This
example defines the "search_1" object and defines conditions of the spec search as shown
below:

[表]
列: Parameter | Value
行 1:
  Spec type
  Timing spec (TM::TIM)
行 2:
  Target pin
  CPandMR
行 3:
  Search method
  Linear search (Linear)
行 4:
  Search range
  50 Hz to 70 Hz
行 5:
  Number of steps
  20
行 6:
  Resolution for the getPassVal or getFailVal member function
  0.01

Then executes a spec search test and checks the transition type. Then retrieves a
pass/fail transition value or displays an error message.

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
