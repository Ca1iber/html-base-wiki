---
type: stage
title: Results / 数据与判定（Test Result Commands）
tags: [results, error-map, datalog, stdf, edl, test-result, error-map-tool]
related:
  - "[[project]]"
  - "[[pin]]"
  - "[[level]]"
  - "[[timing]]"
  - "[[pattern]]"
  - "[[testmethod]]"
  - "[[testflow]]"
  - "[[run]]"
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.05_Data_Bridge.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.11_Batch_Lot_Control.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.11.03.08_EDL_logging_API.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.11.03.10_Test_result_display_update_API.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.11.03.10.01_UpdateResultDisplay.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.62_ERROR_MAP_TEST.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.62.01_PIN_ERROR_MAP_TEST.htm
  - 02_System_reference/02.10_Data_Logging/02.10.01.02.08_Data_logging_profile_API.htm
  - 02_System_reference/02.10_Data_Logging/02.10_Data_Logging.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11.01_Concepts_of_test_result_processing.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.08.06_Print_Error_Map_Data.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.197_SCAN_TEST_RESULT.htm
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.315_VALC__-__VALid_Cycle_range.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.16.02_How_to_capture_the_test_result_in_real_time.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.08.05_Hidden_Error_Map_Upload.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.189_RESULT_AREA_CONFIG.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.231.29_SMC_PUT_DATALOG.htm
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.207_RRDF_-__Result_Retention_area_DeFinition.htm
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.209_RRUD_-__Result_Retention_area_UnDefine.htm
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.208_RRSC_-__Result_Retention_area_Select_for_Capture.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11.01.03.01_Match_loop_traces_in_the_test_results.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11_Test_Result_Commands.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.109_GET_VALUE_RESULT.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11.01.04_Creating_a_high_resolution_timing_diagram.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11.01.04.01_Dependencies.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.251_TMU_RESULTS.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.255_TRANSACTION_RESULT_PROXY.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.171_PROTOCOL_TEST_RESULT_VECTOR.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.26.04.05_Verifying_results.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11.01.02.01.05_Dealing_with_storage_problems_on_Smart_Scale_systems.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11.02.32_SQIB__SQIB__-__SeQuencer_Interrupt_Behavior.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244.09_TESTSET__.judgeAndLog_FunctionalTest.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244.06_TESTSET__.judgeAndLog_DcResultAccessor.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11.02.08_DCEL__DCEL__-__Digital_Compare_Exception_List.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.08.04_Result_Configuration.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.08.04.01_Result_Mode.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.08.04.03_Advanced.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.08.04.02_Execution_Mode.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11.01.02.01.02.05_Possible_combinations_of_CYRM__CYRP__and_DCRM.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.191_RESULT_CONFIGURATION.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.03_TestsuiteProxy.executeSiteInFocus.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.17_TestsuiteProxy.getTestsuiteFlag.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.02_TestsuiteProxy.executeActiveSites.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.21_TestsuiteProxy.isExecuted.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.23_TestsuiteProxy.isPass.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.33_TestsuiteProxy.setTestsuiteFlag.htm
  - 01_Getting_started/01.07_Testing_a_Basic_Digital_Device/01.07.01.01.01_Device_directory_structure.htm
  - 02_System_reference/02.10_Data_Logging/02.10.01_Event_Data_Logging.htm
  - 02_System_reference/02.10_Data_Logging/02.10.03_SmarTest_Data_Formatter.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.06_Datalog_Control_Tool.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.06.01.01_Setting_the_data_log_general_information_in_the_Datalog_Control_tool.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.06.01.02_Setting_the_data_log_output_information_in_the_Datalog_Control_tool.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.06.01_Logging_test_results_with_Datalog_Control_tool_in_EWC.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.25_Shmoo_Tool.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.01_Principles_of_operation_of_the_Integrated_Result_Tool.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.02_Using_the_Integrated_Result_Tool.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13_Integrated_Result_Tool.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.227_SHMOO_RESULT.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.33_Timing_Diagram_Tool.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.231.27_SMC_PIN_ERROR_MAP.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.02.08_CYCLE_CHUNK.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.190_RESULT_AREA_CONFIG_SET.htm
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.212_RRSU___Result_Retention_area_Select_for_Upload.htm
  - 02_System_reference/02.10_Data_Logging/02.10.03.04.02_Creating_both_detailed_and_summary_output_files.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11.02.24_FFPM___First_Failing_cycle_information_Pin_Mapping.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.231.28_SMC_PIN_ERROR_MAP_ACCESSOR.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.08_Error_Map_Tool.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.08.03.02.03_Error_map_tabs.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.08.02_Using_the_Error_Map_Tool.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.08.01.01_Detailed_error_map.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.23_R_R__Repeatability_and_Reproducibility__view.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.03.05_Retrieving_AC_Test_Results.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.03.07_Logging_Data.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.09.02_DataManager.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.85_GET_EDGE_RESULT.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.88_GET_FUNCTIONAL_RESULT.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.174_PUT_DATALOG.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.274_WAVE_LOG.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11.02.36_VNEC__-__Valid_Number_of_Executed_Cycles.htm
  - 02_System_reference/02.10_Data_Logging/02.10.02.12_Appendix_A__Event_Formatter_Files.htm
  - 02_System_reference/02.10_Data_Logging/02.10.03.06.01_Checking_the_contents_of_an_STDF_file.htm
  - 02_System_reference/02.10_Data_Logging/02.10.01.06_Event_Data_Logging_Format__EDF.htm
  - 02_System_reference/02.10_Data_Logging/02.10.01.06.01_EDF_data_organization.htm
  - 02_System_reference/02.10_Data_Logging/02.10.01.04_Data_Retrieval_Library.htm
  - 02_System_reference/02.10_Data_Logging/02.10.01.04.01_DRL_functions.htm
  - 02_System_reference/02.10_Data_Logging/02.10.01.01_Event_Data_Logging_Concepts.htm
  - 02_System_reference/02.10_Data_Logging/02.10.01.11_Appendix_C__File_Locations.htm
  - 02_System_reference/02.10_Data_Logging/02.10.01.10_Appendix_B__The_DRLDump_Tool.htm
  - 02_System_reference/02.10_Data_Logging/02.10.02_Event_Formatter.htm
  - 02_System_reference/02.15_SmartShell/02.15_SmartShell.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.14.02.02_Retrieving__Judging__and_Logging_Digital_Functional_Test_Result.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.08.01_Error_Map.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11.01.02_Using_the_Error_Maps.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11.01.02.01_Configuring_the_Error_Map_recording.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11.01.02.01.01_Termination_of_the_sequencers.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11.01.02.01.02_Recording_parameters.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11.01.02.01.02.01_Recording_mode_for_detailed_Error_Map.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11.01.02.01.02.02_Recording_position.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11.01.02.01.02.03_Result_granularity.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11.01.02.01.02.04_Resolution_of_the_error_code.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11.01.02.01.02.06_Location_of_the_detailed_Error_Map.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11.01.02.01.03_Interrelations_between_sequencer_termination_and_recording_parameters.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11.01.02.01.04_Configuration_commands.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11.01.02.02_Reporting_the_results.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11.01.02.02.01_Retrieving_edge_information_by_repeating_the_test.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11.01.01_Global_result_queries.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11.01.03_Subsidiary_queries.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11.01.02.01.03.01_Detailed_Error_Map.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11.01.02.01.03.02_Overview_Error_Map.htm
  - 02_System_reference/02.10_Data_Logging/02.10.03.01_Standard_Test_Data_Format__STDF__Overview.htm
  - 02_System_reference/02.10_Data_Logging/02.10.03.02_Starting_and_Stopping_the_Formatter.htm
  - 02_System_reference/02.10_Data_Logging/02.10.03.03_Formatting_V93000_Test_Results_to_STDF.htm
  - 02_System_reference/02.10_Data_Logging/02.10.03.04_STDF_Configuration.htm
  - 02_System_reference/02.10_Data_Logging/02.10.03.04.01_Configuring_the_STDF_file_locations.htm
  - 02_System_reference/02.10_Data_Logging/02.10.01.09.01_Testflow_flags_for_data_logging.htm
  - 02_System_reference/02.10_Data_Logging/02.10.01.09.02_Test_suite_flags_for_data_logging.htm
  - 02_System_reference/02.10_Data_Logging/02.10.01.09_Appendix_A__Data_Logging_Flags.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11.01.02.01.06_Result_commands.htm
  - 02_System_reference/02.10_Data_Logging/02.10.03.06_Appendix_B__The_STDF_Reader.htm
  - 02_System_reference/02.10_Data_Logging/02.10.03.02.05_Data_Formatter_errors_and_warnings.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11.01.02.01.02.07_Compression_factor_for_overview_Error_Map.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.10.01_HVM_API_Introduction.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11.02.34_VALR__-__VALid_Range.htm
  - 02_System_reference/02.10_Data_Logging/02.10.01.02_Data_Logging_Profiles.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11.02.01_CDCP__-__Cycle_Device_Cycle_Parameter.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11.02.02_CHER__-__CHeck_ERrors.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11.02.03_CHFA__-__CHannel_FAil_flag.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11.02.05_CYRM__CYRM__-__CYcle_Resolution_Mode.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11.02.06_CYRP__-__CYcle_Resolution_Parameter.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11.02.07_CYRS__-__CYcle_Resolution_State.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11.02.09_DCGM__DCGM__-__Digital_Compare_Global_Mode.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11.02.10_DCRM__DCRM__-__Digital_Compare_Result_Mode.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11.02.11_DCRP__DCRP__-__Digital_Compare_Result_Positioning.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11.02.12_DCRS__-__Digital_Compare_Result_Size.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11.02.13_DCRT__DCRT__-__Digital_Compare_Result_Target.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11.02.14_EAEX__-__Edge_Action_EXpected_data.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11.02.15_EARD__-__Edge_Action_Result_Data.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11.02.16_EARE__-__Edge_Action_REceived_data.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11.02.17_EDGE__-__EDGE_errors.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11.02.18_EMAP__-__Error_MAP.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11.02.19_ERCC__-__ERror_in_Cycle_range_Count.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11.02.20_ERCT__-__ERror_CounT.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11.02.21_ERCY__-__ERror_CYcle.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11.02.22_ERMP__-__ERror_MaP.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11.02.23_FFCI__-__First_Failed_Cycle_Information.htm
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.123_FLBL__-__Failing_LaBeLs.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11.02.25_FTST__-__Functional_TeST.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11.02.26_GETC__-__GET_Cycles.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11.02.27_GETS__-__GET_Sets.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11.02.28_GETV__-__GET_Vectors.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11.02.29_GETX__-__GET_eXtended_vector_information.htm
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.138_HREX__-__High_Resolution_EXecution.htm
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.139_HRIT__HRIT__-__High_Resolution_Interval_of_Time.htm
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.158_MCNT__-__Match_loop_CouNT.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11.02.30_PASS__-__PASS_or_fail_result.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11.02.31_SQGB__SQGB__-__SeQuencer_GloBal.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11.02.33_VALD__-__VALid_Data.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11.02.35_VCYC__-__Valid_CYCle.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11.02.37_VRCS__-__Valid_ReConStruction.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11.02.38_WFEX__-__WaveForm_EXpected_data.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11.02.39_WFRE__-__WaveForm_REceived_data.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.28_DC_RESULT_ACCESSOR.htm
  - 02_System_reference/02.06_Command_Reference/02.06.11.02.04_CYCI__-__get_CYCle_Information.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.194_RESULT_POINT_LIST.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.12_Offline_Result_Emulation.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.12.01_Pre-silicon_and_emulation_workflow.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.12.04_Configuration_API_for_the_offline_result_emulation.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14_Test_Suite_Control_API.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01_TestsuiteProxy.htm
created: 2026-11-12
updated: 2026-11-12
verified: doc-only
---

