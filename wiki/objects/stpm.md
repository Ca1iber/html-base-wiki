---
type: object
title: SmarTest Program Manager
layer: gui
stage: project
tags: []
related: []
sources:
  - 02_System_reference/02.09_Test_Program_Management/02.09.02_SmarTest_Program_Manager.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# SmarTest Program Manager

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **136,662 字符逐字取自** `<02_System_reference/02.09_Test_Program_Management/02.09.02_SmarTest_Program_Manager.htm>` 及其子主题 `<02_System_reference/02.09_Test_Program_Management/02.09.02.02.01_Creating_and_editing_an_STPM_control_file.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.01_Structure_of_an_STPM_control_file.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.02_File_and_parameter_settings.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.03_Preprocessing_and_postprocessing_scripts.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.04_write_tp.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.05_add_test.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.06_add_burst.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.07_add_test_to_burst.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.08_add_empty_test_group.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.09_remove_test.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.10_replace_test.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.11_remove_label.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.12_add_pattern.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.13_replace_pattern.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.14_tpt_generate_template.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.15_tpt_import_from_device.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.16_tpt_generate_device_dir.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.17_tpt_merge.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.18_tpt_add_test.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.19_tpt_replace_test.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.20_tpt_generate_tp.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.21_tpt_compare_tp.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.22_tpt_generate_test_stages.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.23_extract_subflow.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.24_merge_subflow.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.25_remove_subflow.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.26_clear_duplicated.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.27_clear_unused.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.01_STPM_merge_rules_file_syntax.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.02_new_digital_pin.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.03_overwrite_digital_pin_no.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.04_merge_digital_pin_dir.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.05_new_dps_pin.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.06_overwrite_dps_pin_polarity.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.07_new_pin_group.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.08_overwrite_pin_group.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.09_merge_unused_pin_group.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.10_new_port.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.11_overwrite_port.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.12_new_site.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.13_overwrite_channel.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.14_new_timing_equation_set.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.15_new_waveform.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.16_modify_waveform_index.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.17_overwrite_statemap.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.18_new_level_resource.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.19_overwrite_level_resource.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.20_new_level_equation_set.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.21_new_level_set.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.22_new_ac_specset.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.23_new_dc_specset.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.24_overwrite_ac_spec_typ.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.25_overwrite_ac_spec_minmax.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.26_overwrite_dc_spec_typ.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.27_overwrite_dc_spec_minmax.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.28_overwrite_label_wvt.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.04.29_overwrite_flow_var_value.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.05.01_Test_suite_table_of_a_TPT.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.05.02_Bin_table_of_a_TPT.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.05.03_Test_table_of_a_TPT.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.05.04_Test_parameter_table_of_a_TPT.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.05.05_Test_flag_table_of_a_TPT.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.05.06_Test_stage_table_of_a_TPT.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.05.07_OpenOffice_spreadsheet_for_editing_the_CSV_files.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.06_STPM_command_line_options.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Creating and editing an STPM control file）

See the example file in
`Structure of an STPM control file`（raw: `130860.htm`）
.

### Syntax（取自子主题 STPM command line options）

```
stpm[-help][-version][-timestamp][-licwait][-progress][-debug][-template][-setup <control_file>]
```

The
parameters have these effects:

-help
: Displays online help. No merging is performed and no file needs to
be specified.

-version
: The version of STPM is output to STDOUT.

-timestamp
: A time stamp is added to each line that is output to
STDOUT.

-licwait
: If no license is currently available, STPM waits until one
becomes available.

If this option is not used, STPM exits with an error message when no
license is available.

-debug
: Intermediate file are generated to make debugging easier. What
specific files are generated depends on the operations specified in the control file.

-template
: Templates for a
`control file`（raw: `130562.htm`）
 and
a
`merge rules file`（raw: `130563.htm`）
 are created. No conversion is performed and no
control file needs to be specified.

The template files are located in the

templates
 subdirectory of the current directory.

-setup
: The control file to use. You can specify the file using a
relative or absolute path; relative paths are based on the current directory.

See
`STPM Control Fil`（raw: `130562.htm`）
`e`（raw: `118724.htm`）
 for a description of
control files.

All of the parameters are optional. Specifying no parameter at all is the same as
specifying
stpm -help
.

### Example（取自子主题 STPM command line options）

This example launches STPM with the control file

setup/MyControl.setup
. If no license is available, STPM will wait until
the next license becomes available. Each line it outputs to STDOUT will have a
timestamp:

```
stpm -timestamp -licwait -setup setup/MySetup.setup
```

### Example（取自子主题 Structure of an STPM control file）

Sample control file with support for test methods and
binning:

```
##############################
# Input: Device Test Program Location
##

##############################
# Configuration
##

# Master Test Program (MTP) device path
mtp_device_testflow = '/home/user/93K_Device/project.tf'

# Merge Rules file.
merge_rules = '/home/user/setup/merge_rules.py'

##############################
# Integration Commands
##

add_test(
test_flow_file = './home/user/new1_93k/testflow/test.tf', # Link to new test flow file
test = 'test_n1' # test name
)
add_test(
test_flow_file = './home/user/new2_93k/testflow/test.tf', # Link to new test flow file
test = 'test_n2', # target test name
position = 'first',
lev_reuse = 'auto'
)

##############################
# Output: Device Test Program Location
##

# Write Master Test Program (MTP).
write_tp = '/home/user/93K_Device/project.tf'
```

### Syntax（取自子主题 File and parameter settings）

```
mtp_device_testflow = '<testflow_file>'
[mtp_template_dir = '<tpt_dir>']
[merge_rules = '<rules_file>']
[ate_target = '<platform>']
[ate_model = '<model>']
[ate_version = '<version>']
[temp_dir = '<temp_dir>']
[enable_backup = '<backup?>']
```

### Parameters（取自子主题 File and parameter settings）

The parameters of the commands in the order in which they are
listed above:

[表]
行 1:
  mtp_device_testflow
  <testflow_file> (string) is the name and path of the
    testflow file of the MTP which STPM is to modify or otherwise work with.
    
    It can be an absolute or a relative path. If it is a relative path, the base directory is
    the current working directory at the time STPM was called.
行 2:
  mtp_template_dir
  <tpt_dir> (string) is the name and path of the directory
    containing the test program template (TPT).
    
    It can be an absolute or a relative path. If it is a relative path, the base directory is
    the current working directory at the time STPM was called.
    
    This is an optional parameter. Note, however, that some commands require a valid TPT to
    be specified. This is noted in these commands' descriptions.
行 3:
  merge_rules
  <rules_file> (string) is the name and path of the merge
    rules file to use when adding or replacing tests.
    
    It can be an absolute or a relative path. If it is a relative path, the base directory is
    the current working directory at the time STPM was called.
    
    This is an optional parameter. If it is not specified, no merge rules file is used.
行 4:
  ate_target
  <platform> (string) indicates the type of V93000 architecture
    on which the test program will run:
    
    '93000SS': Smart Scale system
行 5:
  ate_model
  <model> (string) indicates the specific test system on which
    the test program will run.
    
    The available settings depend on the specified ate_target.
    
    For '93000SS', you can specify:
    
    'PS1600'
    
    This is an optional parameter. If it is omitted, the default used depends on the
    setting for ate_target:
行 6:
  ate_version
  <version> (string) is the release number of the SmarTest
    version under which the test program will be running.
    
    This is an optional parameter. If it is omitted, "7.1.4" is used.
行 7:
  temp_dir
  <temp_dir> is the directory to which STPM writes temporary
    files.
    
    It can be an absolute or a relative path. If it is a relative path, the base directory is
    the current working directory at the time STPM was called.
    
    Make sure that the directory already exists and that STPM has write privileges in the
    specified directory.
    
    This is an optional parameter. If it is omitted, /tmp is used (the
    tmp subdirectory of the root directory).
行 8:
  enable_backup
  <backup?> (number) specifies whether STPM generates a
    backup copy of each modified file:
    
    0: No backups are generated.
    
    1: Backups are generated.
    
    When backup files are generated, they are stored in a subdirectory of the directory
    in which the original file is located; the subdirectory is named
    back.
    
    The name of the backup file is the same as the original file name, with a timestamp in
    the form "_YYMMDD_HHMMSS" appended.
    
    For example, the backup copy of a pin configuration file mypins.cfg
    that is created on 2 November 2012 at 21:43:23 is stored as
    <device_directory>/configuration/back/mypins_121102_214323.cfg.
    
    This is an optional parameter. If it is omitted, 1 is used (that is, backups are
    generated).

### Example（取自子主题 File and parameter settings）

See the sample control file in
`Structure of an STPM control file`（raw: `130860.htm`）
.

### Syntax（取自子主题 Preprocessing and postprocessing scripts）

Both the
pre_proc
 (shown below) and
post_proc

parameters have the same
syntax.

```
pre_proc = '<script>[&mdir][&sdir][&mtp_tf][&mtp_pmf][&mtp_conf][&mtp_tim][&mtp_lev][&mtp_tt][&mtp_rout][&mtp_wf][&mtp_anctrl][&mtp_chatt][&mtp_prot][&mtp_att][&stp_tf][&stp_pmf][&stp_conf][&stp_tim][&stp_lev][&stp_tt][&stp_rout][&stp_wf][&stp_anctrl][&stp_chatt][&stp_prot][&stp_att][<user_parameters>]'
```

The
available script parameters in the order in which they are listed above:

[表]
行 1:
  <script>
  The name and path of the script file to call.
    
    The path can be absolute or relative. If it is a relative path, the base directory is the
    current working directory at the time STPM was called.
行 2:
  &mdir
  Full path to the MTP directory.
行 3:
  &sdir
  Full path to the STP directory.
行 4:
  &mtp_tf
  Full path to the MTP testflow file.
行 5:
  &mtp_pmf
  Full path to the MTP pattern master file.
行 6:
  &mtp_conf
  Full path to the MTP configuration file.
行 7:
  &mtp_tim
  Full path to the MTP timing file.
行 8:
  &mtp_lev
  Full path to the MTP levels file.
行 9:
  &mtp_tt
  Full path to the MTP test table file.
行 10:
  &mtp_rout
  Full path to the MTP routing file.
行 11:
  &mtp_wf
  Full path to the MTP waveform file.
行 12:
  &mtp_anctrl
  Full path to the MTP analog control file.
行 13:
  &mtp_chatt
  Full path to the MTP channel attributes file.
行 14:
  &mtp_prot
  Full path to the MTP protocols file.
行 15:
  &mtp_att
  Full path to the MTP pin attributes file.
行 16:
  &stp_tf
  Full path to the STP testflow file.
行 17:
  &stp_pmf
  Full path to the STP pattern master file.
行 18:
  &stp_conf
  Full path to the STP configuration file.
行 19:
  &stp_tim
  Full path to the STP timing file.
行 20:
  &stp_lev
  Full path to the STP levels file.
行 21:
  &stp_tt
  Full path to the STP test table file.
行 22:
  &stp_rout
  Full path to the STP routing file.
行 23:
  &stp_wf
  Full path to the STP waveform file.
行 24:
  &stp_anctrl
  Full path to the STP analog control file.
行 25:
  &stp_chatt
  Full path to the STP channel attributes file.
行 26:
  &stp_prot
  Full path to the STP protocols file.
行 27:
  &stp_att
  Full path to the STP pin attributes file.
行 28:
  <user_parameters>
  Text that is passed unchanged to the script. This text must not contain any words
    that begin with &.

Except for the name of the script file, all elements are optional.

### Example（取自子主题 Preprocessing and postprocessing scripts）

This example executes the
write_tp
 command with two scripts:

Before
write_tp
 itself is executed, the

preparation.py
 script from the current working directory is run. No
parameters are passed to this script.

After
write_tp
 has finished executing, the

cleanup.pl
 script is run. This script receives this parameter string
(assuming that the MTP is located in
/user/johndoe/mtp
):

--mdir
'/user/johndoe/mtp' --cmd write --stage
3

```
write_tp('user/johndoe/mtp/flow1.tf',
pre_proc = 'preparation.py',
post_proc = '/usr/tools/scripts/cleanup.pl &mdir --cmd write --stage 3')
```

### Syntax（取自子主题 write_tp）

```
write_tp(
path = '<mtp_target_file>',
[pre_proc = <pre_proc>, ]
[post_proc = <post_proc>]
)
```

### Parameters（取自子主题 write_tp）

The parameters in the order in which they are listed
above:

[表]
行 1:
  path
  <mtp_target_file> (string) is the name and location under
    which STPM saves the MTP (master test program) testflow file after it has modified it.
    
    It can be an absolute or a relative path. If it is a relative path, the base directory is
    the current working directory at the time STPM was called.
    
    You can specify the same file here as for mtp_device_testflow. In that
    case, the original file is modified in place.
    
    (You can still have STPM automatically create a backup of the MTP; see `enable_backup`（raw: `131038.htm`） for details.)
行 2:
  pre_proc
  <pre_proc> is a script that is executed before this
    command.
    
    The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `143913.htm`）.
    
    This is an optional parameter.
行 3:
  post_proc
  <post_proc> is a script that is executed after this
    command.
    
    The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `143913.htm`）.
    
    This is an optional parameter.
```

