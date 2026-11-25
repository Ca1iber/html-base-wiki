---
type: object
title: Utility Card
layer: n/a
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.05_Test_Head_Cards/02.05.08.04_Utility_Card.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Utility Card

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

**文档事实**Utility Card 在八个 4‑row pogo block 上提供 256 条 utility line 和若干 utility 电源，可安装在 V93000 EXA Scale 系统的任意 slot。有两个变体：EK051 与 EK051A；EK051 仅用于 SmarTest 8，EK051A 用于 SmarTest 7（7.10 及以上）和 SmarTest 8。

**文档事实**EXA Scale 基本配置只有少量 internal utility resources：32 条静态控制的 utility line、一个 +5 V utility 电源，以及 legacy SE‑UDPS 的替代。可选的 Utility Card 取代内部 utility line 与内部 +5 V 电源，提供：256 条动态控制的 utility line、一个可提供更大电流的 +5 V 电源、legacy External utility power supply 的替代、一个提供 +15 V / ‑15 V 的电源，以及两个浮动的 24 V 电源。可安装多张 Utility Card 以扩展资源。

**文档事实**功能与特性页（EK051A）细化：256 条 utility line 为 open drain 输出、每线 100 mA、动态（sequencer）控制；电源包括 UP5V +5.0 V/8.0 A，XP pins +5.0 V/12.8 A、+3.3 V/6.0 A、‑5.0 V/6.0 A，UPP15V +15.0 V/3.0 A、UPM15V ‑15.0 V/3.0 A、F24VA/F24VB 24 V/1.0 A。所有 utility 电源都通过 utility pogo block 的独立 sense pin 做 remote sensing。第一张卡的 utility pogo block 为 165–172（UTIL 1–8）；第二张卡占用 265–272 号位置（文档表中这些位置对应 DPS 1–8 槽，顺序为 265=DPS 3、266=DPS 1、267=DPS 2、268=DPS 8、269=DPS 4、270=DPS 5、271=DPS 6、272=DPS 7）。

**推断**由于第二张卡占用 legacy DPS pogo block，安装第二张卡后 Internal Utility Power Option 无法使用——UTILITY_POWER_STATUS 的边说明“second optional Utility Card occupies all (legacy) DPS pogo blocks”可佐证。

## 典型用法

**文档事实**Utility Card 的 utility line 由 pattern sequencer 控制：在 SmarTest 7 的 EXA Scale 上通过 pogo block 的串行接口 pin（FRAMn、SCLK、SINP）由 DUT board 上的数字 pin 驱动；在 SmarTest 8 上整个数据传输由 SmarTest 内部处理，接口不应再接数字 pin。

**文档事实**软件接口：GetUtilityLines / SetUtilityLines 读写 utility line；GET_UTILITY_LINES_STATUS 读状态；UTILITY_SEQ_MODE 与 UTILITY_SEQ_STATIC_MASK 涉及 pogoBlock 选择；UTILITY_POWER_STATUS 和 UPOW 控制/查询 utility 电源，resourceID 1/2 分别对应第一/第二张卡（或第一/第二卡笼的内部电源）。

**文档事实**Utility Pins editor 中，Utility Card 的 utility line 还可配置为 safety line 或 global shutdown line，用于硬件控制地关断 XPS256 pin。

**文档事实**安装两张卡时，第二张卡只能使用三位格式的 pogo block 号：GetUtilityLines 中范围为 265…272，SetUtilityLines 中 pin 名为 UTI26501…UTI27232。

【文档事实/约束】在 SmarTest 7 且安装多于一张 Utility Card 时，不支持跨 Utility Card ganging utility block。

## 和谁有关

- `02.05.08.03_Internal_utility_resources_-_V93000_EXA_Scale_systems.htm`：基本配置的内部资源，是 Utility Card 要取代/扩展的对象。
- `02.03.06.08.02_Utility_pogo_block_-_Utility_Card__V93000_EXA_Scale_systems.htm`：Utility Card 的资源到八个 block 的 pin 分配。
- `02.03.04.05_Sequencer-controlled_utility_lines.htm` 及 `...05.01_Serial_interface_for_sequencer-controlled_utility_lines.htm`、`...05.06_Setting_up_sequencer_control_of_utility_lines.htm`：sequencer 控制由 Utility Card 提供，并分别描述 SmarTest 7 串行接口与 SmarTest 8 内部数据路径。
- `02.03.04.05.03_Ganging_utility_blocks.htm`：EXA Scale + Utility Card 的 ganging 规则，以及跨卡 ganging 不支持。
- `02.07.05.04.05_GetUtilityLines.htm`、`02.07.05.04.07_SetUtilityLines.htm`：第二张卡的三位格式 block 号与 pin 名范围。
- `02.07.04.01.265.02_UTILITY_SEQ_MODE.pogoBlock.htm`、`02.07.04.01.266.02_UTILITY_SEQ_STATIC_MASK.pogoBlock.htm`：pogoBlock 1…8 对应第一张 Utility Card。
- `02.07.04.01.264_UTILITY_POWER_STATUS.htm`（及 `.state`/`.checkState`）、`02.06.12.02.06_UPOW`：Utility Card 电源控制/查询，resourceID 1/2 选择卡。
- `02.08.04.18.03.01.04_Utility_Pins_editor.htm`：safety line / global shutdown 配置。
- `02.03.03.01_DUT_interface_layout.htm`：Utility Card 只能使用 alternate pogo block 号，第二张卡保留 265…272。
- `02.05.01.04_Pogo_mapping.htm`：EXA Scale 的 DPS 槽 pogo block 用于 Internal Utility Power Option 或第二张 Utility Card。
- `02.03.08.01.01.02_AVI64_safety_pogo_pins.htm`：XP pin 的 +5 V 为可选，EXA Scale 至少需一张 Utility Card。
- `02_System_reference/02.05_Test_Head_Cards/02.05.08.01_External_utility_power_supply.htm`：Utility Card 取代 legacy 外部 utility 电源。

## 版本

**文档事实**定义页 Functional changes：Introduced in SmarTest 7.10.0。子主题（Utility Card specifications、Utility Card functionality and features）同样记 Introduced in SmarTest 7.10.0。

## 出处

- `02_System_reference/02.05_Test_Head_Cards/02.05.08.04_Utility_Card.htm`
- `02_System_reference/02.05_Test_Head_Cards/02.05.08.04.02_Utility_Card_specifications.htm`
- `02_System_reference/02.05_Test_Head_Cards/02.05.08.04.03_Utility_Card_functionality_and_features.htm`
