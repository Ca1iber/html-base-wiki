---
type: stage
title: Timing / Wavetable 时序配置（Timing Setup）
tags: [timing, wavetable, equation, fixed-timing, edge, period, device-cycle, multiport, specset]
related:
  - "[[project]]"
  - "[[pin]]"
  - "[[level]]"
  - "[[pattern]]"
  - "[[testmethod]]"
  - "[[testflow]]"
  - "[[run]]"
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.06_Timing_Setup_Commands.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.01_Concepts_of_timing_setup.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.02_List_of_timing_setup_commands.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.01_Waveform_Shapes_and_Edge_Delays.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.02_Data_organization_of_equation_based_timing.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.02.01_Timing_equation_set_reference.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.03_Defining_waveform_shapes.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.03.01_Defining_waveform_shapes_for_Pin_Scale_standard_pins.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.03.01.01_Specifying_the_actions.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.03.01.01.01_Drive_actions.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.03.01.01.02_Receive_actions.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.03.01.01.02.01_Restrictions_for_selective_digital_capture.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.03.01.02_Selecting_and_ordering_edges.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.03.01.02.01_Restrictions_for_drive_edges.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.03.01.02.02_Restrictions_for_receive_edges.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.03.01.03_Combining_selective_digital_capture_with_a_functional_test.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.03.02_Defining_waveform_shapes_for_Smart_Scale_pins.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.03.02.01_Defining_waveforms_for_a_protocol_engine_test.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.03.02.01.01_Special_requirements_for_freezing_the_tracker.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.03.02.02_Defining_the_wavetable_for_a_PRBS_test.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.03.02.03_Defining_the_wavetable_for_a_pattern_based_SmartLoop_test.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.03.03_Defining_the_break_waveform.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.03.04_Handling_waveform_definitions_at_the_firmware_level.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.03.05_Representing_a_pattern_in_device_orientation.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.03.05.01_Syntax_of_the_STATEMAP_section.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.04_Setting_delays_and_periods.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.04.01_Specifying_the_period.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.04.01.01_Defining_the_global_period.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.04.01.01.01_Restrictions_for_multiport_setups.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.04.01.02_Determining_the_period_resolution.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.04.01.02.01_Automatic_calculation_of_period_resolution_for_single-port_setups.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.04.01.02.02_Specifying_the_Period_Resolution.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.04.01.02.03_Period_resolution__clock_resolution__and_master_clock_period.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.04.01.02.04_Period_resolution_for_a_multi-port_setup__Smart_Scale.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.04.02_Setting_the_edge_delays.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.04.02.01_Defining_the_edge_delays_for_Pin_Scale_standard_pins.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.04.02.02_Defining_the_edge_delays_for_Pin_Scale_3600_fast_pins.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.04.02.03_Defining_edge_delays_for_Smart_Scale_pins.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.04.02.03.01_Defining_edge_delays_and_period_length_for_a_protocol_engine_test.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.04.02.03.02_Defining_edge_delays_for_a_PRBS_test.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.04.02.03.03_Defining_edge_delays_for_a_pattern_based_SmartLoop_test.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.05_Defining_the_timing_specification.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.05.01_Consistency_checks_for_edge_delays.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.05.02_Changing_the_runtime_values_of_base_variables.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.05.03_Multiport_timing_specifications.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.05.03.01_Global_and_local_scope_of_base_variables.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.06_Dealing_with_rounding_problems_in_multiport_setups.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.06.01_Avoiding_rounding_problems_with_the_fract___function.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.06.01.01_Syntax_of_fract.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.06.01.02_Usage_of_the_fract___function.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.06.02_Avoiding_rounding_problems_with_different_clock_groups.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.07_Fixed_timing.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.07.01_Data_organization_of_fixed_timing.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.07.02_Defining_waveform_shapes.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.07.03_Defining_the_period.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.01.07.04_Defining_the_Edge_Delays.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.01_APRM_-__Activate_PRiMary_sets.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.02_BWDF__BWDF__-__Break_Waveform_DeFinition.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.03_BWDS__BWDS__-__Break_Waveform_Definition_String.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.04_CDCP__-__Cycle_Device_Cycle_Parameter.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.05_CLKR__CLKR__-__CLocK_Resolution.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.06_DCDT__DCDT__-__Device_Cycle_DefaulT.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.07_DCUD_-__Device_Cycle_UnDefine.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.08_DFCR__DFCR__-__DeFine_Clock_Routing.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.09_DPRT__DPRT__-__Default_PRimary_Timing_sets.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.10_DSCP__DSCP__-__Define_System_Control_Parameter.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.11_EDDC__-__EDge_in_Device_Cycle.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.12_EDSP__EDSP__-__EDge_SPecification.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.13_EQFS_-__EQuation_FileS_command_transfer.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.14_EQSP__EQSP__-__EQuation_SPecification_transfer.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.15_ETDS__ETDS__-__Edge_Timing_Definition_String.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.16_ETIM__ETIM__-__Edge_TIMing.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.17_EUDS__-__Edge_Usage_Definition_String.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.18_EVCK__-__EVent_ClocK.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.19_FTCG__FTCG__-__Functional_Test_ConfiGure.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.20_PCLK__PCLK__-__Pin_CLocK.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.21_PDIV__-__Period_DIVider.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.22_RCLK__-__Reference_CLocK_source.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.23_RSET_-__ReSET.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.24_SCLK__-__System_CLocK_query.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.25_SDSC__-__Set_number_DeSCriptions.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.26_SPCP__-__SPeCification_Port_list.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.27_SPEC__-__SPECification.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.28_SPRM__SPRM__-__Set_PRiMary_sets.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.29_SPST__-__SPecset_STatus.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.30_STRS__-__Spec_TRansition_Search.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.31_SVLR__SVLR__-__Spec_VaLues_at_Runtime.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.32_TSUS__TSUS__-__Timing_Sets_USed.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.33_TSUX__TSUX__-__Timing_Sets_Used_eXtended.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.34_UPTD__UPTD__-__UP_To_Date.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.35_VCLK__-__Verify_CLocK.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.36_VDCG__-__Verify_Device_Cycle_for_Group.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.37_VTIM__-__Verify_TIMing.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.38_VWFG__-__Verify_WaveForms_in_Groups.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.39_VWFS__-__Verify_WaveForm_Sets.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.40_WAVE__WAVE__-__WAVEform.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.41_WFDF__WFDF__-__WaveForm_DeFinition.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.42_WFDS__WFDS__-__WaveForm_Definition_String.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.43_WFUD_-__WaveForm_UnDefine.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.44_WRST_-__Waveform_ReSeT.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.45_WSDM__WSDM__-__Waveform_Set_Display_Mode.htm
  - 02_System_reference/02.06_Command_Reference/02.06.06.02.46_WSUS__WSUS__-__Waveform_Sets_USed.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34_Timing_Setup_Tool.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.01_Description_of_the_Timing_System.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.03_Waveform_and_timing_sets.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.03.01_Relationship_between_waveform_sets_and_timing_sets.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.03.02_Implications_when_running_tests.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.04_Equation_based_timing_setup.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.04.01_Single-port_timing_setup.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.04.02_Multiport_timing_setup.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.04.02.01_Verifying_a_multiport_timing_setup.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.04.03.05.01_CHECK_Statement_Options.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.04.03.06_Error_Reporting.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.04.04_Example_of_the_equation_based_timing_setup_file.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.04.05_Timing_setup_master_file.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.04.05.01_Master_file_format_for_timing_setup.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.05_Mode_context_in_timing_setup.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.06_Using_the_Timing_Setup_Tool.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.06.01_Setting_up_the_wavetables.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.06.02_Defining_the_equation_sets.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.06.03_Defining_the_spec_sets.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.06.05_Setting_the_period.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.06.05.01_Minimum_period___maximum_frequency_of_the_sequencer.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.06.06.01_Watching_System_Resources.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.06.06.06_Downloading_Your_Timing_Setup_into_the_Firmware.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.06.12_Performing_Timing_Checks.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.06.12.02_Checking_for_Timing_Limitations_at_Device_Cycle_Boundaries.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.07_The_Timing_Setup_Window.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.34.07.01_The_Global_Information_Area.htm
  - 01_Getting_started/01.07_Testing_a_Basic_Digital_Device/01.07.01.01.01_Device_directory_structure.htm
  - 01_Getting_started/01.07_Testing_a_Basic_Digital_Device/01.07.01.04.01_Equation_based_timing_setup.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.01.01.03_Task_3__Setups_for_Digital_Channels.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.01.01.04_Task_4__Setting_up_a_Test.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.249_TIMING_SPEC.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.167_PRIMARY_STATUS_-__Primary.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.232_SPECIFICATION.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.37_DIGITAL_WAVEFORM.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.37.16_DIGITAL_WAVEFORM.getTimingResolution.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.248_TIMING_OFFSET_SEARCH_TASK.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.03.02.01_Changing_spec_value_in_primary_timing_spec_set.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.11.01.05.02_Timing_equation_file.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14_Test_Suite_Control_API.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.18_TestsuiteProxy.getTimingEquation.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.19_TestsuiteProxy.getTimingSet.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.20_TestsuiteProxy.getTimingSpec.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.22_TestsuiteProxy.isMultiportTiming.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.26_TestsuiteProxy.setEquationBasedTiming.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.27_TestsuiteProxy.setMultiportTiming.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.09.02_DataManager.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.10.01_HVM_API_Introduction.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.10.03.02.02.20_DownloadTestprogram.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.10.03.02.02.12_ChangeDevice.htm
  - 02_System_reference/02.15_SmartShell/02.15_SmartShell.htm
  - 02_System_reference/02.06_Command_Reference/02.06.13.02.04_TSHA__-__Timing_Setup_Has_Arming.htm
  - 02_System_reference/02.06_Command_Reference/02.06.09.02_List_of_AC_test_function_commands.htm
  - 02_System_reference/02.06_Command_Reference/02.06.09.02.17_TOCF__TOCF__-__Timing_Level_Offset_search_ConFiguration.htm
created: 2026-11-12
updated: 2026-11-12
verified: doc-only
---

# Timing / Wavetable 时序配置

> 把 waveform shape、边沿位置和周期组装成 timing specification，让 pattern 里引用的 device cycle 真正能在 DUT 上按时序执行。

## 目的

**文档事实**：`02.06.06` 开篇定义本阶段的范围：

> The timing setup for a device defines the waveforms that can be sent to the pins of the DUT during a test, and the possible period lengths, that is, the possible lengths of the tester cycle, which is the time span used for executing one waveform.

同一篇把 timing 拆成两个互相独立的维度：**波形形状**（actions 的有序序列）与**边沿位置**（edge delay）。`02.06.06.01.01` 进一步说明：drive 与 receive 各有 8 个 edge（d1–d8 / r1–r8），shape 存在 wavetable，edge delay 与 period 存在 timing set；同一个 shape 可以在不同 timing set 里换边沿位置，从而在一次测试里切换时序。

**文档事实**：SmarTest 的标准 timing 是 equation based。`02.06.06` 原文：

> In equation based timing, waveform shapes are defined in a wavetable, and edge positions are defined in an equation set. Wavetable and equation set are brought together in a timing specification. In a multi-port setup, this must be done separately for every involved port.

同一篇给出另一种形态 fixed timing：每个 setup element 由一条 firmware 命令定义，period 与 edge delay 必须是常量。

**文档事实**：`01.07.01.04.01` 把 equation based timing setup 的任务固定为三步——Generate a Wavetable、Generate a Timing Equation Set、Generate a Timing Specification, linking the wavetables and timing equations。`02.08.04.34.04` 重复同一三步，并说明其元素是 Expressions / equation variables / spec variables，语法与 level equation 相同。

**文档事实**：`02.08.01.01.03` 把本阶段放在 digital channel setup 的中间：先用 Level setup tool 配电平，再用 Timing Setup Tool 定义 digital waveform shapes，最后用 Pattern Tools 配 vectors。`02.08.01.01.04` 说 test 阶段才在 testsuite 里指定 primary sets 与 vector label。

**推断**：本阶段真正产出的是四类可被下游引用的身份——wavetable 名、equation set 号 + specset 号（合起来 `specset_id = 100 * equation_set_no + specset_no`）、timing set 号、multiport specification 名——再加上它们落到硬件上的周期与边沿值。缺任何一类，pattern 里的 device cycle 名或 testflow 里的 primary timing set 就会指向不存在或未定义的数据。

## 前置条件

