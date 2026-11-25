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

（待补）

## 典型用法

（待补）

## 和谁有关

（待补）

## 版本

（待补）

## 出处

（待补）
