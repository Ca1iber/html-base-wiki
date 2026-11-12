---
type: stage
title: Pattern / Vector 配置（Vector Setup）
tags: [pattern, vector, sequencer, label, burst, multiport, sqlb, sqpg]
related:
  - "[[project]]"
  - "[[pin]]"
  - "[[level]]"
  - "[[timing]]"
  - "[[testmethod]]"
  - "[[testflow]]"
  - "[[run]]"
  - "[[results]]"
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16_Pattern_Tools.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.06.15_Align_Display.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.04.01_xN-mode_example.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.04.02_x1_N-mode_example.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.04.04_Changing_the_x-mode_area.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.06.18_Changing_the_x-mode_area.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.06.14_Masking_and_activating_signals.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.04.11_Changing_pattern_tool_preferences.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.06.11_Inserting_and_editing_comments.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.04.02_Editor_status_line.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.06.07_Going_to_a_signal_or_vector.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.01_Collapsed_and_expanded_mode.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.06_Pattern_Editor_tasks.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.02_Signal_and_pin_group_representations.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.07_Pattern_Editor_quick_reference.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.14.01_Moving_vectors_to_another_memory_type.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.03_Multiport_Burst_Editor.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.15.05_Saving_patterns_in_separate_files__Save_Partial_As.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.02.26_SQLA__SQLA__-__SeQuencer_Label_Attribute.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.10_Synchronizing_vectors_in_a_multi-port_setup.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.10.04_Defining_sequencing_groups.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.02_List_of_vector_setup_commands.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.10.01.01_Sequencing_groups_and_pattern_structure.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01_Concepts_of_vector_setup.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.08.05.03.02_Multi-port_burst_labels.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07_Vector_Setup_Commands.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.01_The_structure_of_labels.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.01.01_The_label_definition.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.06_Overview_of_firmware_commands.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.06.02_Controlling_the_sequencers.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.06.03_Managing_the_sequencer_area.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.06.04_Downloading_vectors.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.06.05_Managing_sequencer_constructs.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.06.06_Comments_on_vectors.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.07_Editing_and_executing_labels_at_firmware_level.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.07.01_Creating_a_label.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.07.01.02_Creating_a_label_with_edit_commands.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.07.04_Executing_a_label.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.08_Using_sequencer_instructions.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.08.01_Vector_generating_instructions.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.08.03_Instructions_for_changing_the_setup.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.08.03.01_Changing_the_timing_set__CTIM.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.08.03.02_Changing_the_level_set__CLEV.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.08.04_Loops.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.08.04.01_Endless_loops.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.08.04.03_Match_loops.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.08.04.03.02_Timed_match_loop.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.08.05_Main_programs_and_subroutines.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.08.05.01_Main_labels.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.08.05.02_SVEC_subroutines.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.08.04.02_Counted_loops.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.15.04.01_TPI_functions.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.04.05.01_Function_of_the_base_wavetable.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14_Test_Suite_Control_API.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01_TestsuiteProxy.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.06.16_Creating_a_Digital_Source_setup.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.06.08_Locating_events_and_their_test_points.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.06.09_Renaming_events_and_test_points.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.03.01_From_global_to_port_specific_vector_areas__Migration_and_compatibility.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.03_Pattern_editor_properties_view.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.04.01_Selecting_the_memory_type.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.06.17_Creating_a_Digital_Capture_setup.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.06.06_Replacing_failed_state_characters_for_golden_device.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.08.06_Instructions_for_PRBS_and_SmartLoop_tests.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.06_Cloning_a_pattern.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.15.03_Loading_and_saving_selected_items_of_a_pattern_master_file.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.08.05.03.02.02_Incomplete_multi-port_setups.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.03_Sequencer_areas_and_vector_areas.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.04_Addressing_the_vector_areas.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.06.03_Importing_layouts_of_the_Pattern_Editor.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.03.02_Missing_vector_data_and_migration_from_6.5_to_7.x.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.11_Importing_patterns.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.12_Exporting_patterns.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.06.10.01_Inserting_counted_match_loops.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.04.09_Protocol_pattern_specifics_of_the_Pattern_Explorer.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.04.10_Protocol_pattern_specifics_of_the_Pattern_Editor.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.04.10.01_Reconstructing_transaction_signals.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.04.02_Memory_pooling_within_channel_groups.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.06.19_Adding_synchronization_markers.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.04_Creating_a_multiport_burst.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.03.01_Creating_a_multiport_burst.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.05_Creating_and_assigning_a_port_burst.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.03.02_Creating_and_assigning_a_port_burst.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.03.03_Editing_a_multiport_burst_setup.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.03.04_Working_with_sync_groups.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.07_Moving_or_copying_pattern_files.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.10_Merging_and_splitting_pattern_files.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.09_Checking_pattern_references.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.08_Deleting_pattern_files.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.15.04_Saving_a_pattern_master_file.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.29_TestsuiteProxy.setSequencerLabel.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01.09_TestsuiteProxy.getSequencerLabel.htm
  - 01_Getting_started/01.07_Testing_a_Basic_Digital_Device/01.07.01_Testing_a_basic_digital_device.htm
  - 01_Getting_started/01.07_Testing_a_Basic_Digital_Device/01.07.01.01.01_Device_directory_structure.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.01.01_Digital_test_setup_flow.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.08.05.03.02.03_Using_execution_contexts.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.201_SEQUENCER_CONTEXT.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.06.20_Removing_synchronization_markers.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.202_SEQUENCER_CONTEXT_ITEM.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.143_PatternPort__getInstance.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.185_releaseInstance___-_PatternPort_API.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.149_playPattern.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.223_setWaitTemplatePatternName.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.05_Virtual_sequencer_instructions_for_protocol_patterns.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.08.04.03.03_Fast_Sync.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.08.04.03.03.01_How_to_use_Fast_Sync.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.04.06_How_Vectors_are_Stored_in_Sequencer_Memory.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.04.05.01.01_The_Significance_of_the_Base_Waveform_Set.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.04.03_Dependencies_Between_the_Timing_Setup_and_the_Vector_Setup.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.15_Working_with_pattern_master_files.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.15.02_Loading_or_initializing_a_pattern_master_file.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.15.01_Creating_a_pattern_master_file.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.04.08_Data_Queue.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.04_Pattern_Reference_Information.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.04.07_X_Modes.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.09_TPI_Program_Routines.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.09.02_DataManager.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.09.21_HpFwTask.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.65_EXECUTE_TEST.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.75_FUNCTIONAL_TEST.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.77_FW_TASK.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.88_GET_FUNCTIONAL_RESULT.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.167_PRIMARY_STATUS_-__Primary.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.204_SEQUENCER_STATUS_-__Sequencer.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.235_START_TEST.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.269_VECTOR.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.33_DigitalCapturePort__setDefaultPattern.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.34_DigitalCapturePort__setDefaultPattern___-_Repeat.htm
  - 02_System_reference/02.15_SmartShell/02.15_SmartShell.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.01.01.02_Code-based_and_pattern-based_programming.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.04.05_Wavetables.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.10.01_Synchronization_within_sequencing_groups.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.10.02_De-coupling_ports_by_separate_sequencing_groups.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.10.03_Phase_synchronization_across_sequencing_groups.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.08.05.03.02.01_Timing_ports_and_vector_ports.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.08.02_Address_instructions.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.06.01_Low_level_and_high_level__edit__commands.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.04.04_The_function_of_patterns.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.07.02_Deleting_a_label.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.05_The_pattern_master_file.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.07.01.01_Creating_a_label_with_low_level_commands.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.142_PATTERN_CONTROLLER.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.142.01_PATTERN.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.08.05.02.01_Calculating_the_buffer_cycles_for_JMPE_and_RETC__and_match_loops.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.09.03_How_to_prevent_the_data_queue_from_running_empty.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.09_Managing_the_data_queue.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.09.01_Data_transfer_from_the_vector_area_to_the_data_queue.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.09.02_Operation_mode_of_the_data_queue.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.10.01_HVM_API_Introduction.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.02_Label_definition__sequencer_program__and_sequencer_area.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.01.03_The_sequencer_program.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.07.03.01_Inserting_a_sequencer_instruction.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.07.03_Inserting_and_Deleting_Sequencer_Instructions.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.07.03.02_Deleting_a_sequencer_instruction.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.08.04.03.01.01_Adjusting_the_junctions_between_match_loop_and_surrounding_label.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.08.04.03.01_Counted_match_loops.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.08.05.03.01_Burst_labels.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.08.05.03_Burst_labels_and_multi-port_burst_labels.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.01.02_The_vectors.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.02.01_APDV_-__APpenD_Vectors.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.02.02_APTS_-__APpend_TeSt.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.02.03_BCMT__BCMT__-__Binary_CoMmenT.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.02.04_BLUP_-__BLock_UP_to_date.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.02.05_CMNT__CMNT__-__CoMmeNT.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.02.06_CMVC_-__Clear_and_MoVe_Comments.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.02.07_CNGV_-__CoNnect_Generate_Vectors.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.02.08_CPYV_-__CopY_Vectors.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.02.09_DELI_-__DELete_Instruction.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.02.10_DELV_-__DELete_Vectors.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.02.11_DLPP_-__DeLete_Per_Pin_Subroutine.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.02.12_DLTS_-__DeLete_TeSt.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.02.13_DMAS__DMAS__-__Define_Memory_Area_Size.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.02.14_DPPC_-__Define_Per_Pin_subroutine_Configuration.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.02.15_DPPS__DPPS__-__Define_Per_Pin_Subroutine_label.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.02.16_DPSA__DPSA__-__Define_per_Pin_Subroutine_Address.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.02.17_FTSM__FTSM__-__Functional_Test_Set_Mask.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.02.18_GETA__-__GET_vector_memory_Address_information.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.02.19_INGV_-__INsert_Generate_Vectors.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.02.20_INSI_-__INsert_Instructions.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.02.21_NODV__-__Number_Of_Displayable_Vectors.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.02.22_RSET_-__ReSET.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.02.23_SAOF__SAOF__-__Set_Alternating_Operation_Features.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.02.24_SPGV_-__SPlit_Generate_Vectors.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.02.25_SQGB__SQGB__-__SeQuencer_GloBal.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.02.27_SQLB__SQLB__-__SeQuencer_LaBel_definition.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.02.28_SQPG__SQPG__-__SeQuencer_ProGramming.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.02.29_SQSL__SQSL__-__SeQuencer_Start_Label.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.02.30_SQST__SQST__-__SeQuencer_STate.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.02.31_SQTO__SQTO__-__SeQuencer_TimeOut.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.02.32_SREC__SREC__-__Set_RECeiver_mask.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.02.33_TCMT__TCMT__-__Test_CoMment_Transfer.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.02.34_TSTL__TSTL__-__TeST_Label.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.02.35_VDCG__-__Verify_Device_Cycle_for_Group.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.02.36_VDCN_-__Vector_Device_Cycle_Name.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.02.37_VDCP__VDCP___Vector_Device_Cycle_Parameter.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.02.38_VECC__VECC__-__VECtor_download_Compressed.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.02.39_VECD__VECD__-__VECtor_Download.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.04.01_Definitions__Vector__Pattern__Burst__etc.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.02.40_VPAR__-__Vectors_in_PARallel.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01_Pattern_Explorer.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02_Pattern_Editor.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.01_Opening_the_Pattern_Explorer.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.06.01_Opening_the_Pattern_Editor.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.02_Creating_a_pattern.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.13_Sorting_and_filtering_the_pattern_table.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.14_Editing_properties_in_the_Pattern_Explorer.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.03_Viewing_and_editing_bursts_in_the_Pattern_Explorer.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.06.04_Editing_patterns.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.06.10_Inserting__editing__and_deleting_sequencer_instructions.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.04.03_STATEMAP_section_of_the_wavetable.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.06.05_Finding_and_replacing_pattern_cells.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.04_DUT_oriented_view_-_xN_and_x1_N_mode.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.06.02_Configuring_the_layout_of_the_editor.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.06.12_Copying_patterns.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.06.13_Displaying_failure_data.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.06.10.02_Sequencer_instructions.htm
