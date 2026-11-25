---
type: object
title: Utility Pins editor
layer: gui
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.01.04_Utility_Pins_editor.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Utility Pins editor

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

**文档事实** Utility Pins editor 用于把 utility pin 名称分配给 utility pogo pin。

**文档事实** 参数表包含以下列：

- Name：pin 的描述性名称，最多 16 个字母数字字符；不允许空格及 `# ; ( ' ) ? @ ,` 这些字符；其他 SmarTest 窗口引用该 pin 时总显示该名称；可通过 test method library（GetUtilityLines、SetUtilityLines）、test method API 或自有 test method 访问。
- Mode：定义 utility line 的工作模式，w 为 write-only、r 为 read-only、rw 为 read-write；只写的线选 w，读写线可按用途选 w、r 或 rw；可选 Utility Card 的 utility line 还可配置为 safety line（triggerIfHigh、triggerIfLow）或 XPS256 硬件 shutdown 的 global shutdown line（triggerSiteIfHigh、triggerSiteIfLow）。
- t[ms]：可选等待时间，从 utility line 状态改变到执行下一动作，例如受控 user-relay 的 settling time；在由 routing set、test method 程序或 UTST firmware 命令控制时生效；同时控制多条线时并行切换并使用最长 settling time；仅在 w 或 rw mode 有效；默认 0 ms；也可在 routing set 中另行设置 wait time。
- Comment：可选的 pin 描述。
- Tester Channel：指定 utility pogo block 与 utility line；前三位是 V93000 EXA Scale 系统的 utility pogo block，后两位是 utility line 号，4-row utility block 合法值为 01…32；文档提醒 01…32 与 UTST firmware 命令及 utility pogo block pin designator 使用的 00…31 不同；复用 utility line 时背景变黄，示例中 VS 在四个 site 共用单个 utility pogo pin 16601。

**文档事实** Related information 列出 Utility lines、Pogo pin assignment - Utility pogo blocks、UTST、FLEX_RELAY、Utility Line view、DUT interface layout。

**推断** 因此该编辑器定义的是 utility line 名称与物理 pogo 通道之间的映射，供命令、API 与 routing set 按名称引用。

## 典型用法

**文档事实** 为每个 utility pogo pin 填写 Name、Mode、可选 t[ms]、Comment 与 Tester Channel。

**文档事实** Name 限制为最多 16 个字母数字字符，且不能包含空格与 `# ; ( ' ) ? @ ,`。

**文档事实** 读写线按用途选 Mode：只写用 w，只读用 r，两种功能都用则选 rw。

**文档事实** 需要 XPS256 硬件 shutdown 时选 triggerIfHigh 或 triggerIfLow（safety line），或 triggerSiteIfHigh 或 triggerSiteIfLow（global shutdown line）。

**文档事实** 若受控 user-relay 需要 settling 时间，设置 t[ms]；该值在 routing set、test method 程序或 UTST 命令控制时使用，也可改用 routing set 中的 wait time。

**文档事实** Routing Tools 的 Utility Lines Config editor 可用 Import 按钮导入本编辑器定义；导入会删除配置表现有全部设置，并连同 comments 从所选 pin configuration file 导入。

**文档事实** Working with the Routing Tools editors 的步骤要求在 Utility Pins editor 中打开，并复制所有 names 与 tester channels 到 Utility Lines Config editor 对应单元；这些 utility pins 必须与本编辑器 Name 列一致。

**建议** 把 Name 当作稳定接口；一旦 test method 或 routing set 按名称引用，改名要同步所有引用处。

## 和谁有关

- **文档事实** SetUtilityLines，其文档说合法名称在 Utility Pins editor 中定义，说明该 API 的 pin 名称来源是本编辑器。
- **文档事实** GetUtilityLines，本页参数说明可通过该 test method library 访问 utility pins。
- **文档事实** Routing Tools - Utility Lines Config editor，其中 utility pins 必须与本编辑器 Name 列一致，且 Import 按钮导入本编辑器定义；本页 Related information 也列出该主题。
- **文档事实** Working with the Routing Tools editors，其步骤明确要求打开本编辑器并复制 names 与 tester channels。
- **文档事实** Utility Line view，本页 Related information 列出，入边也引用本页。
- **文档事实** UTST firmware command，t[ms] 在 UTST 控制时生效；本页并提醒其 line number（00…31）与编辑器（01…32）不同。
- **文档事实** FLEX_RELAY，其文档说可使用本编辑器中定义的 utility line 名称。
- **文档事实** DPS_PIN_TASK，其参数说明指 utility pin 名称在本编辑器中定义（用于开关电容）。
- **文档事实** XPS256 safety line 与 DUT board disconnect，XPS256 文档说 safety line 与 global shutdown 的 utility pins 在本编辑器配置。
- **文档事实** Pin setting editors，把本编辑器与 Digital Pins、DPS Pins、Utility Purpose、Virtual Pins 并列为同级编辑器。
- **文档事实** Utility lines、Pogo pin assignment - Utility pogo blocks、DUT interface layout，本页 Related information 列出这些主题。

## 版本

**文档事实** Functional changes 记载 Introduced in SmarTest 6.5.0。

**文档事实** SmarTest 7.1.3：参数 “Operation Mode” 改为 “Mode”。

**文档事实** SmarTest 7.1.3：参数 “Delay [ms]” 改为 “t[ms]”。

**文档事实** SmarTest 7.10.1：V93000 EXA Scale 系统使用三位 utility pogo block 编号。

**文档事实** SmarTest 7.10.2：Mode 参数新增关键字，用于通过 utility lines 配置 XPS256 pins 的 shutdown。

## 出处

- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.01.04_Utility_Pins_editor.htm`，主源，含首段、参数表、Related information 与 Functional changes。
- `extract/edges.jsonl` 入边，用于 SetUtilityLines、GetUtilityLines、Routing Tools - Utility Lines Config editor、FLEX_RELAY、DPS_PIN_TASK、XPS256 页面等旁证。
