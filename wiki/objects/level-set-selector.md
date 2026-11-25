---
type: object
title: LevelSetSelector
layer: L2
stage: level
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.123_LevelSetSelector.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# LevelSetSelector

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,696 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.123_LevelSetSelector.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

The available constructors are listed as follows:

LevelSetSelector()
;

This is the default constructor referring to the
primary level set.

LevelSetSelector(const LevelSetSelector
&
rhs
);

Or,

LevelSetSelector(const LevelSetSelector*

rhs
);

These two constructors refer to an existing LevelSetSelector object.

LevelSetSelector(INT

levelSetId
);

This constructor refers an
existing level set, which can be a fixed level set or an equation based level set.

LevelSetSelector(DIGITAL_OFFSET_SEARCH::PRM_ALL
levelSet
);

This
constructor refers to either the primary level set or all fixed level sets.

[表] Parameters
列: Parameter | Description
行 1:
  rhs
  An existing LevelSetSelector object
行 2:
  levelSetId
  For a fixed level setup, it is the level set number.
    
    For an equation based level setup, the level set ID is calculated as follows:
    
    equset * 100000 + specset * 1000 + level_set_no
行 3:
  levelSet
  DIGITAL_OFFSET_SEARCH::PRM or
    DIGITAL_OFFSET_SEARCH::ALL.
    
    DIGITAL_OFFSET_SEARCH::PRM: Refers to the primary level set, which
    is identical to the use of the default constructor.
    
    DIGITAL_OFFSET_SEARCH::ALL: Refer to all fixed level sets.

Return value

There is no return value.

### Example

Upload the VIH offsets of all fixed level sets for the pin
"pcie_rx1n".

```
STRING strpins("pcie_rx1n");
DIGITAL_OFFSET_SEARCH_TASK dos;
DIGITAL_OFFSET_SEARCH::LevelSetSelector dest(DIGITAL_OFFSET_SEARCH::ALL);

dos.pin(strpins).resourceType(DIGITAL_OFFSET_SEARCH::VIH).searchType(DIGITAL_OFFSET_SEARCH::EYE)
.start(15).numSteps(120).stepWidth(15).restoreFlag(DIGITAL_OFFSET_SEARCH::NO);
dos.execute();

dos.uploadResult(dest, DIGITAL_OFFSET_SEARCH::VIH);
```

<!-- 语法节 end -->

## 是什么

**文档事实**：`LevelSetSelector` 是一个 C++ 类，指向单个 level set 或全部 fixed level set，供 `DIGITAL_OFFSET_SEARCH_TASK` 与 `DIGITAL_OFFSET_SEARCH_PINS` 使用。它定义在头文件 `/opt/hp93000/soc/prod_com/include/MAPI/DigitalOffsetSearchTypes.h`。

**文档事实**：构造方式决定它指向什么：

- 默认构造 `LevelSetSelector()` 指向 primary level set；
- 拷贝构造（引用或指针）指向一个已有的 `LevelSetSelector` 对象；
- `LevelSetSelector(INT levelSetId)` 指向一个已有 level set，可以是 fixed level set 或 equation based level set；equation based 的 ID 按 `equset * 100000 + specset * 1000 + level_set_no` 计算；
- `LevelSetSelector(DIGITAL_OFFSET_SEARCH::PRM_ALL levelSet)` 传 `DIGITAL_OFFSET_SEARCH::PRM` 时等同默认构造（primary），传 `DIGITAL_OFFSET_SEARCH::ALL` 时指向全部 fixed level set。

**文档事实**：本类没有 return value（文档 `Return value` 段如此写）。

## 典型用法

**文档事实**：文档示例把 selector 构造成 `DIGITAL_OFFSET_SEARCH::ALL`，作为 `DIGITAL_OFFSET_SEARCH_TASK::uploadResult` 的目标，把 pin `pcie_rx1n` 上所有 fixed level set 的 VIH offset 上传回去：

```cpp
STRING strpins("pcie_rx1n");
DIGITAL_OFFSET_SEARCH_TASK dos;
DIGITAL_OFFSET_SEARCH::LevelSetSelector dest(DIGITAL_OFFSET_SEARCH::ALL);

dos.pin(strpins).resourceType(DIGITAL_OFFSET_SEARCH::VIH).searchType(DIGITAL_OFFSET_SEARCH::EYE)
.start(15).numSteps(120).stepWidth(15).restoreFlag(DIGITAL_OFFSET_SEARCH::NO);
dos.execute();

dos.uploadResult(dest, DIGITAL_OFFSET_SEARCH::VIH);
```

**推断**：结合本页只列出构造方式、没有成员函数说明，以及示例中它仅作为 `uploadResult` 的实参，可以判断这个类只负责「选哪些 level set」，搜索与上传动作由 `DIGITAL_OFFSET_SEARCH_TASK` 完成。

## 和谁有关

**文档事实**：以下关系均有来源文档中的正文、参数说明或回链证据支撑。

- `DIGITAL_OFFSET_SEARCH_TASK`（`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.36_DIGITAL_OFFSET_SEARCH_TASK.htm`）：本页正文直接说明该类供它使用；其 `uploadOffset`、`uploadResult`、`enableAutoOffsetUpload`、`enableAutoResultsUpload` 的文档都把 `LevelSetSelector` 对象作为选择 level set 的参数。
- [[digital-offset-search-pins]]：本页正文直接说明该类也供它使用；其 `uploadOffset`、`uploadResult`、`getOffset`、`DigitalOffsetResultCopy`（源/目标 level set）与 `DigitalOffsetResultReset` 都要求 `LevelSetSelector` 对象。
- [[timing-set-selector]]：本页 `Related information` 只列了它，属于同类 set selector 的交叉引用。
- **头文件** `DigitalOffsetSearchTypes.h`：本页第一段明确写出本类声明所在。

## 版本

**文档事实**：`Functional changes` 写 `Introduced in SmarTest 7.2.1`。

## 出处

- 主源（也是「语法 / 参数」的逐字来源）：`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.123_LevelSetSelector.htm`（正文、Syntax、Parameters、Example、Related information、Functional changes）。
- 回链证据：`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.36_DIGITAL_OFFSET_SEARCH_TASK.htm`（及其 `uploadOffset` / `uploadResult` / `enableAuto*` 成员页）、`02_System_reference/02.07_Test_Method_Reference/02.07.04.02.17_TimingSetSelector.htm`。
