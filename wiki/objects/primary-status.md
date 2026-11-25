---
type: object
title: PRIMARY_STATUS - (Primary)
layer: L3
stage: level
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.167_PRIMARY_STATUS_-__Primary.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# PRIMARY_STATUS - (Primary)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **13,866 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.167_PRIMARY_STATUS_-__Primary.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Class definition

This API is defined in the header file

/opt/hp93000/soc/prod_com/include/MAPI/PrimaryStat.h
.

Constructor

There is no constructor available for this class.

To use the
PRIMARY_STATUS
 API, you must always use the
system-prepared class object
Primary
 which represents
the current definitions of the digital primaries or represents the
digital primaries to be defined. You cannot create any object of this
API.

Member functions

`assignLabelToCurrentSite()`（raw: `29640.htm#_29640__dle_assignLabelToCurrentSite`）

`assignPinToCurrentSite()`（raw: `29640.htm#_29640__dle_assignPinToCurrentSite`）

`dps()`（raw: `29640.htm#_29640__dle_dps`）

`getAssignedLabelForCurrentSite()`（raw: `29640.htm#_29640__dle_getAssignedLabelForCurrentSite`）

`getAssignedPinForCurrentSite()`（raw: `29640.htm#_29640__dle_getAssignedPinForCurrentSite`）

`getDps()`（raw: `29640.htm#_29640__dle_getDps`）

`getLabel()`（raw: `29640.htm#_29640__dle_getLabel`）

`getLevel()`（raw: `29640.htm#_29640__dle_getLevel`）

`getLevelSpec()`（raw: `29640.htm#_29640__dle_getLevelSpec`）

`getModeContextName()`（raw: `29640.htm#_29640__dle_getModeContextName`）

`getTiming()`（raw: `29640.htm#_29640__dle_getTiming`）

`getTimingSpec()`（raw: `29640.htm#_29640__dle_getTimingSpec`）

`getWaveform()`（raw: `29640.htm#_29640__dle_getWaveform`）

`label()`（raw: `29640.htm#_29640__dle_label`）

`level()`（raw: `29640.htm#_29640__dle_level`）

`timing()`（raw: `29640.htm#_29640__dle_timing`）

`waveform()`（raw: `29640.htm#_29640__dle_waveform`）

For multi-port testing, the following member functions are also
available:

`timing(INT tset, const STRING& port)`（raw: `29640.htm#_29640__dle_timing`）

`timing(const SPECIFICATION& specif)`（raw: `29640.htm#_29640__dle_timing`）

`getSpecification()`（raw: `29640.htm#_29640__dle_getSpecification`）

`getTiming(const STRING& port)`（raw: `29640.htm#_29640__dle_getTiming`）

`isTimingPortBased()`（raw: `29640.htm#_29640__dle_isTimingPortBased`）

`isLabelPortBased()`（raw: `29640.htm#_29640__dle_isLabelPortBased`）

Syntax for common tasks

For changing definitions of digital
primaries:

```
Primary.memberFunction();
```
[表]
行 1:
  memberFunction
  Member functions of the
    PRIMARY_STATUS API.

For retrieving current definition of primary timing/waveform
set number, primary level/DPS set number, or start
label:

```
return_value = Primary.memberFunction;
```
[表]
行 1:
  memberFunction
  A member function of the
    PRIMARY_STATUS API. For
    retrieving data, only one member function is
    available.

For retrieving current definition of primary equation/spec set
number (or specification name of multi-port
testing):

```
return_value = Primary.member_f.s_member_f;
```
[表]
行 1:
  member_f
  A member function (getTimingSpec or getLevelSpec) of the
    PRIMARY_STATUS API. This member
    function calls a subsidiary data container (class
    object of the `TIMING_SPEC`（raw: `29809.htm`） or `LEVEL_SPEC`（raw: `29495.htm`） API). Only one member function is
    available.
    
    For multi-port testing, the
    getSpecification member
    function is available to call the subsidiary data
    container, `SPECIFICATION`（raw: `29771.htm`） API.
行 2:
  s_member_f
  A member function of the subsidiary data
    container. Only one member function is
    available.

For changing a spec value in the spec set (or specification of
multi-port testing) that is currently defined as the
primary:

```
Primary.member_f.s_member_f;
```
[表]
行 1:
  
  For member_f and
    s_member_f, see the `table`（raw: `29640.htm#_29640__t_table_syntax_example_3`） above.

### Member functions

timing()
```
PRIMARY_STATUS& timing(INT tset);
PRIMARY_STATUS& timing(const TIMING_SPEC& specset);
PRIMARY_STATUS& timing(INT tset, const STRING& port);
PRIMARY_STATUS& timing(const SPECIFICATION& specif);
```

The

timing
 member function specifies the
timing-related primaries (except the waveform set). Which primary you
specify is determined by the data type of the specified
parameter.

[表] Parameters
行 1:
  
  tset
  Integer timing set number to be defined as the
    primary. If you specify 0, the current definition is
    unchanged. Even if the setup is equation-based, use
    this parameter to define the primary timing set
    number.
行 2:
  
  specset
  Name of a previously defined `TIMING_SPEC`（raw: `29809.htm`）
    object or
    
    TIMING_SPEC(equation_set_no,
    specset_no).
行 3:
  For multi-port testing, [跨 3 列]
    the following parameters are also available:
行 4:
  
  port
  Port name as string for which tset
    will be defined as the primary. If you omit this
    parameter, tset will be defined
    for all ports. To use this parameter, a
    specification of the timing setup must be currently
    defined as the primary or must be specified as the
    primary by the execution of the
    timing(specif) member
    function.
行 5:
  
  specif
  Name of a previously defined `SPECIFICATION`（raw: `29771.htm`）
    object or
    
    SPECIFICATION("specification_name").
waveform()
```
PRIMARY_STATUS& waveform(INT wfset);
```

This
member function specifies the waveform set to be defined as the
primary.

[表] Parameter
行 1:
  wfset
  Waveform set number to be defined as the primary.
    If you specify 0, the current definition is
    unchanged.
level()
```
PRIMARY_STATUS& level(INT lset);
PRIMARY_STATUS& level(const LEVEL_SPEC& specset);
```

This
member function specifies the level-related primaries (except DPS set).
Which primary you specify is determined by the data type of the
specified parameter.

[表] Parameter
行 1:
  lset
  Integer level set number to be defined as the
    primary. If you specify 0, the current definition is
    unchanged. Even if the setup is the equation-based,
    use this parameter to define the primary level set
    number.
行 2:
  specset
  `LEVEL_SPEC`（raw: `29495.htm`） level equation and spec set
    numbers to be defined as the primaries.
dps()
```
PRIMARY_STATUS& dps(INT dpsset);
```

This member
function specifies the DPS set to be defined as the primary.

[表] Parameter
行 1:
  dpsset
  DPS set number to be defined as the primary. If
    you specify 0, the current definition is
    unchanged.
label()

```
PRIMARY_STATUS& label(const STRING& label);
```

This member function specifies the (digital) sequencer start label name
to be activated.

[表] Parameter
行 1:
  label
  Start label name to be activated.
    
    For multi-port testing, you can specify a multi-port
    burst label name as the start label.
getTiming()
```
INT getTiming();
INT getTiming(STRING& port);
```

This
member function returns the currently defined primary timing set number.
(Note that the
CTIM
 sequencer instruction changes the
timing set, but does not change the definition of the
primary).

For multi-port testing, this member function returns the
currently defined primary timing set number of the specified
port:

[表] Parameter
行 1:
  port
  (For multi-port testing only.) Port name whose
    primary timing set number will be retrieved. To
    specify this parameter, a specification of the
    timing setup must be currently defined as the
    primary. If the currently defined primary timing set
    number is the same in all ports, you may omit this
    parameter even for multi-port testing.
getTimingSpec()
```
TIMING_SPEC& getTimingSpec();
```

This member
function returns the
TIMING_SPEC
 API's class object
that represents the currently defined primary timing equation and spec
set numbers and the spec values. For more information, see
`TIMING_SPEC`（raw: `29809.htm`）
. To use this member function, a timing spec set of
the timing setup must be currently defined as the primary.

There
are no parameters in this member function.

getWaveform()
```
INT getWaveform();
```

This member function returns the
currently defined primary waveform set number. To use this member
function, a waveform set of the timing setup must be currently defined
as the primary.

There are no parameters in this member
function.