- **[[pin]] 已完成，且 mode context 一致**。`02.08.04.34.05` 写明：每个 test 关联一个 mode context，每条 `CONF` 只作用于一个 context；equation set 与 wavetable 各自带 mode context；**primary timing setup 的 equation set 与 base wavetable 必须是同一个 mode context**：

  > Note The specification of a primary timing setup must include a pointer to a timing equation set and to a base wavetable of the same mode context. You cannot define a specification pointing to a wavetable and an equation set of different mode contexts.

  同一篇说未显式指定时用 `DEFAULT`，它覆盖所有 mode 为 `std` 的 pin；FAST pin 必须用用户自定义 context 来定义 timing。**文档事实**：`MODECONTEXT` 行必须紧跟在 `EQNSET` 行之后（`02.08.04.34.05`）；`02.06.06.01.02.01` 把 `MODECONTEXT` 列为 equation set 的可选首项。
- **device 目录与 `timing/` 子目录已存在**：`01.07.01.01.01` 的目录清单里有 `timing`；`02.06.06.01.05` 明说 timing specification 文件位于 `<device_folder>/timing`，文件名可自取（例：`timingSpec1`）。
- **资源上限已定**：`02.06.06.02.10` 说 `DSCP` 定义各类参数集的最大实例数并预留 Sequencer Memory，且**每次调用都会清空 Sequencer Memory**，所以必须重新 load device setup；它的参数可由 device 根目录的 `.technology` 指定。具体的 timing 相关上限见 `02.06.06.02.46`（waveform set 默认 16、最大 16）、`02.06.06.02.32`（所有 waveform set 的 timing set 总数最大 512、默认 256，单个 waveform set 最多 256）、`02.06.06.02.10`（device cycle 默认 256、最大 16384）。
- **fixed timing 的先后顺序**：`02.06.06.02.40` 的 `Prerequisites` 要求 logical waveform 必须先由 `WFDS` 或 `WFDF` 定义；`02.06.06.02.41` 的 `Postrequisites` 要求 `WFDF` 之后必须用 `WAVE` 定义 physical waveform，**即使 logical waveform 不含任何 data parameter 也必须做**。这是 D1 型顺序前置。
- **waveform set / timing set 号必须在当前上限内**：`WFDF`/`WFDS`/`WAVE` 的 `Errors` 都以 `wvf_set` 超过 `WSUS` 上限为报错条件；`ETDS`/`PCLK` 以超过 `TSUS` 上限为报错条件。
- **equation based 需要完整的 specset 指针**：`02.06.06.01.02` 说 spec set 只存在于 specification 内；`02.06.06.02.28` 说 `SPRM` 要用 `specset_id`（`100 * equation_set_no + specset_no`）标识 timing，且 specset_id 必须引用一个已定义的 wavetable。
- **sequencer 状态**：**本次未找到**任何 timing setup 命令要求 sequencer 必须 OFF 的原文（例如 `DFPN` 就有这条要求，而 timing 命令没有）。`02.06.06.02.15` 的 `Postdependencies` 与 `02.06.06.02.31` 均写明改动在**下一次 functional test 开始时**才生效。**推断**：因此可以在测试间隙修改；**建议**：仍在 sequencer 停止时改 timing，并在改完后重新做下载与校验，避免与正在跑的应用模型争用同一份 setup。
- **建议**：先确定三张清单——(1) 每个 pin/port 要用的 waveform shapes；(2) 需要几个 timing set、各自 period 与 edge delay；(3) spec 变量及其 min/max——再动手写 wavetable/equation set。文档没有给这三个清单的模板。

## 涉及对象

下表是本阶段的主对象与层级；46 条 L1 命令的完整覆盖见 L1 表。

| 对象 | 层级 | 在本阶段做什么 |
|---|---|---|
| `Timing Setup Tool` | gui | 本阶段主工具：建立/编辑 wavetable、equation set、spec set，显示 device cycle 与波形，做 timing 检查（`02.08.04.34`）。 |
| `Timing Setup window` | gui | 显示与编辑周期、边沿延迟、device cycle 的主窗口，分 Global Information / Timing Entry / Device Cycle Edit 三个区（`02.08.04.34.07`）。 |
| `Wavetable Editor` | gui | ASCII 编辑器，生成并下载 wavetable；默认显示上次打开的文件，与当前 Timing Setup 无关（`02.08.04.34.06.01`）。 |
| `Spec Tool` | gui | 定义 spec set 的变量值、min/max、单位并下载（`02.08.04.34.06.03`）。 |
| `timing setup file` | file | `<device_dir>/timing` 下的 timing 文件，含 firmware 命令与 `EQSP` 数据块（`02.06.06.01.05`、`02.08.04.34.04.04`）。 |
| `timing setup master file` | file | 把 wavetable、equation set、multiport spec、common block 拆成子文件再组装（`02.08.04.34.04.05`、`.04.05.01`）。 |
| `wavetable` | concept | 按 pin/pin list 定义 shape 与 device cycle，不含 edge delay（`02.06.06.01.02`、`02.06.06.01.03`）。 |
| `equation set` | concept | `EQNSET` + `SPECS` + `EQUATIONS` + timing set；最多 256 个，变量总数最多 4096（`02.06.06.01.02.01`）。 |
| `timing set` | concept | 一个 period 加一组 edge delay；从 1 编号，属于唯一一个 waveform set（`02.06.06.01.07.01`、`02.08.04.34.03.01`）。 |
| `spec set` / `specset_id` | concept | 给 equation set 的 base variable 赋值，并带 min/max；`specset_id = 100 * equation_set_no + specset_no`（`02.06.06.01.02`）。 |
| `timing specification` | concept | 把 equation set、wavetable、spec set 组合成完整 timing；单端口用整数对标识，多端口用名字（`02.06.06.01.05`、`02.06.06.01.05.03`）。 |
| `multiport timing specification` | concept | 按 port sequence 为每个 port 指定 equation set/wavetable/spec 值，并带 `SYNC`（`PHASE` / `SEQUENCE` / `CLOCK`）（`02.06.06.01.05.03`）。 |
| `device cycle` | concept | 一个或多个 waveform 的序列，pattern 通过 device cycle 名引用波形（`02.08.04.34.01.03`、`02.06.06.01.03.04`）。 |
| `break waveform` | concept | sequencer 进入 BREAK 时输出的波形，只允许 drive actions（`02.06.06.01.03.03`）。 |
| `STATEMAP` | concept | wavetable 内描述 tester waveform 到 DUT waveform（x-mode）映射的段（`02.06.06.01.03.05.01`）。 |
| protocol timing segment | file | `USE_PROTOCOL` 引用的协议 timing 段，保存为 protocol 目录下的 `.prot_tim` XML（`02.07.11.01.05.02`）。 |
| 波形定义命令族 | L1 | `WFDS` / `WFDF` / `WAVE` / `BWDF` / `BWDS` / `WFUD` / `WRST`。 |
| 周期与边沿命令族 | L1 | `PCLK` / `ETDS` / `ETIM` / `CLKR`。 |
| 集合数量与传输命令族 | L1 | `WSUS` / `TSUS` / `DSCP` / `EQFS` / `EQSP`。 |
| 校验与回读命令族 | L1 | `VTIM?` / `VWFG?` / `VDCG?` / `VWFS?` / `VCLK?` / `CLKR?` / `SPST?` / `EUDS?` / `EVCK?` / `SCLK?` / `RCLK?` / `PDIV?` / `SPEC?` / `SDSC?` / `SPCP?` / `UPTD?`。 |
| 运行时与 primary set 命令族 | L1 | `SVLR` / `STRS?` / `SPRM` / `APRM` / `FTCG`。 |
| `TIMING_SPEC` | L2 | 访问已有 timing equation + spec set 数据容器，读/改 spec 值（`02.07.04.01.249`）。 |
| `PRIMARY_STATUS` | L2 | 切换 primary timing spec/set，取 `TIMING_SPEC` 对象（`02.07.04.01.167`）。 |
| `SPECIFICATION` | L2 | multiport timing 的 specification 容器（`02.07.04.01.232`）。 |
| `DIGITAL_WAVEFORM` / `TIMING_OFFSET_SEARCH_TASK` | L2 | 与本阶段相邻的测量 API：前者取 timing resolution，后者做 timing offset search；不用于定义 setup（`02.07.04.01.37`、`02.07.04.01.248`）。 |
| `dm_timing` | L3 | TPI `DataManager` 的 timing setup 文件类型，可按文件 load/merge/save/delete（`02.09.01.09.02`）。 |
| `TestsuiteProxy` timing 族 | L3 | 读/设 test suite 的 timing equation/spec/set 与 multiport timing（`02.09.01.14.02.01.18`–`.27`）。 |
| HVM API | L3 | 外部下载 test program / 切 device，间接带上 timing setup；**本次未找到** timing 专用 HVM 命令（`02.09.01.10.01`、`02.09.01.10.03.02.02.20`）。 |
| SmartShell | L3（7.10.3 不存在） | `02.15` 的 `Functional changes` 写明 `Introduced in SmarTest 8.2.5`；本 wiki 面向 7.10.3，不能当可用接口。 |

### 概念文档覆盖（`02.06.06.01.*`，53 篇）

这些是命令参考里的概念/操作模式章，不是命令。逐篇列出，避免只写主路径。

