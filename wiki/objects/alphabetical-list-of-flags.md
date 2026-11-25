---
type: object
title: Alphabetical list of flags
layer: L3
stage: testmethod
tags: []
related: []
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.07.01_Alphabetical_list_of_flags.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Alphabetical list of flags

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

**文档事实**：本页是 testflow tool 中 flags 的按字母顺序参考表，说明控制 testflow 执行众多方面的 flag。所有 flag 的状态保存在 [[testflow-file]] 中；SmarTest 在加载该文件时对参数做 range check。

**文档事实**：表的列是 `Name in GUI / Keyword`、`Area`、`Description`、`Default`。第一列给两个名字：上面的名字显示在 [[flags-page]] 或 Testflow Tool 的 Test suite properties view；下面的名字是存进 [[testflow-file]] 的 keyword。GUI 的 `on`/`off` 对应 testflow file 或 API 中的 `1`/`0`；其他 GUI 下拉标签也同样以整数表示；括号里的整数就是 testflow file/API 使用的值。

**文档事实**：表按 `Area` 覆盖 Site control、Testflow、Test suite、Data logging；另有 `n/a` 的 legacy flags（`dsp_file_enable`、`hw_dsp_disable`、`stdf_generation`、`use_hw_dsp`，标注 “Do not use for new device test programs”）。本页没有 `Syntax`/`Parameters`/`Example` 段标记，因此上面语法节为空。

**文档事实**：本页列出的 flag 如下（按 Area 归组；名字为 GUI 名 / keyword）：
- Site control：`#1 … #n` / `site_control`（Site Control 设为 OTHER 时的 site 顺序）、`Allow Parallel` / `force_serial`、`Site Control` / `site_control`、`Size, Cycle` / `site_control`、`Site Match` / `site_match`。
- Testflow：`buffer_testflow_log`、`check_testmethod_api`、`debug_analog`、`debug_mode`、`global_hold`、`global_overon`、`hold_on_fail`、`limits_enable`、`log_cycles_after`、`log_cycles_before`、`multibin_mode`、`parallel_mode`、`set_bypass_level`、`set_fail_level`、`set_pass_level`、`site_match_mode`、`sqst_mode`、`test_number_enable`、`test_number_inc`、`unburst_mode`、`warn_as_fail`。
- Test suite：`Bypass` / `bypass`、`Fail per label` / `fail_per_label`、`Fail value` / `value_on_fail`、`FFC enable` / `ffc_enable`、`FFV enable` / `ffv_enable`、`FRG enable` / `frg_enable`、`H/L/I/U (multiple execution)` / `frg_single_shot`、`Hold` / `hold`、`Hold on fail` / `hold_on_fail`、`Log first` / `ffc_on_fail`、`Log Mixed Signal Waveforms` / `mx_waves_enable`、`Output on fail` / `output_on_fail`、`Output on pass` / `output_on_pass`、`Pass value` / `value_on_pass`、`Per pin on fail` / `per_pin_on_fail`、`Per pin on pass` / `per_pin_on_pass`、`Set fail` / `set_fail`、`Set pass` / `set_pass`、`Test Level` / `test_level`、`Test Number` / `override_test_number`。
- Data logging：`calib_age_monitor`、`current_monitor`、`datalog_formatter`、`datalog_sample_size`、`diag_monitor`、`graphic_result_display`、`hidden_datalog_mode`、`ink_wafer`、`log_events_enable`、`max_reprobes`、`print_wafermap`、`state_display`、`temp_monitor`、`tm_crash_as_fatal`。
- `n/a`（legacy）：`dsp_file_enable`、`Hardware DSP disable` / `hw_dsp_disable`、`stdf_generation`、`use_hw_dsp`。

**文档事实**：每行 `Default` 不同，源表逐行给出；例如 `parallel_mode` 默认 `on (1)`，`debug_mode` 默认 `0 (Debug off) (0)`，`datalog_sample_size` 默认 `1`，`hidden_datalog_mode` 默认 `0`，`ink_wafer` 默认 `off (0)`。完整默认值和逐条说明以源表为准。

## 典型用法

**文档事实**：flag 在 Testflow tool 的 [[flags-page]] 或 Test suite properties view 中查看/修改；保存后以 keyword 形式进入 [[testflow-file]]。GUI 的 `on`/`off` 写入文件/API 时变为 `1`/`0`。

