---
type: object
title: The model file
layer: file
stage: project
tags: []
related: []
sources:
  - 02_System_reference/02.04_Model_File_and_Licensing/02.04.01_The_model_file.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# The model file

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **5,716 字符逐字取自** `<02_System_reference/02.04_Model_File_and_Licensing/02.04.01_The_model_file.htm>` 及其子主题 `<02_System_reference/02.04_Model_File_and_Licensing/02.04.01.03.01_Model_file_reference__tester.model.htm>`、`<02_System_reference/02.04_Model_File_and_Licensing/02.04.01.03.02_Model_file_reference__model_legacy.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Model file reference (tester.model)）

The following is an example of a
tester.model
 file:

```
GLOBAL
testhead = TH_8CC
dut_interface = SOC_8GROUP
hpib_interface = vxi11/e5810a/192.168.0.100/gpib0
utility_lines = 64, type=static, pogo_size=16
mux_boards = 8, type=PMUX01, pogoblocks=866,868,870,872,881,883,885,887

CARD_CONFIGURATION
slot = 301, HW=PS1600, pogoblocks=101-108
slot = 303, HW=WSMX, pogoblocks=HS:(231 631) HR:(233 633), type=HD2x32
slot = 310, HW=DPS128, pogoblocks=HC:(201-208)
slot = 116, HW=WSRF, pogoblocks=901-902, source=933
```

The default
tester.model
 provided in

/etc/opt/hp93000/soc/
 is a template model file for illustration purposes
only. For example, the PS5000 card can only be used in EXA
Scale™ test systems. PS1600 and PS5000 cards cannot be installed simultaneously in an EXA Scale™ test system. For details, refer to the dedicated
model file sections for each card using the links in the section
`Detailed model file information`（raw: `55954.htm#_55954__model_file_links`）
.

```
# Example for a tester.model file, see detailed syntax description in the TDC

GLOBAL
testhead = TH_8CC # TH_1CC | TH_2CC | TH_4CC | TH_8CC | TH_9Slot | TH_18Slot | TH_27Slot
dut_interface = SOC_8GROUP # SOC_4GROUP | SOC_8GROUP
hpib_interface = vxi11/e5810a/192.168.0.100/gpib0
# utility_lines = 64, type=static, pogo_size=16
# mux_boards = 8, type=PMUX01, pogoblocks=866,868,870,872,881,883,885,887

CARD_CONFIGURATION
slot = 301, HW = PS1600, pogoblocks = 111-118
slot = 310, HW = DPS128, pogoblocks = HV:(201-208)

# slot = 102, HW = PS1600B, pogoblocks = 125-132
# slot = 310, HW = DPS128, pogoblocks = HC:(201-208)
# slot = 303, HW = DPS64, pogoblocks = HC:(201-204), type=REDIRECT, subtype=E8023PF, config= 1:(201 202) 2:(203 204)
# slot = 304, HW = DPS128, pogoblocks = HC:(225 657 425 857 229 661 429 861), type=REDIRECT, subtype=E8023PC, config=225:(225 657) 425:(425 857) 229:(229 661) 429:(429 861)
# slot = 306, HW = DPS64, pogoblocks = HC:(211 643 212 644), type=REDIRECT, subtype=E8023PD, config=211:(211 643) 212:(212 644)

ETC
# REFERENCECLOCK : input = INTERNAL

DMM
# 1: cardcage=1, type=HP3458A, address=18
# 2: cardcage=2, type=HP3458A, address=19
# 3: cardcage=3, type=HP3458A, address=24
# 4: cardcage=4, type=HP3458A, address=25
# 5: cardcage=5, type=HP3458A, address=26
# 6: cardcage=6, type=HP3458A, address=27
# 7: cardcage=7, type=HP3458A, address=28
# 8: cardcage=8, type=HP3458A, address=29

#End of example model file
```

### Example（取自子主题 Model file reference (model/legacy)）

The following is an example of a
model
 file:

