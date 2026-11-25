---
type: object
title: TASK_LIST
layer: L2
stage: testmethod
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.240_TASK_LIST.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# TASK_LIST

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **6,850 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.240_TASK_LIST.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Class definition

This API is defined in the header file

/opt/hp93000/soc/prod_com/include/MAPI/TaskList.h
.

Constructor

```
TASK_LIST();
```

This constructor defines a task list that holds task names to be
executed.

Parameters

There are no parameters associated with this function.

Member functions:

`add()`（raw: `29792.htm#_29792__dle_add`）

`setup()`（raw: `29792.htm#_29792__dle_setup`）

`execute()`（raw: `29792.htm#_29792__dle_execute`）

### Usage

For creating an object:

```
TASK_LIST <object>;
```

For setting up tasks to be performed:

```
<object>.add(task1).add(task2)...add(taskN);
```

For downloading the settings in tasks:

```
<object>.setup();
```

For downloading the settings in tasks and performing the tasks:

```
<object>.execute();
```

[表]
行 1:
  <object>
  Object name to be defined
行 2:
  task1-N
  Object name of the PPMU_SETTING, PPMU_RELAY or
    PPMU_MEASURE class to specify a task to
    be performed. A task list can contain up to 10 tasks.

### Member functions

add()

```
TASK_LIST & add(const TASK& task);
```

This function adds the specified task to the task list. Added tasks are
performed sequentially.

Note
 If you define a
TASK_LIST
 object as
global, the object will not be destroyed when the test method is
completed. This will have the effect that the list grows longer with
every testflow repetition, so that the test time is increased with every
repetition.

[表] Parameter
行 1:
  task
  Object name of the PPMU_SETTING, PPMU_RELAY or
    PPMU_MEASURE class to specify a
    task be performed.

Using the offline result emulation function:

Measurements can be made by using
`DPS_TASK`（raw: `55630.htm`）
,
`SPMU_TASK`（raw: `55670.htm`）
, and

`PPMU_MEASURE`（raw: `29585.htm`）
 objects directly (by calling their

execute()
 member functions) or be put in a

TASK_LIST
 object which queues up tasks to be executed (by calling
the
execute()
 method on the
TASK_LIST
 object
rather than on the task objects themselves). This requires an enhancement also on the

TASK_LIST add()
 method which takes a measurement name as
additional parameter.

```
TASK_LIST& add(const TASK& task)
```

This is the existing function which adds the specified task to the task list.

```
TASK_LIST& add(const TASK& task, const string& measurementName)
```

This function adds the specified task to the task list.

Parameter

[表]
行 1:
  measurementName
  Associate the measurement that will be executed by calling
    task_list.execute() with offline data.

For more details, see
`Parametric offline result emulation`（raw: `128581.htm`）
 in
`Offline Result Emulation`（raw: `128475.htm`）
.

setup()

```
void setup();
```

This function downloads settings defined in the task list. The tasks of
the task list are executed sequentially in the registered order. It is
used when the input parameters of the task are changed during the test
method execution. It can change the parameters of an exisiting MSET and
reuse it to avoid running out of MSETs. (Refer to
`FlexDC`（raw: `122087.htm`）
 and
`Managing DC Tests with Variable Parameters`（raw: `75890.htm`）
 for details.)

Parameters

There are no parameters associated with this function.

execute()

```
void execute();
```

This function performs a test by executing the task list. The tasks of
the task list are executed sequentially in the registered order.

Parameters

There are no parameters associated with this function.

Note
 After the
execute()
 function is performed, you cannot
define any tasks for the digital pin that is not included to the
performed task. For example, the following program defines and executes
the "tasks" task list.

```
PPMU_SETTING setting1;
TASK_LIST tasks;

tasks.add(setting1);

setting1.pin("pin1").vForce(2.1 mV);
setting1.pin("pin1").iRange("10uA");
setting1.pin("pin1").min(0.1 uA).max(5.0 uA);

tasks.execute();
```

After that, you can modify or define tasks for "pin1" as shown below:

```
setting1.pin("pin1").vForce(2.5 mV); // OK
```

However, error occurs if the following program is performed because tasks
for "pin2" is not defined in the "tasks" task list.

```
setting1.pin("pin2").vForce(2.1 mV); // error
```

### Example

In the following example, the task
setting
,
precharge
,

relay_on
,
relay_off
,

ppmuMeasure
,
clamp_on
 and

clamp_off
 are defined and added to the task list. Then a PPMU
measurement is performed by executing the task list.

