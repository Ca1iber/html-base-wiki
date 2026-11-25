---
type: object
title: Pattern Explorer
layer: gui
stage: pattern
tags: []
related: []
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01_Pattern_Explorer.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Pattern Explorer

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,639 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01_Pattern_Explorer.htm>` 及其子主题 `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.06_Cloning_a_pattern.htm>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.07_Moving_or_copying_pattern_files.htm>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.08_Deleting_pattern_files.htm>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.09_Checking_pattern_references.htm>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.14.01_Moving_vectors_to_another_memory_type.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Cloning a pattern）

The following examples explain the transformation to NOP instructions in more
detail.

For the instruction
SSRC dsm_data_pattern
, if the port of the pattern

dsm_data_pattern
 is also the port of the target pattern, the

SSRC
 instruction is cloned to the target pattern without change.

For the instruction
JSUB sub_pattern
, as the port of the pattern

sub_pattern
 is not the same as that of the source pattern, in the target
pattern, the
JSUB
 instruction is replaced by an
NOP

instruction and a warning message is displayed on the console tab.

If an instruction is replaced by
NOP
 in the target pattern (for example,
the
JSUB sub_pattern
 instruction), you must modify the instruction
manually:

Create a new subroutine pattern
sub_pattern_clone
 by cloning the

sub_pattern
 pattern with the port of the target pattern.

Replace
NOP
 with the
JSUB
 instruction using the new
pattern:
JSUB sub_pattern_clone.

### Example（取自子主题 Moving or copying pattern files）

Update of pattern master file when moving
pattern 4
 from the

patterns_a
 folder to the
patterns_b

 folder
:

[表]
列: Before | After
行 1:
  ```
    hp93000,pattern_master_file,0.1
    
    path:
    ../data/patterns_a
    
    files:
    pattern1
    pattern2
    pattern3
    pattern4
    
    path:
    ../data/patterns_b
    
    files:
    pattern5
    pattern6
    ```
  ```
    hp93000,pattern_master_file,0.1
    
    path:
    ../data/patterns_a
    
    files:
    pattern1
    pattern2
    pattern3
    
    path:
    ../data/patterns_b
    
    files:
    pattern4
    pattern5
    pattern6
    ```

### Example（取自子主题 Deleting pattern files）

"Cannot delete ..." error message:

Confirmation dialog:

### Example（取自子主题 Checking pattern references）



### Example（取自子主题 Moving vectors to another memory type）

conv_vector -target SM -p pins_soc pattern_vm
pattern_sm

<!-- 语法节 end -->

## 是什么

**文档事实** Pattern Explorer 是 SmarTest 的 pattern 浏览与管理工具。文档列出六项能力，浏览已加载 setup 中的 patterns，新建 pattern、port burst 与 multiport burst，删除 patterns，加载和保存选中的 patterns，启动 Pattern Editor 与 Multiport Burst Editor，编辑 bursts。

**文档事实** 加载和保存选中 pattern 要求这些 pattern 通过 pattern master file 加载。标准 pattern setup 文件不支持该功能。

**文档事实** 窗口分主区和 details 区。主区列出已加载 setup 的全部 pattern，details 区内容随主区选择变化，无内容可显示时给出提示信息。底部状态行显示选中项、行号与总行数。

**文档事实** 工具栏图标包括 Link with Editor、Show Executed Pattern、Go to Row，快捷键 Ctrl+L，Pin Details Area 与 View Menu。View Menu 提供布局与 preferences。布局含 Vertical、Horizontal、Automatic 三种视图方向以及 Pattern Main Area Only。仅对 pattern master file 即 *.pmfl 有效的图标有 Show Folder in Hierarchy、Show Multiport Burst in Hierarchy、Expand All、Collapse All。

**文档事实** 主区图标表示 folder、modified folder、pattern、已初始化但未加载的 pattern、modified pattern、当前 primary pattern，以及 PortBurst 与 MPBurst 及其 modified 与 primary 状态。已初始化未加载的 pattern 图标、名称等置灰。

