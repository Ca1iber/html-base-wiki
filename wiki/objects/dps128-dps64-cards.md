---
type: object
title: DC Scale DPS128/DPS64 cards
layer: n/a
stage: level
tags: []
related: []
sources:
  - 02_System_reference/02.05_Test_Head_Cards/02.05.05.01_DC_Scale_DPS128_DPS64_cards.htm
  - 02_System_reference/02.05_Test_Head_Cards/02.05.05.01.03_DPS128___DPS64_functionality_and_features.htm
  - 02_System_reference/02.05_Test_Head_Cards/02.05.05.01.04_DPS128___DPS64_hardware_overview.htm
  - 02_System_reference/02.05_Test_Head_Cards/02.05.05.01.05_DPS128___DPS64_power_budget.htm
  - 02_System_reference/02.05_Test_Head_Cards/02.05.05.01.09.01_DPS128_and_DPS64_pogo_cabling_and_model_file_configuration.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# DC Scale DPS128/DPS64 cards

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

**文档事实**DPS128 和 DPS64 是 DC Scale 电源家族的成员，可插在任意 I/O channel card slot。文档给出的两个变体是 DPS128‑HC（E8023CS，128 个 HC 通道）与 DPS64‑HC（E8023CSH，64 个 HC 通道），均为 1.0 A、-2.5 V … +7.0 V；每个通道的存储器为 28 Mbit。每个通道可以：在编程电压下 source/sink 电流、测量所供给的电压和电流、为 DUT board 上的外部电路供电、在 test suite 中编程、跨 site 共享（channel sharing）、ganging 以增大供电电流、做连接性检查、检查器件电源状态。

**文档事实**卡有两种工作模式，且同一通道只能选其一：DPS operating mode（DPS+，像标准 DPS 一样在 testflow 执行期间为器件供电）和 PMU operating mode（SIG，像标准 PMU 一样为单个或一组 test suite 临时供电）。DPS 模式是 PMU 模式的超集，只有 DPS 模式能参与 connect/disconnect 序列和 set activation。

**文档事实**功耗方面，卡有两个 power domain，原始电压电源的最大总功率预算为 426 W，均分后每个 domain 213 W；DPS128 每个 domain 由 64 个通道共享，DPS64 为 32 个通道。SmarTest 会限制总功耗，超出 domain 预算会触发错误消息。支持的配置包括 DPS128/DPS64 与 PS1600 等 Smart Scale 代通道卡混插，以及与 UHC4T 混插。

**文档事实**文档区分 HC 与 HV 通道：Hardware view 展示 HC/HV 在功能、量程和限值上的差异；DPS128 的钳位电流不能设为 0.0 A，最小可编程钳位电流为所选电流范围的 20%（HC）或 10%（HV）。

**推断**由变体表与 Hardware view 描述可推出：DPS128 与 DPS64 的差别主要是每卡通道数（128 vs 64），HC/HV 则是同一卡型内的通道类型差异。

**建议**需要核算总功耗时，文档推荐使用 DC Scale DPS128 Power Calculator；高电流通道应按 Limiting voltage ranges 设置电压范围（如 vout_frc_rng），并按 power domain 到通道的映射分配通道，以避免触发功率限制。

## 典型用法

**文档事实**在 DPS 模式下，卡在 testflow 中持续为 DUT 供电；在 PMU 模式下，只在单个或一组 test suite 内临时供电。两种模式共用同一套逐通道能力（force、measure、share、gang、连接性检查）。

**文档事实**在 equation based level setup 中，可通过 DPSPINS 资源设置电压及电压范围，文档给出的写法如：

```
DPSPINS VDD
vout = 1.8
vout_frc_rng = 3.5 #max bump voltage
```

也可在 SIG（PMU）模式下用 SPMU_TASK 的 vForce/vForceRange，例如：

```
SPMU_TASK force;
force.pin("signal1").vForce(1.8 V).vForceRange(1.8 V)
```