| 分类号 | 文档 | 一句话 |
|---|---|---|
| `02.06.06.01` | Concepts of timing setup | 概念章索引，链到 shape/edge、equation based 数据组织、delay/period、timing specification、rounding、fixed timing。 |
| `02.06.06.01.01` | Waveform Shapes and Edge Delays | drive 与 receive 各 8 个 edge；shape（动作序列）与 edge delay 分开定义；wavetable 存 shape、timing set 存 edge delay 与 period。 |
| `02.06.06.01.02` | Data organization of equation based timing | equation based 由 equation set、wavetable、timing specification（含 spec set）三类数据组成；`specset_id = 100 * eqnset + specset`。 |
| `02.06.06.01.02.01` | Timing equation set reference | `EQNSET` 头、`MODECONTEXT`、`DEFINES`、`SPECS`、`EQUATIONS`、`period_res`、`clocksrc`、`TIMINGSET` 的完整文法；最多 256 个 equation set、4096 个变量。 |
| `02.06.06.01.03` | Defining waveform shapes | shape 是 action 的有序序列；两种格式（带 edge 的 edge-action pair / 不带 edge 由系统分配）；differential pin 的 `@diff`；shape 在 vector 里只存索引。 |
| `02.06.06.01.03.01` | Defining waveform shapes for Pin Scale standard pins | 标准 pin 用 edge-action pair 序列定义 shape；可给 shape 起名字（历史上叫 device cycle）。 |
| `02.06.06.01.03.01.01` | Specifying the actions | drive action 与 receive action 两类；drive action 同时含“驱动值”和“tri-state”两个独立动作。 |
| `02.06.06.01.03.01.01.01` | Drive actions | 三字符动作编码（F + 驱动值 + tri-state），列出 `F00`/`F10`/`FN0`/`FNZ` 等缩写。 |
| `02.06.06.01.03.01.01.02` | Receive actions | 1–2 字符动作编码（E/W + 比较值）；`ARM` 只在 Smart Scale 上启动 TMU；列出 `E0→L` 等缩写。 |
| `02.06.06.01.03.01.01.02.01` | Restrictions for selective digital capture | `C`/`D` 触发/抑制 selective digital capture 的使用要求。 |
| `02.06.06.01.03.01.02` | Selecting and ordering edges | 边沿编号：Pin Scale 用 `dn`/`rn`，Smart Scale 用 `fn`/`sn`；edge delay 定义在 pin 级而不是单个 waveform。 |
| `02.06.06.01.03.01.02.01` | Restrictions for drive edges | 同一 waveform 里两个同类 drive edge 的 delay 必须递增；CHECK 可开关；Smart Scale 无此限制；Pin Scale 上违反会在迁移到 Smart Scale 时得到不同波形。 |
| `02.06.06.01.03.01.02.02` | Restrictions for receive edges | 无 window compare 时顺序任意；有 window compare 时 receive edge 必须按时间与编号递增。 |
| `02.06.06.01.03.01.03` | Combining selective digital capture with a functional test | 正常 digital capture 与 `L`/`H` 比较的关系，以及和 selective digital capture（`C`/`D`）合用的行为。 |
| `02.06.06.01.03.02` | Defining waveform shapes for Smart Scale pins | drive 与 tri-state 分成 `f`/`s` 两组边沿；modified standard 与 native 两种格式；`di` 可混用于内部转换，但同一 `PINS` 块不能混写。 |
| `02.06.06.01.03.02.01` | Defining waveforms for a protocol engine test | protocol engine 波形必须用 native Pin Scale 9G 格式，并满足该节列出的附加条件。 |
| `02.06.06.01.03.02.01.01` | Special requirements for freezing the tracker | 冻结 tracker 需要同时满足的条件。 |
| `02.06.06.01.03.02.02` | Defining the wavetable for a PRBS test | PRBS wavetable 由 SmarTest 从 primary PRBS set 自动生成，用户只需告诉系统两件事。 |
| `02.06.06.01.03.02.03` | Defining the wavetable for a pattern-based SmartLoop test | pattern-based SmartLoop wavetable 由 SmarTest 自动生成。 |
| `02.06.06.01.03.03` | Defining the break waveform | 每个 I / I/O pin 可有 break waveform，由 `brk` 引入，不得含 receive action；未定义时用空定义（什么都不做）。 |
| `02.06.06.01.03.04` | Handling waveform definitions at the firmware level | firmware 仍把 shape 视为 logical/physical/device cycle 三元组；运行期改 shape 必须先 `WFDS ... ALLOW_EQ` 再 `WAVE ... ALLOW_EQ`。 |
| `02.06.06.01.03.05` | Representing a pattern in device orientation | x-mode / fractional x-mode 与 device oriented view；STATEMAP 段与 firmware 的 `VCAT` 命令定义 DUT view。 |
| `02.06.06.01.03.05.01` | Syntax of the STATEMAP section | STATEMAP 表的列：索引、state character、x-mode、selector。 |
| `02.06.06.01.04` | Setting delays and periods | shape 定完后要定 period 与 edge delay，单位 ns；测试中用 `CTIM` 切 timing set。 |
| `02.06.06.01.04.01` | Specifying the period | 可给所有 pin 一个 global period，也可给单 pin 覆盖；multiport 不允许 pin specific period；结果工具不支持 pin specific period。 |
| `02.06.06.01.04.01.01` | Defining the global period | equation based 的 period 写在 `TIMINGSET` 下 `period=`；`PCLK` 只能改运行值，不改 timing set 里的值。 |
| `02.06.06.01.04.01.01.01` | Restrictions for multiport setups | multiport 各 port 的 period 定义基本互相独立。 |
| `02.06.06.01.04.01.02` | Determining the period resolution | 同一单端口 timing spec / waveform set 下所有 pin、所有 timing set 的 period 必须是 period resolution 的整数倍。 |
| `02.06.06.01.04.01.02.01` | Automatic calculation of period resolution for single-port setups | 未指定时由 timing set 1 的 global period 动态算出；给出 PS1600（2.5–10 ns）与 PS5000（1.0 ns–100 µs）范围及自动修正示例。 |
| `02.06.06.01.04.01.02.02` | Specifying the Period Resolution | 用 `period_res` 指定；指定后改 TS1 周期不再重算；`CLKR` 只改运行值。 |
| `02.06.06.01.04.01.02.03` | Period resolution, clock resolution, and master clock period | SmarTest 7.10 master clock 固定 8/3 ns（375 MHz）；clock resolution 由 master clock 与 period resolution 推出；PS1600 要求 1.76–3.52 ns。 |
| `02.06.06.01.04.01.02.04` | Period resolution for a multi-port setup (Smart Scale) | 每个 Smart Scale 通道有自己的 PLL，可各自有 clock resolution / period resolution。 |
| `02.06.06.01.04.02` | Setting the edge delays | edge delay 按 pin 定义，同一 pin 在同一 edge 上的位置在所有 waveform 中相同。 |
| `02.06.06.01.04.02.01` | Defining the edge delays for Pin Scale standard pins | 标准 pin 的 edge delay 一般格式与写法。 |
| `02.06.06.01.04.02.02` | Defining the edge delays for Pin Scale 3600 fast pins | 含 fast pin edge delay 的 equation set 必须关联 mode context；fast pin 的 `period_div` / DELTA 语义。 |
| `02.06.06.01.04.02.03` | Defining edge delays for Smart Scale pins | `f`/`s` edge 可分别给 delay；`di` 表示两者同值；`period_div` 可等距布边沿；`ETDS` 只改运行值。 |
| `02.06.06.01.04.02.03.01` | Defining edge delays and period length for a protocol engine test | `TTMODE` 标记 protocol engine test pin，并定义其 x-mode；protocol engine test 的 period 有额外限制。 |
| `02.06.06.01.04.02.03.02` | Defining edge delays for a PRBS test | PRBS 的 edge 在一个 tester cycle 内等距；可定义起始偏移。 |
| `02.06.06.01.04.02.03.03` | Defining edge delays for a pattern-based SmartLoop test | pattern-based SmartLoop 的 edge 等距；可定义起始偏移。 |
| `02.06.06.01.05` | Defining the timing specification | wavetable + equation set + spec set + CHECK 选项合成 timing specification；文件在 `<device_folder>/timing`；`SVLR` 读写变量。 |
| `02.06.06.01.05.01` | Consistency checks for edge delays | `CHECK` 控制 edge distance（1/2/10 period，drive/receive 分开）与 edge order 检查。 |
| `02.06.06.01.05.02` | Changing the runtime values of base variables | 改 base variable 的运行值会重算整个 timing equation system，不改 setup 值。 |
| `02.06.06.01.05.03` | Multiport timing specifications | 多端口 spec 用名字标识；为每个 port 给 equation set/wavetable/spec 值，并可设 `SYNC` 的 `PHASE` / `SEQUENCE` / `CLOCK`；**若 multiport spec 未覆盖全部已配置 pin，系统可能崩溃**。 |
| `02.06.06.01.05.03.01` | Global and local scope of base variables | 同一 spec 变量可在多个 port 同名；可用 `@port` 限定；`fract()` 要求相关 port 的该变量为 global。 |
| `02.06.06.01.06` | Dealing with rounding problems in multiport setups | 除法产生的 period 小数会导致 SCLK 周期过大或比例失真；两种规避方式。 |
| `02.06.06.01.06.01` | Avoiding rounding problems with the fract() function | 用 `fract()` 定义 period 以保留比例，Pin Scale 与 Smart Scale 均适用。 |
| `02.06.06.01.06.01.01` | Syntax of fract() | `period = fract(<numerator>,<denominator>,<global_var>)`；分子/分母必须是整数（小数被忽略）；只能用于 timing set 的 period 语句。 |
| `02.06.06.01.06.01.02` | Usage of the fract() function | 并非每个 `fract()` 实例都按比例求值；部分实例会被平凡化。 |
| `02.06.06.01.06.02` | Avoiding rounding problems with different clock groups | 把纯 Smart Scale port 分到不同 clock group；clock group 只能在特定 setup 中使用。 |
| `02.06.06.01.07` | Fixed timing | fixed timing 每个元素由一条 firmware 命令定义，period 与 edge delay 必须是常量，数据组织与 equation based 不同。 |
| `02.06.06.01.07.01` | Data organization of fixed timing | 数据组织为 waveform set → 一套 shape（logical/physical/device cycle）+ 一个或多个 timing set；用 `WFDS`/`WAVE`/`ETDS`/`PCLK` 定义。 |
| `02.06.06.01.07.02` | Defining waveform shapes | fixed timing 只有 logical + physical 成对的格式；给出完整命令示例；索引必须用十进制（wavetable 内是十六进制）。 |
| `02.06.06.01.07.03` | Defining the period | 用 `PCLK` 定义；`@` 表示 global period（默认 port 的全部 pin），写具体 pin 则定义 pin specific period。 |
| `02.06.06.01.07.04` | Defining the Edge Delays | 用 `ETDS` 给指定 waveform set / timing set / pin 定义 edge delay。 |

### GUI / 工具章覆盖（`02.08.04.34`）

**文档事实**：本章共 228 篇，其中 `02.08.04.34.02.*` 是与 `02.06.06`（102 篇）**一一对应的整章镜像**（连 46 条命令也重投一遍）。非镜像篇目按路径计为 126 篇；其中 2 组是同题重复投放（`PIN_ALIAS_SET` 与 `Checking for the Combinations used in the Selected Test`），已在表中并列标出。下表按小节逐篇列出；镜像部分不重复计入，命令行见 L1 表。

#### 描述 timing 系统（`02.08.04.34.01.*`）

| 分类号 | 文档 | 一句话 |
|---|---|---|
| `02.08.04.34` | Timing Setup Tool | 本章入口：timing 系统描述、waveform/timing set、equation based setup、mode context、使用工具、Timing Setup window。 |
| `02.08.04.34.01` | Description of the Timing System | 硬件框图与三级关系：device cycle 由 waveform 组成，waveform 由 edge 上的 action 组成，edge 有相对 cycle 起点的 delay。 |
| `02.08.04.34.01.01` | Timing edges | 每通道 16 个 edge generator：8 个 drive、8 个 receive；列出可用资源。 |
| `02.08.04.34.01.01.01` | Drive Edges and Actions | 每个 drive edge 要同时定义 data action 与 tri-state action。 |
| `02.08.04.34.01.01.02` | Receive Edges and Actions | receive edge 可关联的 action 图示。 |
| `02.08.04.34.01.01.03` | Edge Ranges | edge delay 相对 test system cycle 起点编程，给出范围。 |
| `02.08.04.34.01.01.04` | Edge order | 必须遵守的 edge 顺序规则。 |
| `02.08.04.34.01.02` | Waveforms | action 是“把驱动置 0/1”之类的事件，waveform 由 edge action 构成。 |
| `02.08.04.34.01.02.01` | The Physical Waveform Table | 每通道的 physical waveform table 存硬件实际执行的波形。 |
| `02.08.04.34.01.02.02` | The Break Waveform | BREAK 状态输出的 break waveform；总是存在。 |
| `02.08.04.34.01.02.03` | Relationship to Vector Setup | Vector Setup 中 device cycle 的第一个 waveform 叫 Initial Vector。 |
| `02.08.04.34.01.03` | Device Cycles | 用 datasheet 的时序图解释 device cycle 的构成。 |

#### Waveform 与 timing set（`02.08.04.34.03.*`）

| 分类号 | 文档 | 一句话 |
|---|---|---|
| `02.08.04.34.03` | Waveform and timing sets | waveform set 存 system clock period、默认 device cycle、每 pin 的 device cycle 表、physical waveform 表、若干 timing set；timing set 存 period 与 edge delay。 |
| `02.08.04.34.03.01` | Relationship between waveform sets and timing sets | 上电 1 个 waveform set + 1 个 timing set；一次测试只用 1 个 waveform set + 1 个 timing set；timing set 属于唯一 waveform set；每 set 最多 256 个 timing set；primary waveform set ≠ base waveform set。 |
| `02.08.04.34.03.02` | Implications when running tests | 测试中可用 `CTIM` 切 timing set 改边沿；切 waveform set 要重新编程 VCO、只能在测试之间；TS1 精度最高，其他 timing set 的 period 取 master clock 的最近倍数，偏差可到 ±6 ns。 |

#### Equation based timing setup（`02.08.04.34.04.*`）

