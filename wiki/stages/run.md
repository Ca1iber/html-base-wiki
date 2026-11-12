---
type: stage
title: 运行与调试（Run / Debug）
tags: [run, debug, testflow, site-control, flags, connect, disconnect, sequencer, utility-line, hvm, hardware-response-emulator]
related:
  - "[[project]]"
  - "[[pin]]"
  - "[[level]]"
  - "[[timing]]"
  - "[[pattern]]"
  - "[[testmethod]]"
  - "[[testflow]]"
  - "[[results]]"
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.01.01_Digital_test_setup_flow.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.01.01.04_Task_4__Setting_up_a_Test.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.01.01.05_Task_5__Executing_a_Test_and_Obtaining_the_Results.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.01.01.05.01_Setting_up_flags.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.01.01.05.02_Test_Debugging_and_Data_Logging.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.01.01.06_Task_6__Executing_a_Test_Flow_and_Obtaining_the_Results.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.01.02.05_Task_8_and_9__Executing_a_Test_and_Obtaining_the_Results.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.01.02.06_Task_10_and_11__Executing_a_Testflow_and_Obtaining_the_Results.htm
  - 02_System_reference/02.06_Command_Reference/02.06.08_Relays_and_Control_Commands.htm
  - 02_System_reference/02.06_Command_Reference/02.06.08.01_Concepts_of_relay_control.htm
  - 02_System_reference/02.06_Command_Reference/02.06.08.01.01_Connecting_the_DUT_to_the_test_system_resources.htm
  - 02_System_reference/02.06_Command_Reference/02.06.08.01.02_Disconnecting_the_DUT_from_the_tester_resources.htm
  - 02_System_reference/02.06_Command_Reference/02.06.08.01.03_Control_of_the_Pin_Electronics_Relays_and_the_Relay_Switching_Method.htm
  - 02_System_reference/02.06_Command_Reference/02.06.08.01.04_DPS_Control__User_Defined_Connect___Disconnect.htm
  - 02_System_reference/02.06_Command_Reference/02.06.08.01.04.01_Defining_connect_disconnect_sequences.htm
  - 02_System_reference/02.06_Command_Reference/02.06.12_Utility_Line_Commands.htm
  - 02_System_reference/02.06_Command_Reference/02.06.12.01_Accessing_Utility_Lines.htm
  - 02_System_reference/02.06_Command_Reference/02.06.12.02_List_of_utility_line_commands.htm
  - 02_System_reference/02.06_Command_Reference/02.06.12.02.01_DFUP__DFUP__-__DeFine_Utility_Purpose.htm
  - 02_System_reference/02.06_Command_Reference/02.06.12.02.02_DFUT__DFUT__-__DeFine_UTility_line.htm
  - 02_System_reference/02.06_Command_Reference/02.06.12.02.03_UDUP_-__UnDefine_Utility_Purpose.htm
  - 02_System_reference/02.06_Command_Reference/02.06.12.02.04_UDUT_-__UnDefine_UTility_line.htm
  - 02_System_reference/02.06_Command_Reference/02.06.12.02.05_UPAS__UPAS__-__Utility_Purpose_ASsignment_for_multi-site.htm
  - 02_System_reference/02.06_Command_Reference/02.06.12.02.06_UPOW__UPOW__-__Utility_POWer.htm
  - 02_System_reference/02.06_Command_Reference/02.06.12.02.07_UPST__UPST__-__Utility_Purpose_STate.htm
  - 02_System_reference/02.06_Command_Reference/02.06.12.02.08_UPTI__UPTI__-__Utility_Purpose_settling_TIme.htm
  - 02_System_reference/02.06_Command_Reference/02.06.12.02.09_UTIN__-__UTility_line_INputs.htm
  - 02_System_reference/02.06_Command_Reference/02.06.12.02.10_UTIX__-__UTility_line_Inputs_eXtended.htm
  - 02_System_reference/02.06_Command_Reference/02.06.12.02.11_UTOT__UTOT__-__UTility_line_OuTputs.htm
  - 02_System_reference/02.06_Command_Reference/02.06.12.02.12_UTSC__UTSC__-__UTility_line_Serial_Configuration.htm
  - 02_System_reference/02.06_Command_Reference/02.06.12.02.13_UTST__UTST__-__UTility_line_STate.htm
  - 02_System_reference/02.06_Command_Reference/02.06.12.02.14_UTTI__UTTI__-__UTility_line_settling_TIme.htm
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.206_RLYC__RLYC__-__ReLaY_Control.htm
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.198_PSST__PSST__-__Power_Supply_STatus.htm
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.29_CNCT_-_CoNneCT_disCoNneCT.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.02.30_SQST__SQST__-__SeQuencer_STate.htm
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.77_DLSO__Driver_Level_Switch_Off.htm
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.23_CHRS__CHRS__-__CHeck_Routing_Set_globally.htm
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.124_FLSH_-__FLuSH_buffered_commands.htm
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.341_WSDN_-__Wait_Setup_DoNe.htm
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.07_BCMD__BCMD__-_Binding_CoMmanD.htm
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.191_PSFC__PSFC__-__Parallel_Setup_FoCus.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.05.02_Changing_the_runtime_values_of_base_variables.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.31_SVLR__SVLR__-__Spec_VaLues_at_Runtime.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.30_STRS__-__Spec_TRansition_Search.htm
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.92_DSVS__DSVS__-__Define_Spec_Value_Set.htm
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.12_BSVR__BSVR___Bulk_Set_Value_at_Runtime.htm
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.11_BSVE_-__Bulk_Set_Value_Evaluation.htm
  - 02_System_reference/02.06_Command_Reference/02.06.01.05_Site_dependent_firmware_commands.htm
  - 02_System_reference/02.06_Command_Reference/02.06.01.03_Executing_commands_in_a_shell_window_using_the_hpt_utility.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.27_Site_Control_Window.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.27.01_The_states_of_the_sites.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.27.02_Expanded_Site_Control_window.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.27.03_Changing_the_site_in_focus.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.27.04_Selecting_the_sites_to_run_your_test.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.28_Site_Select_view.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.03_Running_a_testflow.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.03.01_Loop_configuration_settings.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.03.02_Using_the_Overon_feature_while_running_a_testflow.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.03.03_Checking_the_execution_flow.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.03.04_Measuring_the_test_time.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.03.05_Adding_user_defined_testflows_to_the_Run_menu.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.04_Debugging_a_testflow.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.04.01_Single_step_testflow_debugging.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.06_Hardware_Response_Emulator.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.06.01_Preparing_Hardware_Response_files.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.06.02_Using_hardware_response_files_for_execution.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.06.03_Hardware_response_files.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.06.04_Supported_test_suites_and_test_method_APIs.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.04_Multiple_Sites_Execution.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.07_Flags.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.07.02_Testflow_flags.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.07.04_Test_suite_flags.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.07.05_Site_control_flags.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.07.06_Flag_priority.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.01.01_Run__and__Run_and_Branch__test_suites.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.01.02_Special_test_suites.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01.11.01_Narrow_selection_and_wide_selection.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01.14_Identifying_fail_labels_in_a_burst.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.31_Test_Program.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.31.02_Executing_a_Test_Program.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.09_Execution_Input.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.09.01_Selecting_an_Execution_Input.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.07_Controlling_a_Production_Run.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.07.01_Aborting_a_Production_Run.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.07.02_Resetting_a_Production_Run.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.07.03_Aborting_a_Testflow.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.07.04_Pausing_a_Production_Run.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.05.05.01_Executing_a_workorder_from_the_operation_control_panel.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.05.04.01_Connect.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.05.04.02_Disconnect.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.205_SET_ACTIVE_SITES.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.209_SET_ENABLED_SITES.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.79_GET_ACTIVE_SITES.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.86_GET_ENABLED_SITES.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.81_GET_CONFIGURED_SITES.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.132_MS_SITE_SET.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.235_START_TEST.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.65_EXECUTE_TEST.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.271_WAIT_TEST_DONE.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.01_ABORT_TEST.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.217_SET_TESTFLOW_FLAG.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.219_SET_TESTSUITE_FLAG.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14_Test_Suite_Control_API.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01_TestsuiteProxy.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.02_TestsuiteProxy.executeActiveSites.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.03_TestsuiteProxy.executeSiteInFocus.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.21_TestsuiteProxy.isExecuted.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.23_TestsuiteProxy.isPass.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.30_TestsuiteProxy.setSiteMatch.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.33_TestsuiteProxy.setTestsuiteFlag.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.12_setSiteInFocus.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.14_setActiveSites.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.15_getActiveSites.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.10.01_HVM_API_Introduction.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.10.03.02.02_Test_Execution_API.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.10.03.02.02.26_GetLevelProfile.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.09.02_DataManager.htm
  - 02_System_reference/02.15_SmartShell/02.15_SmartShell.htm
  - 03_Use_cases_and_application_papers/03.04_How_to_do_disconnect/03.04.01_Overview_of_various_disconnect_methods.htm
  - 03_Use_cases_and_application_papers/03.09_How_to_set_up_sequencer_controlled_utility_lines/03.09.01.01_Serial_interface_for_sequencer-controlled_utility_lines.htm
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.08.06_Debug_View.htm
created: 2026-11-12
updated: 2026-11-12
verified: doc-only
---

# 运行与调试（Run / Debug）

> 把已经组装好的 testflow 真正跑到机台上：选 site、连 DUT、配 flag、启动/暂停/停止、定位失败点，并把结果留给 [[results]]。

## 目的

**文档事实**：在数字测试的总体走查里，第 5 步由两件事组成，表格原文分别是「Build up a test and then execute the test.」与「Obtain the test results and debug the test.」，对应工具是 Testflow Tool、Error Map Tool、Timing Diagram Tool（`02.08.01.01`）。第 6 步把范围放大到整条 testflow，表格原文是「Make a testflow which consists of complete tests and then execute all tests.」与「Obtain the execution flow and debug the testflow.」，工具仍是 Testflow Tool（`02.08.01.01`）。

