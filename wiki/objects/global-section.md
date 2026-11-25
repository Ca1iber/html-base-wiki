---
type: object
title: GLOBAL section
layer: file
stage: project
tags: []
related: []
sources:
  - 02_System_reference/02.04_Model_File_and_Licensing/02.04.01.03.02.01_GLOBAL_section.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# GLOBAL section

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **155 字符逐字取自** `<02_System_reference/02.04_Model_File_and_Licensing/02.04.01.03.02.01_GLOBAL_section.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example

```
...
GLOBAL
testhead = TH_8CC
dut_interface = SOC
device_maintenance = ON
timing_bundle = w256-d8-r8
diag_subsystem_interface = /dev/usb/ttyUSB0
...
```

<!-- 语法节 end -->

## 是什么

**文档事实** GLOBAL section 是 model file 的段，用于定义“使用何种系统”以及“有哪些系统级可用的特性”（原文：define what kind of system is used and what features are available system-wide）。

**文档事实** 文档列出的定义有：`apg_speed`、`device_maintenance`、`diag_subsystem_interface`、`dut_interface`、`hpib_interface`、`memory_pooling`、`memorytest`、`protocol_aware`、`memory_compatibility`（参数表正文写作 `PS1600MemoryCompatibility`）、`rapid_source_synch`、`s&s_value_package`、`testhead`、`timing_bundle`、`triage`、`utility_lines`、`vectorCache`、`xpressdata`。

**文档事实** 各定义的作用（摘要）：`apg_speed` 指定 MTP memory pattern 的最大执行速率（默认 0 Mbps；SOC 可选 400/800/1800 Mbps，需 APG speed license，实际速度取 APG 与通道速度 license 的较低值）；`device_maintenance` 启用 device maintenance/refresh（写 `ON` 启用，默认关闭且无警告，需 FLEXlm license，典型刷新周期 16–32 ms）；`dut_interface` 指定 DUT 接口类型（`SOC | HSM | SOC_8GROUP | SOC_4GROUP`）；`hpib_interface` 指定用于 NIST 可追溯校准的 GPIB 接口（如 `vxi11/<LAN-GPIB gateway>/192.168.0.100/gpib0`）；`memory_pooling` 允许合并多个 pin 的 license 供一个 pin 使用（默认启用，写 `OFF` 关闭）；`memorytest` 启用 memory-test 软件的 pattern 生成（默认关闭、需 license，且自 SmarTest 7.0.1 起废弃）；`protocol_aware` 启用事务型协议测试所需的 protocol-aware 特性；`PS1600MemoryCompatibility` 关闭 PS1600 memory compatibility 模式（默认启用）；`rapid_source_synch` 指定启用 RSS 的 site 数（默认 0，无需 license，在硬件中累积结果并并行处理）；`s&s_value_package` 启用 correction data converter（仅在有有效服务合同时提供）；`testhead` 指定 test head 规模与 card cage 数；`timing_bundle` 指定所有通道捆绑的 waveform/drive edge/receive edge 数；`triage` 指定 Yield Learning Solution 算法（`ON` 启用全部，或 `BCA | END_POINT_LOG | HOLD_TIME_FAULT | SPEED_SCAN` 选单个，需 license）；`utility_lines` 指定 utility line 数量、类型与 pogo 块大小；`vectorCache` 启用/关闭测试处理器的 vector cache（默认启用）；`xpressdata` 启用 Xpress Data Mode（默认关闭，需 license）。

**文档事实** 其中 `apg_speed`、`device_maintenance`、`memorytest`、`timing_bundle`、`xpressdata` 等特性受 license 约束，可能被 device license file 覆盖。

**推断** GLOBAL 管的是整机/系统级配置（test head 规模、DUT 接口、系统级 license 特性、全局 timing/utility 资源），与之相对，IOCHANNEL、DPS、POGOCABLING 等段管更窄的通道/卡/pogo 映射；这由原文的 “system-wide” 与各参数语义归纳。

## 典型用法

**文档事实** 本页示例只展示一个 GLOBAL 块：`testhead = TH_8CC`、`dut_interface = SOC`、`device_maintenance = ON`、`timing_bundle = w256-d8-r8`、`diag_subsystem_interface = /dev/usb/ttyUSB0`。

**文档事实** `testhead` 指定 test head 规模与 card cage 数：`TH_8CC`（Large，8 cage）、`TH_4CC`（Small，4）、`TH_2CC`（Compact，2）、`TH_1CC`（1）。`dut_interface` 可为 `SOC | HSM | SOC_8GROUP | SOC_4GROUP`；SOC 为 Pin Scale 系统标准，SOC_8GROUP 用于大 DUT board，SOC_4GROUP 用于小 DUT board。

**文档事实** `utility_lines = (64 | 128 | 256)[, type = (static | sequencer_controlled)][, pogo_size = (16 | 32)]`，必须反映当前实际安装的硬件能力；`utility_lines = 256` 才能启用每个 pogo 块全部 32 条 utility line；完全不写时系统默认 16 条；只有安装了 4-row utility line pogo 块时才应写 32，否则 SmarTest 不启动。在线使用时 `.technology` 文件（device 视角）也要定义 utility lines，与 model file（system 视角）不一致时会校验并告警；若两处都不写且 `dut_interface = SOC_8GROUP`，大/小 test head 都提供 128 条非 sequencer 可控的 utility lines。

**文档事实** `timing_bundle` 是 system 资源，指定所有通道捆绑的 waveform、drive edge、receive edge 数：`w32-d8-r6`（32/8/6）或 `w256-d8-r8`（256/8/8）。以 1800、2700、3200 Mbps 运行的通道必须配成 `w256-d8-r8` 或 `w32-d8-r6`；每通道的等价资源见 IOCHANNEL section 的 `tim`。

**文档事实** `diag_subsystem_interface` 定义用于 RS-232 低层诊断的串口设备；若同时设置导出变量 `DI_RS-232`，后者优先。文档给出 RHEL 7（SmarTest ≥ 7.5）的 `/dev/ttyUSB0`、`/dev/ttyUSB1`、`/dev/ttyS0`，以及 2/4 端口 MOXA 卡（SmarTest ≥ 7.3）的 `/dev/ttyMUE0`…`/dev/ttyMUE3`。

**文档事实** `xpressdata = ON` 启用 Xpress Data Mode（默认关闭、需 license），操作 Smart Scale 卡必须启用。`memorytest` 在 SmarTest 7.0.1 及以后已废弃，不应再使用；`vectorCache` 默认开启，文档要求在所有当前允许的场景下保持开启；`memory_pooling` 默认开启，写 `OFF` 才关闭；`device_maintenance` 若不写则默认禁用，且不会给出警告或错误。

**建议** 按实际 test head/DUT 接口与硬件能力填写 `testhead`、`dut_interface`、`utility_lines`；1800 Mbps 以上通道使用 `w256-d8-r8`；Smart Scale 系统启用 `xpressdata`；SmarTest ≥ 7.0.1 不再写 `memorytest`；不要关闭 `vectorCache`。

## 和谁有关

- **文档事实** `02_System_reference/02.04_Model_File_and_Licensing/02.04.01.03.02_Model_file_reference__model_legacy.htm` 与 `02_System_reference/02.04_Model_File_and_Licensing/02.04.01.02_Concepts_of_logical_boards.htm` 引用本页：前者把 GLOBAL 列为 legacy model file 的段之一，后者在逻辑板概念中使用 GLOBAL。
- **文档事实** `02_System_reference/02.04_Model_File_and_Licensing/02.04.01.03.02.03_IOCHANNEL_section.htm` 引用本页并说明“自 release 5.2 起建议使用 GLOBAL section 的 `timing_bundle` 参数”，两者在 timing 资源上互补（GLOBAL 为系统级，IOCHANNEL 的 `tim` 为每通道）。
- **文档事实** `02_System_reference/02.04_Model_File_and_Licensing/02.04.01.03.02.02.02_Conversions__pogo_mapping_file__-__POGOCABLING.htm` 引用本页：GLOBAL 的 utility line/pogo 块设置与 POGOCABLING 的 pogo 映射相互关联。
- **文档事实** `02_System_reference/02.04_Model_File_and_Licensing/02.04.05.06_The_device_license_file.htm` 与 `02_System_reference/02.04_Model_File_and_Licensing/02.04.05.07.03_How_to_generate_and_provide_a_device_license_file.htm`：前者说明 device license file 可覆盖 GLOBAL 中受 license 约束的特性（如 `apg_speed`、`device_maintenance`、`memorytest`、`timing_bundle`、`xpressdata`），后者说明生成 device license 时会自动在 GLOBAL 加 `protocol_aware = on`。
- **文档事实** `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.03.03_Technology_file_for_a_device.htm`（另有 `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.15.03_Technology_file_for_a_device.htm`、`01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.01.02_Technology_file_for_a_device.htm` 同题页）引用本页：`utility_lines` 需在 `.technology` 文件与 model file 两侧配合定义，并会被交叉校验。
- **文档事实** `02_System_reference/02.03_DUT_board_design_reference/02.03.04.05.01_Serial_interface_for_sequencer-controlled_utility_lines.htm` 与 `02_System_reference/02.03_DUT_board_design_reference/02.03.04.05.06_Setting_up_sequencer_control_of_utility_lines.htm` 引用本页：前者强调 `utility_lines` 必须反映实际硬件能力，后者给出 `utility_lines = 128, type = sequencer_controlled, pogo_size = 16` 的配置示例。
- **文档事实** `02_System_reference/02.05_Test_Head_Cards/02.05.04.01.03_PS1600_functionality_and_features.htm` 引用本页：操作 Smart Scale 卡必须在 GLOBAL 与 device license file 中启用 `xpressdata`。
- **文档事实** `02_System_reference/02.07_Test_Method_Reference/02.07.11.01.01_License_requirements_for_transaction_based_protocol_tests.htm` 与 `02_System_reference/02.07_Test_Method_Reference/02.07.03.02.03_Direct_DMM_high-accuracy_voltage_measurements_via_utility_pogo_block.htm`：前者用 GLOBAL 的 `protocol_aware` 满足事务型协议测试 license，后者给出 GLOBAL 中 `hpib_interface = vxi11/...` 的 DMM 配置。
- **文档事实** `03_Use_cases_and_application_papers/03.01_Performance_Cookbook__How_to_reduce_test_times/03.01.02.02_Tester_model_and_Configuration.htm` 引用本页：该 cookbook 指出 GLOBAL 中若干参数直接影响 testflow 执行时间。
- **文档事实** `02_System_reference/02.06_Command_Reference/02.06.07.01.04.02_Memory_pooling_within_channel_groups.htm` 与 `02_System_reference/02.06_Command_Reference/02.06.02.02.311_UTOT__UTOT__-__UTility_line_OuTputs.htm`（另有 `02_System_reference/02.06_Command_Reference/02.06.12.02.11_UTOT__UTOT__-__UTility_line_OuTputs.htm`）：分别对应 GLOBAL 的 `memory_pooling` 与 utility line 输出配置。

## 版本

**文档事实** `Functional changes` 记录（按原文）：
- Introduced before SmarTest 6.3.2
- SmarTest 6.5.0: New definition: POGOCABLING
- SmarTest 6.5.2: New definition: triage
- SmarTest 6.5.3: E7032B (L488) LAN to GPIB gateway introduced
- SmarTest 6.5.3: SW Online Value Package license added, which is needed by cal data converter
- SmarTest 6.5.3: RSS no longer requires license
- SmarTest 7.0.1: For HSM: No license required for multiport
- SmarTest 7.0.1: Removed option: ppu_device
- SmarTest 7.0.1: For HSM: Xpress Transfer Mode supported
- SmarTest 7.1.0: New parameters: memory_pooling, protocol_aware
- SmarTest 7.1.0: No license or entry required for multisite
- SmarTest 7.1.0: For MTP on SOC: additional 4600/8000 Mbps speed steps with release 7.1.3.2
- SmarTest 7.2.0: New definition: utility_lines
- SmarTest 7.3.4: New definition: mux_boards
- SmarTest 7.4.3: diag_subsystem_interface definition
- SmarTest 7.4.4: New optional parameter diag_behavior of definition mux_boards
- SmarTest 7.5.3: Term "calibration data converter" replaced

## 出处

- `02_System_reference/02.04_Model_File_and_Licensing/02.04.01.03.02.01_GLOBAL_section.htm`（主源：定义、全部参数、Example、Related information、Functional changes）。
- 关联判断另参考 `extract/edges.jsonl` 中指向本页的入边；本页语法节即同页 Example，无其他语法子主题。
