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

**文档事实**：TIMING_SPEC 是 test method API，访问「某个 timing equation set 中某个 spec set」的数据容器；构造 `TIMING_SPEC(eqnset, specset)` 即绑定一个已存在的 equation set 号与 spec set 号（`02.07.04.01.249`）。

**文档事实**：它用于读取 equation/spec 号与单个 spec 值（`getEquation()`、`getSpec()`、`getSpecValue()`）、修改 spec 值（`change()`）、以及把所有 spec 值恢复为「当前 test suite 的 test method 程序启动时」的值（`restore()`）。SmarTest 中 timing 值默认单位是纳秒。

**文档事实**：改动不会立即到硬件。文档列出的生效时机是：`EXECUTE_TEST`、`START_TEST`、`DIGITAL_CAPTURE_TEST`、`NB_DIGITAL_CAPTURE_START`、`FUNCTIONAL_TEST`，以及 `FLUSH` 后执行 `SPEC_SEARCH.execute()`、`SEQUENCER_STATUS.run()`、`PMU_IFVM.execute()`、`PMU_VFIM.execute()`、`TASK_LIST.execute()`、`DPS_VFIM.execute()` 之一；执行 `FLUSH` 还能把改动反映到 MCD（Test Program Explorer、Spec Tool）。

**文档事实**：改 spec 值不会改写 level/timing 文件；要永久修改必须改对应的 setup 文件。**文档事实**（原文 CAUTION）：LEVEL_SPEC/TIMING_SPEC 为支持 `.restore()` 在 API 层缓存值，firmware 层没有这份缓存，因此除调试目的外不要把这些 API 与修改值的 firmware 命令混用。

**文档事实**（Important points）：每条语句只能写一个成员函数；要修改主 timing specification 或其中的 spec 值，必须显式定义 TIMING_SPEC 类对象再引用它。

## 典型用法

**文档事实**：把 equation set 1、spec set 2 设为主 timing：

```cpp
TIMING_SPEC spec1(1, 2);
Primary.timing(spec1);
```

**文档事实**：修改主 timing 的 spec 值有两种等价写法——经 `Primary.getTimingSpec()` 取对象，或直接引用已定义对象：

```cpp
Primary.getTimingSpec().change("Tp", 10);   // 10 ns
TIMING_SPEC& ts_obj = Primary.getTimingSpec();
ts_obj.change("Tp", 10);
```

`change()` 的第二个参数可带单位（如 `10 ns`）；文档示例说明带 `ns` 时按 10^-9 秒计。读取用 `getSpecValue("Tp")`，取编号用 `getEquation()` / `getSpec()`。

**文档事实**：multiport timing 用 `"spec@port"` 形式取值；multiport specification 由 `SPECIFICATION` API 选择：

```cpp
DOUBLE specValue = Primary.timing(SPECIFICATION("spec"))
                         .getSpecification().getSpecValue("specValue@port");
```

**文档事实**：若在 PRIMARY_STATUS 中切换主 spec set / equation set 之前未 `FLUSH`，先前对 TIMING_SPEC 对象所做、尚未 FLUSH 的 spec 值改动会被清除；文档示例中 `"T"`、`"T2"` 的改动因此被忽略。要保留改动，需在切换前执行 `FLUSH(TM::APRM)`。

**文档事实**：`change()` + `FLUSH` 改了值后，Test Program Explorer 不会显示 timing 已变；调试时若要重载当前 timing setup 文件，需先在 Spec Tool 窗口改一个 spec 值，让 Test Program Explorer 标记 timing 已改。

**建议**：调试期临时改值用 `TIMING_SPEC`；需要长期生效的改动写入 timing setup 文件，不要依赖运行期改值（与文档 CAUTION 一致）。

## 和谁有关

- [[primary-status]] — **文档事实**：`Primary.timing(TIMING_SPEC)` 用于设定主 timing；`Primary.getTimingSpec()` 返回当前主 specification 的 TIMING_SPEC 对象（`02.07.04.01.249` 首段与示例，`02.07.04.01.167`）。
- [[level-spec]] — **文档事实**：对等的 level spec 容器；CAUTION 同时点名两者，并说明两者的 API 层缓存与 `restore()` 机制相同（`02.07.04.01.249`）。
- [[flush]] — **文档事实**：`FLUSH` 决定改动何时生效、是否反映到 MCD；未 FLUSH 时切换主 set 会丢弃改动（`02.07.04.01.249` 首段、Important points）。
- [[svlr]] — **文档事实**：仅调试用途——可暂停 application model，用 firmware 命令 `SVLR` 直接改 spec 值，再恢复运行（`02.07.04.01.249` Note，链到 `02.06.02.02.252`）。
- `SPECIFICATION`（`02.07.04.01.232`）— **文档事实**：multiport timing 的 `"spec@port"` 取值由它选择 specification（Example 4）。
- [[spec-search]] — **文档事实**：`FLUSH` 后 `SPEC_SEARCH.execute()` 是文档列出的改动生效时机之一（`02.07.04.01.249` 首段）。
- [[spec-tool]]、[[timing-setup-tool]]、[[timing-file]] — **文档事实**：MCD 侧可见性涉及 Test Program Explorer 与 Spec Tool；永久改动须落在 timing（setup）文件本身（`02.07.04.01.249` 首段与 CAUTION）。

## 版本

**文档事实** 文档未覆盖（源文档无 `Functional changes` 节）。

## 出处

- `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.249_TIMING_SPEC.htm`（主文档；本页语义、内链关系与 Related information 均出自该篇）。
