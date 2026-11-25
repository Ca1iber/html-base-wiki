---
type: object
title: MTPT (STPM MCM mapping tables)
layer: file
stage: project
tags: []
related: []
sources:
  - 02_System_reference/02.09_Test_Program_Management/02.09.03.04_MTPT__STPM_MCM_mapping_tables.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# MTPT (STPM MCM mapping tables)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **19,874 字符逐字取自** `<02_System_reference/02.09_Test_Program_Management/02.09.03.04_MTPT__STPM_MCM_mapping_tables.htm>` 及其子主题 `<02_System_reference/02.09_Test_Program_Management/02.09.03.04.01_STP_table.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.03.04.02_Pin_mapping_table.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.03.04.03_Group_mapping_table.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.03.04.04_Test_mapping_table.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.03.04.05_Test_suite_table.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.03.04.06_Bin_mapping_table.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.03.04.07_Test_number_mapping_table.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.03.04.08_Testflow_variable_mapping_table.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.03.04.09_Special_tests_table.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.03.04.10_Shared_pins_table.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.03.04.11_Test_flag_table.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.03.04.12_Off_DC_levels_table.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.03.04.14_MTPT_configuration_file.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.03.04.15_OpenOffice_spreadsheet_for_editing_the_CSV_files.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax（取自子主题 STP table）

Each row in the STP table describes one test program. The table contains these
columns:

STP
: The name of the test program

Test Flow Path
: The file path of the STP's testflow file

Prefix
: The prefix that STPM MCM will use for renaming elements from
this STP. This value can be omitted if no prefix is desired for elements from an STP.

Note
that whether STPM MCM actually applies these prefixes to pins from the STP depends on the
value in the
Apply Prefix On Pin Config
 column (see below). Whether the
prefixes are used for other imported elements is controlled by the global setting

apply_prefix_on_specs_and_equations
 (described in
`STPM MCM parameter settings`（raw: `138126.htm`）
).

Bin Offset
: The number that STPM MCM adds to bin numbers from this
STP when merging it into the MTP

Test Number Offset
: The number that STPM MCM adds to test numbers
from this STP when merging it into the MTP

Tim EQNSET Offset
: The number that STPM MCM adds to timing equation
set numbers from this STP when merging it into the MTP

Lev EQNSET Offset
: The number that STPM MCM adds to level equation
set numbers from this STP when merging it into the MTP

Test Mode
: (Optional) The test mode from the test table that is to be
used or this STP. This value can be left empty if no mode is desired for a test.

Apply Prefix On Pin Config
: Whether the prefixes from the

Prefix
 column are used for this pin:

0: The prefix is not applied to the names of pin configuration objects from this STP

1: The prefix is applied to the names of pin configuration objects from this STP

Pin
configuration objects include names of pins, pin groups, power supplies, port, and utility
lines.

Keep Unused Data
: Whether all timing, level, and pattern data from
this STP is copied to the MTP or just the data that is actually used by the MTP:

0: Only timing, level, and pattern data that is used is copied to the MTP

1: All timing, level, and pattern data in the STP is copied to the MTP

Notes
: This column allows both you and STPM MCM to add remarks about
the test program. These notes are just for human consumption and are never processed
automatically by STPM MCM. They may be overwritten when the tables are updated, so they are not
a suitable place for storing important information.

### Syntax（取自子主题 Pin mapping table）

Each row in the pin mapping table describes the mapping of a specific STP pin or
utility line. The table contains these columns:

STP:<STP name>
: Beginning at the left of the table, there is
one column for each STP, with the STP name as the column title. The columns list the pin names
from the STPs.

MTP Pin[@shared port]
: The name of the pin in the MTP. If the pin
belongs to a shared port in the MTP, the port name is appended with a @ character, for example,
"A_CLK@MTP_SHARED".

The default name STPM MCM enters in this column is the STP pin name with
the prefix defined in the
`STP table`（raw: `137967.htm`）
. (If the "apply prefix on pin config"
setting is 0, STPM MCM enters just the STP pin name without the prefix.)

