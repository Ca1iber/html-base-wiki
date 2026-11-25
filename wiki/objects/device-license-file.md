---
type: object
title: The device license file
layer: file
stage: project
tags: []
related: []
sources:
  - 02_System_reference/02.04_Model_File_and_Licensing/02.04.05.06_The_device_license_file.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# The device license file

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **5,782 字符逐字取自** `<02_System_reference/02.04_Model_File_and_Licensing/02.04.05.06_The_device_license_file.htm>` 及其子主题 `<02_System_reference/02.04_Model_File_and_Licensing/02.04.01.03.01_Model_file_reference__tester.model.htm>`、`<02_System_reference/02.04_Model_File_and_Licensing/02.04.01.03.02_Model_file_reference__model_legacy.htm>`、`<02_System_reference/02.04_Model_File_and_Licensing/02.04.05.06.02_Device_license_file_syntax.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Device license file syntax）

```
...
GLOBAL

DSL = DevFam_1
DSL_ALTERNATIVE = DevFam_2

...
```

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

**文档事实** device license file 是 licensing-per-device 使用的按 device 划分的许可文件。该机制允许只向 license server 申请某个 device 真正需要的 license。

**文档事实** licensing-per-device 不破坏既有 model file 概念和机制，而是其附加与增强。device license file 只包含 license 相关条目，并沿用 model file 的语法。

**文档事实** licensing-per-device 可离线也可在线工作。

**文档事实** 若 device license file 存在，必须确保其不为空。文件内容覆盖 model file 中所有 license 相关条目。若 device license file 不含任何 licensing capabilities，model file 中的 license 定义会被忽略。

**文档事实** 文件结构是 model file 的子集。它不替代 model file，而是扩展 model file，列出 speed、memory 等需要 license 的特性，test head 等非 license 条目属于 model file。

**文档事实** 使用 licensing-per-device 时，device-directory 下必须有名为 license 的目录，device license file 放在 `<device-directory>/license`。也可用 V93000_LICENSING 环境变量指定文件。

**文档事实** 文档推荐文件扩展名 `.license`，基名可反映测试场景，例如 `finalTest.license`、`waferSort.license`。

**文档事实** 示例 device license file 位于 `/opt/hp93000/soc_<version>/pws/data/per-device-license.def`，该文件说明 device license file 语法并作为示例。

## 典型用法

**文档事实** 可基于示例文件自行开发 device license file，也可使用 Testflow Analyzer Tool，文档推荐后者。

**文档事实** 文件与 model file 一样分为 GLOBAL、IOCHANNEL、BOARDCONF 等 section。GLOBAL section 指定系统类型与系统级可用特性，各 section 定义 license 相关方面。

**文档事实** device license file 只能包含 license 相关条目，其他条目会导致 parser error。每个包含潜在 license 的 section 需要 header，例如 GLOBAL 或 IOCHANNEL，不需要的 section header 必须删除。

**文档事实** GLOBAL section 接受 DSL 与 DSL_ALTERNATIVE。DSL 指定 Device Specific Licensing 与 device family tag。DSL_ALTERNATIVE 在主 tag 的 license 不足时使用，但 pin configuration 仍须按主 tag 正确签名。这两个参数只在 device license file 中有效，model file 中没有。

**文档事实** 存在多个 device license file 时必须指定使用哪一个。指定方式的优先级为环境变量、Workorder Manager、Change Device。V93000_LICENSING 的优先级高于 Edit Device 对话框与 `.technology` 文件中的 `licensing_file`。

**文档事实** license 在软件启动与 change-device 时请求。评估分两步，先评估 model file，再评估 device license file。指定文件加载失败时会报错，model file 的 licensing 信息仍有效。未指定 device license file 时也是如此。

**文档事实** 每次评估并应用 device license file 或 model file 后，report window 显示 `Dev_license_file: <file name>`。经 V93000_LICENSING 指定时，消息会附加 `specified in V93000_LICENSING`。

## 和谁有关

- **文档事实** model file，device license file 使用相同语法且是其子集与扩展，license 相关条目被 device license file 覆盖，但 model file 仍须加载以提供 DUT interface、模拟板连线和其它配置数据。
- **文档事实** License evaluation，该子主题定义两步评估流程，先 model file 后 device license file，并说明文件为空、加载失败与未指定时的行为。
- **文档事实** Device license file syntax，该子主题给出 section 规则、parser error 条件以及 DSL 与 DSL_ALTERNATIVE 参数。
- **文档事实** Defining the device license file to be used，该子主题给出环境变量、Workorder Manager、Change Device 的层级。
- **文档事实** V93000_LICENSING，该环境变量可直接指定 device license file，并具有最高优先级。
- **文档事实** V93000_MODEL，model file 必须位于默认位置或由该环境变量指定。
- **文档事实** Testflow Analyzer Tool，文档把它列为生成 device license file 的推荐工具。
- **文档事实** Licensed V93000 products，需要 license 的 V93000 特性与产品列表在该页。
- **文档事实** Model file reference (tester.model) 与 Model file reference (model/legacy)，语法节逐字收录这两个 model file 示例，用于对照语法与文件结构。

## 版本

**文档事实** Functional changes 记载 Introduced before SmarTest 6.3.2。子主题 Device license file syntax 记载 SmarTest 6.5.2 新增 DSL 参数，SmarTest 7.2.0 新增 DSL_ALTERNATIVE 参数。

## 出处

- `02_System_reference/02.04_Model_File_and_Licensing/02.04.05.06_The_device_license_file.htm`，主源，含 The structure、TAT、Related information 与 Functional changes。
- `02_System_reference/02.04_Model_File_and_Licensing/02.04.05.06.01_License_evaluation.htm`
- `02_System_reference/02.04_Model_File_and_Licensing/02.04.05.06.02_Device_license_file_syntax.htm`
- `02_System_reference/02.04_Model_File_and_Licensing/02.04.05.06.03_Defining_the_device_license_file_to_be_used.htm`
- 语法节子主题 `02_System_reference/02.04_Model_File_and_Licensing/02.04.01.03.01_Model_file_reference__tester.model.htm` 与 `02_System_reference/02.04_Model_File_and_Licensing/02.04.01.03.02_Model_file_reference__model_legacy.htm`。
