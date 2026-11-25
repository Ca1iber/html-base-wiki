---
type: object
title: Running a testflow
layer: gui
stage: run
tags: []
related: []
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.03_Running_a_testflow.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Running a testflow

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **2,709 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.03_Running_a_testflow.htm>` 及其子主题 `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.03.04_Measuring_the_test_time.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Measuring the test time）

A simple testflow comprises two test suites, cont and func, in this order. cont
performs a continuity test and func a functional test. Both test suites only ask for a global
PASS/FAIL result. The testflow is executed three times for two sites, resulting in six devices.

When the testflow is not optimized, the output of the debug mode 3 is shown as below.

Observe the following points in the listing:

The
# of measure.
 column in the
TESTFLOW INFORMATION

specifies the number of testflow repetitions. The number of measurements that is specified on
the test suite level in the
seq setup
 and
test suite exec.

rows specifies how often the respective test suites are executed. If the testflow is not
optimized, this number is the number of testflow repetitions
multiplied
 by the number of
sites. The reason for this is that the two sites are processed serially in an unoptimized
testflow, so that the test suite must be called twice in every testflow repetition.

The time spent for executing connect and disconnect sequences is not explicitly specified in
an unoptimized testflow. It is included in the test suite execution time. This is in contrast
to the output for optimized testflows, as explained below. In both optimized and unoptimized
testflows a test suite executes a connect or disconnect sequence only if this is
necessary.

The test suites are ordered as they are defined in the testflow file.

The total time for running the testflow is greater than the sum of all total test suite
times. There are several reasons for this. For example, the testflow can contain nodes which
are not test suites, such as Assign Value nodes.

The second figure displays the results after the testflow has been optimized:

Observe the following points in this listing:

An additional line
set connect
 is specified for the test suite

func
, but not for
cont
. This shows that a connect or
disconnect sequence is executed for
func
, but not for
cont
.
In fact, since the tester is in the DISCONNECTED state at the start of a testflow, and the
continuity test of the first test suite must be executed in the DISCONNECTED state, it is not
necessary to disconnect it again. But the functional test of func must be executed in the
CONNECTED state, and therefore a connect sequence must be executed at the start of the second
test suite.

The benefit of downloading the setup data only once can be seen in the
seq
setup
 line of
cont
. The advantage of executing all sites in parallel
can be seen in the
test suite execution
 lines of both test suites. The
parallel execution of the two sites is also reflected in the number of measurements for the

seq setup
 and
test suite execution
 rows (three instead of
six).

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
