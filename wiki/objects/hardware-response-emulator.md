---
type: object
title: Hardware Response Emulator
layer: gui
stage: run
tags: []
related: []
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.06_Hardware_Response_Emulator.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Hardware Response Emulator

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **619 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.06_Hardware_Response_Emulator.htm>` 及其子主题 `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.06.02_Using_hardware_response_files_for_execution.htm>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.06.03_Hardware_response_files.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Using hardware response files for execution）

When the hardware response file is not found for the execution of a test suite with
the pass/fail result, the
Hardware Response Emulator Pass/Fail Dialog

window for the "Import" mode opens.

### Example（取自子主题 Hardware response files）

The hardware response file
TS1;Analog.DGT("a_out").getWaveform(1);1;1

is related to the first execution of the
Analog.DGT("a_out").getWaveform()
 API
called on site 1 in the method program in the
TS1
 test suite. Note that a
hardware response file name contains a default input value even if the value was not set in the
related API. This is the reason why the file name contains
Waveform(1)
 even if
"1" is not set for the API.

<!-- 语法节 end -->

## 是什么

**文档事实**：Hardware Response Emulator（HWRE）是 SmarTest 提供的工具，用于离线调试 testflow 或 test suite 时解决两个问题：test method API 返回随机且无意义的数据；难以方便地控制每个 test suite 的 pass/fail。它后台运行，在测试的适当位置返回预先准备的数据，如 analog waveform、测量值、pass/fail 等（`02.08.04.32.02.06`）。

**文档事实**：两种模式：
- **Import mode**：从 hardware response 文件导入数据，在执行期间返回给 testflow 或 test method API。
- **Store mode**：在线执行时由测量数据、离线执行时由用户提供的数据生成 hardware response 文件。在线跑到 test suite 末尾或「取硬件响应数据的 test method API」时，自动把 pass/fail 与响应数据存入不同文件；离线时在同一时机打开提示窗口，由用户指定虚拟结果或响应数据。

**文档事实**：hardware response 文件与「一次 test suite 或 test method API 的取数执行」对应，文件名格式为 `Testsuite;MAPI;call#;site#`（`02.08.04.32.02.06.03`）。

**文档事实**：可模拟的 test suite 结果与 API 是有限集合：ANALOG/ANALOG_STATUS 类的 `DGT`（`getWaveform`、`getComplexWaveform`、`getDebugWaveform`）、`TIA`（`getResult`、`getMean`、`getMin`、`getMax`、`getJitter`）、`Vector.getVectors`、SpecSearch（`getResultSpec`、`getPassVal`、`getFailVal`）、DC APIs（`PMU_IFVM`、`PMU_VFIM`、`DPS_VFIM`、`PPMU_MEASURE`、`DPS_TASK`、`SPMU_TASK`）、`FW_TASK(command, answer)`、`GET_FUNCTIONAL_RESULT`、`TEST`（functional test）、`SEARCH_FUNC_TASK`、`PATTERN_CONTROLLER`；上述 API 的其他成员函数不支持（`02.08.04.32.02.06.04`）。

## 典型用法

**文档事实**：先用 Store 模式准备文件（`02.08.04.32.02.06.01`）：
1. `Run > Open Run Dialog`，右键 `Testflow (Full)` 新建一个 testflow（文档示例命名 `Testflow (Full_HWRE)`）。
2. 在 Response Emulator 区勾选 `Enable`、选择 `Store mode`，`Apply` 后 `Run`。
3. 在 Hardware Response Emulator 窗口设定 hardware response 目录（可用默认路径、新建目录，或勾 `Add Time Stamp` 并用 `%Y`/`%m`/`%d`/`%H`/`%M`/`%S` 等占位符）。
4. 在 `HW Response Emulator Enable` 列表选择要生成文件的 test suite（默认全选），`OK`。
5. 文件生成到指定目录。

**文档事实**：再用 Import 模式执行（`02.08.04.32.02.06.02`）：Run Dialog 中选 `Testflow (Full)`，在 Response Emulator 区勾选 `Enable checkpoint`、选择 `Import mode`，`Apply`、`Close`，运行 testflow；开始时 HRE 窗口弹出，确认响应目录与目标 test suite 后 `OK`。此后在取数 test suite/API 执行时由文件返回数据。

**文档事实**：若所需 hardware response 文件不存在，会打开 `Hardware Response Emulator Pass/Fail Dialog`（Import 模式），让你指定该 test suite 或 method API 的结果数据并存成响应文件；该对话框与 Store 模式类似，但 test suite 字段显示的是 `Testsuite; call#; site#`（不含 method program 名），并有 `Store hardware response data` 项。

