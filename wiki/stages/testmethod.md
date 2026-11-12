---
type: stage
title: Test Method / 测试方法与 Test Instance（L2 C++ API）
tags: [testmethod, test-instance, utm, cpp, l2, test-method-api, parameters, limits, datalog, ccf, smartrdi]
related:
  - "[[project]]"
  - "[[pin]]"
  - "[[level]]"
  - "[[timing]]"
  - "[[pattern]]"
  - "[[testflow]]"
  - "[[run]]"
  - "[[results]]"
sources:
  - 01_Getting_started/01.06_Test_methods/01.06_Test_methods.htm
  - 01_Getting_started/01.06_Test_methods/01.06.01_Test_Method_Introduction.htm
  - 01_Getting_started/01.06_Test_methods/01.06.02_Setting_up_an_AC_test_with_universal_test_method.htm
  - 01_Getting_started/01.06_Test_methods/01.06.02.01_1._Create_a_Test_Method_Project.htm
  - 01_Getting_started/01.06_Test_methods/01.06.02.02_2._Create_a_Test_Method_Class.htm
  - 01_Getting_started/01.06_Test_methods/01.06.02.03_3._Add_the_source_code.htm
  - 01_Getting_started/01.06_Test_methods/01.06.02.04_4._Build_the_project_to_get_the_universal_test_method_library.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07_Test_Method_Reference.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.01_Introduction.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.01.01_Test_Method_Program_Introduction.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.01.01.01_Testing_flow_and_Test_Method_API.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.01.01.02_Code-based_and_pattern-based_programming.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.02_Universal_Test_Method.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.02.01_Universal_test_method_concept.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.02.01.01_Test_method_executor.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.02.02.01_How_to_create_a_universal_test_method_project.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.02.02.02_How_to_create_a_universal_test_method_class.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.02.02.03_How_to_create_and_execute_a_universal-test-method-based_testflow.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.02.02.04_How_to_debug_a_universal_test_method.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.02.03_Managing_the_universal_test_method_libraries.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.02.04_Using_classic_test_method_in_the_universal_test_method_environment.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.02.05_Converting_user_procedures_to_universal_test_methods.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.02.06_Converting_a_classic_testflow_to_a_UTM-based_testflow.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.02.07_Using_the_predefined_universal_Test_Method_Libraries.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.02.08_List_of_predefined_universal_test_methods.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.02.09_How_to_use_test_method_snippets_in_the_programming.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.02.10_Editing_test_method_from_a_testflow.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.02.11_Using_C_C___functions_from_external_libraries_in_universal_test_methods.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.02.12_How_to_develop_a_test_program_with_concurrent_test_framework.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.02.13_Parameter_types_defined_for_universal_test_method.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.02.13.01_FileString.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.02.13.02_OptionList.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.02.13.03_SpecValue.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.02.13.04_SpecVariable.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.02.13.05_TestMethodParameterProxy.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03_Test_Method_Programming_Essentials.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.01_Points_to_Remember_before_Actual_Programming.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.01.08_Style_of_Test_Method_APIs.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.02_DC_Test_Programming.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.02.01_Flex_DC.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.02.02_DC_Test_Programming_with_PPMU.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.02.03_Direct_DMM_high-accuracy_voltage_measurements_via_utility_pogo_block.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.02.04_DC_test_programming_with_DPS.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.02.05_Setting_up_DC_Connection_for_Analog_Pin.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.02.06_DC_Test_Methods__DC_Sets__and_Measurement_Sets.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.02.07_Executing_PPMU_tests_from_a_pattern.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.02.08_Per_Pin_PMU.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.02.09_Miscellaneous_Considerations_for_DC_tests.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.03_AC_Test_Programming.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.03.01_Using_Setup_APIs_for_AC_test.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.03.02_Changing_and_obtaining_digital_settings.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.03.03_Setting_up_Routing_Connections.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.03.04_Executing_an_AC_Test.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.03.05_Retrieving_AC_Test_Results.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.03.05.01_Retrieving_Results_of_Multiple_Measurements_from_Digitizer_Sampler.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.03.05.02_Retrieving_Result_from_Vector_Memory.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.03.05.03_Retrieving_Functional_Test_Results.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.03.06_Judging_Test_Results.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.03.07_Logging_Data.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.03.08_Executing_a_Transition_Search.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.03.09_A_dynamic_analog_test_example.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.04_ADC_Tests.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.05_DAC_Tests.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.06_Test_method_for_ADC_test.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.07_Test_method_for_DAC_test.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.08_Accessing_Test_Control_Options.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.09_Computing_Measurement_Values.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.10_Executing_Firmware_Commands.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.11_Controlling_GPIB_Instruments.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.12_Controlling_sequencer_status.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.13_Controlling_Multiple_Sites.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.14_Controlling_Multi-port_Test.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.14.02.04_Pass_fail_judgment_of_test_method_based_test_suite_in_a_testflow.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.15_Data_display_API_use_cases.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.16_Programming_Tips.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.17_How_to_handle_the_API_fatal_errors.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.18_X-mode_cycles_versus_tester_cycles.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.19_tmm_console.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.20_Uploading_results_with_TMU_TASK_and_TMU_PINS.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.03.21_Printing_tester_status.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04_API_Reference.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01_APIs_in_alphabetical_order.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.02_Test_method_specific_data_types_and_variables.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.03_Encoding_Decoding_Table_for_A-Law__-Law.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.04_Code_Format_Tables.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.05_Window_functions.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.02_addLimit.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.03_addParameter.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.126_LIMIT.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.241_TEST.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244_TESTSET.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.250_TMLimits.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.10_BEGIN_EXTENSION.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.18_CONNECT.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.35_DIGITAL_CAPTURE_TEST.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.59_END_EXTENSION.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63_EVENT_...__DC_events_API_reference.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.65_EXECUTE_TEST.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.69_FLUSH.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.75_FUNCTIONAL_TEST.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.77_FW_TASK.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.88_GET_FUNCTIONAL_RESULT.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.92_getParameter.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.134_NB_DIGITAL_CAPTURE_END.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.135_NB_DIGITAL_CAPTURE_START.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.142_PATTERN_CONTROLLER.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.174_PUT_DATALOG.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.210_SET_EXCEPTION_HANDLER.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.212_SET_MULTIBIN.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.215_setStopSiteLoop.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.235_START_TEST.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.269_VECTOR.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.271_WAIT_TEST_DONE.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.274_WAVE_LOG.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.05_Test_Method_Library.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.05.01_AC_test_methods__ac_tml.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.05.02_DC_test_methods__dc_tml.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.05.03_DC_test_methods__multi_group_dc_tml.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.05.04_Miscellaneous_test_methods__miscellaneous_tml.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.05.05_ScanTest__scan_tml.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.05.06_SmartCalc_test_methods__smartCalc.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.05.07_TMU_test_methods__tmu_tml.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.06_Test_method_snippets_provided_with_SmarTest.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.07_Shmoo_test_method_customization.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.08_Concurrent_test_framework.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.09_d2s-framework.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.10_SmartCalc_framework.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.11_Protocol_Aware_ATE.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.12_Offline_Result_Emulation.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13_SmartRDI.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.09_TPI_Program_Routines.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.09.02_DataManager.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.09.21_HpFwTask.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14_Test_Suite_Control_API.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.01_How_to_use_the_test_suite_control_API.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02_Test_suite_control_API_reference.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01_TestsuiteProxy.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.11.03.03_Variable_access_API.htm
  - 02_System_reference/02.15_SmartShell/02.15_SmartShell.htm
  - 02_System_reference/02.10_Data_Logging/02.10.01.08.01.01_Generating_test_numbers_from_the_SmarTest_GUI.htm
  - 02_System_reference/02.10_Data_Logging/02.10.01.08.01.01.03_Saving_test_numbers_as_TMLimits_CSV_files.htm
  - 02_System_reference/02.10_Data_Logging/02.10.01.08.01.01.03.01_Structure_of_a_TMLimits_CSV_file.htm
created: 2026-11-12
updated: 2026-11-12
verified: doc-only
---

# Test Method / 测试方法（Test Instance）

> 把 Pin / Level / Timing / Pattern 准备好的 primaries 变成一段可执行的 C++ 测量与判定程序，并让测试套件拿到 pass/fail 与测量数据。

## 目的

**文档事实。** Test method 是「用 test method API 写成的标准或定制 C++ 测试程序」；test method API 是标准 C++ 的扩展函数，用来测量 DUT 输出、取回测量数据、分析数据、判定 pass/fail（`01.06.01`）。Test method program 的主要任务是执行 AC 或 DC 测试，典型五步是：修改/设置 setup 数据 → 执行测试 → 取回原始测量数据 → 计算 → 判定结果（`02.07.01.01.01`）。

**文档事实（UTM）。** Universal test method（UTM）是自 SmarTest 6.3 起的编程风格与环境：一个标准 C++ 工程，独立于任何 device project 与 Eclipse project（`01.06.01`）。它带来四点：参数与限值可在测试方法代码里改而不使既有 testflow 文件失效；测试方法库可作为一个 shared library 分发；工程源码可读可改，除源文件外只有两个构建/工程文件；SmarTest 自带预编译库可直接使用（`02.07.02.01`）。

**文档事实（与 testflow 的边界）。** 在 Testflow Editor 的 Test Suites 页面里，测试套件选用一个 test method program 和 primaries（timing/level-related primaries、primary analog set、start label）。Testflow 执行时，primaries 自动下载并在每个测试套件开始时自动设定，所以测试方法程序不必描述 primaries；它只改需要改的部分，执行 API 会把改动反映到硬件。测试方法程序按判定结果把测试套件的 pass/fail 返回 Testflow，因此 Run & Branch 型测试套件可据此分支（`02.07.01.01`）。

