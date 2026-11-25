---
type: object
title: Technology file for a device
layer: file
stage: project
tags: []
related: []
sources:
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.01.02_Technology_file_for_a_device.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Technology file for a device

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

**没有加标记的语法段。** 定义文档里没有 `Syntax` / `Parameters` / `Example`
这类**段标记**。本脚本一个字都不收录——没有段标记时「哪一段是语法」是猜，
而猜就是编。要看原文：`python show.py <分类号>`。

<!-- 语法节 end -->

## 是什么

**文档事实**：`.technology` 文件定义 technology 相关设置的源目录、若干 device-specific system parameters，以及某些 system parameter 的最大值。最大值决定对应数据结构预留的内存；绝对最大值不会自动全部使用，以便内存用量反映 device 的实际需求。内存有限时，firmware 可能降低一个或多个本来有效的设置以留在限制内（源文指向 Testflow Analyzer Tool、Optimizing the technology file，以及 Result areas for error map data）。每个 device directory 都有一个 `.technology` 文件。

**文档事实**：源文列出的参数为：`/dev_tech/cmos` 或 `/dev_tech/ecl`、`check_compatibility_with_smart_scale`、`check_exa_scale_seq_restrictions`、`device_cycles`、`digital_default_result_area_size`、`dps_sets`、`enforce_smart_scale_dc_sync_compatibility`、`extended_dram_factor`、`fast_bi_directional_capability`、`fast_transfer_buffer_size`、`himem`、`init_vectors_with_value`、`level_sets`、`licensing_file`、`m_sets`、`mset_program_memory_preallocation`、`optimized_multiport_memory_allocation`、`pdc_sets`、`period_res_precision`、`pulldown_in_level_set_0`、`pulldown_not_configured_pins`、`pretty_printed_analog`、`tester_model`、`testpoints`、`timing_sets`、`utility_lines_per_pogoblock`、`waveform_sets`。源表每行给出 Short description、Values（含默认值）、Change Device wizard 字段、DSCP command 和 Note。

**文档事实**（逐个参数的要点）：
- `/dev_tech/cmos` 或 `/dev_tech/ecl`：technology 目录；在 New device 对话框选 technology，device 的 technology 相关 level 等数据存放在 device directory 的子目录中，创建 device 时从对应的 dev_tech 目录初始化；默认 level 由所选 technology 决定，可再定制。
- `check_compatibility_with_smart_scale`：on | off（默认 off）；开启后，selective capture patterns 含 break vector 或 match loop 时给 warning；全局属性，不是 per-channel。
- `check_exa_scale_seq_restrictions`：on（默认）| off；EXA Scale 数字卡的 sequencer 编程限制未遵守时抛 error；全局属性。
- `device_cycles`：默认 256，最大 16384；每个 waveform set 或 wavetable 的最大 device cycles 必须满足 `(device_cycles - 1) / waveform_sets`，且只计含物理 edge action 的 device cycles。
- `digital_default_result_area_size`：默认 0，最大 134217728；external (vector) memory 中 error map 的用户定义大小，单位 bytes，load 时预留；每个 digital pin 都预留（DPS pin 或配成 PMU/DPS 模式的 DC Scale pin 不预留）；不用于 Hidden upload；记录超出预留大小会停止，上传超出记录数据会报错；计入 license limit；1 byte = 1 vector；可用 `DMAS? MFRE` 查可用内存。
- `dps_sets`：默认 32，最大 256。
- `enforce_smart_scale_dc_sync_compatibility`：on | off（默认 off）；在 Smart Scale 卡上生成与 EXA Scale 兼容的 DC 测量固件命令；ON 时每个 measurement set 在 `ACTI`/`PMUM`/`VMUM`/`DVM1`/`DVM2` 动作后生成 `SYNC`。
- `extended_dram_factor`：0–99，默认 80；仅 `himem:on` 时有效；默认 80% tester memory 给 vector area、20% 给其他区域（如 sequencer 编程区或 result area），此值可改比例。
- `fast_bi_directional_capability`：on | off，默认 off；使用时设为 on。
- `fast_transfer_buffer_size`：默认 0；非 0 值范围 131072–16777216 bytes；为 `VEC_TRANSFER_TASK`、`LEV_TRANSFER_TASK`、`PPMU_SETTING` 修改数据提供 buffer；`VEC_TRANSFER_TASK`/`LEV_TRANSFER_TASK` 只能用于 SmartScale 测试头卡；SmarTest ≥ 7.4.3.0 与 < 7.4.3.0 有不同下限公式；≤ 7.4.1.0 时必须为 8192 的倍数；违反规则会报错，可增大 block size 或拆分传输。
- `himem`：on | off，默认 off；使用超过 2 GB vector memory 时设为 on；全局属性；不支持 memory sharing；当前只影响 PS5000。
- `init_vectors_with_value`：on | off，默认 off；用于 SmarTest 启动时预初始化 vector memory；默认按 `DEADBEEF` 序列初始化，此参数可把初始化改为 0；Change Device 向导允许 0–255；关闭或值 0 时与之前 SmarTest 7 版本兼容。
- `level_sets`：默认 32，最大 256。
- `licensing_file`：每 device 的 licensing 文件；不用时为空，否则填文件名。
- `m_sets`：默认 1024，最大 12800；PPMU measurement-set actions 的最大数量；相关命令为 `MSET`、`MEAS`、`PMUR`、`PSFC`、`PQFC`、`PRLT`、`GNOS?`。
- `mset_program_memory_preallocation`：on | off，默认 on；预分配 PPMU measurement-set actions 的内存，大小取决于 `m_sets`。
- `optimized_multiport_memory_allocation`：on | off，默认 off；切换到改进的 pattern loading 算法；multiport setup 中 pattern 无法全部加载时可试，但可能延长 test time。
- `pdc_sets`：默认 1，最大 128；每使用一个 selective capture vector variable 都要增加 `devicecycle_set`。
- `period_res_precision`：系统计算 period resolution 时保存的小数位；文件没有此参数时默认 4；有则以文件值为默认；创建 device 时设为 9（上限）。
- `pulldown_in_level_set_0`：on | off，默认 on；在 level set 0 启用 pulldown 电阻。
- `pulldown_not_configured_pins`：on | off，新 device 默认 on；为 level set 0 中未配置的 pin 启用 pulldown。
- `pretty_printed_analog`：on | off，默认 off；格式化 analog control file 的 XML。
- `tester_model`：`act`（源文另标 `[PPU unused]`）；pay per use 的 tester model。
- `testpoints`：默认 10000，最大 1048576；每 pin 的 testpoint 数；对内存用量影响最大，应谨慎设置，每个 test point 占几十 bytes。
- `timing_sets`：默认 256，最大 999；fixed timing 与 equation-based timing 的 timing set 总数。
- `utility_lines_per_pogoblock`：16 | 32，默认 16；要与 model file GLOBAL section 的 utility lines 设置配合。
- `waveform_sets`：默认 32，最大 128；fixed timing 的 waveform set 与 equation-based timing 的 wavetable 总数；与 `device_cycles` 共同满足上面的公式。

