---
type: object
title: Preprocessing and postprocessing scripts
layer: file
stage: project
tags: []
related: []
sources:
  - 02_System_reference/02.09_Test_Program_Management/02.09.02.03.03_Preprocessing_and_postprocessing_scripts.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Preprocessing and postprocessing scripts

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **2,964 字符逐字取自** `<02_System_reference/02.09_Test_Program_Management/02.09.02.03.03_Preprocessing_and_postprocessing_scripts.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

Both the
pre_proc
 (shown below) and
post_proc

parameters have the same
syntax.

```
pre_proc = '<script>[&mdir][&sdir][&mtp_tf][&mtp_pmf][&mtp_conf][&mtp_tim][&mtp_lev][&mtp_tt][&mtp_rout][&mtp_wf][&mtp_anctrl][&mtp_chatt][&mtp_prot][&mtp_att][&stp_tf][&stp_pmf][&stp_conf][&stp_tim][&stp_lev][&stp_tt][&stp_rout][&stp_wf][&stp_anctrl][&stp_chatt][&stp_prot][&stp_att][<user_parameters>]'
```

The
available script parameters in the order in which they are listed above:

[表]
行 1:
  <script>
  The name and path of the script file to call.
    
    The path can be absolute or relative. If it is a relative path, the base directory is the
    current working directory at the time STPM was called.
行 2:
  &mdir
  Full path to the MTP directory.
行 3:
  &sdir
  Full path to the STP directory.
行 4:
  &mtp_tf
  Full path to the MTP testflow file.
行 5:
  &mtp_pmf
  Full path to the MTP pattern master file.
行 6:
  &mtp_conf
  Full path to the MTP configuration file.
行 7:
  &mtp_tim
  Full path to the MTP timing file.
行 8:
  &mtp_lev
  Full path to the MTP levels file.
行 9:
  &mtp_tt
  Full path to the MTP test table file.
行 10:
  &mtp_rout
  Full path to the MTP routing file.
行 11:
  &mtp_wf
  Full path to the MTP waveform file.
行 12:
  &mtp_anctrl
  Full path to the MTP analog control file.
行 13:
  &mtp_chatt
  Full path to the MTP channel attributes file.
行 14:
  &mtp_prot
  Full path to the MTP protocols file.
行 15:
  &mtp_att
  Full path to the MTP pin attributes file.
行 16:
  &stp_tf
  Full path to the STP testflow file.
行 17:
  &stp_pmf
  Full path to the STP pattern master file.
行 18:
  &stp_conf
  Full path to the STP configuration file.
行 19:
  &stp_tim
  Full path to the STP timing file.
行 20:
  &stp_lev
  Full path to the STP levels file.
行 21:
  &stp_tt
  Full path to the STP test table file.
行 22:
  &stp_rout
  Full path to the STP routing file.
行 23:
  &stp_wf
  Full path to the STP waveform file.
行 24:
  &stp_anctrl
  Full path to the STP analog control file.
行 25:
  &stp_chatt
  Full path to the STP channel attributes file.
行 26:
  &stp_prot
  Full path to the STP protocols file.
行 27:
  &stp_att
  Full path to the STP pin attributes file.
行 28:
  <user_parameters>
  Text that is passed unchanged to the script. This text must not contain any words
    that begin with &.

Except for the name of the script file, all elements are optional.

### Example

This example executes the
write_tp
 command with two scripts:

Before
write_tp
 itself is executed, the

preparation.py
 script from the current working directory is run. No
parameters are passed to this script.

After
write_tp
 has finished executing, the

cleanup.pl
 script is run. This script receives this parameter string
(assuming that the MTP is located in
/user/johndoe/mtp
):

--mdir
'/user/johndoe/mtp' --cmd write --stage
3

```
write_tp('user/johndoe/mtp/flow1.tf',
pre_proc = 'preparation.py',
post_proc = '/usr/tools/scripts/cleanup.pl &mdir --cmd write --stage 3')
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