# Results / 数据与判定

> 把一次测试执行留下的 pass/fail、Error Map 与捕获数据取出来、存下来、看懂，并决定下一步是回调试还是放行。

## 目的

**文档事实**：`02.06.11` 把本章定位为「result tools 所使用的命令」：

> This chapter explains the commands that are used by the result tools. These commands can be grouped as follows: global result commands, commands for managing the Error Maps, subsidiary commands that do not require a previous test execution.

**文档事实**：结果的底层载体是 Error Map；`02.06.11.01.02` 原文：

> The Error Map is used by SmarTest to record information about failing test cycles. This forms the basis for the analysis of the test results.

同页说明 SmarTest 有两张 Error Map：detailed Error Map 给到 cycle 甚至 edge 级；overview Error Map 把多个 cycle 压成一位结果，用于看整段测试或整个 burst 的失败 pattern。两者默认都在 test processor 内，detailed Error Map 也可以放到外部存储器。`02.06.11.01.02.01` 补了一个关键容量事实：

> The internal detailed Error Map is rather small. It can hold information about 8192 cycles at most.

因此本阶段的第一件事不是「读结果」，而是**决定记录什么、记在哪里、记多细**；读只是第二步。`02.06.11.01.02` 把命令分成两组：一组定义记录什么，一组定义报告什么；报告可以过滤和重新格式化已记录的数据，但不能报告没记录的东西（「everything that is reported must have been recorded」）。

**文档事实**：结果有三个层次，对应三种入口：

- **全局 pass/fail**：`FTST?` 执行功能测试并返回整体结果；`PASS?` 给指定 pin/port 子集的单一结果；`CHER?` 给每个 pin 单独结果（`02.06.11.01.01`）。
- **Error Map 分析**：`VALD?` 查实际记录范围，`ERCC?` / `ERCT?` / `ERCY?` 做错误计数，`EMAP?` / `ERMP?` 取 map 内容，`EARE?` / `EARD?` / `EDGE?` 取 edge 动作和失败 edge，`CYCI?` / `FFCI?` 给逐 cycle 或前 n 个失败 cycle 的信息（`02.06.11.01.02.02`）。
- **Subsidiary queries**：不需要先跑测试，但要求用 `SQSL` 把目标 label 设成 start label、用 `SPRM` 声明 primary timing（`02.06.11.01.03`）。

**文档事实**：GUI 侧有 Error Map Tool（低层错误分析主工具）、Timing Diagram Tool（看实际驱动/接收波形）、Integrated Result Tool（对 EDL/STDF 数据日志做统计和图表）、Datalog Control Tool（控制 testflow 的数据日志输出）、Shmoo Tool / Signal Analyzer 等（`02.08.04.08`、`.33`、`.13`、`.06`、`.25`、`.26`）。

**推断**：本阶段实际上是两个动作的闭环：**先配置记录**（`DCGM` / `DCRP` / `DCRM` / `DCRT` / `CYRM` / `CYRP` / `SQGB`），**再在 [[run]] 之后读取和归档**（`FTST?` 结果、Error Map 查询、数据日志）。记录配置写错，后面的所有查询都只是在读一份错的数据；所以前置条件和常见错误都必须先讲配置。

## 前置条件

- **[[run]] 已执行过至少一次功能测试**。**文档事实**：`FTST?` 才是执行功能测试并产生结果的命令（`02.06.11.02.25`）；`ERMP?` 明写「The query is only available after a functional test has been executed.」（`02.06.11.02.22`）。**推断**：只做完 [[testflow]] 而没有执行，结果查询没有数据可读。
- **sequencer 不在运行**。**文档事实**：`CHER?`、`PASS?`、`ERCT?`、`ERMP?`、`CDCP?`、`EAEX?`、`EARE?`、`GETS?`、`GETV?`、`VCYC?`、`VRCS?`、`WFEX?`、`WFRE?` 等的 `Errors` 段都写明「You send the query while the sequencer is running. There is then no result data available.」；`CHER?` 只写「An error is generated if you send the query while the sequencer is running.」（`02.06.11.02.02`、`.30`、`.20`、`.22` 等）。
- **测试之后没有改过 setup**。**文档事实**：`PASS?`、`ERCT?`、`ERMP?` 的 `Errors` 段写明改 setup 后再查询会没有结果数据，必须重新跑测试（`02.06.11.02.30`、`.20`、`.22`）。**推断**：因此「先看结果再改 setup」是硬顺序，不是习惯问题。
- **记录参数必须在测试之前配置好**。**文档事实**：`02.06.11.01.02.01.04` 明说 `SQGB` 与 `DCGM` / `DCRM` / `DCRP` / `DCRT` 是两套竞争的错误 map 配置方式，`SQGB` 的 error map 部分只为兼容保留，新应用应避免；`DCxx` 命令能启用 Pin Scale / Smart Scale 的特有能力。`DCRT` / `DCRM` / `DCRP` / `DCGM` 的参数都作用在「the last executed test」或「the current configuration」上，说明它们是执行前设定（`02.06.11.02.09`、`.10`、`.11`、`.13`）。
- **记录容量与位置要先算**：detailed Error Map 内部最多 8192 cycles；放外部存储器（`DCRT RAM`）才有更大空间；实际能存多少 cycle 用 `DCRS?` 查（`02.06.11.01.02.01`、`02.06.11.01.02.01.02.06`、`02.06.11.02.12`）。
- **边沿级结果的前提**：要么 `DCRM` 的 result granularity 大于 1 且 sub-cycle 不合并多条 edge，要么用 `DCRM 1,PFC` + `CYRM EDGE` 靠重复执行（shots）取 2 bit edge code；后者要求 `CYRP MULT`（默认），否则测试不能执行（`02.06.11.02.18`、`02.06.11.01.02.02.01`、`02.06.11.02.05`、`.06`）。
- **subsidiary queries 的前提**：目标 label 必须是 `SQSL` 设的 start label，timing 必须是 `SPRM` 声明的 primary timing，否则系统返回空（`02.06.11.01.03`、`02.06.11.02.01`、`02.06.11.02.35`）。
- **`VALR?` 的前提**：DC Scale pin 必须执行过 test point pattern，digital pin 必须执行过 DC pattern（`02.06.11.02.34` 的 `Predependencies`）。
- **GUI 结果工具的前提**：Error Map Tool 的分析对象是**上一次执行**记录的 Error Map，需要在工具里选 cycle block 并 `Result > Execute` 重新聚焦 detailed map（`02.08.04.08.01.01`、`02.08.04.08.02`）；Integrated Result Tool 要先加载 EDL 或 STDF 数据日志，系统数据日志流则自动加载（`02.08.04.13.01`）。
- **Datalog Control 的前提**：SmarTest 已启动、testflow 已加载并可执行；它**只用于 testflow 执行结果**，不要拿它记录 test program 的结果（`02.08.04.06.01` 的 `Before you begin` 与 `About this task`）。
- **数据日志开关**：event data logging 默认关闭；要打开需把 system flag `log_events_enable` 设为 on，并打开 test suite flag `output_on_pass` 或 `output_on_fail`；Datalog Control 里指定输出文件时，若 `log_events_enable` 未开，点 `Start Lot` 会报错要求先打开 flag（`02.07.03.03.07`、`02.08.04.06.01.02`）。
- **STDF 生成的前提**：`global.conf` 中 `formatter.stdf.generateStdf` 默认是 False，不生成 STDF；详细/汇总文件的路径和内容由 `global.conf` 与 `formatter.stdf.main.conf` 决定（`02.10.03.04.01`、`02.10.03.04.02`）。
- **高分辨率时序图的前提**：必须先用 `HRIT` 给出 start/stop cycle、offset、samples，再用 `HREX?` 取数据；pin 必须是 O 或 IO；若测试里有 match loop，不能让 match loop 与被采样的区间共用同一 timing set（`02.06.11.01.04`、`.01.04.01`）。
- **建议**：在 [[run]] 之前就把「这次要回答什么问题」定下来——只要 pass/fail 就用 `PASS?` / `CHER?`；要定位失败 cycle 就配 detailed Error Map；要定位失败 edge 就配 edge granularity 或 `CYRM EDGE`；要归档统计就配 Datalog/STDF。记录参数与问题不匹配时，事后无法补。**这是建议，不是文档要求。**

## 涉及对象

