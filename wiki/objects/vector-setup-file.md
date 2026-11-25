---
type: object
title: Concepts of vector setup
layer: file
stage: pattern
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.07.01_Concepts_of_vector_setup.htm
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.05_The_pattern_master_file.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Concepts of vector setup

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **9,443 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.07.01_Concepts_of_vector_setup.htm>` 及其子主题 `<02_System_reference/02.06_Command_Reference/02.06.07.01.01.01_The_label_definition.htm>`、`<02_System_reference/02.06_Command_Reference/02.06.07.01.01.02_The_vectors.htm>`、`<02_System_reference/02.06_Command_Reference/02.06.07.01.02_Label_definition__sequencer_program__and_sequencer_area.htm>`、`<02_System_reference/02.06_Command_Reference/02.06.07.01.03_Sequencer_areas_and_vector_areas.htm>`、`<02_System_reference/02.06_Command_Reference/02.06.07.01.04.01_Selecting_the_memory_type.htm>`、`<02_System_reference/02.06_Command_Reference/02.06.07.01.04_Addressing_the_vector_areas.htm>`、`<02_System_reference/02.06_Command_Reference/02.06.07.01.05_The_pattern_master_file.htm>`、`<02_System_reference/02.06_Command_Reference/02.06.07.01.07.04_Executing_a_label.htm>`、`<02_System_reference/02.06_Command_Reference/02.06.07.01.08.01_Vector_generating_instructions.htm>`、`<02_System_reference/02.06_Command_Reference/02.06.07.01.08.02_Address_instructions.htm>`、`<02_System_reference/02.06_Command_Reference/02.06.07.01.08.06_Instructions_for_PRBS_and_SmartLoop_tests.htm>`、`<02_System_reference/02.06_Command_Reference/02.06.07.01.09.01_Data_transfer_from_the_vector_area_to_the_data_queue.htm>`、`<02_System_reference/02.06_Command_Reference/02.06.07.01.10.01_Synchronization_within_sequencing_groups.htm>`、`<02_System_reference/02.06_Command_Reference/02.06.07.01.10.02_De-coupling_ports_by_separate_sequencing_groups.htm>`、`<02_System_reference/02.06_Command_Reference/02.06.07.01.10.03_Phase_synchronization_across_sequencing_groups.htm>`、`<02_System_reference/02.06_Command_Reference/02.06.07.01.10.04_Defining_sequencing_groups.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 The label definition）

The following instances of the
SQLB
 command define the labels which
provide the standard example for the explanation of the vector
setup:

```
SQLB "test_1",MAIN,4,8,"table1"
SQLB "test_2",MAIN,9,12,"table1"
```

Both
labels are associated with the default port, that is, they can be executed independently (with

FTST?
); both are of type
MAIN
, and both have

table1
 as their base wavetable.

### Example（取自子主题 The vectors）

The following figure shows the left upper corner of the index array for the label

test_1
 of the standard example:

The vector numbers in the first column count the parallel vectors. They are

logical vector numbers
 (for details see
`Addressing the vector areas`（raw: `119995.htm`）
).

### Example（取自子主题 Label definition, sequencer program, and sequencer area）

The following figure shows the label definitions of the standard example and the
corresponding sections of the sequencer area for the default port
@
:

Since the default port contains all configured pins, the sequencer area on the
right side of this figure is stored in the memory of all pins.

### Example（取自子主题 Sequencer areas and vector areas）

The following figure illustrates the case where one pin belongs to more than one
port:

Observe the following points in this figure:

port1
 comprises the pins
Pin1
 and
Pin2
, while
port2
 only
contains
Pin2
.

The arrows indicate which vector area segments belong to which labels.
Pin2
 has two
vector areas, one for the labels of
port1
 and one for the labels of
port2
.

The numbers above the arrow heads are the start addresses of the vector area segments for
the respective label (as defined by
STVA
).

The association of the vector generating instructions to vector area sub-segments is
exemplified by
Pin1
 and
Test 1
.

### Example（取自子主题 Selecting the memory type）

The following figure illustrates how the vector areas of different sites can be physically shared
if the respective channels belong to the same 4-channel group of a Pin Scale 9G
system. It also shows that a
SM
 vector area and a

SHMEM
 vector area can exist in parallel for the same
port.