| 分类号 | 文档 | 一句话 |
|---|---|---|
| `02.08.04.34.04` | Equation based timing setup | 三步：wavetable → equation set → timing specification；元素是 expression、equation variable、spec variable。 |
| `02.08.04.34.04.01` | Single-port timing setup | 单端口 setup 由整数对（equation set 号、spec 计数）标识；同一 equation set 换 spec 值或换 wavetable 都要新建 specification。 |
| `02.08.04.34.04.02` | Multiport timing setup | 多端口 = 每个 port 一份单端口型 specification 之和；equation set 与 wavetable 语法不变；spec 用名字标识；port 顺序影响自动 period resolution。 |
| `02.08.04.34.04.02.01` | Verifying a multiport timing setup | 在 Timing Setup Tool 中用 `Select > Select Specification`、`Select > Port`、`Tset#` 验证各 port；pin 不在任何 port 的 primary multiport spec 里会在 report window 警告，可能需要 reset system。 |
| `02.08.04.34.04.03` | Structure of an equation based timing setup | equation based 的三类数据集合：equation set、wavetable、spec set。 |
| `02.08.04.34.04.03.01` | Data organization of equation based timing | 与 `02.06.06.01.02` 同题同文（重复投放）。 |
| `02.08.04.34.04.03.01.01` | Multiport timing specifications | 与 `02.06.06.01.05.03` 同题同文（重复投放）。 |
| `02.08.04.34.04.03.02` | Common Syntax Used In Timing Wavetables | wavetable 语法总览。 |
| `02.08.04.34.04.03.02.01` | Differential pins - @diff | timing 文件支持 `@diff` pin 语法。 |
| `02.08.04.34.04.03.02.02` | Edge action | edge action 由 `WFDF` 定义，最终编程进硬件。 |
| `02.08.04.34.04.03.02.03` | Physical drive edge action | 允许的 physical drive action 枚举：`N`、`F0N`、`FN0`、`FNZ`、`F00`、`F0Z`、`F10`、`F1Z`、`.`、`!Z`、`Z`、`0`、`1`。 |
| `02.08.04.34.04.03.02.04` | Physical expected edge action | 允许的 expected action 枚举（E/W 系列及缩写）。 |
| `02.08.04.34.04.03.03` | Timing Wavetables - Reference | 定义应用于指定 pin 的 waveform，而不在此定义 edge delay。 |
| `02.08.04.34.04.03.03.01` | Wavetable header | `WAVETBL <name>` 头。 |
| `02.08.04.34.04.03.03.02` | Pin alias set (PIN_ALIAS_SET) | 可选：可在 equation set/wavetable 指定默认 pin alias set。 |
| `02.08.04.34.04.03.03.03` | Wavetable body | wavetable 正文（`PINS` 块与波形行）。 |
| `02.08.04.34.04.03.03.04` | Default device cycle | `default_device_cycle` 语法。 |
| `02.08.04.34.04.03.03.05` | Multiport wavetable setup | multiport 的 wavetable 语法与单端口相同，按 port 使用。 |
| `02.08.04.34.04.03.03.06` | Display mode (display_mode) | `display_mode` 语法。 |
| `02.08.04.34.04.03.03.07` | wavetable | 一个 wavetable 把一个或多个 `PINS` 块应用到 pin list。 |
| `02.08.04.34.04.03.03.08` | Pure waveforms (pure_waveforms) | pure waveform 可为 physical waveform 或 break waveform。 |
| `02.08.04.34.04.03.03.09` | Physical edge action setups | 定义 physical edge action 时必须一次给 6 个（每 edge 一个）。 |
| `02.08.04.34.04.03.03.10` | Physical drive edge action setups | 定义 physical drive edge action 时同样必须给 6 个。 |
| `02.08.04.34.04.03.03.11` | Edge action setups | 定义 edge action 时必须一次给 6 个。 |
| `02.08.04.34.04.03.03.12` | Break waveform | wavetable 中的 break waveform 只允许 drive action。 |
| `02.08.04.34.04.03.03.13` | Device cycle | wavetable 中的 device cycle 定义。 |
| `02.08.04.34.04.03.04` | Timing Equations - Reference | 定义若干 timing equation set；每 set 含 specs、equations、period resolution、timing sets。 |
| `02.08.04.34.04.03.04.01` | Timing equation set header (EQNSET) | `EQNSET` 头与编号/描述。 |
| `02.08.04.34.04.03.04.02` | Pin alias set (PIN_ALIAS_SET) | 与 `34.04.03.03.02` 同题同文（重复投放）。 |
| `02.08.04.34.04.03.04.03` | Equation set body | body 的 4 个 section：specs、equations、period resolution、timing sets。 |
| `02.08.04.34.04.03.04.04` | Multiport equation setup | multiport 中 equation set 关联 ports；一个 equation set 可覆盖多个 port。 |
| `02.08.04.34.04.03.04.05` | specs | equation set 引用的 spec 必须在此列出。 |
| `02.08.04.34.04.03.04.06` | Timing specification header (SPECS) | spec set 的 `SPECS` 头。 |
| `02.08.04.34.04.03.04.07` | Timing spec set | timing set 内一个或多个 spec 的定义语法。 |
| `02.08.04.34.04.03.04.08` | equations | derived spec（equation variable）定义区。 |
| `02.08.04.34.04.03.04.09` | Timing equation header (EQUATIONS) | `EQUATIONS` 头。 |
| `02.08.04.34.04.03.04.10` | Derived specs | equation set 含 0 个或多个 equation。 |
| `02.08.04.34.04.03.04.11` | Period resolution (period_res) | 默认从 TS1 period 自动求；也可用 `period_res` 显式指定。 |
| `02.08.04.34.04.03.04.11.01` | Clock Source and Period Resolution | clock source（internal/external）与 period resolution 的指定。 |
| `02.08.04.34.04.03.04.12` | Period divisor (period_div) | `period_div` 可取 -1（标准 pin）、2/3/4/6/8（fast pin 等）。 |
| `02.08.04.34.04.03.04.13` | Timing sets (TIMINGSET) | `TIMINGSET` 头与编号/描述。 |
| `02.08.04.34.04.03.04.14` | Pin timing resource | `pin_timing_resources` 的 `e1`–`e6` 形式。 |
| `02.08.04.34.04.03.04.15` | Dealing with rounding problems in multiport setups | 与 `02.06.06.01.06` 同题同文（重复投放）。 |
| `02.08.04.34.04.03.04.15.01` | Usage of the fract() function | 与 `02.06.06.01.06.01.02` 同题同文（重复投放）。 |
| `02.08.04.34.04.03.05` | Timing Specifications - Reference | 定义 timing spec，并给每个变量赋 setup/max/min。 |
| `02.08.04.34.04.03.05.01` | CHECK Statement Options | `CHECK all`/`CHECK NONE` 与单项检查关键字；驱动/三态按不同类型处理。 |
| `02.08.04.34.04.03.05.02` | SPECSET | `SPECSET` 头与内容。 |
| `02.08.04.34.04.03.05.03` | spec | 每个 spec 的 setup/initial、minimum、maximum 值行语法。 |
| `02.08.04.34.04.03.06` | Error Reporting | 错误通常到 report window；`CKST?`、`EQFS` 可导向文件；列出 timing 资源 `period_res`、`period`、`d1-d8`、`r1-r8`；含 spec 的方程会按 setup/min/max 组合求值并逐项报错。 |
| `02.08.04.34.04.03.07` | Glossary of terms - timing setup | timing setup 术语表。 |
| `02.08.04.34.04.04` | Example of the equation based timing setup file | 完整 timing 文件示例，文件头 `hp93000,timing,0.1`，含 `EQSP` 数据块、wavetable、equation set、spec set。 |
| `02.08.04.34.04.04.01` | Timing Wavetables - Example | wavetable 示例（`WAVETBL gross_func_wtb` 等）。 |
| `02.08.04.34.04.04.02` | Timing Equations - Example | equation set 示例（`EQNSET 1 "gross_func_eqn"` 等）。 |
| `02.08.04.34.04.04.03` | Timing Specifications - Example | `CHECK`/`SPECSET` 示例。 |
| `02.08.04.34.04.05` | Timing setup master file | timing setup 可单文件，也可把 wavetable/equation set/multiport spec 拆文件再用 master file 连接。 |
| `02.08.04.34.04.05.01` | Master file format for timing setup | master 文件格式：`hp93000,timing_master_file,0.1`、`testerfile:`、`WAVETABLE`/`EQNSET`/`MULTIPORT_SPEC`/`DEFINES` 条目、`PIN_ALIAS_SET`、自动文件名规则。 |
| `02.08.04.34.04.05.02` | Editing the level and timing subfiles | equation based level/timing setup 以字符串参数形式存放在 setup 文件中，可编辑子文件。 |

#### Mode context（`02.08.04.34.05`）

| 分类号 | 文档 | 一句话 |
|---|---|---|
| `02.08.04.34.05` | Mode context in timing setup | equation set 与 wavetable 各带 mode context，两者必须相同；spec 不能跨 context 组合；`MODECONTEXT` 写在 `EQNSET`/`DEFINES` 之后。 |

#### 使用 Timing Setup Tool（`02.08.04.34.06.*`）

| 分类号 | 文档 | 一句话 |
|---|---|---|
| `02.08.04.34.06` | Using the Timing Setup Tool | 用 chip 时序关系示例串起 wavetable、equation set、spec set 与窗口编辑。 |
| `02.08.04.34.06.01` | Setting up the wavetables | 步骤：Select > edit wavetables → Generate → 选 waveform set 与 pin → create → Shell > Download；wavetable 文件是临时的，必须另存或保存 Timing Setup。 |
| `02.08.04.34.06.02` | Defining the equation sets | 步骤：Edit Equations → Generate → 可选自定义 period resolution → `EQNSET` → `SPECS` → `TIMINGSET` → 每 pin 的 edge → Shell > Download；下载时检查语法并报错到 report window。 |
| `02.08.04.34.06.03` | Defining the spec sets | 用 Spec Tool：Create New Specification → 选 equation set 与未用编号 → 给每个变量 Actual/min/max/unit → File > Download → 保存 Timing Setup；含 EQNSET 与 SPECSET 单位冲突警告及两种处理。 |
| `02.08.04.34.06.04` | Methodology for Generating Complex Device Cycles | 从 datasheet 的 device cycle 出发生成复杂 device cycle 的方法。 |
| `02.08.04.34.06.04.01` | Considering Tri-state Switching Accuracy | 切换到 tri-state 的 edge 受 tri-state 精度约束，不受普通驱动精度约束。 |
| `02.08.04.34.06.05` | Setting the period | Select > period 输入 ns；改小 period 可能触发自动修正并在 report window 提示。 |
| `02.08.04.34.06.05.01` | Minimum period / maximum frequency of the sequencer | 各卡最小 period/最大频率：PS1600 2.5 ns/400 MHz，DPS128/DPS64 20 ns/50 MHz，UHC4T 2.5 ns/400 MHz，XPS256 20 ns/50 MHz。 |
| `02.08.04.34.06.06` | Generating a Device Cycle | 生成 device cycle 的离散步骤列表。 |
| `02.08.04.34.06.06.01` | Watching System Resources | 输入 waveform 会消耗系统资源；靠选边沿、分配 action、复用 waveform/index 优化；资源清单见 Timing edges。 |
| `02.08.04.34.06.06.02` | Checking Edge Usage | i/o 列显示该 edge 已被哪些类型 pin 使用。 |
| `02.08.04.34.06.06.03` | Selecting Edges | 选中 edge 才能使用它。 |
| `02.08.04.34.06.06.03.01` | Dropping Unused Edges | 不用的 edge 可移回 unused edge box（位置 0 ns）。 |
| `02.08.04.34.06.06.04` | Positioning Edges | 把 edge 移到 cycle 内某个 delay。 |
| `02.08.04.34.06.06.04.01` | Setting Edge Snapping | 设置 edge snapping 的分辨率。 |
| `02.08.04.34.06.06.05` | Generating a Default Device Cycle | Pattern Tool 的 Display 模式需要 Default Device Cycle。 |
| `02.08.04.34.06.06.06` | Downloading Your Timing Setup into the Firmware | 通过“点到另一个 device cycle”把 waveform 输入 firmware；资源不足时拒绝下载并在 report window 报错。 |
| `02.08.04.34.06.07` | Editing Device Cycles and Waveforms | 显示与编辑 device cycle/waveform 的功能总览。 |
| `02.08.04.34.06.07.01` | Displaying the Timing | 两种显示方式：table format 与 one pin。 |
| `02.08.04.34.06.07.01.01` | Displaying Device Cycles for Pins in Table Format | Select > format pins 的表格显示。 |
| `02.08.04.34.06.07.01.02` | Displaying Device Cycles Generated for One Pin | Select > one pin 的单 pin 显示。 |
| `02.08.04.34.06.07.02` | Using Device Cycle Setup and Edit Modes | 打开窗口默认是 setup mode，另有 edit mode。 |
| `02.08.04.34.06.07.03` | Selecting a Device Cycle for Display/Editing | 在 format pins 模式选择要显示/编辑的 device cycle。 |
| `02.08.04.34.06.07.04` | Selecting a Waveform for Editing | 先选 test system cycle 与 waveform 才能编辑。 |
| `02.08.04.34.06.07.05` | Clearing the Timing Setup | 建新 timing 前清旧 setup 的方法。 |
| `02.08.04.34.06.08` | Using the Marker and Cursor | 用 marker 与 cursor 做跨信号/跨 cycle 的精确比较。 |
| `02.08.04.34.06.09` | Setting up the Table Format | 只显示当前关心的 pin。 |
| `02.08.04.34.06.09.01` | Defining the Table Format | 新建 table format 的步骤。 |
| `02.08.04.34.06.09.02` | Editing the Current Table Format | Format > edit current format。 |
| `02.08.04.34.06.09.03` | Deleting a Table Format | 删除已有 table format。 |
| `02.08.04.34.06.09.04` | Selecting Other Saved Formats | 可存最多 999 个 table format。 |
| `02.08.04.34.06.10` | Configuring the output of the Timing Setup window | 窗口输出的配置方式。 |
| `02.08.04.34.06.10.01` | Displaying the Timing Setup in Double Size | Code > double size。 |
| `02.08.04.34.06.10.02` | Getting a Hardcopy of the Timing Setup Window | Doc > hardcopy。 |
| `02.08.04.34.06.11` | Working with Multiple Waveform and Timing Sets | 多 waveform/timing set 的操作索引。 |
| `02.08.04.34.06.11.01` | Creating Waveform and Timing Sets | 新建 waveform set 的步骤。 |
| `02.08.04.34.06.11.02` | Keeping Waveform Sets Compatible | 测试所需 vector 必须与 timing setup 匹配，不能随意改已配套的 waveform set。 |
| `02.08.04.34.06.12` | Performing Timing Checks | timing/test 能否执行的检查功能总览。 |
| `02.08.04.34.06.12.01` | Checking for Compatible Waveform Sets | 修改 timing 后检查 waveform set 兼容性。 |
| `02.08.04.34.06.12.01.01` | Checking a Waveform Set against another Waveform Set | 任意两个 waveform set 的通用比较。 |
| `02.08.04.34.06.12.01.02` | Checking the Base Waveform Set against another Waveform Set | Base Waveform Set（当前解释 Vector 数据的 set）与另一 set 比较。 |
| `02.08.04.34.06.12.02` | Checking for Timing Limitations at Device Cycle Boundaries | 最小 pulse/window 宽度写死 500 ps；cycle 内与 device cycle 边界都受限；两种检查。 |
| `02.08.04.34.06.12.02.01` | Checking for All Possible Combinations of Device Cycle Sequences | 检查所有 device cycle 相邻组合。 |
| `02.08.04.34.06.12.02.02` | Checking for the Combinations used in the Selected Test | 只检查所选 test 里实际出现的组合。 |
| `02.08.04.34.06.12.02.02.01` | Checking for the Combinations used in the Selected Test | 与 `02.08.04.34.06.12.02.02` 同题同文（重复投放）。 |

