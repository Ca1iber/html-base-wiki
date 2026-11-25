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

**文档事实**：Testflow tool 允许直接运行整个 testflow，或运行其中某个/某些 test suite；文档说明这适用于调试 testflow，以及把新 test suite 集成进 testflow 的过程。

**文档事实**：运行配置在 Run dialog（Run configurations dialog）中设置，从 SmarTest Work Center 的 Run > Run configurations 打开；左侧列表分 Testflow (Full)、Testflow (Selection)、Testflow (User Defined) 三类，右侧设置对应执行配置。

**文档事实**：三类配置的 Loop 区与 Response Emulator 区设置相同；Full 运行整个 testflow，Selection 运行选中的 test suite，User Defined 可新建并运行用户定义 testflow。

**文档事实**：可以把 testflow 或单个 test suite 放入循环，循环在满足指定条件时停止；文档说明该功能用于 test program 调试与开发。

**文档事实**：运行前须确保 testflow 已加载；若要把结果输出到 report window，须在 Flags page 上把 debug_mode testflow flag 设为 off 以外的任意值。

**文档事实**：执行结果在 report window 显示；Flow Sequence Editor 中通过的 test suite 节点为绿色、失败为红色、bypassed 为黄色，Test Suites page 的 Result > Pass/Fail 单元格也会变色。

## 典型用法

**文档事实**：全 testflow：Run > Run configurations → 选 Testflow (Full) → 在右侧配置，必要时在 Loop 区勾选 Enable 并设置 Count 或 Loop Indefinitely → 保持对话框打开并点击 Run。

**文档事实**：Loop 区可设置 Count（限定次数）、Loop Indefinitely（直到 Abort 或 Stop On Fail/Stop On Pass 条件满足）、Stop On Fail、Stop On Pass、Log Loop Number，以及 Pause between loops（毫秒）。Stop On Fail 在到达未设 Overon flag 的 fail bin 时停止；Stop On Pass 要求序列内全部测试通过才停止。

**文档事实**：运行选中 test suite：选 Testflow (Selection)；Site in Focus 勾选时只在 focus site 运行，清除时在所有 active sites 运行；可勾选 Enable 'single step' execution mode 进行调试。

**文档事实**：用户定义 testflow：在 Run dialog 右键 Testflow (User Defined) → New → 输入 Name → 选 current testflow 或 device_directory/testflow 下的其他 testflow → Scope 选 Whole Flow、Testsuite(s) 或 Group(s)（后者可指定执行顺序）。

**文档事实**：Run dialog 关闭时，可在 Flow Sequence Editor 右键 Run Testflow 运行整个当前 testflow，或右键 Run Selected 运行选中的 test suite。

**文档事实**：循环执行时，multi-site 配置仍按每个 loop iteration 在所有 active sites 上执行；testflow variables 与 user flags 不在每次循环结束时重置，只在循环首次启动时重置。

**文档事实**：运行 full testflow 的循环时，每次运行结束都会 disconnect；运行单个 test suite 的循环时不会自动 disconnect，除非 test method 中编程执行 disconnect。

**文档事实**：停止执行可在 Operator Control 窗口点击 ABORT；文档还列出 RESET、ABORT TESTFLOW、PAUSE 的作用，并说明 clean abort looped test 需先 PAUSE 等待执行结束，再 ABORT，最后在 PAUSE 对话框点 Quit。

## 和谁有关

**文档事实**：以下关系均有本页正文、参数说明或回链证据支撑。

- [[test-suites-page]]：本页 Results 段说明执行后 Test Suites page 的 Result > Pass/Fail 单元格会变色；Test Suites page 文档也描述执行结果的边框颜色。
- [[testflow-tool]]：本页属于 Testflow tool 章节，`Using_the_Testflow_Tool` 的回链把 Running a testflow 列为其子主题。
- [[alphabetical-list-of-flags]]、[[flags-page]]：Step 1 要求在 Flags page 设置 debug_mode flag，并链接到 Alphabetical list of flags。
- [[assign-value-node]]：本页 Measuring the test time 指出 testflow 可包含非 test suite 节点，如 Assign Value nodes，因此总时间大于各 test suite 时间之和。
- [[bin]]：Stop On Fail 按 fail bin 停止；文档还说 wide selection 的行为类似运行 testflow 但忽略 binning。
- [[hardware-response-emulator]]：Run dialog 的 Response Emulator 区用于 Response Emulator，文档指向 Preparing/Using hardware response files。
- [[report-window]]：执行结果输出到 report window；Log Loop Number 的消息也输出到 report window。
- [[test-suite]]：Full/Selection/User Defined 三种配置都以 test suite 为选择与循环单位，文档反复使用 test suite 描述执行对象。

## 版本

**文档事实**：本页 Functional changes 记载：

- Introduced before SmarTest 6.3.2——文档集覆盖范围之前已有，是哨兵值，不应理解为 6.3.2 新增。
- SmarTest 6.5.3：running a testflow 的流程发生变化。
- SmarTest 7.1.0：引入用于调试 testflow 的 single step execution mode。
- SmarTest 7.1.2：Stop on Fail 改为序列中任一 test suite 总体 fail 即停止；Stop on Pass 改为序列中全部 test suite 通过才停止。
- SmarTest 7.4.1：Testflow (Full)、Testflow (Selection)、Testflow (User Defined) 新增 Pause between loops 选项，可设置相邻执行之间的等待时间。

**文档事实**：子主题 Loop configuration settings 另记载：SmarTest 6.5.2 用 Run Config window 取代 Looping Configuration Dialog window，并且 testflow/test suite 执行期间不能更改 loop 配置。

## 出处

- 主源（本页「语法 / 参数」与上述事实的主要依据）：`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.03_Running_a_testflow.htm`（正文、Procedures、Results、What to do next、Functional changes）。
- 子主题：`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.03.01_Loop_configuration_settings.htm`（Loop 区参数与 Functional changes）。
- 子主题：`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.03.04_Measuring_the_test_time.htm`（「语法 / 参数」逐字来源）。
- 回链证据：`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02_Using_the_Testflow_Tool.htm`、`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.04.01_Single_step_testflow_debugging.htm`。