| 对象 | 层级 | 在本阶段做什么 |
|---|---|---|
| `Error Map`（detailed / overview） | concept | 记录失败 cycle 的硬件存储结构；detailed 到 cycle/edge，overview 压缩成一位（`02.06.11.01.02`）。 |
| `FTST?` | L1 | 执行功能测试并返回整体 P/F；是大多数结果查询的数据来源。 |
| `PASS?` / `CHER?` / `CHFA?` | L1 | 全局、逐 pin、match loop 的 pass/fail 查询。 |
| `DCGM` / `DCRP` / `DCRM` / `DCRT` / `DCEL` | L1 | 配置 detailed/overview Error Map 的记录模式、位置、粒度、bit code、存储位置与 pin 例外表。 |
| `CYRM` / `CYRP` / `CYRS?` | L1 | 控制 edge 解析模式、shots 行为，并查询结果状态。 |
| `EMAP?` / `ERMP?` / `ERCC?` / `ERCT?` / `ERCY?` / `EDGE?` | L1 | 读取 Error Map 内容、错误计数、错误 cycle 与失败 edge。 |
| `VALD?` / `VALR?` | L1 | 查实际记录到的 cycle 范围 / test point 测量结果数。 |
| `EARE?` / `EARD?` / `EAEX?` / `WFEX?` / `WFRE?` / `CYCI?` / `FFCI?` / `FFPM?` | L1 | 重建逐 cycle / 逐 edge 的驱动、期望、接收数据与失败信息。 |
| `SQGB` / `SQIB` | L1 | sequencer 终止方式；带宽溢出/超时时的行为。 |
| `CDCP?` / `GETC?` / `GETS?` / `GETV?` / `GETX?` / `VCYC?` / `VNEC?` / `VRCS?` | L1 | Subsidiary queries：把 cycle 映射到 device cycle、vector、set、重建范围。 |
| `HRIT` / `HREX?` | L1（子树外） | 高分辨率时序图的设置与执行。 |
| `RRDF` / `RRSC` / `RRSU` / `RRUD` | L1（子树外） | 结果保留区（result retention area），用于 hidden upload 与跨测试保留结果。 |
| `MCNT?` / `FLBL?` | L1（子树外） | match loop 计数、LMAP 模式下的失败 label。 |
| `Error Map Tool` | gui | 看 Overview / Cycles / Edges / Per Pin 四种视图；配置 Result Mode 并执行测试（`02.08.04.08`）。 |
| `Timing Diagram Tool` | gui | 看实际驱动波形与 DUT 响应，标出与期望不符的点（`02.08.04.33`）。 |
| `Integrated Result Tool` | gui | 对 EDL/STDF 数据日志做汇总、趋势、直方图、shmoo、wafer map 等分析（`02.08.04.13`）。 |
| `Datalog Control Tool` | gui | 选 data logging profile、填 lot 信息、指定 EDL/STDF/text 输出、生成 lot summary（`02.08.04.06`）。 |
| `Event Formatter` | gui | 交互调试用的 report 生成器，从 data log stream 读事件并格式化输出（`02.10.02`）。 |
| `Shmoo Tool` / `Signal Analyzer` | gui | shmoo 图与模拟波形分析；与结果分析相邻（`02.08.04.25`、`.26`）。 |
| `R&R view` | gui | 对数据日志做 Repeatability / Reproducibility 统计（`02.08.04.23`）。 |
| `EDL` / `STDF` / text datalog / lot summary | file | 结果归档格式；EDL 是二进制事件流，STDF 是标准测试数据格式，text 供人读，lot summary 按 lot/wafer 汇总（`02.10.01.06`、`02.10.03`、`02.08.04.06.01.02`）。 |
| `dataformatter.log` | file | Data Formatter 的错误/警告日志（`02.10.03.02.05`）。 |
| `RESULT_CONFIGURATION` | L2 | 用 C++ 配置结果宽度、每 cycle 结果数、edge 映射、存储位置、例外表（`02.07.04.01.191`）。 |
| `ERROR_MAP_TEST` / `PIN_ERROR_MAP_TEST` | L2 | 在测试方法里访问硬件 error counter 和 Error Map（仅 Pin Scale）（`02.07.04.01.62`、`.62.01`）。 |
| `SMC_PIN_ERROR_MAP` / `SMC_PIN_ERROR_MAP_ACCESSOR` | L2 | SmartCalc 下的 Error Map 上传，支持 hidden upload（`02.07.04.01.231.27`、`.28`）。 |
| `RESULT_AREA_CONFIG` / `RESULT_AREA_CONFIG_SET` / `RESULT_AREA_CONFIG_PINS` | L2 | 定义和激活结果区，供 hidden upload 使用（`02.07.04.01.189`、`.190`）。 |
| `GET_FUNCTIONAL_RESULT` / `GET_VALUE_RESULT` / `GET_EDGE_RESULT` | L2 | 取功能测试 P/F、测量值、逐 edge 的 `.fff..` 字符串（`02.07.04.01.88`、`.109`、`.85`）。 |
| `DC_RESULT_ACCESSOR` / `RESULT_POINT` / `RESULT_POINT_LIST` / `RESULT_FAIL_INFO` | L2 | 统一处理 DPS/PMU 等 DC 测量结果与失败点（`02.07.04.01.28`、`.194`）。 |
| `TMU_RESULTS` / `TMU_PINS.upload*Results` | L2 | TMU 测量结果的统计与上传（`02.07.04.01.251`）。 |
| `SCAN_TEST_RESULT` / `SCAN_TEST_PIN_RESULT` | L2 | scan 测试结果容器，经 `judgeAndLog_ScanTest()` 写入 STR（`02.07.04.01.197`）。 |
| `SHMOO_RESULT` | L2 | 定义 shmoo 图上显示的结果（`02.07.04.01.227`）。 |
| `TRANSACTION_RESULT_PROXY` / `PROTOCOL_TEST_RESULT_VECTOR` | L2 | 协议 wrapper 事务的捕获结果访问（`02.07.04.01.255`、`.171`）。 |
| `TESTSET().judgeAndLog_*` | L2 | 判定并记录功能、参数、DPS、PMU、scan、spec search 等结果（`02.07.04.01.244.*`）。 |
| `PUT_DATALOG` / `SMC_PUT_DATALOG` / `WAVE_LOG` / `SCATTER_LOG` | L2 | 把标量、字符串、数组、波形写进 data log stream（`02.07.04.01.174`、`.231.29`、`.274`）。 |
| `ProfileMgr` / `Profile` / `Rule` / `Property` | L2 | 数据日志 profile 的 C++ 模型（`02.10.01.02.08`）。 |
| `TestsuiteProxy` | L3 | 执行 test suite 并取 `isPass()` / `isExecuted()` / flag（`02.09.01.14.02.01`）。 |
| `DataManager`（`dm_emap` / `dm_report` / `dm_profile` / `dm_testtable` / `dm_scan_res` / `dm_shmoo` / `dm_tdiag` / `dm_dataform`） | L3 | 按文件类型 load/save/merge/print/查 up-to-date（`02.09.01.09.02`）。 |
| `DRL`（Data Retrieval Library） | L3 | 直接读 data log stream / 已存日志文件的事件与属性（`02.10.01.04`、`.04.01`）。 |
| `DRLDump` / `STDFreader` | gui / tool | 把 EDL 流或 STDF 文件内容打印出来核对（`02.10.01.10`、`02.10.03.06.01`）。 |
| BLC 的 `IssueEDLEvent` / `MoveEDLStream` / `UpdateResultDisplay` | L3 | 外部程序产生 EDL 事件、移动日志流、刷新结果显示（`02.09.01.11.03.08`、`.03.10`）。 |
| `Offline Result Emulation` | L2 | 在没有器件时用配置的伪结果调试 testflow / test method（`02.07.12`）。 |

### 归属判定

这一节是判断，不是文档事实，供维护者复核。

- **`DCGM` / `DCRP` / `DCRM` / `DCRT` / `DCEL` / `CYRM` / `CYRP` 判给本页，但使用时机在 [[run]] 之前**。它们确实在 `02.06.11.02` 命令子树内，内容也全是「记录什么 / 记在哪里 / 报告什么」。但它们不是测试后的查询，而是**下一次执行的记录配置**。本页保留为 L1 主体，同时在「前置条件」里点明必须先于 [[run]] 设置；不把它们挪进 [[run]]，因为文档把它们编在 Test Result Commands 章，而不是 run 章。
- **`SQGB` 判给 [[run]] 的终止控制 + 本页的 error map 配置，但本页只展开后者**。`02.06.11.02.31` 明说它「serves two purposes simultaneously」；文档同时说 error map 部分只为兼容保留、应改用 `DCGM` / `DCRP`。因此本页把它列全，但在用法上不推荐用它的 error map 半。
- **`SQIB` 判给本页**：它控制的是 detailed Error Map 在外部存储器时记录中止（bandwidth overflow）后的行为，以及 sequencer timeout 的行为（`02.06.11.02.32`）。timeout 那半与 [[run]] 有关，但命令文档在本章，整条列在本页。
- **`PRLT?` 判给本页 / [[run]]**：它返回上一次测试的全局 pass/fail，属于结果读取；它在 `02.06.03.02` pin 子树内，pin 页也把它判给了本阶段。本页不重复它的语法，只作为邻接查询记录。
- **`VALC?` 判给本页**：它是 `VALD?` 的 DC Scale 对应物（`02.06.11.02.33` 明说「For DC Scale pins, use VALC?」），但不在 `02.06.11.02` 子树，列在子树外表。
- **`HRIT` / `HREX?` 判给本页**：`02.06.11.01.04` 专门讲怎么创建高分辨率时序图，并点名这两条命令；它们本身在 `02.06.02.02` 字母序命令章。列在子树外表，不冒充 `02.06.11.02` 的成员。
- **`RRDF` / `RRSC` / `RRSU` / `RRUD` 判给本页 / [[run]]**：它们管理结果保留区（result retention area），供 hidden upload 和跨测试保留 Error Map 结果（`02.06.02.02.207`–`.212`）。这是结果存储侧的能力，但配置发生在执行前；列在子树外表。
- **`MCNT?` / `FLBL?` 判给本页**：`MCNT?` 是 match loop 的匹配 pass 数，`FLBL?` 是 LMAP 模式下的失败 label；两者都被本章正文点到（`02.06.11.01.01`、`02.06.11.01.02.01.02.07`）。列在子树外表。
- **GUI 的 Shmoo Tool / Signal Analyzer / R&R view 判给本页，但不展开**：它们消费结果，不产生 Error Map；本页只列对象和入口，细节留给对象页。
- **`DataManager` 的 `dm_bitmap` / `dm_fam` 不是本阶段的 `dm_emap`**：`dm_bitmap` 是 memory test bitmap，`dm_fam` 是 memory test fail memory（`02.09.01.09.02`）。**同形陷阱**：不要拿 memory test 的结果文件当 Error Map 的保存入口。

### 概念与走查文档覆盖（`02.06.11.01.*`）

这一组是命令参考里的概念章，不是命令本身；逐篇列出，避免只写主路径。

| 分类号 | 文档 | 一句话 |
|---|---|---|
| `02.06.11.01` | Concepts of test result processing | 本章概念索引，链到 global queries、Error Maps、subsidiary queries、高分辨率时序图。 |
| `02.06.11.01.01` | Global result queries | `FTST?` 整体 P/F、`PASS?` pin 子集、`CHER?` 逐 pin；`CHFA?` 用于 match loop 失败，match loop cycle 不进 Error Map；`MCNT?` 给匹配的 loop pass 数。 |
| `02.06.11.01.02` | Using the Error Maps | 两张 map 的分工；detailed 到 cycle/edge，overview 按固定 cycle 数或按 burst 内每个 main pattern 压缩；内部 vs 外部存储；记录组/报告组的分工。 |
| `02.06.11.01.02.01` | Configuring the Error Map recording | 内部 detailed map 最多 8192 cycles；因此要配 sequencer termination 和 recording parameters；overview 按 16 cycles 的倍数压缩，压缩因子可选。 |
| `02.06.11.01.02.01.01` | Termination of the sequencers | `SQGB` 定义终止方式：standard、`STSQ`、`SE`、`EL`、`SEEL`。 |
| `02.06.11.01.02.01.02` | Recording parameters | 六个记录参数；粒度与错误码分辨率有依赖，且随硬件类型不同。 |
| `02.06.11.01.02.01.02.01` | Recording mode for detailed Error Map | acquire failure（只记失败 cycle 及周边）vs cycle oriented（全记）；溢出时前者停止、后者回绕；默认 acquire failure，SmarTest 可自动切换。 |
| `02.06.11.01.02.01.02.02` | Recording position | detailed 可把位置解释为 start/stop/ignore；overview 只能当 stop 或 ignore。 |
| `02.06.11.01.02.01.02.03` | Result granularity | 每 cycle 1–8 个结果；2/4 用 sub-cycle 合 edge；提高粒度会减少可存 cycle 数；edge 级信息也可用额外 shots 取得。 |
| `02.06.11.01.02.01.02.04` | Resolution of the error code | 1 bit 只有 pass/fail、可存两倍结果；2 bit 有三种错误码，便于 dual threshold / window compare。 |
| `02.06.11.01.02.01.02.05` | Possible combinations of CYRM, CYRP, and DCRM | 文档声明这是 `DCRM` / `CYRM` / `CYRP` **全部且仅有的**受支持组合表；按 EDGE / CYCL 两大组列出硬件类型与限制。 |
| `02.06.11.01.02.01.02.06` | Location of the detailed Error Map | `DCRT` 决定 TP 或外部存储器；位置按 port 定，多 port 时以 vector port 为准；外部可用量受其它数据占用影响，用 `DCRS?` 查。 |
| `02.06.11.01.02.01.02.07` | Compression factor for overview Error Map | overview 按 16 cycles 倍数压缩；`DCRM` 设 `BFLM`（仅 Smart Scale）或 `LMAP` 时每个 pattern 一个结果；`LMAP` 插 break vector、`BFLM` 不插；给出配套查询 `VALD?` / `ERMP?` / `GETL?` / `FLBL?`。 |
| `02.06.11.01.02.01.03` | Interrelations between sequencer termination and recording parameters | 两种 Error Map 与 termination mode / recording mode / position 的相互约束索引。 |
| `02.06.11.01.02.01.03.01` | Detailed Error Map | 详细互约束表：standard 下 start/stop/ignore 的行为；EL/SE/SEEL/STSQ/STSV 下若干组合「Not allowed!」，`FTST?` 与 `SQST RUN` 不会执行。 |
| `02.06.11.01.02.01.03.02` | Overview Error Map | overview 的互约束表：standard + stop 需要 detailed 也按 stop 解释；start 组合不被配置命令接受；非标准 termination 下 start/stop 都「Not allowed!」。 |
| `02.06.11.01.02.01.04` | Configuration commands | `SQGB` vs `DCGM`/`DCRM`/`DCRP`/`DCRT` 两套方式；`SQGB` 只应用于终止控制；给出「参数 ↔ 命令」对应表。 |
| `02.06.11.01.02.01.05` | Dealing with storage problems on Smart Scale systems | 外部 Error Map + 同 channel group 全 O/IO + 短 cycle 时可能带宽溢出；缓解手段 `DCEL`、`DCRM` 只记所需 edge；中止后仍完成功能测试，后续行为由 `SQIB` 决定；给出 `DCRT`/`DCEL`/`DCRM` 示例。 |
| `02.06.11.01.02.01.06` | Result commands | 一份完整的「配置 Error Map → `FTST?` → `EMAP?`」示例（本页 L1 示例逐字引用）。 |
| `02.06.11.01.02.02` | Reporting the results | 可报告的对象：记录到的 cycle 区域、错误计数、map 内容；`VALD?` 先查区域，`ERCC?`/`ERCT?`/`ERCY?` 计数，`EMAP?`/`ERMP?` 取内容，`EARE?`/`EARD?`/`EDGE?`/`CYCI?`/`FFCI?` 取更细信息。 |
| `02.06.11.01.02.02.01` | Retrieving edge information by repeating the test | Pin Scale 上 `DCRM 8` 只能拿 1 bit；要 2 bit edge 信息时，结果为 cycle 级且测试失败会触发额外 shots；shots 的四个前提（`CYRM EDGE`、`DCRM 1,PFC`、`CYRP MULT`、查询带 `EDGE`/`CYRM`）；match loop pin 不能用 shots。 |
| `02.06.11.01.03` | Subsidiary queries | 不需要先跑测试，但要求 `SQSL` start label + `SPRM` primary timing；第一组返回 cycle range 的 setup 数据（`CDCP?`/`EAEX?`/`GETV?`/`GETS?`），第二组返回 cycle 信息（`GETC?`/`VCYC?`/`VRCS?`），`GETX?` 兼两组。 |
| `02.06.11.01.03.01` | Match loop traces in the test results | match loop 起止落在 8-cycle block 中间时会改变记录结果；`GETV?`/`VCYC?`/`CYCI?` 会显式或隐式告知；给出 `GETV?` 的 counted match loop 示例。 |
| `02.06.11.01.04` | Creating a high resolution timing diagram | 用 `HRIT` 给 start/stop cycle、offset、samples；用 `HREX?` 执行并取 packed binary；只支持 O/IO pin；测完会删除指定 pin 的 Error Map 内容，GUI 会补跑一次恢复、firmware 路径不会。 |
| `02.06.11.01.04.01` | Dependencies | 若测试有 match loop，match loop 与要高分辨率采样的区域不能共用同一 timing set。 |