#### Timing Setup window（`02.08.04.34.07.*`）

| 分类号 | 文档 | 一句话 |
|---|---|---|
| `02.08.04.34.07` | The Timing Setup Window | 窗口分三区：Global Information、Timing Entry、Device Cycle Edit；本章用于设置 fixed timing。 |
| `02.08.04.34.07.01` | The Global Information Area | 显示/输入 current waveform set（WFset #）、current timing set（Tset #）、默认 device cycle、显示 cycle 数。 |
| `02.08.04.34.07.02` | The Timing Entry Area | 三个 overlay：Period、Edge Delays、Cursor/Marker。 |
| `02.08.04.34.07.03` | The Period Overlay | 显示并设置 tester period（单位 ns）。 |
| `02.08.04.34.07.04` | The Edge Delays Overlay | 显示每条 edge 的 delay（ns），可选择并定位 edge。 |
| `02.08.04.34.07.05` | The Cursor and Marker Overlay | marker 提供跨信号/跨 cycle 的参考位置。 |
| `02.08.04.34.07.06` | Device Cycle Edit Area | 横轴 device cycle、纵轴 tester cycle 的矩阵编辑区。 |
| `02.08.04.34.07.06.01` | Displaying inhomogenous timings | 只有 timing 同构时才能按 device cycle 显示；非同构时另作显示。 |

### 归属判定

这一节是判断，不是文档事实，供维护者复核。

- **`DSCP` 判给 [[project]]，但在 L1 表里完整列出**。它确实在 `02.06.06.02`（`.02.10`）子树内，但内容是全局 Sequencer Memory 配额，会影响 level/timing/DPS/device cycle 全部参数集；`02.06.06.02.10` 还说它每次调用清空 Sequencer Memory。把它当 timing 命令展开，会让读者以为 timing 阶段才决定内存配额。
- **`DPRT`、`TSUX` 是 system-only**。两篇都在开头写明它们仅供系统使用，并要求不要从 hpt utility 执行（`02.06.06.02.09`、`.33`）。列出是为了覆盖完整，不代表用户该调用。
- **`EDDC?`、`EDSP` 判给 [[run]]/AC test，不在本阶段展开**。它们同时被投放在 `02.06.06.02`（`.02.11`、`.02.12`）和 `02.06.09.02`（AC test function commands）——后者才是其功能归属：`EDSP` 定义 timing search 的 leading/trailing 搜索边沿，`EDDC?` 查 data parameter + logical device cycle 的 leading/trailing edge。它们是测量/搜索配置，不是 timing setup。
- **`SPRM` / `APRM` / `FTCG` 判给 [[testflow]]/[[run]] 的 primary set 选择**。`SPRM` 定义 primary 的 waveform set / specset / timing set / level set / DPS set；`APRM` 把它激活到硬件；`FTCG` 改 primary set 激活行为。它们在本页列出，因为 timing set 的选择发生在这里；但“哪个 test suite 用哪个 primary set”属于 testflow。
- **`SVLR` / `STRS?` 判给 [[run]] 的运行时调整**。`SVLR` 只改运行值、不改 setup 值，且在下一次 functional test 生效；`STRS?` 反复跑功能测试并扫 spec 变量。本页只保留其“运行期”性质，配置语义仍属 timing。
- **`RSET` 判给 [[project]] 的系统准备**，但从 L1 覆盖角度列出。`RSET TIM` 会把所有 waveform/timing 恢复上电默认值，是破坏性动作；放到“设置 timing”语境里容易被误用。
- **`UPTD` 判给跨 setup 的一致性检查**（Test Program Explorer）。它的 `TIM` flag 与 timing 直接相关，所以列在本页；命令本身不属于 timing 命令族。
- **`DCDT` / `DCUD` 判给 timing（wavetable）但被 pattern 消费**。device cycle 名写在 wavetable 里，vector 通过名字引用；`WSDM` 设的是 Vector Setup 的显示模式，也属 pattern GUI 的显示偏好。列出是因为它们在 `02.06.06.02` 子树内。
- **同形陷阱：`TOCF` / `TORN?` / `TORS?` / `TORR?` / `TORT?` / `TORC` / `TOUD` 不是本阶段命令**。它们名字带 timing，但属于 `02.06.09.02` 的 AC test function commands（embedded timing/level offset search），会改 primary timing 的 offset 并重跑功能测试；是测量/搜索，不是 setup。
- **同形陷阱：`TSHA?` 不是 timing setup 命令**。它问的是“指定 pin 的 wavetable 里有没有 `ARM` action”，属于 `02.06.13` 的 TMU 测量族。
- **`dm_tdiag` 不是 `dm_timing`**。`02.09.01.09.02` 把 `dm_timing` 描述为 timing setup、`dm_tdiag` 描述为 timing diagram；不要拿前者当后者。

## L1 — Firmware / Setup Command

**覆盖范围**：`show.py --list 02.06.06` 返回 102 篇；其中 `02.06.06` 是章入口、`02.06.06.01` 是概念章、`02.06.06.02` 是命令清单索引，命令文档为 `02.06.06.02.01`–`.46` 共 **46 条**。下表按分类号逐条列出，**不代表推荐执行顺序**；每条写命令 + 一句作用 + 出处。