getSpecification()
```
SPECIFICATION& getSpecification();
```

For
multi-port testing only. This member function returns the

SPECIFICATION
 API's class object that represents
the currently defined primary specification name (of the timing setup)
and the spec values (including per-port spec values). For more
information, see
`SPECIFICATION`（raw: `29771.htm`）
. To use this member function, a
specification of the timing setup must be currently defined as the
primary.

There are no parameters in this member function.

getLevel()
```
INT getLevel();
```

This member function returns the
currently defined primary level set number. (note that the

CLEV
 sequencer instruction changes the level set,
but does not change the definition of the primary).

There are no
parameters in this member function.

getLevelSpec()
```
LEVEL_SPEC& getLevelSpec();
```

This member
function returns the
LEVEL_SPEC
 API's class object
that represents the currently defined primary level equation and spec
set numbers and the spec values. For more information, see
`LEVEL_SPEC`（raw: `29495.htm`）
. To use this member function, a level spec set of
the level setup must be currently defined as the primary.

There
are no parameters in this member function.

getDps()
```
INT getDps();
```

This member function returns the
currently defined primary DPS set number. To use this member function, a
DPS set of the level setup must be currently defined as the
primary.

There are no parameters in this member function.

getLabel()
```
const STRING& getLabel();
```

This member function
returns the currently activated (digital) sequencer start
label.

For multi-port testing, this member function can return the
multi-port burst label.

There are no parameters in this member
function.

isTimingPortBased()
```
Boolean isTimingPortBased();
```

For multi-port testing
(however, executable even for non-multi-port). This member function
returns
TRUE
 if any specification of the timing setup
is currently defined as the primary (that is,
TRUE
 if
the current timing setup is port-based). Otherwise (that is, a
non-multi-port spec set or waveform set is used), this member function
returns
FALSE
.

Note
 Do not mix the usage of the firmware command with the test method API to
query or change the hardware status. The test method API uses an internal cache which is not
known and not accessible to the firmware command. The hardware status change made with the
firmware command is not recorded in the cache and the subsequent hardware status querying with
the test method API may return an incorrect result. To query the hardware status with the test
method API, you need to change the hardware status with the test method API. To query the
hardware status with the firmware command, you need to change the hardware status with the
firmware command.

isLabelPortBased()
```
Boolean isLabelPortBased();
```

For multi-port testing
(however, executable even for non-multi-port). This member function
returns
TRUE
 if any multi-port burst label is
currently activated as the start label (that is,
TRUE

if the current vector setup is port-based). Otherwise, this member
function returns
FALSE
.

There are no parameters
in this member function.

assignLabelToCurrentSite()
```
PRIMARY_STATUS & assignLabelToCurrentSite(const STRING & label);
```

This
member function assigns a site specific start label to the current site.
It can only be used within a
FOR_EACH_SITE
 block.
Note that this function requires the parallel enable flag of the
respective testsuite to be set. See also
`How to execute separate patterns per site`（raw: `119760.htm`）
.

[表] Parameter
行 1:
  label
  The label that is to be defined as the start label
    of the current site.
getAssignedLabelForCurrentSite()
```
const STRING & getAssignedLabelForCurrentSite();
```

This
member function returns the start label for the current site. It can
only be used within a
FOR_EACH_SITE
 block. The
function has no parameters.

assignPinToCurrentSite()
```
PRIMARY_STATUS & assignPinToCurrentSite(const STRING & pin = "");
```

This
member function controls which label is to be executed on a channel that
is shared for a pin by sites with different start labels. The operation
mode of this function depends on whether it is used within or outside a

FOR_EACH_SITE
 block. In the first case, it must
be called with a pin which is associated on the current site with a
channel also used by other sites. This call will have the effect that
the start label of the current site will be executed on this channel. If
the function is used outside a
FOR_EACH_SITE
 block,
it must be called with an empty parameter. This has the effect that all
previously defined associations of channel sharing pins with a specific
site are revoked. Note that this function requires the parallel enable
flag of the respective testsuite to be set. See also
`How to execute separate patterns per site`（raw: `119760.htm`）
.

[表] Parameter
行 1:
  pin
  Name of a pin that is mapped to the same channel
    on several sites.
getAssignedPinForCurrentSite()
```
const STRING & getAssignedPinForCurrentSite();
```

