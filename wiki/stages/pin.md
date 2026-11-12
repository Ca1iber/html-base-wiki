---
type: stage
title: Pin / Channel 配置（Pin Configuration）
tags: [pin, configuration, channel, multisite, dfpn]
related:
  - "[[project]]"
  - "[[level]]"
  - "[[timing]]"
  - "[[pattern]]"
  - "[[testmethod]]"
  - "[[testflow]]"
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.03_Pin_configuration_setup_commands.htm
  - 02_System_reference/02.06_Command_Reference/02.06.03.01_Concepts_of_Configuration_setup.htm
  - 02_System_reference/02.06_Command_Reference/02.06.03.01.01_Introduction.htm
  - 02_System_reference/02.06_Command_Reference/02.06.03.01.02_Assigning_a_pin_name_to_a_digital_channel.htm
  - 02_System_reference/02.06_Command_Reference/02.06.03.01.03_Configuring_pin_type_and_operating_mode_for_a_context.htm
  - 02_System_reference/02.06_Command_Reference/02.06.03.01.03.01_Mode_contexts.htm
  - 02_System_reference/02.06_Command_Reference/02.06.03.01.04_Assigning_a_pin_name_to_a_digital_or_DC_scale_channel.htm
  - 02_System_reference/02.06_Command_Reference/02.06.03.01.05_Defining_a_utility_line.htm
  - 02_System_reference/02.06_Command_Reference/02.06.03.01.06_Defining_pin_groups.htm
  - 02_System_reference/02.06_Command_Reference/02.06.03.01.07_Defining_ports.htm
  - 02_System_reference/02.06_Command_Reference/02.06.03.01.08_Defining_a_utility_purpose.htm
  - 02_System_reference/02.06_Command_Reference/02.06.03.01.09_Configuring_additional_sites_for_multi-site_testing.htm
  - 02_System_reference/02.06_Command_Reference/02.06.03.01.10_Controlling_multiple_test_sites.htm
  - 02_System_reference/02.06_Command_Reference/02.06.03.01.10.01_Activating_and_masking_a_site.htm
  - 02_System_reference/02.06_Command_Reference/02.06.03.01.10.02_Setting_the_setup_focus.htm
  - 02_System_reference/02.06_Command_Reference/02.06.03.01.10.03_Defining_the_query_focus.htm
  - 02_System_reference/02.06_Command_Reference/02.06.03.01.10.04_Controlling_the_site_match_function.htm
  - 02_System_reference/02.06_Command_Reference/02.06.03.01.11_Errors.htm
  - 02_System_reference/02.06_Command_Reference/02.06.03.01.12_Pin_Configuration_Example.htm
  - 02_System_reference/02.06_Command_Reference/02.06.03.02_List_of_configuration_commands.htm
  - 02_System_reference/02.06_Command_Reference/02.06.03.02.01_CHIN__-__CHannel_INformation.htm
  - 02_System_reference/02.06_Command_Reference/02.06.03.02.02_CONF__CONF__-__CONFiguration.htm
  - 02_System_reference/02.06_Command_Reference/02.06.03.02.03_CTXT__CTXT__-__ConTeXT.htm
  - 02_System_reference/02.06_Command_Reference/02.06.03.02.04_DFGE__DFGE__-__DeFine_Group_by_Expressions.htm
  - 02_System_reference/02.06_Command_Reference/02.06.03.02.05_DFGP__DFGP__-__DeFine_GrouP.htm
  - 02_System_reference/02.06_Command_Reference/02.06.03.02.06_DFLV__DFLV__-__DeFaultLeVel.htm
  - 02_System_reference/02.06_Command_Reference/02.06.03.02.07_DFPC__DFPC__-__DeFine_Pin_Comment.htm
  - 02_System_reference/02.06_Command_Reference/02.06.03.02.08_DFPN__DFPN__-__DeFine_Pin_Name.htm
  - 02_System_reference/02.06_Command_Reference/02.06.03.02.09_DFPS__DFPS__-__DeFine_Power_Supply.htm
  - 02_System_reference/02.06_Command_Reference/02.06.03.02.10_DFPT__DFPT__-__DeFine_PorT.htm
  - 02_System_reference/02.06_Command_Reference/02.06.03.02.11_DFUP__DFUP__-__DeFine_Utility_Purpose.htm
  - 02_System_reference/02.06_Command_Reference/02.06.03.02.12_DFUT__DFUT__-__DeFine_UTility_line.htm
  - 02_System_reference/02.06_Command_Reference/02.06.03.02.13_DSCP__DSCP__-__Define_System_Control_Parameter.htm
  - 02_System_reference/02.06_Command_Reference/02.06.03.02.14_GCTX__-__Get_ConTeXt.htm
  - 02_System_reference/02.06_Command_Reference/02.06.03.02.15_HWTY__-__HardWare_TYpe.htm
  - 02_System_reference/02.06_Command_Reference/02.06.03.02.16_PACT__PACT__-__Parallel_ACTivities_control.htm
  - 02_System_reference/02.06_Command_Reference/02.06.03.02.17_PALS__PALS__-__Pin_ALlocation_for_multiple_Sites.htm
  - 02_System_reference/02.06_Command_Reference/02.06.03.02.18_PFND__-__Pin_FiND.htm
  - 02_System_reference/02.06_Command_Reference/02.06.03.02.19_PQFC__PQFC__-__Parallel_Query_FoCus.htm
  - 02_System_reference/02.06_Command_Reference/02.06.03.02.20_PRLT__-__request_Parallel_ResuLTs.htm
  - 02_System_reference/02.06_Command_Reference/02.06.03.02.21_PSSL__PSSL___Power_Supply_Safety_Limits.htm
  - 02_System_reference/02.06_Command_Reference/02.06.03.02.22_PSTE__PSTE__-__Parallel_SiTe_Enable.htm
  - 02_System_reference/02.06_Command_Reference/02.06.03.02.23_STME__STME__-__SiTe_Match_Enable.htm
  - 02_System_reference/02.06_Command_Reference/02.06.03.02.24_UDEF_-__UnDEFine_pin.htm
  - 02_System_reference/02.06_Command_Reference/02.06.03.02.25_UDGP_-__UnDefine_GrouP.htm
  - 02_System_reference/02.06_Command_Reference/02.06.03.02.26_UDPS_-__Undefine_DPS_pin.htm
  - 02_System_reference/02.06_Command_Reference/02.06.03.02.27_UDUP_-__UnDefine_Utility_Purpose.htm
  - 02_System_reference/02.06_Command_Reference/02.06.03.02.28_UDUT_-__UnDefine_UTility_line.htm
  - 02_System_reference/02.06_Command_Reference/02.06.03.02.29_UDVP_-__UnDefine_Virtual_Pin.htm
  - 02_System_reference/02.06_Command_Reference/02.06.03.02.30_UPAS__UPAS__-__Utility_Purpose_ASsignment_for_multi-site.htm
  - 02_System_reference/02.06_Command_Reference/02.06.03.02.31_UPST__UPST__-__Utility_Purpose_STate.htm
  - 02_System_reference/02.06_Command_Reference/02.06.03.02.32_UPTI__UPTI__-__Utility_Purpose_settling_TIme.htm
  - 02_System_reference/02.06_Command_Reference/02.06.03.02.33_UTST__UTST__-__UTility_line_STate.htm
  - 02_System_reference/02.06_Command_Reference/02.06.03.02.34_UTTI__UTTI__-__UTility_line_settling_TIme.htm
  - 02_System_reference/02.06_Command_Reference/02.06.03.02.35_VPIN__VPIN__-__Virtual_PIN.htm
  - 02_System_reference/02.06_Command_Reference/02.06.03.02.36_IDN__-__IDeNtify.htm
  - 02_System_reference/02.06_Command_Reference/02.06.03.02.37_OPT__-__hardware_OPTions.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18_Pin_configuration_tool.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.01_Introduction_of_the_Pin_Configuration_Tool.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.01.01_Pin.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.01.02_Pin_group.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.01.03_Port.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.01.04_Alias_set.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.01.05_Utility_purpose.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.02_Using_the_Pin_Configuration_Tool.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.02.01_Opening_the_setup_editor.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.02.02_Importing_the_pin_configuration_from_a_CSV_file.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.02.03_Exporting_the_pin_configuration_to_a_CSV_file.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.02.04_Discarding_the_changes_in_the_pin_configuration_tool.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.02.05_Applying_pin_configuration_data.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.02.06_Saving_a_modified_pin_configuration.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.02.07_Working_with_pins.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.02.07.01_Virtual_pins.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.02.07.02_Editing_the_pin_configuration.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.02.07.03_Defining_a_context.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.02.07.04_Defining_additional_test_sites.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.02.07.05_Copying_and_pasting_a_pin.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.02.07.06_Deleting_a_pin.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.02.07.07_Defining_external_triggers_for_DPS_measurements.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.02.08_Working_with_pin_groups.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.02.08.01_Creating_a_pin_group.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.02.08.02_Editing_a_fixed_group.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.02.08.03_Editing_an_expression-based_group.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.02.08.04_Copying_and_pasting_a_group.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.02.08.05_Deleting_a_group.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.02.09_Working_with_ports.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.02.09.01_Creating_a_port.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.02.09.02_Editing_a_port.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.02.09.03_Copying_and_pasting_a_port.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.02.09.04_Deleting_a_port.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.02.10_Working_with_utility_purposes.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.02.10.01_Creating_a_utility_purpose.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.02.10.02_Editing_a_utility_purpose.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.02.10.03_Copying_and_pasting_a_utility_purpose.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.02.10.04_Deleting_a_utility_purpose.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.02.11_Setting_DC_Scale_voltage_and_current_limits.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03_Elements_of_the_Pin_Configuration_Tool.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.01_Pin_setting_editors.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.01.01_Context_list.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.01.02_Digital_Pins_editor.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.01.03_DPS_Pins_editor.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.01.03.01_DC_Scale_pin__DPS_mode__setup.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.01.03.02_Load_capacitance_connected_to_the_DC_Scale_DPS128_DPS64.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.01.03.03_Load_capacitance_connected_to_the_DC_Scale_XPS256.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.01.04_Utility_Pins_editor.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.01.05_Utility_Purpose_Editor.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.01.06_Virtual_Pins_editor.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.02_Pin_group_editor.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.02.01_Rules_for_defining_groups.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.02.02_Incompatible_pin_groups.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.03_Port_Editor.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.04_Alias_Set_Editor.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.05_DC_Scale_Extensions_editor.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.06_DC_Scale_Limits_editor.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.07_DC_Scale_Regulation_editor.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.08_DC_Scale_Safety_editor.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.09_Ground_sense_editor.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.10_Protocol_assignments.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.10.01_Assigning_pin_roles_and_protocols.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.11_Apply_button.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.12_State_indicator.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.13_Filter_line.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.14_Sorting_rows.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.04_Pin_configuration_file.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.05_Pin_configuration_master_file.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.01.01.02_Task_2__Pin_Configuration_Setup.htm
  - 01_Getting_started/01.07_Testing_a_Basic_Digital_Device/01.07.01.01.01_Device_directory_structure.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.147_PIN_UTILITY.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.81_GET_CONFIGURED_SITES.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.14.32_CCTsetContextPins.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.14.08_CCTgetContextPins.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.14.27_CCTRegisterDCPins.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.05.04.05_GetUtilityLines.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.05.04.07_SetUtilityLines.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.11.01.09.08_Pin_role.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.11.01.09.10_Protocol.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14_Test_Suite_Control_API.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.01_How_to_use_the_test_suite_control_API.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.30_TestsuiteProxy.setSiteMatch.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.10_TestsuiteProxy.getSiteMatch.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.12_setSiteInFocus.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.13_getSiteInFocus.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.14_setActiveSites.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.15_getActiveSites.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.09_TPI_Program_Routines.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.09.01_ChangeDevice.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.09.02_DataManager.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.09.05_GetActiveSites.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.09.06_GetAvailableSites.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.09.08_GetEnabledSites.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.09.13_GetNumberOfSites.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.09.14_GetSiteInFocus.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.09.15_GetSiteState.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.09.25_RestoreSiteState.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.09.26_SetActiveSites.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.09.27_SetEnabledSites.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.09.29_SetSiteInFocus.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.15.04.01_TPI_functions.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.10.01_HVM_API_Introduction.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.10.03.02.02.20_DownloadTestprogram.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.10.03.02.02.12_ChangeDevice.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.10.03.02.02.54_SETUPFILE_DOWNLOAD_COMPLETED.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.10.03.02.02.55_SETUPFILE_DOWNLOAD_STARTED.htm
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.64_DFPR__DFPR__-__DeFine_Pin_Role.htm
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.297_UDPR_-__UnDefine_Pin_Role.htm
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.299_UDPT_-__UnDefine_PorT.htm
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.191_PSFC__PSFC__-__Parallel_Setup_FoCus.htm
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.124_FLSH_-__FLuSH_buffered_commands.htm
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.241_SQST__SQST__-__SeQuencer_STate.htm
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.54_DDIC__DDIC__-__Define_DUT_Interface_Connection.htm
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.206_RLYC__RLYC__-__ReLaY_Control.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.02.03.02_File_and_parameter_settings.htm
  - 02_System_reference/02.15_SmartShell/02.15_SmartShell.htm