| 分类号 | 命令 | 作用 | 出处 |
|---|---|---|---|
| `02.06.06.02` | List of timing setup commands | 命令清单索引，按字母序列出 46 条 timing 命令，本身无语法。 | `02.06.06.02` |
| `02.06.06.02.01` | `APRM` | 按 `FRC`（强制）或 `CNL`（条件）把 `SPRM` 告知 firmware 的 primary sets 激活到硬件；`FTST?`、`RCLS?`、`SQST RUN`、`PSST` 会自行激活，无需先执行它。 | `02.06.06.02.01` |
| `02.06.06.02.02` | `BWDF` / `BWDF?` | 定义 break waveform 的 actions；只允许 drive actions、不得含 data dependent actions；2.1 起在 14-edge setup 中被 `BWDS` 取代，>6 edge 时命令禁用、查询只回前 6 个 edge。 | `02.06.06.02.02` |
| `02.06.06.02.03` | `BWDS` / `BWDS?` | 用定义字符串设置 break waveform；查询返回指定 pin 当前的 break waveform。 | `02.06.06.02.03` |
| `02.06.06.02.04` | `CDCP?` | 对当前已激活 test 给一个 cycle 范围，逐 cycle 返回 device cycle 名与该 cycle 实际执行的 waveform 的 data parameters。 | `02.06.06.02.04` |
| `02.06.06.02.05` | `CLKR` / `CLKR?` | 定义单端口/多端口 timing specification 或 waveform set 的 period resolution；查询可选 `VIRTUAL`（period_res）或 `EXACT`（clock_res）。 | `02.06.06.02.05` |
| `02.06.06.02.06` | `DCDT` / `DCDT?` | 定义默认 device cycle 名；用于在多模式应用里补齐 tester cycle 以同步两条以上 vector stream。 | `02.06.06.02.06` |
| `02.06.06.02.07` | `DCUD` | 从 device cycle 表删除指定 device cycle；不影响 waveform 表与 physical waveform 表。 | `02.06.06.02.07` |
| `02.06.06.02.08` | `DFCR` / `DFCR?` | 改变 hardware group 内的 clock routing；查询只在非默认路由时显示完整路由。 | `02.06.06.02.08` |
| `02.06.06.02.09` | `DPRT` / `DPRT?` | system-only：默认 primary timing sets；文档明说不要从 hpt 执行。 | `02.06.06.02.09` |
| `02.06.06.02.10` | `DSCP` / `DSCP?` | 定义 device cycle、waveform set、timing set、level set、DPS set、device cycle set 等的最大实例数并为 Sequencer Memory 预留空间；每次调用清空 Sequencer Memory；参数可写在 `.technology`。 | `02.06.06.02.10` |
| `02.06.06.02.11` | `EDDC?` | 对 data parameter + logical device cycle 的组合，求 leading 或 trailing edge（搜索用）。 | `02.06.06.02.11` |
| `02.06.06.02.12` | `EDSP` / `EDSP?` | 定义 timing search 的两个搜索边沿（leading / trailing）；AC test 用。 | `02.06.06.02.12` |
| `02.06.06.02.13` | `EQFS` | 编辑器工具用的 equation based 文件 load/save：`spec_type`（LEV/TIM）、`part`（WVT/EQN/SPS）、`LOAD`/`SAVE`、文件路径；错误可导向文件或 `UI_REPORT`。 | `02.06.06.02.13` |
| `02.06.06.02.14` | `EQSP` / `EQSP?` | 以二进制下载 equation based setup 数据块（wavetable/equation/spec）；查询以二进制返回当前 setup；用于 setup 文件与 Test Program Explorer。 | `02.06.06.02.14` |
| `02.06.06.02.15` | `ETDS` / `ETDS?` | 在已有 waveform set/specification 的指定 timing set、指定 pins 上定义或修改 edge delay；equation based 下只改运行值；fast pin 支持 `pdiv:n` 与 `DELTA` 偏移。 | `02.06.06.02.15` |
| `02.06.06.02.16` | `ETIM` / `ETIM?` | 旧版 edge timing 命令；2.1 起 14-edge setup 用 `ETDS` 取代，≤6 edge 仍可用。 | `02.06.06.02.16` |
| `02.06.06.02.17` | `EUDS?` | 返回指定 waveform set 全部 edge 的方向（drive 或 receive）。 | `02.06.06.02.17` |
| `02.06.06.02.18` | `EVCK?` | 返回 multiport timing specification 各 port 的 event clock period（可与 system clock period 不同）。 | `02.06.06.02.18` |
| `02.06.06.02.19` | `FTCG` / `FTCG?` | 改变系统在 primary set 激活方面的行为。 | `02.06.06.02.19` |
| `02.06.06.02.20` | `PCLK` / `PCLK?` | 定义指定 waveform set/equation set 与 timing set 的 test system period；`@` 给全部 pin 同一 period，否则按 pin 设；可触发 period resolution 重算与 timing set >1 的自动修正。 | `02.06.06.02.20` |
| `02.06.06.02.21` | `PDIV?` | 返回指定 setup component 里 fast pin（`CONF` 的 FAST 选项）的 period divider。 | `02.06.06.02.21` |
| `02.06.06.02.22` | `RCLK?` | 查当前启用的是外部还是内部 reference clock。 | `02.06.06.02.22` |
| `02.06.06.02.23` | `RSET` | 用上电默认值加载指定类型的文件；`RSET TIM` 恢复默认 timing（只激活 waveform set 1 / timing set 1）。 | `02.06.06.02.23` |
| `02.06.06.02.24` | `SCLK?` | 返回指定 waveform set/specification 的 system clock 值（协调各通道同时启动的参考时钟）。 | `02.06.06.02.24` |
| `02.06.06.02.25` | `SDSC?` | setup component 的编号与描述互查；找不到时返回空。 | `02.06.06.02.25` |
| `02.06.06.02.26` | `SPCP?` | 显示某个 multiport specification 适用的 port 列表。 | `02.06.06.02.26` |
| `02.06.06.02.27` | `SPEC?` | 返回当前 setup 与硬件配置的信息。 | `02.06.06.02.27` |
| `02.06.06.02.28` | `SPRM` / `SPRM?` | 定义/修改 test suite 或 user procedure 的 primary sets：timing equation+spec set、multiport spec、waveform set、timing set（或 list）、level set、DPS set；不激活硬件。 | `02.06.06.02.28` |
| `02.06.06.02.29` | `SPST?` | 返回 spec set 的 status bits；多数 bit 决定执行时做哪些 edge order / period 违规检查（bit 清零时检查，置位时跳过）。 | `02.06.06.02.29` |
| `02.06.06.02.30` | `STRS?` | 循环重复 functional test，并系统性地改一个 timing 或 level spec 变量的值。 | `02.06.06.02.30` |
| `02.06.06.02.31` | `SVLR` / `SVLR?` | 把 base（spec）变量设为给定值并重算 timing/levels；值必须在 spec set 的 min/max 内，改动在下一次 functional test 生效，setup 值不变；查询可返回实际值、派生值、all/spec/equa、max/min/unit。 | `02.06.06.02.31` |
| `02.06.06.02.32` | `TSUS` / `TSUS?` | 定义给定 waveform set 内 timing set 的数量；超过上限的 set 会被删除；总上限 512、默认 256、单 set 最多 256。 | `02.06.06.02.32` |
| `02.06.06.02.33` | `TSUX` / `TSUX?` | system-only：extended timing sets used；文档明说不要从 hpt 执行（查询可执行）。 | `02.06.06.02.33` |
| `02.06.06.02.34` | `UPTD` / `UPTD?` | 把某 setup/result/command set 声明为 up-to-date / out-of-date；`UPTD?` 返回硬件的 `flag`（1 = 文件与硬件一致，0 = 不一致）；`TIM` 针对 timing setup。 | `02.06.06.02.34` |
| `02.06.06.02.35` | `VCLK?` | 检查期望的 test system period 是否会引起 auto-correction，返回 0 或 1。 | `02.06.06.02.35` |
| `02.06.06.02.36` | `VDCG?` | 对一组 pin 做 device cycle 一致性检查；也可在 `TSTL` 指定的当前 label 语境里用。 | `02.06.06.02.36` |
| `02.06.06.02.37` | `VTIM?` | 检查一个或全部 timing set 里指定 pin 的 period 与 edge timing 是否相同；multiport 下逐 port 比较。 | `02.06.06.02.37` |
| `02.06.06.02.38` | `VWFG?` | 检查指定 pin 是否具有相同的 device cycle 与 waveform 定义，返回 0/1。 | `02.06.06.02.38` |
| `02.06.06.02.39` | `VWFS?` | 检查两个 waveform set 对指定 pin 是否兼容（比较 device cycle 名/序列、`WFDF`/`WAVE` 定义的波形与 data parameters），返回 0/1。 | `02.06.06.02.39` |
| `02.06.06.02.40` | `WAVE` / `WAVE?` | fixed timing 下用 `DD1`/`DD2`/`ED1`/`ED2` 给 logical waveform 的 data parameter 赋值并分配 physical waveform index；没有 `WAVE` 就没有可执行波形；`ALLOW_EQ` 可改 equation based 的运行期定义。 | `02.06.06.02.40` |
| `02.06.06.02.41` | `WFDF` / `WFDF?` | fixed timing 下定义最多 6 个 edge 的 logical waveform；覆盖同名索引会清掉其 physical waveform；查询只回前 6 个 edge。 | `02.06.06.02.41` |
| `02.06.06.02.42` | `WFDS` / `WFDS?` | 用定义字符串定义 logical waveform（fixed timing），也可在 equation based 下改 logical 或 pure physical waveform 的运行期定义；`ALLOW_EQ` 只改运行设置。 | `02.06.06.02.42` |
| `02.06.06.02.43` | `WFUD` | 删除 `WFDF`/`WFDS` 定义的 logical waveform 及其全部 `WAVE` physical waveform；在 equation based 下可删运行期定义。 | `02.06.06.02.43` |
| `02.06.06.02.44` | `WRST` | 重置指定 waveform set、全部 pin 的全部 timing set 与 waveform 定义，并更新硬件；文档说没有错误消息。 | `02.06.06.02.44` |
| `02.06.06.02.45` | `WSDM` / `WSDM?` | 设置 Vector Setup 的 display mode。 | `02.06.06.02.45` |
| `02.06.06.02.46` | `WSUS` / `WSUS?` | 设置已定义 waveform set 的数量（1–最大 16）；可用它删除指定编号以上的 set；上电只有 1 个。 | `02.06.06.02.46` |

### 最小可用示例

以下示例逐字取自文档的 Example 段。

**fixed timing 的完整 shape 链**（`02.06.06.01.07.02`，节选）：

```
WFDS 1,0,,"d1:F00 d2:D11 d3:F0N",(IN1)
WAVE 1,0,F00,,,,0,(IN1)
WAVE 1,0,F10,,,,1,(IN1)
WFDS 1,1,,"d1:FN0 d2:D11 d3:F0N",(IN1)
WAVE 1,1,F00,,,,2,(IN1)
WAVE 1,1,F10,,,,3,(IN1)
WFDS 1,2,,"d2:F1N d3:F0N",(IN1)
WAVE 1,2,,,,,4,(IN1)
WFDS 1,3,,"",(IN1)
WAVE 1,3,,,,,5,(IN1)
WFDS 1,4,,"d4:D22",(IN1)
WAVE 1,4,,F00,,,6,(IN1)
WAVE 1,4,,F10,,,7,(IN1)
WFDS 1,5,,"d5:C2N",(IN1)
WAVE 1,5,,F0N,,,8,(IN1)
WAVE 1,5,,F1N,,,9,(IN1)
BWDS 1,,,"",(IN1)
```

**fixed timing 的 period 与 edge delay**（`02.06.06.01.07.03`、`.07.04`）：

```
PCLK 1,1,12,(@)
ETDS 1,1,,"d1:2 d2:4 d3:8 d4:6 d5:10",(IN1)
```

**logical waveform + 两个 physical waveform**（`02.06.06.02.40`）：

```
> WFDS 1,2,,"d1:D11 d3:0 d4:C11",(pin1,pin2,pin3,pin4)
> WAVE 1,2,F00,,,,4,(pin1,pin2,pin3,pin4)
> WAVE 1,2,F10,,,,5,(pin1,pin2,pin3,pin4)
```

**WFDS 定义与回读**（`02.06.06.02.42`）：

```
> WFDS 1,0,,"e1:F00 e2:D1N e3:F00",(io)
> WFDS 1,1,,"r4:EE1",(io)
> WFDS 1,0,,"d1:F00 d2:F10 d3:F10 d4:F00 d5:F10 d6:F00 d7:F10 d8:F00",(clk)
> WFDS? 1,ALL,,(@)
< WFDS 1,0,,"d1:F00 d2:D1N d3:F00",(io)
< WFDS 1,1,,"r4:EE1",(io)
< WFDS 1,0,,"d1:F00 d2:F10 d3:F10 d4:F00 d5:F10 d6:F00 d7:F10 d8:F00",(clk)
```

**WFDF 六 edge 例**（`02.06.06.02.41`）：

```
> WFDF 1,2,N,N,D11,N,N,N,(D0,D2,D2,D3)
```

**break waveform**（`02.06.06.02.02`）：

```
BWDF 1,N,N,N,F1N,F0N,N,(D0,D1,D2,D3)
```

**period / resolution**（`02.06.06.02.20`、`.02.05`）：

```
PCLK 101,1,20,(@)
PCLK 101,1,40,(S1)
```

```
> CLKR 1,,10
> CLKR? 1
< CLKR 1,1000,10
```

**edge delay（equation based specset 101、timing set 1）**（`02.06.06.02.15`）：

```
> ETDS 1,1,,"e1:0 e2:2 e3:6 e4:4",(io)
> ETDS 1,1,,"d1:0 d2:1 d3:2 d4:3 d5:4 d6:5 d7:6 d8:7",(clk)
> ETDS? 1,1,,(@)
< ETDS 1,1,,"d1:0 d2:2 d3:6 d4:4 r1:0 r2:2 r3:6 r4:4",(io)
< ETDS 1,1,,"d1:0 d2:1 d3:2 d4:3 d5:4 d6:5 d7:6 d8:7",(clk)
```

**multiport specification 的 edge delay**（`02.06.06.02.15`）：

```
> ETDS? "mu_timing",2,,(In1)
< ETDS ETDS "mu_timing",2,,"d1:0",(In1)
> ETDS "mu_timing",2,,"d1:0.5",(In1)
```

**集合数量与 reset**（`02.06.06.02.46`、`.02.32`、`.02.44`）：

```
WSUS 3
TSUS 3,7
WRST 3
```

**primary sets（timing 部分）**（`02.06.06.02.28`）：

```
> SPRM "spec_ClockP_P1_P2","2,1,2",,
> SPRM?
< SPRM "spec_ClockP_P1_P2","2,1,2",101002,101003
```

**multiport timing specification 的文法**（`02.06.06.01.05.03`，节选）：

```
SPECIFICATION "MultSpec"
{
CHECK all
EQNSET 1 "equation set 1"
WAVETBL "wavetable A"
PORT Port1
SYNC
{
PHASE
SEQUENCE "gr1"
}
var 8

EQNSET 1 "equation set 1"
WAVETBL "wavetable B"
PORT Port2
SYNC
{
PHASE
SEQUENCE "gr2"
}
var 12

EQNSET 2 "equation set 2"
WAVETBL "wavetable B"
PORT Port3
SYNC
{
PHASE
SEQUENCE "gr2"
}
var 10
}
```

**完整 timing 文件**见 `02.08.04.34.04.04`；文件头为 `hp93000,timing,0.1`，正文由 firmware 命令（`PCLK`、`CLKR`、`BWDS`、`ETDS`、`DCDT`、`TSUX`…）、`EQSP` 二进制块、`WAVETBL` / `EQNSET` / `CHECK` / `SPECSET` 组成，末尾有 `NOOP`。这说明 equation based 数据在文件里是**以 `EQSP` 内嵌块**出现的，而不是逐条命令可编辑的对象——`02.06.06.01.02` 明说 “The collections themselves cannot be edited with firmware commands.”

### L1 内记录的文档矛盾

1. **timing set 数量上限**。`02.08.04.34.03.02` 写 “The system lets you create up to 999 different timing sets.”；同一章 `02.08.04.34.03.01` 写 “You can store a maximum of 256 timing sets to a waveform set.”；`02.06.06.02.32` 写所有 waveform set 的 timing set 总数最大 512、默认 256，单 set 最多 256。三个数字并列记录，**不自行选一个当正确答案**；实际可用量需按 `DSCP` 与硬件配置在实机核对。
2. **master clock period**。`02.06.06.01.04.01.02.03` 写 “For SmarTest 7.10 the master clock period is fixed at 8/3 = 2.67 ns (frequency of 375 MHz).”；`02.08.04.34.03.02` 写 “The master clock period always remains in the range of 4 to 10 ns.”。**推断**：后者是旧版界面的描述（该页的 `Functional changes` 只到 `Introduced before SmarTest 6.3.2`，没有 7.x 变更记录），前一篇明确针对 7.10；但文档没有声明前者已废弃，因此并列保留，实机以 `SCLK?` / `CLKR? EXACT` 读回为准。
3. **`WFDS` 的 waveform 索引范围**。`02.06.06.02.42` 的 Parameters 写 `wfIndex` 为 0–255，Errors 写 “outside the range of 0 - 256”；`02.06.06.02.41` 的 `WFDF` 写 0–31。原文自相矛盾（0–255 / 0–256），照录，不修正。

## L2 — Test Method API

