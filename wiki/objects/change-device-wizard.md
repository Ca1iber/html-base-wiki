---
type: object
title: Change Device wizard
layer: gui
stage: project
tags: []
related: []
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.03_Change_Device_wizard.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Change Device wizard

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **250 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.03_Change_Device_wizard.htm>` 及其子主题 `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.03.04_Default_levels_file_for_a_device.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Default levels file for a device）

### .default_levels file

All resources except
vol_diff
 and
voh_diff
 are set to
customized default values.

```
vil = 2250mV
vih = 2500mV

vihh = 7.0V

vol = 2250mV
voh = 2500mV

vt = 2500mV
vcom = 2500mV

rec_swing = 0.800V
rec_offset = 0.500V
```

<!-- 语法节 end -->

## 是什么

**文档事实**：用 Change Device wizard 可以激活一个 device，并编辑该 device 的 technology data。

**文档事实**：该 wizard 可从 93000 菜单打开，也可点击 Change Device 按钮打开。

**文档事实**：其子主题为：`Changing the device with the Change Device button`、`Editing technology data`、`Technology file for a device`、`Default levels file for a device`。

**文档事实**：workspace 可包含一个或多个 device，但同一时间只有一个 active device；换 device 就是激活另一个 device。

**文档事实**：device 根目录下的隐藏文件 `.technology` 定义三类信息：technology 相关设置的源目录、某些系统参数的最大值、pay-per-use 应用的目标 test system model。

## 典型用法

**文档事实**：换 device：点击 Change Device 按钮打开 wizard；在 `Device` 文本框输入 device project 的名称和完整路径（也可点 `Browse` 选取）；点 `Finish`。

**文档事实**：激活后，系统检查该 device project 引用的所有 project 是否都在 workspace 中；缺失时弹出 `Warning` 窗口，可点 `Import missing projects into workspace` 导入。Project Explorer 视图中，被激活的 device 标为 `(current device)`。

**文档事实**：编辑 technology data：从 93000 菜单选 `93000 > Device > Change Device`（或点 Change Device 按钮），输入 device project 的名称和完整路径后点 `Next`；在 `Edit Device` 页修改，点 `Finish` 后写入所选 device 的 `.technology` 文件。

**文档事实**：`Edit Device` 页的字段包括：`Device technology`、`Licensing file`、系统参数最大值、`Preinitialize vector memory to value`（0–255）、`RFI to RFE compatibility mode`、`Pretty-printed analog control file`、`Utility block size`（16 或 32 utility lines per pogo block）、`Optimized Multiport Memory Allocation`。

**文档事实**：源文 Note 警告：改 `.technology` 可能导致加载 setup data 或执行测试出问题——technology data 指定 tester 资源分配，与 device 需求不匹配时，device 之后可能无法编辑或测试。

**文档事实**：预定义 device technology 为 `cmos` 与 `ecl`；其默认 level 可用 device 根目录下可选的 `.default_levels` 文件按 device 定制，device 加载时解析该文件，有语法错误则中止加载。

## 和谁有关

**文档事实**：以下关系都有源文正文、子主题或入边支撑；每条注明为什么相关。

- `Change Device button`（`01_Getting_started/01.01_SmarTest_Work_Center/01.01.10.03_Change_Device_button.htm`）：本页说 wizard 可由该按钮打开，子主题给出按钮的操作步骤。为什么：入口。
- [[new-device-wizard]]：本页 `Related information` 列出 `New Device wizard`，两者是并列的设备向导。
- [[technology-file-for-a-device]]：本页子主题之一；`Edit Device` 页的值写入 `.technology`。为什么：编辑对象。
- `Default levels file for a device`（`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.03.04_Default_levels_file_for_a_device.htm`）：本页子主题之一，讲 `.default_levels` 定制。
- `Editing technology data`（`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.03.02_Editing_technology_data.htm`）：本页子主题，给出改 `.technology` 的步骤。
- `Changing the device with the Change Device button`（`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.03.01_Changing_the_device_with_the_Change_Device_button.htm`）：本页子主题，给出换 device 的步骤。
- [[project-explorer-view]]：被激活的 device 在该视图标 `(current device)`。
- `93000 menu and its tools`（`02_System_reference/02.08_Setup_and_Result_Tools/02.08.02_93000_menu_and_its_tools.htm` 与 `01_Getting_started/01.01_SmarTest_Work_Center/01.01.11.01_93000_menu_and_its_tools.htm`）：两页都回链本页，把 wizard 列为菜单工具之一。
- `Selective Digital Capture Actions require a sufficient number of device cycle sets`（`02_System_reference/02.08_Setup_and_Result_Tools/02.08.01.02.07.02.03.02.03_Selective_Digital_Capture_Actions_require_a_sufficient_number_of_device.htm`）：该页说可在 `93000 > Device > Change Device` 中增加 device cycle set 数（在 technology file 中调 Device cycles，或用 `DSCP` 固件命令）。为什么：本 wizard 是调整 device cycles 的入口之一。
- [[device-license-file]]：`Edit Device` 页的 `Licensing file` 字段填写 device license file。
- `Tools in alphabetical order`（`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04_Tools_in_alphabetical_order.htm`）：回链本页，按字母列出工具。

## 版本

**文档事实**：`Functional changes` 记 `Introduced in SmarTest 6.5.2`。子主题 `Changing the device with the Change Device button` 另记 `SmarTest 6.5.2: Changing the device is done in the Change Device Wizard.`，与本页一致。

## 出处

- 主源：`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.03_Change_Device_wizard.htm`（正文、Subtopics、Related information、Functional changes）。
- 子主题（用于操作步骤与 `.technology`/`.default_levels` 事实）：`02.08.04.03.01_Changing_the_device_with_the_Change_Device_button.htm`、`02.08.04.03.02_Editing_technology_data.htm`、`02.08.04.03.03_Technology_file_for_a_device.htm`、`02.08.04.03.04_Default_levels_file_for_a_device.htm`。
- 关系证据：`extract/objpack.py` 的入边。