**关于「Test Instance」这个名称（文档事实 + 本次检索结论）。** 本次检索 `docs.jsonl` 的标题/heading/first_para，并在 `tdc-html/raw` 全文搜索 `test instance`，没有找到以「Test Instance」为标题、章节或正文概念的文档；命中的两篇分别讲 `VCAT` 向量连接和 Switch version tool，与本阶段无关。文档实际用「test suite 选中一个 test method + primaries + parameter/limit 值」来表达其它 ATE 常说的 test instance（`02.07.01.01`、`02.07.02.02.03`）。因此本页正文按文档术语写 **test method / test suite**，不把 Test Instance 当成文档事实。

**推断：** testmethod 处在 `pattern → testmethod → testflow` 之间：[[pattern]] / [[timing]] / [[level]] 提供 primaries，test method 负责执行、取数、计算和 pass/fail 判定，[[testflow]] 负责把多个测试套件、bin 和分支组装起来。文档没有把这条链写成 stage 链；这一读法来自 `01.07` 的章节顺序和 `02.07.02.02.03` 的建 testflow 步骤，是本次归纳。

**建议：** 新代码优先用 `TESTSET` 的 judgeAndLog 系列，而不是旧的 `TEST`。文档明确写 judgeAndLog APIs「replace the existing TEST APIs for improved usability」，并说 `TEST` 只为向后兼容保留、未来版本可能移除（`02.07.04.01.241`）。这是建议，不是本阶段必须完成的步骤。

## 前置条件

1. **Device directory / device project 已存在。** UTM 工程默认与 device 目录同级，且「A universal test method project directory must be outside of any device directory and any Eclipse project directory」（`02.07.02.01`、`02.07.02.02.01`）。见 [[project]]。
2. **SmarTest 6.3 或更高。** UTM 自 6.3 起提供（`01.06.01`、`02.07.02.01`）；建工程、建类、建 testflow 的 `Before you begin` 都重复这一条（`02.07.02.02.01`、`02.07.02.02.02`、`02.07.02.02.03`）。
3. **Device primary setups 已就绪。** 建 UTM 工程的 `Before you begin` 写「the device primary setups are ready to use」（`02.07.02.02.01`）；测试方法默认使用 Testsuite dialog 里指定的 primaries（`02.07.01.01.01`）。**推断：** primaries 由 pin/level/timing/pattern 配置产生，因此按流程顺序要求 [[pin]]、[[level]]、[[timing]]、[[pattern]] 先完成；文档只写「primary setups ready」，没有逐阶段列出。
4. **C/C++ perspective 已打开。** 建工程的第 1 步是 `Window > Open Perspective > Other` 后双击 `C/C++`（`02.07.02.02.01`）；1.06 教程也先要求打开 C/C++ perspective（`01.06.02.01`）。
5. **要执行/调试时，testflow 已存在。** 调试页的 `Before you begin` 要求「A testflow using the test method must be ready for execution」（`02.07.02.02.04`）；建 testflow 页要求 UTM library 已可用（`02.07.02.02.03`）。见 [[testflow]]。
6. **库要共享给其他用户时，先确认 bug free。** 「If your test method libraries are bug free and ready to use, you can share it with other users」（`02.07.02.03`）。
7. **外部 C/C++ 库必须命名为 `libxxx.so`**，并放在 preload 目录：`device/testmethod/sh_lib-EL7-64bit/preload`、`/var/opt/hp93000/soc/testmethod/preload` 或 `/var/opt/hp93000/soc_common/testmethod/preload`（`02.07.02.11`、`02.07.02.01`）。
8. **转换工具只在 32-bit SmarTest 可用。** `convertUP`（用户过程 → UTM）与 `convertTestflow`（classic testflow → UTM testflow）都写明「only available in the 32-bit SmarTest」（`02.07.02.05`、`02.07.02.06`）。
9. **CCF 需要 SmarTest 6.5.4+**（`02.07.02.12`）；**从 testflow 内 `Open Test Method` 编辑需要 6.5.3+**（`02.07.02.10`）。
10. **用 `TMLimits` 时，CSV 必须符合规定列结构，且必须在 `SMC_ARM()` 之前 load。** 文档 CAUTION：「You must not change or reload a TMLimits table while an SMC background process is armed or running.」（`02.07.04.01.250`、`02.10.01.08.01.01.03.01`）。

## 涉及对象

| 对象 | 层级 | 在本阶段做什么 | 出处 |
|---|---|---|---|
| test method class（`.cpp`，可选 `.h`） | file | 测试方法源文件；实现 `initialize()` / `run()` / 可选 `postParameterChange()` / `getComment()` | `02.07.02.01`、`02.07.02.02.02` |
| universal test method project | file | 纯 C++ 工程；生成 `.project`、`.cproject` 与 `Debug/` | `02.07.02.01`、`02.07.02.02.01` |
| UTM library（`lib<Project>.so`） | file | 构建产物；plain C++ shared library，供 testflow/device 引用 | `02.07.02.01`、`02.07.02.02.02` |
| `testmethod.hpp` | file | 声明 `addParameter` / `addLimit` 的头文件 | `02.07.04.01.02`、`02.07.04.01.03` |
| `TestControl.h` | file | 声明 `TEST` 的头文件 | `02.07.04.01.241` |
| `Limit.h` | file | 声明 `LIMIT` 类的头文件 | `02.07.04.01.126` |
| Test Method API | L2 | 执行测量、取数、计算、判定的 C++ API 总称 | `02.07.01.01`、`02.07.03.01.08` |
| UTM executor（两个进程） | L2 | 运行 test method API 程序；第一个用于生产与调试，第二个用于工程调试/Shmoo | `02.07.02.01.01` |
| `tmm_console` | L2 | 从测试方法执行器 shared memory 取信息、停执行器、列/转储可用测试方法 | `02.07.03.19` |
| Testflow Editor / Properties view | gui | 选 test method、设 primaries、改 parameter/limit 值；显示 pass/fail | `02.07.01.01`、`02.07.02.02.03` |
| `addParameter` / `addLimit` | L2 | 在 `initialize()` 里定义参数与限值接口 | `02.07.04.01.03`、`02.07.04.01.02` |
| `TEST` / `TESTSET` | L2 | 判定 pass/fail 并写 event data log；`TESTSET` 的 judgeAndLog 是推荐替代 | `02.07.04.01.241`、`02.07.04.01.244` |
| `LIMIT` / `TMLimits` | L2 | 程序内限值对象 / CSV 外部限值与 test number | `02.07.04.01.126`、`02.07.04.01.250` |
| `FW_TASK` / `BEGIN_EXTENSION` / `END_EXTENSION` | L2 | 在 test method 里直接执行 firmware command | `02.07.03.10` |
| `TestsuiteProxy` | L3 | 测试套件外部控制：attach test method、读写参数/限值、执行、取 pass | `02.09.01.14.02.01` |
| `HpFwTask` | L3 | 从 C 程序直接访问系统硬件 firmware 层（不自动处理 site focus） | `02.09.01.09.21` |
| TMLimits CSV | file | 外部限值与 test number 表；由 `TMLimits::load()` 读入 | `02.10.01.08.01.01.03.01` |
| Test method snippets XML | file | EWC C/C++ Templates 使用的代码片段集 | `02.07.06`、`02.07.02.09` |
| 预定义 Test Method Libraries | L2 | `ac_tml`、`dc_tml`、`multi_group_dc_tml`、`miscellaneous_tml`、`scan_tml`、`smartCalc`、`tmu_tml` | `02.07.05` |
| Concurrent Test Framework（CCF） | L2 | 把多个独立测试组合成一次并发执行 | `02.07.08` |
| d2s-framework | L2 | dynamic-to-static，自动生成静态 vector label | `02.07.09` |
| SmartCalc（SMC） | L2 | 把耗时的计算/上传放到后台线程 | `02.07.10` |
| Protocol Aware ATE | L2 | transaction based protocol testing | `02.07.11` |
| Offline Result Emulation（ORE） | L2 | 无器件时仿真测试/测量结果 | `02.07.12` |
| SmartRDI | L2 | 在 test method 里直接做 DC/digital capture/protocol 编程的 RDI 接口 | `02.07.13` |

### 归属判定

> 以下是判断，不是文档事实，供维护者复核。

- **`01.06` 全章判给本页。** 它是本阶段的定义文档：`01.06.01` 定义 test method / UTM，`01.06.02` 给出从建工程到建库的四步教程。
- **`02.07` 全章判给本页 L2。** 包括 `02.07.05` 测试方法库、`02.07.06` snippets、`02.07.07` Shmoo 定制、`02.07.08` CCF、`02.07.09` d2s、`02.07.10` SmartCalc、`02.07.11` PAT、`02.07.12` ORE、`02.07.13` SmartRDI。它们是 test method 生态的一部分；其中若干子框架横跨 [[pattern]] / [[timing]] / [[results]]，本页按「最近的一段」放在此处，不代表它们只属于本阶段。
- **`02.07.04.01` 的 274 个 API 顶层条目与 1016 个子页判给本页 L2。** 本页不逐条抄 1290 篇，而是给出生命周期索引 + 类别号；完整字母表以 `02.07.04.01_APIs_in_alphabetical_order` 为准（该页列出全部条目）。这样「页面没写」和「源里没有」可由该索引区分。
- **Testflow 侧的测试套件选择、参数/限值编辑判给 [[testflow]]。** `02.08.04.32`（Testflow Tool）里的 Testsuite dialog / Parameters page / Tests page / Testflow Properties view 不复制到本页；本页只说明 test method 怎样暴露参数与限值。
- **`02.10` 的 event data logging / report formatter 判给 [[results]]。** 本页只写 test method 侧写日志的 API（`TEST`、`PUT_DATALOG`、`WAVE_LOG`）与开关条件。
- **`02.06` 任何命令章都不判给本页 L1。** 本次检索未发现以 test method / test suite 为对象的 firmware 命令子树；test method 的 firmware 访问入口是 L2 的 `FW_TASK`（`02.07.03.10`），不是本阶段 L1。
- **`02.09.01.14` TestsuiteProxy 判给本页 L3**，只引用 test method 相关成员；`02.09.01.09` 的 `HpFwTask` 作为 firmware 层的横切入口引用。
- **`02.15` SmartShell 不判给本页 L3。** 该章 `Functional changes` 明写 `Introduced in SmarTest 8.2.5`，而本 wiki 面向 7.10.3；正文只有 PDF 外链（`02.15`）。
- **`02.07.13` SmartRDI 是 L2，不是 L3。** 它是 test method 里的 C++ RDI 接口，属于测试方法编程；不要因为它名字里有 RDI 就当成外部控制层。

