---
type: stage
title: Testflow 组装（Testflow Tool）
tags: [testflow, testflow-tool, flow-data-editor, flow-sequence-editor, test-suite, bin, flag, testflow-file, testflow-master-file, hardware-response-emulator, test-suite-control-api]
related:
  - "[[project]]"
  - "[[pin]]"
  - "[[level]]"
  - "[[timing]]"
  - "[[pattern]]"
  - "[[testmethod]]"
  - "[[run]]"
  - "[[results]]"
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32_Testflow_Tool.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01_Introduction_of_the_Testflow.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.01_Testflow_methodologies.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02_Testflow_components.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.01_Test_suites.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.01.01_Run__and__Run_and_Branch__test_suites.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.01.02_Special_test_suites.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.01.03_Floating_test_suite.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.01.04_Multibin_SmartDisconnect_test_suite.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.01.04.01_Inserting_a_Multibin_SmartDisconnect_test_suite.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.02_Flow_control_nodes.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.02.01_Built-in_functions.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.03_Assign_Value_node.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.04_Print_nodes.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.05_Group_node.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.06_Bins.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.07_Flags.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.07.01_Alphabetical_list_of_flags.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.07.02_Testflow_flags.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.07.03_Testflow_flags_for_data_logging.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.07.04_Test_suite_flags.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.07.05_Site_control_flags.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.07.06_Flag_priority.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.03_Hierarchy_within_a_testflow.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.04_Multiple_Sites_Execution.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.05_Configuring_the_messages_printed_in_the_Report_Window.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02_Using_the_Testflow_Tool.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01_Editing_a_testflow.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01.01_Opening_the_Testflow_Tool.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01.02_Creating_a_testflow.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01.03_Selecting_setup_files.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01.04_Inserting_a_test_suite_into_the_testflow.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01.04.01_Setting_up_a_multiport_testsuite.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01.04.02_Setting_up_a_special_test_suite.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01.04.03_Creating_a_floating_test_suite.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01.04.03.01_Connecting_a_floating_test_suite_to_the_testflow.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01.05_Inserting_a_bin_into_the_testflow.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01.06_Editing_a_test_suite_in_the_Flow_Data_Editor.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01.07_Adding_a_limit_on_the_Tests_page.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01.08_Adding_a_limit_in_the_Properties_view.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01.09_Adding_limits_in_a_TMLimits_test_table.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01.10_Selecting_pins_in_the_Properties_view.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01.11_Working_with_nodes.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01.11.01_Narrow_selection_and_wide_selection.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01.11.02_Inserting_a_node.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01.11.03_Deleting_nodes.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01.11.04_Cutting__copying_and_pasting_nodes.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01.11.05_Moving_nodes.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01.11.06_Cloning_nodes.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01.11.07_Grouping_nodes.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01.12_Working_with_variables.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01.12.01_Defining_variables.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01.12.02_Deleting_variables.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01.12.03_Assigning_values_to_variables.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01.12.04_Assigning_a_level_or_timing_spec_value.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01.12.05_Changing_spec_values_at_run_time.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01.13_Printing_a_graphical_representation_of_the_testflow.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01.14_Identifying_fail_labels_in_a_burst.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01.15_Importing_a_testflow_from_a_CSV_file.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01.16_Exporting_a_testflow_to_a_CSV_file.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.02_Navigating_a_testflow.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.02.01_Searching_for_test_suites__bins_and_variables.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.03_Running_a_testflow.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.03.01_Loop_configuration_settings.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.03.02_Using_the_Overon_feature_while_running_a_testflow.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.03.03_Checking_the_execution_flow.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.03.04_Measuring_the_test_time.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.03.05_Adding_user_defined_testflows_to_the_Run_menu.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.04_Debugging_a_testflow.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.04.01_Single_step_testflow_debugging.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.05_Merging_the_testflows.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.05.01_Source_and_target_testflows.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.06_Hardware_Response_Emulator.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.06.01_Preparing_Hardware_Response_files.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.06.01.01_ARRAY_X_type.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.06.01.02_DOUBLE_type.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.06.01.03_SpecSearch_type.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.06.01.04_DC_API_type.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.06.01.05_FW_TASK_type.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.06.01.06_Pass_Fail_type_and_ERROR_MAP_type.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.06.02_Using_hardware_response_files_for_execution.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.06.03_Hardware_response_files.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.06.04_Supported_test_suites_and_test_method_APIs.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.07_Configuring_the_Testflow_Tool.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03_Elements_of_the_Testflow_Tool.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.01_Flow_Data_Editor.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.01.01_Test_Suites_page.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.01.02_Parameters_page.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.01.03_Tests_page.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.01.04_Bins_page.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.01.05_Variables_page.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.01.06_Flags_page.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.01.07_Setups_page.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.01.08_Information_page.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.02_Flow_Sequence_Editor.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.03_Synchronization_between_the_Flow_Data_Editor_and_the_Flow_Sequence_Edito.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.04_Testflow_Properties_view.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.05_Testflow_file.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.06_Testflow_master_file.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.06.01_Top-level_control_structures.htm
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02.04.05.04_Collision_handling_for_the_testflow_master_file.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.01.02.06_Task_10_and_11__Executing_a_Testflow_and_Obtaining_the_Results.htm
  - 02_System_reference/02.06_Command_Reference/02.06.03_Pin_configuration_setup_commands.htm
  - 02_System_reference/02.06_Command_Reference/02.06.04_Routing_Setup_Commands.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05_Level_Setup_Commands.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06_Timing_Setup_Commands.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07_Vector_Setup_Commands.htm
  - 02_System_reference/02.06_Command_Reference/02.06.08_Relays_and_Control_Commands.htm
  - 02_System_reference/02.06_Command_Reference/02.06.09_AC_Testing_Commands.htm
  - 02_System_reference/02.06_Command_Reference/02.06.10_DC_Measurement_Commands.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11_Test_Result_Commands.htm
  - 02_System_reference/02.06_Command_Reference/02.06.12_Utility_Line_Commands.htm
  - 02_System_reference/02.06_Command_Reference/02.06.13_Commands_for_the_TMU_per_pin.htm
  - 02_System_reference/02.06_Command_Reference/02.06.14_Commands_for_Processing_Results_of_Source_Synchronous_Testing.htm
  - 02_System_reference/02.06_Command_Reference/02.06.15_Commands_for_the_protocol_engine_per_pin.htm
  - 02_System_reference/02.06_Command_Reference/02.06.16_Commands_for_jitter_injection.htm
  - 02_System_reference/02.06_Command_Reference/02.06.17_Commands_for_PRBS_per_pin_tests_and_loopback_tests.htm
  - 02_System_reference/02.06_Command_Reference/02.06.18_Calibration_and_Attributes_Commands.htm
  - 02_System_reference/02.06_Command_Reference/02.06.03.02.16_PACT__PACT__-__Parallel_ACTivities_control.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.24_SVLR__SVLR__-__Spec_VaLues_at_Runtime.htm
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.123_FLBL__-__Failing_LaBeLs.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.02.34_TSTL__TSTL__-__TeST_Label.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.02.02_APTS_-__APpend_TeSt.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.02.12_DLTS_-__DeLete_TeSt.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.02.33_TCMT__TCMT__-__Test_CoMment_Transfer.htm
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02.04.03_Using_the_Setup_Management_Tool_from_the_Command_Line.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.01.01.01_Testing_flow_and_Test_Method_API.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.08.05_Setting_Testflow_Variables.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.08.06_Obtaining_Values_of_Testflow_Variables.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.08.09_Obtaining_Name_of_Currently-Running_Testsuite.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.96_GET_TESTFLOW_FLAG.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.217_SET_TESTFLOW_FLAG.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.219_SET_TESTSUITE_FLAG.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.41_DISCONNECT.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.61_ERROR_EXIT.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.80_GET_BIN.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.82_GET_CURRENT_BIN_INFORMATION.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.84_GET_DISCONNECT_CONTEXT.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.91_GET_MULTIBIN.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.100_GET_TESTSUITE_FLAG.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.188_RESET_MULTIBIN.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.210_SET_EXCEPTION_HANDLER.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.212_SET_MULTIBIN.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.09.02_DataManager.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.09.12_GetLoadedTestflowName.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.09.17_GetTestflowRevisionInfo.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.10.03.02.02.19_DownloadTestflow.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.10.03.02.02.21_ExecBLC.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.10.03.02.02.30_LoadTestflowSync.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.11.03.06_Synchronous_testflow_execution_API.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.11.03.06.01_DownloadTestflowSync.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.11.03.06.02_ExecuteTestflowSync.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.11.03.12.03_GetTestflowInformation.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14_Test_Suite_Control_API.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.01_How_to_use_the_test_suite_control_API.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02_Test_suite_control_API_reference.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01_TestsuiteProxy.htm
  - 02_System_reference/02.15_SmartShell/02.15_SmartShell.htm
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.06_convertTestflow.htm
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.04.06.01_Converting_MTP_testflows_to_UTM.htm
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.13_Running_MTP_testflows_with_MTP-EWC.htm
  - 03_Use_cases_and_application_papers/03.14_Application_Papers/03.14.07.02_New_Tabular_Testflow_Tool_in_the_SmarTest_Work_Center.htm
created: 2026-11-12
updated: 2026-11-12
verified: doc-only
---

# Testflow 组装

> 把已经建好的 test suite 按执行顺序、分支、bin 与 flag 组装成一份可执行、可调试的 testflow 文件。

**全文约定**：标「文档事实」的段落与各表条目均来自所标出处；标「推断：」的是本页从多处材料推出的；标「建议：」的是工程意见。表格行不逐行重复「文档事实」四字。本 wiki 面向 **SmarTest 7.10.3**；页内标注的版本差异只用于避免推荐已被移除的做法。

## 目的

**文档事实**：`02.08.04.32` 对本工具的定位只有一句话：

> The Testflow Tool is used to develop and debug a testflow.

**文档事实**：`02.08.04.32.01` 把 testflow 定义为一个互相连接的测试集合，而不是若干测试的简单列表：

> A testflow is an interconnected collection of individual tests, each one testing a particular parameter.

这些测试可以按顺序、依据前一个或另一个结果、在某个条件成立期间等方式互相连接；合起来构成对器件的完整测试（`02.08.04.32.01`）。

