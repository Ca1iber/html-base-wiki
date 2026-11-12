---
type: stage
title: 建工程 / Device / 目录结构（Project）
tags: [project, workspace, device-directory, technology-file, setup]
related:
  - "[[pin]]"
  - "[[level]]"
  - "[[timing]]"
  - "[[pattern]]"
  - "[[testmethod]]"
  - "[[testflow]]"
sources:
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.04_SmarTest_workspaces.htm
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.04.01_Creating_and_opening_a_workspace.htm
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.04.02_Warnings_and_error_messages_when_starting_SmarTest.htm
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02_Setup_perspective.htm
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.01_Device_Technology_Defaults.htm
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.01.01_Device_Technology_Directory.htm
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.01.02_Technology_file_for_a_device.htm
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02_Test_Program_Explorer.htm
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02.01.01_Loading_a_single_setup_component.htm
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02.01.02_Creating_a_new_single_setup_component.htm
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02.01.03_Changing_setup_data_and_saving_the_changes.htm
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02.01.04_Renaming_a_single_setup_component.htm
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02.01.05_Loading_a_testflow_and_all_setup_components.htm
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02.04_Setup_Management_Tool.htm
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02.04.01_Concept_of_the_Setup_Management_Tool.htm
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02.04.03_Using_the_Setup_Management_Tool_from_the_Command_Line.htm
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.08.02_Project_Explorer_view.htm
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.08.02.03_Device_Directories.htm
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.08.02.04_SmarTest_lock_mechanism.htm
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.08.02.01.01_Importing_a_device_into_your_workspace.htm
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.08.02.01.02_Changing_the_device_in_the_Project_Explorer_view.htm
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.08.02.01.05_Editing_a_Setup_File_Directly.htm
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.10.03.02_Changing_the_device_with_the_Change_Device_button.htm
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.10.03.03_Editing_technology_data.htm
  - 01_Getting_started/01.03_Using_SmarTest/01.03.02_Creating_a_new_device_technology.htm
  - 01_Getting_started/01.07_Testing_a_Basic_Digital_Device/01.07.01_Testing_a_basic_digital_device.htm
  - 01_Getting_started/01.07_Testing_a_Basic_Digital_Device/01.07.01.01_Creating_a_new_device.htm
  - 01_Getting_started/01.07_Testing_a_Basic_Digital_Device/01.07.01.01.01_Device_directory_structure.htm
  - 01_Getting_started/01.07_Testing_a_Basic_Digital_Device/01.07.01.01.02_SmarTest_directory_structure.htm
  - 01_Getting_started/01.07_Testing_a_Basic_Digital_Device/01.07.01.02_Defining_the_pins.htm
  - 01_Getting_started/01.07_Testing_a_Basic_Digital_Device/01.07.01.03_Setting_up_your_levels.htm
  - 01_Getting_started/01.07_Testing_a_Basic_Digital_Device/01.07.01.03.01_Specifying_the_context_for_levels.htm
  - 01_Getting_started/01.07_Testing_a_Basic_Digital_Device/01.07.01.03.02_How_to_create_an_equation_set_using_the_Equation_editor.htm
  - 01_Getting_started/01.07_Testing_a_Basic_Digital_Device/01.07.01.03.03_Creating_new_specification_sets.htm
  - 01_Getting_started/01.07_Testing_a_Basic_Digital_Device/01.07.01.03.04_Verifying_the_level_settings.htm
  - 01_Getting_started/01.07_Testing_a_Basic_Digital_Device/01.07.01.04_Waveform_and_timing_sets.htm
  - 01_Getting_started/01.07_Testing_a_Basic_Digital_Device/01.07.01.04.01_Equation_based_timing_setup.htm
  - 01_Getting_started/01.07_Testing_a_Basic_Digital_Device/01.07.01.04.02_Setting_up_the_wavetables.htm
  - 01_Getting_started/01.07_Testing_a_Basic_Digital_Device/01.07.01.04.03_Defining_the_equation_sets.htm
  - 01_Getting_started/01.07_Testing_a_Basic_Digital_Device/01.07.01.04.04_Defining_the_spec_sets.htm
  - 02_System_reference/02.06_Command_Reference/02.06.01_Introduction_to_firmware_commands.htm
  - 02_System_reference/02.06_Command_Reference/02.06.01.04_System_preparation_by_firmware_commands.htm
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.79_DMAS__DMAS__-__Define_Memory_Area_Size.htm
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.htm
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.93_DTCP__DTCP__-__Define_Technology_Control_Parameters.htm
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.345_RST_-__ReSeT.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.09.04.01_Prepare_device_setup.htm
  - 02_System_reference/02.07_Test_Method_Reference/02.07.11.01.04_Device_setup_specifics.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.01.01_Digital_test_setup_flow.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.01.01.01_Task_1__Test_Planning.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.15_New_Device_wizard.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.15.04_Default_levels_file_for_a_device.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.01_Introduction_of_the_Pin_Configuration_Tool.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.01_Testflow_methodologies.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01.03_Selecting_setup_files.htm
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.01.07_Setups_page.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.09.01_ChangeDevice.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.09.02_DataManager.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.10.01_HVM_API_Introduction.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.10.03.02.02.12_ChangeDevice.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.10.03.02.02.20_DownloadTestprogram.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14_Test_Suite_Control_API.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01_TestsuiteProxy.htm
  - 02_System_reference/02.15_SmartShell/02.15_SmartShell.htm
  - 03_Use_cases_and_application_papers/03.14_Application_Papers/03.14.07.03_STIL_to_V93000_timing_and_vector_translation_with_a_focus_on_x-modes.htm
created: 2026-11-12
updated: 2026-11-12
verified: doc-only
---

# 建工程 / Device / 目录结构

> 在 SmarTest 里建立一个 workspace 与一个 device 目录，让后续 Pin / Level / Timing / Pattern / Testflow 有一个共享的、带默认值的 setup 文件骨架。

## 目的

**文档事实**：本阶段的第一动作是「建 device」，它同时创建 device 目录并把它链接进 workspace：

> With this task you create a new device directory and a link to your workspace.

workspace 本身是 Eclipse 环境，是 device project 的容器：

> A workspace is an Eclipse environment, which contains the configuration settings and your projects you are currently working on.

> The workspace contains a collection of device projects, device folders, and device files. It is a container for organizing your device projects that relate to a specific area.

device 目录则是「按器件存 setup 数据」的单位：

> The system stores device-specific setup data in device directories. Each device that you configure on the V93000 has its own device directory.

**推断**：因此本阶段真正要交付的不是「空目录」，而是三样东西：一个可被 SmarTest 识别的 workspace 链接、一个含 `.technology` 的 device 目录、以及该目录下由 device technology 默认值填好的 setup 文件树。后续各阶段只往这棵树里加内容，不再重新发明目录。

### 本阶段在 setup 文件顺序中的位置

**文档事实**：`01.07` 章按「建 device → 定 pin → 设 level → 设 waveform/timing」排列子话题；`02.08.01.01` 的 digital test setup flow 用任务表给出同一顺序，并把 test program / testflow 放在其后：

| 顺序 | 文档中的步骤 | 文档 | 本 wiki 阶段 |
|---|---|---|---|
| 1 | Plan your device tests and design the DUT board | `02.08.01.01.01` | 本页前置 |
| 2 | 建 device 目录并链接进 workspace | `01.07.01.01` | 本页 |
| 3 | Define the relationship between resource pins and DUT board（Pin Configuration Tool） | `01.07.01.02`、`02.08.01.01` | [[pin]] |
| 4 | Set up levels（Level Setup Tool） | `02.08.01.01` | [[level]] |
| 5 | Set up timing / waveform（Timing Setup Tool） | `02.08.01.01` | [[timing]] |
| 6 | Set up the vector for digital pins（Pattern Tool） | `02.08.01.01` | [[pattern]] |
| 7 | Task 4: Setting up a Test —— Develop the test program（Testflow Tool、Test Method Perspective） | `02.08.01.01` | [[testmethod]] / [[testflow]] |
| 8 | Task 5: Executing a Test and Obtaining the Results —— Build up a test、execute、obtain results and debug | `02.08.01.01` | [[run]] / [[results]] |
| 9 | Task 6: Executing a Test Flow and Obtaining the Results —— Make a testflow of complete tests、execute all tests、debug the testflow | `02.08.01.01` | [[testflow]] / [[run]] |