created: 2026-11-12
updated: 2026-11-12
verified: doc-only
---

# Pin / Channel 配置

> 把 DUT 的引脚名绑定到测试机通道、确定方向与工作模式，并建立 Level / Timing / Pattern 都要引用的名字空间。

## 目的

**文档事实**：`02.06.03` 开篇把这一步定为测试准备的第一件事：

> Configuring pins is the first step you must take when preparing a test. It is impossible to define level, timing, or vector parameters without the pin configuration.

同一篇按功能把配置命令分成 digital pin、mode context、DPS pin、DC Scale pin、utility line、utility DC pin、pin group / port、pin alias、multi-site 九组。`02.06.03.01.01` 重复了这份分组清单，并补了一条运行期限制：

> Note The firmware does not accept any configuration changes while a test is running.

**文档事实**：`02.08.04.18.01` 说明它是所有 setup 文件里最先要完成的那一个：

> The pin configuration file is the first setup file that must be completed before you can test a new device. If the pin configuration details have not been entered, the software will not let you enter details about the DUT in any other setup window.

**文档事实**：`02.08.01.01.02` 把本阶段的任务定义为「Define the relationship between resource pins and DUT board using the Pin configuration tool」，并列四件事：定义 device pin 到 tester resource 的连接、定义 site 数、给 device pin 分配通道、指定 DPS 工作范围；pin group / utility line / utility purpose 是可选步骤；最后 Apply。

**推断**：把以上几处合起来，本阶段实际要产出三样东西——(1) 一张 DUT pin ↔ 测试机通道 ↔ site ↔ 方向/模式的对应关系；(2) 可被 Level / Timing / Pattern 引用的 pin 名、pin group、port、utility 名；(3) 下载到硬件并保存成 `configuration/` 下的 setup 文件。三者缺一，后续阶段就会引用到不存在的名字。

## 前置条件

- **[[project]] 已完成**：device 目录必须存在，其中要有 `configuration` 子目录。`01.07.01.01.01` 的目录清单里明确列出 `configuration`；`02.08.04.18.04` 说 pin 配置文件就存放在 `<device_dir>/configuration`。
- **DUT 板走线与引脚表已确定**：`02.08.04.18.01.01` 说必须先决定 DUT board wiring 如何把测试机通道分给 DUT pin；`02.08.01.01.02` 要求「Define the connections between device pins to tester resources」。**推断**：因此 pin 名与通道号的划分必须以 DUT 引脚表和板级走线为输入，不能先写命令再看板子。
- **sequencer 必须是 OFF（`DFPN` 的硬前提）**：`02.06.03.02.08` 写明「before you can use the DFPN command the sequencer state must be OFF (see the SQST command)」。`CONF`（`02.06.03.02.02`）与 `UDEF`（`02.06.03.02.24`）的 `Errors` 也以 sequencer 处于 RUN/BREAK 为报错条件；`PALS` 的 `Errors` 同样要求不在 RUN/BREAK（`02.06.03.02.17`）。
- **没有测试在运行**：`02.06.03` 与 `02.06.03.01.01` 的 Note 都写明 firmware 不接受测试运行中的配置修改。
- **mode context 先建后用**：若省略 `CONF` 的 `context` 参数，设置落到 `DEFAULT`；其他 context 必须先用 `CTXT` 定义（`02.06.03.01.03.01`、`02.06.03.02.03`）。新 context 是当前 `DEFAULT` 的副本。
- **若用用户自定义默认电平，`DFLV` 必须先于 pin 配置**：`02.06.03.02.06` 写明「The command must be issued after the reset of the system by *RST - (ReSeT) and before pins are configured.」这是 D1 型顺序前置。**归属判定**见下文：`DFLV` 的电气内容属于 [[level]]，本页只取这条顺序规则。
- **多 site 的顺序**：`02.06.03.01.09` 给出三步——先做 site 1 的 pin 配置（site 1 由 `DFPN` 定义），再用 `PSTE` 定义 site 数，再用 `PALS` 给新 site 分配通道；其他配置数据与 site 1 共享。`02.06.03.02.17` 另写明「PALS must be used before any other setup command (including CONF).」
  - **推断**：`PSTE` 的 `Errors` 说「Not all pins at the site have had their channels assigned by the PALS command」会报错，这与 `PSTE` 先、`PALS` 后的顺序不矛盾——合理读法是 `PSTE` 先声明 site 数，`PALS` 补齐通道，检查发生在下发/使用时。文档没有把这句话讲透，实机顺序需验证。
- **跨卡 ganging 先由 `DDIC` 使能连接**：`DFPN`（`02.06.03.02.08`）与 `PALS`（`02.06.03.02.17`）都写明「Before cross-card ganging can be used, the connection must be enabled by command DDIC.」。同一 connectionSet 下的 trace 必须一致（`DFPN` 的 `connectionSet` 参数说明）。
- **`DFPS` 分配 DPS 通道时不要处于 connected 状态**：`02.06.03.02.09` 的 `Errors` 列出「You try to assign DPS channels in the connected state.」
- **建议**：先做一张 `pin name ↔ channel ↔ site ↔ 方向/模式 ↔ pin group/port` 分配表，再动手写配置。文档没有给这张表的模板；先分配再写命令，可以避开 `DFPN` 的 channel already allocated / pin already defined 这类中途返工。

## 涉及对象

下表是本阶段的主对象与层级；每条 L1 命令的完整覆盖见 L1 表。

