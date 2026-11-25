---
type: object
title: Testflow Tool
layer: gui
stage: testflow
tags: []
related: []
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32_Testflow_Tool.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Testflow Tool

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **15,069 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32_Testflow_Tool.htm>` 及其子主题 `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.03_Hierarchy_within_a_testflow.htm>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.05_Configuring_the_messages_printed_in_the_Report_Window.htm>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.05_Testflow_file.htm>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.06_Testflow_master_file.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Hierarchy within a testflow）

In the testflow shown below, there are three distinct levels. If you select either of
the
test suite nodes, all nodes in all levels stemming from this node are also selected.

The figure below shows the effect of selecting node test
_2_1
; the nodes which branches
from test
_2_1
 are also selected. Similarly, you cannot select more than one node from
different levels; you can, however, select more than one node within the same level. For
example, you could select test
_1_2
 and
test_1_3
, but not test
_1_2
 and
test
_2_2
or test
_3_1
.

### Examples（取自子主题 Configuring the messages printed in the Report Window）

### Printing messages for passed and failed sites in the Report Window

This example shows how you can configure the

.testflow.ReportUiOutput.user_def
 file to print messages in the

Report Window
 for all passed and failed sites after a testflow is
executed:

```
<passed>Site: %site -> Bin: %bin -> PASS (Cool)
<failed>Site: %site -> Bin: %bin -> FAIL (Bad)
#<text> This is an example for a commented line (using "#" at the beginning)
```

The messages that are printed in the Report Window are as in the following figure:

### Printing messages for failed sites only in the Report Window

This example shows how you can configure the

.testflow.ReportUiOutput.user_def
 so that only messages for the failed
sites are printed in the
Report Window
:

```
<failed>Site : %site -> Bin: %bin -> FAIL (Bad)
```

### Printing messages in the Report Window for the failed sites after a test suite is executed

This example shows how you can configure your

.testflow.ReportUiOutput.user_def
 file to print a message in the

Report Window
 for the failed sites after a test suite is executed:

```
<failed>TestSuite: %testSuiteName -> Site: %site -> FAIL
```

### Syntax（取自子主题 Testflow file）

The following syntax listing conforms to the Backus-Naur Format (BNF). Additional
symbols used in the syntax description are as follows:

[表]
行 1:
  |
  Indicate that a choice is available; read as or.
行 2:
  :=
  Read as comprises.
行 3:
  <x>
  A single construct, <x>.
行 4:
  [<x>]
  An optional construct <x>: " " or <x>.
行 5:
  (<x> | <y>)
  An alternative construct <x> or <y>.
行 6:
  [<x>] ...
  A sequence of one or more optional <x>: " " or <x>
    or <x> <x> etc.
行 7:
  <x> ...
  A sequence of one or more <x>: <x> or <x>
    <x> etc.
行 8:
  [ ... ]
  A sequence of one or more of the previous line - optional.
行 9:
  "<x>"
  A sequence of (3) predefined characters: "<" and "x" and
    ">".
行 10:
  [0-9A-F]
  A single character from the range 0123456789ABCDEF. Note that
    this differs from optionality grammar which always has a
    construct <> within it's braces, or is the [ ... ]
    specifier.
行 11:
  <x> ::= "x"
  The construct evaluates to the character "x".
行 12:
  --
  Denote a comment.

### Testflow syntax（取自子主题 Testflow file）