**文档事实**：`02.08.04.32.01.01` 给出本阶段的开发方法——先建全局 setup 文件，再逐个开发 test suite，并采用 top-down 方式（先想清楚测试流，再搭流程，最后填每个 test suite 的细节）。全局 setup 文件在 Setups 页选择，包括 pin configuration、timing、levels、vector 和 pin attributes，对整个 testflow 有效；每个 test suite 含一个 test method，且必须定义 primary sets（level 与 timing）。

**推断**：本阶段是「组装」而不是「新建测试内容」。pin/level/timing/pattern 定义的是可被引用的资源，testmethod 定义的是单个 test suite 的可执行体；testflow 这一段决定的是这些 test suite 的**执行顺序、分支条件、bin 归属、flag 开关和运行时变量**，并把它们落成一份文本文件。缺这一层，前几段的资源只能被单独调用，不能形成量产测试程序。

**归属边界（判断，不是文档事实）**：本页覆盖 Testflow Tool 的建流、编辑、调试期运行、合并、HRE 与文件格式。**生产运行**（workorder / Operation Control / 批量执行）归 [[run]]；执行后的数据与判定归 [[results]]。`02.08.04.32.02.03` 里用 Run 对话框跑 Testflow (Full) / (Selection) / (User Defined)，语境是调试与集成，故仍放在本页。

## 前置条件

- **所有 test setup 已加载，所需 test method 已 build**。`02.08.04.32.02.01.02` 的 `Before you begin` 逐字要求：

  > Make sure that
  >
  > All the test setups have been loaded.
  >
  > All the required test methods have been built.

  这是本阶段最硬的前置条件。对应前面的 [[pin]] / [[level]] / [[timing]] / [[pattern]] / [[testmethod]]。
- **全局 setup 文件已存在**。`02.08.04.32.02.01.03` 要求先创建 setup 文件再在 Setups 页选择；同一篇的 Functional changes 明写 `SmarTest 6.5.2: You cannot create setup files with the Testflow Tool.` 所以 setup 文件必须由各自工具产出。
- **插入 test suite 前，primary setup 文件已加载、所需 test method 已 build**。`02.08.04.32.02.01.04`、`.04.02`、`.04.03` 的 `Before you begin` 都重复这一条。
- **运行 testflow 前，testflow 已 load**。`02.08.04.32.02.03`、`.03.02`、`.04.01`、`.05` 均要求 testflow loaded。
- **Testflow Tool 的入口视角已打开**。`02.08.04.32.02.01.01`：

  > Make sure that the 93000 Setup perspective is opened.

- **打开 testflow 时可能检查 test method library 版本**。`02.08.04.32.02.01.01` 说明，启用 `Check UTM test method library version when opening testflow editor` 时，若 testflow 使用的 test method library 不是当前 SmarTest 版本构建的，会显示警告。
- **master file 的引用关系已成立**。`02.08.04.32.03.06` 要求母文件第一行是 `hp93000,testflow_master_file,0.1`，第二行必须是 `testerfile: <tester_file_name>`，之后才是 GROUP / information / flags / bins / setup / VAR 引用。
- **使用 Hardware Response Emulator 前**：已连接测试系统；所需 SmarTest 版本已激活；SmarTest 正在运行；testflow 已 load 且已执行 Load all Setups；testflow 已在 Flow Sequence Editor 打开；需要离线使用的 site 都已 active（`02.08.04.32.02.06.01`）。
- **L3 使用 Test Suite Control API 时**：SmarTest 6.5.2 或更高；在 run shell 中编译（`/opt/hp93000/soc/system/bin/run -S`）；仅支持 UTM-based test suite（`02.09.01.14`、`.14.01`）。
- **建议**：先列出「要跑哪些 test suite、失败走哪条分支、每个分支进哪个 bin、调试期需要哪些 flag」四张清单，再进 Flow Sequence Editor。文档给了功能，没有给这四张清单的模板。

## 涉及对象

| 对象 | 层级 | 在本阶段做什么 |
|---|---|---|
| `Testflow Tool` | gui | 本阶段主工具；开发与调试 testflow（`02.08.04.32`）。 |
| `Flow Data Editor` | gui | 八个页签的表格编辑器：Test Suites / Parameters / Tests / Bins / Variables / Flags / Setups / Information（`02.08.04.32.03.01`）。 |
| `Flow Sequence Editor` | gui | 图形化显示并编辑 testflow 序列；用左侧 Palette 插入节点（`02.08.04.32.03.02`）。 |
| `Testflow Properties view` | gui | 显示并编辑当前选中的 test suite / bin / group / flow control / Assign Value / Print 节点的属性（`02.08.04.32.03.04`）。 |
| `testflow file` | file | 本阶段产物；位于 `<device_dir>/testflow`，存 testflow 的全部数据（`02.08.04.32.03.05`）。 |
| `testflow master file` | file | 把 testflow 拆成多个子文件时使用的母文件；`GROUP` / `information` / `flags` / `bins` / `setup` / `VAR` 引用子文件（`02.08.04.32.03.06`）。 |
| `CSV export/import` | file | testflow 与表格数据之间的导入/导出格式，用于复用、报表与跨平台交换（`02.08.04.32.02.01.15`、`.16`）。 |
| `hardware response file` | file | HRE 的离线响应数据；文件名形如 `Testsuite;MAPI; call#; site#`（`02.08.04.32.02.06.03`）。 |
| `.testflow.ReportUiOutput.user_def` | file | 控制 Report Window 打印内容的配置文件，放在 `<DeviceDirectory>/testflow`（`02.08.04.32.01.05`）。 |
| `test suite` | concept | 独立可执行的测试单元，含 timing/level sets、equations 与 test suite flags（`02.08.04.32.01.02.01`）。 |
| `special test suite` | concept | 在特定时点执行的 test suite：Init / Download / bin_disconnect / multi_bin_decision / Abort / Pause / Reset / Exit（`02.08.04.32.01.02.01.02`）。 |
| `floating test suite` | concept | 不接入 testflow 序列、供调试使用的 test suite；调试完可接入（`02.08.04.32.01.02.01.03`）。 |
| `Multibin SmartDisconnect test suite` | concept | multibin 节点与用户自定义 test suite 的组合，插在 Run and Branch 的 fail 分支，用自定义 disconnect 序列断开失败 site（`02.08.04.32.01.02.01.04`）。 |
| `bin` / `multibin` | concept | 按测试结果分选器件；stop bin / otherwise bin / floating bin 与 multibin（`02.08.04.32.01.02.06`）。 |
| `flag` | concept | 四类：testflow、data logging（system）、test suite、site control（`02.08.04.32.01.02.07`）。 |
| `variable` / `built-in function` | concept | testflow 变量与在条件表达式里取结果、集合数量、burst label 的内建函数（`02.08.04.32.02.01.12`、`02.08.04.32.01.02.02.01`）。 |
| `Hardware Response Emulator (HWRE)` | tool | 离线调试时返回预置的模拟波形、测量值、pass/fail；Store 建文件，Import 用文件（`02.08.04.32.02.06`）。 |
| `smartest_mfh` | tool | Setup Management Tool 的命令行程序；`create` 的 `file_type` 可取 `testflow`，并可 split/assemble testflow 母文件（`01.01.07.02.02.04.03`）。 |
| 本阶段 L2 API | L2 | `SET_TESTFLOW_FLAG` / `SET_TESTSUITE_FLAG` / `SET_MULTIBIN` / testflow 变量 API 等；见 L2 节。 |
| 本阶段 L3 族 | L3 | Test Suite Control API、同步 testflow 执行 API、HVM Test Execution API、TPI `DataManager`；见 L3 节。 |

### 归属判定

**这是判断，不是文档事实。** 写在这里供维护者复核。

- **本次未找到 `02.06` 下的 testflow 专属命令子树。** 按 `02.06` 的章节目录查看：`02.06.03` pin configuration、`02.06.04` routing、`02.06.05` level、`02.06.06` timing、`02.06.07` vector setup、`02.06.08` relays、`02.06.09` AC test、`02.06.10` DC measurement、`02.06.11` test result、`02.06.12` utility line、`02.06.13` TMU、`02.06.14` source synchronous、`02.06.15` protocol engine、`02.06.16` jitter、`02.06.17` PRBS、`02.06.18` calibration；没有以 testflow 命名的命令章。testflow 的配置级语句（`run()`、`run_and_branch()`、`stop_bin` 等）写在 `02.08.04.32.03.05` 的 `## Syntax`（BNF）里，而不是 `02.06`。**因此本页把 testflow 文件/母文件的语句集作为 L1 的覆盖对象；这是本页的判断，不是文档把该语句集称作 L1。**
- **`TSTL` / `APTS` / `DLTS` / `TCMT` 判给 [[pattern]]，不是 testflow。** 这四条虽然名字像「test / label」，但四篇的 `Application` 都逐字写着 `Edit command in Pattern Tool.`（`02.06.07.02.34`、`.02`、`.12`、`.33`）；它们操作的是 sequencer label / vector table，不是 testflow 的 test suite 序列。不要拿它们「补」本页的 L1。
- **`smartest_mfh` 判给 [[project]]，本页只引用其 testflow 母文件行为。** 它是通用的 setup-file split/assemble 工具，`file_type` 可为 level / timing / analog_control / waveform / routing / testflow / testtable；工具本身不属于 testflow 层。本页只写「它会处理 testflow 母文件」这一条，并把命令语法留在 project 页（`01.01.07.02.02.04.03`）。
- **`PACT` 与 `SVLR` 是散落的本阶段 L1。** 两者都属于别的 stage 的命令章（PACT 在 pin configuration 章、SVLR 在 level/timing 章），但 testflow 文档明确在 testflow 语境引用它们：`PACT` 用于 test suite 要求串行执行、或分支后不同 site 走不同路径时（`02.06.03.02.16`）；`SVLR` 是运行期改 level/timing spec 值的固件命令（`02.08.04.32.02.01.12.05`、`02.06.05.02.24`）。本页只列这两条，并保留其原始 stage 的归属。
- **`FLBL?` 判给 [[results]]，不是 testflow。** `FLBL?` 是 burst 失败 label 的结果查询（`02.06.02.02.123`）；testflow 的「Identifying fail labels in a burst」用的是 `burstfirst` / `burstnext` 内建函数，不是 FLBL（`02.08.04.32.02.01.14`）。名字像「fail label」不等于它属于本阶段。
- **HRE 的数据类型六篇判给本页。** ARRAY_X / DOUBLE / SpecSearch / DC API / FW_TASK / Pass-Fail 与 ERROR_MAP 都是 Testflow Tool 的离线调试子工具，不属于 test method 参考（`02.08.04.32.02.06.01.*`）。
- **Memory Test Plus 的 testflow 篇目不判给本页。** `02.12.04.06`、`02.12.04.06.01`、`02.12.02.05.13` 等属于 MTP 产品线；本 wiki 面向 SmarTest 7.10.3 的 93K 基座，MTP 转换/运行不在本页范围。
- **`03.14.07.02` New Tabular Testflow Tool 不判给本页。** 它是 application paper，描述 Work Center 的新表格型 Testflow 工具，不是 `02.08.04.32` 的操作参考；本页不据它推断机台能力。