created: 2026-11-12
updated: 2026-11-12
verified: doc-only
---

# Pattern / Vector 配置（Vector Setup）

> 把「哪些波形在哪个 tester cycle 驱动/比较哪些 pin」编码成 label、vector 数据与 sequencer program，并下载到按 port 划分的 vector area。

## 目的

文档事实：在 vector setup 里定义测试的 label，文档同时称之为 test label、vector label、sequencer label 或 pattern。label 是 SmarTest 的基本处理单元，由一串用于把 vector stream 送给 DUT 的指令组成，并用唯一名字标识（`02.06.07`）。

文档事实：一个 label 由三部分构成（`02.06.07.01.01`）：

- label definition：唯一名字、类型、base wavetable、所属 port；
- 一个 waveform DC/DC power unit 数组，用来标识 vector；
- 一个把上述 vector 施加到 port 各 pin 上的程序。

这三部分通过引用连接：label definition 引用程序，程序中的指令指向 waveform DC/DC power unit 的位置（`02.06.07.01.01`）。

文档事实：`pattern` 是 vector 与 sequencer instruction 的序列；`label` 是 pattern 的名字；Pattern Debug Tool 文档里经常把 label 当作 pattern 的同义词（`02.08.04.16.04.01`）。

文档事实：burst 与 multi-port burst 把多个 MAIN label 用同一组 primary set 连续执行，作用类似一串子程序调用，可显著减少重复的 primary set 激活与 CTOF 开销（`02.06.07.01.08.05.03`、`02.06.07.01.08.05.03.01`）。

推断：本阶段解决的是「vector setup 的定义与下载」；真正把 label 跑起来并判 PASS/FAIL 属于执行阶段（`[[run]]`），而把 label 绑定到 test suite 属于 `[[testmethod]]` / `[[testflow]]`。本页只把执行命令当作边界与验证入口，不展开运行流程。

## 前置条件

1. **device / 目录已建立。** vector setup 文件默认放在 `<device>/vectors` 子目录（`02.06.07.01.05`）；设备目录结构见 `01.07.01.01.01` 与 `[[project]]`。
2. **pin configuration 已完成。** 数字测试 setup flow 把 Pin Configuration Setup 列为 Step 2，把 levels、timing 与 vector setup 列为 Step 3（`02.08.01.01`）。label 必须关联一个 port；port 是可按并行但独立方式测试的一组 pin，默认 port 为 `@`（`02.06.07.01.01`）。7.x 起每个 port 在它包含的每个 pin 上都有自己的 port-specific vector area（`02.06.07.01.03.01`）。port 的定义见 `[[pin]]`。
3. **timing setup 已完成。** 文档事实：timing setup 未完成就不能生成 vector；vector 完成后不能对 timing setup 做大改，否则 vector memory 内容会被错误解释；仍可改 edge 位置（`02.08.04.16.04.03`）。timing/level 数据见 `[[timing]]`、`[[level]]`。
4. **base wavetable / waveform set 已存在。** `SQLB` 要指定 base wavetable（或 fixed timing 的 base waveform set）；它用于 Pattern Tool 在 waveform index 与 device cycle name 之间转换（`02.06.07.01.01.01`、`02.08.04.16.04.05.01`）。`SQLB` 在 base waveform set 超出 `WSUS` 允许范围时报错（`02.06.07.02.27`）。
5. **device cycle 已定义。** `VDCP`/`VDCN` 用 base waveform set / wavetable 把 device cycle 名与 data parameter 翻译成 physical waveform DC/DC power unit（`02.06.07.02.37`、`02.06.07.02.36`）；`VDCG?` 可检查组内 device cycle 的一致性（`02.06.07.02.35`）。
6. **sequencer area 有足够空间。** 低层流程先 `DMAS` 扩大 sequencer area，再 `SQLB` 定义 label（`02.06.07.01.07.01.01`、`02.06.07.02.13`）。`APTS` 会自动扩大，不需要手工 `DMAS`（`02.06.07.02.02`）。
7. **需要编辑的 label 先 `TSTL` 激活。** 大多数修改 sequencer area / vector area 的 edit 命令都要求 label 已用 `TSTL` 激活（`02.06.07.01.06.01`、`02.06.07.02.34`）。
8. **7.x port-specific setup 下载 vector 时要给 port。** 若 vector setup 是 7.x 格式（STVA 地址在 `param_2`、vector area 按 port 划分），`VECD`/`VECC` 必须指定 port；旧格式可省略，由命令分析 STVA 地址定位（`02.06.07.02.39`、`02.06.07.02.38`、`02.06.07.01.03.01`）。
9. **multi-port 需要 port 与 sync group 定义。** 建 multiport burst 前应先定义若干 port，且不能把共享 pin 的两个 port 放进同一个 multiport burst（`02.08.04.16.01.04`）。sync group 内的 port 也不能共享 device pin（`02.08.04.16.03.04`）。timing port 与 vector port 可以不同（`02.06.07.01.08.05.03.02.01`）。
10. **Fast Sync 有版本与硬件前提。** 需要 SmarTest 7.4.0 或更高；属于 match loop 的 device pin 必须在同一个 test processor 上；为吞吐率应尽量减少同一 test processor 上的独立 match loop 数（`02.06.07.01.08.04.03.03.01`）。
11. **memory pooling / license 前提。** 同 4-channel 或 8-channel group 的 channel 共用物理内存，memory pooling 默认开启；HSER 只有具备 SmartLoop license 的 channel 才能参与（`02.06.07.01.04.02`）。

## 涉及对象

### 概念与产物对象

- `pattern`（concept）— vector + sequencer instruction 的序列；Pattern Editor 里是一整张表（`02.08.04.16.04.01`）。
- `label`（concept）— pattern 的名字；类型 `MAIN`/`SVEC`/`BRST`/`DSRC`/`MPBU`/`SJMP` 决定能否直接执行、能否调用子程序（`02.06.07.01.08.05`、`02.06.07.02.27`）。
- `port`（concept）— 可按并行但独立方式测试的 pin 组；默认 `@` 含全部 pin（`02.06.07.01.01`、`02.08.04.16.04.01`）。
- `sequencer-area`（concept）— 按 port 划分、存放该 port 所有 label 的 sequencer program 的内存区域；指令编号跨程序连续编号（`02.06.07.01.02`）。
- `vector-area`（concept）— 按 pin 与 port 划分、存放 physical waveform DC/DC power unit 的区域；同一 port 的各 pin 内容通常不同（`02.06.07.01.03`）。
- `sequencer-program`（concept）— 由 `SQPG` 写入的指令序列；`MAIN` 以 `STVA`/`STSA` 开头、`STOP` 结尾（`02.06.07.01.01.03`、`02.06.07.01.08.05.01`）。
- `sequencer-construct`（concept）— 一条 vector generating instruction 与它在各 pin vector area 中对应数据块的组合（`02.06.07.01.04`）。
- `data-queue`（concept）— sequencer 解码指令时仍能向 DUT 连续供 vector 的队列；以 8 个 waveform 为单位（`02.06.07.01.09`、`02.06.07.01.09.01`）。
- `wavetable`（concept）— 每个 pin/ pin group 的 physical waveform index 与 action / device cycle name 表（`02.08.04.16.04.05`）。
- `base-wavetable`（concept）— 只用于 Pattern Editor 显示/编辑 device cycle name，不用于执行；执行用 primary wavetable（`02.08.04.16.04.05.01`）。
- `device-cycle`（concept）— wavetable 中一个 index 对应的一组 action，有名字；`VDCP`/`VDCN`/`VDCG?` 围绕它工作（`02.08.04.16.04.05`、`02.06.07.02.37`）。
- `pattern-master-file`（file）— 文本文件，列出 pattern 文件与路径；文件头 `hp93000,pattern_master_file,0.1`（`02.06.07.01.05`）。
- `vector-setup-file`（file）— 把全部 label 放在一个大文件里的 vector setup；必须位于 `<device>/vectors`（`02.06.07.01.05`）。
- `pattern-file`（file）— 单个 pattern 的文件；pattern master file 示例使用 `.binl` / `.binl.gz`（`02.06.07.01.05`）。
- `srec-file`（file）— `SREC` 相关文件 `../vectors/.<Pattern-Name>.SREC`，用于保存 receiver mask（`02.06.07.02.32`）。
- `hpt`（tool）— 在 shell 窗口执行 firmware command 的 utility；`VECD` 的 `$VECD` 变体、`DPPS`/`DPSA` 的“不要从 hpt 执行”提示都以它为背景（`02.06.07.01.07.01.01`、`02.06.07.02.15`、`02.06.07.02.16`）。

### GUI / 工具

