---
type: object
title: Sharing configuration file
layer: file
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.07.02_Sharing_configuration_file.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Sharing configuration file

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **9,720 字符逐字取自** `<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.07.02_Sharing_configuration_file.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

The format of the sharing configuration file, using the keywords described
below:

```
pin_configuration:
<pin config file name><context>

fixture_delay_files:
[+<baseboard fixture delay file>]
<fixture delay file> # position x=0,y=0
<fixture delay file> # position x=1,y=0
...
[; # starts next increment of y value
<fixture delay file> # position x=0,y=1
<fixture delay file> # position x=1,y=1
...]
...

domains:
<site number><site number> ...[; <site number><site number> ... ] ... # for z=0
... # for increments of z

[utility_control:
<name>[; (<equation>)] ; (<utility setting>) [; (<pin substitution>)]
...]

topology:
<topo definition> ; <pin group>
...

[fxdl_ignore_pins:
<pin>[, <pin>...] ]

[groups:
<pins or channels> ; offset=<group offset>
...]

[rss_buffer_pins:
<site no>; [<tmp src buffer>], <source buffer>, <global buffer 1>, <global buffer 2> [; ...]
...]
```

Note
that # indicates comments that are not part of the syntax but serve to explain the
semantics.

[表] Keywords
列: | Field | Type | Description
行 1:
  pin_configuration [跨 2 行]
  <pin config file>
  String
  Name of the V93000 pin configuration file used to calculate fixture
    delay.
    
    This pin configuration file is normally identical to the standard pin configuration file.
    You must, however, remove all shared pins from it that are not part of the daisy chain.
行 2:
  <context>
  String
  The context name in the pin configuration file, for example FAST.
行 3:
  fixture_delay_files
  <baseboard fixture delay file>
  String
  The name of the fixture delay file for the baseboard.
    
    The fixture delays in this file must be measured between lower pogo and upper pogo.
    
    This is an optional parameter. It must be prefixed with a plus sign (+).
行 4:
  
  <fixture delay file>
  String
  Fixture delay file names, separated by line breaks.
    
    If a baseboard fixture delay file has been specified (see above), the measurements in
    these files must be from upper pogo to socket pin. If there is no baseboard file, the
    measurements in these files must be from lower pogo to socket pin.
    
    There must be one file for each device. Files must be listed in the order of the devices
    - first the file for the device at the x0,y0 location, then for x1,y0, then x2,y0 etc. When
    files for all devices with a y0 coordinate have been listed, add a semicolon and list all
    devices with a y1 coordinate (x0,y1 x1y1, ...), then for y2 and so on.
    
    For information on determining the coordinates of a device, see `Identifying sites`（raw: `120819.htm`）.
行 5:
  domains
  <site number>
  Integer
  A site number.
    
    The domains keyword is followed by the sites each pin drives.:
    Sites for one pin must
    be listed on one line in the order of the signal propagation.
    
    Different Y-branches driven by the same pin are separated by semicolons.
    
    Sites are numbered according to their coordinates: x0,y0 is numbered 1, x1,y1 is
    numbered 2, and so on.
    
    For information on determining the coordinates of a device, see `Identifying sites`（raw: `120819.htm`）.
行 6:
  utility_control
  <name>
  String
  The entire utility control block is required only for DPS shared load boards and
    can otherwise be omitted.
    
    Each entry in this section specifies the utility line settings to apply before a
    particular test method is executed.
    
    <name> is the name of a utility control.
    
    Different test methods may use different names. The name "default" is used by all test
    methods to specify the default utility line settings.
    
    For details, see the description of the test method you will be using.
行 7:
  
  <equation>
  String
  This is an optional parameter.
    
    It specifies a condition that must be true in order to apply the action described in that
    line.
    
    Conditions can include values and operators.
    
    Supported values are:
    
    Decimal numbers (for example, 123)
    
    Hexadecimal numbers (for example, 0xff)
    
    The variables x and y. They evaluate to the respective coordinate of a site. For
    example, x < 5 is true for all sites with an x-coordinate from 0 to
    4.
    For information on determining the coordinates of a device, see `Identifying sites`（raw: `120819.htm`）.
    
    Supported operators include:
    
    ==
    
    <
    
    <=
    
    >
    
    >=
    
    &&
    
    ||
    
    Four forms of equations are supported:
    
    <value><op><value>. For example: x >
    2
    
    <value><op><value><op><value>. For
    example: 0x77 < x <= 0xff
    
    (<value><op><value>) <op>
    (<value><op><value>). For example: (x <
    5) && (y > 2)
行 8:
  
  <utility setting>
  String
  The utility setting is a list of comma-separated commands that are executed when
    the equation evaluates to true. If there is no equation, the commands are always
    executed.
    
    Parameters can be specified with or without a mask:
    
    Without mask: For example, U5=0x400. A mask of 0xffff in implicitly
    applied.
    
    With a mask: For example, U5=0x400&0xf00.
行 9:
  
  <pin substitution>
  String
  A comma-separated list of assignments of device pin names to pin aliases
    from the test method. For example: DEVICE_SUPPLY=VDD
    
    Which pin aliases are available (here: DEVICE_SUPPLY) depends on the test method.
行 10:
  topology
  <topo definition>
  String
  A specification of the sharing topology used.
    
    Topology definitions have three elements:
    
    x=n, where n is the x-dimension
    of the sharing setup.
    
    y=n, where n is the
    y-dimension.
    
    The type of termination:
    
    noterm: no termination
    
    cross: cross-termination
    
    actterm=<pin>: active
    termination, where <pin> is the termination pin
行 11:
  
  <pin group>
  String
  The pin group in which the pins have this topology.
行 12:
  fxdl_ignore_pins
  <pin>
  String
  A pin that will be ignored by fd_merge.pl and OnlineCompensation.
    
    In other words, these tools will not calculate additional compensation for the pin.
    
    You can specify multiple pins; separate them by commas.
行 13:
  groups
  <pins or channels>
  String
  A specification either of one or more tester channels or of one or more
    pins or pin groups to which the offset is applied.
    
    You can specify:
    
    A single tester channel. For example: 22601
    
    Multiple tester channels separated by commas. For example: 22601, 22603,
    22605
    
    A range of tester channels indicated by a dash. For example:
    22601-22604
    
    A pin or pin group. For example: A1
    
    Multiple pins or pin groups. For example: A1, A3, DQo
    
    Channels, pins and pin groups can be mixed in the same specification, for example:
    A1, DQo, 22601
行 14:
  
  <group offset>
  Double
  The offset that is added to every specified pin or channel. The unit is
    nanoseconds (ns).
    
    The offset can be a positive or negative number, and it can be an integer or a decimal
    fraction. These are all valid values: 3, -3, 2.5, -2.5
行 15:
  rss_buffer_pins
  <site no>; [<tmp src
    buffer>], <source buffer>, <global
    buffer 1>, <global buffer 2>
  String
  The site or sites for which you specify the rapid source sync buffer
    pins.
    
    You can specify:
    
    A single site by providing the number of the site, for example, 3.
    
    Multiple sites by providing their numbers in a comma-separated list, for example, 3, 5,
    7.
    
    A range of sites using a dash, for example, 3-6.
    
    The site specification is followed by the buffer specification (described below).
    There can either be one buffer specification or different buffer specifications for
    multiple domains in the site. If there are multiple specification for different domains,
    they must be separated by semicolons.
    
    Note that sites 241-256 are not available for rapid source sync.
    
    Also note that any buffer pin specification in the BufferPins test
    method parameter overrides this setting in the sharing configuration file.
行 16:
  
  <tmp src buffer>
  String
  A temporary source buffer pin.
    
    This is an optional parameter: If only three pins are listed, it is assumed that no
    temporary source buffer is specified. If four pins are listed, the first is the temporary
    source buffer.
行 17:
  
  <source buffer>
  String
  The source buffer pin.
行 18:
  
  <global buffer 1>
  String
  The first global buffer pin.
行 19:
  
  <global buffer 2>
  String
  The second global buffer pin.

### Example

This sample file works for a 4,2,2 structure; that is, a topology that can has daisy
chains with up to four sites, up to two daisy chains connected to one driver pin, and repeats
this structure over two
domains.

```
pin_configuration:
./128Mx8_Moscato4.pin_forFXDL

