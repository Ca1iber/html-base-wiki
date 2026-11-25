---
type: object
title: DIGITAL_CAPTURE_TEST
layer: L2
stage: testmethod
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.35_DIGITAL_CAPTURE_TEST.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# DIGITAL_CAPTURE_TEST

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **5,320 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.35_DIGITAL_CAPTURE_TEST.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
void DIGITAL_CAPTURE_TEST();
void DIGITAL_CAPTURE_TEST(const TM::WAIT_ACTION& wait_action);
void DIGITAL_CAPTURE_TEST(DOUBLE timeout, const TM::WAIT_ACTION& wait_action);
void DIGITAL_CAPTURE_TEST(const STRING & resultAreaId);
void DIGITAL_CAPTURE_TEST(const STRING & resultAreaId, const STRING& context);
void DIGITAL_CAPTURE_TEST(DOUBLE timeout,
const STRING & resultAreaId);
void DIGITAL_CAPTURE_TEST(DOUBLE timeout,
const STRING & resultAreaId, const STRING& context);
void DIGITAL_CAPTURE_TEST(const TM::WAIT_ACTION& wait_action,
const STRING & resultAreaId);
void DIGITAL_CAPTURE_TEST(const TM::WAIT_ACTION& wait_action,
const STRING & resultAreaId, const STRING& context);
void DIGITAL_CAPTURE_TEST(DOUBLE timeout, const TM::WAIT_ACTION& wait_action,
const STRING & resultAreaId);
void DIGITAL_CAPTURE_TEST(DOUBLE timeout, const TM::WAIT_ACTION& wait_action,
const STRING & resultAreaId, const STRING& context);
```
[表] Parameters
列: I/O | Parameter | Description/Range
行 1:
  I
  timeout
  Timeout time of the measurement (test).
    
    Unit: s
    
    If you omit this parameter, the default timeout is 360000 s.
行 2:
  I
  wait_action
  This parameter allows you to select which sequencer's completion the API waits for,
    from the following hardware categories that are represented by the constant variables. It
    is also valid for combination of them by using "|" (use bitwise OR
    to select multiple ones). For example, if you make this API waited until AWGs and
    digitizers/samplers complete the current sequencer programs, specify
    TM::WAIT_AWG|TM::WAIT_DGT to this parameter.
    
    TM::WAIT_ALL:
    waits until all used digital channels, AWGs,
    digitizers/samplers, and TIAs complete their tasks.
    
    TM::WAIT_DIGITAL (default):
    waits until all used digital
    channels complete the current sequencer program.
    
    TM::WAIT_AWG:
    waits until all used AWGs complete the current
    sequencer programs.
    
    TM::WAIT_DGT:
    waits until all used digitizers and samplers
    complete the current sequencer programs.
    
    TM::WAIT_TIA:
    waits until all used TIAs complete the current
    measurements.
行 3:
  I
  resultAreaId
  The name of a result retention area for background processing. See `RESULT_AREA_CONFIG`（raw: `140869.htm`） API.
    
    For sequencer context executions without using a result area use an empty string for the
    resultAreaId, and specify both this and the context
    parameter. See also example below.
行 4:
  I
  context
  Name of an execution context. The ports of the context must be included in the
    current start label (which must be a multiport burst). For more information on execution
    contexts see `Using execution contexts`（raw: `135848.htm`） .
    
    The context must have been defined on the firmware level (with the
    SQEC command), or as a SEQUENCER_CONTEXT_ITEM
    object. In the latter case this object must have been included in a
    SEQUENCER_CONTEXT object, and must also have been activated on the
    firmware level with the apply() function of this
    SEQUENCER_CONTEXT object. If the context has been defined as a
    SEQUENCER_CONTEXT_ITEM object, you must use the name specified for its
    name parameter.

### Important points

In order for the
DIGITAL_CAPTURE_TEST
 API (or an API that internally
executes the
FLUSH
 API) to reflect the changes that are specified by

ROUTING_STATUS
/
ANALOG_STATUS
 to an
analog
module hardware
, the sequencers in all analog modules must be halted. For more
information, see the
`FLUSH`（raw: `29338.htm`）
 API.

To execute a test that contains digital capturing, use the

DIGITAL_CAPTURE_TEST
 API.

If you attempt to execute a test containing
digital capturing with the
EXECUTE_TEST
 or

START_TEST
 API, the test cannot be done. On the other hand, if you
attempt to execute a test in which digital capturing is not used with the

DIGITAL_CAPTURE_TEST
 API, the execution always results in FAIL.

Before starting test execution, the
DIGITAL_CAPTURE_TEST
 API executes
the
`FLUSH`（raw: `29338.htm`）
 API internally to reflect the changes specified by the following
APIs to the hardware of setup data:

ANALOG

ANALOG_STATUS

PRIMARY_STATUS

TIMING_SPEC / LEVEL_SPEC / SPECIFICATION

ROUTING_STATUS

This API
does not wait until the AWG finishes the
output
.
If an infinite loop sequence (
LOOPI

or
RPTI
) is used for AWG, you can use the

ABORT_TEST
 API to stop the infinite loop of the AWG.

This API does not wait until the Digitizers/Samplers and TIAs finish the measurement. If you
want to wait for them, use the
WAIT_TEST_DONE
 API after this API as
shown
below:

```
:
DIGITAL_CAPTURE_TEST(TM::WAIT_DGT);
:
```

The
NB_DIGITAL_CAPTURE_START
 API waits until the digital sequencer
has completed before returning, while the
NB_DIGITAL_CAPTURE_START();

and
NB_DIGITAL_CAPTURE_END(timeout);
do not. For details, see
`NB_DIGITAL_CAPTURE_START`（raw: `29520.htm`）
 and
`NB_DIGITAL_CAPTURE_END`（raw: `29514.htm`）
.

### Example

### Sequencer context execution without result area
```
string defaultResultAreaId = "";
string contextName = "JTAG_PORT_context"
DIGITAL_CAPTURE_TEST(defaultResultAreaId, contextName);
```

Using
an empty string for the
resultAreaId
, and specify both this and the

context
 parameter allows sequencer context executions without using a result
area.

The
DIGITAL_CAPTURE_TEST
 API starts the test.

<!-- 语法节 end -->

## 是什么

**文档事实** DIGITAL_CAPTURE_TEST 定义在 `/opt/hp93000/soc/prod_com/include/MAPI/Execute.h`，用于执行包含 digital capturing 的测试，启动 digital sequencer 并等待其完成。

**文档事实** 如果用 EXECUTE_TEST 或 START_TEST 执行含 digital capturing 的测试，测试无法执行。反过来，用本 API 执行不含 digital capturing 的测试，结果总是 FAIL。

**文档事实** 执行前本 API 内部调用 FLUSH，把 ANALOG、ANALOG_STATUS、PRIMARY_STATUS、TIMING_SPEC / LEVEL_SPEC / SPECIFICATION、ROUTING_STATUS 指定的 setup 数据改动反映到硬件。

**文档事实** 本 API 不等待 AWG 输出结束，也不等待 Digitizers/Samplers 与 TIA 完成测量。默认等待 TM::WAIT_DIGITAL，默认 timeout 为 360000 s，timeout 与 wait_action 均可由调用者指定。

**文档事实** ROUTING_STATUS 或 ANALOG_STATUS 对模拟模块硬件的改动要被本 API 反映，所有模拟模块中的 sequencer 必须处于 halted 状态。

## 典型用法

**文档事实** 最简单的调用是不带参数或只带等待参数的版本，本 API 会启动测试。需要按硬件类别等待时，可传 TM::WAIT_ALL、TM::WAIT_AWG、TM::WAIT_DGT、TM::WAIT_TIA，并用 `|` 组合，例如 `TM::WAIT_AWG|TM::WAIT_DGT`。

**文档事实** 需要在 Digitizers/Samplers 与 TIA 完成测量后才继续时，在本 API 之后调用 WAIT_TEST_DONE。

**文档事实** 后台处理可用 resultAreaId 指定 RESULT_AREA_CONFIG 定义的结果保留区。sequencer context 执行且不使用结果区时，resultAreaId 传空字符串，并同时传入 context。

**文档事实** context 的端口必须包含在当前 start label 中，且该 start label 必须是 multiport burst。context 必须在固件层用 SQEC 命令定义，或定义为 SEQUENCER_CONTEXT_ITEM 并包含在 SEQUENCER_CONTEXT 中、经该对象的 apply() 在固件层激活。

**文档事实** AWG 使用 LOOPI 或 RPTI 无限循环时，可用 ABORT_TEST 停止该无限循环。

**文档事实** 文档示例用 `string defaultResultAreaId = ""` 与 `string contextName = "JTAG_PORT_context"` 调用 `DIGITAL_CAPTURE_TEST(defaultResultAreaId, contextName)`，以此实现不使用结果区的 sequencer context 执行。

## 和谁有关

- **文档事实** FLUSH，本 API 内部执行 FLUSH，且模拟模块的 ROUTING_STATUS 与 ANALOG_STATUS 改动要求 sequencer halted，文档把 FLUSH 页作为进一步说明。
- **文档事实** EXECUTE_TEST 与 START_TEST，这两者不能执行含 digital capturing 的测试，文档要求改用本 API 或 NB_DIGITAL_CAPTURE_START。
- **文档事实** FUNCTIONAL_TEST，多端口测试中若使用 capture pin，必须用 DIGITAL_CAPTURE_TEST 或 NB_DIGITAL_CAPTURE_START 与 NB_DIGITAL_CAPTURE_END，否则用 FUNCTIONAL_TEST。
- **文档事实** NB_DIGITAL_CAPTURE_START 与 NB_DIGITAL_CAPTURE_END，本页 Important points 把两者列为数字 capture 的另一条执行路径，并对比其等待行为。
- **文档事实** WAIT_TEST_DONE，本 API 不等待 Digitizers/Samplers 与 TIA 完成测量，需用 WAIT_TEST_DONE 补上等待。WAIT_TEST_DONE 页也说明可与本 API 配合。
- **文档事实** ABORT_TEST，用于停止 AWG 的 LOOPI 或 RPTI 无限循环。
- **文档事实** RESULT_AREA_CONFIG，resultAreaId 参数指向的结果保留区由该 API 定义。
- **文档事实** SEQUENCER_CONTEXT 与 SEQUENCER_CONTEXT_ITEM，context 参数的固件层与对象层定义依赖这两者，SEQUENCER_CONTEXT_ITEM 须经 SEQUENCER_CONTEXT 的 apply() 激活。
- **文档事实** VECTOR API，digital capture 设置文档说明执行后用 VECTOR API 取回 captured data。
- **文档事实** PRIMARY_STATUS，由本 API 启动测试时，由 PRIMARY_STATUS 指定的 digital primaries 自动定义为新设置。
- **文档事实** d2s_LABEL_BEGIN，其 d2sExecutionModeType::DIGITAL_CAPTURE_TST 对应 DIGITAL_CAPTURE_TEST()。

## 版本

**文档事实** Functional changes 记载 Introduced before SmarTest 6.3.2。SmarTest 6.5.0 新增参数 resultAreaId。

## 出处

- `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.35_DIGITAL_CAPTURE_TEST.htm`，主源，含定义、参数、Important points、Example 与 Functional changes。