- `Pattern-Tools`（gui）— Pattern Explorer、Pattern Editor、Multiport Burst Editor 三个工具的总称（`02.08.04.16`）。
- `Pattern-Explorer`（gui）— 查看已加载 setup 的 pattern、创建/删除 pattern 与 burst、启停编辑器（`02.08.04.16.01`）。
- `Pattern-Editor`（gui）— 显示、编辑 pattern 并分析 error（`02.08.04.16.02`）。
- `Multiport-Burst-Editor`（gui）— 访问 multiport burst 与各 port burst，显示 sync group 的时间线同步（`02.08.04.16.03`）。
- `Multiport-Burst-Setup-Tool`（gui）— 数字设备走查中列出的 multiport burst 工具名，指向同一 `02.08.04.16.03`（`01.07.01`）。
- `Pattern-Editor-tasks`（gui）— Pattern Editor 任务集（打开、布局、编辑、查找替换、failure data 等）（`02.08.04.16.02.06`）。
- `Multiport-Burst-Editor-tasks`（gui）— 创建/编辑 multiport burst、port burst、sync group（`02.08.04.16.03`）。

### L1 / L2 / L3 边界对象

- `DMAS`（L1）— sequencer area / vector area 容量与查询。
- `SQLB` / `APTS` / `SQLA`（L1）— label 定义、追加、属性。
- `SQPG` / `INSI` / `DELI` / `INGV` / `APDV` / `DELV` / `SPGV` / `CNGV` / `CPYV`（L1）— sequencer program 与 sequencer construct 编辑。
- `VECD` / `VECC` / `VDCP` / `VDCN`（L1）— vector data 下载。
- `TSTL` / `SQSL` / `SQST` / `SQGB` / `SQTO` / `FTSM` / `SREC`（L1）— 编辑会话、启动、状态、终止与 mask。
- `CMNT` / `BCMT` / `TCMT` / `CMVC`（L1）— vector 注释。
- `DLPP` / `DPPC` / `DPPS` / `DPSA`（L1）— per-pin subroutine。
- `PATTERN_CONTROLLER` / `PATTERN`（L2）— 在 pattern 内执行 DC/PPMU/BADC 测量。
- `VECTOR`（L2）— vector variable 数据容器（digital capture / digital source 方向）；**不是**本阶段的 vector setup 文件本身。
- `SEQUENCER_STATUS`（L2）— 通过系统对象 `Sequencer` 控制 run/abort/stopCycle/stopVector。
- `SEQUENCER_CONTEXT` / `SEQUENCER_CONTEXT_ITEM`（L2）— execution context。
- `PRIMARY_STATUS::label()`（L2）— 指定要激活的 sequencer start label。
- `FUNCTIONAL_TEST()` / `START_TEST()` / `EXECUTE_TEST()` / `GET_FUNCTIONAL_RESULT()`（L2）— 执行 label 并取结果，属本阶段与 `[[run]]` 的边界。
- `FW_TASK`（L2）— 在 test method 中执行 firmware command，可覆盖本阶段 L1。
- `TestsuiteProxy`（L3）— test suite 的 `setSequencerLabel()` / `getSequencerLabel()`。
- `DataManager`（L3）— `dm_vector` / `dm_pattern_master_file` 文件操作。
- `HpFwTask`（L3）— C 程序中的 firmware command 入口，可执行本阶段 L1。
- `HVM API`（L3）— 外部控制/监控；本次未找到 pattern/vector 专属成员。

### 归属判定

- `02.06.07.*` 整个命令参考章判给本页；其下 40 条命令全部进 L1，概念文档全部进本页概念覆盖清单。
- `CTIM` / `CLEV` 是 **sequencer instruction**，由 `SQPG` 写入（`02.06.07.02.28`），因此它们在本页出现；但它们引用的 timing set / level set 定义属于 `[[timing]]` / `[[level]]`，本页不重复。
- `SPRM`、`FTST?`、`VCYC?`、`DQUE?`、`EPRC?` 不在 `02.06.07.02` 子树内。本页只在验证/边界中提及，不计入 L1。
- GUI 章节 `02.08.04.16`（Pattern Tools）判给本页；Timing Setup Tool、Level setup tool、Pin configuration tool 不判给本页（工具清单见 `01.07.01`）。
- `VECTOR` L2 API 操作的是 vector variable（digital capture / digital source），与本阶段的 label/vector area 不是同一个对象；列在 L2 但明确标为“同形不同物”。
- `TestsuiteProxy.setMultiportTiming()` 属于 timing 绑定，不判给本页；只有 `setSequencerLabel()` / `getSequencerLabel()` 判给本页。
- SmartShell 在本 wiki 面向的 7.10.3 不存在：全库唯一总述 `02.15_SmartShell` 的 Functional changes 写 `Introduced in SmarTest 8.2.5`，正文只有 PDF 外链（`02_System_reference/02.15_SmartShell/02.15_SmartShell.htm`）。本页不把它当可用 L3 接口。

### 概念文档覆盖（`02.06.07.01.*`，64 篇 + 目录篇）