This
member function returns the channel sharing pins whose channel is
associated with the current site. It can only be used within a

FOR_EACH_SITE
 block. The function has no
parameters.

getModeContextName()
```
bool getModeContextName(STRING& sModeContextName);
```

This member function returns the name of the currently active
`mode context`（raw: `10633.htm`）
.
Parameter
[表]
行 1:
  sModeContextName
  Reference to an already defined string variable
    that is filled with the name of the active mode
    context.
Return value
The member function returns always

true
.

### Examples

### Change the primary timing set
```
Primary.timing(3);

FUNCTIONAL_TEST();
```

The

timing
 member function specifies timing set 3 as the primary
timing set to be defined, and
FUNCTIONAL_TEST
 reflects it to the
hardware then executes a functional test.

### Retrieve the primary DPS set
```
INT dps_setNum;
...
dps_setNum = Primary.getDps();
```

The

getDps
 member function returns the DPS set number that is
currently defined as the primary into the variable

dps_setNum
.

<!-- 语法节 end -->

## 是什么

**文档事实** PRIMARY_STATUS API 访问一个数据容器，该容器保存数字 primary 的当前定义：timing 相关 primary、level 相关 primary 以及 start label。这些定义可通过其成员函数修改。

**文档事实** 该 API 还可调用子数据容器：`TIMING_SPEC` 与 `LEVEL_SPEC` 的类对象，用于修改 primary timing/level 的 equation/spec set 定义及 spec 值；多 port 测试时另有 `SPECIFICATION` 的类对象可用。

**文档事实** 通过本 API 指定的定义变更，会在执行以下任一 API 时真正反映到硬件：`EXECUTE_TEST`、`START_TEST`、`DIGITAL_CAPTURE_TEST`、`NB_DIGITAL_CAPTURE_START`、`FUNCTIONAL_TEST`、`FLUSH` 后执行 `SPEC_SEARCH.execute()`、`FLUSH` 后执行 `SEQUENCER_STATUS.run()`、`FLUSH` 后执行 `PMU_IFVM.execute()`/`PMU_VFIM.execute()`/`TASK_LIST.execute()`/`DPS_VFIM.execute()`。

**文档事实** 执行 `FLUSH` 时，这些变更也可以反映到 MCD；文档把这一点描述为把变更反映到 Test Program Explorer、Spec Tool 等用户界面的选项。

**文档事实** 读取定义时返回的是当前已激活的定义。即使 sequencer 指令 `CTIM`（或 `CLEV`）在 start label 的 vector 生成期间把 timing set（或 level set）从 primary 切换到另一个，该指令也不改变 primary timing set（或 primary level set）的定义。

**文档事实** 该类没有构造函数。使用 PRIMARY_STATUS API 时必须始终使用系统预置的类对象 `Primary`，不能自行创建该 API 的对象。头文件为 `/opt/hp93000/soc/prod_com/include/MAPI/PrimaryStat.h`。

**文档事实** 成员函数覆盖 timing、waveform、level、dps、label 的设置与读取，多 port 下的 port-based timing 与 `SPECIFICATION`，以及 `FOR_EACH_SITE` 内使用的 `assignLabelToCurrentSite`、`assignPinToCurrentSite`。

## 典型用法

**文档事实** 修改 primary timing set：

```cpp
Primary.timing(3);

FUNCTIONAL_TEST();
```

**文档事实** `timing` 成员函数把 timing set 3 指定为要定义的 primary timing set，`FUNCTIONAL_TEST` 把它反映到硬件后执行功能测试。

**文档事实** 读取 primary DPS set：

```cpp
INT dps_setNum;
...
dps_setNum = Primary.getDps();
```

**文档事实** `getDps` 把当前定义为 primary 的 DPS set 号返回给变量 `dps_setNum`。

**文档事实** 读取 primary timing/waveform/level/label 分别用 `Primary.getTiming()`、`Primary.getWaveform()`、`Primary.getLevel()`、`Primary.getLabel()`；读取 primary timing/level 的 equation/spec set 与 spec 值用 `Primary.getTimingSpec()`、`Primary.getLevelSpec()`。

**文档事实** 对 `timing`、`waveform`、`level`、`dps` 传入 0 时，当前定义保持不变；equation-based setup 也要用这些参数指定 primary set 号。