**文档事实**：任务级走查把这一步拆成两段（`02.08.01.01.05`、`02.08.01.01.06`）：

- 单 test 级：设置 system/testflow/test suite flag → 执行 test → 用 Testflow Tool、Timing Diagram Tool、Error Map Tool 看 pass/fail 与数字工作状况 → 有 bug 就改后重跑。
- testflow 级：插入 bin、flow control、assign value 等元素 → 最终确定 system/testflow/test suite flag → 执行全部 test → 取得执行流并调试 → 有 bug 就改后重跑。

**文档事实**：ADC 走查（`02.08.01.02`）的 Task 8/9、10/11 与上述结构一一对应，只是结果工具里多一个 Signal Analyzer Tool（`02.08.01.02.05`、`02.08.01.02.06`）。

**文档事实**：Testflow Tool 的定位是：

> The Testflow tool allows you to directly run the entire testflow or one or more individual test suites from it, which is useful when debugging the testflow, or when integrating new test suites into the testflow.

同页 `About this task` 说明还可以把 testflow 或单个 test suite 放在一个循环里跑，直到满足指定条件，用于 test program 调试与开发（`02.08.04.32.02.03`）。

**文档事实**：本阶段包含三种「跑」的粒度：单个 test suite、test suite 选择（含子分支与否）、整条 testflow；以及一种 test program 粒度：在 Test Program Editor 里右键 `Test Program` → `Run`，或从 Operation Control 执行 workorder（`02.08.04.31.02`、`02.09.01.05.05.01`）。

**推断**：本阶段的边界是「让 test 在机台上执行并观察执行过程」。结果本身的记录配置、读取与归档归 [[results]]；testflow 的组装归 [[testflow]]；test suite 与 test method 的绑定归 [[testmethod]]。本页把 Error Map Tool / Timing Diagram Tool 只当作调试入口列出，不展开其查询语法。

**建议**：先用单选/宽选跑一个小范围、确认 flags 与连线，再跑整条 testflow；本阶段最贵的错误是「连接序列被打断」和「在错误 site 上判读结果」，两者都不会报错，只会给错数据。这是建议，不是文档要求。

## 前置条件

1. **testflow 已加载。** **文档事实**：`02.08.04.32.02.03` 的 `Before you begin` 只有一句「Make sure the testflow has been loaded.」；Overon 与部分调试页同样以此为前置（`02.08.04.32.02.03.02`）。
2. **testflow 已组装完成。** **文档事实**：插入 bin、flow control、assign value 等元素属于第 6 步的前半（`02.08.01.01.06`）；test suite、primary set 与 vector label 的指定属于第 4 步（`02.08.01.01.04`）。组装本身见 [[testflow]]。
3. **primary sets 与 testflow 已定义。** **文档事实**：`02.08.04.27.04` 的 `Before you begin` 写「Make sure that primary sets and the testflow have been defined.」primary set 的定义见 [[timing]] / [[level]]。
4. **三类 flag 已按测试目的设好。** **文档事实**：testflow flags 主要帮助调试 testflow；system flags 控制整个 test program 的执行；test suite flags 控制 test suite 的输出，并直接影响 test suite 如何执行（`02.08.01.01.05.01`）。test suite flags 默认全部 inactive；只勾必要的 flag，因为要采集的结果会显著影响执行时间（`02.08.04.32.01.02.07.04`）。
5. **要输出到 report window 时，`debug_mode` 不能是 off。** **文档事实**：`02.08.04.32.02.03` 的 Step 1 要求在 Flags page 上把 `debug_mode` testflow flag 设为 off 以外的任何值。
6. **运行前要确认每个 site 可用。** **文档事实**：`02.08.04.27.03` 的 `Before you begin` 写「Make sure that each site is available (the setup files for each site are correct).」不可用的 site（例如 pin configuration 有缺陷）不能被 enable、activate 或取得 result focus（`02.08.04.27.01`）。
7. **连接前要确认 break vector 与 format 不与 DUT 冲突。** **文档事实**：`02.06.08.01.01` 的 CAUTION 写：

   > Ensure that the break vector and the format setting do not conflict with the DUT requirements. Particular attention must be given to IO pins to avoid driving into an active output.

8. **不要在 firmware 层把 sequencer 从 OFF 改到 BREAK 后再调用 Connect test method。** **文档事实**：`02.07.05.04.01` 的 `Dependencies` 写「Avoid changing the sequencer state from OFF to BREAK at the firmware command level and subsequently making a call to the connect test method, as this will result in hot switching the AC relays.」
9. **用户自定义 connect/disconnect 序列要有文件，且只在启动或 device change 时读取。** **文档事实**：两个命令文件必须放在被测 device 的 `testfunc` 目录，名字固定为 `connect.user_def` 与 `disconnect.user_def`（`02.06.08.01.04`）。为保持吞吐率，文件只在软件启动或 device change 时读取，运行中编辑可能不生效；shared multisite 不支持该功能（`02.06.08.01.04.01`）。另外，**启动时 SmarTest 总会先做一次标准 disconnect**（`02.06.08.01.04.01`、`03.04.01`）。
10. **用 Hardware Response Emulator 前要准备好硬件响应文件。** **文档事实**：`02.08.04.32.02.06.02` 的 `Before you begin` 要求为 testflow 里所有 test suite 与取数 test method API 准备好 hardware response files；准备方法是用 Store 模式跑一次（`02.08.04.32.02.06.01`）。前提还包括「Connected to a test system」与「Required SmarTest version」（`02.08.04.32.02.06.01`）。
11. **单步调试要先在 Run dialog 打开单步模式。** **文档事实**：`02.08.04.32.02.04.01` 的 `Prerequisites` 写「Enable single step testflow execution, see Step 2 in Running a testflow.」
12. **运行期改 spec 值只能在范围内、且不能与 `LEVEL_SPEC` / `TIMING_SPEC` 混用。** **文档事实**：`SVLR` 的值必须在 spec set 给定的 min/max 内，改动在下一次 functional test 开始时生效，且不改 setup 值（`02.06.06.02.31`）。同页 CAUTION 要求不要把 `LEVEL_SPEC` / `TIMING_SPEC` API 与 firmware 改值命令混用，除调试目的外。

## 涉及对象

### GUI / 工具

| 对象 | 层级 | 在本阶段做什么 | 出处 |
|---|---|---|---|
| `Testflow Tool` | gui | 打开 testflow、设置 Run 配置、执行整条 testflow 或选中的 test suite；承载 Flow Sequence Editor 与 Flow Data Editor | `02.08.04.32.02.03` |
| `Flow Sequence Editor` | gui | 右键 `Run Testflow` / `Run Selected`；执行后节点按 pass/fail/bypass 变色 | `02.08.04.32.02.03` |
| `Run dialog`（Run Configurations） | gui | 选 `Testflow (Full)` / `Testflow (Selection)` / `Testflow (User Defined)`，配 loop、Response Emulator、Site in Focus、单步模式 | `02.08.04.32.02.03`、`02.08.04.32.02.03.01` |
| `Debug view` | gui | 显示执行树，提供 Restart / Resume / Suspend / Terminate / Step Over | `01.01.08.06`、`02.08.04.32.02.04.01` |
| `Site Control Window` | gui | 设置每个 site 的 Enable / Active / Focus；`93000 > System > Site Control` 打开 | `02.08.04.27`、`02.08.04.27.01` |
| `Expanded Site Control window` | gui | 按 test suite 查看/修改 site test sequence、Parallel/Serial/Semi-Parallel 模式、Size/Cycle | `02.08.04.27.02` |
| `Site Select view` | gui | 批量选 site 状态、按结果筛 site、看每个 site 的 Result/Soft/Hard/Pass#/Fail#/Yield%；可导入导出 CSV | `02.08.04.28` |
| `Operation Control window` | gui | 执行期间提供 ABORT / RESET / ABORT TESTFLOW / PAUSE 四个按钮；也提供 Execute Workorder 入口 | `02.09.01.07`、`02.09.01.05.05.01` |
| `Error Map Tool` | gui | 调试数字失败的入口之一；本页只用作出入口，细节见 [[results]] | `02.08.01.01.05` |
| `Timing Diagram Tool` | gui | 看实际驱动/接收波形，定位与期望不符的点；细节见 [[results]] | `02.08.01.01.05` |
| `Pattern Tool` | gui | 调试数字 test 时查看 pattern/vector 的入口（`02.08.01.01.05.02` 点名） | `02.08.01.01.05.02` |
| `Signal Analyzer Tool` | gui | ADC 走查中显示捕获的模拟波形 | `02.08.01.02.05` |
| `Test Method Debugger` | gui | 调试 test method 程序：看源码、设断点、看/改变量、走调用栈；使用时要打开 `Set breakpoint` test suite flag | `02.08.01.01.05.02` |
| `Hardware Response Emulator (HWRE)` | gui / tool | 在离线或联机调试中按准备好的 hardware response file 返回数据与 pass/fail；有 Import / Store 两种模式 | `02.08.04.32.02.06` |
| `hpt` | tool | 在 shell 里直接执行 firmware command，文档明确「useful especially when debugging testflow programs」 | `02.06.01.03` |

### 概念