If an STP pin is not connected to any MTP pin, this is indicated by

__NC__
.

MTP Pin Attribute
: Digital pins can be defined as triggers in this
column; analogs pins can be assigned triggers.

A digital pin is defined as a trigger by
entering a statement in the form

TRIG_DEF:
<trigger_id>
,

<input_pin>
 in this column:

<trigger_id>
 must be
C1
,

C2
,
C3
, or
C4
. Each of these IDs can
be used only once per MCM.

<input_pin>
 specifies which pin is used as the trigger. It can be
either COM1 (to specify the CT2 pin) or COM2 (to specify the CT1 pin).

An analog pin is triggered by a digital pin by including a statement of the form

TRIG:
<pin name>
 in this column.
<pin
name>
 is the name of a pin (as it appears in the
MTP Pin[@shared
port]
 column) that you have declared as a trigger pin as described above.

Site <n>
: There is one column for each site that has been
defined in the
generate_template
 command. These columns list the channel
number that the pin has for the site in question in the MTP. This information is not
automatically generated by STPM MCM and must be filled in by you.

Notes
: This column allows both you and STPM MCM to add remarks about
the pin. These notes are just for human consumption and are never processed automatically by
STPM MCM. They may be overwritten when the tables are updated, so they are not a suitable place
for storing important information.

### Syntax（取自子主题 Group mapping table）

Each row in the group mapping table describes the mapping of a specific STP entity
(port, pin group, or utility purpose). The table contains these columns:

STP:<STP name>
: Beginning at the left of the table, there is
one column for each STP, with the STP name as the column title. The columns list the entity
names from the STPs.

MTP Group
: The name of the entity in the MTP.

The default name STPM
MCM enters in this column is the STP name with the prefix defined in the
`STP table`（raw: `137967.htm`）
. (If the "apply prefix on pin config" setting is 0, STPM MCM enters just the STP pin name
without the prefix.)

If an STP entity is not connected to any MTP entity, this is indicated by

__NC__
.

Notes
: This column allows both you and STPM MCM to add remarks about
the port, pin group, or utility purpose. These notes are just for human consumption and are
never processed automatically by STPM MCM. They may be overwritten when the tables are updated,
so they are not a suitable place for storing important information.

STPM MCM initially fills
this column with the name of the STP from which an entity is imported and the firmware command
that is triggered by the mapping (DFGP for pin groups, DFPT for ports, or DFUP for utility
purposes).

### Syntax（取自子主题 Test mapping table）

Each row in the test mapping table describes the mapping of a specific STP test suite
or test group. In certain cases (see the CCT mode described below), multiple test suites can be
described in one row.

The table contains these columns:

STP:<STP name>
: Beginning at the left of the table, there is
one column for each STP, with the STP name as the column title. The columns list the test suite
or test group names from the STPs.

Mode
: The integration mode for the test suite or test group in the STP:

TG
: Test group integration mode - the test group from the STP is
integrated into the MTP, with all of its contained test suites and test groups and internal
structure (branches etc.) intact. This mode applies only to test groups.

TS
: Test suite integration mode. The test suite is integrated into the
MTP without any surrounding testflow structures. This mode applies only to test suites.

CCT
: Concurrent test integration mode - all test suites in this row are
merged into the same MTP test group, which conforms to the concurrent test framework, and
will be executed concurrently.

This mode applies only to test suites and requires test
suites to be listed in at least two
<STP name>
 columns in this row.

CCT_FG
: This mode is similar to the CCT mode. However, instead of
creating a multi_bin node in the fail branch of the test suite, it creates a test group named
"
<test object name>
_FG" in this branch. You can insert objects into
this group by specifying it as a parent group.

For example, if a test suite has the name
"CCT1" in the
MTP Test Object
 column (see below) and has the
integration mode
CCT_FG
, you can enter "CCT1_FG" in the
MTP
Parent Group
 column (see below) of any other object to include it in the fail
