---
type: object
title: DIGITAL_OFFSET_SEARCH_PINS
layer: L2
stage: pattern
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.36.01_DIGITAL_OFFSET_SEARCH_PINS.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# DIGITAL_OFFSET_SEARCH_PINS

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **42,930 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.36.01_DIGITAL_OFFSET_SEARCH_PINS.htm>` 及其子主题 `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.240_TASK_LIST.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.36.01.01_DIGITAL_OFFSET_SEARCH_PINS.errorCountLimit.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.36.01.02_DIGITAL_OFFSET_SEARCH_PINS.enableFastStop.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.36.01.03_DIGITAL_OFFSET_SEARCH_PINS.execute.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.36.01.04_DIGITAL_OFFSET_SEARCH_PINS.getConfiguration.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.36.01.05_DIGITAL_OFFSET_SEARCH_PINS.getExecutionContext.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.36.01.06_DIGITAL_OFFSET_SEARCH_PINS.getLatestLBTransitionOffset.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.36.01.07_DIGITAL_OFFSET_SEARCH_PINS.getLatestRBTransitionOffset.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.36.01.08_DIGITAL_OFFSET_SEARCH_PINS.getOffset.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.36.01.09_DIGITAL_OFFSET_SEARCH_PINS.getStatus.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.36.01.10_DIGITAL_OFFSET_SEARCH_PINS.minPassCount.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.36.01.11_DIGITAL_OFFSET_SEARCH_PINS.minStableErrorCount.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.36.01.12_DIGITAL_OFFSET_SEARCH_PINS.numSteps.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.36.01.13_DIGITAL_OFFSET_SEARCH_PINS.DigitalOffsetResultCopy.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.36.01.14_DIGITAL_OFFSET_SEARCH_PINS.DigitalOffsetResultReset.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.36.01.15_DIGITAL_OFFSET_SEARCH_PINS.remove.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.36.01.16_DIGITAL_OFFSET_SEARCH_PINS.resolution.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.36.01.17_DIGITAL_OFFSET_SEARCH_PINS.resolutionHistogramSearch.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.36.01.18_DIGITAL_OFFSET_SEARCH_PINS.resourceType.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.36.01.19_DIGITAL_OFFSET_SEARCH_PINS.restoreFlag.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.36.01.20_DIGITAL_OFFSET_SEARCH_PINS.search.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.36.01.21_DIGITAL_OFFSET_SEARCH_PINS.searchType.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.36.01.22_DIGITAL_OFFSET_SEARCH_PINS.setConfiguration.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.36.01.23_DIGITAL_OFFSET_SEARCH_PINS.setExecutionContext.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.36.01.24_DIGITAL_OFFSET_SEARCH_PINS.setup.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.36.01.25_DIGITAL_OFFSET_SEARCH_PINS.start.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.36.01.26_DIGITAL_OFFSET_SEARCH_PINS.stepWidth.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.36.01.27_DIGITAL_OFFSET_SEARCH_PINS.transitionDetection.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.36.01.28_DIGITAL_OFFSET_SEARCH_PINS.TransitionOffsetFound.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.36.01.29_DIGITAL_OFFSET_SEARCH_PINS.uploadLatestTransition.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.36.01.30_DIGITAL_OFFSET_SEARCH_PINS.uploadOffset.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.36.01.31_DIGITAL_OFFSET_SEARCH_PINS.uploadResult.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.36.02_DIGITAL_OFFSET_SEARCH_RESULT_PINS.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.36.03_DIGITAL_OFFSET_SEARCH_TASK.pin.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.36.04_DIGITAL_OFFSET_SEARCH_TASK.resultPin.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.36.05_DIGITAL_OFFSET_SEARCH_TASK.setExecutionContext.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.36.06_DIGITAL_OFFSET_SEARCH_TASK.print.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.36.07_DIGITAL_OFFSET_SEARCH_TASK.enableAutoOffsetUpload.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.36.08_DIGITAL_OFFSET_SEARCH_TASK.enableAutoTransitionUpload.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.36.09_DIGITAL_OFFSET_SEARCH_TASK.enableAutoResultsUpload.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.36.10_DIGITAL_OFFSET_SEARCH_TASK.setup.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.36.11_DIGITAL_OFFSET_SEARCH_TASK.execute.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.36.12_DIGITAL_OFFSET_SEARCH_TASK.remove.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.36.13_DIGITAL_OFFSET_SEARCH_TASK.getStatus.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.36.14_DIGITAL_OFFSET_SEARCH_TASK.getExecutionContext.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.36.15_DIGITAL_OFFSET_SEARCH_TASK.uploadLatestTransition.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.36.16_DIGITAL_OFFSET_SEARCH_TASK.uploadOffset.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.36.17_DIGITAL_OFFSET_SEARCH_TASK.uploadResult.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.36_DIGITAL_OFFSET_SEARCH_TASK.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

This class has no constructor.

List of parameters

There are no parameters.

Return value

There is no return value.

### Syntax（取自子主题 DIGITAL_OFFSET_SEARCH_PINS.errorCountLimit()）

```
DIGITAL_OFFSET_SEARCH_PINS& errorCountLimit(INT errorcountlimit);
```
[表] Parameter
列: Parameter | Description
行 1:
  errorcountlimit
  A number used as an error count limit. The default number is 1.
    
    If an error count of a test is greater than this limit, the test is considered fail.

### Return value（取自子主题 DIGITAL_OFFSET_SEARCH_PINS.errorCountLimit()）

A reference to the
`DIGITAL_OFFSET_SEARCH_PINS`（raw: `140966.htm`）

object.

### Syntax（取自子主题 DIGITAL_OFFSET_SEARCH_PINS.enableFastStop()）

```
void DIGITAL_OFFSET_SEARCH_PINS& enableFastStop(status);
```
[表] Parameter
列: Parameter | Description
行 1:
  status
  TRUE or FALSE to enable or disable the
    FASTSTOP mode.
    
    When FALSE, the standard search mode that returns the largest pass
    area is used.

### Return value（取自子主题 DIGITAL_OFFSET_SEARCH_PINS.enableFastStop()）

A reference to the
`DIGITAL_OFFSET_SEARCH_PINS`（raw: `140966.htm`）

object.

### Syntax（取自子主题 DIGITAL_OFFSET_SEARCH_PINS.execute()）

```
void execute();
```

Return value

There is no return value.

### Syntax（取自子主题 DIGITAL_OFFSET_SEARCH_PINS.getConfiguration()）

```
void getConfiguration(DIGITAL_OFFSET_SEARCH::DigitalOffsetSearchConfigDataType & configdata);
```
[表] Parameter
列: Parameter | Description
行 1:
  configdata
  A data used for storing the retrieved configurations, such as search type, resource
    type, start value, and stop value. See more data type in `DigitalOffsetSearchConfigDataType`（raw: `141168.htm`）.

Return value

There is no return value.

### Syntax（取自子主题 DIGITAL_OFFSET_SEARCH_PINS.getExecutionContext()）

```
const STRING& getExecutionContext();
```

List of parameters

There are no parameters.

### Return value（取自子主题 DIGITAL_OFFSET_SEARCH_PINS.getExecutionContext()）

Returns a context name, or an empty string if no context
execution had been referenced.

### Syntax（取自子主题 DIGITAL_OFFSET_SEARCH_PINS.getLatestLBTransitionOffset()）

```
DOUBLE getLatestLBTransitionOffset();
```

### Return value（取自子主题 DIGITAL_OFFSET_SEARCH_PINS.getLatestLBTransitionOffset()）

Returns the offset at the left boundary of the pass area
found in the latest transition search:

For timing offset searches, the units of the returned values are [s].

For level offset searches, the units of the returned values are [V].

If the offset search had been applied on multiple pins, this function only returns the
largest offset among these pins' in order to form the smallest eye (a pass area).

### Syntax（取自子主题 DIGITAL_OFFSET_SEARCH_PINS.getLatestRBTransitionOffset()）

```
DOUBLE getLatestRBTransitionOffset();
```

### Parameter（取自子主题 DIGITAL_OFFSET_SEARCH_PINS.getLatestRBTransitionOffset()）

There is no parameter.

### Return value（取自子主题 DIGITAL_OFFSET_SEARCH_PINS.getLatestRBTransitionOffset()）

Returns the offset at the right boundary of the pass area in
the latest transition search:

For timing offset searches, the units of the returned values are [s].

For level offset searches, the units of the returned values are [V].

If the offset search had been applied on multiple pins, this function only returns the
smallest offset among these pins' in order to form the smallest eye (a pass area).

### Syntax（取自子主题 DIGITAL_OFFSET_SEARCH_PINS.getOffset()）