### 名称对照

| 文档里的名字 | 含义 | 出处 |
|---|---|---|
| test method | 用 test method API 写的 C++ 测试程序 | `01.06.01` |
| test method program | 同上，强调是一段可执行程序 | `02.07.01.01` |
| universal test method（UTM） | 自 SmarTest 6.3 起的标准 C++ 工程式测试方法 | `01.06.01`、`02.07.02.01` |
| classic test method | UTM 之前的测试方法；可转换到 UTM 环境 | `02.07.02.04`、`02.07.02.06` |
| test suite | testflow 里「test method + primaries + parameter/limit 值」的实例 | `02.07.01.01`、`02.07.02.02.03` |
| Test Instance | 本次未在语料中找到该术语；按文档应读作 test suite | 本次检索结论 |

## L1 — Firmware / Setup Command

**文档未覆盖。**

**为什么是「文档未覆盖」而不是漏写（检索记录）。** 本次检查了 `02.06` Command Reference 的 18 个章（`02.06.01`–`02.06.18`）与 `02.06.02` 命令字母索引，没有发现以 test method、test suite 或 test instance 为对象的命令子树。Test method 的选择、参数值与限值写入属于 testflow 文件/Testflow Tool（`02.07.01.01`、`02.07.02.02.03`），不通过某个本阶段专属 firmware 命令完成。

**文档事实（firmware 访问的唯一入口在本阶段是 L2 而不是 L1）。** Test method 可以在程序里执行 firmware command，但入口是 C++ API：`FW_TASK` 执行 firmware command 并接回输出，`BEGIN_EXTENSION`/`END_EXTENSION` 声明一个可以在 firmware 层访问系统硬件或 MCD 的块（`02.07.03.10`）。示例中的 `DFCM`、`PTST?` 是 firmware command 本身，但它们由 `FW_TASK` 调用，不是本阶段的独立命令页。因此它们列在 L2，不伪造成 L1 子树。

**同形陷阱。** `02.07.03.12` 在讲 sequencer 控制时同时给了 `Sequencer.reset()`（L2 API）与 `FW_TASK("SQGB ACQF,0;")`（经 L2 调用的 firmware 命令）两种写法；`SQGB` 属于 sequencer/vector 阶段，不是本阶段 L1。不要因为示例里出现 firmware command 就把它写成本阶段命令。

## L2 — Test Method API

**文档事实（总览）。** 本阶段的核心材料是 `02.07_Test_Method_Reference`，共 13 章。API 有两种形态：函数型（C 函数风格，如 `DSP_FFT(source_array, result_array, window);`）与 C++ 类类型（可链式调用成员函数，如 `ANALOG(1).DGT("Vout").vOffset(0.5 V).vRange("6");`）（`02.07.03.01.08`）。

### 章节结构（`02.07`，13 章）

| 章 | 分类号 | 内容 | 主要子节（分类号） |
|---|---|---|---|
| Introduction | `02.07.01` | 测试流程与 API 总览 | `02.07.01.01` Test Method Program Introduction；`.01.01` Testing flow and Test Method API；`.01.02` Code-based and pattern-based programming（7.10.2 引入） |
| Universal Test Method | `02.07.02` | UTM 概念、工程、库、参数类型 | `.01` concept（含 `.01.01` executor）；`.02` developing library（`.02.01` 建工程、`.02.02` 建类、`.02.03` 建并执行 testflow、`.02.04` 调试、`.02.05` Cppcheck、`.02.06` valgrind、`.02.07` callgrind、`.02.08` 在 SmarTest 外开发）；`.03` 管理库（`.03.01` 系统级安装、`.03.02` 多目录、`.03.03` 库间调用）；`.04` classic TM 在 UTM 环境（`.04.01` 工程转换、`.04.02` 导入、`.04.03` 不完整 classic TM 转换）；`.05` 用户过程转换（`.05.01`）；`.06` classic testflow 转换（`.06.01`）；`.07` 预定义 UTM 库；`.08` 预定义 UTM 清单；`.09` snippets（`.09.01`–`.09.05`）；`.10` 从 testflow 编辑；`.11` 外部 C/C++ 库（`.11.01` modern C++）；`.12` CCF 开发（`.12.01`、`.12.02`）；`.13` 参数类型（`.13.01`–`.13.05`） |
| Test Method Programming Essentials | `02.07.03` | 编程要点与各类测试写法 | `.01` 编程前要点（`.01.01` 语言、`.01.02` 单位、`.01.03` 数据类型、`.01.04` STRING、`.01.05` COMPLEX、`.01.06` ARRAY_x、`.01.07` 数学常量、`.01.08` API 风格）；`.02` DC 测试编程（`.02.01` Flex DC、`.02.02` DC Test Programming with PPMU、`.02.03` Direct DMM high-accuracy voltage measurements via utility pogo block、`.02.04` DC test programming with DPS、`.02.05` Setting up DC Connection for Analog Pin、`.02.06` DC Test Methods, DC Sets, and Measurement Sets、`.02.07` Executing PPMU tests from a pattern、`.02.08` Per Pin PMU、`.02.09` Miscellaneous Considerations for DC tests）；`.03` AC 测试编程（`.03.01` Using Setup APIs for AC test、`.03.02` Changing and obtaining digital settings、`.03.03` Setting up Routing Connections、`.03.04` Executing an AC Test、`.03.05` Retrieving AC Test Results、`.03.06` Judging Test Results、`.03.07` Logging Data、`.03.08` Executing a Transition Search、`.03.09` A dynamic analog test example）；`.04` ADC Tests（`.04.01` INL/DNL Ramp、`.04.02` INL/DNL Sine、`.04.03` Offset、`.04.04` FS Gain/LSB Gain、`.04.05` Calculation of Distortion Parameters、`.04.06` Encoding/Decoding Formats）；`.05` DAC Tests（`.05.01` Available Analog Modules、`.05.02` DNL、`.05.03` INL、`.05.04` Offset、`.05.05` FS Gain、`.05.06` LSB Gain、`.05.07` Gain Mismatch、`.05.08` THD、`.05.09` SND、`.05.10` SNR、`.05.11` SFDR、`.05.12` Signal、`.05.13` Signal Processing）；`.06` ADC test method；`.07` DAC test method；`.08` 测试控制选项（`.08.01`–`.08.11`）；`.09` 计算测量值；`.10` 执行 firmware commands；`.11` GPIB 仪器；`.12` sequencer 状态；`.13` 多 site（`.13.01`–`.13.10`）；`.14` 多 port（`.14.01`、`.14.02`）；`.15` 数据展示 API 用例（`.15.01`–`.15.03`）；`.16` 编程技巧（`.16.01`–`.16.03`）；`.17` API fatal errors（`.17.01`、`.17.02`）；`.18` X-mode vs tester cycles；`.19` `tmm_console`；`.20` TMU_TASK/TMU_PINS 上传结果；`.21` 打印 tester status（`.21.01`–`.21.03`） |
| API Reference | `02.07.04` | 全部 API、数据类型、编码表、窗函数 | `.01` 字母序 API（274 个顶层条目 + 1016 子页）；`.02` test method 专用数据类型（`.02.01` ARRAY_I、`.02.02` ARRAY_D、`.02.03` ARRAY_COMPLEX、`.02.04` ARRAY_CHAR、`.02.05` ARRAY_BOOL、`.02.06` ARRAY_LL、`.02.07` COMPLEX、`.02.08` CYCLE_CHUNK、`.02.09` DOUBLE_VECTOR、`.02.10` FileString、`.02.11` INT_VECTOR、`.02.12` OptionList、`.02.13` SpecVariable、`.02.14` SpecValue、`.02.15` STRING_VECTOR、`.02.16` TestMethodParameterProxy、`.02.17` TimingSetSelector、`.02.18` Macros to get the SmarTest version number）；`.03` A-law/µ-law 编解码表；`.04` code format tables；`.05` window functions |
| Test Method Library | `02.07.05` | SmarTest 自带测试方法库 | `.01` `ac_tml`；`.02` `dc_tml`；`.03` `multi_group_dc_tml`；`.04` `miscellaneous_tml`；`.05` `scan_tml`；`.06` `smartCalc`；`.07` `tmu_tml` |
| Test method snippets | `02.07.06` | 自带代码片段 | `.01` DC templates；`.02` ADC；`.03` DAC；`.04` CODEC；`.05` baseband→RF；`.06` RF→baseband；`.07` RF→RF；`.08` Miscellaneous |
| Shmoo test method customization | `02.07.07` | 定制 Shmoo 测试方法 | `.01` Creating；`.02` Customized shmoo test template（`.02.01` 函数说明）；`.03` 在 Shmoo Tool 看定制结果；`.04` source-sync shmoo |
| Concurrent test framework | `02.07.08` | CCF 概念、模板、参数、API、指南 | `.01` CCF-ISR mode；`.02` Merging the setups；`.03` CCF test method template；`.04` Test method parameters；`.05` Testflow variables；`.06` CCF APIs；`.07` Guidelines |
| d2s-framework | `02.07.09` | dynamic-to-static | `.01` Introduction；`.02` d2s feature set；`.03` d2s modes；`.04` serial protocol 实现（`.04.01`–`.04.04`） |
| SmartCalc framework | `02.07.10` | 后台线程计算/上传 | `.01` multithreading basics；`.02` considerations（`.02.01`–`.02.02`）；`.03` use models（`.03.01`–`.03.03`）；`.04` implementation（`.04.01`–`.04.12`）；`.05` recommendations |
| Protocol Aware ATE | `02.07.11` | transaction based protocol testing | `.01`（`.01.01`–`.01.12`，含 license、API、device setup、equation system、multisite、datalog、SmartCalc、术语、同步、encode/decode、SLIMbus） |
| Offline Result Emulation | `02.07.12` | 无器件时仿真结果 | `.01` pre-silicon workflow；`.02` concept；`.03` test program requirements；`.04` configuration API（`.04.01`–`.04.03`）；`.05` setup file（`.05.01`）；`.06` examples（`.06.01`–`.06.03`） |
| SmartRDI | `02.07.13` | test method 内的 RDI 编程 | `.01` release info；`.02` install/use；`.03` RDI；`.04` RDI_Configure；`.05` code structure；`.06` RDI_INFO_LEVEL；`.07` 函数字母序；`.08` general topics；`.09` alarm；`.10` d2s-like protocol；`.11` DC AWG/DGT；`.12` DC test setup；`.13` digital capture；`.14` relay control；`.15` Routing Tools；`.16` error map；`.17` functional test；`.18` level/timing set changes；`.19` cogo；`.20` testflow burst/concurrency；`.21` TMU；`.22` tool functions；`.23` utility lines；`.24` vector/protocol programming |

