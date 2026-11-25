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

**文档事实** LEVEL_SPEC 是 test method API，用于访问已存在的 level equation set 与 spec set 的内容。

**文档事实** 它提供六项功能：取 level equation set 号、取 level spec set 号、取某个 spec 的值、修改某个 spec 的值、针对特定 pin 修改 spec 值、复位 spec 值。

**文档事实** 该 API 定义于头文件 `/opt/hp93000/soc/prod_com/include/MAPI/LevelSpec.h`。

**文档事实** 构造 `LEVEL_SPEC(INT eqnset, INT specset)` 创建表示 equation set 中某个现有 level spec set 内容的对象；eqnset 为 equation set 号，specset 为 spec set 号。

**文档事实** 成员函数：getEquation() 返回 equation set 号；getSpec() 返回 spec set 号；getSpecValue(const STRING& spec) 查询 spec 值；change(spec, value) 修改 spec 值，change(spec, value, pin) 修改特定 pin 或 pin list 的值，value 必须落在 spec set 规定的范围内；restore() 把所有 spec 值复位为当前 test suite 的 test method 程序启动时生效的值。

**文档事实** 每条语句只能指定一个成员函数；`Primary.getLevelSpec().func()` 作用于当前 primary level spec，其中 getLevelSpec() 是 PRIMARY_STATUS 的成员函数。

**文档事实** CAUTION：不要把 LEVEL_SPEC 或 TIMING_SPEC API 与出于调试以外原因修改值的 firmware 命令混用；这两个 API 会缓存值以支持 restore()，固件层没有该缓存；改 spec 值不会修改 level 或 timing 文件，永久修改必须在对应 setup 文件中进行。

**文档事实** 调试用途的 Note：可在 application model 运行时暂停，用 firmware 命令 SVLR 从 hpt 直接改 spec 值，然后恢复运行。

**文档事实** 另一条 Note：针对 pin 的值只保留一个 flush cycle，且不能用 getSpecValue(spec) 取回 pin 特定值。

**推断** 因此它适合 test method 运行期临时修改 level spec；需要持久生效的修改应落到 setup 文件。

## 典型用法

**文档事实** Example 1：`LEVEL_SPEC spec1(1, 2); Primary.level(spec1);` 把 level equation set 1、spec set 2 设为 primary level specification。

**文档事实** Example 2：`Primary.getLevelSpec().change("v_low", -2.1 V);`，或先取引用 `LEVEL_SPEC& ls_obj = Primary.getLevelSpec();` 再 `ls_obj.change("v_low", -2.1 V);`，把 v_low 改为 -2.1 V。

**文档事实** Example 3：`Primary.getLevelSpec().change("vdde", 4.4, "VCC"); FLUSH(TM::APRM);` 只改 VCC pin 的 vdde；省略 pin 的 `change("vdde", 4.5)` 改所有 pin（含 VCC），随后 FLUSH。

**文档事实** Example 4：在 ON_FIRST_INVOCATION_BEGIN() 中创建 `LEVEL_SPEC newSpec(2,2)`，在 FOR_EACH_SITE_BEGIN/END 内按 CURRENT_SITE_NUMBER() 为每个 site 赋不同值，再用 FLUSH() 写入 tester。

**文档事实** Example 5：`double vLow = Primary.getLevelSpec().getSpecValue("v_low");`；已知 equation set 与 spec set 号时可用 `LEVEL_SPEC(1, 2).getSpecValue("v_low")`。

**建议** 运行期改动前先记录原值，或依赖 restore() 复位到当前 test suite 的 test method 程序启动时的值。

## 和谁有关

- **文档事实** PRIMARY_STATUS - (Primary)，getLevelSpec() 是其成员函数并返回 LEVEL_SPEC 对象；Primary.level(LEVEL_SPEC) 用于设定 primary level spec，Example 1 直接使用。
- **文档事实** TIMING_SPEC，CAUTION 与 Related information 把二者并列为姊妹 API，均缓存值以支持 restore()。
- **文档事实** Changing spec value in primary level spec set，该页说明 `<memberFunction>` 是 LEVEL_SPEC API 的成员函数，只能指定一个，且不能在该语句中指定 PRIMARY_STATUS 的其他成员函数。
- **文档事实** Changing and obtaining digital settings，该页说明 level(LEVEL_SPEC(...)) 版本用于访问 LEVEL_SPEC 成员函数，getLevelSpec() 返回带 primary level spec/equation sets 的 LEVEL_SPEC 对象。
- **文档事实** SVLR firmware command，本页 Note 说明调试时可在暂停 application model 后用 SVLR 从 hpt 修改 spec 值。
- **文档事实** LEV_TRANSFER_TASK 与 LEV_TRANSFER_PIN_TASK，这两个页面在入边中引用 LEVEL_SPEC。
- **文档事实** APIs in alphabetical order，该页把 LEVEL_SPEC 列入 API 清单。
- **文档事实** DC Test Programming，该页在说明 DPS_TASK 时提到 primary level spec/equation sets，与本页的 level spec 概念相关。

## 版本

**文档事实** Functional changes 记载 Introduced before SmarTest 6.3.2。

**文档事实** SmarTest 7.1.1：新增针对特定 pin / pin list 的 change 函数。

## 出处

- `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.124_LEVEL_SPEC.htm`，主源，含首段、Class definition、Member functions、Examples、Related information 与 Functional changes。
- `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.167_PRIMARY_STATUS_-__Primary.htm`，getLevelSpec() 与 Primary.level(LEVEL_SPEC) 的旁证。
- `02_System_reference/02.07_Test_Method_Reference/02.07.03.03.02.02_Changing_spec_value_in_primary_level_spec_set.htm` 与 `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.249_TIMING_SPEC.htm`，入边旁证。
- `extract/edges.jsonl` 入边，用于 LEV_TRANSFER_TASK、SVLR、DC Test Programming 等旁证。