### Example（取自子主题 Addressing the vector areas）

The following figure displays the relations between the sequencer program and the
vector areas of the standard example, and also illustrates the various concepts introduced to
describe the structure of these areas:

The left side of the figure shows a section of the sequencer area for the default
port
@
. It contains the sequencer programs for two labels (command line 4
through 8 and line 9 through 12). The right side displays the associated segments of the vector
areas for the pins
IN1
 and
OUT1
.

Notice the following points in the
figure:

An instance of the sequencer area for
@
 is contained in the memory of
both pin
IN1
 and pin
OUT1
.

Each of the rows on the right side represents one memory word.

Every cell of a row represents 8 bits. Every active vector contains one physical waveform
index (which is displayed in hexadecimal notation).

The padding (inactive) vectors are left blank in the figure.

The numbers to the left of the memory words specify the absolute start addresses of the
words within the vector areas.

The numbers above the memory words are the logical vector numbers.

The first label contains two sequencer constructs:

The first construct consists of the
RPTV
 instruction and the single
words starting at address 408 in the vector areas of both pins. Only the first 7 data cells
of this block contain waveform DC/DC power units.

The second construct consists of the
GENV
 instruction and the two words
starting at addresses 416 and 424. The last 7 cells of the second word contain no user
data.

The second label contains one sequencer construct (framed by a dotted line), which
comprises two words.

### Syntax（取自子主题 The pattern master file）

The syntax of the pattern master file is as
follows:

hp93000,pattern_master_file,0.1

[path:

[<
relative_or_absolute_path_1

>]]

files:

<
file_name_1_1
>

<
file_name_1_2
>

...

<
file_name_1_m
>

[[path:

[<
relative_or_absolute_path_2
>]]

files:

<
file_name_2_1
>

<
file_name_2_2
>

...

<
file_name_2_n
>

...]

The
default for the path is the
vectors
subdirectory of the current device. But
if you specify a path, note that the reference directory for relative paths is the

waste
 subdirectory of the device. Therefore, if your pattern files are in
the subdirectory
sample
 of the
vectors
 directory,
you must specify the relative path to this directory as

./vectors/sample
.

You can add comments to a pattern master file
after "
-- "
 (2 times the minus sign followed by a space) at the beginning
of a line.

### Example（取自子主题 The pattern master file）

Both the usage of relative paths and the insertion of comments are illustrated by the
following example
file:

```
hp93000,pattern_master_file,0.1

-- The following file must reside in <device>/vectors:
files:
sample1.binl

-- The following path points to <device>/vectors/pmfl_test:
path: ../vectors/pmfl_test

files:
sample2.binl.gz
sample3.binl.gz
```

### Example（取自子主题 Executing a label）

In order to execute the label
test_2
 of the standard example with the
timing defined in the
`Timing Setup Commands`（raw: `10585.htm`）
 chapter, proceed as follows:

SQSL "test_2"

SPRM 101,1,101002,101003

FTST?

### Example（取自子主题 Vector generating instructions）

Two examples of vector generating instructions
are:

```
SQPG 7,GENV,9,,,(@)
```

This
GENV
 instruction
generates 9 vectors.

```
SQPG 6,RPTV,6,5,,(@)
```

This

RPTV
 instruction generates 6 vectors 5 times in a row.

### Example（取自子主题 Address instructions）

If the vector setup contains only patterns for the default port, the reply of an

SQPG?
 query looks as
follows:

```
> SQPG? "test",(@)
< SQPG 5,STVA,112,,,(@)
< SQPG 6,STSA,,,,(@)
< SQPG 7,GENV,9,,,(@)
< SQPG 8,STOP,,,,(@)
```

The

STVA
 address is returned as
param_1
. However, after you
have added a pattern for a user defined port to the setup, it will be returned as

param_2
:

```
> SQPG? "test",(@)
< SQPG 5,STVA,,112,,(@)
< SQPG 6,STSA,,,,(@)
< SQPG 7,GENV,9,,,(@)
< SQPG 8,STOP,,,,(@)
```

### Examples（取自子主题 Instructions for PRBS and SmartLoop tests）

### Example 1

The following is the sequencer program of a PRBS test.