fixture_delay_files:
./TSE_FXDL/Y2/FXDL1.txt
./TSE_FXDL/Y2/FXDL2.txt
./TSE_FXDL/Y2/FXDL3.txt
./TSE_FXDL/Y2/FXDL4.txt
;
./TSE_FXDL/Y2/FXDL5.txt
./TSE_FXDL/Y2/FXDL6.txt
./TSE_FXDL/Y2/FXDL7.txt
./TSE_FXDL/Y2/FXDL8.txt

domains:
1 2 3 4; 5 6 7 8
9 10 11 12; 13 14 15 16

utility_control:
idd; (y<=0); (U7=0x222&0xfff); (DEVICE_SUPPLY=VDD)
idd; (y>=1); (U7=0x111&0xfff); (DEVICE_SUPPLY=VDD)
iddq; (y<1); (U7=0x777&0xfff); (DEVICE_SUPPLY=VDD)
iddq; (y>=1); (U7=0xbbb); (DEVICE_SUPPLY=VDD)
leakage; (U5=0x001&0x001)
oc_reset; (U5=0x000&0x400,U5=0x400&0x400,U7=0x000&0xfff,U5=0x000&0x400)
default; (U7=0x000,U5=0x000&0x401)

topology:
x=4,y=2, actterm=VTERM ; SharedGrp
x=4,y=2, cross ; CrossTermGrp