**说明。** 上表只到「章 → 主要子节」。`02.07.04.01` 的 274 个顶层 API 与 `02.07.13` 的数百个函数不逐条展开；它们的完整叶子清单由各自章节页列出，分类号可直接定位。本页在「生命周期相关 API 索引」里另给出一条最小可用的生命周期 API 集。

### 生命周期一：定义（工程、类、四个成员函数）

**文档事实（工程）。** UTM project 是纯 C++ 工程，独立于所有 device；建工程时在工程目录下生成 `.project`（Eclipse 工程描述）与 `.cproject`（构建设置：源码/库搜索路径、依赖库、编译选项）（`02.07.02.01`）。工程名默认是「device name + `_tml`」；device 名里的点会换成下划线，工程名不得含点；工程名同时是目录名与 shared library 的基础名，例如 `MyTMLib` → `libMyTMLib.so`，库名除 `.so` 外不得含点（`02.07.02.02.01`）。1.06 教程里默认工程名示例是 `act299_tml`（`01.06.02.01`）。

**文档事实（类）。** Test method class 是 C++ 类实现文件，固定包含下列成员函数（`02.07.02.01`）：

| 成员函数 | 作用 | 调用时机 |
|---|---|---|
| `initialize()` | 定义对 testflow 暴露的参数与限值接口；只能用 `addParameter()` 与 `addLimit()`，其它 test method API 不能用 | testflow 打开或新增 test method 时一次；已加载 test method 被修改并重编译时一次；运行时每个 test suite 开始时一次；loop testflow 时只在第一次迭代调用；loop 单个 test suite 时每次迭代都调用；第一次运行 loop testflow 时，被 bypass 的 test suite 也会调用 |
| `run()` | 定义测试设置与测量；`addParameter()`/`addLimit()` 之外的 test method API 只能在这里用 | 每个 test suite 执行期间，对每个 active site 调用一次；每次调用前 SmarTest 会把参数重置为默认值 |
| `postParameterChange(const std::string&)` | 可选；参数值改变后的自定义检查 | testflow 打开/新增 test method 时一次；运行时由 `getParameter(...)` 或 `setValueAsString(...)` 改参数时；每个 test suite 开始时对每个已定义参数调用；由 `initialize()` 调用两次（一次设默认值，一次设 Parameters page / Properties view 的值）。此函数内不能用 test method API |
| `getComment()` | 返回 test method class 的注释 | `New Run Node Wizard` 的 `Select Test Method` 对话框打开并选中测试方法时；注释显示在对话框的 Info 区 |

**文档事实（调用限制）。** 参数定义顺序很重要：从外部改参数值时按 `initialize()` 中的定义顺序生效，Properties view 也按该顺序显示（`02.07.02.01`）。`run()` 不能调用另一个 test method，但可以调用自己的 C/C++ 函数（`02.07.02.01`、`02.07.02.11`）。若不需要 per-site 设置/结果处理，可用 `setStopSiteLoop()` 让后续 site 的 `run()` 不再执行以省测试时间（`02.07.02.01`、`02.07.04.01.215`）。

**文档事实（1.06 最小可用示例）。** 教程建 `PspecSearch` 类后在 `initialize()` 里加限值，在 `run()` 里做 `SEARCH_FUNC_TASK` 测量并判定（`01.06.02.02`、`01.06.02.03`）：

```
// Declare V93000 variables
SEARCH_FUNC_TASK tSearch;
CONNECT(); // Connect, if tester is disconnected

ON_FIRST_INVOCATION_BEGIN();
// Define measurement sequence and execute test
tSearch.pin(mSPinList).spec(mSSpecVariableName.mName,mSSpecVariableName.mType).method(mSSearchType).start(mDxStart)
.stop(mDxStop).stepWidth(mDxStep).resolution(mDxRes).resultPins(mSResultPins);

// Execute measurement
tSearch.execute();
ON_FIRST_INVOCATION_END();

//judge and log the test results
if (tSearch.getPassFail() == TRUE)
{
// Check for valid measurement results & datalog
TEST(mSPinList,"limit",tSearch.getPassValue(mSPinList));
}
```

对应的 `initialize()` 一行是 `addLimit("limit");`（`01.06.02.03`）。

### 生命周期二：参数（`addParameter`）

**文档事实（语法）。** `addParameter` 在 `initialize()` 内使用，语法为 `addParameter("parameterIdentifier","parameterType", &pValueObject, const TmParameterMode mode = TM_PARAMETER_INPUT).function1().function2()...`；定义在 `/opt/hp93000/soc/testmethod/include/testmethod.hpp`。`mode` 可取 `TM_PARAMETER_INPUT` 或 `TM_PARAMETER_OUTPUT`。返回 `TestMethodParameterProxy` 引用，因此可链式调用 `setDefault()`、`setOptions()`、`setComment()` 等（`02.07.04.01.03`、`02.07.02.13.05`）。

**文档事实（示例）。**

```
protected:
double mVoltage;

virtual void initialize()
{
addParameter("param1","double",&mVoltage,testmethod::TM_PARAMETER_INPUT)
.setDefault("1.0")
.setOptions("0.0:1.0")
.setComment("voltage to charge");
}
```

（逐字取自 `02.07.04.01.03`。）

**文档事实（参数类型）。** `addParameter` 的 `parameterType` 文档列出 `int`、`double`、`string`、`PinString`、`SpecVariable`、`SpecValue`、`ContextPins`、`OptionList`；创建类向导还列出 `FileString`（`02.07.04.01.03`、`02.07.02.02.02`）。各类型含义：

| 类型 | 用途 | 出处 |
|---|---|---|
| `PinString` | pins、pin list 或 pin group | `02.07.04.01.03` |
| `SpecVariable` | timing/level 文件里定义的 spec 变量；值形如 `"LEV.1.fooSpec[mV]"` / `"TIM.3.barSpec@port1[A]"` | `02.07.02.13.04` |
| `SpecValue` | 带单位的值，格式 `"value[unit]"`；有 `getValue()`/`getUnit()`/`getBaseUnit()` 等成员 | `02.07.02.13.03` |
| `ContextPins` | 定义 CCF 的 `CCF_FocusedPins` 参数 | `02.07.02.02.02`、`02.07.04.01.03` |
| `OptionList` | 以逗号分隔的多个选项；本质是 `vector<string>` | `02.07.02.13.02` |
| `FileString` | 一个或多个文件名；支持 `abcde(1-3)`、`abcd(e|f)` 展开 | `02.07.02.13.01` |

**文档事实（输出参数）。** 建类向导可加输出参数 `result0`、`result1`、`result2`、`result3`；之后要增删参数可直接改源文件（`02.07.02.02.02`）。参数名支持层级：用 `.` 定义 `x.start`、`x.stop`、`x.step`、`x.scale`，在 Properties view 里显示为层级（`02.07.02.02.02`）。

**文档事实（运行时读写）。** 运行时可用 `getParameter(...)` 取参数、用 `setValueAsString(...)` 改参数，后者会触发 `postParameterChange()`（`02.07.02.01`、`02.07.02.13.05`）。

**文档事实（一致性检查）。** 新增参数后 Properties view 会变灰、Inconsistency Check 按钮启用；点该按钮按测试方法代码更新参数设置（`02.07.04.01.03`、`02.07.02.02.02`）。

### 生命周期三：限值（`addLimit` / `LIMIT` / `TMLimits`）

**文档事实（`addLimit`）。** `addLimit` 给测试方法加一个限值，默认值是 `'NA'`；实际限值必须在 tabular testflow editor 的 Limits tab 或 Properties view 里填。语法 `TestMethodLimitProxy& addLimit(const std::string& testName)`，定义在 `testmethod.hpp`（`02.07.04.01.02`）。

