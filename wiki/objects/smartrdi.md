---
type: object
title: SmartRDI
layer: L3
stage: testmethod
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13_SmartRDI.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# SmartRDI

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **147,013 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.13_SmartRDI.htm>` 及其子主题 `<02_System_reference/02.06_Command_Reference/02.06.02.02.242_SQTO__SQTO__-__SeQuencer_TimeOut.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.231.27_SMC_PIN_ERROR_MAP.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.04.01_Example_of_keyword_setups_in_the_RDI_Configure_file.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.04.02_getRdiConfig.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.06.01_rdi.getInfoLevel.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.06.02_rdi.setInfoLevel.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.01.02_execute.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.01.04_RDI_BEGIN.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.01.05_RDI_END.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.01.06_RDI_INIT.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.02_Changing_the_default_pin_status_with_SmartRDI.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.03_Changing_the_parameter_value_at_runtime_with_SmartRDI.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.09_Pass_Fail_per_label.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.12_Register_Access_library.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.14_Setting_and_retrieving_the_setup_name_with_SmartRDI.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.17_Sync_group_support_with_SmartRDI.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.19.01_Using_hidden_upload_with_SmartRDI.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.20_Using_Offline_Result_Emulation_in_SmartRDI.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.09.01_Alarm_setup_file.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.09.02_Alarm_handling_commands.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.10.01_RDI_protocol_template.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.10.02_pname.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.10.03_read.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.10.04_readExpect.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.10.05_regNum.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.10.06_write.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.10.07_writeBurst.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.10.08_getData.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.10.09_getDataStream.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.10.10_getPassFail.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.10_SmartRDI__d2s-like_protocol_test_setup.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.11.01_Using_a_DC_resource_as_an_AWG_with_SmartRDI.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.11.02_Runtime_DC_waveform.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.11.03_DC_waveforms_per_site.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.11.04_Using_a_DC_resource_as_a_digitizer_with_SmartRDI.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.11.05_Using_a_DC_Scale_resource_as_a_digitizer_while_sourcing_a_waveform_on_th.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.11.06_Serial_Semi-parallel_execution_of_BADC_as_digitizer_over_sites.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.11.07_DC_waveform_and_sampling_in_parallel.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.11.08_Parallel_pulse_actions_with_measurement_and_sampling.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02_Setting_up_DC_Scale_pins_with_SmartRDI.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.01_Generating_a_new_digital_capture_pattern_with_SmartRDI.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.02_Inserting_digital_capture_actions_in_an_existing_pattern_with_SmartRDI.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.03_Using_Immediate_Upload_in_SmartRDI.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.04_addVecRange.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.05_bitPerWord.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.06_burstUpload.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.07_capMode.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.08_copyLabel.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.09_enPassFail.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.10_format.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.11_initDiscard.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.12_interSkip.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.13_label.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.14_pin.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.15_samples.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.16_vecVar.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.17_vecVarOnly.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.18_getVector.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.19_getVectorBit.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.20_rdi.id__.getVectorFromVV.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.13.21_getVecVar.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.14.01_pin.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.14.02_runTimeVal.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.14.03_setOff.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.14.04_setOffRunTime.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.14.05_setOn.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.14.06_setOnRunTime.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.14_SmartRDI__Digital_channel_relay_control.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.15.05_rdi.route.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.16.01_combinedFailCount.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.16.02_emapLocation.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.16.03_failCount.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.16.04_failCyc.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.16.05_FFC.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.16.06_FFV.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.16.07_label.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.16.08_multiFFC.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.16.09_pfMap.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.16.10_rdi.func__.startVec.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.16.11_rdi.func__.stopVec.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.16.12_xMode.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.16.13_getFailCount.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.16.14_getFailCyc.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.16.15_getFFC.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.16.16_getPfMap.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.16.17_rdi.id__.getCombinedFailCount.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.16.18_rdi.id__.getFFV.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.16.19_rdi.id__.getMultiFFC.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.16_SmartRDI__Error_map_results_from_user_patterns.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.17.01.01_rdi.func__.burst.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.17.01.02_rdi.func__.burstId.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.17.01.03_rdi.func__.burstRunTime.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.17.01.05_rdi.func__.label.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.17.01.06_rdi.func__.labelRunTime.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.17.01.07_rdi.func__.perLabelPassFail.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.17.01.09_rdi.func__.readMatchCount.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.17.01.10_rdi.func__.readMatchPassFail.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.17.01.13_rdi.getBurstPassFail.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.17.01.14_rdi.id__.getBurstPassFail.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.17.01.15_rdi.id__.getLabel.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.17.01.16_rdi.id__.getMatchCount.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.17.01.17_rdi.id__.getMatchPassFail.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.17.01.18_rdi.id__.getMultiPassFail.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.17.01.19_rdi.id__.getPassFail.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.17.01.20_rdi.port_TA__MULTI_PORT_.func.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.17.01_FUNC.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.17.02_Retrieving_match_loop_results_from_user_patterns.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.17_Functional_test_setup.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.18.01_set.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.18_SmartRDI__Level_and_timing_set_changes.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.19.01_Structures_of_multiple_cogo___nodes.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.19.02_Sequencer-controlled_searching_with_cogo.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.20.03_postBurst.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.21.01_rdi.tmu__.dataRate.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.21.02_rdi.tmu__.disable.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.21.03_rdi.tmu__.enPassFail.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.21.04_rdi.tmu__.initDiscard.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.21.05_rdi.tmu__.insertVec.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.21.06_rdi.tmu__.interSkip.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.21.07_rdi.tmu__.label.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.21.08_rdi.tmu__.label__.copyLabel.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.21.09_rdi.tmu__.measMode.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.21.10_rdi.tmu__.measNum.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.21.11_rdi.tmu__.pin.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.21.12_rdi.tmu__.preScaler.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.21.13_rdi.tmu__.samples.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.21.14_rdi.id__.getArm.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.21.15_rdi.id__.getInterSkip.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.21.16_rdi.id__.getMultiArm.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.21.17_rdi.id__.getPreScaler.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.21.18_rdi.id__.getPassFail.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.21.19_rdi.id__.getPropDelay.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.21.20_rdi.id__.getStamp.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.21.21_rdi.id__.getTmuErrorState.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.21.22_rdi.id__.getTmuFinished.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.21_SmartRDI__TMU_test_setup.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.22.01_getLabelCycleNum.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.22.02.01_setGlobalVar.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.22.02.02_getGlobalVar.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.22.03_dtos.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.22.04_itos.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.22.05_itos_hex.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.22.06_reverseBits.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.22.07_getCommentCycleNum.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.22.08_getCommentVectorNum.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.23.01_pin.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.23.02_setOff.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.23.03_setOn.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.23.04_Sequencer_Controlled_Utility_Mask_with_SmartRDI.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.23_SmartRDI__Utility_lines_control.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.02_bitLength.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.03_burstLabel.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.04_burstUpload.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.05_comment.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.06_copyLabel.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.07_defaultBit.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.08_defaultVec.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.09_download.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.10_emapLocation.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.11_enPassFail.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.12_expectBit.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.13_expectData.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.14_failCount.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.15_failCyc.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.16_failNode.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.17_FFC.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.18_fillBit.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.19_fillVec.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.20_insertJmpe.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.21_insertSub.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.22_label.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.23_labelName.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.24_multiFFC.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.25_passNode.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.26_pMode.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.27_pModeStrobe.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.28_readBit.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.29_readData.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.30_rdi.smartVec__.readMode.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.31_repeat.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.32_repeatSub.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.33_rdi.smartVec__.vecEditMode.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.34_vecLength.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.35_writeBit.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.36_writeData.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.37_writeDataBurst.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.38_writeParData.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.39_writeParDataBurst.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.40_writePat.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.41_writeVec.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.42_xMode.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.43_getFailCount.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.44_getFailCyc.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.45_getFFC.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.46_rdi.id__.getMultiFFC.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.47_getReadBit.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.24.48_getReadData.htm>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.01.05_Variables_page.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Example of keyword setups in the RDI_Configure file）

```
// UTIL setup
UTIL_BLOCK = 12,34,5,6,7,8
UTIL_FRAM = UL_FRAM1,UL_FRAM3,UL_FRAM5,UL_FRAM6,UL_FRAM7,UL_FRAM8
UTIL_SCLK = UL_SCLK,UL_SCLK3,UL_SCLK,UL_SCLK,UL_SCLK,UL_SCLK
UTIL_SINP = UL_SINP,UL_SINP3,UL_SINP,UL_SINP,UL_SINP,UL_SINP
UTIL_SOUT = UL_SOUT,UL_SOUT3,UL_SOUT,UL_SOUT,UL_SOUT,UL_SOUT
UTIL_CTRL_MAX_SPEED = 2e6
UTIL_DYN_MASK_UNSPECIFIED_PIN = FALSE
UTIL_DYN_MASK_INACTIVE_SITE = TRUE
# UTIL_PADDING_RPTV_FLAT

// SmartVec setup
VEC_EDIT_MODE = VTT
DEFAULT_EMAP_LOCATION = TP
DEFAULT_SMV_READ_MODE = EMAP
SMV_DIGCAP_AUTO_BURSTUPLOAD = FALSE
SMV_VEC_MEM_TYPE = SHMEM
USER_NAMED_PATTERN_CONTENT_CHECK = FALSE

// Default pin status
DEFAULT_STATUS_PIN = pinA,pinB
DEFAULT_STATUS_INDEX = 0,1

// Setup name
ANALOG_SET_NAME_MD5 = TRUE
BURST_NAME_MD5 = TRUE

// PPMU setup
PPMU_DEFAULT_RELAY = NO
PPMU_DEFAULT_VALUE_MODE = SA

// Pass or fail per label
PER_LABEL_FUNC_RESULT_MODE = FLBL
PER_LABEL_FUNC_RESULT_NO_BREAK_VEC = TRUE

// ORE setup
ORE_FILE = " "
ENABLE_ORE = FALSE
ORE_TEMPLATE_BY_USER_CODE = TRUE

// Upload
DC_BURST_SITE_UPLOAD = TRUE
DIGCAP_ADAPTIVE_RESULT_SIZE = TRUE
DIGCAP_BURST_SITE_UPLOAD = TRUE

// Debug
REPORT_RESULT_IN_SINGLE_MODE = TRUE
ENABLE_RDI_INFO_LOG_FILE = TRUE

// SMC execution
DISABLE_SMC_EXEC_GLOBAL = TRUE
DISABLE_SMC_EXEC_SHORT_BURST = TRUE

// Production
SETUP_UPTODATE = TRUE

// Alarm handling for DCVI
ALARM_HANDLING_DCVI_ENABLE = TRUE
ALARM_HANDLING_DCVI_SETUP_FILE = "testmethod/RDI_Alarm_setup"

// Others
VEC_MODE_SAMPLING_WAIT = MSET
PURE_GENERATION_MODE = TRUE
ROUTING_SETUP_FILE = "testmethod/routing_tool_states_1.xml"
# ROUTING_SETUP_FILE = ./routing/Routing_Configure.xml
ALLOW_SAME_RESULT_ID_ACROSS_RDI_BLOCK = TRUE
# TMU_TIMEOUT_50ms = FALSE
```

### Syntax（取自子主题 getRdiConfig()）

```
string rdi.getRdiConfig(string optionName);
```
[表] Parameter
列: Parameter | Description
行 1:
  optionName
  The option name to be queried.

### Return Value（取自子主题 getRdiConfig()）

The option value returns.

### Example（取自子主题 getRdiConfig()）

```
rdi.getRdiConfig("RF_CAL_DEFAULT");
```

For the option

RF_CAL_DEFAULT
, one of the three values will return: ON, OFF, and
SYSTEM_CAL.

### Examples（取自子主题 Changing the default pin status with SmartRDI）

### Example 1
```
RDI_BEGIN();
rdi.setPinStatus("pinA",3);
rdi.digCap("mcsame1_DATA1_0").pin("DATA2").samples(30).execute();
rdi.clearPinStatus("pinA");
RDI_END();
```

### Example 2

Do not use
`setPinStatus()`（raw: `142779.htm`）
 and
`clearPinStatus()`（raw: `142780.htm`）
 in the
`burstLabel`（raw: `149059.htm`）
 block of
`smartVec`（raw: `149036.htm`）
.

Wrong position:

```
RDI_BEGIN();
rdi.smartVec().burstLabel("labelName").begin();
...
rdi.setPinStatus("A",1); // This is not allowed.
...
rdi.smartVec().burstLabel().end();
RDI_END();
```

Correct
position:

```
RDI_BEGIN();
rdi.setPinStatus("A",1); // This is correct.
rdi.smartVec().burstLabel("labelName").begin();
...
...
rdi.smartVec().burstLabel().end();
RDI_END();
```

### Example（取自子主题 SmartRDI: Utility lines control）

```
class RDI_STAT_UTIL: public testmethod::TestMethod
{
protected:

string sMode;
STRING_VECTOR utilitylineStatus_1,utilitylineStatus_2,utilitylineStatus_3;

virtual void initialize()
{
addParameter("RDIMode","string",&amp;sMode, testmethod::TM_PARAMETER_INPUT).setOptions("SINGLE:BURST:PROD").setDefault("BURST");
}

virtual void run()
{
RDI_INIT();

ON_FIRST_INVOCATION_BEGIN();

//
// Select smartRDI Mode
//
TA::USER_RUN_MODE mode;

if (sMode == "SINGLE") mode = TA::SINGLE;
else if (sMode == "BURST") mode = TA::BURST;
else if (sMode == "PROD") mode = TA::PROD;

utilitylineStatus_1 = GET_UTILITY_LINES_STATUS(0);

//
// Set 4 util lines of util block 2-9 defined in pin file
//
rdi.util().pin("SEQ_LED_201,SEQ_LED_207, SEQ_LED_209,SEQ_LED_215").setOn().execute();
rdi.wait(2 ms);
utilitylineStatus_2 = GET_UTILITY_LINES_STATUS(0);

//
// Reset 4 util lines of util block 2-9 defined in pin file
//
rdi.util().pin("SEQ_LED_201,SEQ_LED_207,SEQ_LED_209,SEQ_LED_215").setOff().execute();
rdi.wait(4 ms);
utilitylineStatus_3 = GET_UTILITY_LINES_STATUS(0);

ON_FIRST_INVOCATION_END();

//
// Datalog
//
cout << "after reset" << endl;

for(int i=1; i<9;i++)
{
cout << "STAT_UTIL" << i << " = " << utilitylineStatus_1[i-1] << endl;
}

cout << "after set on" << endl;

for(int i=1; i<9;i++)
{
cout << "STAT_UTIL" << i << " = " << utilitylineStatus_2[i-1] << endl;
}
cout << "after set off" << endl;

for(int i=1; i<9;i++)
{
cout << "STAT_UTIL" << i << " = " << utilitylineStatus_3[i-1] << endl;
}

return;
}

virtual void postParameterChange(const string&amp; parameterIdentifier)
{
return;
}

virtual const string getComment() const
{
string comment = "please add your comment for this method.";
return comment;
}
};
```

### Syntax（取自子主题 RDI_INIT()）

```
RDI_INIT();
```

RDI_INIT()
 must be called before
`ON_FIRST_INVOCATION_BEGIN();`（raw: `29526.htm`）
.

### Syntax（取自子主题 RDI_BEGIN()）

```
RDI_BEGIN();
RDI_BEGIN(mode);
```

[表] Parameter
列: Parameter | Description
行 1:
  mode
  The optional execution mode. It can be:
    
    TA::BURST: Pattern-based execution
    mode. This is the default mode.
    
    TA::SINGLE: Single step execution mode
    for debugging.
    
    TA::PROD: Production mode. No new
    setups will be generated. The saved setups from the
    pattern‑based mode will be used.

### Examples（取自子主题 RDI_BEGIN()）

### Example 1: Minimum code

The following example shows the minimum code for a RDI block. The ellipses ("...")
are to be replaced with your code.

```
RDI_BEGIN();
...
...
RDI_END();
```

### Example 2: Optional curly brackets

The example utilizes an optional pair of curly brackets "{" and "}". These optional
curly brackets are used for simplifying the correct indentation with assistance of
the related Eclipse tool.

```
RDI_BEGIN();
{
...
...
}
RDI_END();
```

Note
 The two use options (with or without curly brackets) should not be mixed in one
test method class.

### Syntax（取自子主题 RDI_END()）

```
RDI_END();
RDI_END(mode);
```
[表] Parameter
列: Parameter | Description
行 1:
  mode
  The optional execution mode. If mode is not specified, the blocking pattern
    execution is used by default.
    
    TA::BLOCKING is to be used to start
    the blocking pattern execution at the end of the RDI
    block. No other action can be performed while the
    pattern burst is running.
    
    This is the default option.
    
    TA::NON_BLOCKING is to be used to
    start the non-blocking pattern burst execution at the
    end of the RDI block. Other actions can be performed
    while the pattern burst is running.
    
    The command `RDI_WAIT_TEST_DONE()`（raw: `153002.htm`） is to be used to align the end of the non-blocking
    pattern execution.

### Examples（取自子主题 RDI_END()）

### Example 1: Minimum code

The following example shows the minimum code for
a RDI block. The ellipses ("...") are to be replaced with your
code.

```
RDI_BEGIN();
...
...
RDI_END();
```

### Example 2: Optional curly brackets

The example utilizes an optional pair
of curly brackets "{" and "}". These optional curly brackets are used for simplifying the
correct indentation with assistance of the related Eclipse
tool.

```
RDI_BEGIN();
{
...
...
}
RDI_END();
```

Note
 The two use options (with or without curly brackets) should not be mixed in one
test method class.

### Example 3: Non-blocking execution
```
RDI_BEGIN();
...
RDI_END(TA::NON_BLOCKING); // Execution of the pattern burst starts.

//
// Actions during pattern burst execution
//
...
...

RDI_WAIT_TEST_DONE(); // Wait for end of pattern burst.
```

If
RDI_END()
 is used instead of
RDI_END(mode)
, the RDI
block is executed in a blocking way, which means no other jobs can be executed while
the pattern burst is running.

### Syntax（取自子主题 execute()）

```
execute();
```

List of parameters

There are no parameters.

Return value

There is no return value.

### Example（取自子主题 execute()）

```
rdi.util().pin("upin_A").setOn().pin("upin_B").setOff().execute();
```

### Syntax（取自子主题 rdi.getInfoLevel()）

```
int getInfoLevel();
```

### Example（取自子主题 rdi.getInfoLevel()）

Changing the RDI_INFO_LEVEL to
2

```
...
cout<<"RDI_INFO_LEVEL ="rdi.getInfoLevel()<<endl;
rdi.setInfoLevel(2);

RDI_BEGIN();
rdi.dc().pin("DATA1").vForce(3 V).execute();
rdi.dc().pin("DATA2").iForce(0 mA).vMeas().measWait(100 us).execute();
RDI_END();

cout<<"RDI_INFO_LEVEL ="rdi.getInfoLevel()<<endl;

rdi.setInfoLevel(0);
```

In the SmarTest UI report window:

```
RDI_INFO_LEVEL = 0

Total: 26.071 msec
Setup Generation: 15.631 msec
Action pattern & Dc generation: 14.090 msec
Burst pattern gen: 0.080 msec
Other init & check: 0.069 msec
Pattern Cycle Calculation: 1.376 msec
User Code: 0.016 msec
Setup Command: 6.044 msec
DC Setup: 5.839 msec
Other Command: 0.205 msec
Pattern Execution: 3.278 msec
Result Upload: 1.043 msec
DC Result Upload: 1.023 msec
Others: 0.075 msec

RDI_INFO_LEVEL = 2
```

### Syntax（取自子主题 rdi.setInfoLevel()）

```
void setInfoLevel(int val);
```

### Example（取自子主题 rdi.setInfoLevel()）

Setting the RDI_INFO_LEVEL to
2
 for a block:

```
...
cout<<"RDI_INFO_LEVEL ="rdi.getInfoLevel()<<endl;
rdi.setInfoLevel(2);

RDI_BEGIN();
rdi.dc().pin("DATA1").vForce(3 V).execute();
rdi.dc().pin("DATA2").iForce(0 mA).vMeas().measWait(100 us).execute();
RDI_END();

cout<<"RDI_INFO_LEVEL ="rdi.getInfoLevel()<<endl;

rdi.setInfoLevel(0);
```

The SmarTest UI report window shows the level 2 information:

```
RDI_INFO_LEVEL = 0

Total: 26.071 msec
Setup Generation: 15.631 msec
Action pattern & Dc generation: 14.090 msec
Burst pattern gen: 0.080 msec
Other init & check: 0.069 msec
Pattern Cycle Calculation: 1.376 msec
User Code: 0.016 msec
Setup Command: 6.044 msec
DC Setup: 5.839 msec
Other Command: 0.205 msec
Pattern Execution: 3.278 msec
Result Upload: 1.043 msec
DC Result Upload: 1.023 msec
Others: 0.075 msec

RDI_INFO_LEVEL = 2
```

### Example（取自子主题 Variables page）

You can use a user flag to branch in a testflow, depending on the current value of the flag.
This lets you control the testflow execution during a test program run.

### Examples（取自子主题 Changing the parameter value at runtime with SmartRDI）

### Example 1: DC test - Using different values for different sites
```
ARRAY_D rtv_arr(4); // Define a variable for quad-site tests
rtv_arr.init(0.0);

ON_FIRST_INVOCATION_BEGIN();

rtv_arr[0]=1.0; rtv_arr[1]=1.1; rtv_arr[2]=1.2; rtv_arr[3]=1.3;

rdi.runTimeVal("rtv",rtv_arr);

rdi.dc().pin("A").vForce("rtv").execute(); // Both code‑based or pattern‑based modes are supported.

ON_FIRST_INVOCATION_END();
```

### Example 2: RF stimulus - Using the different values for different sites
```
ARRAY_D power(4); // Define a variable for quad-site tests
power.init(0.0);

power[0]=-10;power[1]=-11;power[2]=-12;power[3]=-13;

ON_FIRST_INVOCATION_BEGIN();

rdi.runTimeVal("ppp",power);

RDI_BEGIN();

rdi.rfs().pin("A").signal(TA::CW).power("ppp").freq(1e9).execute();

RDI_END();

ON_FIRST_INVOCATION_END();
```

### Example 3: Protocol test - Changing the write data at runtime
```
ARRAY_I write_data(2); // Define a variable for dual-site test
write_data.init(0);

write_data[0]=0x1;
write_data[1]=0x2;

rdi.runTimeVal("data",write_data); // Site data array

RDI_BEGIN();

rdi. protocol().pname("i2c").write(0x4,"data").execute();

RDI_END();
```

### Examples（取自子主题 Pass/Fail per label）

### Returning functional test results per label

```
RDI_BEGIN();
rdi.smartVec("1").pin("Pin2")
.expectData(20,2)
.execute();
rdi.dc("2").label("pat1")
.insertSub(10)
.pin("VI1")
.vForce(1)
.enPassFail()
.execute();
rdi.func("3").label("Label1")
.execute();
RDI_END();
```

### No ID, no Pass/Fail result per label

```
RDI_BEGIN();
rdi.smartVec().pin("Pin1")
.writeData(20,8,2)
.pin("Pin2")
.expectData(20,2)
.execute();
rdi.func().label("Label1")
.execute();
RDI_END();
```

### Examples（取自子主题 Register Access library）

### Example 1

RA operations without register structure
definitions

```
RDI_BEGIN();

// Write register
RA_WRITE(0x1234, 0x55);
// Read a register under ID : READ_ID_1
RA_READ("READ_ID_1", 0x1234);
// Read a register and compare against expected value without mask
RA_COMPARE(0x1234, 0x55);
// Read a register and compare against expected value with mask
RA_COMPARE(0x1234, 0x55, 0xFE);
// Write run time per site data
RA_WRITE_DYNAMIC("DYN_ID_1", 0x1234);
// Read a register again
RA_READ("READ_ID_2", ADDR1);
// Compare by reading register
RA_COMPARE("COMP_ID_1", ADDR1, DATA1);

rdi.wait(10 ms);

RDI_END();
```

### Example 2

RA operations with register structure definitions

```
MultiSite<ULONG64> dynData;
dynData[0] = 0x7E; dynData[1] = 0x01;
RA_SET_DYNAMIC_DATA("DynID1", dynData);

RDI_BEGIN();
rdi.dc().pin("VDD").vForce(3.3).execute();
reg.PERIPHERAL0().REGISTER0().setValue(0x5E).write(); // Write Register
reg.PERIPHERAL0().REGISTER1().setField_FIELDA(1).write(); // Write Field (RMW)
reg.PERIPHERAL0().REGISTER1().read("readID1"); // Read Register
reg.PERIPHERAL0().REGISTER0().setValue(0x5E).compare("CompareID1"); // Read and Compare
reg.PERIPHERAL0().REGISTER2().writeDynamic("DynID1"); // Write a per site runtime register value

// Other RDI operations
rdi.wait(2 ms);
rdi.dc("rdiID1").pin("D1").iForce(0).vMeas().execute();
...
RDI_END();

ULONG64 regValue = RA_GET_READ_RESULT("readID1");
bool comparePF = RA_GET_COMPARE_RESULT("CompareID1").getPassFail()
```