**整理说明**：上表第 4–6 行在文档里是同一个 `Task 3: Setups for Digital Channels` 的三个子项，本页按 wiki 的 stage 拆开；这不是文档的三条独立任务。

**文档事实（唯一一条明确的 setup 文件先后）**：pin configuration file 是第一个必须完成的 setup 文件：

> The pin configuration file is the first setup file that must be completed before you can test a new device. If the pin configuration details have not been entered, the software will not let you enter details about the DUT in any other setup window.

**推断**：上表的 1–9 是文档的组织顺序，不是一份被文档声明的单一强制加载顺序。证据是 `02.08.04.32.01.01` 在列 testflow 的 global setup files 时写的是「pin configurations, timing, levels, vector and pin attributes」，timing 在 levels 之前，与 `01.07` 的次序相反。因此除「pin configuration 必须最先」之外，本页不把其它排序写成硬约束；实际先做 level 还是先做 timing，文档没有把两者之间定为前置关系。

**文档事实**：setup 文件可以逐个建，也可以由 testflow 一次性加载：

> If your test setup is based on a testflow and you want to edit your setup data, you do not need to load each single configuration file as Pin Configuration, Levels, Timing etc.. You can load all setup data in one step as described in this topic.

## 前置条件

- **workspace 已建立并可打开**。SmarTest 启动时先选 workspace；默认路径是 `/home/<user name>/workspace_<revision>`（`01.01.04`、`01.01.04.01`）。文档建议 workspace 名带主版本号，便于多版本并存（`01.01.04.01`）。
- **同一 workspace 不能被两个用户共用，也不能被同一用户同时开两次**：

  > A workspace cannot be shared among different users and cannot be used twice by the same user at the same time. Every user has to maintain his/her own workspace. If you need to run several SmarTest sessions in parallel, use different workspace names. Workspaces are not backward compatible among major SmarTest revisions.

- **workspace 目录与 project/device 目录不能互相嵌套**：

  > Make sure that the workspace directory is not located inside a project directory and vice versa.

- **若之前在做别的 device，先存 setup、停测试**。`01.07.01.01` 的 `Before you begin` 原文要求：

  > If you have worked on another device before, perform the following actions before creating a new device:
  > Save the setup data.
  > Stop or finish any active test.

- **新建 device 时必须指定一个「新的或空的」目录**。首次在当前 system controller 上启动 SmarTest 会先弹 Select device 对话框；文档明确：

  > However, even if there are valid SmarTest devices located in the selected directory, the Create Device button only becomes active after a new or empty directory is specified.

- **device technology 已选定**。New Device wizard 的 `Device technology` 默认是 `cmos`，也可选 `ecl`（`01.07.01.01`、`02.08.04.15`）。文档说这两个 technology 决定 high/low level 等默认值（`01.01.07.02.01`）。若需要别的默认值，可复制 `cmos` 或 `ecl` 目录、改其中的默认文件，再在 wizard 里输入新 technology 名（`01.03.02`）。
- **导入已有 device 时，目录必须含 `.technology`**。导入只是建立链接，不复制内容；且必须在文件对话框里双击进入 device 目录，否则报 `/<path>/<directory> does not have .technology file.`（`01.01.08.02.01.01`）。
- **对 device 目录有写权限**。有写权限的用户使用 device 时会在目录里生成 `lock_file`；只有写权限用户才能第二次运行该 device 软件（`01.01.08.02.04`）。只读 device 可以工作，但所有修改必须存到别的目录（`01.01.08.02.04`）。
- **DUT 板与资源需求已规划**。`02.08.01.01.01` 的 Task 1 要求：研究器件、确定需要哪些测试与参数、用什么 test methodology、需要多少 digital channel，核对可用测试系统资源，并设计 DUT board。Task 1 下有三篇叶子：`02.08.01.01.01.01` Verifying Available Test System Resources、`.01.02` Overview of DUT Board Design Considerations、`.01.03` Preliminary Checklist（`02.08.01.01.01`）。**推断**：Task 1 的结论会直接落到本阶段的 wizard 参数（channel 数、Utility block size、Fast Transfer Buffer Size、testpoints、Result Area Size），所以不宜在规划前就把这些上限写死。
- **若改 `.technology`，device project 必须已存在**（`01.01.10.03.03` 的 `Before you begin`）。
- **建议**：把 device 目录放在独立于 workspace 的路径，并在名字里带器件名/项目名（文档示例 `my_74ACT299_tp`，见 `01.07.01.01.01`）。文档只给了「不能互相嵌套」这一条硬规矩，命名风格是建议。

## 涉及对象

| 对象 | 层级 | 在本阶段做什么 |
|---|---|---|
| workspace | gui / file | Eclipse 环境与目录容器；保存配置设置和 device project 链接（`01.01.04`）。 |
| device project / device directory | file | 每颗器件一个目录，存放全部 setup 数据与 `.technology`（`01.01.08.02.03`、`01.01.07.02.01.01`）。 |
| `.technology` | file | 器件根目录下的隐藏文件，定义 technology 源目录、若干器件级系统参数与上限；`.default_levels` 是另一个可选文件（`01.01.07.02.01.02`）。 |
| `.default_levels` | file | 可选的器件根目录文件，覆盖所选 technology 的默认电平（`02.08.04.15.04`）；内容归 [[level]]，文件位置与加载属本阶段。 |
| `New Device wizard` | gui | 建 device 目录、选 technology、设内存上限、决定是否建后即激活（`01.07.01.01`、`02.08.04.15`）。 |
| `Change Device wizard` | gui | 切换 active device；也用于改 `.technology`（`01.01.10.03.02`、`01.01.10.03.03`）。 |
| `Project Explorer view` | gui | 显示 device 目录树；导入/移除 device、激活 device，激活项标 `(current device)`（`01.01.08.02`、`01.01.08.02.01.02`）。 |
| `Test Program Explorer` | gui | 显示 device 的逻辑 setup 结构；从这里创建/加载/保存各 setup component（`01.01.07.02.02`）。 |
| `Setup perspective` | gui | SmarTest 首次启动的默认 perspective，含 Test Program Explorer、Project Explorer、Properties、Outline、Help、Problems、Firmware view、Console、Error Log（`01.01.07.02`）。 |
| `Device Technology Directory`（`/opt/hp93000/soc/dev_tech`） | file | `cmos` / `ecl` 的默认 setup 文件模板来源；新建设置文件时取这里的默认值（`01.01.07.02.01.01`、`01.01.07.02.02.01.02`）。 |
| `Setup Management Tool` / `smartest_mfh` | gui / file | 可选的 setup 组件拆分/合并工具；用 master file 管 level、timing、testflow、TMLimits 等组件（`01.01.07.02.02.04`、`.04.01`、`.04.03`）。 |
| `lock_file` / SmarTest lock mechanism | file | 有写权限用户使用 device 时生成的锁文件，阻止其他用户同时使用（`01.01.08.02.04`）。 |
| `.device_inuse_soc@<hostname>` | file | 用户 home 目录下的文件，记住上次使用的 device 并指向其目录（`01.01.08.02.03`）。 |
| `DSCP` / `DSCP?` | L1 | 为各类 parameter set 预留 sequencer memory；切换 device 时自动执行，值来自 `.technology`（`02.06.02.02.90`）。 |
| `DTCP` / `DTCP?` | L1 | 补充 DSCP，控制 `testpoints`、`extended_dram_factor`；需 `*RST` 激活（`02.06.02.02.93`）。 |
| `DMAS` / `DMAS?` | L1 | 定义/查询 sequencer 逻辑内存区；本阶段只用查询确认 DSCP 后的剩余内存（`02.06.02.02.79`、`02.06.01.04`）。 |
| `*RST` | L1 | 复位 firmware 与 calibration、装载 power-up 默认值；激活 DTCP 定义（`02.06.02.02.345`、`02.06.02.02.93`）。 |
| `ChangeDevice`（TPI） | L3 | 从程序里按 device path/name 切换 device（`02.09.01.09.01`）。 |
| `DataManager`（TPI） | L3 | 对 device 内的 setup 文件做 load/merge/save/delete；`Fid` 表按文件类型分组（`02.09.01.09.02`）。 |
| `ChangeDevice`（HVM） | L3 | 远程设置 SmarTest session 的目标 device；发 `DEVICE_CHANGE_STARTED` / `DEVICE_CHANGE_COMPLETED`（`02.09.01.10.03.02.02.12`）。 |
| `DownloadTestprogram`（HVM） | L3 | 下载 test program，连带下载 testflow 与 setup files（`02.09.01.10.03.02.02.20`）。 |
| `TestsuiteProxy` | L3 | Test suite control API 的 test suite 代理；本阶段核对过其成员表（34 条文档 = 1 条索引 + 33 个成员），未发现 device/workspace 相关成员（`02.09.01.14.02.01`）。 |
| `SmartShell` | L3（7.10.3 不存在） | 外部脚本接口；文档写明 `Introduced in SmarTest 8.2.5`，不能当作本版本的可用入口（`02.15`）。 |