**文档事实**：文件名示例 `TS1;Analog.DGT("a_out").getWaveform(1);1;1` 对应 TS1 test suite 中 site 1 第一次调用 `Analog.DGT("a_out").getWaveform()`；即使 API 未设置 `"1"`，文件名仍包含默认输入值 `Waveform(1)`（`02.08.04.32.02.06.03`）。

**文档事实**：两篇子主题对启用控件的写法不同——Store 模式写作 `Enable`，Import 模式写作 `Enable checkpoint`；此处按原文并列，不推断二者在各版本中的对应关系。

**建议**：先用 Store 模式在一台有真实测量数据的在线环境生成响应集，再用 Import 模式离线复现；这样调试时的数据与波形来自实际采集，而不是随机值（文档说明这两点正是 HWRE 的用途）。

## 和谁有关

- [[testflow-tool]] — **文档事实**：HRE 的配置入口在 testflow 运行对话框的 Response Emulator 区；`Using the Testflow Tool` 将 HRE 列为相关条目（入边语境）。
- [[run-dialog]] — **文档事实**：准备与执行都从 `Run > Open Run Dialog` 进入，在 Response Emulator 区选择 Store/Import 模式（`02.08.04.32.02.06.01`、`02.08.04.32.02.06.02`）。
- `Hardware response files`（`02.08.04.32.02.06.03`）— **文档事实**：本页子主题，定义响应文件的内容与 `Testsuite;MAPI;call#;site#` 命名。
- `Supported test suites and test method APIs`（`02.08.04.32.02.06.04`）— **文档事实**：本页子主题，限定可模拟的 test suite 结果与 API 清单。
- `Offline Result Emulation`（`02.07.12`）— **文档事实**：本页 Related information 链到 ORE；ORE 的 concept 页与 ORE setup file 页也链回 HRE（`02.07.12.02`、`02.07.12.05`）。
- `Offline result emulation setup file`（`02.07.12.05`）— **文档事实**：ORE 使用 XML 格式 setup file，并可定义 digital pattern fails、parametric values、analog waveforms、digital capture waveforms；ORE 由 `OfflineResultEmulationConfig` 配置（`02.07.12.02`）。**推断**：ORE 与 HRE 在文档中是互链但各自独立的主题（配置 API 与 setup file 不同），所读文档未说明两者共用同一文件格式或机制。
- `Pre-silicon and emulation workflow`（`02.07.12.01`）、`Concept of offline result emulation`（`02.07.12.02`）— **文档事实**：这些页指向 HRE 了解离线模拟细节（入边语境）。
- `Checking the execution flow`（`02.08.04.32.02.03.03`）— **文档事实**：HRE 的 Related information 列出该篇，用于检查 testflow 执行流。
- [[spec-search]] — **文档事实**：HWRE 支持 SpecSearch 的 `getResultSpec`、`getPassVal`、`getFailVal`，因此 spec search 的结果也可由响应文件提供（`02.08.04.32.02.06.04`）。
- `Debugging a testflow`（`02.08.04.32.02.04`）、`Using the debugger`（`01.03.03.01`）— **文档事实**：这两篇引用 HRE（入边语境）。

## 版本

**文档事实**（主文档 `Functional changes`）：Introduced before SmarTest 6.3.2（哨兵值：文档集覆盖范围之前已有，不代表 6.3.2 的变更）。

**文档事实**（子主题 `Functional changes`）：
- `Preparing Hardware Response files`：Introduced before SmarTest 6.3.2；**SmarTest 6.5.3：准备 hardware response 文件的流程发生变化**。
- `Using hardware response files for execution`：Introduced before SmarTest 6.3.2；**SmarTest 6.5.3：使用 hardware response 文件执行的流程发生变化**。
- `Hardware response files`、`Supported test suites and test method APIs`：Introduced before SmarTest 6.3.2。

## 出处

- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.06_Hardware_Response_Emulator.htm`（主文档：Import/Store 模式、用途、Related information、Functional changes）。
- 子主题：`02.08.04.32.02.06.01_Preparing_Hardware_Response_files.htm`、`02.08.04.32.02.06.02_Using_hardware_response_files_for_execution.htm`、`02.08.04.32.02.06.03_Hardware_response_files.htm`、`02.08.04.32.02.06.04_Supported_test_suites_and_test_method_APIs.htm`。
- 关系核对：`02_System_reference/02.07_Test_Method_Reference/02.07.12.02_Concept_of_offline_result_emulation.htm`、`02.07.12.05_Offline_result_emulation_setup_file.htm`（ORE 互链）。