### Example（取自子主题 Setting and retrieving the setup name with SmartRDI）

Retrieving the analog set
name

```
string analogSetName = rdi.id("AWG_1").getAnaSet();
string pAnalogSetName = rdi.getPriAnalogset();
```

Setting
the analog set name and pattern burst
name

```
rdi.setAnaSet("set1");
rdi.setPatBurst("pattBurst1");
RDI_BEGIN();
...
RDI_END();
```

### Example（取自子主题 Sync group support with SmartRDI）

```
rdi.syncGroup("sg1").addPort("ptA");
rdi.syncGroup("sg2").addPort("ptB").addPort("ptC");

RDI_BEGIN();
rdi.port("ptA")...
rdi.port("ptB")...
rdi.port("ptC")...
RDI_END();
```

### Example（取自子主题 Using Offline Result Emulation in SmartRDI）

ORE file locations must be loaded before
RDI_INIT()
 in the first test
suite.

```
virtual void run()
{
static int i = 0;
string oreFile[4];

// Load ORE files before RDI_INIT() in the first test suite.
oreFile[0] = "./demo1.xml";
oreFile[1] = "./demo2.xml";
oreFile[2] = "./demo3.xml";
oreFile[3] = "./demo4.xml";

SET_USER_STRING("RDI_ORE_FILE", oreFile[i]);

RDI_INIT();

ON_FIRST_INVOCATION_BEGIN();

RDI_BEGIN();
rdi.emap("emap").label("funcPass").pin("DATA2").failCount(2).execute();
RDI_END();

i++;

ON_FIRST_INVOCATION_END();

cout<<"in run "<<i<<" , ore getFailCout result"<< rdi.id("emap").getFailCount()<<endl;

return;
}
```

### Examples（取自子主题 Alarm setup file）

### Example 1

An alarm setup file

```
DEBUG_VALUE = TRUE # This must be the first setup entry in the file.

SET DEFAULT # Applied by default
GlobalLimitRelForce = 10%
GlobalLimitMinDisForce = 10 mV
GlobalLimitRelClamp = 10 mV

PINS UB_AVI VDD_AVI VDD_PVI
# No local limit value defined means that global values are applied.

SET A1
# Alarm checks on VDD_AVI are skipped.

PINS UB_AVI
LimitRelForce = 10%
LimitMinDisForce = 5 mV
# Used for vForce checks.
# vClamp settings are used for vClamp checks.

PINS VDD_PVI
GlobalLimitRelForce = 10% #
GlobalLimitMinDisForce = 10 mV
# Used for vForce checks.

LimitRelClamp = 100 mV
# Used for vClamp checks.

SET A2
# Alarm checks on both VDD_AVI and VDD_PVI are skipped.

PINS UB_AVI
LimitLo = 4.7 # default V
LimitHi = 5.3
# Used for both vForce and vClamp checks.
...
```

### Example 2

DEBUG_VALUE setting allows more information shown in the UI report window

Starting from 7.5.2, SmartRDI provides more information in the UI report window when the

DEBUG_VALUE
 is enabled in the alarm setup file.

burst:: _rdi_burst_AVI64_Alarm_handling_Test_bk2

Alarm DC Result ::

Site [1]

ID:alarm_pass_fail_pin_AVI2_AVI4 , AVI2 = 3.00034, AVI4 = 2.00040 << F
<< (2.80000,3.20000),

ID:func_fail2 , AVI2 = 2.999909, AVI4 = 2.00036 << F
<< (2.80000,3.20000),

=============================================

Site [2]

ID:alarm_pass_fail_pin_AVI2_AVI4 , AVI2 = 2.999226, AVI4 = 1.99909 << F
<< (2.80000,3.20000),

ID:func_fail2 , AVI2 = 3.00074, AVI4 = 2.00028 << F
<< (2.80000,3.20000),

=============================================

### Examples（取自子主题 Alarm handling commands）

```
rdi.alarm().applySet("abc"); // Use an alarm handing set "abc"

RDI_BEGIN();
rdi.class(id)... // Each measurement with "id" triggers an alarm compare event after it
...
rdi.alarm().check().execute(); // Add an alarm check point
RDI_END();

rdi.id("id").getAlarmPassFail("pinA"); // Alarm result of pinA, and any result "id" in burst
rdi.id("id").getAlarmPassFail(); // Alarm result for all alarm pins.
```

Each of these commands takes effect in its test suite and subsequently keeps valid no matter
where it is located, inside or outside an

RDI_BEGIN
-
RDI_END
 block in the test
suite.

```
RDI_BEGIN();
rdi.alarm().globalLimitRelForcePercent(0.1);
...
RDI_END();

RDI_BEGIN();
... // the globalLimitRelForcePercent also takes effect.
RDI_END();
```

### Examples（取自子主题 SmartRDI: d2s-like protocol test setup）

### Basic data reading and writing
```
ON_FIRST_INVOCATION_BEGIN();
RDI_BEGIN();
rdi.protocol().pname("i2c").write(0x1,0x2).execute();
rdi.protocol("id2").pname("i2c").read(0x1).execute();
rdi.protocol("id3").pname("i2c").readExpect(0x1,0x03).execute();
rdi.protocol("id4").pname("i2c").readExpect(0x1,0x03,0x1).execute();
RDI_END( );
ON_FIRST_INVOCATION_END();
int result=rdi.id("id2").getData();
int pf=rdi.id("id3").getPassFail();
```

Burst
data reading and
writing

```
ARRAY_I data(3);
data[0]=0x9; data[1]=0xa; data[2]=0x7;
ON_FIRST_INVOCATION_BEGIN();
RDI_BEGIN();
rdi.protocol().pname("prt").writeBurst(0x1,data).execute();
rdi.protocol("id1").pname("prt").regNum(3).read(0x01).execute();
RDI_END( );
ON_FIRST_INVOCATION_END();
ARRAY_I result=rdi.id("id1").getDataStream();
```

### Runtime data writing
```
ARRAY_I write_data(2);
write_data[0]=0x1;
write_data[1]=0x2;
rdi.runTimeVal("data",write_data); // site data array
RDI_BEGIN();
rdi.protocol().pname("i2c").writeBurst(0x4,"data").execute();
RDI_END();
```

### Example（取自子主题 RDI protocol template）

This is an example of a SmartRDI protocol template:

```
#ifndef PROTOTEMPLATE_H_
#define PROTOTEMPLATE_H_
#include <string>
#include <map>
#include "rdi.hpp"
using namespace std;
/**
* @class protocolTemplate
*
* @brief Protocol customized class template (D2S)
*
* @details This class must be defined before expected protocol is applied in the TP.
* In structure, it must be inherited from protocolBase and corelated parameters
* must be defined. Even if some of the parameters is not used, a dummy value must be defined as well.
*
* @note How to apply user customerized protocol template :
* - Duplicate file "protocolTemplate.h" and rename file to your protocol name, for example, "protocol_JTAG.h"
* - Do change the header as following :
* - "#ifndef PROTOTEMPLATE_H_" to "#ifndef PROTO_JTAG_H_"
* - "#define PROTOTEMPLATE_H_" to "#define PROTO_JTAG_H_"
* - Do replace name "protocolTemplate" to "yourProtocolName" throughout text line from class definition to the end.
* e.g. Replace "protocolTemplate" with "protocolJtag"
* - Do customerized parameters in getXXXXXX() functions. Pat attention to getInterfaceName(),
* which will be referred by LEGO as your protocol name and used int LEGO() .protocol("prtocolName")....
* - In your UTM cpp file do include your customerized protocol class, for example, #include "protocol_JTAG.h"
*
*/
class protocolTemplate : public protocolBase
{
public:

virtual string getInterfaceName() { return "interfaceName"; }

/******************************************************************************
* General Protocol Parameter
* ****************************************************************************/
virtual void init()
{
interfaceName = getInterfaceName();
dataMode = 0; // 0: organize data vertically 1: organize data horizontally
addressBits = 8;
dataBits = 8;
highWaveformIndex = 1;
lowWaveformIndex = 0;
highStrobeWaveformIndex = 3;
lowStrobeWaveformIndex = 2;
maskStrobeWaveformIndex = 4;
vecBitRepeats = 1;
/******************************************************************************
* Protocol Write Parameters
* ****************************************************************************/
writeTemplatePatternName = "d2s_template";
writePinName = "DATA1";
writeAddressVectorNumberLSB = 7;
writeAddressVectorNumberMSB = 0;
writeDataVectorNumberLSB = 22;
writeDataVectorNumberMSB = 15;
writeVectorsPerRegister = 10;
/******************************************************************************
* Protocol Read Parameters
* ****************************************************************************/
readTemplatePatternName = "d2s_template";
readAddressPinName = "DATA1";
readPinName = "DATA1";
readAddressVectorNumberLSB = 7;
readAddressVectorNumberMSB = 0;
readDataVectorNumberLSB = 22;
readDataVectorNumberMSB = 15;
readVectorsPerRegister = 10;
readCycleOffset = 0;
}
static protocolTemplate& getInstance()
{
static protocolTemplate ins;
ins.init();
return ins;
}

protected:
protocolTemplate() { getProtocolMap()[getInterfaceName()] = this; }
protocolTemplate(const protocolTemplate&);
protocolTemplate& operator= (const protocolTemplate&);
};
REGISTER_PROTOCOL(protocolTemplate);
#endif /* PROTOTEMPLATE_H_ */
```

### Syntax（取自子主题 pname()）

```
pname(const string& sProtocolName);
```
[表] List of parameters
列: Parameter | Description
行 1:
  sProtocolName
  The defined protocol to use.

### Example（取自子主题 pname()）

```
rdi.protocol().pname("i2c").write(0x1,0x2).execute();
```

### Syntax（取自子主题 read()）

```
read(long long iAddr);
read(long iAddr);
read(int iAddr);
```
[表] List of parameters
列: Parameter | Description
行 1:
  iAddr
  The address to read data.

### Example（取自子主题 read()）

```
rdi.protocol("id1").pname("i2c").read(0x1).execute();
```

### Syntax（取自子主题 readExpect()）

```
readExpect(long long iAddr, long long iExp, long long mask = 0x00);
readExpect(long long iAddr, const ARRAY_I& iExp);
readExpect(long long iAddr, const ARRAY_LL& iExp);
readExpect(long long iAddr, const ARRAY_I& iExp, const ARRAY_I& mask);
readExpect(long long iAddr, const ARRAY_LL& iExp, const ARRAY_LL& mask);
```
[表] List of parameters
列: Parameter | Description
行 1:
  iAddr
  The address to read.
行 2:
  iExp
  The expected data.
行 3:
  mask
  The value to mask the expected value per bit. The bit value 1 means mask and the
    bit value 0 means unmask.
    
    By default, all bits are unmasked.

### Example（取自子主题 readExpect()）

```
rdi.protocol("id4").pname("i2c").readExpect(0x1,0x03,0x1).execute();
```

### Syntax（取自子主题 regNum()）

```
regNum(int iRegNr);
```
[表] List of parameters
列: Parameter | Description
行 1:
  iRegNr
  The register number to read

### Example（取自子主题 regNum()）

```
rdi.protocol("id1").pname("prt").regNum(3).read(0x01).execute();
```

### Syntax（取自子主题 write()）

```
write(long long iAddr, long long iData);
write(long long iAddr, long iData);
write(long long iAddr, int iData);
write(long iAddr, long iData);
write(long iAddr, int iData);
write(int iAddr, long iData);
write(int iAddr, int iData);
write(long long iAddr, const string &sData);
write(long long iAddr, const ARRAY_I &aiBurstData);
write(long long iAddr, const ARRAY_LL &aiBurstData);
```
[表] List of parameters
列: Parameter | Description
行 1:
  iAddr
  The address to write.
行 2:
  iData
  The data to write.
行 3:
  sData
  The string containing the data to write at runtime. Refer to `Changing the parameter value at runtime with SmartRDI`（raw: `144753.htm`）.
行 4:
  aiBurstData
  The array containing the burst of data to be written.

### Examples（取自子主题 write()）

### Write specific data
```
rdi.protocol().pname("i2c").write(0x1,0x2).execute();
```

### Write at runtime
```
ARRAY_I write_data(2); // Define a variable for a dual-site test
write_data[0]=0x1;
write_data[1]=0x2;
rdi.runTimeVal("data",write_data); // Site data array
RDI_BEGIN();
rdi.protocol().pname("i2c").write(0x4,"data").execute();
RDI_END();
```

### Syntax（取自子主题 writeBurst()）

```
writeBurst(long long iAddr, const ARRAY_I& aiBurstData);
writeBurst(long long iAddr, const ARRAY_LL& aiBurstData);
writeBurst(long long iAddr, const string &sData);
```
[表] List of parameters
列: Parameter | Description
行 1:
  iAddr
  The address to write.
行 2:
  aiBurstData
  The array containing the burst of data to write.
行 3:
  sData
  The string containing the data to write at runtime.

### Example（取自子主题 writeBurst()）

```
rdi.protocol().pname("i2s").writeBurst(0x3, arr).execute();
```

### Syntax（取自子主题 getData()）

```
int getData();
```

### Example（取自子主题 getData()）

```
int result=rdi.id("id1").getData();
```

### Syntax（取自子主题 getDataStream()）

```
ARRAY_LL& getDataStream();
```

### Example（取自子主题 getDataStream()）

```
ARRAY_LL result;
result=rdi.id("1").getDataStream();
```

### Syntax（取自子主题 getPassFail()）

```
int getPassFail();
```

### Example（取自子主题 getPassFail()）

```
int result = rdi.id("protocol_1").getPassFail();
```

### Example（取自子主题 Using a DC resource as an AWG with SmartRDI）

```
anaWaveform vwav ("UP_V");
vwav.definition(TM::SINE).periods(3).amplitude(3 V).offset(0.5 V).samples(2048);
...
rdi.dc().pin("VI32_1").waveform(vwav).FS(10 KHz).execute();
rdi.dc().pin("VI32_1").vForce().waveform(vwav).FS(10 KHz).execute();
rdi.dc().pin("DPS32_SIG_1").vForce().waveform(vwav).FS(10 KHz).execute();
rdi.port("ptPin1").dc().pin("DATA1").waveform(vwav).samplePeriod(100 us).execute();
rdi.port("ptPin1").dc().pin("DATA1").iForce().waveform(vwav).sampleCycle(1000).execute();
```

### Example（取自子主题 Runtime DC waveform）

```
ARRAY_I sites;
Int siteNum = GET_CONFIGURED_SITES(sites); // To get all Configured Sites
vector<anaWaveform> siteWav(siteNum); // Runtime waveform array for multisite testing.

for(int i=0;i<siteNum;i++)
{
anaWaveform tmpWave("tmpWave");
tmpWave.definition(TA::SINE).samples(1024).offset(offset).periods(12).amplitude(1);
siteWav[i]=tmpWave;
}
rdi.runtimeVal("rtWave",siteWav); // Runtime waveform matches run time ID.

RDI_BEGIN();
rdi.port("ptPin").dc().pin("pinA").vForce().waveform("rtWave").FS(10 KHz).execute();
// Waveform downloading happens before each execution.
RDI_END();
```

### Example（取自子主题 DC waveforms per site）

```
vector<anaWaveform> siteWav(siteNum); // Per site waveform array.

FOR_EACH_SITE_BEGIN();
anaWaveform tmpWave("tmpWave");
tmpWave.definition(TA::SINE).samples(1024).offset(offset).periods(12).amplitude(1);
siteWav[CURRENT_SITE_NUMBER()-1]=tmpWave;
FOR_EACH_SITE_END();

rdi.perSiteVal("rtWave",siteWav); // Per site waveform matches perSiteVal ID.

RDI_BEGIN();
rdi.port("ptPin").dc().pin("pinA").vForce().waveform("rtWave").FS(10 KHz).execute();
// Waveform downloading happens before each execution.
RDI_END();
```

### Example（取自子主题 Using a DC resource as a digitizer with SmartRDI）

```
rdi.dc().pin("DPS128_1")
.iForce(2 mA).vMeas().samples(1024).FS(10 KHz).execute();

rdi.dc().pin("DATA1")
.vForce(1 V).iMeas().samples(1024).capMode(TA::VEC)
.valueMode(TA::BADC).FS(10 KHz).execute();

rdi.dc().pin("DATA1")
.vMeas().samples(1024).capMode(TA::VEC)
.valueMode(TA::SA).FS(1 KHz).execute();

rdi.port("ptPin1").dc().pin("DATA1")
.samples(1024).capMode(TA::TRIG)
.valueMode(TA::BADC).FS(10 KHz).execute();

rdi.port("ptPin1").dc().pin("DATA1",TA::BADC)
.samples(1024).capMode(TA::TRIG).FS(10KHz).execute();
```

### Example（取自子主题 Using a DC Scale resource as a digitizer while sourcing a waveform on the same pin）

```
rdi.dc("id").pin().vForce().iMeas().waveform(wav).FS(10 KHz).execute();
rdi.dc("id").pin().vForce().vMeas().waveform(wav).FS(10 KHz).execute();
rdi.dc("id").pin().iForce().iMeas().waveform(wav).samplePeriod(100 us).execute();
rdi.dc("id").pin().iForce().vMeas().waveform(wav).sampleCycle(1000).execute();
```

### Example（取自子主题 Serial/Semi-parallel execution of BADC as digitizer over sites）

We assume Pin "DATA36" shares one BADC on sites1 & 2 (pogo 103) and another BADC
on sites 3 & 4 (pogo 104).

Example for a semi-parallel execution of digitizing by
BADCs shared over sites. For pin "DATA36", sites 1 & 3 are executed at first followed by
sites 2 & 4. Below are the example code as well as the code logic illustration.

```
SEMI_PARALLEL_CONFIG semi;
semi.group(1).add(1).add(3);
semi.group(2).add(2).add(4);

RDI_BEGIN();
RDI_SEMI_PARALLEL_TEST_BEGIN(semi);
rdi.dc().pin("DATA36").vMeas().samples(1024).FS(10 KHz).execute();
RDI_SEMI_PARALLEL_TEST_END();
RDI_END();
```

### Examples（取自子主题 DC waveform and sampling in parallel）

### Forcing a waveform on a pin and taking samples on another pin

```
RDI_BEGIN();
rdi.port("portC").dc().pin("A").waveform(sine).FS(100 KHz)
.pin("B").samples(1024).FS(100 KHz)
.execute();
RDI_END();
```

### Forcing a waveform and taking samples in parallel on multiple pins

```
RDI_BEGIN();
rdi.dc().pin("AVI1").vForce().waveform(sine1).sampleCycle(1000)
.pin("AVI2").iForce().waveform(sine2).sampleCycle(1000).execute();
RDI_END();
```

### Forcing a waveform and taking samples on the same DC Scale pin

```
RDI_BEGIN();
rdi.dc("id1").pin().vForce().iMeas().waveform(wav).FS(10 KHz).execute();
rdi.dc("id2").pin().vForce().vMeas().waveform(wav).FS(10 KHz).execute();
rdi.dc("id3").pin().iForce().iMeas().waveform(wav).FS(10 KHz).execute();
rdi.dc("id4").pin().iForce().vMeas().waveform(wav).FS(10 KHz).execute();
RDI_END();
```

### Example（取自子主题 Parallel pulse actions with measurement and sampling）

```
rdi.dc().pin("A").vPulse(5 V,2 V,2000 us)
.pin("B").vMeas().measWait(800 us)
.pin("C").iPulse(1 mA,0.5 mA,2000 us).vMeas().measWait(800 us)
.execute();
```

### Examples（取自子主题 Setting up DC Scale pins with SmartRDI）

### PMU (SIG) operating mode
```
rdi.dc().pin("DCS_SIG").vForce(2 V).vForceRange(25 V).iForceRange(100 uA).execute();

RDI_BEGIN();

rdi.dc().pin("DCS_SIG").iMeasRange(100 uA).execute();
rdi.dc().pin("DCS_SIG").vForce(10 V).execute();
rdi.dc().pin("DCS_SIG").iMeas().execute();
rdi.dc().pin("DCS_SIG").vForce(8 V).execute();
rdi.dc().pin("DCS_SIG").iMeas().execute();

RDI_END();

rdi.dc().pin("DCS_SIG").disconnect().execute();
```

### DPS operating mode
```
rdi.dc().pin("DCS_DPS").connect().execute();

RDI_BEGIN();

rdi.dc().pin("DCS_DPS").vForce(10 V).execute();
rdi.dc().pin("DCS_DPS").iMeas().execute();
rdi.dc().pin("DCS_DPS").vForce(8 V).execute();
rdi.dc().pin("DCS_DPS").iMeas().execute();

RDI_END();

rdi.dc().pin("DCS_DPS").disconnect().execute();
```

### Examples（取自子主题 Generating a new digital capture pattern with SmartRDI）

### Digital capture without hidden upload
```
ON_FIRST_INVOCATION_BEGIN();
RDI_BEGIN();
rdi.digCap("cap").pin("DO").samples(100).initDiscard(10).interSkip(1,2).execute();
RDI_END( );
ON_FIRST_INVOCATION_END();
const ARRAY_I& aiData = rdi.id("cap").getVector("DO");
```

### Digital capture with hidden upload
```
run()
{
ON_FIRST_INVOCATION_BEGIN();
rdi.hiddenUpload(TA::DIGCAP);
RDI_BEGIN();
rdi.digCap("id2").pin("A").samples(1024).execute();
RDI_END();
ON_FIRST_INVOCATION_END();
SMC_ARM();
}
...
public:
void SMC_backgroundProcessing()
{
ARRAY_I bits = rdi.id("id2").getVectorBit();
}
```

### Example（取自子主题 Inserting digital capture actions in an existing pattern with SmartRDI）

```
RDI_BEGIN();
rdi.digCap("mps").label("lpDcap_new").pin("DATA2,DATA6").addVecRange(3,15).samples(10).execute();
RDI_END();
```

In
this example, the digital capture actions will be inserted in the vector range (3,15) of the
pattern
lpDcap_new
 for the pin
DATA2
 and

DATA6
. 10 samples are captured for each pin. The following two figures shows
the existing pattern and the pattern generated after inserting the digital capture
actions.

### Examples（取自子主题 Using Immediate Upload in SmartRDI）

### Using immediate upload for data upload only

In the example below,
digCapImmediateUpload()
 is used alone to upload digital
capture data immediately while the test is running. The upload of the captured data referenced
by "resultId" is started while the burst is executed.

```
rdi.digCapImmediateUpload("resultId");

RDI_BEGIN();
rdi.digCap("resultId").samples(...)...execute();
...
RDI_END(); // Raw Result upload within pattern run

rdi.id("resultId").getVector();
```

### Using immediate upload for data upload and result calculation

In the example below,
digCapImmediateUpload()
 is used together with

getImmediateVector()
 to upload digital capture data as well as hide result
calculation while the test is running.

```
rdi.digCapImmediateUpload("resultId");

RDI_BEGIN();
rdi.digCap("resultId").samples(SAMPLE_SIZE).bitPerWord(BPW).execute();
RDI_END( TA::NON_BLOCKING);

bool dataIsRemaining;
ARRAY_I resultChunk;
ARRAY_I uploadDataOffset(MAX_SITE_NUM);

while (dataIsRemaining)
{dataIsRemaining = false;
FOR_EACH_SITE_BEGIN()
site = CURRENT_SITE_NUMBER();
if (uploadDataoffset[site] < SAMPLE_SIZE/BPW-1)
{resultChunk=rdi.id("resultId").getImmediateVector(uploadDataOffset[site]);
uploadDataOffset[site] += resultChunk.size();
dataIsRemaining = true;
//-------------- calculation e.g. fill histogram array ---------------------------------
}
FOR_EACH_SITE_END()；
}
RDI_WAIT_TEST_DONE();
```

getImmediateVector()
 returns an array of vectors. The array size in SER mode
is calculated by dividing sampleSize with bitPerWord. So in this example, the maximum array size
equals to
SAMPLE_SIZE
 divided by
BPW
. Pay attention that
in serial mode, the default setting for bitPerWord is 32.

In offline mode, the chunk size from each
getImmediateVector()
 upload is 0. A
working online code may cause an endless loop in offline execution. It is recommended to define
an extra end loop criterion, for example, define the maximum number of loop executions.

Important: With SmarTest7.4.3.0 and 7.4.3.1, immediate upload only allows ONE result id in a
pin.

### Syntax（取自子主题 addVecRange()）

```
addVecRange(int iRangeBf, int iRangeAft);
```
[表] Parameter List
列: Parameter | Description
行 1:
  iRangeBf
  The start vector to do the digital capture.
行 2:
  iRangeAft
  The end vector to do the digital capture.

### Examples（取自子主题 addVecRange()）

### Generic example
```
rdi.digCap("norm").label("lpDcap_new").pin("DATA2").addVecRange(3,15).samples(10).execute();
```

Please
note that
addVecRange()
 should always be used together with

rdi.digCap().label()
.

### For multiple positions with cont()
```
rdi.digCap().pin("A").samples(100).cont();
rdi.digCap().pin("A").addVecRange(3,6).cont();
rdi.digCap().pin("A").addVecRange(10,20).cont();
rdi.digCap().execute();
```