- `02.06.07.01` Concepts of vector setup — 本阶段概念目录，下分 10 个子章（`02.06.07.01`）。
- `02.06.07.01.01` The structure of labels — label 三部分：定义、vector 数组、sequencer program；port 与 vector 定义（`02.06.07.01.01`）。
- `02.06.07.01.01.01` The label definition — `SQLB` 指定名字、类型、程序位置、base wavetable、port（`02.06.07.01.01.01`）。
- `02.06.07.01.01.02` The vectors — 每列一个 pin、每行一个 vector 的 physical waveform DC/DC power unit 数组（`02.06.07.01.01.02`）。
- `02.06.07.01.01.03` The sequencer program — 发送 waveform、改 timing/level、循环与子程序的简单语言（`02.06.07.01.01.03`）。
- `02.06.07.01.02` Label definition, sequencer program, and sequencer area — sequencer area 按 port 划分，指令编号跨程序连续（`02.06.07.01.02`）。
- `02.06.07.01.03` Sequencer areas and vector areas — vector area 按 pin 与 port 划分，STVA 指向 label 的起始地址（`02.06.07.01.03`）。
- `02.06.07.01.03.01` From global to port specific vector areas — 7.0 起从全局 vector area 改为 port-specific；旧格式转换与兼容性（`02.06.07.01.03.01`）。
- `02.06.07.01.03.02` Missing vector data and migration from 6.5 to 7.x — 缺 vector data 的 error/warning 与 7.x 迁移风险（`02.06.07.01.03.02`）。
- `02.06.07.01.04` Addressing the vector areas — 64-bit word、8-bit data unit、最大 index 255、padding、logical vector number（`02.06.07.01.04`）。
- `02.06.07.01.04.01` Selecting the memory type — `SM` / `SHMEM` / `HSER` 与 multisite 共享语义（`02.06.07.01.04.01`）。
- `02.06.07.01.04.02` Memory pooling within channel groups — 4/8-channel group 内 vector memory pooling、license 限制（`02.06.07.01.04.02`）。
- `02.06.07.01.05` The pattern master file — 单一大 vector setup 文件与 pattern master file 两种组织方式、语法与路径规则（`02.06.07.01.05`）。
- `02.06.07.01.06` Overview of firmware commands — 按功能与复杂度分组的 vector setup 命令总览（`02.06.07.01.06`）。
- `02.06.07.01.06.01` Low level and high level (edit) commands — 低层命令只改一种 area，edit 命令同步改两种 area（`02.06.07.01.06.01`）。
- `02.06.07.01.06.02` Controlling the sequencers — `SQST` / `FTST?` / `SQTO` / `SQGB` / `SQSL`（`02.06.07.01.06.02`）。
- `02.06.07.01.06.03` Managing the sequencer area — `DMAS` / `SAOF` / `SQLB` / `SQLA` / `DLTS` / `APTS` / `INSI` / `INGV` / `DELI`（`02.06.07.01.06.03`）。
- `02.06.07.01.06.04` Downloading vectors — `VECD` / `VECC` / `VDCP` / `VDCN` / `GETA?`（`02.06.07.01.06.04`）。
- `02.06.07.01.06.05` Managing sequencer constructs — `INGV` / `APDV` / `DELV` / `SPGV` / `CNGV` / `CPYV`（`02.06.07.01.06.05`）。
- `02.06.07.01.06.06` Comments on vectors — `CMNT` / `BCMT` / `TCMT` / `CMVC`（`02.06.07.01.06.06`）。
- `02.06.07.01.07` Editing and executing labels at firmware level — 创建、修改、执行 label 的总览（`02.06.07.01.07`）。
- `02.06.07.01.07.01` Creating a label — 新 label 通常追加在 sequencer area 末尾；低层与 edit 两条路径（`02.06.07.01.07.01`）。
- `02.06.07.01.07.01.01` Creating a label with low level commands — `DMAS?` → `DMAS` → `SQLB` → `SQPG` → `VECD` 三步流程（`02.06.07.01.07.01.01`）。
- `02.06.07.01.07.01.02` Creating a label with edit commands — `APTS` → `TSTL` → `INGV` → `VECD`（`02.06.07.01.07.01.02`）。
- `02.06.07.01.07.02` Deleting a label — `DLTS` 删除 label，并重排 vector data 避免空洞（`02.06.07.01.07.02`）。
- `02.06.07.01.07.03` Inserting and Deleting Sequencer Instructions — 插删 vector generating instruction 必须维护已有 GENV/RPTV 的向量指向（`02.06.07.01.07.03`）。
- `02.06.07.01.07.03.01` Inserting a sequencer instruction — 一般用 `INSI` + `SQPG`；vector generating 用 `INGV`（`02.06.07.01.07.03.01`）。
- `02.06.07.01.07.03.02` Deleting a sequencer instruction — 一般用 `DELI`；vector generating 用 `DELV` 再 `DELI`（`02.06.07.01.07.03.02`）。
- `02.06.07.01.07.04` Executing a label — `SQSL` 指定 start label、`SPRM` 指定 primary sets、`FTST?` 执行并返回 PASS/FAIL（`02.06.07.01.07.04`）。
- `02.06.07.01.08` Using sequencer instructions — sequencer instruction 控制 vector 流向 DUT（`02.06.07.01.08`）。
- `02.06.07.01.08.01` Vector generating instructions — `GENV` / `RPTV` 的长度、重复次数与最大向量数（`02.06.07.01.08.01`）。
- `02.06.07.01.08.02` Address instructions — `STVA` 的地址在 7.x 放 `param_1` 还是 `param_2` 的规则（`02.06.07.01.08.02`）。
- `02.06.07.01.08.03` Instructions for changing the setup — `CTIM` / `CLEV` 在执行中改 timing/level，且在子程序返回后仍有效（`02.06.07.01.08.03`）。
- `02.06.07.01.08.03.01` Changing the timing set (CTIM) — `CTIM` 触发 CTOF 序列、break/hold 时间组成（`02.06.07.01.08.03.01`）。
- `02.06.07.01.08.03.02` Changing the level set (CLEV) — `CLEV` 与 `CTIM` 类似，长度等于 `p1 = p2` 的 `CTIM`（`02.06.07.01.08.03.02`）。
- `02.06.07.01.08.04` Loops — endless / counted / match 三类循环（`02.06.07.01.08.04`）。
- `02.06.07.01.08.04.01` Endless loops — `LBGN` … `LEND`；只能是最外层循环，最多嵌套 7 层（`02.06.07.01.08.04.01`）。
- `02.06.07.01.08.04.02` Counted loops — `LBGN <次数>` … `LEND`，或用 `RPTJ` + `JSUB` 重复调用子程序（`02.06.07.01.08.04.02`）。
- `02.06.07.01.08.04.03` Match loops — 让无 reset pin 的 DUT 进入目标状态；结果不进 error map，只影响整体 PASS/FAIL（`02.06.07.01.08.04.03`）。
- `02.06.07.01.08.04.03.01` Counted match loops — `MACT` + `GENV`/`RPTV` + `MRPT`；`CONTINUE` 选项（`02.06.07.01.08.04.03.01`）。
- `02.06.07.01.08.04.03.01.01` Adjusting the junctions between match loop and surrounding label — 8-cycle block 归属问题；match loop 前至少插 7 个无 compare 的 buffer vector（`02.06.07.01.08.04.03.01.01`）。
- `02.06.07.01.08.04.03.02` Timed match loop — `WTER` / `MBGN` / `WTER` / `MJPE` / `MEND` 序列，默认 900 s 超时（`02.06.07.01.08.04.03.02`）。
- `02.06.07.01.08.04.03.03` Fast Sync — 每个 test processor 最多 8 个 sync port、支持 1024 sites 的非确定性处理（`02.06.07.01.08.04.03.03`）。
- `02.06.07.01.08.04.03.03.01` How to use Fast Sync — 前置条件、port/timing 设置、`site_match_mode`/`Site Match` OFF、`NIFE`、`STME FAST`（`02.06.07.01.08.04.03.03.01`）。
- `02.06.07.01.08.05` Main programs and subroutines — label 类型决定能否直接执行与调用关系（`02.06.07.01.08.05`）。
- `02.06.07.01.08.05.01` Main labels — 三条限制；必须以 `STVA` + `STSA` 开头、`STOP` 结尾（`02.06.07.01.08.05.01`）。
- `02.06.07.01.08.05.02` SVEC subroutines — 不能直接调用；`JSUB`/`JMPE`/`COGO` 调用，可嵌套 7 层；`RSUB`/`RETC` 返回（`02.06.07.01.08.05.02`）。
- `02.06.07.01.08.05.02.01` Calculating the buffer cycles for JMPE and RETC (and match loops) — 用 `EPRC?` 求 error flag 传播所需 buffer cycles（`02.06.07.01.08.05.02.01`）。
- `02.06.07.01.08.05.03` Burst labels and multi-port burst labels — 用同一 primary set 连续跑多个 MAIN label；burst 不能嵌套（`02.06.07.01.08.05.03`）。
- `02.06.07.01.08.05.03.01` Burst labels — 与独立 MAIN label 的两点差异：primary set 只激活一次、label 之间不补 break cycle（`02.06.07.01.08.05.03.01`）。
- `02.06.07.01.08.05.03.02` Multi-port burst labels — 多 port 并行 burst；同一 label 名可跨 port 重复，内部名为 `<label>@<port_name>`；上限 32766 label/port、256 port（`02.06.07.01.08.05.03.02`）。
- `02.06.07.01.08.05.03.02.01` Timing ports and vector ports — timing port 与 vector port 可以完全不同，也可单 port 对 multi-port 组合（`02.06.07.01.08.05.03.02.01`）。
- `02.06.07.01.08.05.03.02.02` Incomplete multi-port setups — 未覆盖 pin 的 break vector 行为与 W280 警告（`02.06.07.01.08.05.03.02.02`）。
- `02.06.07.01.08.05.03.02.03` Using execution contexts — `SQEC` 定义、`SQRC` 删除、`SQLC?`/`SQSC?` 查询；并行限制（`02.06.07.01.08.05.03.02.03`）。
- `02.06.07.01.08.06` Instructions for PRBS and SmartLoop tests — `PRBS` / `LPBK` / `BRKV` / `TMUA` / `LBGN`/`LEND` 的使用限制（`02.06.07.01.08.06`）。
- `02.06.07.01.09` Managing the data queue — data queue 的作用与三个理解要点（`02.06.07.01.09`）。
- `02.06.07.01.09.01` Data transfer from the vector area to the data queue — sequencer 同时 flatten label，按 8 个 waveform 一块送入 queue（`02.06.07.01.09.01`）。
- `02.06.07.01.09.02` Operation mode of the data queue — queue 满/空时的填充与排空行为（`02.06.07.01.09.02`）。
- `02.06.07.01.09.03` How to prevent the data queue from running empty — 规则与 `FLQU`、`DQUE?`；Pin Scale queue 832 个 instance（`02.06.07.01.09.03`）。
- `02.06.07.01.10` Synchronizing vectors in a multi-port setup — sequencing group 精确同步与 PHASE 部分同步（`02.06.07.01.10`）。
- `02.06.07.01.10.01` Synchronization within sequencing groups — 每次 `CTIM` 后同步；默认 sequencing group；`CLEV` 后需额外 `CTIM` 才能重新同步（`02.06.07.01.10.01`）。
- `02.06.07.01.10.01.01` Sequencing groups and pattern structure — 同组 port 的 pattern 必须有相同数量的 timing/level set change；match loop 建议独占 sequencing group（`02.06.07.01.10.01.01`）。
- `02.06.07.01.10.02` De-coupling ports by separate sequencing groups — 不同 CTOF 数量的 port 必须分到不同 sequencing group，代价是不能精确同步（`02.06.07.01.10.02`）。
- `02.06.07.01.10.03` Phase synchronization across sequencing groups — `PHASE` flag、super-period 与 SCLK overflow（`02.06.07.01.10.03`）。
- `02.06.07.01.10.04` Defining sequencing groups — 可在 timing specification 或 vector setup（Multiport Burst setup tool / `SQLB`）定义；两边定义必须兼容，不要占用 `Default` 名（`02.06.07.01.10.04`）。

### GUI 文档覆盖（`02.08.04.16.*`，77 篇）