```
<test_flow> := [<lang_rev>]
[<sections>]

<sections> := <sections> [<section>]

<section> := {information <information_section> end |
declarations <declarations_section> end |
flags <flags_section> end |
tests <tests_section> end |
testfunctions <testfunction_section> end |
datasets <dataset_section> end |
test_suites <test_suites_section> end |
initialize <initialize_section> end |
download <download_section> end |
abort <abort_section> end |
pause <pause_section> end |
reset <reset_section> end |
exit <exit_section> end |
test_flow <test_flow_section> end |
binning <binning_section> end |
context <setup_section> end |
hardware_bin_descriptions <hardware_bin_descriptions_section> end }

<lang_rev> := language_revision = <revision_number>;

<revision_number> := <integer>

<information_section> := <information_section> [<infospec>]

<infospec> := {description = "<description_string>"; |
device_name = "<device_name>"; |
device_revision = "<device_revision>"; |
test_revision = "<test_revision>"; }

<description_string> := <string>
<device_name> := <string>
<device_revision> := <string>
<test_revision> := <string>

<declarations_section> := <declarations_section> [<declaration>]

<declaration> := {@<var_name> = <expression> |
@<var_name> = <string> }

<var_name> := {<label> |
<flag_name> |
<test_suite>.<ts_flag>|
* <test_suite>.ffc_on_fail}

<flags_section> := <flags_section> [<flag_spec>]

<flag_spec> := {<flag_name> = <flag_value>; |
user <user_flag_name> = <flag_value>;}

<flag_name> := {<tflow_flag> | <system_flag> }

<system_flag> := {datalog_formatter |
datalog_sample_size |
graphic_result_displ|
state_display |
print_wafermap |
ink wafer |
max_reprobes |
temp_monitor |
calib_age_monitor |
diag_monitor |
current_monitor }

<tflow_flag> := {set pass level |
set fail level |
bypass level |
hold on fail |
global_hold |
debug mode |
site_match_mode }

<user_flag_name> := <label>

<flag_value> := {<integer> | <boolean>}

<dataset_section> := <dataset_section> [<dataset_spec>]

<dataset_spec> := <dataset_label>:
[file = "<dataset_file>";]

<dataset_label> := <label>

<dataset_file> := the name of a V93000 dataset file

<tests_section> := <tests_section> [<test_spec>]

<test_spec> := <test_label>:
[user_procedure = "<user parameters>";]

<test_label> := <label>

<user parameters> := <string>

<testfunction_section> := <testfunction_section> [<testfunction>]

<testfunction> := <testfunction_identifier>:
testfunction_description = <string>;
testfunction_parameters = <string>;

<testfunction_identifier> := <label>

<test_suites_section> := <test_suites_section> [<test_suite_entry>]

<test_suite_entry> := <test_suite>:
{datasets = <dataset_label>; |
tests = <test_label>; |
test_level = <test_level>; |
local_flags = <ts_flag> [, ...];|
* ffc_on_fail = <ffc_count>; |
override = <boolean>; |
override_dpsset = <expression>; |
override_levset = <expression>; |
override_seqlbl = <expression>; |
override_timset = <expression>; |
* override_wvfset = <expression>; |
override_testf = <label>; |
site_match = {0 | 1}; |
site_control = "<site_control_info>";}

<test_suite> := <label>
<test_level> := <integer>
* <ffc_count> := <integer>
<site_control_info>:= <sequence_type>: [<sequence_info>]
(<sequence_info> is omitted if
<sequence_type> = serial or parallel)
<sequence_type> := {serial|parallel|semiparallel|other}
<sequence_info> := {<size>:<cycle>:|<sequence_order>}
(If <sequence_type> = semiparallel,
<size>:<cycle>: is used.
If <sequence_type> = other,
<sequence_order> is used.)
<size> := an integer number (where 0 = undefined)
<cycle> := an integer number (where 0 = undefined),
or -1 for "unbouded"
<sequence_order> := <sequence_order_element>:
[<sequence_order_element>:]
<sequence_order_element> := an integer number
(where, 0 = undefined, or
a pogitive integer = test order)

<ts_flag> := {bypass |
set_pass |
set_fail |
hold |
hold_on_fail |
output_on_pass |
output_on_fail |
value_on_pass |
value_on_fail |
per_pin_on_pass |
per_pin_on_fail }

<initialize_section> := <test_suite_entry>

<download_section> := <test_suite_entry>

<abort_section> := <test_suite_entry>

<pause_section> := <test_suite_entry>

<reset_section> := <test_suite_entry>

<exit_section> := <test_suite_entry>

<test_flow_section> := <statement>;
[...]

<statement> := {<assignment> |
run(<test_suite>) |
run_and_branch(<test_suite>)
then <statement> [else <statement>] |
print(<print_expression>) |
print_dl(<print_expression>) |
if <expression> then <statement>
[else <statement>] |
while <expression> do <statement> |
for <assignment>;<expression>;<assignment>;
do <statement> |
repeat <statement>; until <expression> |
'{' <statement> [;<statement>]... '}'
[[<compound_state>],
[<compound_label>],
[<compound_description>]] |
stop_bin1)(<major_bin>, <minor_bin>, , <good_flag>,
<reprobe_flag>, <color>, <physical_bin>
[, <over_on_flag>]);}

<assignment> :={@<var_name> = <expression> |
@<var_name> = <string>}

<compound_state> := {open | closed}
<compound_label> := <string>
<compound_description> := <string>
<over_on_flag> := {over_on | not_over_on}
<good_flag> := {good | bad}
<reprobe_flag> := {reprobe | noreprobe}

<print_expression> := {<expression> |
<string_with_vars> }

<hardware_bin_descriptions_section> := {<integer> = <string> ;
[...]}

<binning_section> :=
otherwise bin2) = <major_bin> <minor_bin>, , <good_flag>,
<reprobe_flag>, <color>,
<physical_bin>[, <over_on_flag>] ;

<major_bin> := <character>[<character>]

<minor_bin> := <string_with_vars>

<evaluation_limit> := <integer>

<consideration window> := <integer>

<action_limit> := <integer>

<message> := <string> given as report warning or
stop message

<setup_section> := context_config_file = <string>;
context_analog_control_file = <string>;
context_attrib_file = <string>;
context_channel_attrib_file = <string>;
context_config_file = <string>;
context_levels_file = <string>;
context_mixsgl_file = <string>;
context_protocols = <string>;
context_routing_file = <string>;
context_testtable_file = <string>;
context_timing_file = <string>;
context_vector_file = <string>;
context_waveform_file = <string>;

<color> := an integer number (where 0 = black, 1 = white, 2 = red,
3 = yellow, 4 = green, 5 = cyan, 6 = blue, 7 = magenta),
or the name of the color in lower case.

<expression> := an arithmetic, string and/or boolean
expression with operators:
+
-
*
/
>
>=
<
<=
==
!=
(
)
and
or
not
and operands:
pass(<test_suite>)
fail(<test_suite>)
tf_result(<test_suite>,<result_index>)
has_run(<test_suite>)
has_not_run(<test_suite>)
* wsus()
tsus()
lsus()
dsus()
bsus()
( expression )
@<var_name>
<real_number>
<string>

<string_with_vars> := "[[<chars>] \@<var_name> ]... [<chars>]"

<result_index> := <integer> in the range from 0 to
TF_MAX_NR_RSLTS-1

<label> := [A-Za-z]<chars>

<string> := any sequence of ASCII characters delimited
by ""
<chars> := any sequence of ASCII characters without "

<real_number> := any integer or real number, containing [0-9]
and for real numbers, the decimal point.

<integer> := an integer number

<boolean> := {0 | 1}
```