### Testflow 组件与语义（覆盖 `02.08.04.32.01.*`）

| 分类号 | 文档 | 一句话 |
|---|---|---|
| `02.08.04.32.01` | Introduction of the Testflow | testflow 是互相连接的测试集合，可按顺序/结果/条件连接；本章下分 methodologies、components、hierarchy、multiple sites、Report Window 消息。 |
| `02.08.04.32.01.01` | Testflow methodologies | top-down 开发：先建全局 setup 文件，再逐个开发 test suite；primary sets 必须定义。 |
| `02.08.04.32.01.02` | Testflow components | 组件清单：test suites、flow control / Assign Value / Print 节点、built-in functions、bins、flags、variables、group node。 |
| `02.08.04.32.01.02.01` | Test suites | test suite 是独立可执行测试；含 timing/level sets、equations 与 test suite flags；分 Run/Run and Branch、special、Multibin SmartDisconnect、floating 四型。 |
| `02.08.04.32.01.02.01.01` | "Run" and "Run and Branch" test suites | Run 只有一条路径；Run and Branch 按 pass/fail 结果分支。 |
| `02.08.04.32.01.02.01.02` | Special test suites | 在特定时点执行的 suite；不在 Flow Sequence Editor 显示，而在 Test Suites 页末尾；含 8 种（原文称 seven types，见下）。 |
| `02.08.04.32.01.02.01.03` | Floating test suite | 不接入序列、用于调试；调试完可接入。SmarTest 6.5.2 引入。 |
| `02.08.04.32.01.02.01.04` | Multibin SmartDisconnect test suite | multibin + 自定义 disconnect suite；插在 Run and Branch 的 fail 分支；site mask 进入 run() 时已反转。SmarTest 7.6.1 引入。 |
| `02.08.04.32.01.02.01.04.01` | Inserting a Multibin SmartDisconnect test suite | 先建 universal test method class，再从 fail 分支 Palette 的 `Multibin Disconnect` 插入。 |
| `02.08.04.32.01.02.02` | Flow control nodes | 条件分支与循环：if...then / repeat...until / while...do / for...do；条件是算术/布尔表达式。 |
| `02.08.04.32.01.02.02.01` | Built-in functions | 15 个内建函数，必须小写；见下表。 |
| `02.08.04.32.01.02.03` | Assign Value node | 在 testflow 某点给变量赋值；另有 Assign Level Value / Assign Timing Value。 |
| `02.08.04.32.01.02.04` | Print nodes | Print（Report Window）与 Print to Datalog；字符串不加引号。 |
| `02.08.04.32.01.02.05` | Group node | 把同一层的连续节点收成一个 Group；Group Bypass 会跳过整组；7.1.3 引入 Bypass。 |
| `02.08.04.32.01.02.06` | Bins | stop bin / otherwise bin / floating bin；一个 bin 只能生成一个 hardware bin 与一个 software bin。 |
| `02.08.04.32.01.02.07` | Flags | 四类 flag 总览；逐 flag 见 `.01`。 |
| `02.08.04.32.01.02.07.01` | Alphabetical list of flags | 全量字母序 flag 表：GUI 名 + 文件关键字 + Area + 说明 + 默认值；所有 flag 状态存在 testflow 文件。 |
| `02.08.04.32.01.02.07.02` | Testflow flags | 调试用，按 testflow 生效；`debug_mode`、`global_hold`、`global_overon`、`unburst_mode` 等。 |
| `02.08.04.32.01.02.07.03` | Testflow flags for data logging | 又称 system flags；控制 datalog 与监控，按 testflow 生效。 |
| `02.08.04.32.01.02.07.04` | Test suite flags | 控制该 suite 采集/输出哪些结果；按 suite 生效，默认全不激活。 |
| `02.08.04.32.01.02.07.05` | Site control flags | 改 site focus 或并行/串行；按 suite 生效；存在 testflow 文件的 `test_suites` 段。 |
| `02.08.04.32.01.02.07.06` | Flag priority | 两条：pass level 优先于 fail level；单 suite 的 Set pass / Set fail / Bypass 优先于全局 testflow flags。 |
| `02.08.04.32.01.03` | Hierarchy within a testflow | 分支节点把 flow 分成多个 level；选择/剪切/复制/粘贴不能跨 level。 |
| `02.08.04.32.01.04` | Multiple Sites Execution | 多 site 到同一 suite 时并行进出；有分支时 false（失败）路径总是先执行。 |
| `02.08.04.32.01.05` | Configuring the messages printed in the Report Window | 在 testflow 目录放 `.testflow.ReportUiOutput.user_def`，用 `<passed>` / `<failed>` / `<text>` 控制打印。 |

#### 内建函数（`02.08.04.32.01.02.02.01`）

| 函数 | 作用 |
|---|---|
| `tf_result(<test_suite_name>, <result_index>)` | 取该 suite 结果数组指定下标的值。 |
| `pass(<test_suite_name>)` | suite 通过返回 1，否则 0。 |
| `fail(<test_suite_name>)` | suite 失败返回 1，否则 0。 |
| `has_run(<test_suite_name>)` | 本次 testflow 执行中已跑过返回 1。 |
| `has_not_run(<test_suite_name>)` | 尚未跑过返回 1。 |
| `lsus()` | 已用 level set 数。 |
| `dsus()` | 已用 DPS equation set 数。 |
| `tsus(waveset_no)` | 已用 timing set 数。 |
| `wsus()` | 已用 waveform set 数。 |
| `burstfirst(burstlabel)` | 返回 burst 的第一个 label。 |
| `burstnext(burstlabel)` | 返回 burst 中下一个 label；已是最后一个则返回空串。 |
| `spst_timing(eqst_no, spst_no)` | timing equation set + spec set 组合有效返回 1。 |
| `spst_level(eqst_no, spst_no)` | level equation set + spec set 组合有效返回 1。 |
| `svlr_timing(eqst_no, spst_no, "variable_name")` | 取 timing equation 变量的值。 |
| `svlr_level(eqst_no, spst_no, "variable_name")` | 取 level equation 变量的值。 |

**文档事实**：`Built-in functions must be specified using lower case characters.`

#### 特殊 test suite（`02.08.04.32.01.02.01.02`）

**文档事实**：该篇写 `There are seven types of special test suites.`，但同篇表格实际列出 8 行。**原文如此**，本页按 8 行转述，不替文档改数。

| 类型 | 执行时点 / 作用 |
|---|---|
| `Init` | Download 之后、testflow 第一次运行之前；给测试系统初始设置。 |
| `Download` | testflow 载入后执行；可加载 Setups 页选定的 pin configuration 或其他 setup。 |
| `bin_disconnect` | 器件落入 bin 时执行；若用 `DISCONNECT` API，有自定义 disconnect 序列则执行它，否则执行标准序列；legacy 的失败器件断开方式，新器件建议用 Multibin SmartDisconnect。 |
| `multi_bin_decision` | 一个或多个 site 到达 multi_bin 节点时执行；配合 `SET_MULTIBIN` 决定 bin。 |
| `Abort` | 进入 abort 状态时执行。 |
| `Pause` | 进入 pause 状态时执行；在 application model 的 pause 段之前。 |
| `Reset` | 进入 reset 状态时执行；会 reset 硬件。 |
| `Exit` | 进入 exit 状态时执行；仅当 testflow 由 test program 启动时相关。 |

**文档事实**：`Do not throw any exceptions from inside special test suites, as the handling is not compatible with the testflow executor.`

#### Multibin SmartDisconnect 的附加规则（`02.08.04.32.01.02.01.04`、`.04.01`）

- 插在 **Run and Branch 的 fail 分支**；test method 必须按该 Run and Branch 的硬件设置来写，负责 disable/disconnect 失败 site。
- 进入 `run()` 时 **site mask 已被 SmarTest 反转**：只有对应的 Run and Branch 失败的 site 是 active；离开该 suite 时自动复位为仍通过的 site。
- 失败 site active 期间才使能 DC events；离开该 suite 后 DC events 复位到旧状态并在所有 site 上执行。
- 执行该 test method 前会做一次 **SmartCalc 同步**，确保结果已收集、失败/已断开 site 的线程已停止。
- 必须**在 testflow 末尾再加一个 test suite**，对通过的 site 执行适配的 disconnect 序列；若前一个 Run and Branch 也挂了 Multibin SmartDisconnect，可复用同一个 test method class 做最终 disconnect。
- **不要**与 legacy `bin_disconnect`、user-defined disconnect sequence 混用。
- 插入时在 fail 分支选 `Multibin Disconnect`，用 New Multibin Disconnect Wizard 选 test method；也可把已有 floating suite 接入并指定为 Multibin SmartDisconnect 节点类型（`.04.03.01`）。

#### 四类 flag 的名字清单（逐 flag 细节见 `02.08.04.32.01.02.07.01`）

