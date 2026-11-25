---
type: object
title: Utility line assignments
layer: n/a
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.04.01_Utility_line_assignments.htm
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.04.02_Utility_line_characteristics.htm
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.06.08_Pogo_pin_assignment_-_Utility_pogo_blocks.htm
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.05.05_Internal_utility_power_supply__V93000_systems.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Utility line assignments

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

**文档事实**所有 utility line 都有读、写能力，通过 DUT interface 上的 utility pogo block 引出。一个 utility pogo block 含 16 条 utility line（00–15）或 32 条（00–31）。选用哪种 block 取决于 DUT interface 类型与供电需求：

- 所有小 DUT interface 使用 16‑line、2‑row、34 pogo pin 的 block，DUT interface 共 64 条 utility line。
- DUT Scale / 大 DUT interface 可用 16‑line（2‑row）或 32‑line（4‑row，68 pogo pin）block：2‑row 总计 128 条，4‑row 总计 256 条；使用 256 条要求 4‑row block 且 SmarTest 7.2（或更高）。

**文档事实**4‑row block 多出的 pogo pin 不仅提供额外 utility line，还提供 External utility power supply 的 power line；外部 utility 电源只能经 4‑row utility pogo block 访问。

**文档事实**所有 utility pogo cable 始终有 32 条 utility line；pogo block 可互换并插在 cable 末端。2‑row 与 4‑row utility pogo block 不允许在同一 DUT interface 上混用。

**文档事实**编号：SmarTest 7.2 及以上按所选 block 类型把 utility line 编号为 01–16 或 01–32，与硬件记号 00–15 / 00–31 不同（存在 -1 偏移）。文档建议为让 4‑row block 通用，在所有 DUT board 的第 3、4 行位置加 dummy pad。

**文档事实**警告：4‑row utility block 的行序为 c‑a‑b‑d（为兼容 2‑row block），与其他 4‑row pogo block 的 a‑b‑c‑d 不同；使用错误行序会使 DUT board 不可用。

**文档事实**8 个 utility block（8 组）可用于：Large Test Head + large DUT interface、Small Test Head + DUT Scale interface、Compact Test Head + DUT Scale interface、A‑Test Head + DUT Scale interface。4 个 utility block（UTIL 1–4）可用于：Small / Compact / A‑Test Head + small DUT interface。

**文档事实**utility line 的电气特性（线数、控制方式、输出/输入电路）见 Utility line characteristics；内部 utility 电源经 UP5V pin 提供给 utility pogo block。

## 典型用法

**文档事实**DUT board 设计时先按所需线数与 DUT board 电源需求选择 2‑row（16 line）或 4‑row（32 line）block：小接口用 16‑line，DUT Scale / 大接口可到 128 或 256 条。

**文档事实**需要 External utility power supply 时只能使用 4‑row block；需要 sequencer 控制时，可将数字 pin 接到 utility pogo block 的串行接口（见 Setting up sequencer control of utility lines）。

**文档事实**软件侧用 DFUT（Define UTility line）、UTIX（utility line inputs extended）、UTOT（utility line outputs）等命令定义/驱动，用 GET_UTILITY_LINES_STATUS 读取状态。Utility Line view 中通道号按 [01…32] 从右到左显示，底层编号为 [00…31]，对应 “URW##” 方案。

**建议**文档建议 4‑row block 通用化时在 DUT board 第 3/4 行加 dummy pad；4‑row block 必须使用 c‑a‑b‑d 行序。

## 和谁有关

- `02.03.06.08_Pogo_pin_assignment_-_Utility_pogo_blocks.htm`：给出各 test head / DUT interface 组合下 utility 与 DPS block 的布置，本页是这些布置的总览来源。
- `02.03.04.02_Utility_line_characteristics.htm`：定义 utility line 的电气特性、pull‑up 等；本页负责 block 与线数分配。
- `02.03.04.07.01_Designing_compatible_utility_lines.htm`：说明每个 block 提供 16 或 32 条线，并回指本页查 block 类型。
- `02.03.04.05.03_Ganging_utility_blocks.htm`：说明用 8 个 32‑bit（4‑row）block 可控制最多 256 条 utility line，与本页 256 线上限一致。
- `02.03.05.06_External_utility_power_supply__V93000_systems.htm`、`02.03.05.05_Internal_utility_power_supply__V93000_systems.htm`：4‑row block 承载外部 utility 电源线，内部电源经 UP5V 引出。
- `02.06.02.02.70_DFUT...`、`02.06.03.02.12_DFUT...`、`02.06.12.02.02_DFUT...`：DFUT 命令说明直接让读者参阅 Utility line assignments 与 DUT interface layout。
- `02.06.02.02.310_UTIX...`、`UTOT...`、`GET_UTILITY_LINES_STATUS`：这些命令说明 utility line 以 pogo block 组织、每 block 32 线，并回指本页。
- `01.01.07.05.04_Utility_Line_view.htm`（及 `01.01.07.05.05_Using_the_Utility_Line_View.htm`）：解释 Utility Line view 的 [01…32] 与 [00…31] 编号偏移，与本页 SmarTest 7.2 编号说明对应。
- `02.03.06.08.03…09_Utility_pogo_block_-_*`：各 test head / 接口的 pogo block 页均声明“布置总览见 Utility line assignments”。

## 版本

**文档事实**本页 Functional changes：

- Introduced before SmarTest 6.3.2
- SmarTest 6.5.4：CTH with DUT Scale interface introduced
- SmarTest 7.1.0：A‑test head introduced
- SmarTest 7.2.0：256 sequencer‑controlled utility lines introduced on ATH/CTH/STH DUT Scale and on LTH
- SmarTest 7.2.0：External utility power introduced on ATH/CTH/STH DUT Scale and on LTH

**文档事实**子主题补充：Utility line characteristics 记 SmarTest 8.3.4 增加 V93000 EXA Scale 的 utility line 特性；Internal utility power supply (V93000 systems) 记 Introduced in SmarTest 7.5.2。

## 出处

- `02_System_reference/02.03_DUT_board_design_reference/02.03.04.01_Utility_line_assignments.htm`
- `02_System_reference/02.03_DUT_board_design_reference/02.03.04.02_Utility_line_characteristics.htm`
- `02_System_reference/02.03_DUT_board_design_reference/02.03.06.08_Pogo_pin_assignment_-_Utility_pogo_blocks.htm`
- `02_System_reference/02.03_DUT_board_design_reference/02.03.05.05_Internal_utility_power_supply__V93000_systems.htm`