| 对象 | 层级 | 在本阶段做什么 |
|---|---|---|
| `Pin Configuration tool` | gui | 编辑 pin 配置文件的主工具；含 Pin Settings、Groups、Ports、Alias Sets、Utility Purpose 等编辑器（`02.08.04.18.03`）。 |
| `pin configuration file` | file | `<device_dir>/configuration` 下的 `.cfg` 文件，正文是 firmware 命令（`02.08.04.18.04`）。 |
| `pin configuration master file` | file | 把 package 文件与若干 alias 文件组装成一份 pin 配置；由 Setup Management Tool 使用（`02.08.04.18.05`）。 |
| CSV import / export | file | 从 CSV 导入或导出 pin 配置表，便于跨平台交换与存档（`02.08.04.18.02.02`、`.02.03`）。 |
| `DFPN` / `DFPN?` | L1 | 给 digital 通道或 PMU 模式的 DC Scale 通道分配 pin 名；也用于 DC Scale ganging。 |
| `DFPS` / `DFPS?` | L1 | 给 DPS 通道分配 pin 名、极性与 pin number；也用于 DPS 模式 DC Scale 与 ganging。 |
| `CONF` / `CONF?` | L1 | 在指定 mode context 里设定 pin 类型与工作模式；查询现有设置。 |
| `CTXT` / `CTXT?` | L1 | 建立/删除用户自定义 mode context（新 context 是 DEFAULT 的副本）。 |
| `DFGP` / `DFGE` / `UDGP` | L1 | 定义固定 pin group / 表达式 pin group / 删除组定义。 |
| `DFPT` / `UDPT` | L1 / L1 子树外 | 定义与删除 port；port 可以当 pin group 使用。 |
| `DFUT` / `DFUP` / `UPST` / `UPAS` / `UTST` / `FLSH` | L1（`FLSH` 在子树外） | 定义 utility line / utility purpose，设置其状态；`FLSH` 把缓冲的 utility 设置真正下发。 |
| `PSTE` / `PALS` | L1 | 定义 site 数；为 site 2 及以后分配通道。 |
| `PACT` / `PQFC` / `PSFC` / `STME` | L1（`PSFC` 在子树外） | 多 site 的激活/mask、query focus、setup focus、site match 控制。 |
| `CHIN?` / `PFND?` / `GCTX?` / `HWTY?` / `*OPT?` | L1 | 回读通道、port/差分对、mode context、硬件类型与硬件选项。 |
| `PSSL` | L1 | 给 DPS power pin 与 DC signal (PMU) pin 设 force voltage / current clamp 安全限值。 |
| `PIN_UTILITY` / `PinUtility` | L2 | 在测试方法里展开 pin list / pin group，查询 pin 背后的硬件类型。 |
| `GET_CONFIGURED_SITES` | L2 | 读回 pin 配置里设置的 site 数与 site 号。 |
| `CCTsetContextPins` / `CCTgetContextPins` / `CCTRegisterDCPins` | L2 | 指定同步/独立 sequencer 上执行的 pins/ports；登记动态 DC 测试用的 pin/group。 |
| `GetUtilityLines` / `SetUtilityLines` | L2 | universal test method 中读取/设置 utility line 状态。 |
| `Pin_role` / `Protocol` | L2 | protocol assignment 在测试方法侧的模型类：pin role 是协议里的抽象硬件 pin 名，protocol 是传输规则集合。 |
| `DataManager`（`dm_config`） | L3 | 从程序里 load/merge/save/delete/查询 pin 配置 setup 文件。 |
| TPI site 族 | L3 | 读取/设置 site 数、可用/启用/激活 site、query focus 与 site 状态快照。 |
| `TestsuiteProxy` | L3 | Test Suite Control API 的测试套件代理；本阶段用其 site match 与 site focus 方法。 |
| HVM API | L3 | 外部控制 test program / device 下载；文档未提供 pin 配置专用 HVM 命令。 |
| SmartShell | L3（7.10.3 不存在） | 外部脚本接口；文档写明 `Introduced in SmarTest 8.2.5`，本 wiki 面向 7.10.3，不能当可用接口。 |

### 概念与走查文档覆盖（`02.06.03.01.*`）

这一组是命令参考里的概念/走查章，不是命令本身；本页把它们逐篇列出，避免只写主路径。

| 分类号 | 文档 | 一句话 |
|---|---|---|
| `02.06.03.01` | Concepts of Configuration setup | 本阶段概念章的索引，链到 Introduction、各类 pin、groups/ports、multi-site、Errors 与 Example。 |
| `02.06.03.01.01` | Introduction | 重申 pin 配置是测试准备第一步；按功能列出全部命令组；测试运行中不接受配置修改；指向示例文件。 |
| `02.06.03.01.02` | Assigning a pin name to a digital channel | 用 `DFPN` 给 digital 通道分配 pin 名；五位数通道号的含义；用 `UDEF` + `DFPN` + `CONF` 可换名并保留原 setup 数据（仅 waveform-set setup）。 |
| `02.06.03.01.03` | Configuring pin type and operating mode for a context | `DFPN` 之后必须用 `CONF` 配类型与工作模式；给出 PS1600/PS5000 支持的模式表；未指定 context 时落到 DEFAULT。 |
| `02.06.03.01.03.01` | Mode contexts | `DEFAULT` 由系统提供；`CTXT` 建的用户 context 是 DEFAULT 的副本；level/timing/vector 必须选同一个 context；可用 `GCTX?` 回读。 |
| `02.06.03.01.04` | Assigning a pin name to a digital or DC scale channel | DC Scale 通道按工作模式选命令：PMU 模式用 `DFPN`，DPS 模式用 `DFPS`；模式由命名命令决定，`CONF` 不能改；两者都可用 channel list 做 ganging。 |
| `02.06.03.01.05` | Defining a utility line | `DFUT` 给 utility line 分配名字与模式；通道号三段式；`UTST` 设状态、`FLSH` 下发；`UTTI` 设 settling time。 |
| `02.06.03.01.06` | Defining pin groups | 固定组用 `DFGP`，表达式组用 `DFGE`；组类型 I/O/DC/X 与 I/O/IO/DC；表达式支持 `+` `*` `-`；看成员要用 `DFGP?`，`DFGE?` 只返回表达式。 |
| `02.06.03.01.07` | Defining ports | Port 用 `DFPT` 建、`UDPT` 删；默认 port 是 `@`；port 不能与 pin/group 同名，不支持表达式定义，但可以当 pin group 用。 |
| `02.06.03.01.08` | Defining a utility purpose | `DFUP` 建 utility purpose；要先用 `UPST` 选中再 `FLSH` 才激活；`UDUP` 删除；`UPTI` 设 settling time；`UPAS` 管 site > 1。 |
| `02.06.03.01.09` | Configuring additional sites for multi-site testing | 三步：site 1 配置 → `PSTE` 定 site 数 → `PALS` 给新 site 分通道；其他配置与 site 1 共享；`PSTE? STR` 看实际可用 site。 |
| `02.06.03.01.10` | Controlling multiple test sites | 多 site 要能激活/mask site、控制后续 setup 命令影响哪些 site、控制 query focus；match loop 或共享模拟模块时还要配 site match。 |
| `02.06.03.01.10.01` | Activating and masking a site | `PACT` 激活或 mask site；mask 后 receiver 关闭、无结果；文档说明它是 tpi 接口的 firmware 实现。 |
| `02.06.03.01.10.02` | Setting the setup focus | `PSFC` 限定后续 setup 命令影响哪些 site；只有部分命令遵守 setup focus，vector setup 多数不遵守。 |
| `02.06.03.01.10.03` | Defining the query focus | `PQFC` 控制 query focus；默认是第一个可用 site，不一定是 site 1。 |
| `02.06.03.01.10.04` | Controlling the site match function | site match 控制同时/依次启动；match loop 需要 ON，共享触发通道需要 OFF；默认行为是 AUTO；>255 site 必须关 site match。 |
| `02.06.03.01.11` | Errors | 本阶段总错误条件：测试运行中、资源未安装、资源已被占用、系统无 DPS、sequencer 不在 OFF、resistive divider 超范围。 |
| `02.06.03.01.12` | Pin Configuration Example | 给出一份完整 pin 配置示例；示例里的 `--` 注释只为读者理解，真实 firmware 命令文件不能带注释。 |

### Pin Configuration Tool（GUI）文档覆盖（`02.08.04.18.*`）

这一章共 68 篇。按概念 / 使用流程 / 编辑器元素 / 文件四段逐篇列出；GUI 操作与 L1 命令的对应关系不在本页展开，留给 mapping 页。

#### 概念

| 分类号 | 文档 | 一句话 |
|---|---|---|
| `02.08.04.18` | Pin configuration tool | 本章入口，指向 Introduction、Using、Elements、Pin configuration file、Master file。 |
| `02.08.04.18.01` | Introduction of the Pin Configuration Tool | 说明 pin 配置文件是第一个必须完成的 setup 文件；未填则其他 setup 窗口不允许输入 DUT 细节。 |
| `02.08.04.18.01.01` | Pin | 要靠 DUT board wiring 决定通道到 DUT pin 的分配；可定义 DUT pin 与通道配置。 |
| `02.08.04.18.01.02` | Pin group | 把 pin 成组后可像单 pin 一样处理，压缩数据、便于读；地址总线是典型例子。 |
| `02.08.04.18.01.03` | Port | Port 是按独立时序/独立 sequencer 程序划分的 pin 组；默认 port 是全部 pin（`@`）。 |
| `02.08.04.18.01.04` | Alias set | 一个 pin 可有多个 alias，按核组织成 alias set；pin 配置文件、level/timing equation、master 文件、setup API 文件、test method 源文件都支持 alias。 |
| `02.08.04.18.01.05` | Utility purpose | 一组 utility line 加其 setting（0/1/X）；与单条 utility line 的区别是带整组 setting，多 site 时可为每 site 不同。 |

#### 使用流程

