---
type: object
title: Event Formatter
layer: gui
stage: results
tags: []
related: []
sources:
  - 02_System_reference/02.10_Data_Logging/02.10.02_Event_Formatter.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Event Formatter

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **4,841 字符逐字取自** `<02_System_reference/02.10_Data_Logging/02.10.02_Event_Formatter.htm>` 及其子主题 `<02_System_reference/02.10_Data_Logging/02.10.02.04_Shmoo_output_of_the_Event_Formatter.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Shmoo output of the Event Formatter）

A shmoo data log shown with Event Formatter is similar to the one
below.

```
======== Started Testsuite Shmoo_2D ============================================

******** Started Site : 1 ******************************************************
Equation Set 512; Spec Set 256; Timing Set 256
Equation Set 512; Spec Set 512; Level Set 512
Startlabel: spec_search

-------- Test Name: 714 parameters[1] -----------------------------------------
-------- Shmoo -----------------------------------------------------------------
Title: 714 parameters
Test Mode: pass/fail,cycle error count
Result Pins: @
Result Resolution: 1.000000
Description:

........ Shmoo Axis Information ................................................
X-Axis
TotalSteps: 10
LinearSteps: 1
Test Range: [0.000000 ... 1.000000]
Scale: Linear
=> Step Ratio: 0.100000
PrimaryValue: 0.500000
Parameter: Spec Variable
Spec: LEV.2.VIL[V]
SetupPins: I/O0,I/O1
Description:

Y-Axis
TotalSteps: 10
LinearSteps: 1
Test Range: [0.000000 ... 10.000000]
Scale: Linear
=> Step Ratio: 1.000000
PrimaryValue: 5.000000
Parameter: Spec Variable
Spec: TIM.2.tpd_CP_IOx[ns]
SetupPins: @
Description:

........ Shmoo Matrix ..........................................................
' ' = point not calculated
'.' = point passed
'*' = point failed
'E' = point returned an error

Shmoo Pin Number : 1
Shmoo TestMode Number : 2
Shmoo Pin Names : @;
Shmoo Test Modes : pass/fail;cycle error count;

Number Of Cells : 121

Pin: @, TestMode : pass/fail

00000000001
...........
01234567890
00000000000
00000000000
+---------->
0.000|...........
1.000|...........
2.000|...........
3.000|...........
4.000|...........
5.000|...........
6.000|...........
7.000|...........
8.000|...........
9.000|...........
10.000v...........

Pin: @, TestMode : cycle error count

0 0 0 0 0 0 0 0 0 0 1
. . . . . . . . . . .
0 1 2 3 4 5 6 7 8 9 0
0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0
+------------------------------------------->
0.000| 0 0 0 0 0 0 0 0 0 0 0
1.000| 0 0 0 0 0 0 0 0 0 0 0
2.000| 0 0 0 0 0 0 0 0 0 0 0
3.000| 0 0 0 0 0 0 0 0 0 0 0
4.000| 0 0 0 0 0 0 0 0 0 0 0
5.000| 0 0 0 0 0 0 0 0 0 0 0
6.000| 0 0 0 0 0 0 0 0 0 0 0
7.000| 0 0 0 0 0 0 0 0 0 0 0
8.000| 0 0 0 0 0 0 0 0 0 0 0
9.000| 0 0 0 0 0 0 0 0 0 0 0
10.000v 0 0 0 0 0 0 0 0 0 0 0

Executed Testmethod ac_tml.AcTest.Shmoo on Site 1: PASSED
******** Ended Site : 1 ******************************************************

******** Started Site : 2 ******************************************************
Equation Set 512; Spec Set 256; Timing Set 256
Equation Set 512; Spec Set 512; Level Set 512
Startlabel: spec_search

-------- Test Name: 714 parameters[1] -----------------------------------------
-------- Shmoo -----------------------------------------------------------------
Title: 714 parameters
Test Mode: pass/fail,cycle error count
Result Pins: @
Result Resolution: 1.000000
Description:

........ Shmoo Axis Information ................................................
X-Axis
TotalSteps: 10
LinearSteps: 1
Test Range: [0.000000 ... 1.000000]
Scale: Linear
=> Step Ratio: 0.100000
PrimaryValue: 0.500000
Parameter: Spec Variable
Spec: LEV.2.VIL[V]
SetupPins: I/O0,I/O1
Description:

Y-Axis
TotalSteps: 10
LinearSteps: 1
Test Range: [0.000000 ... 10.000000]
Scale: Linear
=> Step Ratio: 1.000000
PrimaryValue: 5.000000
Parameter: Spec Variable
Spec: TIM.2.tpd_CP_IOx[ns]
SetupPins: @
Description:

........ Shmoo Matrix ..........................................................
' ' = point not calculated
'.' = point passed
'*' = point failed
'E' = point returned an error

Shmoo Pin Number : 1
Shmoo TestMode Number : 2
Shmoo Pin Names : @;
Shmoo Test Modes : pass/fail;cycle error count;

Number Of Cells : 121

Pin: @, TestMode : pass/fail

00000000001
...........
01234567890
00000000000
00000000000
+---------->
0.000|...........
1.000|...........
2.000|...........
3.000|...........
4.000|...........
5.000|...........
6.000|...........
7.000|...........
8.000|...........
9.000|...........
10.000v...........

Pin: @, TestMode : cycle error count

0 0 0 0 0 0 0 0 0 0 1
. . . . . . . . . . .
0 1 2 3 4 5 6 7 8 9 0
0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0
+------------------------------------------->
0.000| 0 0 0 0 0 0 0 0 0 0 0
1.000| 0 0 0 0 0 0 0 0 0 0 0
2.000| 0 0 0 0 0 0 0 0 0 0 0
3.000| 0 0 0 0 0 0 0 0 0 0 0
4.000| 0 0 0 0 0 0 0 0 0 0 0
5.000| 0 0 0 0 0 0 0 0 0 0 0
6.000| 0 0 0 0 0 0 0 0 0 0 0
7.000| 0 0 0 0 0 0 0 0 0 0 0
8.000| 0 0 0 0 0 0 0 0 0 0 0
9.000| 0 0 0 0 0 0 0 0 0 0 0
10.000v 0 0 0 0 0 0 0 0 0 0 0

Shmoo picture has been saved in: /home/Devices/74HC299/shmoo/shmooPNG/shmoo_2D
Executed Testmethod ac_tml.AcTest.Shmoo on Site 2: PASSED
******** Ended Site : 2 ******************************************************

======== Ended Testsuite Shmoo_2D ==============================================
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