```
DOUBLE getOffset(SetSelector& selector, RESOURCE_TYPE resource) throws TMException;
```
[表] Parameters
列: Parameter | Description
行 1:
  selector
  It can be:
    
    A TimingSetSelector object defined with `TimingSetSelector`（raw: `141248.htm`）, specifies the timing
    sets. Or,
    
    A LevelSetSelector object defined with `LevelSetSelector`（raw: `141182.htm`）, specifies the level
    sets.
行 2:
  resource
  It can be a timing resource or a level resource whose offset you want to get.
    Choose a timing or level resource for the timing or level selector respectively. Otherwise,
    an exception will be thrown.
    
    For the resource types, see the following table.
[表] Available options of parameter: <resource>
列: Option | Description
行 1:
  DIGITAL_OFFSET_SEARCH::RECEIVE
  Receive edges
行 2:
  DIGITAL_OFFSET_SEARCH::FAST_DRIVE
  Fast drive edges
行 3:
  DIGITAL_OFFSET_SEARCH::SLOW_DRIVE
  Slow drive edges
行 4:
  DIGITAL_OFFSET_SEARCH::VIH
  High driver levels
行 5:
  DIGITAL_OFFSET_SEARCH::VIL
  Low driver levels
行 6:
  DIGITAL_OFFSET_SEARCH::VOH
  High receiver levels
行 7:
  DIGITAL_OFFSET_SEARCH::VOL
  Low receiver levels

Note
 On PS1600 cards both
DIGITAL_OFFSET_SEARCH::VOH
 and

 DIGITAL_OFFSET_SEARCH::VOL
 are supported for retrieving the level
offsets.

### Return value（取自子主题 DIGITAL_OFFSET_SEARCH_PINS.getOffset()）

A reference to the
`DIGITAL_OFFSET_SEARCH_PINS`（raw: `140966.htm`）

object.

### Example（取自子主题 DIGITAL_OFFSET_SEARCH_PINS.getOffset()）

Do a VIH search with a positive step width. The search will start from Fail until
Pass, intending to do a left (or lower) boundary search. The setup and result pins are the same.
Set the RestoreFlag to
NO.

```
STRING strpins("PS1600_pin_1");

DIGITAL_OFFSET_SEARCH_TASK dos;

dos.pin(strpins)
.resourceType(DIGITAL_OFFSET_SEARCH::VIH)
.searchType(DIGITAL_OFFSET_SEARCH::RB)
.start(15 mV)
.numSteps(120)
.stepWidth(15 mV)
.restoreFlag(DIGITAL_OFFSET_SEARCH::NO);

dos.execute();

DIGITAL_OFFSET_SEARCH::LevelSetSelector dest(101001);

dos.pin(strpins).uploadOffset(dest, DIGITAL_OFFSET_SEARCH::VIH);

DOUBLE offset;

offset = dos.pin(strpins).getOffset(dest, DIGITAL_OFFSET_SEARCH::VIH);
```

### Syntax（取自子主题 DIGITAL_OFFSET_SEARCH_PINS.getStatus()）

```
DIGITAL_OFFSET_SEARCH::STATUS_TYPE getStatus();
```

List of parameters

There are no parameters.

### Return value（取自子主题 DIGITAL_OFFSET_SEARCH_PINS.getStatus()）

Returns the execution status for all of the sites under
test, which can be
SUCCESS
,
FAILED
,

ABORTED
 or
NOT_EXECUTE
.

### Syntax（取自子主题 DIGITAL_OFFSET_SEARCH_PINS.minPassCount()）

```
DIGITAL_OFFSET_SEARCH_PINS& minPassCount(INT minpasscount);
```
[表] Parameter
列: Parameter | Description
行 1:
  minpasscount
  A number used as the minimum consecutive pass count to stop a binary search.
    
    When a consecutive pass count is larger than or equal to the minimum count, the binary
    search stops.

### Return value（取自子主题 DIGITAL_OFFSET_SEARCH_PINS.minPassCount()）

A reference to the
`DIGITAL_OFFSET_SEARCH_PINS`（raw: `140966.htm`）

object.

### Syntax（取自子主题 DIGITAL_OFFSET_SEARCH_PINS.minStableErrorCount()）

```
DIGITAL_OFFSET_SEARCH_PINS& minStableErrorCount(INT minStableErrCount);
```
[表] Parameter
列: Parameter | Description
行 1:
  minStableErrCount
  A number used to define the minimum number of adjacent tests that have the same
    number of errors.

### Return value（取自子主题 DIGITAL_OFFSET_SEARCH_PINS.minStableErrorCount()）

A reference to the
`DIGITAL_OFFSET_SEARCH_PINS`（raw: `140966.htm`）

object.

### Syntax（取自子主题 DIGITAL_OFFSET_SEARCH_PINS.numSteps()）

```
DIGITAL_OFFSET_SEARCH_PINS& numSteps(INT numstep);
```
[表] Parameter
列: Parameter | Description
行 1:
  numstep
  The number of search steps excluding the start value.

### Return value（取自子主题 DIGITAL_OFFSET_SEARCH_PINS.numSteps()）

A reference to the
`DIGITAL_OFFSET_SEARCH_PINS`（raw: `140966.htm`）

object.

### Syntax（取自子主题 DIGITAL_OFFSET_SEARCH_PINS.DigitalOffsetResultCopy()）

```
void DigitalOffsetResultCopy(DIGITAL_OFFSET_SEARCH::SetSelector &source, DIGITAL_OFFSET_SEARCH::SetSelector &dest);
```
[表] Parameters
列: Parameter | Description
行 1:
  source
  The source timing set specified with an object of the `TimingSetSelector`（raw: `141248.htm`）
    class.
    
    Or,
    
    The source level set specified with an object of the `LevelSetSelector`（raw: `141182.htm`） class.
行 2:
  dest
  The destination timing set specified with an object of the `TimingSetSelector`（raw: `141248.htm`）
    class.
    
    Or,
    
    The destination level set specified with an object of the `LevelSetSelector`（raw: `141182.htm`）
    class.

Return value

There is no return value.

### Example（取自子主题 DIGITAL_OFFSET_SEARCH_PINS.DigitalOffsetResultCopy()）

```
DIGITAL_OFFSET_SEARCH::LevelSetSelector sour();
DIGITAL_OFFSET_SEARCH::LevelSetSelector dest(102003);
STRING strpins("pcie_rx1n");
DIGITAL_OFFSET_SEARCH_TASK dos;

dos.pin(strpins)
.resourceType(DIGITAL_OFFSET_SEARCH::VIH)
.searchType(DIGITAL_OFFSET_SEARCH::EYE)
.start(15 mV).numSteps(120).stepWidth(15 mV)
.restoreFlag(DIGITAL_OFFSET_SEARCH::NO);

dos.execute();

dos.pin(strpins).DigitalOffsetResultCopy(sour, dest);
```

### Syntax（取自子主题 DIGITAL_OFFSET_SEARCH_PINS.DigitalOffsetResultReset()）

```
void DigitalOffsetResultReset (DIGITAL_OFFSET_SEARCH::SetSelector & selector);
```
[表] Parameter
列: Parameter | Description
行 1:
  selector
  It can be:
    
    A TimingSetSelector object defined with `TimingSetSelector`（raw: `141248.htm`）, selects timing sets.
    Or,
    
    A LevelSetSelector object defined with `LevelSetSelector`（raw: `141182.htm`）, selects level
    sets.

Return value

There is no return value.

### Syntax（取自子主题 DIGITAL_OFFSET_SEARCH_PINS.remove()）

```
void remove() const;
```

List of parameters

There are no parameters.

Return value

There is no return value.

### Syntax（取自子主题 DIGITAL_OFFSET_SEARCH_PINS.resolution()）

```
DIGITAL_OFFSET_SEARCH_PINS& resolution(DOUBLE res);
```
[表] Parameter
列: Parameter | Description
行 1:
  res
  The resolution of the binary search.
    
    For timing searches, the unit is seconds [s].
    
    For voltage searches, the unit is Volts [V].

### Return value（取自子主题 DIGITAL_OFFSET_SEARCH_PINS.resolution()）

A reference to the
`DIGITAL_OFFSET_SEARCH_PINS`（raw: `140966.htm`）

object.

### Syntax（取自子主题 DIGITAL_OFFSET_SEARCH_PINS.resolutionHistogramSearch()）

```
DIGITAL_OFFSET_SEARCH_PINS& resolutionHistogramSearch(DOUBLE res);
```
[表] Parameter
列: Parameter | Description
行 1:
  res
  The step width for the histogram based search.

### Return value（取自子主题 DIGITAL_OFFSET_SEARCH_PINS.resolutionHistogramSearch()）

A reference to the
`DIGITAL_OFFSET_SEARCH_PINS`（raw: `140966.htm`）