| 分类号 | 文档 | 一句话 |
|---|---|---|
| `02.08.04.18.02` | Using the Pin Configuration Tool | 使用流程的索引，链到打开编辑器、CSV 导入/导出、Revert、Apply、保存、pin/group/port/utility purpose 编辑、DC Scale 限值。 |
| `02.08.04.18.02.01` | Opening the setup editor | 在 setup perspective 的 Test Program Explorer 中双击 setup component 打开 Pin Setting / Core Allocation / DPS Channel Mode / Utility Purpose 编辑器。 |
| `02.08.04.18.02.02` | Importing the pin configuration from a CSV file | 从 CSV 导入 pin 配置；前提是 CSV 存在且已载入一个空的 pin 配置文件。 |
| `02.08.04.18.02.03` | Exporting the pin configuration to a CSV file | 把 pin 配置导出到 CSV，用于报告与文档化；前提是已载入 pin 配置文件。 |
| `02.08.04.18.02.04` | Discarding the changes in the pin configuration tool | 用 File > Revert 或右键 Revert 丢弃尚未 Apply 的修改；若 Apply 失败，Revert 会被禁用。 |
| `02.08.04.18.02.05` | Applying pin configuration data | 与其他 setup 窗口不同，pin 配置用 Apply 下载；组件用 Apply，整份文件用 Apply All；文档说只有应用 pin setting 数据或整份 pin 配置文件时才弹 Confirm Apply。 |
| `02.08.04.18.02.06` | Saving a modified pin configuration | 改 pin 配置后先 Apply、保存 pin 配置，再重新载入其他 setup；文档用 CAUTION 禁止改完立即保存其他 setup。 |
| `02.08.04.18.02.07` | Working with pins | pin 编辑子任务的索引：virtual pin、编辑 pin、定义 context、定义 additional sites、复制/粘贴、删除、DPS 外部触发。 |
| `02.08.04.18.02.07.01` | Virtual pins | Virtual pin 无 pogo 连接，用于记录未直连 pin 的结果；名字最长 64 字符；配置变更事件写入 data log。 |
| `02.08.04.18.02.07.02` | Editing the pin configuration | 在 Pin Setting editor 按 spec sheet 逐 pin 输入；最后 Apply 并保存 pin 配置文件。 |
| `02.08.04.18.02.07.03` | Defining a context | 右键 Pin Setting > Add Context，选一个已有 context 作基础，输入新 context 名；结果在 Context list 出现新名字。 |
| `02.08.04.18.02.07.04` | Defining additional test sites | 先完成 site 1，再右键 Pin Settings > Define Site，输入 site 总数，逐 site 分配通道，最后 Apply + 保存。 |
| `02.08.04.18.02.07.05` | Copying and pasting a pin | 复制一行 pin 配置再粘贴，pin 名自动变成 `CopyOf_<原名>`。 |
| `02.08.04.18.02.07.06` | Deleting a pin | 选中 pin 行按 Delete，确认后从 Pin Setting editor 删除。 |
| `02.08.04.18.02.07.07` | Defining external triggers for DPS measurements | 若要用外部触发做 DPS 电流测量，先在 Digital Pins editor 建一个 dummy pin（如 `ext_trig`，type `i`，填预分配通道），再向它施加 vector 作为触发。 |
| `02.08.04.18.02.08` | Working with pin groups | group 的创建、编辑固定组、编辑表达式组、复制/粘贴、删除的索引。 |
| `02.08.04.18.02.08.01` | Creating a pin group | 右键 Groups > New，选 Fixed Group 或 Expression Based Group，输入组名。 |
| `02.08.04.18.02.08.02` | Editing a fixed group | 从 Available Pin List 加成员；不选 Mixed Group 时，混合类型会按类型拆成同名多组。 |
| `02.08.04.18.02.08.03` | Editing an expression-based group | 三步：定义 group expression、选 component type、求值；成员可含 pin、group、pin alias。 |
| `02.08.04.18.02.08.04` | Copying and pasting a group | 以已有 group 为起点复制出新 group。 |
| `02.08.04.18.02.08.05` | Deleting a group | 删除 group；若被表达式组引用，那些组会重新求值。 |
| `02.08.04.18.02.09` | Working with ports | port 创建、编辑、复制/粘贴、删除的索引；操作与 group 类似。 |
| `02.08.04.18.02.09.01` | Creating a port | 右键 Ports > New，输入 port 名。 |
| `02.08.04.18.02.09.02` | Editing a port | 用 Add > / Add All >> / < Remove / << Remove All 管理 Port Members；可用 filter line 找 pin。 |
| `02.08.04.18.02.09.03` | Copying and pasting a port | 以已有 port 为起点复制出新 port。 |
| `02.08.04.18.02.09.04` | Deleting a port | 删除 port；若被表达式组引用，那些组会重新求值。 |
| `02.08.04.18.02.10` | Working with utility purposes | utility purpose 创建、编辑、复制/粘贴、删除的索引。 |
| `02.08.04.18.02.10.01` | Creating a utility purpose | 右键 Utility Purpose > New，输入名字。 |
| `02.08.04.18.02.10.02` | Editing a utility purpose | 从 Utility Lines 区加成员，并设置每 site 的状态（1/0/X）与 settling time。 |
| `02.08.04.18.02.10.03` | Copying and pasting a utility purpose | 以已有 utility purpose 为起点复制出新的一项。 |
| `02.08.04.18.02.10.04` | Deleting a utility purpose | 删除 utility purpose。 |
| `02.08.04.18.02.11` | Setting DC Scale voltage and current limits | 在 DC Scale Limits 编辑器设 Max/Min Volt、Max Source/Sink；超限会报错；前提是已定义所需 pin 与 DC Scale 卡。 |

#### 编辑器元素

| 分类号 | 文档 | 一句话 |
|---|---|---|
| `02.08.04.18.03` | Elements of the Pin Configuration Tool | 层级视图与各编辑器功能总表（Pin Settings、Groups、Ports、Alias Sets、Utility Purpose 等）。 |
| `02.08.04.18.03.01` | Pin setting editors | 五类 pin setting editor（Digital、DPS、Utility、Utility Purpose、Virtual）；多 site 时显示所有 site 的 tester channel。 |
| `02.08.04.18.03.01.01` | Context list | Digital Pins editor 的 context 下拉；最多 10 个 context；DEFAULT 选中时 pin 自动成为 standard / `std`；level/timing/vector 必须用同一 context。 |
| `02.08.04.18.03.01.02` | Digital Pins editor | 配置 digital pin 与 PMU 模式 DC Scale pin；列 Name/No/Type/Mode/Tester Channel/HW/Connection Set。 |
| `02.08.04.18.03.01.03` | DPS Pins editor | 配置 DPS 模式 pin（含 DC Scale）的参数表。 |
| `02.08.04.18.03.01.03.01` | DC Scale pin (DPS mode) setup | DPS 模式下 DC Scale pin 的字段：Name、Pol（必须 POS）、C[uF]、HW 等。 |
| `02.08.04.18.03.01.03.02` | Load capacitance connected to the DC Scale DPS128/DPS64 | 按 DUT board 负载电容自动选 performance range；PMU 模式还可在硬件视图或 `SPMU_PIN_TASK.loadCap()` 设置。 |
| `02.08.04.18.03.01.03.03` | Load capacitance connected to the DC Scale XPS256 | 同理按负载电容自动选范围；最大电容受所选电流范围限制，SmarTest 会自动限制。 |
| `02.08.04.18.03.01.04` | Utility Pins editor | 给 utility pogo pin 分配名字与 mode（w/r 等）；可用 `GetUtilityLines` / `SetUtilityLines` 或 test method 访问。 |
| `02.08.04.18.03.01.05` | Utility Purpose Editor | 选择 utility line 成员，显示各 site 状态 1/0/X 与 settling time。 |
| `02.08.04.18.03.01.06` | Virtual Pins editor | 定义 virtual pin 名；可用于 `SMC_TEST()`、`TESTSET().judgeAndLog_ParametricTest()`、`TESTSET().judgeAndLog_ScanTest()` 记录结果。 |
| `02.08.04.18.03.02` | Pin group editor | 选择 fixed / expression-based group 的成员。 |
| `02.08.04.18.03.02.01` | Rules for defining groups | 固定组最多 2400 个；所有组 pin 总数上限 1,228,800；组名不能与已有 digital pin/group 重名。 |
| `02.08.04.18.03.02.02` | Incompatible pin groups | timing 不接受混合 I/O 或不同操作模式；level 不接受 o 与 io 混合；vector 只能全 i / 全 o / 全 io。 |
| `02.08.04.18.03.03` | Port Editor | 选 port 成员；port 不能与 pin/group 同名；不支持表达式 port；port 可当 pin group 用。 |
| `02.08.04.18.03.04` | Alias Set Editor | 查看/创建/编辑/复制/粘贴/删除 alias set（package pin name + pin alias）。 |
| `02.08.04.18.03.05` | DC Scale Extensions editor | 配置 DC Scale 卡升级 license 特性（文档说当前仅 XPS256 有此需求）；设置存入 pin 配置文件，可用 TAT 导出到 device license file。 |
| `02.08.04.18.03.06` | DC Scale Limits editor | 每 pin 的 Max/Min Volt、Max/Min Source 限值；仅对 DC Scale 卡生效。 |
| `02.08.04.18.03.07` | DC Scale Regulation editor | 设电压/电流 filter、slew、Cap、LoadStep 等全局默认；只能在 disconnected 状态应用。 |
| `02.08.04.18.03.08` | DC Scale Safety editor | 设 max/warn Vdrop、Vdrop hold time、是否 Vdrop 时断开等全局安全默认。 |
| `02.08.04.18.03.09` | Ground sense editor | 使用 Pin Scale 5000 时按 site 配置 ground sense pogo（文档标注 Introduced in SmarTest 7.10.3）。 |
| `02.08.04.18.03.10` | Protocol assignments | 把 port / pin group 赋给 protocol，把 resource (hardware) pin 赋给 pin role。 |
| `02.08.04.18.03.10.01` | Assigning pin roles and protocols | 在 Protocol Assignment 区选 port 与 protocol，把协议的 pin role 连到 V93000 的 resource pin；前提是 port 与 pin role 已定义。 |
| `02.08.04.18.03.11` | Apply button | 快捷菜单里的 Apply，把编辑器中的 pin 配置数据下载到硬件。 |
| `02.08.04.18.03.12` | State indicator | 方块在 setup component 名前，表示组件内容与硬件一致 / 不一致（需 Apply）；星号在 component 名后，表示 pin 配置文件与硬件数据不一致。 |
| `02.08.04.18.03.13` | Filter line | Pin Setting / Group / Port / Utility Purpose 编辑器里的过滤行，支持正则表达式。 |
| `02.08.04.18.03.14` | Sorting rows | 点列头可对 Pin Setting / Group / Port 编辑器的行排序。 |

#### 文件

| 分类号 | 文档 | 一句话 |
|---|---|---|
| `02.08.04.18.04` | Pin configuration file | 文件位于 `<device_dir>/configuration`，正文是与 GUI 参数一一对应的 firmware 命令；也可以用文本编辑器直接写。 |
| `02.08.04.18.05` | Pin configuration master file | 单文件或 master 文件组装；master 文件引用 package 文件与 alias 文件，Setup Management Tool 负责组装与校验。 |

### 归属判定

这一节是判断，不是文档事实，供维护者复核。