**文档事实** 若在 PRIMARY_STATUS 指定变更后需要由 DC 测试 API（`PMU_VFIM`、`PMU_IFVM`、`DPS_VFIM`）生成 vector，必须先执行 `FLUSH` 以反映变更；`FUNCTIONAL_TEST` 不处理 analog set 与 routing set，涉及 analog 模块的功能测试也要先 `FLUSH`。

**文档事实** 多 port 测试可用 `timing(INT tset, const STRING& port)` 为指定 port 定义 primary timing set，或用 `timing(const SPECIFICATION& specif)` 指定 specification；用 `isTimingPortBased()`、`isLabelPortBased()` 判断当前 timing setup/vector setup 是否 port-based。

**文档事实** `assignLabelToCurrentSite` 为当前 site 指定 site 专用 start label，只能在 `FOR_EACH_SITE` 块内使用，并且要求相应 testsuite 的 parallel enable 标志已置位；`assignPinToCurrentSite` 控制多个 site 共用同一 channel 时哪个 label 在该 channel 上执行，块内带 pin 调用、块外以空参数调用可撤销先前的关联。

**文档事实** `getModeContextName(STRING&)` 返回当前 active mode context 的名称，文档称该成员函数总是返回 `true`。

**建议** 不要用 firmware command 与 test method API 混查或混改硬件状态：文档说明 test method API 使用内部 cache，firmware command 的硬件状态变更不会记录到该 cache，随后的 API 查询可能返回错误结果。

## 和谁有关

- **TIMING_SPEC / LEVEL_SPEC / SPECIFICATION** — **文档事实**：本页把它们列为 PRIMARY_STATUS 可调用的子数据容器；`getTimingSpec()`、`getLevelSpec()`、`getSpecification()` 返回对应类对象，用于修改 primary 的 spec set 与 spec 值。
- **FUNCTIONAL_TEST / START_TEST / EXECUTE_TEST / DIGITAL_CAPTURE_TEST / NB_DIGITAL_CAPTURE_START** — **文档事实**：执行这些 API 时，PRIMARY_STATUS 指定的数字 primary（timing/level 相关 primary 与 start label）会自动定义为新设置并激活到硬件，因此无需再执行 `FLUSH`。
- **FLUSH** — **文档事实**：本页说明 `FLUSH` 可把变更反映到 MCD（供 UI 显示），也是 DC 测试 API 生成 vector 前反映 primary 变更的手段；表格按 API 列出 primary 是在 Define 还是 Activate 阶段生效。
- **PMU_VFIM / PMU_IFVM / DPS_VFIM / TASK_LIST / SPMU_TASK / DPS_TASK / SEQUENCER_STATUS / SPEC_SEARCH** — **文档事实**：这些出现在本页的生效时机表中；DC API（`PMU_VFIM`、`PMU_IFVM`、`DPS_VFIM`）需先 `FLUSH` 才能反映 primary 变更。
- **CTIM / CLEV（sequencer 指令）** — **文档事实**：本页明确它们只切换当前 timing/level set，不改变 primary 的定义。
- **FOR_EACH_SITE** — **文档事实**：`assignLabelToCurrentSite`、`getAssignedLabelForCurrentSite`、`assignPinToCurrentSite`、`getAssignedPinForCurrentSite` 只能在 `FOR_EACH_SITE` 块内使用。
- **How to execute separate patterns per site** — **文档事实**：`assignLabelToCurrentSite` 与 `assignPinToCurrentSite` 的说明都链接到该页，并指出需要 testsuite 的 parallel enable 标志。
- **mode context** — **文档事实**：`getModeContextName` 返回当前 active mode context 的名称，正文链接到 mode context 的说明页。
- **testflow** — **文档事实**：本页脚注说明 testflow 会在每个 testsuite 的 test method 程序启动前自动完成 primary 的定义与激活。

## 版本

**文档事实** Functional changes 记载：Introduced before SmarTest 6.3.2；SmarTest 7.5.3 新增成员函数 `getModeContextName()`。

## 出处

- `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.167_PRIMARY_STATUS_-__Primary.htm`：主源，含 API 概述、生效时机、Class definition、成员函数说明、Syntax for common tasks、Examples、Important points、Functional changes。