## L1 — Firmware / Setup Command

**覆盖范围**：`show.py --list 02.06.11` 返回 66 篇，其中属于 `02.06.11.02` 命令子树的共 40 篇——1 篇索引 + 39 篇命令文档（`.01`–`.39`）。下表按分类号顺序逐条列出，**不代表推荐执行顺序**。每条写命令 + 一句作用 + 出处。

| 分类号 | 命令 | 作用 | 出处 |
|---|---|---|---|
| `02.06.11.02` | List of test result commands | 命令清单索引，本身无语法。 | `02.06.11.02` |
| `02.06.11.02.01` | `CDCP?` | 用 primary wavetable 把物理波形 DC/DC power unit 翻译成 device cycle 名与数据参数；逐 cycle 回答，无法重建的 cycle 可能缺失或报 `UC`。 | `02.06.11.02.01` |
| `02.06.11.02.02` | `CHER?` | 上一次测试在指定 pin 上的 pass/fail，逐 pin 返回；支持 `MUX` 合并 HXA 复用 pin。 | `02.06.11.02.02` |
| `02.06.11.02.03` | `CHFA?` | 返回 counted match loop 最后一个 loop cycle 在指定 pin 上的结果；match loop cycle 不进 Error Map。 | `02.06.11.02.03` |
| `02.06.11.02.04` | `CYCI?` | 逐 cycle 返回上一次执行的完整信息：vector 号、label、type、seq status、comment、waveform 数与二进制数据；`resolution_mode` 可为 `CYCL` 或跟随 `CYRM`。 | `02.06.11.02.04` |
| `02.06.11.02.05` | `CYRM` / `CYRM?` | 设置 cycle resolution mode：`CYCL` 正常、`EDGE` 允许失败后重跑以取 2 bit edge code 并禁止合并 edge 的 `DCRM` 配置（`DCRM 1,PFC` 除外）。 | `02.06.11.02.05` |
| `02.06.11.02.06` | `CYRP` / `CYRP?` | 设置 EDGE 模式的 recovery（`RCRY`/`NRCR`）与 shots（`ONE`/`MULT`）；`ONE` 可阻止多重 shot。 | `02.06.11.02.06` |
| `02.06.11.02.07` | `CYRS?` | 查询指定 pin 的结果状态：`INVL` 无结果、`CYCL` 有 cycle 级结果、`EDGE` 有 edge 级结果；取最低状态。 | `02.06.11.02.07` |
| `02.06.11.02.08` | `DCEL` / `DCEL?` | 维护 pin 级例外表，把指定 pin 的 detailed Error Map 强制放回内部 TP，覆盖 `DCRT` 的 port 级 RAM 设置。 | `02.06.11.02.08` |
| `02.06.11.02.09` | `DCGM` / `DCGM?` | 设 detailed map 记录模式（`ALL`/`FAIL`/`STRD`）和 `DCRP` 位置的解释方式（detailed `STRT`/`HALT`/`NONE`，overview `HALT`/`NONE`）。 | `02.06.11.02.09` |
| `02.06.11.02.10` | `DCRM` / `DCRM?` | 配置 Error Map：`EMAP` 设每 cycle 结果数（1/2/4/6/8）、1/2 bit code、sub-cycle；`OVEM` 设压缩模式（`FCM`/`LMAP`/`BFLM`）与因子。 | `02.06.11.02.10` |
| `02.06.11.02.11` | `DCRP` / `DCRP?` | 设 Error Map 记录位置（start 或 stop），用 `ref_port` 计 cycle；实际解释由 `DCGM` 决定。 | `02.06.11.02.11` |
| `02.06.11.02.12` | `DCRS?` | 按当前粒度、bit 长度与存储位置返回 detailed Error Map 能存多少 cycle。 | `02.06.11.02.12` |
| `02.06.11.02.13` | `DCRT` / `DCRT?` | 设 detailed Error Map 存 TP 还是外部 RAM（RDRAM/vector memory）；按 port 生效；`DCRT?` 回读。 | `02.06.11.02.13` |
| `02.06.11.02.14` | `EAEX?` | 返回指定 cycle range 的 drive 与 expected edge action 数据，用于 cycle reconstruction。 | `02.06.11.02.14` |
| `02.06.11.02.15` | `EARD?` | 返回所有使用 edge 的 drive、expected、received compare 数据；可合并映射到同一 HXA pin 的多颗 Pin Scale pin 结果；用于 Timing Diagram 的 cycle reconstruction。 | `02.06.11.02.15` |
| `02.06.11.02.16` | `EARE?` | 返回 drive/receive edge action 数据与错误信息；不支持 HXA，文档说将由 `EARD?` 取代，新应用用 `EARD?`。 | `02.06.11.02.16` |
| `02.06.11.02.17` | `EDGE?` | 对每个 pin 返回上一次功能测试中失败的 edge 字符串（`F` 失败，`.` 未失败）。 | `02.06.11.02.17` |
| `02.06.11.02.18` | `EMAP?` | 以多种格式返回 detailed Error Map 的二进制内容；支持 `CYCL`/`SCYC`/`EDGE` 分辨率、`PPIN`/`COMB`、packed/byte 对齐；是 `ERMP?` 的更强版本。 | `02.06.11.02.18` |
| `02.06.11.02.19` | `ERCC?` | 返回指定 cycle range 内的错误数；`ERCP` 逐 pin、`ERCG` 全局求和。 | `02.06.11.02.19` |
| `02.06.11.02.20` | `ERCT?` | 返回含错误的 result 数；若 `DCRM` 为 `8,PF`，返回所有记录 cycle 中失败 compare action 的总数；`ERCP`/`ERCG`/`EOLY` 三种 type。 | `02.06.11.02.20` |
| `02.06.11.02.21` | `ERCY?` | 返回错误 cycle 以及 expected / received 数据；`CYC`/`EXP`/`REC`/`ALL` 四种 type。 | `02.06.11.02.21` |
| `02.06.11.02.22` | `ERMP?` | 读取 Error Map 内容：可给整体一位结果、逐 pin 结果、带错误码的 detailed 结果、错误 cycle 地址、edge 级结果；`map_id` 决定格式。 | `02.06.11.02.22` |
| `02.06.11.02.23` | `FFCI?` | 速度优化地返回前 n 个失败 cycle 的信息（按 acquisition start cycle 排序），针对当前 mode context 的全部 O/IO pin 或指定 port。 | `02.06.11.02.23` |
| `02.06.11.02.24` | `FFPM?` | 返回 `FFCI?` 回复中 pin 的排列顺序；按 pogo 号而非 `DFPN` 定义顺序。 | `02.06.11.02.24` |
| `02.06.11.02.25` | `FTST?` | 执行功能测试并返回整体 `P`/`F`；测试必须已由 `SQLB` 定义、`SQSL` 激活。 | `02.06.11.02.25` |
| `02.06.11.02.26` | `GETC?` | 给当前 start label 的逻辑 vector 号，返回 Error Map 内的 cycle 号；文档标注不再维护，推荐 `GETX?`。 | `02.06.11.02.26` |
| `02.06.11.02.27` | `GETS?` | 返回给定 cycle range 使用的 timing set 与 level set；不可重建的 range 返回空。 | `02.06.11.02.27` |
| `02.06.11.02.28` | `GETV?` | 返回生成给定 cycle range 的 sequencer 指令（`GENV`/`RPTV`/`SRCV`/`MACT`/`BRK` 等）与 vector 范围。 | `02.06.11.02.28` |
| `02.06.11.02.29` | `GETX?` | 在 cycle 与 vector 之间双向映射：给 cycle 查 vector/label，或给 label + vector 查首个 cycle。 | `02.06.11.02.29` |
| `02.06.11.02.30` | `PASS?` | 对最后一次测试在指定 pin list 或 port list 上返回单一 P/F；`PASS?PPIN` 逐 pin 返回。 | `02.06.11.02.30` |
| `02.06.11.02.31` | `SQGB` / `SQGB?` | 同时控制 sequencer 终止方式与（兼容用的）Error Map 记录；终止模式含 standard、`ACQF`/`ACFF`、`EL`/`ELPT`、`EMPS`、`SE`、`SEEL`、`STSQ`、`STSV`。 | `02.06.11.02.31` |
| `02.06.11.02.32` | `SQIB` / `SQIB?` | 定义带宽溢出导致记录中止、或 sequencer timeout 时的行为：`ERIM`/`ERRQ`/`FLIM`/`FLRQ`。 | `02.06.11.02.32` |
| `02.06.11.02.33` | `VALD?` | 返回指定 digital pin 在 Error Map 中记录到的首个 cycle（或 label call）与总 cycle 数；`map_id` 区分 `ERRM`/`OVEM`/`LMAP`/`RECD`/`DERR`/`EOLY`。 | `02.06.11.02.33` |
| `02.06.11.02.34` | `VALR?` | 返回指定 pin 记录到的 test point 测量数或 DC pattern 测量数；`map_state` 为 `INVL`/`INCS`/`CONS`。 | `02.06.11.02.34` |
| `02.06.11.02.35` | `VCYC?` | 返回指定 cycle range 的物理波形 DC/DC power unit；先 `SQSL` 设 start label，多 site 时还要 `PQFC`。 | `02.06.11.02.35` |
| `02.06.11.02.36` | `VNEC?` | 返回 COGO 结构 burst 的已执行 cycle 数；只支持单 pin，`value_format` 目前只支持 `ASC`。 | `02.06.11.02.36` |
| `02.06.11.02.37` | `VRCS?` | 返回已重建的 cycle 范围；`STRT`/`STOP` 决定计数方向，`STRD`/`FULL` 决定遇到歧义指令时停止还是按最大 cycle 继续。 | `02.06.11.02.37` |
| `02.06.11.02.38` | `WFEX?` | 返回 drive 与 expected edge action 数据；只对 6-edge setup 有效，仅因兼容保留，新应用用 `EAEX?`。 | `02.06.11.02.38` |
| `02.06.11.02.39` | `WFRE?` | 返回 drive 与 receive edge action 数据及错误信息；只对 6-edge setup 有效，仅因兼容保留，新应用用 `EARE?`。 | `02.06.11.02.39` |