- **`DFLV` 判给 [[level]]，但仍在 L1 表里列出**。它确实在 `02.06.03.02` 子树内（`.02.06`），但内容全是 VIL/VIH/VOL/VOH/VT 等默认电平；命令清单按 firmware 功能分组，不按 stage 分组。本页只取它的一条顺序规则（`*RST` 之后、pin 配置之前）放进前置条件。**理由**：如果把 `DFLV` 当 pin 命令展开，读者会以为电平默认值在这里设置。
- **`DSCP` 判给 [[project]]，但仍在 L1 表里列出**。它在同一子树内（`.02.13`），定义的是 sequencer memory 里各类参数集的最大实例数；「Every call of DSCP deletes all data that were previously contained in the Sequencer Memory.」它与 pin 配置的相似之处只是同处一章。
- **`PRLT?` 判给 [[results]] / [[run]]**。它返回上一次测试的全局 pass/fail，属于结果读取；列在本页只是因为它在 `02.06.03.02` 子树内。
- **`PACT` / `PQFC` / `PSTE` / `PALS` / `STME` 的 site 控制部分判给 [[run]] / [[testflow]]**。本页承担的是 site 数与通道分配这一半；激活/mask、focus、match 的执行语义在运行与 testflow 阶段。它们仍在 L1 表里完整列出。
- **`PSSL` 与 GUI 的 DC Scale Limits / Regulation / Safety 编辑器**：`PSSL` 在 pin 子树内，按覆盖要求列在 L1；但限值/供电安全更靠近 [[level]] 的 DPS 电平配置。GUI 的三个 DC Scale 编辑器也列在覆盖表里，本页不展开其电气语义。
- **`*IDN?` / `*OPT?` / `HWTY?` / `CHIN?`** 是横切的识别与硬件查询命令，列在本页是因为它们在 pin 子树内；不要据此认为 pin 配置本身需要它们。
- **子树外但本章点名的命令**（`DFPR` / `UDPR` / `UDPT` / `PSFC` / `FLSH` / `SQST` / `DDIC` / `RLYC`）单独列在下文子树外表，不计入 `02.06.03.02` 的 38 条覆盖数。**理由**：它们在 `02.06.03` 正文的分组清单里出现，属于本阶段会用到的邻接命令，但不是 `--list 02.06.03.02` 的成员。
- **`dm_attrib` / `dm_catr` 不是本阶段的 `dm_config`**。`DataManager` 的 `Fid` 表把 `dm_config` 描述为 pin configuration setup，而 `dm_attrib` 是 pin attribute setup、`dm_catr` 是 channel attributes（`02.09.01.09.02`）。**同形陷阱**：不要拿 `dm_attrib` 当 pin 配置文件的加载入口。

## L1 — Firmware / Setup Command

**覆盖范围**：`show.py --list 02.06.03.02` 返回 38 条，其中 `02.06.03.02` 本身是 `List of configuration commands` 索引，其余 37 条是命令文档。下表按分类号顺序逐条列出，**不代表推荐执行顺序**。每条都写命令 + 一句作用 + 出处。

| 分类号 | 命令 | 作用 | 出处 |
|---|---|---|---|
| `02.06.03.02` | List of configuration commands | 配置命令清单的索引；按 digital / context / DPS / DC Scale / utility / groups / alias / multi-site 分组，本身无语法。 | `02.06.03.02` |
| `02.06.03.02.01` | `CHIN?` | 查询指定通道或全部通道的类型、物理位置、板号与通道信息，按每个 pin 返回。 | `02.06.03.02.01` |
| `02.06.03.02.02` | `CONF` / `CONF?` | 在指定 mode context 中给 pin 设定类型与工作模式；`CONF?` 回读现有设置。 | `02.06.03.02.02` |
| `02.06.03.02.03` | `CTXT` / `CTXT?` | 定义或删除 mode context 名；新 context 是当前 DEFAULT 的副本。 | `02.06.03.02.03` |
| `02.06.03.02.04` | `DFGE` / `DFGE?` | 用 `+` / `*` / `-` 集合表达式定义表达式型 pin group；`DFGE?` 返回组类型与表达式。 | `02.06.03.02.04` |
| `02.06.03.02.05` | `DFGP` / `DFGP?` | 定义固定数字 pin group；重复用同名会把新 pin 追加到原组；`DFGP?` 返回成员与类型。 | `02.06.03.02.05` |
| `02.06.03.02.06` | `DFLV` / `DFLV?` | 设定用户默认电平（VIL/VIH/VOL/VOH/VT 等）；必须在 `*RST` 后、pin 配置前；内容归 [[level]]。 | `02.06.03.02.06` |
| `02.06.03.02.07` | `DFPC` / `DFPC?` | 给已由 `DFPN` 定义的 pin 加注释；`DFPC?` 回读一个或多个 pin 的注释。 | `02.06.03.02.07` |
| `02.06.03.02.08` | `DFPN` / `DFPN?` | 给 digital 通道或 DC Scale 通道分配 pin 名（DC Scale 进入 PMU 模式）；也支持 DC Scale ganging；sequencer 必须 OFF。 | `02.06.03.02.08` |
| `02.06.03.02.09` | `DFPS` / `DFPS?` | 告诉软件哪个 DPS 通道接到哪个 pin、极性是什么；也用于 DPS 模式 DC Scale 与 ganging。 | `02.06.03.02.09` |
| `02.06.03.02.10` | `DFPT` / `DFPT?` | 定义 port；重复用同名会追加 pin；`DFPT?` 查一个或全部 port 定义。 | `02.06.03.02.10` |
| `02.06.03.02.11` | `DFUP` / `DFUP?` | 定义 utility purpose（一组 utility line + 每条线的标准输出状态）；状态需 `UPST` + `FLSH` 激活。 | `02.06.03.02.11` |
| `02.06.03.02.12` | `DFUT` / `DFUT?` | 给 utility line 定义符号名与操作模式；`UTST` 用这个名字设/读状态。 | `02.06.03.02.12` |
| `02.06.03.02.13` | `DSCP` / `DSCP?` | 定义各类参数集最大实例数并预留 sequencer memory；每次调用清空 sequencer memory；文档说它取代旧的 `CNTR` / `CNTR?`；归 [[project]]。 | `02.06.03.02.13` |
| `02.06.03.02.14` | `GCTX?` | 查询指定 setup component（TIM/LEV/WAVE/LBL/SPCF/CURR）或当前生效的 mode context。 | `02.06.03.02.14` |
| `02.06.03.02.15` | `HWTY?` | 显示硬件属性：machine、testhead、dut_if。 | `02.06.03.02.15` |
| `02.06.03.02.16` | `PACT` / `PACT?` | 激活或 mask site；每次执行都会重置所有 site 的结果；文档说它是 tpi 接口的 firmware 实现，建议用 tpi 调用。 | `02.06.03.02.16` |
| `02.06.03.02.17` | `PALS` / `PALS?` | 定义 site > 1 的 pin 通道；site 1 由 `DFPN` 定义；必须先于其他 setup 命令（含 `CONF`）。 | `02.06.03.02.17` |
| `02.06.03.02.18` | `PFND?` | 反查包含指定 pin 的 port，或差分对中的另一端。 | `02.06.03.02.18` |
| `02.06.03.02.19` | `PQFC` / `PQFC?` | 设定哪个 site 拥有 query focus；文档说它是 tpi 接口的 firmware 实现。 | `02.06.03.02.19` |
| `02.06.03.02.20` | `PRLT?` | 并行返回指定 site 上一次测试的全局 pass/fail；结果会被 `CSAS` / `PSAS` 作废，建议紧跟功能测试。 | `02.06.03.02.20` |
| `02.06.03.02.21` | `PSSL` / `PSSL?` | 给 DPS power pin 与 DC signal (PMU) pin 设 force voltage 与两个 current clamp 的安全限值；默认 OFF。 | `02.06.03.02.21` |
| `02.06.03.02.22` | `PSTE` / `PSTE?` | 定义 pin 配置里要配多少个 site（最大 1024）；`PSTE? STR` 返回哪些 site 实际可用；文档说它不支持 HV 模式的 pin。 | `02.06.03.02.22` |
| `02.06.03.02.23` | `STME` / `STME?` | 设定 site match：ON 依次启动、OFF 同时启动、AUTO 检查共享通道、FAST 启用 Fast Sync；默认 AUTO；只配一个 site 时命令不做事。 | `02.06.03.02.23` |
| `02.06.03.02.24` | `UDEF` | 从当前配置移除已定义 pin；sequencer 不得在 run/break。 | `02.06.03.02.24` |
| `02.06.03.02.25` | `UDGP` | 拆掉 `DFGP` 或 `DFGE` 定义的 group。 | `02.06.03.02.25` |
| `02.06.03.02.26` | `UDPS` | 移除 `DFPS` 定义的 DPS pin，并解除 gang（master/slave）配置。 | `02.06.03.02.26` |
| `02.06.03.02.27` | `UDUP` | 删除一个或多个 utility purpose 名；未定义会报错。 | `02.06.03.02.27` |
| `02.06.03.02.28` | `UDUT` | 删除 utility line 名，并把写 utility line 的输出置 0。 | `02.06.03.02.28` |
| `02.06.03.02.29` | `UDVP` | 删除 `VPIN` 定义的 virtual pin 或 virtual pin 列表。 | `02.06.03.02.29` |
| `02.06.03.02.30` | `UPAS` / `UPAS?` | 为 site > 1 给同一 utility purpose 分配不同的标准输出状态；需先 `DFUP`。 | `02.06.03.02.30` |
| `02.06.03.02.31` | `UPST` / `UPST?` | 设定 utility purpose 内 utility line 的输出（desired）状态；之后必须 `FLSH`。 | `02.06.03.02.31` |
| `02.06.03.02.32` | `UPTI` / `UPTI?` | 设定 utility purpose 的 settling time；`WSDN` 使用；默认 0 ms。 | `02.06.03.02.32` |
| `02.06.03.02.33` | `UTST` / `UTST?` | 设定或读取 utility line 的输出状态；需 `DFUT` 定义，之后必须 `FLSH`。 | `02.06.03.02.33` |
| `02.06.03.02.34` | `UTTI` / `UTTI?` | 设定单条 utility line 的 settling time；并行切换时取最长值；默认 0 ms。 | `02.06.03.02.34` |
| `02.06.03.02.35` | `VPIN` / `VPIN?` | 给 virtual pin 分配名字；不接 pogo，可用来记录测试结果；不能加入 port 或 group。 | `02.06.03.02.35` |
| `02.06.03.02.36` | `*IDN?` | 显示当前型号、firmware revision 与 revision date。 | `02.06.03.02.36` |
| `02.06.03.02.37` | `*OPT?` | 读取已安装硬件选项（控制板、时钟板、通道卡、模拟卡、DPS 卡）与每通道的 SM/VM 深度等信息。 | `02.06.03.02.37` |

### 最小可用示例

以下示例逐字取自文档的 Example 段。

**digital pin 绑定与回读**（`02.06.03.02.08`）：