**文档事实** 状态行示例为 1/200 表示 200 行中的第 1 行。处在过滤格时显示 Filter/200。

## 典型用法

**文档事实** 打开方式。先加载 Pin Configuration、Levels、Timing、Pattern，再在 Test Program Explorer 双击 pattern 项。调试 testflow 时也可在 Properties view 右键 pattern 项选 Open Pattern 或按 F3，这会打开 Pattern Explorer 并把 pattern 载入编辑器。

**文档事实** 新建 pattern。在主区右键选 New > Pattern，填写 Pattern Name、Pattern Type、Port、Memory Type、Wavetable、Folder。Pattern Type 可取 Main、SJMP、SubRoutine、Burst、DSRC。Memory Type 可取 SM 或 SHMEM。Folder 只在 pattern master file setup 中可用。新建 pattern 只含一行带 STOP 指令的 vector。

**文档事实** 查看和编辑 burst。在主区高亮 burst 后 details 区显示其内容。可点 Lock detailed area 图标锁定 details 区，再用 Copy、Insert、Paste、Up、Down、Delete 调整。双击 burst 在 Pattern Editor 中打开，被引用 pattern 以 CALL pattern_name 列在 Instruction 列，可选中 CALL 后按 F3 或右键 Open Referenced Pattern 打开。burst 始终使用默认 port @。

**文档事实** 创建 multiport burst。右键选 New > Multiport Burst，在 Name 填名，在 Port Bursts 列表选 port，可为每个 port 改 sync group，在 Folder 指定 port burst 文件位置。共享同一批 pin 的两个或更多 port 不能同时分配。结果以 Type = MPBurst 出现在 Pattern Explorer。port burst 文件要等显式保存 multiport burst 时才写入指定文件夹。

**文档事实** 创建和分配 port burst。port burst 是面向一组 pin 的 burst，始终属于某个 multiport burst，并且必须属于某个 sync group。可从 Pattern Explorer 或 Multiport Burst Editor 打开 New Port Burst 对话框。设备 pin 只能属于所选 port 中的一个。结果在 Pattern Explorer 中列在对应 multiport burst 下，命名语法为 `<MultiportBurstName>@<Port>`。

**文档事实** 克隆 pattern。右键源 pattern 选 Clone，填目标 pattern 名、目标 port、Folder。目标 pattern 的类型与源相同，只关联所选目标 port。源 pattern 的 vector variable 在其 pin 全部包含于目标 port 时也被克隆。若 CALL、JSUB、JPPS、SSRC、JMPE 使用 pattern 参数且该 pattern 的 port 不是目标 port 子集，该指令在目标 pattern 中改为 NOP，并在 console 给出警告，需要手工修正。

**文档事实** 文件管理操作。移动或复制 pattern 文件只在 pattern master file setup 中可用，可在快捷菜单选 Move 或改 Location 单元格，保存时自动更新 pattern master file。删除 pattern 文件时可只删 pattern master file 中的引用，或同时从文件系统删除，后者仍会保留 `file_name.bak` 备份。被其他 pattern 引用的 pattern 不能删除，会弹出 Cannot delete 错误，可点 Show References 在 Search view 中查看引用。合并与拆分 pattern 文件用 Merge Pattern 对话框，实际拆分或合并在保存时发生。

**文档事实** 导入与导出。导入支持 ASCII Interface 格式与 STIL 格式，分别用 ASCII Interface 工具 v2b 与 STIL 工具 stil2bin。ASCII 导入需要 `.avc`、`.tmf`、`.wtb` 文件，STIL 导入需要 `.pat.stil` 文件。导出只支持 MAIN 类型 pattern，分别用 b2a 与 bin2stil。ASCII 导出生成 `.avc`、`.tmf`、`.wtb` 和 `.b2alog`，STIL 导出生成 `.pat.stil` 和 `.stilExplog`。

