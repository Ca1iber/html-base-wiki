---
type: stage
title: Level / 电平配置（Level Setup）
tags: [level, dc, dps, termination, clamp, equation-based, fixed-level]
related:
  - "[[project]]"
  - "[[pin]]"
  - "[[timing]]"
  - "[[pattern]]"
  - "[[testmethod]]"
  - "[[testflow]]"
  - "[[run]]"
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.05.01_Concepts_of_level_setup.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.02_List_of_level_setup_commands.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05_Level_Setup_Commands.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.05.01_Create_a_fixed_level_set.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.05.01.01_Set_fixed_driver_levels.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.05.01.02_Set_fixed_receiver_levels.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.05.02_Delete_a_Fixed_Level_Set.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.05.03_Set_the_termination_mode_of_a_Fixed_Level_Set.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.05.04_Set_Fixed_Power_Supply_Levels.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.05.07_Example_of_a_Fixed_Level_Setup_File.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.08_EQFC__EQFC__-__EQualization_and_Filter_Configuration.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.05.05_Controlling_high-Z_behavior_of_digital_pins_while_the_sequencers_are_OFF.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.16_PSSR__PSSR__-_Power_Supply_Slew_Rate.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.04.02.06.01_Pin_exclusion.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.03_DFSP__DFSP__-__DeFine_Sampling_Profile.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.07_ENSP__ENSP__-__ENable_Sampling_Profile.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.04.02.07_IO_PINS_resources.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.05.06_Pull-down_function.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.03_Clamping.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.01_Basic_concepts_of_levels.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.01.01_Drive_Levels.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.01.02_Compare_Levels__Thresholds.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.01.02.01_Comparing_output_signals.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.01.03_Termination_types.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.01.03.01_Active_load_termination.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.01.03.02_Driver_termination.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.02_DPS__Device_Power_Supply__pins.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.05_Data_Organization_of_Fixed_Levels.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.05.01.03_Set_fixed_clamping_levels.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.04_Data_Organization_of_Equation_Based_Levels.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.04.01_Elements_of_Equation_Based_Level_Setup.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.04.02_Structure_of_an_equation_based_level_setup.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.04.02.01_Equation_set_number_and_description.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.04.02.02_Mode_context_in_level_setup.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.04.02.03_Specs_module.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.04.02.04_Equations_module.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.04.02.05_DPS_module.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.04.02.06_Level_sets.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.04.02.08_Supported_level_resources.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.04.02.06.02_Additional_pin_qualifier__diff.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.04.02.07.01_Implicit_setting_of_termination_mode_for_standard_single-ended.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.04.02.07.02_Explicit_setting_of_termination_mode_for_standard_single-ended.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.04.02.09_Spec_sets.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.04.03_Testing_with_equation_based_level_sets.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.04.03.01_Verifying_the_level_settings.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.04.04_Example_of_an_equation_based_level_setup.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.01_APRM_-__Activate_PRiMary_sets.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.02_CLMP__CLMP__-__CLaMP_level.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.04_DPRL__DPRL__-__Default_PRimary_Level_sets.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.05_DRLV__DRLV__-__DRive_LeVel.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.06_DSUS__DSUS__-__Dps_Sets_USed.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.09_EQFS_-__EQuation_FileS_command_transfer.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.10_EQSP__EQSP__-__EQuation_SPecification_transfer.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.11_FTCG__FTCG__-__Functional_Test_ConfiGure.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.12_LSUS__LSUS__-__Level_Sets_USed.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.13_LSUX__LSUX__-__Level_Sets_Used_eXtended.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.14_MERL__MERL__-__Message_ERror_Limits.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.15_PSLV__PSLV__-__Power_Supply_LeVel.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.17_RCLS__-__ReCeive_Level_Sensitivity.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.18_RCLV__RCLV__-__ReCeive_LeVel.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.19_RSET_-__ReSET.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.20_SDSC__-__Set_number_DeSCriptions.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.21_SLDO_-__Switch_Level_and_Dps_Order.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.22_SPRM__SPRM__-__Set_PRiMary_sets.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.23_SPST__-__SPecset_STatus.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.24_SVLR__SVLR__-__Spec_VaLues_at_Runtime.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.25_TERM__TERM__-__TERMination_mode.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.26_UPTD__UPTD__-__UP_To_Date.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.27_WAIT_-__WAIT.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.28_RST_-__ReSeT.htm
  - 02_System_reference/02.06_Command_Reference/02.06.04_Routing_Setup_Commands.htm
  - 02_System_reference/02.06_Command_Reference/02.06.04.01_Concepts_of_routing_setup.htm
  - 02_System_reference/02.06_Command_Reference/02.06.04.01.01_Introduction.htm
  - 02_System_reference/02.06_Command_Reference/02.06.04.01.02_Defining_Routing_Set.htm
  - 02_System_reference/02.06_Command_Reference/02.06.04.01.03_Setting_up_Routing.htm
  - 02_System_reference/02.06_Command_Reference/02.06.04.01.04_Defining_and_Activating_Primary_Set.htm
  - 02_System_reference/02.06_Command_Reference/02.06.04.02_List_of_routing_setup_commands.htm
  - 02_System_reference/02.06_Command_Reference/02.06.04.02.01_DSCP__DSCP__-__Define_System_Control_Parameter.htm
  - 02_System_reference/02.06_Command_Reference/02.06.04.02.02_SRPR__SRPR__-__Set_Routing_PRimary.htm
  - 02_System_reference/02.06_Command_Reference/02.06.04.02.03_UDRS_-__UnDefine_Routing_Set.htm
  - 02_System_reference/02.06_Command_Reference/02.06.01.04_System_preparation_by_firmware_commands.htm
  - 01_Getting_started/01.07_Testing_a_Basic_Digital_Device/01.07.01_Testing_a_basic_digital_device.htm
  - 01_Getting_started/01.07_Testing_a_Basic_Digital_Device/01.07.01.01.01_Device_directory_structure.htm
  - 01_Getting_started/01.07_Testing_a_Basic_Digital_Device/01.07.01.03_Setting_up_your_levels.htm
  - 01_Getting_started/01.07_Testing_a_Basic_Digital_Device/01.07.01.03.01_Specifying_the_context_for_levels.htm
  - 01_Getting_started/01.07_Testing_a_Basic_Digital_Device/01.07.01.03.02_How_to_create_an_equation_set_using_the_Equation_editor.htm
  - 01_Getting_started/01.07_Testing_a_Basic_Digital_Device/01.07.01.03.03_Creating_new_specification_sets.htm
  - 01_Getting_started/01.07_Testing_a_Basic_Digital_Device/01.07.01.03.04_Verifying_the_level_settings.htm
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02.04.04_Creating_a_level_master_file.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14_Level_setup_tool.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.01_Basic_concepts_of_levels.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.02.01_The_advantage_of_using_level_setup_file_to_store_all_the_level_sets.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.02.03.07.01_DPSPINS_resources.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.02.03.08.02_Termination_Mode.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.02.03.10_Error_Reporting.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.02.05_Level_setup_master_file.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.02.05.01_Master_file_format_for_level_setup.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.02.05.02_Editing_the_level_and_timing_subfiles.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.03_Elements_of_the_Level_Setup_window.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.03.01_How_to_read_the_IO_Level_Setup_window.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.03.02_How_to_read_the_DPS_Setup_window.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.04_Opening_and_using_the_Level_Setup_Tool.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.04.01_Setting_up_your_levels.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.04.02_Specifying_the_context_for_levels.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.04.03_How_to_create_an_equation_set_using_the_Equation_editor.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.04.04_Creating_new_specification_sets.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.04.05_How_to_set_the_driver_levels_for_differential_pins.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.04.06_How_to_set_the_driver_levels_for_single_ended_pins.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.04.07_How_to_set_the_driver_levels_for_DUT_inputs.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.04.08_How_to_set_the_termination_for_DUT_outputs.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.04.08.01_Using_the_clamp_for_termination.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.04.08.02_Using_the_active_load_for_termination.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.04.08.03_Using_the_cross_termination.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.04.08.04_Using_the_bidir_receiver_termination_for_full_swing_in_fast_mode.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.04.09_How_to_set_the_comparator_thresholds_for_single-ended_pins.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.04.10_How_to_use_the_Dynamic_Driver_High_Level_Shift__v3h__feature_for_fast_mo.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.04.11_Working_with_level_sets_and_DPS_sets.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.04.11.01_Setting_switching_order_modes_of_level_sets_and_DPS_sets.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.05.01_Termination_mode.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.05.02_Setting_up_the_levels_for_the_Pin_Scale_1600_card.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.01.06_Automatic_level_adjustment_for_series_resistance.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.06.01.01_To_set_the_power_supply_voltage_levels.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.06.02.06_Related_Firmware_Commands.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.30_Spec_Tool.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.30.02_General_Editing_Features_of_the_Spec_Tool.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.30.02.18_How_to_restore_the_equation_settings_after_you_change_them_in_the_Timing.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.124_LEVEL_SPEC.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.167_PRIMARY_STATUS_-__Primary.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.123_LevelSetSelector.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.05.04.06_SetupLevelSet0.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.14.02_CCTchangeLevelSpec.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.03.02.02_Changing_spec_value_in_primary_level_spec_set.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.11.01.05.01_Level_equation_file.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14_Test_Suite_Control_API.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01_TestsuiteProxy.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.05_TestsuiteProxy.getLevelEquation.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.06_TestsuiteProxy.getLevelSet.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.07_TestsuiteProxy.getLevelSpec.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.25_TestsuiteProxy.setEquationBasedLevel.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.09_TPI_Program_Routines.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.09.02_DataManager.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.09.10_GetEQVariableValue.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.09.22_InsertEQVariableInCache.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.11.03.02_Level_control_API.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.11.03.02.01_StartLevel.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.10.03.02.02.26_GetLevelProfile.htm
  - 02_System_reference/02.15_SmartShell/02.15_SmartShell.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.08.03.02_Changing_the_level_set__CLEV.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.02.04.18_new_level_resource.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.02.04.19_overwrite_level_resource.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.02.04.20_new_level_equation_set.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.02.04.21_new_level_set.htm