branch of CCT1.

NOP
: This object is not integrated into the MTP.

You can use this
mode to temporarily exclude objects that you may want to include again later (and therefore
do not want to delete from the table), for example during debugging.

MTP Parent Group
: The test group in the MTP into which this test
suite or test group is put. This entry is ignored if a matching test object already exists in
the MTP. (See
MTP Test Object
, below, for details.)

If there is no
entry in this column, the test group or test suite is integrated at the end of the testflow in
the MTP.

MTP Test Object
: The name of the test suite or test group in the MTP
that is replaced by the object from the STP.

If an object with this name already exists in
the MTP, the object from the STP replaces it. If no object with this name exists in the MTP,
the object from the STP is copied to the location specified by the entry in the
MTP
Parent Group
 column and renamed, if necessary.

Notes
: This column allows both you and STPM MCM to add remarks. These
notes are just for human consumption and are never processed automatically by STPM MCM. They
may be overwritten when the tables are updated, so they are not a suitable place for storing
important information.

### Syntax（取自子主题 Test suite table）

Each row in the test suite table describes one test suite. The table contains these
columns:

STP
: The name of the STP (source test program) from which the test
suite is imported

STP TestSuite
: The name of the test suite in the STP

MTP TestSuite
: The name of the test suite in the MTP

Test Flags
: The name of the test flag set that is applied to the test
suite in the MTP.

This name must match the entry for the desired flag set in the

FlagSet Id
 column of the
`Test flag table`（raw: `138058.htm`）
.

If the
Test Flags
 column contains the value

__DEFAULT__
, no test flag set is specified for the test suite and it uses
the default test flags for the MTP.

UTM Id
: The ID of the UTM that will be executed by this test
suite

Limits
: Test limits specified for the test suite

Each limit entry
has the format
<limit name>
=
<lower
value>
 <= x <=
<upper limit>
. You can omit either
the lower or the upper limit (for example
functional = x <= 4)
. You can
also use < in place of <=.

If you want to specify more than one limit, you must put each one in a new line (separated
by CR characters) and put a semicolon (;) after each limit except the last one.

Parameters
: The parameters that are passed to the test method when
the test suite is executed

Each parameter entry has the format
<parameter
name>
=
<parameter value>
.

If you want to specify more than one parameter, you must put each one in a new line
(separated by CR characters) and put a semicolon (;) after each parameter except the last
one.

Notes
: This column allows both you and STPM MCM to add remarks about
the test suite. These notes are just for human consumption and are never processed
automatically by STPM MCM. They may be overwritten when the tables are updated, so they are not
a suitable place for storing important information.

STPM MCM initially fills this column with
the information on where it has replaced pin, group, or port names, as well as any
warnings.

### Syntax（取自子主题 Bin mapping table）

Each row in the bin mapping table describes the mapping of a specific STP bin. The
table contains these columns:

STP
: The name of the STP from which the bin is imported

STP SBin
: The software bin number of the bin in the STP

SBin
: The software bin number of the bin in the MTP

SBin Label
: The software bin label of the bin in the MTP

HBin
: The hardware bin number of the bin in the MTP

HBin Label
: The hardware bin label of the bin in the MTP

Type
: The type of the bin in the MTP. The value in this column can be

good
 or
bad
.

Color
: The color of the bin in the MTP

Reprobe
: Whether the Reprobe flag is set for this bin in the MTP. The
value in this column can be 0 (Reprobe off) or 1 (Reprobe on).

Overon
: Whether the Overon flag is set for this bin in the MTP. The
value in this column can be 0 (Overon off) or 1 (Overon on).

Notes
: This column allows both you and STPM MCM to add remarks about
the bn. These notes are just for human consumption and are never processed automatically by
STPM MCM. They may be overwritten when the tables are updated, so they are not a suitable place
for storing important information.

STPM MCM initially fills this column with the source of
the bin. It also notes any conflicting definitions it finds and indicates bins that are
default bins.