**文档事实（`LIMIT`）。** `LIMIT` 类保存 lower limit、upper limit 与比较算子，可构造对象并作为 `TEST` 的参数传入；`TM::Pass` / `TM::Fail` 可强制判 pass/fail。`LIMIT` 不能在 `ON_FIRST_INVOCATION` 块内使用，即使在 `FOR_EACH_SITE` 块内也不行（`02.07.04.01.126`、`02.07.04.01.241`）。

**文档事实（`TMLimits`）。** `TMLimits` 用外部 CSV 控制限值与 test numbering；同一 testflow 可在不同测试模式/阶段间切换（例如晶圆用松限值、QC 用紧限值），模式由 `load()` 选择；CSV 可脱离 SmarTest 用 Open Office Calc 或文本编辑器改。`load()` 有三种形式：无参、`load(limitfile)`、`load(limitfile, mode)`（`02.07.04.01.250`）。CSV 是标准 CSV：第一行列名，第二行 test mode，每个 test 一行；列可选但关键列必须存在（`02.10.01.08.01.01.03.01`）。

**文档事实（TMLimits 与 SMC 的约束）。** 若在 SmartCalc 框架下配合后台处理使用 `TMLimits`：必须在 `SMC_ARM()` 之前把表 load 进内存；所有需要的设置要在 SMC 后台进程 armed 之前完成；严禁在 SMC 后台进程 armed/running 时改或重 load 表，否则可能数据无效或测试方法崩溃（`02.07.04.01.250`）。

**文档事实（限值与 testflow 的边界）。** `TEST` 的 `testname` 参数指向 Properties view 里的限值；不传 `limit` 参数时就用 Properties view 的值（`02.07.04.01.241`、`02.07.03.03.06`）。

### 生命周期四：执行

**文档事实（AC 测量）。** 按测试类型选 API（`02.07.03.03.04`）：

| 测试类型 | 执行 API |
|---|---|
| AC measurement test | `EXECUTE_TEST` 或 `START_TEST` + `WAIT_TEST_DONE` |
| Digital capture test | `DIGITAL_CAPTURE_TEST`，或 `NB_DIGITAL_CAPTURE_START` + `NB_DIGITAL_CAPTURE_END` |
| Digital functional test | `FUNCTIONAL_TEST` |

**文档事实（执行细节）。** `EXECUTE_TEST(...)` 启动 digital sequencer 并开始测试，可设 timeout；超时后把 timeout flag 置 1 并继续下一条语句，例如 `EXECUTE_TEST(0.1 sec, &timeout_flag);`。`START_TEST()` 把 sequencer 从 `BRK` 变 `RUN`，`WAIT_TEST_DONE(timeout, &timeout_flg)` 等 digital sequencer 与所有模拟模块 sequencer（AWG 除外）停止；这一对的优点是工作站可在硬件测试期间做别的工作。若用 `EXECUTE_TEST` 跑含 digital capture 的测试，测试无法完成（`02.07.03.03.04`）。`FUNCTIONAL_TEST` 会先激活 digital primaries；若同时用模拟模块，要在 `FUNCTIONAL_TEST` 前用 `FLUSH` 激活 primary analog set 与 routing connections（`02.07.03.03.04`）。

**文档事实（DC）。** DC 测试先按资源类型用 Setup APIs 设好测量条件，再执行并取结果；文档建议用 FlexDC APIs 以节省测试时间（`02.07.03.02`）。DC test 分两部分：定义测量参数、执行测试并取回结果；DC set / measurement set 用于避免循环里重复定义和下载（`02.07.03.02.06`）。PPMU、DPS、Flex DC、Per Pin PMU、从 pattern 执行 PPMU 各有专页（`02.07.03.02.02`–`.02.08`）。

**文档事实（代码型 vs 图案型）。** Code-based programming 由工作站直接控制硬件（也称 static programming）；pattern-based programming 由 pattern-sequencer 控制硬件（也称 sequencer-controlled / dynamic programming），时序更稳定。DC Scale 卡用 `EVENT...` API 定义 DC event，并用 `PATTERN_CONTROLLER` 或 Pattern Editor 插入现有 pattern。并非所有 code-based 可控功能都能在 pattern-based 里用（`02.07.01.01.02`）。该篇标注 `Introduced in SmarTest 7.10.2`。

**文档事实（连接与路由）。** AC 测试前必须执行 `CONNECT` 序列给 DUT 上电并把目标 pin 接到 tester 资源（`02.07.03.03`）；模拟模块连接/utility line 用 `ROUTING_STATUS` 设置，可逐 pin 设置后 `FLUSH()`，也可用已备好的 routing set（`02.07.03.03.03`）。

**文档事实（sequencer 状态）。** 可用 `SEQUENCER_STATUS`（`Sequencer` 对象）或 firmware `SQGB` 控制 sequencer 状态，例如 `Sequencer.reset();` 或 `FW_TASK("SQGB ACQF,0;")`；DC 测试方法库在测量后不 clear sequencer，因为会影响 result tools / result firmware commands（`02.07.03.12`）。

**文档事实（在 test method 里执行 firmware command）。** 用 `FW_TASK`、`BEGIN_EXTENSION`、`END_EXTENSION`；例子：

```
STRING dfcm("DFCM 1,4000,50,-1.0,1.00,4000,5,NGNG,(CP)\n");
STRING ptstq("PTST? 1,NONE,CVAL\n");

BEGIN_EXTENSION();
FW_TASK(dfcm);
STRING answer;
FW_TASK(ptstq, answer);
:
:
END_EXTENSION();
```

（逐字取自 `02.07.03.10`。）进入 extension block 前应先 `FLUSH`，因为 `ANALOG`、`ANALOG_STATUS`、`PRIMARY_STATUS`、`ROUTING_STATUS` 的 setup data 存在缓存里，`FLUSH` 才把它们下载到硬件/MCD；extension block 内的缓存机制会被系统临时关闭以避免冲突（`02.07.03.10`）。

**文档事实（test control）。** `02.07.03.08` 提供：DC 测试前应用指定 vector、返回测试运行状态、中止测试、等待时间、设置/读取 testflow 变量、设置/读取 flag、取当前运行 testsuite 名、控制错误信息输出、把模拟波形送给 Signal Analyzer（`.08.01`–`.08.11`）。

**文档事实（多 site / 多 port）。** 多 site 需设 `Parallel Mode Enable` testflow flag 与 `Allow Parallel` test suite flag（`02.07.03.13`）；多 port 用 `DIGITAL_CAPTURE_TEST` / `NB_DIGITAL_CAPTURE_*` / `FUNCTIONAL_TEST`，capture pin 参与时必须用 digital capture 系列，否则用 `FUNCTIONAL_TEST`（`02.07.03.14`）。

### 生命周期五：结果处理（取回 / 计算 / 判定 / 记录）

**文档事实（取回原始数据）。** 按数据类型选择：

| 数据 | API / 写法 | 出处 |
|---|---|---|
| 模拟波形（digitizer/sampler） | `Analog.DGT("Vout").getWaveform()`；换 analog set 时要指定测量时的 set，取数用 `ANALOG_STATUS`（`Analog` 对象） | `02.07.03.03.05.01` |
| 向量内存中的 digital capture | `VECTOR("Cap_A").getVectors(256)` → `ARRAY_I` | `02.07.03.03.05.02` |
| functional test 结果 | `GET_FUNCTIONAL_RESULT(pin)`；省略 pin 返回 global pass/fail；一般直接用 `TEST` 判定，可不调它 | `02.07.03.03.05.03` |
| DC 结果 | `PMU_IFVM` / `PMU_VFIM` / `DPS_VFIM` / `PPMU_MEASURE` / `DC_RESULT_ACCESSOR` 等对象 | `02.07.04.01.241` |
| TMU 结果 | 从 channel memory 的 result area 上传到 workstation 的 result cache；按 `TMU_TASK` 或 `TMU_PINS` 上传 | `02.07.03.20` |

**文档事实（计算）。** Computation APIs 覆盖从数组加减到 ADC 线性度等应用计算；例如复数运算 `DSP_ADD_C`、`DSP_SUB_C`、`DSP_MUL_C`、`DSP_DIV_C`，以及数据转换、DSP 滤波、FFT、统计等（`02.07.03.09`）。完整 `DSP_*` 家族在 `02.07.04.01.53.*`。

**文档事实（判定）。** `TEST(...)` 接收测试结果，在限值范围内返回 `TRUE`；`testname` 指向 Properties view 里的限值。默认 `continue = FALSE`：`TEST` 判 fail 会终止测试方法程序执行；要无论结果都继续，传 `continue` 参数。多 site 时有一个特殊行为：**第一个 site 即使 `TEST` 返回 FAIL 且 `continue = FALSE` 也会继续**，后续 site 才会终止。连续多次 `TEST` 的最终结果是所有调用的逻辑 AND（任一次 FAIL 则整体 FAIL）。可用 `TEST ("","",TM::Fail,0)` 强制 fail、`TEST ("","",TM::Pass,0)` 强制 pass（`02.07.04.01.241`）。`TEST` 不能在 first-invocation block 内使用，即使在「each site」循环块内也不行（`02.07.04.01.241`）。

**文档事实（新接口）。** `TESTSET` 的 judgeAndLog 系列（`judgeAndLog_FunctionalTest`、`judgeAndLog_ParametricTest`、`judgeAndLog_PmuIfvm`、`judgeAndLog_PmuVfim`、`judgeAndLog_PpmuMeasure`、`judgeAndLog_Dps`、`judgeAndLog_DpsVfim`、`judgeAndLog_SpecSearch`、`judgeAndLog_DcResultAccessor`、`judgeAndLog_ScanTest`、`judgeAndLog_PptiaTask`、`judgeAndLog_Spmu` 等）取代旧 `TEST`，文档建议使用（`02.07.04.01.241`、`02.07.04.01.244`）。