### 最小可用示例

以下示例逐字取自文档的 Example 段。

**完整链路：配置 Error Map → 执行 → 在 edge 级报告**（`02.06.11.01.02.01.06`）：

```
# Put Error Map into cycle oriented mode (for
# quicker response of EMAP?) with start position:
DCGM ALL,STRT,NONE
# Start recording at first cycle:
DCRP EMAP,0,(@)
# Record 1 bit results on edge level:
DCRM EMAP,8,PF,(@)
# Put detailed Error Map into external memory:
DCRT RAM,(@)
# Execute functional test
FTST?
# Report on edge level. All 15000 cycles are returned
# in one reply (ERMP? can only return 2048 cycles):
EMAP? PPIN,0,15000,EDGE,8,PF,ALL,BYTE,,(@)
```

**全局结果查询**（`02.06.11.02.25`、`.30`、`.02`）：

```
FTST?
```
```
FTST P
```
```
PASS? (@)
```
```
PASS P, (@)
```
```
CHER? (@)
```
```
CHER F,(Q0,Q1)
CHER P,(Q2)
CHER F,(Q3)
```

**match loop 失败**（`02.06.11.02.03`）：

```
CHFA? (D1)
```
```
CHFA F, (D1)
```

**Smart Scale 带宽溢出的缓解配置**（`02.06.11.01.02.01.05`）：

```
DCRT RAM,(@)
DCEL DCRT,TP,SET,(P2,P4,P6,P8)
DCRM EMAP,4,PF,"c1:2 c2:4 c3:6 c4:8",(@)
```

文档说明：这样配置后，用 `EMAP?` 的 `EDGE` 分辨率取结果，会按 edge 位置返回；若 4 条 edge 全失败，回复形如 `01010101`。

**edge 模式参数**（`02.06.11.02.05`、`.06`）：

```
CYRM CYCL,,(@)
CYRM CYCL,,(MatchLoopPin)
```
```
CYRP NRCR,ONE
```

**按容量反推可记录范围**（`02.06.11.02.12`）：

```
> DCGM ALL,HALT,NONE
> DCRT TP,(P1)
> DCRM EMAP,8,PF,(P1)
> CYRM CYCL,,(P1)
> DCRS? EMAP,,,(P1)
< DCRS EMAP,8,PF,2048,(P1)
> DCRP 3360,(P1)
> FTST?
> EMAP? PPIN,1312,2048,EDGE,8,PF,ALL,BYTE,(P1)
```

**周期信息查询**（`02.06.11.01.03.01` 的 `GETV?` 示例）：

```
> GETV? 0,200,(CP)
< GETV 0,8,0,13,GENV,,,(CP)
< GETV 8,7,23,8,MTCH,,,(CP)
< GETV 15,2,31,2,GENV,,,(CP)
< GETV 17,7,-1,-1,BRK,,,(CP)
```

### 子树外但本章点名的命令

以下命令不在 `02.06.11.02` 子树，但本章正文、概念页或结果工具文档直接点名；单独列出，不计入 39 条覆盖数。

| 命令 | 作用 | 出处 |
|---|---|---|
| `VALC?` | `VALD?` 的 DC Scale 版本：返回 DC Scale pin 在 Error Map 中记录到的首个 cycle 与总 cycle 数。 | `02.06.02.02.315` |
| `HRIT` / `HRIT?` | 启动/结束高分辨率时序测量并定义 start/stop cycle、offset、samples；必须用 `HRIT END` 正常结束，否则 firmware 可能崩溃。 | `02.06.02.02.139` |
| `HREX?` | 执行高分辨率测量，返回 packed binary 的 L/H/I/U 结果流。 | `02.06.02.02.138` |
| `RRDF` | 定义 result retention area（ID、大小、pin list）。 | `02.06.02.02.207` |
| `RRSC` | 选择后续测试的 capture 结果区；`OFF` 恢复普通采集。 | `02.06.02.02.208` |
| `RRSU` | 选择后续 `ERMP?`/`EMAP?` 的 upload 源结果区；`OFF` 恢复默认。 | `02.06.02.02.212` |
| `RRUD` | 删除所有已定义的结果保留区。 | `02.06.02.02.209` |
| `MCNT?` | 返回 counted match loop（`MACT`）在第几个 pass 匹配；多个 loop 时为累计值。 | `02.06.02.02.158` |
| `FLBL?` | 在 overview Error Map 为 `LMAP` 模式时，返回 burst 内失败 label 的信息；非 `LMAP` 会报错。 | `02.06.02.02.123` |

### L1 内记录的文档差异

1. **`DCRP` 的语法与示例不一致**。`02.06.11.02.11` 的语法是 `DCRP {error_map_pos},{(ref_port)}`，参数表没有 `EMAP` 这一项；但 `02.06.11.01.02.01.06` 的示例写 `DCRP EMAP,0,(@)`，`02.06.11.02.31` 也用 `DCRP EMAP,<error_map_pos>,<ref_port>` 描述 `ACQF` 的等价设置。**两说并列记录，不自行选一个当正确答案**；实机用法需验证。
2. **`CYRS?` 的文档形态不一致**。标题与正文都把它写成 query（`CYRS?`），但语法块同时给出 `CYRS? {(pinlist)}` 和 `CYRS {result_state}, {(pinlist)}`；后者像设置命令。本页按正文「query」使用，语法块中的 `CYRS` 形式原样记录待核。
3. **overview Error Map 的压缩描述口径不同**。`02.06.11.01.02` 说它「combines multiple cycles into one result」；`02.06.11.01.02.01` 说「compresses multiples of 16 cycles」；`02.08.04.08.01` 说「combines every 2000 or more cycles into one result depending on the number of cycles of the test setup」。三者不是同一句话，`DCRM` 的 `FCM` 因子必须能被 16 整除、默认 4096。**记录差异，不合并成一个数字。**

## L2 — Test Method API

**文档事实**：L2 不是「只能读结果」；它可以配置结果记录、访问 Error Map、判定并写数据日志。

### 结果配置与结果区

- **`RESULT_CONFIGURATION`**（`02.07.04.01.191`）：头文件 `/opt/hp93000/soc/prod_com/include/MAPI/ResultConfiguration.h`。构造函数接收 `portName`、`numberOfResultsPerCycle`（`RPC1`/`RPC2`/`RPC4`/`RPC6`/`RPC8`）、`resultWidth`（`_1Bit` / `_2Bit`）、`resultStorageLocation`（`TP` / `RAM`）、`edgeToResultMapping`、`resultGranularity`、`resultStorageLocationExceptionPinList`、`resultStorageIncompleteBehavior`、`multipleExecutions`。**文档事实**：`02.08.04.08.04` 给出 GUI Result Configuration 各字段与这些 member function 的对应表（`setResultWidth()`、`setNumberOfResultsPerCycle()`、`setEdgeToResultMapping()`、`setResultStorageLocation()`、`setResultStorageLocationExceptionPinList()`、`setMultipleExecutions()`、`setResultGranularity()`、`setResultGranularityExceptionPinList()`、`setResultStorageIncompleteBehavior()`）。
- **`RESULT_AREA_CONFIG`**（`02.07.04.01.189`）：头文件 `/opt/hp93000/soc/prod_com/include/MAPI/ResultAreaConfig.h`；构造函数接收 pin/port list，member functions 为 `appendArea()`、`activate()`、`activateWithoutOverwrite()`、`release()`、`removeAllAreas()`。**文档事实**：result area 总数（TMU + digital + DC）不得超过 465；其中 TMU 至少 15、最多 100。
- **`RESULT_AREA_CONFIG_SET` / `RESULT_AREA_CONFIG_PINS`**（`02.07.04.01.190`）：前者持有 digital / DC 结果区的 setup，后者按 pin 设 error map / DC value 结果区大小与 retention 开关（`02.07.04.01.190.01` 起的子页）。**文档事实**：`RESULT_AREA_CONFIG_SET` 明说 result areas 使 hidden upload 可访问这些区域。

### Error Map 访问

- **`ERROR_MAP_TEST`**（`02.07.04.01.62`）：头文件 `MAPI/ErrorMap.h`；构造函数带 `TM::CYCLE_MODE`（`XMODE_CYCLES` 或 `TESTER_CYCLES`）与 `skipErrorMapConfig`；member functions 含 `pin()`、`getErrorCount()`、`getLastCycleExecuted()`、`getNumberOfExecutedTesterCycles()`、`GET_FIRST_FAILING_XMODE_CYCLE()`。
- **`PIN_ERROR_MAP_TEST`**（`02.07.04.01.62.01`）：头文件 `MAPI/PinErrorMap.h`；无 public constructor，从 `ERROR_MAP_TEST` 取得实例。member functions 含 `setStartCycle()`、`setLocation()`、`setRecordingMode()`、`getErrorCount()`、`getFirstFailingCycles()`（有带 `fewerFailsReturnedDueToEmapFull` 的重载）、`getFailingCyclesInRange()`、`getPassFailResultsInRange()`、`getExpectedDataInRange()`、`getExpectedDataForCycles()`、`getLastCycleExecuted()`。**文档事实**：这两个 API 只支持 Pin Scale 测试系统。
- **`SMC_PIN_ERROR_MAP`**（`02.07.04.01.231.27`）：头文件 `MAPI/SMART_CALC2.h`；按 pin + result area 上传 Error Map，支持 SmartCalc 与 hidden upload，兼容 Pin Scale；构造函数 `SMC_PIN_ERROR_MAP(pinName, resultArea)` 或带 `site`。**文档事实**：它要求 X1/X2/X4 的标准 edge-to-result 映射；其它映射要用 `RESULT_CONFIGURATION` 设。
- **`SMC_PIN_ERROR_MAP_ACCESSOR`**（`02.07.04.01.231.28`）：多 pin 的便利包装，构造函数带 `site`、`pinNames`、`resultArea`、`maxFailsPerPin`。
- **`CYCLE_CHUNK`**（`02.07.04.02.08`）：`long long cycle` + `std::vector<char> edges` 的结构，承载 `SMC_PIN_ERROR_MAP.getNextCycleChunk()` 上传的一块结果。

### pass/fail、测量值与 edge 结果