**文档事实**DPS128/DPS64 支持多种 pogo cable assembly（E8023PA … E8023PK），每种都要求在 model file 的 POGOCABLING 段做对应配置：E8023PA、E8023PH 无特殊规则；E8023PB/PC/PD/PE/PF/PG/PK 使用 REDIRECT 类型/子类型，并且需要录入 virtual pogo blocks。

**建议**文档建议用 Hardware view 的 Profile、Surge Tracker、ADC 等交互功能观察执行期间的电压/电流波形，并可从 Sample Code view 复制生成的 test method 代码。

## 和谁有关

- `02.05.05_DC_Scale_cards.htm`（DC Scale cards 总览）：把本卡列为 DC Scale 卡之一，是上级分类页。
- `02.07.04.01.234.01.01_SPMU_PIN_TASK.clamp.htm`：clamp 成员函数的适用范围明确写到 DC Scale DPS128/64 卡与 XPS256 卡。
- `02.07.04.01.234.01.04_SPMU_PIN_TASK.connectState.htm`：connectState 目前只用于 DPS128/DPS64 与 XPS256。
- `02.07.04.01.234.01.19_SPMU_PIN_TASK.loadCap.htm`：loadCap 仅在 PMU 模式下由 DPS128/DPS64 与 XPS256 支持。
- `02.07.13.12.02.35_restoreRange.htm`：restoreRange 仅由 DPS128/DPS64 与 XPS256 支持，且只能用于 pattern‑based 模式。
- `02.07.13.12.02.17_iForceRange.htm`、`02.07.13.12.02.42_vForceRange.htm`：这些范围设置函数的适用卡列表包含 DPS128/DPS64。
- `02.07.04.01.24_DC_PROFILING_DEFINE.htm`、`02.07.04.01.27_DC_PROFILING_ON.htm`：对这些卡，profiling 时改变电流测量范围不受支持，measureRange 在 measureType=TM::CURRENT 时被忽略。
- `02.08.04.14.02.03.07.01_DPSPINS_resources.htm`：DPSPINS 的 standard 模式被描述为动态行为与 DPS128/DPS64 类似。
- `02.05.05.03.10.01_XPS256_specific_setup_tasks.htm`：同一 tester.model 中混用 DPS128/DPS64 与 XPS256 不受支持，SmarTest 会报错并忽略所有 XPS256 卡——这是重要的互斥约束。
- `02.07.04.01.43.05_DPS_AUX_TASK.getSurgeTrackerStatus.htm`、`02.07.04.01.43.01.07_DPS_AUX_PIN_TASK.setMode.htm`：surge tracker 支持的卡包括 DPS128/DPS64 与 XPS256。
- `02.04.01.03.02.06_DPS_section.htm`：model file 的 DPS 段把 DCS‑DPS128HC 对应到 DPS128‑HC 与 DPS64‑HC。

## 版本

**文档事实**本页 Functional changes：Introduced in SmarTest 7.2.1；SmarTest 7.2.2：Support of DPS128‑HC/HV 和 DPS128‑HV。

**文档事实**所引子主题另有：功能与特性页记 7.2.1 引入、7.2.2 支持 DPS128‑HC/HV 与 DPS128‑HV、7.6.0 增加 DPS128‑HC 的 Kelvin measurement / force drop measurement；hardware overview 页在 7.3.2 增加 DPS128/DPS64 hardware views 的 Load Capacitance 字段；power budget 页记 7.2.1 引入、7.2.2 支持 HC/HV 与 HV。

## 出处

- `02_System_reference/02.05_Test_Head_Cards/02.05.05.01_DC_Scale_DPS128_DPS64_cards.htm`
- `02_System_reference/02.05_Test_Head_Cards/02.05.05.01.03_DPS128___DPS64_functionality_and_features.htm`
- `02_System_reference/02.05_Test_Head_Cards/02.05.05.01.04_DPS128___DPS64_hardware_overview.htm`
- `02_System_reference/02.05_Test_Head_Cards/02.05.05.01.05_DPS128___DPS64_power_budget.htm`
- `02_System_reference/02.05_Test_Head_Cards/02.05.05.01.09.01_DPS128_and_DPS64_pogo_cabling_and_model_file_configuration.htm`