**文档事实（可靠性标记）。** `TEST` 的 `reliability` 参数可取 `TM::RELIABLE` / `TM::UNRELIABLE`，用于在 event data log 里标记结果不可靠；省略等同于 `TM::RELIABLE`，但 `TM::RELIABLE` 不会写日志。若结果要转成 STDF，`pin` 必须是已定义的 pin 名；可把 `Check Testmethod API` flag 设为 on，使非法 pin 名在运行时直接 fatal error（`02.07.04.01.241`）。

**文档事实（日志）。** 测试方法型测试套件在执行 `TEST` 与 `PUT_DATALOG` 时做 event data logging。默认关闭；要开启须把 system flag `log_events_enable` 设为 `on`，并把 test suite flag `output_on_pass` 或 `output_on_fail` 设为 `on`；报告器要选 `EventFormatter`。`PUT_DATALOG` 还能输出 `WAVE_LOG` 对象里的数组/带 caption 的模拟波形（`02.07.03.03.07`、`02.07.04.01.241`、`02.07.04.01.274`）。

**文档事实（测试套件级 pass/fail）。** 一个测试套件里若所有 `TEST` 都判 pass，则 testflow 里该测试套件按 pass 处理（多 port 也一样）；任一 `TEST` 判 fail，则该测试套件按 fail 处理（`02.07.03.14.02.04`）。

### 生命周期六：执行器、调试、库

**文档事实（两个执行器）。** UTM 有两个 test method executor 进程。第一个用于生产模式 testflow 执行，也用于测试方法调试；UTM Debugger 总是 attach 第一个。执行 UTM testflow 时若第一个未运行会启动；testflow 执行结束后**不会终止**，所以 UTM 代码里的 global/static 变量下次运行不会重新初始化；要每次运行前重置，可在 testflow 里插入 `initialize` 或 `download` 型 special test suite，用一个 test method 重新初始化全局变量/对象（`02.07.02.01.01`）。第二个执行器用于测试工程：当第一个被断点阻塞时，要执行单个测试套件或跑 Shmoo Tool 就用它；需在 `Window > Preferences > Advantest V93000 > Testflow Tool` 勾选 `Execute selected UTM Test Method as separate process (to avoid blocking)`，否则默认用第一个（`02.07.02.01.01`）。

**文档事实（终止执行器）。** 在 SmarTest Eclipse Workcenter 用 `Run > Terminate Test Method Execution` 或 `Project > Build All`；也可在命令行用 `/opt/hp93000/soc/testmethod/bin/tmm_console -e stopAll`（`02.07.02.01.01`）。

**文档事实（`tmm_console`）。** 位于 `/opt/hp93000/soc/testmethod/bin`；常用参数：`stopAll`（终止两个执行器）、`pid`（打印当前执行器进程号）、`list types`（列出本 device 所有可用 test method）、`dumpTimeLogger`（转储测试方法执行时间日志）、`dump types`（转储全部可用 test method 的详细信息）。支持 batch `-e <parameter>` 与交互两种方式（`02.07.03.19`）。

**文档事实（调试）。** 在 Debug perspective 调试；执行测试套件会停在第一个断点。进程启动后不会在结束后停止；若异常终止，下次执行会重新启动，此时要特别注意 testflow 变量，否则可能得到错误结果。可在 Console view 用 `p variable1` 查变量、`p testmethod_api` 执行 API 并打印返回值。暂停在断点时还可以执行另一个 UTM test suite（`02.07.02.02.04`）。

**文档事实（库搜索顺序）。** SmarTest 与 test method executor 启动时按以下顺序搜索 UTM library：① 当前 device 的 `testmethod/sh_lib-EL7-64bit`（构建 device project 时，其引用的 UTM 工程会自动构建并把 shared library 拷到这里）；② `/opt/hp93000/soc/testmethod/library/sh_lib`（预定义 `libac_tml.so`、`libdc_tml.so`、`libpptia_tml.so` 等）；③ `/var/opt/hp93000/soc/testmethod`；④ `/var/opt/hp93000/soc_common/testmethod`；⑤ `V93000_TM_LIBRARY_PATH` 定义的目录（`02.07.02.01`）。

**文档事实（外部库）。** 外部 C/C++ 库可用 preload 机制在 test method library 之前加载，名字必须是 `libxxx.so`，放在 `device/testmethod/sh_lib-EL7-64bit/preload`、`/var/opt/hp93000/soc/testmethod/preload` 或 `/var/opt/hp93000/soc_common/testmethod/preload`（`02.07.02.11`、`02.07.02.01`）。

**文档事实（snippets）。** 测试方法片段通过 EWC 的 C/C++ Templates 使用：`Window > Preferences > C/C++ > Editor > Templates`；系统自带片段从 XML 自动导入（路径见「文档内不一致」）（`02.07.02.09`）。

### 测试方法库与子框架（`02.07.05`–`02.07.13`）

**文档事实（`02.07.05` 测试方法库）。** 库是 SmarTest 自带测试方法集合，特点是尽量优化吞吐、支持 multisite、带注释、代码结构统一；结构含四个主要块（`02.07.05`）。成员如下：

| 库 | 分类号 | 成员 |
|---|---|---|
| `ac_tml` | `02.07.05.01` | `Frequency_byDigitalCapture`、`FunctionalTest`、`JitterHistogram`、`JitterSeparation`、`JitterSeparationHS`、`JitterStardust`、`ParametricFunctionalTest`、`SetBasedSpecSearch`、`Shmoo`、`SpecSearch` |
| `dc_tml` | `02.07.05.02` | `Continuity`、`DpsConnectivity`、`DpsStatus`、`DVM`、`GeneralPMU`、`HighZ`、`Leakage`、`OperatingCurrent`、`OutputDC`、`ProductionIddq`、`StandbyCurrent` |
| `multi_group_dc_tml` | `02.07.05.03` | `Continuity`、`DpsConnectivity`、`DpsStatus`、`GeneralPMU`、`Leakage`、`OperatingCurrent`、`OutputDC`、`ProductionIddq` |
| `miscellaneous_tml` | `02.07.05.04` | `Connect`、`Disconnect`、`ExecuteLinuxCommand`、`FwEscape`、`GetUtilityLines`、`SetupLevelSet0`、`SetUtilityLines`、`StartSequencer`、`TestheadTemperature`、`TestState` |
| `scan_tml` | `02.07.05.05` | `ScanTest`（章节只有一篇，未再分成员页） |
| `smartCalc` | `02.07.05.06` | `SMC__SYNCHRONIZE`、`SMC__SYNCHRONIZE_ALL`、`SMC__CLEANUP` |
| `tmu_tml` | `02.07.05.07` | `DriftEyeOpening`、`Frequency`、`Jitter (TIE)`、`PropDelay`、`PulseWidth`、`RiseFallTime` |

**文档事实（`02.07.06` snippets）。** 自带片段分 DC、ADC、DAC、CODEC、baseband→RF、RF→baseband、RF→RF 与 Miscellaneous 八类（`02.07.06`）。

**文档事实（`02.07.07` Shmoo 定制）。** 不用现成 `ac_tml.AcTest.Shmoo` 时可定制自己的 Shmoo 测试方法：保留原参数/函数、增加新参数、显示期望结果；含模板函数说明、在 Shmoo Tool 查看定制结果、source-sync Shmoo（`02.07.07`）。

**文档事实（`02.07.08` CCF）。** Concurrent test 是给 DUT 的独立 block 分配独立 port 以同时测试；CCF 把多个独立测试组合成一次并发执行，同时保持每个测试的结构（`02.07.08`）。

**文档事实（`02.07.09` d2s）。** d2s（dynamic-to-static）自动生成静态、测试时间高效的 vector label，同时保留开发期动态修改能力；6.5.4 引入（`02.07.09`）。

**文档事实（`02.07.10` SmartCalc）。** SMC 把耗时的计算与测试数据上传移到后台线程，与 SmarTest 前台进程尽量并行；multithreading basics / considerations / use models / implementation / recommendations 五节（`02.07.10`）。

**文档事实（`02.07.11` PAT）。** Protocol Aware ATE 处理 SOC 与 JTAG、MDIO、I2C 等标准宿主接口的协议通信；transaction based protocol testing 子章覆盖 license、API、device setup、equation system、multisite、datalog、术语、同步、encode/decode、SLIMbus（`02.07.11`）。

**文档事实（`02.07.12` ORE）。** ORE 在器件可用前，用用户定义的测试/测量结果做离线验证、调试与回归，不需要录制数据；按 device spec 定义要检测的 failure 类型（`02.07.12`）。

**文档事实（`02.07.13` SmartRDI）。** SmartRDI 是 test method 里的 RDI 编程接口，覆盖 DC、digital capture、protocol、TMU、error map、routing、vector 等；有按版本的 release information（含 `SmartRDI 7.10.3` 等）（`02.07.13`）。

### 生命周期相关 API 索引

**说明。** 下表是本阶段生命周期最常用的一组 API，不是全部。全部 274 个顶层 API 以 `02.07.04.01_APIs_in_alphabetical_order` 为准（该页逐条列出并带分类号）。

