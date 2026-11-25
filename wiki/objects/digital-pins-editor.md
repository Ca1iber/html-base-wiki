---
type: object
title: Digital Pins editor
layer: gui
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.01.02_Digital_Pins_editor.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Digital Pins editor

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **330 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.01.02_Digital_Pins_editor.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Examples

### DC Scale pin (PMU mode) setup

The following table shows an example
configuration for DC Scale pins in PMU mode.

[表]
列: Name | Type | Mode | HW | Connection Set | Comment | Tester Channel
行 1:
  Vdd_1
  dc
  SIG
  DCS-DPS128HC
  
  
  10104
行 2:
  Vdd_2
  dc
  SIG
  DCS-DPS128HC
  
  
  10105-10106

### Utility DC pin setup

<!-- 语法节 end -->

## 是什么

**文档事实** Digital pins 与 PMU operating mode 的 DC Scale pins 在 Digital Pins editor 中配置。

**文档事实** 编辑器主要由 tabular pin configuration area 构成，右上角的 CONTEXT drop-down list 用于选择 mode context。

**文档事实** 在 pin configuration area 中，Name、No、Type 配置 DUT pins；Mode 与 Tester Channel 告诉软件如何配置测试系统通道；HW 显示 tester channel 的硬件信息；Connection Set 提供顺序复用 DC Scale 通道的能力。

**文档事实** Name 是 DUT pin 的描述性唯一名字，最多 64 个 alphanumeric 字符，不允许空格与 #、;、括号、单引号、?、@、, 这些字符，也不建议使用 < 与 >，否则无法保存 Pattern Debug Tool 的配置布局。No 是可选参数，按 DUT 封装定义 pin number。Type 取 off、i、o、io、dc，其中 dc 表示 PMU operating mode 的 DC Scale pin 或 utility DC pin。Mode 取 std、fast、SIG、CMON，其中 std 用于 digital 通道标准模式，fast 用于 Pin Scale 5000 通道，SIG 用于 DC Scale pin 的 PMU operating mode，CMON 仅适用于 XPS256 且把引脚配置为 current monitor 输出。Scaling 仅用于 CMON，定义 XPS256 current monitor 输出的 scaling factor，单位 V/A。

**文档事实** HW 列不可编辑，填入 Tester Channel 后自动显示该通道硬件信息，可能显示 PS1600、PS5000、DCS-DPS128HC、XPS256、DMM。Connection Set 是可选字符串参数，当前不支持。Comment 是可选字符串，用于附加描述。Tester Channel 是接到 DUT 的测试机通道，用五位 channel ID 标识。IO 通道的语法是 aaabb，aaa 是物理 pogo block 号或虚拟 pogo block 号，物理 pogo block 号范围是 101 到 132、201 到 232、301 到 332、401 到 432，bb 是 01 到 16 的通道号。Utility DC pin 的 channel id 是 UTIDC 加三位数，指定 card cage 的 utility block。DC Scale 通道另有 ganging 规则。

**文档事实** DC Scale pin 的 PMU operating mode 设置要求 Type 为 dc、Mode 为 SIG。

## 典型用法

**文档事实** 文档给出的 PMU mode DC Scale pin 示例是 Vdd_1 取 dc、SIG、DCS-DPS128HC、通道 10104，Vdd_2 取 dc、SIG、DCS-DPS128HC、通道 10105-10106。通道范围可用连字符 "-" 指定，也可用逗号 "," 分隔每个通道。

**文档事实** DC Scale 通道 ganging 除 XPS256 外只能在同一个 DC Scale 卡内并联连续通道，串联链可从任意通道开始，最少 2 个连续通道；第一个通道自动设为 master，其余设为 slave。DPS128 与 DPS64 可在卡内任意数量的连续通道上 ganging，但不能跨卡，且通道必须同为 HC 或 HV 类型。XPS256 的 ganging 规则见 XPS256 ganged 的 Ganging characteristics。

**文档事实** 在 DPS128/64 与 XPS256 上，不能在 unganged mode 对 ganged group 执行 current compare；已经激活的 comparator 在 unganged mode 会被静默禁用，文档为免打断 testflow 不发出 error 或 warning，ganged group 恢复后 comparator 的前一状态自动恢复。

**文档事实** Utility DC pin 的通道标识是 UTIDC 后接三位数，指定 card cage 的 utility block。文档的 Utility DC pin setup 小节只有标题，没有给出示例。

**推断** 定义一个 PMU mode 的 DC Scale pin 至少要在同一行填 Name、Type 为 dc、Mode 为 SIG 与 Tester Channel，四者缺一就无法表达文档示例中的完整配置。

**文档事实** 给 pin 命名时应避开文档列出的禁用字符与 < >，否则可能无法保存 Pattern Debug Tool 的配置布局。

## 和谁有关

**文档事实** 它属于 Pin setting editors 家族，与 DPS Pins editor、Utility Pins editor、Utility Purpose Editor、Virtual Pins editor 并列；Pin configuration tool 的 Elements 文档把它列为一个编辑器。

**文档事实** DPS Pins editor 与本编辑器决定 DC Scale 通道的工作模式。XPS256 在 PMU operating mode 下要在本编辑器定义为 Type 为 dc、Mode 为 SIG；DPS operating mode 则用 DPS Pins editor 定义为 device power supply。

**文档事实** XPS256 current monitor 与 XPS256 programming - Current monitor 使用本编辑器的 CMON Mode 与 Scaling 列。

**文档事实** Routing Tools 的 Utility Lines Control editor 要求控制 pin 已在本编辑器定义；文档强烈建议所有 site 的 digital control pin 分配到同一通道。

**文档事实** Connection Set 列定义 connection sets，空字符串为默认 connection set；SmartRDI 的 alarm handling 文档说 connection sets 允许以另一个名字复用引脚或配置原本作为 gang group 的引脚，称为 Ganging on the fly。

**文档事实** 定义 device pin 与 tester resource 的连接、定义 site 数、分配通道、指定 DPS operating range 这些任务都引用本编辑器，见 Task 2 Pin Configuration Setup 与 Defining the pins。

**文档事实** UHC4T specific setup tasks、DPS128/DPS64 functionality and features、PMU operating mode of DC Scale cards、XPS256 operating modes、XPS256 ganged、XPS256 programming - PMU operating mode、XPS256 programming - Ganging 都引用本编辑器的 DC Scale pin (PMU mode) setup。

**文档事实** DC_RESULT_ACCESSOR 同时支持用 DPS Pins editor 定义的 DPS operating mode pins 与用本编辑器定义的 PMU operating mode pins。

## 版本

**文档事实** 在 SmarTest 6.5.0 引入。

**文档事实** SmarTest 7.1.3 把参数 Instrument 改为 HW，移除参数 Ser.R[ohm]，增加 HV mode 选项。

**文档事实** SmarTest 7.2.0 修改 pin name 长度。

**文档事实** SmarTest 7.3.1 增加 Connection Set 参数与 DC Scale PVI8 卡。

**文档事实** SmarTest 7.4.0 增加 DC Scale AVI64 卡。

**文档事实** SmarTest 7.5.0 增加 DC Scale FVI16 卡。

**文档事实** SmarTest 7.10.0 不再支持 PVI8，也不再支持 HV mode 选项。

**文档事实** SmarTest 7.10.1 增加 DC Scale XPS256 卡。

**文档事实** SmarTest 7.10.2 为 XPS256 current monitor 增加 Mode 列的 CMON 选项与 Scaling 列。

## 出处

- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.01.02_Digital_Pins_editor.htm`