```
GLOBAL
testhead = TH_8CC
dut_interface = SOC
device_maintenance = OFF
multiport = ON
noise_figure = OFF
memory_stacker = OFF
multisite = ON
memorytest = OFF
timing_bundle = w256-d8-r8
psrf_pa_library = OFF
xpressdata = OFF
S&S_value_package = ON
protocol_aware = ON

utility_lines = 256, type = sequencer_controlled, pogo_size = 32

IOCHANNEL

10101-10816:HW = PS1600, speed = max-rate, smem = 224M, diff, tmu, loopback
10901-11616:HW = PS1600, speed = max-rate, smem = 224M, diff, tmu, loopback
11701-12416:HW = PS1600, speed = max-rate, smem = 224M, diff, tmu, loopback
12501-13216:HW = PS1600, speed = max-rate, smem = 224M, diff, tmu, loopback
20101-20816:HW = PS1600, speed = max-rate, smem = 224M, diff, tmu, loopback
20901-21616:HW = PS1600, speed = max-rate, smem = 224M, diff, tmu, loopback
21701-22416:HW = PS1600, speed = max-rate, smem = 224M, diff, tmu, loopback
40901-41616:HW = PS1600, speed = max-rate, smem = 224M, diff, tmu, loopback

DPS

22501-22516: type = DCS-DPS128HC
22601-22616: type = DCS-DPS128HC
22901-22916: type = DCS-DPS128HC
23001-23016: type = DCS-DPS128HC

30101-30316: type = DCS-DPS128HC
30401-30416: type = DCS-DPS128HC
30501-30716: type = DCS-DPS128HC
30801-30816: type = DCS-DPS128HC
30901-32416: type = DCS-DPS128HC

34101-34816: type = DCS-DPS128HC
42501-43216: type = DCS-DPS128HC
45901-46216: type = DCS-DPS128HC

POGOCABLING

101: pogoblocks = "165,166,167,168,169,170,171,172",type=UTILITY
102: pogoblocks = "109,110,111,112,113,114,115,116"
103: pogoblocks = "320,324,303,307,230,226,316,312"
104: pogoblocks = "217,218,219,220,221,222,223,224"
105: pogoblocks = "309,310,425,429,301,302,305,306"
106: pogoblocks = "225,657,229,661", type=REDIRECT,subtype=E8023PD, config="225=225,657;229=229,661"
107: pogoblocks = "311,313,426,427,428,430,431,432"
108: pogoblocks = "409,410,411,412,413,414,415,416"
109: pogoblocks = "209,210,211,212,213,214,215,216"

201: pogoblocks = "304,736,308,740", type=REDIRECT,subtype=E8023PD, config="304=304,736;308=308,740"
202: pogoblocks = "459,460,341,342", type=REDIRECT,subtype=E8023PF, config="5=459, 460;1=341, 342"
203: pogoblocks = "461,462,343,344", type=REDIRECT,subtype=E8023PF, config="6=461, 462;2=343, 344"
204: pogoblocks = "125,126,127,128,129,130,131,132"
205: pogoblocks = "117,118,119,120,121,122,123,124"
206: pogoblocks = "101,102,103,104,105,106,107,108"
207: pogoblocks = "201,202,203,204,205,206,207,208"
208: pogoblocks = "314,315,317,318,319,321,322,323"
209: pogoblocks = "345,346,347,348", type=REDIRECT,subtype=E8023PF, config="3=345, 346;8=347, 348"

# 110: pogoblocks = "304,736,308,740", type=REDIRECT,subtype=E8023PD, config="304=304,736;308=308,740"
# 111: pogoblocks = "459,460,341,342", type=REDIRECT,subtype=E8023PF, config="5=459, 460;1=341, 342"
# 112: pogoblocks = "461,462,343,344", type=REDIRECT,subtype=E8023PF, config="6=461, 462;2=343, 344"
# 113: pogoblocks = "125,126,127,128,129,130,131,132"
# 114: pogoblocks = "117,118,119,120,121,122,123,124"
# 115: pogoblocks = "101,102,103,104,105,106,107,108"
# 116: pogoblocks = "201,202,203,204,205,206,207,208"
# 117: pogoblocks = "314,315,317,318,319,321,322,323"
# 118: pogoblocks = "345,346,347,348", type=REDIRECT,subtype=E8023PF, config="3=345, 346;8=347, 348"
```

<!-- 语法节 end -->

## 是什么

**文档事实** model file 包含 tester 的硬件配置：它指定安装了哪些 test head 卡、这些卡的特性，以及卡到 DUT board 接口 pogo pin 的映射；同时指定测试系统的 reference clock 信号。SmarTest 需要这些信息来为被测测试设置测试系统资源的配置与特性。

**文档事实** 在线模式下 SmarTest 启动时读取 model file，并在 report window 的 MAXIMUM POSSIBLE CONFIGURATION 表中报告检测到的硬件；离线模式下则显示 model file 定义的 requested configuration，并列出所引用或被链接的 model file。

**文档事实** 无论在线还是离线启动，使用的都是同一个 model file：位于默认位置的文件、从默认位置链接到的文件，或由环境变量 `V93000_MODEL` 指定的文件。