| 生命周期 | API / 类 | 分类号 | 一句作用 |
|---|---|---|---|
| 定义 | `addParameter` | `02.07.04.01.03` | 在 `initialize()` 定义输入/输出参数 |
| 定义 | `addLimit` | `02.07.04.01.02` | 在 `initialize()` 定义限值名（默认 `NA`） |
| 定义 | `getParameter` | `02.07.04.01.92` | 运行时读参数值 |
| 定义 | `setStopSiteLoop` | `02.07.04.01.215` | 让后续 site 不再执行 `run()` |
| 参数 | `TestMethodParameterProxy` | `02.07.02.13.05` | `addParameter`/`getParameter` 返回的代理，设默认/选项/注释/可见性 |
| 参数 | `SpecVariable` / `SpecValue` / `OptionList` / `FileString` | `02.07.02.13.04` / `.03` / `.02` / `.01` | 四类专用参数值 |
| 限值 | `LIMIT` | `02.07.04.01.126` | lower/upper/算子容器，作 `TEST` 参数 |
| 限值 | `TMLimits` | `02.07.04.01.250` | CSV 外部限值 + test number + 多模式 |
| 执行 | `EXECUTE_TEST` | `02.07.04.01.65` | 启动 sequencer 执行 AC 测量，可带 timeout |
| 执行 | `START_TEST` / `WAIT_TEST_DONE` | `02.07.04.01.235` / `.271` | 启动 / 等待 sequencer 完成，可在中间做别的工作 |
| 执行 | `DIGITAL_CAPTURE_TEST` / `NB_DIGITAL_CAPTURE_START` / `NB_DIGITAL_CAPTURE_END` | `.35` / `.135` / `.134` | digital capture 测试及其非阻塞版本 |
| 执行 | `FUNCTIONAL_TEST` | `02.07.04.01.75` | digital functional test |
| 执行 | `GET_FUNCTIONAL_RESULT` | `02.07.04.01.88` | 取最新 functional pass/fail（可按 pin） |
| 执行 | `CONNECT` | `02.07.04.01.18` | 连接 DUT、上电、接资源 |
| 执行 | `FLUSH` | `02.07.04.01.69` | 把缓存 setup 数据下载到硬件/MCD |
| 执行 | `FW_TASK` / `BEGIN_EXTENSION` / `END_EXTENSION` | `.77` / `.10` / `.59` | 在 test method 里执行 firmware command |
| 执行 | `PATTERN_CONTROLLER` / `EVENT_...` | `.142` / `.63` | pattern-based 编程与 DC event 定义 |
| 取数 | `VECTOR` | `02.07.04.01.269` | 从 vector memory 取 digital capture 数据 |
| 取数 | `ANALOG_STATUS`（`Analog` 对象） | `02.07.03.03.05.01` | 取模拟波形，需测量时的 analog set |
| 取数 | `TMU_TASK` / `TMU_PINS` | `02.07.03.20` | 把 TMU 结果上传到 result cache |
| 计算 | `DSP_*` | `02.07.04.01.53.*` | 数组/复数/滤波/FFT/统计等计算 |
| 判定 | `TEST` | `02.07.04.01.241` | 判 pass/fail 并写 event data log |
| 判定 | `TESTSET` | `02.07.04.01.244` | judgeAndLog 系列，推荐替代 `TEST` |
| 记录 | `PUT_DATALOG` / `WAVE_LOG` | `.174` / `.274` | 输出数组数据 / 构造带 caption 的波形日志对象 |
| 错误 | `SET_EXCEPTION_HANDLER` | `02.07.04.01.210` | 预置 fatal error 处理 |
| 多 bin | `SET_MULTIBIN` | `02.07.04.01.212` | soft/hard bin 多 bin 支持 |

### 文档内不一致（原样记录）

按 schema §9，以下为源文档自身的不一致，**不自行选一个当正确答案**：

1. **库搜索环境变量名。** `02.07.02.01` 写 `V93000_TM_LIBRARY_PATH`；`02.07.02.03` 写 `93000_TM_LIBRARY_PATH`。两处都指「多个目录下的 UTM library」所用的系统环境变量，但拼写不同（`02.07.02.01`、`02.07.02.03`）。
2. **snippets XML 路径三种写法。** `02.07.02.01` 写 `/opt/hp93000/soc/testmethod/library/testmethodsnippet.xml`；`02.07.02.09` 写 `/opt/hp93000/soc/segements/tml/testmethodSnipptets.xml`（`segements`、`Snipptets` 原文如此）；`02.07.06` 写 `/opt/hp93000/soc/segments/tml/testmethodSnippet.xml`（`02.07.02.01`、`02.07.02.09`、`02.07.06`）。
3. **`addParameter` 的类型清单与建类向导不一致。** `02.07.04.01.03` 的类型表列 `int`、`double`、`string`、`PinString`、`SpecVariable`、`SpecValue`、`ContextPins`、`OptionList`，不含 `FileString`；`02.07.02.02.02` 的向导类型清单含 `FileString`。`FileString` 另有独立参数类型页（`02.07.02.13.01`）。
4. **1.06 教程的默认工程名与 02.07 的命名规则不同。** `01.06.02.01` 写默认工程名 `act299_tml`；`02.07.02.02.01` 写默认是「device name + `_tml`」。前者是具体 device 的示例，后者是一般规则，本页按「示例 vs 规则」理解，不视为冲突（`01.06.02.01`、`02.07.02.02.01`）。

## L3 — 外部控制

**文档事实（结构）。** L3 入口是横切的，能力面按阶段分族。横切入口有两类：Test Suite Control API（`TestsuiteProxy`，`02.09.01.14`）与 TPI Program Routines（`02.09.01.09`）。本阶段的专属族是 **TestsuiteProxy 的 test method 成员**：

- `TestsuiteProxy.attachTestmethod()`：给测试套件 attach 一个 universal test method（`02.09.01.14.02.01.01`）。
- `TestsuiteProxy.getTestmethodName()`：取测试套件当前 test method 名（`02.09.01.14.02.01.13`）。
- `TestsuiteProxy.getTestmethodParameterNames()`：取参数名列表（`02.09.01.14.02.01.14`）。
- `TestsuiteProxy.getTestmethodParameterValue()`：取某个参数值（`02.09.01.14.02.01.15`）。
- `TestsuiteProxy.setTestmethodParameterValues()`：设置参数值（`02.09.01.14.02.01.32`）。
- `TestsuiteProxy.getTestmethodDefaultLimitNames()` / `getTestmethodUserDefinedLimitNames()`：取默认/用户自定义限值名（`02.09.01.14.02.01.11` / `.16`）。
- `TestsuiteProxy.getTestmethodLimitValue()`：取限值（`02.09.01.14.02.01.12`）。
- `TestsuiteProxy.setTestmethodLimits()`：设置限值（`02.09.01.14.02.01.31`）。
- `TestsuiteProxy.executeSiteInFocus()` / `executeActiveSites()`：执行测试套件（`.03` / `.02`）。
- `TestsuiteProxy.isExecuted()` / `isPass()`：取是否已执行 / 是否 pass（`.21` / `.23`）。
- `selectTestmethodExecutor()` / `getTestmethodExecutorIndex()`：选择/查询 test method executor（`02.09.01.14.02.10` / `.11`）。

**文档事实（Test Suite Control API 的适用范围）。** 它用于在 testflow tool 之外直接控制测试套件；只支持 UTM-based test suite；不能在 test method 编程里使用；同一客户端进程不能与 HVM API、BLC API 并行使用；需要 SmarTest 6.5.2+，程序要从 run shell（`$/opt/hp93000/soc/system/bin/run -S`）构建，包含 `testsuitecontrol_api.hpp` 并使用 `testsuitecontrol` 命名空间（`02.09.01.14`、`02.09.01.14.01`）。

**文档事实（TPI）。** `HpFwTask` 允许 C 程序在 firmware 层直接访问系统硬件，但**不自动处理 site focus**：不带 site focus 设置命令时，setup 命令作用于默认 focus（通常所有 site），result query 取默认 site（通常 site 1）的结果。它的定位与 L2 `FW_TASK` 相对：`FW_TASK` 在 test method 内执行 firmware command，`HpFwTask` 在外部 C 程序里执行（`02.09.01.09.21`、`02.07.03.10`）。TPI `DataManager` 的文件 ID 里没有 `dm_testmethod`；与本阶段相关的是 `dm_testflow`（testflow file）与 `dm_testprog`（test program）（`02.09.01.09.02`）。

**同形陷阱 / 边界。** `02.07.13` SmartRDI 名字像外部接口，实际是 test method 内的 C++ RDI API，属 L2（见「归属判定」）。HVM/BLC 的本次检索：在 `02.09.01.10`（HVM）、`02.09.01.11`（BLC）两章中，按标题与首段检索 test method / test suite，只命中 BLC 的 `Variable access API`（`GetApplicationVar`/`SetApplicationVar`）；它让外部程序（如 test method）通过 CPI 访问 application model 变量，是变量访问，不是对 test method 的 attach/参数/限值外部控制（`02.09.01.11.03.03`）。**本次未找到** HVM/BLC 中专门控制 test method 的成员；这不是「不存在」的全称断言。

**SmartShell。** 全库唯一一篇 SmartShell 总述 `02.15` 明写 `Introduced in SmarTest 8.2.5`，而本 wiki 面向 7.10.3；该章正文只有 PDF 外链，没有本阶段可用的命令语义。因此**不把 SmartShell 当作 7.10.3 的 testmethod L3 接口**（`02.15`）。

**本次未找到**：7.10.3 下用于「枚举/替换 test method 库文件本身」的外部控制接口。Test Suite Control API 能 attach test method、读写参数与限值、执行并取 pass；TPI DataManager 能操作 testflow/test program 文件；但没有找到直接管理 UTM 共享库文件的外部接口。这是检索结果，不是「不提供」的断言。

## 产物

**文档事实。**

