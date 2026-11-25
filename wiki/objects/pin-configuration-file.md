---
type: object
title: Pin configuration file
layer: file
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.04_Pin_configuration_file.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.05_Pin_configuration_master_file.htm
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.09.01_Pin_configuration_file.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Pin configuration file

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,381 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.04_Pin_configuration_file.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example

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

<!-- 语法节 end -->

## 是什么

**文档事实** Pin Configuration Tool 把数据保存在 `<device_dir>/configuration` 目录下的 pin configuration file 中；文件内容是一组 firmware commands，与工具中设定的参数一一对应。

**文档事实** 文档明确允许用 text editor 代替 Pin Configuration Tool，按 firmware command 集合的形式创建或编辑该文件。

**文档事实** 文档示例文件的首行为 `hp93000,config,0.1`；其后出现 `DFPN`、`DFPS`、`DFAN`、`PSTE`、`CONF`、`RDIV`、`DDSL`、`PSLC`、`NOOP` 等命令。文档没有逐条解释这些命令的语义。

**文档事实** 多端口的 pin configuration file 用固件命令 `DFPT` 定义端口；示例中 `DFPT (…), (port_1)` 把一组引脚归入一个端口。

**文档事实** 配置也可以拆成多个文件：由 pin configuration master file 引用各个子文件，Setup Management Tool 使用 master file 组装出完整配置。其中一个子文件是 package file，其余称为 alias files。

**文档事实** Memory Test Plus 文档中的同名条目指 `.pin` 文件：它说明 DUT 上有哪些引脚，可由 Pin mapping file 用 `using pinconfig` 关键字引用（指定端口、多端口操作或自动波形生成时需要）。这是另一份文档中的同名对象，与 SmarTest 主文档描述的固件命令文件不同。

## 典型用法

**文档事实** 常规流程是在 Pin Configuration Tool 中设置引脚，由工具把结果写入该文件；需要批量修改或脚本化生成时，可直接编辑文件文本（原文 Note 明确允许使用 text editor）。

**文档事实** 多端口 DUT 需要额外写 `DFPT` 行来声明端口及其成员引脚。

**文档事实** 配置规模较大、需要多人并行维护时，可拆成 package file 与 alias files，再由 master file 合并。合并时 Setup Management Tool 会校验：各文件站点数相同、alias 文件中的所有 channel 都出现在 package file 中、各文件的 context 不重复（`DEFAULT` 除外），以及 package file 中 channel 的方向声明满足 alias 的方向要求；任一条不满足则中止组装并报错。

**文档事实** 使用 `conv_vector` 时，如果把 port name 当作 pin list 传入，该命令无法识别端口内包含哪些引脚，此时必须指定 pin configuration file。

**建议** 该文件是纯文本固件命令集合，适合纳入版本控制与评审，以便追踪引脚/端口配置的差异；文档本身未对版本控制作出说明。

## 和谁有关

**文档事实** Pin Configuration Tool（`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18_Pin_configuration_tool.htm`）：该工具写入并维护本文件，文档原文为 "The Pin Configuration tool stores the data in the pin configuration file"。

**文档事实** Pin configuration master file（`02.08.04.18.05`）：当配置拆分为多个文件时，master file 用 `hp93000,config_master_file,0.1` 头、`testerfile: <tester_file_name>` 行和后续子文件引用把各部分合并；Setup Management Tool 据此组装。

**文档事实** DC Scale Extensions editor（`02.08.04.18.03.05`）：该编辑器的设置也存进 Pin configuration file，并用固件命令 `DFDM` 保存。

**文档事实** Level Setup tool（`02.08.04.14.01.06`）：如果在 Pin Configuration 中输入了 DUT 板上与引脚串联的电阻值，Level Setup tool 会读取该值，并补偿该电阻造成的电平衰减。

**文档事实** `conv_vector`（`02.08.04.16.01.14.01`）：指定 port name 作 pin list 时它无法识别端口内引脚，必须借助 pin configuration file 提供的信息。

**文档事实** STPM 的 `tpt_generate_template`（`02.09.02.03.14`）与 test program template（`02.09.02.01.02.03`）：STPM 生成模板文件时不创建 device-specific 的 Pin configuration file，需在使用前手工补上。

## 版本

**文档事实** 主文档 `Functional changes` 段只写「Introduced before SmarTest 6.3.2」，未列出后续变更。Memory Test Plus 中的同名条目也只写这一句。

## 出处

- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.04_Pin_configuration_file.htm`（主源：文件位置、固件命令示例、Note、Functional changes）
- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.05_Pin_configuration_master_file.htm`（master file、package/alias files 与组装校验规则）
- `02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.03.03.09.01_Pin_configuration_file.htm`（`.pin` 文件、`using pinconfig`）
- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18_Pin_configuration_tool.htm`（Pin Configuration Tool 入口及其子主题）
