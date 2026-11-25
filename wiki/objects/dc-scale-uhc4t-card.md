---
type: object
title: DC Scale UHC4T card
layer: n/a
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.05_Test_Head_Cards/02.05.05.02_DC_Scale_UHC4T_card.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# DC Scale UHC4T card

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **707 字符逐字取自** `<02_System_reference/02.05_Test_Head_Cards/02.05.05.02_DC_Scale_UHC4T_card.htm>` 及其子主题 `<02_System_reference/02.05_Test_Head_Cards/02.05.05.02.04_UHC4T_hardware_overview.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 UHC4T hardware overview）

### UHC4T hardware view

Only the UHC4T supports the Curr Limiter protection
option. Therefore, only the DCS-UHC4T hardware view shows this option and the Equation Set and
Spec Set fields.

The hardware views are interactive.

The
Profile
field
for example, allows you to measure and display current and voltage waveforms during pattern
execution in the Hardware perspective. For details see
`Profiling of DC Scale cards with Hardware view`（raw: `136105.htm`）
.

The
underlying sequences also generate sample test method code for the executed measurement in the
Sample Code view. You can directly copy and paste the code from the view into your test method
program. For details see
`Sample Code view`（raw: `108172.htm`）
.

<!-- 语法节 end -->

## 是什么

**文档事实** DC Scale UHC4T 是面向超高电流的 device power supply（DPS）卡，每卡 4 通道，高功率模式下每通道最大 40 A（每卡 160 A）；通道可在卡内及跨 UHC4T 卡 ganging，以获得更高电流。规格页给出：最大电压 0 V 至 +4 V；单通道最大 source/sink 电流随电压降额——40 A @ 2.0 V、30 A @ 2.5 V、20 A @ 3.0 V、16 A @ 4.0 V；每板最大 160 A @ 2.0 V，系统最大电流为板数 × 160 A。测试流执行时它按普通 DPS 工作；相对普通 DPS，它额外提供用于保护测试设备的若干报警、用于差分电压监测的高速采样器，以及 force/return 线电压降测量。

**文档事实** UHC4T 只支持 DPS operating mode（可作 DPS 与电压表），与其他 DC Scale 卡不同，不支持 PMU operating mode。它支持静态与动态（sequencer 控制）测量；电压测量必须使用高阻（himp）连接状态。卡有两种功率模式：High power（最大 40 A）与 Precision（最大 1.5 A，但电流测量精度更高）。

**文档事实** 功能子主题列出的特性包括：任意数量已装通道跨卡、按任意顺序 ganging；每通道高速采样器（digitizer）用于差分电压测量与波形捕获，且采样器有独立信号 pogo pin；报警与电压降测量等保护功能；fast preload mode；peak mode；支持通道在多个 site 间共享。软件标识符为 `DCS-UHC4T`。

**文档事实** 只有 UHC4T 支持 Curr Limiter protection 选项，因此只有 DCS-UHC4T 的 hardware view 显示该选项以及 Equation Set、Spec Set 字段。

**推断** 从“每通道 40 A、每卡 160 A、可跨卡 ganging”与 Precision 模式 1.5 A 的划分看，UHC4T 的定位是用 ganging 覆盖数十至上百安培的器件供电，同时用 Precision 模式兼顾小电流下的测量精度；文档未直接给出“定位”措辞，此句为归纳。

## 典型用法

**文档事实** 在测试流中把 UHC4T 配置为 DPS operating mode，像标准 DPS 一样给器件供电，并参与 connect/disconnect 序列与 set activation。UHC4T pin 只能配置为 DPS operating mode，使用 DPS Pins editor 配置，且不需要为 UHC4T pin 指定负载电容。

**文档事实** 机台配置：必须在 model file 的 DPS 段与 POGOCABLING 段（legacy `model`），或 `tester.model` 的 CARD_CONFIGURATION 段中定义 UHC4T，软件标识符为 `DCS-UHC4T`。两种 pogo cable：E8013UHP 的四个通道接到合并为一个单元的 pogo 块对，model file 只需填 S1 位置，S2 由软件自动占用；E8024UHPS 的两个 pogo 块可在电缆长度限制内任意安装，需用 `type`/`subtype`/`config` 定义两个块的位置。规格页还要求 UHC4T 使用 universal DC/DC，且相邻卡也必须是 UHC4T（两张卡成对位于奇/偶 card cage slot）。

**文档事实** Ganging 在 DPS Pins editor 中定义：同卡用 `-` 指定通道范围，跨卡用 `,` 分隔各卡通道范围。跨卡 ganging 在 DUT board 上要求把上一卡的 `Gang_out` 接到下一卡的 `Gang_in`（daisy chain，P4→P1）；也可在 pin configuration file 中用 `DDIC` 定义 DUT board 连接、再用 `DFPS` 定义 gang。

**文档事实** 要使用 UHC4T 的全部特性必须使用 equations；基于 equation 的 level setup 提供 UHC4T 专属参数（如多种 connect state）。Level Setup 工具显示 vout、ilimit、t_ms、offcurr、vout_frc_rng、iout_clamp_rng、disable_const_curr_check、connect_state、curr_limiter；除 connect state 与 current limiter mode 外，不显示 fast preload time、voltage drop threshold 等 UHC4T 专属特性。Current limiter protection 通过 DPSPINS resources 的 `protect` 参数在 level setup equations 中启用。

**文档事实** hardware view 是交互式的：Profile 字段可在 Hardware perspective 中测量并显示 pattern 执行期间的电流/电压波形；底层 sequence 还会在 Sample Code view 中生成所执行测量的示例 test method 代码，可直接复制到 test method。

**建议** 首次使用前按 `UHC4T specific setup tasks` 完成 model file、pogo cable、通道分配、pin 配置、ganging 与 equations；具体功率/测量模式与保护设置按对应子主题和器件电流需求选择。

## 和谁有关

- **文档事实** `02_System_reference/02.05_Test_Head_Cards/02.05.05_DC_Scale_cards.htm` 与 `02_System_reference/02.01_Release_Information/02.01.02_V93000_Components_and_Compatibility.htm` 引用本页：前者把 UHC4T 与 DPS128/64、XPS256 并列为 DC Scale 卡家族成员，后者在 V93000 组件与兼容性主题中引用本卡。
- **文档事实** `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.03_XPS256_functionality_and_features.htm` 写明“Massive channel ganging allows replacement of the DC Scale UHC4T card”，即 XPS256 可作为 UHC4T 的替代方案。
- **文档事实** `02_System_reference/02.04_Model_File_and_Licensing/02.04.01.03.02.06_DPS_section.htm` 引用本页：UHC4T 必须在 model file 的 DPS 段中定义，软件标识符为 `DCS-UHC4T`。
- **文档事实** `02_System_reference/02.03_DUT_board_design_reference/02.03.08.01.06_DC_Scale_UHC4___UHC4T_card.htm`、`.../02.03.06.02.06_UHC4___UHC4T_pogo_pin_assignment.htm` 引用本页：前者是 DUT board design reference 中的 UHC4/UHC4T 卡页，后者给出 pogo pin 分配，说明 UHC4T 的 pogo/布线设计约束。
- **文档事实** `02_System_reference/02.06_Command_Reference/02.06.02.02.303_UHCM__UHCM__-__Ultra_High_Current_power_supply_Modes.htm`（及 `.../02.06.10.02.16_UHCM__UHCM__-__Ultra_High_Current_power_supply_Modes.htm`）引用本页：force/return 线电压降测量参数“仅 UHC4T 与 XPS256 支持”。
- **文档事实** `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.02.03.07.01_DPSPINS_resources.htm` 引用本页：其中多个参数标注“仅 UHC4T 支持”或“UHC4T 与 XPS256 支持”，并给出 UHC4T 的 level setup 参数与 `protect`。
- **文档事实** `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.01.03.01_DC_Scale_pin__DPS_mode__setup.htm` 与 `.../02.08.04.14.06.01.03_Using_the_UNGANG_connect_state_with_DC_Scale_DPS_cards.htm` 引用本页：前者是 UHC4T DPS pin 设置，后者说明 UHC4T 的 `UNGANG` connect state 兼具“移出 ganged 组”和“High-power 切 Precision”双重作用。
- **文档事实** `02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.44_vMeasForceDrop.htm` 与 `.../02.07.13.12.02.46_vMeasReturnDrop.htm` 引用本页：这两个成员函数在 UHC4T 的 DPS operating mode 下受支持。
- **文档事实** 本页子主题 `02_System_reference/02.05_Test_Head_Cards/02.05.05.02.03_UHC4T_functionality_and_features.htm`、`.../02.05.05.02.04_UHC4T_hardware_overview.htm`、`.../02.05.05.02.05_UHC4T_specific_setup_tasks.htm`：分别提供功能/特性、硬件视图、机型配置与 setup 细节。

## 版本

**文档事实** 本页 `Functional changes`：`Introduced in SmarTest 6.5.0`；`SmarTest 7.3.2: Introduction of UHC4T`。

**文档事实** 功能与特性子主题、硬件概览子主题的 `Functional changes` 对同一版本记为 `SmarTest 7.3.2: Support of UHC4T`；硬件概览另记 `SmarTest 7.3.2: Measure Voltage Drop and Sampler fields of UHC4 and UHC4T generate sample test method code`。

**文档事实** 规格子主题写明 `The E8024UH UHC4T requires SmarTest 7.3.2 or higher`。

**推断** 两条并列记录中，7.3.2 明确对应 UHC4T 的引入/支持；6.5.0 的 “Introduced” 可能是该 TDC 主题（或 UHC4 系列）的引入版本，文档未进一步说明二者的关系。

## 出处

- `02_System_reference/02.05_Test_Head_Cards/02.05.05.02_DC_Scale_UHC4T_card.htm`（主源：简介、Related information、Functional changes）。
- `02_System_reference/02.05_Test_Head_Cards/02.05.05.02.02_UHC4T_specifications.htm`（通道/电流/电压指标与 pogo/cable 约束）。
- `02_System_reference/02.05_Test_Head_Cards/02.05.05.02.03_UHC4T_functionality_and_features.htm`（DPS 模式、功率/测量模式、特性、equations、profiling、软件标识符）。
- `02_System_reference/02.05_Test_Head_Cards/02.05.05.02.04_UHC4T_hardware_overview.htm`（本页语法节来源；hardware view）。
- `02_System_reference/02.05_Test_Head_Cards/02.05.05.02.05_UHC4T_specific_setup_tasks.htm`（model file、pogo cable、通道分配、pin 配置、ganging、equations、current limiter）。
- 关联判断另参考 `extract/edges.jsonl` 中指向本页的入边。