- **UTM 工程目录**：含 `.project`（Eclipse 工程描述）与 `.cproject`（构建设置）（`02.07.02.01`、`02.07.02.02.01`）。
- **test method 源文件**：C++ class 实现文件；建类向导可勾选 `Separate Header File and Source file` 拆分头/源文件（`02.07.02.02.02`）。
- **UTM library**：构建后出现在工程目录的 `Debug/` 子目录，例如 `/home/demo/devices/act299_tml/Debug/`（`02.07.02.02.02`）；它本身是 plain C++ shared library（`02.07.02.01`）。
- **device 侧库目录**：`device/testmethod/sh_lib-EL7-64bit/`；把库拷到这里即可给该 device 的测试使用（`02.07.02.01`）。
- **系统级库目录**：`/var/opt/hp93000/soc/testmethod/sh_lib` 或 `/var/opt/hp93000/soc_common/testmethod/sh_lib`（`02.07.02.01`）。
- **preload 目录**：`.../testmethod/sh_lib-EL7-64bit/preload`、`/var/opt/hp93000/soc/testmethod/preload`、`/var/opt/hp93000/soc_common/testmethod/preload`（`02.07.02.11`、`02.07.02.01`）。
- **TMLimits CSV**：标准 CSV，两行表头（列名 + test mode）+ 每个 test 一行；由 `TMLimits::load()` 读入（`02.10.01.08.01.01.03.01`、`02.07.04.01.250`）。
- **snippets XML**：系统自带片段文件（路径三种写法见「文档内不一致」）（`02.07.02.09`、`02.07.06`）。
- **testflow 中的测试套件配置**：选中的 test method 名、primaries、parameter/limit 值。该配置落在 testflow 文件里，由 [[testflow]] 阶段生成/保存；本阶段只负责提供可被引用的库与参数/限值接口（`02.07.01.01`、`02.07.02.02.03`）。

**边界说明。** 本阶段不产出测试结果数据；测量数据、event data log、报告属于 [[results]]。本阶段也不产出 testflow 流程结构；test suite/bin/branch 属于 [[testflow]]。

## 验证

以下均为文档给出的验证入口，未自行发明。

1. **建工程后看 Results。** 文档写应在 C/C++ perspective 看到 UTM 工程文件夹，指定位置出现以工程名命名的目录，其中含 `.project` 与 `.cproject`（`02.07.02.02.01`）。
2. **建类/构建后看 Results。** 构建成功后在工程目录 `Debug/` 子目录找到 test method library；示例路径 `/home/demo/devices/act299_tml/Debug/`（`02.07.02.02.02`）。1.06 教程的构建步骤要求看 Console view 是否有错误（`01.06.02.04`）。
3. **调试后看 Results。** 文档的 Results 段写「Your test method is bug free and ready to use.」；调试中可在 Console view 用 `p variable1`、`p testmethod_api` 查值/执行并看返回（`02.07.02.02.04`）。
4. **建 testflow 后看 Results。** 文档写「The testflow is ready for execution and test method debugging.」（`02.07.02.02.03`）。
5. **`tmm_console` 查询。** `list types` 列出本 device 所有可用 test method；`dump types` 转储全部可用 test method 的详细信息；`pid` 打印当前执行器进程号；`dumpTimeLogger` 转储执行时间日志（`02.07.03.19`）。
6. **Properties view 一致性。** 增删参数并重编译后，打开该测试套件的 Properties view，若显示灰化说明视图里的参数与测试方法代码不一致；点 Inconsistency Check 按钮按代码更新，再核对参数（`02.07.02.02.02`、`02.07.04.01.03`）。
7. **判定结果。** `TEST` 返回 `Boolean`；测试套件内所有 `TEST` 都 pass 则 testflow 里该套件 pass，任一 fail 则 fail（`02.07.04.01.241`、`02.07.03.14.02.04`）。
8. **event data log / 报告。** 开启 `log_events_enable` 与 `output_on_pass`/`output_on_fail`，报告器选 `EventFormatter`，执行 `TEST` 或 `PUT_DATALOG` 后应在报告窗口看到格式化数据（`02.07.03.03.07`）。
9. **L3 查询。** 用 `TestsuiteProxy.getTestmethodName()`、`getTestmethodParameterNames()`、`getTestmethodParameterValue()`、`getTestmethodLimitValue()`、`getTestmethodDefaultLimitNames()`、`isExecuted()`、`isPass()` 核对测试套件的 test method 绑定、参数、限值与执行结果（`02.09.01.14.02.01`）。
10. **库搜索是否命中。** 文档给出搜索顺序（device → `/opt/hp93000/soc/testmethod/library/sh_lib` → `/var/opt/...` → `V93000_TM_LIBRARY_PATH`）；若 `list types` 看不到自己的 test method，按该顺序检查库放在哪一层（`02.07.02.01`、`02.07.03.19`）。这是按文档顺序排查，不是文档写明的「验证命令」。

## 常见错误

| 症状 | 文档给出的原因 / 处理 | 出处 |
|---|---|---|
| 类名首字母小写，建类报错 | 类名必须以大写字母开头，否则弹错误信息 | `02.07.02.02.02` |
| 工程/库名含点导致构建或引用异常 | 工程名不得含点；库名除 `.so` 外不得含点；device 名里的点会换成下划线 | `02.07.02.02.01` |
| 两个 UTM 工程用同一个类名 | 文档要求避免；必须在不同工程复用时，把类源文件放进工程子目录以区分相对路径 | `02.07.02.02.02` |
| 加/删参数后 Properties view 变灰、参数不可改 | 视图里的参数与测试方法代码不一致；点 Inconsistency Check 按代码更新 | `02.07.02.02.02`、`02.07.04.01.03` |
| 限值一直是 `NA`，`TEST` 不按预期判定 | `addLimit` 只加名字并给默认 `'NA'`；实际值要在 tabular testflow editor 的 Limits tab 或 Properties view 填 | `02.07.04.01.02` |
| `TEST` 判 fail 后程序直接结束 | 默认 `continue = FALSE`；要无论结果都继续，传 `continue` 参数 | `02.07.04.01.241` |
| 多 site 下第一个 site 的 `TEST` fail 却没停 | 文档明确：第一个 site 即使 fail 且 `continue = FALSE` 也会继续；后续 site 才终止 | `02.07.04.01.241` |
| 在 first-invocation block 里用 `TEST` / `LIMIT` 报错 | `TEST` 不能在 first-invocation block 内使用（即使在 each-site 循环内）；`LIMIT` 不能在 `ON_FIRST_INVOCATION` 内使用（即使在 `FOR_EACH_SITE` 内） | `02.07.04.01.241`、`02.07.04.01.126` |
| 用 `EXECUTE_TEST` 跑含 digital capture 的测试，测试做不完 | 含 digital capture 的测试要用 `DIGITAL_CAPTURE_TEST` 或 `NB_DIGITAL_CAPTURE_START/END` | `02.07.03.03.04` |
| `FUNCTIONAL_TEST` 同时用模拟模块时模拟部分没生效 | 要在 `FUNCTIONAL_TEST` 前用 `FLUSH` 激活 primary analog set 与 routing connections | `02.07.03.03.04` |
| `WAIT_TEST_DONE` 超时后程序被中止 | 未设置 flag 参数时，timeout 会中止程序；按文档设置 flag | `02.07.03.03.04` |
| 在 extension block 里改 setup 后行为冲突 | 进入 extension block 前先 `FLUSH`；block 内缓存被系统临时关闭，避免 test method API 与 firmware command 冲突 | `02.07.03.10` |
| 第二次跑 testflow 时全局/静态变量还是上次的值 | 第一个 UTM executor 在 testflow 结束后不终止，global/static 不会自动重初始化；插入 `initialize`/`download` special test suite 重置 | `02.07.02.01.01`、`02.07.02.02.03` |
| 调试断点时无法单独跑另一个测试套件/Shmoo | 第二个 executor 未启用；在 `Testflow Tool` preference 勾选 `Execute selected UTM Test Method as separate process (to avoid blocking)` | `02.07.02.01.01` |
| 执行器异常终止后下次结果错误 | 进程会重新启动，但 testflow 变量可能未重置；文档提醒特别注意 testflow 变量 | `02.07.02.02.04` |
| 在 SmarTest 外跑转换工具失败 | `convertUP` / `convertTestflow` 只在 32-bit SmarTest 可用 | `02.07.02.05`、`02.07.02.06` |
| 在 SMC 后台进程 armed/running 时改/重 load TMLimits，数据无效或崩溃 | 文档 CAUTION 明确禁止；必须在 `SMC_ARM()` 前 load，所有设置先完成 | `02.07.04.01.250` |
| 想从 test method 里调用另一个 test method | 文档明确不能；可调用自己的 C/C++ 函数 | `02.07.02.01` |
| 在 `initialize()` / `postParameterChange()` 里用 setup/execution API | `initialize()` 只能用 `addParameter`/`addLimit`；`postParameterChange()` 不能用 test method API | `02.07.02.01` |
| 结果转 STDF 时 pin 名非法 | `TEST` 的 pin 必须是已定义 pin 名；把 `Check Testmethod API` flag 设为 on 可让非法 pin 在运行时 fatal error | `02.07.04.01.241` |
| 结果被误当可靠数据记录 | 用 `TEST` 的 `reliability` 参数标 `TM::UNRELIABLE`；但系统 Event Formatter 不会把 unreliable 状态写进报告窗口，需自研 formatter | `02.07.04.01.241` |

**关于独立的 Errors 汇总章：文档未覆盖。** 本阶段没有像 pin 那样的专门错误章；上表条目来自各 API/流程页的 `Errors`、`Warnings`、`Note`、`CAUTION` 段。没有文档依据的「常见错误」未写入。

## 下一步

**[[testflow]]**。本阶段产出的 UTM library 还没有被任何测试套件引用；下一步是在 Testflow Editor 里新建/打开 testflow，把 test method 选进测试套件，设 primaries 与 parameter/limit 值，再保存并执行（`02.07.02.02.03`、`02.07.01.01`）。文档的 `What to do next` 也是这个方向：建类 → 加源码 → 构建 → 建 testflow → 调试（`01.06.02`、`02.07.02.02.02`、`02.07.02.02.03`）。

testflow 组装好之后才进入 [[run]]（执行/调试）与 [[results]]（测量数据、event data log 与报告）。