- **Testflow flags（`02.08.04.32.01.02.07.02`）**：`buffer_testflow_log`、`check_testmethod_api`、`debug_analog`、`debug_mode`、`global_hold`、`global_overon`、`hold_on_fail`、`limits_enable`、`log_cycles_after`、`log_cycles_before`、`multibin_mode`、`parallel_mode`、`set_bypass_level`、`set_fail_level`、`set_pass_level`、`site_match_mode`、`sqst_mode`、`test_number_enable`、`test_number_inc`、`unburst_mode`、`warn_as_fail`。
- **Data logging / system flags（`02.08.04.32.01.02.07.03`）**：`calib_age_monitor`、`current_monitor`、`datalog_formatter`、`datalog_sample_size`、`diag_monitor`、`graphic_result_display`、`hidden_datalog_mode`、`ink_wafer`、`log_events_enable`、`max_reprobes`、`print_wafermap`、`state_display`、`temp_monitor`、`tm_crash_as_fatal`。
- **Test suite flags（`02.08.04.32.01.02.07.04`）**：`bypass`、`fail_per_label`、`value_on_fail`、`ffc_enable`、`ffv_enable`、`frg_enable`、`frg_single_shot`、`ffc_on_fail`、`hold`、`hold_on_fail`、`mx_waves_enable`、`output_on_fail`、`output_on_pass`、`value_on_pass`、`per_pin_on_fail`、`per_pin_on_pass`、`set_fail`、`set_pass`、`site_match`、`test_level`、`override_test_number`。
- **Site control flags（`02.08.04.32.01.02.07.05`）**：`force_serial`（GUI 名 Allow Parallel 的反向）、`site_control`、`size` / `cycle`（SEMIPARALLEL 用）、`#1 … #n`（OTHER 用的 site 执行顺序）、`site_match`。

### 编辑、运行、调试与合并（覆盖 `02.08.04.32.02.*`）

| 分类号 | 文档 | 一句话 |
|---|---|---|
| `02.08.04.32.02` | Using the Testflow Tool | 本章索引：编辑、导航、运行、调试、合并、HRE、配置。 |
| `02.08.04.32.02.01` | Editing a testflow | 编辑操作索引。 |
| `02.08.04.32.02.01.01` | Opening the Testflow Tool | 在 93000 Setup perspective 的 Test Program Explorer 双击 testflow；可只开 Flow Data Editor 或 Flow Sequence Editor。 |
| `02.08.04.32.02.01.02` | Creating a testflow | 两种建法：Flow Sequence Editor 搭序列 + Flow Data Editor 填属性；或先建 floating suite/bin 再接入；前置为 setup 已 load、test method 已 build；**SmarTest 7.0.3 起 classic testflow 不受支持**。 |
| `02.08.04.32.02.01.03` | Selecting setup files | 在 Setups 页逐项选择 pin configuration 等文件；之后 Load All Setups 或单项 Load；6.5.2 起 Testflow Tool 不能创建 setup 文件。 |
| `02.08.04.32.02.01.04` | Inserting a test suite into the testflow | 在插入点用 Palette 的 Run Test / Run and Branch；也可只填 suite 名与 test method，继承前一个 suite 的 primary sets。 |
| `02.08.04.32.02.01.04.01` | Setting up a multiport testsuite | 三段：timing sets（端口序列对应）、level sets（与单端口相同）、multiport burst label；timing set 串如 `"1,2,1,3"`。 |
| `02.08.04.32.02.01.04.02` | Setting up a special test suite | 在 Test Suites 页 Add Special Test Suite；只显示在该页、青色背景；删除按 Delete。 |
| `02.08.04.32.02.01.04.03` | Creating a floating test suite | 在 Test Suites 页 Add Test Suite 或复制现有 suite；灰色背景；不在序列里。 |
| `02.08.04.32.02.01.04.03.01` | Connecting a floating test suite to the testflow | 在插入点 Insert Floating Test Suite；可选插入本体或副本、Run / Run and Branch / Multibin SmartDisconnect 节点类型。 |
| `02.08.04.32.02.01.05` | Inserting a bin into the testflow | stop bin 用 Palette 的 goodbin / badbin；floating bin 在 Bins 页 Add Bin；multibin 用 Palette 的 Multi Bin；每个 testflow 默认有 otherwise bin；**CCF block 内的所有 test suite 必须使用 multibin**。 |
| `02.08.04.32.02.01.06` | Editing a test suite in the Flow Data Editor | 在 Test Suites 页改 name、primary sets、test setup、flags；可复制粘贴（special suite 不能改名、不能复制粘贴）；FFV/FRG 等子 flag 依赖 FFC enable。 |
| `02.08.04.32.02.01.07` | Adding a limit on the Tests page | Tests 页 Add Limit；可选 6 个默认 limit 或自定义；单位如 `1.05[mV]` 或 `1.05 mV`。 |
| `02.08.04.32.02.01.08` | Adding a limit in the Properties view | 从 Test Suite > Test Method > Limits 右键 New；结果同步显示在 Tests 页。 |
| `02.08.04.32.02.01.09` | Adding limits in a TMLimits test table | 在 Test Program Explorer load/open TMLimits CSV（或其 .mfh），用 test table editor 改；可加 `Test mode` 行。 |
| `02.08.04.32.02.01.10` | Selecting pins in the Properties view | 对 `PinString` 类型参数选 `@`（全部适用 pin）或任意单 pin 列表。 |
| `02.08.04.32.02.01.11` | Working with nodes | 节点类型全集：Run、Run and branch、Good bin、Bad bin、Multibin、Print、Print to Datalog、If/Then、Repeat、While、For、Assign Value、Assign Level Value、Assign Timing Value。 |
| `02.08.04.32.02.01.11.01` | Narrow selection and wide selection | narrow 只选节点本身，wide 连同子分支；wide 执行行为像跑整个 testflow，但**忽略 binning**；调试结果需要 wide；Ctrl+点击或 Ctrl+Right/Left 切换。 |
| `02.08.04.32.02.01.11.02` | Inserting a node | 点插入点变红 → Palette 选节点 → 填向导 → Finish。 |
| `02.08.04.32.02.01.11.03` | Deleting nodes | 选中后 Delete；Run/Run and Branch 必须 wide 选；可在确认框把 suite 转为 floating；普通 suite 不能在 Flow Data Editor 删除。 |
| `02.08.04.32.02.01.11.04` | Cutting, copying and pasting nodes | 同层才能一起选；粘贴的 suite 名加数字后缀，是副本而非 clone。 |
| `02.08.04.32.02.01.11.05` | Moving nodes | 选中同层节点 → 右键 Move 到插入点；Ctrl+Z 撤销。 |
| `02.08.04.32.02.01.11.06` | Cloning nodes | Paste As Link；只可 clone suite 与 bin 节点；suite clone 共享同一 suite（Linked test suite），bin clone 不新增 Bins 页行。 |
| `02.08.04.32.02.01.11.07` | Grouping nodes | 把同一层连续节点收进 Group；只影响显示，不改变功能。 |
| `02.08.04.32.02.01.12` | Working with variables | 变量章索引。 |
| `02.08.04.32.02.01.12.01` | Defining variables | 必须先在 Variables 页建变量，才能在 testflow 里使用；6.5.2 起不支持只在 Assign Value 节点隐式定义。 |
| `02.08.04.32.02.01.12.02` | Deleting variables | 变量必须已定义且未被任何节点使用，才能删除。 |
| `02.08.04.32.02.01.12.03` | Assigning values to variables | 两种方式：Assign Value 节点；或在 Variables 页改 Current Value。 |
| `02.08.04.32.02.01.12.04` | Assigning a level or timing spec value | 用 assign level value / assign timing value 节点，填 equation set、spec set、变量与值。 |
| `02.08.04.32.02.01.12.05` | Changing spec values at run time | 可用固件命令 `SVLR`，或 Flow Sequence Editor 的 New Assign Level/Timing Spec Wizard；multiport 需 equation set 与 spec set 号。 |
| `02.08.04.32.02.01.13` | Printing a graphical representation of the testflow | File > Save as picture，把 Flow Sequence Editor 存为图片（如 `testflow.jpg`）。 |
| `02.08.04.32.02.01.14` | Identifying fail labels in a burst | burst 模式一次跑多个 label；用 `unburst_mode` flag 或 for 循环 + `burstfirst` / `burstnext` 定位失败 label。 |
| `02.08.04.32.02.01.15` | Importing a testflow from a CSV file | Test Program Explorer 右键 testflow → Import；**不要取消勾选 Setups 列表任一项**，否则报错并阻止导入。 |
| `02.08.04.32.02.01.16` | Exporting a testflow to a CSV file | 右键 testflow → Export；可勾选导出内容；若要再导回 SmarTest，Setups 列表必须全勾。 |
| `02.08.04.32.02.02` | Navigating a testflow | 书签、Filter 行、Navigate > Go To、Next/Previous Annotation。 |
| `02.08.04.32.02.02.01` | Searching for test suites, bins and variables | Navigate > Go To > Test Suite / Bin / Group / Variable；也可 Ctrl+F 在 Flow Data Editor 页查找。 |
| `02.08.04.32.02.03` | Running a testflow | Run 对话框跑 Testflow (Full) / (Selection) / (User Defined)；可设 loop、Stop On Fail/Pass、single step、Response Emulator。Loop 执行时 testflow 变量与 user flags **不在每轮结束复位**，只在第一次循环开始时复位；整条 testflow 的 loop 每轮结束都会 disconnect，单 suite 的 loop 不 disconnect（除非 test method 自己编程）。 |
| `02.08.04.32.02.03.01` | Loop configuration settings | Loop 区：Enable、Count、Loop Indefinitely、Stop on Fail、Stop on Pass、Log Loop Number、Pause between loops。 |
| `02.08.04.32.02.03.02` | Using the Overon feature while running a testflow | 设 `global_overon` 为 on，并在不需要的 bin 上关掉 overon；testflow 会越过 stop bin 继续。若该 stop bin 是 flow 的最后一个 bin，器件会继续进入 otherwise bin；overon 也可用于条件表达式。 |
| `02.08.04.32.02.03.03` | Checking the execution flow | 两种方式：HRE 预设 pass/fail；或在每条路径插 Assign Value 节点计数，并把计数表达式写进 bin description。 |
| `02.08.04.32.02.03.04` | Measuring the test time | 设 `debug_mode` 为 3 或 4；线性 flow 设 `global_overon` 与所有 stop bin 的 overon；用 sublevel_dialog application model 起 workorder。 |
| `02.08.04.32.02.03.05` | Adding user defined testflows to the Run menu | Run > Open Run Dialog → 选 testflow → Common → Display in favorite menu 选 Run → Apply。 |
| `02.08.04.32.02.04` | Debugging a testflow | 打开 Testflow Tool 时自动显示 Debug view；设 `debug_mode` 控制 Report Window 信息级别；多 site 用 Site Control Window。 |
| `02.08.04.32.02.04.01` | Single step testflow debugging | Debug view 的 Suspend / Step Over / Resume / Terminate；full testflow 不能直接单步，需先 Run and Hold after here。文档**不推荐**用 hold flags 做调试（会改 testflow 内容、弹窗可能被主窗口遮住、恢复前要清除所有 hold flag、loop 不能逐轮单步）。 |
| `02.08.04.32.02.05` | Merging the testflows | 从 source 向 target 复制元素；Flow Sequence Editor 或 ASCII Interface 两种工具；缺变量时弹 Add New Variables。 |
| `02.08.04.32.02.05.01` | Source and target testflows | 只能 source→target 单向复制；source 只读、不能执行或修改。 |
| `02.08.04.32.02.06` | Hardware Response Emulator | 解决离线调试两个问题：API 返回随机数据、无法控制每个 suite 的 pass/fail；分 Import / Store 模式。 |
| `02.08.04.32.02.06.01` | Preparing Hardware Response files | 在线 Store 模式跑 testflow，为所有 suite 与取数 API 生成响应文件；可设 HW Response Directory、时间戳、目标 suite。 |
| `02.08.04.32.02.06.01.01` | ARRAY_X type | Store 模式下 DGT 波形类（getWaveform / getComplexWaveform / getDebugWaveform）、TIA.getResult 与 Vector.getVectors 的响应文件编辑对话框。 |
| `02.08.04.32.02.06.01.02` | DOUBLE type | TIA 的 getMean/getMin/getMax/getJitter 与 getValue 的单值响应对话框。 |
| `02.08.04.32.02.06.01.03` | SpecSearch type | SPEC_SEARCH.execute() 与 SEARCH_FUNC_TASK.execute() 的响应对话框，填 result spec / passval / failval。 |
| `02.08.04.32.02.06.01.04` | DC API type | DC API 类（`PMU_IFVM`、`PMU_VFIM`、`DPS_VFIM`、`PPMU_MEASURE`、`DPS_TASK`、`SPMU_TASK`）的测量值响应对话框。 |
| `02.08.04.32.02.06.01.05` | FW_TASK type | `FW_TASK(command, answer)` 的固件任务响应对话框。 |
| `02.08.04.32.02.06.01.06` | Pass/Fail type and ERROR_MAP type | 为 suite 或 API 指定虚拟 pass/fail 与 error map。 |
| `02.08.04.32.02.06.02` | Using hardware response files for execution | Run 对话框 Response Emulator 区 Enable + Import mode；缺文件时弹对话框要求指定数据。 |
| `02.08.04.32.02.06.03` | Hardware response files | 响应数据文件；文件名 `Testsuite;MAPI; call#; site#`，可省略 call#/site# 表示全匹配。 |
| `02.08.04.32.02.06.04` | Supported test suites and test method APIs | 支持模拟的 API 清单：`ANALOG` 或 `ANALOG_STATUS` 类的 DGT / TIA、Vector、SpecSearch、DC APIs、FW_TASK、GET_FUNCTIONAL_RESULT、TEST、SEARCH_FUNC_TASK、PATTERN_CONTROLLER；其他成员函数不支持。 |
| `02.08.04.32.02.07` | Configuring the Testflow Tool | 在 Window > Preferences 配置 Testflow Tool 与相关 preference 页。 |

