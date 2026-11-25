---
type: object
title: Utility pogo block - Utility Card (V93000 EXA Scale systems)
layer: n/a
stage: project
tags: []
related: []
sources:
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.06.08.02_Utility_pogo_block_-_Utility_Card__V93000_EXA_Scale_systems.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Utility pogo block - Utility Card (V93000 EXA Scale systems)

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

**文档事实**：V93000 EXA Scale 系统可选装 Utility Card（EK051A）；每张卡提供 256 条动态控制的 utility lines 和若干 utility power supplies，这些资源被引到八个 4-row utility pogo blocks（`02.03.06.08.02` 首段）。

**文档事实**：适用系统为 EXA Scale（SmarTest 7+8）；未装 Utility Card 的 EXA Scale 系统应参考 `Utility pogo block - Basic configuration (V93000 EXA Scale systems)`（同页首段与表格）。

**文档事实**：4-row utility block 的行序是 `c-a-b-d`（为兼容 2-row block），与其他 4-row pogo block 的 `a-b-c-d` 不同；文档 CAUTION 明确说用错行序会导致 DUT board 不可用（同页「Mapping of pin groups and utility pogo blocks」）。

**文档事实**：八个 utility pogo blocks 到 DUT interface 的 legacy pogo block 映射随第一/第二张 Utility Card 不同：第一张卡为 165–172（UTIL 1–8），第二张卡为 265–272（按 DPS 3、1、2、8、4、5、6、7 的顺序）（同页「Utility pogo block mapping」表）。

**文档事实**：每个 utility block 的 pin 名称与功能包括 `DSC`（DUT board detection，低=已连接）、`FRAMn`、`PDCF/PDCS`、`PGDS/PGRD/PGND`、`POG4R`、`SINP/SOUT/SCLK`（串行接口）、`UGND/UGNDs`、`UP5V`、`UPP15V/UPM15V`、`URW##`、`XPP5V/XPM5V/XPP3V3`、`XDCGD`，以及部分电源的 sense pin（`…s`）与 return pin（`…R`）；完整名称表见同页「Pin description」（同页）。

**文档事实**：`Utility DC pins` 在 Digital Pins Editor 中记为 `UTIDC165`（第一张卡）/`UTIDC265`（第二张卡），文档注明它们仅在 SmarTest 7.10 支持（同页「Utility DC pins」）。

**文档事实**：布线规则包括：同一 utility supply 输出的所有 block pogo pins 接到 DUT board 上独立的 power plane；所有 sense pins 接到相关 plane；不同 Utility Card 的 utility supply pogo pins 不得互连；utility ground 对 system ground 的最大偏移 ±0.5 V；block 1 的 `URW14`/`URW15` 内部接 DUT Interface EEPROM，不得用于其他用途（同页「Wiring rules and notes」）。

**文档事实**：电源映射表给出 `UP5V`（+5.0 V/8.0 A）、XP pins（`XPP5V` +5.0 V/12.8 A、`XPP3V3` +3.3 V/6.0 A、`XPM5V` −5.0 V/6.0 A），以及 `UPP15V`（+15.0 V/3.0 A）、`UPM15V`（−15.0 V/3.0 A）、`F24VA`/`F24VB`（24 V/1.0 A）；`UPP15V`/`UPM15V`/`F24VA`/`F24VB` 只在部分 block 上提供（同页「Utility power supply mapping of the Utility Card」）。

**推断**：这是一页 DUT board 设计参考（pin/power 映射），不是可调用的 API；使用前必须先确定装的是第一张还是第二张 Utility Card，因为两卡对 DUT interface 的 block 映射不同（依据同页 mapping 段与 CAUTION）。

## 典型用法

**文档事实**：做 DUT board 设计时，按本页「Mapping of pins on a 4-row utility pogo block」的 Block 1 表确定每个 4-row block 的 1–15 号位置（c/a/b/d 四行）上的 pin；Block 1 的示例位置包括 `XPP5V`、`URW00`、`UGND`、`URW16`、`UP5V`、`DSC`、`POG4R`、`SINP/SOUT` 等，且 c15 现为 `PGND`（同页表与 Functional changes）。

**文档事实**：布线与电源连接按「Wiring rules and notes」执行：每个 supply 独立 power plane、sense pin 接对应 plane、不同卡不互连、utility ground 对 system ground 偏移不超过 ±0.5 V（同页）。

