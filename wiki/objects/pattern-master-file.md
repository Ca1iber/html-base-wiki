---
type: object
title: The pattern master file
layer: file
stage: pattern
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.05_The_pattern_master_file.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# The pattern master file

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,177 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.07.01.05_The_pattern_master_file.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

The syntax of the pattern master file is as
follows:

hp93000,pattern_master_file,0.1

[path:

[<
relative_or_absolute_path_1

>]]

files:

<
file_name_1_1
>

<
file_name_1_2
>

...

<
file_name_1_m
>

[[path:

[<
relative_or_absolute_path_2
>]]

files:

<
file_name_2_1
>

<
file_name_2_2
>

...

<
file_name_2_n
>

...]

The
default for the path is the
vectors
subdirectory of the current device. But
if you specify a path, note that the reference directory for relative paths is the

waste
 subdirectory of the device. Therefore, if your pattern files are in
the subdirectory
sample
 of the
vectors
 directory,
you must specify the relative path to this directory as

./vectors/sample
.

You can add comments to a pattern master file
after "
-- "
 (2 times the minus sign followed by a space) at the beginning
of a line.

### Example

Both the usage of relative paths and the insertion of comments are illustrated by the
following example
file:

```
hp93000,pattern_master_file,0.1

-- The following file must reside in <device>/vectors:
files:
sample1.binl

-- The following path points to <device>/vectors/pmfl_test:
path: ../vectors/pmfl_test

files:
sample2.binl.gz
sample3.binl.gz
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