### For multiple positions without cont()
```
rdi.digCap().pin("A").samples(100)
.addVecRange(3,6)
.addVecRange(10,20)
.execute();
```

### A range from a parameter list
```
rdi.digCap().pin("A").samples(100).cont();
for (i = 0; i < listSize(); i++)
rdi.digCap().pin("A").addVecRange(beginVec[i],endVec[i]).cont();
rdi.digCap().execute();
```

### Syntax（取自子主题 bitPerWord()）

```
bitPerWord(int iBit);
```
[表] Parameter List
列: Parameter | Description
行 1:
  iBit
  The number of bits. The default value is 32.

### Example（取自子主题 bitPerWord()）

```
rdi.digCap("norm").label("lpDcap_new").pin("DATA2").addVecRange(3,15).samples(10).bitPerWord(4).execute();
```

### Syntax（取自子主题 burstUpload()）

```
burstUpload();
```

### Examples（取自子主题 burstUpload()）

### Common upload with separated results retrieval

This example uses

burstUpload()
 to combine multiple results into a common upload, and retrieves
results one by one through individual result
ID.

```
RDI_BEGIN();
...
rdi.digCap().burstUpload().begin();
rdi.smartVec(); // register setting 1
rdi.digCap("10M").pin(A).samples(1000).execute();
rdi.smartVec(); // register setting 2
rdi.digCap("20M").pin(A).samples(2000).execute();
rdi.smartVec(); // register setting 3
rdi.digCap("30M").pin(A).samples(4000).execute();
rdi.digCap().burstUpload().end();
...
RDI_END();

ARRAY_I vec1,vec2,vec3;
vec1=rdi.id("10M").getVectorBit();
vec2=rdi.id("20M").getVectorBit();
vec3=rdi.id("30M").getVectorBit();
```

### Common upload with combined results retrieval

This example uses

burstUpload()
 to combine multiple results into a common upload, and retrieves
combined results through a common result
ID.

```
RDI_BEGIN();
...
rdi.digCap("bid").burstUpload().begin();
rdi...
rdi.digCap().pin(A).samples(1000).execute();
rdi...
rdi.digCap().pin(A).samples(2000).execute();
rdi...
rdi.digCap().pin(A).samples(4000).execute();
rdi.digCap().burstUpload().end();
...
RDI_END();

rdi.id("bid").getVector();
rdi.id("bid").getVectorBit();
```

### Syntax（取自子主题 capMode()）

```
capMode(TA::DCAP_MODE mode);
```
[表] List of parameters
列: Parameter | Description
行 1:
  mode
  The digital capture mode.
[表] List of available options of parameter: mode
列: Option | Description
行 1:
  TA::SER
  The serial digital capture mode.
    
    A vector variable is created for each capture pin with the specified number of bits per
    word.
行 2:
  TA::PAR
  The parallel digital capture mode.
    
    A vector variable is created for all capture pins with one sample per word.

### Example（取自子主题 capMode()）

```
rdi.digCap("cap").pin("DATA1,DATA2").capMode(TA::SER).samples(100).execute();
```

### Syntax（取自子主题 copyLabel()）

```
label("Label").copyLabel(boolVar);
```
[表] List of parameters
列: Parameter | Description
行 1:
  boolVar
  Specifies whether to edit an existing pattern, or create a copy
    from an existing pattern and edit the copied pattern.
[表] List of available options of parameter: bool
列: Option | Description
行 1:
  true
  Make a copy of an existing pattern and edit the copied pattern.
    This is the default
    value.
行 2:
  false
  Edit an existing pattern.

Return value

There is no return value.

### Example（取自子主题 copyLabel()）

```
RDI_BEGIN();
...
rdi.digCap().label("Label").copyLabel(false).pin("A").addVecRange(0,100).samples(100).execute();
...
RDI_END();
```

### Syntax（取自子主题 enPassFail()）

```
enPassFail();
```

### Example（取自子主题 enPassFail()）

```
RDI_BEGIN();
rdi.tmu("a").label("label1").pin("A")....enPassFail().execute()
rdi.dc("b").label("label2").pin("B")....enPassFail().execute();
rdi.digCap("c").label("label3").pin("C")....enPassFail().execute();
RDI_END();

rdi.id("a").getPassFail();
rdi.id("b").getPassFail();
rdi.dc("c").getPassFail();
```

### Syntax（取自子主题 format()）

```
format(enum format);
```
[表] List of parameters
列: Parameter | Description
行 1:
  format
  A data format to be used in a digital capture test.
    
    The data format can be one of:
    
    BIN, COMP1, COMP2,
    MOD_COMP1, SYMM, MOD_SYMM,
    GRAY, BCD, ALAW,
    MOD_ALAW, and MSB.
    
    For more information about the format definition, see `Code Format Tables`（raw: `29874.htm`）.

### Example（取自子主题 format()）

```
RDI_BEGIN()
rdi.digCap("id1").pin("pinA").format(TA::COMP).samples(1024).bitPerWord(16).execute();
rdi.digCap("id2").pin("GroupB").format(TA::GRAY).capMode(TA::PAR).samples(1000).execute();
RDI_END();
rdi.id("id1").getVector();
rdi.id("id2").getVector();
```

### Syntax（取自子主题 initDiscard()）

```
initDiscard(long iInitSkipSamples);
```

[表] List of parameters
列: Parameter | Description
行 1:
  iInitSkipSamples
  The number of initial samples to be skipped.
    
    For different types of cores, default values are different:
    
    LF core: Default value is 64.
    
    VHF or IQ core: With oversampling, the default value 64; without oversampling, the
    default value is 0.
    
    Other cores: Default value is 0.

### Example（取自子主题 initDiscard()）

```
rdi.digCap("cap").pin("DATA1").samples(100).initDiscard(10).interSkip(1,2).execute();
```

### Syntax（取自子主题 interSkip()）

```
interSkip(int iBlockLength ,int iInterSkipSamples);
```
[表] Parameter List
列: Parameter | Description
行 1:
  iBlockLength
  The number of samples to capture
行 2:
  iInterSkipSamples
  The number of samples to discard

### Example（取自子主题 interSkip()）

```
rdi.digCap("norm").label("lpDcap_new").pin("DATA2").samples(100).interSkip(2,3).execute();
```

### Syntax（取自子主题 label()）

```
label(const string& sLabelName);
```
[表] Parameter List
列: Parameter | Description
行 1:
  sLabelName
  The label name

### Example（取自子主题 label()）

```
RDI_BEGIN();
rdi.digCap("norm").label("lpDcap_new").pin("DATA2").addVecRange(3,15).samples(10).execute();
RDI_END();
```

### Syntax（取自子主题 pin()）

```
pin(const string& sPin);
```
[表] List of parameters
列: Parameter | Description
行 1:
  sPin
  The digital capture pin.

### Example（取自子主题 pin()）

```
rdi.digCap("cap").pin("DO").samples(100).execute();
```

### Syntax（取自子主题 samples()）

```
samples(long iSamples);
```
[表] List of parameters
列: Parameter | Description
行 1:
  iSamples
  The number of samples.
```

```

### Example（取自子主题 samples()）

```
rdi.digCap("cap").pin("DATA1").samples(100).execute();
```

### Syntax（取自子主题 vecVar()）

```
vecVar(string);
```

### Example（取自子主题 vecVar()）

```
RDI_BEGIN();
rdi.digCap("id").label("userLabel").vecVar("vvName1").vecVar("vvName2").execute();
RDI_END(); // "vvName1" and "vvName2" must already exist in the user pattern.

ARRAY_I ary = rdi.id("id").getVectorFromVV("vvName1");
ARRAY_I ary2 = rdi.id("id").getVectorFromVV("vvName2");
```

### Syntax（取自子主题 vecVarOnly()）

vecVarOnly()

### Example（取自子主题 vecVarOnly()）

```
RDI_BEDIN();
rdi.digCap("dcap").vecVarOnly().pin("pinA").samples(100).execute();
rdi.func("id2").label("label").execute();
RDI_END();

const ARRAY_I& aiData = rdi.id("dcap").getVector()
```

### Syntax（取自子主题 getVector()）

```
ARRAY_I& getVector(const string& pin);
```
[表] Parameter
列: Parameter | Description
行 1:
  pin
  The pin to query.

### Return value（取自子主题 getVector()）

The reference to an ARRAY_I object containing the captured
data of words.

### Examples（取自子主题 getVector()）

```
const ARRAY_I& aiData = rdi.id("cap").getVector("DATA1");
```

```
...
// gpDATA is a pin group which has DATA1 and DATA2.
rdi.digCap("cap").pin("gpDATA").samples(100).execute();
...
// Do not use a pin group name here and must use a pin list.
ARRAY_I ar = rdi.id("cap").getVector("DATA1,DATA2");
```

Note
 For the parallel transfer mode, the pin list must be used in

getVector()
 even though the pin group has been used in the setup
part.

### Syntax（取自子主题 getVectorBit()）

```
ARRAY_I& getVectorBit(const string& pin);
```
[表] Parameter List
列: Parameter | Description
行 1:
  pin
  The pin to retrieve.

### Example（取自子主题 getVectorBit()）

```
ARRAY_I arr;
arr=rdi.id("norm").getVectorBit("pinA");
```

### Syntax（取自子主题 rdi.id().getVectorFromVV()）

```
ARRAY_I& getVectorFromVV(string variableName);
```

### Example（取自子主题 rdi.id().getVectorFromVV()）

```
RDI_BEGIN();
rdi.digCap("id").label("userLabel").vecVar("vvName1").vecVar("vvName2").execute();
RDI_END();

ARRAY_I ary = rdi.id("id").getVectorFromVV("vvName1");
ARRAY_I ary2 = rdi.id("id").getVectorFromVV("vvName2");
```

### Syntax（取自子主题 getVecVar()）

```
string getVecVar(const string& pin);
```
[表] List of parameters
列: Parameter | Description
行 1:
  pin
  The pin to query.

### Example（取自子主题 getVecVar()）

```
rdi.id("dc_hidden_4pins").getVecVar("DATA2");
```

### Example（取自子主题 Using hidden upload with SmartRDI）

RF and
DC

```
virtual void run()
{
RDI_INIT();

ON_FIRST_INVOCATION_BEGIN();
{
rdi.hiddenUpload(TA::ALL);

RDI_BEGIN();
{
rdi.rfm("id1").pin("A").signal(TA::MOD_OUT).freq(1e9).bw(2e6).execute();
rdi.dc("id2").pin("A").iForce(1 mA).vMeas().execute();
rdi.dc("id3").pin("B").vForce(1 V).iMeas().average(5).execute();
}
RDI_END();
}
ON_FIRST_INVOCATION_END();

SMC_ARM();

return;
}

public:

void SMC_backgroundProcessing()
{
double pwr = rdi.id("id1").getPower();
double r1 = rdi.id("id2").getValue();
double r2 = rdi.id("id3").getValue();
}
```

Digitizer and digital
capture

```
virtual void run()
{
RDI_INIT();

ON_FIRST_INVOCATION_BEGIN();
{
rdi.hiddenUpload(TA::ALL);

RDI_BEGIN();
{
rdi.dgt("id1").pin("A").samples(1024).filter(1e6).FS(20e6).execute();
rdi.digCap("id2").pin("A").samples(1024).execute();
}
RDI_END();
}
ON_FIRST_INVOCATION_END();

SMC_ARM();

return;
}

public:

void SMC_backgroundProcessing()
{
ARRAY_D wave1 = rdi.id("id1").getWaveform();
ARRAY_I bits = rdi.id("id2").getVectorBit();
}
```

Error
map

```
virtual void run()
{
RDI_INIT();

ON_FIRST_INVOCATION_BEGIN();
{
rdi.hiddenUpload(TA::ALL); // Include the EMAP mode

RDI_BEGIN();
{
rdi.smartVec("rb").pin("A").readBit(100).execute();
rdi.emap("fc").label("bbb").pin("A").failCyc().execute();
}
RDI_END();
}
ON_FIRST_INVOCATION_END();

SMC_ARM();

return;
}

public:

void SMC_backgroundProcessing()
{
rdi.id("rb").getReadBit();
rdi.id("fc").getFailCyc();
}
```

### Example（取自子主题 SmartRDI: Digital channel relay control）

```
RDI_BEGIN();
rdi.hwRelay().pin("pinA").setOn("DC,AC").setOff("PPMU").execute();
rdi.hwRelay().pin("pinB").setOff("ALL").execute();
RDI_END();
```

See

`setOn()`（raw: `141810.htm`）
 for more information about
AMUX_PPMU
 and

AMUX_BADC
 relay options.

### Syntax（取自子主题 pin()）

```
pin(const string& sPin);
```
[表] List of parameters
列: Parameter | Description
行 1:
  sPin
  One or more digital pin names.
    
    For more pin names, separate them with comma.

### Example（取自子主题 pin()）

```
rdi.hwRelay().pin("pinA").setOn("DC,AC").setOff("PPMU").execute();
```

### For protocol or smartVec test（取自子主题 runTimeVal()）

```
runTimeVal(const string& name, const ARRAY_I& value);
runTimeVal(const string& name, const ARRAY_LL& value);
runTimeVal(const string& name, const long long value);
runTimeVal(const string& name, const ARRAY_D &value);
runTimeVal(const string& name, const double value);
runTimeVal(const string& name, const int value);
runTimeVal(const string& name, vector<ARRAY_I> &value);
runTimeVal(const string& name, vector<ARRAY_LL> &value);
runTimeVal(const string& name, vector<vector<string>> &value);
```

[表] runTimeVal data types for vector editing
列: smartVec() function | runTimeVal() Data type | Description
行 1:
  `writeVec(string rtv, int vecPos)`（raw: `149037.htm`） [跨 2 行]
  vector<ARRAY_I>
  Different vectors per site.
行 2:
  ARRAY_I
  Same vectors on all sites.
行 3:
  `writeBit(string rtv, int bitPos)`（raw: `149044.htm`） [跨 2 行]
    `expectBit(string rtv, int bitPos)`（raw: `149046.htm`）
  vector<ARRAY_I>
  Different bitStreams per site.
行 4:
  ARRAY_I
  Same bitStreams on all sites.
行 5:
  `writeData(string rtv, int numOfBits, int bitPos)`（raw: `149051.htm`） [跨 2 行]
    `expectData(string rtv, int numOfBits, int bitPos)`（raw: `149056.htm`）
  ARRAY_I or ARRAY_LL
  Different data per site.
行 6:
  Int or long long
  Same data on all sites.
行 7:
  `writeParData(string rtv, int bitPos)`（raw: `149054.htm`） [跨 2 行]
  ARRAY_I or ARRAY_LL
  Different data per site.
行 8:
  Int or long long
  Same data on all sites.

See the
`example`（raw: `144754.htm#_144754__example_runtime_vec_edit`）
 below.

### For DC test, TMU, and RF stimulus（取自子主题 runTimeVal()）

```
runTimeVal(const string& name, const ARRAY_D &value);
runTimeVal(const string& name, const double value);
runTimeVal(const string& name, vector<anaWaveform> &value);
```

### For func and hwRelay（取自子主题 runTimeVal()）

```
runTimeVal(const string& name, vector<string> &value);
```

[表] List of parameters
列: Parameter | Description
行 1:
  name
  The name of the parameter which value can be changed at runtime.
行 2:
  value
  The value to be used at runtime. The array type of value can contain different values for
    different sites.

### Examples（取自子主题 runTimeVal()）

Using different values for different
sites

```
ARRAY_D rtv_arr(4);
rtv_arr[0]=1.0;
rtv_arr[1]=1.1;
rtv_arr[2]=1.2;
rtv_arr[3]=1.3;

rdi.runTimeVal("rtv",rtv_arr);
```

Using
the same value for all
sites

```
double vol; vol=1.5;
rdi.runTimeVal("vvv",vol);
```

Controlling relays

```
vector <string> rtRelay(2); // 2 sites
rtRelay[0] = "AC"; // AC relay on site 1 is selected
rtRelay[1] = "PPMU"; // PPMU relay on site 2 is selected

rdi.runTimeVal("rtd", rtRelay);

RDI_BEGIN();
rdi.hwRelay().pin().setOnRunTime("rtd").execute();
RDI_END();
```

"NO"
 action on one site and some action on another in
runtime

```
vector<string> vecOn(2), vecOff(2); //2 sites
vecOn[0]="NO"; vecOn[1]="AC";
vecOff[0]="AC"; vecOff[1]="NO";

rdi.runTimeVal("rt1",vecOn);
rdi.runTimeVal("rt2",vecOff);

//----------- site1 opens AC; site2 closes AC----------------------------
RDI_BEGIN();
rdi.hwRelay().pin("A").setOnRunTime("rt1").setOffRunTime("rt2").execute();
RDI_END();
```

Alarm checking on pins using runTimeVal()

```
...
rdi.runTimeVal("rtvForce", rtvForce);
rdi.dc().pin("rtvPin").vForce(0 V).iClamp(50 uA).execute();

RDI_BEGIN();
...
rdi.dc("id").pin("rtvPin").vForce("rtvForce").iClamp(50 uA)
.vMeas().measwait(100 us).execute();
...
RDI_END();
```

See
`Alarm checking on pins using runTimeVal()`（raw: `345141.htm#_345141__alarm_check_on_pins_with_runTimeVal`）

Runtime vector editing

```
ARRAY_I trimData = ... // based on previous measurement.
rdi.runTimeVal("trimValue", trimData);

RDI_BEGIN();
...
rdi.smartVec().pin(pinA).writeData("trimValue",8).execute();
...
RDI_END();
```

### Syntax（取自子主题 setOff()）

```
setOff(const string& sRelays);
```
[表] Parameter
列: Parameter | Description
行 1:
  sRelays
  The string defines the relays to open. It can be any combination of the strings
    
    "DC",
    
    "AC" or
    
    "PPMU"
    
    separated by a comma (",").
    
    You can also use "ALL" to open all three relays.

### Example（取自子主题 setOff()）

```
rdi.hwRelay().pin("pinA")
.setOn("DC,AC")
.setOff("PPMU")
.execute();
```

### Syntax（取自子主题 setOffRunTime()）

```
setOffRunTime(string runTimeValueString);
```
[表] Parameter
列: Parameter | Description
行 1:
  runTimeValueString
  The string defines the runtime value.

### Examples（取自子主题 setOffRunTime()）

### In the dynamic mode

```
vector <string> rtRelay(2); // 2 sites
rtRelay[0] = "AC"; // AC relay on site 1 is selected
rtRelay[1] = "PPMU"; // PPMU relay on site 2 is selected

rdi.runTimeVal("rtd", rtRelay);

RDI_BEGIN();
rdi.hwRelay().pin().setOffRunTime("rtd").execute();
RDI_END();
```

### In the static mode

```
vector <string> rtRelay(2); // 2 sites
rtRelay[0] = "AC"; // AC relay on site 1 is selected
rtRelay[1] = "PPMU"; // PPMU relay on site 2 is selected

rdi.runTimeVal("rtd", rtRelay);
rdi.hwRelay().pin(A).setOffRunTime("rtd").execute(); //static
```

### Syntax（取自子主题 setOn()）

```
setOn(const string& sRelays);
```
[表] Parameter
列: Parameter | Description
行 1:
  sRelays
  The string defines the relays to close. It can be any combination of the
    strings
    
    "DC",
    
    "AC" or
    
    "PPMU"
    
    separated by a comma (",").
    
    You can also use "ALL" to connect all three relays.
    
    It also can be:
    
    "AMUX_PPMU": Closes the pin's PPMU relay. The signal will pass
    though PPMU and reach the multiplexer. Then, the multiplexer will transfer this signal to
    the board ADC.
    
    "AMUX_BADC":
    This option controls the multiplexer before a board
    ADC to select the voltage signal coming from the measured pin that has been connected to
    a DC Line and inputs it to the board ADC for value measurement. To close the DC relay,
    use setOn("DC") one more time. See the example below.
    
    See the
    MUX_VM_HIZ_ON description in the `PPMU_PIN_RELAY`（raw: `29612.htm`） topic for more
    information.
    
    These two options work only with setOn(). Do NOT use them with
    setOff(), for example, setOff("AMUX_PPMU").
    CAUTION In the high impedance mode, the board ADC may generate a spike when the DC
    relay of a digital bin is being closed. To avoid the spike occurrence, discharge the board
    ADC or force a voltage before the next measurement.

### Example（取自子主题 setOn()）

```
rdi.hwRelay().pin("pinA").setOn("DC,AC").setOff("PPMU").execute();
rdi.hwRelay().pin("pinB").setOn("AMUX_PPMU").execute();
rdi.hwRelay().pin("pinC").setOn("AMUX_BADC").execute();
```

Using
setOn("AMUX_BADC")
 to configure AMUX and

setOn("DC")
 to close the DC relay:

```
rdi.hwRelay().pin("pinA").setOn("AMUX_BADC").setOff("AC_PPMU").execute(); // AMUX on
rdi.hwRelay().pin("pinA").setOn("DC").execute(); // DC on
rdi.hwRelay().pin("pinA").setOff("All").execute(); // All off
```

### Syntax（取自子主题 setOnRunTime()）

```
setOnRunTime(string runTimeValueString);
```
[表] Parameter
列: Parameter | Description
行 1:
  runTimeValueString
  The string defines the runtime value.

### Examples（取自子主题 setOnRunTime()）

### In the dynamic mode

```
vector <string> rtRelay(2); // 2 sites
rtRelay[0] = "AC"; // AC relay on site 1 is selected
rtRelay[1] = "PPMU"; // PPMU relay on site 2 is selected

rdi.runTimeVal("rtd", rtRelay);

RDI_BEGIN();
rdi.hwRelay().pin().setOnRunTime("rtd").execute();
RDI_END();
```

### In the static mode

```
vector <string> rtRelay(2); // 2 sites
rtRelay[0] = "AC"; // AC relay on site 1 is selected
rtRelay[1] = "PPMU"; // PPMU relay on site 2 is selected

rdi.runTimeVal("rtd", rtRelay);
rdi.hwRelay().pin(A).setOnRunTime("rtd").execute(); //static
```

### Syntax（取自子主题 rdi.route()）

Usage of the function:

The function can be called in the code‑based mode or in the pattern‑based mode.
For more information, refer to
`Pattern-based mode`（raw: `142069.htm#_142069__dle_Pattern-based_mode`）
 and

`Code-based mode`（raw: `142069.htm#_142069__dle_Code-based_mode`）
 in topic
`SmartRDI`（raw: `142069.htm`）
.

```
routeGroup& route(const int id);
routeGroup& route(const string& id="");
```

[表] List of parameters
列: Parameter | Description
行 1:
  id
  Optional ID for the following setups.
    The parameter can be
    defined as int or as
    string.
    
    Default value: Empty string
    ""

### Return value（取自子主题 rdi.route()）

A reference to the
routeGroup
 object.

### Example（取自子主题 rdi.route()）

### Example 1

```
RDI_INIT();
...
...
ON_FIRST_INVOCATION_BEGIN();
{
...
...
RDI_BEGIN();
{
...
...
rdi.route().applyState("Connect_load").execute();
...
...
}
RDI_END();
...
...
}
ON_FIRST_INVOCATION_END();
...
...
```

### Example（取自子主题 SmartRDI: Error map results from user patterns）

This diagram shows an error map example.

In this example, results are:

failCount
= 3

failCyc
= 10, 14, 17

pfMap
= 1,1,1,1,0,1,1,1,0,1,1,0,1

FFC
= 10

The cycle number starts from "0".

The following example includes all functions of
the
emap()

class:

```
ON_FIRST_INVOCATION_BEGIN();
rdi.emapLocation(TA::RAM);
RDI_BEGIN();
rdi.emap("a").label("label1").pin("pA").failCount().pfMap()
.pin("pC").failCyc(5).execute();
rdi.emap("b").label("label2").pin("pB").FFC(150).execute();
RDI_END();
ON_FIRST_INVOCATION_END();

int fcount=rdi.id("a").getFailCount("pA");
ARRAY_BOOL map=rdi.id("a").getPfMap("pA");
ARRAY_LL fcPostion=rdi.id("a").getFailCyc("pC");
int ffc=rdi.id("b").getFFC();
```

### Syntax（取自子主题 combinedFailCount()）

```
combinedFailCount(long startCycle);
```

[表] List of parameters
列: Parameter | Description
行 1:
  startCycle
  The number of the first cycle in the label in which the fails are counted.
    Default
    is 0, which means the start of the pattern.

### Example（取自子主题 combinedFailCount()）

```
RDI_BEGIN();
rdi.emap("a").label("pat").pin("@").combinedFailCount().execute();
RDI_END();
int dVal =rdi.id("a").getCombinedFailCount();
```

Note
 pin("@") can only be used for the combinedFailCount() command and cannot be
used with all the other error map commands.

### Syntax（取自子主题 emapLocation()）

```
emapLocation(TA::EMAP_LOCATION location);
```
[表] List of parameters
列: Parameter | Description
行 1:
  location
  The location of type TA::EMAP_LOCATION that
    defines where error maps are stored.
[表] List of available options of parameter: location
列: Option | Description
行 1:
  TA::TP
  The location is the internal test processor memory.
行 2:
  TA::RAM
  The location is the unused vector memory.

### Example（取自子主题 emapLocation()）

```
rdi.emapLocation(TA::RAM);
```

