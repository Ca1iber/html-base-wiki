---
type: object
title: Pin configuration master file
layer: file
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.05_Pin_configuration_master_file.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Pin configuration master file

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **2,825 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.05_Pin_configuration_master_file.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Header rows

A pin configuration master file always begins with a header
row that must have this content:

```
hp93000,config_master_file,0.1
```

The
second line specifies the tester file which is to be divided. It has the
format:

```
testerfile: <tester_file_name>
```

It
specifies the tester setup file which is to be split.

The subsequent lines in the pin
configuration master file associate each part of the pin configuration with a subfile.

The
paths for the subfiles can be relative or absolute. The reference directory for relative paths
is the directory of the master file.

You can insert comments anywhere in the file. They
are identified by the hash (
#
) character at the start of a
line.

### Format of entries

The entry format for the parts is as
follows:

```
Package: <package_file_name.cfg>
alias_set_name_1: <alias_file_name_1.cfg>
...
alias_set_name_X: <alias_file_name_X.cfg>
```

The

Package
 keyword refers to the package file. The pin names specified in this
file are all used in the assembled file.

The subsequent lines in the master file specify
that the alias set named with "
alias_set_name_X
" is generated with the
information extracted from the file "
alias_file_name_X.cfg
".

### Examples

### package.cfg

The following example shows how the Setup Management Tool
assembles three pin configuration files according to the master file.

The file

package.cfg
 is the package file, and the other two files,

TRANSIO.cfg
 and
USB.cfg,
 are the alias
files.

```
hp93000,config,0.1
DFPN 10201,"",(Data_in_2)
DFPN 10202,"",(Data_in_1)
DFPN 10212,"",(Data_in_5)
DFPN 10213,"",(Data_in_4)
DFPN 10214,"",(Data_in_3)
PSTE 1
CONF OFF,F160,(Data_in_2,Data_in_1,Data_in_5,Data_in_4,Data_in_3)
RDIV 0,(Data_in_2,Data_in_1,Data_in_5,Data_in_4,Data_in_3)
NOOP "6.5.2",,,
```

### transio_file.cfg
```
hp93000,config,0.1
DFPN 10202,"",(Data1)
DFPN 10201,"",(Data2)
PSTE 1
CONF IO,F160,(Data1,Data2)
RDIV 0,(Data1,Data2)
NOOP "6.5.2",,,
```

### usb_file.cfg
```
hp93000,config,0.1
DFPN 10214,"",(Data3)
DFPN 10213,"",(Data4)
DFPN 10212,"",(Data5)
PSTE 1
CONF IO,F160,(Data3,Data4,Data5)
RDIV 0,(Data3,Data4,Data5)
NOOP "6.5.2",,,
```

The
pin configuration master file is the
following:

```
hp93000,config_master_file,0.1
testerfile:demo.cfg

Package:package.cfg

TRANSIO:transio_file.cfg
USB:usb_file.cfg
```

The
pin configuration file assembled from the above files looks like
this:

```
hp93000,config,0.1
DFPN 10201,"",(Data_in_2)
DFPN 10202,"",(Data_in_1)
DFPN 10212,"",(Data_in_5)
DFPN 10213,"",(Data_in_4)
DFPN 10214,"",(Data_in_3)
DFPR "TRANSIO","Data2",(Data_in_2)
DFPR "TRANSIO","Data1",(Data_in_1)
DFPR "USB","Data5",(Data_in_5)
DFPR "USB","Data4",(Data_in_4)
DFPR "USB","Data3",(Data_in_3)
PSTE 1
CONF OFF,F160,(Data_in_2,Data_in_1,Data_in_5,Data_in_4,Data_in_3)
RDIV 0,(Data_in_2,Data_in_1,Data_in_5,Data_in_4,Data_in_3)
NOOP "6.5.2",,,
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