object.

### Syntax（取自子主题 DIGITAL_OFFSET_SEARCH_PINS.resourceType()）

```
DIGITAL_OFFSET_SEARCH_PINS& resourceType(DIGITAL_OFFSET_SEARCH::RESOURCE_TYPE resource);
```
[表] Parameter
列: Parameter | Description
行 1:
  resource
  A timing or level resource whose offset you want to search for.
    
    The available resources are in the following table.
[表] Available options of parameter: <resource>
列: Option | Description
行 1:
  DIGITAL_OFFSET_SEARCH::RECEIVE
  Receive edges
行 2:
  DIGITAL_OFFSET_SEARCH::DRIVE
  Drive edges which contain both FAST_DRIVE and
    SLOW_DRIVE
行 3:
  DIGITAL_OFFSET_SEARCH::FAST_DRIVE
  Fast drive edges
行 4:
  DIGITAL_OFFSET_SEARCH::SLOW_DRIVE
  Slow drive edges
行 5:
  DIGITAL_OFFSET_SEARCH::ALL_EDGES
  All edges containing FAST_DRIVE, SLOW_DRIVE, and
    RECEIVE
行 6:
  DIGITAL_OFFSET_SEARCH::VIH
  High driver levels
行 7:
  DIGITAL_OFFSET_SEARCH::VIL
  Low driver levels
行 8:
  DIGITAL_OFFSET_SEARCH::VIOFFSET
  The search of the offsets for VIH and VIL at the same time
行 9:
  DIGITAL_OFFSET_SEARCH::VTH
  Receiver thresholds
行 10:
  DIGITAL_OFFSET_SEARCH::VOH
  High receiver levels
行 11:
  DIGITAL_OFFSET_SEARCH::VOL
  Low receiver levels
行 12:
  DIGITAL_OFFSET_SEARCH::VOOFFSET
  The search of the offsets for VOH and VOL at the same time
行 13:
  DIGITAL_OFFSET_SEARCH::VISWING
  Driver swings
行 14:
  DIGITAL_OFFSET_SEARCH::VOSWING
  Receiver swings

### Return value（取自子主题 DIGITAL_OFFSET_SEARCH_PINS.resourceType()）

A reference to the
`DIGITAL_OFFSET_SEARCH_PINS`（raw: `140966.htm`）

object.

### Syntax（取自子主题 DIGITAL_OFFSET_SEARCH_PINS.restoreFlag()）

```
DIGITAL_OFFSET_SEARCH_PINS& restoreFlag(DIGITAL_OFFSET_SEARCH::YES_NO restoreflag);
```
[表] Parameter
列: Parameter | Description
行 1:
  restoreflag
  It can be:
    
    DIGITAL_OFFSET_SEARCH::YES: Enables the restore flag.
    
    DIGITAL_OFFSET_SEARCH::NO: (Default) Disables the restore flag.

### Return value（取自子主题 DIGITAL_OFFSET_SEARCH_PINS.restoreFlag()）

A reference to the
`DIGITAL_OFFSET_SEARCH_PINS`（raw: `140966.htm`）

object.

### Syntax（取自子主题 DIGITAL_OFFSET_SEARCH_PINS.search()）

```
DIGITAL_OFFSET_SEARCH::STATUS_TYPE search();
```

List of parameters

There are no parameters.

### Return value（取自子主题 DIGITAL_OFFSET_SEARCH_PINS.search()）

Returns the execution status which can be

SUCCESS
,
FAILED
,
ABORTED
 or

NOT_EXECUTED
.

### Syntax（取自子主题 DIGITAL_OFFSET_SEARCH_PINS.searchType()）

```
DIGITAL_OFFSET_SEARCH_PINS& searchType(DIGITAL_OFFSET_SEARCH::SEARCH_TYPE stype);
```
[表] Parameter
列: Parameter | Description
行 1:
  stype
  A search type. See the search types in the following table.
[表] List of available options of parameter: <stype>
列: Option | Description
行 1:
  DIGITAL_OFFSET_SEARCH::LB
  Searches for the left boundary (the fail to pass transition) of the pass area.
行 2:
  DIGITAL_OFFSET_SEARCH::RB
  Searches for the right boundary (the pass to fail transition) of the pass area.
行 3:
  DIGITAL_OFFSET_SEARCH::EYE
  Searches for the middle of the pass area.
[表] List of search types for each search resources
列: Search resources | Search types
行 1:
  Timing resources [跨 2 列]
行 2:
  DRIVE
  LB, RB, EYE
行 3:
  RECEIVE
  LB, RB, EYE
行 4:
  FAST_DRIVE
  LB, RB, EYE
行 5:
  SLOW_DRIVE
  LB, RB, EYE
行 6:
  Level resources [跨 2 列]
    1
行 7:
  VIL
  LB, RB
行 8:
  VIH
  LB, RB
行 9:
  VISWING
  LB, RB
行 10:
  VIOFFSET
  EYE, LB, RB
行 11:
  VOL
  LB, RB
行 12:
  VOH
  LB, RB
行 13:
  VTH
  EYE, LB, RB
行 14:
  VOOFFSET
  EYE, LB, RB
行 15:
  VOSWING
  LB, RB

1: Level resources: LB means the lower boundary (the fail to pass transition) of
the pass area. RB means the upper boundary (the pass to fail transition) of the pass
area.

To learn these search resources, see
`DIGITAL_OFFSET_SEARCH_PINS.resourceType()`（raw: `141059.htm`）
.

For level
resources, most of them can only search for one transition, either LB or RB. The EYE search only
applies for moving two level resources to the same direction, such as VTH, VIOFFSET, and
VOOFFSET.

### Return value（取自子主题 DIGITAL_OFFSET_SEARCH_PINS.searchType()）

A reference to the
`DIGITAL_OFFSET_SEARCH_PINS`（raw: `140966.htm`）

object.

### Syntax（取自子主题 DIGITAL_OFFSET_SEARCH_PINS.setConfiguration()）

```
DIGITAL_OFFSET_SEARCH_PINS& setConfiguration(DIGITAL_OFFSET_SEARCH::DigitalOffsetSearchConfigDataType & configdata);
```
[表] Parameter
列: Parameter | Description
行 1:
  configdata
  The configuration data, such as search type, resource type, start value, stop
    value, etc.. For more data types, see `DigitalOffsetSearchConfigDataType`（raw: `141168.htm`）.

### Return value（取自子主题 DIGITAL_OFFSET_SEARCH_PINS.setConfiguration()）

A reference to the
`DIGITAL_OFFSET_SEARCH_PINS`（raw: `140966.htm`）

object.

### Syntax（取自子主题 DIGITAL_OFFSET_SEARCH_PINS.setExecutionContext()）

```
DIGITAL_OFFSET_SEARCH_PINS& setExecutionContext(const STRING& context);
```
[表] Parameter
列: Parameter | Description
行 1:
  context
  An execution context you have already defined with the `SEQUENCER_CONTEXT`（raw: `136815.htm`） API
    or the `SQEC`（raw: `137546.htm`） firmware command.

### Return value（取自子主题 DIGITAL_OFFSET_SEARCH_PINS.setExecutionContext()）

A reference to the
`DIGITAL_OFFSET_SEARCH_PINS`（raw: `140966.htm`）

object.

### Syntax（取自子主题 DIGITAL_OFFSET_SEARCH_PINS.setup()）

```
void setup();
```

List of parameters

There are no parameters.

Return value

There is no return value.

### Syntax（取自子主题 DIGITAL_OFFSET_SEARCH_PINS.start()）

```
DIGITAL_OFFSET_SEARCH_PINS& start(DOUBLE startval);
```
[表] Parameter
列: Parameter | Description
行 1:
  startval
  A value represents the interval between the search start and the value of the
    searched `resource`（raw: `141059.htm`）. It can be a negative value. Therefore, the
    start position is calculated from:
    
    the value of the searched resource + startval
    
    The units for timing and voltage searches are seconds [s] and Volts [V] respectively.

### Return value（取自子主题 DIGITAL_OFFSET_SEARCH_PINS.start()）

A reference to the
`DIGITAL_OFFSET_SEARCH_PINS`（raw: `140966.htm`）

object.

### Syntax（取自子主题 DIGITAL_OFFSET_SEARCH_PINS.stepWidth()）

```
DIGITAL_OFFSET_SEARCH_PINS& stepWidth(DOUBLE stepwidth);
```
[表] Parameter
列: Parameter | Description
行 1:
  stepwidth
  The step width of a search. It can be positive or negative.
    
    For timing searches, the unit is seconds [s].
    
    For voltage searches, the unit is Volts [V].

### Return value（取自子主题 DIGITAL_OFFSET_SEARCH_PINS.stepWidth()）