### Example（取自子主题 Testflow file）

```
hp93000,testflow,0.1
language_revision = 1;

information

device_name = "74145";

device_revision = "1";

test_revision = "1";

description = "The 74145 is a BCD-to-Decimal Converter";

end
-----------------------------------------------------------------
declarations

end
-----------------------------------------------------------------
implicit_declarations

end
-----------------------------------------------------------------
flags

datalog_formatter = 0;
datalog_sample_size = 1;
graphic_result_displa = 1;
state_display = 0;
print_wafermap = 0;
ink_wafer = 0;
max_reprobes = 1;
temp_monitor = 1;
calib_age_monitor = 1;
diag_monitor = 1;
current_monitor = 1;
log_events_enable = 1;
set_pass_level = 0;
set_fail_level = 0;
set_bypass_level = 0;
hold_on_fail = 0;
global_hold = 0;
debug_mode = 0;
debug_analog = 0;
parallel_mode = 1;
site_match_mode = 2;
global_overon = 0;
limits_enable = 0;
test_number_enable = 1;
test_number_inc = 1;
log_cycles_before = 0;
log_cycles_after = 0;
unburst_mode = 0;
sqst_mode = 0;
warn_as_fail = 1;
use_hw_dsp = 0;
dsp_file_enable = 0;
buffer_testflow_log = 0;
check_testmethod_api = 0;
stdf_generation = 1;
tm_crash_as_fatal = 1;
hidden_datalog_mode = 0;
multibin_mode = 0;
end
-----------------------------------------------------------------
testmethodparameters
tm_1:
"testName" = "Functional";
"output" = "ReportUI";
tm_2:
"pinlist" = "@";
"testCurrent" = "-80[uA]";
"settlingTime" = "4[ms]";
"measurementMode" = "PPMUpar";
"polarity" = "BPOL";
"prechargeToZeroVol" = "ON";
"testName" = "passVolt_mV";
"output" = "ReportUI";
tm_3:
"pinlist" = "io_in";
"measure" = "BOTH";
"measureMode" = "PPMUpar";
"relaySwitchMode" = "DEFAULT(BBM)";
"forceVoltageLow" = "0[mV]";
"forceVoltageHigh" = "4500[mV]";
"spmuClampCurrentLow" = "0[uA]";
"spmuClampCurrentHigh" = "0[uA]";
"ppmuPreCharge" = "ON";
"prechargeVoltageLow" = "0[mV]";
"prechargeVoltageHigh" = "0[mV]";
"settlingTimeLow" = "2[ms]";
"settlingTimeHigh" = "2[ms]";
"preFunction" = "ALL";
"controlTestNumOfFunctional" = "NO";
"stopCycVecLow" = "0";
"stopCycVecHigh" = "0";
"testName" = "(passCurrentLow_uA,passCurrentHigh_uA)";
"output" = "ReportUI";
end
-----------------------------------------------------------------
testmethodlimits
tm_1:
"Functional" = "":"NA":"":"NA":"":"":"";
tm_2:
"passVolt_mV" = "200":"GE":"800":"LE":"":"":"0";
tm_3:
"passCurrentLow_uA" = "-100":"GE":"100":"LE":"":"":"0";
"passCurrentHigh_uA" = "-100":"GE":"100":"LE":"":"":"0";
end
-----------------------------------------------------------------
testmethods
tm_1:
testmethod_class = "ac_tml.AcTest.FunctionalTest";
tm_2:
testmethod_class = "dc_tml.DcTest.Continuity";
tm_3:
testmethod_class = "dc_tml.DcTest.Leakage";
end
-----------------------------------------------------------------
test_suites
Continuity:
override = 1;
override_tim_equ_set = 1;
override_lev_equ_set = 2;
override_tim_spec_set = 1;
override_lev_spec_set = 2;
override_timset = 1;
override_levset = 1;
override_seqlbl = "gross_func";
override_testf = tm_2;
local_flags = output_on_pass, output_on_fail, value_on_pass, value_on_fail, per_pin_on_pass, per_pin_on_fail;
site_match = 0;
site_control = "parallel:";
Leakage:
override = 1;
override_tim_equ_set = 1;
override_lev_equ_set = 2;
override_tim_spec_set = 1;
override_lev_spec_set = 1;
override_timset = 1;
override_levset = 1;
override_seqlbl = "gross_func_leak";
override_testf = tm_3;
local_flags = output_on_pass, output_on_fail, value_on_pass, value_on_fail, per_pin_on_pass, per_pin_on_fail;
site_match = 0;
site_control = "parallel:";
gross_func:
override = 1;
override_tim_equ_set = 1;
override_lev_equ_set = 2;
override_tim_spec_set = 1;
override_lev_spec_set = 2;
override_timset = 1;
override_levset = 1;
override_seqlbl = "gross_func";
override_testf = tm_1;
local_flags = output_on_pass, output_on_fail, value_on_pass, value_on_fail, per_pin_on_pass, per_pin_on_fail;
site_match = 0;
site_control = "parallel:";
end
-----------------------------------------------------------------
test_flow

run_and_branch(Continuity)
then
{
}
else
{
stop_bin "2", "Failed Continuity", , bad, noreprobe, red, 2, over_on;
}
run_and_branch(gross_func)
then
{
}
else
{
stop_bin "4", "Failed functional", , bad, noreprobe, red, 4, over_on;
}
run_and_branch(Leakage)
then
{
}
else
{
stop_bin "6", "Failed Leakage", , bad, noreprobe, red, 6, over_on;
}
stop_bin "1", "Pass", , good, noreprobe, green, 1, over_on;
end
-----------------------------------------------------------------
binning
otherwise bin = "db", "", , bad, noreprobe, red, , not_over_on;
end
-----------------------------------------------------------------
context

context_config_file = "pins_74ACT299_Incorruptus_CSDPS";
context_levels_file = "levels";
context_timing_file = "timing";
context_vector_file = "all.binl";
context_channel_attrib_file = "ChannelAttribute.soc";
end
-----------------------------------------------------------------
hardware_bin_descriptions
end
```