- **`GET_FUNCTIONAL_RESULT()`**（`02.07.04.01.88`）：返回最近一次功能测试（也支持 PPMU/SPMU/DPS）的 P/F；支持无参、按 pin、按 pin + context、按 port + label + `TM::FUNCIONAL_RESULT_TYPE`（取 burst 结果时须 `TM::FTST_BURST`），以及返回 `std::vector<FUNC_TEST_BURST_RESULT>` 的重载。**文档事实（约束）**：`PRLT` 取到的结果会被 `CSAS` / `PSAS` 作废；`GET_FUNCTIONAL_RESULT()` 必须在 `DPS_AUX_PIN_TASK.check...()` 之前调用；改 `SEQUENCER_CONTEXT` 会让结果失效，要用 `Primary.label()` + `FLUSH()` 恢复；API 应放在 `ON_FIRST_INVOCATION` block 外，「Any action which restarts the sequencers will erase the functional results.」
- **`GET_VALUE_RESULT`**（`02.07.04.01.109`）：`ARRAY_D GET_VALUE_RESULT(const STRING& singlePin)`；上传并返回指定 pin 的测量值；头文件 `MAPI/ResultAccessor.h`。
- **`GET_EDGE_RESULT`**（`02.07.04.01.85`）：返回功能测试的逐 edge 字符串（如 `".fff.."`）；头文件 `MAPI/EyeEdgeTbl.h`；返回 query focus 的 site，逐 site 取要在 `FOR_EACH_SITE` block 内。
- **`DC_RESULT_ACCESSOR`**（`02.07.04.01.28`）：头文件 `MAPI/DcResultAccessor.h`；统一处理 DPS/PMU 测量结果，配套 `RESULT_POINT`、`RESULT_POINT_LIST`（`02.07.04.01.194`）、`RESULT_FAIL_INFO`；支持 `uploadResult()` 等。
- **`TMU_RESULTS`**（`02.07.04.01.251`）：TMU 结果的统计访问（period min/max/mean/median/stddev/PP/range、pin 结果、raw data、pin error state 等）；结果由 `TMU_PINS.uploadPeriodResults()` / `uploadRawResults()` / `uploadRawResultsFlat()` 上传（`02.07.04.01` 中同族页）。
- **`SCAN_TEST_RESULT` / `SCAN_TEST_PIN_RESULT`**（`02.07.04.01.197`）：scan 结果容器，经 `TESTSET().judgeAndLog_ScanTest()` 写入 datalog 的 STR 记录；member functions 含 `totalFailures()`、`totalCyclesExecuted()`、`pin()`、`setTestConditionList()`、`setLabelName()`。
- **`SHMOO_RESULT`**（`02.07.04.01.227`）：`ShmooResultAdapter` 的预定义实例，用来定义 shmoo 图显示的结果；member functions 含 `site()`、`pin()`、`testName()`、`index()`、`setResult()`、`coordinate()`、`getSiteList()`、`getPinList()`、`getTestList()`、`getResult()`。
- **`TRANSACTION_RESULT_PROXY` / `PROTOCOL_TEST_RESULT_VECTOR`**（`02.07.04.01.255`、`.171`）：协议 wrapper 事务的捕获结果；单参数可直接转 `INT`/`STRING`，多参数按声明顺序索引或按参数名访问；`PROTOCOL_TEST_RESULT_VECTOR` 提供 `size()`、`operator[]`、`getResultArray()`。

### 判定与日志写入

- **`TESTSET().judgeAndLog_*`** 共 12 个成员：`FunctionalTest`、`ParametricTest`、`Dps`、`DpsVfim`、`PmuIfvm`、`PmuVfim`、`PpmuMeasure`、`PptiaTask`、`ScanTest`、`SpecSearch`、`Spmu`、`DcResultAccessor`（`02.07.04.01.244.06`–`.17`）。以 `judgeAndLog_DcResultAccessor()` 为例，签名 `bool judgeAndLog_DcResultAccessor(const DC_RESULT_ACCESSOR &dc, INT logTestNumber = DEFAULT_LOGTESTNUMBER_VALUE);`，返回 pass/fail，`logTestNumber` 可覆盖实际 test number。**文档事实**：只有前六位数字保证正确写入 STDF。
- **`PUT_DATALOG`**（`02.07.04.01.174`）：头文件 `MAPI/TestControl.h`；重载覆盖字符串、`WAVE_LOG`、`SCATTER_LOG`、`ARRAY_I` / `ARRAY_D` 的 x/y series、`GENERIC_DATA_EVENT`；受 data logging profile 规则控制。
- **`SMC_PUT_DATALOG`**（`02.07.04.01.231.29`）：SmartCalc 背景线程的日志写入，缓冲到 `SMC_SYNCHRONIZE()` 时执行；要求 report formatter 设为 `EventFormatter`，并打开 `log_events_enable` 与 `output_on_pass`/`output_on_fail`。
- **`WAVE_LOG`**（`02.07.04.01.274`）：带标题/单位/comment 的波形数据容器，作为 `PUT_DATALOG` / `PUT_DEBUG` 参数。
- **Data logging profile API**（`02.10.01.02.08`）：`ProfileMgr`（`getInstance()` / `freeInstance()`，创建/激活/加载/保存/删除 profile）、`Profile`、`Rule`、`Property`；规则串示例 `"*leakage*.*.*.datalog_detail=2"`。
- **多 port 功能测试的检索/判定/记录**（`02.07.03.14.02.02`）：`TEST` API 指定 port 可取该 port 的结果；省略 port 则按所有 port 是否全 pass 判定；日志开关同样要求 `log_events_enable` 加 `output_on_pass` / `output_on_fail`，逐 pin 结果要 `per_pin_on_pass` / `per_pin_on_fail`；不判定只取结果用 `GET_FUNCTIONAL_RESULT`。

### 离线结果与文档未覆盖

- **Offline Result Emulation（ORE）**（`02.07.12`）：在没有器件时按器件规格定义伪失败，用于 testflow / test method / DSP routine 的离线验证、调试和回归；需要 S&S_TOOLS_PACKAGE license；配置接口见 `OfflineResultEmulationConfig`（`02.07.12.04`）。**推断**：它产出的是「模拟结果」，不是机台真实结果，不能混进本阶段的真实判定。
- **文档未覆盖**：本次未找到用于配置 **STDF 文件路径/内容** 或 **lot summary** 的 C++ Test Method API。文档把这两件事放在 `global.conf` / `formatter.stdf.main.conf`（`02.10.03.04.01`、`02.10.03.04.02`）和 Datalog Control Tool（`02.08.04.06.01.02`）里。**这是「本次未找到」，不是「文档不提供」。**
- **文档未覆盖**：本次未找到与 L1 `SQIB` 一一对应的 C++ API；`SQIB` 的行为目前只在 firmware 命令层描述（`02.06.11.02.32`）。

## L3 — 外部控制

**L3 入口是横切的，能力面按阶段分族。** 横切入口见 `02.09.01.14`（Test Suite Control API）、`02.09.01.09`（TPI Program Routines，含 `DataManager`）、`02.09.01.10`（HVM API）与 `02.10.01.04`（DRL）。本阶段的专属族是：**Test suite 执行结果族**、**TPI 的结果/报告文件族**、**DRL 数据日志读取族**、**BLC 的 EDL 与结果显示族**、**HVM 的 testflow 执行事件族**。

**文档事实（Test Suite Control API 的边界）**：`02.09.01.14` 原文：

> Test suite control API is used to directly control the test suites outside of the testflow tool. Only UTM-based test suites are supported with these APIs.

并写明：

> They cannot be used in test method programming and also cannot be used in parallel with HVM API and BLC API by the same client process.

### Test Suite Control API：`TestsuiteProxy`

`02.09.01.14.02.01` 的成员中与本阶段相关的是：

- `executeActiveSites()`（`.02.01.02`）— 在所有 active site 上执行该 test suite。
- `executeSiteInFocus()`（`.02.01.03`）— 在 query focus 的 site 上执行。
- `isExecuted(const int site)`（`.02.01.21`）— 该 site 是否执行过；返回 bool。
- `isPass(const int site)`（`.02.01.23`）— 该 site 的执行 pass/fail；文档说明：执行 pass 或 `set_pass` flag 为 on 时返回 true；执行 fail、`set_fail` flag 为 on 或 test suite 未执行时返回 false。
- `getTestsuiteFlag(const TestsuiteFlag name)` / `setTestsuiteFlag(...)`（`.02.01.17` / `.02.01.33`）— 读写 test suite flag；数据日志相关的 `output_on_pass` / `output_on_fail` / `per_pin_on_pass` / `per_pin_on_fail` 属于这组（`02.10.01.09.02`）。

**推断**：`isPass()` 只回答「这个 test suite 在该 site 上过没过」，不提供 Error Map、错误 cycle 或逐 pin 细节；不要把它当成 `EMAP?` 的远程等价物。文档没有声明二者等价。

### TPI：`DataManager` 的结果/报告文件族

`02.09.01.09.02` 的 `Fid` 表中与本阶段直接相关的是：

- `dm_emap` — error map。
- `dm_report` — report。
- `dm_profile` — data logging profile file。
- `dm_testtable` — test table file。
- `dm_scan_res` — scan test results。
- `dm_shmoo` — shmoo。
- `dm_tdiag` — timing diagram。
- `dm_dataform` — data bridge command set。

`Opc` 表提供 `dm_load`（replace current setup by file）、`dm_merge`、`dm_save`（save current setup to file）、`dm_print`、`dm_copy_in`、`dm_delete`、`dm_utd`（return up to date status）。**文档事实**：`Device` 用空字符串表示当前 device；`Flags` 有 `DM_OWRT` / `DM_FORCE` / `DM_SILENT`；`State` 为 1 表示 `dm_utd` 的 up-to-date、0 表示 not up-to-date / 其它操作 ok、< -1 表示 not ok。

**推断**：`dm_emap` 是「Error Map 文件」的加载/保存入口，而 `dm_report` / `dm_scan_res` / `dm_shmoo` / `dm_tdiag` 是结果产物的文件入口；它们不是同一种东西。**同形陷阱**：不要把 `dm_report` 当成 STDF 或 data log 的入口——STDF/EDL 由 Data Formatter / Datalog Control 管，不在这个 `Fid` 列表里。

### DRL：数据日志读取

**文档事实**：`02.10.01.04` 说明 DRL 是访问 data log stream 与已保存日志文件的 API；头文件 `/opt/hp93000/soc/com/include/drl.h`，同目录还有 `dcl.h`、`dcl_drl.h`。它提供读事件记录、抽属性、存到相应数据类型的能力；Event Formatter 就建在 DRL 上。

`02.10.01.04.01` 列出的函数包括：`DRLStart`、`DRLStop`、`DRLSave`、`DRLTruncate`、`DRLFreeEvent`、`DRLKeepEvent`、`DRLEventAvailable`、`DRLGetNextUnmaskedEvent`、`DRLEventGetType`、`DRLEventGetAttribute`、`DRLEventGetFirstAttributeByType`、`DRLEventGetNextAttributeByType`、`DRLEventGetNoOfAttributes`、`DRLGetEventMask`、`DRLSetEventMask`，以及 pin/site 映射类 `DRLNumberOfPins`、`DRLNumberOfSites`、`DRLNumberOfPinGroups`、`DRLPinIndexToName`、`DRLPinIndexToChannel`、`DRLPinIndexToNumber`、`DRLPinGroupIndexToName`、`DRLPinGroupIndexToPins`、`DRLPinGroupNameToIndex`。

**文档事实**：`02.09.01.16.02` 说明「To capture the test result in real-time from the data log stream, you can use the Event Formatter or create your own data retrieval routine.」并列出 DRL 可取的数据类型，包括 test result（pass/fail、per pin pass/fail、per pin result value range、port pass/fail、detailed error map information、error overview、measured range/unit、failing cycle/pin list、IDDQ ganged current）与 shmoo 信息。**推断**：这是 7.10.3 上最接近「外部程序实时拿结果」的文档化路径；它不是 HVM 的功能。

### BLC：EDL 与结果显示

- **`IssueEDLEvent()` / `MoveEDLStream()`**（`02.09.01.11.03.08`）：BLC 的两个 EDL logging API。可产生的 EDL 事件包括 `AppModelLevelStartEventType`、`AppModelLevelEndEventType`、`AppModelLevelLoopEventType`、`AssignmentEventType`、`TestProgramStartEvent`、`TestProgramEndEvent`；`AssignmentEventType` 只能显式发出；事件生成受 `LOG_EVENTS_ENABLE` system flag 控制。
- **`UpdateResultDisplay()`**（`02.09.01.11.03.10.01`）：清空/刷新 test result display；wafer sort 换 wafer 时清 wafer map 并更新 header/sub-header，package test 换 package 时更新 header/sub-header；参数为 `SESSION_ID`、可选 `HEADER`、`SUBHEADER`；成功返回 `SUCCESS`，否则返回带 `ILLEGAL_OPERATION` 等 code 的 error object。

