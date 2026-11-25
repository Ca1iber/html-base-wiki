---
type: object
title: SHARING_CONFIGURATION
layer: n/a
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25_SHARING_CONFIGURATION.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# SHARING_CONFIGURATION

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **14,812 字符逐字取自** `<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25_SHARING_CONFIGURATION.htm>` 及其子主题 `<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.07.02_Sharing_configuration_file.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.01_SHARING_CONFIGURATION.getInstance.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.02_SHARING_CONFIGURATION.hasLoaded.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.03_SHARING_CONFIGURATION.load.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.04_SHARING_CONFIGURATION.setRefPin.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.05_SHARING_CONFIGURATION.getModeContext.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.06_SHARING_CONFIGURATION.isFXDLIgnorePin.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.07_SHARING_CONFIGURATION.utilitySearchFirst.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.08_SHARING_CONFIGURATION.utilitySearchNext.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.09_SHARING_CONFIGURATION.utilityActionExecute.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.10_SHARING_CONFIGURATION.utilityGetApplicableSitesString.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.11_SHARING_CONFIGURATION.utilitySubstitutePins.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.12_SHARING_CONFIGURATION.domainsGetXSize.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.13_SHARING_CONFIGURATION.domainsGetYSize.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.14_SHARING_CONFIGURATION.domainsGetZSize.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.15_SHARING_CONFIGURATION.domainsGetApplicableSitesString.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.16_SHARING_CONFIGURATION.domainsGetSiteAtPos.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.17_SHARING_CONFIGURATION.getTerminatedPinList.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.18_SHARING_CONFIGURATION.getBufferPinMap.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25.19_SHARING_CONFIGURATION.getDomain.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Class definition

### Member functions

`getInstance ()`（raw: `131631.htm`）

Data loading functions:

`hasLoaded () const`（raw: `131633.htm`）

`load (const string &config)`（raw: `131634.htm`）

`setRefPin (const string &pinName)`（raw: `131635.htm`）

Data accessing functions:

`getModeContext () const`（raw: `131644.htm`）

`isFXDLIgnorePin (const string &pinname) const`（raw: `131645.htm`）

`utilitySearchFirst (const string &name) const`（raw: `131646.htm`）

`utilitySearchNext (const string &name) const`（raw: `131647.htm`）

`utilityActionExecute (int index) const`（raw: `131650.htm`）

`utilityGetApplicableSitesString (int index) const`（raw: `131651.htm`）

`utilitySubstitutePins (int index, const string &pinsFrom, string &pinsTo) const`（raw: `131652.htm`）

`domainsGetXSize () cons`（raw: `131653.htm`）
t

`domainsGetYSize () const`（raw: `131654.htm`）

`domainsGetZSize () const`（raw: `131655.htm`）

`domainsGetApplicableSitesString (int x, int y) const`（raw: `131660.htm`）

`domainsGetSiteAtPos (int x, int y, int z) const`（raw: `131661.htm`）

`getTerminatedPinList (const string &vterm) const`（raw: `131664.htm`）

`getBufferPinMap () const`（raw: `131665.htm`）

`getDomain (int site) const`（raw: `131666.htm`）

Note
 To use the SHARING_CONFIGURATION API, you must first call getInstance().
Then you can use other member functions. See the example in
`SHARING_CONFIGURATION.getInstance()`（raw: `131631.htm`）
.

### Syntax（取自子主题 SHARING_CONFIGURATION.getInstance()）

```
static SHARING_CONFIGURATION & getInstance() [static]
```

### Example（取自子主题 SHARING_CONFIGURATION.getInstance()）

This code fragment demonstrates how to use
getInstance()
 to create
the SHARING_CONFIGURATION object for using other member
functions.

```
//You must first use getInstance() to get the only one active object of the SHARING_CONFIGURATION class.
SHARING_CONFIGURATION &sharingConfig = SHARING_CONFIGURATION::getInstance();