**文档事实**（Application note）：定义大量 testpoints 时必须遵守规则——与其它设置不同，testpoints 所需的最大内存会在 load device 的一开始就预留（由 `DTCP` 与 `*RST`）；内存在 model file 中所有可用的 DC Scale 卡上预留；无论之后是否使用都按最大需求预留；预留量取决于 `testpoints` 与卡相关结构（XPS256 每 testpoint 56 bytes，DPS128 与 UHC4T 46 bytes）；DPS128/DPS64 在 `waveform_sets=128` 时最多预留 523012 个 testpoint，更低的 waveform_sets 支持更多 testpoint。忽略规则、定义过多 testpoints 可能导致后续 setup/pattern 内存溢出；溢出时 UI report window 显示 “ERROR: Specified set size is too large for memory configuration”，SmarTest 恢复之前的 setup 或默认 setup，新定义设置和 pattern 不可用。

## 典型用法

**文档事实**：每个 device directory 的 `.technology` 文件可用源文示例作为骨架：`/dev_tech/cmos`、`device_cycles`、`waveform_sets`、`timing_sets`、`level_sets`、`dps_sets`、`pdc_sets`、`m_sets`、`period_res_precision`、`testpoints`、`utility_lines_per_pogoblock`、`tester_model`、`licensing_file`、`init_vectors_with_value`、`fast_transfer_buffer_size`。

**文档事实**：通常通过 Change Device 对话框（菜单 `93000 > Change Device`）修改；改动写入 `.technology` 并用 `DSCP` 等固件命令立即通知 firmware，之后每次选中该 device 都永久生效。Change Device 窗口没有的参数只能直接编辑 `.technology` 文件永久修改；此时必须手工发 `DSCP` 把新值告知 firmware，或重新选中 device（会重新发 `DSCP`）。

**文档事实**：新建 device 时在 New device 对话框选 technology；相关 level 等数据从 dev_tech 目录初始化到 device directory 子目录。