### 工具元素与文件格式（覆盖 `02.08.04.32.03.*`）

| 分类号 | 文档 | 一句话 |
|---|---|---|
| `02.08.04.32.03` | Elements of the Testflow Tool | 两个编辑器：Flow Data Editor 与 Flow Sequence Editor。 |
| `02.08.04.32.03.01` | Flow Data Editor | 八个页签的表格编辑器。 |
| `02.08.04.32.03.01.01` | Test Suites page | 加/删 special 与 floating suite，编辑所有 suite 设置；Result 列显示颜色边框；有 annotation bar（bookmarked / executed / passed / failed / invalid 等）与 Validate setups、Check Inconsistency 按钮。 |
| `02.08.04.32.03.01.02` | Parameters page | 显示 test method 参数；Action Name 为 `proj.class`；要显示参数必须先 build test method library。 |
| `02.08.04.32.03.01.03` | Tests page | 显示 test method 定义的 result limit 范围；可加多个 limit；Test Name 取自 TEST API 的 testname。 |
| `02.08.04.32.03.01.04` | Bins page | 三类 bin：stop、special（青底）、floating（灰底）；每 testflow 默认 otherwise bin；只能加/删 floating bin。 |
| `02.08.04.32.03.01.05` | Variables page | DOUBLE / STRING / USERFLAG 三类；Initial Value 在手动跑 testflow 或启动 test program 时赋值；Current Value 可在执行中改。 |
| `02.08.04.32.03.01.06` | Flags page | 设 system flags 与 testflow flags；也可从 Operation Control 的 Production Settings 进入。 |
| `02.08.04.32.03.01.07` | Setups page | 显示当前 testflow 的 primary setup 文件；无效文件黄色高亮（未 load 或不存在）。 |
| `02.08.04.32.03.01.08` | Information page | 编辑 description、device name、device revision、test revision；供 application model 等使用；可用 `GET_TEST_INFO` 查询这些信息。 |
| `02.08.04.32.03.02` | Flow Sequence Editor | 图形化显示 testflow，左侧 Palette 插入组件；可缩放。 |
| `02.08.04.32.03.03` | Synchronization between the Flow Data Editor and the Flow Sequence Editor | 两个编辑器与 Flow Data Editor 各页自动同步；不同步时检查配置。 |
| `02.08.04.32.03.04` | Testflow Properties view | 显示 testflow / suite / bin / group / 节点属性；含 Site Control 的 PARALLEL / SERIAL / SEMIPARALLEL / OTHER / UNDEF（OTHER 与 UNDEF 只能在这里设）；无效 primary set 黄色高亮。 |
| `02.08.04.32.03.05` | Testflow file | testflow 文件语法（BNF）、range check、`## Syntax`、`## Example`；存于 `<device_dir>/testflow`。 |
| `02.08.04.32.03.06` | Testflow master file | 单文件或拆成子文件；母文件第一行 `hp93000,testflow_master_file,0.1`，第二行 `testerfile:`；group 名冲突可由 setup management tool 自动改名或由 `REMAP` 指定新名；跨 setup 文件的 bind 需在母文件里手写 `[Bind: ...]`（`01.01.07.02.02.04.05.04`）。 |
| `02.08.04.32.03.06.01` | Top-level control structures | 母文件顶层可加 `if` / `for` / `while` / `repeat until` 控制结构，assemble 时加入、split 时忽略。 |

## L1 — Firmware / Setup Command

### 边界结论

**判断**：本次**未找到** `02.06 Command Reference` 下的 testflow 专属命令子树。testflow 的 L1 级接口是 **testflow 文件与 testflow 母文件的配置语句**；此外，本阶段实际调用两条散落在别章的固件命令（`SVLR`、`PACT`），列在最后。**文档事实**：`02.08.04.32.03.05` 自带 `## Syntax`，以 BNF 定义 testflow 文件；`02.08.04.32.03.06` 与 `.03.06.01` 定义母文件条目与顶层控制结构。

**文档事实**：`02.08.04.32.03.05` 说明 testflow 文件是文本文件，可直接用文本编辑器改，但**推荐只用 Testflow Tool 改**：

> Since the testflow file is a text file, you can change parameters directly using a text editor. However, we recommend changing the settings only by the Testflow Tool of the SmarTest Work Center.

**推断**：把文件语句当 L1 的理由是——它是本阶段唯一可直接书写、可版本化、可被外部程序生成的配置级接口；L2/L3 都是运行期控制，不生成 testflow 序列本身。

### testflow 文件的段落（`02.08.04.32.03.05`）

BNF 顶层 `<section>` 的全部取值如下。每个段落在文件里写作 `关键字 ... end`（BNF 用 `{ ... | ... }` 表示备选，不是要求写字面花括号）。

| 段落 | 作用 |
|---|---|
| `information` | description、device_name、device_revision、test_revision。 |
| `declarations` | `@<var_name> = <expression>` 或 `@<var_name> = <string>`；var_name 可为 label、flag_name、`<test_suite>.<ts_flag>`、`* <test_suite>.ffc_on_fail`。 |
| `flags` | `<flag_name> = <flag_value>;` 或 `user <user_flag_name> = <flag_value>;`。 |
| `tests` | `<test_label>:`，可带 `user_procedure = "<user parameters>";`。 |
| `testfunctions` | test function 的描述与参数。 |
| `datasets` | `<dataset_label>:`，可带 `file = "<dataset_file>";`。 |
| `test_suites` | 每个 test suite 的 datasets / tests / test_level / local_flags / override 系列 / site_match / site_control。 |
| `initialize` | 特殊段落：一个 `<test_suite_entry>`。 |
| `download` | 特殊段落：一个 `<test_suite_entry>`。 |
| `abort` | 特殊段落：一个 `<test_suite_entry>`。 |
| `pause` | 特殊段落：一个 `<test_suite_entry>`。 |
| `reset` | 特殊段落：一个 `<test_suite_entry>`。 |
| `exit` | 特殊段落：一个 `<test_suite_entry>`。 |
| `test_flow` | 可执行语句序列；见下表。 |
| `binning` | otherwise bin 的定义。 |
| `context` | 各 setup 文件的引用（config / analog_control / attrib / channel_attrib / levels / mixsgl / protocols / routing / testtable / timing / vector / waveform）。 |
| `hardware_bin_descriptions` | `<integer> = <string>;` 的硬件 bin 描述。 |

**文档事实**：文件首部为 `hp93000,testflow,0.1`；示例中还出现 `language_revision = 1;`（`02.08.04.32.03.05` 的 `## Example`）。