### Example（取自子主题 Testflow master file）

```
hp93000,testflow_master_file,0.1

testerfile: testflow

information: files/general.tfl
flags: files/general.tfl
bins: files/general.tfl
setup: files/general.tfl
VAR_Default: files/vars.tfl

GROUP group1: files/group1.tfl
VAR myvar1: files/group1.tfl
VAR myvar2: files/group1.tfl

GROUP group2: files/group2.tfl
VAR myvar3: files/group2.tfl
```

<!-- 语法节 end -->

## 是什么

**文档事实** Testflow Tool 是 SmarTest Work Center 中用于开发和调试 testflow 的 GUI 工具。

**文档事实** testflow 是由各个测试互连而成的集合，每个测试检验一个特定参数；这些测试可以按顺序、按先前/其他测试结果、在某个条件成立期间等多种方式互连，共同组成对器件的完整测试。

**文档事实** Testflow Tool 有两个编辑器用于开发和调试 testflow：Flow Data Editor 以表格/电子表格形式显示 testflow 元素，便于纵览各组件、也便于调试；Flow Sequence Editor 显示测试的流程图，提供 testflow 结构信息。两者以两种不同方式表示同一份 testflow 文件中的信息。

**文档事实** 两个编辑器处理的是同一个 testflow 文件，该文件位于 `<device directory>/testflow` 目录。Testflow Properties view 显示所选 test suite 的属性。

