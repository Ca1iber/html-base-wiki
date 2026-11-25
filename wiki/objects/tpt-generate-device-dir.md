---
type: object
title: tpt_generate_device_dir
layer: L2
stage: project
tags: []
related: []
sources:
  - 02_System_reference/02.09_Test_Program_Management/02.09.02.03.16_tpt_generate_device_dir.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# tpt_generate_device_dir

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,771 字符逐字取自** `<02_System_reference/02.09_Test_Program_Management/02.09.02.03.16_tpt_generate_device_dir.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
tpt_generate_device_dir(
tpt_dir = <tpt_directory>,
device_dir = <directory>,
[device_name = <device_name>, ]
[pre_proc = <pre_proc>, ]
post_proc = <post_proc>]
)
```

### Parameters

The parameters in the order in which they are listed
above:

[表]
行 1:
  tpt_dir
  <tpt_directory> (string) is the name and path of the
    directory containing the TPT files from which the device directory is to be generated.
    
    The path can be either absolute or relative to the current working directory.
行 2:
  device_dir
  <directory> (string) is the path, including the name,
    where the new device directory is created. The directory must either not exist yet (in
    which case STPM creates it) or it must be empty.
    
    The path can be either absolute or relative to the current working directory.
行 3:
  device_name
  <device_name> (string) is the name for the newly created
    device.
    
    This parameter is optional. If it is omitted, "device" is used.
行 4:
  pre_proc
  <pre_proc> is a script that is executed before this
    command.
    
    The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `143913.htm`）.
    
    This is an optional parameter.
行 5:
  post_proc
  <post_proc> is a script that is executed after this
    command.
    
    The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `143913.htm`）.
    
    This is an optional parameter.

### Example

This example creates a device directory for the device "my_device" from the TPT master
file "my_tpt.tpt" (located in the current working directory). The device directory is located at
the same level as the current working
directory.

```
tpt_generate_device_dir(
tpt_dir = 'my_tpt/'
device_dir = '../my_device/'
device_name = 'my_device',
)
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