**同形陷阱**：`UpdateResultDisplay()` 只改显示，不改结果数据；不要拿它当「刷新/重算结果」的接口。

### HVM API

**文档事实**：`02.09.01.10.01` 把 HVM API 分为 SmarTest Session Management、Test Execution、Hardware Information、Calibration and Diagnostic 四类。Test Execution API 的职责是「set a device and test program, control the execution of the test program, test flow and BLC, generate the related event and notify the event to SmarTest」。**本次未找到**在 `02.09.01.10.03.02` 的 API 清单里名为 `GetTestResult` / `GetResult` 之类的测试结果读取函数；这些 API 提供的是执行控制与事件通知。**这是「本次未找到」，不是「HVM 不提供任何结果接口」**；若要外部实时取结果，文档指向 DRL（`02.09.01.16.02`）。

### SmartShell

**文档事实**：`02.15` 是全库唯一一篇 SmartShell 总述页；其 `Functional changes` 写明 **`Introduced in SmarTest 8.2.5`**，而本 wiki 面向 SmarTest 7.10.3。**结论**：SmartShell 在本 wiki 的目标版本不存在，不能作为本阶段的 L3 接口。该页正文只有 PDF 外链，没有结果级内容。

### L3 同形陷阱与未覆盖

- **`isPass()` 不是 Error Map 查询**：它给 test suite 级 P/F，不给 cycle/edge 细节（`02.09.01.14.02.01.23`）。
- **`dm_report` 不是 STDF/data log**：它是 report 文件类型；STDF 与 EDL 由 Data Formatter / Datalog Control 产生（`02.09.01.09.02`、`02.10.03`）。
- **`UpdateResultDisplay()` 不是结果上传**：它只更新显示（`02.09.01.11.03.10.01`）。
- **文档未覆盖**：本次未找到通过 L3 直接执行 `EMAP?` / `ERMP?` 等价查询的接口。Test Suite Control API 只有 `isPass()` 级结果；TPI 只有文件级 `dm_emap`；HVM 清单里没有结果读取函数。**这是本次检索的结论，不是全称断言。**

## 产物

**文档事实（先分清「硬件里的结果」与「文件」）**：Error Map 首先是 test processor 或外部 RDRAM 里的硬件数据，不是自动落盘的文件；默认在内部 TP，`DCRT RAM` 才放外部存储器（`02.06.11.01.02`、`02.06.11.02.13`）。要变成可带走的产物，必须通过查询打印、结果区上传或数据日志输出。

### 设备目录与结果相关子目录

**文档事实**：`01.07.01.01.01` 的 device directory 清单里有这些与本阶段相关的子目录：`error_map`、`report`、`scan_res`、`shmoo`、`format`、`profiles`、`testtable`、`timing_dgrm`、`di_report`、`applicat`、`data_set`。**推断**：`error_map` 存 Error Map 相关文件，`report` 存打印/报告，`scan_res` 存 scan 结果，`shmoo` 存 shmoo 数据，`profiles` 存 data logging profile，`testtable` 存 test table/TMLimits；这些目录名与 `DataManager` 的 `Fid` 名称有对应，但文档没有逐条声明一一对应。

### 打印/导出 Error Map

**文档事实**：Error Map Tool 的 `File > Print Error Map Data` 把 Error Map 数据写到文件或直接打印；文件保存在 `/device/report` 目录（`02.08.04.08.06`）。可选范围：All executed ports / Selected port；All recorded failures / Abort after maximum failure count；是否包含 Receive data、Expected data；Print to file 时填文件名，否则打到 console。输出列至少三列，按设置加两列：

```
label1@port1:
Error number | Cycle number| Pinname | Expected data | Received data
1| 70| Sdo1| 1| 0
2| 98| Sdo1| 1| 0
3| 110| Sdo2| 1| 0
4| 111| Sdo2| 0| 1
5| 112| Sdo2| 0| 1
6| 113| Sdo2| 0| 1
7| 117| Sdo3| 1| 0
8| 118| Sdo2| 1| 0
9| 118| Sdo3| 1| 0
```

Expected/Received 列的字符含义：`0` 数据 0、`1` 数据 1、`I` intermediate、`U` unstable（`02.08.04.08.06`）。

### 数据日志文件

**文档事实**：Datalog Control Tool 的 File tab 可以把数据日志输出到 **EDL 文件、STDF 文件、text 文件、custom data log 文件或 data log console**；还可生成 **lot summary** 或 **partial lot summary** 文本文件，per-wafer lot summary 只在 PROBER 测试且勾选 `Per Wafer` 时可指定（`02.08.04.06.01.02`）。

- **EDL**：二进制事件流；每个事件一条 event record，每条 record 由 header（Record Length 四字节、Event Type 两字节）和 body（若干 attribute record）组成；attribute record 也有 Record Length + Attribute Type（`02.10.01.06.01`）。`02.10.01.04` 明说可以把 data log stream 保存成文件后再离线读。
- **STDF**：标准测试数据格式；可生成 detailed 与 summary 两份，summary 文件名在 detailed 名后加 `.summary`（`02.10.03.04.02`）。**文档事实**：`global.conf` 的默认路径是 `$HOME/stdf`（detailed）、`$HOME/stdf/summary`（summary）、`$HOME/stdf/manual`（Testflow Editor 生成）；`formatter.stdf.generateStdf` 默认 False（`02.10.03.04.01`）。**推断**：不打开 `generateStdf` 就没有 STDF 产物，这是默认行为。
- **text data log**：可指定 test name 宽度、是否显示 pin name 列；可同时输出到 console（`02.08.04.06.01.02`）。
- **lot summary**：文本；可按 All Tests / Fail Tests / No Tests 选内容，可按 site 汇总（`02.08.04.06.01.02`）。
- **dataformatter.log**：Data Formatter 的错误/警告日志；位置优先级：`HP83000_ROOT` 已定义 → `/etc/opt/hp93000/soc/`；否则 `HOME` 已定义 → 用户 home；都不定义 → 当前目录；超过 1 MB 时自动裁剪到小于 5 KB（`02.10.03.02.05`）。

### shmoo 与其它

- **shmoo plot**：可保存为 PNG 或 ASCII（`02.08.04.25`）；shmoo 结果来自 `SHMOO_RESULT` / Shmoo Tool，属于结果分析产物。
- **data log stream**：Integrated Result Tool 的系统数据日志流不会自动存盘；文档专门有一节讲怎么保存（`02.08.04.13.02`）。
- **没有默认的「results 文件」**：**推断**：一次普通功能测试结束后，结果留在硬件 Error Map 与内存里的数据日志流中；要形成文件，必须显式打印、上传到结果区、或开启 Datalog/STDF 输出。

## 验证

**文档事实**：结果阶段的验证不是单一命令，而是「先确认记录范围，再确认内容，再确认文件」三层。

### 命令层

- **整体 P/F**：`FTST?` 返回 `FTST P` 或 `FTST F`（`02.06.11.02.25`）；`PASS? (@)` 返回 `PASS P, (@)` / `PASS F, (@)`（`02.06.11.02.30`）；`CHER? (@)` 逐 pin 返回 `CHER P,...` / `CHER F,...`（`02.06.11.02.02`）。
- **match loop**：`CHFA? (D1)` 返回 `CHFA F, (D1)`；match loop 失败不能用 Error Map 查，必须用它（`02.06.11.02.03`）。
- **记录范围**：`VALD? ERRM,(pins)` 返回 `VALD {map_state},{map_id},{start},{number},{(pinlist)}`；`0` 表示请求范围内没有数据（`02.06.11.02.33`）。DC Scale 用 `VALC?`（`02.06.02.02.315`）。
- **结果状态**：`CYRS? (pinlist)` 返回 `INVL`（没有功能测试结果）、`CYCL`（有 cycle 级结果，但不全是 edge 级）、`EDGE`（全部 pin 都有 edge 级结果）（`02.06.11.02.07`）。
- **map 有效性**：`VALR?` 的 `map_state` 为 `INVL`（setup 改过但没跑测试）、`INCS`（Error Map 内容与当前 setup 不一致）、`CONS`（内容与当前 setup 一致）（`02.06.11.02.34`）。
- **容量**：`DCRS? EMAP,,,(P1)` 返回 `DCRS EMAP,8,PF,2048,(P1)` 这类结果；用它可以反推「从感兴趣的 cycle 起还能记多少」（`02.06.11.02.12`）。
- **错误计数**：`ERCC? ERCP,1000,200,(pin1,pin2)` 返回每个 pin 的错误数；`ERCT? ERCP,(Q0)` 返回含错误的 result 数；`ERCY? ALL,0,,2,(pin1,pin2)` 返回前两个错误 cycle 及数据（`02.06.11.02.19`、`.20`、`.21`）。
- **map 内容**：`EMAP?` / `ERMP?` 的回复格式由参数决定；`ERMP? OVEM,0,16,F160,(Q0)` 返回 `ERMP OVEM,0,16,F160,(Q0),#9000000001 0x80` 这类带 `#spec(data)` 的二进制串（`02.06.11.02.22`）。
- **逐 edge 失败**：`EDGE? (pin1,pin2,pin3,pin4)` 返回 `EDGE ...F.... (pin1,pin2)` 这类字符串（`02.06.11.02.17`）。
- **重建范围**：`VRCS?` 的 `reconstr_state` / `start_cycle` / `no_of_cycles` 告诉你哪些 cycle 可重建；`GETS?` / `GETV?` 对不可重建范围返回空（`02.06.11.02.37`、`.27`、`.28`）。
- **subsidiary 的「有没有东西」**：`CDCP?` / `VCYC?` 在没有 `SQSL` start label 或没有 `SPRM` primary sets 时返回空；返回空本身就是验证信号（`02.06.11.02.01`、`.35`）。

### GUI 层

- **Error Map Tool**：`93000 > Results > Error Map` 打开；先选 Acquisition Mode（Force Cycle Oriented / Force Failure Oriented / Follow Current Mode），再在 Result Configuration 选粒度与存储位置，然后 `Result > Execute`；在 Overview tab 看哪些 cycle block 有错，切到 Cycles 或 Edges tab 看细节；如果错误不在 detailed map 范围内，在 Overview 选更后的 block 重复执行（`02.08.04.08.02`）。**文档事实**：错误以红色 cell 显示；Edges tab 只在 result granularity 为 edge 级时可用（`02.08.04.08.03.02.03`）。
- **Timing Diagram Tool**：看实际驱动波形与 DUT 输出，并标出接收数据与 Pattern Tool 中期望数据不一致的点（`02.08.04.33`）。
- **Integrated Result Tool**：加载 EDL 或 STDF 后，Data Log Explorer 列出日志；data navigation view 自动给 test/wafer/device/bin 汇总；Analysis views 给趋势、直方图、shmoo、wafer map 等图（`02.08.04.13.01`、`.02`）。
- **Datalog Control**：`Results` 段写明「The data log files and the lot summary file you specified are generated.」；执行 testflow 后按 File tab 指定的路径检查文件（`02.08.04.06.01`）。
- **R&R view**：可对 `.edl` 或 `.stdf` 数据日志打开，给重复性/再现性统计（`02.08.04.23`）。

### 文件层

- **STDF 内容**：用 `STDFreader stdf_file_name` 读 STDF，打印所有 record 及其字段到 stdout（`02.10.03.06.01`）。
- **EDL/日志流内容**：用 `DRLDump` 读二进制日志流并打印成可读格式；它可以在 SmarTest 不运行时处理已存日志，输出到 stdout，格式比 Event Formatter 简单（`02.10.01.10`）。
- **Data Formatter 错误**：查 `dataformatter.log`；位置规则见上（`02.10.03.02.05`）。
- **建议**：把 `FTST?` / `PASS?` / `CHER?` 的返回串、`VALD?` 的 range、`CYRS?` 的 state 一起记录成一份「本次结果快照」，再与 Error Map Tool / 数据日志对照。**这是建议，不是文档要求**；文档没有提供一键校验整份结果的命令。