**文档事实（断连方式的选择，`03.04.01`）**：SmarTest 提供四种断连方式——标准 disconnect 序列（内置；若未被用户序列替代，在每个 stop bin 对失败 site 或剩余 pass site 执行；stop bin 上只对非 shared pin 执行，除非所有 site 都已 bin）、用户自定义 disconnect 序列（只覆盖 stop bin，且不区分 shared / non-shared pin）、特殊 test suite `bin_disconnect`（需配合 test method 里的 conditional disconnect）、`Multibin SmartDisconnect`（multibin 节点 + user defined test suite 的组合，文档推荐新程序使用）。共同的语义是：在 run-and-branch 的 fail 分支只对失败 site 执行，在 pass 分支对剩余 site 执行（`03.04.01`）。

| 对象 | 层级 | 在本阶段做什么 | 出处 |
|---|---|---|---|
| `site state`（Enable / Active / Focus） | concept | Enable 决定连接序列是否连该 site；Active 决定 testflow 是否为该 site 执行并处理错误；Focus 决定结果与 firmware 查询显示哪个 site | `02.08.04.27.01` |
| `site test sequence` | concept | 决定多 site 的执行顺序；可由 Size/Cycle 自动生成或手工填序号 | `02.08.04.27.02` |
| `site control mode`（Parallel / Serial / Semi-Parallel） | concept | Expanded Site Control window 里的三种模式；`allow parallel` flag 必须先打开才能选 Parallel / Semi-Parallel | `02.08.04.27.02` |
| `narrow / wide selection` | concept | 窄选只选节点本身，宽选连同子分支；宽选行为像跑整条 testflow，但忽略 binning；调试时要用宽选才能得到一致的 PASS/FAIL 显示 | `02.08.04.32.02.01.11.01` |
| `Run` / `Run and Branch` test suite | concept | 两种 testflow 节点；选哪种节点决定该 test suite 的 pass/fail 结果是否决定后续流向 | `02.08.04.32.01.02.01.01` |
| `special test suite`（Init / Download / Abort / Reset / Pause / Exit / bin_disconnect / multi_bin_decision） | concept | 在 testflow 的特定时点执行，不显示为 Flow Sequence Editor 节点；Abort/Reset/Pause/Exit 对应 Operation Control 的状态。**文档正文写「seven types」，但同页表格列了 8 行（含 Download）——原文如此** | `02.08.04.32.01.02.01.02` |
| `Overon` | concept | 让 testflow 越过 stop bin 继续执行，用于开发 testflow | `02.08.04.32.02.03.02` |
| `testflow loop` | concept | Count / Loop Indefinitely / Stop on Fail / Stop on Pass / Log Loop Number / Pause between loops | `02.08.04.32.02.03.01` |
| `testflow flag` | concept | 按 testflow 存的调试/执行控制 flag，存于 testflow 文件 `flags` 段 | `02.08.04.32.01.02.07.02` |
| `test suite flag` | concept | 按 test suite 存，控制采集哪些结果与如何执行；存于 testflow 文件 `test_suites` 段 | `02.08.04.32.01.02.07.04` |
| `site control flag` | concept | 按 test suite 存，控制 focus、并行/串行、Site Match；存于 `test_suites` 段 | `02.08.04.32.01.02.07.05` |
| `flag priority` | concept | pass level 与 fail level 冲突时 pass level 优先；单个 test suite 的 Set pass / Set fail / Bypass 优先于全局 testflow flags | `02.08.04.32.01.02.07.06` |
| `burst` | concept | 一次执行一串 label；失败时要定位是哪个 label，可用 `unburst_mode` 或 for loop + `burstfirst()` / `burstnext()` | `02.08.04.32.02.01.14` |
| `Execution Input` | concept | 生产流程在运行期送入的数据接口（如 ID 与其他运行期才有的编号） | `02.08.04.09` |
| `test program` | concept | testflow 与 test environment definition 的组合；至少要有 testflow 与 application file | `02.08.04.31` |

### 文件

| 对象 | 层级 | 在本阶段做什么 | 出处 |
|---|---|---|---|
| `connect.user_def` / `disconnect.user_def` | file | 用户自定义 connect/disconnect 序列的 firmware command 文件，放在 `<device>/testfunc` | `02.06.08.01.04` |
| `hardware response file` | file | HWRE 的输入/输出；文件名由 `Testsuite;MAPI; call#; site#` 决定 | `02.08.04.32.02.06.03` |
| `Site Control CSV` | file | Site Select view 导出/导入 site 状态、执行结果与汇总 | `02.08.04.28` |
| `testflow file` | file | 本阶段的输入；其 `flags` / `test_suites` 段存放三类 flag | `02.08.04.32.01.02.07.02`、`02.08.04.32.01.02.07.04` |

### L1 / L2 / L3 边界对象

| 对象 | 层级 | 在本阶段做什么 | 出处 |
|---|---|---|---|
| `RLYC` / `PSST` / `CNCT` / `SQST` / `DLSO` / `CHRS` / `FLSH` / `WSDN` / `BCMD` | L1 | 标准与用户自定义 connect/disconnect 序列的组成命令（详见 L1 甲族） | `02.06.08.01.04.01` |
| `DFUP` / `DFUT` / `UDUP` / `UDUT` / `UPAS` / `UPOW` / `UPST` / `UPTI` / `UTIN?` / `UTIX?` / `UTOT` / `UTSC` / `UTST` / `UTTI` | L1 | utility line 的定义、激活、读取与 settling time（详见 L1 乙族） | `02.06.12.02` |
| `SVLR` / `DSVS` / `BSVR` / `BSVE` / `STRS?` | L1 | 运行期修改 timing/level spec 值并重算方程（详见 L1 丙族） | `02.06.06.01.05.02`、`02.06.06.02.31`、`02.06.06.02.30` |
| `PSFC` | L1（边界） | 把 setup 改动限制到部分 site；RLYC 的多 site 安全用法会先 `PSFC` 到 enabled sites | `02.06.02.02.191`、`02.06.02.02.206` |
| `FTST?` / `SQSL` / `SQGB` / `SQTO` / `FTSM` | L1（边界） | 执行与终止配置；在 [[pattern]] / [[results]] 已逐条展开 | `02.06.11.02.25`、`02.06.07.02`、`02.06.11.02.31` |
| `SPRM` / `APRM` | L1（边界） | primary set 的指定与激活；配置语义归 [[timing]] | `02.06.06.02.28`、`02.06.06.02.01` |
| `Connect` / `Disconnect` | L2 | UTM 里的 connect/disconnect test method，做与标准序列同类的事：继电器、DPS 上下电、sequencer 状态 | `02.07.05.04.01`、`02.07.05.04.02` |
| `SET_ACTIVE_SITES` / `GET_ACTIVE_SITES` / `SET_ENABLED_SITES` / `GET_ENABLED_SITES` / `GET_CONFIGURED_SITES` | L2 | 在 test method 内读写 site 状态 | `02.07.04.01.205`、`.209`、`.79`、`.86`、`.81` |
| `MS_SITE_SET` | L2 | site 状态数组类型，索引 1 起，`[0]` 被忽略 | `02.07.04.01.132` |
| `START_TEST` / `EXECUTE_TEST` / `WAIT_TEST_DONE` / `ABORT_TEST` | L2 | 启动/等待/中止 sequencer 与模拟 sequencer | `02.07.04.01.235`、`.65`、`.271`、`.01` |
| `SET_TESTFLOW_FLAG` / `SET_TESTSUITE_FLAG` | L2 | 在 test method 内改 flag | `02.07.04.01.217`、`.219` |
| `TestsuiteProxy` | L3 | 在 testflow 之外执行 test suite、取每 site 结果、设 flag 与 Site Match | `02.09.01.14.02.01` |
| `setActiveSites` / `setSiteInFocus` / `executeActiveSites` / `executeSiteInFocus` | L3 | Test suite control API 的 site 与执行入口 | `02.09.01.14.02.14`、`.12`、`02.09.01.14.02.01.02`、`.03` |
| `HVM Test Execution API` | L3 | 外部程序启停 testflow/test program、查询执行状态、接收执行事件 | `02.09.01.10.03.02.02` |
| `DataManager`（`dm_testflow`） | L3 | 按文件类型操作 testflow 文件 | `02.09.01.09.02` |
| `SmartShell` | L3 | 在 7.10.3 **不存在**：该章 `Functional changes` 写 `Introduced in SmarTest 8.2.5`，正文只有 PDF 外链 | `02.15` |

### 归属判定

这一节是判断，不是文档事实，供维护者复核。