- `02.08.04.16` Pattern Tools — 创建、编辑、调试 pattern 与 burst 的三个工具总览（`02.08.04.16`）。
- `02.08.04.16.01` Pattern Explorer — 浏览已加载 setup 的 pattern，创建/删除 pattern 与 burst，启动编辑器（`02.08.04.16.01`）。
- `02.08.04.16.01.01` Opening the Pattern Explorer — 显示已加载 setup 的全部 pattern（`02.08.04.16.01.01`）。
- `02.08.04.16.01.02` Creating a pattern — `New > Pattern`，选类型（Main / SJMP / SubRoutine / Burst / DSRC）、port、memory type、base wavetable、folder（`02.08.04.16.01.02`）。
- `02.08.04.16.01.03` Viewing and editing bursts in the Pattern Explorer — burst 是对 main pattern 的 CALL 序列，连续无 break 执行，固定用默认 port `@`（`02.08.04.16.01.03`）。
- `02.08.04.16.01.04` Creating a multiport burst — 多个 port burst 并行组合；不能把共享 pin 的 port 放进同一 multiport burst；结果类型 `MPBurst`（`02.08.04.16.01.04`）。
- `02.08.04.16.01.05` Creating and assigning a port burst — port burst 是某 port 的 main pattern 序列，必须是 multiport burst 的一部分并属于 sync group（`02.08.04.16.01.05`）。
- `02.08.04.16.01.06` Cloning a pattern — 按原 pattern 的全部或部分 pin 生成新 pattern（`02.08.04.16.01.06`）。
- `02.08.04.16.01.07` Moving or copying pattern files — 在文件夹结构中组织 pattern 文件；仅 pattern master file setup 可用（`02.08.04.16.01.07`）。
- `02.08.04.16.01.08` Deleting pattern files — 可只删 pattern master file 中的引用，或同时删文件（`02.08.04.16.01.08`）。
- `02.08.04.16.01.09` Checking pattern references — 检查引用以维持有效的 pattern master file 结构（`02.08.04.16.01.09`）。
- `02.08.04.16.01.10` Merging and splitting pattern files — Merge Pattern 对话框用于合并或拆分 pattern 文件（`02.08.04.16.01.10`）。
- `02.08.04.16.01.11` Importing patterns — 从 ASCII Interface 格式或 STIL 格式导入（`02.08.04.16.01.11`）。
- `02.08.04.16.01.12` Exporting patterns — 把任意 MAIN pattern 导出为 ASCII Interface 或 STIL 格式（`02.08.04.16.01.12`）。
- `02.08.04.16.01.13` Sorting and filtering the pattern table — pattern 很多时排序/过滤以提高可读性（`02.08.04.16.01.13`）。
- `02.08.04.16.01.14` Editing properties in the Pattern Explorer — 编辑 pattern、port burst、multiport burst 的属性（`02.08.04.16.01.14`）。
- `02.08.04.16.01.14.01` Moving vectors to another memory type — 用 ASCII Interface 附带的 `conv_vector` 工具把 vector 从 VM 移到 SM（`02.08.04.16.01.14.01`）。
- `02.08.04.16.01.15` Working with pattern master files — pattern master file 与单一 pattern 文件的取舍、性能差异（`02.08.04.16.01.15`）。
- `02.08.04.16.01.15.01` Creating a pattern master file — master file 包含文件名与路径列表（`02.08.04.16.01.15.01`）。
- `02.08.04.16.01.15.02` Loading or initializing a pattern master file — 可从 Testflow Editor 或 Test Program Explorer 加载（`02.08.04.16.01.15.02`）。
- `02.08.04.16.01.15.03` Loading and saving selected items of a pattern master file — 在 Pattern Explorer 中加载/保存单个 pattern、port burst、multiport burst 或整个 folder（`02.08.04.16.01.15.03`）。
- `02.08.04.16.01.15.04` Saving a pattern master file — 可按原名保存，或另存为包含全部引用 pattern 的单一 pattern 文件（`02.08.04.16.01.15.04`）。
- `02.08.04.16.01.15.05` Saving patterns in separate files (Save Partial As) — 拆分 pattern 文件并把部分 pattern 另存（`02.08.04.16.01.15.05`）。
- `02.08.04.16.02` Pattern Editor — 显示、编辑 pattern 并分析 error（`02.08.04.16.02`）。
- `02.08.04.16.02.01` Collapsed and expanded mode — 两种显示模式；expanded 显示实际执行的 cycle，只有当前 primary pattern 能进入（`02.08.04.16.02.01`）。
- `02.08.04.16.02.02` Signal and pin group representations — signal 的多种显示格式，用括号缩写标识（`02.08.04.16.02.02`）。
- `02.08.04.16.02.03` Pattern editor properties view — 显示 vector 参数等属性（`02.08.04.16.02.03`）。
- `02.08.04.16.02.04` DUT oriented view - xN and x1/N mode — 按 DUT 周期显示 pattern 的两种 x-mode（`02.08.04.16.02.04`）。
- `02.08.04.16.02.04.01` xN-mode example — xN mode 示例（`02.08.04.16.02.04.01`）。
- `02.08.04.16.02.04.02` x1/N-mode example — x1/N mode 示例（`02.08.04.16.02.04.02`）。
- `02.08.04.16.02.04.03` STATEMAP section of the wavetable — wavetable 的 STATEMAP 段定义 xN/x1/N 显示（`02.08.04.16.02.04.03`）。
- `02.08.04.16.02.04.04` Changing the x-mode area — 修改 signal 的 x-mode area（`02.08.04.16.02.04.04`）。
- `02.08.04.16.02.05` Virtual sequencer instructions for protocol patterns — 编辑器为 protocol pattern 的生成 vector stream 添加虚拟 sequencer instruction（`02.08.04.16.02.05`）。
- `02.08.04.16.02.06` Pattern Editor tasks — Pattern Editor 任务总览（`02.08.04.16.02.06`）。
- `02.08.04.16.02.06.01` Opening the Pattern Editor — 打开编辑器（`02.08.04.16.02.06.01`）。
- `02.08.04.16.02.06.02` Configuring the layout of the editor — layout 决定显示哪些 signal、用什么格式（`02.08.04.16.02.06.02`）。
- `02.08.04.16.02.06.03` Importing layouts of the Pattern Editor — 导入 layout，避免重建并可跨 device 共享（`02.08.04.16.02.06.03`）。
- `02.08.04.16.02.06.04` Editing patterns — 插入/删除 vector line、复制粘贴 vector cell、编辑 cell、复制 event/test point（`02.08.04.16.02.06.04`）。
- `02.08.04.16.02.06.05` Finding and replacing pattern cells — 查找/替换单个或连续 vector cell，也可搜注释（`02.08.04.16.02.06.05`）。
- `02.08.04.16.02.06.06` Replacing failed state characters for golden device — 对 golden device 应用 pattern 以调试（`02.08.04.16.02.06.06`）。
- `02.08.04.16.02.06.07` Going to a signal or vector — 跳到 signal、tester vector/cycle、X-vector/cycle 或 Index/Call number（`02.08.04.16.02.06.07`）。
- `02.08.04.16.02.06.08` Locating events and their test points — event/test point 用蓝色 annotation 标在 ruler 上（`02.08.04.16.02.06.08`）。
- `02.08.04.16.02.06.09` Renaming events and test points — 在 Rename Event 对话框改名（`02.08.04.16.02.06.09`）。
- `02.08.04.16.02.06.10` Inserting, editing, and deleting sequencer instructions — 在 Instruction 列插入/编辑/删除 sequencer instruction；需 collapsed mode（`02.08.04.16.02.06.10`）。
- `02.08.04.16.02.06.10.01` Inserting counted match loops — 在 Pattern Editor 中插入 counted match loop（`02.08.04.16.02.06.10.01`）。
- `02.08.04.16.02.06.10.02` Sequencer instructions — 每个 vector 默认 `GENV`；sequencer instruction 集合的说明（`02.08.04.16.02.06.10.02`）。
- `02.08.04.16.02.06.11` Inserting and editing comments — header Comment 列与 signal Comments 列联动（`02.08.04.16.02.06.11`）。
- `02.08.04.16.02.06.12` Copying patterns — Pattern Explorer 与 Pattern Editor 可复制整个 pattern 或任意区域（`02.08.04.16.02.06.12`）。
- `02.08.04.16.02.06.13` Displaying failure data — 分析哪个 cycle 在哪个 signal 失败（`02.08.04.16.02.06.13`）。
- `02.08.04.16.02.06.14` Masking and activating signals — 调试时屏蔽已知问题（如坏 pin）（`02.08.04.16.02.06.14`）。
- `02.08.04.16.02.06.15` Align Display — 对齐各结果分析工具的显示（`02.08.04.16.02.06.15`）。
- `02.08.04.16.02.06.16` Creating a Digital Source setup — 创建含 VVC 的 Digital Source setup（`02.08.04.16.02.06.16`）。
- `02.08.04.16.02.06.17` Creating a Digital Capture setup — 高速捕获大量不可预测数字输出（`02.08.04.16.02.06.17`）。
- `02.08.04.16.02.06.18` Changing the x-mode area — 基于 xN 示例修改 signal 的 x-mode area（`02.08.04.16.02.06.18`）。
- `02.08.04.16.02.06.19` Adding synchronization markers — 在某个 pin 的 vector 上添加 sync marker（`02.08.04.16.02.06.19`）。
- `02.08.04.16.02.06.20` Removing synchronization markers — 删除或移动 sync marker（`02.08.04.16.02.06.20`）。
- `02.08.04.16.02.07` Pattern Editor quick reference — content assist 的用法（`02.08.04.16.02.07`）。
- `02.08.04.16.03` Multiport Burst Editor — 访问 multiport burst 与 port burst；Overview 页 + port burst 页 + sync group 页（`02.08.04.16.03`）。
- `02.08.04.16.03.01` Creating a multiport burst — Pattern Explorer 中新建 multiport burst（`02.08.04.16.03.01`）。
- `02.08.04.16.03.02` Creating and assigning a port burst — 新建 port burst 并分配到 multiport burst 与 sync group（`02.08.04.16.03.02`）。
- `02.08.04.16.03.03` Editing a multiport burst setup — 插入 CALL/NOP、改 sync group；通用编辑规则（`02.08.04.16.03.03`）。
- `02.08.04.16.03.04` Working with sync groups — sync group 强制 port 同时开始；不能共享 pin；expanded mode 显示 fail 信息与时间线（`02.08.04.16.03.04`）。
- `02.08.04.16.04` Pattern Reference Information — pattern 与 pattern tools 的参考信息总览（`02.08.04.16.04`）。
- `02.08.04.16.04.01` Definitions: Vector, Pattern, Burst, etc. — Vector / X-vector / Pattern / Label / Port / Burst / Port Burst / Multiport Burst / Sequencer instruction 定义（`02.08.04.16.04.01`）。
- `02.08.04.16.04.02` Editor status line — 状态行显示选中项、行号与总行数（`02.08.04.16.04.02`）。
- `02.08.04.16.04.03` Dependencies Between the Timing Setup and the Vector Setup — timing 未完成不能生成 vector；vector 完成后不能大改 timing（`02.08.04.16.04.03`）。
- `02.08.04.16.04.04` The function of patterns — test 由 pattern（label）及关联 vector 构成；多个 test 在内存中连续排列（`02.08.04.16.04.04`）。
- `02.08.04.16.04.05` Wavetables — wavetable 的 pin/group、physical index、action 与 device cycle name；调试用 wavetable（`02.08.04.16.04.05`）。
- `02.08.04.16.04.05.01` Function of the base wavetable — base wavetable 用于显示/编辑，primary wavetable 用于执行（`02.08.04.16.04.05.01`）。
- `02.08.04.16.04.05.01.01` The Significance of the Base Waveform Set — Vector Memory 的解释依赖 waveform set；base waveform set 是 Vector Setup 解释当前内存内容的依据（`02.08.04.16.04.05.01.01`）。
- `02.08.04.16.04.06` How Vectors are Stored in Sequencer Memory — Pin Scale 的 RDRAM 组织：64-bit word、8 个 8-bit frame、每 vector 8 bit、256 个 physical waveform index（`02.08.04.16.04.06`）。
- `02.08.04.16.04.07` X Modes — 把多个 device cycle 放进一个 test system cycle；X4/X8 与 drive/receive edge 数（`02.08.04.16.04.07`）。
- `02.08.04.16.04.08` Data Queue — data queue 的作用、填充指导、`FLQU` 与 `DQUE?`（`02.08.04.16.04.08`）。
- `02.08.04.16.04.09` Protocol pattern specifics of the Pattern Explorer — protocol transaction 生成的 pattern 与普通 pattern 一样显示（`02.08.04.16.04.09`）。
- `02.08.04.16.04.10` Protocol pattern specifics of the Pattern Editor — 编辑器增强以查看 protocol transaction（`02.08.04.16.04.10`）。
- `02.08.04.16.04.10.01` Reconstructing transaction signals — 从模拟 pattern 或非 protocol pattern 的 vector 重建 transaction（`02.08.04.16.04.10.01`）。
- `02.08.04.16.04.11` Changing pattern tool preferences — 调整 error annotation、error marker 等显示选项（`02.08.04.16.04.11`）。

## L1 — Firmware / Setup Command

命令子树 `02.06.07.02` 共 40 篇、40 条命令（带 `?` 的查询形式与命令形式合为同一条）。以下逐条给出「命令名 + 一句作用 + 出处」；重要命令附文档中的最小示例。

### 标签 / 内存区

- **`DMAS, DMAS?`** — 定义或扩展各 port 的 sequencer program 逻辑内存区；查询返回已用/剩余内存。文档事实：命令侧自 7.0.1 起只支持 `SQPG` area；`PARA` / `PPSQ` / `RSLT` / `MFRE` / `MFRP` 等是查询侧能力（`02.06.07.02.13`）。示例中 `DMAS? SQPG,SM,(@)` 先返回当前末尾 `9`，再把新规模设为 `13`：
  ```
  DMAS SQPG,SM,13,(@)
  ```
- **`SAOF, SAOF?`** — 切换操作模式（`ZERO` / `APP` / `LOAD` / `TMLD` / `EGRP` / label 名），并影响 `DMAS` 是“定义”还是“追加”（`02.06.07.02.23`）。
  ```
  SAOF APP
  SAOF ZERO
  ```
- **`SQLB, SQLB?`** — 定义 label 的名字、类型、sequencer program 起止命令号、base waveform set/wavetable 与 port；也可用同一组参数改名。文档事实：`SQLB` 覆盖 sequencer area 的既有片段，**不能扩大** sequencer area，且片段不得与既有程序重叠；要追加 MAIN/SVEC label 应先用 `APTS`（`02.06.07.02.27`）。
  ```
  SQLB "test_1",MAIN,4,8,"table1"
  SQLB "test_2",MAIN,9,12,"table1"
  ```