## 常见错误

**文档事实**：本阶段没有独立的 `Errors` 章（不像 pin 有 `02.06.03.01.11`）；错误条件分散在各命令的 `Errors` 段、`02.06.11.01.02.01.03.*` 的互约束表、`02.10.03.02.05` 的 Data Formatter 错误，以及 `02.08.04.08.01.01` 的 Error Map Tool `Problems` 段。

### 查询层

| 症状 | 可能原因（文档） | 排查入口 | 出处 |
|---|---|---|---|
| 查询报「no result data available」 | sequencer 正在运行 | 先停 sequencer，再查；`SQST` | `02.06.11.02.02`、`.20`、`.22`、`.30`、`.01`、`.14`、`.16`、`.27`、`.28`、`.35`、`.37` |
| 改了 setup 后查询没有结果 | setup 已变，旧结果失效 | 重新跑测试；不要改完 setup 再查 | `02.06.11.02.30`、`.20`、`.22` |
| `CYRS?` 返回 `INVL` | 还没执行过功能测试 | `FTST?` 或跑 testflow | `02.06.11.02.07` |
| `VALR?` 返回 `INVL` / `INCS` | setup 改过没跑测试 / map 内容与 setup 不一致 | 重新执行测试；用 `VALR?` 确认 `CONS` | `02.06.11.02.34` |
| `VALD?` 选 `LMAP` 但上次测试是 `FCM` | overview map 模式不匹配 | 用 `VALD? OVEM` 或重跑为 `LMAP` | `02.06.11.02.33` |
| `ERMP?` 报 errors-only map 不可用 / 参数越界 / cycle 数为 0 或负 | map 配置或参数不合法 | 检查 `DCRM`/`DCRT`；检查 `start_cycle`、`no_of_cycles` | `02.06.11.02.22` |
| `ERCY?` 报错 | `no_of_cycles` 与 `no_of_errors` 都没给；或无失败数据 | 二选一必填；重跑测试 | `02.06.11.02.21` |
| `GETX?` 报错 | label 不存在 / 未执行 / 逻辑 vector 不存在 / cycle 不存在 | 用 `SQSL` 确认 start label；用 `GETV?` 查实际执行范围 | `02.06.11.02.29` |
| `CDCP?` / `VCYC?` 返回空 | 没有用 `SQSL` 设 start label，或没有 `SPRM` primary sets；或范围内没有 device cycle | 先 `SQSL` + `SPRM`，再查 | `02.06.11.02.01`、`.35`、`02.06.11.01.03` |
| `VNEC?` 报错 | 没有结果数据；或一次查多个 pin | 只查一个 pin；先跑测试 | `02.06.11.02.36` |
| `CDCP?` / `EAEX?` / `EARE?` / `GETS?` / `GETV?` / `VCYC?` / `VRCS?` / `WFEX?` / `WFRE?` 报 invalid cycle range | cycle range 不合法 | 按 0…2^48-1 或 -2^48…-1 的范围检查 | `02.06.11.02.01`、`.14`、`.16`、`.27`、`.28`、`.35`、`.37`、`.38`、`.39` |
| `CYCI?` 报 primary timing setup 变过 | 上次执行后改了 primary timing | 重新执行测试 | `02.06.11.02.04` |
| `CYCI?` 请求超过 256 cycles | 文档规定只报 256 cycles | 分段查询 | `02.06.11.02.04` 的 `Warnings` |

### 记录配置层

| 症状 | 可能原因（文档） | 排查入口 | 出处 |
|---|---|---|---|
| `FTST?` 拒绝执行 | `SQGB` 设了 `EL`/`SE`/`SEEL`/`STSQ`/`STSV`，同时 `DCGM` 的 position 解释是 `STRT`/`HALT`；或 `DCRM`/`CYRM`/`CYRP` 组合不受支持 | 把 `DCGM` 第二/三参数设为 `NONE`；查组合表 | `02.06.11.01.02.01.03.01`、`.03.02`、`02.06.11.01.02.01.02.05`、`02.06.11.02.09` |
| `SQGB` 报 `analyze_delay` 超范围 | 参数越界 | 检查 `SQGB?` 回读 | `02.06.11.02.31` |
| `DCRP` 的位置被忽略并 warning | 当前是非标准 sequencer mode（`EL`/`SE`/`SEEL`/`STSQ`/`STSV`） | 改回 `STRD`；DCRP 定义仍然保存 | `02.06.11.02.11` |
| `DCRP` 的 reference port 不属于 start label | 单 port start label 必须用默认 `@` | 用 `SQSL`/`DCRP?` 核对 | `02.06.11.02.11` |
| 感兴趣区域被覆盖 | cycle oriented 模式下 map 满了会回绕；standard termination + start/ignore 尤其明显 | 用 `DCGM ... HALT` 设 stop；用 `DCRS?` 算容量；把 map 放外部 RAM | `02.06.11.01.02.01.02.01`、`.03.01`、`02.06.11.02.12` |
| acquire failure 模式提前停止记录 | map 满了就停，可能还没到感兴趣区域 | 同上；或改 cycle oriented | `02.06.11.01.02.01.02.01`、`.03.01` |
| Smart Scale 上记录中止（recording abort） | 外部 map + 同 channel group 全 O/IO + 短 cycle，带宽不够 | `DCEL` 把无关 pin 导回内部 map；`DCRM` 只记所需 edge；`SQIB` 选错误行为 | `02.06.11.01.02.01.05`、`02.06.11.02.08`、`.32` |
| 要求 edge 结果但只拿到 1 bit | `DCRM 8` 在 Pin Scale 上只能 1 bit；或 shots 前提不满足 | 用 `DCRM 1,PFC` + `CYRM EDGE` + `CYRP MULT`；或 `DCRM 4` + sub-cycle 只含单 edge | `02.06.11.01.02.02.01`、`02.06.11.02.05`、`.06` |
| match loop pin 拿不到 edge 信息 | shots 会改变 match loop 行为，文档禁止对 match loop pin 用 shots | 用 `CHFA?` / `MCNT?` 查 match loop；`CYRM CYCL` 排除该 pin | `02.06.11.01.02.02.01`、`02.06.11.02.03`、`02.06.02.02.158` |
| `LMAP` 模式测试不能执行 | start pattern 不是 burst；或 port 混了 Smart Scale 与 EXA Scale pin | 改用 burst start label；拆 port | `02.06.11.01.02.01.02.07`、`02.06.11.02.10` |
| `BFLM` 模式某 pattern 失败 | 每个 pattern 必须产生 8 个以上 cycle | 检查 pattern 长度；改用 `LMAP` | `02.06.11.01.02.01.02.07` |
| `FLBL?` 报错 | 上一次测试不是 `LMAP` 模式 | 重跑为 `LMAP`；或不用 `FLBL?` | `02.06.02.02.123` |
| `VALR?` 报错 | DC Scale pin 没有 test point pattern / digital pin 没有 DC pattern | 先执行 test point pattern 或 DC pattern | `02.06.11.02.34` |

### GUI / 文件层

| 症状 | 可能原因（文档） | 排查入口 | 出处 |
|---|---|---|---|
| Error Map Tool 的 Cycles/Edges 里找不到错误 | cycle 数很大导致 overview block size > 2k，且 Acquisition Mode 是 Force Cycle Oriented | 用 extended memory；或把 Acquisition Mode 改为 Force Failure Oriented | `02.08.04.08.01.01` |
| Error Map Tool 的 Edges tab 不可用 | result granularity 不是 edge 级 | 在 Result Configuration 把粒度改为 edge 级 | `02.08.04.08.03.02.03` |
| Result Configuration 的 OK 按钮灰掉 | 选的粒度/bit code 组合在当前硬件上不一致 | 查 `CYRM`/`CYRP`/`DCRM` 组合表；换组合 | `02.08.04.08.04.01` |
| 高分辨率时序测量后 Error Map 内容没了 | `HRIT`/`HREX?` 会删除指定 pin 的 Error Map 内容；firmware 路径不会自动恢复 | 重新执行功能测试；GUI 路径会自动补跑 | `02.06.11.01.04` |
| firmware 在用完 `HRIT` 后异常 | 没有用 `HRIT END` 正常结束 | 补 `HRIT END`；重跑 | `02.06.02.02.139` |
| Datalog Control 记录 test program 结果后数据混乱 | 它只用于 testflow 执行结果 | 用 testflow 执行；不要拿它记 test program | `02.08.04.06.01` |
| 点 `Start Lot` 报错要求先打开 flag | `log_events_enable` 没开 | 开 `log_events_enable`；再开 `output_on_pass`/`output_on_fail` | `02.08.04.06.01.02`、`02.10.01.09.01` |
| 没有 STDF 文件 | `formatter.stdf.generateStdf` 默认 False | 改 `global.conf` / `formatter.stdf.main.conf`；重启 SmarTest | `02.10.03.04.01`、`02.10.03.04.02` |
| STDF 只有半份（缺 summary 或 detailed） | `generateDetailedFile` / `generateSummaryFile` 只开了一个 | 两个都设为 true；`STDF_FILE_SRC`/`STDF_SUMMARY_FILE_SRC` 指向 app model 变量 | `02.10.03.04.02` |
| Data Formatter 出错但报告窗口没有 | 错误写到 `dataformatter.log` | 按 `HP83000_ROOT` / `HOME` 优先级找日志文件 | `02.10.03.02.05` |
| 两份文档说的 `STDFreader` 路径不同 | `02.10.01.11` 写 `/opt/hp93000/soc/formatter/bin/STDFreader`；`02.10.03.06.01` 写 `/opt/hp93000/soc/system/bin` | 两处都试；以实际安装为准 | `02.10.01.11`、`02.10.03.06.01` |
| Integrated Result Tool 里没有历史结果 | 系统数据日志流不会自动存盘 | 用「Saving the system data log stream」；或加载已存 EDL/STDF | `02.08.04.13.02` |
| shmoo 图看不到/不能归档 | 没把 Shmoo Tool 的测试转入 testflow | 先把 shmoo 测试转入 testflow，再执行并保存 PNG/ASCII | `02.08.04.25` |

## 下一步

**文档事实**：results 是九段流程的最后一页，没有「下一个 stage」；文档也没有在 `02.06.11` 里定义一条固定的后续流程。结果的分析工具本身会互相跳转：Integrated Result Tool 可以从 Testflow Tool 右键打开某个 test 的结果，也可以从 FFC Pareto 跳到 Pattern Explorer 看失败 cycle（`02.08.04.13.01`）。

**建议**：按结果性质回流——

- **失败且需要定位**：回 [[run]]，用 Error Map Tool / Timing Diagram Tool 看 cycle/edge；必要时回 [[pattern]] 看 pattern，或回 [[timing]] 检查 timing set。结果页只告诉你「哪里失败」，不替你改 setup。
- **pass/fail 判错或限值不对**：回 [[testmethod]] 检查 `TESTSET().judgeAndLog_*` 的判定与 limits，或回 [[testflow]] 检查 flag（`output_on_pass` / `output_on_fail` / `per_pin_on_*`）与数据日志 profile。
- **结果归档/统计**：留在本页，用 Datalog Control + Integrated Result Tool；STDF 路径与内容按 `global.conf` / `formatter.stdf.main.conf` 配。
- **下一步的硬前提**：在 [[run]] 之后、动任何 setup 之前先把结果取出来；文档明确改 setup 会让结果查询没有数据（`02.06.11.02.30`、`.20`、`.22`）。