```
> DFPN 10101,"1",(Clock)
> DFPN 10102,"2",(D0)
> DFPN? (@)
```

**DC Scale ganging（PMU 模式）**（`02.06.03.02.08`）：

```
DFPN (11901, 11902),,(vee)
```

**DPS pin**（`02.06.03.02.09`）：

```
DFPS 11,POS,(Vee)
```

**pin type 与工作模式**（`02.06.03.02.02`）：

```
> CONF IO,F160,(D0,D1)
```

**固定组与表达式组**（`02.06.03.01.06`）：

```
> DFGP X,(SI1,SI2,SO1,SO2),(SCAN)
> DFGP O,(O1,SO1,SO2),(OUT)
> DFGE O,"SCAN * OUT",(SCAN_OUT)
> DFGE? (SCAN_OUT)
< DFGE O,"SCAN * OUT",(SCAN_OUT)
> DFGP? (SCAN_OUT)
< DFGP O,(SO1,SO2),(SCAN_OUT)
```

文档特别说明：要看表达式组的成员 pin 必须用 `DFGP?`，`DFGE?` 只返回定义表达式。

**port**（`02.08.04.18.04` 的 multi-port 示例，节选两行）：

```
DFPT (CP_1,DS7_1,DS0_1,I/O7_1,I/O6_1,I/O5_1,I/O4_1,I/O3_1,I/O2_1,
I/O1_1,IO0_1,Q7_1,Q0_1,S1_1,S0_1,_MR_1), (port_1)
DFPT (CP_2,DS7_2,DS0_2,I/O7_2,I/O6_2,I/O5_2,I/O4_2,I/O3_2,I/O2_2,
I/O1_2,I/O0_2,Q7_2,Q0_2,S1_2,S0_2,_MR_2), (port_2)
```

**utility purpose 与状态激活**（`02.06.03.02.11`）：

```
> DFUP (16501,16502,16503,16504),"0110",(AWG_CNCT)
> UPST ,(AWG_CNCT)
> FLSH
> UPST? (AWG_CNCT)
< UPST "0110",(AWG_CNCT)
```

**多 site**（`02.06.03.02.22`、`02.06.03.02.17`）：

```
> PSTE 3
```

```
> PSTE? STR
< PSTE "101"
```

```
PALS 2,10201,,(Clock)
PALS 2,10202,,(D0)
```

**site match**（`02.06.03.02.23`）：

```
> STME AUTO,
> STME?
< STME ON,
```

**site 激活/mask**（`02.06.03.02.16`）：

```
> PACT ACTIVE, 1
> PACT MASKED, 2
> PACT MASKED, 3
```

**完整配置文件示例**见 `02.06.03.01.12`；该页明说示例里的 `--` 注释只是为了读者理解，「it is not possible to include comments in your firmware command files!」。`02.08.04.18.04` 另给出 `hp93000,config,0.1` 开头的实际文件样例，并说明「You can use a text editor instead of the Pin Configuration Tool to create or edit a pin configuration file in the form of a set of firmware commands.」

### 子树外但本章点名的命令

`02.06.03` 的分组清单里还出现以下命令；它们不在 `02.06.03.02` 子树内，单独列出以免读者在本页找不到入口。

| 命令 | 作用 | 出处 |
|---|---|---|
| `DFPR` / `DFPR?` | 定义 pin alias set 以及 pin alias 与 package pin name 的关系；`DFPR?` 回读。 | `02.06.02.02.64` |
| `UDPR` | 删除 pin alias 定义。 | `02.06.02.02.297` |
| `UDPT` | 删除已定义的 port。 | `02.06.02.02.299` |
| `PSFC` / `PSFC?` | 设定 setup focus，限定后续 setup 命令影响哪些 site。 | `02.06.02.02.191` |
| `FLSH` | 把缓冲的 utility 命令（`UPST` / `UPTI` / `UTST` / `UTTI`）真正下发到硬件。 | `02.06.02.02.124` |
| `SQST` / `SQST?` | 控制/查询 sequencer 状态；`DFPN` 等命令要求它为 OFF。 | `02.06.02.02.241` |
| `DDIC` / `DDIC?` | 描述跨 DC Scale 卡 ganging 所需的 DUT board trace；跨卡 ganging 前必须先使能。 | `02.06.02.02.54` |
| `RLYC` / `RLYC?` | 控制 DUT pin 到测试机资源的 relay；`UDEF` / `CONF` 会打开 relay，需要 `RLYC` 重新闭合。 | `02.06.02.02.206` |

### L1 内记录的文档矛盾

1. **`DFPN` / `DDIC` 的 `connectionSet` 参数**。两篇的参数表都先写「This parameter is currently not used.」，随后又写「This extra string parameter adds the ability to define several pins containing the same DC Scale channel in PMU mode.」并说明同一 connectionSet 下的 trace 必须一致。这是同一篇文档内部的前后不一致，**不自行选一个当正确答案**；实际用法需按后一段的说明并实机确认。
2. **group 内 pin 总数上限**。`02.08.04.18.03.02.01` 写「The maximum number of pins in all groups is 1,228,800.」；`DFGE` / `DFGP` 的 `Errors` 段写「There are too many pins in the group (max. number of pins in all groups is 1843200).」两个数字并列记录，不判断哪个对。

## L2 — Test Method API

**文档事实（边界）**：pin 配置本身不在测试方法里创建。`02.07.04.01.147` 开头写明：

> When creating a device test, all pins to be tested are defined using the Pin Configuration tool.

**本次未找到**任何可以在 C++ 测试方法里创建、修改 pin 配置或写回 pin 配置文件的 API。测试方法侧找到的是消费 pin 配置的接口：

- **`PIN_UTILITY` / `PinUtility`**（`02.07.04.01.147`）。头文件 `/opt/hp93000/soc/prod_com/include/MAPI/PinUtility.h`；类没有 public constructor，只能用系统准备好的 `PinUtility` 对象。成员函数：
  - `expandDigitalPinNamesFromPinList()` — 把 pin list 中指定类型的 pin 名转成 `STRING_VECTOR`，pin group 名会被展开；文档说它只为向下兼容保留，新应用用 `getDigitalPinNamesFromPinList()`。
  - `getDigitalPinNamesFromPinList()` — 同上，并可选择缺 pin / 类型不匹配时报错，以及按字母序或组定义序排序。
  - `getDpsPinNamesFromPinList()` — 把 DPS pin 名列表转成 `STRING_VECTOR`。
  - `getPinType()` — 查询 pin 背后的硬件能力（示例返回 `PS1600`、`DCS-DPS128HC`、`DCS-VI32` 等）。
  - `getSharedDigitalPins()` — 返回在多个 site 间共享的 digital pin。
  - `getSharedDpsPins()` — 返回在多个 site 间共享的 DPS pin。
  - `createPinListFromPinNames()` — 把 `STRING_VECTOR` 拼回逗号分隔的 pin list 字符串。

  文档给的最小用法：

```
STRING pinList = "pin1,pin2,pin3";
STRING_VECTOR pinNameList;
pinNameList = PinUtility.getDigitalPinNamesFromPinList(pinList, TM::IO_PIN, TRUE,TRUE);
```

- **`GET_CONFIGURED_SITES`**（`02.07.04.01.81`）：返回 pin 配置里设置的 site 数，并把 site 号写进 `ARRAY_I&`；头文件 `/opt/hp93000/soc/prod_com/include/MAPI/SiteControl.h`。文档用例：配了 site 1–4 时返回 4。
- **`CCTsetContextPins` / `CCTgetContextPins`**（`02.07.04.01.14.32` / `.14.08`）：设置/读取在同步或独立 sequencer 上执行的 pins 与 ports；头文件 `/opt/hp93000/soc/testmethod/include/CCTestMethod.hpp`。
- **`CCTRegisterDCPins`**（`02.07.04.01.14.27`）：登记动态（sequencer 控制的）DC 测试要用的 pin 或 pin group，参数可为 Smart Scale 或 DC Scale pin；文档说通常放在 `init()` 里。
- **`GetUtilityLines` / `SetUtilityLines`**（`02.07.05.04.05` / `.07`）：universal test method 中读取/设置最多 512 条 utility line 的状态；`SetUtilityLines` 可用 utility line 名或 utility purpose 名。
- **`Pin_role` / `Protocol`**（`02.07.11.01.09.08` / `.10`）：protocol assignment 的测试方法侧模型。文档说 pin role 是协议定义里用的抽象接口（硬件）pin 名，physical device pin 在 protocol assignment 里赋给 pin role；transactions 里只用 pin role，不用 physical pin name。

**推断**：L2 与 L1 的分工是：pin 配置建名字空间，测试方法按名字取用。因此测试方法里出现 pin 名写错时，根因往往在本阶段，而不是测试方法本身。

## L3 — 外部控制

**L3 入口是横切的，能力面按阶段分族。** 横切入口是 `Test Suite Control API`（`02.09.01.14`）、`TPI Program Routines`（`02.09.01.09`）与 `HVM API`（`02.09.01.10`）；本阶段的专属族是 TPI 的 `dm_config` 与 site 状态族、Test Suite Control API 的 site 方法、HVM 的 test program / device 下载。

**文档事实（Test Suite Control API 的边界）**：`02.09.01.14` 写明：

> Test suite control API is used to directly control the test suites outside of the testflow tool. Only UTM-based test suites are supported with these APIs.

并写明：

> They cannot be used in test method programming and also cannot be used in parallel with HVM API and BLC API by the same client process.

### TPI 的 `dm_config` 文件族

`02.09.01.09.02` 的 `Fid` 表把 `dm_config` 描述为「pin configuration setup」。同页 `Opc` 表给出可用操作：`dm_load`（replace current setup by file）、`dm_merge`（merge a file (add additional pins)）、`dm_save`（save current setup to file）、`dm_delete`（delete file）、`dm_utd`（return up to date status for the file specified by Fid）。**文档事实**：pin 配置被列为 `DataManager` 的一个文件类型。**推断**：因此它在 L3 上可按 setup 文件整体 load/save/merge，而不是逐条 pin 命令的远程封装。

**同形陷阱**：`dm_attrib`（pin attribute setup）与 `dm_catr`（channel attributes）不是 `dm_config`；不要拿它们当 pin 配置文件的入口（`02.09.01.09.02`）。

