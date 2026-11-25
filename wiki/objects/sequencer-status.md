---
type: object
title: SEQUENCER_STATUS - (Sequencer)
layer: L3
stage: pattern
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.204_SEQUENCER_STATUS_-__Sequencer.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# SEQUENCER_STATUS - (Sequencer)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **8,384 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.204_SEQUENCER_STATUS_-__Sequencer.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Class definition

### Member Functions
```
SEQUENCER_STATUS& stopCycle(int num);
SEQUENCER_STATUS& stopCycle(int num, const STRING& portName);
SEQUENCER_STATUS& stopVector(int num);
SEQUENCER_STATUS& reset();
run(TM::RUN_STATUS status = TM::NORMAL);
abort();
Boolean isRunning();
const STRING getSequencerStatus() const;
```

### Syntax

For running the sequencers until
the specified cycle

Sequencer.stopCycle(num).run(mode);

For
running the sequencers until the specified
vector

Sequencer.stopVector(num).run(mode);

For other
operations of the sequencers

Sequencer.member_func;

[表] Parameters
行 1:
  num
  Tester cycle number or vector number
行 2:
  mode
  Execution mode of the sequencers. You can also set the run member
    function separately as shown below:
    
    Sequencer.run(mode)
行 3:
  member_func
  Member function of the SEQUENCER_STATUS API

### Member functions

### stopCycle()
```
SEQUENCER_STATUS& stopCycle(int num);
SEQUENCER_STATUS& stopCycle(int num, const STRING& portName);
```

This
member function specifies a tester cycle after which the sequencers will stop (the specified
cycle is the last cycle that is executed, see Example section) in the global sequencer run
subsequently started with
run()
. If the current start label is a multiport
burst, you must also specify the port to which this cycle number refers.

The setting of
this function affects not only the
run()
 member function but also the

EXECUTE_TEST
,
START_TEST
,

FUNCTIONAL_TEST
,
DIGITAL_CAPTURE_TEST
,

NB_DIGITAL_CAPTURE_START
 API, and pre-action of the DC APIs.

This
function is provided to change the behavior of the sequencer execution temporarily. However the
setting of this function is effective until all settings are reset by the

reset()
 member function of this API. Therefore you should reset the setting
by using the
reset()
 member function at the end of the test suite or
before starting the sequencer for the other test.

[表] Parameters
行 1:
  num
  Tester cycle number where the sequencer stops
行 2:
  portName
  The port to which to apply the stop cycle.

### stopVector()
```
SEQUENCER_STATUS& stopVector(int num);
```

After
the sequencer is started by the run member function or others, the
stopVector()

member function specifies a vector number after which the sequencer stops (the specified vector
is the last vector in this execution, see Example section).

Notices for using this
function are the same as the
stopCycle
 member function.

[表] Parameter
行 1:
  num
  Vector number where the sequencer stops

### reset()
```
SEQUENCER_STATUS& reset();
```

This member
function clears the setting of the
stopCycle
 and

stopVector
 member function. Use this member function to perform a
standard functional test after using the
stopCycle
 and

stopVector
 member function, else the sequencer stops at the point
specified with the
stopCycle
 and
stopVector
 member
function.

Note that Sequencer.reset() will clear the settings done by stopCycle() and
stopVector() but this will only take effect (that is, it will only be flushed, that is,
downloaded) before the next sequencer run initiated through the test methods APIs listed above
under the stopCycle() member function. If the reset is to take effect earlier,

FLUSH
 must be called explicitly.

Note also that

reset()
 does not affect the current sequencer status. If you want to stop
the sequencers, you must call
Sequencer.abort()
.

Note
 In an
AC test, you need to clear the sequencer settings before the measurement.

### run()
```
run(TM::RUN_STATUS status = TM::NORMAL);
```

This
member function starts a global sequencer run. The sequencers pause after the tester cycle or
vector that is specified with the
stopCycle
 or
stopVector

member function. Note that the sequencers will only be started if no sequencer run is already
active. In this latter case you must stop all active runs with the
abort()

member function before you can call
run()
 successfully.

Note that the
DPS128/DPS64, when starting the sequencer with the
run()
 member function or
with the
`SQST RUN`（raw: `98752.htm`）
 firmware command, cannot execute dynamic and
static DC actions in parallel. Use
`profiling`（raw: `136105.htm`）
 for measurements in
parallel to a dynamic pattern.