```
PPMU_SETTING ppmuSetting;
PPMU_RELAY ppmuRelay_on, ppmuRelay_off;
PPMU_MEASURE ppmuMeasure;
PPMU_CLAMP ppmuClamp_on, ppmuClamp_off;
TASK_LIST taskList_1;

ON_FIRST_INVOCATION_BEGIN();

//
// Setups for PPMU
//
ppmuSetting.pin("S0").iRange(1 mA).min(0 V).max(4.3 V).iForce(10 uA);
ppmuSetting.pin("S1").iRange(10 mA).min(-10 uA).max(30 uA).vForce(3.3 V);

//
// Relay setups
//
ppmuRelay_on.pin("S0,S1").status("PPMU_ON");
ppmuRelay_on.wait(1.3 ms);
ppmuRelay_off.pin("S0,S1").status("AC_ON");

//
// Measurement setups
//
ppmuMeasure.pin("S0,S1").execMode(TM::PVAL);

//
// Hardware specific programming to avoid hot switching on the current force setup
//
ppmuClamp_on.pin("S0").status("CLAMP_ON").low(2.6 V).high(2.9 V);
ppmuClamp_off.pin("S0").status("CLAMP_OFF");

//
// Build and execute the task list
//
taskList_1.add(ppmuSetting)
.add(ppmuClamp_on)
.add(ppmuRelay_on)
.add(ppmuClamp_off)
.add(ppmuMeasure)
.add(ppmuRelay_off);

taskList_1.execute();

ON_FIRST_INVOCATION_END();

//
// Result upload and Datalog
//
double VMeas, IMeas;

VMeas = ppmuMeasure.getValue("S0");
IMeas = ppmuMeasure.getValue("S1");

TEST("DC_Test",ppmuMeasure, true);
```

The following example shows how to measure a current on a device pin and then use it
as a force value for a following measurement for multi-sites. The result value of
the first measurement differs from site to site.

```
PPMU_MEASURE ppmuMeasure2;

ON_FIRST_INVOCATION_BEGIN();

PPMU_MEASURE ppmuMeasure1;
PPMU_SETTING ppmuSetting1,ppmuSetting2;
PPMU_RELAY ppmuRelayOn, acRelayOn;
TASK_LIST multiDeltaFlexDc1, multiDeltaFlexDc2;

// 1st measurement
ppmuSetting1.pin("I/O1").vForce(0 V).iRange(1 uA).max(1 uA).min(-1 uA);
ppmuRelayOn.pin("I/O1").status("PPMU_ON");
ppmuRelayOn.wait(1.3 ms);
ppmuMeasure1.pin("I/O1").execMode(TM::PVAL);
acRelayOn.pin("I/O1").status("AC_ON");
multiDeltaFlexDc1.add(ppmuSetting1).add(ppmuRelayOn).add(ppmuMeasure1);
multiDeltaFlexDc1.execute();

// dummy setting for avoiding DC set run out
ppmuSetting2.pin("I/O1").iForce(0 uA).iRange(1 mA).max(0.5 V).min(-0.5 V);
ppmuSetting2.wait(1 ms);
ppmuMeasure2.pin("I/O1").execMode(TM::PVAL);
multiDeltaFlexDc2.add(ppmuSetting2).add(ppmuMeasure2).add(acRelayOn);
multiDeltaFlexDc2.setup();

// 2nd measurement
FOR_EACH_SITE_BEGIN();

ppmuSetting2.pin("I/O1")
.iForce(ppmuMeasure1.getValue("I/O1"))
.iRange(ppmuMeasure1.getValue("I/O1"))
.max(0.5 V)
.min(-0.5 V);

FOR_EACH_SITE_END();

multiDeltaFlexDc2.execute();

ON_FIRST_INVOCATION_END();

TEST("I/O1",
"multi_delta",
ppmuMeasure2.getPassFail("I/O1")?TM::Pass:TM::Fail,
ppmuMeasure2.getValue("I/O1"),
true );
```

<!-- 语法节 end -->

## 是什么

**文档事实**：`TASK_LIST` 是数据容器，保存要执行的 `PPMU_SETTING`、`PPMU_RELAY`、`PPMU_MEASURE` 任务；任务按加入任务表的顺序执行（`02.07.04.01.240`）。

**文档事实**：定义在头文件 `/opt/hp93000/soc/prod_com/include/MAPI/TaskList.h`；构造函数 `TASK_LIST()` 无参数（`02.07.04.01.240`）。

**文档事实**：成员函数为 `add()`（把任务加入列表，可链式调用）、`setup()`（下载任务设置）、`execute()`（下载设置并执行任务）（`02.07.04.01.240`）。

**文档事实**：一个任务表最多容纳 10 个任务（`02.07.04.01.240`）。

**文档事实**：`setup()` 按注册顺序顺序下发任务设置；用于测试方法执行期间任务输入参数发生变化的场景，可修改已有 MSET 的参数并复用，以避免 MSET 用尽（文档指向 FlexDC 与 Managing DC Tests with Variable Parameters）（`02.07.04.01.240`）。

**文档事实**：`execute()` 执行任务表即完成一次测试；执行后，对未包含在已执行任务中的数字 pin 不能再定义任务。示例：执行过含 `pin("pin1")` 的列表后，改 `pin1` 可以，改 `pin2` 会报错（`02.07.04.01.240`）。

**文档事实**：若把 `TASK_LIST` 对象定义为全局，测试方法结束后对象不会被销毁，任务表会在每次 testflow 重复时变长，导致测试时间逐次增加（`02.07.04.01.240`）。