```

### Example（取自子主题 write_tp）

See the sample control file in
`Structure of an STPM control file`（raw: `130860.htm`）
.

### Syntax（取自子主题 add_test）

```
add_test(
test_flow_file = '<testflow_file>',
[test_source = '<test_source>', ]
[test_group = '<test_group>', ]
[test = '<test>', ]
[position = '<position>', ]
[tim_reuse = '<timing_reuse>', ]
[lev_reuse = '<level_reuse>', ]
[pat_reuse = '<pattern_reuse>', ]
[reuse_scope = '<scope>', ]
[pat_dir = '<path>', ]
[test_flags = [<test_flags>], ]
[test_method = '<method>', ]
[test_params = {<params>}, ]
[sbin_num = <sbin_num>,]
[sbin_label = '<sbin_label>', ]
[hbin_num = <hbin_num>,]
[hbin_label = '<hbin_label>', ]
[pre_proc = <pre_proc>, ]
[post_proc = <post_proc>]
)
```

### Parameters（取自子主题 add_test）

The parameters in the order in which they are listed
above:

[表]
行 1:
  test_flow_file
  <testflow_file> (string) is the path, including the name,
    of the testflow file of the source test program (STP) that contains the test that you want
    to add to the MTP.
    
    The path can be either absolute or relative to the current working directory.
行 2:
  test_source
  <test_source> (string) is the name of the test from the
    STP that will be added to the MTP.
    
    If the STP contains only a single test, the test_source parameter can
    be omitted. If the STP contains multiple tests, test_source is
    required.
行 3:
  test_group
  <test_group> (string) is the testflow group in which the
    test suite is generated.
    
    If this parameter is not specified, the test suite is generated at the root of the MTP,
    at the end of the testflow.
行 4:
  test
  <test> is the name for the added test in the MTP.
    
    If this parameter is omitted, the name is added to the MTP with the same name that it has
    in the STP.
    
    If there is already a test with the same name in the MTP, the test from the STP is not
    added and an error is generated. (This applies in both cases, whether you have specified a
    name using the test parameter or whether the default name is used.)
行 5:
  position
  <position> (string) is the position within a test group
    where the new test is inserted.
    
    The following values are available:
    
    optimal: STPM inserts the test in a position in the testflow group
    that requires the least amount of level and timing reloads during execution.
    
    first: The test suite is inserted as the first test in the testflow
    group.
    
    last: The test suite is inserted as the last in the testflow
    group.
    
    after:<test_name>: The test suite is
    inserted immediately after the test suite with the name
    <test_name> in the testflow group.
    
    before:<test_name>: The test suite is
    inserted immediately before the test suite with the name
    <test_name> in the testflow group.
    
    If this parameter is omitted, optimal is used.
    
    If the test_group parameter (see above) is omitted, the
    position parameter is ignored.
行 6:
  tim_reuse
  <timing_reuse> (string) is the way in which timing
    settings in the MTP are to be reused for the added test:
    
    auto: STPM tries to reuse an existing timing, merging the timing
    from the new test with it. If this is not possible, a new timing is created.
    
    test:<test-name>: The timing from the
    existing test suite with the name <test-name> is used for the
    added test.
    
    <primary-keys>: You can explicitly specify the timing to use.
    How to do this differs for single-port and multiport tests:
    
    Single-port timing: Specify the timing as a combination of indexes, separated by
    periods:
    <eqnset-index>.<timset-index>.<specset-index>
    
    Multiport timing: Specify the name of the multiport specification to use.
    
    none: STPM will not try to reuse any timing. Instead, it always
    creates new timing for the added test.
    
    If this parameter is omitted, none is used.
行 7:
  lev_reuse
  <level_reuse> (string) is the way in which level settings
    in the MTP are to be reused for the added test:
    
    auto: STPM tries to reuse existing levels, merging the levels from
    the new test with hem. If this is not possible, new levels are created.
    
    test:<test-name>: The levels from the
    existing test suite with the name <test-name> are used for the
    added test.
    
    <primary-keys>: You can explicitly specify the levels to use
    as a combination of indexes, separated by
    periods:
    <eqnset-index>.<levelset-index>.<specset-index>
    
    none: STPM will not try to reuse any levels. Instead, it always
    creates new levels for the added test.
    
    If this parameter is omitted, none is used.
行 8:
  pat_reuse
  <pattern_reuse> (string) is the way in which patterns in
    the MTP are to be reused for the added test:
    
    test:<test-name>: The patterns from the
    existing test suite with the name <test-name> are used for the
    added test.
    
    <pattern-label>: You can explicitly specify the patterns to
    use by providing the name of the pattern label.
    
    none: STPM will not try to reuse any patterns. Instead, it always
    creates new patterns for the added test.
    
    If this parameter is omitted, none is used.
行 9:
  reuse_scope
  <scope> (string or list of strings) are the testflow
    groups that STPM is to analyze for purposes of merging or reusing primaries. STPM will
    ignore primaries from other testflow groups.
    
    The scope can be:
    
    "*all*" to tell STPM to consider all groups
    
    A comma-separated list of testflow groups, enclosed in square brackets
    
    If this parameter is not specified, the default is for STPM to consider the test
    suites in the testflow group specified in the test_group parameter (see
    above).
    
    If test_group is not specified either, all groups are considered.
行 10:
  pat_dir
  <path> (string) is the path of the directory where STPM is
    to store patterns that it copies from the STP to the device directory.
    
    The path is relative to the vectors subdirectory of the device
    directory.
    
    If this parameter is omitted, patterns is used. (That is, the
    patterns are copied to the vectors/patterns/ subdirectory of the
    device directory.)
行 11:
  test_flags
  <test_flags> (list of strings) is a list of test suite
    flags that are enabled for the imported test. The list must be enclosed in square
    brackets.
    
    Include in the list each test suite flag you want to be enabled for the test in the MTP,
    enclosed in quotes and separated by commas.
    
    You can specify all flags supported in SmarTest. Use these spellings:
    
    bypass
    
    fail_per_label
    
    ffc_enable
    
    ffc_scan_enable
    
    ffv_enable
    
    frg_enable
    
    frg_single_shot
    
    hold
    
    hold_on_fail
    
    mx_waves_enable
    
    output_on_fail
    
    output_on_pass
    
    per_pin_on_fail
    
    per_pin_on_pass
    
    set_pass
    
    set_fail
    
    value_on_fail
    
    value_on_pass
    
    For example: test_flags = ['hold_on_fail','per_pin_on_fail']
    
    If this parameter is omitted, no flags are enabled for the test.
行 12:
  test_method
  <method> (string) is the class of the test method of the
    test being added (for example, "ac_tml.AcTest.FunctionalTest").
    
    If this parameter is omitted, the test is added to the MTP with the same type that it has
    in the STP.
行 13:
  test_params
  <params> (list of name/value pairs) is a list of parameter
    values with which to call the test method.
    
    This is a list of name/value pairs that are separated by commas; the entire list is
    wrapped in curly braces:
    {<name>':'<value>',...}
    
    Each name and value is a string, both are separated by a colon:
    
    <name> is the name of a parameter that is known to the test
    method.
    
    <value> is the value that is passed into this parameter when
    the test method is called.
    
    For example: test_params = {'param1':'0','my_param':'CLK'}
    
    This is an optional parameter. If it is omitted, no parameters are passed to the test
    method.
行 14:
  sbin_num
  <sbin_num> (string) is the software bin ID of the bin
    associated with the added test.
    
    To be compatible with the SmarTest Data Formatter, the number must be between 0 and
    32767.
    
    This is an optional parameter; if hbin_num (see below) is specified,
    it is required. If it is omitted, a "Run" node without any associated bin is inserted in
    the test flow.
行 15:
  sbin_label
  <description> (string) is a short text describing the
    purpose of the software bin. It is intended for human readers.
    
    This is an optional parameter. If it is omitted, the bin remains unlabeled.
行 16:
  hbin_num
  <hbin_num> (number) is the ID of the hardware bin connected to
    the software bin you are defining.
    
    This is an optional parameter. If sbin_num (see above) is not
    specified, the hbin_num parameter cannot be specified.
行 17:
  hbin_label
  <hbin_label> (string) is a short text describing the
    purpose of the hardware bin. It is intended for human readers.
    
    This is an optional parameter. If it is omitted, the bin remains unlabeled.
行 18:
  pre_proc
  <pre_proc> is a script that is executed before this
    command.
    
    The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `143913.htm`）.
    
    This is an optional parameter.
行 19:
  post_proc
  <post_proc> is a script that is executed after this
    command.
    
    The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `143913.htm`）.
    
    This is an optional parameter.

### Example（取自子主题 add_test）

See the sample control file in
`Structure of an STPM control file`（raw: `130860.htm`）
.

### Syntax（取自子主题 add_burst）

```
add_burst(
name = '<burst_name>',
[ports = ('<port>', ... ),]
[pre_proc = <pre_proc>, ]
[post_proc = <post_proc>]
)
```

### Parameters（取自子主题 add_burst）

The parameters in the order in which they are listed
above:

[表]
行 1:
  name
  <testflow_file> (string) is the path, including the name,
    of the testflow file of the source test program (STP) that contains the test that you want
    to add to the MTP.
    
    The path can be either absolute or relative to the current working directory.
行 2:
  ports
  <ports> (list of strings) is a list of the ports for which
    the burst will be generated.
    
    You can list any number of ports. Each port must be an individual string, the strings
    must be separated by commas, and the list must be enclosed in parentheses.
    
    This parameter is optional. If it is not specified, STPM creates a single-port burst.
行 3:
  pre_proc
  <pre_proc> is a script that is executed before this
    command.
    
    The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `143913.htm`）.
    
    This is an optional parameter.
行 4:
  post_proc
  <post_proc> is a script that is executed after this
    command.
    
    The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `143913.htm`）.
    
    This is an optional parameter.

### Syntax（取自子主题 add_test_to_burst）

```
add_test_to_burst(
test_flow_file = '<testflow_file>',
[test_source = '<test_source>', ]
test = '<test>',
[position = '<position>', ]
[pat_dir = '<path>', ]
[pat_reuse = '<mode>',]
[pre_proc = <pre_proc>, ]
[post_proc = <post_proc>]
)
```

### Parameters（取自子主题 add_test_to_burst）

The parameters in the order in which they are listed
above:

[表]
行 1:
  test_flow_file
  <testflow_file> (string) is the path (including the name)
    of the testflow file of the source test program (STP) that contains the test that you want
    to add to the test in the MTP.
    
    The path can be either absolute or relative to the current working directory.
行 2:
  test_source
  <test_source> (string) is the name of the test from the
    STP that will be added to the MTP.
    
    If the STP contains only a single test, the test_source parameter can
    be omitted. If the STP contains multiple tests, test_source is
    required.
行 3:
  test
  <test> (string) is the name of the existing test in the
    MTP. The test from the STP is added to this test.
行 4:
  position
  <position> (string) is the position within the existing
    pattern burst where the new test is inserted.
    
    The following values are available:
    
    first: STPM inserts the pattern from the STP at the beginning of the
    test (burst) in the MTP.
    
    last: The pattern from the STP is inserted at the end of the test
    (burst) in the MTP.
    
    after:<label_name>: The pattern from the
    STP is inserted immediately after the label with the name
    <label_name> in the test in the MTP.
    
    before:<label_name>: The pattern from the
    STP is inserted immediately before the label with the name
    <label_name> in the test in the MTP.
    
    If this parameter is omitted, last is used.
行 5:
  pat_dir
  <path> (string) is the path of the directory where STPM is
    to store patterns that it copies from the STP to the device directory.
    
    The path is relative to the vectors subdirectory of the device
    directory.
    
    If this parameter is omitted, patterns is used. (That is, the
    patterns are copied to the vectors/patterns/ subdirectory of the
    device directory.)
行 6:
  pat_reuse
  <mode> (string) is the way in which patterns in the MTP
    are to be reused for the test that is added to the burst:
    
    test:<test-name>: The patterns from the
    existing test suite with the name <test-name> are used for the
    added test.
    
    <pattern-label>: You can explicitly specify the patterns to
    use by providing the name of the pattern label.
    
    none: STPM will not try to reuse any patterns. Instead, it always
    creates new patterns for the added test.
    
    If this parameter is omitted, none is used.
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

### Example（取自子主题 add_test_to_burst）

See the sample control file in
`Structure of an STPM control file`（raw: `130860.htm`）
.

### Syntax（取自子主题 add_empty_test_group）

```
add_empty_test_group(
test_group = '<test_group>',
[description = '<description>',]
[parent = '<parent>', ]
[position = '<position>', ]
[pre_proc = <pre_proc>, ]
[post_proc = <post_proc>]
)
```

### Parameters（取自子主题 add_empty_test_group）

The parameters in the order in which they are listed
above:

[表]
行 1:
  test_group
  <test_group> (string) is the name of the new test group
    you want to create in the MTP.
行 2:
  description
  <description> is a brief statement about the purpose of
    the new test group.
    
    This parameter is intended just for humans; omitting it does not in any way affect the
    function of the test group.
    
    This is an optional parameter. If it is omitted, no description is stored with the test
    group.
行 3:
  parent
  <parent> (string) is the name of the test group in which
    the new test group will be created.
    
    The test group you name as the parent must already exist in the MTP.
    
    This is an optional parameter. If it is not specified, the test group is created at the
    top level of the MTP.
行 4:
  position
  <position> (string) is the position within the parent
    where the new test group is created.
    
    The following values are available:
    
    first: The test group is created at the beginning of the
    parent.
    
    last: The test group is created at the end of the parent.
    
    If this parameter is omitted, last is used.
行 5:
  pre_proc
  <pre_proc> is a script that is executed before this
    command.
    
    The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `143913.htm`）.
    
    This is an optional parameter.
行 6:
  post_proc
  <post_proc> is a script that is executed after this
    command.
    
    The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `143913.htm`）.
    
    This is an optional parameter.

### Syntax（取自子主题 remove_test）

```
remove_test(
test = '<test>',
[tim_remove = '<timing_remove>', ]
[lev_remove = '<level_remove>', ]
[pat_remove = '<pattern_remove>', ]
[test_remove = <test_remove>, ]
[keep_pat_label = <keep_label>, ]
[pre_proc = <pre_proc>, ]
[post_proc = <post_proc>]
)
```

### Parameters（取自子主题 remove_test）

The parameters in the order in which they are listed
above:

[表]
行 1:
  test
  <test> (string) is the name of the test suite in the MTP
    that STPM should remove.
行 2:
  tim_remove
  <timing_remove> is an instruction for STPM on how to
    remove the timing settings of the removed test:
    
    unused: STPM removes the settings if no other test uses them. (STPM
    may not be able to detect usage by tests that switch primaries in the C++ code.)
    
    none: The timing settings are not removed, even if no other test
    uses them.
    
    If this parameter is omitted, unused is used.
行 3:
  lev_remove
  <level_remove> (string) is an instruction for STPM on how
    to remove the levels of the removed test:
    
    unused: STPM removes the levels if no other test uses them. (STPM
    may not be able to detect usage by tests that switch primaries in the C++ code.)
    
    none: The levels are not removed, even if no other test uses
    them.
    
    If this parameter is omitted, unused is used.
行 4:
  pat_remove
  <pattern_remove> (string) is an instruction for STPM on
    how to remove the patterns of the removed test:
    
    unused: STPM removes the patterns if no other test uses them. (STPM
    may not be able to detect usage by tests that switch primaries in the C++ code.)
    
    none: The patterns are not removed, even if no other test uses
    them.
    
    If this parameter is omitted, unused is used.
行 5:
  test_remove
  <test_remove> (number) specifies whether the test suite is
    removed from the MTP:
    
    0: The test suite is not removed.
    
    1: The test suite is removed.
    You can still remove timing, level, or patterns as
    described above. Indexes in the test suite that point to removed primaries are reset.
    
    This parameter is optional. If it is not specified, the test suite is removed (as if
    you had specified test_remove = 1.)
行 6:
  keep_pat_label
  <keep_label> (number) specifies whether the test suite
    labels in the MTP are kept when the test is removed:
    
    0: The pattern labels are removed from the MTP.
    
    1: The pattern labels are kept in the MTP.
    
    This parameter is optional. If it is not specified, the labels are removed (as if
    you had specified keep_pat_label = 0.)
    
    This parameter is ignored if test_remove = 0 is specified
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

### Syntax（取自子主题 replace_test）

```
replace_test(
test_flow_file = '<testflow_file>',
[test_source = '<test_source>', ]
test = '<test>',
[tim_reuse = '<timing_reuse>', ]
[lev_reuse = '<level_reuse>', ]
[pat_reuse = '<pattern_reuse>', ]
[reuse_scope = '<scope>', ]
[copy_test_method = '<copy_tm_att>', ]
[tim_remove = '<timing_remove>', ]
[lev_remove = '<level_remove>', ]
[pat_remove = '<pattern_remove>', ]
[pat_dir = '<path>', ]
[pre_proc = <pre_proc>, ]
[post_proc = <post_proc>]
)
```

### Parameters（取自子主题 replace_test）

The parameters in the order in which they are listed
above:

[表]
行 1:
  test_flow_file
  <testflow_file> (string) is the path (including the name)
    of the testflow file of the source test program (STP) that contains the test with which you
    want to replace an existing test in the MTP.
    
    The path can be either absolute or relative to the current working directory.
行 2:
  test_source
  <test_source> (string) is the name of the test from the
    STP that will be used to replace the existing test in the to the MTP.
    
    If the MTP already contains a test by that name and the primaries are already set for
    that test, an error is generated and the test is not added to the MTP.
    
    If the STP contains only a single test, the test_source parameter can
    be omitted. If the STP contains multiple tests, test_source is
    required.
行 3:
  test
  <test> (string) is the name of the test in the MTP that is
    to be replaced.
行 4:
  tim_reuse
  <timing_reuse> (string) is the way in which timing
    settings in the MTP are to be reused for the replacement test:
    
    auto: STPM tries to reuse an existing timing, merging the timing
    from the replacement test with it. If this is not possible, a new timing is created.
    
    test:<test-name>: The timing from the
    existing test suite with the name <test-name> is used for the
    replacement test.
    
    <primary-keys>: You can explicitly specify the timing to use.
    How to do this differs for single-port and multiport tests:
    
    Single-port timing: Specify the timing as a combination of indexes, separated by
    periods:
    <eqnset-index>.<timset-index>.<specset-index>
    
    Multiport timing: Specify the name of the multiport timing set to use.
    
    none: STPM will not try to reuse any timing. Instead, it always
    creates new timing for the replacement test.
    
    If this parameter is omitted, none is used.
行 5:
  lev_reuse
  <level_reuse> (string) is the way in which level settings
    in the MTP are to be reused for the replacement test:
    
    auto: STPM tries to reuse existing levels, merging the levels from
    the replacement test with them. If this is not possible, new levels are created.
    
    test:<test-name>: The levels from the
    existing test suite with the name <test-name> are used for the
    replacement test.
    
    <primary-keys>: You can explicitly specify the levels to use
    as a combination of indexes, separated by
    periods:
    <eqnset-index>.<levelset-index>.<specset-index>
    
    none: STPM will not try to reuse any levels. Instead, it always
    creates new levels for the replacement test.
    
    If this parameter is omitted, none is used.
行 6:
  pat_reuse
  <pattern_reuse> (string) is the way in which patterns in
    the MTP are to be reused for the replacement test:
    
    test:<test-name>: The patterns from the
    existing test suite with the name <test-name> are used for the
    replacement test.
    
    <pattern-label>: You can explicitly specify the patterns to
    use by providing the name of the pattern label.
    
    none: STPM will not try to reuse any patterns. Instead, it always
    creates new patterns for the replacement test.
    
    If this parameter is omitted, none is used.
行 7:
  reuse_scope
  <scope> (string or list of strings) are the testflow
    groups that STPM is to analyze for purposes of merging or reusing primaries. STPM will
    ignore primaries from other testflow groups.
    
    The scope can be:
    
    "*all*" to tell STPM to consider all groups
    
    A comma-separated list of testflow groups
    
    If this parameter is not specified, the test suites in the testflow group containing
    the replaced test are considered.
行 8:
  copy_test_method
  <copy_tm_att> (0 or 1) specifies whether the attributes
    for the test method of the replaced test are copied from the STP or whether the attributes
    in the MTP are used:
    
    0 (default): The attributes from the MTP are kept.
    
    1: The attributes from the STP are copied to the MTP.
    
    If this parameter is not specified, the attributes from the MTP are kept.
行 9:
  tim_remove
  <timing_remove> (string) is an instruction for STPM on how
    to remove the timing settings of the replaced test:
    
    unused: STPM removes the settings if no other test uses them. (STPM
    may not be able to detect usage by tests that switch primaries in the C++ code.)
    
    none: The timing settings are not removed, even if no other test
    uses them.
    
    If this parameter is omitted, unused is used.
行 10:
  lev_remove
  <level_remove> (string) is an instruction for STPM on how
    to remove the levels of the replaced test:
    
    unused: STPM removes the levels if no other test uses them. (STPM
    may not be able to detect usage by tests that switch primaries in the C++ code.)
    
    none: The levels are not removed, even if no other test uses
    them.
    
    If this parameter is omitted, unused is used.
行 11:
  pat_remove
  <pattern_remove> (string) is an instruction for STPM on
    how to remove the patterns of the replaced test:
    
    unused: STPM removes the patterns if no other test uses them. (STPM
    may not be able to detect usage by tests that switch primaries in the C++ code.)
    
    none: The patterns are not removed, even if no other test uses
    them.
    
    If this parameter is omitted, unused is used.
行 12:
  pat_dir
  <path> (string) is the path of the directory where STPM is
    to store patterns that it copies from the STP to the device directory.
    
    The path is relative to the vectors subdirectory of the device
    directory.
    
    If this parameter is omitted, patterns is used. (That is, the
    patterns are copied to the vectors/patterns/ subdirectory of the
    device directory.)
行 13:
  pre_proc
  <pre_proc> is a script that is executed before this
    command.
    
    The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `143913.htm`）.
    
    This is an optional parameter.
行 14:
  post_proc
  <post_proc> is a script that is executed after this
    command.
    
    The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `143913.htm`）.
    
    This is an optional parameter.

### Example（取自子主题 replace_test）

See the sample control file in
`Structure of an STPM control file`（raw: `130860.htm`）
.

### Syntax（取自子主题 remove_label）

```
remove_label(
label = '<label_name>',
[pmf_only = <pmf_flag>, ]
[pre_proc = <pre_proc>, ]
[post_proc = <post_proc>]
)
```

### Parameters（取自子主题 remove_label）

The parameters in the order in which they are listed
above:

[表]
行 1:
  label
  <label_name> (string) is the name of the label that you
    want to remove from the MTP.
行 2:
  pmf_only
  <pmf_flag> (0 or 1) specifies whether the pattern is
    deleted from the MTP or only its entry from the pattern master:
    
    0 (default): The pattern is deleted from the MPT.
    
    1: The pattern is kept in the MTP, but its entry is removed from the pattern master
    file
    
    If this parameter is not specified, the pattern is deleted from the MTP.
行 3:
  pre_proc
  <pre_proc> is a script that is executed before this
    command.
    
    The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `143913.htm`）.
    
    This is an optional parameter.
行 4:
  post_proc
  <post_proc> is a script that is executed after this
    command.
    
    The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `143913.htm`）.
    
    This is an optional parameter.

### Syntax（取自子主题 add_pattern）

```
add_pattern(
test_flow_file = '<testflow_file>',
context = '<source>',
[pat_dir = '<path>', ]
[pre_proc = <pre_proc>, ]
[post_proc = <post_proc>]
)
```

### Parameters（取自子主题 add_pattern）

The parameters in the order in which they are listed
above:

[表]
行 1:
  test_flow_file
  <testflow_file> (string) is the path (including the name)
    of the testflow file of the source test program (STP) that contains the pattern that you
    want to add to the MTP.
    
    The path can be either absolute or relative to the current working directory.
行 2:
  context
  <source> (string) describes the location of the desired
    pattern in the STP. There are two ways to specify the location:
    
    By providing the label name. For example: "pattern1".
    
    By providing the names of the test and the test suite, divided by a colon. For example:
    "mytest:ts3".
    
    STPM will interpret any string without a colon as a label name and any string with a
    colon as the names of a test and a test suite.
行 3:
  pat_dir
  <path> (string) is the path of the directory where STPM is
    to store patterns that it copies from the STP to the device directory.
    
    The path is relative to the vectors subdirectory of the device
    directory.
    
    If this parameter is omitted, patterns is used. (That is, the
    patterns are copied to the vectors/patterns/ subdirectory of the
    device directory.)
行 4:
  pre_proc
  <pre_proc> is a script that is executed before this command.
    
    The syntax of the parameter value is described in Preprocessing and postprocessing
    scripts.
    
    This is an optional parameter.
行 5:
  post_proc
  <post_proc> is a script that is executed after this command.
    
    The syntax of the parameter value is described in Preprocessing and postprocessing
    scripts.
    
    This is an optional parameter.

### Example（取自子主题 add_pattern）

This example adds the pattern from the test suite "func_ts_2" in the "func_test" test
in the "tf1.tf" testflow to the
/vectors/patterns
 directory of the MTP
device
directory.

```
add_pattern(test_flow_file='/user/johndoe/stp/tf1.tf', context='func_test:func_ts_2')
```

### Syntax（取自子主题 replace_pattern）

```
replace_pattern(
test_flow_file = '<testflow_file>',
context = '<source>',
test = '<test_suite>',
[pat_dir = '<path>', ]
[pat_remove = '<pat_remove>', ]
[waveforms_compare_mode = '<compare_mode>', ]
[pre_proc = <pre_proc>, ]
[post_proc = <post_proc>]
)
```

### Parameters（取自子主题 replace_pattern）

The parameters in the order in which they are listed
above:

[表]
行 1:
  test_flow_file
  <testflow_file> (string) is the path (including the name)
    of the testflow file of the source test program (STP) that contains the pattern that you
    want to add to the MTP.
    
    The path can be either absolute or relative to the current working directory.
行 2:
  context
  <source> (string) describes the location of the desired
    pattern in the STP. There are two ways to specify the location:
    
    By providing the label name. For example: "pattern1".
    
    By providing the names of the test and the test suite, divided by a colon. For example:
    "mytest:ts3".
    
    STPM will interpret any string without a colon as a label name and any string with a
    colon as the names of a test and a test suite.
行 3:
  test
  <test_suite> (string) is the name of the MTP test suite in
    which you want to replace the pattern.
行 4:
  pat_dir
  <path> (string) is the path of the directory where STPM is
    to store patterns that it copies from the STP to the device directory.
    
    The path is relative to the vectors subdirectory of the device
    directory.
    
    If this parameter is omitted, patterns is used. (That is, the
    patterns are copied to the vectors/patterns/ subdirectory of the
    device directory.)
行 5:
  pat_remove
  <pat_remove> (string) specifies whether the old pattern
    from the MTP test suite is deleted from the MTP device directory:
    
    'unused' (default): The pattern is deleted if no other test uses
    it.
    
    'none': The pattern is not deleted.
    
    If this parameter is not specified, the pattern is deleted if no other test uses
    it.
行 6:
  waveforms_compare_mode
  <compare_mode> (string) specifies whether the waveforms in
    the new pattern are compared to the waveforms in the old pattern:
    
    'none' (default): The waveforms of the two patterns are not
    compared.
    
    'error': The waveforms are compared and an error is generated if any
    differences are found.
    
    'warning': The waveforms are compared and a warning is generated if
    any differences are found.
    
    If this parameter is not specified, the waveforms are not compared.
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

### Example（取自子主题 replace_pattern）

This example adds the pattern from the test suite "func_ts_2" in the "func_test" test
in the "tf1.tf" testflow to the
/vectors/patterns
 directory of the MTP
device
directory.

```
add_pattern(test_flow_file='/user/johndoe/stp/tf1.tf', context='func_test:func_ts_2')
```

### Syntax（取自子主题 tpt_generate_template）

```
tpt_generate_template(
tpt_dir = <location>,
[pre_proc = <pre_proc>, ]
[post_proc = <post_proc>]
)
```

### Parameters（取自子主题 tpt_generate_template）

The parameters in the order in which they are listed
above:

[表]
行 1:
  tpt_dir
  <location> (string) is the path, including the name, where
    the new template files and directories are created.
    
    The path can be either absolute or relative to the current working directory.
    
    If the directory does not yet exist, STPM creates it.
行 2:
  pre_proc
  <pre_proc> is a script that is executed before this
    command.
    
    The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `143913.htm`）.
    
    This is an optional parameter.
行 3:
  post_proc
  <post_proc> is a script that is executed after this
    command.
    
    The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `143913.htm`）.
    
    This is an optional parameter.

### Example（取自子主题 tpt_generate_template）

This example creates a test program template in the subdirectory "new_template" of the
current working
directory.

```
generate_new(
tpt_dir = 'new_template'
)
```

### Syntax（取自子主题 tpt_import_from_device）

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

### Parameters（取自子主题 tpt_import_from_device）

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

### Example（取自子主题 tpt_import_from_device）

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

### Syntax（取自子主题 tpt_generate_device_dir）

```
tpt_generate_device_dir(
tpt_dir = <tpt_directory>,
device_dir = <directory>,
[device_name = <device_name>, ]
[pre_proc = <pre_proc>, ]
post_proc = <post_proc>]
)
```

### Parameters（取自子主题 tpt_generate_device_dir）

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

### Example（取自子主题 tpt_generate_device_dir）

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

### Syntax（取自子主题 tpt_merge）

```
tpt_merge(
source_tpts = [<tpt_list>],
target_tpt = <directory>,
[pre_proc = <pre_proc>, ]
[post_proc = <post_proc>]
)
```

### Parameters（取自子主题 tpt_merge）

The parameters in the order in which they are listed
above:

[表]
行 1:
  source_tpts
  <tpt_file> (list of strings) is a list of TPT directories
    that you want to merge into a single TPT.
    
    Include in the list the path of each TPT you want to merge, enclosed in quotes and
    separated by commas.
    
    Paths can be either absolute or relative to the current working directory.
    
    In case of conflicts, objects from any source TPT overwrite those in the target TPT and
    objects from source TPTs at the end of the list overwrite those from TPTs at the beginning
    of the list.
行 2:
  target_tpt
  <directory> (string) is the path, including the name,
    where the merged device directory is created. The TPT must already exist.
    
    The path can be either absolute or relative to the current working directory.
行 3:
  pre_proc
  <pre_proc> is a script that is executed before this
    command.
    
    The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `143913.htm`）.
    
    This is an optional parameter.
行 4:
  post_proc
  <post_proc> is a script that is executed after this
    command.
    
    The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `143913.htm`）.
    
    This is an optional parameter.

### Example（取自子主题 tpt_merge）

This example copies the contents from three test program templates into one new
template..

```
tpt_merge(
source_tpts = ['my_tpt','my_other_tpt','../reference/best_tpt')
target_tpt = '../merged_tpt/'
)
```

### Syntax（取自子主题 tpt_add_test）

```
tpt_add_test(
test_flow_file = '<testflow_file>',
[test_source = '<test_source>', ]
[test = '<test>', ]
[position = '<position>', ]
[tim_reuse = '<timing_reuse>', ]
[lev_reuse = '<level_reuse>', ]
[pat_reuse = '<pattern_reuse>', ]
[reuse_scope = '<scope>', ]
[pat_dir = '<path>', ]
[pre_proc = <pre_proc>, ]
[post_proc = <post_proc>]
)
```

### Parameters（取自子主题 tpt_add_test）

The parameters in the order in which they are listed
above:

[表]
行 1:
  test_flow_file
  <testflow_file> (string) is the path, including the name,
    of the testflow file of the source test program (STP) that contains the test that you want
    to add to the MTP.
    
    The path can be either absolute or relative to the current working directory.
行 2:
  test_source
  <test_source> (string) is the name of the test from the
    STP that will be added to the MTP. The test must be included in the `test suite table`（raw: `132779.htm`）.
    
    If the STP contains only a single test, the test_source parameter can
    be omitted. If the STP contains multiple tests, test_source is
    required.
行 3:
  test
  <test> is the name for the added test in the MTP.
    
    If this parameter is omitted, the name is added to the MTP with the name specified for it
    in the `test suite table`（raw: `132779.htm`）.
    
    If there is already a test with the same name in the MTP, the test from the STP is not
    added and an error is generated. (This applies in both cases, whether you have specified a
    name using the test parameter or whether the default name is used.)
行 4:
  position
  <position> (string) is the position within a test group
    where the new test is inserted.
    
    The following values are available:
    
    optimal: STPM inserts the test in a position in the testflow group
    that requires the least amount of level and timing reloads during execution.
    
    first: The test suite is inserted as the first test in the testflow
    group.
    
    last: The test suite is inserted as the last in the testflow
    group.
    
    after:<test_name>: The test suite is
    inserted immediately after the test suite with the name
    <test_name> in the testflow group.
    
    before:<test_name>: The test suite is
    inserted immediately before the test suite with the name
    <test_name> in the testflow group.
    
    If this parameter is omitted, optimal is used.
行 5:
  tim_reuse
  <timing_reuse> (string) is the way in which timing
    settings in the MTP are to be reused for the added test:
    
    auto: STPM tries to reuse an existing timing, merging the timing
    from the new test with it. If this is not possible, a new timing is created.
    
    test:<test-name>: The timing from the
    existing test suite with the name <test-name> is used for the
    added test.
    
    <primary-keys>: You can explicitly specify the timing to use.
    How to do this differs for single-port and multiport tests:
    
    Single-port timing: Specify the timing as a combination of indexes, separated by
    periods:
    <eqnset-index>.<timset-index>.<specset-index>
    
    Multiport timing: Specify the name of the multiport specification to use.
    
    none: STPM will not try to reuse any timing. Instead, it always
    creates new timing for the added test.
    
    If this parameter is omitted, none is used.
行 6:
  lev_reuse
  <level_reuse> (string) is the way in which level settings
    in the MTP are to be reused for the added test:
    
    auto: STPM tries to reuse existing levels, merging the levels from
    the new test with hem. If this is not possible, new levels are created.
    
    test:<test-name>: The levels from the
    existing test suite with the name <test-name> are used for the
    added test.
    
    <primary-keys>: You can explicitly specify the levels to use
    as a combination of indexes, separated by
    periods:
    <eqnset-index>.<levelset-index>.<specset-index>
    
    none: STPM will not try to reuse any levels. Instead, it always
    creates new levels for the added test.
    
    If this parameter is omitted, none is used.
行 7:
  pat_reuse
  <pattern_reuse> (string) is the way in which patterns in
    the MTP are to be reused for the added test:
    
    test:<test-name>: The patterns from the
    existing test suite with the name <test-name> are used for the
    added test.
    
    <pattern-label>: You can explicitly specify the patterns to
    use by providing the name of the pattern label.
    
    none: STPM will not try to reuse any patterns. Instead, it always
    creates new patterns for the added test.
    
    If this parameter is omitted, none is used.
行 8:
  reuse_scope
  <scope> (string or list of strings) are the testflow
    groups that STPM is to analyze for purposes of merging or reusing primaries. STPM will
    ignore primaries from other testflow groups.
    
    The scope can be:
    
    "*all*" to tell STPM to consider all groups
    
    A comma-separated list of testflow groups, enclosed in square brackets
    
    If this parameter is not specified, the default is for STPM to consider the test
    suites in the testflow group specified in the test_group parameter (see
    above).
    
    If test_group is not specified either, all groups are considered.
行 9:
  pat_dir
  <path> (string) is the path of the directory where STPM is
    to store patterns that it copies from the STP to the device directory.
    
    The path is relative to the vectors subdirectory of the device
    directory.
    
    If this parameter is omitted, patterns is used. (That is, the
    patterns are copied to the vectors/patterns/ subdirectory of the
    device directory.)
行 10:
  pre_proc
  <pre_proc> is a script that is executed before this
    command.
    
    The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `143913.htm`）.
    
    This is an optional parameter.
行 11:
  post_proc
  <post_proc> is a script that is executed after this
    command.
    
    The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `143913.htm`）.
    
    This is an optional parameter.

### Example（取自子主题 tpt_add_test）

See the sample control file in
`Structure of an STPM control file`（raw: `130860.htm`）
.

### Syntax（取自子主题 tpt_replace_test）

```
tpt_replace_test(
test_flow_file = '<testflow_file>',
[test_source = '<test_source>', ]
test = '<test>',
[tim_reuse = '<timing_reuse>', ]
[lev_reuse = '<level_reuse>', ]
[pat_reuse = '<pattern_reuse>', ]
[reuse_scope = '<scope>', ]
[tim_remove = '<timing_remove>', ]
[lev_remove = '<level_remove>', ]
[pat_remove = '<pattern_remove>', ]
[pat_dir = '<path>', ]
[pre_proc = <pre_proc>, ]
[post_proc = <post_proc>]
)
```

### Parameters（取自子主题 tpt_replace_test）

The parameters in the order in which they are listed
above:

[表]
行 1:
  test_flow_file
  <testflow_file> (string) is the path (including the name)
    of the testflow file of the source test program (STP) that contains the test with which you
    want to replace an existing test in the MTP.
    
    The path can be either absolute or relative to the current working directory.
行 2:
  test_source
  <test_source> (string) is the name of the test from the
    STP that will be used to replace the existing test in the to the MTP. The test must be
    included in the `test suite table`（raw: `132779.htm`）.
    
    If the MTP already contains a test by that name and the primaries are already set for
    that test, an error is generated and the test is not added to the MTP.
    
    If the STP contains only a single test, the test_source parameter can
    be omitted. If the STP contains multiple tests, test_source is
    required.
行 3:
  test
  <test> (string) is the name of the test in the MTP that is
    to be replaced.
行 4:
  tim_reuse
  <timing_reuse> (string) is the way in which timing
    settings in the MTP are to be reused for the replacement test:
    
    auto: STPM tries to reuse an existing timing, merging the timing
    from the replacement test with it. If this is not possible, a new timing is created.
    
    test:<test-name>: The timing from the
    existing test suite with the name <test-name> is used for the
    replacement test.
    
    <primary-keys>: You can explicitly specify the timing to use.
    How to do this differs for single-port and multiport tests:
    
    Single-port timing: Specify the timing as a combination of indexes, separated by
    periods:
    <eqnset-index>.<timset-index>.<specset-index>
    
    Multiport timing: Specify the name of the multiport timing set to use.
    
    none: STPM will not try to reuse any timing. Instead, it always
    creates new timing for the replacement test.
    
    If this parameter is omitted, none is used.
行 5:
  lev_reuse
  <level_reuse> (string) is the way in which level settings
    in the MTP are to be reused for the replacement test:
    
    auto: STPM tries to reuse existing levels, merging the levels from
    the replacement test with them. If this is not possible, new levels are created.
    
    test:<test-name>: The levels from the
    existing test suite with the name <test-name> are used for the
    replacement test.
    
    <primary-keys>: You can explicitly specify the levels to use
    as a combination of indexes, separated by
    periods:
    <eqnset-index>.<levelset-index>.<specset-index>
    
    none: STPM will not try to reuse any levels. Instead, it always
    creates new levels for the replacement test.
    
    If this parameter is omitted, none is used.
行 6:
  pat_reuse
  <pattern_reuse> (string) is the way in which patterns in
    the MTP are to be reused for the replacement test:
    
    test:<test-name>: The patterns from the
    existing test suite with the name <test-name> are used for the
    replacement test.
    
    <pattern-label>: You can explicitly specify the patterns to
    use by providing the name of the pattern label.
    
    none: STPM will not try to reuse any patterns. Instead, it always
    creates new patterns for the replacement test.
    
    If this parameter is omitted, none is used.
行 7:
  reuse_scope
  <scope> (string or list of strings) are the testflow
    groups that STPM is to analyze for purposes of merging or reusing primaries. STPM will
    ignore primaries from other testflow groups.
    
    The scope can be:
    
    "*all*" to tell STPM to consider all groups
    
    A comma-separated list of testflow groups
    
    If this parameter is not specified, the test suites in the testflow group containing
    the replaced test are considered.
行 8:
  tim_remove
  <timing_remove> (string) is an instruction for STPM on how
    to remove the timing settings of the replaced test:
    
    unused: STPM removes the settings if no other test uses them. (STPM
    may not be able to detect usage by tests that switch primaries in the C++ code.)
    
    none: The timing settings are not removed, even if no other test
    uses them.
    
    If this parameter is omitted, unused is used.
行 9:
  lev_remove
  <level_remove> (string) is an instruction for STPM on how
    to remove the levels of the replaced test:
    
    unused: STPM removes the levels if no other test uses them. (STPM
    may not be able to detect usage by tests that switch primaries in the C++ code.)
    
    none: The levels are not removed, even if no other test uses
    them.
    
    If this parameter is omitted, unused is used.
行 10:
  pat_remove
  <pattern_remove> (string) is an instruction for STPM on
    how to remove the patterns of the replaced test:
    
    unused: STPM removes the patterns if no other test uses them. (STPM
    may not be able to detect usage by tests that switch primaries in the C++ code.)
    
    none: The patterns are not removed, even if no other test uses
    them.
    
    If this parameter is omitted, unused is used.
行 11:
  pat_dir
  <path> (string) is the path of the directory where STPM is
    to store patterns that it copies from the STP to the device directory.
    
    The path is relative to the vectors subdirectory of the device
    directory.
    
    If this parameter is omitted, patterns is used. (That is, the
    patterns are copied to the vectors/patterns/ subdirectory of the
    device directory.)
行 12:
  pre_proc
  <pre_proc> is a script that is executed before this
    command.
    
    The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `143913.htm`）.
    
    This is an optional parameter.
行 13:
  post_proc
  <post_proc> is a script that is executed after this
    command.
    
    The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `143913.htm`）.
    
    This is an optional parameter.

### Syntax（取自子主题 tpt_generate_tp）

```
tpt_generate_tp(
[generate_complete_device_directory = <complete_device_flag>, ]
[error_on_non_existing_primaries = <missing_primaries_flag>, ]
[ignore_empty_groups = <ignore_empty_groups_flag>, ]
[pre_proc = <pre_proc>, ]
[post_proc = <post_proc>]
)
```

### Parameters（取自子主题 tpt_generate_tp）

[表]
行 1:
  generate_complete_device_directory
  <complete_device_flag> specify whether a complete device
    directory or only a skeleton is generated:
    
    0: The generated device directory contains only a testflow file. If the use of a test
    table is specified in the TPT, a test table is also generated.
    
    1 (default): A complete device directory is generated.
    
    If this parameter is omitted, 1 is used (a complete directory is generated).
行 2:
  error_on_non_existing_primaries
  <missing_primaries_flag> specifies whether warnings are
    generated for missing primaries:
    
    0: STPM generates no warning if a test suite refers to primaries that do not exist in
    the TPT.
    
    1 (default): STPM generates warnings when non-existent primaries are referenced.
    
    If this parameter is omitted, 1 is used (warnings are generated).
行 3:
  ignore_empty_groups
  <ignore_empty_groups_flag> specifies what happens with
    empty groups in the testflow of the TPT:
    
    0: Empty groups are copied to the testflow of the output test program.
    
    1 (default): Empty groups are not copied to the testflow of the output test
    program.
    
    If this parameter is omitted, 1 is used (empty groups are not copied).
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

### Syntax（取自子主题 tpt_compare_tp）

```
tpt_compare_tp(
[report_file_path = '<report_file>', ]
[include_groups = <include_groups>, ]
[pre_proc = <pre_proc>, ]
[post_proc = <post_proc>]
)
```

### Parameters（取自子主题 tpt_compare_tp）

[表]
行 1:
  report_file_path
  <report_file> (string) is the path (including the name)
    where the command is to store the report file.
    
    If this parameter is omitted, the file is named compare_log.html and
    is stored in the current working directory.
行 2:
  include_groups
  <include_groups> (list of strings) is a list of groups in
    the specified testflow that are to be compared.
    
    Each group name is a string enclosed in single or double quotes; groups are separated by
    commas, and the list is enclosed in square brackets.
    
    This parameter is optional. If it is omitted, the entire testflow is compared.
行 3:
  pre_proc
  <pre_proc> is a script that is executed before this
    command.
    
    The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `143913.htm`）.
    
    This is an optional parameter.
行 4:
  post_proc
  <post_proc> is a script that is executed after this
    command.
    
    The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `143913.htm`）.
    
    This is an optional parameter.

### Syntax（取自子主题 tpt_generate_test_stages）

```
tpt_generate_test_stages(
[include_undefined_objects = <flag>, ]
[pre_proc = <pre_proc>, ]
[post_proc = <post_proc>]
)
```

### Parameters（取自子主题 tpt_generate_test_stages）

The parameters in the order in which they are listed
above:

[表]
行 1:
  include_undefined_objects
  <flag> (0 or 1) specifies how STPM treats undefined
    objects in the `test stage table`（raw: `140683.htm`）:
    
    0: Undefined objects are not included in the data log profile.
    
    1 (default): Undefined objects are treated as enabled.
    An object is considered
    undefined for a test stage when the object's row contains neither Y
    nor N in the column for that test stage.
    
    If this parameter is omitted, 1 is used. That is, undefined objects are considered to
    be enabled.
行 2:
  pre_proc
  <pre_proc> is a script that is executed before this
    command.
    
    The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `143913.htm`）.
    
    This is an optional parameter.
行 3:
  post_proc
  <post_proc> is a script that is executed after this
    command.
    
    The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `143913.htm`）.
    
    This is an optional parameter.

### Syntax（取自子主题 extract_subflow）

```
extract_subflow(
test_flow_file = '<file_path>',
test_groups = [<group_list>],
[levels_mode = <levels_mode>, ]
[timing_mode = <timing_mode>,
[pattern_mode = <pattern_mode>, ]
[config_mode = <config_mode>, ]
[keep_tim_eqnsets = [<tim_eqnsets>], ]
[keep_lev_eqnsets = [<lev_eqnsets>], ]
[keep_wavetables = [<wavetables>], ]
[keep_specifications = [<specs>], ]
[keep_pattern_files = [<pattern_files>], ]
[keep_setup_file_names = <keep_file_names_flag>, ]
[copy_static_content = [<copy_items>], ]
[copy_patterns = <copy_pattern_flag>, ]
[allow_overwrite = <overwrite_flag>, ]
[pre_proc = <pre_proc>, ]
[post_proc = <post_proc>]
)
```

### Parameters（取自子主题 extract_subflow）

The parameters in the order in which they are listed
above:

[表]
行 1:
  test_flow_file
  <file_path> (string) is the name and path of the testflow
    file for the STP you want to generate.
    
    It can be an absolute or a relative path. If it is a relative path, the base directory is
    the current working directory at the time STPM was called.
    
    If folders specified in the path do not yet exist, STPM creates them.
行 2:
  test_groups
  <group_list> (list of strings) is a list of test groups
    that are exported. The list must be enclosed in square brackets..
    
    Include in the list each testflow group you want to export to the STP, enclosed in quotes
    and separated by commas.
    
    For example: test_groups = ['tg3','fail_tg']
行 3:
  levels_mode
  <levels_mode> specifies the way in which level settings
    are extracted from the MTP:
    
    'used' (default): Only level settings that are used by the extracted
    test groups are copied from the MTP to the STP.
    
    'all': All level settings from the MTP are copied to the STP, even
    if none of the extracted test groups is using them.
    
    'keep_file': No level settings are copied to the STP. Instead, the
    STP uses the level file of the MTP. This requires that the STP is located in the same
    directory as the MTP.
    
    This parameter is optional. If it is omitted, only the level settings used in the
    subflow are copied.
行 4:
  timing_mode
  <timing_mode> specifies the way in which timing settings
    are extracted from the MTP:
    
    'used' (default): Only timing settings that are used by the
    extracted test groups are copied from the MTP to the STP.
    
    'all': All timing settings from the MTP are copied to the STP, even
    if none of the extracted test groups is using them.
    
    'keep_file': No timing settings are copied to the STP. Instead, the
    STP uses the timing file of the MTP. This requires that the STP is located in the same
    directory as the MTP.
    
    This parameter is optional. If it is omitted, only the timing settings used in the
    subflow are copied.
行 5:
  pattern_mode
  <pattern_mode> specifies the way in which patterns are
    extracted from the MTP:
    
    'used' (default): Only patterns that are used by the extracted test
    groups are copied from the MTP to the STP.
    
    'all': All patterns from the MTP are copied to the STP, even if none
    of the extracted test groups is using them.
    
    This parameter is optional. If it is omitted, only the patterns used in the subflow
    are copied.
行 6:
  config_mode
  <config_mode> specifies the way in which configuration
    settings are extracted from the MTP:
    
    'used': Only configuration settings that are used by the extracted
    test groups are copied from the MTP to the STP.
    
    'all' (default): All configuration settings from the MTP are copied
    to the STP, even if none of the extracted test groups is using them.
    
    This parameter is optional. If it is omitted, all config settings from the MTP are
    copied.
行 7:
  keep_tim_eqnsets
  <tim_eqnsets> is a list of timing equation sets that are
    extracted from the MTP even if they are not used by the extracted test groups.
    
    The value is a list of equation set numbers separated by commas. For example: [1, 5, 9,
    13]
    
    This parameter is optional.
行 8:
  keep_lev_eqnsets
  <lev_eqnsets> is a list of level equation sets that are
    extracted from the MTP even if they are not used by the extracted test groups.
    
    The value is a list of equation set numbers separated by commas. For example: [7,8]
    
    This parameter is optional.
行 9:
  keep_wavetables
  <wavetables> is a list of wavetables that are extracted
    from the MTP even if they are not used by the extracted test groups.
    
    The value is a list of wavetable names, enclosed in quotes and separated by commas. For
    example: ['mytable', 'wavetable2']
    
    This parameter is optional.
行 10:
  keep_specifications
  <specifications> is a list of specifications that are
    extracted from the MTP even if they are not used by the extracted test groups.
    
    The value is a list of specification names, enclosed in quotes and separated by commas.
    For example: ['spec5', 'spec5b']
    
    This parameter is optional.
行 11:
  keep_pattern_files
  <pattern_files> is a list of level pattern files that are
    extracted from the MTP even if they are not used by the extracted test groups.
    
    The value is a list of pattern file paths, enclosed in quotes and separated by commas.
    Paths can be absolute or relative to the directory of the MTP. For example:
    ['/home/johndoe/tps/init_pattern.bin l', 'device/vectors/pat3.binl'']
    
    This parameter is optional.
行 12:
  keep_setup_file_names
  <keep_file_names_flag> specifies whether the names of
    setups are changed in the exported testflow:
    
    0 (default): The names are changed to match the name of the extracted testflow.
    
    1: The names remain the same as in the MTP.
    
    This parameter is optional. If it is omitted, the names are changed.
行 13:
  copy_static_content
  <copy_items> (list of strings) specifies is a list of
    names of files or directories that are to be copied from the device directory of the MTP to
    the device directory of the extracted subflow.
    
    The list may contain only names (of files or directories), not paths. The named items
    must be located in the top level of the device directory. Each name is enclosed in quotes
    and separated by commas.
    
    These values are supported:
    
    A list of names of files or directories (but not paths). The named items must be
    located in the top level of the device directory. Each name is enclosed in quotes and
    separated by commas.
    For example: copy_static_content = ['my_notes.txt','Change
    log']
    
    If you include standard directories in this list (see below), STPM generates a warning
    and does not copy the contents.
    
    ['*all*'] (default): Every file and directory in the device
    directory is copied, except the standard directories testflow,
    timing, levels,
    configuration, vectors, and
    testtable.
    
    []: No additional files or directories are copied.
    
    This parameter is optional. If it is omitted, all objects from the top level of the
    device directory are copied (as if ['*all*'] had been specified).
行 14:
  copy_patterns
  <copy_pattern_flag> specifies whether the patterns from
    the MTP are copied to the STP:
    
    0: The patterns are not copied to the STP. The pattern master file of the STP refers to
    the patterns in the MTP.
    
    1 (default): The patterns are copied to the STP. There are no references to the MTP
    patterns in the pattern master file of the STP.
    
    This parameter is optional. If it is omitted, the patterns are copied.
行 15:
  allow_overwrite
  <overwrite_flag> specifies whether STPM may overwrite
    existing files in the STP directory:
    
    0 (default): No existing files or directories in the device directory may be
    overwritten. If this prevents STPM from saving a created file, it displays an error and
    stops the conversion.
    
    1: STPM may overwrite existing files and directories.
    
    This parameter is optional. If it is omitted, no files or directories are
    overwritten.
行 16:
  pre_proc
  <pre_proc> is a script that is executed before this
    command.
    
    The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `143913.htm`）.
    
    This is an optional parameter.
行 17:
  post_proc
  <post_proc> is a script that is executed after this
    command.
    
    The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `143913.htm`）.
    
    This is an optional parameter.

### Syntax（取自子主题 merge_subflow）

```
merge_subflow(
test_flow_file = '<file_path>',
[include_groups = [<include_group_list>], ]
[exclude_groups = [<exclude_group_list>], ]
[parent = '<parent_group>', ]
[position = '<position>', ]
[tim_eqnset_index = '<tim_index>', ]
[lev_eqnset_index = '<lev_index>', ]
[levels_mode = <levels_mode>, ]
[timing_mode = <timing_mode>, ]
[pattern_mode = <pattern_mode>, ]
[keep_tim_eqnsets = [<tim_eqnsets>], ]
[keep_lev_eqnsets = [<lev_eqnsets>], ]
[keep_wavetables = [<wavetables>], ]
[keep_specifications = [<specs>], ]
[keep_pattern_files = [<pattern_files>], ]
[copy_static_content = [<copy_items>], ]
[pre_proc = <pre_proc>, ]
[post_proc = <post_proc>]
)
```

### Parameters（取自子主题 merge_subflow）

The parameters in the order in which they are listed
above:

[表]
行 1:
  test_flow_file
  <file_path> (string) is the name and path of the testflow
    file for the STP you want to merge into the MTP.
    
    It can be an absolute or a relative path. If it is a relative path, the base directory is
    the current working directory at the time STPM was called.
行 2:
  include_groups
  <include_group_list> (list of strings) is a list of
    testflow groups that STPM is to import. If you use this parameter, only those groups
    specified in the list are imported.
    
    The list must be enclosed in square brackets. Each testflow group in the list must be
    enclosed in quotes and separated by commas.
    
    For example: test_groups = ['tg3','fail_tg']
    
    This parameter is optional. It cannot be used when you also specify
    exclude_groups (see below).
行 3:
  exclude_groups
  <exclude_group_list> (list of strings) is a list of
    testflow groups that STPM is to exclude from the merge process. If you use this parameter,
    all groups from the STP are merged, except those groups specified in the list.
    
    The list must be enclosed in square brackets. Each testflow group in the list must be
    enclosed in quotes and separated by commas.
    
    For example: test_groups = ['tg3','fail_tg']
    
    This parameter is optional. It cannot be used when you also specify
    include_groups (see above).
行 4:
  parent
  <parent_group> (string) is the name of the test group into
    which the tests from the subflow will be inserted.
    
    The test group you name as the parent must already exist in the MTP.
    
    This is an optional parameter. If it is not specified, the subflow in imported into the
    top level of the MTP.
行 5:
  position
  <position> (string) is the position within the parent
    where the imported tests are inserted.
    
    The following values are available:
    
    first: The tests are inserted at the beginning of the parent.
    
    last: The tests are inserted at the end of the parent.
    
    after:<test_name>: The test suite is
    inserted immediately after the test suite with the name
    <test_name> in the testflow group.
    
    before:<test_name>: The test suite is
    inserted immediately before the test suite with the name
    <test_name> in the testflow group.
    
    If this parameter is omitted, last is used.
行 6:
  tim_eqnset_index
  <tim_index> (string) specifies how the timing equation set
    indexes are imported from the STP to the MTP:
    
    'keep': The indexes are transferred unchanged.
    
    'keep+<number>':
    <number> is added to each index that is imported.
    
    This is an optional parameter. If it is not specified, 'keep' is
    used.
行 7:
  lev_eqnset_index
  <lev_index> (string) specifies how the level equation set
    indexes are imported from the STP to the MTP:
    
    'keep': The indexes are transferred unchanged.
    
    'keep+<number>':
    <number> is added to each index that is imported.
    
    This is an optional parameter. If it is not specified, 'keep' is
    used.
行 8:
  levels_mode
  <levels_mode> specifies the way in which level settings
    are merged into the MTP:
    
    'used' (default): Only level settings that are used by the merged
    subflow are copied from the STP to the MTP.
    
    'all': All level settings from the STP are copied to the MTP, even
    if none of the merged test groups is using them.
    
    This parameter is optional. If it is omitted, only the level settings used in the
    subflow are copied.
行 9:
  timing_mode
  <timing_mode> specifies the way in which timing settings
    are merged into the MTP:
    
    'used' (default): Only timing settings that are used by the merged
    subflow are copied from the STP to the MTP.
    
    'all': All timing settings from the STP are copied to the MTP, even
    if none of the merged test groups is using them.
    
    This parameter is optional. If it is omitted, only the timing settings used in the
    subflow are copied.
行 10:
  pattern_mode
  <pattern_mode> specifies the way in which timing settings
    are merged into the MTP:
    
    'used' (default): Only patterns that are used by the merged subflow
    are copied from the STP to the MTP.
    
    'all': All patterns from the STP are copied to the MTP, even if none
    of the merged test groups is using them.
    
    This parameter is optional. If it is omitted, only the patterns used in the subflow
    are copied.
行 11:
  keep_tim_eqnsets
  <tim_eqnsets> is a list of timing equation sets from the
    STP that are merged into the MTP even if they are not used by the merged test groups.
    
    The value is a list of equation set numbers separated by commas. For example: [1, 5, 9,
    13]
    
    This parameter is optional.
行 12:
  keep_lev_eqnsets
  <lev_eqnsets> is a list of level equation sets from the
    STP that are merged into the MTP even if they are not used by the merged test groups.
    
    The value is a list of equation set numbers separated by commas. For example: [7,8]
    
    This parameter is optional.
行 13:
  keep_wavetables
  <wavetables> is a list of wavetables from the STP that are
    merged into the MTP even if they are not used by the merged test groups.
    
    The value is a list of wavetable names, enclosed in quotes and separated by commas. For
    example: ['mytable', 'wavetable2']
    
    This parameter is optional.
行 14:
  keep_specifications
  <specifications> is a list of specifications from the STP
    that are merged into the MTP even if they are not used by the merged test groups.
    
    The value is a list of specification names, enclosed in quotes and separated by commas.
    For example: ['spec5', 'spec5b']
    
    This parameter is optional.
行 15:
  keep_pattern_files
  <pattern_files> is a list of level pattern files from the
    STP that are merged into the MTP even if they are not used by the merged test groups.
    
    The value is a list of pattern file paths, enclosed in quotes and separated by commas.
    Paths can be absolute or relative to the directory of the MTP. For example:
    ['/home/johndoe/tps/init_pattern.bin l', 'device/vectors/pat3.binl'']
    
    This parameter is optional.
行 16:
  copy_static_content
  <copy_items> (list of strings) specifies is a list of
    names of files or directories that are to be copied from the device directory of the merged
    STP to the device directory of the MTP.
    
    The list may contain only names (of files or directories), not paths. The named items
    must be located in the top level of the device directory. Each name is enclosed in quotes
    and separated by commas.
    
    These values are supported:
    
    A list of names of files or directories (but not paths). The named items must be
    located in the top level of the device directory. Each name is enclosed in quotes and
    separated by commas.
    For example: copy_static_content = ['my_notes.txt','Change
    log']
    
    If you include standard directories in this list (see below), STPM generates a warning
    and does not copy the contents.
    
    ['*all*']: Every file and directory in the device directory is
    copied, except the standard directories testflow,
    timing, levels,
    configuration, vectors, and
    testtable.
    
    [] (default): No additional files or directories are copied.
    
    This parameter is optional. If it is omitted, no additional content is copied (as if
    [] had been specified).
行 17:
  pre_proc
  <pre_proc> is a script that is executed before this
    command.
    
    The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `143913.htm`）.
    
    This is an optional parameter.
行 18:
  post_proc
  <post_proc> is a script that is executed after this
    command.
    
    The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `143913.htm`）.
    
    This is an optional parameter.

### Syntax（取自子主题 remove_subflow）

```
extract_subflow(
test_flow_file = '<file_path>',
[include_groups = [<include_group_list>], ]
[exclude_groups = [<exclude_group_list>], ]
[pre_proc = <pre_proc>, ]
[post_proc = <post_proc>]
)
```

### Parameters（取自子主题 remove_subflow）

The parameters in the order in which they are listed
above:

[表]
行 1:
  test_flow_file
  <file_path> (string) is the name and path of the testflow
    file for the STP. The tests that were imported from this STP will be removed from the
    MTP.
    
    It can be an absolute or a relative path. If it is a relative path, the base directory is
    the current working directory at the time STPM was called.
行 2:
  include_groups
  <include_group_list> (list of strings) is a list of
    testflow groups that STPM is to remove. If you use this parameter, only those groups
    specified in the list are removed from the MTP.
    
    The list must be enclosed in square brackets. Each testflow group in the list must be
    enclosed in quotes and separated by commas.
    
    For example: test_groups = ['tg3','fail_tg']
    
    This parameter is optional. It cannot be used when you also specify
    exclude_groups (see below).
行 3:
  exclude_groups
  <exclude_group_list> (list of strings) is a list of
    testflow groups that STPM is to leave in the MTP. If you use this parameter, all groups in
    the STP are deleted from the MTP, except those groups specified in the list.
    
    The list must be enclosed in square brackets. Each testflow group in the list must be
    enclosed in quotes and separated by commas.
    
    For example: test_groups = ['tg3','fail_tg']
    
    This parameter is optional. It cannot be used when you also specify
    include_groups (see above).
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

### Syntax（取自子主题 clear_duplicated）

```
clear_duplicated(
[proc_wavetables = <0_or_1>, ]
[proc_tim_eqnsets = <0_or_1>, ]
[proc_tim_sets = <0_or_1>, ]
[proc_tim_specsets = <0_or_1>, ]
[proc_lev_eqnsets = <0_or_1>, ]
[proc_lev_sets = <0_or_1>, ]
[proc_lev_specsets = <0_or_1>, ]
[proc_specifications = <0_or_1>, ]
[proc_merge_pins = <0_or_1>, ]
[skip_wavetables = [<wavetables>], ]
[skip_tim_eqnsets = [<tim_eqnsets>], ]
[skip_lev_eqnsets = [<lev_eqnsets>], ]
[skip_specifications = [<specs>], ]
[analyze_only = <analyze_flag>, ]
[analyzer_path = <path>, ]
[pre_proc = <pre_proc>, ]
[post_proc = <post_proc>]
)
```

### Parameters（取自子主题 clear_duplicated）

The parameters in the order in which they are listed
above:

[表]
行 1:
  proc_wavetables
  Whether duplicate wavetables are removed:
    
    0: They are not removed.
    
    1: They are removed.
    
    This parameter is optional, the default is 1.
行 2:
  proc_tim_eqnsets
  Whether duplicate timing equation sets are removed:
    
    0: They are not removed.
    
    1: They are removed.
    
    This parameter is optional, the default is 1.
行 3:
  proc_tim_sets
  Whether duplicate timing sets are removed:
    
    0: They are not removed.
    
    1: They are removed.
    
    This parameter is optional, the default is 1.
行 4:
  proc_tim_specsets
  Whether duplicate timing specifications are removed:
    
    0: They are not removed.
    
    1: They are removed.
    
    This parameter is optional, the default is 1.
行 5:
  proc_lev_eqnsets
  Whether duplicate level equation sets are removed:
    
    0: They are not removed.
    
    1: They are removed.
    
    This parameter is optional, the default is 1.
行 6:
  proc_lev_sets
  Whether duplicate level sets are removed:
    
    0: They are not removed.
    
    1: They are removed.
    
    This parameter is optional, the default is 1.
行 7:
  proc_lev_specsets
  Whether duplicate level spec sets are removed:
    
    0: They are not removed.
    
    1: They are removed.
    
    This parameter is optional, the default is 1.
行 8:
  proc_specifications
  Whether duplicate specifications are removed:
    
    0: They are not removed.
    
    1: They are removed.
    
    This parameter is optional, the default is 1.
行 9:
  proc_merge_pins
  Whether definitions for similar pins are merged in the wavetable, timing set, level
    set, and DPS pins definitions:
    
    0: They are not merged.
    
    1: They are merged.
    
    This parameter is optional, the default is 0.
行 10:
  skip_wavetables
  <wavetables> is a list of wavetables that are not removed
    from the MTP even if they are duplicates.
    
    The value is a list of wavetable names, enclosed in quotes and separated by commas. For
    example: ['wt1', 'wt2', 'wt3']
    
    This parameter is optional.
行 11:
  skip_tim_eqnsets
  <tim_eqnsets> is a list of timing equation sets that are
    not removed from the MTP even if they are duplicates.
    
    The value is a list of equation set numbers separated by commas. For example: [1, 5, 9,
    13]
    
    This parameter is optional.
行 12:
  skip_lev_eqnsets
  <lev_eqnsets> is a list of level equation sets that are
    not removed from the MTP even if they are duplicates.
    
    The value is a list of equation set numbers separated by commas. For example: [7,8]
    
    This parameter is optional.
行 13:
  skip_specifications
  <specifications> is a list of specifications that are not
    removed from the MTP even if they are duplicates.
    
    The value is a list of specification names, enclosed in quotes and separated by commas.
    For example: ['spec1', 'spec2', 'spec3']
    
    This parameter is optional.
行 14:
  analyze_only
  <analyze_flag> specifies whether duplicate primaries are
    actually removed:
    
    0: Any found duplicates are removed.
    
    1: No primaries are removed but STPM generates a report of found duplicates.
    
    This parameter is optional, the default is 0.
行 15:
  analyzer_path
  <path> is the name and location of the report file
    containing the result of the analysis.
    
    If analyze_only (see above) is 0, this parameter is ignored. If
    analyze_only is 1, this parameter is observed.
    
    This parameter is optional. If it is not specified, the default is <device
    directory>/reports/duplicated_report.csv.
行 16:
  pre_proc
  <pre_proc> is a script that is executed before this
    command.
    
    The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `143913.htm`）.
    
    This is an optional parameter.
行 17:
  post_proc
  <post_proc> is a script that is executed after this
    command.
    
    The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `143913.htm`）.
    
    This is an optional parameter.

### Syntax（取自子主题 clear_unused）

```
clear_unused(
[proc_timing = <0_or_1>, ]
[proc_levels = <0_or_1>, ]
[proc_patterns = <0_or_1>, ]
[proc_ports = <0_or_1>, ]
[proc_groups = <0_or_1>, ]
[proc_nonexistent_pins = <0_or_1>, ]
[skip_wavetables = [<wavetables>], ]
[skip_tim_eqnsets = [<tim_eqnsets>], ]
[skip_lev_eqnsets = [<lev_eqnsets>], ]
[skip_specifications = [<specifications>], ]
[skip_patterns = [<patterns>], ]
[analyze_only = <analyze_flag>, ]
[analyzer_path = <path>, ]
[pre_proc = <pre_proc>, ]
[post_proc =<post_proc>]
)
```

### Parameters（取自子主题 clear_unused）

The parameters in the order in which they are listed
above:

[表]
行 1:
  proc_timing
  Whether unused wavetables, timing equation sets, timing sets, and timing spec sets
    are deleted from the MTP:
    
    0: They are not removed.
    
    1: They are removed.
    
    This parameter is optional, the default is 1.
行 2:
  proc_levels
  Whether unused level equation sets, level sets, and level spec sets are deleted
    from the MTP:
    
    0: They are not removed.
    
    1: They are removed.
    
    This parameter is optional, the default is 1.
行 3:
  proc_patterns
  Whether unused pattern labels are removed:
    
    0: They are not removed.
    
    1: They are removed.
    
    This parameter is optional, the default is 1.
行 4:
  proc_ports
  Whether unused ports are removed:
    
    0: They are not removed.
    
    1: They are removed.
    
    This parameter is optional, the default is 1.
行 5:
  proc_groups
  Whether unused pin groups are removed:
    
    0: They are not removed.
    
    1: They are removed.
    
    This parameter is optional, the default is 1.
行 6:
  proc_nonexistent_pins
  Whether timing and level specifications for unused pins are removed:
    
    0: They are not removed.
    
    1: They are removed.
    
    This parameter is optional, the default is 0.
行 7:
  skip_wavetables
  <wavetables> is a list of wavetables that are not removed
    from the MTP even if they are unused.
    
    The value is a list of wavetable names, enclosed in quotes and separated by commas. For
    example: ['wt1', 'wt2', 'wt3']
    
    This parameter is optional.
行 8:
  skip_tim_eqnsets
  <tim_eqnsets> is a list of timing equation sets that are
    not removed from the MTP even if they are unused.
    
    The value is a list of equation set numbers separated by commas. For example: [1, 5, 9,
    13]
    
    This parameter is optional.
行 9:
  skip_lev_eqnsets
  <lev_eqnsets> is a list of level equation sets that are
    not removed from the MTP even if they are unused.
    
    The value is a list of equation set numbers separated by commas. For example: [7,8]
    
    This parameter is optional.
行 10:
  skip_specifications
  <specifications> is a list of specifications that are not
    removed from the MTP even if they are unused.
    
    The value is a list of specification names, enclosed in quotes and separated by commas.
    For example: ['spec1', 'spec2', 'spec3']
    
    This parameter is optional.
行 11:
  skip_patterns
  <patterns> is a list of pattern files that are not removed
    from the MTP even if they are unused.
    
    The value is a list of paths of pattern files, enclosed in quotes and separated by
    commas. The paths can be either absolute or relative to current device directory (in which
    case they must include the name of the directory).
    
    For example (assuming a device directory named mtp):
    ['/usr/engineer/pat.binl', 'mtp/vectors/DAC/pat.binl']
    
    This parameter is optional.
行 12:
  analyze_only
  <analyze_flag> specifies whether duplicate primaries are
    actually removed:
    
    0: Any found duplicates are removed.
    
    1: No primaries are removed but STPM generates a report of found duplicates.
    
    This parameter is optional, the default is 0.
行 13:
  analyzer_path
  <path> is the name and location of the report file
    containing the result of the analysis.
    
    If analyze_only (see above) is 0, this parameter is ignored. If
    analyze_only is 1, this parameter is observed.
    
    This parameter is optional. If it is not specified, the default is <device
    directory>/reports/unused_report.csv.
行 14:
  pre_proc
  <pre_proc> is a script that is executed before this
    command.
    
    The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `143913.htm`）.
    
    This is an optional parameter.
行 15:
  post_proc
  <post_proc> is a script that is executed after this
    command.
    
    The syntax of the parameter value is described in `Preprocessing and postprocessing scripts`（raw: `143913.htm`）.
    
    This is an optional parameter.

### Syntax（取自子主题 STPM merge rules file syntax）

The merge rules file contains a range of flags, which can be set to

allow
,
reject
, or
ignore
. Not all
options are available for all flags.

The three settings usually have the same general
effect:

allow
: STPM performs the merger and automatically resolves any conflicts
that may occur. This automatic resolution may have side effects, such as when pin numbers
change.

ignore
: STPM performs the merger but does not resolve any conflicts that
may occur. If the rule was triggered, you will usually need to manually resolve the issues in
the target file (processed MTP).

reject
: STPM aborts the merger with an error without changing the MTP.
You will have to manually resolve the issue in the source files (STP and/or original MTP).

This table lists the available flags and their supported settings. For details on the
effect of each flag, see the pages describing the individual flags.

[表]
列: Flag | Available settings | Default
行 1:
  Allow
  Ignore
  Reject
行 2:
  Pin, port, and site rules
  
  
  
  
行 3:
  `new_digital_pin`（raw: `131165.htm`）
  +
  
  +
  allow
行 4:
  `overwrite_digital_pin_no`（raw: `131174.htm`）
  +
  +
  +
  ignore
行 5:
  `merge_digital_pin_dir`（raw: `131180.htm`）
  +
  
  +
  allow
行 6:
  `new_dps_pin`（raw: `131183.htm`）
  +
  
  +
  allow
行 7:
  `overwrite_dps_pin_polarity`（raw: `131185.htm`）
  +
  +
  +
  ignore
行 8:
  `new_pin_group`（raw: `131187.htm`）
  +
  +
  +
  allow
行 9:
  `overwrite_pin_group`（raw: `131189.htm`）
  +
  +
  +
  ignore
行 10:
  `merge_unused_pin_group`（raw: `140672.htm`）
  +
  +
  
  allow
行 11:
  `new_port`（raw: `131201.htm`）
  +
  
  +
  allow
行 12:
  `overwrite_port`（raw: `131218.htm`）
  +
  +
  +
  reject
行 13:
  `new_site`（raw: `131227.htm`）
  +
  
  +
  allow
行 14:
  `overwrite_channel`（raw: `131229.htm`）
  +
  +
  +
  ignore
行 15:
  Timing and levels rules
  
  
  
  
行 16:
  `new_timing_equation_set`（raw: `131679.htm`）
  +
  
  +
  allow
行 17:
  `new_waveform`（raw: `131680.htm`）
  +
  
  +
  allow
行 18:
  `modify_waveform_index`（raw: `131681.htm`）
  +
  
  +
  allow
行 19:
  `overwrite_statemap`（raw: `131684.htm`）
  +
  +
  +
  ignore
行 20:
  `new_level_resource`（raw: `131688.htm`）
  +
  +
  +
  allow
行 21:
  `overwrite_level_resource`（raw: `131689.htm`）
  +
  +
  +
  ignore
行 22:
  `new_level_equation_set`（raw: `131690.htm`）
  +
  
  +
  allow
行 23:
  `new_level_set`（raw: `131691.htm`）
  +
  
  +
  allow
行 24:
  `new_ac_specset`（raw: `131692.htm`）
  +
  
  +
  allow
行 25:
  `new_dc_specset`（raw: `131693.htm`）
  +
  
  +
  allow
行 26:
  `overwrite_ac_spec_typ`（raw: `131695.htm`）
  +
  +
  +
  reject
行 27:
  `overwrite_ac_spec_minmax`（raw: `131697.htm`）
  +
  +
  +
  reject
行 28:
  `overwrite_dc_spec_typ`（raw: `131698.htm`）
  +
  +
  +
  reject
行 29:
  `overwrite_dc_spec_minmax`（raw: `131699.htm`）
  +
  +
  +
  reject
行 30:
  Pattern rules
  
  
  
  
行 31:
  `overwrite_label_wvt`（raw: `135571.htm`）
  +
  +
  
  allow
行 32:
  Testflow rules
  
  
  
  
行 33:
  `overwrite_flow_var_value`（raw: `140686.htm`）
  +
  +
  +
  reject

### Example（取自子主题 STPM merge rules file syntax）

This example merge rules file sets all available options. Note that this is not
necessary; if an option is missing, the default setting is used for
it.

```
new_digital_pin = 'reject'
overwrite_digital_pin_no = 'reject'
merge_digital_pin_dir = 'reject'
new_dps_pin = 'reject'
overwrite_dps_pin_polarity = 'reject'
new_pin_group = 'allow'
overwrite_pin_group = 'ignore'
merge_unused_pin_group = 'ignore'
new_port = 'allow'
overwrite_port = 'reject'
new_site = 'reject'
overwrite_channel = 'ignore'

new_timing_equation_set = 'allow'
new_waveform = 'reject'
modify_waveform_index = 'reject'
overwrite_statemap = 'reject'
new_level_resource = 'reject'
overwrite_level_resource = 'reject'
new_level_equation_set = 'allow'
new_level_set = 'allow'
new_ac_specset = 'allow'
new_dc_specset = 'allow'
overwrite_ac_spec_minmax = 'reject'
overwrite_dc_spec_minmax = 'reject'
overwrite_ac_spec_typ = 'reject'
overwrite_dc_spec_typ = 'reject'
```
```
overwrite_label_wvt = 'reject'

overwrite_flow_var_value = 'reject'
```

### Syntax（取自子主题 new_digital_pin）

The
new_digital_pin
 flag can be set to
allow

(default) or
reject
:

allow

STPM adds the pin to the MTP and notes it in the
log:

```
Warning: New digital pin 'sig1' was added to MTP.
```

reject

STPM does not add the pin or the test to the MTP and the merge
process fails. The error is noted in the
log:

```
Error: Digital pin 'sig1' is not defined in MTP.
```

### Example（取自子主题 new_digital_pin）

This setting makes sure that no digital pins are added to the MTP and merge processes
fail that would require pins to be
added:

```
new_digital_pin = 'reject'
```

### Syntax（取自子主题 overwrite_digital_pin_no）

The
overwrite_digital_pin_no
 flag can be set to

allow
,
ignore
 (default), or

reject
:

allow

STPM changes the pin number in the MTP and notes it in the
log:

```
Warning: Pin number conflict detected: digital pin 'sig1', '1'(STP)->'2'(MTP)
(overwriting MTP pin number by '1')
```

ignore

STPM does not change the pin number in the MTP but still adds
the test from the STP (source test program) and notes it in the
log:

```
Warning: Pin number conflict detected: digital pin 'sig1', '1'(STP)->'2'(MTP)
(keeping MTP pin number '2')
```

reject

STPM does not add the test to the MTP and the merge process
fails. The error is noted in the
log:

```
Error: Pin number conflict detected: digital pin 'sig1', '1'(STP)->'2'(MTP)
```

### Example（取自子主题 overwrite_digital_pin_no）

This setting makes sure that no digital pins are renumbered in the MTP and merge
processes fail that would require pins to be
renumbered:

```
overwrite_digital_pin_no = 'reject'
```

### Syntax（取自子主题 merge_digital_pin_dir）

The
merge_digital_pin_dir
 flag can be set to

allow
 (default) or
reject
:

allow

STPM changes all pins in the MTP with incompatible directions to
IO pins and notes it in the
log:

```
Warning: Pin type conflict detected: digital pin 'clk',
'IO'->'I' (merging pin types, IO + I -> IO)
Warning: Pin type conflict detected: digital pin 'sigA',
'IO'->'I' (merging pin types, IO + I -> IO)
```

reject

STPM does not add the test to the MTP and the merge process
fails. The error is noted in the
log:

```
Error: Pin type conflict detected: digital pin 'clk', 'O'->'I'
Error: Pin type conflict detected: digital pin 'sigA', 'IO'->'O'
```

### Example（取自子主题 merge_digital_pin_dir）

This setting makes sure that all digital pins in the MTP keep their directions and
merge processes fail that would require pins to change their
direction:

```
merge_digital_pin_dir = 'reject'
```

### Syntax（取自子主题 new_dps_pin）

The
new_dps_pin
 flag can be set to
allow

(default) or
reject
:

allow

STPM adds the pin to the MTP and notes it in the
log:

```
Warning: New power supply pin 'vcc1' was added to MTP.
```

reject

STPM does not add the pin or the test to the MTP and the merge
process fails. The error is noted in the
log:

```
Error: Power supply pin 'vcc1' is not defined in MTP
```

### Example（取自子主题 new_dps_pin）

This setting makes sure that no DPS pins are added to the MTP and merge processes fail
that would require pins to be added:

```
new_dps_pin = 'reject'
```

### Syntax（取自子主题 overwrite_dps_pin_polarity）

The
overwrite_dps_pin_polarity
 flag can be set to

allow
,
ignore
 (default), or

reject
:

allow

STPM changes the pin polarity in the MTP and notes it in the
log:

```
Warning: Polarity conflict detected: power supply pin 'vcc', 'NEG'(STP)->'POS'(MTP)
(overwriting MTP pin polarity by 'NEG')
```

ignore

STPM does not change the pin polarity in the MTP but still adds
the test from the STP (source test program) and notes it in the
log:

```
Warning: Polarity conflict detected: power supply pin 'vcc', 'NEG'(STP)->'POS'(MTP)
(keeping MTP pin polarity 'POS')
```

reject

STPM does not add the test to the MTP and the merge process
fails. The error is noted in the
log:

```
Error: Polarity conflict detected: power supply pin 'vcc', 'NEG'(STP)->'POS'(MTP)
```

### Example（取自子主题 overwrite_dps_pin_polarity）

This setting makes sure that no DPS pin polarities are changed in the MTP and merge
processes fail that would require pin polarities to be
changed:

```
overwrite_dps_pin_polarity = 'reject'
```

### Syntax（取自子主题 new_pin_group）

The
new_pin_group
 flag can be set to
allow

(default),
ignore
, or
reject
:

allow

STPM adds the pin group to the MTP and notes it in the
log:

```
Warning: New pin group 'MY_GROUP' was added to MTP
```

ignore

STPM adds the test to the MTP but does not create the pin group
in the MTP. Instead, it uses the individual member pins of the ignored group in the MTP.

This is noted in the
log:

```
Warning: Pin group 'MY_GROUP' is not defined in MTP (ignored)
```

reject

STPM does not add the pin group or the test to the MTP and the
merge process fails. The error is noted in the
log:

```
Error: Pin group 'MY_GROUP' is not defined in MTP
```

### Example（取自子主题 new_pin_group）

This setting causes STPM to always automatically create new pin groups when they are
needed to merge tests:

```
new_pin_group = 'allow'
```

### Syntax（取自子主题 overwrite_pin_group）

The
overwrite_pin_group
 flag can be set to
allow
,

ignore
 (default), or
reject
:

allow

STPM changes the pin group definition in the MTP. Any pins that
were part of the group before its definition was overwritten and now are no longer part of it
are added individually in all locations where the group is used.

This is noted in the
log:

```
Warning: Pin group conflict detected: group 'all_inputs',
'I:clk,data,sigA,sigB'(STP)->'I:clk,data,sigA'(MTP)
(overwriting MTP group by I:clk,data,sigA,sigB)
```

ignore

STPM does not change the pin group definition in the MTP but
still adds the test from the STP (source test program) and notes it in the
log:

```
Warning: Pin group conflict detected: group 'all_inputs',
'I:clk,data,sigA,sigB'(STP)->'I:clk,data,sigA'(MTP)
(keeping MTP group definition I:clk,data,sigA)
```

reject

STPM does not add the test to the MTP and the merge process
fails. The error is noted in the
log:

```
Error: Pin group conflict detected: group 'all_inputs',
'I:clk,data,sigA,sigB'(STP)->'I:clk,data,sigA'(MTP)
```

### Example（取自子主题 overwrite_pin_group）

This setting makes sure that no pin group definitions in the MTP are changed but that
merge processes requiring such changes still succeed. (This usually requires you to fix the
resulting MTP before it can be
used.)

```
overwrite_pin_group = 'ignore'
```

### Syntax（取自子主题 merge_unused_pin_group）

The
merge_unused_pin_group
 flag can be set to

allow
 (default) or
ignore
:

allow

STPM imports the pin group definition into the MTP.

ignore

STPM does not import the pin group definition into the MTP.

In both cases, the test is imported into the MTP. Note that this rule affects only unused
pin groups; it has no effect on used pin groups.

### Example（取自子主题 merge_unused_pin_group）

This setting makes sure that only pin group definitions are imported into the MTP that
are actually used.

```
merge_unused_pin_group = 'ignore'
```

### Syntax（取自子主题 new_port）

The
new_port
 flag can be set to
allow
 (default)
or
reject
:

allow

STPM adds the port definition to the MTP and notes it in the
log:

```
Warning: New port 'port1' was added to MTP
```

reject

STPM does not add the port definition or the test to the MTP and
the merge process fails. The error is noted in the
log:

```
Error: Port 'port1' is not defined in MTP
```

### Example（取自子主题 new_port）

This setting causes STPM to add any new port definitions to the MTP when they are
needed to merge a test:

```
new_port = 'allow'
```

### Syntax（取自子主题 overwrite_port）

The
overwrite_port
 flag can be set to
allow
,

ignore
, or
reject
 (default):

allow

STPM changes the port definition in the MTP and notes it in the
log:

```
Warning: Port conflict detected: port 'port1', 'sigA,clk'(STP)->'sigA'(MTP) (overwriting MTP port by sigA,clk)
```

ignore

STPM does not change the port definition in the MTP but still
adds the test from the STP (source test program) and notes it in the
log:

```
Warning: Port conflict detected: port 'port1', 'sigA,clk'(STP)->'sigA'(MTP) (keeping MTP port definition sigA)
```

reject

STPM does not add the port definition or the test to the MTP and
the merge process fails. The error is noted in the
log:

```
Error: Port conflict detected: port 'port1', 'sigA,clk'(STP)->'sigA'(MTP)
```

### Example（取自子主题 overwrite_port）

This setting makes sure that no port definitions are changed in the MTP and merge
processes fail that would require ports to be
redefined:

```
overwrite_port = 'reject'
```

### Syntax（取自子主题 new_site）

The
new_site
 flag can be set to
allow
 (default)
or
reject
:

allow

STPM adds the site definition to the MTP and notes it in the
log:

```
Warning: Sites 2..5 are not defined in MTP (added)
```

reject

STPM does not add the site definition or the test to the MTP and
the merge process fails. The error is noted in the
log:

```
Error: Sites 2..5 are not defined in MTP
```

### Example（取自子主题 new_site）

This setting makes sure that no site definitions are added to the MTP and merge
processes fail that would require site definitions to be
added:

```
new_site = 'reject'
```

### Syntax（取自子主题 overwrite_channel）

The
overwrite_channel
 flag can be set to
allow
,

ignore
 (default), or
reject
:

allow

STPM changes the channel definition in the MTP and notes it in
the
log:

```
Warning: Pin channel conflict detected: pin 'sigB', site 1, '10406'(STP)->'10405'(MTP)
(overwriting MTP channel by '10406')
```

ignore

STPM does not change the channel definition in the MTP but still
adds the test from the STP (source test program) and notes it in the
log:

```
Warning: Pin channel conflict detected: pin 'sigB', site 1, '10406'(STP)->'10405'(MTP)
(keeping MTP channel '10405')
```

reject

STPM does not add the channel definition or the test to the MTP
and the merge process fails. The error is noted in the
log:

```
Error: Pin channel conflict detected: pin 'sigB', site 1, '10406'(STP)->'10405'(MTP)
```

### Example（取自子主题 overwrite_channel）

This setting makes sure that no channel definitions in the MTP are changed but that
merge processes requiring such changes still succeed. (This usually requires you to fix the
resulting MTP before it can be
used.)

```
overwrite_channel = 'ignore'
```

### Syntax（取自子主题 new_timing_equation_set）

The
new_timing_equation_set
 flag can be set to

allow
 (default) or
reject
:

allow

STPM adds a new wavetable, equation set, and spec set to the MTP
and notes it in the log. Note that it first adds an error message to the log caused by the
inability to reuse existing primaries, but this error is non-fatal and does not prevent the
test from being
added:

```
Trying to reuse the following tests primaries:
[Stil_1]
Error: Equation 'eq_shared = 2.51' differs from master equation in MTP EQNSET 1
Reuse failed - see errors above.
Adding WAVETBL 'wt1'
Adding EQNSET 2
Adding SPECSET 1
```

reject

STPM does not add the primaries or the test to the MTP and the
merge process fails. The error is noted in the
log:

```
Trying to reuse the following tests primaries:
[Stil_1]
Error: Equation 'eq_shared = 2.51' differs from master equation in MTP EQNSET 1
Reuse failed - see errors above.
Adding WAVETBL 'wt1'
Adding EQNSET 2
Error: Failed: adding new equation set was rejected by merge rule 'new_timing_equation_set'
```

### Example（取自子主题 new_timing_equation_set）

This setting causes STPM to add any new timing equations to the MTP when they are
needed to merge a
test:

```
new_timing_equation_set = 'allow'
```

### Syntax（取自子主题 new_waveform）

The
new_waveform
 flag can be set to
allow

(default) or
reject
:

allow

STPM adds a new waveform to the MTP and notes it in the log. Note
that it first adds an error message to the log caused by the inability to reuse existing
waveforms, but this error is non-fatal and does not prevent the test from being
added:

```
Trying to reuse the following tests primaries:
[Stil_1]
Error: Waveform [1 "0.0:1 25.0:F1N 75.0:F0N" M]
is not covered by any MTP waveform in pin 'clk', wavetable 'wt1'
Reuse failed - see errors above.
Adding WAVETBL 'wt1'
Adding EQNSET 2
Adding SPECSET 1
```

reject

STPM does not add the waveform to the MTP. Instead, it tries to
add a new timing equation set. If that succeeds, the test is added to the MTP. If adding the
equation set fails, the merge process fails and the MTP is not changed.

The error is noted in the
log:

```
Trying to reuse the following tests primaries:
[Stil_1]
Error: Waveform [1 "0.0:1 25.0:F1N 75.0:F0N" M]
is not covered by any MTP waveform in pin 'clk', wavetable 'wt1'
Reuse failed - see errors above.
```

### Example（取自子主题 new_waveform）

This setting makes sure that no waveforms are added to the MTP and merge processes
fail that would require waveforms to be
added:

```
new_waveform = 'reject'
```

### Syntax（取自子主题 modify_waveform_index）

The
modify_waveform_index
 flag can be set to

allow
 (default) or
reject
:

allow

STPM changes the waveform index in the added test and notes it in
the log. It also modifies the patterns using these waveforms, which may greatly increase the
processing time for adding large tests (patterns with hundreds of megabytes).

Note that it first adds an error message to the log caused by the inability to reuse an
existing waveform index, but this error is non-fatal and does not prevent the test from being
added:

```
Trying to reuse the following tests primaries:
[Stil_11]
Warning: Waveform [0 "0.0:1 25.0:F1N 75.0:F0N" P]
is not covered by any MTP waveform in pin 'clk', wavetable 'wt1'
Error: Waveform [0 "0.0:1 25.0:F1N 75.0:F0N" P]
index was changed (0->1) in pin 'clk', wavetable 'wt1'
```

reject

STPM does not change the waveform index. Instead, it tries to
add a new timing equation set. If that succeeds, the test is added to the MTP. If adding the
equation set fails, the merge process fails and the MTP is not changed.

```
The error is noted in the log:Trying to reuse the following tests primaries:
[Stil_1]
Warning: Waveform [0 "0.0:1 25.0:F1N 75.0:F0N" P]
is not covered by any MTP waveform in pin 'clk', wavetable 'wt1'
Error: Waveform [0 "0.0:1 25.0:F1N 75.0:F0N" P]
index was changed (0->1) in pin 'clk', wavetable 'wt1'
Reuse failed - see errors above.
```

### Example（取自子主题 modify_waveform_index）

This setting makes sure that no waveforms in the MTP are reused with a different
index, and merge processes fail that would require waveforms to be reused with a different
index:

```
modify_waveform_index = 'reject'
```

### Syntax（取自子主题 overwrite_statemap）

The
overwrite_statemap
 flag can be set to
allow
,

ignore
 (default), or
reject
:

allow

STPM overwrites the state map in the MTP and notes it in the
log:

```
Warning: Statemap info of waveform [2 "{ 80.0:L }" L] differs from MTP
waveform statemap in pin 'data', wavetable 'wt1':
[H x1 wt1] != [L x1 wt1] (overwriting master statemap by 'H x1 wt1')
```

ignore

STPM does not change the state map in the MTP but still adds the
test from the STP (source test program) and notes it in the
log:

```
Warning: Statemap info of waveform [2 "{ 80.0:L }" L] differs from MTP
waveform statemap in pin 'data', wavetable 'wt1':
[H x1 wt1] != [L x1 wt1] (keeping master statemap 'L x1 wt1')
```

reject

STPM does not change the state map. Instead, it tries to add a
new timing equation set. If that succeeds, the test is added to the MTP. If adding the
equation set fails, the merge process fails and the MTP is not changed.

The error is noted in the
log:

```
Error: Statemap info of waveform [2 "{ 80.0:L }" L] differs from MTP
waveform statemap in pin 'data', wavetable 'wt1':
[H x1 wt1] != [L x1 wt1]
```

### Example（取自子主题 overwrite_statemap）

This setting makes sure that the state map of the MTP is not overwritten and merge
processes fail that would require it to be
overwritten:

```
overwrite_statemap = 'reject'
```

### Syntax（取自子主题 new_level_resource）

The
new_level_resource
 flag can be set to
allow

(default) or
reject
:

allow

STPM adds the level resource to the MTP and notes it in the
log:

```
Warning: Resource 'ioh' is not defined for master pin 'out' in
levelset 1 (set to the new value: '5.0').
```

reject

STPM does not add the level resource or the test to the MTP and
the merge process fails. The error is noted in the
log:

```
Error: Resource 'ioh' is not defined for master pin 'out' in levelset 1
```

### Example（取自子主题 new_level_resource）

This setting makes sure that no level resources are added to the MTP and merge
processes fail that would require level resources to be
added:

```
new_level_resource = 'reject'
```

### Syntax（取自子主题 overwrite_level_resource）

The
overwrite_level_resource
 flag can be set to

allow
,
ignore
 (default), or

reject
:

allow

STPM overwrites the level resource in the MTP and notes it in the
log:

```
Warning: Resource 'vih' conflict detected for master pin 'clk'
in levelset 1 (vil != vih) (keeping master resource value 'vih')
```

ignore

STPM does not change the level resource in the MTP but still
adds the test from the STP (source test program) and notes it in the
log:

```
Warning: Resource 'vih' conflict detected for master pin 'clk'
in levelset 1 (vil != vih) (overwriting master resource value by 'vil')
```

reject

STPM does not change the level resource. Instead, it tries to
add a new level equation set. If that succeeds, the test is added to the MTP. If adding the
equation set fails, the merge process fails and the MTP is not changed.

The error is noted in the
log:

```
Error: Resource 'vih' conflict detected for master pin 'clk' in levelset 1 (vil != vih)
```

### Example（取自子主题 overwrite_level_resource）

This setting makes sure that the level resources in the MTP are not overwritten and
merge processes fail that would require level resources to be
overwritten:

```
overwrite_level_resource = 'reject'
```

### Syntax（取自子主题 new_level_equation_set）

The
new_level_equation_set
 flag can be set to

allow
 (default) or
reject
:

allow

STPM adds the level equation set to the MTP and notes it in the
log. Note that it first adds an error message to the log, but this error is non-fatal and does
not prevent the test from being
added:

```
Error: Resource 'vih' conflict detected for master pin 'clk' in
levelset 1 (vil != vih)
Warning: Resource 'ioh' is not defined for master pin 'out' in
levelset 1 (set to the new value: '5.0' ).
Adding new levels equation set [EQNSET 3 'DCL2']
Adding new levels specset [SPECSET 1 'Cat1_Sel1']
```

reject

STPM does not add the level equation set or the test to the MTP
and the merge process fails. The error is noted in the
log:

```
Error: Resource 'vih' conflict detected for master pin 'clk' in
levelset 1 (vil != vih)
Warning: Resource 'ioh' is not defined for master pin 'out' in
levelset 1 (set to the new value: '5.0' ).
```

### Example（取自子主题 new_level_equation_set）

This setting causes STPM to add any new level equation sets to the MTP when they are
needed to merge a test:

```
new_level_equation_set = 'allow'
```

### Syntax（取自子主题 new_level_set）

The
new_level_set
 flag can be set to
allow

(default) or
reject
:

allow

STPM adds the level set to the MTP and notes it in the log. Note
that it first adds an error message to the log, but this error is non-fatal and does not
prevent the test from being
added:

```
Error: Resource 'ioh' is not defined for master pin 'out' in levelset 1
Warning: Adding new levelset [LEVELSET 1 'DCL2'] due to the conflict(s) above
```

reject

STPM does not add the level set to the MTP. Instead, it tries to
add a new level equation set. If that succeeds, the test is added to the MTP. If adding the
equation set fails, the merge process fails and the MTP is not changed.

The error is noted in the
log:

```
Error: Resource 'vih' conflict detected for master pin 'clk' in
levelset 1 (vil != vih)
```

### Example（取自子主题 new_level_set）

This setting causes STPM to add any new level sets to the MTP when they are needed to
merge a test:

```
new_level_set = 'allow'
```

### Syntax（取自子主题 new_ac_specset）

The
new_ac_specset
 flag can be set to
allow

(default) or
reject
:

allow

STPM adds the AC spec set to the MTP and notes it in the
log:

```
Warning: Spec 'my_values.max' value differs from master spec value
in specset 1 (61 != 6)
Warning: New specset required due to the conflict(s) above.
Adding SPECSET 12
```

reject

STPM does not add the spec set to the MTP. Instead, it tries to
add new level and timing equation sets. If that succeeds, the test is added to the MTP. If
adding the equation sets fails, the merge process fails and the MTP is not changed.

The error is noted in the
log:

```
Error: Spec 'my_values.max' value differs from master spec value
in specset 1 (61 != 6)
```

### Example（取自子主题 new_ac_specset）

This setting causes STPM to add any new AC spec sets to the MTP when they are needed
to merge a test:

```
new_ac_specset = 'allow'
```

### Syntax（取自子主题 new_dc_specset）

The
new_dc_specset
 flag can be set to
allow

(default) or
reject
:

allow

STPM adds the DC spec set to the MTP and notes it in the
log:

```
Warning: Spec 'vih.max' value differs from master spec value
in specset 1 (4.31 != 4.3)
Warning: New specset required due to the conflict(s) above.
Adding SPECSET 12
```

reject

STPM does not add the spec set to the MTP. Instead, it tries to
add new level and timing equation sets. If that succeeds, the test is added to the MTP. If
adding the equation sets fails, the merge process fails and the MTP is not changed.

The error is noted in the
log:

```
Error: Spec 'vih.max' value differs from master spec value
in specset 1 (4.31 != 4.3)
```

### Example（取自子主题 new_dc_specset）

This setting causes STPM to add any new DC spec sets to the MTP when they are needed
to merge a test:

```
new_dc_specset = 'allow'
```

### Syntax（取自子主题 overwrite_ac_spec_typ）

The
overwrite_ac_spec_typ
 flag can be set to

allow
,
ignore
, or
reject

(default):

allow

STPM overwrites the AC spec value in the MTP and notes it in the
log:

```
Warning: Spec 'my_values.typ' value differs from
master spec value in specset 1 (5.1 != 5)
(overwriting master spec value by '5.1')
```

ignore

STPM does not change the AC spec value in the MTP but still adds
the test from the STP (source test program) and notes it in the
log:

```
Warning: Spec 'my_values.typ' value differs from
master spec value in specset 1 (5.1 != 5)
(keeping master spec value '5')
```

reject

STPM does not change the AC spec value. Instead, it tries to add
new level and timing equation sets. If that succeeds, the test is added to the MTP. If adding
the equation sets fails, the merge process fails and the MTP is not changed.

The error is noted in the
log:

```
Error: Spec 'my_values.typ' value differs from master spec value in specset 1 (5.1 != 5)
```

### Example（取自子主题 overwrite_ac_spec_typ）

This setting makes sure that the typical AC spec values in the MTP are not overwritten
and merge processes fail that would require these values to be
overwritten:

```
overwrite_ac_spec_typ = 'reject'
```

### Syntax（取自子主题 overwrite_ac_spec_minmax）

The
overwrite_ac_spec_minmax
 flag can be set to

allow
,
ignore
, or
reject

(default):

allow

STPM overwrites the AC spec values in the MTP and notes it in the
log:

```
Warning: Spec 'my_values.min' value differs from master spec value
in specset 1 (42 != 4) (overwriting master spec value by '42')
Warning: Spec 'my_values.max' value differs from master spec value
in specset 1 (61 != 6) (overwriting master spec value by '61')
```

ignore

STPM does not change the AC spec values in the MTP but still
adds the test from the STP (source test program) and notes it in the
log:

```
Warning: Spec 'my_values.min' value differs from master spec value
in specset 1 (42 != 4) (keeping master spec value '4')
Warning: Spec 'my_values.max' value differs from master spec value
in specset 1 (61 != 6) (keeping master spec value '6')
```

reject

STPM does not change the AC spec value. Instead, it tries to add
new level and timing equation sets. If that succeeds, the test is added to the MTP. If adding
the equation sets fails, the merge process fails and the MTP is not changed.

The error is noted in the
log:

```
Error: Spec 'my_values.min' value differs from master spec value
in specset 1 (42 != 4) (keeping master spec value '4')
Error: Spec 'my_values.max' value differs from master spec value
in specset 1 (61 != 6) (keeping master spec value '6')
```

### Example（取自子主题 overwrite_ac_spec_minmax）

This setting makes sure that the minimum and maximum AC spec values in the MTP are not
overwritten and merge processes fail that would require these values to be
overwritten:

```
overwrite_ac_spec_minmax = 'reject'
```

### Syntax（取自子主题 overwrite_dc_spec_typ）

The
overwrite_dc_spec_typ
 flag can be set to

allow
,
ignore
, or
reject

(default):

allow

STPM overwrites the DC spec value in the MTP and notes it in the
log:

```
Warning: Spec 'vih.typ' value differs from master spec value
in specset 1 (4.1 != 4) (overwriting master spec value by '4.1')
```

ignore

STPM does not change the DC spec value in the MTP but still adds
the test from the STP (source test program) and notes it in the
log:

```
Warning: Spec 'vih.typ' value differs from master spec value
in specset 1 (4.1 != 4) (keeping master spec value '4')
```

reject

STPM does not change the DC spec value. Instead, it tries to add
new level and timing equation sets. If that succeeds, the test is added to the MTP. If adding
the equation sets fails, the merge process fails and the MTP is not changed.

The error is noted in the
log:

```
Error: Spec 'vih.typ' value differs
from master spec value in specset 1 (4.1 != 4)
```

### Example（取自子主题 overwrite_dc_spec_typ）

This setting makes sure that the typical DC spec values in the MTP are not overwritten
and merge processes fail that would require these values to be
overwritten:

```
overwrite_dc_spec_typ = 'reject'
```

### Syntax（取自子主题 overwrite_dc_spec_minmax）

The
overwrite_dc_spec_minmax
 flag can be set to

allow
,
ignore
, or
reject

(default):

allow

STPM overwrites the DC spec values in the MTP and notes it in the
log:

```
Warning: Spec 'vih.min' value differs from master spec value
in specset 1 (3.51 != 3.5) (overwriting master spec value by '3.51')
Warning: Spec 'vih.max' value differs from master spec value
in specset 1 (4.31 != 4.3) (overwriting master spec value by '4.31')
```

ignore

STPM does not change the DC spec values in the MTP but still
adds the test from the STP (source test program) and notes it in the
log:

```
Warning: Spec 'vih.min' value differs from master spec value
3 in specset 1 (3.51 != 3.5) (keeping master spec value '3.5')
4 Warning: Spec 'vih.max' value differs from master spec value
5 in specset 1 (4.31 != 4.3) (keeping master spec value '4.3')
```

reject

STPM does not change the DC spec values or add the test to the
MTP, and the merge process fails. The error is noted in the
log:

```
Error: Spec 'vih.min' value differs from master spec value
in specset 1 (3.51 != 3.5)
```

### Example（取自子主题 overwrite_dc_spec_minmax）

This setting makes sure that the minimum and maximum DC spec values in the MTP are not
overwritten and merge processes fail that would require these values to be
overwritten:

```
overwrite_dc_spec_minmax = 'reject'
```

### Syntax（取自子主题 overwrite_label_wvt）

The
overwrite_label_wvt
 flag can be set to
allow

(default) or
ignore
:

allow

STPM replaces the wavetable name in the pattern it imports from
the STP with the name of a suitable wavetable that already present in the MTP (if such a
wavetable exists). A wavetable is considered suitable if the pattern does not need to be
modified (except for the replacement of the wavetable name attribute).

ignore

STPM always leaves the name of the wavetable in the imported
pattern as is and imports the wavetable.

There is no warning irrespective of the setting of this option. This setting has no
effect when additional modifications to the pattern are needed during the import.

### Example（取自子主题 overwrite_label_wvt）

This setting makes sure that the wavetable information in imported patterns is not
modified:

```
overwrite_statemap = 'ignore'
```

### Syntax（取自子主题 overwrite_flow_var_value）

The
overwrite_flow_var_value
 flag can be set to

allow
,
ignore
, or
reject

(default):

allow

STPM overwrites the value of the user testflow variable in the
MTP with the value from the STP and generates a warning.

ignore

STPM keeps the value of the user testflow variable in the MTP
(ignoring the value from the STP) and generates a warning.

reject

STPM stops merging the subflow and generates an error.

### Example（取自子主题 overwrite_flow_var_value）

This setting lets changed values from the STP overwrite the values in the
MTP:

```
overwrite_flow_var_value = allow
```

### Syntax（取自子主题 Test suite table of a TPT）

Each row in the test suite table describes one test suite. The table contains these
columns:

TestSuite Name
: The name for the test suite in the test program.

Test Group
: The test group in the test program to which the test
suite belongs.

If this column is left empty, the test suite is placed in the top level of the
testflow.

Timing
: The timing to be used by this test, specified as the indexes
of the equation set, spec set, and timing set to use (for example, 1|2|1).

This column can be
left empty, in which case any generated test program will not include timing information for
this test suite.

Levels
: The levels to be used by this test, specified as the indexes
of the equation set, spec set, and level set to use (for example, |speci|1,1,3).

This column
can be left empty, in which case any generated test program will not include level information
for this test suite.

Pattern
: The name of the pattern to be used by this test.

This
column can be left empty, in which case any generated test program will not include pattern
information for this test suite.

Test Flags
: The name of a set of test suite flags that is defined in
the
`test flag table`（raw: `132781.htm`）
. The name you specify here must come from the

Flag Set ID
 column.

Notes
: Any notes you want to make about the test suite. Comments are
strictly for human use and are not processed in any way by STPM.

### Syntax（取自子主题 Bin table of a TPT）

Each row in the bin table describes one bin. The table contains these columns:

SBin
: The ID of the software bin. It is used to refer to this bin from
the
`test suite table`（raw: `132779.htm`）
. To be compatible with the SmarTest Data
Formatter, the number must be between 0 and 32767.

SBin Label
: The name of the software bin.

HBin
: The ID of the hardware bin connected to the software bin.

HBin Label
: The name of the hardware bin.

Note that this information
will be ignored by STPM when it converts the CSV file into a testflow.

Type
: The type of the bin. It can be "good", "bad", or "other".

Color
: The color for the bin. The color can be any string.

If this
column is left empty, STPM uses "" (empty string) for the color.

Reprobe
: The reprobe flag for the bin. It can be 1 (on) or 0 (off).

If this column is left empty, STPM uses 0 (reprobe off).

Overon
: The overon flag for the bin. It can be 1 (on) or 0 (off).

If this column is left empty, STPM uses 0 (overon off).

Notes
: Any notes you want to make about the bin. Comments are
strictly for human use and are not processed in any way by STPM.

### Syntax（取自子主题 Test table of a TPT）

Each row in the test suite table describes one test. The table contains these
columns:

Test Suite Name
: The name of the test suite in the test program that
contains the test. The test suite must be defined with this name in the
`test suite table`（raw: `132779.htm`）
.

Test Name
: The name of the test.

Test Stage
: The name of the test stage for which these limits apply.

If this column is left empty, the limits in this row apply to all test stages.

SBin
: The number of the software bin to which this test is connected. You
can specify any bin number that is defined in the SBin column of the
`bin table`（raw: `132775.htm`）
.

If this column is left empty, no binning occurs as a result of this test.

Test Number
: The test number for this test.

If this column is left
empty, the test number will be generated automatically by SmarTest.

Lower Limit
: The lower limit for this test.

If this column is left
empty, there is no lower limit for the test.

Lower Op
: The operator for comparing the lower limit for this test
with the measured value.

This column is required when a lower limit has been specified (see
above) and ignored otherwise.

Upper Op
: The operator for comparing the measured value with the
upper limit for this test with the measured value.

This column is required when an upper
limit has been specified (see above) and ignored otherwise.

Upper Limit
: The upper limit for this test.

If this column is left
empty, there is no upper limit for the test.

Unit
: The unit for the lower and upper limit values for this
test.

Whether a value is required in this column when a limit is specified depends on the
test method. The permitted values likewise depend on the test method.

Source
: Whether this limit will be stored in the testflow or in the
test table.

Notes
: Any notes you want to make about the test. Comments are
strictly for human use and are not processed in any way by STPM.

### Syntax（取自子主题 Test parameter table of a TPT）

Each row in the test suite table describes one set of test parameters. The table
contains these columns:

Test Suite Name
: The name of the test suite in the test program to
which the parameters apply. The test suite must be defined with this name in the
`test suite table`（raw: `132779.htm`）
.

Test Method
: The name of the test method being executed in the test
suite.

Param
: Each of these named
Param
 contains the
name and value for one parameter that is passed to the test method.

You can create as many
parameter columns as desired. Each column must have the title

Param
.

Parameters must be specified in the column the form

<name>
=
<value>
, for
example,
output=None
.

### Syntax（取自子主题 Test flag table of a TPT）

Each row in the test flag table describes one set of settings of test suite flags. The
table contains these columns:

Flag Set ID
: The name for the set of test flags. It is used to refer
to this set from the
`test suite table`（raw: `132779.htm`）
.

(individual flags): Each column corresponds to one flag. It can contain 1 to indicate that
the flag is on, or 0 to indicate that it is off.

Notes
: Any notes you want to make about the test flag set. Comments
are strictly for human use and are not processed in any way by STPM.

### Syntax（取自子主题 Test stage table of a TPT）

Each row in the test flags table describes a test object. The table contains these
columns:

Test Object
: The object to which different values are assigned in
different test stages. You can specify the name of a test group, test suite, or user testflow
variable here.

Type
: The type of the object. Supported types include:

GROUP
: test group

TEST_SUITE
: test suite

USER_FLAG
: user testflow variable

Stage: <stage>
: Each test stage has its own column with the
name "Stage" foollowe dby the name of the stage, for example,
Stage: QA
.
You can freely choose the names of the stages.

Each column specifies how the test object is
to be handled in this stage:

For test groups and test suites, the columns contain Y or N:

Y
: The
object is included in the test in this stage.

N
: The object is not included in the test in this stage.

For testflow variables, the columns contain an integer that is assigned to the variable in
this test stage.

Notes
: Any notes you want to make about the test object. Comments are
strictly for human use and are not processed in any way by STPM.

### Controls（取自子主题 OpenOffice spreadsheet for editing the CSV files）

STPM adds controls to the upper left corner of the spreadsheet (see graphic
above):

Load TPT
: Clicking this button lets you load a set of CSV
files.

Select the desired TPT master file in the Open dialog; the spreadsheet loads the CSV
files referenced in it.

Reload TPT
: Clicking this button reloads the information from the
last loaded set of CSV files.

Note that this overwrites any changes you may have made.

Save TPT
: Clicking this button saves the current state of the
spreadsheets to the corresponding CSV files.

### Sheets（取自子主题 OpenOffice spreadsheet for editing the CSV files）

Each sheet in the OpenOffice document contains one of the imported
CSV tables described in
`Test program template files`（raw: `132774.htm`）
.

### Columns（取自子主题 OpenOffice spreadsheet for editing the CSV files）

For descriptions of the table columns, see the documentation of
the CSV file containing the column in
`Test program template files`（raw: `132774.htm`）
.

Several of the columns have
drop-down lists from which you can choose appropriate values:

`Test suite table`（raw: `132779.htm`）

Test Flags

`Bin table`（raw: `132775.htm`）

Type

Color

Reprobe

Overon

`Test table`（raw: `140679.htm`）

Test Suite Name

Test Stage

SBin

Lower Op

Upper Op

Source

`Test parameter table`（raw: `140680.htm`）

Test Suite Name

`Test flag table`（raw: `132781.htm`）

Each column representing a flag

`Test stage table`（raw: `140683.htm`）

Type

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