[表] Parameter
行 1:
  status
  Sequencer running mode. The following modes are available:
    
    TM::NORMAL (Default) The sequencer executes the pattern.
    
    TM::ENDLESS_LOOP The sequencer repeats the complete test,
    including primary activation and multiport synchronization, in an endless loop and can only
    be stopped by a break action. See also the EL mode in `SQGB, SQGB? - (SeQuencer GloBal)`（raw: `98746.htm`）.
    
    TM::ENDLESS_PATTERN_LOOP The sequencer repeats only the user
    sequencer program defined in the pattern. This avoids critical holds during measurement
    for example, for IDD operating currents).
    
    In case of multiport testing, ports may run with different frequencies. Using the ELPT
    mode in this case, can lead to the situation, that for loop counts >1 the
    synchronization is no longer executed. See also the ELPT mode in `SQGB, SQGB? - (SeQuencer GloBal)`（raw: `98746.htm`）
    
    TM::STOPONERROR The sequencer stops when an error occurs in the
    execution.
    
    TM::STOPONERROR_LOOP The sequencer stops when an error occurs in
    an endless loop.

### abort()
```
abort();
```

This member function sets all
active sequencer runs into the break state. It can be used, for example, to stop an endless loop
started with
Sequencer.run(TM::ENDLESS_PATTERN_LOOP)
, and must be called in
this situation before a new sequencer run can be started.

There are no parameters in this
member function.

### isRunning()
```
Boolean isRunning();
```

This member
function returns whether the digital sequencers are running or not. You can also use the
`IS_TEST_RUNNING`（raw: `29490.htm`）
 API that returns whether either the analog or digital
sequencer is running.

There are no parameters in this member function.

### getSequencerStatus()
```
const STRING getSequencerStatus() const;
```

This
member function returns the current sequencer status. It can be OFF, RUN, HALT or
BRK.

### Examples

### Example 1

Given the following pattern, the member functions

stopVector
 and
stopCycle
 behave as follows.

Sequencer.stopCycle(13).run();

The sequencer stops after executing cycle
number 13 (p1 set to 1)

Sequencer.stopCycle(14).run();

The sequencer stops after executing cycle
number 14 (p1 set to 0)

Sequencer.stopVector(9).run();

The sequencer stops after executing vector
number 9 (p1 set to 1)

Sequencer.stopVector(10).run();

The sequencer stops after executing
vector number 10 (p1 set to 0)

### Example 2

The following example will perform a DC measurement using
FlexDC. First, it prepares the needed flex dc settings, then it starts the sequencer and pauses
on tester cycle 15 to perform the DC measurement at pin
"pin1".

```
virtual void run()
{
PPMU_SETTING setting1;
TASK_LIST tasks;
PPMU_RELAY relay_on, relay_off;
PPMU_MEASURE ppmu_meas;
PPMU_CLAMP clamp_on, clamp_off;

double VMeas_seq1;
ON_FIRST_INVOCATION_BEGIN();
setting1.pin("pin1").vForce(2.1 mV);
setting1.pin("pin1").iRange("10uA");
setting1.pin("pin1").min(0.1 uA).max(25.0 uA);

relay_on.pin("pin1").status("PPMU_ON");
relay_on.wait(1.3 ms);
relay_off.pin("pin1").status("AC_ON");

clamp_on.pin("pin1").status("CLAMP_ON").low(2.6 V).high(2.9 V);
clamp_off.pin("pin1").status("CLAMP_OFF");

ppmu_meas.pin("pin1"). execMode(TM::PVAL);

tasks.add(setting1).add(clamp_on).add(relay_on).add(clamp_off). add(ppmu_meas).add(relay_off);
Sequencer.stopCycle(15).run();
tasks.execute();
ON_FIRST_INVOCATION_END();
VMeas_seq1 = ppmu_meas.getValue("pin1");
Sequencer.reset();

return;
}
```

### Example 3
```
Sequencer.run(TM::ENDLESS_PATTERN_LOOP);
DPS_VFIM("@").execute();
Sequencer.abort();
```

This
example achieves an operating current test of the DPS with the test method. First, it starts the
sequencer in an endless pattern loop. Then it performs a current measurement at a random device
cycle. Then it aborts the
sequencer.

### Example 4
```
Sequencer.reset();
PMU_IFVM("@").preAction("FTST").execute();
```

This
example resets the sequencer before performing a functional test that is a pre-action of the DC
test. However, It is recommended to use FLEX DC instead of PMU_IFVM and use

SEQUENCER_STATUS
 APIs to execute a functional pattern as pre action if
required as shown in above example 1.

<!-- 语法节 end -->

## 是什么

