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

**文档事实**：Setup Management Tool 让多个用户并行处理同一 setup component 的不同部分而互不干扰。即使每个用户都需要访问完整 setup component，只要不改同一部分，也可用它做分布式 setup 开发与调试。

**文档事实**：它可处理以下 setup component：Level setup、Timing setup、Testflow setup、TMLimits test table setup。

**文档事实**：该工具通过「setup component 被加载或保存时调用的脚本」集成进 Test Program Explorer；也可以从命令行或由用户程序调用。

**文档事实**：本页的子主题为 `Concept of the Setup Management Tool`、`Using the Setup Management Tool from the Test Program Explorer`、`Using the Setup Management Tool from the Command Line`、`Creating a level master file`、`Collision handling`。

## 典型用法

**文档事实**：核心场景是多个用户各自维护 setup component 的子文件，再由 master file 合并。本页 `Collision handling` 子主题给出四类 master file 的冲突处理示例：

- **level master file**：重复的 `EQNSET` 在 assemble 时被改写为 `EQNSET 1[REMAP 2]` 形式；也可手工把冲突的 equation set 号 remap 到别的号；若手工 remap 又造成新冲突，工具会继续自动处理。
- **timing master file**：分「Automatically Bind」（各用户的 timing 文件在不同目录，工具可自动判断需要更新的部分，并改写 `EQNSET`、`WAVETABLE`、`MULTIPORT_SPEC`、`CLOCK_SET`）与「Manually Bind」（文件都在同一目录，工具无法判断，需要先用 `[Bind ...]` 明确指定）。
- **waveform master file**：重复的 `LABEL` 被改写为 `LABEL label_1 [REMAP label_2]`。
- **TMLimits master file**：同一 test 由 suite name 与 test name 的组合识别（字段顺序无关）；只保留先加载文件中的定义，后加载文件中的同 test 定义被丢弃。

**文档事实**：操作入口有两条——从 Test Program Explorer 或从命令行，分别由两个子主题说明。

## 和谁有关

**文档事实**：以下关系均有来源文档中的正文或回链证据支撑。

- [[test-program-explorer]]：本页明确说工具通过 TPE 在加载/保存 setup component 时调用的脚本集成进 TPE。
- [[pin-configuration-master-file]]：该页说明 pin configuration 可由 master file 合并各子文件，并提到 Setup Management Tool（回链证据）。
- `Level setup master file`（`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.14.02.05_Level_setup_master_file.htm`）、`Timing setup master file`（`02.08.04.34.04.05_Timing_setup_master_file.htm`）、`Master file format for timing setup`（`02.08.04.34.04.05.01`）：这些 master file 主题都指向本工具；timing 一页还说明只有每个 section 顶部的 common block 会被本工具识别（回链证据）。
- `Protection for your setup files`（`01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02.03_Protection_for_your_setup_files.htm`）：该页讨论 `hp83_import` 与加密 setup 文件时引用本工具与 master file；其子页 `Customized hp83_import for encrypted setup files` 说明该定制导入忽略 Setup Management Tool，因为它面向分布式开发（回链证据）。
- **四个 setup component**：Level setup、Timing setup、Testflow setup、TMLimits test table setup——本页正文列出，也是本工具的作用对象。
- **五个子主题**：本页 `Subtopics` 明确列出（见「是什么」）。

## 版本

**文档事实**：`Functional changes` 记录：

- `Introduced before SmarTest 6.3.2`——哨兵值，表示文档集覆盖范围之前已有，不能当作 6.3.2 的变更；
- SmarTest 6.5.3：开始支持 TMLimits setup。

## 出处

- 主源：`01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02.04_Setup_Management_Tool.htm`（正文、Subtopics、Functional changes）。
- 「语法 / 参数」节另逐字取自子主题：`01.01.07.02.02.04.05_Collision_handling.htm`、`01.01.07.02.02.04.05.01_Collision_handling_for_the_level_master_file.htm`、`01.01.07.02.02.04.05.02_Collision_handling_for_the_timing_master_file.htm`、`01.01.07.02.02.04.05.03_Collision_handling_for_the_waveform_master_file.htm`、`01.01.07.02.02.04.05.05_Collision_handling_for_the_TMLimits_master_file.htm`。