//Load sharing configuration file "default.cfg".
sharingConfig.load("default.cfg");
```

### Syntax（取自子主题 SHARING_CONFIGURATION.hasLoaded()）

```
bool hasLoaded() const
```

### Syntax（取自子主题 SHARING_CONFIGURATION.load()）

```
void load(const string & config)
```
[表]
列: Parameter | Description
行 1:
  config
  The name of the sharing configuration file which you want to load.
    
    The file must be located in the <device
    directory>/configuration/ directory.

### Syntax（取自子主题 SHARING_CONFIGURATION.setRefPin()）

```
void setRefPin(const string & pinName)
```
[表]
列: Parameter | Description
行 1:
  pinName
  The name of a pin whose sharing configuration information you want to load.

### Syntax（取自子主题 SHARING_CONFIGURATION.getModeContext()）

```
const string & getModeContext() const
```

### Syntax（取自子主题 SHARING_CONFIGURATION.isFXDLIgnorePin()）

```
bool isFXDLIgnorePin(const string & pinname) const
```
[表]
列: Parameter | Description
行 1:
  pinName
  The name of a pin for which you want to know whether it is ignored by the fixture
    delay settings.

### Syntax（取自子主题 SHARING_CONFIGURATION.utilitySearchFirst()）

```
int utilitySearchFirst(const string & name) const
```
[表]
列: Parameter | Description
行 1:
  name
  The name of a utility control line which you want to find in the `utility control block`（raw: `96971.htm`）.

### Syntax（取自子主题 SHARING_CONFIGURATION.utilitySearchNext）

```
int utilitySearchNext(const string & name) const
```
[表]
列: Parameter | Description
行 1:
  name
  The name of a utility control line which you want to search in the `utility control block`（raw: `96971.htm`）.

### Syntax（取自子主题 SHARING_CONFIGURATION.utilityActionExecute()）

```
int utilityActionExecute(int index) const
```
[表]
列: Parameter | Description
行 1:
  index
  The location of a utility control line within the utility_control block in the
    `Sharing configuration file`（raw: `96971.htm`）.
    
    0 represents the first line.

### Syntax（取自子主题 SHARING_CONFIGURATION.utilityGetApplicableSitesString()）

```
string utilityGetApplicableSitesString(int index) const
```
[表]
列: Parameter | Description
行 1:
  index
  The location of a utility control line within the utility_control block in the
    `Sharing configuration file`（raw: `96971.htm`）.
    
    0 represents the first line.

### Syntax（取自子主题 SHARING_CONFIGURATION.utilitySubstitutePins()）

```
void utilitySubstituePins(int index, const string & pinsFrom, string & pinsTo) const
```
[表]
列: Parameter | Description
行 1:
  index
  The location of a utility control line within the utility_control block in a `Sharing configuration file`（raw: `96971.htm`）. In this line, pins' substitutions are defined.
    
    0 represents the first line in the utility_control block.
行 2:
  pinsFrom
  The pin names which will be substituted with new names. Multiple names are
    separated with commas.
    
    Both the pin names and the new names have already been defined in the utility control
    line
行 3:
  pinsTo
  This variable stores the returned new names which replace the pin names in
    pinsFrom.
    
    The new names have already been defined in the utility control line.

### Syntax（取自子主题 SHARING_CONFIGURATION.domainsGetXSize()）

```
int domainsGetXSize() const
```

### Syntax（取自子主题 SHARING_CONFIGURATION.domainsGetYSize()）

```
int domainsGetYSize() const
```

### Syntax（取自子主题 SHARING_CONFIGURATION.domainsGetZSize()）

```
int domainsGetZSize() const
```

### Syntax（取自子主题 SHARING_CONFIGURATION.domainsGetApplicableSitesString()）

```
string domainsGetApplicableSitesString(int x, int y) const
```
[表]
列: Parameter | Description
行 1:
  x
  The position in the X dimension, starts from 0.
行 2:
  y
  The position in the Y dimension, starts from 0.

### Syntax（取自子主题 SHARING_CONFIGURATION.domainsGetSiteAtPos()）

```
int domainsGetSiteAtPos(int x, int y, int z) const
```
[表]
列: Parameter | Description
行 1:
  x
  The position in the X dimension, starts from 0.
行 2:
  y
  The position in the Y dimension, starts from 0.
行 3:
  y
  The position in the Z dimension, starts from 0.

### Syntax（取自子主题 SHARING_CONFIGURATION.getTerminatedPinList()）

```
string getTerminatedPinList(const string & vterm) const
```
[表]
列: Parameter | Description
行 1:
  vterm
  The termination pin terminates the pins you want to retrieve.

### Syntax（取自子主题 SHARING_CONFIGURATION.getBufferPinMap()）

```
const map<int, string> & getBufferPinMap() const
```

### Syntax（取自子主题 SHARING_CONFIGURATION.getDomain()）

```
vector <int> getDomain(int site) const
```
[表]
列: Parameter | Description
行 1:
  site
  The site number from which you want to get the domain.

### Syntax（取自子主题 Sharing configuration file）

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

### Example（取自子主题 Sharing configuration file）

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

**文档事实** SHARING_CONFIGURATION 类提供访问 Sharing configuration file 中所含数据的 API，可读取 pin_configuration、fixture_delay_files、domains、utility_control、topology、fxdl_ignore_pins、groups、rss_buffer_pins 等配置。

**文档事实** 该 API 仅适用于 MTP；定义在 `/opt/93000mts/mts/solution_tools/import/SHARING_CONFIGURATION.h`。

**文档事实** 使用前必须先调用 `getInstance()` 取得该类唯一的活动对象，之后才能调用其他成员函数。

**文档事实** 成员函数分为数据加载类（`hasLoaded()`、`load()`、`setRefPin()`）与数据访问类（`getModeContext()`、`isFXDLIgnorePin()`、`utility*`、`domains*`、`getTerminatedPinList()`、`getBufferPinMap()`、`getDomain()`）。

## 典型用法

**文档事实** 先以 `SHARING_CONFIGURATION &sharingConfig = SHARING_CONFIGURATION::getInstance();` 取得对象，再调用 `sharingConfig.load("default.cfg");`；`load()` 的文件必须位于 `<device directory>/configuration/` 目录。

**文档事实** 也可用 `setRefPin(pinName)` 从指定 pin 的物理连接加载 sharing configuration 信息；`hasLoaded()` 可判断是否已有配置被加载。

**文档事实** utility 控制相关流程为：`utilitySearchFirst(name)` / `utilitySearchNext(name)` 定位 utility_control 块中的控制行，`utilityActionExecute(index)` 执行该行设置，`utilityGetApplicableSitesString(index)` 取得适用 site，`utilitySubstitutePins(index, pinsFrom, pinsTo)` 取得替换后的 pin 名。

**文档事实** domains 相关访问包括 `domainsGetXSize()`/`domainsGetYSize()`/`domainsGetZSize()` 查询尺寸，`domainsGetApplicableSitesString(x, y)` 查询指定 (x, y) 的适用 site，`domainsGetSiteAtPos(x, y, z)` 与 `getDomain(site)` 分别做位置到 site、site 到 domain 的查询。

**文档事实** 还可用 `getTerminatedPinList(vterm)` 取得由指定 termination pin 端接的 pin 列表，用 `getBufferPinMap()` 取得 buffer pin 映射。

## 和谁有关

- Sharing configuration file：**文档事实** 本页首段说明该类就是用于访问该文件中的数据；其 `load()` 文件位于 device 目录的 configuration 子目录。
- MTP_IDD_TASK：**文档事实** 该 API 文档把 SHARING_CONFIGURATION 列为完成 IDD 测试所需的 API 之一。
- MTP_LEAKAGE_TASK：**文档事实** 该 API 文档把 SHARING_CONFIGURATION 列为完成 shared leakage 测试所需的 API 之一。
- Driver Sharing APIs：**文档事实** 该页在"在一个 test method 内测试任意数量 pin"的类列表中列出 SHARING_CONFIGURATION。
- fd_merge.pl / OnlineCompensation：**文档事实** Sharing configuration file 的 `fxdl_ignore_pins` 关键字说明这些 pin 会被这两个工具忽略；`isFXDLIgnorePin()` 用于查询该忽略列表。
- `getInstance()`：**文档事实** 本页 Note 要求先调用它，其子主题给出取得唯一活动对象的示例。

## 版本

**文档事实** Introduced in MTP 3.1.5（本页及各成员函数子主题的 `Functional changes` 均为该值）。

## 出处

- `02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.25_SHARING_CONFIGURATION.htm`
- `02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.07.02_Sharing_configuration_file.htm`（文件格式与关键字）
- `02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.13_MTP_IDD_TASK.htm`（关系核对）
- `02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.14_MTP_LEAKAGE_TASK.htm`（关系核对）
- `02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.02.05.06.07.09.03_Driver_Sharing_APIs.htm`（关系核对）