### 01.07 章结构覆盖（叶子与归属）

`01.07 Testing a Basic Digital Device` 是定义文档所在的章。它共 16 篇（含 5 篇带 `Subtopics` 的索引、11 篇叶子），逐篇列出以免只写主路径；叶子的一行说明只取该篇开头或 `Before you begin` 的实义：

| 分类号 | 文档 | 一句话 | 归入阶段 |
|---|---|---|---|
| `01.07` | Testing a Basic Digital Device | 章入口；列出 digital testing 的 setup tools（Pin configuration、Level、Timing、Spec、Pattern、Multiport Burst、Pin Attribute Setup Expert、Protocol editor、Site Control、Testflow）与 debug tools（Error Map、Integrated Result、Pin Margin、Shmoo、Timing Diagram、Pattern）。 | — |
| `01.07.01` | Testing a basic digital device | 用例入口；链到建 device、定 pin、设 level、设 waveform/timing 四段。 | 本页 |
| `01.07.01.01` | Creating a new device | 建 device 目录并链接 workspace；给出 New Device wizard 的完整操作。 | 本页 |
| `01.07.01.01.01` | Device directory structure | `ls -al` 的 device 目录清单 + Project Explorer / Test Program Explorer 视图。 | 本页 |
| `01.07.01.01.02` | SmarTest directory structure | 安装目录中 version-specific 与 common 文件的划分。 | 本页 |
| `01.07.01.02` | Defining the pins | 用 Pin Configuration Tool 定义 device pin 到 tester resource 的连接、site 数、通道分配。 | [[pin]] |
| `01.07.01.03` | Setting up your levels | level 章索引；链到 context、equation set、spec set、verifying。 | [[level]] |
| `01.07.01.03.01` | Specifying the context for levels | 每个 level equation set 关联一个 context；未指定时用 `DEFAULT`；前提是 Level Setup 窗口已打开。 | [[level]] |
| `01.07.01.03.02` | How to create an equation set using the Equation editor | 用 Level Setup tool 与 equation editor 建 equation set；前提是 pin configuration 已设好。 | [[level]] |
| `01.07.01.03.03` | Creating new specification sets | 用 Spec Tool 建 specification set；level 需要 equation set，timing 需要 equation set + wavetable。 | [[level]] / [[timing]] |
| `01.07.01.03.04` | Verifying the level settings | 核对输入值/变量/equation；CAUTION：在 Level Setup Editor 改值只临时覆盖，不写回 level setup file。 | [[level]] |
| `01.07.01.04` | Waveform and timing sets | timing 章索引；链到 equation based timing、wavetable、equation set、spec set。 | [[timing]] |
| `01.07.01.04.01` | Equation based timing setup | timing setup 的三件事：wavetable、timing equation set、把两者连起来的 timing specification。 | [[timing]] |
| `01.07.01.04.02` | Setting up the wavetables | 打开 Timing Setup，在 Select 菜单选 edit wavetables。 | [[timing]] |
| `01.07.01.04.03` | Defining the equation sets | 在 Timing Setup 的 Select 菜单选 Edit Equations，点 Generate。 | [[timing]] |
| `01.07.01.04.04` | Defining the spec sets | 用 Spec Tool 给已声明变量定义 SPECSET；含 EQNSET 与 SPECSET 的单位冲突说明。 | [[timing]] |

**文档事实**：这四段就是 `01.07.01` 的子话题顺序；本页只承担第一段 `Creating a new device`（含 `01.07.01.01`、`.01.01`、`.01.02`），其余三段按上表交给 [[pin]] / [[level]] / [[timing]]，不在本页重复其操作细节。

### 归属判定

这一节是判断，不是文档事实，供维护者复核。

- **device 创建 / workspace / `.technology` 判给本页。** 定义文档 `01.01.04` 讲 workspace，`01.07.01.01` 讲建 device，`01.01.07.02.01.02` 讲 `.technology`；三者共同构成「工程骨架」。pin / level / timing 等页只消费这些文件，不负责建。
- **`.default_levels` 的文件位置判给本页，电平内容判给 [[level]]。** `02.08.04.15.04` 说它必须在 device 根目录、在 device 加载时被解析；这属于工程骨架。它里面是一条条 `DFLV` 定义，语法与电平语义属于 [[level]]。
- **`DSCP` 判给本页，尽管它定义的 parameter set 被后续所有阶段消费。** `02.06.01.04` 明说它是「create a new test configuration」之前必须定义的控制参数；`DSCP` 文档又明说「called every time you switch to another device」。这正是本阶段的动作。`DSCP` 的每个参数（waveform/timing/level/dps/pmu 等上限）在对应 stage 页里只需引用，不重复讲。
- **`DTCP` 判给本页。** 它只控制 `testpoints` 与 `extended_dram_factor`，两者都在 `.technology` 里，属于器件级参数。
- **`DMAS` 的主体判给 [[pattern]]，只有 `DMAS? MFRE` / `MFRP` 查询在本页出现。** `02.06.01.04` 把它作为「查 DSCP 后还剩多少内存」的手段；`02.06.02.02.79` 的本体是 sequencer 程序区/结果区分配，属于 pattern 与运行阶段。
- **`*RST` 判给本页，但它与 [[pin]] 有顺序关系。** `*RST` 会删除 pin 定义、资源、除默认外的 DPS set（`02.06.02.02.345`）；DTCP 又要求 `*RST` 才生效（`02.06.02.02.93`）。**推断**：所以 `*RST` 必须在 pin 配置之前，否则会把刚写好的 pin 定义清掉。文档没有用一句话把这条顺序写出来，本页按两条文档事实推出。
- **Setup Management Tool 判给「setup 组件开发」，不判给本页。** 它管理 level / timing / testflow / TMLimits 等组件的 master file（`01.01.07.02.02.04`），不属于建工程。本页只在产物里提一句它会把 master file 组装成 tester setup file。
- **`TestsuiteProxy` 不判给本页。** 其 33 个成员（`02.09.01.14.02.01`，另有 1 条索引）覆盖 test suite 的 name、level/timing 引用、test method 绑定、site match、执行与 pass/fail；**本次未找到** device、workspace、`.technology` 相关成员。因此 L3 的 device 能力走 TPI/HVM，不走 Test suite control API。
- **同一篇文档的重复投放**：`Creating a new device` 另投放于 `01.01.10.03.01` 与 `02.08.04.15.01`；`Editing technology data` 另投放于 `02.08.04.15.02`；`Technology file for a device` 另投放于 `02.08.04.15.03`。按 `schema-pages.md` §9 视为同一篇，不重复计入 `sources:`，也不据它们制造「多篇文档互相印证」的假证据。