If any conflicts are noted, they are prefixed with the coordinates of the conflicting cell
(in standard Excel notation). For example, "[D6]" indicates that the value in row 6, column D
conflicts with an earlier entry in the same column.

### Syntax（取自子主题 Test number mapping table）

Each row in the test suite table describes one test number. The table contains these
columns:

STP
: The name of the STP (source test program) from which the test
number is imported

STP Test Number
: The test number as it is used in the STP

MTP Test Number
: The test number in the MTP to which the STP test
number is mapped

Notes
: This column allows both you and STPM MCM to add remarks about
the test number. These notes are just for human consumption and are never processed
automatically by STPM MCM. They may be overwritten when the tables are updated, so they are not
a suitable place for storing important information.

STPM MCM initially fills this column with
the information on the source of the number and any detected conflicts.

### Syntax（取自子主题 Testflow variable mapping table）

Each row in the testflow variable mapping table describes the mapping of a specific
variable or flag. The table contains these columns:

STP
: The name of the STP from which the variable is imported

For
system testflow flags, this column contains
SYSTEM_FLAGS
.

STP Var
: The name of the variable or flag in the STP

For system
testflow flags, this column is empty.

MTP Var
: The name of the MTP variable or flag to which the STP
variable or flag is mapped

Type
: The data type of the MTP variable or flag

Value
: The value to which the MTP variable or flag is set

For
system flags, the value may initially be empty if a flag was defined in none of the STPs or
had different settings in different STPs. You must fill in any empty cells in this column;
otherwise, STPM will generate an error when creating the MTP.

Notes
: This column allows both you and STPM MCM to add remarks about
the variable or flag. These notes are just for human consumption and are never processed
automatically by STPM MCM. They may be overwritten when the tables are updated, so they are not
a suitable place for storing important information.

STPM MCM notes here any conflicts and
other issues detected.

### Syntax（取自子主题 Special tests table）

Each row in the special tests table describes the handling of one type of special test
suite. The table contains these columns:

Type
: The kind of
`special test suite`（raw: `20281.htm`）
 that
the column describes

Master STP
: The name of the STP from which this kind of test suite is
imported.

For example, when the entry for "download" in this column is "MyTP4", every time
the
download
 special test suite is needed in the MTP, the version from the
MyTP4 STP is used.

An entry of __NONE__ in this column indicates that none of the specified STPs contain a
special test of this type.

Notes
: This column allows both you and STPM MCM to add remarks. These
notes are just for human consumption and are never processed automatically by STPM MCM. They
may be overwritten when the tables are updated, so they are not a suitable place for storing
important information.

### Syntax（取自子主题 Shared pins table）

Each row in the shared pins table describes the handling of one set of shared pins. The
table contains these columns:

CCT Group Name
: The name of an MTP test group that contains
concurrent tests

The name must appear in the
MTP Parent Group
 column
in the
`Test mapping table`（raw: `137976.htm`）
 and the mode specified for the group must be

CCT
.

Shared DPS Pin/Port
: The name of the shared pin or digital port

If
a shared port is noted here, it must be listed in the
MTP Pin[@shared
port]
 column of the
`Pin mapping table`（raw: `137972.htm`）
.

Master STP
: The name of the STP from which the timings and levels for
this shared pin or port are imported.

Notes
: This column allows both you and STPM MCM to add remarks about
the shared pin. These notes are just for human consumption and are never processed
automatically by STPM MCM. They may be overwritten when the tables are updated, so they are not
a suitable place for storing important information.

### Syntax（取自子主题 Test flag table）

Each row in the test flag table describes a test flag set. The table contains these
columns:

FlagSet Id
: The name of the flag set

This name can be used to
reference the flag set from the
`Test suite table`（raw: `137978.htm`）
.

(individual flags): Each column corresponds to one flag. It can contain 1 to indicate that
the flag is on, or 0 to indicate that it is off.