A reference to the
`DIGITAL_OFFSET_SEARCH_PINS`（raw: `140966.htm`）

object.

### Syntax（取自子主题 DIGITAL_OFFSET_SEARCH_PINS.transitionDetection()）

```
DIGITAL_OFFSET_SEARCH_PINS& transitionDetection (DIGITAL_OFFSET_SEARCH::TR_DETECTION_TYPE detectiontype);
```
[表] Parameter
列: Parameter | Description
行 1:
  detectiontype
  The transition detection type.
    
    See the available types in the following table.
[表] List of available options of parameter: <detectiontype>
列: Option | Description
行 1:
  DIGITAL_OFFSET_SEARCH::PF
  Pass/fail transition
行 2:
  DIGITAL_OFFSET_SEARCH::ECL
  Use the specified `error count limit`（raw: `141062.htm`） to consider a test
    pass or fail.
    
    If the error count of a test is greater than this limit, the test is considered fail.
    Otherwise, the test is considered pass.

### Return value（取自子主题 DIGITAL_OFFSET_SEARCH_PINS.transitionDetection()）

A reference to the
`DIGITAL_OFFSET_SEARCH_PINS`（raw: `140966.htm`）

object.

### Syntax（取自子主题 DIGITAL_OFFSET_SEARCH_PINS.TransitionOffsetFound()）

```
DIGITAL_OFFSET_SEARCH::RESULT_FOUND TransitionOffsetFound();
```

### Parameters（取自子主题 DIGITAL_OFFSET_SEARCH_PINS.TransitionOffsetFound()）

There is no parameters.

### Return value（取自子主题 DIGITAL_OFFSET_SEARCH_PINS.TransitionOffsetFound()）

Returns the status of the last transition offset search. It
can be
FOUND
,
NOT_FOUND
,
LB_NOT_FOUND
,
or
RB_NOT_FOUND
.

### Syntax（取自子主题 DIGITAL_OFFSET_SEARCH_PINS.uploadLatestTransition()）

```
void uploadLatestTransition();
```

List of parameters

There are no parameters.

Return value

There is no return value.

### Syntax（取自子主题 DIGITAL_OFFSET_SEARCH_PINS.uploadOffset()）

```
void uploadOffset(SetSelector &selector, RESOURCE_TYPE resource) throws TMExcption;
```
[表] Parameters
列: Parameter | Description
行 1:
  selector
  It can be:
    
    A TimingSetSelector object defined with the `TimingSetSelector`（raw: `141248.htm`） class, to select
    timing sets. Or,
    
    A LevelSetSelector object defined with the `LevelSetSelector`（raw: `141182.htm`） class, to select
    level sets.
行 2:
  resource
  It can be a timing resource or a level resource whose offset you want to upload.
    Choose a timing or level resource for the timing or level selector accordingly. Otherwise,
    an exception will be thrown.
    
    For the resource types, see the following table.
[表] Available options of parameter: <resource>
列: Option | Description
行 1:
  DIGITAL_OFFSET_SEARCH::RECEIVE
  Receive edges
行 2:
  DIGITAL_OFFSET_SEARCH::DRIVE
  Drive edges which contain both FAST_DRIVE and
    SLOW_DRIVE
行 3:
  DIGITAL_OFFSET_SEARCH::FAST_DRIVE
  Fast drive edges
行 4:
  DIGITAL_OFFSET_SEARCH::SLOW_DRIVE
  Slow drive edges
行 5:
  DIGITAL_OFFSET_SEARCH::ALL_EDGES
  All edges containing FAST_DRIVE, SLOW_DRIVE, and
    RECEIVE
行 6:
  DIGITAL_OFFSET_SEARCH::VIH
  High driver levels
行 7:
  DIGITAL_OFFSET_SEARCH::VIL
  Low driver levels
行 8:
  DIGITAL_OFFSET_SEARCH::VIOFFSET
  The search of the offsets for VIH and VIL at the same time
行 9:
  DIGITAL_OFFSET_SEARCH::VTH
  Receiver thresholds
行 10:
  DIGITAL_OFFSET_SEARCH::VOH
  High receiver levels
行 11:
  DIGITAL_OFFSET_SEARCH::VOL
  Low receiver levels
行 12:
  DIGITAL_OFFSET_SEARCH::VOOFFSET
  The search of the offsets for VOH and VOL at the same time
行 13:
  DIGITAL_OFFSET_SEARCH::VISWING
  Driver swings
行 14:
  DIGITAL_OFFSET_SEARCH::VOSWING
  Receiver swings

Return value

There is no return value.

### Example（取自子主题 DIGITAL_OFFSET_SEARCH_PINS.uploadOffset()）

```
STRING strpins("pcie_rx1n");
DIGITAL_OFFSET_SEARCH_TASK dos;

dos.pin(strpins)
.resourceType(DIGITAL_OFFSET_SEARCH::VIH)
.searchType(DIGITAL_OFFSET_SEARCH::EYE)
.start(15 mV)
.numSteps(120)
.stepWidth(15 mV)
.restoreFlag(DIGITAL_OFFSET_SEARCH::NO);

dos.execute();

DIGITAL_OFFSET_SEARCH::LevelSetSelector dest(DIGITAL_OFFSET_SEARCH::ALL);

dos.pin(strpins).uploadOffset(dest, DIGITAL_OFFSET_SEARCH::VIH);
```

### Syntax（取自子主题 DIGITAL_OFFSET_SEARCH_PINS.uploadResult()）

```
void uploadResult(SetSelector& selector, RESOURCE_TYPE resource) throws TMException;
```
[表] Parameters
列: Parameter | Description
行 1:
  selector
  It can be:
    
    A TimingSetSelector object defined with `TimingSetSelector`（raw: `141248.htm`）, to select timing sets.
    Or,
    
    A LevelSetSelector object, defined with `LevelSetSelector`（raw: `141182.htm`）, to select level sets.
行 2:
  resource
  It can be a timing resource or a level resource whose offset and/or boundaries of
    the pass area you want to upload.
    
    Use a timing or level resource for the timing or level selector accordingly. Otherwise,
    an exception will be thrown.
    
    For the resource types, see the following table.
[表] Available options of parameter: <resource>
列: Option | Description
行 1:
  DIGITAL_OFFSET_SEARCH::RECEIVE
  Receive edges
行 2:
  DIGITAL_OFFSET_SEARCH::DRIVE
  Drive edges which contain both FAST_DRIVE and
    SLOW_DRIVE
行 3:
  DIGITAL_OFFSET_SEARCH::FAST_DRIVE
  Fast drive edges
行 4:
  DIGITAL_OFFSET_SEARCH::SLOW_DRIVE
  Slow drive edges
行 5:
  DIGITAL_OFFSET_SEARCH::ALL_EDGES
  All edges containing FAST_DRIVE, SLOW_DRIVE, and
    RECEIVE
行 6:
  DIGITAL_OFFSET_SEARCH::VIH
  High driver levels
行 7:
  DIGITAL_OFFSET_SEARCH::VIL
  Low driver levels
行 8:
  DIGITAL_OFFSET_SEARCH::VIOFFSET
  The search of the offsets for VIH and VIL at the same time
行 9:
  DIGITAL_OFFSET_SEARCH::VTH
  Receiver thresholds
行 10:
  DIGITAL_OFFSET_SEARCH::VOH
  High receiver levels
行 11:
  DIGITAL_OFFSET_SEARCH::VOL
  Low receiver levels
行 12:
  DIGITAL_OFFSET_SEARCH::VOOFFSET
  The search of the offsets for VOH and VOL at the same time
行 13:
  DIGITAL_OFFSET_SEARCH::VISWING
  Driver swings
行 14:
  DIGITAL_OFFSET_SEARCH::VOSWING
  Receiver swings

Return value

There is no return value.

### Example（取自子主题 DIGITAL_OFFSET_SEARCH_PINS.uploadResult()）

```
STRING strpins("pcie_rx1n");

DIGITAL_OFFSET_SEARCH_TASK dos;

dos.pin(strpins)
.resourceType(DIGITAL_OFFSET_SEARCH::VIH)
.searchType(DIGITAL_OFFSET_SEARCH::EYE)
.start(15 mV)
.numSteps(120)
.stepWidth(15 mV)
.restoreFlag(DIGITAL_OFFSET_SEARCH::NO);

dos.execute();

DIGITAL_OFFSET_SEARCH::LevelSetSelector dest(DIGITAL_OFFSET_SEARCH::ALL);

dos.pin(strpins).uploadResult(dest, DIGITAL_OFFSET_SEARCH::VIH);
```

### Syntax（取自子主题 DIGITAL_OFFSET_SEARCH_TASK.pin()）