## L1 — Firmware / Setup Command

**本次未找到独立命令子树**：`New Device` 只有 GUI wizard 路径——`93000 > Device > New Device`，或 `File > New Project > 93000 > New Device`（`01.07.01.01`）。本次在 `02.06_Command_Reference` 下**未找到** device / workspace / project 的 firmware 命令子树；本次也未找到用 firmware 命令创建 device 目录的文档。

**文档事实（本阶段确有系统准备命令）**：`02.06.01.04` 在建立新测试配置之前先要求定义系统控制参数：

> Before you create a new test configuration, you must define some control parameters. The command DSCP, DSCP? - (Define System Control Parameter) is provided for this purpose.

这些命令可以通过三种方式下发：`hpt` shell 工具、测试方法里的 `FW_TASK` API、或 SmarTest Work Center 的 Firmware view（`02.06.01`）。下表只列 `02.06.01.04` 点名且实际作用于本阶段的 4 条；**不是**一个 `02.06.xx` 命令子树的完整枚举。

| 分类号 | 命令 | 在本阶段的作用 | 出处 |
|---|---|---|---|
| `02.06.02.02.90` | `DSCP` / `DSCP?` | 定义各类 parameter set 的最大实例数并为它们在 Sequencer Memory 预留空间；切换 device 时自动调用，参数值来自 `.technology`；`DSCP?` 回读现有设置。 | `02.06.02.02.90`、`02.06.01.04` |
| `02.06.02.02.93` | `DTCP` / `DTCP?` | 补充 `DSCP`，控制 `.technology` 里的 `testpoints` 与 `extended_dram_factor`；值必须由 `*RST` 激活。 | `02.06.02.02.93` |
| `02.06.02.02.79` | `DMAS` / `DMAS?` | 定义/扩展端口 sequencer 程序的逻辑内存区；本阶段只用 `DMAS? MFRE` / `MFRP` 查还剩多少 vector 内存。 | `02.06.02.02.79`、`02.06.01.04` |
| `02.06.02.02.345` | `*RST` | 复位 firmware 与全部 calibration 数据，把 power-up 默认值装入硬件；同时激活 `DTCP` 定义。 | `02.06.02.02.345`、`02.06.02.02.93` |

**文档事实（两条命令的版本注记）**：`DSCP` 文档说明它取代旧版的 `CNTR` / `CNTR?`（`02.06.02.02.90`）。`DMAS` 的版本变化是：SmarTest 7.0.1 起仅 `SQPG` 区仍支持 `DMAS`；7.0.3 的 `MTST` 选项不再有效；7.3.2 的 `MFRE` 区类型新增 `PER_CHANNEL`，并新增 `MFRP` 区类型（`02.06.02.02.79`）。

### 最小可用示例（逐字取自文档）

**DSCP 参数设定**（`02.06.02.02.90` 的 `Example`）：

```
DSCP 256,16,256,32,32,1024,16,1,256,
```

`DSCP?` 的返回格式（`02.06.02.02.90`）：

```
DSCP {device_cycle}, {waveform_set}, {timing_set}, {level_set}, {dps_set},
{pmu_set}, {devicecycle_set}, {routing_set}, [period_res_prec],
[period_res_compatibility_model]
```

**DTCP 与 `*RST`**（`02.06.02.02.93`）：

```
> DTCP? "testpoints"
< DTCP "testpoints", "0"
> DTCP "testpoints", "100"
> DTCP? "testpoints"
< DTCP "testpoints", "100"
> *RST
> DTCP? "testpoints"
< DTCP "testpoints", "100"
```

**查询剩余 vector 内存**（`02.06.02.02.79`）：

```
> DMAS? MFRE,,(port12)
< DMAS MFRE,SM,84288,(port12)
```

**`*RST`**（`02.06.02.02.345`）：

```
*RST
```

### L1 内记录的文档矛盾：DSCP 默认值

`02.06.01.04` 与 `02.06.02.02.90` 对 DSCP 的 power-on 默认值说法不一致。前者写：

> At power-on, the DSCP command assumes the following default values.
> DSCP 256, 16, 256, 32, 32, 16, 16,32,256, 256

并解释为 256 device cycles、16 waveform sets、256 timing sets、32 level sets、32 DPS sets、**16 pmu sets**、**16 device cycle sets**、256 routing sets、**256 analog sets**。注意它给了 **10 个数字但只列 9 个参数名**，第 10 个数字在文中没有对应项。

后者（DSCP 命令页）给出的参数默认值是 **pmu_set 1024**、**devicecycle_set 1**、routing_set 256，且第 9 个参数是 `period_res_prec`（默认 4），并没有 `analog_set`；其示例是：

```
DSCP 256,16,256,32,32,1024,16,1,256,
```

**记录，不选边**：两篇都是文档事实。前者把第 9 类参数写成 `analog sets`，后者写成 `period_res_prec`；两者的 pmu / devicecycle 默认值也不同。实际下发前应以本机 7.10.3 的 `DSCP?` 回读为准（这是建议，不是文档承诺）。

### L1 的顺序与副作用

- **`DSCP` 会清空 Sequencer Memory**：

  > Every call of DSCP deletes all data that were previously contained in the Sequencer Memory. Therefore, you have to reload the device setup after changing parameters using the DSCP command.

- **`DTCP` 的值不是立即生效的**：

  > The values that are defined with DTCP must be activated with the *RST command.

  且 `DTCP?` 回读的是「selected value」，不是 active value：

  > Note that this is not the active value, if a new value has been defined, but not yet been activated with *RST.

- **`*RST` 会删掉已定义的 pin/资源/DPS set**：文档的 `type` 参数说明列出 `All pin definitions (for example pins defined with DFAN) will be deleted.`、`All resources (for example objects defined with RDEF) will be deleted`、`All DPS sets, except the default set, will be deleted.`（`02.06.02.02.345`）。**推断**：因此 `*RST` 的合理位置是在 [[pin]] 之前；本页不把它写成「随时可发」的复位命令。

## L2 — Test Method API

文档未覆盖

**边界说明**：文档给出的建 device 路径是 GUI wizard（`01.07.01.01`）；**本次未找到** C++ test method 侧的 device 创建/修改 API。测试方法运行在已经存在的 device 内，因此本阶段没有对应的 L2 API。

`02.07` 里与本阶段沾边的两篇是：

- `02.07.09.04.01` **Prepare device setup**：讲 d2s 框架下写 test method 代码前要先建好 device 的 setup files；其 `Before you begin` 明确把「Create the setup files for your device」列成前提，并指向 Setup and Result Tools 章。它不是创建 device 的 API。
- `02.07.11.01.04` **Device setup specifics**：讲 transaction-based protocol testing 对 device setup 的额外要求（只支持 UTM、只支持 UMM、device setup 要遵守 multi-port 规则、model/license 文件要更新）。同样是约束，不是建工程 API。

**推断**：如果确实要在测试方法里发本阶段的 firmware 命令，`02.06.01` 说明 firmware 命令可以经 `FW_TASK` API 放进 test method；但这是命令下发通道，不等于「测试方法能建 device」。本页不把 `FW_TASK` 当成 L2 的 device 创建接口。

