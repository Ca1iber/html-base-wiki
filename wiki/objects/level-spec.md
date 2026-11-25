---
type: object
title: LEVEL_SPEC
layer: L2
stage: level
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.124_LEVEL_SPEC.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# LEVEL_SPEC

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **5,234 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.124_LEVEL_SPEC.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Class definition

This API is defined in the header file

/opt/hp93000/soc/prod_com/include/MAPI/LevelSpec.h
.

Constructor
```
LEVEL_SPEC(INT eqnset, INT specset);
```

This constructor creates the
LEVEL_SPEC
 API's class
object that represents the contents of an existing level spec set in an
equation set.

[表] Parameters
行 1:
  eqnset
  Equation set number.
行 2:
  specset
  Spec set number.
Member functions

`getEquation()`（raw: `29495.htm#_29495__dle_getEquation`）

`getSpec()`（raw: `29495.htm#_29495__dle_getSpec`）

`getSpecValue()`（raw: `29495.htm#_29495__dle_getSpecValue`）

`change()`（raw: `29495.htm#_29495__dle_change`）

`restore()`（raw: `29495.htm#_29495__dle_restore`）

Usage of the API

```
LEVEL_SPEC obj(eqnset, specset);
obj.memberFunction();
```

First you define a
LEVEL_SPEC
 object for the specified
equation set and spec set. Then you can work with the object using the
member functions of
LEVEL_SPEC
.

In the above example,
obj
 is an object of

LEVEL_SPEC
,
eqnset
 is a level
equation set number,
specset
 is a spec set number and

memberFunction
 is one of the member functions of

LEVEL_SPEC
 (see member functions below).

Only one member function can be specified in per statement.

```
Primary.getLevelSpec().func();
```

With this syntax, you work with the current primary level spec.
`getLevelSpec()`（raw: `29640.htm#_29640__dle_getLevelSpec`）
 is a member function of
`PRIMARY_STATUS - (Primary)`（raw: `29640.htm`）
 and
func()
 is one of the member
functions of
LEVEL_SPEC
.

### Member functions

getEquation()

```
INT getEquation();
```

This member function returns the equation set number.

getSpec()

```
INT getSpec();
```

This member function returns the spec set number.

getSpecValue()

```
DOUBLE getSpecValue(const STRING& spec);
```

This member function queries the value of the specified level spec.

[表] Parameter
行 1:
  spec
  Name of the spec whose value will be queried.
change()

```
void change(const STRING& spec, DOUBLE value);
void change(const STRING& spec, DOUBLE value, const STRING& pin);
```

This member function changes the value of the specified spec.

The second version of the function changes the value of the specific spec
for the specific pin.

[表] Parameters
行 1:
  spec
  Name of the spec whose value will be changed.
行 2:
  value
  Value applied to spec.
    
    The value must be within the range that is specified
    in the spec set.
行 3:
  pin
  The pin or pin list the value will be applied
    to.

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

Note
 The value for the specified pin is only stored for one
flush cycle. You cannot retrieve the pin specific values using

getSpecValue(
spec
)
.

restore()

```
void restore();
```

This member function resets the values of all specs to the ones that were
in effect when the test method program in the current test suite is
started.

### Examples

### Example 1: Changing the primary level specification

The level equation set 1 and spec set 2 are set as primary level specification.

```
LEVEL_SPEC spec1(1, 2);
Primary.level(spec1);
```

### Example 2: Changing a spec value in the primary spec set

The value of the spec
v_low
 is changed to -2.1 V.

```
Primary.getLevelSpec().change("v_low", -2.1 V);
```

or

```
LEVEL_SPEC& ls_obj = Primary.getLevelSpec();
ls_obj.change("v_low", -2.1 V);
```

### Example 3: Changing a spec value in the primary spec set for a specific pin or all pins

For pin
VCC
 the value of
vdde
 is changed to 4.4
V:

```
Primary.getLevelSpec().change("vdde", 4.4, "VCC");
FLUSH(TM::APRM);
```

For all pins the value of
vdde
 is changed to 4.5 V. This includes
the
VCC
 pin:

```
Primary.getLevelSpec().change("vdde", 4.5);
FLUSH(TM::APRM);
```

### Example 4: Changing a spec value and assigning a different value for each site

This example shows how you can change a spec value for the variable

VCC
. Different value is assigned for each site:

```
ON_FIRST_INVOCATION_BEGIN();

LEVEL_SPEC newSpec(2,2); // Creating a LEVEL_SPEC object to change level set 2 and spec set 2

FOR_EACH_SITE_BEGIN();

newSpec.change("VCC", 0.1 * CURRENT_SITE_NUMBER() ); //Assigning new value to VCC

FOR_EACH_SITE_END();

FLUSH(); // Writing the changes to the tester

ON_FIRST_INVOCATION_END();
```

### Example 5: Querying a spec value in the primary spec set

The value of the spec
v_low
 is returned:

```
double vLow = Primary.getLevelSpec().getSpecValue("v_low");
```

or (if you know the level equation set number and spec set number),

```
double vLow = LEVEL_SPEC(1, 2).getSpecValue("v_low");
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