```
DIGITAL_OFFSET_SEARCH_PINS& pin(const STRING& pinlist);
```
[表] Parameter
列: Parameter | Description
行 1:
  pinlist
  The pins on which you want to search for timing or level offsets.

### Return value（取自子主题 DIGITAL_OFFSET_SEARCH_TASK.pin()）

Returns the reference to a
`DIGITAL_OFFSET_SEARCH_PINS`（raw: `140966.htm`）
 object so
that you can use its member functions to set up search conditions for the specified pins.

### Example（取自子主题 DIGITAL_OFFSET_SEARCH_TASK.pin()）

```
STRING strpins1("pcie_tx1n");
DIGITAL_OFFSET_SEARCH_TASK dos;

dos.pin(strpins1).resourceType(VIH);
```

### Syntax（取自子主题 DIGITAL_OFFSET_SEARCH_TASK）

```
DIGITAL_OFFSET_SEARCH_TASK();
```

This constructor creates an object
of the
DIGITAL_OFFSET_SEARCH_TASK()
 class.

List of parameters

There are no parameters.

Return value

There is no return value.

### Examples（取自子主题 DIGITAL_OFFSET_SEARCH_TASK）

### Example 1

Do a VIL search with a positive step width. The search will
start from Pass until Fail, intending to do a right boundary search. The setup and result pins
are the same. Set the RestoreFlag to
YES.

```
STRING setupPins("pcie_tx1n");
STRING resultPins("pcie_rx1n");

DIGITAL_OFFSET_SEARCH_TASK dos;

ON_FIRST_INVOCATION_BEGIN();

dos.pin(setupPins)
.resourceType(DIGITAL_OFFSET_SEARCH::VIL)
.searchType(DIGITAL_OFFSET_SEARCH::RB)
.start(-0.5 V)
.numSteps(4)
.stepWidth(0.25 V)
.minPassCount(1)
.transitionDetection(DIGITAL_OFFSET_SEARCH::PF)
.resolution(0.05 V)
.errorCountLimit(1)
.restoreFlag(DIGITAL_OFFSET_SEARCH::YES);

dos.resultPin(setupPins).setResultPin(resultPins);

dos.setup();
dos.execute();

dos.uploadLatestTransition();

ON_FIRST_INVOCATION_END();

DIGITAL_OFFSET_SEARCH::RESULT_FOUND result;

result = dos.pin(setupPins).TransitionOffsetFound();

if( result != DIGITAL_OFFSET_SEARCH::NOT_FOUND )
{
if( result != DIGITAL_OFFSET_SEARCH::RB_NOT_FOUND )
{
cout << "rbOffset = " << dos.pin( setupPins ).getLatestRBTransitionOffset() << endl;
}
else
{
cout << "rbOffset = NOT_FOUND" << endl;
}
}
```

### Example 2

Do an EYE search for VTH in order to bring the threshold to
the middle. The VTH needs to pass for VIL/VIH between 'VTH + 1.5V' and 'VTH - 1.0V'. The setup
and result pins are the same. Set the RestoreFlag to
NO.

```
STRING setupPins("pcie_tx1n");

DIGITAL_OFFSET_SEARCH_TASK dos;

ON_FIRST_INVOCATION_BEGIN();

dos.pin(setupPins)
.resourceType(DIGITAL_OFFSET_SEARCH::VTH)
.searchType(DIGITAL_OFFSET_SEARCH::EYE)
.start(1.5 V)
.numSteps(5)
.stepWidth(-0.5 V)
.minPassCount(1)
.transitionDetection(DIGITAL_OFFSET_SEARCH::PF)
.resolution(0.05 V)
.errorCountLimit(1)
.restoreFlag(DIGITAL_OFFSET_SEARCH::NO);

dos.setup();
dos.execute();

ON_FIRST_INVOCATION_END();
```

### Example 3

Do a timing offset
search.

```
STRING pinTX1("pcie_tx1n");
STRING pinRX1("pcie_rx1n");
STRING pinRX2("pcie_rx2n");

DIGITAL_OFFSET_SEARCH_TASK dos_search;
DIGITAL_OFFSET_SEARCH_TASK dos_alignment;

ON_FIRST_INVOCATION_BEGIN();

//
// Timing alignment: searches new receive edge position between
// (current poistion - 100ns) to (current position + 100ns)
//
dos_alignment.pin(pinRX2)
.resourceType(DIGITAL_OFFSET_SEARCH::RECEIVE)
.searchType(DIGITAL_OFFSET_SEARCH::EYE)
.start(-100 ns)
.numSteps(10)
.stepWidth(20 ns)
.restoreFlag(DIGITAL_OFFSET_SEARCH::NO);

//
// Search for a driver resource (move TX1 depending on PASS/FAIL of RX1)
//
dos_search.pin(pinTX1)
.resourceType(DIGITAL_OFFSET_SEARCH::DRIVE)
.searchType(DIGITAL_OFFSET_SEARCH::EYE)
.start(-10 ms)
.numSteps(100)
.stepWidth(10 ms)
.minPassCount(1)
.transitionDetection(DIGITAL_OFFSET_SEARCH::PF)
.resolution(10 ms)
.errorCountLimit(1)
.restoreFlag(DIGITAL_OFFSET_SEARCH::YES);

dos_search.resultPin(pinTX1).setResultPin(pinRX1);

dos_alignment.setup();
dos_search.setup();

dos_alignment.execute();
dos_search.execute();
```

```
ON_FIRST_INVOCATION_END();

DIGITAL_OFFSET_SEARCH::TimingSetSelector dest;

dos_search.uploadResult(dest, DIGITAL_OFFSET_SEARCH::DRIVE);

DIGITAL_OFFSET_SEARCH::RESULT_FOUND result;

result = dos_search.pin(pinTX1).TransitionOffsetFound();

if (result != DIGITAL_OFFSET_SEARCH::NOT_FOUND)
{
if (result != DIGITAL_OFFSET_SEARCH::LB_NOT_FOUND)
{
cout << "leftTranstition = "
<< dos_search.pin(pinTX1).getLatestLBTransitionOffset() << endl;
}
else
{
cout << "leftTranstition = NOT_FOUND" << endl;
}
if (result != DIGITAL_OFFSET_SEARCH::RB_NOT_FOUND)
{
cout << "rightTranstition = "
<< dos_search.pin(pinTX1).getLatestRBTransitionOffset() << endl;
}
else
{
cout << "rightTranstition = NOT_FOUND" << endl;
}
}
else
{
cout << "lb/rb transition/boundaries NOT_FOUND" << endl;
}

int site = CURRENT_SITE_NUMBER();

cout << "site " << site << ": "
<< dos_search.pin(pinTX1).getOffset(dest, DIGITAL_OFFSET_SEARCH::DRIVE) << endl;
```

### Syntax（取自子主题 DIGITAL_OFFSET_SEARCH_RESULT_PINS）

This class has no constructor. You cannot directly create an object with this class. It
is a sub-class of
`DIGITAL_OFFSET_SEARCH_TASK`（raw: `140965.htm`）
.

An instance of this class is created with
`DIGITAL_OFFSET_SEARCH_TASK.resultPin()`（raw: `141030.htm`）
.

This API is defined in the header file

/opt/hp93000/soc/prod_com/include/MAPI/DigitalOffsetSearchResultPins.h
.

List of parameters

There are no parameters.

Return value

There is no return value.

### Syntax（取自子主题 DIGITAL_OFFSET_SEARCH_TASK.resultPin()）

```
DIGITAL_OFFSET_SEARCH_RESULT_PINS& resultPin(const STRING& setupPin);
```
[表] Parameter
列: Parameter | Description
行 1:
  setupPin
  The pins for which you want to create a DIGITAL_OFFSET_SEARCH_RESULT_PINS
    object.

### Return value（取自子主题 DIGITAL_OFFSET_SEARCH_TASK.resultPin()）

Returns a reference to the
`DIGITAL_OFFSET_SEARCH_RESULT_PINS`（raw: `141031.htm`）
 object so
that you can use its member functions to define different result pins or retrieve defined result
pins.

### Examples（取自子主题 DIGITAL_OFFSET_SEARCH_TASK.resultPin()）

### Example 1

Define the result pin as the same as the setup pin
"pcie_tx1n". "pcie_tx1n" is an IO
pin.

```
STRING strpins1("pcie_tx1n");

DIGITAL_OFFSET_SEARCH_TASK dos;

dos.resultPin(strpins1);
```

### Example 2

Define "pcie_tx2n" as the result pin while the setup pin is
"pcie_tx1n".

```
STRING strpins1("pcie_tx1n");
STRING strpins2("pcie_tx2n");

DIGITAL_OFFSET_SEARCH_TASK dos;

dos.resultPin(strpins1).setResultPin(strpins2);
```