### TPI 的 site 状态族

以下例程都在 `02.09.01.09` 的 TPI Program Routines 索引下：

- `GetNumberOfSites`（`.09.13`）— 读当前配置的 site 数。
- `GetAvailableSites`（`.09.06`）— 读可用 site 集合；可用 = 已配置 site 中扣除硬件缺陷后能用的那些。
- `GetActiveSites`（`.09.05`）— 读激活 site 集合；激活 site 会被测试并评估结果，去激活 site 仍测试但结果被忽略。
- `GetEnabledSites`（`.09.08`）— 读启用 site 集合；启用 site 在下一次 test routine 初始化时连接。
- `GetSiteInFocus`（`.09.14`）— 读当前 query focus 的 site 号。
- `GetSiteState`（`.09.15`）— 读 focus / enabled / active 三者的状态快照（`MS_SITE_STATE`）。
- `RestoreSiteState`（`.09.25`）— 恢复 `GetSiteState` 保存的状态；前后 site 数不一致会报错。
- `SetActiveSites`（`.09.26`）— 激活/去激活 site；文档说只在 test method 执行上下文内有效。
- `SetEnabledSites`（`.09.27`）— 启用/禁用 site；同样只在 test method 执行上下文内有效。
- `SetSiteInFocus`（`.09.29`）— 设置 query focus；无效 site 号时 focus 不变。

**推断**：这套 site 族与 L1 的 `PSTE` / `PALS` / `PACT` / `PQFC` 是同一组 site 概念在不同层的入口；文档没有逐条声明它们等价，因此不能据此认为可互换。

另外，`ChangeDevice`（`.09.01`）按 device path/name 切换当前 device；**推断**：切换 device 会连带改变 pin 配置的上下文，但文档没有在 `ChangeDevice` 页直接说它加载 `dm_config`，需实机核对。`02.09.01.15.04.01` 把 `HpInit()`、`ChangeDevice()`、`DataManager()` 列为 TPI library 的代表函数。

### Test Suite Control API

`02.09.01.14.02.01` 的 `TestsuiteProxy` 成员中与本阶段相关的是：

- `setSiteMatch()` / `getSiteMatch()`（`.02.01.30` / `.02.01.10`）— 设置/读取 test suite 的 site match 值；取值域是 `SITEMATCH_OFF` / `SITEMATCH_ON` / `SITEMATCH_AUTO` / `SITEMATCH_UNDEFINED`。
- `setSiteInFocus()` / `getSiteInFocus()`（`.02.12` / `.02.13`）— 设置/读取聚焦 site；若 site 尚未激活，`setSiteInFocus` 会先激活它。
- `setActiveSites()` / `getActiveSites()`（`.02.14` / `.02.15`）— 设置/读取 active site 集合；若 site 未启用，`setActiveSites` 会先启用它。

**推断**：`setSiteMatch()` 与 `02.06.03.01.10.04` 描述的 Site Match test suite flag 取值域一致；但文档没有直接声明 L1 的 `STME` 与 L3 的 `setSiteMatch()` 可以互替，**不能据此认定等价**。

### HVM API

`02.09.01.10.01` 把 HVM API 分为 SmarTest Session Management、Test Execution、Hardware Information、Calibration and Diagnostic 四类。与本阶段沾边的是 Test Execution API：

- `DownloadTestprogram`（`02.09.01.10.03.02.02.20`）— 下载 test program，文档说下载内容包括 test flow、setup files 与其他组件；下载期间会多次发出 `SETUPFILE_DOWNLOAD_STARTED` / `SETUPFILE_DOWNLOAD_COMPLETED` 事件。
- `ChangeDevice`（`...02.12`）— 设置 SmarTest session 的目标 device；开始/完成时发 `DEVICE_CHANGE_STARTED` / `DEVICE_CHANGE_COMPLETED`。
- `SETUPFILE_DOWNLOAD_STARTED` / `SETUPFILE_DOWNLOAD_COMPLETED`（`...02.55` / `.54`）— setup 文件下载开始/完成的异步事件。

**本次未找到** pin 配置专用的 HVM 命令；只能通过 test program / device 下载间接带上 pin 配置。**推断**：若要从外部精确控制“只改 pin 配置并下载”，HVM 不是合适的入口，应看 TPI 的 `DataManager(dm_config, ...)`。

### SmartShell

`02.15` 是全库唯一一篇 SmartShell 总述页；其 `Functional changes` 写明 **`Introduced in SmarTest 8.2.5`**，而本 wiki 面向 SmarTest 7.10.3。**结论（文档事实）**：SmartShell 在本 wiki 的目标版本不存在，不能作为本阶段的 L3 接口。该章正文只有 PDF 外链，也没有 pin 配置级内容。

## 产物

**文档事实**：

- **pin 配置文件**：`02.08.04.18.04` 写明文件位于 `<device_dir>/configuration`，并说文件「contains a set of firmware commands corresponding exactly to the parameters specified within the Pin Configuration tool」。文件头是 `hp93000,config,0.1`；样例正文含 `DFPN`、`DFPS`、`DFAN`、`PSTE`、`CONF`、`RDIV`、`DDSL`、`PSLC`、`NOOP` 等命令。该页还明确：可以用文本编辑器代替 Pin Configuration Tool 直接写这份 firmware 命令文件。
- **可选 master 文件**：`02.08.04.18.05` 说明可以把配置拆成 package 文件与 alias 文件，再用 master 文件组装。master 文件头固定为 `hp93000,config_master_file,0.1`，第二行是 `testerfile: <tester_file_name>`，随后是 `Package: <file>` 与若干 `<alias_set_name>: <file>`。子文件路径可相对可绝对，相对路径以 master 文件所在目录为基准；可用 `#` 注释。Setup Management Tool 用它组装。
- **CSV**：Pin Configuration tool 支持从 CSV 导入、导出 pin 配置（`02.08.04.18.02.02` / `.02.03`）；导出用于报告与文档化。
- **alias set**：`02.08.04.18.01.04` 说 pin 配置文件、level/timing equation setup 文件、pin configuration master file、使用 setup API 的文件（analog control / waveform）与 test method 源文件都支持 pin alias。
- **DC Scale Extensions**：`02.08.04.18.03.05` 说该编辑器的设置存入 pin 配置文件，并可用 Testflow Analyzer Tool (TAT) 导出到 device license file。
- **备份路径旁证**：`02.09.02.03.02` 的 STPM 参数说明以 pin 配置文件 `mypins.cfg` 为例，给出备份路径 `<device_directory>/configuration/back/mypins_121102_214323.cfg`。这是 STPM 转换工具的行为，不是 Pin Configuration tool 的保存动作，只能作为 `.cfg` 放在 `configuration/` 下这一命名约定的旁证。
- **没有单独的运行期产物**：本阶段产出的是 setup 文件与其在硬件上的下载状态，不产出结果数据。

**文档事实（重要副作用）**：`02.08.04.18.02.06` 原文：

> CAUTION Setup data becomes invalid when there is a change in the pin configuration. Never save the setup (except the pin configuration) immediately after modifying the pin configuration! You would overwrite valid setup files with invalid data or no data.

## 验证

- **GUI 侧（首选）**：`02.08.04.18.02.05` 写明「Unlike all the other setup windows, you download pin configuration data by clicking the Apply button.」Apply 之后看状态指示器：
  - 修改后、Apply 前：Square State Indicator 变黄，表示编辑器数据与硬件不同。
  - Apply 后：「The Square State Indicator becomes green which means that the data has been downloaded to the hardware.」
  - 文件名后出现星号：「The Asterisk State Indicator appears after the pin configuration file name as shown in the figure below. That means the pin configuration file is not consistent with the data in the hardware.」
  - `02.08.04.18.03.12` 补充：方块在 setup component 名前、星号在其后；两者分别覆盖组件级与文件级的一致性。
- **命令回读**：
  - `DFPN? (@)` 列出所有由 `DFPN` 定义的 pin（`02.06.03.02.08`）。
  - `DFPS?` 回读 DPS 通道、极性与 pin number（`02.06.03.02.09`）。
  - `CONF?` 回读引脚类型与工作模式；`ALL` 列出所有 mode context（`02.06.03.02.02`）。
  - `DFGP? (SCAN_OUT)` 返回组成员；`DFGE? (SCAN_OUT)` 返回定义表达式（`02.06.03.01.06`）。
  - `DFPT?` 回读 port 定义（`02.06.03.02.10`）。
  - `PFND? (I/O1_1)` 查 pin 属于哪些 port；`PFND? DIFF,(P+)` 查差分对（`02.06.03.02.18`）。
  - `PSTE? STR` 返回 site string；文档用例 `PSTE "101"` 表示配了 3 个 site、但 site 2 不可用（`02.06.03.02.22`）。
  - `PACT? STR` 返回每个 site 的激活/mask 状态（`02.06.03.02.16`）；`PQFC?` 返回当前 query focus（`02.06.03.02.19`）。
  - `GCTX?` 回读 level / timing / wavetable / label / multiport 等组件使用的 mode context（`02.06.03.02.14`）；`02.06.03.01.03.01` 要求这些 context 必须一致。
  - `CHIN? ALL` 核对通道类型与物理位置，可用来确认 `DFPN` 里的通道号确实指向预期板卡（`02.06.03.02.01`）。
  - `HWTY?` 与 `*OPT?` 核对机器型号、testhead、DUT interface 与已装硬件选项（`02.06.03.02.15`、`.36`、`.37`）。
  - `VPIN? (@)` 列出所有 virtual pin；`DFPC?` 回读 pin 注释；`PSSL?` 回读安全限值（`02.06.03.02.35`、`.07`、`.21`）。
- **多 site 目视检查**：`02.08.04.18.02.07.04` 的 Results 段写明，若多个 site 的 pin 共用完全相同的 digital channel，对应通道会以黄色背景显示，要求「Please carefully check the channel assignment.」
- **master 文件组装校验**：`02.08.04.18.05` 列出 Setup Management Tool 会检查的四条：不同文件的 site 数相同；alias 文件里的所有 channel 都出现在 package 文件；不同文件的 context 不重复（DEFAULT 除外）；channel 在 package 文件里必须定义为 I/O 才能让不同 alias 使用 I 和 O 两个方向，否则所有 alias 必须同方向。任一条不满足，组装中止并报错。
- **建议**：Apply 之前用 `DFPN? (@)`、`CONF?`、`DFGP?`、`DFPT?` 的输出与分配表逐项对照；也可以用 CSV 导出做人工 diff（导出功能见 `02.08.04.18.02.03`）。**本次未找到**文档里被描述为一键校验整份 pin 配置的命令或工具，验证必须按对象逐条做。这是建议，不是文档要求。