- **本阶段没有独占的 `02.06.xx` 命令章。** `02.06.08`「Relays and Control Commands」整章 7 篇，全是概念页（1 篇章索引 + `02.06.08.01` 与 4 个叶子 + `.01.04.01`），**没有一条命令定义**；它规定的 connect/disconnect 序列里的命令全部定义在 `02.06.02.02` 字母序命令章。因此 L1 只能按「该章点名的命令」建族，不能按「子树 = 整章」数条数。
- **`02.06.06.01.05.*` 不判给本页。** 它是 timing specification 子树（`Defining the timing specification` 及其 4 个子页），归 [[timing]]；其中只有 `02.06.06.01.05.02`「Changing the runtime values of base variables」讲的是运行期行为，而它点名的命令（`SVLR` / `DSVS` / `BSVR` / `BSVE`）不在本子树内。本页只收这几条**运行期改值命令**，不收整个 `02.06.06.01.05` 子树。
- **`SVLR` / `STRS?` 与 [[timing]] 的边界**：[[timing]] 页已把二者判给本阶段的「运行时调整」，同时在它自己的 L1 表里保留了配置语义。本页按同一判定收 `SVLR` / `SVLR?` / `STRS?`，并补上 `DSVS` / `BSVR` / `BSVE` 这条「先赋值、后一次重算」的路径（`02.06.06.01.05.02`）；timing 页未列这三条。
- **`02.06.12.02` 整族判给本页**，理由是它控制的是执行期间的外部设备（relay、solenoid、indicator），并且与 connect/disconnect 序列共用 `FLSH` / `WSDN`（`02.06.12.01`、`02.06.08.01.04.01`）。但其中 `DFUP` / `DFUT` / `UDUP` / `UDUT` 是**定义侧**命令，语义上同时属于 pin configuration / routing（`DFUP` 与 `UDUT` 的 `Application` 分别指回 `02.06.03`），本页仍逐条列出，避免整族留洞。
- **`FTST?` / `SQSL` / `SQGB` / `SQTO` / `FTSM` 判给 [[pattern]] / [[results]]，不重复展开。** 它们是真正的「执行」命令，但文档把 `FTST?` 编在 Test Result Commands（`02.06.11.02.25`），把 `SQSL` / `SQGB` / `SQTO` / `FTSM` 编在 Vector Setup Commands（`02.06.07.02`）。本页只在 L1 边界列出名字、作用与出处，不计入本页覆盖数。
- **`PSFC` 判给「横切」**：它既不是本阶段专有，也不只服务本阶段；但 RLYC 的多 site 安全用法明确要求在 `RLYC` 前先 `PSFC` 到 enabled sites（`02.06.02.02.206`）。本页把它列为边界对象，不单独建族。
- **GUI 侧 `Site Control Window` 与 `Site Select view` 都判给本页**：前者是逐 site 勾选，后者是批量管理与按结果筛选（`02.08.04.27`、`02.08.04.28`）。`Expanded Site Control window` 属于前者的一部分。
- **`02.08.04.31` Test Program 判给本页**：它描述如何把整条 test program 跑起来（右键 `Test Program` → `Run`），与 testflow 级执行同层，但不属于 testflow 组装。`02.08.04.31.01`（创建/保存 test program）不属于本阶段，未列。
- **`02.08.04.09` Execution Input 判给本页**：它是运行期数据接口，不是 setup 编辑功能。
- **结果工具（Error Map / Timing Diagram / Signal Analyzer / Integrated Result）判给 [[results]]**：本页只保留「调试时该打开哪个工具」的入口，不写其查询语法与数据格式，避免与 [[results]] 重复。
- **SmartShell 不作为可用的 L3 接口**：`02.15` 的 `Functional changes` 写 `Introduced in SmarTest 8.2.5`，本 wiki 面向 7.10.3；该章正文只有 SmartShell 7 的 PDF 外链（`02.15`）。

### 文档覆盖（章结构 + 叶子篇名 + 分类号）

| 章 | 叶子 | 一句话 |
|---|---|---|
| `02.08.01.01` Digital test setup flow | `.01`–`.06` | 6 个 Task 的总走查；第 5/6 步是本阶段（`.05` 单 test、`.06` testflow） |
| `02.08.01.01.05` Task 5 | `.05.01` Setting up flags、`.05.02` Test Debugging and Data Logging | flag 三类分工；调试工具与 Test Method Debugger |
| `02.08.01.02` ADC test setup flow | `.02.05` Task 8 and 9、`.02.06` Task 10 and 11 | 同构的 ADC 版执行/调试走查 |
| `02.06.08` Relays and Control Commands | `.01` Concepts of relay control、`.01.01` Connecting the DUT、`.01.02` Disconnecting the DUT、`.01.03` Control of the Pin Electronics Relays、`.01.04` DPS Control、`.01.04.01` Defining connect/disconnect sequences | 连接/断开与 relay 控制；无命令叶子 |
| `02.06.12` Utility Line Commands | `.01` Accessing Utility Lines、`.02` List of utility line commands（14 条） | utility line 的低层/高层访问、缓冲与 settling time |
| `02.08.04.27` Site Control Window | `.01` The states of the sites、`.02` Expanded Site Control window、`.03` Changing the site in focus、`.04` Selecting the sites to run your test | site 三态、执行顺序、focus 与选 site |
| `02.08.04.28` Site Select view | — | 单页；批量 site 状态、结果导航/排序/过滤、CSV 导入导出 |
| `02.08.04.32.02.03` Running a testflow | `.01` Loop configuration、`.02` Overon、`.03` Checking the execution flow、`.04` Measuring the test time、`.05` Adding user defined testflows to the Run menu | 执行主流程、循环、路径统计、test time 测量、Run 菜单 |
| `02.08.04.32.02.04` Debugging a testflow | `.01` Single step testflow debugging | Debug view 的 Suspend/Step Over/Resume/Terminate 与限制 |
| `02.08.04.32.02.06` Hardware Response Emulator | `.01` Preparing Hardware Response files、`.02` Using hardware response files for execution、`.03` Hardware response files、`.04` Supported test suites and test method APIs；`.01` 下 6 个类型子页：`.01.01` ARRAY_X type、`.01.02` DOUBLE type、`.01.03` SpecSearch type、`.01.04` DC API type、`.01.05` FW_TASK type、`.01.06` Pass/Fail type and ERROR_MAP type | 离线/联机调试的假数据机制 |
| `02.08.04.32.01.02.07` Flags | `.01` Alphabetical list of flags、`.02` Testflow flags、`.03` Testflow flags for data logging、`.04` Test suite flags、`.05` Site control flags、`.06` Flag priority | 四类 flag 的完整清单与优先级 |
| `02.08.04.32.01.04` Multiple Sites Execution | — | 多 site 到达/离开 test suite 的同步语义；分支先跑 false 路径 |
| `02.08.04.32.01.02.01.01` Run / Run and Branch test suites | — | 两种节点对 pass/fail 的使用方式 |
| `02.08.04.32.01.02.01.02` Special test suites | — | 8 种特殊 test suite 的触发时点 |
| `02.08.04.32.01.02.01.04` Multibin SmartDisconnect test suite | `.04.01` Inserting a Multibin SmartDisconnect test suite | multibin 节点 + user defined test suite 的组合，文档推荐新程序使用 |
| `02.08.04.32.02.01.11.01` Narrow / wide selection | — | 两种选择的语义与调试要求 |
| `02.08.04.32.02.01.14` Identifying fail labels in a burst | — | `unburst_mode` 与 for loop + `burstfirst()` / `burstnext()` 两种定位法 |
| `02.08.04.31` Test Program | `.02` Executing a Test Program | 整条 test program 的执行入口 |
| `02.08.04.09` Execution Input | `.01` Selecting an Execution Input | 运行期数据接口的加载 |
| `02.09.01.07` Controlling a Production Run | `.01` Aborting、`.02` Resetting、`.03` Aborting a Testflow、`.04` Pausing、`.04.01` Using the Form Dialog Screen | Operation Control 四个按钮的语义；pause 时 wafer_auto 模型弹出 Form Dialog |
| `03.04` How to do disconnect | `.01` Overview、`.01.01` Comparing、`.01.02` Standard、`.01.03` User-defined、`.01.03.01` Effects、`.01.03.02` Conditional final disconnect、`.01.04` bin_disconnect、`.01.04.01` bin_disconnect 实现、`.01.05` Multibin SmartDisconnect、`.02` Avoiding pass/fail site dependency、`.02.01` 描述、`.02.02` Workarounds | 断连方式的取舍；stop bin 与共享 pin 的 site 依赖 |
| `02.06.01.05` Site dependent firmware commands | —（一张 119 行的命令表） | 哪些命令受 site focus 影响（命令侧 / 查询侧两列） |
| `02.06.01.03` hpt utility | `.01`–`.06` | shell 里执行 firmware command，调试 testflow 用 |

## L1 — Firmware / Setup Command

**覆盖范围（本次判定）**：本阶段没有 `02.06.xx` 独占命令章（理由见「归属判定」）。本页把本阶段实际使用的 runtime/control 命令按三族收全，共 **28 条**：

- 甲族：connect/disconnect 与 tester 状态，**9 条**（`02.06.08` 点名，语法在 `02.06.02.02`）；
- 乙族：utility line 控制，**14 条**（`02.06.12.02`）；
- 丙族：运行期 spec 值修改，**5 条**（`02.06.06.01.05.02` 与 `02.06.06.02` 点名）。

另有 8 条执行入口 / 横切命令（`FTST?` / `SQSL` / `SQGB` / `SQTO` / `FTSM` / `SPRM` / `APRM` / `PSFC`）列在 `### 丁、边界命令` 中，多数已在别的 stage 页覆盖，**不计入 28 条**。

### 甲、Connect / Disconnect 与 tester 状态（9 条）

| 命令 | 一句作用 | 出处 |
|---|---|---|
| `RLYC` / `RLYC?` | 控制把 DUT pin 连到各种 tester 资源的 relay 位置；查询返回现有 relay 设置。多 site 下可能影响已 bin 的 site，文档有 CAUTION。 | `02.06.02.02.206` |
| `PSST` / `PSST?` | 对指定 pin 打开/关闭 DPS；`Application` 明确写用于 connect and disconnect the test system。 | `02.06.02.02.198` |
| `CNCT` | 按卡类型连接/断开指定模块的全部输出 pin；PPS 卡上断开该模块所有 PPS core 的输出。 | `02.06.02.02.29` |
| `SQST` / `SQST?` | 控制 sequencer 集合状态：`OFF`（sequencer 与 clock 都关，全部 pin 高阻）、`HALT`（clock 关，driver 保持最后电平）、`BRK`（clock 开，施加 break vector）、`RUN`、`ABRT`（需指定 execution context）、`CBRK`。不能从 `HALT` 直接到 `OFF` 或反之，必须先经 `BRK`。connect 序列的最后一步是 `SQST BRK`，disconnect 序列里要把它设回 `SQST OFF`。 | `02.06.07.02.30` |
| `DLSO` | 对 setup focus 内的 site 激活 level set 0，默认效果是把通道切到高阻；文档说明可在 `RLYC` 关 AC relay 前用它避免 hot switching。 | `02.06.02.02.77` |
| `CHRS` / `CHRS?` | 控制 SmarTest 对不一致 routing 请求的行为：`OFF` 尽量满足（默认），`ON` 直接报错并保持原 routing 状态。 | `02.06.02.02.23` |
| `FLSH` | 把 `UPST` / `UPTI` / `UTST` / `UTTI` 缓冲在 MCD 里的 utility line 设置并行下载到硬件。`MUX` 参数只供系统生成的 testflow 断连序列使用，**不要**在用户 procedure 或 hpt 里用。 | `02.06.02.02.124` |
| `WSDN` | 等待 `FLSH` 触发的 analog set / routing 下载完成；`FLSH` 没在跑时立即返回。 | `02.06.02.02.341` |
| `BCMD` / `BCMD?` | 对 binding instance 做 `Set` / `Reset` / `Action`（运行期属性）；标准 disconnect 序列里有 `BCMD "",ACTION,"Update",`。 | `02.06.02.02.07` |

