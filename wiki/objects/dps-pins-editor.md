---
type: object
title: DPS Pins editor
layer: gui
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.01.03_DPS_Pins_editor.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# DPS Pins editor

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **344 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.01.03_DPS_Pins_editor.htm>` 及其子主题 `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.01.03.01_DC_Scale_pin__DPS_mode__setup.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example

See
`DC Scale pin (DPS mode) setup`（raw: `105676.htm`）

### Example（取自子主题 DC Scale pin (DPS mode) setup）

The following table shows the configuration for DC Scale pins.

[表]
列: Name | Pol | C[uF] | HW | Comment | Tester Channel
行 1:
  Site 1
  Site 2
行 2:
  Vdd_DPS1
  POS
  0.0
  DCS-DPS128HC
  
  10101
  10104
行 3:
  Vdd_DPS2
  POS
  0.0
  DCS-DPS128HC
  2 channels ganged
  10102-10103
  10105-10106

<!-- 语法节 end -->

## 是什么

**文档事实** DPS Pins editor 是 SmarTest 的 pin 设置编辑器之一，用于配置以 DPS 工作模式使用的 DC Scale pin。Pin setting editors 父页把它与 Digital Pins editor、Utility Pins editor、Utility Purpose Editor、Virtual Pins editor 并列。pin 信息输入在对应 Pin setting editor 的 pin configuration 区，多 site 测试时所有 site 的 tester channel 都显示在 pin setting editor 中。

**文档事实** 参数表列出 Name、Pol、C[uF]、HW、Comment、Tester Channel。Name 是 DUT pin 的描述名，最多 16 个字母数字字符，不允许空格以及 `#`、`;`、`(`、`'`、`)`、`?`、`@`、`,`。Pol 指定 DPS pin 的极性，为 POS。

**文档事实** C[uF] 是负载电容，可留空或按 DPS 类型填写。HW 列不可编辑，输入 tester channel 后自动显示该通道的硬件信息，可能显示 DCS-DPS128HC、DCS-UHC4T、DCS-XPS256。Comment 为可选的描述。Tester Channel 指定 DPS 通道。

**文档事实** DC Scale 卡可位于任意 I/O 通道卡槽，因此 DC Scale 通道的编号规则与 IO 通道相同。

**文档事实** 除 XPS256 外，只能在同一 DC Scale 卡内对连续通道做 gang，即并行连接。gang 链可从任意通道开始，至少包含 2 个连续通道，可用 `-` 表示范围，或用 `,` 分隔各通道。序列中第一个通道自动设为主通道，其余设为从通道。

**文档事实** 各 DC Scale 卡的 gang 规则不同。DPS128 与 DPS64 只能在同一卡内对任意数量的连续通道做 gang，不能跨卡，且通道类型必须同为 HC 或 HV。UHC4T 可在同一卡内以及同一 test head 内跨卡做 gang，跨卡时用逗号分隔各卡的通道范围。XPS256 的 ganging 见 XPS256 ganged 页的 Ganging characteristics 节。

**文档事实** 在 DPS128、DPS64 与 XPS256 上，不能在 unganged 模式下对 ganged 通道组执行 current compare。已激活的比较器在 unganged 模式下被静默禁用，不给出错误或警告，以避免中断 testflow。ganged 组恢复后，比较器原状态自动恢复。

## 典型用法

**文档事实** DPS 工作模式下的 DC Scale pin 在 DPS Pins editor 中配置，配置含 Name、Pol、C[uF]、HW、Comment、Tester Channel，Pol 须为 POS。

**文档事实** 文档给出 Site 1 与 Site 2 的配置示例。Vdd_DPS1 的 Pol 为 POS，C[uF] 为 0.0，HW 为 DCS-DPS128HC，Site 1 通道为 10101，Site 2 通道为 10104。Vdd_DPS2 的 Pol 为 POS，C[uF] 为 0.0，HW 为 DCS-DPS128HC，Comment 为 2 channels ganged，Site 1 通道为 10102-10103，Site 2 通道为 10105-10106。

**文档事实** C[uF] 对 DPS128、DPS64 或 XPS256 可填负载电容，细节见两个 Load capacitance 子主题。UHC4T pin 无需指定负载电容。

**文档事实** UHC4T pin 只能配置为 DPS 工作模式，用 DPS Pins editor 配置。

**文档事实** 要使用 SmartRDI 的 connect() 或 DC Scale DPS 相关 API，DC Scale pin 必须已在 DPS Pins editor 中配置为 DPS 工作模式。该函数不支持 DC Scale pin 的 PMU 工作模式。

**建议** 做 ganging 时按卡类型遵守连续通道规则，DPS128 与 DPS64 不要跨卡，UHC4T 跨卡时用逗号分隔各卡通道范围。

## 和谁有关

**文档事实** Pin setting editors 父页 `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.01_Pin_setting_editors.htm`。它把 DPS Pins editor 与 Digital Pins editor、Utility Pins editor、Utility Purpose Editor、Virtual Pins editor 并列为 pin 设置编辑器，并说明 pin 参数在各自的 pin configuration 区输入。

**文档事实** DC Scale pin (DPS mode) setup `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.01.03.01_DC_Scale_pin__DPS_mode__setup.htm`。它是本页的示例与子主题，详细说明 DPS 模式 DC Scale pin 的配置与 ganging 规则。