**文档事实** testflow 可以存成单个文件，也可以把各部分存成独立子文件，再由 testflow master file 把组成完整 testflow 的各部分汇总起来；后一种结构便于多个用户并行处理同一 testflow。

**文档事实** 使用 Testflow Tool 时还可获得导航辅助（书签、Flow Data Editor 的过滤行、Flow Sequence Editor 的搜索、Next/Previous Annotation 按钮）、运行与调试、testflow 合并等能力；SmarTest 另提供离线的 Hardware Response Emulator 来辅助调试 testflow 或 test suite。

## 典型用法

**文档事实** 打开方式：先打开 93000 Setup perspective，在 Test Program Explorer 视图中双击 testflow 项。若配置为 Open recent editor，会打开最近关闭的编辑器（Flow Data Editor 或 Flow Sequence Editor）与 Properties view；若配置为 Open integrated testflow tool，会打开 Flow Data Editor、Flow Sequence Editor 与 Properties view。也可右键 testflow 项，选择 Open With > Flow Sequence Editor 或 Open With > Flow Data Editor 只打开其中一个编辑器。

**文档事实** 编辑 testflow 的步骤包括：打开工具、创建 testflow、选择 setup 文件、插入 test suite 与 bin、在 Flow Data Editor 中编辑 test suite、在 Tests 页或 Properties view 添加 limit、处理节点、变量、打印 testflow 的图形表示、从 CSV 导入或导出到 CSV、识别 burst 中的 fail label。

**文档事实** 可以直接运行整个 testflow，或运行其中一个/多个 test suite；也可以让 testflow 或单个 test suite 在循环中运行直到满足指定条件。文档说明这适用于调试 testflow，或把新 test suite 集成进 testflow 时。

**文档事实** 调试时 SmarTest 会自动显示 Debug view；开始调试前用 Debug Mode flag 选择 Report window 中的调试信息级别；可以逐个 test suite 单步执行（SmarTest 7.1.0 引入单步执行模式）；多 site 调试时可借助 Site Control Window 识别通过/失败的 site，并查看各 site 的结果。

**文档事实** 合并 testflow 时，目标 testflow 需先加载，然后在 Test Program Explorer 中右键 testflow 项并选择 Open testflow to merge 选源 testflow；在源 testflow 的 Flow Sequence Editor 中复制一个或多个元素并粘贴到目标 testflow，节点设置会一并复制。若复制元素用到目标中不存在的变量，SmarTest 会打开 Add New Variables 窗口；若合并后 test suite 的 primary 设置无效，需要手工修正。

**文档事实** Hardware Response Emulator（HWRE）用于离线调试 testflow 或 test suite：Import 模式导入 hardware response 文件中的数据，并在执行期间返回给 testflow 或 test method API；Store 模式从在线执行的测量数据或离线执行的用户提供数据生成 hardware response 文件。

**文档事实** Report Window 中按 site 打印的消息可通过 `.testflow.ReportUiOutput.user_def` 配置，支持 `<passed>`、`<failed>` 行以及 `%site`、`%bin`、`%testSuiteName` 等占位符，`#` 开头的行是注释；示例包括同时打印通过/失败 site、只打印失败 site、以及 test suite 执行后打印失败 site。