## L3 — 外部控制

**L3 入口是横切的，能力面按阶段分族。** 横切入口见 TPI Program Routines（`02.09.01.09`）、HVM API（`02.09.01.10`）与 Test Suite Control API（`02.09.01.14`）；本阶段的专属族是 **device 选择 / device 内 setup 文件操作 / test program 下载**。

**文档事实（Test Suite Control API 的边界）**：`02.09.01.14` 写明：

> Test suite control API is used to directly control the test suites outside of the testflow tool. Only UTM-based test suites are supported with these APIs.

> They cannot be used in test method programming and also cannot be used in parallel with HVM API and BLC API by the same client process.

**本次未找到** `TestsuiteProxy`（`02.09.01.14.02.01`）中与 device、workspace、`.technology` 相关的成员；它的 33 个成员集中在 test suite 的 name、level/timing 引用、test method 绑定、site match、执行与 pass/fail。因此本阶段不把 Test suite control API 写成 device 控制入口。

### TPI Program Routines

- **`ChangeDevice`**（`02.09.01.09.01`）——按 device path 与 device name 切换当前 device：

  > This procedure lets you change the currently used device to another device specified by device path and device name.

  文档给出 `VOID ChangeDevice(CHAR *device_path, CHAR *device_name, INT32 force_change, INT32 *return_state);`；示例随后调用 `DataManager(dm_testprog, dm_load, ...)` 与 `ExecTestProgram()`。**推断**：这是「把工程切过去再跑」的外部骨架，但它**不创建** device，只切换。

- **`DataManager`**（`02.09.01.09.02`）——从程序里访问 Test Program Explorer：

  > This procedure allows access from within a program to the SmarTest Test Program Explorer (successor of the Data Manager).

  `Fid` 表按文件类型列出 `dm_config`（pin configuration setup）、`dm_level`（level setup）、`dm_timing`（timing setup）、`dm_vector`（vector setup）、`dm_testflow`（testflow file）、`dm_testprog`（test program）、`dm_emap`（error map）等；**本次未找到** `dm_device` 或 `dm_workspace` 这样的 Fid。**推断**：L3 能操作的是 device 内部的 setup 文件，不是 device 目录本身；建目录仍需 GUI 或直接文件系统操作。

### HVM API

`02.09.01.10.01` 把 HVM API 分成 SmarTest Session Management、Test Execution、Hardware Information、Calibration and Diagnostic 四类；并明确 **Switching SmarTest versions is not supported in HVM API**。

- **`ChangeDevice`**（`02.09.01.10.03.02.02.12`）：

  > This remote control command sets the designated device for a SmarTest session.

  参数为 `SESSION_ID`、`DEVICE_PATH`、`DEVICE_NAME`，可选 `DEVICE_LICENSE`；开始/完成时分别发 `DEVICE_CHANGE_STARTED` / `DEVICE_CHANGE_COMPLETED`。文档的约束是「SmarTest session is running」且「no other change device is in operation」。

- **`DownloadTestprogram`**（`02.09.01.10.03.02.02.20`）：

  > Downloading the test program involves downloading the test flow, the setup files and other components of the test program.

  每个 setup file 的下载都会发一对 `SETUPFILE_DOWNLOAD_STARTED` / `SETUPFILE_DOWNLOAD_COMPLETED`。其 `Dependency` 写明 **A device is already set for SmarTest.**——即必须先有本阶段的产物。

### SmartShell

`02.15` 是全库唯一一篇 SmartShell 总述页，其 `Functional changes` 写明 **`Introduced in SmarTest 8.2.5`**，而本 wiki 面向 SmarTest 7.10.3。**结论（文档事实）**：SmartShell 在本 wiki 的目标版本不存在，不能作为本阶段的 L3 接口；该章正文只有 PDF 外链。

## 产物

### 1. workspace 目录

**文档事实**：workspace 是 Eclipse 环境，保存配置设置与 device project 链接；默认路径 `/home/<user name>/workspace_<revision>`（`01.01.04`、`01.01.04.01`）。文档建议用 3 位版本号命名，例如 `workspace_7.1.4`（`01.01.04.01`）。

- **原文如此**：`01.01.04` 的示例把 SmarTest 6.5.3 对应到 `/home/<user name>/workspace_7.1.3`——版本号 6.5.3 与目录名 7.1.3 对不上。照录，不替它改。
- workspace **不是** device 目录；两者不能互相嵌套（`01.01.04`）。
- **三个操作入口**（`01.01.04.01`）：新建 workspace 时用建议路径或输入新路径后 OK；打开已有 workspace 用 Browse 选；切换用 `File > Switch Workspace`，SmarTest 关闭当前 workspace 再打开所选。
- **启动对话框不出现时**：若勾过 `Use this as the default and do not ask again`，到 `Window > Preferences > General > Startup and Shutdown` 启用 `Prompt for workspace on startup`；另一条恢复路径是删除 `<$HOME>/.eclipse`（`01.01.04`）。

### 2. device 目录结构

**文档事实**：`01.07.01.01.01` 给出一个真实 device 目录的 `ls -al` 输出，并说明可以在 SmarTest Setup Perspective 的 Project Explorer / Test Program Explorer 里看同一结构。`01.01.07.02.01.01` 逐项解释每个子目录「Contains」什么。合并两篇后共 34 项（含隐藏文件与二级路径）：

| 条目 | 内容（按 `01.01.07.02.01.01`） |
|---|---|
| `.project` | Configuration of the device project |
| `.settings/vectors` | Layout data for the Pattern Debug Tool and Pattern Explorer |
| `.technology` | 器件 technology 文件，见下文第 3 节 |
| `analog_control` | Analog setup file |
| `applicat` | Application data for production mode |
| `calibration` | Calibration data；`ACTCatr` 文件见 `02.08.04.04.01.01` |
| `ch_attributes` | Channel attributes files |
| `configuration` | Pin file（pin 配置文件，归 [[pin]]） |
| `data_set` | (Reserved) |
| `di_report` | (Reserved) |
| `error_map` | Exported error maps in ASCII format |
| `format` | Pin display information for GUI tools |
| `levels` | Level file（归 [[level]]） |
| `license` | License file |
| `lock_file` | Lock file for the device（见下文第 6 节） |
| `pin_attributes` | Edge delays for each pin, used for calibration |
| `profiles` | 原文写 `Date logging configuration`（原文如此） |
| `report` | Log file |
| `routing` | Analog and relay routing information |
| `scan_res` | (Reserved) |
| `shmoo` | Shmoo setup and result files |
| `testflow` | Testflow file（归 [[testflow]]） |
| `testfunc` | Customer-defined connect and disconnect sequences |
| `testmethod` | Test method file（归 [[testmethod]]） |
| `testprog` | Test program file |
| `testtable` | Test table file（SmarTest 7.2.2 起新建 device 时创建） |
| `timing` | Timing file（归 [[timing]]） |
| `timing_dgrm` | 原文写 `(Reserved`（缺右括号，原文如此） |
| `vectors` | Vector file（归 [[pattern]]） |
| `vectors/.cache` | Cached pattern file dependencies |
| `wafertyp` | Wafer description file |
| `waste` | Default temporary directory |
| `waveform` | Waveform file（归 [[timing]]） |
| `waveform/.result` | Result waveform file |

**文档事实（这棵树的性质）**：

> Within each of the sub-directories are files (containing firmware commands) which specify the default values. Every time you create a new setup file, the defaults are used and, of course, can be changed.

> Some of these directories are generated only when particular tools or options are used, not by default. Additional directories may be present that were created by third-party tools such as version control software.

**文档事实（New Device wizard 的字段与注记）**：`01.07.01.01` 与 `02.08.04.15` 两篇共同列出 wizard 的选项：