**文档事实**：标准 connect 序列（`02.06.08.01.04.01`）：

```
RLYC CNCT,OFF,(@)
PSST ON
CNCT ON,(@)
SQST BRK
```

**文档事实**：标准 disconnect 序列（`02.06.08.01.04.01`）：

```
DLSO (@)
CHRS OFF
FLSH MUX
WSDN
SQST OFF
CNCT OFF,(@)
BCMD "",ACTION,"Update",
PSST OFF
RLYC IDLE,OFF,(@)
```

**文档事实**：用户自定义 connect 序列可以按 DPS 分组上电（`02.06.08.01.04.01`）：

```
RLYC CNCT,OFF,(@)
PSST ON,(pinlist for DPS1)
PSST ON,(pinlist for DPS2)
CNCT ON,(@)
SQST BRK
```

**文档事实**：自定义 disconnect 序列把 `PSST OFF` 按相反顺序拆成两组（`02.06.08.01.04.01`）：

```
SQST OFF
CNCT OFF,(@)
CHRS OFF
FLSH MUX
WSDN
PSST OFF,(pinlist for DPS2)
PSST OFF,(pinlist for DPS1)
RLYC IDLE,OFF,(@)
```

**文档事实**：connect 的物理顺序与理由（`02.06.08.01.01`）：

> In order to avoid hot switching of the relays, the connect sequence starts from the sequencer OFF state. Then the AC relay (connection to the pin electronics) is closed and subsequently the DPS is powered up. The sequencer is then set to the break state.

同页说明：sequencer 在 OFF 时全部 pin 进入 High-Z；设到 break 后 pin electronics 变 active 并施加 break vector，DUT 输入 pin 上的实际信号由 break vector 与 timing setup 定义的 signal format 共同决定（`02.06.08.01.01`）。disconnect 用同一组命令、相反顺序（`02.06.08.01.02`）。

**文档事实**：`02.06.08.01.03` 说明 Smart Scale 每个 channel 有 AC relay 与 PPMU relay；AC relay 把 DUT pin 连到 `DFPN` 定义的 channel，要收发 vector 必须闭合。同页 Note 写「The HPPMU is not supported with SmarTest 7.10.」

### 乙、Utility line 控制（14 条，`02.06.12.02`）

| 命令 | 一句作用 | 出处 |
|---|---|---|
| `DFUP` / `DFUP?` | 定义一组 utility line（utility purpose）并给每个 channel 赋标准输出状态；标准设置要用 `UPST` + `FLSH` 激活。 | `02.06.12.02.01` |
| `DFUT` / `DFUT?` | 给单条 utility line 定义符号名与操作模式；定义可被 `UTST` 用来设置或读取状态。 | `02.06.12.02.02` |
| `UDUP` | 删除一个或多个已定义的 utility purpose 名；`@` 删除全部。 | `02.06.12.02.03` |
| `UDUT` | 删除已定义的 utility line 名，并把 write line 的输出置 0（low）；`@` 删除全部。 | `02.06.12.02.04` |
| `UPAS` / `UPAS?` | 给 site > 1 的同一个 utility purpose 赋不同的标准输出状态；激活要先用 `PSFC` 限定到该 site，再 `UPST` + `FLSH`。 | `02.06.12.02.05` |
| `UPOW` / `UPOW?` | 开关 utility 电源（可选 Utility Card 或 internal utility power supplies）；文档 Note 要求 `UPOW ON` 在 test-flow 执行中只发一次。 | `02.06.12.02.06` |
| `UPST` / `UPST?` | 设置 utility purpose 内各 line 的输出（期望）状态；必须再用 `FLSH` 才下载到硬件。 | `02.06.12.02.07` |
| `UPTI` / `UPTI?` | 设置某个 utility purpose 的 settling time；`WSDN` 后按它等待，默认 0 ms。 | `02.06.12.02.08` |
| `UTIN?` | 读 7 条 utility input line `URW06 … URW00` 的当前状态；为 F330 兼容保留。 | `02.06.12.02.09` |
| `UTIX?` | 读 utility line 的当前状态（扩展形式）；所有 utility line 都有读写能力。 | `02.06.12.02.10` |
| `UTOT` / `UTOT?` | 低层设置整块 utility line 的状态；立即下载到硬件，不缓冲。输出为 open collector，编程 0 = high（高阻），1 = low。 | `02.06.12.02.11` |
| `UTSC` / `UTSC?` | 通过串行接口控制 utility line，并可把多个 utility block gang 到一个 master block 上；只在该系统提供 dynamic access utility lines 时可用。 | `02.06.12.02.12` |
| `UTST` / `UTST?` | 设置/读取单条 utility line 的输出（`w`）或输入（`r`）状态；需 `FLSH` 激活，`UTST?` 可同时给输出与输入状态。 | `02.06.12.02.13` |
| `UTTI` / `UTTI?` | 设置单条 utility line 的 settling time；`WSDN` 后按最长的那条等待，默认 0 ms。 | `02.06.12.02.14` |

**文档事实**：高低层分工（`02.06.12.01`）：

> In contrast to UTOT, UTST and UPST do not download their settings directly to the hardware. They only define the data to be downloaded. The actual activation must be done with the FLSH command.

**文档事实**：`DFUP` 的最小示例（`02.06.12.02.01`）：

```
> DFUP (16501,16502,16503,16504),"0110",(AWG_CNCT)
> UPST ,(AWG_CNCT)
> FLSH
> UPST? (AWG_CNCT)
< UPST "0110",(AWG_CNCT)
```

**文档事实**：`UTST` 的最小示例（`02.06.12.02.13`）：

```
UTST 1,(Filt1,Filt2)
UTST 0,(Filt3,Filt4)
FLSH
WSDN
UTST? w,(Filt1,Filt2,Filt3,Filt4)
```

**文档事实**：文档说 utility line 也可由 sequencer 控制，那是另一套机制（串行接口、ganging、SmarTest 7 依赖）；本页不展开，入口是 `03.09.01.*`（`03.09.01.01`）。

### 丙、运行期 spec 值修改（5 条）

| 命令 | 一句作用 | 出处 |
|---|---|---|
| `SVLR` / `SVLR?` | 把一个 base（spec）变量设为给定值并重算 timing 或 level；新值在下一次 functional test 开始时生效，setup 值不变；下一次修改会先把上一次的改动复位。 | `02.06.06.02.31` |
| `DSVS` / `DSVS?` | 定义 spec value set，把一组 base 变量赋值的动作打包，使方程系统只需重算一次。 | `02.06.02.02.92` |
| `BSVR` / `BSVR?` | 在 spec value set 内给某个 base 变量赋值。 | `02.06.02.02.12` |
| `BSVE` | 用指定 spec value set 的值重算方程系统；前置是 `DSVS` 已定义、`BSVR` 已赋值。 | `02.06.02.02.11` |
| `STRS?` | 循环重复 functional test，在给定区间内系统性地改一个 timing/level spec 变量，找出 PASS/FAIL 翻转点。 | `02.06.06.02.30` |

**文档事实**：`SVLR` 示例（`02.06.06.02.31`）：

```
> SVLR? TIM,ALL,ALL,"f"
< SVLR TIM,,"spec_p_1_p_2","f@p_1",35
< SVLR TIM,,"spec_p_1_p_2","f@p_2",33
< SVLR TIM,1,1,"f",37
```

**文档事实**：一次重算多条变量的完整路径（`02.06.06.01.05.02`）：

```
> SVLR? TIM, 1,1,all
< SVLR TIM,1,1,"per1",25
< SVLR TIM,1,1,"per2",50
> DSVS 11, "per", TIM,1,1
> BSVR 11,"per1",30
> BSVR 11,"per2",60
> SVLR? TIM, 1,1,all
< SVLR TIM,1,1,"per1",25
< SVLR TIM,1,1,"per2",50
> BSVE 11
> SVLR? TIM, 1,1,all
< SVLR TIM,1,1,"per1",30
< SVLR TIM,1,1,"per2",60
```

**文档事实**：`STRS?` 示例（`02.06.06.02.30`）：

```
STRS? 0.5,2.0,LB,,LEV,"aclk_vo_swing",0.1,0.1
```

返回 `STRS GE,2,,`。

**文档事实**：`SVLR` 的 `Application` 段写「The assign value node in the testflow.」，并注明多 site 时每个 site 可以设自己的值（`02.06.06.02.31`）。**推断**：这就是「testflow 的 Assign Value 节点 ↔ 运行期改 spec 值」的对应关系；但文档只说「用于」，没有声明节点内部就是发 `SVLR`，所以不写成等价。

### 丁、边界命令（8 条，不计入本页覆盖数）

**说明**：下表的命令名与分类号取自 `show.py --list` 的篇名；一句作用取自本 wiki 已建的 [[pattern]] / [[results]] 页（它们逐条读过原文），本页**未重读**这些命令原文。列在这里是为了不漏掉本阶段会用到的执行入口，而不是把它们的语法搬过来。