created: 2026-11-12
updated: 2026-11-12
verified: doc-only
---

# Level / 电平配置（Level Setup）

> 给每个 DUT 引脚赋予驱动电平、比较阈值、端接/负载、clamp 和 DPS 电压，并把这些值组织成可在测试中整体切换的 level set / DPS set。

## 目的

**文档事实。** 通道卡的每个通道包含 driver、双电平 comparator、active load 和 clamp；level setup 就是给这些资源赋值，涉及六类量：drive levels、compare levels、termination modes、load currents、clamp levels、power supply voltage（`02.06.05`）。文档给出两种做法：

- **fixed level setup**：用固件命令把值写成常量，存进每一个 level set；可对单个引脚或 `DFGP` 定义的 pin group 设置（`02.06.05.01.05`）。
- **equation-based level setup**：用表达式、equation variable、spec variable 计算电平值，整套数据作为一个数据块下载（`02.06.05.01.04`、`02.06.05.01.04.01`）。

两种方式**不互斥**，可以写在同一个 level 文件里；level 文件位于 device directory 的 `levels` 子目录（`02.06.05`、`01.07.01.01.01`）。

**文档事实（版本）。** fixed level setup 在 SmarTest 7.4.1T 起停止支持，文档建议 7.2 及以上版本一律使用 equation-based level setup（`02.06.05.01.05.01`、`02.06.05.01.05.02`、`02.06.05.01.05.04`、`02.06.05.01.05.07` 均有同一 Note）。本 wiki 面向 7.10.3，因此新建设置应以 equation-based 为主。

**文档事实（为什么值得拆多个 set）。** 每个 level set 都是“当前器件所有逻辑引脚”的完整、自包含定义，每个 DPS set 覆盖所有 DPS 引脚；一个文件里的多个 set 在 load 时一起进硬件，运行时只需切换 set，不需要重新下载，因此可提升吞吐（`02.08.04.14.02.01`）。DPS 侧：DUT 进入 connect 后 DPS 被编程到 `vout`，经过内部稳定时间和 setup time `t_ms`，sequencer 才启动（`02.06.05.01.02`）。

**推断：** 在 `project → pin → level → timing → pattern` 这条链上，level 是 pin 的电气条件与后续时序/向量之间的中间层：它依赖 pin 配置给出的 pin 类型与 mode context，又为 pattern 执行和测试套件的 primary set 提供电压条件。文档没有把它写成 stage 链；`01.07.01` 的章节顺序（Defining the pins → Setting up your levels → Waveform and timing sets）支持这一读法，但这条链是本次归纳。

**建议：** 新建 7.10.3 工程直接用 equation-based level setup；只有维护旧环境，或需要使用文档明确排除 equation-based 的 level set 0 高阻行为时，才回退到 fixed 命令（level set 0 的限制见下文 L1）。这是建议，不是文档要求。

## 前置条件

1. **Device directory 已建立**，且其中存在 `levels` 子目录（`01.07.01.01.01`）。见 [[project]]。
2. **Pin configuration 已完成。** 文档在“用 Equation editor 建 equation set”的 `Before you begin` 中写 `You have set up your pin configuration.`（`01.07.01.03.02`、`02.08.04.14.04.03`）。Level Setup 窗口的 `pin/group name`、`pin type` 两列来自 Pin Configuration，在 Level Setup 中不可编辑（`02.08.04.14.03.01`）。见 [[pin]]。
3. **每个 level set 必须覆盖 pin configuration 中定义的全部引脚。** 文档示例明确写 `every level set must contain information for all pins defined in your pin configuration`（`01.07.01.03.02`）。在 equation-based 中，未列出的 I/O 引脚会产生 warning 并使用默认设置（`02.06.05.01.04.02.07`）。
4. **Mode context 对齐。** 若 pin configuration 用了用户自定义 mode context，level setup 必须把设置分配到这些 context，且 timing 也要为这些 context 定义；不写时自动使用 `DEFAULT`（`02.06.05.01.04.02.02`、`01.07.01.03.01`、`02.08.04.14.04.02`）。
5. **集合容量已由 `DSCP` 定义。** `level_set` 默认 32、最大 256；`dps_set` 默认 32、最大 256（`02.06.04.02.01`、`02.06.01.04`）。**`DSCP` 每次执行都会清掉 Sequencer Memory 中已有数据并复位所有 set**，改完必须重新装载 device setup（`02.06.04.02.01`、`02.06.01.04`）。
6. **DPS 引脚已由 `DFPS` 定义。** `PSLV`/`PSSR`/`DFSP`/`ENSP` 都要求引脚“previously configured with the DFPS command”（`02.06.05.02.15`、`02.06.05.02.16`、`02.06.05.02.03`、`02.06.05.02.07`）。`DFPS` 属 pin 命令子树（见 [[pin]]），不是本阶段 L1。
7. **要用的 pin group 已由 `DFGP` 定义。** `DRLV`/`RCLV`/`CLMP` 的 pinlist 可直接引用 `DFGP` 组（`02.06.05.02.05`、`02.06.05.02.18`、`02.06.05.02.02`）。
8. **equation-based 的 spec 值已在 Spec Tool 中赋值。** `SPECS` 模块只声明变量和单位，不给值；值由 `SPECSET`/Spec Tool 提供（`02.06.05.01.04.02.03`、`02.06.05.01.04.02.09`）。创建 spec set 前至少需要一个 equation set（`01.07.01.03.03`、`02.08.04.14.04.04`）。
9. **level set 0（高阻行为）有额外顺序。** 先 load level setup 文件，再用 `TERM`/`CLMP` 编程 level set 0，然后把 sequencer 置 `BRK` 使命令生效；顺序不能反，因为 load 会重置 level set 0（`02.06.05.01.05.05`）。
10. **fixed 方式先查 `LSUS?`。** 创建新 set 前用 `LSUS?` 查当前 set 数，再用下一个可用编号（`02.06.05.01.05.01`、`02.06.05.01.05.04`）。
11. **手改 master file 的子文件时注意字节数。** equation 数据在 setup 文件中是 `EQSP` 的字符串参数，带字节长度；用 Setup Management Tool 拆出的子文件可随意编辑，但单独 load 一个手改过的子文件时必须手工改字节数（`02.08.04.14.02.05.02`）。

## 涉及对象

| 对象 | 层级 | 在本阶段做什么 |
|---|---|---|
| Level Setup Tool | gui | 打开 level 窗口、编辑 equation/spec、下载到硬件、查看 I/O 与 DPS 视图（`02.08.04.14.04`） |
| Level Equation Editor（NEdit） | gui | 编辑 `EQNSET`/`SPECS`/`EQUATIONS`/`DPSPINS`/`LEVELSET`；`Shell > Download` 或 F8 下载（`02.08.04.14.04.01`、`01.07.01.03.02`） |
| Spec Tool | gui | 创建/复制/删除 spec set，给 spec 变量赋值并下载（`02.08.04.30`、`02.08.04.30.02`） |
| Test Program Explorer | gui | 装载/保存 level setup 与 level master file；`Levels` 图标入口（`02.08.04.14.04`、`01.01.07.02.02.04.04`） |
| Report window | gui | 显示下载、检查与违反项错误（`02.08.04.14.02.03.10`） |
| `DSCP` | L1 | 定义 level set / DPS set 的最大数量并为它们预留 Sequencer Memory（`02.06.04.02.01`） |
| `DRLV` / `RCLV` | L1 | 设置 driver 电平 / comparator 阈值（`02.06.05.02.05`、`02.06.05.02.18`） |
| `TERM` / `CLMP` | L1 | 端接模式与 clamp 电平（`02.06.05.02.25`、`02.06.05.02.02`） |
| `PSLV` / `PSSR` | L1 | DPS 输出电压/电流/阻抗/setup time 与电压斜率（`02.06.05.02.15`、`02.06.05.02.16`） |
| `SPRM` / `APRM` | L1 | 定义 / 激活 primary sets（`02.06.05.02.22`、`02.06.05.02.01`） |
| `EQFS` / `EQSP` | L1 | 方程文件的 load/save 与二进制下载/回读（`02.06.05.02.09`、`02.06.05.02.10`） |
| `SVLR` | L1 | 运行时改 spec 值并重算电平/时序（`02.06.05.02.24`） |
| `SPST?` | L1 | 查询 status bits，判断 setup 是否被 `DRLV`/`RCLV`/`TERM`/`PSLV`/`SVLR` 改过（`02.06.05.02.23`） |
| `UPTD` | L1 | 查询/声明 setup 与硬件是否一致（`LEV`/`DPS` flag）（`02.06.05.02.26`） |
| level 文件 | file | `levels` 目录下，首行形如 `hp93000,level,0.1`；保存全部 level set（`02.07.11.01.05.01`、`02.06.05`） |
| level master file | file | `levels.mfh`，用 `EQNSET n: file` 等条目把子文件组装成完整 level setup（`02.08.04.14.02.05.01`） |
| `eqnset_<n>.lev` / `GENERAL.lev` | file | Setup Management Tool 拆出的子文件；切换顺序保存在 `GENERAL.lev`（`01.01.07.02.02.04.04`、`02.08.04.14.02.05.01`） |
| `.prot_lev` | file | `USE_PROTOCOL` 引用的协议 level segment，XML，存放在器件 protocol 目录（`02.07.11.01.05.01`） |
| `LEVEL_SPEC` | L2 | 读取/修改 equation set + spec set 中的 spec 值（`02.07.04.01.124`） |
| `PRIMARY_STATUS`（`Primary`） | L2 | 访问 level-related primaries，取 `getLevelSpec()`（`02.07.04.01.167`） |
| `SetupLevelSet0` | L2 | 改 level set 0 的 clamp 与 active load（`02.07.05.04.06`） |
| `TestsuiteProxy` | L3 | 读写测试套件的 level equation/spec/set（`02.09.01.14.02.01`） |
| `DataManager`（TPI） | L3 | 以 `dm_level` 文件 ID 访问 level setup 文件（`02.09.01.09.02`） |
| `CLEV` | sequencer | 在向量执行中切换到另一个 level set（`02.06.07.01.08.03.02`） |

