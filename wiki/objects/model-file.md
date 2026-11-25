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

（待补）

## 典型用法

（待补）

## 和谁有关

（待补）

## 版本

（待补）

## 出处

（待补）