**文档事实**：使用 `UTSC`、`DFUP`、`DFUT`、`UTIX`、`UTOT` 等命令时，pogo block 以三位数标识（`DFUP`/`DFUT` 中是五位数通道号的前三位），有效 block 号参考本页「Utility pogo block mapping」；`GetUtilityLines`/`SetUtilityLines` 与 `Utility Line view` 也指向本页的 mapping（入边语境，`02.06.02.02.312`、`.69`、`.70`、`.310`、`.311`、`02.07.05.04.05`、`.07`、`01.01.07.05.04`）。

**文档事实**：第一张卡与第二张卡的映射不同；例如第二张卡的 utility block 1 落在 DPS 3（265）、block 2 落在 DPS 1（266），而第一张卡 block 1–8 依次是 UTIL 1–8（165–172）（同页 mapping 表）。

**建议**：做 DUT board 设计评审时，把本页 mapping 表和电源映射表一起看——mapping 决定 block 号，电源映射决定该 block 上是否真有某路 supply（同页两节互相引用）。

## 和谁有关

- **Utility Card（EK051A）** — **文档事实**：本页描述该卡提供的八个 utility pogo blocks 的 pin/power 分配；Utility Card 参考页与 sitemap 把本页列为 pogo pin assignment（`02.05.08.04`、`02.05.08.04.01`–`.04`、`02.02.01.05.02` 入边语境）。
- **Utility lines / Utility power supplies** — **文档事实**：本页 Related information 直接列出这两篇；`URW##` 是 utility line，`UP5V/XP/UPP15V/UPM15V/F24V` 是 utility supply（`02.03.04`、`02.03.05`；本页 Related information）。
- **DUT interface layout** — **文档事实**：本页 Related information 列出；block 映射与 `DPS 1…8`/`UTIL 1…8` 的对应需结合 DUT interface layout 理解（`02.03.03.01`）。
- **Basic configuration (V93000 EXA Scale)** — **文档事实**：未装 Utility Card 时的 pogo pin assignment 以该页为准（`02.03.06.08.01` 入边语境与本页首段）。
- **UTSC / DFUP / DFUT / UTIX / UTOT** — **文档事实**：这些命令/查询的 pogo block 号以本页 mapping 为准（`02.06.02.02.312`、`.69`、`.70`、`.310`、`.311` 等入边语境）。
- **GetUtilityLines / SetUtilityLines** — **文档事实**：两页的 See also 指向本页「Utility pogo block mapping」（`02.07.05.04.05`、`.07` 入边语境）。
- **Utility Line view** — **文档事实**：该 GUI 视图的 block 号参考本页 mapping（`01.01.07.05.04` 入边语境）。
- **UP5V / XP / UPP15V-UPM15V-F24V pins** — **文档事实**：电源映射与这些电源 pin 页一一对应；第二张卡的 DPS block 顺序与第一张卡不同（`02.03.05.01`–`.03`、`02.05.08.04.02.01`–`.04` 入边语境）。
- **Utility pogo block - ATH/CTH/STH/LTH** — **文档事实**：这些页给出 `URW00…URW31` 的 2-row/4-row 命名与 SmarTest 编号方案，与本页的 4-row 块命名配套（`02.03.06.08.03`–`.09` 入边语境）。
- **Release information** — **文档事实**：记录本页 Block 1 pin c15 由 `UGND` 改为 `PGND`（`02.03.01.01` 入边语境）。

## 版本

**文档事实**（`02.03.06.08.02` 的 Functional changes）：

- Introduced in SmarTest 8.3.4
- SmarTest 7.10.2 / 8.4.4：Block 1 的 c15 pin 由 `UGND` 改为 `PGND`。

除此之外没有更细的版本变更记录；更早版本情况文档未覆盖。

## 出处

- `02_System_reference/02.03_DUT_board_design_reference/02.03.06.08.02_Utility_pogo_block_-_Utility_Card__V93000_EXA_Scale_systems.htm`（主文档，含 pin description、block mapping、power supply mapping 与 Functional changes）
- `02.03.06.08.01_Utility_pogo_block_-_Basic_configuration__V93000_EXA_Scale_systems.htm`
- `02.03.04_Utility_lines.htm`、`02.03.05_Utility_power_supplies.htm`、`02.03.03.01_DUT_interface_layout.htm`
- `02.05.08.04_Utility_Card.htm`、`02.05.08.04.01_Utility_Card_sitemap.htm`、`02.05.08.04.03_Utility_Card_functionality_and_features.htm`
- `02.07.05.04.05_GetUtilityLines.htm`、`02.07.05.04.07_SetUtilityLines.htm`
- `02.06.02.02.312_UTSC__UTSC__-__UTility_line_Serial_Configuration.htm`、`02.06.02.02.69_DFUP__DFUP__-__DeFine_Utility_Purpose.htm`、`02.06.02.02.70_DFUT__DFUT__-__DeFine_UTility_line.htm`