- **`SQLA, SQLA?`** — 给 label 关联属性：`PARA_MEM`（`SM` / `NONE` / `SHMEM` / `HSER`）与 `PARA_MCTX`（pin mode context）；memory type 只能在 label 还没有 GENV/RPTV 时改（`02.06.07.02.26`）。
  ```
  SQLA LBL,"test_2","PARA_MEM=SHMEM"
  ```
- **`DLTS`** — 删除指定 label，并重排 vector data 位置，避免内存空洞（`02.06.07.02.12`）。
  ```
  DLTS "MPBU_port_1_port_2",(port_1)
  ```
- **`APTS`** — 高层追加 label：自动扩大 sequencer area、把 STVA 指到 vector area 末尾；只支持 `MAIN` / `SVEC` / `DSRC`（`02.06.07.02.02`）。
  ```
  APTS "test_2",MAIN,"table1"
  ```
- **`TSTL, TSTL?`** — 激活 label 进入编辑状态；大量修改 sequencer/vector area 的命令都要求先 `TSTL`（`02.06.07.02.34`）。
  ```
  TSTL "test_2",(@)
  ```
- **`BLUP`** — 修改 label 的“已更新/已变更”状态（`UPTD` / `CHNG`），只接受 `LBL` 类型；文档明确要求小心使用（`02.06.07.02.04`）。
  ```
  BLUP "test",LBL,UPDT,
  ```

### Sequencer 控制

- **`SQSL, SQSL?`** — 把已定义的 `MAIN` / `BRST` / `MPBU` label 设为 start label，供 `FTST?` 执行；支持 site-specific start label（`02.06.07.02.29`）。文档示例中 `SQSL? TYPE` 的返回为 `SQSL "test_1",MAIN,(@)`：
  ```
  SQSL "test_1"
  ```
- **`SQST, SQST?`** — 控制 sequencer 集合状态：`OFF` / `HALT` / `BRK` / `ABRT` / `CBRK` / `RUN`，可按 execution context 指定（`02.06.07.02.30`）。
  ```
  SQST RUN
  ```
- **`SQGB, SQGB?`** — 同时控制 sequencer 终止方式与 Error Map 记录方式（`ACQF` / `ACFF` / `EL` / `ELPT` / `EMPS` / `SE` / `SEEL` / `STSQ` / `STRD` / `STSV`）（`02.06.07.02.25`）。
  ```
  SQGB STSQ,30,(P2)
  ```
- **`SQTO, SQTO?`** — 设置 sequencer timeout，单位秒；默认 900，范围 0.001 到 2147483（`02.06.07.02.31`）。
  ```
  SQTO 3000
  ```
- **`FTSM, FTSM?`** — 为下一次 sequencer run 设置 cycle mask：`run_to`、`mask_before`、`mask_after`；`SET` 保存并在 `CLEAR` 时恢复原 `SQGB` 值（`02.06.07.02.17`）。文档说明用 `FTSM SET,,10,20` 可只保留 cycle 10 到 20 的结果。
- **`SREC, SREC?`** — 屏蔽/激活/保存/恢复指定 receiver pin，使其不参与全局 PASS/FAIL（`ACT` / `X` / `STOR` / `RSTO`）（`02.06.07.02.32`）。
  ```
  SREC X, (D1, D2, D3, D4)
  ```
- **`RSET`** — 按文件类型加载 power-on default：`DPS` / `FCR` / `LEV` / `TIM` / `VEC` / `ATR` / `PDL` / `CAL` / `MTPP`；`RSET VEC` 清空 vector setup（`02.06.07.02.22`）。
  ```
  RSET TIM
  ```

### Sequencer program 与 sequencer construct 编辑

- **`SQPG, SQPG?`** — 把 sequencer instruction 写入 sequencer area 的既有命令行；**覆盖**现有指令，且不修改 vector area；查询可返回单行/区间/全部（`02.06.07.02.28`）。
  ```
  SQPG 7,GENV,9,,,(@)
  SQPG 6,RPTV,6,5,,(@)
  ```

#### SQPG 可写入的 sequencer instruction（文档事实，`02.06.07.02.28`）

| 指令 | 一句作用 |
|---|---|
| `BEND` | 标记 normal burst 或 multi-port burst label 的结束。 |
| `BRKV` | 生成 break vector；`param_1` 数量、`param_2` 等待 ns。 |
| `CALL` | 在 burst / multiport burst 中调用 MAIN label；label 名放 `param_2`。 |
| `CLEV` | 改变 level set；`param_1` 为 set 号或 `PRM`。 |
| `COGO` | 条件跳转；只能在 SVEC 中用，返回地址不入调用栈。 |
| `CTIM` | 改变 timing set；`param_1` 为 set 号或 `PRM`。 |
| `FLQU` | 向 data queue 插入 fill break vector。 |
| `GENV` | 生成并行 vector；`param_1` 为数量。 |
| `JMPE` | 依 error flag 条件跳转到 SVEC 子程序。 |
| `JPPS` | 跳转到 per-pin 子程序；被计为一个 logical vector。 |
| `JSUB` | 跳转到 vector 类型子程序或 scan 子程序。 |
| `JTIN` | 在 Smart Scale port 上启动/停止 jitter injection。 |
| `LBGN` | counted 或 endless loop 的开始；counted loop 的次数放 `param_1`。 |
| `LEND` | 循环结束。 |
| `LPBK` | 启动 SmartLoop™ 测试。 |
| `MACT` | counted match loop 开始；`param_1` 为最大失败循环数，可带 `CONTINUE` / `TIL_FAIL_STOP` / `TIL_FAIL_CONT`。 |
| `MBGN` | timed（old style）match loop 开始。 |
| `MEAS` | 执行已用 `MSET` 下载的 PPMU measurement set。 |
| `MEND` | timed match loop 结束。 |
| `MJPE` | timed match loop 中匹配成功时跳出。 |
| `MRPT` | counted match loop 中 compare vector 与 dummy vector 的分界；指定 dummy vector 数。 |
| `NOP` | 不操作 DUT，但提高 instruction density。 |
| `PRBS` | 启动 PRBS 测试。 |
| `RETC` | 依 error flag 从 SVEC 条件返回；可重置 flag。 |
| `RGOP` | 寄存器算术操作（`RESET` / `INC` / `INC_LOWER` / `INC_UPPER` / `SHL`）。 |
| `RPTJ` | 重复紧随其后的 `JSUB`，次数放 `param_1`。 |
| `RPTV` | 重复一段 vector；`param_1` 长度、`param_2` 重复次数。 |
| `RSJP` | 从 `SJMP` 子程序返回（仅向下兼容）。 |
| `RSUB` | 从 SVEC 子程序返回。 |
| `SRCV` | source vector block 开始；与 `SSRC` 配合。 |
| `SSRC` | 指定含 source pin vector 的 DSRC label。 |
| `STOP` | 停止 label；每个 MAIN label 必须有。 |
| `STSA` | label header 的 scan vector 地址指令；每个 MAIN label 必须有。 |
| `STVA` | label header 的 parallel vector 地址指令；MAIN 与 SVEC 必须有；地址须为 8 的倍数。 |
| `TMUA` | 为 pattern port 的所有 pin arm TMU per pin。 |
| `WAIT` | 生成数量最接近指定 ns 的 break vector；范围 0 到 5592402。 |
| `WTER` | timed match loop 中遇错等待。 |
| `XACT` | 执行一条 DC waveform；waveform 名放 `param_2`。 |

文档事实：timed match loop 的指令顺序必须是 `WTER` → `MBGN` → `GENV` → `WTER` → `MJPE` → `MEND`；counted match loop 必须是 `MACT` → `GENV` → `MRPT`。`MEND` 时会检查前序指令，不满足则 `MBGN` / `MJPE` 退化为 `NOP`（`02.06.07.02.28`）。
- **`INSI`** — 在命令号前插入指定数量的 `NOP` 占位行，之后用 `SQPG` 覆盖（`02.06.07.02.20`）。
  ```
  INSI 358, 12
  ```
- **`DELI`** — 从 sequencer area 删除指令；若删的是 vector generating instruction，只删指令、不删对应 vector（`02.06.07.02.09`）。
  ```
  DELI 7,1
  ```
- **`INGV`** — 插入一条 GENV 并在 vector area 中为新指令腾出空间，保持后续指令的 vector 指向正确；是插入 vector generating instruction 的正确入口（`02.06.07.02.19`）。
  ```
  INGV 3,11
  ```
- **`APDV`** — 在 `GENV` / `RPTV` / `MRPT` construct 末尾追加 vector（`02.06.07.02.01`）。
  ```
  APDV 2,25
  ```
- **`DELV`** — 从 `GENV` / `RPTV` / `MRPT` construct 末尾删除 active vector；若删满整个 construct，该指令变成 `NOP`（`02.06.07.02.10`）。
  ```
  DELV 2,25
  ```
- **`SPGV`** — 把一个 `GENV` construct 在指定 logical vector 处拆成两个 `GENV` construct（`02.06.07.02.24`）。
  ```
  SPGV 7
  ```
- **`CNGV`** — 把两个连续的 `GENV` construct 合并成一个，长度相加（`02.06.07.02.07`）。
  ```
  CNGV 2
  ```
- **`CPYV`** — 在同一个 sequencer construct 内复制 active vector 到另一位置（`02.06.07.02.08`）。
  ```
  CPYV 12,9,3,(S0_1)
  ```
- **`NODV?`** — 返回当前 `TSTL` 选中 label 的 active vector 数（`02.06.07.02.21`）。
- **`VPAR?`** — 返回指定 vector 范围内各 sequencer instruction 的命令号及其第一个受影响 vector 的 logical address；non-linear 或 match 序列不完整时返回 `NISQ`（`02.06.07.02.40`）。
  ```
  VPAR? 0,15
  ```
- **`GETA?`** — 按 logical vector number 返回该 vector 在 vector area 中的绝对地址；结果可作 `VECD` 的输入（`02.06.07.02.18`）。
  ```
  GETA? VEC,,9,(S0_1)
  ```
- **`VDCG?`** — 检查组内 device cycle 是否在每个 pin 的 waveform set 中定义且长度一致；`ALL` 比较全部 device cycle，`FDC` 比较第一个 device cycle；7.10 的 `dev_cyc_len` 恒为 1（`02.06.07.02.35`）。
  ```
  VDCG? 1,ALL,(inputs)
  ```