**文档事实** 排序与过滤。点击表头字段排序，第一次升序，再点降序，再点取消，不支持多列排序。双击青色过滤格输入条件，支持正则表达式，按 Ctrl+Spacebar 激活内容辅助。

**文档事实** 在 Pattern Explorer 中可编辑 pattern、port burst、multiport burst 的属性，包括创建、重命名、删除，创建或改 port burst 的 sync group，把 pattern 类型在 Main 与 SubRoutine 间互改，改 wavetable，改 memory，在 pattern master file setup 中改 pattern 文件位置，选 Pattern Editor layout。Port 属性不可编辑。Main 与 SubRoutine 互改受引用限制，被 burst 引用的 main pattern 不能改为 subroutine，被 JSUB 引用的 subroutine 不能改为 main pattern。

**文档事实** pattern master file。用 New Pattern Setup wizard 创建，Type 选 Pattern Master File，默认位于 device 的 vectors 文件夹，初始只有 `hp93000,pattern_master_file,0.1` 头行。文件内容为路径与文件名列表，注释行以 `--` 开头。可从 Test Program Explorer 选 Load 或 Initialize Pattern Master File，后者不加载 pattern，State 列标为 Not Loaded，pattern 在 Pattern Explorer 中置灰。可保存为原文件或单个 pattern 文件。Save Partial As 只把选中 pattern 保存到单独文件。

**文档事实** 把 vector 从 vector memory 移到 sequencer memory 可用 ASCII Interface 自带的 conv_vector 工具，文档示例为 `conv_vector -target SM -p pins_soc pattern_vm pattern_sm`。vector 文件用 port 名时必须用 `-p` 指定 pin configuration file。conv_vector 不接受 pattern master file。

**文档事实** 文档还说明 pattern master file 的取舍。以 pattern master file 存储时 pattern 文件可放在文件系统任意位置，只加载所需 pattern，只保存改动过的文件。单个 pattern 文件则全部 pattern 在一个大文件里，文件须位于 device directory，调试时整文件加载。下载时 pattern master file 比单个 pattern 文件多用约 5% 到 20% 时间。文档建议调试用 pattern master file，生产用单个 pattern 文件 allvec.bin。

## 和谁有关

**文档事实** Pattern Editor `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02_Pattern_Editor.htm`。本页 Related information 互指，另一文档说明两者配合创建、克隆、编辑和调试 patterns 与 bursts，本页双击 pattern 或 burst 也打开 Pattern Editor。

**文档事实** Multiport Burst Editor `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.03_Multiport_Burst_Editor.htm`。本页 Related information 指向它，port burst 与 multiport burst 的编辑任务在那边。

**文档事实** Pattern Tools 父页 `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16_Pattern_Tools.htm`。它把 Pattern Explorer、Pattern Editor、Multiport Burst Editor 归为一组。

**文档事实** Pattern Explorer preference page `01_Getting_started/01.01_SmarTest_Work_Center/01.01.14.13_Pattern_Explorer_preference_page.htm`。本页 View Menu 的 Preferences 打开它，其设置同时作用于 Pattern Explorer 与 Pattern Editor。

**文档事实** Trace Function `02_System_reference/02.06_Command_Reference/02.06.01.03.05_Using_the_Trace_Function.htm`。明确写 Pattern Explorer 与 Pattern tool 不发出 firmware 命令，因此它们的活动不记录在 MCDLog 文件。

**文档事实** Function of the base wavetable `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.04.05.01_Function_of_the_base_wavetable.htm`。本页新建 pattern 与改属性时选的 wavetable 只是 base wavetable，用于 Pattern Editor 显示，不是执行用的 primary wavetable。

**文档事实** Integrated Result Tool 与 FFC Pareto chart view `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.01_Principles_of_operation_of_the_Integrated_Result_Tool.htm`、`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.04.06_FFC_Pareto_chart_view.htm`。可从 FFC Pareto chart 的快捷菜单打开 Pattern Explorer 显示选中的失败 cycle，前提包括 pattern 文件已加载。