### 概念页对照（`02.06.05.01.*`）

| 概念页 | 一句话 | 出处 |
|---|---|---|
| Basic concepts of levels | level setup 给 drive levels、compare levels、load currents、power supply voltage 等资源赋值 | `02.06.05.01.01` |
| Drive Levels | 对 i / io 引脚定义输入信号的高 `vih`、低 `vil` 驱动电平 | `02.06.05.01.01.01` |
| Compare Levels (Thresholds) | 对 o / io 引脚定义输出比较阈值 `voh`/`vol` | `02.06.05.01.01.02` |
| Comparing output signals | comparator 输出高/低比较结果；compare 阈值可用 PS1600/PS5000 的 `vol`/`voh` 与 PS5000 的 `vth` 编程；Smart Scale 可设差分阈值，Pin Scale 差分阈值固定 0 V | `02.06.05.01.01.02.01` |
| Termination types | 传输线必须端接以避免反射；可选 driver、clamp、active load、differential termination，具体取决于通道卡 | `02.06.05.01.01.03` |
| Active load termination | 端接由 `iol`/`ioh` 负载电流与换向电压 `vt` 描述：输出电压高于 `vt` 时取 `ioh`，低于时取 `iol` | `02.06.05.01.01.03.01` |
| Driver termination | 用 driver 内部 50 Ω 端接传输线；o 引脚端接到任意电压，io 引脚端接到 drive high/low | `02.06.05.01.01.03.02` |
| DPS (Device Power Supply) pins | DUT 电源引脚由 DPS 提供 `vout`；connect 后经稳定时间与 `t_ms`，sequencer 启动 | `02.06.05.01.02` |
| Clamping | clamp 用 `vcl`/`vch` 限制反射峰值；PS1600 的 clamp 集成在 driver 中，clamp mode 分 `auto`/`on` | `02.06.05.01.03` |
| Data Organization of Equation Based Levels | 用变量与运算符构造表达式来确定电平，比 fixed 更灵活，整套数据作为数据块下载 | `02.06.05.01.04` |
| Elements of Equation Based Level Setup | 三要素：表达式、equation variables、spec variables | `02.06.05.01.04.01` |
| Structure of an equation based level setup | 必需模块：equation set number、Specs、Equations、DPS、Level sets，外加 Spec Sets | `02.06.05.01.04.02` |
| Equation set number and description | `EQNSET` 编号 1–256 且唯一，描述可选、最多 60 字符 | `02.06.05.01.04.02.01` |
| Mode context in level setup | mode context 定义每个引脚的类型与工作模式；`MODECONTEXT` 行紧跟 `EQNSET`；用户自定义 context 还需在 timing 中定义；带 fast differential 引脚的 level setup 必须是 equation-based，且比较/驱动电平的设置方式与标准引脚不同 | `02.06.05.01.04.02.02` |
| Specs module | `SPECS` 声明 spec 变量与单位，不给值；单位只能在此定义 | `02.06.05.01.04.02.03` |
| Equations module | `EQUATIONS` 定义 equation system；方程数必须等于变量数 | `02.06.05.01.04.02.04` |
| DPS module | `DPSPINS <pin>` 后用表达式给 DPS 电平（如 `vout`） | `02.06.05.01.04.02.05` |
| Level sets | `LEVELSET` 编号 1–99，`PINS` 赋值；所有 equation set 合计最多 256 个 level set | `02.06.05.01.04.02.06` |
| Pin exclusion | `PINS <pin list> -( <exclude list> )` 从前一个 pin list 中排除引脚（也适用于 DPS 引脚） | `02.06.05.01.04.02.06.01` |
| Additional pin qualifier @diff | `@diff` 让差分对只写一个连接即可完整定义；仅 equation editor 可用 | `02.06.05.01.04.02.06.02` |
| IO PINS resources | I/O 引脚资源全表（`vil`/`vih`/`v3h`/`vihh`/`vol`/`voh`/`vth`/`iol`/`ioh`/`vt`/`hyst`/`irng`/`orng`/`rec_offset`/`rec_swing`/`term`/`vcl`/`vch`）；`term` 必须是第一个值 | `02.06.05.01.04.02.07` |
| Implicit setting of termination mode | 标准/单端端接模式由 `ioh`/`iol`/`vt` 的有无推出：都无 = off，仅 `vt` = t，`vt=vih` = h，`vt=vil` = l，三者都有 = a | `02.06.05.01.04.02.07.01` |
| Explicit setting of termination mode | 差分端接必须用 `term` 显式设置；单端也可显式；`term` 行必须紧跟 `PINS` 行，取值如 `off`/`on`/`center_tap`/`single_ended_cross` | `02.06.05.01.04.02.07.02` |
| Supported level resources | 按卡、端接模式、pin type 列出可用资源（PS1600/PS5000 的单端、差分、clamp 三张表） | `02.06.05.01.04.02.08` |
| Spec sets | `SPECSET` 编号 1–99，给 `SPECS` 声明的变量赋值；不同 spec set 可用于不同测试 | `02.06.05.01.04.02.09` |
| Testing with equation based level sets | 跑测试时可选用 level GUI 或 `EQFS`/`EQSP`/`EQFC`；必须选一个 equation set、该 set 下的一个 level set、一个 spec set | `02.06.05.01.04.03` |
| Verifying the level settings | 用 `Show I/O Eqn & Specs Results` / `Show DPS Eqn & Specs Results` 改 `Eqn#`/`Sps#`/`Lset#` 核对 | `02.06.05.01.04.03.01` |
| Example of an equation based level setup | 完整示例：`SPECS` + `EQUATIONS` + `DPSPINS` + `LEVELSET`/`PINS` | `02.06.05.01.04.04` |
| Data Organization of Fixed Levels | fixed 方式用固件命令把电平写成每个 level set 内的常量，可对单引脚或 `DFGP` 组 | `02.06.05.01.05` |
| Create a fixed level set | 用 `LSUS` 定数量、`DRLV`/`RCLV`/`TERM`/`CLMP`/`EQFC` 写值；上电时只有 level set 1 | `02.06.05.01.05.01` |
| Set fixed driver levels | `DRLV` 设 driver 的逻辑 0/1 电压；省略参数时固件插入适当值 | `02.06.05.01.05.01.01` |
| Set fixed receiver levels | `RCLV` 设 comparator 的逻辑 0/1 阈值；串联电阻造成的压降自动补偿 | `02.06.05.01.05.01.02` |
| Set fixed clamping levels | 可用 `CLMP` 或 `TERM` 设 clamp；要独立于端接模式设置时用 `CLMP` | `02.06.05.01.05.01.03` |
| Delete a Fixed Level Set | 用 `LSUS` 删除单个/多个 set，level set 1 不能删 | `02.06.05.01.05.02` |
| Set the termination mode of a Fixed Level Set | `TERM` 设输出引脚端接电压、io 引脚端接高/低 driver 电平、clamp 电压 | `02.06.05.01.05.03` |
| Set Fixed Power Supply Levels | `DSUS` 定 DPS set 数量、`PSLV` 设电压/限流/断开阻抗/setup time；上电时只有 DPS set 1 | `02.06.05.01.05.04` |
| Controlling high-Z behavior ... sequencers OFF | sequencer OFF 时 level set 0 生效；set 0 只能用 fixed 编程、不能作 primary、不在 `ALL` 中 | `02.06.05.01.05.05` |
| Pull-down function | PS1600 的 14.3 kΩ pulldown / PS5000 的 active load discharge；可由 level set 0 全局默认或显式 `term off pulldown` 控制 | `02.06.05.01.05.06` |
| Example of a Fixed Level Setup File | 给出 `hp93330,level,0.1` + `PSLV`/`DRLV`/`RCLV`/`TERM` 的完整 fixed 文件示例 | `02.06.05.01.05.07` |