**文档事实**：参数设置的几个典型场景：
- 想用 >2 GB vector memory：`himem:on`，可能配合 `extended_dram_factor` 调整 vector 区比例。
- 使用 `VEC_TRANSFER_TASK`/`LEV_TRANSFER_TASK`/`PPMU_SETTING` fast transfer：设置足够的 `fast_transfer_buffer_size`；默认 0 不提供 buffer，非 0 值 131072–16777216 bytes，并按源文公式计算。
- 用 selective capture：按每个 selective capture vector variable 增加 `pdc_sets`/`devicecycle_set`；用 PS5000 时注意 `check_exa_scale_seq_restrictions`。
- 用 utility pogo block：`utility_lines_per_pogoblock` 必须与 model file 及布线工具中的 block size 一致（16 或 32）。
- 大量 testpoints：按 Application note 估算内存，避免溢出。

**建议（文档明确写出的）**：`testpoints` “should be set with caution”，因为对内存影响最大；`optimized_multiport_memory_allocation` 可能延长 test time，仅在 pattern 无法全部加载时考虑。

## 和谁有关

- [[new-device-wizard]] / Creating a new device：新建 device 时选 technology，并从 dev_tech 初始化目录；`.technology` 的 technology 目录行直接指向该页。
- [[change-device-wizard]] 与 Editing technology data / Edit Device page：正常修改 `.technology` 的入口；Edit Device 页字段与 `.technology` 参数的对应关系看本页参数表的 “Change Device wizard” 行。
- [[dscp]]：Change Device 的改动通过 `DSCP` 通知 firmware；直接改文件后必须手工 `DSCP` 或重新选 device。
- [[dtcp]]：`DTCP` 与 `*RST` 在 load device 开始时按 `testpoints` 预留内存。
- [[model-file]]：testpoints 内存在 model file 中所有可用 DC Scale 卡上预留；`utility_lines_per_pogoblock` 要与 model file GLOBAL section 的 utility lines 配合。
- [[device-technology-directory]] / Device Technology Defaults：technology 目录结构与默认值所在的上下文。
- **Testflow Analyzer Tool / Optimizing the technology file**：firmware 可能为内存限制降低设置；TAT 提供 set 数量，Optimizing 页讲如何按实际使用量调整 sets。
- **Result areas for error map data**：`digital_default_result_area_size` 与 error map 内存预留相关。
- **Fast Transfer APIs**：`fast_transfer_buffer_size` 被 `LEV_TRANSFER_TASK`、`VEC_TRANSFER_TASK`、`PPMU_SETTING` 使用；PPMU fast transfer 要求至少 131072 bytes，否则报错。
- **Routing Tools / utility pogo block**：`utility_lines_per_pogoblock` 必须与 Global Setup editor 的 Pogo block size 一致。
- **Selective capture / PS5000**：`check_exa_scale_seq_restrictions` 在 PS5000 selective capture 的 match loop 场景被引用；`pdc_sets` 与 `devicecycle_set` 用于 selective capture vector variable。
- **`GNOS?`**：`m_sets` 的参数说明把 `MSET`、`MEAS`、`PMUR`、`PSFC`、`PQFC`、`PRLT`、`GNOS?` 列为相关命令。
- **`pulldown_in_level_set_0` / `pulldown_not_configured_pins`**：与 level set 0 的保护、PS1600 level setup 相关。

## 版本

**文档事实**：`Functional changes` 写 “Introduced before SmarTest 6.3.2”；之后为：7.1.4 提高 PDC_set 上限；7.1.4.5 新增 `pulldown_in_level_set_0`；7.2.0 新增 `utility_lines_per_pogoblock`；7.2.1 Testflow Analyzer tool 提供 sets 数量；7.2.2 新增 Result Area Size；7.2.3.9 / 7.3.4.4 / 7.4.1.1 新增 `pulldown_not_configured_pins`；7.2.3.9 / 7.3.4.4 / 7.4.1.1 / 7.4.2 新增 `mset_program_memory_preallocation`；7.3.2 新增 `fast_transfer_buffer_size`；7.4.1 新增使用 `fast_transfer_buffer_size` 的 API `LEV_TRANSFER_TASK`。

## 出处

- 主源：`01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.01.02_Technology_file_for_a_device.htm`（正文、Available parameters、Changing the .technology file、Parameters of the .technology file、Application note、Related information、Functional changes）。
- 关系证据：`extract/objpack.py` 入边，主要来自 `01.01.10.03.03_Editing_technology_data`、`02.06.02.02.93_DTCP`、`02.06.02.02.90_DSCP`、`02.04.05.07.02_Optimizing_the_technology_file`、`02.07.04.01.270_VEC_TRANSFER_TASK`、`02.07.04.01.125_LEV_TRANSFER_TASK`、`02.07.04.01.160_PPMU_SETTING`、`02.07.13.15.01.01_Routing_Tools_-_Global_Setup_editor` 等。
