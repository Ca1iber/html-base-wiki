---
type: object
title: Setup Management Tool
layer: gui
stage: project
tags: []
related: []
sources:
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02.04_Setup_Management_Tool.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Setup Management Tool

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **4,954 字符逐字取自** `<01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02.04_Setup_Management_Tool.htm>` 及其子主题 `<01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02.04.05.01_Collision_handling_for_the_level_master_file.htm>`、`<01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02.04.05.02_Collision_handling_for_the_timing_master_file.htm>`、`<01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02.04.05.03_Collision_handling_for_the_waveform_master_file.htm>`、`<01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02.04.05.05_Collision_handling_for_the_TMLimits_master_file.htm>`、`<01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02.04.05_Collision_handling.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Collision handling）

See the examples in each kind of setup master file collision handling.

### Examples（取自子主题 Collision handling for the level master file）

### Example1

The original level master file looks like below:

```
Tester File: combination.lev
EQNSET 1: ../../usb/levels/eqnset_01.lev
EQNSET 1: ../../rf/levels/eqnset_01.lev
EQNSET 3: ../../rf/levels/eqnset_03.lev
```

After the automatic collision handling, it will be changed
to:

```
Tester File: combination.lev
EQNSET 1: ../../usb/levels/eqnset_01.lev
EQNSET 1[REMAP 2]: ../../rf/levels/eqnset_01.lev
EQNSET 3: ../../rf/levels/eqnset_03.lev
```

You can re-map the collision equation set number to another one like
below:

```
Tester File: combination.lev
EQNSET 1: ../../usb/levels/eqnset_01.lev
EQNSET 1[REMAP 4]: ../../rf/levels/eqnset_01.lev
EQNSET 3: ../../rf/levels/eqnset_03.lev
```

### Example 2

If you create a new collision when re-mapping manually like
below:

```
Tester File: combination.lev
EQNSET 1: ../../usb/levels/eqnset_01.lev
EQNSET 1[REMAP 3]: ../../rf/levels/eqnset_01.lev
EQNSET 3: ../../rf/levels/eqnset_03.lev
```

After the automatic collision handling, it will be changed
to:

```
Tester File: combination.lev
EQNSET 1: ../../usb/levels/eqnset_01.lev
EQNSET 1[REMAP 3]: ../../rf/levels/eqnset_01.lev
EQNSET 3[REMAP 2]: ../../rf/levels/eqnset_03.lev
```

### Examples（取自子主题 Collision handling for the timing master file）

### Automatically Bind

In this example, the timing files for usb test are in
one directory and the timing files for rf test are in another directory. The collision can be
handled automatically and the related parts will be updated automatically.

Before
assembling, the master file
is:

```
EQNSET 1: ../../usb/timing/eqnset_01.tim
EQNSET 1: ../../rf/timing/eqnset_01.tim
WAVETABLE wtbl_1: ../../usb/timing/part1.tim
WAVETABLE wtbl_1: ../../rf/timing/part1.tim
MULTIPORT_SPEC "spec_1": ../../usb/timing/spec_1.tim
MULTIPORT_SPEC "spec_1": ../../rf/timing/spec_1.tim
CLOCK_SET clset_1: ../../usb/timing/clock_1.tim
CLOCK_SET clset_1: ../../rf/timing/clock_1.tim
```

After
assembling, the master file
is:

```
EQNSET 1: ../../usb/timing/eqnset_01.tim
EQNSET 1[REMAP 2]: ../../rf/timing/eqnset_01.tim
WAVETABLE wtbl_1: ../../usb/timing/part1.tim
WAVETABLE wtbl_1[REMAP wtbl_2]: ../../rf/timing/part1.tim
MULTIPORT_SPEC "spec_1": ../../usb/timing/spec_1.tim
MULTIPORT_SPEC "spec_1"[REMAP "spec_2"]: ../../rf/timing/spec_1.tim
CLOCK_SET clset_1: ../../usb/timing/clock_1.tim
CLOCK_SET clset_1[Remap clset_2]: ../../rf/timing/clock_1.tim
```

### Manually Bind

In this example all the timing files are located in one
directory. The setup management tool does not know which parts need to be updated after collision
resolved. You need to clearly specify the
Bind
 files before assembling.

Before
assembling, the timing master file looks like
below:

```
EQNSET 1: ../../ALL/timing/eqnset_01.tim
EQNSET 1: ../.. /ALL /timing/aaa.tim
[Bind: ../../ ALL /timing/ddd.tim]

WAVETABLE wtbl_1: ../../ ALL /timing/part1.tim
WAVETABLE wtbl_1: ../../ ALL /timing/ddd.tim

MULTIPORT_SPEC "spec_1": ../../ ALL /timing/spec_1.tim
MULTIPORT_SPEC "spec_1": ../../ ALL /timing/cccc.tim
[Bind ../../ ALL /timing/ddd.tim;
../../ ALL /timing/aaa.tim;]

CLOCK_SET clset_1: ../../ ALL /timing/clock_1.tim
CLOCK_SET clset_1: ../.. /ALL /timing/ffff.tim
[Bind ../../ ALL /timing/ddd.tim;
../../ ALL /timing/aaa.tim;]
```

After
assembling, the master file will be changed
to:

```
EQNSET 1: ../../ALL/t"iming/eqnset_01.tim
EQNSET 1[REMAP 2]: ../.. /ALL /timing/aaa.tim
[Bind: ../../ ALL /timing/ddd.tim]

WAVETABLE wtbl_1: ../../ ALL /timing/part1.tim
WAVETABLE wtbl_1 [REMAP wtbl_2]: ../../ ALL /timing/ddd.tim

MULTIPORT_SPEC "spec_1": ../../ ALL /timing/spec_1.tim
MULTIPORT_SPEC "spec_1" [REMAP "spec_2"]: ../../ ALL /timing/cccc.tim
[Bind ../../ ALL /timing/ddd.tim;
../../ ALL /timing/aaa.tim;]

CLOCK_SET clset_1: ../../ ALL /timing/clock_1.tim
CLOCK_SET clset_1 [REMAP "clset_2"]: ../.. /ALL /timing/ffff.tim
[Bind ../../ ALL /timing/ddd.tim;
../../ ALL /timing/aaa.tim;]
```

### Example（取自子主题 Collision handling for the waveform master file）

Before assembling, the waveform master file looks like
below:

```
testerfile: demo.wav
LABEL label_1 : files/label_1.wav
LABEL label_1 : files/label_2.wav
LABEL label_3 : files/label_34.wav
LABELlabel_4 : files/label_34.wav
```

After
assembling, the waveform master file will be changed
to:

```
testerfile: demo.wav
LABEL label_1 : files/label_1.wav
LABEL label_1 [REMAP label_2] : files/label_2.wav
LABEL label_3 : files/label_34.wav
LABEL label_4 : files/label_34.wav
```

### Example（取自子主题 Collision handling for the TMLimits master file）

File
1:

```
"Suite name", "Test name", "Test number", "Units", "Lsl", "Usl", "Test_remarks"
...
"Continuity2", "DC_CONT_P", "555", "UNIT", "-0.1", "0.1", "WalkZP"
...
```

File
2:

```
"Test name", "Suite name", "Test number", "Rem"
...
"DC_CONT_P", "Continuity2", "125", "optional"
...
```

Both
files define the same test, which is identified by the combination of suite name and test name.
(The order of the fields does not matter.)

Only the definition in file 1 is kept (assuming
that file 1 is loaded before file 2); the definition in file 2 is discarded.

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