```
> SQPG? "prbs_test",(@)
< SQPG 0,STVA,0,,,(@)
< SQPG 1,STSA,,,,(@)
< SQPG 2,BRKV,200,0,,(@)
< SQPG 3,LBGN,100,,,(@)
< SQPG 4,TMUA,,,,(@)
< SQPG 5,PRBS,2147483647,4095,,(@)
< SQPG 6,LEND,,,,(@)
< SQPG 7,STOP,,,,(@)
```

This
example combines a PRBS test with a TMU per pin measurement. Note that the

TMUA
 instruction is included in a loop. Note also that the first parameter
of
PRBS
 is set to its maximum value 2
31
 - 1, and that the number
of cycles is increased above this maximum by multiplication with the second parameter, which is
also set to its maximum value 2
12
 - 1.

### Example 2
```
> SQPG? "loopback_tmu",(@)
< SQPG 0,STVA,0,,,(@)
< SQPG 1,STSA,,,,(@)
< SQPG 2,LPBK,1000,1,,(@)
< SQPG 3,TMUA,,,,(@)
< SQPG 4,LPBK,500,1,,(@)
< SQPG 5,STOP,,,,(@)
```

This
example combines a SmartLoop™ test with a TMU per pin
measurement.

### Example（取自子主题 Data transfer from the vector area to the data queue）

The following figure illustrates the transfer process for one pin:

Note the following points in the figure:

The example slightly deviates from the vector setup standard example.

The flattened vector instances, not the stored vectors, must be a multiple of 8. The label
has 16 active vectors, but is flattened to 22 instances. Therefore two break vector instances
are required.

### Example（取自子主题 Synchronization within sequencing groups）

The following figure illustrates the algorithm by a sequencing group consisting of two
ports:

The variables
j
,
k
,
m
,
n
, are integers.

Observe
that the synchronization is based on the simultaneous change to the new period within the CTOF
sequence which is triggered by a
CTIM
 instruction. Therefore, the user
vectors can only be synchronized exactly at the start of a functional test if a timing set is
activated before the first user vector. By default, this condition is satisfied for any
sequencing group that contains more than one port (even if the primary sets are the same as
before). But if this activation is suppressed with the
FTCG
 firmware command
(option
ON
), exact synchronization is not
possible.

The
following figure shows a "macroscopic" view of a multi-port burst for three ports that belong to
the same sequencing group:

Observe that the user vectors start synchronously not only at the start of the
testsuite, but also after the
CTIM
 instruction that occurs in the sequencer
programs of all three ports.

### Example（取自子主题 De-coupling ports by separate sequencing groups）

The following figure shows two testsuites for three ports belonging to two sequencing
groups:

Observe the following points in the figure:

The start of the user vectors in Sequencing Group 1 and Sequencing Group 2 is not
simultaneous.

In contrast to
Port A
, the two ports of sequencing group 2 contain an additional

CTIM
 instruction in the first testsuite.

Port A
 in Sequencing Group 1 waits for
Port B
 and
Port C
 in Sequencing
Group 2 to finish their user vectors before the second testsuite starts.

### Example（取自子主题 Phase synchronization across sequencing groups）

The following figure shows phase synchronization after the internal

CTIM
 at test start for the two ports of the figure in
`Synchronization within sequencing groups`（raw: `55334.htm`）
, which are now supposed to belong to different sequencing groups and to
have the
PHASE
 flag set:

j, k
,
m
,
n
,
x
,
y
 are integers.

Since the
start of the user vectors of port A is delayed by a multiple of p
B
, and
k ×

p
A
 + F
A
 +
m ×
8
 ×
p
A
 is also a multiple of
p
B
 by

k ×
p
A
 + F
A
 +
m ×
8
 ×

p
A
 =
k ×
p
B
 +
n ×
8
 ×
p
B
,

the
first user vector of port A in the figure above is still synchronous with some user vector of
port
B.

### Example（取自子主题 Defining sequencing groups）

For sequencing group definitions within a multi-port specification, see the example in

`Multi-port timing specifications`（raw: `10599.htm`）
. The same grouping could
be defined in the vector setup with the
SQLB
 command as
follows:

```
> SQLB "MP_B",MPBU,28,31,"gr1",(port1)
> SQLB "MP_B",MPBU,28,29,"gr2",(port2)
> SQLB "MP_B",MPBU,31,32,"gr2",(port3)
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