| 命令 | 一句作用 | 本页为何只列入口 | 出处 |
|---|---|---|---|
| `FTST?` | 执行 functional test 并返回整体 `P` / `F`；test 必须已由 `SQLB` 定义、`SQSL` 激活。 | [[results]] 已逐条展开 | `02.06.11.02.25` |
| `SQSL` / `SQSL?` | 把 `MAIN` / `BRST` / `MPBU` label 设为 start label。 | [[pattern]] 已展开 | `02.06.07.02.29` |
| `SQGB` / `SQGB?` | 同时控制 sequencer 终止方式与 Error Map 记录。 | [[pattern]] / [[results]] 已展开 | `02.06.11.02.31` |
| `SQTO` / `SQTO?` | 设 sequencer timeout（秒）。 | [[pattern]] 已展开 | `02.06.07.02.31` |
| `FTSM` / `FTSM?` | 为下一次 sequencer run 设 cycle mask。 | [[pattern]] 已展开 | `02.06.07.02.17` |
| `SPRM` / `APRM` | 指定 / 激活 primary set。 | 配置语义归 [[timing]] / [[level]] | `02.06.06.02.28`、`02.06.06.02.01` |
| `PSFC` / `PSFC?` | 限制 setup 改动只作用于部分 site；默认所有 site 都有 setup focus。 | 横切；只在多 site 安全用法里出现 | `02.06.02.02.191` |
| `SHSP` / `SHVL` | shmoo 的 spec 与取值。 | shmoo 属 [[results]] / Shmoo Tool | `02.06.02.02.221`、`02.06.02.02.222` |

### L1 内记录的文档差异

1. **标准 connect 序列有两份写法。** `02.06.08.01.01` 的默认序列表是 `RLYC AC, OFF, (all I pins)` / `RLYC AC, OFF, (all remaining ac pins)` / `PSST ON` / `SQST BRK`；而 `02.06.08.01.04.01` 的「Standard connect/disconnect sequence」是 `RLYC CNCT,OFF,(@)` / `PSST ON` / `CNCT ON,(@)` / `SQST BRK`。两处都在 `02.06.08` 章内，**不自行选一个当正确答案**；实机以哪份为准需验证。
2. **`RLYC AC, OFF` 里的 `OFF` 是 `dc_target`，不是 `pin_mode`。** `pin_mode` 取 `AC` 表示 AC relay 闭合；`dc_target` 取 `OFF` 表示打开所有 channel board 与 clock board relay（`02.06.02.02.206`）。因此这句命令与 `02.06.08.01.01` 正文「AC relay is closed」方向一致——记在这里是为了防止把它误读成「断开 AC」。真正的差异仍是第 1 条的 `AC,OFF` 与 `CNCT,OFF` 两种开头。
3. **utility line 的电气上限有两个数字。** 章页 `02.06.12` 写「maximum current of 60 mA and a maximum voltage of 4.85 V」；`02.06.12.02.02`（`DFUT`）与 `02.06.12.02.13`（`UTST`）都写「maximum current of 100 mA and a maximum voltage of about 5.0 V」。两说并列，不合并。
4. **`FLSH` 的 `MUX` 参数是系统内部用的。** 文档明确「Do not use this parameter for programming a user procedure or executing the FLSH command from the hpt.」（`02.06.02.02.124`），但标准 disconnect 序列里却出现 `FLSH MUX`（`02.06.08.01.04.01`）。**推断**：序列表展示的是 SmarTest 自己生成的序列，不是给用户手抄的模板；用户自定义序列请用不带 `MUX` 的 `FLSH`。
5. **`PSST` 离线报错。** `PSST` 的 `Errors` 段写「You try to use the PSST or PSST? commands offline.」（`02.06.02.02.198`）。**推断**：离线跑 HRE 时，任何走到 connect 序列的路径都会先撞上这条。

## L2 — Test Method API

**文档事实**：本次读到的 L2 能力可归为四组：site 控制、flag 控制、sequencer/模拟执行控制、connect/disconnect 本身（分组是本页做的，成员各自有出处）。

### Site 控制

- **`SET_ACTIVE_SITES(TM::MS_SITE_SET)`**（`02.07.04.01.205`）：激活/取消激活 site，并更新 test method 内部缓存。文档 Note 明确它是「expert usage」，用于临时改变 active site，不用于常规 site 处理。被取消激活的 site 仍会被测，但结果不参与评估；DC test point 会被抑制。
- **`GET_ACTIVE_SITES`**（`02.07.04.01.79`）：返回 active site 数并把 site 号写入参数；并行执行时一般与 enabled sites 相同，串行执行时只返回当前 focus 的 site；在 `ON_FIRST_INVOCATION` 块外只返回调用程序的那一个 site。
- **`SET_ENABLED_SITES(TM::MS_SITE_SET)`**（`02.07.04.01.209`）：使能/禁用 site；enabled site 在下一个 test routine 初始化时连接，禁用立即生效。
- **`GET_ENABLED_SITES`**（`02.07.04.01.86`）：返回最初在 Site Control window 设置、且未被 bin 掉的 site。
- **`GET_CONFIGURED_SITES(ARRAY_I&)`**（`02.07.04.01.81`）：返回 pin configuration 里配置的 site 数。
- **`MS_SITE_SET`**（`02.07.04.01.132`）：长度为 `MS_MAX_SITES+1` 的 char 数组；索引 1 起，`[0]` 被忽略；非 0 表示激活，0 表示取消。

**文档事实（文档差异）**：`SET_ENABLED_SITES` 的参数表把两个分支都写成「enabled」：

> If sites[i] is not 0, site i will be enabled.
>
> If sites[i] = 0, site i will be enabled.

第二行应为 disabled（同页示例与 `GET_ENABLED_SITES` 的行为都表明 0 = 禁用）。**原文如此**，本页不擅自改文档，只记录。

### Flag 控制

- **`SET_TESTFLOW_FLAG(const STRING& flag, INT value)`**（`02.07.04.01.217`）：设置 testflow flag；头文件 `/opt/hp93000/soc/prod_com/include/MAPI/TestControl.h`。文档 Note 要求记住改 flag 只在下一次 test suite 执行时生效。
- **`SET_TESTSUITE_FLAG(const STRING& tsname, const STRING& flag, INT value)`**（`02.07.04.01.219`）：设置指定 test suite 的 flag；同样下一次执行才生效；部分 flag 只读，不能用此 API 设置。
- **`GET_TESTFLOW_FLAG` / `GET_TESTSUITE_FLAG`**：由 `02.08.04.32.01.02.07.02` / `.04` 的附加说明点名，用于读当前设置。本页未逐条展开其签名。

**文档事实**：`check_testmethod_api` 置 on 时，`TEST` 与 `PUT_DATALOG` 的 pin name 参数会在运行期被校验，非法 pin 名触发 fatal error；置 off（默认）则不校验。若要用 STDF 做结果分析，应把它置 on，否则 STDF 会丢失非法 pin 名的信息（`02.08.04.32.01.02.07.02`）。

### 执行控制

- **`START_TEST()`**（`02.07.04.01.235`）：从 start label 启动 digital sequencer，从 `BRK` 进入 `RUN`，**不等待**完成即执行下一条语句；必须与 `WAIT_TEST_DONE` 配合。
- **`EXECUTE_TEST`**（`02.07.04.01.65`）：同样从 start label 启动并 `BRK`→`RUN`，但会等到 digital 与 analog sequencer（AWG 除外）停止，或到超时。
- **`WAIT_TEST_DONE`**（`02.07.04.01.271`）：等待测试完成；可检测 digitizer/sampler 是否收到 trigger；超过 timeout 且未给 `timeout_info` 时测试被 abort、test suite 判 FAILED。
- **`ABORT_TEST`**（`02.07.04.01.01`）：中止所有 analog sequencer 与 digital sequencer，关闭所有 analog module 的 external trigger；digital sequencer 转到 break cycle，AWG/digitizer/sampler 停止，TIA 复位。

**文档事实（约束）**：`START_TEST` / `EXECUTE_TEST` 若要反映 `ROUTING_STATUS` / `ANALOG_STATUS` 对 analog module 硬件的改动，所有 analog module 的 sequencer 必须处于 halted 状态（`02.07.04.01.235`、`02.07.04.01.65`）。`START_TEST` 内部会执行 `FLUSH`，把 `ANALOG` / `ANALOG_STATUS` / `PRIMARY_STATUS` / `TIMING_SPEC` / `LEVEL_SPEC` / `SPECIFICATION` / `ROUTING_STATUS` 的改动刷到 setup 或硬件（`02.07.04.01.235`）。

### Connect / Disconnect

- **`Connect`**（`02.07.05.04.01`）：仅 UTM 可用；连接 AC relay 到 DUT 输入/输出/双向 pin，按 pin configuration 的顺序给 DPS 上电（每个 DPS channel 连接后按 level setup 的 wait time 等待），最后把 sequencer 设到 break/on。
- **`Disconnect`**（`02.07.05.04.02`）：仅 UTM 可用；把 sequencer 设 off，按 pin configuration 的相反顺序给 DPS 下电（此时不用 level setup 的 wait time），断开全部 relay（含 analog module 的 multiplexer）；sequencer off 时 driver 自动 tri-state。

**文档事实（约束）**：两个 test method 都写「If the … sequence cannot be executed successfully, the previous test system state will be recovered.」；恢复失败时状态按硬件实际状态置为 CONNECTED 或 DISCONNECTED，并在 Report Window 多打警告（`02.07.05.04.01`、`02.07.05.04.02`）。`Connect` 另有 hot switching 的 `Dependencies`（见前置条件第 8 条）。

### 文档未覆盖