**文档事实**：`add(task, measurementName)` 重载把测量与离线数据关联，用于 Parametric offline result emulation；离线结果仿真在 SmarTest 7.1.3 引入（`02.07.04.01.240`）。

## 典型用法

**文档事实**：典型顺序是「声明任务对象 → 配置 pin、量程、继电器、测量 → 依次 `add()` → `execute()` → 用 `getValue()`/`getPassFail()` 取结果并 `TEST()`」（`02.07.04.01.240`）。

**文档事实**：示例 1 把 `ppmuSetting`、`ppmuClamp_on`、`ppmuRelay_on`、`ppmuClamp_off`、`ppmuMeasure`、`ppmuRelay_off` 按顺序加入任务表，在 `ON_FIRST_INVOCATION_BEGIN()` 内执行；示例中的 `PPMU_CLAMP` 用于避免 current force setup 上的 hot switching（`02.07.04.01.240`）。

**文档事实**：示例 2 先用 `setup()` 下发第二组任务，在 `FOR_EACH_SITE_BEGIN()`/`FOR_EACH_SITE_END()` 之间按 site 修改 `iForce`，再 `execute()`；其中 `ppmuSetting2` 是避免 DC set 用尽的 dummy setting（`02.07.04.01.240`）。

**文档事实**：`DPS_TASK`、`SPMU_TASK`、`PPMU_MEASURE` 可以直接调用 `execute()`，也可以放入 `TASK_LIST` 排队、由 `TASK_LIST.execute()` 统一执行；后一种需要 `add(task, measurementName)` 重载（`02.07.04.01.240`）。

**文档事实**：`setup()` 可以只下载设置而不执行，随后再改参数并 `execute()`；示例 2 正是这种两段式用法（`02.07.04.01.240`）。

**建议**：不要把 `TASK_LIST` 定义成全局对象——文档明确说明会逐次累积任务并拉长测试时间（`02.07.04.01.240`）。

## 和谁有关

- **PPMU_SETTING / PPMU_RELAY / PPMU_MEASURE** — **文档事实**：这三类对象就是任务表保存并顺序执行的任务（`02.07.04.01.240`）。
- **DPS_TASK**（[[dps-task]]）/ **SPMU_TASK**（[[spmu-task]]）— **文档事实**：离线结果仿真时可直接 `execute()`，也可经 `TASK_LIST` 排队执行（`02.07.04.01.240`）。
- **FlexDC / Managing DC Tests with Variable Parameters** — **文档事实**：`setup()` 通过修改已有 MSET 参数并复用来避免 MSET 用尽，文档把这两篇列为细节来源（`02.07.04.01.240`）。
- **Parametric offline result emulation / Offline Result Emulation** — **文档事实**：`add(task, measurementName)` 的 `measurementName` 用于把测量与离线数据关联（`02.07.04.01.240`）。
- **FOR_EACH_SITE_BEGIN / FOR_EACH_SITE_END**（[[for-each-site-begin]]）— **文档事实**：多 site 示例在二者之间按 site 修改任务参数（`02.07.04.01.240`）。
- **ON_FIRST_INVOCATION_BEGIN / ON_FIRST_INVOCATION_END、`TEST()`** — **文档事实**：示例用前者包住一次性建立/执行，用后者上传结果（`02.07.04.01.240`）。
- **PPMU_CLAMP** — **文档事实**：示例代码用到了它，但类说明与 `add()` 参数说明只把任务类型列为 `PPMU_SETTING`、`PPMU_RELAY`、`PPMU_MEASURE`；此处照原样记录（`02.07.04.01.240`）。
- **MSET / DC set** — **文档事实**：`setup()` 可修改已有 MSET 的参数并复用它，以避免 MSET 用尽；示例以 “dummy setting” 规避 DC set run out（`02.07.04.01.240`）。

## 版本

**文档事实**：Functional changes 记 “Introduced before SmarTest 6.3.2”（文档集覆盖起点前的哨兵值，不能当作 6.3.2 的变更），以及 “SmarTest 7.1.3: Offline result emulation introduced”（`02.07.04.01.240`）。

**文档事实**：正文描述的 `add(const TASK& task, const string& measurementName)` 重载正对应 7.1.3 引入的离线结果仿真；它把任务执行结果与离线数据关联（`02.07.04.01.240`）。

## 出处

- `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.240_TASK_LIST.htm`（主文档：类定义、成员函数、示例、Functional changes）
- 关联（正文回链）：`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.157_PPMU_MEASURE.htm`、`02.07.04.01.158_PPMU_RELAY.htm`、`02.07.04.01.160_PPMU_SETTING.htm`、`03_Use_cases_and_application_papers/03.01_Performance_Cookbook__How_to_reduce_test_times/03.01.05.02_FlexDC.htm`、`02_System_reference/02.07_Test_Method_Reference/02.07.03.02.06.03_Managing_DC_Tests_with_Variable_Parameters.htm`；Parametric offline result emulation 见正文 raw `128581.htm`