### Syntax（取自子主题 DIGITAL_OFFSET_SEARCH_TASK.setExecutionContext()）

```
void setExecutionContext(const STRING& context);
```
[表] Parameter
列: Parameter | Description
行 1:
  context
  An execution context you have already defined with the `SEQUENCER_CONTEXT`（raw: `136815.htm`） API
    or the `SQEC`（raw: `137546.htm`） firmware command.

Return value

There is no return value.

### Syntax（取自子主题 DIGITAL_OFFSET_SEARCH_TASK.print()）

```
void print(std::ostream & os) const;
```
[表] Parameter
列: Parameter | Description
行 1:
  os
  The output stream to be used as target for the printed data.

Return value

There is no return value.

### Examples（取自子主题 DIGITAL_OFFSET_SEARCH_TASK.print()）

### Example 1: Output to the standard output stream
```
DIGITAL_OFFSET_SEARCH_TASK dos;

dos.pin("PS1600_pin_1")
.resourceType(DIGITAL_OFFSET_SEARCH::VIH)
.searchType(DIGITAL_OFFSET_SEARCH::RB)
.start(15 mV)
.numSteps(120)
.stepWidth(15 mV)
.restoreFlag(DIGITAL_OFFSET_SEARCH::NO);

dos.execute();

dos.print(std::cout);
```

The
example above results in the following output in the
ui_report

window:

```
TOCF LB,VIH,15,120,15,1E-06,1,0,0,PF,,NO,(PS1600_pin_1)
```

### Example 2: Output to a user defined stream
```
DIGITAL_OFFSET_SEARCH_TASK dos;

dos.pin("PS1600_pin_1")
.resourceType(DIGITAL_OFFSET_SEARCH::VIH)
.searchType(DIGITAL_OFFSET_SEARCH::RB)
.start(15 mV)
.numSteps(120)
.stepWidth(15 mV)
.restoreFlag(DIGITAL_OFFSET_SEARCH::NO);

dos.execute();

std::stringstream outStream;

dos.print(outStream);

cout << "DIGITAL_OFFSET_SEARCH_TASK: " << outStream.str() << endl;
```

The
example above results in the following output in the
ui_report

window:

```
DIGITAL_OFFSET_SEARCH_TASK: TOCF LB,VIH,15,120,15,1E-06,1,0,0,PF,,NO,(PS1600_pin_1)
```

### Syntax（取自子主题 DIGITAL_OFFSET_SEARCH_TASK.enableAutoOffsetUpload()）

```
void enableAutoOffsetUpload(SetSelector& selector, RESOURCE_TYPE resource) throws TMException;
```
[表] Parameters
列: Parameter | Description
行 1:
  selector
  It can be:
    
    A timing set selector defined with `TimingSetSelector`（raw: `141248.htm`）, used to select the timing
    sets for use.
    
    A level set selector defined with `LevelSetSelector`（raw: `141182.htm`）, used to select the level
    sets for use.
行 2:
  resource
  A timing or level resource whose offset you will upload. In the following table,
    you will see the available resources.
[表] Available options of parameter: <resource>
列: Option | Description
行 1:
  DIGITAL_OFFSET_SEARCH::RECEIVE
  Receive edges
行 2:
  DIGITAL_OFFSET_SEARCH::DRIVE
  Drive edges which contain both FAST_DRIVE and
    SLOW_DRIVE
行 3:
  DIGITAL_OFFSET_SEARCH::FAST_DRIVE
  Fast drive edges
行 4:
  DIGITAL_OFFSET_SEARCH::SLOW_DRIVE
  Slow drive edges
行 5:
  DIGITAL_OFFSET_SEARCH::ALL_EDGES
  All edges containing FAST_DRIVE, SLOW_DRIVE, and
    RECEIVE
行 6:
  DIGITAL_OFFSET_SEARCH::VIH
  High driver levels
行 7:
  DIGITAL_OFFSET_SEARCH::VIL
  Low driver levels
行 8:
  DIGITAL_OFFSET_SEARCH::VIOFFSET
  The search of the offsets for VIH and VIL at the same time
行 9:
  DIGITAL_OFFSET_SEARCH::VTH
  Receiver thresholds
行 10:
  DIGITAL_OFFSET_SEARCH::VOH
  High receiver levels
行 11:
  DIGITAL_OFFSET_SEARCH::VOL
  Low receiver levels
行 12:
  DIGITAL_OFFSET_SEARCH::VOOFFSET
  The search of the offsets for VOH and VOL at the same time
行 13:
  DIGITAL_OFFSET_SEARCH::VISWING
  Driver swings
行 14:
  DIGITAL_OFFSET_SEARCH::VOSWING
  Receiver swings

Return value

There is no return value.

### Example（取自子主题 DIGITAL_OFFSET_SEARCH_TASK.enableAutoOffsetUpload()）

Refer to the example in
`DIGITAL_OFFSET_SEARCH_TASK.enableAutoTransitionUpload()`（raw: `146558.htm`）
.

### Syntax（取自子主题 DIGITAL_OFFSET_SEARCH_TASK.enableAutoTransitionUpload()）

```
void enableAutoTransitionUpload();
```

List of parameters

There are no parameters.

Return value

There is no return value.

### Example（取自子主题 DIGITAL_OFFSET_SEARCH_TASK.enableAutoTransitionUpload()）

Utilizing the
TASK_LIST
 API to perform two different digital offset
searches. One searches the
pcie_rx1p
 pin and the other one searches the

pcie_rx2p

pin.

```
DIGITAL_OFFSET_SEARCH_TASK dos_task_1;
DIGITAL_OFFSET_SEARCH_TASK dos_task_2;
TASK_LIST dos_tasklist;
DIGITAL_OFFSET_SEARCH::LevelSetSelector lss(DIGITAL_OFFSET_SEARCH::PRM);

static DIGITAL_OFFSET_SEARCH::DigitalOffsetSearchConfigDataType configdata;
configdata.resourceType = DIGITAL_OFFSET_SEARCH::VIL;
configdata.searchType = DIGITAL_OFFSET_SEARCH::EYE;
configdata.start = -100 mV;
configdata.numSteps = 200;
configdata.stepWidth = 1 mV;

dos_task_1.pin("pcie_rx1p").setConfiguration(configdata);
dos_task_2.pin("pcie_rx2p").setConfiguration(configdata);

dos_task_1.enableAutoTransitionUpload();
dos_task_2.enableAutoTransitionUpload();

dos_task_1.enableAutoOffsetUpload(lss, DIGITAL_OFFSET_SEARCH::VIL);
dos_task_2.enableAutoOffsetUpload(lss, DIGITAL_OFFSET_SEARCH::VIL);

// add both tasks to list
dos_tasklist.add(dos_task_1);
dos_tasklist.add(dos_task_2);

ON_FIRST_INVOCATION_BEGIN();

//execute list
dos_tasklist.execute();

FOR_EACH_SITE_BEGIN();

try
{
DOUBLE offset = dos_task_1.pin("pcie_rx1p").getLatestLBTransitionOffset();
}
catch (TESTMETHOD_API::TMException & e)
{
//ERROR CASE
}

try
{
DOUBLE offset = dos_task_1.pin("pcie_rx1p").getOffset(lss, DIGITAL_OFFSET_SEARCH::VIL);
}
catch (TESTMETHOD_API::TMException & e)
{
//ERROR CASE
}

try
{
DOUBLE offset = dos_task_2.pin("pcie_rx2p").getLatestLBTransitionOffset();
}
catch (TESTMETHOD_API::TMException & e)
{
//ERROR CASE
}

try
{
DOUBLE offset = dos_task_2.pin("pcie_rx2p").getOffset(lss, DIGITAL_OFFSET_SEARCH::VIL);
}
catch (TESTMETHOD_API::TMException & e)
{
//ERROR CASE
}

FOR_EACH_SITE_END();

ON_FIRST_INVOCATION_END();
```

### Syntax（取自子主题 DIGITAL_OFFSET_SEARCH_TASK.enableAutoResultsUpload()）

```
void enableAutoResultsUpload(SetSelector& selector, RESOURCE_TYPE resource) throws TMException;
```
[表] Parameters
列: Parameter | Description
行 1:
  selector
  It can be:
    
    A timing set selector defined with `TimingSetSelector`（raw: `141248.htm`）, used to select the timing
    sets for use.
    
    A level set selector defined with `LevelSetSelector`（raw: `141182.htm`）, used to select the level
    sets for use.
行 2:
  resource
  A timing or level resource whose offset you will upload. In the following table,
    you will see the available resources.
[表] Available options of parameter: <resource>
列: Option | Description
行 1:
  DIGITAL_OFFSET_SEARCH::RECEIVE
  Receive edges