### 归属判定

> 以下是判断，不是文档事实，供维护者复核。

- **`02.06.05.02` 的 28 条命令全部判给本页**，即使其中部分命令只在 fixed 流程里有意义。页面对每条都给出名字、一句作用和出处，满足“子树不漏项”。
- **`DSCP` 判给本页 L1，尽管它在 `02.06.04`（Routing Setup Commands）子树。** 理由：`LSUS`/`DSUS`/`CLMP`/`DRLV`/`RCLV`/`TERM`/`PSLV` 的上限与 set 编号都以 `DSCP` 定义为准（各命令参数表），且 `DSCP` 直接决定 level set 与 DPS set 容量。Routing 的另外两条命令 `SRPR`/`UDRS` **不判给本页**：它们操作的是 analog routing set，不写任何电平值（`02.06.04.02.02`、`02.06.04.02.03`）。`02.06.04.01.02`–`.01.04` 提到的 `DFRS`/`DFRT`/`ACRS` 属模拟 routing，也不在本页 L1。
- **`DFPS`、`DFGP`、`DFAN` 等判给 [[pin]]。** 本页只把它们写成前置条件；`PSLV` 等命令的 “previously defined by DFPS” 是使用前提，不是本页要教的配置动作。
- **`CLEV`/`CTIM` 判给 [[pattern]] / sequencer 层。** `CLEV` 只在向量表里切 level set，属于运行时切换；`PRIMARY_STATUS` 文档还特别说明 `CLEV` 不改变 primary level set 的定义（`02.07.04.01.167`）。
- **`SWNG`/`ASWE`/`ASWM` 不判给本页 L1。** 它们只出现在 Mixed Level Devices 用例的 “Related Firmware Commands” 中（`02.08.04.14.06.02.06`），本页不复制其语义。
- **HVM `GetLevelProfile`、BLC `StartLevel()` 是同形陷阱，不判给本页。** 二者操作的是 application model 的 level 结构（`WAFER_LEVEL`/`DEVICE_LEVEL`/`CUSTOM_LEVEL`），返回/维护的是变量表，不是电压 level（`02.09.01.10.03.02.02.26`、`02.09.01.11.03.02.01`）。
- **`DIGITAL_WAVEFORM.levelStart` / `levelStop` / `levelResolution` 不判给本页。** 它们是 offset search 的搜索范围/分辨率，不是 level setup（`02.07_Test_Method_Reference` 的 `DIGITAL_WAVEFORM` 成员）。
- **`UPTD` 判给本页但用途是跨阶段状态查询。** 它既覆盖 `LEV` 也覆盖 `DPS`、`TIM`、`VEC` 等，这里只写与 level 有关的部分，不把它写成 level 专属命令。

### GUI / 工具章节

**Level Setup Tool（`02.08.04.14`，共 88 篇）。** 章节结构如下；括号内是分类号，叶子页按原文篇名列出。

- `02.08.04.14.01` Basic concepts of levels：与 `02.06.05.01.01`–`.03` 重复的概念页——`.01.01` Drive Levels、`.01.02` Compare Levels (Thresholds)、`.01.02.01` Comparing output signals、`.01.03` Termination types、`.01.03.01` Active load termination、`.01.03.02` Driver termination、`.01.04` Clamping、`.01.05` DPS (Device Power Supply) pins、`.01.06` Automatic level adjustment for series resistance（串联电阻自动补偿，`02.08.04.14.01.06`）。
- `02.08.04.14.02` Equation based level setup：`.02.01` 把全部 level set 存进一个文件的好处；`.02.02` Elements of Equation Based Level Setup / `.02.02.01` Syntax of expression / `.02.02.02` Common Syntax Elements；`.02.03` Structure（`.02.03.01` EQNSET、`.02.03.02` SPECS、`.02.03.02.01` SPECS header、`.02.03.03` Level spec set、`.02.03.04` EQUATIONS、`.02.03.04.01` EQUATIONS header、`.02.03.05` Pin alias set、`.02.03.06` derived_spec、`.02.03.07` DPSPINS、`.02.03.07.01` DPSPINS resources、`.02.03.08` LEVELSET、`.02.03.08.01` IO PINS resources、`.02.03.08.02` Termination Mode、`.02.03.09` Level specifications、`.02.03.09.01` SPECSET、`.02.03.09.02` spec、`.02.03.10` Error Reporting、`.02.03.11` Glossary of terms）；`.02.04` 示例（`.02.04.01` Equation based level setup file example、`.02.04.02` Level specification: setup example）；`.02.05` Level setup master file（`.02.05.01` Master file format、`.02.05.02` Editing the level and timing subfiles）。
- `02.08.04.14.03` Elements of the Level Setup window：`.03.01` IO Level Setup 窗口读数、`.03.02` DPS Setup 窗口读数（DPS 参数表）。
- `02.08.04.14.04` Opening and using：`.04.01` Setting up your levels、`.04.02` Specifying the context for levels、`.04.03` How to create an equation set using the Equation editor、`.04.04` Creating new specification sets、`.04.05` driver levels for differential pins、`.04.06` driver levels for single ended pins、`.04.07` driver levels for DUT inputs、`.04.08` termination for DUT outputs（`.04.08.01` clamp、`.04.08.02` active load、`.04.08.03` cross termination、`.04.08.04` bidir_receiver for full swing in fast mode）、`.04.09` comparator thresholds for single-ended pins、`.04.10` Dynamic Driver High Level Shift (v3h)、`.04.11` Working with level sets and DPS sets（`.04.11.01` switching order modes）。
- `02.08.04.14.05` Level setup related card specifications：`.05.01` Termination mode（按卡列出可用模式与参数）、`.05.02` Setting up the levels for the Pin Scale 1600 card（三电平 driver、pulldown、差分阈值）。
- `02.08.04.14.06` Level setup related use cases：`.06.01` Setting up the Device Power Supply（`.06.01.01` 设置电源电压、`.06.01.02` DPS connect setup time and voltage ramps、`.06.01.02.01` DPS pins with connect setup time、`.06.01.02.02` DPS pins with voltage ramps、`.06.01.02.02.01` Voltage ramps、`.06.01.02.02.01.01` Current clamp handling、`.06.01.02.02.02` Voltage ramp example、`.06.01.03` UNGANG connect state）；`.06.02` Mixed Level Devices（`.06.02.01` Introduction、`.06.02.02` Different Swings、`.06.02.02.01` Estimate the time shift、`.06.02.02.02` Compensation of Different Swings、`.06.02.03` Considerations（`.06.02.03.01` Need for Swing Adjustment、`.06.02.03.02` Throughput and Test System Resources、`.06.02.03.03` Swing Adjustment Strategy）、`.06.02.04` Concept、`.06.02.05` Using Automatic Swing Adjustment、`.06.02.06` Related Firmware Commands）。

**Spec Tool（`02.08.04.30`，共 26 篇）。** `.01` The Spec Tool window；`.02` General Editing Features，含 `.02.01` Creating new specification sets、`.02.02` Copying、`.02.03` Deleting、`.02.04` Changing the Description、`.02.05` Assigning to Another Equation Set、`.02.06` Changing the Specification Set Number、`.02.07` Changing Compatibility Options、`.02.08` Assigning to Another Wavetable、`.02.09` Changing the Version Header、`.02.10` Changing the Check Options、`.02.11` Changing the Header、`.02.12` Adding a New Spec/Variable、`.02.13` Deleting a Spec/Variable、`.02.14` Changing Spec Values、`.02.15` Copying Spec Values、`.02.16` multiport timing specification（`.02.16.01`–`.02.16.04`）、`.02.17` How to perform a measurement、`.02.18` How to restore the equation settings、`.02.19` Error Checking Facilities。Spec Tool 与 level 相关的三件事：单位只能在 EQNSET 定义、不能在 Spec Tool 定义；Spec Tool 的 download 只改后端硬件，前端要再 `APRM` 或 disconnect/connect；EQNSET 与 SPECSET 单位冲突会弹 warning（`02.08.04.30.02`）。

## L1 — Firmware / Setup Command

**覆盖说明。** `python show.py --list 02.06.05` 共 70 篇，其中命令页 28 条（`02.06.05.02.01`–`.28`）。下面**逐条**给出命令名、一句作用、出处；重要命令另给文档中的最小示例。另有 `DSCP`（`02.06.04.02.01`）因定义 level/DPS 容量而纳入本节。

**equation-based 的 set 标识（文档事实）。** 多个命令在 equation-based setup 中要求 `level_set_id` 而不是 level set 编号，公式统一为：

```
level_set_id = 100000 * equation_set_no + 1000 * specset_no + level_set_no
```

`DPS set ID` 则为 `100000*equation_set_no + 1000*specset_no + 1`；`SPRM` 的 timing spec set ID 为 `100*equation_set_no + specset_no`（`02.06.05.02.02`、`02.06.05.02.05`、`02.06.05.02.18`、`02.06.05.02.25`、`02.06.05.02.15`、`02.06.05.02.22`）。