**文档未覆盖**：本次未找到用 C++ Test Method API 直接控制 Operation Control 的 ABORT / RESET / ABORT TESTFLOW / PAUSE 四个按钮的接口。文档把这四个动作描述为 Operation Control window 的行为（`02.09.01.07`），并由 application model 决定实际效果（`02.09.01.07`）。

## L3 — 外部控制

**L3 入口是横切的，能力面按阶段分族。** 横切入口见 `02.09.01.14`（Test Suite Control API）、`02.09.01.10`（HVM API）与 `02.09.01.09`（TPI）。本阶段的专属族是：**test suite 的执行与 site 族**、**testflow/test program 的外部启停与事件族**、**`dm_testflow` 文件族**。

### Test Suite Control API（`02.09.01.14`）

**文档事实**：定位与限制（`02.09.01.14`）：

> Test suite control API is used to directly control the test suites outside of the testflow tool. Only UTM-based test suites are supported with these APIs. This is a set of independent APIs. They cannot be used in test method programming and also cannot be used in parallel with HVM API and BLC API by the same client process.

- **会话级（篇名级记录）**：`02.09.01.14.02` 下的成员篇名包括 `initializeSession()`、`detachSession()`、`exitProcess()`、`getTestsuite()`、`getAllTestsuiteNames()`、`getSpecialTestsuite()`、`createFloatingTestsuite()`、`deleteFloatingTestsuite()`、`selectTestmethodExecutor()`、`getTestmethodExecutorIndex()`。本次只到篇名层，未逐篇读其签名；引用时以篇名为准（`02.09.01.14.02`）。
- **site 级**：`setSiteInFocus(int)`（未激活则先激活；site 不可用则报错且不改）、`getSiteInFocus()`、`setActiveSites(const std::set<int>&)`（未 enable 则先 enable 再 activate；不可用则报错且不改）、`getActiveSites()`（`02.09.01.14.02.12`–`.15`）。
- **`TestsuiteProxy`**（`02.09.01.14.02.01`）：
  - `executeActiveSites()` — 在 active sites 上执行该 test suite（`02.09.01.14.02.01.02`）。
  - `executeSiteInFocus()` — 只在 focus site 上执行（`02.09.01.14.02.01.03`）。
  - `setTestsuiteFlag(TestsuiteFlag, int)` / `getTestsuiteFlag()` — 枚举含 `TESTSUITEFLAG_BYPASS`、`SET_PASS`、`SET_FAIL`、`HOLD`、`HOLD_ON_FAIL`、`OUTPUT_ON_PASS`、`OUTPUT_ON_FAIL`、`VALUE_ON_PASS`、`VALUE_ON_FAIL`、`PER_PIN_ON_PASS` 等（`02.09.01.14.02.01.33`；`getTestsuiteFlag()` 本页只到篇名层）。
  - `setSiteMatch(SiteMatchValue)` / `getSiteMatch()` — 取值 `SITEMATCH_OFF` / `ON` / `AUTO` / `UNDEFINED`（`02.09.01.14.02.01.30`）。
  - `isExecuted(int site)` / `isPass(int site)` — 每 site 的执行与 pass/fail 查询（`02.09.01.14.02.01.21`、`.23`）。
- **文档事实**：`executeActiveSites()` 与 `getActiveSites()` 合用的例子见 `02.09.01.14.02.15`：执行 `mysuite` 后逐个 active site 打 PASS/FAILED。

### HVM API（`02.09.01.10`）

**文档事实**：HVM API 让外部程序接入 SmarTest 执行环境：既能监控执行事件，也能用外部命令控制执行（`02.09.01.10.01`）。四个能力组里与本阶段直接相关的是 **Test Execution API**（`02.09.01.10.03.02.02`）。

**文档事实**：Test Execution API 在页面上列出的成员，本次按功能归为以下几组（分组是本页做的）：

- **下载/加载**：`DownloadTestflow`、`DownloadTestprogram`、`LoadTestflowSync`、`LoadTestprogramSync`；
- **执行**：`ExecTestflow`、`ExecTestprogram`、`ExecBLC`；
- **中止/暂停/恢复**：`AbortTestFLow`、`AbortTestprogram`、`AbortBLC`、`PauseTestprogram`、`PauseBLC`、`ResumeTestprogram`、`ResumeBLC`；
- **状态与事件**：`GetSmarTestExecStatus`、`GetLastEvent`、`IssueHVMExecutionEvent()`、`IssueEDLEvent()`、`GetApplicationProfile`、`GetLevelProfile`、`ChangeDevice`；
- **执行事件通知**：`TESTFLOW_EXEC_STARTED` / `_COMPLETED` / `_ABORTED`、`TESTPROGRAM_EXEC_STARTED` / `_COMPLETED` / `_ABORTED` / `_PAUSED` / `_RESUMED`、`DIE_STARTED` / `_COMPLETED`、`LOT_*`、`WAFER_*`、`CASSETTE_*`、`PACKAGE_*`、`STRIP_*`、`LEVEL_*`、`SETUPFILE_DOWNLOAD_*`、`TESTFLOW_DOWNLOAD_*`、`TESTPROGRAM_DOWNLOAD_*`、`DEVICE_CHANGE_*`、`DIALOG_*`、`ALARM_NOTIFICATION`。

**文档事实（同形陷阱）**：`GetLevelProfile` 里的 `Level` 是 application model 的层级结构，**不是**电压 level——该页的报错说明写「Level information is not available because application model level has not been initialized yet.」；不要拿它去补 [[level]] 页（`02.09.01.10.03.02.02.26`）。

**文档事实（约束）**：Test Suite Control API 与 HVM API、BLC API 不能由同一个 client process 并行使用（`02.09.01.14`）。

### TPI（`02.09.01.09`）

- **`DataManager`**（`02.09.01.09.02`）：`Fid` 参数 `dm_testflow` 表示 testflow 文件；同一接口按文件类型做 load/save 等操作。这是本阶段在 TPI 侧最直接的对应物。
- **文档未覆盖**：本次未找到 TPI 中专门「启动/停止 testflow 执行」的成员；TPI 文档里的执行入口没有在本次阅读范围内出现。**这是「本次未找到」，不是「文档不提供」。**

### SmartShell

**文档事实**：`02.15` 的 `Functional changes` 写 `Introduced in SmarTest 8.2.5`，正文只有 `SmartShell_7_Quick_Start.pdf`、`SmartShell_7_User_Guide.pdf`、`SmartShell_7_Command_Reference.pdf` 三个 PDF 外链。本 wiki 面向 SmarTest 7.10.3，因此**本页不把 SmartShell 当作可用的 L3 接口**；该章对它「让外部工具控制 test execution 并取回结果」的描述，只说明这个接口在**更晚版本**里的形态。

### 生产入口（非 API）

**文档事实**：生产模式下，Operation Control window 的 `Execute Workorder` 是另一个执行入口；workorder 按用户列在其 home 目录的 workorder 目录下，supervisor/engineering 模式可重新分配（`02.09.01.05.05.01`）。本页把它记为入口，不展开 workorder 的文件格式。

## 产物

**推断**：本阶段不产生新的 setup 文件；它消费 [[testflow]] 阶段产出的 testflow 文件与各 setup 文件，产生的是执行痕迹与结果数据。

- **report window 输出** — testflow 与各 test suite 的执行结果、loop 信息、计时信息（`debug_mode` 3/4）都出现在 report window（`02.08.04.32.02.03`、`02.08.04.32.02.03.04`）。
- **Flow Sequence Editor 的着色状态** — passed 节点绿、failed 节点红、bypassed 节点黄；执行后若再编辑 testflow，所有 test suite 边框变虚线（`02.08.04.32.02.03`）。
- **Test Suites 页的 `Result > Pass/Fail` 单元格颜色** — 绿底 = passed、红底 = failed、绿框 = set to pass、红框 = set to fail、黄框 = set to bypass（`02.08.04.32.02.03`）。
- **Error Map 数据（机台内存）** — 由执行产生、由 [[results]] 读取；本页不重复其格式。
- **data log stream（若开启）** — 由 test suite flag `output_on_pass` / `output_on_fail` 与 system flag `log_events_enable` 控制（`02.08.01.01.05.01`）；归档格式见 [[results]]。
- **hardware response file（HWRE Store 模式）** — 文件名格式 `Testsuite;MAPI; call#; site#`，其中 `site#` 是 query focus 的 site 号；文件建在 testflow 指定的目录（`02.08.04.32.02.06.03`）。示例名：`TS1;Analog.DGT("a_out").getWaveform(1);1;1`（同页）。
- **Site Select CSV** — 导出整张表（state、testflow 执行结果、每 site 汇总），也可只把 site 状态导回（`02.08.04.28`）。
- **Debug view 的执行树** — 临时状态，不是文件；显示当前停在哪个 test suite / 第几次 loop（`02.08.04.32.02.04.01`）。
- **无 device 目录产物** — **推断**：本阶段本身不向 device 目录写新文件；`connect.user_def` / `disconnect.user_def` 是输入而非产物（`02.06.08.01.04`）。

## 验证

以下均为文档给出的查询/观察入口，不是本页发明的方法。