**文档事实** Load capacitance connected to the DC Scale DPS128/DPS64 `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.01.03.02_Load_capacitance_connected_to_the_DC_Scale_DPS128_DPS64.htm` 与 Load capacitance connected to the DC Scale XPS256 `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.01.03.03_Load_capacitance_connected_to_the_DC_Scale_XPS256.htm`。它们规定 C[uF] 是否以及如何填写。DPS128 与 DPS64 以及 XPS256 上在 C[uF] 输入电容会对 DPS 模式通道生效，SmarTest 会据负载电容自动设定性能范围，XPS256 会把所设值自动限制到其当前电流量程允许的最大值。

**文档事实** DC Scale DPS128/DPS64 cards、DC Scale UHC4T card、DC Scale XPS256 card `02_System_reference/02.05_Test_Head_Cards/02.05.05.01_DC_Scale_DPS128_DPS64_cards.htm`、`02_System_reference/02.05_Test_Head_Cards/02.05.05.02_DC_Scale_UHC4T_card.htm`、`02_System_reference/02.05_Test_Head_Cards/02.05.05.03_DC_Scale_XPS256_card.htm`。它们是 DPS 模式 setup 的 Related information，提供硬件能力与工作模式依据。

**文档事实** UHC4T specific setup tasks `02_System_reference/02.05_Test_Head_Cards/02.05.05.02.05_UHC4T_specific_setup_tasks.htm`。它说明 UHC4T pin 只能用 DPS Pins editor 配置为 DPS 模式，无需负载电容，ganging 组也在 DPS Pins editor 中定义。

**文档事实** XPS256 operating modes 与 XPS256 in DPS operating mode `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.05_XPS256_operating_modes.htm`、`02_System_reference/02.05_Test_Head_Cards/02.05.05.03.05.01_XPS256_in_DPS_operating_mode.htm`。它们说明 XPS256 通道在 DPS Pins editor 中定义为 device power supply 即处于 DPS 模式。

**文档事实** XPS256 programming - DPS operating mode `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.07_XPS256_programming_-_DPS_operating_mode.htm`。它说明 XPS256 pin 在 DPS Pins editor 中定义为 device power supply 即为 DPS 模式，且与其他 DC Scale 卡一样 Pol 须设为 POS。

**文档事实** DPS operating mode of DC Scale cards 与 Pin configuration and level setup in DPS operating mode `02_System_reference/02.05_Test_Head_Cards/02.05.05.04_DPS_operating_mode_of_DC_Scale_cards.htm`、`02_System_reference/02.05_Test_Head_Cards/02.05.05.04.02.02_Pin_configuration_and_level_setup_in_DPS_operating_mode.htm`。它们说明 DPS 模式 pin 配置与 level setup 的流程，具体 setup 步骤指向本页。

**文档事实** Hardware view diagram of DC Scale channels in DPS operating mode `02_System_reference/02.05_Test_Head_Cards/02.05.05.04.01_Hardware_view_diagram_of_DC_Scale_channels_in_DPS_operating_mode.htm`。它引用 DPS Pins editor，说明 DPS 模式通道的硬件视图。

**文档事实** SmartRDI connect `02_System_reference/02.07_Test_Method_Reference/02.07.13.12.02.03_connect.htm` 与 `02_System_reference/02.07_Test_Method_Reference/02.07.13.12.01.03.03_connect.htm`。它们说明 connect() 只用于在 DPS Pins editor 中配置为 DPS 模式的 DC Scale pin，不支持 PMU 模式。

**文档事实** DC_RESULT_ACCESSOR `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.28_DC_RESULT_ACCESSOR.htm`。它同时支持 DPS Pins editor 定义的 DPS 模式 pin 与 Digital Pins editor 定义的 PMU 模式 pin。

**文档事实** DPS_PIN_TASK `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.50.01_DPS_PIN_TASK.htm`。它说明临时设定的负载电容在测量后自动恢复为 DPS Pins editor 或 DPSPINS resources 中定义的原值。

## 版本

**文档事实** 主页 Functional changes 记载，Introduced in SmarTest 6.5.0。7.1.3 把参数 Polarity 改为 Pol，把 Load Capacitor [uF]/V-Ramp [us] 改为 C[uF]，把 Instrument 改为 HW。7.3.1 增加 DC Scale PVI8 卡，7.3.2 增加 DC Scale UHC4T 卡，7.4.0 增加 DC Scale AVI64 卡，7.5.0 增加 DC Scale FVI16 卡，7.10.1 增加 DC Scale XPS256 卡。

**文档事实** 子主题 DC Scale pin (DPS mode) setup 的 Functional changes 记录 6.5.0 起 DPS 模式的 DC Scale pin 在 DPS Pins editor 中设置，7.1.3 的三项改名与主页一致，并有 PVI8 7.3.1、AVI64 7.4.0、FVI16 7.5.0 三条。该子主题的列表没有 UHC4T 的 7.3.2 与 XPS256 的 7.10.1 两条。

**文档事实** 子主题 Load capacitance connected to the DC Scale DPS128/DPS64 的 Functional changes 记载，Introduced in SmarTest 7.2.3，负载电容参数在 7.2.3.2 patch 中支持。子主题 Load capacitance connected to the DC Scale XPS256 记载，Introduced in SmarTest 7.10.1。

## 出处

- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.01.03_DPS_Pins_editor.htm`。主源，含参数表、示例、Functional changes。
- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.01.03.01_DC_Scale_pin__DPS_mode__setup.htm`。用于 DPS 模式配置、ganging 规则与示例。
- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.01.03.02_Load_capacitance_connected_to_the_DC_Scale_DPS128_DPS64.htm` 与 `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.01.03.03_Load_capacitance_connected_to_the_DC_Scale_XPS256.htm`。用于 C[uF] 行为与版本。
- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.01_Pin_setting_editors.htm`。用于确认编辑器归类。