### `test_flow` 段的语句（L1 核心）

下列各条是 `02.08.04.32.03.05` 的 `<statement>` 产生式中的备选，分行摘录（不是整段逐字；原文用 `|` 与花括号组织备选，此处已省略）：

```text
<assignment> := @<var_name> = <expression> | @<var_name> = <string>
run(<test_suite>)
run_and_branch(<test_suite>) then <statement> [else <statement>]
print(<print_expression>)
print_dl(<print_expression>)
if <expression> then <statement> [else <statement>]
while <expression> do <statement>
for <assignment>;<expression>;<assignment>; do <statement>
repeat <statement>; until <expression>
'{' <statement> [;<statement>]... '}' [[<compound_state>], [<compound_label>], [<compound_description>]]
stop_bin1)(<major_bin>, <minor_bin>, , <good_flag>, <reprobe_flag>, <color>, <physical_bin>[, <over_on_flag>]);
otherwise bin2) = <major_bin> <minor_bin>, , <good_flag>, <reprobe_flag>, <color>, <physical_bin>[, <over_on_flag>] ;
```

| 语句 | 一句话作用 |
|---|---|
| `@var = expression` / `@var = "string"` | 给 testflow 变量赋值。 |
| `run(<test_suite>)` | 顺序执行一个 test suite，不按结果分支。 |
| `run_and_branch(<test_suite>) then ... [else ...]` | 按该 suite 的 pass/fail 走 then 或 else 分支。 |
| `print(<print_expression>)` | 把表达式或字符串打印到 Report Window。 |
| `print_dl(<print_expression>)` | 打印到 Datalog。 |
| `if <expression> then ... [else ...]` | 条件分支。 |
| `while <expression> do ...` | 条件循环。 |
| `for <assignment>;<expression>;<assignment>; do ...` | 计数循环。 |
| `repeat ...; until <expression>` | 至少执行一次，直到条件成立。 |
| `{ ... }` | 复合语句块，可带 open/closed、label、description。 |
| `stop_bin` / `otherwise bin` | 把器件放入 good/bad bin 或 otherwise bin；带 over_on 标志。 |

**原文如此**：BNF 里 `stop_bin` 一行写作 `stop_bin1)(`、`otherwise bin` 一行写作 `otherwise bin2)`；这是源文档的拼写，不是本页改写。**建议**：用 GUI 生成这两行，避免手写。**文档事实**：同篇 `## Example` 还出现一个 `implicit_declarations` 段，但顶层 `<section>` 产生式没有列它；原文如此。

**文档事实**：表达式支持 `+` `-` `*` `/` `>` `>=` `<` `<=` `==` `!=` `(` `)` `and` `or` `not`；操作数支持 `pass()`、`fail()`、`tf_result()`、`has_run()`、`has_not_run()`、`wsus()`、`tsus()`、`lsus()`、`dsus()`、`bsus()`、`@<var_name>`、实数、字符串。注意 BNF 里 `bsus()` 出现在表达式操作数中，但内建函数正文的清单没有 `bsus()`；**两处不一致，原文如此**。

### testflow 母文件的条目（`02.08.04.32.03.06`、`.03.06.01`）

```text
hp93000,testflow_master_file,0.1
testerfile: <tester_file_name>
GROUP <group_name> [open|closed]: <file_name>
information: <file_name>
bins: <file_name>
flags: <file_name>
setup: <file_name>
VAR <variable_name>: <file_name>
VAR_default: <file_name>
```

| 条目 | 作用 |
|---|---|
| `GROUP <name> [open\|closed]: <file>` | 把 group 子文件接入母文件；`open`/`closed` 只影响编辑器显示。 |
| `information: <file>` | 全局 information 段，只能出现一次。 |
| `bins: <file>` | 全局 bins 段，只能出现一次。 |
| `flags: <file>` | 全局 flags 段，只能出现一次。 |
| `setup: <file>` | 全局 setup 段，只能出现一次。 |
| `VAR <name>: <file>` | 指定变量所在子文件。 |
| `VAR_default: <file>` | 未显式列出的变量都收到这里；同篇示例写作 `VAR_Default`，原文如此。 |

**文档事实**：母文件里可以放注释（行首 `#`）；子文件路径可相对或绝对，相对路径以母文件目录为基准；单独 test suite 或 bin 不能拆成子文件，所以顶层对象必须是 group。自动生成的 group 子文件名为 `group_<group_name>.tfl`，可用环境变量 `VERIGY93000_MFH_PREFIX` 加前缀（`02.08.04.32.03.06`）。

**顶层控制结构（`02.08.04.32.03.06.01`）**：

| 结构 | 写法 |
|---|---|
| `if` | `if @myvar = 1` … `endif` |
| `for` | `for @myvar = 0; @myvar < 10 ; @myvar = @myvar + 1` … `endfor` |
| `while` | `while @myvar <= 10` … `endwhile` |
| `repeat until` | `repeat until @myvar = 0` … `endrepeat` |

**文档事实**：母文件里的 testflow 变量必须带 `@` 前缀；`for` / `while` 可在行尾加分号后写 `testnumber_increment = <number>`，用于 STDF 测试编号（`if` 与 `repeat` 段内也可写）；这些控制结构在 assemble 时加入、split 时被忽略。

### 散落的 L1 固件命令（本阶段实际使用）

| 命令 | 在本阶段的作用 | 出处 |
|---|---|---|
| `SVLR` / `SVLR?` | 运行期设置 level/timing 的 base（spec）变量并重算；新值在下一次 functional test 开始时生效；不改 setup 值。testflow 的 Assign Level/Timing Spec 节点与它对应。 | `02.06.05.02.24`、`02.08.04.32.02.01.12.05` |
| `PACT` / `PACT?` | mask/activate site；Site Control 窗口使用，也在 test suite 要求串行、或分支后不同 site 走不同路径时用于 testflow 执行。**每次 PACT 都会重置所有 site 的结果**；文档注明它实现 tpi 接口，建议改用 tpi call。 | `02.06.03.02.16` |

**建议**：testflow 里优先用 `Assign Level Value` / `Assign Timing Value` 节点表达运行期 spec 变更，把 `SVLR` 留给调试或确有必要的手写文件；不要用 `PACT` 做 site 控制的唯一手段，文档自己指向 tpi 接口。

**文档未覆盖**：`02.06 Command Reference` 中没有「创建 testflow」「下载 testflow」「执行 testflow」的固件命令；本次未找到这类命令章。不要把它们编进 L1。

## L2 — Test Method API

**文档事实**：`02.07.01.01.01` 把 test method 的典型流程固定为五步（改 setup、执行、取原始数据、计算、判定），并说明另有控制测试序列、访问 flag 与变量、多 site、多 port、GPIB、从 test method 执行固件命令的 API。本阶段用到的 L2 集中在「读/写 flag、读/写 testflow 变量、bin、当前 suite 身份、disconnect 上下文」几族。

| API | 在本阶段做什么 | 关键约束 / 出处 |
|---|---|---|
| `SET_TESTFLOW_FLAG(const STRING& flag, INT value)` | 运行期改 testflow flag。 | `Changing the flag state will be valid at the execution of the next test suite.`（`02.07.04.01.217`） |
| `GET_TESTFLOW_FLAG(const STRING& flag, INT *value)` | 读 testflow flag 当前值。 | 头文件 `MAPI/TestControl.h`（`02.07.04.01.96`）。 |
| `SET_TESTSUITE_FLAG(const STRING& tsname, const STRING& flag, INT value)` | 改指定 test suite 的 flag。 | `Change of any flag state will be valid when the next testsuite is executed.`；部分 flag 只读，不能 set（`02.07.04.01.219`）。 |
| `GET_TESTSUITE_FLAG(...)` | 读 test suite flag；只读/可写属性以该篇为准。 | `02.07.04.01.219` 指向它。 |
| `SET_MULTIBIN(const char* softbin, int hardbin)` | 在 test method 里为 multibin 选择 bin。 | 要求 fail 分支已插 multibin 图标，且所用 bin 是 testflow 里的普通或 floating bin；同一 test method 里最后一次 `passed = false` 的调用覆盖之前的调用；**不要在 SmartCalc 框架里使用**（`02.07.04.01.212`）。若 bin 未定义，multibin 会落到 otherwise bin（`02.08.04.32.02.01.05`）。 |
| `GET_MULTIBIN` / `RESET_MULTIBIN` | 读 multibin 的 soft/hard bin；复位为 soft bin 空串、hard bin -1。 | `02.07.04.01.91`、`.188`。 |
| `GET_BIN` | 取器件已到达的 bin 的 software/hardware bin 号；overon 时取第一个到达的 bin。 | `02.07.04.01.80`。 |
| `GET_CURRENT_BIN_INFORMATION` | 取当前 bin 的完整信息（hw/sw number 与 description、good、reprobe、overon、otherwise）。 | **只能用在 special test suite `bin_disconnect` 的 test method 里**（`02.07.04.01.82`）。 |
| `SET_USER_FLAG` / `SET_USER_DOUBLE` / `SET_USER_STRING` | 写 testflow 的 user flag、double、string 变量。 | `02.07.03.08.05`。 |
| `GET_USER_FLAG` / `GET_USER_DOUBLE` / `GET_USER_STRING` | 读上述变量当前值。 | `02.07.03.08.06`。 |
| `GET_TESTSUITE_NAME` | 取当前正在运行的 test suite 名。 | `02.07.03.08.09`。 |
| `GET_DISCONNECT_CONTEXT()` | 判断当前 test method 是作为普通 suite 还是 disconnect 上下文运行；返回 `TM::IN_FLOW` / `GOOD_BINNING` / `FAIL_BINNING` / `DEFAULT_BINNING` / `TESTMETHOD_ERROR` / `TESTFLOW_ABORT`。 | 支持 `bin_disconnect` 与 Multibin SmartDisconnect；普通 suite 只会返回 `IN_FLOW`（`02.07.04.01.84`、`02.08.04.32.01.02.01.04.01`）。 |
| `DISCONNECT` | 断开测试资源并置为 disconnect 状态；在 special test suite `bin_disconnect` 里执行。 | 多 site 时必须放在 first-invocation 块、不能放在 `each site` 循环块；不要与单独 relay 切换混用（`02.07.04.01.41`、`02.08.04.32.01.02.01.02`）。 |
| `TEST` / `PUT_DATALOG` 的 pin name 参数 | 当 `check_testmethod_api` 为 on 时，未定义的 pin name 会导致运行期 fatal error。 | `02.08.04.32.01.02.07.02`。 |
| `SET_EXCEPTION_HANDLER` | 处理 `check_testmethod_api` 产生的异常。 | `02.08.04.32.01.02.07.02`；7.3.3.1 起异常处理已简化，不再必须注册（`02.07.04.01.210`）。 |
| `ERROR_EXIT` | 按 `TM::EXIT_TYPE` 立即结束当前 testflow / test program（ABORT_FLOW、EXIT_FLOW、EXIT_TO_BIN、RETURN_TO_FLOW、RETRY、INTERACTIVE、THROUGH、NONE）。 | **不要在 special test suite 内使用**，与 testflow executor 不兼容（`02.07.04.01.61`）。 |