### Syntax（取自子主题 failCount()）

The Vector class there is no return value.

```
failCount(int startCyc,int cycRange)
failCount(int startCyc) // From the start cycle to the end.
failCount() // From the beginning to the end.
```

[表] List of parameters
列: Parameter | Description
行 1:
  startCyc
  The number of the first cycle in the cycle range in which the fails are counted. An
    integer. Cycle numbers are zero-based.
    
    This is an optional parameter. If it is omitted, the cycle range starts with the first
    cycle.
行 2:
  cycRange
  The number of the cycles in the cycle range in which the fails are counted. An integer.
    Cycle numbers are zero-based.
    
    This is an optional parameter. If it is omitted, the cycle range ends with the last
    cycle.

Note

The fail count and fail position are about "compare edge" (not tester cycle). So they
supports xMode directly.

The xMode parameter for a pin must be correct, otherwise the result for the pin will not
be correct.

The parameter specified in the function, such as
startCyc
 and

cycRange
, is about user cycles (edge), not tester cycles. This setting is
critical when xMode is set to be greater than 1.

For one pin, xMode must remain the same in different labels in burst; otherwise the
results might be wrong.

### Example（取自子主题 failCount()）

```
rdi.emap("a").label("label1").pin("pA").failCount().pfMap().pin("pC").failCyc(5).execute();
```

### Syntax（取自子主题 failCyc()）

```
failCyc(int startCyc,int cycRange);
failCyc(int startCyc); // From the start cycle to the end.
failCyc(); // From the beginning to the end.
```

[表] List of parameters
列: Parameter | Description
行 1:
  startCyc
  The number of the first cycle in the cycle range in which the fails are counted. An
    integer. Cycle numbers are zero-based.
    
    This is an optional parameter. If it is omitted, the cycle range starts with the first
    cycle.
行 2:
  cycRange
  The number of the cycles in the cycle range. An integer. Cycle numbers are
    zero-based.
    
    This is an optional parameter. If it is omitted, the cycle range ends with the last
    cycle.

Note

The fail count and fail position are about "compare edge" (not tester cycle). So they
supports xMode directly.

The xMode parameter for a pin must be correct, otherwise the result for the pin will not
be correct.

The parameter specified in the function, such as
startCyc
 and

cycRange
, is about user cycles (edge), not tester cycles. This setting is
critical when xMode is set to be greater than 1.

For one pin, the xMode must remain the same in different labels in burst; otherwise the
results might be wrong.

### Example（取自子主题 failCyc()）

```
rdi.emap("a").label("label1").pin("pA").failCount().pfMap().pin("pC").failCyc(5).execute();
```

### Syntax（取自子主题 FFC()）

```
FFC(int startCyc); // From the start cycle to the end.
FFC(); // From the beginning to the end.
```
[表] List of parameters
列: Parameter | Description
行 1:
  startCyc
  The number of the first cycle in the cycle range in which the fails are counted. An
    integer. Cycle numbers are zero-based.
    
    This is an optional parameter. If it is omitted, the cycle range starts with the first
    cycle.

Note

The fail count and fail position are about "compare edge" (not tester cycle). So they
supports xMode directly.

The xMode parameter for a pin must be correct, otherwise the result for the pin will not
be correct.

The parameter specified in the function, such as
startCyc
 and

cycRange
, is about user cycles (edge), not tester cycles. This setting is
critical when xMode is set to be greater than 1.

For one pin, xMode must remain the same in different labels in burst; otherwise the
results might be wrong.

### Example（取自子主题 FFC()）

```
rdi.emap("b").label("label2").pin("pB").FFC(150).execute();
```

### Syntax（取自子主题 FFV()）

```
FFV(int startCycle);
```

[表] List of parameters
列: Parameter | Description
行 1:
  startCycle
  The number of the first cycle in the cycle range.

### Example（取自子主题 FFV()）

```
RDI_BEGIN();
rdi.emap("a").label("label2").pin("pB")
.FFV(10).execute();
RDI_END();

int iffv=rdi.id("a").getFFV();
```

### Syntax（取自子主题 label()）

```
label(const string& sLabelName);
```

[表] List of parameters
列: Parameter | Description
行 1:
  sLabelName
  The label to be executed.

### Example（取自子主题 label()）

```
rdi.emap("a").label("label1").pin("pA").failCount().pfMap()
.pin("pC").failCyc(5).execute();
```

### Syntax（取自子主题 multiFFC()）

```
multiFFC(int startCycle, int FailNumber);
```

[表] List of parameters
列: Parameter | Description
行 1:
  startCycle
  The number of the first cycle to start the action.
行 2:
  FailNumber
  The number of failing cycles within a pattern to acquire.

Use the following functions to collect the result:

getMultiFFC(string resultPin)

getMultiFFC()
:Use this command if only one result pin exists.

Note

The fail count and fail position are about "compare edge" (not tester cycle). So they
supports
`xMode`（raw: `149062.htm`）
 directly.

The
`xMode`（raw: `149062.htm`）
 parameter for a pin must be correct, otherwise the
result for the pin will not be correct.

The parameter specified in the function, such as
startCyc
 and

cycRange
, is about user cycles (edge), not tester cycles. This setting is
critical when
`xMode`（raw: `149062.htm`）
 is set to be greater than 1.

For one pin,
`xMode`（raw: `149062.htm`）
 must remain the same in different labels
in burst; otherwise the results might be wrong.

### Example（取自子主题 multiFFC()）

```
RDI_BEGIN();
rdi.emap("mffc").label("abc")
.pin("inA")
.multiFFC(0,100)
.execute();
/* For smartVec():
rdi.smartVec("mffc").label("abc")
.pin("inA")
.multiFFC(0,100)
.execute();
*/

RDI_END();

rdi.id("mffc").getMultiFFC();
```

### Syntax（取自子主题 pfMap()）

```
pfMap(int startCyc,int cycRange)
pfMap(int startCyc) // From the start cycle to the end.
pfMap() // From the beginning to the end.
```
[表] List of parameters
列: Parameter | Description
行 1:
  startCyc
  The number of the first cycle in the cycle range in which the fails are counted. An
    integer. Cycle numbers are zero-based.
    
    This is an optional parameter. If it is omitted, the cycle range starts with the first
    cycle.
行 2:
  cycRange
  The number of the cycles in the cycle range. An integer. Cycle numbers are
    zero-based.
    
    This is an optional parameter. If it is omitted, the cycle range ends with the last
    cycle.

Note

The fail count and fail position are about "compare edge" (not tester cycle). So they
supports xMode directly.

The xMode parameter for a pin must be correct, otherwise the result for the pin will not
be correct.

The parameter specified in the function, such as
startCyc
 and

cycRange
, is about user cycles (edge), not tester cycles. This setting is
critical when xMode is set to be greater than 1.

For one pin, the xMode must remain the same in different labels in burst; otherwise the
results might be wrong.

### Example（取自子主题 pfMap()）

```
rdi.emap("a").label("label1").pin("pA").failCount().pfMap().pin("pC").failCyc(5).execute();
```

### Syntax（取自子主题 rdi.func().startVec()）

```
rdi.func().startVec(int vec);
```
[表] List of parameters
列: Parameter | Description
行 1:
  vec
  The number of a vector in the pattern.

### Examples（取自子主题 rdi.func().startVec()）

### Example 1

For an IDDQ test, the code could be:

```
RDI_BEGIN();
rdi.func().label("abc").stopVec(39).execute();
rdi.dc().pin("VDD").iMeas().execute();
rdi.func().label("abc").startVec(40).stopVec(49).execute();
rdi.dc().pin("VDD").iMeas().execute();
rdi.func().label("abc").startVec(50).stopVec(80).execute();
rdi.dc().pin("VDD").iMeas().execute();
RDI_END();
```

Vector lines start from 0.

### Example 2

startVec() and stopVec() are supported in the
`emap()`（raw: `149537.htm`）

class.

```
RDI_BEGIN();

rdi.emap("id").label("abc").pin("A")
.startVec(10).stopVec(30)
.failCout(5,10).FFC(5).execute();

RDI_END();
...
rdi.id("id").getFailCout();
rdi.id("id").getFFC();
```

In this example, a new pattern
abc_START_10_STOP_30
 will be generated,
which begins at
startVec(10)
 and ends at
stopVec(30)
. The

FFC(5)
 means that the start cycle 5 is in the new generated pattern.

### Syntax（取自子主题 rdi.func().stopVec()）

```
rdi.func().stopVec(int vec);
```
[表] List of parameters
列: Parameter | Description
行 1:
  vec
  Vector line

### Examples（取自子主题 rdi.func().stopVec()）

### Example 1
```
rdi.func().label("label").stopVec(vec).execute();
```

### Example 2

startVec() and stopVec() are supported in the
`emap()`（raw: `149537.htm`）

class.

```
RDI_BEGIN();

rdi.emap("id").label("abc").pin("A")
.startVec(10).stopVec(30)
.failCout(5,10).FFC(5).execute();

RDI_END();
...
rdi.id("id").getFailCout();
rdi.id("id").getFFC();
```

In this example, a new pattern
abc_START_10_STOP_30
 will be generated. The

FFC(5)
 means that the start cycle 5 is in the new generated pattern.

### Syntax（取自子主题 xMode()）

```
xMode(int Xmode);
```
[表] List of parameters
列: Parameter | Description
行 1:
  Xmode
  The number of device cycles in each tester cycle.

Note

The fail count and fail position are about "compare edge" (not tester cycle). So they
supports xMode directly.

The xMode parameter for a pin must be correct, otherwise the result for the pin will not
be correct.

The parameter specified in the function, such as
startCyc
 and

cycRange
, is about user cycles (edge), not tester cycles. This setting is
critical when xMode is set to be greater than 1.

For one pin, xMode must remain the same in different labels in burst; otherwise the
results might be wrong.

Note
 For correctly retrieving the results of error map data:

For a specified pin, in one RDI_BEGIN/RDI_END block, its xMode number must remain the same
value, no matter it is for a SmartRDI command or in the user pattern.

In the wavetable, the length of the device cycle name must align with the xMode() value.
For example, if you set xMode to xMode(2), the dvc must correspondingly have two letters,
such as "LL", "00", "11", "LL". Even the dvc of the physical index f, which normal value is
"." with SmartRDI, must be ".." for xMode(2). Otherwise SmarTest cannot recognize the correct
xMode value from pattern.

### Example（取自子主题 xMode()）

```
RDI_BEGIN();
rdi.emap().label("abc").pin("DATA").failCount().xMode(4).execute();
RDI_END();
```

### Syntax（取自子主题 getFailCount()）

```
int getFailCount(string pin)
```
[表] List of parameters
列: Parameter | Description
行 1:
  pin
  The name of the pin for which to count the fails.
    Note It can only be a single pin.
    Do not use multiple pins, a pin group or @ for all pins.

### Example（取自子主题 getFailCount()）

### General example
```
int fcount=rdi.id("a").getFailCount("pinA");
```

### Syntax（取自子主题 getFailCyc()）

```
ARRAY_LL getFailCyc(string sPin);
```
[表] Parameter
列: Parameter | Description
行 1:
  sPin
  The name of the pin for which to return the failing cycle positions.
    Note It can only
    be a single pin. Do not use multiple pins, a pin group or @ for all pins.

### Return value（取自子主题 getFailCyc()）

An ARRAY_LL object containing failing cycle positions is
returned.

### Example（取自子主题 getFailCyc()）

```
ARRAY_LL fcPostion=rdi.id("a").getFailCyc("pC");
```

### Return value（取自子主题 getFFC()）

The return value is an integer indicating the first failing cycle.

### Example（取自子主题 getFFC()）

```
int ffc=rdi.id("b").getFFC("pA");
```

### Syntax（取自子主题 getPfMap()）

```
ARRAY_BOOL getPfMap(string pin)
```
[表] List of parameters
列: Parameter | Description
行 1:
  pin
  The name of the pin for which to return the pass/fail map.
    Note It can only be a
    single pin. Do not use multiple pins, a pin group or @ for all pins.

### Example（取自子主题 getPfMap()）

```
ARRAY_BOOL map=rdi.id("a").getPfMap("pA");
```

### Syntax（取自子主题 rdi.id().getCombinedFailCount()）

```
ARRAY_LL getCombinedFailCount();
```

### Example（取自子主题 rdi.id().getCombinedFailCount()）

```
RDI_BEGIN();
rdi.emap("a").label("pat").pin("@").combinedFailCount().execute();
RDI_END();
int dVal =rdi.id("a").getCombinedFailCount();
```

Note
 pin("@") can only be used for the combinedFailCount() command and cannot be
used with all the other error map commands.

### Syntax（取自子主题 rdi.id().getFFV()）

```
int getFFV(string pin);
```

[表] List of parameters
列: Parameter | Description
行 1:
  pin
  The name of the pin for which to return the number of the first fail vector.
    
    It can only be a single pin. Do not use multiple pins, a pin group or @ for all pins.

### Example（取自子主题 rdi.id().getFFV()）

Working together with
`FFV()`（raw: `350386.htm`）
.

```
RDI_BEGIN();
rdi.emap("a").label("label2").pin("pB")
.FFV(10).execute();
RDI_END();

int iffv=rdi.id("a").getFFV("pB");
```

### Syntax（取自子主题 rdi.id().getMultiFFC()）

```
ARRAY_LL getMultiFFC(string pin);
ARRAY_LL getMultiFFC(); // if only one result pin exists.
```

[表] List of parameters
列: Parameter | Description
行 1:
  pin
  The pin for which to retrieve the number of failing cycles.

### Example（取自子主题 rdi.id().getMultiFFC()）

```
RDI_BEGIN();
rdi.emap("mffc").label("abc")
.pin("inA")
.multiFFC(0,100)
.execute();
RDI_END();

rdi.id("mffc").getMultiFFC();
```

### Syntax（取自子主题 SMC_PIN_ERROR_MAP）

```
SMC_PIN_ERROR_MAP( const STRING &pinName, const STRING &resultArea);
SMC_PIN_ERROR_MAP(const int site, const STRING &pinName, const STRING &resultArea);
```

This
API is defined in the header file

/opt/hp93000/soc/prod_com/include/MAPI/SMART_CALC2.h
.

Parameters
[表]
列: Parameter | Description
行 1:
  pinName
  The pin for which the error map will be
    uploaded.
行 2:
  resultArea
  The name of the result area which is used to acquire
    the fail data.
行 3:
  site
  The site number.
Return value
The constructor has no return value.

### Example（取自子主题 SMC_PIN_ERROR_MAP）

The following example shows how to upload a pin error map data. The default upload
chunk size of 512KB is used.

```
virtual void run()
{
ON_FIRST_INVOCATION_BEGIN();

// Variables.
STRING mPinaName = "PinA";
STRING mAreaId = "Area1";

// Select result area for storing results.
RESULT_AREA_CONFIG_SET resArea(mAreaId);
resArea.setAsPrimary();

//Configure result mode
RESULT_CONFIGURATION resConfig;
resConfig.setResultStorageLocation(RESULT_CONFIGURATION::RAM);
resConfig.setResultGranularity(RESULT_CONFIGURATION::cycle,"@");
resConfig.setNumberOfResultsPerCycle(RESULT_CONFIGURATION::RPC8);
resConfig.setResultWidth(RESULT_CONFIGURATION::_1Bit);
resConfig.enable();

// Run functional test.
SMC_FUNCTIONAL_TEST();

// Loop over all sites and upload results
FOR_EACH_SITE_BEGIN();

SMC_ARM(mPinName, mAreaId);

FOR_EACH_SITE_END();

// A newly created result configuration contains the default settings.
// This can be used to reset the result configuration:

RESULT_CONFIGURATION defaultConfig;
defaultConfig.enable();
resArea.deselectGlobally();

ON_FIRST_INVOCATION_END();

return;
}

public:

void SMC_backgroundProcessing(string pin, string Area)
{
CYCLE_CHUNK cycles;

SMC_PIN_ERROR_MAP errorMap(pin,Area);

while ( true == errorMap.getNextCycleChunk(cycles))
{
// Outputs result information, only needed for debug information
cout << cycles;

// do post processing
}
}
```

### Example（取自子主题 Functional test setup）

```
ON_FIRST_INVOCATION_BEGIN();
RDI_BEGIN();
rdi.func("f1").label("PATT1").execute();
rdi.func().burst("BURST1").execute();
RDI_END();
ON_FIRST_INVOCATION_END();
int result1 = rdi.id( "f1" ).getPassFail(); //result for PATT1
int result2 = rdi.getBurstPassFail(); // result for PATT1 and BURST1
```

### Member functions（取自子主题 FUNC）

[表]
列: Setup
行 1:
  `rdi.func().burst()`（raw: `143122.htm`）
行 2:
  `rdi.func().burstId()`（raw: `148642.htm`）
行 3:
  `rdi.func().burstRunTime()`（raw: `348893.htm`）
行 4:
  `rdi.func().execute()`（raw: `355436.htm`）
行 5:
  `rdi.func().label()`（raw: `141530.htm`）
行 6:
  `rdi.func().labelRunTime()`（raw: `149521.htm`）
行 7:
  `rdi.func().perLabelPassFail()`（raw: `348961.htm`）
行 8:
  `rdi.func().pin()`（raw: `355399.htm`）
行 9:
  `rdi.func().startVec()`（raw: `149585.htm`）
行 10:
  `rdi.func().stopVec()`（raw: `149338.htm`）
行 11:
  `rdi.port(TA::MULTI_PORT).func()`（raw: `353728.htm`）
[表]
列: Result retrieval
行 1:
  `rdi.getBurstPassFail()`（raw: `141532.htm`）
行 2:
  `rdi.id().getBurstPassFail()`（raw: `148644.htm`）
行 3:
  `rdi.id().getLabel()`（raw: `149592.htm`）
行 4:
  `rdi.id().getMultiPassFail()`（raw: `348894.htm`）
行 5:
  `rdi.id().getPassFail()`（raw: `141723.htm`）
[表]
列: For match loops
行 1:
  Setup [跨 2 行]
  `rdi.func().readMatchCount()`（raw: `149589.htm`）
行 2:
  `rdi.func().readMatchPassFail()`（raw: `149588.htm`）
行 3:
  Result retrieval [跨 2 行]
  `rdi.id().getMatchCount()`（raw: `149591.htm`）
行 4:
  `rdi.id().getMatchPassFail()`（raw: `149590.htm`）

### Example（取自子主题 Retrieving match loop results from user patterns）

```
RDI_BEGIN();
rdi.func("mch").label("abc").readMatchPassFail("pinA")
.readMatchCount("pinA").execute();
RDI_END();
rdi.id("mch").getMatchPassFail();
rdi.id("mch").getMatchCount();
```

### Syntax（取自子主题 rdi.func().burst()）

```
rdi.func().burst(const string& sLabelName);
```
[表] List of parameters
列: Parameter | Description
行 1:
  sLabelName
  The burst pattern name

### Examples（取自子主题 rdi.func().burst()）

### Example 1

Specifying an existing burst label to be executed in the functional test

```
RDI_BEGIN();
rdi.dc().pin("dig").vForce(1 V).execute();
rdi.func().burst("ExistBurst").execute();
rdi.digCap().pin("dig2").samples(8).execute();
RDI_END();
```

### Example 2 Working together with port() actions

Combining an existing burst label with other port actions, such as dc, digCap, and emap
actions.

One
port:

```
RDI_BEGIN();
rdi.port("pt1")
rdi.port("pt1").func().burst("ExistBurst").execute();
rdi.port("pt1")....
RDI_END();
```

Multiple
ports:

```
RDI_BEGIN();
rdi.port("pt1").dc().pin("dig").vForce(1 V).execute();
rdi.port("pt1").func().burst("ExistBurst").execute();
rdi.portSync();
rdi.port("pt2").func().burst("ExistBurst").execute();
rdi.port("pt2").digCap().pin("dig2").samples(8).execute();
RDI_END();
```

### Retrieving the pass/fail results

Use
ARRAY_I& getMultiPassFail(string sPort=="@");
 to get all pass/fail
results for each main label from the burst label on different
ports.

```
RDI_BEGIN();
...
rdi.port("pt1").func("id1").burst("MPBurst1").execute();
...
rdi.port("pt2").func("id2").burst("MPBurst2").execute();
...
RDI_END();

int pf = rdi.id("id1").getPassFail(); // returns 0
ARRAY_I ary2 = rdi.id("id1").getMultiPassFail(); // returns { 0,1,0 } ,1st and 3rd label failed

int pf = rdi.id("id1").getPassFail(); // returns 1
ARRAY_I ary3 = rdi.id("id2").getMultiPassFail(); // returns { 1,1,1 }, all 3 labels passed
```

### Syntax（取自子主题 rdi.func().burstId()）

```
void rdi.func().burstId(string burstId, string resultPins);
```
[表] List of parameters
列: Parameter | Description
行 1:
  burstId
  The ID assigned to a burst pattern test.
行 2:
  resultPins
  A pin, multiple pins, the name of a pin group or a port to generate the pass/fail test
    result.
    
    If no pin is specified, all pins are used by default.
    
    Note Any ID specified in rdi.burstId() must match those result IDs specified
    in getBurstPassFail(). For example, if a pin group ID is specified in burstId(), you must
    use the group ID in getBurstPassFail(). If you use an ID of a pin from the group,
    getBurstPassFail() cannot return the result for the pin.

### Examples（取自子主题 rdi.func().burstId()）

### Generic example
```
{
...
ON_FIRST_INVOCATION_BEGIN();

RDI_BEGIN();
rdi.burstId("bid1","pinA,pinB");
// Burst pattern setups and execution
...
RDI_END();

RDI_BEGIN();
rdi.burstId("bid2","pinGrpAB");
// Burst pattern setups and execution
...
RDI_END();

ON_FIRST_INVOCATION_END();

int result = rdi.id("bid1").getBurstPassFail("pinA"); // Retrieve the burst pattern test result from pinA.
int result = rdi.id("bid1").getBurstPassFail("pinB"); // Retrieve the burst pattern test result from pinB.
int result = rdi.id("bid2").getBurstPassFail("pinGrpAB"); // Retrieve the burst pattern test result from the pin group.
int resultALL = rdi.id("bid1").getBurstPassFail(); // Retrieve the burst pattern test result from all pins.
...
}
```

### For a port ID
```
RDI_BEGIN();
rdi.burstId("idA","ptA"); // ptA is a port
rdi.func()...
rdi.dc()...
rdi.smartVec()...
...
RDI_END();

rdi.id("idA").getBurstPassFail("ptA");
```

### Syntax（取自子主题 rdi.func().burstRunTime()）

```
rdi.func().burstRunTime(string sRunTime,int iMaxNum);
```

[表] List of parameters
列: Parameter | Description
行 1:
  sRunTime
  The runtime value.
行 2:
  iMaxNum
  The maximum number of burst labels to be patched.

### Example（取自子主题 rdi.func().burstRunTime()）

```
vector<string> vec_port1;
vec_port1.clear();
vec_port1.push_back("label3");
vec_port1.push_back("label7");
vec_port1.push_back("label25");
vec_port1.push_back("label31");
rdi.runTimeVal("rt",vec_port1); // The label to be patched into the burst.

RDI_BEGIN();
rdi.port("A").func("id").burstRunTime("rt",200).execute();
RDI_END();

ARRAY_I ary = rdi.id("id").getMultiPassFail();
```

### Syntax（取自子主题 rdi.func().label()）

```
rdi.func().label(const string& sLabelName);
```
[表] List of parameters
列: Parameter | Description
行 1:
  sLabelName
  The label to be executed.

### Example（取自子主题 rdi.func().label()）

```
rdi.func().label("PATT1").execute();
```

### Syntax（取自子主题 rdi.func().labelRunTime()）

```
rdi.func().labelRunTime(const string& runTimeId);
```
[表] List of parameters
列: Parameter | Description
行 1:
  runTimeId
  The ID of the label you want to run.

### Example（取自子主题 rdi.func().labelRunTime()）

```
vector <string> siteLabel(siteNum); // Labels for each site.

siteLabel[0]="A1"; // Change label, site 1.
siteLabel[1]="B1"; // Change label, site 2.
siteLabel[2]="NO_LABEL"; // Change label, site 3.
...
rdi.runTimeVal("rtID", siteLabel);
RDI_BEGIN();
rdi.func().labelRunTime("rtID").execute(); //Label "A1" and "B1" are generated for site 1 and 2; no label is generated on site 3.
RDI_END();
```

### Syntax（取自子主题 rdi.func().perLabelPassFail()）

```
rdi.func().perLabelPassFail(bool flag);
```

### Example（取自子主题 rdi.func().perLabelPassFail()）

```
rdi.func("id1").burst("burstLabel").perLabelPassFail(true).execute();
ARRAY_I ary = rdi.id("id").getMultiPassFail();

rdi.func("id2").burst("MP_burstLabel").perLabelPassFail(true).execute();
ARRAY_I ary2 = rdi.id("id").getMultiPassFail("port1");
ARRAY_I ary3 = rdi.id("id").getMultiPassFail("port2");
```

### Syntax（取自子主题 rdi.port(TA::MULTI_PORT).func()）

```
rdi.port(TA::MULTI_PORT).func();
```

