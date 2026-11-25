---
type: object
title: tpt_import_from_device
layer: L3
stage: project
tags: []
related: []
sources:
  - 02_System_reference/02.09_Test_Program_Management/02.09.02.03.15_tpt_import_from_device.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# tpt_import_from_device

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **4,967 字符逐字取自** `<02_System_reference/02.09_Test_Program_Management/02.09.02.03.15_tpt_import_from_device.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
tpt_import_from_device(
device_test_flow = <testflow_file>,
tpt_dir = <location>,
[include_groups = <include_groups>, ]
[empty_groups = <empty_groups>, ]
[copy_static_content = <copy_items>], ]
[allow_overwrite = <overwrite_flag>, ]
[pre_proc = <pre_proc>, ]
[post_proc = <post_proc>]
)
```

### Parameters

[表]
行 1:
  device_test_flow
  <testflow_file> (string) is the path of the testflow file
    from which the test program template is to be generated.
    
    The path can be either absolute or relative to the current working directory.
行 2:
  tpt_dir
  <location> (string) is the path, including the name, where
    the new template files and directories are created.
    
    The path can be either absolute or relative to the current working directory.
    
    If the directory does not yet exist, STPM creates it. If the directory already exists, it
    must either be empty or the allow_overwrite parameter (see below) must
    be set to 1.
行 3:
  include_groups
  <include_groups> (list of strings) is a list of groups in
    the specified testflow that are to be imported.
    
    Each group name is a string enclosed in single or double quotes; groups are separated by
    commas, and the list is enclosed in square brackets.
    
    You can use the ? and * wildcard characters in the group name strings. (See empty_groups,
    below, for details.)
    
    This parameter is optional. If it is omitted, all groups are imported.
行 4:
  empty_groups
  <empty_groups> (list of strings) is a list of groups that
    are to be emptied.
    
    An empty group is transferred to the test program template, but none of the test suites
    it contains are transferred. Empty groups are useful to preserve the structure of the
    testflow. They can be filled with new test suites later.
    
    Each group name is a string enclosed in single or double quotes; groups are separated by
    commas, and the list is enclosed in square brackets.
    
    You can use the ? and * wildcard characters in the group name strings; ? matches any
    single character and * matches zero or more characters.
    
    For example, to empty all groups, you would specify empty_groups = '*'.
    To empty the group temp1 and all groups with the name "test" followed by a single
    character, you would specify empty_groups = 'temp1', 'test?'.
    
    This parameter is optional. If it is omitted, no groups are emptied.
行 5:
  copy_static_content
  <copy_items> (list of strings) is a list of names of files
    or directories that are to be copied from the existing device directory to the TPT
    directory.
    
    The list may contain only names (of files or directories), not paths. The named items
    must be located in the top level of the device directory. Each name is enclosed in quotes
    and separated by commas.
    
    For example: copy_static_content = ['my_notes.txt','Change log']
    
    If you include standard directories in this list (testflow,
    timing, levels,
    configuration, vectors,
    testtable), STPM generates a warning and does not copy the
    contents.
    
    Any directories that are copied by means of this command will be included in the device
    directory generated with `tpt_generate_device_dir`（raw: `132751.htm`）.
    
    This parameter is optional. If it is omitted, no additional content is copied.
行 6:
  allow_overwrite
  <overwrite_flag> specifies whether STPM may overwrite
    existing files in the test program template directory:
    
    0 (default): No existing files or directories in the test program template directory
    may be overwritten. If this prevents STPM from saving a created file, it displays an error
    and stops the conversion.
    
    1: STPM may overwrite existing files and directories.
    
    This parameter is optional. If it is omitted, no files or directories are
    overwritten.
行 7:
  pre_proc
  <pre_proc> is a script that is executed before this
    command.
    
    The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `143913.htm`）.
    
    This is an optional parameter.
行 8:
  post_proc
  <post_proc> is a script that is executed after this
    command.
    
    The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `143913.htm`）.
    
    This is an optional parameter.

### Example

This example converts the testflow "my_testflow" (located in the "testflow"
subdirectory of the current working directory) into a test program template in the directory
"new_template", which is located at the same level as the current working directory. It copies
all groups, empties the groups "init_group" and "final_group", copies the temp subdirectory to
the TPT directory, and overwrites any existing files in the TPT
directory.

```
tpt_import_from_device(
device_test_flow = 'testflow/my_testflow',
tpt_dir = '../new_template',
empty_groups = ['init_group', 'final_group'],
copy_static_content = ['temp'],
allow_overwrite = 1
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