**文档事实**：表中可直接套用的几个例子：
- `parallel_mode` 设为 `on` 时多 site 的 test suite 并行；若个别 test suite 自身设为 serial，则仍按 test suite 的设置串行。
- `check_testmethod_api` 控制未定义 pin 名是否导致 fatal error；源文写明若将使用 STDF 分析测试结果，应设为 `on`。
- `hidden_datalog_mode`：`0` 关闭；`1` compatibility mode（limits 取 `SMC_SYNCHRONIZE()` 定义的值）；`2` full hidden mode（含 `LIMIT` 支持，limits 取调用 test suite 定义的值，源文推荐此模式）。开启 hidden mode 后交互执行 SMC test suite 可能出现缺失/意外 data log entry，源文建议此时不要开启。
- `site_match_mode`：测试超过 255 个 site 时必须设为 `off`，否则产生错误消息；共享 BADC 时必须关闭 site matching。
- `datalog_sample_size`：`n` 为每 n 个 device 记录一次；范围 1–9999，默认 1；100 表示只记录每第 100 个 device。
- `test_number_enable`：`2` = on + validity check；检查 test number 为 0、缺失或已分配给其他 test，出现则 test suite 以 fail 停止。
- `global_overon`、`unburst_mode`、`multibin_mode`、`set_pass_level`/`set_fail_level`/`set_bypass_level` 分别按行内描述控制 stop bin 继续、burst 重跑、multibin 抑制与按 test level 判 pass/fail/bypass。

**文档事实/建议**：表中许多行带 “For optimized throughput, set the flag to ...”，例如 `buffer_testflow_log` off、`calib_age_monitor` off、`current_monitor` off、`datalog_formatter` off、`debug_mode` off、`global_hold` off、`global_overon` on、`graphic_result_display` off、`hold_on_fail` off、`limits_enable` off、`log_cycles_after`/`log_cycles_before` 0、`max_reprobes` 1、`print_wafermap` off、`state_display` off、`temp_monitor` off、`test_number_inc` 1、`warn_as_fail` off。这些是文档给出的吞吐建议，不是对所有配置都成立的硬性要求。

## 和谁有关

- [[testflow-file]]：flag 状态的实际存储处，加载时做 range check；keyword 列就是写入文件的名字。为什么：本页第一列下半部分即文件 keyword。
- [[flags-page]]、Test suite properties view、Testflow Properties view：显示 GUI 名并编辑 flag；本页第一列上半部分即这些界面中的名字。
- **Testflow flags / Test suite flags / Site control flags**（`02.08.04.32.01.02.07.02`、`.04`、`.05`）：这几个子页按类别收录同一批 flag 的 additional information，并回链本页；本页是它们的字母序总表。
- **`MONITOR_CALL`**：`calib_age_monitor`、`current_monitor`、`diag_monitor`、`temp_monitor` 控制 monitor 进程在 `MONITOR_CALL` 执行时检查什么。为什么：这些 flag 的描述直接指向该命令。
- **`SET_MULTIBIN`、`RESET_MULTIBIN`、`TESTSET().judgeAndLog`、`SMC_SYNCHRONIZE()`、`SMC_TEST()`**：`multibin_mode` 的 `suppress_on_set_pass` 会忽略这些调用中的 multibin 设置；`test_number_enable` 影响 `TEST()`/`SMC_TEST()` 的 test number 记录。
- **`DCRM`**：`Fail per label` 启用时 error map 使用 `DCRM` 的 LMAP 模式。
- **Site control / 多 site**：`Allow Parallel`、`Site Control`、`Size, Cycle`、`Site Match` 与 Expanded Site Control window、`FOR_SEMI_PARALLEL_TEST_BEGIN`/`FOR_SEMI_PARALLEL_TEST_END` 相关；`03.01.03.01` 的性能手册要求 `parallel_mode` on 且每个 test suite 勾 Allow Parallel。
- **Data logging / binning**：`log_events_enable`、`datalog_sample_size`、`graphic_result_display`、`ink_wafer`、`print_wafermap` 等影响 data logging 与 bin 展示；`global_overon` 与 Overon flag、`03.02.02.06.07` 的 multibin 用法相关。
- **Testflow 调试**：`debug_mode`、`global_hold`、`hold_on_fail`、`sqst_mode` 被调试/单步相关页面引用；`debug_mode` 的值决定 Report window 的调试信息级别。

## 版本

**文档事实**：`Functional changes` 写 “Introduced before SmarTest 6.3.2”，之后依次为：SmarTest 6.5.3 移除 `rf_cal_interp`；6.5.4 移除 `rf_dembedCal_enable`；7.1.0 移除 `OOC_watch`、`OOC_sample_size`、FFC scan info enable、Hardware DSP disable；7.1.2 移除 `rf_cal_enable`；7.1.3 移除 `optimized_mode`、新增 `hidden_datalog_mode`；7.1.4 把 `use_hw_dsp`、`dsp_file_enable` 标为 legacy；7.2.0 移除 `report_to_file`、`report_to_printer`、`datalog_to_file`、`datalog_to_printer`、`datalog_to_report_win`；7.4.5 把 `stdf_generation` 标为 legacy。

## 出处

- 主源：`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.07.01_Alphabetical_list_of_flags.htm`（整张 flag 表、Related information、Functional changes）。
- 关系证据：`extract/objpack.py` 入边，主要来自 `02.08.04.32.01.02.07.02`（Testflow flags）、`.04`（Test suite flags）、`.05`（Site control flags）、`02.08.04.32.01.02.07_Flags`、`02.08.04.32.03.05_Testflow_file`、`03.01.03.01` 等。