- `Change to new device after creation` —— 勾选则建完即激活该 device。
- `Device Path` —— 新 device 的路径与名字（文档示例 `my_74ACT299_tp`）。
- `Device technology` —— 默认 `cmos`，也可选 `ecl`；决定默认 level 等。
- `Preinitialize vector memory to value` —— 0–255 的初始化值；对应 `.technology` 的 `init_vectors_with_value`。
- extra options —— 各系统参数的最大值，决定为相应数据结构预留多少内存；不合适的值会让字段高亮并在顶部显示错误。
- `Utility block size` —— 16 或 32 utility lines per pogo block。
- `Fast Transfer Buffer Size` —— 文档要求最小 131072。
- `Skip the V3 delay adjust option. It is supported only by the HSM3600 card.`
- `Fast bidirectional capability is no longer supported.`
- 若 RFI board 被限制为 RFE card，选 `RFI to RFE compatibility mode`。

**文档矛盾（并列记录，不选边）**：`01.01.07.02.01.02` 的 `.technology` 参数表仍列 `fast_bi_directional_capability`（`on | off`，默认 off），并给它一个 Change Device wizard 字段 `Fast bidirectional capability`；`02.08.04.15` 的 New Device wizard 页却写 `Fast bidirectional capability is no longer supported.` 两篇同时存在，本页不判断该参数在 7.10.3 上是否仍可设置。

**文档事实**：`testtable` 子目录自 SmarTest 7.2.2 起在新建 device 时创建（`01.07.01.01` 与 `01.07.01.01.01` 的 Functional changes）。本 wiki 面向 7.10.3，因此该目录在默认骨架里。

### 3. `.technology` 文件

**文档事实**：每个 device 目录根下都有一个 `.technology`。`01.01.07.02.01.02` 给出样例：

```
/dev_tech/cmos
device_cycles: 256
waveform_sets: 16
timing_sets: 256
level_sets: 32
dps_sets: 32
pdc_sets: 1
m_sets: 1024
period_res_precision: 9
testpoints: 10000
utility_lines_per_pogoblock: 16
tester_model: act
licensing_file:
init_vectors_with_value: 50
fast_transfer_buffer_size: 131072
```

它定义三类信息（`01.01.10.03.03`）：technology 相关设置的源目录、若干系统参数的最大值、pay-per-use 的目标测试系统型号。

**文档事实**：`.technology` 通常由 Change Device wizard 的 Edit Device 页更新；wizard 里的修改会存入 `.technology`，并「communicated immediately to the firmware using the DSCP (Define System Control Parameter) and other firmware commands」。不在 wizard 里的参数只能直接编辑文件；直接改后必须手动发 `DSCP`，或重新选择 device（会重新发 `DSCP`）（`01.01.07.02.01.02`）。

完整参数表（`01.01.07.02.01.02` 的 `Parameters of the .technology file`，27 项）：

| 参数 | 默认 / 范围 | Change Device wizard 字段 | 说明 |
|---|---|---|---|
| `/dev_tech/cmos` 或 `/dev_tech/ecl` | n/a | Device technology | technology 目录；决定默认 level 等 |
| `check_compatibility_with_smart_scale` | on \| off（默认 off） | Smart Scale compatibility checker | 开启后 selective capture pattern 含 break vector / match loop 时给 warning |
| `check_exa_scale_seq_restrictions` | on（默认） \| off | Exa Scale check of sequencer program restrictions | 开启后 EXA Scale 的 sequencer 编程限制不满足会报错 |
| `device_cycles` | 256 / 最大 16384 | Device cycles | 单个 pin 的最大 device cycle 数；对应 DSCP `device_cycle` |
| `digital_default_result_area_size` | 0 / 最大 134217728 | Result Area Size | 外部 vector memory 里 error map 的用户定义大小，单位 byte；在每个 digital pin 上预留（DPS pin、以及配置为 PMU 或 DPS 模式的 DC Scale pin 不预留）；可用 `DMAS? MFRE` 查空间 |
| `dps_sets` | 32 / 256 | DPS sets | 最大 DPS set 数；对应 DSCP `dps_set` |
| `enforce_smart_scale_dc_sync_compatibility` | on \| off（默认 off） | SmartScale enforce DC sync compatibility | 在 Smart Scale 卡上生成与 EXA Scale 兼容的 DC 测量 FW 命令 |
| `extended_dram_factor` | 0–99，默认 80 | n/a | `himem:on` 时 vector 区占内存比例；DTCP 可改 |
| `fast_bi_directional_capability` | on \| off（默认 off） | Fast bidirectional capability | 文档只写「Set to on when used」 |
| `fast_transfer_buffer_size` | 默认 0；其他值 131072–16777216 | Fast Transfer Buffer Size | `VEC_TRANSFER_TASK` / `LEV_TRANSFER_TASK` / `PPMU_SETTING` 的传输缓冲 |
| `himem` | on \| off（默认 off） | Himem | 使用 >2 GB vector memory；当前只影响 PS5000；不支持 memory sharing |
| `init_vectors_with_value` | on \| off（默认 off） | Preinitialize vector memory（0–255） | 启动时预初始化 vector 区；默认 DEADBEEF，可改为 0 |
| `level_sets` | 32 / 256 | Level sets | 最大 level set 数；对应 DSCP `level_set` |
| `licensing_file` | 空或文件名 | Licensing file | 每器件 license 文件 |
| `m_sets` | 1024 / 12800 | M sets | PPMU measurement-set action 上限；对应 DSCP `pmu_set` |
| `mset_program_memory_preallocation` | on \| off（默认 on） | MSET memory pre-allocation | 预分配 MSET 内存，大小取决于 `m_sets` |
| `optimized_multiport_memory_allocation` | on \| off（默认 off） | Optimized Multiport Memory Allocation | 改进 pattern loading 算法；可能延长测试时间 |
| `pdc_sets` | 1 / 128 | PDC sets | physical device cycle set 上限；每用一个 selective capture vector variable 就要增加；对应 DSCP `devicecycle_set` |
| `period_res_precision` | 默认 4；建 device 时设为 9 | n/a | 系统计算 period resolution 的小数位；对应 DSCP `period_res_prec` |
| `pulldown_in_level_set_0` | on \| off（默认 on） | Pulldown in level set 0 | level set 0 中启用 pulldown |
| `pulldown_not_configured_pins` | on \| off（默认 on） | Pulldown not configured pins | level set 0 中给未配置 pin 启用 pulldown |
| `pretty_printed_analog` | on \| off（默认 off） | Pretty-printed analog control file | 格式化 analog control file 的 XML |
| `tester_model` | act（另列 `[PPU unused]`） | n/a | pay-per-use 的 tester model |
| `testpoints` | 10000 / 最大 1048576 | Testpoints | 每 pin 的 testpoint 数；对内存影响最大；DTCP 可改 |
| `timing_sets` | 256 / 999 | Timing sets | fixed + equation-based timing set 总数；必须 ≥ waveform set 数；对应 DSCP `timing_set` |
| `utility_lines_per_pogoblock` | 16 \| 32（默认 16） | Utility block size | 每个 pogo block 的 utility line 数 |
| `waveform_sets` | 32 / 128 | Waveform sets | waveform set（fixed timing）+ wavetable（equation-based）总数；对应 DSCP `waveform_set` |

**文档事实（两条公式）**：

- `device_cycles` 与 `waveform_sets` 必须满足：`Maximum number of device cycles per waveform set or wavetable = (device_cycles - 1) / waveform_sets`（`01.01.07.02.01.02`）。
- `fast_transfer_buffer_size` 在 SmarTest ≥ 7.4.3.0 上的规则是 `fast_transfer_buffer_size ≥ blockSize * (number of digital pins specified in VEC_TRANSFER_TASK() * number of configured sites)`，并且 `fast_transfer_buffer_size` 还必须大于 `the largest used VTT (transfer) size multiplied by the number of configured (DPS and digital) channels`；文档建议按至少 2000 channels 估算，以容纳未来 site 数增加（`01.01.07.02.01.02`）。对 SmarTest < 7.4.3.0，规则改为按所有 site 的 digital 与 DPS/DC 通道数计算；对 ≤ 7.4.1.0，该值还必须是 8192 bytes 的倍数（同页）。New Device 操作步骤另写「Set the Fast Transfer Buffer Size to a minimum of 131072.」（`01.07.01.01`）。