### Example（取自子主题 rdi.port(TA::MULTI_PORT).func()）

Multi-port burst with
.port(TA::MULTI_PORT)
:

```
RDI_BEGIN();
rdi.port("pt1").dc().pin("dig").vForce(1 V).execute();
rdi.port(TA::MULTI_PORT).func().burst("MPBurst1").execute(); // no port
rdi.port("pt2").digCap().pin("dig2").samples(8).execute();
RDI_END();
```

### Retrieving the result on all pins（取自子主题 rdi.getBurstPassFail()）

```
int rdi.getBurstPassFail();
```

### Retrieving the result on a specific pin or port（取自子主题 rdi.getBurstPassFail()）

```
int getBurstPassFail(string pin);
```
[表] Parameter
列: Parameter | Description
行 1:
  pin
  The pin or port on which you want to retrieve the burst pattern pass/fail
    result.

### Return Value（取自子主题 rdi.getBurstPassFail()）

Returns:

1 if the result is pass.

0 if the result is fail.

### Examples（取自子主题 rdi.getBurstPassFail()）

### Example 1

Retrieving the result as soon as the burst pattern test is
executed

```
{
ON_FIRST_INVOCATION_BEGIN();
RDI_BEGIN();
//burst pattern test setup and execution
...
RDI_END();

FOR_EACH_SITE_BEGIN();
int result = rdi.getBurstPassFail("pinB");
FOR_EACH_SITE_END();

RDI_BEGIN();
//another burst pattern test setup and execution
...
RDI_END();

FOR_EACH_SITE_BEGIN();
int resultALL = rdi.getBurstPassFail();
FOR_EACH_SITE_END();
ON_FIRST_INVOCATION_END();
}
```

### Example 2

Retrieving the result at the end of the test
method

```
{
...
ON_FIRST_INVOCATION_BEGIN();

RDI_BEGIN();
rdi.burstId("bid","A");
//burst pattern setups and execution
...
RDI_END();

RDI_BEGIN();
...
...
RDI_END();

ON_FIRST_INVOCATION_END();

int result = rdi.id("bid").getBurstPassFail("A"); //Retrieve the burst pattern test result from Pin A.
int resultALL = rdi.id("bid").getBurstPassFail(); //Retrieve burst pattern test result from all pins.
}
```

### Syntax（取自子主题 rdi.id().getLabel()）

```
string rdi.id().getLabel()
```

### Example（取自子主题 rdi.id().getLabel()）

```
RDI_BEGIN();
...
rdi.func("id1").label("abcd").execute();
...
RDI_END();

rdi.id("id1").getLabel() // Returns "abcd".
```

### Syntax（取自子主题 rdi.id().getBurstPassFail()）

```
rdi.id(string burstId);
rdi.id(int burstId);
```
[表] List of parameters
列: Parameter | Description
行 1:
  burstId
  The same ID that you have given in a `rdi.func().burstId()`（raw: `148642.htm`）. It supports both
    string and int types.

### Example（取自子主题 rdi.id().getBurstPassFail()）

For its usages, see the Example section in
`rdi.func().burstId()`（raw: `148642.htm`）
.

### Syntax（取自子主题 rdi.id().getMultiPassFail()）

```
ARRAY_I& rdi.id().getMultiPassFail();
ARRAY_I& rdi.id().getMultiPassFail(string sPort=="@");
```

[表] List of parameters
列: Parameter | Description
行 1:
  sPort
  The port name.

### Examples（取自子主题 rdi.id().getMultiPassFail()）

Also see the example in
`rdi.func().burstRunTime()`（raw: `348893.htm`）
.

```
rdi.func("id1").burst("burstPattern").perLabelPassFail(true).execute();
ARRAY_I ary = rdi.id("id1").getMultiPassFail();

rdi.func("id2").burst("MP_burst").perLabelPassFail(true).execute();
ARRAY_I ary2 = rdi.id("id2").getMultiPassFail("port1");
ARRAY_I ary3 = rdi.id("id2").getMultiPassFail("port2");
```

### Syntax（取自子主题 rdi.id().getPassFail()）

```
int rdi.id().getPassFail();
```

List of parameters
There are no parameters.
Return Value
The pass/fail result is returned:

1 is returned for pass and

0 is returned for fail.

### Example（取自子主题 rdi.id().getPassFail()）

```
int result = rdi.id("f1").getPassFail();
```

### Syntax（取自子主题 rdi.id().getMatchCount()）

```
int rdi.id().getMatchCount(string pin)
```

### Example（取自子主题 rdi.id().getMatchCount()）

```
int rdi.id("mch").getMatchCount();
```

### Syntax（取自子主题 rdi.id().getMatchPassFail()）

```
bool rdi.id().getMatchPassFail(string pin)
```

### Example（取自子主题 rdi.id().getMatchPassFail()）

```
rdi.id("mch").getMatchPassFail("pinA");
```

### Syntax（取自子主题 rdi.func().readMatchCount()）

```
rdi.func().readMatchCount(string pin)
```

### Example（取自子主题 rdi.func().readMatchCount()）

```
rdi.func("mch").label("abc").readMatchPassFail("pinA").readMatchCount("pinA").execute();
```

### Syntax（取自子主题 rdi.func().readMatchPassFail()）

```
rdi.func().readMatchPassFail(string pin)
```

### Example（取自子主题 rdi.func().readMatchPassFail()）

```
rdi.func("mch").label("abc").readMatchPassFail("pinA").readMatchCount("pinA").execute();
```

### Example（取自子主题 SmartRDI: Level and timing set changes）

```
RDI_BEGIN();
rdi.level().set(1);
rdi.func().label("aaa").execute();
rdi.timing().set(1);
rdi.func().label("bbb").execute();
RDI_END();
```

### Syntax（取自子主题 set()）

```
set(int setNum);
```
[表] List of parameters
列: Parameter | Description
行 1:
  setNum
  The timing or level set number

### Example（取自子主题 set()）

```
RDI_BEGIN();
...
rdi.level().set(1);
rdi.timing().set(2);
...
RDI_END();
```

### Example（取自子主题 Structures of multiple cogo() nodes）

```
RDI_BEGIN();
rdi.cogo().node("a",TA::ROOT).passNode("b").failNode("c").begin();
rdi.func().label("abc").execute(); // Pass/fail judgment.
rdi.cogo().wait(30 us); // System-reserved waiting time.
rdi.cogo().node().end();

rdi.cogo().node("b").passNode("RETURN").failNode("RETURN").begin();
rdi.dc().pin("VDD").iMeas().limit(0,1 mA).execute(); // Pass/fail judgment.
rdi.cogo().wait(20 us); // System-reserved waiting time.
rdi.cogo().node().end();

rdi.cogo().node("c").passNode("RETURN").failNode("RETURN").begin();
rdi.smartVec().pin("D1").expectData(0x55,8).execute(); // Pass/fail judgment.
rdi.cogo().wait(30 us); // System-reserved waiting time.
rdi.cogo().node().end();
RDI_END();
```

Each
structure needs at least one ROOT node.

### Examples（取自子主题 Sequencer-controlled searching with cogo）

### A binary search in a TRIM test

```
RDI_BEGIN();
rdi.cogo("trim").search(TA::BINARY).pathPin("pinA")
.start(0).stop(0xff).init(0x88).step(4).blockBegin();
rdi.smartVec().pin("SDA").writeData(0x53,8,0)
.writeData(rdi.searchInput(),8,16)
.execute();
rdi.wait(100 us);
rdi.dc().pin("LDO").vMeas().limit(0,5).execute(); // Pass/fail judgment.
rdi.cogo().wait(100 us); // Time long enough for pass/fail judgment.
rdi.cogo().search().blockEnd();
RDI_END();

rdi.id("trim").getSearchResult();
```

### A linear search in a Hysteresis test

```
RDI_BEGIN();
rdi.cogo("cogo_hyst_linear").search(TA::HYST_LINEAR)
.pathPin("DATA3")
.start(0).stop(3).step(5).blockBegin();
rdi.dc().pin("DATA1").vForce(rdi.searchInput()).execute();
rdi.dc().pin("DATA2").iForce(0 mA).vMeas()
.measWait(100 us).limit(1.2,2.2).execute();
rdi.wait(2 ms);
rdi.cogo().search().blockEnd();
RDI_END()；

rdi.id("cogo_hyst_linear").getSearchResult();
```

### Result retrieval with pathPin()

```
RDI_BEGIN();
rdi.cogo("cogo_sVec_linear").search(TA::LINEAR)
.pathPin("DATA11")
.start(0).stop(0xff).step(4).blockBegin();
rdi.smartVec().pin("DATA1").writeData(rdi.searchInput(),8,16)
.pin("DATA2").expectData(0xAA,8,16).execute();
rdi.cogo().wait(1 ms);
rdi.cogo().blockEnd();
RDI_END();

rdi.id("cogo_sVec_linear").getSearchResult();
```

See also
`pathPin()`（raw: `149529.htm`）
.

### Result retrieval without pathPin()

```
RDI_BEGIN();
rdi.cogo("cogo_linear_wo_pathPin").search(TA::LINEAR)
.start(0).stop(0xff).step(4).blockBegin();
rdi.smartVec().pin("DATA1 ").writeData(rdi.searchInput(),8,16)
.pin("DATA2").expectData(0xAA,8,16).execute();
rdi.cogo().wait(1 ms);
rdi.cogo().blockEnd();
RDI_END()

rdi.id("cogo_linear_wo_pathPin").getSearchResult();
```

See also
`pathPin()`（raw: `149529.htm`）
.

### Syntax（取自子主题 postBurst()）

```
postBurst()
```

### Example（取自子主题 postBurst()）

This is a template for the code structure of concurrent test framework in SmartRDI.

```
#include "rdi.hpp"

class UserClassName: public CCTestMethod_SYNC
{
protected:
...
virtual void preStart()
{ // Static commands before burst pattern execution
}
virtual void burstRun()
{ // Pattern-based SmartRDI commands
}
virtual void postBurst() // New in SmartRDI 2.5.1
{ // Static commands after the burst pattern execution
}
virtual void postProcess()
{ // Result retrieval, calculation, and datalog
}
...
};
REGISTER_TESTMETHOD("UserClassName", UserClassName);
```

### Examples（取自子主题 SmartRDI: TMU test setup）

### Creating an independent TMU measurement

```
RDI_BEGIN();

rdi.tmu("1").pin("PVI8_1")
.vth(3.0 V, 5.0 V)
.samples(4)
.measMode(TA::PULSE_HIGH)
.execute();

rdi.wait(1 ms);

RDI_END();
```

The
execute()
 here means the start of the TMU measurement. The TMU
measurement takes place in the next event within this RDI_BEGIN/END() block.

### Inserting a TMU measurement into an existing pattern

```
RDI_BEGIN();

rdi.tmu("id").label("func1").pin("DATA1")
.insertVec(200)
.vth(1.5 V)
.samples(2)
.measMode(TA::RISE_FALL)
.execute();

RDI_END();
```

In this example, a TMU measurement is inserted into a copy of the
func1

pattern.

### Syntax（取自子主题 rdi.tmu().dataRate()）

```
tmuBase& dataRate(double iDataRate);
```
[表] Parameter
列: Parameter | Description
行 1:
  dataRate
  The data rate in bits/second or Hertz (Hz).

Note
 The functions rdi.tmu().dataRate() and
`rdi.tmu().preScaler()`（raw: `149112.htm`）
 cannot
be used together for the same pin in one
rdi ... execute()

block.

### Return Value（取自子主题 rdi.tmu().dataRate()）

A reference to the
tmuBase

object.

### Example（取自子主题 rdi.tmu().dataRate()）

```
RDI_BEGIN();

rdi.tmu().pin("PVI8_PMU_1") // PVI8_TMU
.measMode(TA::RISE_TIME)
.dataRate(25 MHz)
.vth(1.0 V, 2.0 V)
.samples(50)
.execute();

rdi.wait(100 us);

rdi.tmu().pin("PS1600_1") // Digital TMU
.measMode(TA::RISE)
.dataRate(10 MHz)
.vth(1.0 V)
.samples(50)
.execute();

rdi.wait(100 us);

RDI_END();
```

Note
 For supported DC Scale pins, the initDiscard(), interSkip(), preScaler(), and
dataRate() settings must be the same within one
RDI_BEGIN() ... RDI_END()

block.

```
RDI_BEGIN();

rdi.tmu("1").pin("PVI8_PMU_1")
.vth(3.0 V, 5.0 V)
.samples(4)
.measMode(TA::PULSE_HIGH)
.interSkip(2).initDiscard(3).dataRate(25 MHz)
.execute();

rdi.wait(1 ms);

rdi.tmu("2").pin("PVI8_PMU_1")
.vth(1.0 V, 3.0 V)
.samples(8)
.measMode(TA::RISE_TIME)
.interSkip(2).initDiscard(3).dataRate(25 MHz)
.execute();

rdi.wait(2 ms);

RDI_END();
```

Note
 For a digital pin, all the parameters must be the same within one

RDI_BEGIN() ... RDI_END()

block.

```
RDI_BEGIN();

rdi.tmu("1").pin("PS1600_1")
.vth(1.0 V).samples(5).measMode(TA::RISE).execute();

rdi.wait(1 ms);

rdi.tmu("2").pin("PS1600_1")
.vth(1.0 V).samples(5).measMode(TA::RISE).execute();

rdi.wait(2 ms);

RDI_END();
```

### Syntax（取自子主题 rdi.tmu().disable()）

```
tmuBase& disable();
```

Note
 If there is no disable()
in the
RDI_BEGIN() ... RDI_END()
 block, the TMU disable event will still be
put at the end of the created pattern burst.

### Return Value（取自子主题 rdi.tmu().disable()）

A reference to the
tmuBase

object.

### Example（取自子主题 rdi.tmu().disable()）

```
RDI_BEGIN();

rdi.tmu().pin("PVI8_PMU_1")
.vth(3.0 V, 5.0 V).samples(4).measMode(TA::PULSE_HIGH).execute();

rdi.wait(1 ms);

rdi.tmu().pin("PVI8_PMU_1").disable().execute();

rdi.wait(2 ms);

RDI_END();
```

The
code above results in the following sequence in the created pattern burst:

TMU arm

TMU threshold, measurement mode, samples

Wait 1 ms

TMU disable

Wait 2 ms

### Syntax（取自子主题 rdi.tmu().enPassFail()）

```
tmuBase& enPassFail()
```

### Return Value（取自子主题 rdi.tmu().enPassFail()）

A reference to the
tmuBase

object.

### Example（取自子主题 rdi.tmu().enPassFail()）

```
RDI_BEGIN();

rdi.tmu("a").label("label1").pin("A") ... .enPassFail().execute();
rdi.dc("b").label("label2").pin("B") ... .enPassFail().execute();
rdi.digCap("c").label("label3").pin("C") ... .enPassFail().execute();

RDI_END();

int testResult_a = rdi.id("a").getPassFail();
int testResult_b = rdi.id("b").getPassFail();
int testResult_c = rdi.id("c").getPassFail();
```

### Syntax（取自子主题 rdi.tmu().initDiscard()）

```
tmuBase& initDiscard(int iInitDiscard);
```
[表] Parameter
列: Parameter | Description
行 1:
  iInitDiscard
  The number of initial discards.

### Return Value（取自子主题 rdi.tmu().initDiscard()）

A reference to the
tmuBase

object.

### Example（取自子主题 rdi.tmu().initDiscard()）

```
RDI_BEGIN();

rdi.tmu().pin("PVI8_PMU_1") // PVI8_TMU
.measMode(TA::RISE_TIME)
.initDiscard(0)
.vth(1.0 V, 2.0 V)
.samples(50)
.execute();

rdi.wait(100 us);

rdi.tmu().pin("PS1600_1") // Digital TMU
.measMode(TA::RISE)
.initDiscard(3)
.vth(1.0 V)
.samples(50)
.execute();

rdi.wait(100 us);

RDI_END();
```

Note
 For supported DC Scale pins, the preScaler() and dataRate() settings must be the
same within one
RDI_BEGIN()
 ...
RDI_END()
 block. Functions

interSkip()
 and
initDiscard()
 must be omitted or set to
0.

```
RDI_BEGIN();

rdi.tmu("1").pin("PVI8_PMU_1")
.vth(3.0 V, 5.0 V)
.samples(4)
.measMode(TA::PULSE_HIGH)
.preScaler(2).dataRate(25 MHz)
.execute();

rdi.wait(1 ms);

rdi.tmu("2").pin("PVI8_PMU_1")
.vth(1.0 V, 3.0 V)
.samples(8)
.measMode(TA::RISE_TIME)
.preScaler(2).dataRate(25 MHz)
.execute();

rdi.wait(2 ms);

RDI_END();
```

Note
 For a digital pin, all the parameters must be the same within one

RDI_BEGIN() ... RDI_END()

block.

```
RDI_BEGIN();

rdi.tmu("1").pin("PS1600_1").vth(1.0 V).samples(5).measMode(TA::RISE).execute();

rdi.wait(1 ms);

rdi.tmu("2").pin("PS1600_1").vth(1.0 V).samples(5).measMode(TA::RISE).execute();

rdi.wait(2 ms);

RDI_END();
```

### Syntax（取自子主题 rdi.tmu().insertVec()）

```
tmuBase& insertVec(int iVecNum);
```
[表] Parameter
列: Parameter | Description
行 1:
  iVecNum
  The line number of the vector where you want to insert the TMU event.

Note
 The correct sequence of
`rdi.tmu().label()`（raw: `149120.htm`）
 and

.insertVec()
 must be strictly followed within the
rdi ...
execute()
 block if you want to insert TMU events into an already existing
pattern.

### Return Value（取自子主题 rdi.tmu().insertVec()）

A reference to the
tmuBase

object.

### Example（取自子主题 rdi.tmu().insertVec()）

```
RDI_BEGIN();

rdi.tmu("id_1").label("func_1").pin("PVI8_PMU_1")
.insertVec(100).vth(3.0 V, 5.0 V)
.insertVec(500).samples(4).measMode(TA::PULSE_HIGH)
.dataRate(25 MHz)
.execute();

rdi.wait(1 ms);

rdi.tmu("id_2").label("func_2").pin("PS1600_1")
.insertVec(280)
.vth(3.0 V)
.samples(4)
.measMode(TA::RISE)
.dataRate(25 MHz)
.execute();

rdi.wait(1 ms);

RDI_END();

RDI_BEGIN();

rdi.tmu("id").label("func")
.pin("PVI8_PMU_1")
.insertVec(100).vth(3.0 V, 5.0 V)
.insertVec(500).samples(4).measMode(TA::PULSE_HIGH)
.dataRate(25 MHz)
.pin("PS1600")
.insertVec(200)
.vth(1.5 V)
.samples(2)
.measMode(TA::RISE_FALL)
.execute();

rdi.wait(1 ms);

RDI_END();
```

### Syntax（取自子主题 rdi.tmu().interSkip()）

```
tmuBase& interSkip(int iInitSkipSamples);
```
[表] Parameter
列: Parameter | Description
行 1:
  iInitSkipSamples
  The number of event to ignore between samples.

### Return Value（取自子主题 rdi.tmu().interSkip()）

A reference to the
tmuBase

object.

### Example（取自子主题 rdi.tmu().interSkip()）

```
RDI_BEGIN();

rdi.tmu("1").pin("PVI8_PMU_1") // PVI8_TMU
.measMode(TA::RISE_TIME)
.interSkip(0)
.vth(1.0 V, 2.0 V)
.samples(50)
.execute();

rdi.wait(100 us);

rdi.tmu("2").pin("PS1600_1") // Digital TMU
.measMode(TA::RISE)
.interSkip(3)
.vth(1.0 V)
.samples(50)
.execute();

rdi.wait(100 us);

RDI_END();
```

Note
 For supported DC Scale pins, the preScaler() and dataRate() settings must be the
same within one
RDI_BEGIN()
 ...
RDI_END()
 block. Functions

interSkip()
 and
initDiscard()
 must be omitted or set to
0.

```
RDI_BEGIN();

rdi.tmu("1").pin("PVI8_PMU_1")
.vth(3.0 V, 5.0 V)
.samples(4)
.measMode(TA::PULSE_HIGH)
.preScaler(2).dataRate(25 MHz)
.execute();

rdi.wait(1 ms);

rdi.tmu("2").pin("PVI8_PMU_1")
.vth(1.0 V, 3.0 V)
.samples(8)
.measMode(TA::RISE_TIME)
.preScaler(2).dataRate(25 MHz)
.execute();

rdi.wait(2 ms);

RDI_END();
```

Note
 For a digital pin, all the parameters must be the same within one

RDI_BEGIN() ... RDI_END()

block.

```
RDI_BEGIN();

rdi.tmu("1").pin("PS1600_1").vth(1.0 V).samples(5).measMode(TA::RISE).execute();

rdi.wait(1 ms);

rdi.tmu("2").pin("PS1600_1").vth(1.0 V).samples(5).measMode(TA::RISE).execute();

rdi.wait(2 ms);

RDI_END();
```

### Syntax（取自子主题 rdi.tmu().label()）

```
tmuGroup& label(const string &sLabel);
```
[表] Parameter
列: Parameter | Description
行 1:
  sLabel
  The name of the label.

Note
 The correct sequence of
rdi.tmu().label()
 and

.insertVec()
 must be respected within the
rdi ... execute()

block if you want to insert the TMU events into an already existing pattern.

### Return Value（取自子主题 rdi.tmu().label()）

A reference to the
tmuGroup

object.

### Example（取自子主题 rdi.tmu().label()）

```
RDI_BEGIN();

rdi.tmu("id_1").label("func_1").pin("PVI8_PMU_1")
.insertVec(100).vth(3.0 V, 5.0 V)
.insertVec(500).samples(4).measMode(TA::PULSE_HIGH)
.dataRate(25 MHz)
.execute();

rdi.wait(1 ms);

rdi.tmu("id_2").label("func_2").pin("PS1600_1")
.insertVec(280)
.vth(3.0 V)
.samples(4)
.measMode(TA::RISE)
.dataRate(25 MHz)
.execute();

.rdi.wait(1 ms);

RDI_END();
```

### Syntax（取自子主题 rdi.tmu().label().copyLabel()）

```
label("Label").copyLabel(boolVar);
```
[表] List of parameters
列: Parameter | Description
行 1:
  boolVar
  Specifies whether to edit an existing pattern, or create a copy
    from an existing pattern and edit the copied pattern.
[表] List of available options of parameter: bool
列: Option | Description
行 1:
  true
  Make a copy of an existing pattern and edit the copied pattern.
    This is the default
    value.
行 2:
  false
  Edit an existing pattern.

Return value

There is no return value.

### Example（取自子主题 rdi.tmu().label().copyLabel()）

```
RDI_BEGIN();
...
rdi.tmu("id_2").label("func_2").copyLabel(false).pin("PS1600_1")
.insertVec(280)
.vth(3.0 V)
.samples(4)
.measMode(TA::RISE)
.dataRate(25 MHz)
.execute();
...
RDI_END();
```

### Syntax（取自子主题 rdi.tmu().measMode()）

Syntax for digital pins

```
tmuBase& measMode(TA::TMU_EDGE_MODE digital_measMode);
```

Syntax
for DC Scale pins in the PMU operating
mode:

```
tmuBase& measMode(TA::TMU_MEAS_MODE dcScale_measMode);
```
[表] Parameters
列: Parameter | Description
行 1:
  digital_measMode
  Defines the TMU measurement mode for:
    
    Smart Scale digital pins
    
    DC Scale pins in the Digital I/O operating mode
    
    For the available options, refer to table `Available options of parameter: digital_measMode`（raw: `149091.htm#_149091__t_options_digital_measMode`） below.
行 2:
  dcScale_measMode
  Defines the TMU measurement mode for: DC Scale pins in the PMU
    operating mode
[表] Available options of parameter: digital_measMode
列: Option | Description
行 1:
  TA::RISE
  One edge type to trigger the event, the rising Edge.
行 2:
  TA::FALL
  One edge type to trigger the event, the falling Edge.
行 3:
  TA::RISE_FALL
  One edge type to trigger the event, the alternate rising and falling edges. This
    option is used for pulse and jitter measurements.
    In this case, the prescaler must be set
    to a value > 1 and < 17. Moreover, if an event discard is specified, it must be even
    (including 0). For conceptual information about the operation mode of the TMU with this
    option, see example "Pulse width measurement" in `TMU per Pin overview`（raw: `125212.htm`）.
    
    Note The RISE_FALL mode of the digital TMU requires clean and
    sharp edges of the signal. Otherwise more than one sample might be recorded from one
    edge.

### Return Value（取自子主题 rdi.tmu().measMode()）

A reference to the
tmuBase

object.

### Example（取自子主题 rdi.tmu().measMode()）

```
RDI_BEGIN();

rdi.tmu().pin("PS1600_1")
.vth(1.0 V).samples(5).measMode(TA::RISE).execute();

rdi.tmu().pin("PVI8_PMU_1")
.measMode(TA::RISE_TIME)
.connectMode(TA::HIGH_BW)
.vth(1.0 V,2.0 V).samples(50).execute();

rdi.wait(100 us);

RDI_END();
```

### Syntax（取自子主题 rdi.tmu().measNum()）

