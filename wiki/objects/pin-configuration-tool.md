---
type: object
title: Pin configuration tool
layer: gui
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18_Pin_configuration_tool.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Pin configuration tool

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **4,586 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18_Pin_configuration_tool.htm>` 及其子主题 `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.03_Port_Editor.htm>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.06_DC_Scale_Limits_editor.htm>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.13_Filter_line.htm>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03.14_Sorting_rows.htm>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.04_Pin_configuration_file.htm>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.05_Pin_configuration_master_file.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Port Editor）

The following picture shows a port Port_IO consisting of eight pins.

In the
Available Pin List
, the "√" character preceding with the pin name
means that this pin has been added to Port_IO.

### Example（取自子主题 DC Scale Limits editor）



### Example（取自子主题 Filter line）

When you type
I/O
in the filter line of the Pin Name column,
all the pins whose names include
I/O
are shown.

### Example（取自子主题 Sorting rows）

The following examples sort the Pin Name column in ascending and descending order.

### Example（取自子主题 Pin configuration file）

The figures below show the pin setting and the contents of the related pin configuration file.

```
hp93000,config,0.1
DFPN 10208,"108",(IAQ_D8)
DFPN 10207,"107",(IAQ_D7)
DFPN 10206,"106",(IAQ_D6)
DFPN 10205,"105",(IAQ_D5)
DFPN 10204,"104",(IAQ_D4)
DFPN 10203,"103",(IAQ_D3)
DFPN 10202,"102",(IAQ_D2)
DFPN 10201,"101",(IAQ_D1)
DFPN 10403,"",(WDA_TRIG)
DFPN 10401,"",(WDB_TRIG)
DFPS 11,POS,(VCC1)
DFPS 12,POS,(VEE)
DFPS 14,POS,(DRC_IN_TERM)
DFAN "MCB231,1,i","232",(input_a_1)
DFAN "MCB231,2,i","234",(input_a_2)
PSTE 1
CONF OFF,F160,(IAQ_D8,IAQ_D7,IAQ_D6,IAQ_D5,IAQ_D4,IAQ_D3,IAQ_D2,IAQ_D1,
WDA_TRIG,WDB_TRIG)
RDIV 0,(IAQ_D8,IAQ_D7,IAQ_D6,IAQ_D5,IAQ_D4,IAQ_D3,IAQ_D2,IAQ_D1,
WDA_TRIG,WDB_TRIG)
DDSL 0,(VCC1)
DDSL 0,(VEE)
DDSL 0,(DRC_IN_TERM)
PSLC 0.1,(VCC1,VEE,DRC_IN_TERM)
NOOP "6.1.0",,,
```

The following lines shows a multi-port pin configuration file. The firmware command

DFPT
is used to define ports.

```
hp93000,config,0.1
DFPN 10102,"12",(CP_1)
DFPN 10302,"12",(CP_2)
...
DFPT (CP_1,DS7_1,DS0_1,I/O7_1,I/O6_1,I/O5_1,I/O4_1,I/O3_1,I/O2_1,
I/O1_1,IO0_1,Q7_1,Q0_1,S1_1,S0_1,_MR_1), (port_1)
DFPT (CP_2,DS7_2,DS0_2,I/O7_2,I/O6_2,I/O5_2,I/O4_2,I/O3_2,I/O2_2,
I/O1_2,I/O0_2,Q7_2,Q0_2,S1_2,S0_2,_MR_2), (port_2)
...
```

Note
 You can use a text editor instead of the Pin Configuration Tool to create or edit
a pin configuration file in the form of a set of firmware commands.

### Header rows（取自子主题 Pin configuration master file）

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

### Format of entries（取自子主题 Pin configuration master file）

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

### Examples（取自子主题 Pin configuration master file）

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

**文档事实** Pin Configuration tool 用于编辑 pin configuration file；文档称 pin configuration file 是测试新器件前必须首先完成的 setup 文件，若 pin configuration 尚未录入，软件不会允许在其他 setup 窗口中输入 DUT 信息。

**文档事实** 该工具的主题覆盖 pin、pin group、port、alias set 与 utility purpose，并包含 Digital Pins、DPS Pins、Utility Pins、Port Editor、DC Scale Limits editor 等子编辑器与元素。

**文档事实** 除该工具外，也可以用文本编辑器按 firmware 命令集合的形式创建或编辑 pin configuration file。

## 典型用法

**文档事实** 在工具中定义 pin、pin group、port 与 utility purpose；Port Editor 的 Available Pin List 中，pin 名前的 "√" 表示该 pin 已加入相应 port。

**文档事实** Pin Name 列的 filter line 可按名称过滤（例如输入 I/O 会显示所有名称含 I/O 的 pin），该列也支持升序/降序排序。

**文档事实** 可用 DC Scale Limits editor 设置 DC Scale 电压/电流限制；文档还提供导入/导出 CSV、应用、保存和丢弃修改的步骤。

**文档事实** pin configuration file 也可由文本编辑器直接编辑；多 port 文件用 DFPT 定义 port；master file 由 Setup Management Tool 按其中的 package/alias 引用组装。

## 和谁有关

- Pin configuration file：**文档事实** 主页面与 Introduction 子主题说明该工具的作用就是编辑此文件。
- Pin configuration master file：**文档事实** 该子主题说明 Setup Management Tool 依据 master file 把 package 文件与各 alias 子文件组装成完整的 pin configuration。
- Level Setup window：**文档事实** 该页面说明其前两列 pin/group 名和 pin type 显示的是在 Pin Configuration window 中定义的数据，且不能在该窗口编辑。
- DPS Setup window：**文档事实** 该页面说明 DPS pin 名来自在 Pin configuration tool 中定义或导入的名称。
- Pogo mapping：**文档事实** 该页面说明 signal-to-pogo pin 分配在 Pin configuration tool 中配置。
- Sequencer-controlled utility lines：**文档事实** 该页面要求按 DUT board 设计使用 Pin configuration tool 设置 pin configuration。

## 版本

**文档事实** 主页面本身没有 `Functional changes` 段；`Introduction of the Pin Configuration Tool` 子主题记为 Introduced before SmarTest 6.3.2。

**文档事实** `Elements of the Pin Configuration Tool` 子主题记录：SmarTest 6.5.2 增加 Alias Sets editor；7.1.0 增加 Protocol Assignments；7.1.3 将 utility purpose editor 迁到 Pin Settings；7.2.1 增加 DC Scale Limits；7.4.0 增加 DC Scale Extensions；7.10.1 增加 DC Scale Regulation 与 DC Scale Safety；7.10.3 增加 Ground sense。

## 出处

- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18_Pin_configuration_tool.htm`
- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.01_Introduction_of_the_Pin_Configuration_Tool.htm`
- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.02_Using_the_Pin_Configuration_Tool.htm`
- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.03_Elements_of_the_Pin_Configuration_Tool.htm`（仅 `Functional changes` 段）
