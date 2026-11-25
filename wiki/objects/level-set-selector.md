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

（待补）

## 典型用法

（待补）

## 和谁有关

（待补）

## 版本

（待补）

## 出处

（待补）