行 2:
  DIGITAL_OFFSET_SEARCH::DRIVE
  Drive edges which contain both FAST_DRIVE and
    SLOW_DRIVE
行 3:
  DIGITAL_OFFSET_SEARCH::FAST_DRIVE
  Fast drive edges
行 4:
  DIGITAL_OFFSET_SEARCH::SLOW_DRIVE
  Slow drive edges
行 5:
  DIGITAL_OFFSET_SEARCH::ALL_EDGES
  All edges containing FAST_DRIVE, SLOW_DRIVE, and
    RECEIVE
行 6:
  DIGITAL_OFFSET_SEARCH::VIH
  High driver levels
行 7:
  DIGITAL_OFFSET_SEARCH::VIL
  Low driver levels
行 8:
  DIGITAL_OFFSET_SEARCH::VIOFFSET
  The search of the offsets for VIH and VIL at the same time
行 9:
  DIGITAL_OFFSET_SEARCH::VTH
  Receiver thresholds
行 10:
  DIGITAL_OFFSET_SEARCH::VOH
  High receiver levels
行 11:
  DIGITAL_OFFSET_SEARCH::VOL
  Low receiver levels
行 12:
  DIGITAL_OFFSET_SEARCH::VOOFFSET
  The search of the offsets for VOH and VOL at the same time
行 13:
  DIGITAL_OFFSET_SEARCH::VISWING
  Driver swings
行 14:
  DIGITAL_OFFSET_SEARCH::VOSWING
  Receiver swings

Return value

There is no return value.

### Example（取自子主题 DIGITAL_OFFSET_SEARCH_TASK.enableAutoResultsUpload()）

Refer to the example in
`DIGITAL_OFFSET_SEARCH_TASK.enableAutoTransitionUpload()`（raw: `146558.htm`）
.

### Syntax（取自子主题 DIGITAL_OFFSET_SEARCH_TASK.setup()）

```
void setup();
```

List of parameters

There are no parameters.

Return value

There is no return value.

### Syntax（取自子主题 DIGITAL_OFFSET_SEARCH_TASK.execute()）

```
void execute();
```

List of parameters

There are no parameters.

Return value

There is no return value.

### Syntax（取自子主题 DIGITAL_OFFSET_SEARCH_TASK.remove()）

```
void remove(const STRING& pinlist);
```
[表] Parameter
列: Parameter | Description
行 1:
  pinlist
  The pins whose DIGITAL_OFFSET_SEARCH_PINS instance you want to remove from
    DIGITAL_OFFSET_SEARCH_TASK.

Return value

There is no return value.

### Syntax（取自子主题 DIGITAL_OFFSET_SEARCH_TASK.getStatus()）

```
DIGITAL_OFFSET_SEARCH::STATUS_TYPE getStatus();
```

### Return value（取自子主题 DIGITAL_OFFSET_SEARCH_TASK.getStatus()）

Returns the execution status for all of the sites under
test, which can be
SUCCESS
,
FAILED
,

ABORTED
 or
NOT_EXECUTE
.

### Syntax（取自子主题 DIGITAL_OFFSET_SEARCH_TASK.getExecutionContext()）

```
const STRING& getExecutionContext();
```

List of parameters

There are no parameters.

### Return value（取自子主题 DIGITAL_OFFSET_SEARCH_TASK.getExecutionContext()）

Returns a context name, or an empty string if no context
execution had been referenced.

### Syntax（取自子主题 DIGITAL_OFFSET_SEARCH_TASK.uploadLatestTransition()）

```
void uploadLatestTransition();
```

List of parameters

There are no parameters.

Return value

There is no return value.

### Syntax（取自子主题 DIGITAL_OFFSET_SEARCH_TASK.uploadOffset()）

```
void uploadOffset(SetSelector& selector, RESOURCE_TYPE resource) throws TMException;
```
[表] Parameters
列: Parameter | Description
行 1:
  selector
  It can be:
    
    A TimingSetSelector object defined with `TimingSetSelector`（raw: `141248.htm`）, to select the timing
    sets to be used. Or,
    
    A LevelSetSelector object defined with `LevelSetSelector`（raw: `141182.htm`）, to select the level
    sets to be used.
行 2:
  resource
  It can be a timing resource or a level resource whose offset you want to
    upload.
    
    Choose a timing or level resource for the timing or level selector respectively.
    Otherwise, an exception will be thrown.
    
    For the resource types, see the following table.
[表] Available options of parameter: <resource>
列: Option | Description
行 1:
  DIGITAL_OFFSET_SEARCH::RECEIVE
  Receive edges
行 2:
  DIGITAL_OFFSET_SEARCH::DRIVE
  Drive edges which contain both FAST_DRIVE and
    SLOW_DRIVE
行 3:
  DIGITAL_OFFSET_SEARCH::FAST_DRIVE
  Fast drive edges
行 4:
  DIGITAL_OFFSET_SEARCH::SLOW_DRIVE
  Slow drive edges
行 5:
  DIGITAL_OFFSET_SEARCH::ALL_EDGES
  All edges containing FAST_DRIVE, SLOW_DRIVE, and
    RECEIVE
行 6:
  DIGITAL_OFFSET_SEARCH::VIH
  High driver levels
行 7:
  DIGITAL_OFFSET_SEARCH::VIL
  Low driver levels
行 8:
  DIGITAL_OFFSET_SEARCH::VIOFFSET
  The search of the offsets for VIH and VIL at the same time
行 9:
  DIGITAL_OFFSET_SEARCH::VTH
  Receiver thresholds
行 10:
  DIGITAL_OFFSET_SEARCH::VOH
  High receiver levels
行 11:
  DIGITAL_OFFSET_SEARCH::VOL
  Low receiver levels
行 12:
  DIGITAL_OFFSET_SEARCH::VOOFFSET
  The search of the offsets for VOH and VOL at the same time
行 13:
  DIGITAL_OFFSET_SEARCH::VISWING
  Driver swings
行 14:
  DIGITAL_OFFSET_SEARCH::VOSWING
  Receiver swings

Return value

There is no return value.

### Example（取自子主题 DIGITAL_OFFSET_SEARCH_TASK.uploadOffset()）

```
DIGITAL_OFFSET_SEARCH_TASK dos;
DIGITAL_OFFSET_SEARCH::LevelSetSelector dest(DIGITAL_OFFSET_SEARCH::ALL);
dos.uploadOffset(dest, DIGITAL_OFFSET_SEARCH::VIH);
```

### Syntax（取自子主题 DIGITAL_OFFSET_SEARCH_TASK.uploadResult()）

```
void uploadResult(SetSelector& selector, RESOURCE_TYPE resource) throws TMException;
```
[表] Parameters
列: Parameter | Description
行 1:
  selector
  It can be:
    
    A TimingSetSelector object defined with `TimingSetSelector`（raw: `141248.htm`）, to select the timing
    sets for use.
    
    A LevelSetSelector object defined with `LevelSetSelector`（raw: `141182.htm`）, to select the level
    sets for use.
行 2:
  resource
  A timing or level resource whose offset you want to upload. See the following table
    for the resource types.
    
    Choose a timing or level resource for the timing or level selector respectively.
    Otherwise, an exception will be thrown.
[表] Available options of parameter: <resource>
列: Option | Description
行 1:
  DIGITAL_OFFSET_SEARCH::RECEIVE
  Receive edges
行 2:
  DIGITAL_OFFSET_SEARCH::DRIVE
  Drive edges which contain both FAST_DRIVE and
    SLOW_DRIVE
行 3:
  DIGITAL_OFFSET_SEARCH::FAST_DRIVE
  Fast drive edges
行 4:
  DIGITAL_OFFSET_SEARCH::SLOW_DRIVE
  Slow drive edges
行 5:
  DIGITAL_OFFSET_SEARCH::ALL_EDGES
  All edges containing FAST_DRIVE, SLOW_DRIVE, and
    RECEIVE
行 6:
  DIGITAL_OFFSET_SEARCH::VIH
  High driver levels
行 7:
  DIGITAL_OFFSET_SEARCH::VIL
  Low driver levels
行 8:
  DIGITAL_OFFSET_SEARCH::VIOFFSET
  The search of the offsets for VIH and VIL at the same time
行 9:
  DIGITAL_OFFSET_SEARCH::VTH
  Receiver thresholds
行 10:
  DIGITAL_OFFSET_SEARCH::VOH
  High receiver levels
行 11:
  DIGITAL_OFFSET_SEARCH::VOL
  Low receiver levels
行 12:
  DIGITAL_OFFSET_SEARCH::VOOFFSET
  The search of the offsets for VOH and VOL at the same time
行 13:
  DIGITAL_OFFSET_SEARCH::VISWING
  Driver swings
行 14:
  DIGITAL_OFFSET_SEARCH::VOSWING
  Receiver swings

