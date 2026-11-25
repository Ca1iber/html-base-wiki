---
type: object
title: TimingSetSelector
layer: L2
stage: timing
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.02.17_TimingSetSelector.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# TimingSetSelector

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **2,522 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.02.17_TimingSetSelector.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

The default constructor
TimingSetSelector()
 is equal to

TimingSetSelector(DIGITAL_OFFSET_SEARCH::PRM, DIGITAL_OFFSET_SEARCH::PRM).
R
 efers to the primary timing set.

The available constructors
are:

```
TimingSetSelector();
TimingSetSelector (const TimingSetSelector& rhs);
TimingSetSelector (const TimingSetSelector* rhs);
TimingSetSelector (const STRING& multiportspec, INT timingset);
TimingSetSelector (INT waveformORspecId, INT timingset);
TimingSetSelector (DIGITAL_OFFSET_SEARCH::PRM_ALL waveformOrSpec,
INT timingset);
TimingSetSelector (const STRING& multiportspec,
DIGITAL_OFFSET_SEARCH::PRM_ALL timingset);
TimingSetSelector (INT waveformOrSpecId,
DIGITAL_OFFSET_SEARCH::PRM_ALL timingset);
TimingSetSelector (DIGITAL_OFFSET_SEARCH::PRM_ALL waveformOrSpec,
DIGITAL_OFFSET_SEARCH::PRM_ALL timingset);
TimingSetSelector(const TimingSetSelector & rhs, INT timingSet);
TimingSetSelector(const STRING& waveformOrSpec, const STRING& timingSet);
TimingSetSelector(const STRING& timingSelector);
```
[表] Parameters
列: Parameter | Description
行 1:
  rhs
  The name of an existing TimingSetSelector object.
行 2:
  multiportspec
  The name of a multi-port specification, in a multi-port setup.
行 3:
  waveformORspecId (INT)
  In fixed timing setup, it is the waveform set number.
    
    In equation based timing setup, it is a timing specification ID calculated as
    follows:
    
    100*equation_set_no + specset_no
行 4:
  waveformOrSpec
    (DIGITAL_OFFSET_SEARCH::PRM_ALL)
  It can be:
    
    DIGITAL_OFFSET_SEARCH::PRM: Selects the primary
    specification
    
    DIGITAL_OFFSET_SEARCH::ALL: Selects all waveform sets in the
    fixed timing set.
    Note that this option is only supported for waveform sets, not for
    specification ID's.
行 5:
  timingset
    
    (INT)
  The timing set number to select.
行 6:
  timingset
    
    (DIGITAL_OFFSET_SEARCH::PRM_ALL)
  It can be:
    
    DIGITAL_OFFSET_SEARCH::PRM: Selects the current primary timing
    set.
    
    DIGITAL_OFFSET_SEARCH::ALL: Selects all timing sets in a timing
    set group.

Return value

There is no return value.

### Example

```
DIGITAL_OFFSET_SEARCH_TASK dos;
STRING strpins1("pcie_tx1n");
DIGITAL_OFFSET_SEARCH::TimingSetSelector dest("multi_port", DIGITAL_OFFSET_SEARCH::ALL);

dos.pin(strpins1).resourceType(DIGITAL_OFFSET_SEARCH::RECEIVE).searchType(DIGITAL_OFFSET_SEARCH::EYE)
.start(15).numSteps(120).stepWidth(15)
.restoreFlag(DIGITAL_OFFSET_SEARCH::NO);
dos.execute();
dos.uploadResult(dest, DIGITAL_OFFSET_SEARCH::ALL_EDGES);
```

<!-- 语法节 end -->

## 是什么

**文档事实** TimingSetSelector 类表示单个 timing set 或全部 fixed timing set。

**文档事实** 它与 DIGITAL_OFFSET_SEARCH_TASK 和 DIGITAL_OFFSET_SEARCH_PINS 一起使用；类定义在头文件 `/opt/hp93000/soc/prod_com/include/MAPI/DigitalOffsetSearchTypes.h`。

**文档事实** 构造需要两个参数：第一个选择 waveform set（fixed timing）、timing specification（equation based timing）或 multi-port specification；第二个从该 waveform set/specification 中选择一个或全部 timing set。对 multi-port specification，selector 指向的 port 由 DIGITAL_OFFSET_SEARCH_TASK 对象的 pin list 决定。

**文档事实** 默认构造 `TimingSetSelector()` 等价于 `TimingSetSelector(DIGITAL_OFFSET_SEARCH::PRM, DIGITAL_OFFSET_SEARCH::PRM)`，指向 primary timing set。

**文档事实** 参数语义：INT 型 waveformORspecId 在 fixed timing 下是 waveform set 号，在 equation based timing 下是 `100*equation_set_no + specset_no` 的 timing specification ID；DIGITAL_OFFSET_SEARCH::PRM 选 primary specification 或当前 primary timing set；DIGITAL_OFFSET_SEARCH::ALL 在 waveform 参数上选 fixed timing set 中全部 waveform set（仅支持 waveform set，不支持 specification ID），在 timingset 参数上选 timing set group 中全部 timing set。

## 典型用法

**文档事实** 源页示例先创建 `DIGITAL_OFFSET_SEARCH_TASK dos` 与 `TimingSetSelector dest("multi_port", DIGITAL_OFFSET_SEARCH::ALL)`，设置 dos 的 pin/resourceType/searchType/start/numSteps/stepWidth/restoreFlag 后执行 `dos.execute()`，再调用 `dos.uploadResult(dest, DIGITAL_OFFSET_SEARCH::ALL_EDGES)`，把结果上传到 selector 选定的 timing set。

**文档事实** 该类也被 DIGITAL_OFFSET_SEARCH 的其他上传/读取接口用作 timing set 选择参数，例如 uploadOffset/uploadResult、getOffset、DigitalOffsetResultCopy/Reset。

**文档事实** 源页说明该类没有返回值（构造函数）。

## 和谁有关

- **文档事实** DIGITAL_OFFSET_SEARCH_TASK：本页明确说明 TimingSetSelector 与它一起使用；示例与 uploadOffset/uploadResult、enableAutoOffsetUpload、enableAutoResultsUpload 都用它选择 timing set，且对 multi-port 而言 selector 的 port 由该 task 的 pin list 决定。
- **文档事实** DIGITAL_OFFSET_SEARCH_PINS：本页明确说明 TimingSetSelector 与它一起使用；uploadOffset/uploadResult、getOffset、DigitalOffsetResultCopy、DigitalOffsetResultReset 等接口以 TimingSetSelector 参数指定 timing set。
- **文档事实** LevelSetSelector：本页 Related information 指向它，作为 level 侧对应的 selector 类。
- **文档事实** DIGITAL_OFFSET_SEARCH_TASK.uploadResult() 的 dest 参数：该页说明它接收用 TimingSetSelector 定义的 dest 对象，用于选择结果要上传到的 timing set。

## 版本

**文档事实** Functional changes 记 Introduced in SmarTest 7.2.1。

## 出处

- `02_System_reference/02.07_Test_Method_Reference/02.07.04.02.17_TimingSetSelector.htm`，主源，含类说明、构造与参数语义、示例、Related information 与 Functional changes。