| # | 命令 | 一句作用 | 出处 |
|---|---|---|---|
| 1 | `APRM` | 激活由 `SPRM` 告知固件的 primary sets；`FRC` 强制、`CNL` 条件激活；`FTST?`/`RCLS?`/`SQST RUN`/`PSST` 会自行激活，无需先执行 `APRM` | `02.06.05.02.01` |
| 2 | `CLMP` | 定义指定引脚/组的 clamp 低、高电压并开关 clamp，写入指定 level set；`CLMP?` 返回实际 clamp 电平与 on/off；`ALL`/`PRM` 可用 | `02.06.05.02.02` |
| 3 | `DFSP` | 定义 functional test 期间的电压/电流 sampling profile（仅 DC Scale 卡）；参数为 measure type、range、sampling rate、average factor、keep_range | `02.06.05.02.03` |
| 4 | `DPRL` | 把 Level Setup 工具定位到指定 level set / DPS set；`DPRL?` 返回；用于 Test Flow Editor 与 level setup 的内部通信 | `02.06.05.02.04` |
| 5 | `DRLV` | 设置 driver 的逻辑 0/1 电平（mV），可对 `DFGP` 组；`DRLV?` 查询；equation-based 时只改 runtime 值，不改 setup 值 | `02.06.05.02.05` |
| 6 | `DSUS` | 设定已定义 DPS set 的数量（1 到 `DSCP` 上限），可借此删除高位 set；`DSUS?` 查询当前数量 | `02.06.05.02.06` |
| 7 | `ENSP` | 使能/禁用指定引脚参与 `DFSP` 的电压/电流采样（`ON`/`OFF`） | `02.06.05.02.07` |
| 8 | `EQFC` | 配置 PS1600/PS5000 的 equalization 与 low-pass filter 参数（`EQI1`–`EQI3`、`EQO1`–`EQO3`、`LPFI`/`LPFO`），按引脚设置 | `02.06.05.02.08` |
| 9 | `EQFS` | 编辑器工具用的方程文件 load/save（`LEV`/`TIM`、`EQN`/`SPS`/`WVT`、`LOAD`/`SAVE`、临时文件，可选错误文件） | `02.06.05.02.09` |
| 10 | `EQSP` | 以二进制格式下载/回读 equation-based setup 数据（level/timing 的 equations、specs、wavetable）；`EQSP?` 回读 | `02.06.05.02.10` |
| 11 | `FTCG` | 改变 functional test 开始时 primary sets 的激活行为（`SKPR`，`ON`/`OFF`/`NEVER`，按 port/sequencing group） | `02.06.05.02.11` |
| 12 | `LSUS` | 设定已定义 level set 的数量（1 到 `DSCP` 上限），可删除高位 set；`LSUS?` 查询；equation-based 时按 equation set 查 | `02.06.05.02.12` |
| 13 | `LSUX` | 系统内部（Test Flow Optimizer）使用，返回优化前的 level set 数；`SWAP`/`NONE`；文档明确“不要从 hpt 执行”，但可查询 | `02.06.05.02.13` |
| 14 | `MERL` | 设置 `CKST` 与 `EQFS` 的详细消息/错误消息上限（默认 10 / 40，范围 1–30000） | `02.06.05.02.14` |
| 15 | `PSLV` | 对 `DFPS` 定义过的 DPS 通道设置输出电压、源/灌电流限制、断开阻抗、setup time；作用于 primary DPS set 时立即生效 | `02.06.05.02.15` |
| 16 | `PSSR` | 为 DPS-slot DPS 与 DC Scale 通道定义电压上升/下降斜率与稳定时间；与 `PSLV` 的 `setup_time`、equation 的 `t_ms` 互斥 | `02.06.05.02.16` |
| 17 | `RCLS?` | 测量指定输出引脚接收端的阈值电平；可做 pass/fail 或带 limit 的值搜索，返回 `LT`/`LE`/`EQ`/`GE`/`GT`/`P`/`F` 与结果值 | `02.06.05.02.17` |
| 18 | `RCLV` | 设置 comparator 的逻辑 1/0 阈值（mV），可对 `DFGP` 组；`RCLV?` 查询；DUT 板串联电阻造成的压降会自动补偿 | `02.06.05.02.18` |
| 19 | `RSET` | 用指定类型文件（`DPS`/`FCR`/`LEV`/`TIM`/`VEC`/`ATR`/`PDL`/`CAL`/`MTPP`）的 power-on 默认值装载硬件 | `02.06.05.02.19` |
| 20 | `SDSC?` | 由描述查 setup 组件编号，或由编号查描述；覆盖 `LEV`/`TIM`/`ANA` 与 `EQN`/`SPS`/`L`/`LSET`/`TSET`/`WSET`/`ASET`/`RSET` 等类型 | `02.06.05.02.20` |
| 21 | `SLDO` | 在两个 test suite 之间切换 level set / DPS set 时选择电压切换顺序（`FDSL` 先 DPS、`CVDL` 依电压方向）与报告模式 | `02.06.05.02.21` |
| 22 | `SPRM` | 定义/修改 test suite 或用户过程内 test 的 primary sets（waveform/timing/level/DPS）；equation-based 用 `specset_id`/`level_set_id`/`dps_set_id`；multiport 可传 multi-port specification 与 timing set list；不激活硬件 | `02.06.05.02.22` |
| 23 | `SPST?` | 查询 spec set 的 status bits（周期/边沿检查是否被抑制、setup 是否被 `ETIM`/`PCLK`/`DRLV`/`RCLV`/`TERM`/`PSLV`/`SVLR`/`SHVL` 改过） | `02.06.05.02.23` |
| 24 | `SVLR` | 运行时把 spec 变量设为新值并重算 timing/levels；不改 setup 值；可只改单个引脚；新值在下一个 functional test 开始时生效 | `02.06.05.02.24` |
| 25 | `TERM` | 设置 output/IO 引脚的 termination mode 及其参数（端接电压、active load 电流、clamp 电压、pulldown） | `02.06.05.02.25` |
| 26 | `UPTD` | 声明或查询某 setup/result/command set 是否与硬件一致（1 = 一致，0 = 不一致）；`LEV`/`DPS` 等 status | `02.06.05.02.26` |
| 27 | `WAIT` | 让 MCD 等待指定微秒数再执行下一条固件命令，用于继电器切换或电源稳定 | `02.06.05.02.27` |
| 28 | `*RST` | 复位固件与全部校准数据，装载 power-on 默认值；不带参数会强制 disconnect、删除默认以外的 DPS set 及资源/引脚定义，`SWR` 则删除所有资源与引脚定义并复位 instrument | `02.06.05.02.28` |
| — | `DSCP` | 定义 device cycle、waveform/timing/level/DPS/routing 等 parameter set 的最大实例数并预留 Sequencer Memory；`level_set` 与 `dps_set` 默认 32、最大 256 | `02.06.04.02.01` |

### 重点命令与最小示例

以下示例全部逐字取自文档；单位、参数顺序按原文。

**`DRLV`（driver 电平）**

```
DRLV {level_set_no | level_set_id}, [logic_0_level], [logic_1_level], [v3h_level | range,] {(pinlist)}
DRLV? {level_set_no | level_set_id}, {(pinlist)}
```

```
DRLV 1,-1750,-850,(Q0,Q1,Q2,Q3)
```

把 level set 1 中 Q0–Q3 的逻辑 0/1 驱动电平设为 -1750 / -850 mV（`02.06.05.02.05`）。文档另给 8 V 量程示例 `DRLV 1,-1750,-850,8000,(avi64Pin1)`。注意：每次调用 `DRLV` 都需要激活 level set，多 site 并行时可能增加测试时间，文档建议此时改用 `SVLR`。

**`RCLV`（comparator 阈值）**

```
RCLV {level_set_no | level_set_id}, [vth | logic_0_level], [logic_1_level], [range,] {(pinlist)}
RCLV? {level_set_no | level_set_id}, {(pinlist)}
```

```
RCLV 1,-1300,-750,(Q0)
```

低/高比较阈值 -1300 / -750 mV（`02.06.05.02.18`）。`vth` 是 FAST comparator 的单阈值。文档警告：给高分辨率电流 comparator 指定 `range` 会被忽略。

**`TERM`（端接模式）**

```
TERM {level_set_no | level_set_id}, [term_mode], [term_pulldown,] [param_1], [param_2], [param_3],
[l_range], [h_range], [hr_mode,] {(pinlist)}
TERM? {level_set_no | level_set_id}, {(pinlist)}
```

```
TERM 1,T,-1500,,,,,(Q1)
TERM 3,A,3000,1500,1000,I3E4,I3E4,(out)
TERM 1,CT,2000,,,,,(o1,o1-)
TERM 1,OFF,PULLDOWN,,,,,,(Q1,Q2)
```

分别表示：输出引脚 Q1 端接到 -1500 mV；引脚组 `out` 的 active load 换向电压 3 V、Iol/Ioh = 1.5/1.0 mA、两端都用 0–30 mA 量程；差分对 `o1`/`o1-` 用 center-tap 端接到 2000 mV；PS1600 上打开/关闭 pulldown（`02.06.05.02.25`）。文档的 Termination modes 表列出 `OFF`、`DIFHIZ`、`T`、`H`、`L`、`A`、`CT`、`XSE`、`X`、`C` 及各自参数；level set 0 只支持 `OFF`（默认）、`T`、`C`、`A`。

**`CLMP`（clamp）**

```
CLMP {level_set|level_set_id}, [clamp_mode], [low_clamp_level], [high_clamp_level], {(pinlist)}
CLMP? {level_set|level_set_id}, {(pinlist)}
```

```
CLMP 1,ON,-10,5100,(Q0,Q1,Q2,Q3)
```