**文档事实**：`SET_TESTFLOW_FLAG` 与 `SET_TESTSUITE_FLAG` 的生效点都是**下一个 test suite**，不是当前 suite；这是本阶段最容易误判的运行时序。**建议**：在 suite 的 `ON_FIRST_INVOCATION` 之外改 flag，或把 flag 改动放在目标 suite 之前的独立节点/suite 里。

**文档事实**：`02.07.04.01.219` 提示 test suite flag 中有若干 read-only flag 不能用 `SET_TESTSUITE_FLAG` 设置。哪些 flag 只读，以 `GET_TESTSUITE_FLAG` 篇为准；本页不逐条抄该表。

**文档未覆盖**：本次未找到「用 Test Method API 创建/删除 test suite 或修改 testflow 序列」的 API。L2 只能改运行期状态与变量；结构编辑属于 GUI 或 L3 Test Suite Control API。

## L3 — 外部控制

**L3 入口是横切的，能力面按阶段分族。** Test Suite Control API、HVM API、BLC API、TPI Program Routines 都是跨阶段的入口；本阶段的专属族是「test suite 级控制 + testflow 下载/执行 + testflow 文件管理」。

### Test Suite Control API（`02.09.01.14`）

**文档事实**：

> Test suite control API is used to directly control the test suites outside of the testflow tool.

> Only UTM-based test suites are supported with these APIs.

> This is a set of independent APIs. They cannot be used in test method programming and also cannot be used in parallel with HVM API and BLC API by the same client process.

> Running test suite control API interactively with testflow UI tool is NOT recommended.

**前置**：SmarTest 6.5.2 或更高；C++ 程序包含 `testsuitecontrol_api.hpp`，使用命名空间 `testsuitecontrol`；在 run shell（`/opt/hp93000/soc/system/bin/run -S`）中编译；链接 `-ltestsuitecontrol_api`（`02.09.01.14.01`）。

**会话级函数**：`initializeSession()`、`detachSession()`、`exitProcess()`、`getTestsuite(name)`、`getAllTestsuiteNames()`、`getSpecialTestsuite(...)`、`createFloatingTestsuite(name)`、`deleteFloatingTestsuite(name)`、`selectTestmethodExecutor(...)`、`getTestmethodExecutorIndex()`、`setSiteInFocus(site)`、`getSiteInFocus()`、`setActiveSites(set<int>)`、`getActiveSites()`（`02.09.01.14.02`）。

**`TestsuiteProxy` 成员**（`02.09.01.14.02.01`）：

| 族 | 成员 |
|---|---|
| 执行 | `executeActiveSites()`、`executeSiteInFocus()`、`isExecuted()`、`isPass(site)` |
| 身份 | `getName()`、`setName()` |
| test method | `attachTestmethod()`、`getTestmethodName()`、`getTestmethodParameterNames()`、`getTestmethodParameterValue()`、`setTestmethodParameterValues()`、`getTestmethodDefaultLimitNames()`、`getTestmethodUserDefinedLimitNames()`、`getTestmethodLimitValue()`、`setTestmethodLimits()` |
| level | `getLevelEquation()`、`getLevelSpec()`、`getLevelSet()`、`setEquationBasedLevel()` |
| timing | `getTimingEquation()`、`getTimingSpec()`、`getTimingSet()`、`setEquationBasedTiming()`、`setMultiportTiming()`、`isMultiportTiming()` |
| 其他 setup | `getAnalogSet()`、`setAnalogSet()`、`getSequencerLabel()`、`setSequencerLabel()` |
| flag / site | `getTestsuiteFlag()`、`setTestsuiteFlag()`、`getSiteMatch()`、`setSiteMatch()` |

**推断**：这族 API 让外部程序在不打开 Testflow Tool 的情况下，对当前 testflow 里的现有 suite 做「改 setup → 执行 → 读 isPass」；它**不**创建 testflow 序列，也不替代本阶段的结构编辑。

### 同步 testflow 执行 API（BLC 族，`02.09.01.11.03.06`）

| API | 作用 | 约束 / 错误 |
|---|---|---|
| `DownloadTestflowSync` | 同步下载 testflow setup 文件；每个 testflow 调用一次。 | 调用时状态变 LOADING，结束变 WAITING；`FILE_NOT_FOUND` 表示 testflow 不存在（`02.09.01.11.03.06.01`）。 |
| `ExecuteTestflowSync` | 同步执行 testflow。 | **必须在 `DownloadTestflowSync()` 之后**；状态须为 WAITING，否则 `ILLEGAL_OPERATION`；可选 `SITE_ID_FOR_SITES` 与 `SITE_SETUP_FOR_SITES`（`02.09.01.11.03.06.02`）。 |
| `GetTestflowInformation` | 查询已下载 testflow 的 device name/version、description、test revision。 | `The information can only be successfully queried after a testflow is downloaded.`（`02.09.01.11.03.12.03`） |

**文档事实**：`02.09.01.11.03.06` 说明这些 API 同步下载并执行 testflow，另有 HVM API 用于异步执行。

### HVM Test Execution API（`02.09.01.10.03.02.02`）

| API | 作用 | 约束 |
|---|---|---|
| `LoadTestflowSync` | 把 testflow 载入 SmarTest（不下载 setups），可指定替代 setup 元素。 | 需要 device 已设置；替代类型限 `SETUP:LEVEL` / `SETUP:TIMING` / `SETUP:VECTOR` / `SETUP:PIN_CONFIG` / `SETUP:PIN_ATTRIBUTE` / `SETUP:WAVEFORM` / `SETUP:ROUTING` / `SETUP:ANALOG_CONTROL` / `SETUP:CHANNEL_ATTRIBUTE`（`02.09.01.10.03.02.02.30`）。 |
| `DownloadTestflow` | 把指定 testflow 及其全部 setup 文件下载到 tester；过程中发异步事件。 | 需要 device 已设置；不指定 testflow name 时须先 `LoadTestflowSync` / `LoadTestprogramSync` 或已有 testflow 载入（`02.09.01.10.03.02.02.19`）。 |
| `ExecBLC` | 异步执行一个 BLC 可执行客户端。 | 可等 HVM 事件 `TESTPROGRAM_EXEC_STARTED` 判断是否在跑；要求 SmarTest 状态 idle（`02.09.01.10.03.02.02.21`）。 |

**文档事实**：`DownloadTestflow` 会发 `TESTFLOW_DOWNLOAD_STARTED` / `TESTFLOW_DOWNLOAD_COMPLETED`，每个 setup 文件还会发 `SETUPFILE_DOWNLOAD_STARTED` / `SETUPFILE_DOWNLOAD_COMPLETED`。

### TPI Program Routines（`02.09.01.09`）

| 入口 | 作用 |
|---|---|
| `DataManager(dm_testflow, ...)` | TPI 的 testflow 文件操作：`dm_load` / `dm_save` / `dm_utd` / `dm_delete` / `dm_optimize` / `dm_del_optimize` / `dm_optimize_utd` 等（`02.09.01.09.02`）。 |
| `GetLoadedTestflowName()` | 返回当前载入的 testflow 名；没有则空串（`02.09.01.09.12`）。 |
| `GetTestflowRevisionInfo(path, info)` | 解析 testflow 文件，取 description / device_name / device_revision / test_revision（`02.09.01.09.17`）。 |

**版本注意**：`DataManager` 仍列 `dm_optimize` 系列，但 `02.08.04.32.02.03.04` 的 Functional changes 写明 `SmarTest 7.1.0: Removed testflow optimization function`。**推断**：7.10.3 上不要依赖 optimized testflow 这一路径；以 `dm_load` / `dm_save` 为可用基线。

### SmartShell（7.10.3 不存在）

**文档事实**：`02.15` 的 Functional changes 逐字为 `Introduced in SmarTest 8.2.5`。本 wiki 面向 SmarTest 7.10.3，因此 SmartShell **不能**作为本阶段的 L3 入口；本页不据它写任何执行步骤。

### L3 覆盖结论与未覆盖项

- **文档未覆盖**：本次未找到 TPI 中「创建/编辑 testflow 序列」的 routine；`DataManager` 只提供文件级 load/save/delete/optimize 操作。
- **本次未找到**：HVM 的异步 testflow 执行命令清单（`02.09.01.11.03.06` 只说 `There are also some HVM APIs defined to execute the testflow asynchronously.`，未在该篇列出）。已找到的相邻 API 是 `LoadTestflowSync` / `DownloadTestflow` / `ExecBLC`。
- **建议**：外部自动化优先用 Test Suite Control API 做 suite 级设置与执行、用 BLC 同步 API 做整条 testflow 的下载/执行；Test Suite Control API 不能与 HVM API 或 BLC API 在同一客户端进程中并行使用，且不要和 Testflow UI 同时交互（`02.09.01.14`）。

## 产物