**文档事实（边界）**：测试方法侧访问的是**已存在的** timing 数据容器，不负责创建 wavetable/equation set。`02.07.04.01.249` 开头写明：

> The TIMING_SPEC API accesses the data container holding the contents of an existing timing equation and spec set.

- **`TIMING_SPEC`**（`02.07.04.01.249`）。头文件 `/opt/hp93000/soc/prod_com/include/MAPI/TimingSpec.h`；构造 `TIMING_SPEC(INT eqnset, INT specset)`。
  - `getEquation()` — 返回 equation set 号。
  - `getSpec()` — 返回 spec set 号。
  - `getSpecValue(const STRING& spec)` — 读 spec 值；multiport 用 `"spec@port"`。
  - `change(const STRING& spec, DOUBLE value)` — 改 spec 值，值必须在 spec set 的 min/max 内；`10 ns` 这类单位写法可用。
  - `restore()` — 把当前 testsuite 启动时的 spec 值恢复。
  - 生效时机：`EXECUTE_TEST`、`START_TEST`、`DIGITAL_CAPTURE_TEST`、`NB_DIGITAL_CAPTURE_START`、`FUNCTIONAL_TEST`，或 `FLUSH` 后接 `SPEC_SEARCH.execute()` / `SEQUENCER_STATUS.run()` / `PMU_IFVM.execute()` / `PMU_VFIM.execute()` / `TASK_LIST.execute()` / `DPS_VFIM.execute()`。`FLUSH` 也可把改动反映到 MCD（Test Program Explorer / Spec Tool）。
  - 文档给了最小用法：

```
TIMING_SPEC spec1(1, 2);
Primary.timing(spec1);
Primary.timing(1);
```

```
Primary.getTimingSpec().change("Tp", 10);
DOUBLE specValue = Primary.getTimingSpec().getSpecValue("Tp");
```

- **`PRIMARY_STATUS`**（`02.07.04.01.167`）：`timing(...)` 设 primary timing spec/set；`getTimingSpec()` 取当前 primary 的 `TIMING_SPEC`；`getTiming()` / `getTiming(const STRING& port)` 读 timing set；multiport 还有 `isTimingPortBased()`、`getSpecification()`。文档说 `CTIM` 在 vector generation 中切 timing set **不会**改变 primary timing set 的定义。
- **`SPECIFICATION`**（`02.07.04.01.232`）：multiport timing 的 specification 容器，按 port 改 spec 值；配 `PRIMARY_STATUS.timing(SPECIFICATION)` 使用。
- **`DIGITAL_WAVEFORM`**（`02.07.04.01.37`）：不定义 setup，但 `timingResolution()` / `getTimingResolution()`（`02.07.04.01.37.16`）用于数字波形捕获的时间分辨率；相关但不等价于 timing setup 的 period resolution。
- **`TIMING_OFFSET_SEARCH_TASK`**（`02.07.04.01.248`）：对已有 timing 做 offset search 并回写测量结果，头文件 `MAPI/TimingOffsetSearchTask.h`；文档建议改用 `DIGITAL_OFFSET_SEARCH_TASK`。它是**测量/校准**，不是 setup 编辑。

**文档事实（文件层面）**：`02.07.11.01.05.02` 描述 timing equation file 的 `USE_PROTOCOL` 语句，可把 protocol timing segment（protocol 目录下的 `.prot_tim` XML）并入 equation system；可在 `SPECS`/`EQUATIONS` 使用，**不得写在 `SPECSET` 段**。

**本次未找到**任何在 C++ 测试方法里创建 wavetable、equation set、spec set 或写回 timing setup 文件的 API；测试方法能改的是已有 spec set 的**运行值**，且文档用 CAUTION 警告不要与 firmware 的 `SVLR` 混用（`02.07.04.01.249`、`02.06.06.02.31`）。**推断**：L2 与 L1 的分工是“L1 建 timing 容器，L2 在运行中改 spec 值并切 primary”。

## L3 — 外部控制

**L3 入口是横切的，能力面按阶段分族。** 横切入口是 `Test Suite Control API`（`02.09.01.14`）、`TPI Program Routines`（`02.09.01.09`）与 `HVM API`（`02.09.01.10`）；本阶段的专属族是 `TestsuiteProxy` 的 timing 方法、TPI 的 `dm_timing` 文件类型，以及 HVM 的 test program 下载（间接）。

**文档事实（Test Suite Control API 的边界）**：`02.09.01.14` 写明：

> Test suite control API is used to directly control the test suites outside of the testflow tool. Only UTM-based test suites are supported with these APIs.

并写明：

> They cannot be used in test method programming and also cannot be used in parallel with HVM API and BLC API by the same client process.

### `TestsuiteProxy` 的 timing 族

- `getTimingEquation()`（`.02.01.18`）— 取 test suite 使用的 timing equation。
- `getTimingSet()`（`.02.01.19`）— 取 timing set。
- `getTimingSpec()`（`.02.01.20`）— 取 timing spec。
- `isMultiportTiming()`（`.02.01.22`）— 查当前 timing set 是否 multiport timing。
- `setEquationBasedTiming(const std::string& timingEquation, const std::string& timingSpec, const std::string& timingSet)`（`.02.01.26`）— 设 equation based timing。
- `setMultiportTiming(const std::string& multiportSpec, const std::string& timingSet)`（`.02.01.27`）— 设 multiport timing。

对应关系：L1 的 `SPRM` 用 `specset_id` + timing set 号选 primary，`TestsuiteProxy` 用**名字字符串**选 timing equation/spec/set 与 multiport spec。**推断**：两者操作的是同一组 primary timing 概念，但文档没有声明可互替，**不能据此认为等价**，混用需实机确认。

### TPI 的 `dm_timing`

`02.09.01.09.02` 的 `Fid` 表把 `dm_timing` 描述为 “timing setup”，`dm_tdiag` 描述为 “timing diagram”。`Opc` 表给出 `dm_load`（replace current setup by file）、`dm_merge`（merge a file）、`dm_append`、`dm_save`、`dm_print`、`dm_copy_in`、`dm_delete`、`dm_utd`（返回文件是否 up-to-date）。**文档事实**：timing setup 是 `DataManager` 的一个文件类型，因此可整文件 load/save/merge，而不是逐条 timing 命令的远程封装。

**同形陷阱**：`dm_tdiag` 是 timing diagram，不是 `dm_timing`；`dm_level` 是 level setup，不是 timing。

### HVM API

`02.09.01.10.01` 把 HVM API 分为 SmarTest Session Management、Test Execution、Hardware Information、Calibration and Diagnostic 四类。与本阶段沾边的是 Test Execution：

- `DownloadTestprogram`（`02.09.01.10.03.02.02.20`）— 下载 test program，包括 test flow、setup files 与其他组件；每个 setup 文件下载都会发 `SETUPFILE_DOWNLOAD_STARTED` / `SETUPFILE_DOWNLOAD_COMPLETED`。
- `ChangeDevice`（`02.09.01.10.03.02.02.12`）— 设置 SmarTest session 的目标 device；开始与完成时分别发 `DEVICE_CHANGE_STARTED` / `DEVICE_CHANGE_COMPLETED`；执行前要确保 session 在运行且没有另一个 change device 在进行。

**本次未找到** timing 专用的 HVM 命令；只能通过 test program / device 下载间接带上 timing setup。**推断**：若要从外部只改 timing 并单独下发，HVM 不是合适入口，应看 TPI 的 `DataManager(dm_timing, ...)`。

### SmartShell

`02.15` 的 `Functional changes` 写明 **`Introduced in SmarTest 8.2.5`**，而本 wiki 面向 SmarTest 7.10.3。**结论（文档事实）**：SmartShell 在本 wiki 的目标版本不存在，不能作为本阶段的 L3 接口；该章正文只有 PDF 外链，也没有 timing 级内容。

### 同形陷阱（记下来防止被“补”进 L3）

- `TOCF`/`TOCF?`、`TORN?`、`TORS?`、`TORR?`、`TORT?`、`TORC`、`TOUD` — 名字含 timing，但它们是 `02.06.09.02` 的 embedded timing/level offset search 命令族，用于测量并修正 primary timing 的偏移，不是 setup 的 L1/L3 入口（`02.06.09.02.17`）。
- `TSHA?` — 名字是 “Timing Setup Has Arming”，实际查 wavetable 里有没有 TMU 的 `ARM` action，属于 `02.06.13` 的 TMU 测量（`02.06.13.02.04`）。
- `DRLTimingsAttr` — 数据日志的 timing 属性，不是 timing setup。

## 产物

**文档事实**：

- **timing setup 文件**：`02.06.06.01.05` 说明文件位于 `<device_folder>/timing`，文件名可自取（例 `timingSpec1`）。`02.08.04.34.04.04` 给出完整示例，文件头是：

```
hp93000,timing,0.1
```

  正文包含 firmware 命令（`PCLK`、`CLKR`、`BWDS`、`ETDS`、`DCDT`、`TSUX`）、`EQSP TIM,WVT,#...` / `EQSP TIM,EQN,#...` / `EQSP TIM,SPS,#...` 数据块，以及 `WAVETBL`、`EQNSET`、`CHECK`、`SPECSET` 文本；示例以 `NOOP "6.5.3",,,` 结尾。`02.06.06.01.02` 明说这些数据集合**不能**用 firmware 命令编辑，只能查询与在运行期改定义。
- **可选 master 文件**：`02.08.04.34.04.05` 说明可把 wavetable、equation set（连同其单端口 timing specification）、multiport specification、common block 拆成子文件，用 master 文件连接；`02.08.04.34.04.05.01` 给出格式：首行 `hp93000,timing_master_file,0.1`，第二行 `testerfile: <tester_file_name>`，随后是 `WAVETABLE <name> [PIN_ALIAS_SET <set>]: <file>`、`EQNSET <n> [PIN_ALIAS_SET <set>]: <file>`、`MULTIPORT_SPEC "<name>": <file>`、`DEFINES: <file>`；路径可相对（以 master 文件目录为基准）可绝对；`#` 开头为注释。自动生成的文件名规则为 `eqnset_<n>.tim`、`wvt_<name>.tim`、`mport_<name>.tim`、`defines.tim`，可用 `VERIGY93000_MFH_PREFIX` 加前缀。
- **协议 timing 段**：`02.07.11.01.05.02` 说 `USE_PROTOCOL` 引用的 timing segment 存为 device 的 protocol 目录下 `.prot_tim` XML；可在 `SPECS` / `EQUATIONS` 引用，不能在 `SPECSET` 引用。
- **fixed timing 的组织**：`02.06.06.01.07.01` 说 fixed timing 的数据组织为 waveform set → 一套 shape（logical/physical/device cycle）+ 一个或多个 timing set；由 `WFDS`/`WAVE`/`ETDS`/`PCLK` 定义。**文档未覆盖** fixed timing 文件的独立完整样例（现有完整样例是 equation based 的 `02.08.04.34.04.04`）。
- **不产出结果数据**：本阶段产出的是 setup 文件与其在硬件上的下载状态；结果数据在 [[results]]。
- **旁证（非本阶段工具行为）**：`01.07.01.01.01` 的 device 目录清单里同时有 `timing` 与 `timing_dgrm`；`timing_dgrm` 是 timing diagram 目录，不是 timing setup 的产物，本页不把它算作本阶段输出。

**文档事实（副作用）**：`02.06.06.02.10`：

> Note Every call of DSCP deletes all data that were previously contained in the Sequencer Memory. Therefore, you have to reload the device setup after changing parameters using the DSCP command.

## 验证

- **GUI 下载即校验（首选）**：
  - wavetable：`02.08.04.34.06.01` 步骤 `Shell > Download`；若有错，report window 会给错误；下载后 Test Program Explorer 会 out of date，需要保存 Timing Setup。
  - equation set：`02.08.04.34.06.02` 说 `Shell > Download` 时会检查语法，错误进 report window。
  - spec set：`02.08.04.34.06.03` 说 Spec Tool 的 `File > Download` 下载变量值，求值错误进 report window。
  - 波形录入：`02.08.04.34.06.06.06` 说点另一个 device cycle 即把 waveform 输入 firmware；资源不足时拒绝下载并在 report window 报错。
- **GUI timing 检查**：`02.08.04.34.06.12` 提供两类检查——waveform set 兼容性、device cycle 边界上的 timing 限制；`02.08.04.34.06.12.02` 说明最小 pulse/window 宽度在软件内设为 500 ps，且可在 cycle 内与 device cycle 边界两处违反；该页另提醒软件可编程的最小值低于系统规格值，设更小值需实测验证信号性能。
- **multiport 目视验证**：`02.08.04.34.04.02.01` 的步骤——`Select > Show Eqn & Spec Results`、`Select > Select Specification...` 选 specification、`Select > Port...` 切 port，再看 `Equation` / `Wavetable` / `Tset#` / `Timing` 字段与波形。
- **命令回读**：

