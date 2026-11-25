---
type: object
title: Utility power supplies
layer: n/a
stage: project
tags: []
related: []
sources:
  - 02_System_reference/02.03_DUT_board_design_reference/02.03.05_Utility_power_supplies.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Utility power supplies

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

**文档事实** utility power supplies 为 DUT board 或 probe card 上的有源元件（如继电器、运算放大器、buffer）供电。与 device power supplies 不同，它们提供固定电压，不提供可编程 clamp current 或测量功能。

**文档事实** 本页按电压与接口列出可用的 utility power supplies：+5 V 对应所有 utility pogo block 上的 UP5V pin；+5 V、+3.3 V、-5 V 对应所有 4-row utility pogo block 上的 XP... pins；+15 V、-15 V、24 V floating 对应部分 4-row utility pogo block 上的 UPP15V、UPM15V、F24V pins；+5 V、+12 V、+15 V、-15 V 对应 3-row DPS pogo block（Internal Utility Power Option，或 V93000 的 SE-UDPS）。EXA Scale 与 V93000 各有对应子主题，部分接口在 V93000 上为 n.a.。

**文档事实** 所有 utility power supplies 的共性：只能工作在单象限——force 正电压并 source 电流，或 force 负电压并 sink 电流；输出可开或关。因此它们不能在输出端 force 0 V，也不能对 DUT board 上的电路放电。

**文档事实** 由此必须注意：电压降到 0 V 的时间取决于负载与 DUT board 电容，高负载电流缩短该时间，大电容延长该时间；短时间关断电源会造成 critical voltage drop（brownout），可能使数字电路进入未定义状态；已关断 utility line 的内部 pull-up 电阻与 DUT board 上连接电路也可能把已关断电源的输出电压抬到未定义值。

**文档事实** 开关与过载行为按电源不同：EXA Scale 的 UP5V 可经 SmarTest API 同时开关 Utility Card（或内部资源所在卡笼）所有 utility pogo block 的输出；Pin Scale/Smart Scale 兼容设置下第一卡笼或第一 Utility Card 的 UP5V 默认开启，EXA Scale 标准设置下默认关闭。V93000 的 UPV5 在 test head 上电并加载 SmarTest 时自动开启。XP 三路输出在 EXA Scale 上可按输出、按 Utility Card 单独开关，兼容设置下只能成组控制；UPP15V/UPM15V/F24V 四路输出可按输出、按卡单独开关；Internal Utility Power Option 只能成组、按卡开关。过载时，有的电源自动关闭并在故障消除后自动恢复，有的自动关闭后必须用 API 重新使能。

**文档事实** 可切换的 utility power supplies 由 SmarTest 7 的 test method API UTILITY_POWER_STATUS 或 SmarTest 8 的 Device Test API IUtilityPower 控制。

**推断** 因此它是 DUT board 设计用的板级固定电源资源，不是测试程序中可编程的 DPS 通道：文档把它与 device power supplies 明确对立，并强调无 clamp 与测量功能。

## 典型用法

**文档事实** 选型时先按所需电压与接口查 Overview 表：UP5V、XP...、UPP15V/UPM15V/F24V 或 DPS pogo block，再按系统（EXA Scale 或 V93000）进入对应子主题。

**文档事实** 设计 DUT board 时必须按 Common characteristics 处理掉电：不能假设电源会主动把节点拉到 0 V；要按负载电流与 DUT board 电容估算放电时间，并避免短时间关断造成 brownout。

**文档事实** 还需考虑已关断 utility line 的 pull-up 与外部电路可能抬高输出电压；文档要求参考 Utility line characteristics 与 Utility line example circuits。

**文档事实** 需要软件开关时，用 UTILITY_POWER_STATUS（SmarTest 7）或 IUtilityPower（SmarTest 8）；开关粒度与默认状态按 Power on/off behavior 表：UP5V 全卡/卡笼统开，XP 三路可单独（兼容模式下成组），UPP15V/UPM15V/F24V 四路可单独，Internal Utility Power Option 成组。

**文档事实** 使用 Pin Scale/Smart Scale 兼容设置时，EXA Scale 的 UP5V 默认开启；要采用 EXA Scale 标准行为（默认关闭）必须显式启用，脚注指向 Internal utility resources specific setup tasks 与 Utility Card specific setup tasks。

**文档事实** 过载后的恢复策略按电源不同：一类在故障消除后自动恢复，另一类必须用 API 重新使能；Power on/off behavior 表逐项列出。

**建议** 在 DUT board 设计评审中把关断后如何放电、掉电时哪些节点会被 pull-up 抬高、过载后是否需要重新使能列为检查项；这些正是文档明确提醒且没有软件补偿的部分。

## 和谁有关

- **文档事实** UTILITY_POWER_STATUS（test method API）与 IUtilityPower（Device Test API）：本页明写可切换的 utility power supplies 由二者控制。
- **文档事实** UPOW（Utility POWer）：UPOW 页说明 "For information on the utility power supplies see Utility power supplies"（objpack 入边）。
- **文档事实** Utility pogo block - Basic configuration、Utility pogo block - Utility Card、Utility pogo block - LTH/STH/CTH/ATH：本页 pogo pin assignment 表把 UP5V、XP...、UPP15V/UPM15V/F24V 接口链接到这些 pogo block 页。
- **文档事实** Internal Utility Power Option pogo pin assignments 与 SE-UDPS pogo pin assignments：DPS pogo block 上 3-row 电源的 pin 分配页。
- **文档事实** Utility line characteristics 与 Utility line example circuits：本页在说明已关断电源可能被 pull-up/外部电路抬高时引用。
- **文档事实** Internal utility resources specific setup tasks 与 Utility Card specific setup tasks：脚注说明 Pin Scale/Smart Scale 兼容设置与 EXA Scale 新行为的启用位置。
- **文档事实** Utility power supply - UP5V pins、XP pins、UPP15V/UPM15V/F24V pins（EXA Scale），以及 Internal utility power supply、External utility power supply、Internal Utility Power Supply (SE-UDPS)（V93000）：本页各电压/接口与各系统的子主题。
- **文档事实** Release information：该页把本页的四个 EXA Scale 子主题列为 utility power supplies 的发布信息条目（objpack 入边）。

## 版本

**文档事实** Functional changes 记：Introduced in SmarTest 7.5.2；SmarTest 8.3.4 新增 V93000 EXA Scale 系统的 utility power supplies。

## 出处

- `02_System_reference/02.03_DUT_board_design_reference/02.03.05_Utility_power_supplies.htm`，主源，含 Overview、Common characteristics、Pogo pin assignment、Power on/off behavior 与 Functional changes，已用 `show.py` 读取。
- 子主题名称、pogo block 与 API 关系取自该主页的正文/表格链接及 `extract/objpack.py` 入边索引。