**文档事实** model file 的默认位置是 `/etc/opt/hp93000/soc/model`；该路径也可为指向 `/etc/opt/hp93000/soc_common/model` 的链接。文件名依语法为 `model` 或 `tester.model`（见 Model file sections）；如需其他文件名，设置 `V93000_MODEL` 并给出实际文件名（如 `model.offline`）。

**文档事实** 对有 license 要求的测试系统资源与特性，SmarTest 先依据 model file 生成 license 请求，再读取 `*.lic` license 文件向 license server 签出所需 license。

## 典型用法

**文档事实** 每次在线启动生成的模板 `/var/opt/hp93000/soc_<version>/model_template` 展示 maximum possible configuration；基于该模板的 model file 或 device license file 会请求并占用所有可能被用到的 license。

**文档事实** 位于 `/opt/hp93000/soc_<version>/pws/data/model.def` 的示例 model file 演示正确的 model file 语法。

**文档事实** 除 model file 外，可用一个或多个 device license file 实现 licensing-per-device；该机制是 model file 概念的附加与增强，device license file 沿用 model file 语法且只包含 license 相关条目。

**文档事实** 若存在 device license file，其参数会被评估，model file 中任何 licensing 参数都被忽略；文档建议用 Testflow Analyzer Tool (TAT) 开发 device license file。

**文档事实** 语法节示例显示：GLOBAL 段设置 testhead、dut_interface、hpib_interface、utility_lines、mux_boards 等；CARD_CONFIGURATION 段以 `slot = …, HW=…, pogoblocks=…` 描述卡；legacy 的 `model` 格式另有 IOCHANNEL、DPS、POGOCABLING 等段。

**建议** 修改前先读 Editing the model file、Switching model files、Converting legacy model files 等子主题，再按目标语法编辑。

## 和谁有关

- **文档事实** Model file sections — 决定文件名是 `model` 还是 `tester.model`，并给出各 section 的语法细节；本页在文件名说明处指向它。
- **文档事实** Editing the model file、Concepts of logical boards、Converting legacy model files — 本页子主题，分别覆盖编辑、逻辑板概念与旧文件转换。
- **文档事实** Report window — model file 被引用的情况会在 report window 列出（Functional changes 记 SmarTest 6.5.4 这一变化），且在线/离线配置表都在 report window 显示。
- **文档事实** Configuration information in the report window — 引用本页，并用 MAXIMUM POSSIBLE CONFIGURATION 与 REQUESTED CONFIGURATION 两表说明 model file / device license file 的配置呈现。
- **文档事实** Device license file — 沿用 model file 语法，是其子集与增强；存在时覆盖 model file 的 licensing 参数。
- **文档事实** System .lic license files、License Management — model file 生成 license 请求后由 `*.lic` 文件完成签出，License Management 页把 model file 列为其中一环。
- **文档事实** Testflow Analyzer Tool (TAT) — 文档推荐用它开发 device license file。
- **文档事实** V93000_MODEL、SmarTest environment variables — 前者指定非默认的 model file，后者是 model file 指定方式的说明页。
- **文档事实** Technology file for a device — 说明 "memory 在所有 model file 中可用的 DC Scale 卡上预留"。
- **文档事实** DPS128/DPS64 pogo cabling and model file configuration、PSSL pogo cable assembly — 说明 model file 的 DPS、POGOCABLING 等段需要特定条目。
- **文档事实** Direct DMM high-accuracy voltage measurements — 说明把 DMM 集成进 model file 需在 GLOBAL 指定 hpib_interface 并添加 DMM 段。
- **文档事实** Internal Utility Power Supply (SE-UDPS) — 说明 SE-UDPS 需在 model file 的 DPS 段与 POGOCABLING 段定义。
- **文档事实** Configuration for digital cards、Configuration for DPSs — 引用本页，说明 model file 或 device license file 启用所需资源与特性。

## 版本

**文档事实** Functional changes 记载：Introduced before SmarTest 6.3.2；SmarTest 6.5.4：Report window 列出所引用的 model file；SmarTest 7.5.3：model file 使用说明更新。

## 出处

- `02_System_reference/02.04_Model_File_and_Licensing/02.04.01_The_model_file.htm`，主源，含文件位置、license 请求、Detailed model file information 与 Functional changes。
- 语法节子主题 `02_System_reference/02.04_Model_File_and_Licensing/02.04.01.03.01_Model_file_reference__tester.model.htm`。
- 语法节子主题 `02_System_reference/02.04_Model_File_and_Licensing/02.04.01.03.02_Model_file_reference__model_legacy.htm`。