### 4. 可选 `.default_levels`

**文档事实**：`.default_levels` 是可选的、放在 device 根目录的文件，用来定制当前 device 的默认电平；SmarTest 在 device 加载时解析它（`02.08.04.15.04`）：

> The optional .default_levels file holds the customized default levels for the currently loaded device. Like the .technology file, the .default_levels file must be stored in the root directory of the device.

> SmarTest loads and parses the file when the device is loaded.

若文件可用，`ui_report` 会显示 `Setting default levels from /.../.default_levels`；若语法错误，加载中止并在 `ui_report` 报错，修好后必须重新加载 device（`02.08.04.15.04`）。语法与电平语义归 [[level]]。

### 5. 默认 setup 文件与 setup component

**文档事实**：新建单个 setup component 时，文件用默认设置创建；默认值存在中央目录：

> The new component (file) is created with the default settings, which are stored in a central directory (which you can also edit if you want). These settings reset the hardware to the power-up default settings, and are stored in the directory:
> /opt/hp93000/soc/dev_tech/<device_technology_name>

（`01.01.07.02.02.01.02`）

**文档事实**：`02.08.04.32.01.01` 列出 testflow 的 global setup files：

> The global setup files are selected on the Setups page including pin configurations, timing, levels, vector and pin attributes. These setups are valid for the entire testflow.

**推断**：这就是本阶段产出的「骨架」的消费方式——device 目录里先有这些组件文件（或至少先有 `configuration/` 等子目录），testflow 阶段再在 Setups page 上把它们逐个选上；`02.08.04.32.02.01.03` 的 `Before you begin` 也要求「the setup files have been created」。

**文档事实（单个 component 的加载/保存）**：

- 加载前必须先导入 device 并激活它；在 Test Program Explorer 里右键 component → `Load...` → 选文件 → OK。可以加载属于别的 device 的 setup 文件，文件名旁会显示 `[external]`。同一 component 可以重复加载，软件不检查是否已加载；改过未存的 component 可用 `Reload` 丢弃改动（`01.01.07.02.02.01.01`）。
- 用 tool 改过数据后，component 标 `*`；右键 `Save...` 保存，多选时先选第一个再 Ctrl+click 其它 component（`01.01.07.02.02.01.03`）。
- 也可以直接用编辑器改 setup file：在 Project Explorer 里双击文件打开、编辑、保存；改完必须用 Test Program Explorer 重新加载。文档警告这样做会绕过一致性检查，且编辑器可能无法正确解释 binary 数据（timing/vector 尤其）（`01.01.08.02.01.05`）。
- testflow 的 Setups page 显示当前 testflow 的 primary setup files；未加载或不存在的 setup file 以黄色高亮。选文件的方式是双击 Pin Configuration 行的 File 列，按 Ctrl+Space 从已有文件列表里选；其它 setup 文件同理（`02.08.04.32.03.01.07`、`02.08.04.32.02.01.03`）。

### 6. `lock_file` 与 `.device_inuse_soc@<hostname>`

**文档事实**：

> If a device directory is being used by a user (normally the superuser) with write permission for that directory, then a lock file is created in the directory. This prevents other users from using that device software. Only a user with write permission can run the device software a second time.

（`01.01.08.02.04`）

**文档事实**：每次使用系统时，home 目录下会写 `.device_inuse_soc@<hostname>`，记住上次使用的 device 并指向其目录；如果它不存在，或 device 目录缺失/损坏，系统显示 Select Device Folder 窗口（`01.01.08.02.03`）。

### 7. workspace 里的链接

**文档事实**：导入 device 只建立链接，不复制：

> Importing a device means that you create a link to your device directory. It does not copy the contents of your device directory to your workspace.

（`01.01.08.02.01.01`）

导入的操作路径：在 navigator 上右键 → `Import...` → `Existing Device/TestMethod into Workspace` → 选 device 目录 → OK；选目录时必须双击进入，不能只选中上级目录（`01.01.08.02.01.01`）。

**文档事实**：激活 device 后，Project Explorer 里该项标 `(current device)`（`01.01.08.02.01.02`、`01.01.10.03.02`）。workspace 可以含多个 device，但同一时间只有一个 active（`01.01.10.03.02`）。切换入口有两个：Project Explorer 里右键 device → `93000 > Change Device`（`01.01.08.02.01.02`），或 V93000 图标栏的 `Change Device` 按钮 → 在 wizard 里输入 device 名与完整路径（或用 Browse）→ Finish（`01.01.10.03.02`）。

### 8. SmarTest 安装目录（与 device 目录区分）

**文档事实**：安装时一部分数据是 version-specific，一部分是 common；version-specific 存在 `/etc/opt/hp93000/soc_<version>` 与 `/var/opt/hp93000/soc_<version>`，common 存在 `/etc/opt/hp93000/soc_common` 与 `/var/opt/hp93000/soc_common`，并用符号链接指过去（`01.07.01.01.02`）。两表的内容：

| 类别 | 路径 | 说明 |
|---|---|---|
| version-specific | `/etc/opt/hp93000/soc_<version>/PH_Libs` | Prober/Handler libraries |
| version-specific | `/opt/hp93000/soc_<version>/pws/lbin/start_edt_env` | equation / specification / wavetable 数据的文本编辑器脚本 |
| version-specific | `/var/opt/hp93000/soc_<version>/PH_Libs` | 上次使用 prober/handler 的消息 |
| common | `/etc/opt/hp93000/soc_common/lbin/` | 低层二进制；各版本目录里有链接 |
| common | `/etc/opt/hp93000/soc_common/model`、`org`、`passwd`、`ppu_alarms` | 杂项配置文件 |
| common | `/var/opt/hp93000/soc_common/calibration` | 校准目录 |
| common | `/var/opt/hp93000/soc_common/.sif_files` | System Information Files；HP-UX 上仍在 `/var/opt/hp93000/soc` |
| common | `/var/opt/hp93000/soc_common/tracecal`、`tmp`、`diagnostic` | 数据目录 |
| common | `/var/opt/hp93000/soc_common/prog_bug_log`、`monitor` | 安装时生成、所有版本共享的数据文件 |

原文的 Data directories 行把 `tmp` 与 `diagnostic` 两个路径挤在一起，读作 `/var/opt/hp93000/soc_common/tmp` 与 `/var/opt/hp93000/soc_common/diagnostic`。

### 9. 可选：master file 与转换工具

- **Setup Management Tool**：把 level / timing / testflow / TMLimits 等 setup component 拆成 subfile，由 master file 记录成员和合并后的 tester setup file 名；SmarTest 本身不支持这些组件的 master file 概念，必须由工具先合并成单一 setup file 才能下载（`01.01.07.02.02.04`、`.04.01`）。命令行程序名 `smartest_mfh`，位于 `/opt/hp93000/soc/com/SETUP_MAN`，支持 `assemble`、`split`、`assemble_all`（`.04.03`）。
- **STILReader**：文档另提到它可以「converts one STIL file into a complete V93000 device directory, containing a pin configuration, levels, timing, and vectors」（`03.14.07.03`）。**这是转换工具路径，不是 New Device wizard 路径**；它生成的是同一类 device 目录，但本页不把它展开成流程。

## 验证