level set 1 中 Q0–Q3 的 clamp 打开，低 -10 mV、高 5100 mV（`02.06.05.02.02`）。文档说明：PS9G 没有 clamp，设置会被忽略；PS1600 的 clamp 电平与 driver 电平必须落在 -2.0 V…7.0 V 的 9.0 V 窗口内（`02.06.05.01.03`）。

**`PSLV`（DPS 电平）**

```
PSLV {dps_No|dps_set_id}, [voltage], [source_current], [sink_current,] [impedance], [setup_time], {(pinlist)}
PSLV? {dps_No|dps_set_id}, {(pinlist)}
```

```
PSLV 1,5.2,0.5,HIZ,15,(Vee)
```

DPS set 1：5.2 V、0.5 A 限流、断开状态 `HIZ`（最小电流）、setup time 15 ms（`02.06.05.02.15`）。`impedance` 还可取 `LOZ`、`HIZ_R`、`LOZ_HIZ`、`LOZ_HIZ_R`；`PSLV ALL` 只作用于非 equation-based 的 DPS set。

**`SPRM` / `APRM`（primary sets）**

```
SPRM [waveform_set_no], [timing_set_no], [level_set_no|level_set_id], [dps_set_no|dps_set_id]
SPRM {timing_specset_id}, [timing_set_no], [level_set_no|level_set_id], [dps_set_no|dps_set_id]
SPRM? 
APRM {mode}
```

```
APRM CNL
```

`SPRM` 只是“定义/记录” primary sets，不激活硬件；`APRM` 才把 `SPRM` 定义的主集合激活到硬件（`02.06.05.02.22`、`02.06.05.02.01`）。`SPRM` 即使发现某个 set 不存在也会保存传入值（文档 Note）。

**`EQFS` / `EQSP`（方程数据搬运）**

```
EQFS LEV,EQN,LOAD,"/tmp/level_equation",
```

把 `/tmp/level_equation` 作为 level equation 文件 load 进来（`02.06.05.02.09`、`02.06.05.01.04.03`）。

`EQSP` 的二进制块格式为：`#` + 1 位“长度说明符的位数” + 若干位长度（字节）+ 数据，数据以 `@` 终止；文档给出 `EQSP? TIM,WVT` 的回读示例（`02.06.05.02.10`）。

**`SPST?` / `UPTD` / `SVLR`（状态与运行时改值）**

```
SPST? {spec_type}, {equation_set_no}, {specset_no}
SPST? lev,all,all
```

status 位 8 表示 timing/level 数据可被 `ETIM`/`PCLK`/`DRLV`/`RCLV`/`TERM`/`PSLV` 等改写；位 10 表示被 `SVLR` 改过（`02.06.05.02.23`）。`TERM` 也会置位 bit 8（`02.06.05.02.25`）。

```
UPTD? CONF
UPTD LEV,1
```

`UPTD?` 返回 1/0；上电、`*RST`、`DSCP` 后所有 flag 为 0（`02.06.05.02.26`）。

```
SVLR {spec_type}, {equation_set_no}, {specset_no}, {"spec_name"}, {value} [,(pinlist)]
```

`SVLR` 只改 runtime，不改 setup 值；下一次 functional test 开始时生效。文档 CAUTION：不要为了调试以外的目的把 `LEVEL_SPEC`/`TIMING_SPEC` API 与固件改值命令混用（`02.06.05.02.24`）。

**`DSCP`（容量）**

```
DSCP [device_cycle], [waveform_set], [timing_set], [level_set], [dps_set], [pmu_set],
[devicecycle_set], [routing_set], [period_res_prec],
DSCP 256,16,256,32,32,1024,16,1,256,
```

第 4 个参数是 level set 上限，第 5 个是 DPS set 上限（`02.06.04.02.01`）。上电默认 `DSCP 256, 16, 256, 32, 32, 16, 16, 32, 256, 256`（`02.06.01.04`）。

### fixed level set 流程（文档事实，但 7.10.3 已停止支持）

文档把下列命令列为“创建 level set 相关命令”，但没有逐条规定执行顺序；下面的编号**顺序是推断**，命令名、作用与出处是文档事实（`02.06.05.01.05.01`、`02.06.05.01.05.04`）：

1. `LSUS?` 查当前 set 数，选下一个编号（`02.06.05.01.05.01`）。
2. `DRLV` 设 driver 电平（`02.06.05.01.05.01.01`）。
3. `RCLV` 设 comparator 阈值（`02.06.05.01.05.01.02`）。
4. `TERM` 设端接；或 `CLMP` 独立设 clamp（`02.06.05.01.05.03`、`02.06.05.01.05.01.03`）。
5. DPS 侧用 `DSUS` 定数量、`PSLV` 设电压/限流/断开阻抗/setup time（`02.06.05.01.05.04`）。
6. 删除 set 用 `LSUS`（set 1 不能删）（`02.06.05.01.05.02`）。

文档的 fixed level 文件示例（`02.06.05.01.05.07`）：

```
hp93330,level,0.1
PSLV 1,-4.5,0.4,HIZ,10,(Vee) - set Power Supply LeVels
DRLV 1,-1700,-950,(CP,D3,D0_NCET,MR,NCEP,P3,P2,P1,P0,S2,S1,S0)-set DRiver LeVels
RCLV 1,-1300,-750,(NQ3,NQ2,NQ1,NQ0,NTC,Q3,Q2,Q1,Q0) - set ReCeiver LeVels
TERM 1,a,-800,3000,4000,I5E3,I5E3,(Q0,Q1,Q2,Q3) - set TERMination mode
```

注意这个示例的首行是 `hp93330,level,0.1`；较新的文档示例首行为 `hp93000,level,0.1`（`02.07.11.01.05.01`）。两种都见于文档，不要据首行判断版本能力。

### equation-based level 文件骨架（文档事实）

必需模块：equation set number、Specs module、Equations module、DPS module、Level sets module，外加 Spec Sets（在 Spec Tool 中定义）（`02.06.05.01.04.02`）。最小骨架（由 `02.06.05.01.04.02.03`–`.05`、`02.06.05.01.04.04`、`01.07.01.03.02` 组合）：

```
EQNSET 1 "Equation set 1"
MODECONTEXT "DEFAULT"

SPECS
vcc_level [V] # Base Vcc voltage
vcc_offset [V] # Offset to add to vcc_level

EQUATIONS
vil_level = vcc_level*0.1
vih_level = vcc_level*0.9

DPSPINS vcc
vout = vcc_level + vcc_offset
ilimit = 20
t_ms = 0
offcurr = min

LEVELSET 1 "nominal"
PINS ctrl ser_in
vil = vil_level
vih = vih_level

PINS ser_out
vol = 2.4
voh = 2.6
```

语法要点（全部文档事实）：

- `EQNSET` 编号 1–256，必须唯一；描述最多 60 字符（`02.06.05.01.04.02.01`）。
- `MODECONTEXT "name"` 必须紧跟 `EQNSET` 行；不写则 `DEFAULT`（`02.06.05.01.04.02.02`）。
- `SPECS` 只声明变量与单位，不给值；单位只能在 equation setup 里定义（`02.06.05.01.04.02.03`）。
- `EQUATIONS` 的行数必须等于 equation variable 数，左边是变量、右边是表达式（`02.06.05.01.04.02.04`）。
- `LEVELSET` 编号 1–99，描述可选；所有 equation set 合计最多 256 个 level set（`02.06.05.01.04.02.06`）。
- `PINS` 资源可写 `vil`/`vih`/`v3h`/`vihh`/`vol`/`voh`/`vth`/`iol`/`ioh`/`vt`/`vcl`/`vch`/`hyst`/`irng`/`orng`/`rec_offset`/`rec_swing`/`term`；`term` 若使用必须是第一个值，其余顺序任意但不可重复（`02.06.05.01.04.02.07`）。
- 引脚排除语法 `PINS <pin list> -( <exclude pin list> )`；括号内侧必须有空格（`02.06.05.01.04.02.06.01`）。
- `@diff` 只用于差分对，且只能写在 equation editor，不能写在 level/timing GUI（`02.06.05.01.04.02.06.02`）。
- 端接模式可由资源隐式决定（`ioh`/`iol`/`vt` 的有无），也可用 `term` 显式指定；显式 `term` 行必须紧跟 `PINS` 行（`02.06.05.01.04.02.07.01`、`02.06.05.01.04.02.07.02`）。
- 不同卡、端接模式、pin type 支持的资源不同，见 Supported level resources 的三张表（`02.06.05.01.04.02.08`）。

### level set 0 / 高阻 / pulldown（fixed 专属）

- sequencer 在 RUN/BRK 时用用户 level set；在 OFF 时用预定义的 level set 0；`DLSO` 执行时也会激活 level set 0（`02.06.05.01.05.05`）。
- level set 0 只能用 fixed level setup 编程，不能写进 equation-based setup；不能被 `SPRM` 选为 primary；不包含在 `TERM`/`CLMP` 的 `ALL` 参数里；只支持部分端接模式（`02.06.05.01.05.05`）。
- 编程顺序：load level setup → `TERM`/`CLMP` 编程 set 0 → `SQST BRK`；三步只在 testflow 开始时做一次；下载新 level setup 后 set 0 会被重置（`02.06.05.01.05.05`）。
- 文档示例：