Notes
: This column allows both you and STPM MCM to add remarks about
the flag set. These notes are just for human consumption and are never processed automatically
by STPM MCM. They may be overwritten when the tables are updated, so they are not a suitable
place for storing important information.

In all columns describing flag settings, 0 indicates that the flag is off and 1 indicates
that it is on.

### Syntax（取自子主题 Off DC levels table）

Each row in the levels table describes the levels for one DC pin. The table contains
these columns:

MTP Pin
: The name of the DC pin in the MTP for which you are setting
the levels. The pin names in this column must match the names in the
`Pin mapping table`（raw: `137972.htm`）
.

The
__DEFAULT__
 entry is already predefined; it applies to all pins
of inactive STPs for which there is no explicit entry in this table. (That is, all pins whose
name does not appear in the
MTP Pin
 column.)

vout
: The DC power supply voltage in V

ilimit
: The connect current limit in mA

offcurr
: The off current state of the pin

Supported states are:

min
: Minimum current for high impedance

act
: Actual current for low impedance

open
: High impedance and open output relay

See
`DPSPINS resources`（raw: `16887.htm`）

for more information on these states.

vih
: The Vih voltage in V

vil
: The Vil voltage in V

voh
: The Voh voltage in V

vol
: The Vol voltage in V

Notes
: This column allows both you and STPM MCM to add remarks about
the level. These notes are just for human consumption and are never processed automatically by
STPM MCM. They may be overwritten when the tables are updated, so they are not a suitable place
for storing important information.

### Syntax（取自子主题 MTPT configuration file）

The internal structure of the MTPT configuration file is private and subject to change
without notice.

### Controls（取自子主题 OpenOffice spreadsheet for editing the CSV files）

STPM MCM adds controls to the upper left corner of the spreadsheet (see graphic
above):

Open MTPT
: Clicking this button lets you load a set of CSV
files.

Select the desired
`MTPT configuration file`（raw: `137968.htm`）
 (with a .mtpt filename extension) in the
Open dialog; the spreadsheet loads the CSV files belonging to it.

Reload MTPT
: Clicking this button reloads the information from the
last loaded set of CSV files.

Note that this overwrites any unsaved changes you may have made
in OpenOffice.

Save MTPT
: Clicking this button saves the current state of the
spreadsheets to the corresponding CSV files.

Update Shared Pins
: Clicking this button creates one entry in the

`Shared pins table`（raw: `138031.htm`）
 for each shared pin specified in the
`Pin mapping table`（raw: `137972.htm`）
. All
entries created by clicking this button have default values.

### Sheets（取自子主题 OpenOffice spreadsheet for editing the CSV files）

Each sheet in the OpenOffice document contains one of the imported
CSV tables described in
`MTPT (STPM MCM mapping tables)`（raw: `138082.htm`）
.

### Columns（取自子主题 OpenOffice spreadsheet for editing the CSV files）

For descriptions of the table columns, see the documentation of
the CSV file containing the column in
`MTPT (STPM MCM mapping tables)`（raw: `138082.htm`）
. In the spreadsheet, columns with
a light blue title cell contain data related to the STPs and columns with a medium blue title
cell contain data related to the MTP.

Several of the columns have drop-down lists from
which you can choose appropriate values:

`STP table`（raw: `137967.htm`）

Apply Prefix On Pin Config

Keep Unused Data

`Pin mapping table`（raw: `137972.htm`）

MTP Pin Attribute

`Test mapping table`（raw: `137976.htm`）

Mode

`Test suite table`（raw: `137978.htm`）

STP

Test Flags

`Bin mapping table`（raw: `138001.htm`）

STP

Type

Color

Reprobe

Overon

`Test number mapping table`（raw: `138003.htm`）

STP

`Testflow variable mapping table`（raw: `138022.htm`）

STP

Type

`Special tests table`（raw: `138023.htm`）

Type

`Test flag table`（raw: `138058.htm`）

All columns representing individual flags

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