**文档事实** SEQUENCER_STATUS 是访问「保存数字 sequencer 状态的数据容器」的测试方法 API，通过成员函数操作 sequencer。

**文档事实** 使用限制：必须使用系统预先准备的类对象 `Sequencer`；不能自行创建 SEQUENCER_STATUS 类的对象。该 API 不影响模拟 sequencer。

**文档事实** 该 API 不支持 execution context：只能通过 `run()` 启动全局 sequencer run（执行当前 start label），只能通过 `abort()` 全局中止所有活动 run。

**文档事实** 若已有 sequencer 在运行（例如处于 endless loop），`run()` 不会再启动全局 run；必须先 `abort()` 停掉所有活动 run。

**文档事实** API 定义在头文件 `/opt/hp93000/soc/prod_com/include/MAPI/SequencerStat.h`。

**文档事实** 成员函数共七类：`stopCycle`（带 `portName` 与不带 `portName` 两个重载）、`stopVector`、`reset`、`run`、`abort`、`isRunning`、`getSequencerStatus`。

**文档事实** `stopCycle(num[, portName])` 指定随后由 `run()` 启动的全局 run 在第 num 个 tester cycle 之后停止（该 cycle 是最后执行的一个）；若当前 start label 是 multiport burst，还必须给出该 cycle 号所属的 port。它的设置不仅影响 `run()`，也影响 EXECUTE_TEST、START_TEST、FUNCTIONAL_TEST、DIGITAL_CAPTURE_TEST、NB_DIGITAL_CAPTURE_START 这些 API 以及 DC API 的 pre-action。设置一直有效，直到 `reset()` 清除；因此应在 test suite 末尾、或在为另一项测试启动 sequencer 之前 reset。

**文档事实** `stopVector(num)` 指定 sequencer 在第 num 个 vector 之后停止（该 vector 是本次执行最后一个）；注意事项与 `stopCycle` 相同。

**文档事实** `reset()` 清除 `stopCycle`/`stopVector` 的设置；不 reset 的话，后续标准 functional test 会在先前指定的点停止。reset 要等到下一次由上述 test method API 发起的 sequencer run 之前才 flush（download）；要更早生效必须显式调用 FLUSH。`reset()` 不改变当前 sequencer 状态；要停止 sequencer 必须调用 `abort()`。AC test 中必须在测量前清除 sequencer 设置。

**文档事实** `run(status = TM::NORMAL)` 启动全局 sequencer run；sequencer 在 `stopCycle`/`stopVector` 指定的 cycle 或 vector 之后暂停；只有在没有活动 run 时才会启动。

**文档事实** `status` 模式：`TM::NORMAL`（执行 pattern）、`TM::ENDLESS_LOOP`（无限重复完整测试，含 primary activation 与 multiport 同步，只能由 break 动作停止）、`TM::ENDLESS_PATTERN_LOOP`（只重复 pattern 中用户 sequencer 程序，避免测量期间的关键 hold，例如 IDD 工作电流测量）、`TM::STOPONERROR`（执行出错时停止）、`TM::STOPONERROR_LOOP`（在 endless loop 中出错时停止）。multiport 下各 port 频率可不同；此时用 ELPT 模式，当 loop count > 1 时同步可能不再执行。

**文档事实** `abort()` 把所有活动 sequencer run 置为 break 状态，可用于停止以 `TM::ENDLESS_PATTERN_LOOP` 启动的无限循环，且必须在新 run 之前调用。

**文档事实** `isRunning()` 返回数字 sequencer 是否在运行；要判断模拟或数字 sequencer 是否在运行，用 IS_TEST_RUNNING API。

**文档事实** `getSequencerStatus()` 返回当前 sequencer 状态：`OFF`、`RUN`、`HALT` 或 `BRK`。

**文档事实** 限制：DPS128/DPS64 用 `run()` 或固件命令 `SQST RUN` 启动 sequencer 时，不能并行执行动态与静态 DC 动作；与动态 pattern 并行的测量要用 profiling。

## 典型用法

**文档事实** Example 1：`Sequencer.stopCycle(13).run();` 在第 13 个 cycle（p1=1）后停；改 `stopCycle(14)` 则在第 14 个 cycle（p1=0）后停；`stopVector(9)` 在第 9 个 vector（p1=1）后停，`stopVector(10)` 在第 10 个 vector（p1=0）后停。

**文档事实** Example 2：FLEX DC 测量。先在 `ON_FIRST_INVOCATION_BEGIN()` 内准备 PPMU_SETTING、PPMU_RELAY、PPMU_CLAMP、PPMU_MEASURE 等 task，再 `Sequencer.stopCycle(15).run();` 启动 sequencer 并在 tester cycle 15 暂停，`tasks.execute()` 执行 DC 测量，读回 `ppmu_meas.getValue("pin1")` 后 `Sequencer.reset();`。