```
CLMP 0,ON,vcl,vch,(@)
TERM 0,A,vcom,iol,ioh,,,(@)
SQST BRK
SQST OFF
```

- pulldown：PS1600 有 14.3 kΩ 可切换 pulldown，PS5000 用 active load 的 pin line discharge；默认在 pin disconnect 时接合（`02.06.05.01.05.06`）。全局默认由 level set 0 与 `.technology` 的 `pulldown_in_level_set_0: off` 控制；显式设置可在 Level Setup 的 `pulldown` 列选 `pulldown`/`none`，或在方程里写 `term off pulldown` / `term off`，且该行上一行必须是 `PINS`（`02.06.05.01.05.06`）。
- 做 off-state DC 测量（Board ADC、SPMU IFVM/VFIM、continuity）时可能需要临时关 pulldown：

```
TERM 0,OFF,NONE,,,,,,(pin_group)
SQST BRK
SQST OFF
```

重新打开：

```
TERM 0,OFF,PULLDOWN,,,,,,(pin_group)
SQST BRK
SQST OFF
```

## L2 — Test Method API

**文档事实。** 本阶段对应的 C++ Test Method API 主要有四类：

1. **`LEVEL_SPEC`**（头文件 `/opt/hp93000/soc/prod_com/include/MAPI/LevelSpec.h`）：访问已有 level equation set + spec set 的内容。构造函数 `LEVEL_SPEC(INT eqnset, INT specset)`；成员 `getEquation()`、`getSpec()`、`getSpecValue(const STRING& spec)`、`change(const STRING& spec, DOUBLE value)`、`change(..., const STRING& pin)`、`restore()`。示例：

```
LEVEL_SPEC spec1(1, 2);
Primary.level(spec1);
Primary.getLevelSpec().change("v_low", -2.1 V);
Primary.getLevelSpec().change("vdde", 4.4, "VCC");
FLUSH(TM::APRM);
double vLow = Primary.getLevelSpec().getSpecValue("v_low");
```

`change()` 的 per-pin 版本只保留一个 flush 周期，且不能用 `getSpecValue` 读回引脚特定值；`restore()` 把 spec 值恢复为当前 test suite 的程序启动时的值（`02.07.04.01.124`）。

2. **`PRIMARY_STATUS`**（`Primary` 对象，头文件 `PrimaryStat.h`）：访问当前数字 primaries（timing、level、start label）；与 level 有关的是 `getLevelSpec()`、`getLevel()`、`level()`，DPS set 侧还有 `getDps()`、`dps()`。修改要等 `EXECUTE_TEST`/`START_TEST`/`FUNCTIONAL_TEST`/`FLUSH` 等执行后才反映到硬件（`02.07.04.01.167`）。文档另给“在 primary level spec set 中改 spec 值”的专页，只能用 `LEVEL_SPEC` 的一个成员函数，不能在同句混用 `PRIMARY_STATUS` 的其他成员（`02.07.03.03.02.02`）。

3. **`SetupLevelSet0`**：改 level set 0（高阻态）的 clamp 与 active load。参数为 `Pins[]`、`ClampVoltage.Mode[]`/`Low_V[]`/`High_V[]`、`ActiveLoad.Mode[]`/`CommutationVoltage_V[]`/`SourceCurrent_A[]`/`SinkCurrent_A[]`；PS9G 无 clamp/active load，设置被忽略（`02.07.05.04.06`）。它对应 L1 中 level set 0 的 `TERM`/`CLMP` 用法。

4. **`CCTchangeLevelSpec`**（`CCTestMethod.hpp`）：`void CCTchangeLevelSpec(const string& old_spec, DOUBLE value);`，改指定 spec 的值；7.2.0 引入，7.2.1 从 `CCT_changeLevelSpec` 改名（`02.07.04.01.14.02`）。

5. **`LevelSetSelector`**（`DigitalOffsetSearchTypes.h`）：给 `DIGITAL_OFFSET_SEARCH_TASK`/`DIGITAL_OFFSET_SEARCH_PINS` 指认单个 level set（fixed 编号或 equation-based ID `equset*100000 + specset*1000 + level_set_no`）、primary 或全部 fixed set（`02.07.04.01.123`）。

**本次未找到**：与 `DRLV`/`RCLV`/`TERM`/`CLMP`/`PSLV` 一一对应的“直接写电平”L2 API。L2 侧文档化的改值入口集中在 spec 变量（`LEVEL_SPEC`、`CCTchangeLevelSpec`）与 level set 0（`SetupLevelSet0`）；其余电平配置仍走 setup 文件/固件命令。这是检索结果，不是“不存在”的全称断言。

## L3 — 外部控制

**L3 入口是横切的，能力面按阶段分族。** 横切入口有两类：Test Suite Control API（`TestsuiteProxy`，`02.09.01.14`）与 TPI Program Routines（`02.09.01.09`）。本阶段的专属成员是：

- `TestsuiteProxy.getLevelEquation()`：取测试套件使用的 level equation（`02.09.01.14.02.01.05`）。
- `TestsuiteProxy.getLevelSpec()`：取 level spec（`02.09.01.14.02.01.07`）。
- `TestsuiteProxy.getLevelSet()`：取 level set（`02.09.01.14.02.01.06`）。
- `TestsuiteProxy.setEquationBasedLevel(levelEquation, levelSpec, levelSet)`：给测试套件设置 equation-based level 信息（`02.09.01.14.02.01.25`）。
- TPI `DataManager` 的 `dm_level` 文件 ID：对应 level setup 文件（`02.09.01.09.02`）。
- TPI `GetEQVariableValue` / `InsertEQVariableInCache`：`equation_system` 可取 `LEVEL_EQ_SYSTEM`，按 equation set + spec set + site 读取/缓存 spec 或 equation 变量（`02.09.01.09.10`、`02.09.01.09.22`）。

Test Suite Control API 的适用范围是文档写明的：用于在 testflow tool 之外直接控制 test suite，只支持 UTM-based test suite，不能用于 test method 编程，也不能与 HVM API、BLC API 由同一客户端进程并行使用（`02.09.01.14`）。STPM merge rules 里还有四条与 level 有关的合并策略：`new_level_resource`（`allow`/`reject`）、`overwrite_level_resource`（`allow`/`ignore`/`reject`）、`new_level_equation_set`（`allow`/`reject`）、`new_level_set`（`allow`/`reject`），控制把测试合入 master test program 时 level 资源/方程集/level set 的增改行为（`02.09.02.04.18`–`.21`）。

**同形陷阱（显式记录）。**

- HVM 的 `GetLevelProfile` 返回的是 application model 中某个 level 的变量名/变量值（`LEVEL_NAME`、`LEVEL_TYPE`、`VARIABLE_NAME_LIST`、`VARIABLE_VALUE_LIST`），level 类型是 `WAFER_LEVEL`/`DEVICE_LEVEL`/`CUSTOM_LEVEL`；它不是引脚电压 level（`02.09.01.10.03.02.02.26`）。
- BLC 的 `StartLevel()`/`LoopLevel()`/`CompleteLevel()` 维护的是 application model 文件的 level 结构，会发 `AppModelLevelStartEventType`/`LEVEL_STARTED` 事件；同样不是电压 level（`02.09.01.11.03.02`、`02.09.01.11.03.02.01`）。
- `TestsuiteProxy` 只能改测试套件的 level equation/spec/set 归属，不改具体电压值；改值仍要靠 spec 变量（`02.09.01.14.02.01.25`）。

**SmartShell。** 全库唯一的 SmartShell 总述 `02.15` 明写 `Introduced in SmarTest 8.2.5`，而本 wiki 面向 7.10.3；该章正文只有 PDF 外链，没有本阶段可用的命令语义。因此**不把 SmartShell 当作 7.10.3 的 level L3 接口**（`02.15`）。

**文档未覆盖**：7.10.3 下用于“直接读写某个引脚当前驱动/比较电平”的外部控制接口。本次在 Test Suite Control API、TPI、HVM/BLC 章中未找到这类成员；上列成员只覆盖 equation/spec/set 的归属与 spec 变量值。

## 产物

**文档事实。**

- **level 文件**：位于 device directory 的 `levels/` 子目录（`01.07.01.01.01`）。首行形如 `hp93000,level,0.1`（`02.07.11.01.05.01`；fixed 示例为 `hp93330,level,0.1`，`02.06.05.01.05.07`）。文件内含一个或多个 `EQNSET`（每个含 `SPECS`/`EQUATIONS`/`DPSPINS`/`LEVELSET`），也可混入 fixed 命令（`02.06.05`、`02.06.05.01.04.02`）。
- **level master file**：`levels.mfh`，首行 `hp93000,level_master_file,0.1`，第二行 `testerfile: <name>`，其后是 `EQNSET <n> [PIN_ALIAS_SET <name>]: <file>`、`TESTDATA <name>: <file>`、`DEFINES: <file>`、`GENERAL: <file>`（`02.08.04.14.02.05.01`）。把 `levels` 另存为 `.mfh` 后，`levels/` 下会出现 `changelog.txt`、`eqnset_01.lev`、`eqnset_02.lev`、`levels`、`levels.mfh`（`01.01.07.02.02.04.04`）。
- **`GENERAL.lev`**：level switching order（`SLDO`）保存在 master file 的 `GENERAL` 条目指向的文件中（`02.08.04.14.02.05.01`、`02.08.04.14.04.11.01`）。
- **`TESTDATA` 块**：DC Scale 动态测量时由 SmarTest 自动创建，对应 `DFTD`（`02.08.04.14.02.05.01`）。
- **`.prot_lev`**：`USE_PROTOCOL` 引用的协议 level segment，XML，保存在器件的 protocol 目录（`02.07.11.01.05.01`）。
- **硬件侧产物**：所有 set 随 load 一起进入硬件；实际生效的是 primary 或 `CLEV` 指定的 level set（`02.08.04.14.02.01`、`02.06.07.01.08.03.02`）。