Return value

There is no return value.

### Example（取自子主题 DIGITAL_OFFSET_SEARCH_TASK.uploadResult()）

```
DIGITAL_OFFSET_SEARCH_TASK dos;
DIGITAL_OFFSET_SEARCH::LevelSetSelector dest(DIGITAL_OFFSET_SEARCH::ALL);
dos.uploadResult(dest, DIGITAL_OFFSET_SEARCH::VIH);
```

### Class definition（取自子主题 TASK_LIST）

This API is defined in the header file

/opt/hp93000/soc/prod_com/include/MAPI/TaskList.h
.

Constructor

```
TASK_LIST();
```

This constructor defines a task list that holds task names to be
executed.

Parameters

There are no parameters associated with this function.

Member functions:

`add()`（raw: `29792.htm#_29792__dle_add`）

`setup()`（raw: `29792.htm#_29792__dle_setup`）

`execute()`（raw: `29792.htm#_29792__dle_execute`）

### Usage（取自子主题 TASK_LIST）

For creating an object:

```
TASK_LIST <object>;
```

For setting up tasks to be performed:

```
<object>.add(task1).add(task2)...add(taskN);
```

For downloading the settings in tasks:

```
<object>.setup();
```

For downloading the settings in tasks and performing the tasks:

```
<object>.execute();
```

[表]
行 1:
  <object>
  Object name to be defined
行 2:
  task1-N
  Object name of the PPMU_SETTING, PPMU_RELAY or
    PPMU_MEASURE class to specify a task to
    be performed. A task list can contain up to 10 tasks.

### Member functions（取自子主题 TASK_LIST）

add()

```
TASK_LIST & add(const TASK& task);
```

This function adds the specified task to the task list. Added tasks are
performed sequentially.

Note
 If you define a
TASK_LIST
 object as
global, the object will not be destroyed when the test method is
completed. This will have the effect that the list grows longer with
every testflow repetition, so that the test time is increased with every
repetition.

[表] Parameter
行 1:
  task
  Object name of the PPMU_SETTING, PPMU_RELAY or
    PPMU_MEASURE class to specify a
    task be performed.

Using the offline result emulation function:

Measurements can be made by using
`DPS_TASK`（raw: `55630.htm`）
,
`SPMU_TASK`（raw: `55670.htm`）
, and

`PPMU_MEASURE`（raw: `29585.htm`）
 objects directly (by calling their

execute()
 member functions) or be put in a

TASK_LIST
 object which queues up tasks to be executed (by calling
the
execute()
 method on the
TASK_LIST
 object
rather than on the task objects themselves). This requires an enhancement also on the

TASK_LIST add()
 method which takes a measurement name as
additional parameter.

```
TASK_LIST& add(const TASK& task)
```

This is the existing function which adds the specified task to the task list.

```
TASK_LIST& add(const TASK& task, const string& measurementName)
```

This function adds the specified task to the task list.

Parameter

[表]
行 1:
  measurementName
  Associate the measurement that will be executed by calling
    task_list.execute() with offline data.

For more details, see
`Parametric offline result emulation`（raw: `128581.htm`）
 in
`Offline Result Emulation`（raw: `128475.htm`）
.

setup()

```
void setup();
```

This function downloads settings defined in the task list. The tasks of
the task list are executed sequentially in the registered order. It is
used when the input parameters of the task are changed during the test
method execution. It can change the parameters of an exisiting MSET and
reuse it to avoid running out of MSETs. (Refer to
`FlexDC`（raw: `122087.htm`）
 and
`Managing DC Tests with Variable Parameters`（raw: `75890.htm`）
 for details.)

Parameters

There are no parameters associated with this function.

execute()

```
void execute();
```

This function performs a test by executing the task list. The tasks of
the task list are executed sequentially in the registered order.

Parameters

There are no parameters associated with this function.

Note
 After the
execute()
 function is performed, you cannot
define any tasks for the digital pin that is not included to the
performed task. For example, the following program defines and executes
the "tasks" task list.

```
PPMU_SETTING setting1;
TASK_LIST tasks;

tasks.add(setting1);

setting1.pin("pin1").vForce(2.1 mV);
setting1.pin("pin1").iRange("10uA");
setting1.pin("pin1").min(0.1 uA).max(5.0 uA);

tasks.execute();
```

After that, you can modify or define tasks for "pin1" as shown below:

```
setting1.pin("pin1").vForce(2.5 mV); // OK
```

However, error occurs if the following program is performed because tasks
for "pin2" is not defined in the "tasks" task list.

```
setting1.pin("pin2").vForce(2.1 mV); // error
```

### Example（取自子主题 TASK_LIST）

In the following example, the task
setting
,
precharge
,

relay_on
,
relay_off
,

ppmuMeasure
,
clamp_on
 and

clamp_off
 are defined and added to the task list. Then a PPMU
measurement is performed by executing the task list.

```
PPMU_SETTING ppmuSetting;
PPMU_RELAY ppmuRelay_on, ppmuRelay_off;
PPMU_MEASURE ppmuMeasure;
PPMU_CLAMP ppmuClamp_on, ppmuClamp_off;
TASK_LIST taskList_1;

ON_FIRST_INVOCATION_BEGIN();

//
// Setups for PPMU
//
ppmuSetting.pin("S0").iRange(1 mA).min(0 V).max(4.3 V).iForce(10 uA);
ppmuSetting.pin("S1").iRange(10 mA).min(-10 uA).max(30 uA).vForce(3.3 V);

//
// Relay setups
//
ppmuRelay_on.pin("S0,S1").status("PPMU_ON");
ppmuRelay_on.wait(1.3 ms);
ppmuRelay_off.pin("S0,S1").status("AC_ON");

//
// Measurement setups
//
ppmuMeasure.pin("S0,S1").execMode(TM::PVAL);

//
// Hardware specific programming to avoid hot switching on the current force setup
//
ppmuClamp_on.pin("S0").status("CLAMP_ON").low(2.6 V).high(2.9 V);
ppmuClamp_off.pin("S0").status("CLAMP_OFF");

//
// Build and execute the task list
//
taskList_1.add(ppmuSetting)
.add(ppmuClamp_on)
.add(ppmuRelay_on)
.add(ppmuClamp_off)
.add(ppmuMeasure)
.add(ppmuRelay_off);

taskList_1.execute();

ON_FIRST_INVOCATION_END();

//
// Result upload and Datalog
//
double VMeas, IMeas;

VMeas = ppmuMeasure.getValue("S0");
IMeas = ppmuMeasure.getValue("S1");

TEST("DC_Test",ppmuMeasure, true);
```

The following example shows how to measure a current on a device pin and then use it
as a force value for a following measurement for multi-sites. The result value of
the first measurement differs from site to site.

```
PPMU_MEASURE ppmuMeasure2;

ON_FIRST_INVOCATION_BEGIN();

PPMU_MEASURE ppmuMeasure1;
PPMU_SETTING ppmuSetting1,ppmuSetting2;
PPMU_RELAY ppmuRelayOn, acRelayOn;
TASK_LIST multiDeltaFlexDc1, multiDeltaFlexDc2;

// 1st measurement
ppmuSetting1.pin("I/O1").vForce(0 V).iRange(1 uA).max(1 uA).min(-1 uA);
ppmuRelayOn.pin("I/O1").status("PPMU_ON");
ppmuRelayOn.wait(1.3 ms);
ppmuMeasure1.pin("I/O1").execMode(TM::PVAL);
acRelayOn.pin("I/O1").status("AC_ON");
multiDeltaFlexDc1.add(ppmuSetting1).add(ppmuRelayOn).add(ppmuMeasure1);
multiDeltaFlexDc1.execute();

// dummy setting for avoiding DC set run out
ppmuSetting2.pin("I/O1").iForce(0 uA).iRange(1 mA).max(0.5 V).min(-0.5 V);
ppmuSetting2.wait(1 ms);
ppmuMeasure2.pin("I/O1").execMode(TM::PVAL);
multiDeltaFlexDc2.add(ppmuSetting2).add(ppmuMeasure2).add(acRelayOn);
multiDeltaFlexDc2.setup();

// 2nd measurement
FOR_EACH_SITE_BEGIN();

ppmuSetting2.pin("I/O1")
.iForce(ppmuMeasure1.getValue("I/O1"))
.iRange(ppmuMeasure1.getValue("I/O1"))
.max(0.5 V)
.min(-0.5 V);

FOR_EACH_SITE_END();

multiDeltaFlexDc2.execute();

ON_FIRST_INVOCATION_END();

TEST("I/O1",
"multi_delta",
ppmuMeasure2.getPassFail("I/O1")?TM::Pass:TM::Fail,
ppmuMeasure2.getValue("I/O1"),
true );
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
