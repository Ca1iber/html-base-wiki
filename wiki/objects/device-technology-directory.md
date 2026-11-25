---
type: object
title: Device Technology Directory
layer: file
stage: project
tags: []
related: []
sources:
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.01.01_Device_Technology_Directory.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Device Technology Directory

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

**没有加标记的语法段。** 定义文档里没有 `Syntax` / `Parameters` / `Example`
这类**段标记**。本脚本一个字都不收录——没有段标记时「哪一段是语法」是猜，
而猜就是编。要看原文：`python show.py <分类号>`。

<!-- 语法节 end -->

## 是什么

**文档事实**：本页列出 cmos 与 ecl 两种默认 device technology 目录的路径和子目录。源文给出的默认路径是 `/opt/hp93000/soc/dev_tech`。

**文档事实**：源表列出以下子目录及其内容（34 项，逐项对应）：

- `.project`：device project 的配置
- `.settings/vectors`：Pattern Debug Tool 与 Pattern Explorer 的布局数据
- `.technology`：device 的 technology file，详见 `Technology file for a device`
- `analog_control`：analog setup 文件
- `applicat`：production mode 的 application data
- `calibration`：标定数据（ACTCatr 文件见 `ACTCatr`）
- `ch_attributes`：channel attributes 文件
- `configuration`：pin 文件
- `data_set`：（保留，Reserved）
- `di_report`：（保留，Reserved）
- `error_map`：以 ASCII 格式导出的 error map
- `format`：供 GUI 工具使用的 pin 显示信息
- `levels`：level 文件
- `license`：license 文件
- `lock_file`：device 的锁文件
- `pin_attributes`：每个 pin 的 edge delay，用于标定
- `profiles`：date logging 配置（源文如此拼写）
- `report`：log 文件
- `routing`：analog 与 relay 布线信息
- `scan_res`：（保留，Reserved）
- `shmoo`：shmoo setup 与结果文件
- `testflow`：testflow 文件
- `testfunc`：客户自定义的 connect / disconnect 序列
- `testmethod`：test method 文件
- `testprog`：test program 文件
- `testtable`：test table 文件
- `timing`：timing 文件
- `timing_dgrm`：（保留，Reserved）
- `vectors`：vector 文件
- `vectors/.cache`：pattern 文件依赖的缓存
- `wafertyp`：wafer 描述文件
- `waste`：默认临时目录
- `waveform`：waveform 文件
- `waveform/.result`：结果 waveform 文件

**文档事实**：其中一部分目录只在用到特定工具或选项时才生成，并非默认都有；也可能出现第三方工具（例如版本控制软件）创建的额外目录。

**文档事实**：每个子目录内是包含固件命令、用于指定默认值的文件；每次新建 setup 文件都会采用这些默认值，之后可以修改。

**推断**：结合“新建 setup 文件时使用默认值”一句，`/opt/hp93000/soc/dev_tech` 下的这些目录是新建 setup 时取默认值的来源；源文没有把它们称作“模板”。

## 典型用法

**文档事实**：源文只给出目录表，没有给出操作步骤；按文件类型可定位到对应子目录，例如 level 文件在 `levels/`、timing 文件在 `timing/`、testflow 文件在 `testflow/`、vector 文件在 `vectors/`、test program 文件在 `testprog/`、test method 文件在 `testmethod/`、pin 文件在 `configuration/`、waveform 文件在 `waveform/`。

**文档事实**：新建 setup 文件时，系统采用这些目录里的默认值；随后可以修改，所以新建得到的文件是“默认值 + 修改”。

**文档事实**：部分目录只在特定工具或选项下生成，并非默认都有。

**推断**：因此某个子目录不存在时，可先考虑对应工具或选项目前没有使用。

**建议**：具体的文件格式与参数以各子目录对应的专题页（如 `Technology file for a device`、`Application Data`）为准，本页只给出目录级索引。

## 和谁有关

**文档事实**：以下关系都有源文的表格行、正文或入边支撑；每条注明为什么相关。

- [[technology-file-for-a-device]]：本页 `.technology` 行指到该页，其 Change Device / New Device 下的同名子主题也回链本页。为什么：`.technology` 子目录就是 technology file 的存放位置。
- `ACTCatr`（`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.04.01.01_ACTCatr.htm`）：本页 `calibration` 行明确指到它。
- `Channel attributes files`（`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.04.01_Channel_attributes_files.htm`）：本页 `ch_attributes` 行明确指到它。
- `Application Data`（`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.01_Application_Data.htm`）：本页 `Related information` 的唯一一条。
- `Device Technology Defaults`（`01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.01_Device_Technology_Defaults.htm`）：本页的父主题，回链本页；它讲这些默认值的含义。
- `Creating a new device technology`（`01_Getting_started/01.03_Using_SmarTest/01.03.02_Creating_a_new_device_technology.htm`）：回链本页；新建 technology 时以这些默认目录为依据。
- [[device-directory]]（`01_Getting_started/01.07_Testing_a_Basic_Digital_Device/01.07.01.01.01_Device_directory_structure.htm`）：回链本页；它讲 device 目录结构，本页讲 technology 默认目录，两者是不同层级的目录说明。
- 新建 device 的三篇文档（`01.01.10.03.01_Creating_a_new_device`、`01.07.01.01_Creating_a_new_device`、`02.08.04.15.01_Creating_a_new_device`）：均回链本页，作为目录结构参考。
- `About projects, file system, and references`（`01_Getting_started/01.01_SmarTest_Work_Center/01.01.06_About_projects__file_system__and_references.htm`）：回链本页，属文件系统上下文。

## 版本

**文档事实**：`Functional changes` 记录：

- `Introduced before SmarTest 6.3.2`；
- SmarTest 7.0.3：移除 `bitmap`、`bitmap_conf`、`mem_llapg`、`scrambling` 四个目录。

**推断**：`Introduced before SmarTest 6.3.2` 是文档集常用的哨兵写法，表示该内容在 6.3.2 之前已存在，不能读作“6.3.2 才引入”。

## 出处

- 主源：`01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.01.01_Device_Technology_Directory.htm`（正文、子目录表、Related information、Functional changes）。
- 关系证据：`extract/objpack.py` 的入边（10 条）与本页表格中的内部链接。