- **建 device 的 `Results`（首选）**：`01.07.01.01` 写明：

  > SmarTest creates a set of data for your new device and activates the device.

  > The values you entered during this task are written to the Technology file for a device.

  因此最低验证是：device 被激活、`.technology` 里能看到 wizard 输入的值。

- **目录级**：`01.07.01.01.01` 给出的方法就是在终端里进入 device 目录并 `ls -al`：

  > In a terminal window, change into the device project directory you just created (for example, my_74ACT299_tp) with the command cd and type the command ls -al.

  对照上表 34 项检查 `.technology`、`configuration`、`levels`、`timing`、`vectors`、`testflow`、`testmethod` 等是否在。注意「Some of these directories are generated only when particular tools or options are used, not by default.」——不是 34 项都必须一次出现。

- **GUI 级**：
  - Project Explorer 里 active device 标 `(current device)`（`01.01.08.02.01.02`、`01.01.10.03.02`）。
  - Test Program Explorer 里：文件名显示在 component 位置说明该 setup 文件已加载；`*` 表示改过未保存；`[external]` 表示该 component 不属于当前 active device（`01.01.07.02.02`）。
  - 新建单个 setup component 后，component 位置应显示新文件名（`01.01.07.02.02.01.02`）。

- **文件级**：
  - 导入 device 时若报 `/<path>/<directory> does not have .technology file.`，说明目录里没有 `.technology` 或没有真正进入该目录（`01.01.08.02.01.01`）。
  - `.default_levels` 可用时，`ui_report` 出现 `Setting default levels from /.../.default_levels`；语法错误时出现 `ERROR: ../.default_levels:##: DFLV VIL,STD,225: expected resource=voltage. for example, vt=50mV)`（`02.08.04.15.04`）。

- **命令回读**：
  - `DSCP?` 回读当前 parameter set 上限（`02.06.02.02.90`）。
  - `DTCP? "testpoints"` / `DTCP? "extended_dram_factor"` 回读 selected value；注意 `*RST` 前它可能不是 active value（`02.06.02.02.93`）。
  - `DMAS? MFRE,,(port12)` 或 `DMAS? ALL` 查剩余内存（`02.06.02.02.79`、`02.06.01.04`）。

- **workspace 启动检查**：启动时的 warning 会检查 device 及其引用的 test method projects；缺失时提示导入，点 `Import missing projects into workspace` 可补（`01.01.04.02`）。

- **建议**：建完 device 后先不要急着写 pin/level，先做三件事——`ls -al` 看骨架、看 `.technology` 的 `device_cycles`/`waveform_sets`/`timing_sets` 是否符合计划、用 `DSCP?` 确认固件侧的上限与文件一致。文档没有提供「一键校验整份 device 目录」的命令；这是建议，不是文档要求。

## 常见错误

| 症状 | 可能原因（文档） | 排查入口 | 出处 |
|---|---|---|---|
| workspace 与 device/project 目录互相嵌套 | 文档明确不允许这种布局：workspace 目录不能在 project 目录里，反之亦然 | 把两者分开放 | `01.01.04` |
| 启动时弹 Select Device Folder | `.device_inuse_soc@<hostname>` 不存在，或上次的 device 目录缺失/损坏 | 选已有 device，或在空目录里新建 | `01.01.08.02.03` |
| 启动报 `Workspace in use, choose a different one.` | 另一个用户正在用该 workspace | 确认是否有其他用户；若 home 在 NFS 上，确认允许 file lock；否则把 workspace 建到 `/var` 下 | `01.01.04.02` |
| 启动报 `java.io.IOException: No locks available` | NFS mounted home 不允许 file locks | 同上的 NFS/file lock 检查；把 workspace 建到 `/var` | `01.01.04.02` |
| New Device 的 `Create Device` 按钮灰着 | 没有指定新的或空的目录 | 换一个新建/空目录 | `01.07.01.01` |
| 导入 device 报 `/<path>/<directory> does not have .technology file.` | 在文件对话框里只选中了上级目录，没有双击进入 device 目录 | 双击进入 device 目录再 OK | `01.01.08.02.01.01` |
| 第二个用户/第二次运行打不开 device | device 目录已被有写权限的用户加了 `lock_file` | 等锁释放；只读 device 的修改另存到别的目录 | `01.01.08.02.04` |
| New Device wizard 某字段变红、顶部出现错误 | 参数值不适合；例如 Fast Transfer Buffer Size 太小 | 按顶部提示改；文档要求 Fast Transfer Buffer Size 至少 131072 | `01.07.01.01` |
| 改过 `.technology` 后 device 不能编辑/测试 | technology 数据指定 tester resource 分配，和器件需求不匹配 | 回到 Change Device wizard 的 Edit Device 页复核；文档警告「the device cannot be edited or tested later on.」 | `01.01.10.03.03` |
| SmarTest 运行中在 Linux shell 里重命名 setup 文件，随后报错 | SmarTest 认不出被外部改名的文件 | 用 Test Program Explorer 的 `Save As...`，不要用 `Rename File`；再删原文件 | `01.01.07.02.02.01.04` |
| 直接编辑 setup 文件后加载结果异常 | 直接编辑绕过一致性检查；编辑器可能误读 binary 数据（timing/vector 尤其） | 尽量用对应 setup tool；直接编辑只适合有经验用户 | `01.01.08.02.01.05` |
| 改 DSCP 参数后原有 setup 数据丢失 | `Every call of DSCP deletes all data that were previously contained in the Sequencer Memory.` | 改完 `DSCP` 后重新加载 device setup | `02.06.02.02.90` |
| `DTCP` 设了新值但硬件行为没变 | 新值未用 `*RST` 激活 | 发 `*RST` 后再 `DTCP?` 确认 | `02.06.02.02.93` |
| 发 `*RST` 后 pin/资源/DPS set 没了 | `*RST` 会删除 pin 定义、资源、除默认外的 DPS set | 把 `*RST` 放在 [[pin]] 之前（推断）；重做被删的配置 | `02.06.02.02.345` |
| 新建 setup component 后硬件回到 power-up 默认 | 新文件用 `/opt/hp93000/soc/dev_tech/<tech>` 的默认设置创建，并 reset 硬件 | 建完再把需要的值写回；这是文档描述的行为 | `01.01.07.02.02.01.02` |
| 切 device 后弹 Warning，说缺少 referenced projects | active device 引用的 test method projects 不在 workspace | 点 `Import missing projects into workspace` | `01.01.10.03.02` |
| 旧 workspace 在新主版本打不开 | workspace 不向下兼容 | 每个主版本建新 workspace；文档示例：6.5.4 的 workspace 不能在 7.1 打开 | `01.01.04` |
| 同 workspace 想开第二个 SmarTest session 失败 | 同一用户不能同时用两次同一 workspace | 用不同 workspace name | `01.01.04` |
| 想同时用两个 device | 一个 workspace 同一时间只有一个 active device | 用 Change Device 切换，不要指望并行 active | `01.01.10.03.02` |

## 下一步

下一步是 [[pin]]。

**文档事实**：`02.08.04.18.01` 明说 pin configuration file 是第一个必须完成的 setup 文件，未填则软件不允许在其它 setup 窗口输入 DUT 细节；`02.08.01.01` 的任务表也把 `Task 2: Pin Configuration Setup` 排在 levels / timing / vector 之前。因此建好 device 骨架后先做 [[pin]]，再进 [[level]]、[[timing]]、[[pattern]]。

**文档事实（本阶段留下的两条线）**：`*RST` 会删 pin 定义、`DTCP` 又需要 `*RST` 才生效；`.technology` 定义了 `device_cycles` / `waveform_sets` / `timing_sets` / `level_sets` 等上限。**推断**：这些上限会在 [[timing]]、[[level]]、[[pattern]] 阶段变成真实约束；如果到 [[pin]] 之后才发现不够，回改 `.technology` 往往要重载 device，代价比现在一次规划大。