**文档事实** Pin configuration file `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.18.04_Pin_configuration_file.htm`。conv_vector 用它识别 port 中的 pin。

**文档事实** Multiport Burst Editor 的编辑页 `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.03.03_Editing_a_multiport_burst_setup.htm`。它称多数 Open、Cut、Copy、Paste、Insert、Delete、Up、Down 任务与 Pattern Editor 和 Pattern Explorer 的任务相同。

**文档事实** sync groups `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.03.04_Working_with_sync_groups.htm`。port burst 必须属于 sync group，sync group 强制其 port 在同一时间点开始。

**文档事实** ASCII Interface 与 Data Conversion 章 `02_System_reference/02.11_Data_Conversion_and_Bridges/02.11.02.01_Introduction_to_the_ASCII_Interface.htm`、`02_System_reference/02.11_Data_Conversion_and_Bridges/02.11.02.03.08_Calling_v2b_Directly.htm`、`02_System_reference/02.11_Data_Conversion_and_Bridges/02.11.02.04_Binary_to_ASCII_Conversion.htm`。导入导出的 v2b、stil2bin、b2a、bin2stil 都在该章。Creating a pattern master file 页另说明 ASCII Interface 会自动生成 pattern master file，并指向该章。

**文档事实** Test Program Explorer 的 Setup 操作 `01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02.01.03_Changing_setup_data_and_saving_the_changes.htm`、`01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02.01.06_Loading_or_initializing_a_pattern_master_file.htm`、`01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02.01.08_Appending_a_file_to_a_loaded_file__Merge.htm`。创建、加载、初始化、合并以及 Save Partial As 也有入口在那里。

## 版本

**文档事实** 主页 Functional changes 记载，Introduced before SmarTest 6.3.2。6.5.3 为 pattern master file 增加视图模式与加载保存功能，增加 State 与 Location 列，增加表示 pattern 状态的图标。7.1.3 增加支持 multiport burst 的图标与功能。

**文档事实** 子主题 Functional changes 记载，Cloning 于 6.5.3 引入，7.1.3 增加 Folder 字段并支持克隆到更大的目标 port。Import 与 Export 于 6.5.3 引入，6.5.4 增加 STIL Converter。Moving or copying pattern files、Deleting pattern files、Checking pattern references 于 7.1.3 引入。Merging and splitting 于 7.1.3 引入，7.5.0 支持按文件夹批量选择。Moving vectors to another memory type 在 6.3.2 之前引入。Creating a pattern 在 6.3.2 之前引入，7.1.3 增强 pattern 创建与 pattern 文件处理。Viewing and editing bursts 6.5.3 支持双击与右键打开被引用 pattern，7.1.3 在状态行显示被引用 pattern。Creating a multiport burst 与 Creating and assigning a port burst 于 7.1.3 引入。

**文档事实** pattern master file 相关子主题的 Functional changes 记载，Working with pattern master files 于 6.5.3 支持 pattern master file，7.1.3 在 New Pattern Setup wizard 增加 Pattern Master File 选项。Creating a pattern master file 与 Loading or initializing a pattern master file 也于 6.5.3 起支持 pattern master file。Saving a pattern master file 于 6.3.2 引入，7.3.1 起不支持 Save as a different master file。Saving patterns in separate files 于 6.3.2 引入。

## 出处

- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01_Pattern_Explorer.htm`。主源，含能力列表、界面、图标、状态行、Related information、Functional changes。
- 子主题 `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.01_Opening_the_Pattern_Explorer.htm` 至 `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.01.15.05_Saving_patterns_in_separate_files__Save_Partial_As.htm`，含 `02.08.04.16.01.14.01_Moving_vectors_to_another_memory_type.htm`。全部读过，用于典型用法与版本。
