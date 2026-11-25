---
type: object
title: Structure of an equation based level setup
layer: file
stage: level
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.04.02_Structure_of_an_equation_based_level_setup.htm
  - 02_System_reference/02.06_Command_Reference/02.06.05.01.05_Data_Organization_of_Fixed_Levels.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Structure of an equation based level setup

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **410 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.05.01.04.02_Structure_of_an_equation_based_level_setup.htm>` 及其子主题 `<02_System_reference/02.06_Command_Reference/02.06.05.01.04.02.03_Specs_module.htm>`、`<02_System_reference/02.06_Command_Reference/02.06.05.01.04.02.06.01_Pin_exclusion.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Specs module）

```
SPECS
vcc_level [V] # Base vcc voltage
vcc_offset [V] # Offset to add to vcc_level
```

### Syntax（取自子主题 Pin exclusion）

```
PINS <pin list> [-( <exclude pin list> )] [# comment]
```

Note
 You must type a blank between the left parenthesis and
<exclude pin
list>
 and a blank between
<exclude pin list>
 and the
right parenthesis.

### Example（取自子主题 Pin exclusion）

```
LEVELSET 1 "normal"
PINS I_PINS -( i1+@diff ) # remove pair
vil=0
vih=4.3

PINS i1+@diff
vil=0
vih=3.3
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