**文档事实** Example 3：`Sequencer.run(TM::ENDLESS_PATTERN_LOOP);` → `DPS_VFIM("@").execute();` → `Sequencer.abort();`，在无限 pattern loop 中于随机 device cycle 测 DPS 工作电流，然后中止 sequencer。

**文档事实** Example 4：`Sequencer.reset();` 后执行 `PMU_IFVM("@").preAction("FTST").execute();`，在 DC 测试的 pre-action 前清空 sequencer 设置。文档同时建议用 FLEX DC 代替 PMU_IFVM，并在需要 functional pattern 作 pre-action 时按 Example 2 用 SEQUENCER_STATUS API。

**建议** 把 `stopCycle`/`stopVector` 视为「一次性定长执行」的手段，用完立即 `reset()`；否则该设置会延续到后续 test suite，文档明确要求在使用后 reset。

**建议** 需要在 DC 测量前稳定 pattern 时，优先用 `stopCycle` 定位并暂停 sequencer（Example 2 的模式），不要沿用 PMU_IFVM 的 functional pre-action 老写法——文档本身推荐 FLEX DC。

## 和谁有关

- **文档事实** SQGB —— 固件侧控制 sequencer 状态的命令；`run()` 的 `EL` 与 `ELPT` 模式语义分别对应 SQGB 的 EL / ELPT 模式，正文两处指向该页。
- **文档事实** SQST —— `SQST RUN` 也能启动 sequencer，并与 `run()` 共有「DPS128/DPS64 不能并行动态与静态 DC」的限制。
- **文档事实** Controlling sequencer status（`02.07.03.12`）—— 明写 test method 编程中可用 SEQUENCER_STATUS API 或固件命令 SQGB 显式控制 sequencer 状态；并说明 DC test method library 测量后不清 sequencer、AC library 在测量前用 `Sequencer.reset()` 或 `SQGB ACQF,0` 清除。
- **文档事实** EXECUTE_TEST、START_TEST、FUNCTIONAL_TEST、DIGITAL_CAPTURE_TEST、NB_DIGITAL_CAPTURE_START —— `stopCycle` 的设置同样作用于这些 API（以及 DC API 的 pre-action）。
- **文档事实** [[flush]] —— `reset()` 要早于下一次 run 生效，必须显式调用 FLUSH。
- **文档事实** IS_TEST_RUNNING —— `isRunning()` 只回答数字 sequencer；要覆盖模拟 sequencer 用 IS_TEST_RUNNING。
- **文档事实** WAIT_TEST_DONE / SMC_WAIT_TEST_DONE —— 可与 SEQUENCER_STATUS 一起使用，此时超时从对应 API 执行结束时开始计。
- **文档事实** Applying Desired Vector before DC Test（`02.07.03.08.01`）—— 指出也可用 SEQUENCER_STATUS API 施加目标 vector address 或 device cycle 对应的 vector。
- **文档事实** [[dps128-dps64-cards]] —— 上述动态/静态 DC 限制的硬件来源；文档给出的并行测量替代是 profiling。
- **文档事实** PMU_IFVM、DPS_VFIM —— 分别出现在 Example 4 与 Example 3；前者文档建议改用 FLEX DC。
- **文档事实** APIs in alphabetical order（`02.07.04.01`）—— SEQUENCER_STATUS 收录于该 API 索引。

## 版本

**文档事实** Functional changes：Introduced before SmarTest 6.3.2；SmarTest 6.5.2 新增 `run()` 的 `TM::STOPONERROR` 与 `TM::STOPONERROR_LOOP` 选项、新增 `getSequencerStatus()` 成员函数、`stopCycle()` 新增 `portName` 参数；SmarTest 6.5.4 新增 `run()` 的 `TM::ENDLESS_PATTERN_LOOP` 选项。

## 出处

- `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.204_SEQUENCER_STATUS_-__Sequencer.htm` —— 主源：正文与使用限制、Class definition、Syntax、各成员函数说明、Examples 1–4、Functional changes。
- `02_System_reference/02.07_Test_Method_Reference/02.07.03.12_Controlling_sequencer_status.htm` —— 读了控制方式、DC/AC test programming 与 Functional changes。
- 其余跨页条目（SQGB、SQST、WAIT_TEST_DONE 等）取自各页被本接口引用的语境句，未整篇通读。
