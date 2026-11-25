---
type: object
title: STPM control file
layer: file
stage: project
tags: []
related: []
sources:
  - 02_System_reference/02.09_Test_Program_Management/02.09.02.03_STPM_control_file.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# STPM control file

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **96,665 字符逐字取自** `<02_System_reference/02.09_Test_Program_Management/02.09.02.03_STPM_control_file.htm>` 及其子主题 `<02_System_reference/02.09_Test_Program_Management/02.09.02.03.01_Structure_of_an_STPM_control_file.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.02_File_and_parameter_settings.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.03_Preprocessing_and_postprocessing_scripts.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.04_write_tp.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.05_add_test.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.06_add_burst.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.07_add_test_to_burst.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.08_add_empty_test_group.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.09_remove_test.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.10_replace_test.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.11_remove_label.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.12_add_pattern.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.13_replace_pattern.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.14_tpt_generate_template.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.15_tpt_import_from_device.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.16_tpt_generate_device_dir.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.17_tpt_merge.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.18_tpt_add_test.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.19_tpt_replace_test.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.20_tpt_generate_tp.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.21_tpt_compare_tp.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.22_tpt_generate_test_stages.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.23_extract_subflow.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.24_merge_subflow.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.25_remove_subflow.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.26_clear_duplicated.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.02.03.27_clear_unused.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

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

<!-- 语法节 end -->

## 是什么

**文档事实** STPM control file 是给 SmarTest Program Manager（STPM）的脚本，告诉 STPM 如何执行一次 conversion process；其中包含用于添加、替换、删除 test 的命令，以及参数和 setup 命令。

**文档事实** 该文件的结构遵循 Python 编程语言的约定，可用普通文本编辑器创建和修改。STPM 本身从命令行控制；控制文件由命令行指定（`-setup` 选项），STPM 的具体操作由控制文件内容决定。

**文档事实** 控制文件中可包含三类设置：指定文件的设置（`mtp_device_testflow`、`mtp_template_dir`、`merge_rules`），定义环境的设置（`ate_target`、`ate_model`、`ate_version`），以及其他设置（`temp_dir`、`enable_backup`）。`mtp_device_testflow` 是必需的；其余设置可选。`merge_rules` 省略时不使用 merge rules file；`mtp_template_dir` 虽为可选，但部分命令要求存在有效的 TPT。路径可为绝对或相对路径，相对路径以调用 STPM 时的当前工作目录为基准。

**文档事实** 可选设置的文档默认值：`ate_target` 只列出 `'93000SS'`（Smart Scale system）；对应 `'93000SS'` 的 `ate_model` 可指定 `'PS1600'`，省略时默认值取决于 `ate_target`；`ate_version` 省略时用 `"7.1.4"`；`temp_dir` 省略时用 `/tmp`（且目录必须已存在、STPM 对其有写权限）；`enable_backup` 省略时用 1。备份放在原文件所在目录的 `back` 子目录，文件名追加 `_YYMMDD_HHMMSS` 时间戳。

**文档事实** 命令包括：`write_tp`；test 级操作 `add_test`、`add_burst`、`add_test_to_burst`、`add_empty_test_group`、`remove_test`、`replace_test`、`remove_label`；pattern 级操作 `add_pattern`、`replace_pattern`；TPT 操作 `tpt_generate_template`、`tpt_import_from_device`、`tpt_generate_device_dir`、`tpt_merge`、`tpt_add_test`、`tpt_replace_test`、`tpt_generate_tp`、`tpt_compare_tp`、`tpt_generate_test_stages`；subflow 操作 `extract_subflow`、`merge_subflow`、`remove_subflow`；清理操作 `clear_duplicated`、`clear_unused`。

**文档事实** 命令参数中的 MTP、STP、TPT 分别指 master test program、source test program、test program template：`mtp_device_testflow` 指向 MTP 的 testflow；`add_test` 等的 `test_flow_file` 指向 STP；`mtp_template_dir` 指向 TPT 目录。

**文档事实** 各命令都可带可选的 `pre_proc` 与 `post_proc`：前者在命令执行前运行，后者在执行后运行。两者的值使用同一语法：`<script>` 加上可选的 26 个以 `&` 开头的占位符（`&mdir`、`&sdir`、`&mtp_tf`、`&mtp_pmf`、`&mtp_conf`、`&mtp_tim`、`&mtp_lev`、`&mtp_tt`、`&mtp_rout`、`&mtp_wf`、`&mtp_anctrl`、`&mtp_chatt`、`&mtp_prot`、`&mtp_att`、`&stp_tf`、`&stp_pmf`、`&stp_conf`、`&stp_tim`、`&stp_lev`、`&stp_tt`、`&stp_rout`、`&stp_wf`、`&stp_anctrl`、`&stp_chatt`、`&stp_prot`、`&stp_att`），以及原样传给脚本的 `<user_parameters>`。除脚本名外，其余元素都是可选的；`<user_parameters>` 不得包含以 `&` 开头的词。

## 典型用法

**文档事实** 文档给出的示例控制文件是典型骨架：先写 `mtp_device_testflow = '...project.tf'` 与可选的 `merge_rules = '...merge_rules.py'`，再用两个 `add_test(...)` 从外部 testflow 引入 test（第二个带 `position = 'first'`、`lev_reuse = 'auto'`），最后写出 MTP 的目标路径。

**文档事实** 需注意：示例控制文件把写回写成赋值形式 `write_tp = '<path>'`，而 `write_tp` 命令子主题给出的语法是函数调用形式 `write_tp(path = '<mtp_target_file>', [pre_proc = ...], [post_proc = ...])`；两种写法在文档中并存。

**文档事实** `write_tp` 的 `path` 可与 `mtp_device_testflow` 相同，此时原文件被就地修改；是否生成备份由 `enable_backup` 控制。

**文档事实** `add_test` 的常用参数：`test_flow_file`（必需）；`test_source`（STP 含多个 test 时必需）；`test`（MTP 中的新名字，若 MTP 已有同名 test 则不添加并报错）；`test_group`（省略时 test suite 生成在 MTP 根、testflow 末尾）；`position`（默认 `optimal`，可选 `first`、`last`、`after:<test_name>`、`before:<test_name>`；未指定 `test_group` 时 `position` 被忽略）；`tim_reuse`/`lev_reuse`/`pat_reuse`（默认均为 `none`，可选 `auto`、`test:<test-name>`、显式 primary keys 等）；`reuse_scope`；`pat_dir`（默认 `patterns`，即 `vectors/patterns/`）；`test_flags`；`test_method`；`test_params`；以及 `sbin_num`/`sbin_label`/`hbin_num`/`hbin_label`。

**文档事实** 其余 test/pattern 命令：`add_burst` 在 MTP 中创建空 burst，之后可向其中加 test；`add_test_to_burst` 把外部 STP 中的 test 加到 MTP 中已有的 test（burst）；`add_empty_test_group` 创建新 test group，`parent` 必须已存在（省略时建在顶层），`position` 默认 `last`；`remove_test` 默认删除 test suite（`test_remove = 1`），并按 `unused` 策略处理 timing/level/pattern，`keep_pat_label` 默认 0；`replace_test` 的 `copy_test_method` 默认 0（保留 MTP 的属性），reuse 默认 `none`、remove 默认 `unused`；`remove_label` 的 `pmf_only` 默认 0（从 MTP 删除 pattern），设为 1 时保留 pattern、只从 pattern master file 移除其条目；`replace_pattern` 的 `pat_remove` 默认 `unused`，`waveforms_compare_mode` 默认 `none`。

**文档事实** `pre_proc` / `post_proc` 示例：执行 `write_tp` 前运行当前目录的 `preparation.py`（不传参数）；执行后运行 `/usr/tools/scripts/cleanup.pl`，后者收到 `--mdir '/user/johndoe/mtp' --cmd write --stage 3` 这样的参数串（`&mdir` 被替换为 MTP 路径，其余文本原样传递）。

**文档事实** TPT 相关命令构成一套模板工作流：`tpt_generate_template` 生成新的空 TPT；`tpt_import_from_device` 从现有 device 目录生成 TPT（可选 `include_groups`、`empty_groups`、`copy_static_content`、`allow_overwrite`，后者默认 0）；`tpt_generate_device_dir` 从 TPT 生成 device 目录（`device_dir` 必须不存在或为空，`device_name` 默认 `"device"`）；`tpt_add_test` / `tpt_replace_test` 在 TPT 中增加/替换 test；`tpt_generate_tp` 由现有 test program 与 TPT 生成新 test program；`tpt_compare_tp` 比较 MTP 与 TPT 规范并输出报告（默认 `compare_log.html`）；`tpt_merge` 合并多个 TPT（冲突时 source TPT 覆盖 target，列表中靠后的 source 覆盖靠前的）；`tpt_generate_test_stages` 从 TPT 的 test stage table 生成 data log profile。

**文档事实** subflow 工作流：`extract_subflow` 把 MTP 的一部分导出为新的 STP；`merge_subflow` 把先前用 `extract_subflow` 导出的 STP 重新导入 MTP；`remove_subflow` 从 MTP 删除某 STP 导入的部分。`merge_subflow` 与 `remove_subflow` 的 `include_groups` 与 `exclude_groups` 互斥。

**文档事实** 清理命令：`clear_duplicated` 删除 MTP 中的重复 primaries，并把对重复项的引用改为指向原项；`clear_unused` 删除未使用的 primaries、patterns 与 objects。两者的 `analyze_only = 1` 都表示只生成报告、不实际删除；`analyzer_path` 指定报告路径（默认分别为 `<device directory>/reports/duplicated_report.csv` 与 `unused_report.csv`）。

## 和谁有关

- **文档事实** 与 SmarTest Program Manager（STPM）：控制文件决定 STPM 的操作；STPM 从命令行运行，`-setup` 选项指定控制文件。入边 `Using SmarTest Program Manager` 的表述是 STPM 的操作细节由其 control file 内容决定。
- **文档事实** 与 `STPM command line options`：入边说明 `-setup` 用于在命令行指定控制文件，因此两者是“入口参数—配置文件”的关系。
- **文档事实** 与 `STPM merge rules file`：入边说明使用哪个 merge rules file 由 STPM control file 指定；对应本文件的 `merge_rules` 设置。
- **文档事实** 与 `Creating and editing an STPM control file`：该主题说明控制文件可用标准文本编辑器创建/修改，并遵循 Python 语法约定；本页是其语法与命令的汇总入口。
- **文档事实** 与 Test program template（TPT）主题：`mtp_template_dir` 指定 TPT 目录，`tpt_*` 命令围绕 TPT 的生成、导入、合并、对比以及从 TPT 生成 test program/device 目录。
- **文档事实** 与各命令子主题：`02.09.02.03.01`–`02.09.02.03.27` 分别记录结构、文件/参数设置、预处理/后处理脚本以及各命令的完整参数表；本页 `Subtopics` 是这些页面的索引。
- **文档事实** 与 `STPM UI plug-in`、`STPM MCM parameter settings`：入边显示 `STPM UI plug-in` 的相关页引用本控制文件；`STPM MCM parameter settings` 则是 STPM MCM 的平行控制文件设置页，说明其参数用于指定 STPM MCM 操作的目录与 testflow。

## 版本

**文档事实** `Functional changes` 只记载 `Introduced in SmarTest 7.0.4`，未列后续变更。

## 出处

- 主文档：`02_System_reference/02.09_Test_Program_Management/02.09.02.03_STPM_control_file.htm`（Subtopics、Functional changes）。
- 语法/参数材料另取自其全部子主题 `02.09.02.03.01`–`02.09.02.03.27`（Structure、File and parameter settings、Preprocessing and postprocessing scripts、write_tp、add_*、remove_*、replace_*、tpt_*、*_subflow、clear_*；objscaffold 逐字汇总，已读）。
- 「和谁有关」另参考 `extract/edges.jsonl` 中指向/离开该页的边记录（含 STPM 总览、命令行、merge rules、UI plug-in 等页的 context）。