fxdl_ignore_pins:
A3, A4

groups:
22601, 22602 ; offset=3
22701-22716 ; offset=-4
A0, A1 ; offset=4.7

rss_buffer_pins:
1,3,5,7; A.00, A.01, A.02
2,4,8,9; A.03, A.04, A.05
```

<!-- 语法节 end -->

## 是什么

**文档事实**：sharing configuration file 定义 load board 的 sharing 结构，被所有 sharing test methods 以及 `fd_merge` 工具使用（`02.12.02.05.06.07.07.02` 首段）。

**文档事实**：它包含的信息是：pins 的物理设置、fixture delay 文件名、每条 chain 的 site 数、y-shared pins 或 chains 的数量、每条 chain 上 site 的顺序，以及可选的 rapid source sync buffer pins（同页首段）。

**文档事实**：文件必须存放在当前 device 的 `configuration` 目录下（同页首段）。

**文档事实**：关键字共八组：`pin_configuration`（pin config file + context）、`fixture_delay_files`、`domains`、`utility_control`、`topology`、`fxdl_ignore_pins`、`groups`、`rss_buffer_pins`；语法模板中 `utility_control`、`fxdl_ignore_pins`、`groups`、`rss_buffer_pins` 标为可选（同页 Syntax 与 Keywords 表）。

**文档事实**：`pin_configuration` 指定的 pin configuration file 用于计算 fixture delay，必须移除不属于 daisy chain 的 shared pins；`utility_control` 只有 DPS shared load boards 必需，其他情况可省略（同页 Keywords 表）。

**推断**：因为 test method 与 `fd_merge`/`OnlineCompensation` 都读同一个文件，它实际上是 load board 共享拓扑（site 链、fixture delay、utility line、buffer pin）的单一描述源；改拓扑会同时影响测试执行与 fixture delay 补偿（依据：首段「used by all sharing test methods as well as the fd_merge tool」及 `fxdl_ignore_pins` 说明）。

## 典型用法

**文档事实**：一个可用的样例是 4,2,2 结构（每条 daisy chain 最多 4 sites、每个 driver pin 最多接 2 条 daisy chain、重复 2 个 domain），节选如下（同页 Example）：

```text
pin_configuration:
./128Mx8_Moscato4.pin_forFXDL

fixture_delay_files:
./TSE_FXDL/Y2/FXDL1.txt
./TSE_FXDL/Y2/FXDL2.txt
;
./TSE_FXDL/Y2/FXDL5.txt
./TSE_FXDL/Y2/FXDL6.txt

domains:
1 2 3 4; 5 6 7 8
9 10 11 12; 13 14 15 16

