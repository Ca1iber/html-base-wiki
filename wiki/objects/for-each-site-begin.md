---
type: object
title: FOR_EACH_SITE_BEGIN
layer: L2
stage: testmethod
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.70_FOR_EACH_SITE_BEGIN.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# FOR_EACH_SITE_BEGIN

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,596 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.70_FOR_EACH_SITE_BEGIN.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
FOR_EACH_SITE_BEGIN();
```

List of parameters

There are no parameters.

Return value

There is no return value.

### Examples

### Example 1: Minimum code

The following example shows the minimum code for
a "each site loop block". The ellipses ("...") are to be replaced with your
code.

```
ON_FIRST_INVOCATION_BEGIN();
...
...
FOR_EACH_SITE_BEGIN();
...
...
FOR_EACH_SITE_END();
...
...
ON_FIRST_INVOCATION_END();
```

### Example 2: Optional curly brackets

The example utilizes optional pairs
of curly brackets "{" and "}". These optional curly brackets are used for simplifying the
correct indentation with assistance of the related Eclipse
tool.

```
ON_FIRST_INVOCATION_BEGIN();
{
...
...
FOR_EACH_SITE_BEGIN();
{
...
...
}
FOR_EACH_SITE_END();
...
...
}
ON_FIRST_INVOCATION_END();
```

### Example 3
```
ON_FIRST_INVOCATION_BEGIN();
{
//
// Pre-measurement
//
PMU_IFVM pmuIfvm("Aout_trig");
...
...

//
// Serial execution for all Sites - BEGIN
//
FOR_EACH_SITE_BEGIN();
{
//
// Get pre-measurement result for each site
//
DOUBLE V_off = pmuIfvm.getValue("Aout_trig");

//
// Set pre-measurement result for each site
// as site-specific setup condition
//
DGT("Aout").vOffset(V_off);

//Serial Execution for All Sites - END
}
FOR_EACH_SITE_END();

//
// Setup and test Execution on all active sites
//
EXECUTE_TEST(0.1 sec);
...
...
}
ON_FIRST_INVOCATION_END();
```

FOR_EACH_SITE_BEGIN()

and
FOR_EACH_SITE_END()
 declare the each site loop block in the
first-invocation block. All APIs in each site loop block are executed serially for all sites
when the program is run for the first tested site.

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