## 常见错误

**文档事实**：`02.06.03.01.11` 给出本阶段的总错误条件——测试正在运行、编程的资源未安装、资源已被占用、系统里没有装 device power supply、sequencer 不在 OFF 状态、resistive divider 值超范围。

### 命令级症状

| 症状 | 可能原因（文档） | 排查入口 | 出处 |
|---|---|---|---|
| `CHIN?` 报错 | `channel_nr` 值错误 | 用 `CHIN? ALL` 或 `*OPT?` 核对通道 | `02.06.03.02.01` |
| `CONF` 报错 | sequencer 处于 run 或 break | `SQST` 先停 sequencer | `02.06.03.02.02` |
| `DFPN` 报 channel invalid / not installed | 五位数通道号写错或该通道未装 | `CHIN? <channel>`；`*OPT?` | `02.06.03.02.08` |
| `DFPN` 报 channel already allocated / pin already defined | 同一通道或同名 pin 已定义过 | `DFPN? (@)` 全量回读 | `02.06.03.02.08` |
| `DFPN` 报 pin name already used as a group name | pin 名与组名冲突 | `DFGP?` / `DFGE?` 查组名 | `02.06.03.02.08` |
| `DFPN` 报 sequencer in RUN or BREAK | sequencer 状态不是 OFF | `SQST` | `02.06.03.02.08` |
| `DFPN` 报 ganging 的通道不全是 DC Scale | 通道列表混入非 DC Scale 通道 | `CHIN?` 逐个核对通道类型 | `02.06.03.02.08` |
| `DFPS` 报 DPS 未装 / 通道已分配 / 通道号无效 | 超过已装 DPS 数、通道已占用、未装或号错 | `*OPT?`；`DFPS?` | `02.06.03.02.09` |
| `DFPS` 报 connected state 下分配 DPS 通道 | 在 connected 状态下发 `DFPS` | 先断开 DUT 再分配 | `02.06.03.02.09` |
| `DFGE` 报组数超过 2400 / 类型非法 / pin 太多 / 递归 / 表达式为空或有错 / 组名与 pin 冲突 | `DFGE` 的 `Errors` 段 | 用 `DFGP?` / `DFGE?` 查现有组；减少组数或表达式规模 | `02.06.03.02.04` |
| `DFGP` 报组数超过 2400 / 组名与 pin/DPS pin 冲突 / pin 太多 | `DFGP` 的 `Errors` 段 | 同上 | `02.06.03.02.05` |
| `DFUP` 报 setting 含 0/1/X 以外字符、长度与通道列表不一致、名字已被占用、通道号超范围 | utility purpose 的 setting 格式或命名/通道冲突 | `DFUP?` 回读；检查 setting 长度与通道号 | `02.06.03.02.11` |
| `DFUT` 报通道号超范围 / 通道已被占用 / utility 名与 analog/digital pin 冲突 / 指定通道在 `DFUT` 里是 READ ONLY | utility line 通道号、模式或命名冲突 | `DFUT?` 回读；`HWTY?` 核对硬件 | `02.06.03.02.12` |
| `DSCP` 报 cycles / waveform sets / timing sets / level sets / DPS sets 数量超范围或内存不足 | sequencer memory 参数超限 | `DSCP?` 回读；按当前内存配置缩小参数集 | `02.06.03.02.13` |
| `PACT` 报 not all pins at the site have had their channels assigned by `PALS` | 该 site 的通道未分配完 | `PALS? ALL,(<pin>)` 逐 site 查 | `02.06.03.02.16` |
| `PACT` 对不可用 site 只发 warning | 该 site 不可用 | `PSTE? STR` 看哪些 site 是 `"1"` | `02.06.03.02.16` |
| `PALS` 报 channel invalid / not installed / pin name already used as a group name / sequencer RUN 或 BREAK | `PALS` 的 `Errors` 段 | 先 `SQST`，再 `DFPN?` / `DFGP?` | `02.06.03.02.17` |
| `PQFC` 对不可用 site 发 warning、focus 不变；或报 `PALS` 未分配 | site 不存在/不可用，或通道未分配 | `PSTE? STR`；`PALS?` | `02.06.03.02.19` |
| `PSTE` 报 not all pins at the site have had their channels assigned by `PALS` | 新 site 的通道没分配完 | `PALS? ALL,(<pin>)` | `02.06.03.02.22` |
| `PSTE` 报 all channels are listed in the MCDIgnore file | 该 site 用到的通道全部被 MCDIgnore | 查 MCDIgnore 文件与服务手册 | `02.06.03.02.22` |
| `STME` 报错 | 参数不是 ON/OFF/AUTO/FAST | `STME?` 回读 | `02.06.03.02.23` |
| 其它 firmware 命令（如 `PSLV`）超过 `PSSL` 限值时 firmware 打印错误信息 | 安全限值设得过紧，或操作超出 pin 允许范围 | `PSSL?` 回读限值；按 DPS 规格重设 | `02.06.03.02.21` |
| `UDEF` 报错 | sequencer 在 run 或 break | `SQST` | `02.06.03.02.24` |
| `UDUP` 报错 | 引用的 utility purpose 未定义 | `DFUP?` 回读 | `02.06.03.02.27` |
| `UDUT` 报错 | 引用的 utility line 未定义 | `DFUT?` 回读 | `02.06.03.02.28` |
| `UDVP` 报错 | 指定 pin 不是 virtual pin，或从未定义 | `VPIN? (@)` | `02.06.03.02.29` |
| `UPAS` 报错 | 未用 `PSTE` 做 multisite；site 号越界；名字不是 utility purpose 或已被占用；setting 不一致/字符非法/长度不符 | `PSTE?`；`DFUP?`；检查 setting | `02.06.03.02.30` |
| `UPST` 报错 | 引用 utility line 未定义，或同一通道有 exclusive setting | `DFUT?` / `UPST?` | `02.06.03.02.31` |
| `UPTI` 报错 | settling time 小于 0 或超范围；utility purpose 未定义 | `UPTI?`；`DFUP?` | `02.06.03.02.32` |
| `UTTI` 报错 | settling time 小于 0 | `UTTI?` | `02.06.03.02.34` |
| `UTST` 警告 | 引用 utility line 未定义 | `DFUT?` | `02.06.03.02.33` |
| `VPIN` 报错 | pin 名已被其它 pin、port 或 group 使用 | `DFPN? (@)` / `DFGP?` / `DFPT?` | `02.06.03.02.35` |
| `DFPC` 报错 | pin 未经 `DFPN` 定义（`Predependencies`） | `DFPN?` | `02.06.03.02.07` |
| `DFLV` / `DFPC` / `UDGP` / `UDPT` 没有 `Errors` 段 | — | **文档未覆盖** | `02.06.03.02.06`、`.07`、`.25`、`.299` |

### GUI / 文件级症状

| 症状 | 可能原因（文档） | 排查入口 | 出处 |
|---|---|---|---|
| Apply 后方块不是绿色 | 数据没下载到硬件，或只改了编辑器没 Apply | 重新 Apply，看是否弹 Confirm Apply | `02.08.04.18.02.05` |
| 文件名后出现星号 | 配置文件与硬件数据不一致 | 保存文件或重新 Apply，使两者一致 | `02.08.04.18.02.05` |
| Apply 失败后想 Revert，但 Revert 不可用 | 文档说 Apply 失败时 Revert 会被禁用 | 先修复 Apply 失败原因 | `02.08.04.18.02.04` |
| 改完 pin 配置后保存其他 setup，导致其他 setup 变空/变错 | pin 配置变化会使其他 setup 失效 | 先 Apply 并保存 pin 配置，再重新加载其他 setup；不要立刻保存其他 setup | `02.08.04.18.02.06` |
| master 文件组装被中止 | site 数不同；alias 文件的 channel 不在 package 文件；不同文件 context 重复（DEFAULT 除外）；package 里通道方向与 alias 冲突 | 逐条对照四条规则检查各子文件 | `02.08.04.18.05` |
| group 在 timing / level / vector 窗口不显示或半色调 | 组内 pin 不兼容：timing 不接受混合 I/O 或不同模式；level 不接受 o 与 io 混合；vector 只能全 i/全 o/全 io | 在 Pin group editor 检查成员类型 | `02.08.04.18.03.02.02` |
| 表达式组成员与定义表达式对不上 | 看成员要用 `DFGP?`，`DFGE?` 只返回表达式 | `DFGP? (组名)` | `02.06.03.01.06` |
| 想加第 11 个 mode context 失败 | Context list 文档写明最多 10 个 context | 删掉不用的 context 或复用 | `02.08.04.18.03.01.01` |
| 多 site 下 site 数够了但有的 site 不能测 | 该 site 用的通道在 MCDIgnore 里 | `PSTE? STR` 看哪些 site 是 `"0"` | `02.06.03.02.22`、`02.06.03.01.09` |
| level / timing / pattern 里 context 对不上 | mode context 必须在所有 setup 组件里一致 | `GCTX?` 回读各 setup 组件使用的 context | `02.06.03.01.03.01` |
| >255 site 的多 site 测试报错 | site match 必须为 off | `STME OFF`；文档同时提醒 >255 site 并非所有 test head card 都支持 | `02.06.03.01.10.04` |

## 下一步

下一步是 [[level]]。

**文档事实**：`02.06.03` 明说没有 pin 配置就无法定义 level、timing 或 vector 参数；`02.06.03.01.03.01` 还要求 level、timing、vector setup 选用的 mode context 必须一致，而这个 context 正是在本阶段用 `CTXT` / `CONF` 建立的。因此先把 pin 与 context 定稳，再进 [[level]]；之后才轮到 [[timing]]、[[pattern]] 与 [[testmethod]]。多 site 的 site match 与 focus 语义会在 [[run]] / [[testflow]] 阶段继续使用。