topology:
x=4,y=2, actterm=VTERM ; SharedGrp
x=4,y=2, cross ; CrossTermGrp
```

**文档事实**：`fixture_delay_files` 每行一个 device 的 fixture delay 文件，按 x0,y0、x1,y0…… 排；y 增加时用分号换行。有 baseboard file 时测量范围是 upper pogo→socket pin，无 baseboard 时是 lower pogo→socket pin，baseboard 文件必须以 `+` 前缀给出（同页 Keywords 表）。

**文档事实**：`utility_control` 的行用 `name; (equation); (utility setting); (pin substitution)` 形式；equation 可用 x/y 坐标比较（例如 `x < 5`）；utility setting 可带或不带 mask；名称 `default` 由所有 test methods 使用（同页 Keywords 表与 Example）。

**文档事实**：在 test method 里由 `sharingConfigFile()` 指定该文件；`SHARED_IDD_TEST`、`SHARED_LEAKAGE_PARALLEL_TEST`、`SHARED_VBUMP_TEST`、`SHARED_CONTINUITY_TEST`、`SOURCESYNC_TEST` 都有这个成员，文件应位于 `<device directory>/configuration/`（入边语境，`02.12.06.22.02` 等）；`fd_merge` 也以该文件为输入（`02.12.02.05.06.07.07.03` 入边语境）。

**文档事实**：`rss_buffer_pins` 指定 rapid source sync 的临时/源/全局 buffer pin；sites 241–256 不可用于 rapid source sync，且 test method 的 `BufferPins` 参数会覆盖此设置（同页 Keywords 表）。

**建议**：先用样例文件改出 4,2,2 的骨架，再按实际 fixture 的 FXDL 文件顺序与 `domains` 填写；文档把「参考样例文件创建」列为创建方式（`02.12.02.05.06.07.07.03` 入边语境），但未规定必须逐字段从零编写。

## 和谁有关

- **SHARING_CONFIGURATION** — **文档事实**：该类「provides an API for accessing the data contained in the Sharing configuration file」，其 `load()` 读 device 目录的 configuration 子目录（`02.12.06.25` 入边语境；同目录对象页 `sharing-configuration`）。
- **SHARED_IDD_TEST / SHARED_LEAKAGE_PARALLEL_TEST / SHARED_VBUMP_TEST / SHARED_CONTINUITY_TEST / SOURCESYNC_TEST** — **文档事实**：这些 test method 的 `sharingConfigFile()` 用来指定本文件，文件须在 `<device directory>/configuration/`（`02.12.06.22.02`、`.23.02`、`.24.02`、`.21.02`、`.29.11` 入边语境）。
- **fd_merge tool / fd_merge.pl** — **文档事实**：`fd_merge` 以本文件为输入合并 fixture delay 文件；`fxdl_ignore_pins` 中的 pin 会被 `fd_merge.pl` 和 `OnlineCompensation` 忽略（`02.12.02.05.06.07.07.06`、`.06.01`、`.03` 入边语境；本页 Keywords 表）。
- **Fixture delay measurement on shared drivers / Measuring fixture delay** — **文档事实**：这些主题要求准备本文件，并在 `fixture_delay_files` 中引用 FXDL 文件（`02.12.02.05.06.07.07`、`.05`、`.05.01` 入边语境）。
- **Pin configuration file / context（如 `FAST`）** — **文档事实**：`pin_configuration` 行同时给出 pin config file 名与 context 名（本页 Keywords 表）。
- **FOR_EACH_TEST_BEGIN / FOR_EACH_TEST_BEGIN_WITH_RESET / GET_CURRENT_UTILITY_CONTROL** — **文档事实**：shared sites 按本文件 `utility_control` 设置分组；`GET_CURRENT_UTILITY_CONTROL` 读取当前 utility control（`02.12.06.04`、`.05`、`.07` 入边语境）。
- **MTP_CONTINUITY_TASK / MTP_LEAKAGE_TASK** — **文档事实**：两者的 `postExecute()` 会恢复本文件中指定的设置（`02.12.06.10.05`、`.14.05` 入边语境）。
- **SharedIDD / SharedLeakageParallel / SharedVBump / SharedContinuity 语法页** — **文档事实**：这些语法页把本文件作为 `utility_control` / buffer pin 细节的出处（`02.12.02.05.06.07.09.14`、`.11`、`.16`、`.09` 入边语境）。
- **DPS Sharing Diagnostic / Diagnostic configuration file** — **文档事实**：DPS Sharing Diagnostic 要求本文件定义 `oc_reset`、`default`、`idd` 等 utility control 与 `actterm` topology；Diagnostic configuration file 沿用同样的 utility control 语法（`02.12.04.07.01`、`.03` 入边语境）。

## 版本

**文档事实**（`02.12.02.05.06.07.07.02` 的 Functional changes）：

- Introduced before SmarTest 6.3.2（哨兵值：表示文档集覆盖起始之前已存在，不是 6.3.2 的变更）
- MTP 3.0.1：引入全新语法以支持 Y sharing 与 hybrid sharing。
- MTP 3.0.3（MTP on SOC 103.0.0）：新增 rapid source sync buffer pins 段。

除此之外没有更细的版本变更记录；更早版本情况文档未覆盖。

## 出处

- `02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.07.02_Sharing_configuration_file.htm`（主文档，含 Syntax、Example 与 Functional changes）
- `02.12.06.25_SHARING_CONFIGURATION.htm` 及其 `utilitySearchFirst/Next()`、`utilityActionExecute()`、`utilityGetApplicableSitesString()`、`utilitySubstitutePins()`、`getTerminatedPinList()` 子主题
- `02.12.06.21.02`、`02.12.06.22.02`、`02.12.06.23.02`、`02.12.06.24.02`、`02.12.06.29.11`（各 `sharingConfigFile()` 子主题）
- `02.12.02.05.06.07.07.03_Creating_a_sharing_configuration_file.htm`、`02.12.02.05.06.07.07.05_Fixture_delay_compensation_process.htm`、`02.12.02.05.06.07.07.06_Fd_merge_tool.htm`
- `02.12.04.07.01_Using_DPS_Sharing_Diagnostic.htm`、`02.12.04.07.03_Diagnostic_configuration_file.htm`