### Vector / device cycle 下载

- **`VECD, VECD?`** — 以未压缩二进制格式按绝对地址把 vector data 下载到 pin 的 vector area；7.x port-specific setup 必须指定 port，地址与长度须为 8 的倍数（`02.06.07.02.39`）。
  ```
  VECD? PARA,SM,0,16,(OUT1)
  ```
- **`VECC, VECC?`** — 与 `VECD` 相同，但输入/输出为压缩二进制格式，通常下载更快（`02.06.07.02.38`）。
  ```
  VECC? PARA,ALL,0,,(S0)
  ```
- **`VDCP, VDCP?`** — 高层 vector data 传输：按 device cycle 名与四个 direction parameter，在 logical vector number 处写入 physical waveform DC/DC power unit；查询反向显示（`02.06.07.02.37`）。
  ```
  VDCP 0,"DNRZ",1,,F10,N,N,N,(S0_1)
  ```
- **`VDCN`** — 用 device cycle 的 default data parameter（drive `F00`、expected `FX`）下载 vector；`FDC` 表示取该 pin 的第一个 device cycle；按 logical vector number 与 repeat count 操作（`02.06.07.02.36`）。
  ```
  VDCN 93, "EXAMPL", 1, 15, (@)
  ```

### Vector 注释

- **`CMNT, CMNT?`** — 在 port 级按 active vector 计数添加/查询注释；可跨 label 边界（`02.06.07.02.05`）。
  ```
  CMNT 15,"Start of test_2"
  ```
- **`BCMT, BCMT?`** — 以二进制格式批量下载/读取指定 vector 范围的注释；只能在 `LOAD` 或 `APP` 模式使用，默认 `EDIT` 模式不行（`02.06.07.02.03`）。
  ```
  BCMT?
  ```
- **`TCMT, TCMT?`** — 在 `TSTL` 激活的 label 内按 logical vector 号插入/读取注释；空文本表示删除（`02.06.07.02.33`）。
  ```
  TCMT 2063,"Start of test 2"
  ```
- **`CMVC`** — 在 label 内移动注释范围，或删除源与目标之间的注释；`vect_length` 为 0 表示只删除（`02.06.07.02.06`）。
  ```
  CMVC 0,4,2
  ```

### Per-pin subroutine

- **`DLPP`** — 删除一个 per-pin subroutine（`02.06.07.02.11`）。
  ```
  DLPP "summer"
  ```
- **`DPPC, DPPC?`** — 定义 PPSS label 的配置：`SMSTART` / `SMLEN` / `VMSTART` / `VMLEN` / `RELOC` / `MWAIT` / `MAXLEN`；用于 memory test 与 APG pattern translator（`02.06.07.02.14`）。
- **`DPPS, DPPS?`** — 定义 Per-Pin Subroutine label 与 per-pin cycle length；文档明确它由 MTL compiler 生成，不要从 hpt 执行，只可查询（`02.06.07.02.15`）。
- **`DPSA, DPSA?`** — 定义 per-pin subroutine 在每个 pin 上的 sequencer 起始地址；同样由 MTL compiler 生成，不要从 hpt 执行，只可查询（`02.06.07.02.16`）。

## L2 — Test Method API

文档事实：本次找到的 pattern 相关 L2 主要分四类——在 pattern 内执行 DC 测量（`PATTERN_CONTROLLER` / `PATTERN`）、读写 vector variable（`VECTOR`）、控制 sequencer 与 execution context（`SEQUENCER_STATUS` / `SEQUENCER_CONTEXT`）、以及执行 label 并取结果（`FUNCTIONAL_TEST` / `START_TEST` / `EXECUTE_TEST` / `GET_FUNCTIONAL_RESULT`）。**本次未找到专门用于定义 label 或直接写 vector area 的 C++ Test Method API**；文档给出的路径是在 test method 中用 `FW_TASK` 执行本页 L1（`02.07.04.01.77`）。

- **`PATTERN_CONTROLLER`** — 在 pattern 内执行 DC Scale DC / PPMU / BADC 测试；`label()` 取得 `PATTERN` 子容器，`setup()` 把 DC task 写入子 pattern，`execute()` / `getPassFail()` 执行并取结果（`02.07.04.01.142`）。
- **`PATTERN`** — 不能直接实例化，只能由 `PATTERN_CONTROLLER::label()` 取得；持有某个 subpattern 的 DC task / DC waveform（`02.07.04.01.142.01`）。
- **`VECTOR`** — vector variable 的数据容器，`setVectors()` / `getVectors()` / `upload()` 等读写 vector variable；用于 digital capture 数据搬运或 digital source 下载，**不是**本阶段 label 的 vector area 本身（`02.07.04.01.269`）。
- **`SEQUENCER_STATUS`（系统对象 `Sequencer`）** — `run()` / `abort()` / `stopCycle()` / `stopVector()` / `isRunning()`；不支持 execution context，只能全局启动/中止（`02.07.04.01.204`）。
- **`SEQUENCER_CONTEXT` / `SEQUENCER_CONTEXT_ITEM`** — 用 port 列表定义 execution context，`add()` / `erase()` / `apply()` / `reset()` 下载到 firmware（`02.07.04.01.201`、`02.07.04.01.202`）。
- **`PRIMARY_STATUS::label()`** — 指定要激活的 sequencer start label；multi-port 时可指定 multiport burst label（`02.07.04.01.167`）。
- **`FUNCTIONAL_TEST()`** — 启动 digital sequencer、把 vector 送给 DUT 并比较输出；结果由 `GET_FUNCTIONAL_RESULT()` 或 `TEST` 取回（`02.07.04.01.75`）。
- **`START_TEST()`** — 从 start label 启动 sequencer，从 `BRK` 进入 `RUN`，不等待完成；需与 `WAIT_TEST_DONE` 配合（`02.07.04.01.235`）。
- **`EXECUTE_TEST()`** — 执行测试；文档将其与 `START_TEST()` 对比，后者不等完成（`02.07.04.01.65`）。
- **`GET_FUNCTIONAL_RESULT()`** — 读取 functional test 的 PASS/FAIL 结果（`02.07.04.01.88`）。
- **`FW_TASK`** — 在 test method 中执行一条或多条 firmware command；是本阶段 L1 在 C++ test method 内的直接入口（`02.07.04.01.77`）。
- **`PatternPort` / `playPattern()` / `setWaitTemplatePatternName()`** — CCT multiport sequencer synchronizer 的 pattern port API；`playPattern()` 把 PatternPort label 嵌入 input burst pattern label（`02.07.04.01.143`、`02.07.04.01.149`、`02.07.04.01.223`、`02.07.04.01.185`）。
- **`DigitalCapturePort::setDefaultPattern()`** — 给 digital capture port 设置默认 pattern vector state；带 `repeatNum` 的重载可指定 pattern 重复次数。属 pattern 相邻能力，页面不展开其流程（`02.07.04.01.33`、`02.07.04.01.34`）。

文档事实：pattern-based programming 指硬件由 pattern-sequencer 控制，与由 workstation 直接控制的 code-based programming 相对；DC event 可通过 `PATTERN_CONTROLLER` 或 Pattern Editor 插入已有 pattern（`02.07.01.01.02`）。

## L3 — 外部控制

**L3 入口是横切的，能力面按阶段分族。** Test suite control API（分类号 `02.09.01.14`）与 TPI（分类号 `02.09.01.09`）是横切入口；本阶段的专属族是 `TestsuiteProxy` 的 start label 绑定（`setSequencerLabel` / `getSequencerLabel`）与 TPI 的 `dm_vector` / `dm_pattern_master_file` 文件族。

- **Test suite control API / `TestsuiteProxy`** — `setSequencerLabel(const std::string& value)` 设置 test suite 的 sequencer label，值必须是 `"\"label_name\""` 形式；`getSequencerLabel()` 读取当前值（`02.09.01.14`、`02.09.01.14.02.01`、`02.09.01.14.02.01.29`、`02.09.01.14.02.01.09`）。这是本阶段在 test suite 层的直接对应接口。
- **TPI / `DataManager`** — 文件 ID `dm_vector` 表示 vector setup，`dm_pattern_master_file` 表示 pattern master file；操作包括 `dm_load` / `dm_save` / `dm_merge` / `dm_append` / `dm_pload` / `dm_plinit` / `Dm_blload` / `Dm_pldump` / `Dm_ustate` / `Dm_labsave` 等。文档特别说明：`dm_pattern_master_file` 只保存更新过的 pattern 到新 master file；要写回既有文件用 `dm_vector`（`02.09.01.09`、`02.09.01.09.02`）。
- **TPI / `HpFwTask`** — C 程序直接执行 firmware command 的入口；可用来执行本页 L1，但不会自动处理 site focus（`02.09.01.09`、`02.09.01.09.21`）。
- **HVM API** — 提供 SmarTest session 管理、test execution、硬件信息、校准诊断等外部控制/监控；本次找到的是通用 test program/testflow 控制，**本次未找到 pattern/vector 专属的 HVM 成员**（`02.09.01.10.01`）。
- **SmartShell** — 在 7.10.3 不存在；文档写 `Introduced in SmarTest 8.2.5`，且该章正文只有 PDF 外链（`02.15_SmartShell`）。因此本页不把 SmartShell 当作可用的 L3 接口。

## 产物

- **vector setup 文件** — 可以把所有 label 放在一个大的 vector setup 文件里；该文件必须位于当前 device 的 `vectors` 子目录（`02.06.07.01.05`）。
- **pattern master file** — 文件头 `hp93000,pattern_master_file,0.1`；包含 `path:` 与 `files:` 段，列出 pattern 文件名与路径；注释以 `-- ` 开头；文件本身必须位于 `<device>/vectors`。`path` 默认是当前 device 的 `vectors`；若显式指定，相对路径的参考目录是 device 的 `waste` 子目录，例如 pattern 文件在 `vectors/sample` 下时要写 `./vectors/sample`。文档事实：该文件必须手工创建（或用 ASCII interface）（`02.06.07.01.05`）。
- **pattern 文件** — pattern master file 引用的单个 pattern 文件；文档示例为 `sample1.binl`、`sample2.binl.gz`、`sample3.binl.gz`（`02.06.07.01.05`）。Pattern Explorer 对 pattern master file 使用 `*.pmfl` 后缀（`02.08.04.16.01`）。
- **单一大 pattern 文件** — 文档把 `allvec.bin` 作为“全部 pattern 在一个文件”的生产推荐形态；pattern master file 下载时间约多 5% 到 20%（最坏情况）（`02.08.04.16.01.15`）。
- **SREC 文件** — `../vectors/.<Pattern-Name>.SREC`，保存 receiver mask 设置；`SREC` 查询/报警排查会引用它（`02.06.07.02.32`）。
- **内存中的 label / sequencer area / vector area** — label、sequencer program、physical waveform DC/DC power unit 最终位于 channel memory 的 sequencer area 与 vector area；vector area 按 port 划分（`02.06.07.01.02`、`02.06.07.01.03`）。
- **binary vector data 格式** — vector area 以 64-bit word 组织，每 word 分 8 个 8-bit data unit，每 unit 存一个 physical waveform index，最大 255（`02.06.07.01.04`）。