| 产物 | 位置 / 格式 | 说明 |
|---|---|---|
| **testflow 文件** | `<device_dir>/testflow/<testflow_name>`；文本，首行 `hp93000,testflow,0.1`。 | 本阶段主产物；包含 information / declarations / flags / tests / test_suites / test_flow / binning / context 等段（`02.08.04.32.03.05`）。文档示例文件名为 `demo.tf`、路径 `/home/device_demo/testflow/demo.tf`（`02.09.01.09.17`）；扩展名不是本页的规定。 |
| **testflow 母文件 + 子文件** | 母文件 `.mfh`（首行 `hp93000,testflow_master_file,0.1`）；子文件如 `group_<name>.tfl`。 | 多用户并行编辑时使用；母文件用 `GROUP` / `information` / `flags` / `bins` / `setup` / `VAR` 引用子文件（`02.08.04.32.03.06`）。 |
| **CSV 导出** | 任意路径；逗号分隔，含 `$,Testsuites` / `$,Parameters` / `$,Tests` / `$,Bins` / `$,Variables` / `$,Flags` / `$,Setups` / `$,Information` / `$,FlowSequence` 九段。 | 用于报表、文档、复用与跨平台交换（`02.08.04.32.02.01.16`）。 |
| **testflow 图片** | 用户指定路径，如 `testflow.jpg`。 | Flow Sequence Editor 的图形表示（`02.08.04.32.02.01.13`）。 |
| **Report Window 消息配置** | `<DeviceDirectory>/testflow/.testflow.ReportUiOutput.user_def`。 | `<passed>` / `<failed>` / `<text>` 三标签；`%site` / `%bin` / `%testSuiteName` 占位符；文件不存在则用标准消息，文件存在但为空则不打印（`02.08.04.32.01.05`）。 |
| **hardware response files** | HRE 指定的 HW Response Directory；文件名 `Testsuite;MAPI; call#; site#`。 | 离线调试产物；Store 模式生成，Import 模式使用；可省略 call#/site# 表示全匹配（`02.08.04.32.02.06.03`）。 |
| **optimized testflow（历史产物）** | 由 `dm_optimize` 类操作生成。 | `SmarTest 7.1.0: Removed testflow optimization function`（`02.08.04.32.02.03.04`）；7.10.3 不应把它当默认产物。 |
| **Report / Datalog 条目** | Report Window / event data log。 | `Print` 与 `Print to Datalog` 节点产生；数据落盘与判定属于 [[results]]（`02.08.04.32.01.02.04`）。 |

**建议**：把 testflow 文件与母文件一起纳入版本控制；如果使用母文件，同时提交母文件、全部子文件与 `testerfile` 指向的 setup 文件，否则换机后相对路径引用会断。

## 验证

| 要确认的事 | 文档给的验证方法 | 出处 |
|---|---|---|
| testflow 文件可被解析、参数在范围内 | 加载时 SmarTest 做 range check；非法参数会中止加载并在 `ui_report` 显示错误（见「常见错误」）。文档没有单独的「解析成功」提示；**推断**：能正常加载即未触发该错误。 | `02.08.04.32.03.05` |
| 所有 primary setup 都有效 | Test Suites 页的 **Validate setups** 按钮：无效 setup（未 load 或所选设置不存在）的 equation/set 号标黄并显示 annotation。 | `02.08.04.32.03.01.01` |
| test suite 与当前 testflow 一致 | **Check Inconsistency** / **Check All Inconsistencies**：不一致的 test setup 条目黄色背景、Properties view 灰化；按钮可把 suite 适配到当前 testflow。 | `02.08.04.32.03.01.01`、`02.08.04.32.03.01.02`、`02.08.04.32.03.04` |
| 运行结果符合预期 | Report Window 显示结果；Flow Sequence Editor 中通过的 suite 节点绿色、失败红色、bypass 黄色；Test Suites 页 `Result > Pass/Fail` 变色。 | `02.08.04.32.02.03` |
| 多 site 结果 | Test Suites 页显示所有 site 时，仅当所有 site 通过才绿色；只看 site in focus 时按 focus site 结果变色。 | `02.08.04.32.02.03`、`02.08.04.32.03.01.01` |
| 编辑后结果是否过期 | 执行后再编辑 testflow，所有 suite 边框变成虚线。 | `02.08.04.32.02.03` |
| 每条路径被走了多少次 | 在路径上插 Assign Value 节点自增变量，把 `path_1=@{path_1}, path_2=@{path_2}` 之类表达式写进 bin description；执行后 data log 中有计数。 | `02.08.04.32.02.03.03` |
| 测试时间 | 设 `debug_mode` 为 3 或 4，在 Report Window 看 TESTFLOW INFORMATION 与每条 suite 的 seq setup / test suite exec 行；按文档要求消除 GDF、prober/handler 等干扰。 | `02.08.04.32.02.03.04` |
| 执行流是否符合设计（离线） | 用 HWRE Import 模式预设每个 suite 的 pass/fail，再跑 testflow，观察走哪条分支。 | `02.08.04.32.02.06`、`02.08.04.32.02.06.02` |
| 逐 suite 调试 | Debug view 的 Suspend / Step Over / Resume / Terminate；full testflow 需先 Run and Hold after here。 | `02.08.04.32.02.04.01` |
| 已下载 testflow 的元信息 | `GetTestflowInformation`（须先下载）；`GetLoadedTestflowName`；`GetTestflowRevisionInfo`。 | `02.09.01.11.03.12.03`、`02.09.01.09.12`、`02.09.01.09.17` |
| L3 下载/执行是否成功 | `DownloadTestflowSync` / `ExecuteTestflowSync` 返回 `SUCCESS` 或无错误对象；状态依次为 LOADING → WAITING → TESTING → WAITING。 | `02.09.01.11.03.06.01`、`.02` |

**文档未覆盖**：没有文档化的「testflow 校验命令行」或「testflow lint 命令」；不要自己发明。可用的验证入口就是 GUI 的 Validate setups / Check Inconsistency、加载时的 range check，以及运行结果颜色。

## 常见错误

| 症状 | 原因 / 排查入口 | 出处 |
|---|---|---|
| 加载 testflow 直接中止，`ui_report` 出现 `error: [;] Flag ... must be between ... and ...` 与 `ERROR: cannot parse shm setting from testflow '.../TestFlow'` | 文件里有超出范围的参数；按报错的行号与 `;` 附近定位。 | `02.08.04.32.03.05` |
| 加载时警告 `Testflow flag "<flag_name>" is not defined.` | 用了未定义的 testflow flag；用户 flag 要用 `user` 关键字定义。 | `02.08.04.32.01.02.07.02` |
| 加载时出现 `Warning: Invalid flag statement encountered in testflow file, in the "flags" section:` 后接 `The flag "<bad_flag_name>" is not defined.` 与 `Use the "user" keyword to define a user flag.` | flags 段里的 flag 名非法；同样用 `user` 关键字定义用户 flag。 | `02.08.04.32.01.02.07.02` |
| 勾选 FFV enable / FRG enable / FFC scan info enable / Log first 时底部报错 | 这些是 `ffc_enable` 的子 flag，必须先勾 `FFC enable`；`H/L/I/U (multiple execution)` 需要先勾 `FRG enable`。 | `02.08.04.32.02.01.06` |
| Test Suites 页某些 equation/set 号变黄，Properties view 灰化 | setup 文件未加载或所选设置不存在；点 Validate setups 或 Check Inconsistency 修正。 | `02.08.04.32.03.01.01`、`02.08.04.32.03.04` |
| 加 bin 被拒绝 | 两个 bin 的 SBin 相同且任一非 Notes 属性不同即冲突；不能加冲突 bin。 | `02.08.04.32.02.01.05` |
| 合并 testflow 后 suite 的 primary setting 黄色高亮 | 源 testflow 的 timing/level spec 号在目标 testflow 里不存在；手工改选目标中存在的 spec。 | `02.08.04.32.02.05` |
| 合并时弹 Add New Variables | 源元素用了目标 testflow 没有的变量；选 OK 自动建变量（初值取源值），或 Cancel 放弃复制。 | `02.08.04.32.02.05` |
| CSV 导入失败 | 在 Import 93000 Setup 窗口取消了 Setups 列表的勾选；文档明说不要取消。 | `02.08.04.32.02.01.15` |
| special test suite 抛异常后行为异常 | special test suite 里抛出的异常与 testflow executor 不兼容；不要从 special suite 抛异常。 | `02.08.04.32.01.02.01.02` |
| 带 Group Bypass 的 testflow 在旧版本打不开 / 不兼容 | Group Bypass 是 7.1.3 引入；文档明说带该标志的 testflow 与 7.1.3 之前版本不向后兼容。 | `02.08.04.32.01.02.05` |
| HRE Import 模式提示找不到 hardware response file | 该 suite / API 的响应文件不存在；对话框要求现场指定结果数据并保存为响应文件。 | `02.08.04.32.02.06.02` |
| 单步模式无法从 Testflow (Full) 启动 | 文档明确的限制；先选第一个 suite 执行 `Run and Hold after here`，再继续 Step Over。 | `02.08.04.32.02.04.01` |
| `DownloadTestflowSync` 返回 `FILE_NOT_FOUND` / `ILLEGAL_OPERATION` | testflow 不存在，或 SmarTest 状态不是 WAITING；先确认 testflow 名与当前状态。 | `02.09.01.11.03.06.01` |
| `ExecuteTestflowSync` 返回 `ILLEGAL_OPERATION: No testflow is downloaded.` | 没有先调用 `DownloadTestflowSync()`，或状态不在 WAITING。 | `02.09.01.11.03.06.02` |
| `LoadTestflowSync` 返回 `No device has been installed, please change device` | 没有已设置的 device；该 API 的 Dependency 要求 device 已载入。 | `02.09.01.10.03.02.02.30` |
| Test Suite Control API 与 Testflow UI 同时操作，行为互相影响 | 文档明说两边的创建/删除/改 setup 会互相反映，且不推荐与 UI 交互式同时跑。 | `02.09.01.14` |

**同形陷阱（反例）**：`PACT` 每次执行都会重置**所有** site 的结果，即使只指定一个 site（`02.06.03.02.16`）。不要把它当成只影响目标 site 的普通开关。

## 下一步

**[[run]]**：testflow 组装并调试通过后，下一步是把它作为测试程序的一部分正式运行——生产运行、workorder、Operation Control、abort/reset/pause 状态与批量执行属于 [[run]]。本页的 Run 对话框只覆盖开发/调试期的 Testflow (Full)/(Selection)/(User Defined)；正式运行与执行后的数据判定分别交给 [[run]] 与 [[results]]。
