---
type: object
title: ON_FIRST_INVOCATION_BEGIN
layer: L2
stage: testmethod
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.138_ON_FIRST_INVOCATION_BEGIN.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# ON_FIRST_INVOCATION_BEGIN

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,612 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.138_ON_FIRST_INVOCATION_BEGIN.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
ON_FIRST_INVOCATION_BEGIN();
```

This API is defined in the header file

/opt/hp93000/soc/prod_com/include/MAPI/MapiUtil.h
.

List of parameters
There are no parameters.
Return value
There is no return value.

### Examples

### Example 1: Minimum code

The following example shows the minimum code for
a "first-invocation block". The ellipses ("...") are to be replaced with your
code.

```
ON_FIRST_INVOCATION_BEGIN();
...
...
ON_FIRST_INVOCATION_END();
```

### Example 2: Optional curly brackets

The example utilizes an optional pair
of curly brackets "{" and "}". These optional curly brackets are used for simplifying the
correct indentation with assistance of the related Eclipse
tool.

```
ON_FIRST_INVOCATION_BEGIN();
{
...
...
}
ON_FIRST_INVOCATION_END();
```

### Example 3
```
//
// Parallel Execution for All Sites - BEGIN
//
ON_FIRST_INVOCATION_BEGIN();

//
// Setup and Test Execution
//
Routing.pin("Aout").connect(TM::SINGLE);
Analog.DGT("Aout").enable();
EXECUTE_TEST(0.1 sec);

//
// Retrieve measured analog waveform
//
ARRAY_D AnaWave = Analog.DGT("Aout").getWaveform();
Routing.pin("Aout").disconnect();
Analog.DGT("Aout").disable();

FLUSH();

//
// Parallel Execution for All Sites - END
//
ON_FIRST_INVOCATION_END();
...
...
```

ON_FIRST_INVOCATION_BEGIN
 and

ON_FIRST_INVOCATION_END
 declare the first-invocation block. All APIs in
this block are executed for all sites in parallel once only when the program is run for the first
tested site. Hence, the analog modules on the all connected site, specified by the "Aout" pin,
are enabled and then the measurements are done on all connected sites.

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