## 验证

以下均为文档给出的查询/检查入口，不是本页发明的方法。

- **标签定义**：`SQLB?` 查询 label 名、类型、起止命令号、base wavetable 与 port（`02.06.07.02.27`）。
- **sequencer program**：`SQPG?` 返回单行、区间或整个 port 的 sequencer area，可与预期指令逐行比对（`02.06.07.02.28`）。
- **内存使用**：`DMAS? SQPG,SM,(port)` 返回 sequencer area 当前末尾；`DMAS? PARA,SM,PER_PORT,(port)` 返回 vector area 当前末尾；`DMAS? MFRE` / `MFRP` 返回可追加的 vector 数或 pool 余量（`02.06.07.02.13`）。
- **vector 数量**：`NODV?` 返回当前 label 的 active vector 数（`02.06.07.02.21`）。
- **指令与 vector 对应**：`VPAR?` 返回指定范围内指令号与首个受影响 vector；返回 `NISQ` 表示 sequencer program 不满足上下文条件、Vector Setup 无法显示（`02.06.07.02.40`）。
- **绝对地址**：`GETA?` 返回 logical vector 的绝对地址与剩余 active vector 数（`02.06.07.02.18`）。
- **device cycle 一致性**：`VDCG?` 检查同一 pin 组的 device cycle 是否都存在且长度一致（`02.06.07.02.35`）。
- **vector 数据回读**：`VECD?` / `VECC?` 按地址与长度回读 vector area，可与下载数据比对（`02.06.07.02.39`、`02.06.07.02.38`）。
- **注释**：`CMNT?`（port 级）、`TCMT?`（label 级）、`BCMT?`（二进制批量）回读注释（`02.06.07.02.05`、`02.06.07.02.33`、`02.06.07.02.03`）。
- **start label / 状态 / 终止模式**：`SQSL?` 返回 start label（可加 `TYPE` / `ALL`）；`SQST?` 返回当前最大状态；`SQGB?` 返回终止/Error Map 设置；`FTSM?` 返回当前 cycle mask（`02.06.07.02.29`、`02.06.07.02.30`、`02.06.07.02.25`、`02.06.07.02.17`）。
- **执行 label**：`SQSL` + `SPRM` + `FTST?`，`FTST?` 返回全局 PASS/FAIL；`VCYC?` 可检查当前 start label 的用户 cycle 是否被 break cycle 补齐到 8 的倍数（`02.06.07.01.07.04`）。
- **data queue**：`DQUE?` 返回上一次 sequencer run 期间 data queue 的最小 level，用于判断是否需要 `FLQU`（`02.06.07.01.09.03`）。
- **GUI**：Pattern Editor 用 base wavetable 把 vector area 中的 physical waveform index 翻译成 device cycle name；无法翻译时显示 `?`（`02.08.04.16.04.05.01`、`02.08.04.16.04.05`）。Multiport Burst Editor 的 fail 信息与时间线同步只在 expanded mode 显示，且需先定义 start label 或跑过 testflow（`02.08.04.16.03.04`）。
- **建 multiport burst 的结果**：Pattern Explorer 中出现 `Type = MPBurst` 的项；port burst 文件在显式保存 multiport burst 之前不会写入指定目录（`02.08.04.16.01.04`）。
- **建 pattern 的结果**：新 pattern 只有一行 vector，含 `STOP` 指令（`02.08.04.16.01.02`）。
- **Fast Sync 的结果**：文档写 site scaling synchronization 的 overhead 显著降低（`02.06.07.01.08.04.03.03.01`）。

## 常见错误

- **未用 `TSTL` 激活 label。** `APDV`、`CMVC`、`CNGV`、`CPYV`、`DELI`、`DELV`、`INGV`、`INSI`、`SPGV`、`VDCN`、`VDCP`、`VPAR?` 等都要求先 `TSTL`；错误信息通常包含 “No label has been activated for editing” / “No label has been selected for editing”（`02.06.07.02.01`、`02.06.07.02.06`、`02.06.07.02.07`、`02.06.07.02.08`、`02.06.07.02.09`、`02.06.07.02.10`、`02.06.07.02.19`、`02.06.07.02.20`、`02.06.07.02.24`、`02.06.07.02.36`、`02.06.07.02.37`、`02.06.07.02.40`）。
- **对错误的 construct 类型执行命令。** `APDV` 要求 `GENV` / `RPTV` / `MRPT`；`SPGV` 要求 `GENV`；`DELV` 开头写 `GENV` / `RPTV` / `MRPT`，但同篇 Errors 段只列 `GENV` / `RPTV`——**文档自相矛盾，原文如此**，使用前需按目标版本实测确认（`02.06.07.02.01`、`02.06.07.02.10`、`02.06.07.02.24`）。
- **用 `SQPG` 插入 GENV 而不修 vector area。** `SQPG` 只覆盖指令、不调整 vector area，后续 GENV/RPTV 会指向错误数据，甚至跨到下一个 label；插入 vector generating instruction 应使用 `INGV`（`02.06.07.02.28`、`02.06.07.01.07.03.01`）。
- **用 `DELI` 删 vector generating instruction。** `DELI` 不删对应 vector，后续指令会指错；应先用 `DELV` 删 vector 子段，再用 `DELI` 删变成 `NOP` 的指令（`02.06.07.01.07.03.02`、`02.06.07.02.09`）。
- **地址不是 8 的倍数。** `VECD`/`VECC` 要求地址与长度都是 8 的倍数；`STVA` 地址也必须是 8 的倍数；否则报错（`02.06.07.02.39`、`02.06.07.02.38`、`02.06.07.01.04`）。
- **7.x setup 下载 vector 时漏 port。** port-specific vector area 必须指定 port；旧格式可省略但由命令分析 STVA 定位（`02.06.07.02.39`、`02.06.07.02.38`、`02.06.07.01.03.01`）。
- **缺 vector data。** 若某个 pattern 在所有 pin 上都没有完整 vector data，SmarTest 报 error；若只在部分 pin 缺，报 warning；缺 data 的 pin 行为依赖 session 历史，可能被错误解释（`02.06.07.01.03.02`）。
- **多 port setup 不完整。** timing setup 未覆盖所有具备 sequencing 能力的 pin 会出 `W280`；vector port 的 pin 没有对应 timing port 会出 “pins with vectors running at undefined speed”（`02.06.07.01.08.05.03.02.02`）。
- **同一 sequencing group 内 match loop 失败 + `CTIM`/`CLEV`。** 失败 match loop 的 port 停止，其他 port 在下一个 `CTIM`/`CLEV` 处无限等待；match loop 应独占 sequencing group（`02.06.07.01.10.01.01`）。
- **match loop 与外围 label 的 8-cycle 边界。** match loop 起始 block 中属于外围 label 的 cycle 不会进 Error Map；应在 match loop 前插至少 7 个无 compare 的 buffer vector（`02.06.07.01.08.04.03.01.01`）。
- **data queue 被抽空。** 指令密度高、vector generating instruction 太短时 queue 会空，系统报出 label / vector / cycle / command number；可用 `FLQU` 填 break vector、优先 `RPTV`、加长 vector generating instruction，并用 `DQUE?` 检查（`02.06.07.01.09.03`、`02.08.04.16.04.08`）。
- **`SREC` 报警。** 报告窗口出现 `WARNING: SREC -name "<Pin-Name>" unknown` 时，检查该 pin 是否在 pin configuration 中；若不需要，从 `../vectors/.<Pattern-Name>.SREC` 删除（`02.06.07.02.32`）。
- **`VPAR?` 返回 `NISQ`。** 表示 sequencer program 不满足上下文条件（vector 非线性使用、`WTER` 无 `MBGN`、`MJPE` 无 `MEND` 等），该 label 无法被 Vector Setup 显示（`02.06.07.02.40`）。
- **`DPPS` / `DPSA` 被从 hpt 执行。** 两者由 MTL compiler 生成；文档明确不要从 hpt utility 执行，只可查询（`02.06.07.02.15`、`02.06.07.02.16`）。
- **Pattern Editor 打不开超大 pattern。** 文档明确超过 500,000 条指令的 pattern 不能在 Pattern Editor 中打开（`02.08.04.16`）。
- **F330 scan pattern 不受支持。** 自 7.0.1 起 F330 scan 已 obsolete，Eclipse-based pattern tools 会报 `Unsupported pattern type` / `WARNING: FW mnemonic [SCAN] not supported for label type`；需用 6.5.2 之前的版本查看（`02.08.04.16`）。
- **`SQLB` 重名 / 名字过长。** 同一 label 重复定义、名字超过 128 字符、base waveform set 超出 `WSUS` 范围都会报错（`02.06.07.02.27`）。
- **`SQSL` 与共享 channel。** 若一个 channel 被多个 site 共享，`SQSL` 会报错（`02.06.07.02.29`）。
- **文档冲突：data queue 容量与填充率。** `02.06.07.01.09.03` 写 Pin Scale 的 data queue 为 `832 = 104 * 8` 个 vector instance、最大填充率 1 instance / 0.625 ns；`02.08.04.16.04.08` 写 data queue 为 `512 = 64 * 8` 个 vector、固定填充率 1 vector / 3.14 ns。两篇给的是不同数字，本页不自行选定；实际机台需按硬件型号与版本确认（`02.06.07.01.09.03`、`02.08.04.16.04.08`）。

## 下一步

下一步是 `[[testmethod]]`：本阶段只把 label、vector data 与 sequencer program 准备好；要让这些 label 在 test suite 中被执行，需要在 test method / test suite 中绑定 start label（L3 的 `TestsuiteProxy.setSequencerLabel()`，或 L2 的 `PRIMARY_STATUS::label()`），再由 `FUNCTIONAL_TEST()` / `START_TEST()` 启动。随后在 `[[testflow]]` 中把 test suite 组装进流程，最后进入 `[[run]]` 执行与调试。