- **report window**：testflow 结果与 loop 号输出在这里；`Log Loop Number` 打开时每个 loop 开头打印 `Executing Test Flow Loop Iteration: 2` 形式的消息（`02.08.04.32.02.03.01`）。
- **Flow Sequence Editor 颜色**：passed/failed/bypassed 分别为绿/红/黄（`02.08.04.32.02.03`）。
- **Test Suites 页颜色与边框**：单元格底色表示实际结果，边框颜色表示被设为 pass/fail/bypass；二者的区别见上「产物」（`02.08.04.32.02.03`）。
- **多 site 的单元格语义**：Test Suites 页显示所有 site 时，只有全部 site pass 才绿；只显示 focus site 时按该 site 的结果着色（`02.08.04.32.02.03`）。
- **Site Select view**：`Result` 列给 `N/A` / `PASS` / `FAIL`；`Soft` / `Hard` 给软件/硬件 bin；`Pass#` / `Fail#` / `Sum#` / `Yield%` 给全部 loop 的累计；summary line 给全 site 的 Pass#/Fail#/Sum#/Yield%（`02.08.04.28`）。
- **Debug view**：显示执行节点（如 `Testflow (Full)`）与其子项（如 `Ftest (Testsuite_1)`）；Step Over 后子项从 `Ftest (Testsuite_1)` 变为 `Ftest (Testsuite_2)`（`02.08.04.32.02.04.01`）。
- **Operation Control window**：testflow 运行时出现 ABORT / RESET / ABORT TESTFLOW / PAUSE 四个按钮（`02.08.04.32.02.03`、`02.09.01.07`）。
- **test time 测量**：`debug_mode` 设 3 或 4 后，report window 出现完整测试与 application model 每一层的 timing 信息；`TESTFLOW INFORMATION` 的 `# of measure.` 列是 testflow 重复次数（`02.08.04.32.02.03.04`）。
- **路径覆盖统计**：在每个路径插入 Assign Value 节点累加变量，并在 bin 的 Description 里写 `path_1=@{path_1}, path_2=@{path_2}`，执行后 data log 里有各路径次数（`02.08.04.32.02.03.03`）。
- **运行期 spec 值**：`SVLR?` 可读回当前 runtime 值与 min/max/unit；`BSVE` 后才看得到 spec value set 的新值（`02.06.06.02.31`、`02.06.06.01.05.02`）。
- **HWRE 是否生效**：test 执行开始时弹 Hardware Response Emulator window，确认 hardware response 目录与目标 test suite 后点 OK；文件缺失时会弹对话框要求指定数据（`02.08.04.32.02.06.02`）。
- **单步是否可按**：只有 `Resume` / `Terminate` / `Step Over` 三个按钮 enabled 时，才说明执行停在可单步的状态（`02.08.04.32.02.04.01`）。

## 常见错误

- **用户自定义 disconnect 造成 pass/fail site dependency。** 用户自定义序列不区分 shared / non-shared pin，会只按文件里的 pin 标识断连；为避开 site 依赖，可能需要只对非 shared pin 定义用户序列，shared pin 只在 testflow 末尾手工断一次。分析与其他 workaround 见 `03.04.02` / `03.04.02.01` / `03.04.02.02`，实现见 `03.04.01.03.01` / `03.04.01.03.02`（`03.04.01`）。
- **`SQST` 在 `HALT` 与 `OFF` 之间直跳。** 文档明确「you cannot pass directly from HALT to OFF or from OFF to HALT. You must first pass to BRK in both cases.」；`ABRT` 还要求指定 execution context（`02.06.07.02.30`）。
- **hot switching。** 症状：relay 在带电状态下切换，可能损伤 DUT 或 tester。原因：在 firmware 层把 sequencer 从 OFF 改到 BREAK，随后又调 `Connect` test method（`02.07.05.04.01`）。**文档要求**：connect 序列本身要从 sequencer OFF 起跑（`02.06.08.01.01`）。
- **多 site 下直接发 `RLYC` 影响已 bin 的 site。** 症状：binning 错误、甚至器件损坏；UI 仍认为该 site 已断开，但 relay 实际已闭合，testflow 结束时不会再断开它（`02.06.02.02.206`）。文档给的编程提示是先用 `PSFC` 限定到 enabled sites 再 `RLYC`，之后 `PSFC ALL`（`02.06.02.02.206`）。
- **`RLYC` 改变 relay 状态后 connect/disconnect flag 与实际不符。** 在 connected 状态用 `RLYC` 打开 relay，后续测试不会再调 connect 序列；反过来在 disconnected 状态闭合 relay，continuity test 不会再调 disconnect 序列，二者都会导致错误结果（`02.06.02.02.206`）。
- **在 connected 状态禁用 site。** 症状：出现 warning；文档要求只能在 disconnected 状态用 enable 按钮关 site（`02.08.04.27.01`）。
- **`Execute site in focus` 把 Error Map 数据清掉。** 该操作会先把其它 active site 全部 mask，跑完再重新激活；而重新激活会 reset 所有 site 的 Error Map 数据，于是刚为 focus site 产生的数据被删。要看这些数据，必须先把除 focus site 外的 site 全部 inactivate（`02.08.04.27.01`）。
- **用窄选跑单个 test suite，结果受前一个 test suite 影响。** 不带子分支的窄选按当前状态执行，每个 test suite 的执行受上一个结果影响；宽选则把所选构成临时 testflow，行为像跑完整 flow 但忽略 binning（`02.08.04.32.02.03`、`02.08.04.32.02.01.11.01`）。
- **loop 里断开行为不同。** 跑整条 testflow 的 loop 在**每次** run 结束都 disconnect；只跑单个 test suite 的 loop 不 disconnect，除非在 test method 里自己写（`02.08.04.32.02.03`）。
- **`Break`（stop sign）不能中止 loop。** 文档明确「The Break button (stop sign) does not abort the loop execution.」；要干净地中止 loop，顺序是 PAUSE → 等执行结束 → ABORT → 在 PAUSE 对话框按 Quit（`02.08.04.32.02.03`）。
- **loop 配置不能在执行中改。** SmarTest 6.5.2 起不允许在 testflow 或 test suite 执行期间改 loop 配置（`02.08.04.32.02.03.01`）。
- **单步跑不了 `Testflow (Full)`。** 文档 `Limitation` 写「You cannot start a full testflow execution (default name: Testflow (Full)) in the single step mode.」；绕法是先跑第一个 test suite 的 `Run and Hold after here`，等 hold 停住后再单步（`02.08.04.32.02.04.01`）。
- **hold flag 调试的坑。** 文档不推荐用 hold flags 调试：它会改变 testflow 内容并可能被保存；弹窗可能在主窗口后面而看不见；要恢复执行必须把剩余 hold flag 全部取消；且 hold 之后仍要逐 test suite 设 flag 才能一步步走（`02.08.04.32.02.04.01`）。
- **未定义/非法的 testflow flag。** 加载 testflow 时会对未定义或非法 flag 打 warning，消息模板为 `Testflow flag "<flag_name>" is not defined.` 与 `Warning: Invalid flag statement encountered in testflow file, in the "flags" section: The flag "<bad_flag_name>" is not defined. Use the "user" keyword to define a user flag.`（`02.08.04.32.01.02.07.02`）。
- **`check_testmethod_api` 关着却用 STDF。** pin name 参数不校验，STDF 会丢失非法 pin 名信息，导致 STDF 结果无法分析（`02.08.04.32.01.02.07.02`）。
- **flag 优先级误判。** pass level 与 fail level 冲突时 pass level 优先；单 test suite 的 Set pass / Set fail / Bypass 优先于全局 testflow flags（`02.08.04.32.01.02.07.06`）。
- **`Site Match` 与共享 analog module。** 使用多个 site 共享的 analog module 时要设 `site_match`；文档同时要求 `Allow parallel` flag 在依赖前一 test suite 状态/错误信息、或使用 user-procedure 时必须关闭，否则应串行（`02.08.04.32.01.02.07.05`）。
- **用户自定义 connect/disconnect 不生效。** 文件只在软件启动或 device change 时读取，运行中改文件可能没效果；shared multisite 不支持（`02.06.08.01.04.01`）。
- **自定义序列里的 `FLSH MUX`。** `MUX` 是系统内部参数，文档要求不要在用户 procedure 或 hpt 里用（`02.06.02.02.124`）。
- **`PSST` 离线报错。** 离线执行 connect 序列会报错；`PSST` 的 `Errors` 明确列了离线使用（`02.06.02.02.198`）。
- **`SVLR` 的两个报错条件。** spec 不存在，或新值导致 range / limit 违反（`02.06.06.02.31`）。**`STRS?` 的报错条件**：所用 primary sets 不是 equation-based（`02.06.06.02.30`）。
- **`SVLR` 与 `LEVEL_SPEC` / `TIMING_SPEC` 混用。** 文档 CAUTION 要求除调试目的外不要混用；两个 API 会缓存值以支持 `.restore()`，firmware 层没有这个缓存（`02.06.06.02.31`）。
- **HWRE 找不到响应文件。** Import 模式下若所需文件不存在，会弹 Hardware Response Emulator Dialog 要求人工指定结果并保存（`02.08.04.32.02.06.02`）。
- **不可用 site 无法操作。** 因 pin configuration 缺陷而不可用的 site 不能被 enable / activate / 取得 result focus（`02.08.04.27.01`）。
- **`Execute Workorder` 的权限。** 用户只能执行自己 workorder 目录下的 workorder；supervisor/engineering 模式才可重新分配（`02.09.01.05.05.01`）。

## 下一步

下一步是 [[results]]：本阶段只负责把 test 跑起来并观察执行过程；要回答「这次到底 pass 还是 fail、失败在哪个 cycle/edge、结果存在哪里」，需要 [[results]] 里的 Error Map 查询、`FTST?` / `PASS?` / `CHER?`、数据日志与 STDF 归档。**文档事实**：数字走查把第 5 步的产出定义为「Obtain the test results and debug the test」，工具点名 Testflow Tool、Timing Diagram Tool、Error Map Tool（`02.08.01.01.05`）；数据记录与读取命令编在 `02.06.11`（[[results]]）。若调试发现 setup 问题，回到对应的 [[pin]] / [[level]] / [[timing]] / [[pattern]] / [[testmethod]] / [[testflow]] 页修正后再次进入本阶段。