```
measNum(int sNumber);
```
[表] List of parameters
列: Parameter | Description
行 1:
  sNumber
  The number of existing arming actions in the label.

### Example（取自子主题 rdi.tmu().measNum()）

```
RDI_BEGIN();

...rdi.tmu("tmu_test").label("abc").pin("DATA1").vth(1.0 v)

.sample(4).measMode(TA::RISE).measNum(5).execute(); // Do not have to use insertVec().

rdi.wait(1 ms);

RDI_END();

ARRAY_D result = rdi.id("id").getStamp(); // The size of the returned ARRAY_D is 20 which is from measNum(5) and sample(4).
```

### Syntax（取自子主题 rdi.tmu().pin()）

```
tmuBase& pin(const string& sPin);
```
[表] Parameter
列: Parameter | Description
行 1:
  sPin
  The pin on which the following setups will be done. Its value can
    be a pin, a pin group, a port name as a pin group, the pins or pin
    groups separated with comma, or all pins.

### Return Value（取自子主题 rdi.tmu().pin()）

A reference to the
tmuBase

object.

### Example（取自子主题 rdi.tmu().pin()）

```
RDI_BEGIN();

rdi.tmu().pin("PVI8_PMU_1")
.measMode(TA::RISE_TIME)
.connectMode(TA::HIGH_BW)
.vth(1.0 V,2.0 V).samples(50)
.execute();

rdi.tmu().pin("PS1600_1")
.vth(1.0 V).samples(5).measMode(TA::RISE)
.execute();

rdi.wait(100 us);

RDI_END();
```

### Syntax（取自子主题 rdi.tmu().preScaler()）

```
tmuBase& preScaler(int iPreScaler);
```
[表] Parameter
列: Parameter | Description
行 1:
  iPreScaler
  The prescaler value.

Note
 The functions
`rdi.tmu().dataRate()`（raw: `149111.htm`）
 and
rdi.tmu().preScaler() cannot be used together for the same pin in one
rdi
... execute()
 block.

### Return Value（取自子主题 rdi.tmu().preScaler()）

A reference to the
tmuBase

object.

### Example（取自子主题 rdi.tmu().preScaler()）

```
RDI_BEGIN();

rdi.tmu().pin("PVI8_PMU_1")
.measMode(TA::RISE_TIME)
.preScaler(2)
.vth(1.0 V,2.0 V)
.samples(50)
.execute();

rdi.wait(100 us);

RDI_END();
```

Note
 For supported DC Scale pins, the initDiscard(), interSkip(),
preScaler(), and dataRate() settings must be the same within one

RDI_BEGIN() ... RDI_END()

block.

```
RDI_BEGIN();

rdi.tmu("1").pin("PVI8_PMU_1")
.vth(3.0 V, 5.0 V)
.samples(4)
.measMode(TA::PULSE_HIGH)
.preScaler(2).interSkip(2).initDiscard(3).dataRate(25 MHz)
.execute();

rdi.wait(1 ms);

rdi.tmu("2").pin("PVI8_PMU_1")
.vth(1.0 V,3.0 V)
.samples(8)
.measMode(TA::RISE_TIME)
.preScaler(2).interSkip(2).initDiscard(3).dataRate(25 MHz)
.execute();

rdi.wait(2 ms);

RDI_END();
```

Note
 For a digital pin, all the parameters must be the same within one

RDI_BEGIN() ... RDI_END()

block.

```
RDI_BEGIN();

rdi.tmu("1").pin("PS1600_1")
.vth(1.0 V).samples(5).measMode(TA::RISE).execute();

rdi.wait(1 ms);

rdi.tmu("2").pin("PS1600_1")
.vth(1.0 V).samples(5).measMode(TA::RISE).execute();

rdi.wait(2 ms);

RDI_END();
```

### Syntax（取自子主题 rdi.tmu().samples()）

```
tmuBase& samples(int iSamples);
```
[表] Parameter
列: Parameter | Description
行 1:
  iSamples
  The number of samples.

### Return Value（取自子主题 rdi.tmu().samples()）

A reference to the
tmuBase

object.

### Example（取自子主题 rdi.tmu().samples()）

```
RDI_BEGIN();

rdi.tmu().pin("PVI8_PMU_1")
.measMode(TA::RISE_TIME)
.vth(1.0 V,2.0 V)
.samples(50)
.execute();

rdi.wait(100 us);

rdi.tmu().pin("PS1600_1")
.measMode(TA::RISE)
.vth(1.0 V)
.samples(50)
.execute();

rdi.wait(100 us);

RDI_END();
```

### Syntax（取自子主题 rdi.id().getArm()）

```
double getArm(const string &sPin);
```
[表] Parameter
列: Parameter | Description
行 1:
  sPin
  The pin that returns the arm time.

### Return Value（取自子主题 rdi.id().getArm()）

Double value that represents the time from the
beginning of the used pattern to the position where the arming of the TMU is
done.

### Example（取自子主题 rdi.id().getArm()）

```
ON_FIRST_INVOCATION_BEGIN();

RDI_BEGIN();

rdi.tmu("result_1").pin("PVI8_PMU_1")
.measMode(TA::RISE_TIME).vth(1.0 V, 2.0 V).samples(50).execute();

rdi.wait(100 us);

rdi.tmu("result_2").pin("PS1600_1")
.measMode(TA::RISE).vth(1.0 V).samples(50).execute();

rdi.wait(100 us);

RDI_END();

ON_FIRST_INVOCATION_END();

double value_1 = rdi.id("result_1").getArm("PVI8_PMU_1");
double value_2 = rdi.id("result_2").getArm("PS1600_1");
```

### Syntax（取自子主题 rdi.id().getInterSkip()）

```
int getInterSkip(const string &sPin);
```
[表] Parameter
列: Parameter | Description
行 1:
  sPin
  The pin that returns the "interSkip" value.

### Return Value（取自子主题 rdi.id().getInterSkip()）

Integer value of "interSkip" parameter.

### Example（取自子主题 rdi.id().getInterSkip()）

```
ON_FIRST_INVOCATION_BEGIN();

RDI_BEGIN();

rdi.tmu("result_1").pin("PVI8_PMU_1")
.measMode(TA::RISE_TIME).interSkip(3)
.vth(1.0 V,2.0 V).samples(50).execute();

rdi.wait(100 us);

rdi.tmu("result_2").pin("PS1600_1")
.measMode(TA::RISE).interSkip(3).vth(1.0 V).samples(50).execute();

rdi.wait(100 us);

RDI_END();

ON_FIRST_INVOCATION_END();

int value_7 = rdi.id("result_1").getInterSkip("PVI8_PMU_1");
int value_8 = rdi.id("result_2").getInterSkip("PS1600_1");
```

### Syntax（取自子主题 rdi.id().getMultiArm()）

```
ARRAY_D getMultiArm(const string &sPin);
```
[表] List of parameters
列: Parameter | Description
行 1:
  sPin
  The pin to get the multiple arm time from.

### Example（取自子主题 rdi.id().getMultiArm()）

```
ON_FIRST_INVOCATION_BEGIN();

RDI_BEGIN();

rdi.tmu("result_2").label("tmu_label").pin("PS1600_1")
.measMode(TA::RISE).vth(1.0 V)
.insertVec(10).samples(50)
.insertVec(20).samples(50).execute();

rdi.wait(100 us);

RDI_END();

ON_FIRST_INVOCATION_END();

ARRAY_D value_4 = rdi.id("result_2").getMultiArm("PS1600_1");
```

### Syntax（取自子主题 rdi.id().getPreScaler()）

```
int getPreScaler(const string &sPin);
```
[表] Parameter
列: Parameter | Description
行 1:
  sPin
  The pin to get the preScaler value.

### Return Value（取自子主题 rdi.id().getPreScaler()）

Integer value of the prescaler.

### Example（取自子主题 rdi.id().getPreScaler()）

```
ON_FIRST_INVOCATION_BEGIN();

RDI_BEGIN();

rdi.tmu("result").pin("PVI8_PMU_1")
measMode(TA::RISE_TIME).preScaler(2).vth(1.0 V,2.0 V).samples(50).execute();

rdi.wait(100 us);

rdi.tmu("result_2").pin("PS1600_1")
.measMode(TA::RISE).preScaler(2).vth(1.0 V).samples(50).execute();

rdi.wait(100 us);

RDI_END();

ON_FIRST_INVOCATION_END();

int value_5 = rdi.id("result_1").getPreScaler("PVI8_PMU_1");
int value_6 = rdi.id("result_2").getPreScaler("PS1600_1");
```

### Syntax（取自子主题 rdi.id().getPassFail()）

```
int rdi.id().getPassFail();
```

List of parameters
There are no parameters.
Return Value
The pass/fail result is returned:

1 is returned for pass and

0 is returned for fail.

### Example（取自子主题 rdi.id().getPassFail()）

```
int result = rdi.id("f1").getPassFail();
```

### Syntax（取自子主题 rdi.id().getPropDelay()）

```
rdi.id("id").getPropDelay(sPin1,sPin2); // For one ID.
```

```
rdi.id("id1","id2").getPropDelay(sPin1,sPin2); // For different IDs.
```

Note
rdi.id("id1","id2")...
 can be used only for

getPropDelay()
.

### Examples（取自子主题 rdi.id().getPropDelay()）

### One ID

```
RDI_BEGIN();
rdi.tmu("id1").pin("DATA1")....;
.pin("DATA2")....;
...
RDI_END();

double propDelay = rdi.id("id1").getPropDelay("DATA1","DATA2");
```

### Different IDs

```
RDI_BEGIN();
rdi.tmu("id1").pin("DATA1")....;
rdi.tmu("id2").pin("DATA2")....;
...
RDI_END();

double propDelay = rdi.id("id1","id2").getPropDelay("DATA1","DATA2");
```

### Syntax（取自子主题 rdi.id().getStamp()）

```
ARRAY_D getStamp(const string &sPin);
```
[表] List of parameters
列: Parameter | Description
行 1:
  sPin
  The pin that returns the stamp value.

### Example（取自子主题 rdi.id().getStamp()）

```
ON_FIRST_INVOCATION_BEGIN();

RDI_BEGIN();

rdi.tmu("result_1").pin("PVI8_PMU_1")
.measMode(TA::RISE_TIME).vth(1.0 V, 2.0 V).samples(50).execute();

rdi.wait(100 us);

rdi.tmu("result_2").pin("PS1600_1")
.measMode(TA::RISE).vth(1.0 V).samples(50).execute();

rdi.wait(100 us);

RDI_END();

ON_FIRST_INVOCATION_END();

ARRAY_D value_9 = rdi.id("result_1").getStamp("PVI8_PMU_1");
ARRAY_D value_10 = rdi.id("result_2").getStamp("PS1600_1");
```

### Syntax（取自子主题 rdi.id().getTmuErrorState()）

```
int getTmuErrorState(string pin);
```

getTmuErrorState()
 retrieves the TMU error state per pin in a burst. For
multiple TMU measurements in the burst, it retrieves all the TMU states for the pin.

See
`TMU_RESULTS.getPinErrorState()`（raw: `145798.htm`）
 for the content and meaning of error states.

### Examples（取自子主题 rdi.id().getTmuErrorState()）

### Example 1

```
RDI_BEGIN();
rdi.tmu("id1").pin("dig1").vth(2).samples(5).measMode(TA::RISE).execute(); // 1
rdi.tmu().pin("dig1").vth(2).samples(10).measMode(TA::RISE).execute(); // 2
...
RDI_END();
int errorState = rdi.id("id1").getTmuErrorState("dig1"); // get the result from 1 and 2.
```

### Example 2

Hidden upload
support

```
rdi.hiddenUpload(TA::ALL);
RDI_BEGIN();
rdi.tmu("id1").pin("dig1").vth(2).samples(5).measMode(TA::RISE).execute();
...
RDI_END();

void SMC_backgroundProcessing()
{
int errorState = rdi.id("id1").getTmuErrorState("dig1");
int errorState1 = rdi.site(2).id("id1").getTmuErrorState("dig1"); // result for site 2
}
```

### Syntax（取自子主题 rdi.id().getTmuFinished()）

```
bool getTmuFinished();
```
Return value

TRUE
: Measurements on all sites have been done.

FALSE
: Measurements on a site is SmarTest Work Center.

### Example（取自子主题 rdi.id().getTmuFinished()）

```
RDI_BEGIN();
rdi.tmu("id1").pin("dig1").vth(2).samples(5).measMode(TA::RISE).execute();
...
RDI_END();

bool flag = rdi.id("id1").getTmuFinished();
```

### SQTO（取自子主题 SQTO, SQTO? - (SeQuencer TimeOut)）

```
SQTO {timeout} // in seconds
```

### SQTO?（取自子主题 SQTO, SQTO? - (SeQuencer TimeOut)）

```
SQTO?
```

returns:

```
SQTO {timeout}
```

### Parameters（取自子主题 SQTO, SQTO? - (SeQuencer TimeOut)）

[表]
行 1:
  timeout
  Defines the time (in seconds) that the sequencer runs. The default value is 900 and
    the range is 0.001 to 2147483.

### Example（取自子主题 SQTO, SQTO? - (SeQuencer TimeOut)）

```
SQTO 3000
```

This example programs the sequencer to exit after 50
minutes.

### Syntax（取自子主题 getLabelCycleNum()）

```
int getLabelCycleNum(string Label);
```
[表] List of parameters
列: Parameter | Description
行 1:
  Label
  A single label's name.

Return value

There is no return value.

Note
 This command is not thread-safe. DO NOT put it into the
`SMC_backgroundProcessing()`（raw: `120107.htm#_120107__s_SMC_backgroundProcessing`）
 function.

### Example（取自子主题 getLabelCycleNum()）

```
int iCycle=rdi.getLabelCycleNum("Label");
```

### Syntax（取自子主题 dtos()）

```
string rdi.dtos(double)
```

### Example（取自子主题 dtos()）

```
double d =100.001;
string str=rdi.dtos(d); // str = "100.001"
```

### Syntax（取自子主题 itos()）

```
string rdi.itos(integerVal);
```

### Example（取自子主题 itos()）

```
long long l = 100;
string str = rdi.itos(l); // str = "100"
```

### Syntax（取自子主题 itos_hex()）

```
string rdi.itos_hex(integerVal);
```

### Syntax（取自子主题 reverseBits()）

```
long long rdi.reverseBits(long long data, int bitLen);
```
[表] List of parameters
列: Parameter | Description
行 1:
  bitLen
  Bit length.

### Syntax（取自子主题 getCommentCycleNum()）

```
int& rdi.getCommentCycleNum(string labelName,string comment);
```

[表] Parameters
列: Parameter | Description
行 1:
  labelName
  The name of the pattern in which you want to retrieve a comment's cycle number. A string.
行 2:
  comment
  The string of the comment for which you want to retrieve its cycle number in the pattern
    specified with labelName.

### Return Value（取自子主题 getCommentCycleNum()）

This function returns a cycle number in integer.

Note
 This command is not thread-safe. DO NOT put it into the
SMC_BackgroundProcessing() function.

### Example（取自子主题 getCommentCycleNum()）

```
// Return the cycle number of the comment string "trigger" in label "modeSet".
int trigCyc=rdi.getCommentCycleNum("modeSet","trigger");

// If necessary, use waitCyc() to align the action with the position of a comment in a pattern.
RDI_BEGIN();
rdi.port("A").func().label("modeSet").execute();
rdi.port("B").waitCycle(trigCyc);
rdi.port("B").dc().pin(VI).samples(1000).FS(50 KHz).execute();
RDI_END();
```

### Syntax（取自子主题 getCommentVectorNum()）

```
int& rdi.getCommentVectorNum(string labelName,string comment);
```
[表] Parameters
列: Parameter | Description
行 1:
  labelName
  The name of the pattern in which you want to retrieve a comment's vector number. A string.
行 2:
  comment
  The string of the comment for which you want to retrieve its vector number in the pattern
    specified with labelName.

### Return Value（取自子主题 getCommentVectorNum()）

This function returns a vector number in integer.

Note
 This command is not thread-safe. DO NOT put it into the
SMC_BackgroundProcessing() function.

### Example（取自子主题 getCommentVectorNum()）

```
// Return the vector number of the comment string "trigger" in label "modeSet".
int trigCyc=rdi.getCommentVectorNum("modeSet","trigger");

// If necessary, use waitCyc() to align the action with the position of a comment in a pattern.
RDI_BEGIN();
rdi.port("A").func().label("modeSet").execute();
rdi.port("B").waitCycle(trigCyc);
rdi.port("B").dc().pin(VI).samples(1000).FS(50 KHz).execute();
RDI_END();
```

### Syntax（取自子主题 setGlobalVar()）

```
void rdi.setGlobalVar(variable_name, value)
```
[表] List of parameters
列: Parameter | Description
行 1:
  variable_name
  The name of the variable to which you want to assign the value. A string.
行 2:
  value
  The value to assign to the variable. The value must have one of these data
    types:
    
    int
    
    double
    
    ARRAY_I
    
    ARRAY_D
    
    vector<ARRAY_I>
    
    vector<ARRAY_D>

### Example（取自子主题 setGlobalVar()）

This example assigns the value of a program variable (myVar) to the SmartRDI variable
abc.

```
int myVar = 100;
rdi.setGlobalVar("abc",myVar);
```

### Syntax（取自子主题 getGlobalVar()）

```
bool rdi.getGlobalVar(variable_name,value);
```
[表] Parameters
列: Parameter | Description
行 1:
  variable_name
  The name of the variable to which you want to assign the value. A string.
行 2:
  value
  The value to assign to the variable. The value must have one of these data
    types:
    
    int
    
    double
    
    ARRAY_I
    
    ARRAY_D
    
    vector<ARRAY_I>
    
    vector<ARRAY_D>

### Return Value（取自子主题 getGlobalVar()）

This function returns
true
 if the
specified SmartRDI variable exists. Otherwise, it returns
false
.

### Example（取自子主题 getGlobalVar()）

```
if (rdi.getGlobalVar("abc",b)) cout<<b<<end;
```

### Syntax（取自子主题 pin()）

```
pin(const string& sPin);
```
[表] List of parameters
列: Parameter | Description
行 1:
  sPin
  One or more utility pin names.
    
    For more pine names, separate them with comma.

### Example（取自子主题 pin()）

```
rdi.util().pin("upin_A").setOn().pin("upin_B").setOff().execute();
```

### Syntax（取自子主题 setOff()）

```
setOff();
```

### Example（取自子主题 setOff()）

```
rdi.util().pin("upin_B").setOff().execute();
```

### Syntax（取自子主题 setOn()）

```
setOn();
```

### Example（取自子主题 setOn()）

```
rdi.util().pin("upin_A").setOn().execute();
```

### Examples（取自子主题 Sequencer Controlled Utility Mask with SmartRDI）

### Utility Mask with Unganged Configuration

Below is an example of
sequencer‑controlled utility mask in an unganged configuration.

### Utility Mask with Ganged (1-8) Configuration

Below is an example of
sequencer‑controlled utility mask in an ganged configuration.

### Syntax（取自子主题 bitLength()）

```
bitLength(int length);
```
[表] List of parameters
列: Parameter | Description
行 1:
  length
  The length of the bit stream.

Note
 If the pattern contents exceed the length defined by the

bitLength()
 parameter, the length of the generated pattern refers to the
actual contents' length.

### Example（取自子主题 bitLength()）

```
RDI_BEGIN();
rdi.smartVec().pin("DATA1").defaultBit(0).bitLength(10).execute();
RDI_END();
```

### Syntax（取自子主题 burstLabel()）

```
burstLabel(const string &labelName);
burstLabel(const string &labelName,TA::MD5_OPTION);
```
[表] List of parameters
列: Parameter | Description
行 1:
  labelName
  The specified name of the big label.
    
    The label name can be as long as 128 characters at maximum.
行 2:
  TA::MD5_OPTION
  The option which defines to use an MD5 postfix string or not in the label name.
[表] List of available options of parameter: <TA::MD5_OPTION>
列: Option | Description
行 1:
  TA::MD5_ON
  With an MD5 postfix string in the label name. This is the default value.
    
    With MD5_ON, the maximum length of a valid "targetLabelName" in the generated pattern
    name is 74.
行 2:
  TA::MD5_OFF
  Withou an MD5 postfix string in the label name.
    
    With MD5_OFF, the maximum length of a valid "targetLabelName" in the
    generated pattern name is 111.

### Examples（取自子主题 burstLabel()）

### Example 1
```
...
RDI_BEGIN();
rdi.smartVec().burstLabel("burstlabel").begin();
rdi.smartVec().pin("DATA1").writeVec("01",2).execute();
rdi.smartVec().pin("DATA3").fillBit(1,8,4).execute();
rdi.smartVec().pin("DATA7").writeData(0x54,8,4).execute();
rdi.smartVec().burstLabel().end();
RDI_END();

// Allow repeat() and wait() in burstLabel() in SmartRDI 2.3.1
RDI_BEGIN();
rdi.smartVec().burstLabel("burstlabel").begin();
rdi.smartVec().pin("DATA1").writeVec("01",2).repeat(2).execute();
rdi.wait(1 ms);
rdi.smartVec().pin("DATA3").fillBit(1,8,4).repeat(3).execute();
rdi.wait(1 ms);
rdi.smartVec().pin("DATA7").writeData(0x54,8,4).repeat(4).execute();
rdi.smartVec().burstLabel().end();
RDI_END();

// Allow to get the Pass-Fail result with burstLabel() in SmartRDI 2.3.1
RDI_BEGIN();
rdi.smartVec("pf_result").burstLabel("burstlabel").enPassFail().begin();
rdi.wait(1 ms);
rdi.smartVec().pin("DATA3"). writeData(0x54,8,4)
.pin("DATA4"). expectData(0x54,8,4)
.repeat(3).execute();
rdi.wait(1 ms);
rdi.smartVec().pin("DATA5"). writeData(0x55,8,24)
.pin("DATA6"). expectData(0x55,8,24)
.repeat(3).execute();
rdi.smartVec().burstLabel().end();
RDI_END();
...
int passfail_result=rdi.id("pf_result").getPassFail();
```

Note
 The resulting "big pattern" is automatically reusable. If the content is changed,
the postfix of the pattern name will be changed and a new pattern will be created. If the
content is not changed, SmartRDI will reuse the existing pattern. An
md5

postfix string will be added to the created label.

### Example 2
```
burstLabel("abc") // The default is with an MD5 postfix
burstLabel("abc",TA::MD5_ON) // With an MD5 postfix
burstLabel("abc",TA::MD5_OFF) // Without an MD5 postfix
```

Note
 In case that the MD5 postfix option is OFF, make sure that if the content is
different, the label name must be different.

### Example 3
```
RDI_BEGIN();
...
rdi.smartVec("pf").burstLabel("abc").enPassFail().begin();
rdi.smartVec()...
...
rdi.smartVec().burstLabel().end();
...
RDI_END();

Rdi.id("pf").getPassFail();
```

### Example 4

Since SmartRDI 2.4.4, the combination of run-time accesses for
the VTT mode within a
burstLabel().begin()
/
burstLabel().end()

block is
supported.

```
rdi.smartVec().vecEditMode(TA::VTT);
rdi.runTimeVal("rtData",rtData);

RDI_BEGIN();
rdi.smartVec().burstLabel("abc").begin();
for(int k=0;k<64;k++) // 64 vector segments to edit in run time
{
rdi.smartVec().pin("DATA1").writeData("rtData",16,0).vecLength(160).execute();
}
rdi.smartVec().burstLabel().end();
RDI_END();
```

There
should be no instructions like
MACT
,
RPTV
,

JSUB
 inside the burst label.

### Example 5

Before SmartRDI 2.4.5, the

rdi.smartVec().burstLabel().begin()/rdi.smartVec().burstLabel().end()
 block
can only be used for a single port.

SmartRDI 2.4.5 supports the combination of multiple
parallel
execute()
 commands for specified ports by

rdi.port().smartVec().burstLabel()
. It also supports the combined usage with

portSync()
. See example below.

### Syntax（取自子主题 burstUpload()）

```
burstUpload();
```

### Example（取自子主题 burstUpload()）

```
// you can get a combined result of all readBit()/readData() inside burstUpload.begin()/end() from only one id.
ON_FIRST_INVOCATION_BEGIN();

rdi.smartVec().readMode(TA::EMAP); // TA::DIGCAP

RDI_BEGIN();
rdi.smartVec("id").burstUpload().begin();
rdi.smartVec(id1).pin("DATA2").readBit(2,2).execute();
rdi.smartVec(id2).pin("DATA2").readBit(4,4).execute();
rdi.smartVec(id3).pin("DATA4").readData(8,8).execute();
rdi.smartVec(id4).pin("DATA4").readData(8,12).execute();
rdi.smartVec().burstUpload().end();
RDI_END();

ON_FIRST_INVOCATION_END();

ARRAY_I bitResult=rdi.id("id").getReadBit("DATA2");
ARRAY_LL dataResult=rdi.id("id").getReadData("DATA4");
```

### Syntax（取自子主题 comment()）

```
comment(const string &comment, int vecNum);
```

[表] List of parameters
列: Parameter | Description
行 1:
  comment
  The content to be added.
行 2:
  vecNum
  The position of the vector.