**文档事实** Testflow Tool 可在 Preferences window（Window > Preferences）中配置；相关偏好页包括 Testflow Tool、Flow Sequence Editor、Testflow Tool - Table Annotations、Test Suites preference page。

**建议** 即使 testflow 文件是文本文件、可以直接用文本编辑器修改，文档也建议只通过 Testflow Tool 修改设置，以避开参数范围检查等加载错误。

## 和谁有关

- **Flow Data Editor** — **文档事实**：Testflow Tool 的两个编辑器之一，以表格形式显示 testflow 元素，提供组件纵览并辅助调试。
- **Flow Sequence Editor** — **文档事实**：另一个编辑器，以流程图形表示 testflow 结构，并带有插入 Testflow components 的 Palette。
- **Testflow Properties view** — **文档事实**：显示所选 test suite 的属性；Testflow Tool 的 integrated 打开模式会同时打开该视图。
- **Testflow file** — **文档事实**：两个编辑器处理同一份位于 `<device_dir>/testflow` 的文件；该页给出 testflow 文件的 BNF 语法与示例，并建议通过 Testflow Tool 修改设置。
- **Testflow master file** — **文档事实**：testflow 可拆成多个子文件，由 master file 汇总；该页说明 master file 的格式与可拆分的部分（test suite groups、Information、Flags、Bins、Setup、Variables）。
- **Testflow components / Test suites / Bins / Flags / Variables** — **文档事实**：这些是 testflow 的组成元素，工具用于编辑和运行它们；报告消息、调试模式等由相应 flag 控制。
- **Debug view / Site Control Window** — **文档事实**：调试 testflow 时 Debug view 自动显示，Site Control Window 用于多 site 调试时识别通过/失败 site 并查看各 site 结果。
- **Hardware Response Emulator** — **文档事实**：工具提供的离线调试手段，返回预先准备的数据并可控制各 test suite 的 pass/fail。
- **Report window 与 `.testflow.ReportUiOutput.user_def`** — **文档事实**：该文件配置 testflow 执行后打印到 Report Window 的通过/失败 site 消息。
- **Preferences window / Testflow Tool preference page** — **文档事实**：Testflow Tool 的配置入口，包括选择最近编辑器、integrated 打开模式、编辑器选择同步等选项。
- **Test Program Explorer 与 93000 Setup perspective** — **文档事实**：打开 Testflow Tool 的前置环境；在该视图中双击 testflow 项打开工具，右键可执行 Open testflow to merge。
- **Integrated Result Tool** — **文档事实**：其原理页说明可从 data navigation view 在 Testflow Tool 中打开测试或 bin 的定义，也可在 Testflow Tool 中右键测试、从快捷菜单在 Integrated Result Tool 中打开其结果（objpack 入边引文）。

## 版本

**文档事实** 主文档 Functional changes 只记一条：Introduced before SmarTest 6.3.2。其子主题另记有：SmarTest 6.5.2 将 Flow Sequence Editor 集成进 SmarTest Eclipse Work Center、Properties view 取代 Testsuite view（Elements of the Testflow Tool）；SmarTest 7.1.0 引入单步执行调试模式（Debugging a testflow）；SmarTest 7.2.1 在打开 testflow 编辑器时检查 test method 库版本（Opening the Testflow Tool）。

## 出处

- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32_Testflow_Tool.htm`：主源，含 Subtopics、工具定义与 Functional changes。
- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03_Elements_of_the_Testflow_Tool.htm`：两个编辑器、Properties view、同一 testflow 文件与 Functional changes。
- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.03_Hierarchy_within_a_testflow.htm`、`02.08.04.32.01.05_Configuring_the_messages_printed_in_the_Report_Window.htm`、`02.08.04.32.03.05_Testflow_file.htm`、`02.08.04.32.03.06_Testflow_master_file.htm`：语法节所用的四个子主题，提供层次选择、报告消息、testflow 文件语法与 master file 格式。
- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02_Using_the_Testflow_Tool.htm` 及其子主题（Editing、Navigating、Running、Debugging、Merging、Hardware Response Emulator、Configuring）：开发、导航、运行、调试、合并与配置的做法与版本信息。
- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01.01_Opening_the_Testflow_Tool.htm`：打开工具的前置条件与三种打开模式。