| 查询 | 能确认什么 | 出处 |
|---|---|---|
| `VTIM? <set>,<tset>,(<pins>)` | 指定 pin 的 period 与 edge timing 是否一致，返回 1/0 | `02.06.06.02.37` |
| `VWFG?` | 指定 pin 的 device cycle 与 waveform 定义是否一致，返回 1/0 | `02.06.06.02.38` |
| `VDCG?` | 一组 pin 的 device cycle 一致性；可在 `TSTL` 当前 label 下查 | `02.06.06.02.36` |
| `VWFS? <set1>,<set2>,(<pins>)` | 两个 waveform set 是否兼容，返回 1/0 | `02.06.06.02.39` |
| `VCLK? <set>,<tset>,<period>,(<pins>)` | 该 period 是否会被 auto-correct，返回 0/1 | `02.06.06.02.35` |
| `CLKR? EXACT <set>` | 实际 clock resolution（`VIRTUAL` 查 period resolution） | `02.06.06.02.05` |
| `TSUS? <set>` / `WSUS?` | 当前 timing set / waveform set 数量 | `02.06.06.02.32`、`.46` |
| `SPST?` | 哪些 edge order / period 检查是启用的 | `02.06.06.02.29`、`02.06.06.01.05.01` |
| `SVLR? TIM,<eqn>,[specset],"<name>"` | spec / equation 变量的实际值、MIN/MAX/UNIT | `02.06.06.02.31` |
| `UPTD? TIM` | 文件与硬件是否一致（1/0） | `02.06.06.02.34` |
| `SPEC?` / `SCLK?` / `EVCK?` / `RCLK?` / `PDIV?` | 当前 setup/硬件配置、system clock、event clock、reference clock、fast pin period divider | `.02.27`、`.02.24`、`.02.18`、`.02.22`、`.02.21` |
| `SPCP?` / `TSUS? "<spec>"[,(port)]` | multiport specification 的 port 列表与各 port 的 timing set 数 | `02.06.06.02.26`、`.32` |
| `SDSC?` | setup component 编号与描述互查 | `02.06.06.02.25` |

- **错误报告口径**：`02.08.04.34.04.03.06` 说 timing 违规检查覆盖 `period_res`、`period`、`d1-d8`、`r1-r8`；若违规来自含 spec 的方程，会按 setup 值、再按 min、再按 max 组合求值并逐项报错；错误消息给出 specset、resource、求值结果、以及是哪个 spec 的 min/max 导致。
- **建议**：每次下载后用 `UPTD? TIM` + `VTIM?` + `VWFS?` 做一次机器可读的核对，再用 `SPST?` 确认检查没有被关掉；**本次未找到**一条“整份 timing setup 一键校验”的命令，只能按对象逐条查。这是建议，不是文档要求。

## 常见错误

**文档事实**：timing 命令族没有像 pin 配置那样的单篇总错误章；错误条件分散在各命令 `Errors` 段与 `02.08.04.34.04.03.06`。下表按症状归并。

### 命令级症状

| 症状 | 可能原因（文档） | 排查入口 | 出处 |
|---|---|---|---|
| `WFDF`/`WFDS` 报 edge action 与 edge order 不匹配 | 同一 waveform 内同类 drive edge 的 delay 未递增，或 window open/close 缺失 | 用 `ETDS?` 看 delay；重排 waveform 或改 delay；注意 CHECK 可关闭检查 | `02.06.06.02.41`、`.42`、`02.06.06.01.03.01.02.01` |
| `WFDF`/`WFDS` 只发 warning、edge 被自动修正 | 未用 edge 的位置不符合新定义隐含的顺序，系统自动修正 | 读 warning；核对 `ETDS?` 与实际使用的 edge | `02.06.06.02.41`、`.42` |
| `WAVE` 报 “no logical waveform exists” | 未先用 `WFDS`/`WFDF` 定义 logical waveform | 先 `WFDS?`/`WFDF?` 回读 | `02.06.06.02.40` |
| `WAVE` 报 “redefine a physical waveform” | 同一 logical waveform 的 physical waveform 已存在 | 先 `WFUD` 删除，再重新 `WFDS` + `WAVE` | `02.06.06.02.40` |
| `WAVE`/`WFDS` 报 index 超范围 | waveform 索引超出 0–31 或 0–255（`WFDS` 的 Errors 段写 0–256，见 L1 矛盾记录） | 用合法索引；以目标卡型上限为准 | `02.06.06.02.40`、`.42` |
| `WFDF` 超过 6 个 edge | 该命令只支持 ≤6 edge | 改用 `WFDS` / `ETDS`（14-edge） | `02.06.06.02.41`、`02.06.06.01.07.02` |
| `ETDS` 在 equation based 下**不报** edge order 违规 | 文档明说 equation based 下 ETDS 违反 edge order 时不返回错误 | 不能靠报错判断；用 `VTIM?` / CHECK / 实机波形核对 | `02.06.06.02.15` |
| `ETDS` 报 window open/close 顺序错、edge 超出 period | delay 与 `WFDS`/`BWDS` 定义不一致，或同方向 edge 不在一个 period 内 | 回读 waveform 与 timing set，重排 | `02.06.06.02.15` |
| `PCLK` 报 period 超范围 | 超出该机型允许的 period 范围（例 PS800 2.5–31250 ns） | 查硬件规格；用 `VCLK?` 预判是否 auto-correct | `02.06.06.02.20`、`.35` |
| 周期被自动修正、不是输入值 | period 不是 period resolution 的整数倍；TS1 改周期会自动重算 resolution 并修正其他 timing set | `CLKR?` / `PCLK?` 的 `EXACT` query mode / `VCLK?` | `02.06.06.02.20`、`02.06.06.01.04.01.02.01` |
| `WSUS`/`TSUS` 报超范围 | waveform set > 16，或 timing set 超过 `DSCP` 允许值 | `WSUS?`、`TSUS?`、`DSCP?` | `02.06.06.02.46`、`.32` |
| 加载 timing 文件后数据丢失 | `DSCP` 每次调用清空 Sequencer Memory | 重新 load device setup | `02.06.06.02.10` |
| `SPRM` 报某个 set 不存在，但仍保存了值 | 文档说 `SPRM` 即使检测到值不指向已存在 set，也总是存储传入值 | `SPRM?` 回读；`TSUS?`/`SPCP?` 核对 | `02.06.06.02.28` |
| `SVLR` 报 spec 不存在或越界 | 变量名错、或改动导致 range/limit 违规 | `SVLR?` 查实际值/`MIN`/`MAX` | `02.06.06.02.31` |
| `WRST` 执行后 setup 全空 | 文档说它重置该 waveform set 的全部 timing/waveform；且“There are no error messages.” | 误用后重新下载 setup；把 `WRST` 当 destructive | `02.06.06.02.44` |
| `RSET TIM` 后只剩 TS1/waveform set 1 | 默认 timing 只激活 waveform set 1 的 timing set 1 | 重新 load 完整 timing；把 `RSET` 当 destructive | `02.06.06.02.23` |
| `SPST?` 显示检查被关掉 | status bit 置位表示跳过该检查 | 用 `SPST?` 逐 bit 读；重新下载含 `CHECK` 的 spec | `02.06.06.02.29` |

### setup / 文件级症状

| 症状 | 可能原因（文档） | 排查入口 | 出处 |
|---|---|---|---|
| 下载被拒绝，report window 报资源不足 | 输入 waveform 用掉超过可用的 edge/波形资源 | 看 `Timing edges` 资源清单；减少 edge 或复用 waveform/index | `02.08.04.34.06.06.06`、`.06.06.01` |
| Spec Tool 弹单位不一致警告 | EQNSET 与 SPECSET 的单位不同（常见于 STIL reader 2.1 及更早转换的 setup） | 按警告二选一：Spec Tool `Download` 后用 EQNSET 单位，或改 EQNSET 与 SPECSET 同单位 | `02.08.04.34.06.03` |
| multiport spec 少了某些 pin，report window 警告，甚至要 reset system | primary multiport timing spec 未覆盖当前 multi-port burst start label 里的全部 pin | 用 `SPCP?` 看 port 列表；补齐 spec；必要时换 device 重置 | `02.08.04.34.04.02.01`、`02.06.06.01.05.03` |
| 系统可能崩溃 | multiport timing specification 未覆盖全部已配置 pin | 同上；这是文档原句的强警告 | `02.06.06.01.05.03` |
| spec 指向的 wavetable 与 equation set 的 mode context 不同 | 不允许跨 context 组合 | `02.08.04.34.05`；检查 `MODECONTEXT` 与 Context 字段 | `02.08.04.34.05` |
| Smart Scale 上 spec 不能执行 | edge 间隔超过 10 个 user period，或 distance check 被关掉 | 看 `CHECK` 设置；`SPST?` | `02.06.06.01.05.01` |
| `CHECK NONE` 在 Pin Scale Digital Cards 上被拒 | 文档明说该卡不允许 `CHECK NONE` | 改用单项检查关闭 | `02.08.04.34.04.03.05.01` |
| 编辑完 wavetable/equation/spec 后文件没保留 | Wavetable Editor 里的是临时文件；必须保存 Timing Setup 或另存 | 回到 Test Program Explorer 保存 Timing Setup | `02.08.04.34.06.01`、`.06.02`、`.06.03` |
| `UPTD? TIM` 返回 0 | 文件与硬件不一致（改过未下载，或下载后未保存） | 重新下载或保存；再看状态指示 | `02.06.06.02.34` |
| CKST?/SPST? 报 level/timing 资源违规 | 方程求值超出资源范围；错误按 setup/min/max 的 spec 组合逐项报告 | 看错误消息里的 specset、resource、spec min/max | `02.08.04.34.04.03.06` |
| 改了 `SVLR` 又用 `TIMING_SPEC`，值互相覆盖/丢失 | 文档 CAUTION：两种方式不要混用；`TIMING_SPEC` 有 `.restore()` 缓存，firmware 层没有 | 二选一；调试时用 `SVLR`，测试方法里用 `TIMING_SPEC` | `02.06.06.02.31`、`02.07.04.01.249` |
| `FLUSH` 前又切了 primary spec，`change()` 被忽略 | 文档示例说明：未 `FLUSH` 就改 primary，先前 spec 改动会被丢弃 | 改 primary 前先 `FLUSH(TM::APRM)` | `02.07.04.01.249` |
| waveform set 与 vector 不再匹配 | 测试所需 vector 与 timing setup 必须匹配 | 用 `VWFS?` 比较 set；GUI 的 waveform set 兼容性检查 | `02.08.04.34.06.11.02`、`02.06.06.02.39` |
| 修改 timing 后发现 period 精度变差 | TS1 精度最高；其他 timing set 取 master clock 最近倍数，偏差可到 ±6 ns | 需要精确 period 时换 waveform set，而不是换 timing set | `02.08.04.34.03.02` |

**本页未逐一转录每条命令的 `Errors` 段**：上表只收录本次实际读到并核对过的错误条件；其余命令的错误面以各自文档的 `Errors` / `Warnings` 段为准。**文档事实**：`02.06.06` 子树的 102 篇里没有独立的错误汇总篇（与 pin 配置的 `02.06.03.01.11` 不同），所以不能给出按错误码组织的完整错误清单。

## 下一步

下一步是 [[pattern]]。

**文档事实**：`02.08.01.01.03` 的顺序是先 level、再 timing、最后 vectors（Pattern Tools）；`02.08.04.34.03.01` 说一次测试用一个 waveform set 和一个 timing set，pattern 通过 device cycle 名引用 wavetable 中的波形；`02.06.06.01.03` 说 vector 里存的是 waveform 的**索引**，shape 只在 physical waveform table 里存一次。因此 timing setup 必须先稳定，pattern 才能把 device cycle 名与波形索引写对。

之后再进 [[testmethod]] 与 [[testflow]]：`02.08.01.01.04` 说 test 阶段在 testsuite 里指定 primary sets 与 vector label；`02.06.06.02.28` 的 `SPRM` 与 `02.06.06.02.01` 的 `APRM` 就是那时被调用的。测试执行中可用 `CTIM` 切 timing set（`02.06.06.01.04`、`02.08.04.34.03.02`），这条运行期语义在 [[run]] 阶段使用。