See
`SMV_IGNORE_COMMENT`（raw: `146692.htm#_146692__row_SMV_IGNORE_COMMENT`）
, which can be used
in the
`RDI_Configure file`（raw: `146692.htm`）
 to globally disable comment output in
pattern generation.

### Examples（取自子主题 comment()）

```
RDI_BEGIN();
rdi.smartVec().pin("DATA1").writeData(0x54,8).comment("MSB",0).comment("LSB",8).execute();
RDI_END();
```

Note
 Adding comments significantly increases the time for pattern generation
(first-run). To reduce the first-run time, you can remove the comment commands from your code
after the pattern generation and debugging have been finished.

### Syntax（取自子主题 copyLabel()）

```
label("Label").copyLabel(boolVar);
```
[表] List of parameters
列: Parameter | Description
行 1:
  boolVar
  Specifies whether to edit an existing pattern, or create a copy
    from an existing pattern and edit the copied pattern.
[表] List of available options of parameter: bool
列: Option | Description
行 1:
  true
  Make a copy of an existing pattern and edit the copied pattern.
    This is the default
    value.
行 2:
  false
  Edit an existing pattern.

Return value

There is no return value.

### Example（取自子主题 copyLabel()）

```
RDI_BEGIN();
...
rdi.smartVec().label("label4").copyLabel(false).pin("D3").writeData(0x55,8,0).execute();
...
RDI_END();
```

### Syntax（取自子主题 defaultBit()）

```
defaultBit(int bit);
defaultBit(string bit);
```
[表] List of parameters
列: Parameter | Description
行 1:
  bit
  The bit or string you want to write into the pattern.

### Example（取自子主题 defaultBit()）

```
RDI_BEGIN();
rdi.smartVec().pin("DATA1").bitLength(20).defaultBit(0).execute();
RDI_END();
```

Supporting
a
string

```
RDI_BEGIN();
rdi.smartVec().pin("DATA1").bitLength(20).defaultBit("L").execute();
RDI_END();
```

### Syntax（取自子主题 defaultVec()）

```
defaultVec(int index);
defaultVec(string dvc);
```
[表] List of parameters
列: Parameter | Description
行 1:
  index
  The physical index you want to write to the pattern .
行 2:
  dvc
  The device cycle you want to write to the pattern.

### Example（取自子主题 defaultVec()）

```
RDI_BEGIN();
rdi.smartVec().pin("DATA1").defaultVec(0).vecLength(10).execute(); // index
rdi.smartVec().pin("DATA3").defaultVec("1").vecLength(10).execute(); // device cycle
RDI_END();
```

### Syntax（取自子主题 download()）

```
download();
```

A statement example that
download()
 works together with

write...()
 and
expect...()

commands:

```
rdi.smartVec().pin(pName).write...("rtData",...).download();
```

```
rdi.smartVec().pin(pName).expect...("rtData",...).download();
```

### Examples（取自子主题 download()）

### download() code structure

```
ARRAY_LL rtData = ...
rdi.runTimeVal("rtD", rtData);

//Download value into the existing pattern label "abc"
rdi.smartVec().label("abc").copyLabel(false).pin("D1").writeData("rtD",8).download();

//Create a new label "cde" based on code and download runtime data in it.
rdi.smartVec().pin("D2").defaultBit(1).writeData("rtD",8,10).labelName("cde").download();
```

### Hidden vector download

```
ARRAY_LL rtData= ...
rdi.runTimeVal("rtData", rtData);

RDI_BEGIN();
...
RDI_END(TA::NON_BLOCKING);

rdi.smartVec().pin(pinA).writeData("rtData",8).labelName("abc").download();
...
RDI_WAIT_TEST_DONE();
```

### Using copyLabel(false) and download() together

```
RDI_BEGIN();
rdi.func("id1").label("label1").execute(); // measurement
rdi.digCap().pin(A).samples(5).execute(); // measurement
RDI_END(TA::NON_BLOCKING);

rdi.smartVec().label("abc").copyLabel(false).pin("pinA").writeData("rtD",8).download();
// HVD to the existing pattern "abc" without creating a new pattern.

RDI_WAIT_TEST_DONE();
```

### NON_BLOCKING starts at the second run

```
RDI_BEGIN()
rdi.dc().pin("dig").vForce(1).iMeas().execute();
RDI_END(TA::NON_BLOCKING)

rdi.smartVec() label("abc").copyLabel(false).pin("pinA").writeData("rtD",8).download();

RDI_WAIT_TEST_DONE();
```

### Syntax（取自子主题 emapLocation()）

```
emapLocation(TA::EMAP_LOCATION loc);
```
[表] List of parameters
列: Parameter | Description
行 1:
  TA::EMAP_LOCATION loc
  The location where error maps are stored.
[表] List of available options of parameter: <TA::EMAP_LOCATION loc>
列: Option | Description
行 1:
  TA::TP
  The location is the test processor on the card. The default value.
行 2:
  TA::RAM
  The location is the unused vector memory on the tester.

### Example（取自子主题 emapLocation()）

```
rdi.emapLocation(TA::RAM);
rdi.smartVec().readMode(TA::EMAP)

RDI_BEGIN();
rdi.smartVec().pin("A").readBit(10000).execute();
RDI_END();
```

### Syntax（取自子主题 enPassFail()）

```
enPassFail(bool val = true)
```

### Example（取自子主题 enPassFail()）

```
RDI_BEGIN();
rdi.smartVec("a").label("label1").pin("A")....enPassFail(true).execute();
rdi.smartVec("b").label("label2").pin("B")....enPassFail().execute();
RDI_END();

rdi.id("a").getPassFail();
rdi.id("b").getPassFail();
```

### Syntax（取自子主题 expectBit()）

```
expectBit(ARRAY_I bitStream,int startBit=0);
expectBit(string rtv, int startBit=0); // For runtime setup
```

Relationship of bit to
DVC:

X1 mode: bit 0 to DVC "L", 1 to "H", and 2 to "X".

Xn mode: 0101 to "LHLH" and 0112 to "LHHX".

 SmartRDI always deals with 0, 1, and 2 for DVC "L", "H", and "X".
[表] List of parameters
列: Parameter | Description
行 1:
  bitStream
  The expected bit stream you need to get from the captured pin.
行 2:
  startBit
  The starting position of the bits to be compared. If the startBit
    parameter is not specified, the default value is 0.
行 3:
  rtv
  The value to be used at runtime.

### Example（取自子主题 expectBit()）

```
ARRAY_I bitStream(4);
bitStream[0]=1;
bitStream[1]=0;
bitStream[2]=1;
bitStream[3]=1;

ON_FIRST_INVOCATION_BEGIN();

RDI_BEGIN();
rdi.smartVec(1).pin("DATA7").expectBit(bitStream,2).execute();
RDI_END();

ON_FIRST_INVOCATION_END();

int pf_result=rdi.id(1).getPassFail();
```

### Syntax（取自子主题 expectData()）

```
expectData(long long data, int bitLength, int startBit=0);
expectData(string rtv, int bitLength, int startBit=0);
```
[表] List of parameters
列: Parameter | Description
行 1:
  data
  The expected data you want to get from the captured pin.
行 2:
  bitLength
  The length of the bits (data will be automatically converted into bits) to be
    written.
行 3:
  startBit
  The starting position of the bits to be compared. If the
    startBit parameter missing, the default value is 0.
行 4:
  rtv
  The value to be used at runtime.

### Examples（取自子主题 expectData()）

### Example 1
```
RDI_BEGIN();
rdi.smartVec().pin("DATA3").expectData(0x54,8,2).execute();
RDI_END();
```

### Example 2

This example demonstrates how to use

expectData()
 at
runtime.

```
ARRAY_I outputSite = ...
rdi.runTimeVal("rtValue", outputSite);
RDI_BEGIN();
...
rdi.smartVec("a").pin("pinA").expectData("rtValue",8).execute();
...
RDI_END();

int result = rdi.id("a").getPassFail();
```

### Syntax（取自子主题 failCount()）

```
failCount(int startCyc,int cycRange);
failCount(int startCyc);
failCount();
```
[表] List of parameters
列: Parameter | Description
行 1:
  startCyc
  Start cycle.
行 2:
  cycRange
  Cycle range.

Return value

There is no return value.

Note

The fail count and fail position are about "compare edge" (not tester cycle). So they
supports xMode directly.

The xMode parameter for a pin must be correct, otherwise the result for the pin will not
be correct.

The parameter specified in the function, such as
startCyc
 and

cycRange
, is about user cycles (edge), not tester cycles. This setting is
critical when xMode is set to be greater than 1.

For one pin, xMode must remain the same in different labels in burst; otherwise the
results might be wrong.

### Syntax（取自子主题 failCyc()）

```
failCyc(int startCyc,int cycRange);
failCyc(int startCyc);
failCyc();
```
[表] List of parameters
列: Parameter | Description
行 1:
  startCyc
  Start cycle.
行 2:
  cycRange
  Cycle range.

Return value

There is no return value.

Note

The fail count and fail position are about "compare edge" (not tester cycle). So they
supports xMode directly.

The xMode parameter for a pin must be correct, otherwise the result for the pin will not
be correct.

The parameter specified in the function, such as
startCyc
 and

cycRange
, is about user cycles (edge), not tester cycles. This setting is
critical when xMode is set to be greater than 1.

For one pin, xMode must remain the same in different labels in burst; otherwise the
results might be wrong.

### Syntax（取自子主题 failNode()）

```
failNode();
```

List of parameters

There are no parameters.

Return value

There is no return value.

### Example（取自子主题 failNode()）

```
RDI_BEGIN();
...
rdi.smartVec...
.insertJmpe(2).failNode().pin("DATA1").writeData(0xf,8,0)...execute();
...
RDI_END();
```

### Syntax（取自子主题 FFC()）

```
FFC(int startCyc);
FFC();
```
[表] List of parameters
列: Parameter | Description
行 1:
  startCyc
  The number of the first cycle in a cycle range in which fails are counted.
    
    An integer. Cycle counting starts from zero.
    
    This is an optional parameter. If it is omitted, the cycle range starts with the first
    cycle.

Return value

There is no return value.

Note

The fail count and fail position are about "compare edge" (not tester cycle). So they
supports xMode directly.

The xMode parameter for a pin must be correct, otherwise the result for the pin will not
be correct.

The parameter specified in the function, such as
startCyc
 and

cycRange
, is about user cycles (edge), not tester cycles. This setting is
critical when xMode is set to be greater than 1.

For one pin, xMode must remain the same in different labels in burst; otherwise the
results might be wrong.

### Syntax（取自子主题 fillBit()）

```
fillBit(int bit,int bitLength,int startBit);
fillBit(const string bit,int bitLength,int startBit);
```
[表] List of parameters
列: Parameter | Description
行 1:
  bit
  The bit or string that you want to write to the pattern.
行 2:
  bitlength
  The length of the bits to be filled.
行 3:
  startBit
  The starting position of the bit to be written. If you do not specify a starting
    position, the default value is 0.

### Example（取自子主题 fillBit()）

```
RDI_BEGIN();
rdi.smartVec().pin("DATA1").fillBit(1,4,2).execute(); // index
RDI_END();
```

Supporting
a
string

```
RDI_BEGIN()
rdi.smartVec().pin("A").defaultBit(0).fillBit("p",4,1)
.xMode(2).bitLength(6)
.execute();
RDI_BEGIN();
```

You
must define device cycles in the corresponding wavetable.

### Syntax（取自子主题 fillVec()）

```
fillVec(int index,int vecLength,int startVec);
fillVec(string dvc,int vecLength,int startVec);
```
[表] List of parameters
列: Parameter | Description
行 1:
  index
  The physical index you want to write to the pattern .
行 2:
  dvc
  The device cycle you want to write to the pattern.
行 3:
  vecLength
  The length of the vector to be filled.
行 4:
  startVec
  The starting position of the vector to be written. If the
    startVec parameter missing, the default value is 0.

Note
 You must define the device cycles' names in the corresponding
wavetables.

### Example（取自子主题 fillVec()）

```
RDI_BEGIN()
rdi.smartVec().pin("DATA1").fillVec(3,1).execute(); // physical index= 3
rdi.smartVec().pin("DATA3").fillVec("0101",4).execute(); // device cycle
RDI_END();
```

### Syntax（取自子主题 insertJmpe()）

```
insertJmpe(int vecLine, int level);
```
[表] List of parameters
列: Parameter | Description
行 1:
  vecLine
  Number of the vector line where you want to insert the subroutine.
行 2:
  level
  Subroutine level. This refers to the target level at which you want to insert a new
    subroutine.
    
    The default value is 1, which means the first level subroutine and
    actually refers to the main pattern. To insert a subroutine into another subroutine, you
    should specify a level larger than 1.

Return value

There is no return value.

### Examples（取自子主题 insertJmpe()）

### Example 1
```
RDI_BEGIN();
rdi.smartVec(). pin("DATA1").writeData(0x1,8,0)// the content in main pattern
.insertJmpe(2).passNode().pin("DATA1").writeData(0x0,8,0) // the content of pass branch label of JMPE in main pattern
.failNode().pin("DATA1").writeData(0xf,8,0).execute(); // the content of fail branch label by JMPE in main pattern
RDI_END();
```

This
code example inserts two subroutines into the pattern at vector 2: one subroutine for pass node
and the other for fail node. See the figure below.

### Example 2

You can use
insertJmpe()
 inside
`insertSub()`（raw: `152254.htm`）
. Below is an
example.

```
RDI_BEGIN();
...
rdi.smartVec().pin()...pin()...
.insertSub(3).repeatSub()...
.insertJmpe(5,2).passNode()...
.failNode()...
.execute();
...
RDI_END();
```

### Example 3

You can also use
`insertSub()`（raw: `152254.htm`）
 inside

insertJmpe()
. Below is an
example.

```
RDI_BEGIN();
...
rdi.smartVec().pin()...pin()...
.insertJmpe(3)
.passNode()...
.insertSub(5,2).repeatSub()...
.failNode()...
.execute();
...
RDI_END();
```

### Example 4

You can insert
JSUB
 and

JMPE
 in the same vector line of a label. The
JSUB

instruction is invoked before the
JMPE
 instruction in this case. Below is an
example.

```
RDI_BEGIN();
rdi.smartVec("id5").pin("DATA1").writeData(0x1,8,0)
.insertSub(2).pin("DATA1").writeData(0x1,8,0)
.insertSub(2).pin("DATA1").writeData(0x2,8,0)
.insertJmpe(2).passNode().pin("DATA1").writeData(0x3,8,0)
.failNode().pin("DATA1").writeData(0x4,8,0)
.execute();
RDI_END();
```

### Syntax（取自子主题 insertSub()）

```
insertSub(int vecLine);
insertSub(int vecLine, int level);
```
[表] List of parameters
列: Parameter | Description
行 1:
  vecLine
  Number of the vector line where you want to insert the subroutine.
行 2:
  level
  Subroutine level. This refers to the target level at which you want to insert a new
    subroutine.
    
    The default value is 1, which means the first level subroutine and
    actually refers to the main pattern. To insert a subroutine into another subroutine, you
    should specify a level larger than 1.

Return value

There is no return value.

### Examples（取自子主题 insertSub()）

### Example 1
```
RDI_BEGIN();
rdi.smartVec("id2").pin("DATA1").writeData(0x1,8,0); // the content of the main pattern
.insertSub(3).pin("DATA1").writeData(0x3,8,0); // the content of sublabel A which is inserted in the main pattern
.insertSub(6).pin("DATA1").writeData(0x6,8,0); // the content of sublabel B, which is inserted in the main pattern
.insertSub(9,2).pin("DATA1").writeData(0x9,8,2).execute(); // the content of sublabel C which is inserted in sublabel B
RDI_END();
```

In
the example above, subroutines A and B are inserted into the main pattern at vector lines 3 and
6. subroutine C is inserted into a level 2 subroutine at vector line 9. Because the insertion is
always made in the closest label when multiple subroutines exist at the target insertion level,
subrountine C is inserted into subroutine B which is closer than A. The created pattern
structure is as follows.

### Example 2

Below is an example of using
`label()`（raw: `152250.htm`）
, for
example
label("abc")
, within

insertSub()
:

```
RDI_BEGIN();
...
rdi.smartVec().pin()...pin()... // the content in the main pattern
.insertSub(10).label("abc") // label "abc" is inserted in the main pattern with JSUB
.insertSub(5 ).label("abc").pin()...pin()... // sublabel A (copied and edited from "abc") is inserted in the main pattern with JSUB
...
RDI_END();
```

In
this example,

If there are no
pin()...pin()...
 settings after
label()
,
the label "abc" will be directly called by JSUB.

If there are
pin()...pin()...
 settings after
label()
, the
label "abc" will be copied and edited, then called by JSUB.

If the label "abc" is not a subroutine, SmartRDI will clone it to a subroutine, then call it
by JSUB and give a warning.

### Example 3

Below is an example when
insertSub()
 is put
in to
`label()`（raw: `152250.htm`）
, for example

label("abc")
:

```
RDI_BEGIN();
rdi.smartVec().label("abc").pin()...pin()... // the content in the main pattern
.insertSub(5).pin()...pin()... // the content in sublabel A, which is inserted in the main pattern
RDI_END();
```

In
this example,

If
`copyLabel()`（raw: `152245.htm`）
 is set to
true
, the JSUB will be inserted into
the copy of label "abc"; if
`copyLabel()`（raw: `152245.htm`）
 is set to
false
, the
JSUB will be inserted directly into label "abc".

Following the general rule, omitting the
`copyLabel()`（raw: `152245.htm`）
 command by default makes a
copy of the label "abc" and inserts the modification. The copied label name will hold the
content of the actions. It ensures the right content in the right pattern.

### Example 4

insertSub(
) can be used inside a

burstLabel().begin()
/
burstLabel().end()
 block, as long as it
is not inserted into a user label. Below is an
example.

```
RDI_BEGIN();
rdi.smartVec().burstLabel("smv").begin();
rdi.smartVec().pin("DATA1").readData(2,0)
.insertSub(3).repeatSub(5).pin("DATA1").writeData(0x86,8,3).execute();
rdi.smartVec()
.insertSub(10).pin("DATA1").writeData(0x86,8,3).execute();
rdi.smartVec().burstLabel().end();
RDI_END();
```

### Syntax（取自子主题 label()）

```
label(const string& sLabelName);
```

[表] List of parameters
列: Parameter | Description
行 1:
  sLabelName
  The label to be executed / pattern on which measurement is performed.

Return value

There is no return value.

### Example（取自子主题 label()）

```
RDI_BEGIN();
...
rdi.smartVec().label("label4").pin("D3").writeData(0x55,8,0).execute();
...
RDI_END();
```

### Syntax（取自子主题 labelName()）

```
labelName(const string &name);
labelName(const string &name, TA::MD5_OPTION);
```
[表] List of parameters
列: Parameter | Description
行 1:
  name
  User specified name for the label.
行 2:
  TA::MD5_OPTION
  The option which defines to use an MD5 postfix string or not.
[表] List of available options of parameter: <TA::MD5_OPTION>
列: Option | Description
行 1:
  TA::MD5_ON
  With an MD5 postfix string in the label name.
    With MD5_ON, the maximum length of a
    valid "targetLabelName" in the generated pattern name is 74.
行 2:
  TA::MD5_OFF
  Without an MD5 postfix string in the label name. This is the default value.
    
    With MD5_OFF, the maximum length of a valid "targetLabelName" in the
    generated pattern name is 111.

### Example（取自子主题 labelName()）

```
RDI_BEGIN();
rdi.smartVec().pin("DATA1,DATA3").writeData(0x54,8,2).readData(8,20).labelName("label_name").execute();
RDI_END();
```

Note
 If a label with the same name exists, the pattern will not be re-generated. So
make sure that the label name will change if the content changes.

### Syntax（取自子主题 multiFFC()）

```
multiFFC(int startCycle, int FailNumber);
```

[表] List of parameters
列: Parameter | Description
行 1:
  startCycle
  The number of the first cycle to start the action.
行 2:
  FailNumber
  The number of failing cycles within a pattern to acquire.

Use the following functions to collect the result:

getMultiFFC(string resultPin)

getMultiFFC()
:Use this command if only one result pin exists.

Note

The fail count and fail position are about "compare edge" (not tester cycle). So they
supports
`xMode`（raw: `149062.htm`）
 directly.

The
`xMode`（raw: `149062.htm`）
 parameter for a pin must be correct, otherwise the
result for the pin will not be correct.

The parameter specified in the function, such as
startCyc
 and

cycRange
, is about user cycles (edge), not tester cycles. This setting is
critical when
`xMode`（raw: `149062.htm`）
 is set to be greater than 1.

For one pin,
`xMode`（raw: `149062.htm`）
 must remain the same in different labels
in burst; otherwise the results might be wrong.

### Example（取自子主题 multiFFC()）

```
RDI_BEGIN();
rdi.emap("mffc").label("abc")
.pin("inA")
.multiFFC(0,100)
.execute();
/* For smartVec():
rdi.smartVec("mffc").label("abc")
.pin("inA")
.multiFFC(0,100)
.execute();
*/

RDI_END();

rdi.id("mffc").getMultiFFC();
```

### Syntax（取自子主题 passNode()）

```
passNode();
```

List of parameters

There are no parameters.

Return value

There is no return value.

### Example（取自子主题 passNode()）

```
RDI_BEGIN();
...
rdi.smartVec...
.insertJmpe(2).passNode().pin("DATA1").writeData(0x0,8,0)...execute();
...
RDI_END();
```

### Syntax（取自子主题 pMode()）

```
pMode(int Pmode);
```
[表] List of parameters
列: Parameter | Description
行 1:
  Pmode
  The number of tester cycles per device cycle.

### Example（取自子主题 pMode()）

```
RDI_BEGIN();
rdi.smartVec().pin("DATA1").fillBit(1,4,2).pMode(2).execute();
rdi.smartVec().pin("DATA3").readBit(4,2).pMode(2).execute();
rdi.smartVec().pin("DATA5").writeData(0x54,8,4).pMode(4).execute();
rdi.smartVec().pin("DATA7").readData(8,4).pMode(4).execute();
RDI_END();
```

### Syntax（取自子主题 pModeStrobe()）

```
pModeStrobe(int strobePos);
```
[表] List of parameters
列: Parameter | Description
行 1:
  strobePos
  The strobe position within pMode cycles.

### Example（取自子主题 pModeStrobe()）

```
RDI_BEGIN();
rdi.smartVec().pin("DATA7").readData(8,4).pMode(4).pModeStrobe(3).execute();
RDI_END();
```

The
following code illustrates the operation of
pModeStrobe.

```
rdi.smartVec().pin("A").expectBit(arr).pMode(4).pModeStrobe(2).execute();
```

expect bit : 001-> LLH

vec: XLXXXHXXXHXX

### Syntax（取自子主题 readBit()）

```
readBit(int bitLength,int startBit);
```
[表] List of parameters
列: Parameter | Description
行 1:
  bitLength
  The length of the bits to be read
行 2:
  startBit
  The starting position of the bits to be read. If the "startBit" parameter missing,
    the default value is 0.

### Example（取自子主题 readBit()）

```
RDI_BEGIN();
rdi.smartVec().pin("DATA1").readBit(4,2).execute();
RDI_END();
```

### Syntax（取自子主题 readData()）

```
readData(int bitLength,int startBit);
```
[表] List of parameters
列: Parameter | Description
行 1:
  bitLength
  The length of the bits (data will be automatically converted into bits) to be
    read.
行 2:
  startBit
  The starting position of the bits to be read. If the startBit
    parameter missing, the default value is 0.

### Example（取自子主题 readData()）

```
RDI_BEGIN();
rdi.smartVec("result").pin("DATA1").readData(4,2).execute();
RDI_END();
...
ARRAY_LL data_result = rdi.id("result").getReadData("DATA1");
```

### Syntax（取自子主题 rdi.smartVec().readMode()）

```
readMode(TA::MEAS_TYPE mode);
```
[表] List of parameters
列: Parameter | Description
行 1:
  mode
  The read mode.
[表] List of available options of parameter: <mode>
列: Option | Description
行 1:
  TA::EMAP
  The error map as the read mode.
    
    In this mode, for each pin, the ERROR_MAP_TEST API is used to get all
    failed positions. A post processing is done afterward.
行 2:
  TA::DIGCAP
  The digital capture as the read mode.
    
    In this mode, a dummy pattern with a digital capture variable is created. It cannot be
    mixed with the digCap() class inside a
    burstUpload-begin()/end() block.

Note
 The option
TA::EMAP
 cannot be used together with a match loop
in label.

### Example（取自子主题 rdi.smartVec().readMode()）

```
rdi.smartVec().readMode(TA::EMAP);

RDI_BEGIN();
...
rdi.smartVec().pin("A").read...().execute();
...
RDI_END();
```

### Syntax（取自子主题 repeat()）

```
repeat(int rptNum);
repeat(int rptNum, int vecSize, int startVec); // relevant only for the Vector class
```

[表] List of parameters
列: Parameter | Description
行 1:
  rptNum
  The loop / repeat number.
行 2:
  vecSize
  Only Vector class: Vector size. Used together with startVec to define
    the sector for repetition.