本阶段不产出测试结果数据；结果类产物见 [[results]]。

## 验证

以下均为文档给出的验证入口，未自行发明。

1. **Level Setup 窗口即时反映硬件。** 打开方式：Test Program Explorer 双击 `Level` 图标；默认显示 I/O pins 视图（`02.08.04.14.04`）。文档写：窗口始终与硬件中的活动 level 设置保持一致，编辑电平值后“一离开该字段”就生效（`02.08.04.14.04`）。
2. **`Select > Show I/O Eqn & Specs Results`。** 依次改 `Eqn#`（equation set）、`Sps#`（spec set）、`Lset#`（level set），核对值是否符合要求；DPS 用 `Select > Show DPS Eqn & Specs Results`，FAST 引脚用 `Select > Show Fast Eqn. & Specs Results`（`02.06.05.01.04.03.01`、`02.08.04.14.04.11`、`02.08.04.14.04.10`）。
3. **查询命令。** `DRLV?`、`RCLV?`、`TERM?`、`CLMP?`、`EQFC?`、`PSLV?`、`PSSR?`、`DSUS?`、`LSUS?`、`SPRM?`、`SDSC?`、`DPRL?` 返回对应 set/引脚的现有设置（各命令页）。
4. **接收端阈值实测。** `RCLS?` 对输出引脚做阈值搜索/测量，返回 `P`/`F` 或 `LT`/`LE`/`EQ`/`GE`/`GT` 及结果 mV（`02.06.05.02.17`）。示例：

```
RCLS? H,3000,6000,(Q0)
RCLS EQ,5300
```

5. **状态位与文件状态。** `SPST?` 查 spec set 的 status bits（例如 bit 8 表示被 `DRLV`/`RCLV`/`TERM`/`PSLV` 改过，bit 10 表示被 `SVLR` 改过）；`UPTD? LEV`/`UPTD? DPS` 返回 1/0 判断硬件与文件是否一致（`02.06.05.02.23`、`02.06.05.02.26`）。
6. **Report window / 错误文件。** 下载后检查 Report window 的报错；`EQFS` 可把详细错误写到 `error_filename`，或写 `UI_REPORT` 到报告窗口；`MERL` 控制错误/消息条数上限（`02.08.04.14.02.03.10`、`02.06.05.02.09`、`02.06.05.02.14`）。
7. **GUI 的 Results 段。** 各 how-to 页的 `Results` 明确写出应看到什么：例如单端 driver 设置后 `level [V] low/high` 列显示 drive levels；clamp 设置后 clamp mode 显示 `on`、`clamp low/high [V]` 显示电压；active load 后 termination mode 显示 `load`，`termination lev/v3h`、`Iol [mA]`、`Ioh [mA]` 显示对应值；context 显示在 Level Setup 窗口的 Context 字段（`02.08.04.14.04.06`、`02.08.04.14.04.08.01`、`02.08.04.14.04.08.02`、`01.07.01.03.01`）。
8. **fixed clamp/termination 的文档级验证。** `CLMP?` 返回 clamp 电平与模式，`TERM?` 返回端接参数；`02.06.05.01.04.03.01` 的 Procedure 也适用于 equation-based（改 `Eqn#`/`Sps#`/`Lset#` 后核对）。

## 常见错误

| 症状 | 文档给出的原因 / 处理 | 出处 |
|---|---|---|
| Level Setup 窗口信息区出现 `EDITED`，窗口值与方程文件不一致 | 直接在 Level Setup 窗口改了电平值；用 `Edit > Restore` 选 spec set 恢复（与 timing 同理） | `02.08.04.30.02.18`、`02.08.04.14.04.06` |
| Spec Tool 已 download，但前端/硬件行为没变 | Spec Tool 只改后端硬件，不自动更新前端；需 `APRM`，或做 disconnect/connect，或用 Hardware view 逐通道 disconnect/connect | `02.08.04.30.02` |
| 弹 unit 不一致 warning | 已加载的 SPECSET 单位与 EQNSET 单位不同；按 warning 选择“用 EQNSET 单位”（Download 后 Save）或改 EQNSET 单位 | `02.08.04.30.02` |
| 用 NEdit 的 `File > Save` 后改动丢失/未进 setup | 文档明确：不要用 NEdit 的 `File > Save`；应先 `Shell > Download`，再在 Test Program Explorer 保存 Level Setup | `01.07.01.03.02`、`02.08.04.14.04.01` |
| 在 7.10.3 上按 fixed 流程配置 | fixed level setup 自 7.4.1T 停止支持；改用 equation-based | `02.06.05.01.05.01` 等 |
| 改 `DSCP` 后所有 set 丢失/行为异常 | `DSCP` 会清空 Sequencer Memory 并复位所有 set；必须重新装载 device setup | `02.06.04.02.01`、`02.06.01.04` |
| `TERM` 报错：对 o pin 用了 H 或 L | o pin 不能用 H/L，应用 `T`（带端接电压） | `02.06.05.02.25` |
| `TERM` 报错：参数组合不对/参数过多/电流量程不对 | 端接模式与 `param_1`–`param_3`、`l_range`/`h_range` 有固定组合；按 Termination modes 表检查 | `02.06.05.02.25` |
| `CLMP` 在 PS9G 上无效果 | PS9G 没有 clamp，设置被忽略 | `02.06.05.02.02` |
| `DRLV`/`RCLV`/`TERM` 只给 warning，值被自动修正 | 电平/阈值超出 spec、swing 限制或量程时会发生 auto-correction；查 warning 并核对卡规格 | `02.06.05.02.05`、`02.06.05.02.18`、`02.06.05.02.25` |
| `RCLV` 指定的 `range` 无效果 | 高分辨率电流 comparator 的 range 被忽略（warning） | `02.06.05.02.18` |
| level set 0 设置不生效 | 必须 load level setup 后再用 `TERM`/`CLMP` 编程，并 `SQST BRK` 使其生效；下载新 level setup 会重置 set 0 | `02.06.05.01.05.05` |
| level set 0 写进 equation 文件或 `SPRM` 选不到 | set 0 只能用 fixed level setup；不能作为 primary；不在 `TERM`/`CLMP` 的 `ALL` 中 | `02.06.05.01.05.05` |
| DC 测量/continuity 结果被 pulldown 影响 | off-state 测量时 pulldown 可能接合；可临时 `TERM 0,OFF,NONE`，测完 `TERM 0,OFF,PULLDOWN` 恢复 | `02.06.05.01.05.06` |
| 改了端接后比较结果不对 | 端接后传输线环境变化，原先按未端接设定的 compare threshold 可能不再适用；SmarTest 不会自动调阈值 | `02.08.04.14.04.08` |
| `SPRM` 报 set 不存在但仍继续 | 文档 Note：`SPRM` 即使检测到 set 不存在也会保存传入值；需自己核对 `SPRM?` | `02.06.05.02.22` |
| 混用 `LEVEL_SPEC` 与 `SVLR` 后 restore 行为异常 | 两类接口缓存机制不同；文档 CAUTION 禁止为调试以外目的混用 | `02.06.05.02.24`、`02.07.04.01.124` |
| 某些 I/O 引脚电平像“没设置” | equation set 未列出该 I/O 引脚会 warning，并使用默认设置 | `02.06.05.01.04.02.07` |
| 手改子文件后单独 load 报字节数错误 | `EQSP` 数据块带字节长度；单独 load 手改子文件需手工改长度，或用 Setup Management Tool 重组 | `02.08.04.14.02.05.02` |
| `UPTD?` 一直返回 0 | level 命令/equation setup/pin 命令都会把 `LEV`/`DPS` flag 置 0，直到保存或装载；上电/`*RST`/`DSCP` 也全为 0 | `02.06.05.02.26` |

**文档未覆盖**：本阶段没有独立的 `Errors` 汇总章（不像 pin 有 `02.06.03.01.11`）。各命令页的 `Errors`/`Warnings` 段是唯一文档化的错误清单，本表已按其内容归纳；没有文档依据的“常见错误”未写入。

## 下一步

**[[timing]]**。基本数字流程的章节顺序是 Defining the pins → **Setting up your levels** → Waveform and timing sets（`01.07.01`）；level 给出电压条件，timing/wavetable 在此之上定义边沿与周期。两者都完成后才进入 [[pattern]]；`testmethod` 里用 `LEVEL_SPEC` 改 spec 值、`testflow` 里用 `SPRM`/`APRM` 选 primary level set、[[pattern]] 阶段用 `CLEV` 在向量中切 set、`results` 阶段看测量结果。

**建议：** 在进入 [[timing]] 前，先用 `DRLV?`/`RCLV?`/`TERM?`/`PSLV?` 或 `Show I/O Eqn. & Specs Results` 把 level set 逐项核对一遍；否则 timing/pattern 调不通时很难区分是电平还是时序问题。这是建议，不是文档规定的步骤。