行 3:
  startVec
  Only Vector class: Start vector. Used together with vecSize to define
    the sector for repetition.

### Examples（取自子主题 repeat()）

### Example 1

```
// Have some content repeats in pattern, for example, clock signal
RDI_BEGIN();
rdi.port("clk").smartVec().pin("CLK").writePat("0,1,1").repeat(1000).execute();
RDI_END();
// readBit()/readData() with a huge number
RDI_BEGIN();
rdi.smartVec().pin("dout").readBit(10000).execute(); // original
RDI_END();
RDI_BEGIN();
rdi.smartVec().pin("dout").readBit(1).repeat(10000).execute();
RDI_END();
```

### Example 2

```
RDI_BEGIN();
rdi.smartVec()...repeat(5,10,2).repeat(4,5,20).execute();
// add RPTV to 2 different segments of the pattern
RDI_END();
```

### Syntax（取自子主题 repeatSub()）

```
repeatSub(int repeatNum);
```
[表] List of parameters
列: Parameter | Description
行 1:
  repeatNum
  number of repeated subroutine calls.

Return value

There is no return value.

### Example（取自子主题 repeatSub()）

```
RDI_BEGIN();
rdi.smartVec(). pin("DATA1").writeData(0x1,8,0) // the content in the main pattern
.insertSub(5).repeatSub(5).pin("DATA1").writeData(0x3,8,0).execute(); // the content in sublabel 1, RPTJ 5, which is inserted in the main pattern
RDI_END();
```

With
the above code, you add the target subroutine at the vector 5 for five times, as the figure
below shows.

### Syntax（取自子主题 rdi.smartVec().vecEditMode()）

```
rdi.smartVec().vecEditMode(TA::Mode);
```
[表] List of parameters
列: Parameter | Description
行 1:
  TA::Mode
  The mode to be used for one piece of pattern.
[表] List of available options of parameter: <TA::Mode>
列: Option | Description
行 1:
  TA::VECD
  The VECD firmware command mode, which calls the
    VECD FW command for vector editing.
行 2:
  TA::VTT
  The VEC_TRANSFER_TASK API mode.

### Examples（取自子主题 rdi.smartVec().vecEditMode()）

### Example 1

To change the edit mode across
RDI_BEGIN()
/
RDI_END()

blocks:

```
rdi.smartVec().vecEditMode(TA::VECD);
RDI_BEGIN();
...
rdi.smartVec() ... execute(); // Runtime editing
...
RDI_END();

rdi.smartVec().vecEditMode(TA::VTT);
RDI_BEGIN();
...
rdi.smartVec() ... execute(); // Runtime editing
...
RDI_END();
```

### Example 2

To change edit mode inside the
RDI_BEGIN()
/
RDI_END()
 block:

```
RDI_BEGIN();
rdi.smartVec().vecEditMode(TA::VECD);
rdi.smartVec()...;// run-time edit
rdi.smartVec().vecEditMode(TA::VTT);
rdi.smartVec()...;// run-time edit
RDI_END();
```

### Example 3

Use only the VTT mode for editing vectors when
`copyLabel()`（raw: `152252.htm`）
 is used for the
label.

```
rdi.smartVec().vecEditMode(TA::VTT);

RDI_BEGIN();
rdi.smartVec().label("sLabel").copyLabel(false).pin(A)
.writeData("rt",8,0).execute();
rdi.smartVec().label("sLabel").copyLabel(false).pin(A)
.writeData("rt",8,8).execute(); // a different position
RDI_END();
```

### Syntax（取自子主题 vecLength()）

```
vecLength(int length);
```
[表] List of parameters
列: Parameter | Description
行 1:
  length
  The length of the pattern.

Note
 If the pattern contents exceed the length defined by the

vecLength()
 parameter, the length of the generated pattern refers to the
value of the
vecLength()
 parameter. The overhang will be cut
off.

### Example（取自子主题 vecLength()）

```
RDI_BEGIN();
rdi.smartVec().pin("DATA1").defaultVec(0).vecLength(10).execute();
RDI_END();
```

### Syntax（取自子主题 writeBit()）

```
writeBit(ARRAY_I bitStream,int startBit);
writeBit(const string &sData, int startBit); // application for runtime
writeBit(vector<ARRAY_I> perSiteBitStream, int startBit);
```

For pattern generation with bit streams per site, the sizes of all elements in

ARRAY_I
 must be the same. The value for a site can be different from the
value for another site. The values for all sites cannot be changed at runtime.

For more information about bits versus DVCs, see
`Relationship between bits and device cycles`（raw: `351019.htm`）
.

[表] List of parameters
列: Parameter | Description
行 1:
  bitStream
  The bit stream to be written to the pattern.
行 2:
  sData
  The sData of the parameter that can be changed at runtime.
行 3:
  startBit
  The bit position in pattern, starting from which the specified bit stream or sData to be
    written on.
    
    If the startBit parameter is not specified, the default value is
    0.
行 4:
  perSiteBitStream
  The bit stream per site.

### Examples（取自子主题 writeBit()）

```
...
ARRAY_I bitStream(4);
bitStream[0]=1;
bitStream[1]=0;
bitStream[2]=1;
bitStream[3]=1;

RDI_BEGIN();
rdi.smartVec().pin("DATA1").writeBit(bitStream,4).execute();
rdi.smartVec().pin("DATA1").writeBit(bitStream).execute(); // The value of the "startBit" is 0.
RDI_END();
```

Application for
runtime

```
...
// This data type for writeBit() runtime
vector<ARRAY_I> runtime_vec_ARRAY_I;
//Initialize the array with required data
rdi.runTimeVal("string_runtime_vec_ARRAY_I", runtime_vec_ARRAY_I);

// This data type for writeBit() runtime
ARRAY_I runtime_ARRAY_I;
//Initialize the array with required data
rdi.runTimeVal("string_runtime_ARRAY_I", runtime_ARRAY_I);

RDI_BEGIN();
rdi.smartVec().pin("DATA1").writeBit("string_runtime_vec_ARRAY_I",2).execute();
rdi.smartVec().pin("DATA3").writeBit("string_runtime_ARRAY_I",4).execute();
RDI_END();
```

Pattern generation with per-site
data

```
...
vector<ARRAY_I> perSiteBitStream_1,perSiteBitStream_2;
ARRAY_I dataBit(8);
dataBit[0] = 1;
...
RDI_BEGIN();
rdi.smartVec().pin("DATA3").writeBit(perSiteBitStream_1,0).writeData(0x55,8,20).execute();
...
RDI_END();
ARRAY_I bitStream(20),bitStream_2(20);
...
perSiteBitStream_1.push_back(bitStream);
perSiteBitStream_2.push_back(bitStream_2);
...
RDI_BEGIN();
rdi.smartVec().pin("DATA1").writeBit(perSiteStream_1,0).defaultBit(0)
.pin("DATA2").readData(4,0).execute();
...
RDI_END();
```

### Syntax（取自子主题 writeData()）

```
writeData(long long data,int bitLength,int startBit);
writeData(const string &sData, int bitLength, int startBit); // application for runtime
writeData(ARRAY_LL perSiteData, int bitLength, int startBit); // values for all sites must be different each other and cannot be changed at runtime
```
[表] List of parameters
列: Parameter | Description
行 1:
  data
  The data block you want to write to the pattern.
行 2:
  bitLength
  The length of the bits (data will be automatically converted into bits) to be written.
行 3:
  sData
  The sData of the parameter that can be changed at runtime.
行 4:
  startBit
  The starting position of the bits to be written. If the startBit parameter is
    not specified, the default value is 0.
行 5:
  perSiteData
  The array of data.

### Example（取自子主题 writeData()）

```
RDI_BEGIN();
rdi.smartVec().pin("DATA1").writeData(0x54,8,4).execute();
rdi.smartVec().pin("DATA3").writeData(0x54,8).execute(); // the value of the "startBit" is 0.
RDI_END();

// application for runtime
static int runtime=0;
ARRAY_I runtime_ARRAY_I; // this data type for writeData() runtime is supported
ARRAY_LL runtime_ARRAY_LL; // this data type for writeData() runtime is supported
int runtime_int;// this data type for writeData() run-time is supported
long long runtime_longlong; // this data type for writeData() runtime is supported
rdi.runTimeVal("string_runtime_ARRAY_I", runtime_ARRAY_I);
rdi.runTimeVal("string_runtime_ARRAY_LL", runtime_ARRAY_LL);
rdi.runTimeVal("string_runtime_int", runtime_int);
rdi.runTimeVal("string_runtime_longlong", runtime_longlong);

RDI_BEGIN();
rdi.smartVec().pin("DATA1").writeData("string_runtime_ARRAY_I",8,2).execute();
rdi.smartVec().pin("DATA3").writeData("string_runtime_ARRAY_LL",8,4).execute();
rdi.smartVec().pin("DATA5").writeData("string_runtime_int",4,2).execute();
rdi.smartVec().pin("DATA7").writeData("string_runtime_longlong",64,4).execute();
RDI_END();

// Pattern generation with different data per site.
ARRAY_LL Data(4); // four sites are used
Data[0]=1;
Data[1]=2;
Data[2]=3;
Data[3]=4;

RDI_BEGIN();
rdi.smartVec().pin("DATA2").writeData(Data,4).execute();
RDI_END();
```

### Syntax（取自子主题 writeDataBurst()）

```
writeDataBurst(ARRAY_I data, ARRAY_I bitLength, ARRAY_I startBit);
writeDataBurst(ARRAY_I data, int bitLength, int bitDistance, int startBit);
writeDataBurst(ARRAY_I data, int bitLength); // startBit =0,bitDistance=bitLength
writeDataBurst(ARRAY_LL data, ARRAY_I bitLength, ARRAY_I startBit);
writeDataBurst(ARRAY_LL data, int bitLength, int bitDistance, int startBit);
writeDataBurst(ARRAY_LL data, int bitLength); // startBit =0,bitDistance=bitLength
```
[表] List of parameters
列: Parameter | Description
行 1:
  data
  The array of data you want to write to the pattern.
行 2:
  bitLength
  The length of the bits (data will be automatically converted into bits) to be
    written.
行 3:
  bitDistance
  The bit distance between one data and the next data.
行 4:
  startBit
  The starting position of the bits to be written. If the startBit
    parameter missing, the default value is 0.

### Example（取自子主题 writeDataBurst()）

```
ARRAY_I array_data_1(4); // data array
array_data_1[0]=0x1;
array_data_1[1]=0x23;
array_data_1[2]=0x456;
array_data_1[3]=0x7890;
ARRAY_I bitLength(4); // bitLength array
bitLengt[0]=4;
bitLengt[1]=8;
bitLengt[2]=12;
bitLengt[3]=16;
ARRAY_I startBit(4); // startBit array
startBit[0]=0;
startBit[1]=4;
startBit[2]=12;
startBit[3]=24;
RDI_BEGIN();
rdi.smartVec().pin("DATA1").writeDataBurst(array_data_1,bitLength,startBit).execute();
RDI_END();
ARRAY_I array_data_2(4);
array_data_2[0]=0x12;
array_data_2[1]=0x34;
array_data_2[2]=0x56;
array_data_2[3]=0x78;
RDI_BEGIN();
rdi.smartVec().pin("DATA3").writeDataBurst(array_data_2,8,4).execute(); // the default value of "startBit" is 0
rdi.smartVec().pin("DATA5").writeDataBurst(array_data_2,8).execute(); // startBit=0,bitDistance=bitLength
RDI_END();
```

### Syntax（取自子主题 writeParData()）

```
writeParData(long long Data, int startBit);
writeParData(const string &sData, int startBit); // application for runtime
writeParData(ARRAY_LL perSiteData, int startBit);
```

For pattern generation with different data per site, values for all sites must be different
each other and cannot be changed at runtime.

[表] List of parameters
列: Parameter | Description
行 1:
  data
  The array of data you want to write to the pattern.
行 2:
  sData
  The sData of the parameter that can be changed at run-time.
行 3:
  startBit
  The starting position of the bits to be written. If the startBit parameter is
    not specified, the default value is 0.
行 4:
  perSiteData
  The array of data.

### Example（取自子主题 writeParData()）

```
// 11(Dec) = 1011(Bin), "1011" will be assigned into the four pins successively,
// DATA1=1,DATA3=0,DATA5=1,DATA7=1
// 6(Dec) = 110(Bin), "110" will be assigned into the three pins successively,
// DATA9=1,DATA11=1,DATA13=0
RDI_BEGIN();
rdi.smartVec().pin("DATA1,DATA3,DATA5,DATA7").writeParData(11,4).execute();
rdi.smartVec().pin("DATA9,DATA11,DATA13").writeParData(6,4).execute();
RDI_END();

//application for runtime
static int runtime=0;
ARRAY_I runtime_ARRAY_I(4);//parallel data array, this data type for writeParData() run-time is supported
ARRAY_LL runtime_ARRAY_LL(4);//parallel data array, this data type for writeParData() run-time is supported
int runtime_int;//this data type for writeParData() run-time is supported
long long runtime_longlong;//this data type for writeParData() run-time is supported
rdi.runTimeVal("string_runtime_ARRAY_I", runtime_ARRAY_I);
rdi.runTimeVal("string_runtime_ARRAY_LL", runtime_ARRAY_LL);
rdi.runTimeVal("string_runtime_int", runtime_int);
rdi.runTimeVal("string_runtime_longlong", runtime_longlong);
RDI_BEGIN();
rdi.smartVec().pin("DATA1,DATA3,DATA5,DATA7").writeParData("string_runtime_ARRAY_I",2).execute();
rdi.smartVec().pin("DATA9,DATA11,DATA13,DATA15").writeParData("string_runtime_ARRAY_LL",4).execute();
rdi.smartVec().pin("DATA17,DATA19,DATA21,DATA23").writeParData("string_runtime_int",6).execute();
rdi.smartVec().pin("DATA25,DATA27,DATA29,DATA31").writeParData("string_runtime_longlong",8).execute();
RDI_END();

// Pattern generation with different data per site.
ARRAY_LL perSiteData(4); // four sites are used
...
RDI_BEGIN();
rdi.smartVec().pin("GP").writeParData(perSiteData).execute();
RDI_END();
```

### Syntax（取自子主题 writeParDataBurst()）

```
writeParDataBurst(ARRAY_I data, int bitDistance, int startBit);
writeParDataBurst(ARRAY_I data); // bitDistance=1, startBit=0
writeParDataBurst(ARRAY_LL data, int bitDistance, int startBit);
writeParDataBurst(ARRAY_LL data);// bitDistance=1, startBit=0
```
[表] List of parameters
列: Parameter | Description
行 1:
  data
  The array of data you want to write to the pattern.
行 2:
  bitDistance
  The bit distance between one data and the next data.
行 3:
  startBit
  The starting position of the bits to be written. If the startBit
    parameter missing, the default value is 0.

### Example（取自子主题 writeParDataBurst()）

```
ARRAY_I I_ParDataBurst(4); // parallel data array
I_ParDataBurst[0]=0x01;
I_ParDataBurst[1]=0x05;
I_ParDataBurst[2]=0x09;
I_ParDataBurst[3]=0x0B;
RDI_BEGIN();
rdi.smartVec().pin("DATA1,DATA3,DATA5,DATA7").writeParDataBurst(I_ParDataBurst,2,4).execute();
rdi.smartVec().pin("DATA1,DATA3,DATA5,DATA7").writeParDataBurst(I_ParDataBurst).execute();
RDI_END();
ARRAY_LL LL_ParDataBurst(4); // parallel data array
LL_ParDataBurst[0]=0x01;
LL_ParDataBurst[1]=0x05;
LL_ParDataBurst[2]=0x09;
LL_ParDataBurst[3]=0x0B;
RDI_BEGIN();
rdi.smartVec().pin("DATA1,DATA3,DATA5,DATA7").writeParDataBurst(LL_ParDataBurst,2,4).execute();
rdi.smartVec().pin("DATA1,DATA3,DATA5,DATA7").writeParDataBurst(LL_ParDataBurst).execute();
RDI_END();
```

### Syntax（取自子主题 writePat()）

```
writePat(const string &dvc,int startVec);
```
[表] List of parameters
列: Parameter | Description
行 1:
  dvc
  The device cycle you want to write into the pattern.
行 2:
  startVec
  The starting position of the vector to be written. If the
    startVec parameter missing, the default value is 0.

### Example（取自子主题 writePat()）

```
RDI_BEGIN();
rdi.smartVec().pin("DATA1").writePat("0,1,Z,Z,H",1).execute();
RDI_END();
```

### Syntax（取自子主题 writeVec()）

```
writeVec(vector<string> dvcList, int startVec);
writeVec(ARRAY_I indexList, int startVec);
writeVec(const string &sData, int startVec); // application for runtime
writeVec(vector<ARRAY_I> perSiteIndex, int startVec);
writeVec(vector<vector<string>> perSiteDvc, int startVec);
```

For pattern generation with per-site data, the sizes of all elements in

ARRAY_I
 or
vector<string>
 must be the same. The value
for a site can be different from the value for another site. The values for all sites cannot be
changed at runtime.

[表] List of parameters
列: Parameter | Description
行 1:
  dvcList
  The device cycle list you want to write to the pattern.
行 2:
  indexList
  The physical index list you want to write to the pattern.
行 3:
  sData
  The sData of the parameter that can be changed at runtime.
行 4:
  startVec
  The starting position of the vector to be written. If the startVec parameter
    is not specified, the default value is 0.
行 5:
  perSiteIndex
  The index list per site.
行 6:
  perSiteDvc
  The device cycle list per site.

### Examples（取自子主题 writeVec()）

```
vector<string> dvcList;
dvcList.push_back("1"); // device cycle
dvcList.push_back("0");

ARRAY_I indexList(3);
indexList[0]=0; // physical index
indexList[1]=1;
indexList[2]=2;
RDI_BEGIN();
rdi.smartVec().pin("DATA1").writeVec(dvcList,1).execute(); // dvcList
rdi.smartVec().pin("DATA3").writeVec(indexList,4).execute(); // indexList
RDI_END();
```

Application for
runtime

```
vector<ARRAY_I> runtime_vec_ARRAY_I; // this data type for writeData() runtime is supported
rdi.runTimeVal("string_runtime_vec_ARRAY_I", runtime_vec_ARRAY_I);

// This data type for writeData() run-time is supported
ARRAY_I runtime_ARRAY_I;
//Initialize the array with required data
rdi.runTimeVal("string_runtime_ARRAY_I", runtime_ARRAY_I);

RDI_BEGIN();
rdi.smartVec().pin("DATA1").writeVec("string_runtime_vec_ARRAY_I",2).execute();
rdi.smartVec().pin("DATA3").writeVec("string_runtime_ARRAY_I",4).execute();
RDI_END();
```

Pattern generation with per-site
data

```
// The sizes of ARRAY_I index1, index2, index3, and index4 must be the same:
ARRAY_I index1(8), index2(8), index3(8), index4(8);
vector<ARRAY_I> perSiteIndex;
perSiteIndex.push_back(index1);
...
RDI_BEGIN();
rdi.smartVec().pin("A").writeVec(perSiteIndex,2).execute();
RDI_END();
```

```
...
vector<string> vec_s;
vec_s.push_back("0");
vec_s.push_back("1");
vec_s.push_back("0");
vec_s.push_back("1");

vector<string> vec_s1;
vec_s1.push_back("1");
vec_s1.push_back("0");
vec_s1.push_back("1");
vec_s1.push_back("0");

vector<vector<string> > vec_vec_s;
vec_vec_s.push_back(vec_s);
vec_vec_s.push_back(vec_s1);
vec_vec_s.push_back(vec_s);
vec_vec_s.push_back(vec_s1);

RDI_BEGIN();
rdi.smartVec().pin("DATA1").writeVec(vec_vec_s).execute();
RDI_END();
```

### Syntax（取自子主题 xMode()）

```
xMode(int Xmode);
```
[表] List of parameters
列: Parameter | Description
行 1:
  Xmode
  The number of device cycles in each tester cycle.

Note

The fail count and fail position are about "compare edge" (not tester cycle). So they
supports xMode directly.

The xMode parameter for a pin must be correct, otherwise the result for the pin will not
be correct.

The parameter specified in the function, such as
startCyc
 and

cycRange
, is about user cycles (edge), not tester cycles. This setting is
critical when xMode is set to be greater than 1.

For one pin, the xMode must remain the same in different labels in burst; otherwise the
results might be wrong.

Note
 For correctly retrieving the results of error map data:

For a specified pin, in one RDI_BEGIN/RDI_END block, its xMode number must remain the same
value, no matter it is for a SmartRDI command or in the user pattern.

In the wavetable, the length of the device cycle name must align with the xMode() value.
For example, if you set xMode to xMode(2), the dvc must correspondingly have two letters,
such as "LL", "00", "11", "LL". Even the dvc of the physical index f, which normal value is
"." with SmartRDI, must be ".." for xMode(2). Otherwise SmarTest cannot recognize the correct
xMode value from pattern.

### Example（取自子主题 xMode()）

```
RDI_BEGIN();
rdi.smartVec().pin("DATA1").fillBit(1,4,2).xMode(2).execute();
rdi.smartVec().pin("DATA3").readBit(4,2).xMode(2).execute();
rdi.smartVec().pin("DATA5").writeData(0x54,8,4).xMode(4).execute();
rdi.smartVec().pin("DATA7").readData(8,4).xMode(4).execute();
RDI_END();
```

Data
from
`readBit()`（raw: `149049.htm`）
,
`readData()`（raw: `149057.htm`）
,
`expectBit()`（raw: `149046.htm`）
, or
`expectData()`（raw: `149056.htm`）
 can cross over device
cycles.

```
RDI_BEGIN();
rdi.smartVec().pin("A").expectData(0,4,1).defaultBit(0)
.xMode(2).bitLength(8)
.execute();
RDI_END();
```

The
result vector:

Supporting a string from
`fillBit()`（raw: `149045.htm`）
 and
`defaultBit()`（raw: `149047.htm`）
.

```
RDI_BEGIN();
rdi.smartVec().pin("A").defaultBit(0).fillBit("p",4,1)
.xMode(2).bitLength(6)
.execute();
RDI_END();
```

The
result vector:

Note
 You must define device cycle names in the corresponding
wavetable.

### Syntax（取自子主题 getFailCount()）

```
int getFailCount(string pin);
```
[表] List of parameters
列: Parameter | Description
行 1:
  pin
  Specifies a pin for which to get the fail count.

### Return value（取自子主题 getFailCount()）

The return value is an integer indicating the number of
errors.

### Example（取自子主题 getFailCount()）

```
ON_FIRST_INVOCATION_BEGIN();

RDI_BEGIN();
rdi.smartVec("a").pin("pA").writePat("0,1,1,H,H,H,L").failCount().execute();
RDI_END();

ON_FIRST_INVOCATION_END();

int fcount=rdi.id("a").getFailCount("pA");
```

### Syntax（取自子主题 getFailCyc()）

```
ARRAY_LL getFailCyc(string pin);
```
[表] List of parameters
列: Parameter | Description
行 1:
  pin
  Specifies a pin for which to get all failing cycles' positions.

### Return value（取自子主题 getFailCyc()）

The return value is an ARRAY_LL indicating all failing
cycles' positions.

### Syntax（取自子主题 getFFC()）

```
int getFFC(string pin);
```
[表] List of parameters
列: Parameter | Description
行 1:
  pin
  Specifies a pin for which to get the first failing cycle.

### Return value（取自子主题 getFFC()）

The return value is an integer indicating the first failing
cycle.

### Syntax（取自子主题 rdi.id().getMultiFFC()）

```
ARRAY_LL getMultiFFC(string pin);
ARRAY_LL getMultiFFC(); // if only one result pin exists.
```

[表] List of parameters
列: Parameter | Description
行 1:
  pin
  The pin for which to retrieve the number of failing cycles.

### Example（取自子主题 rdi.id().getMultiFFC()）

```
RDI_BEGIN();
rdi.emap("mffc").label("abc")
.pin("inA")
.multiFFC(0,100)
.execute();
RDI_END();

rdi.id("mffc").getMultiFFC();
```

### Syntax（取自子主题 getReadBit()）

```
ARRAY_I getReadBit(const string &pin);
```
[表] List of parameters
列: Parameter | Description
行 1:
  pin
  The pin to query.

Note
 If the pin parameter is missing, the default pin will be
used.

### Example（取自子主题 getReadBit()）

```
ON_FIRST_INVOCATION_BEGIN();
RDI_BEGIN();
rdi.smartVec("result").pin("DATA1").readBit(4,2).execute();
RDI_END();
ON_FIRST_INVOCATION_END();
ARRAY_I bit_result = rdi.id("result").getReadBit("DATA1");
```

### Syntax（取自子主题 getReadData()）

```
ARRAY_LL getReadData(const string &pin);
```

[表] List of parameters
列: Parameter | Description
行 1:
  pin
  The pin to query.

### Example（取自子主题 getReadData()）

```
ON_FIRST_INVOCATION_BEGIN();
RDI_BEGIN();
rdi.smartVec("result").pin("DATA1").readData(4,2).execute();
RDI_END();
ON_FIRST_INVOCATION_END();
ARRAY_LL data_result = rdi.id("result").getReadData("DATA1");
```

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
