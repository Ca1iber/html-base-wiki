---
type: object
title: TESTSET().testname()
layer: L2
stage: results
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244.23_TESTSET__.testname.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# TESTSET().testname()

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,202 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244.23_TESTSET__.testname.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
TESTSET & testname(const STRING &name);
TESTSET & testname(const STRING &name, const bool forceSTDFTestName);
```
[表]
列: Parameter | Description
行 1:
  name
  The test name that is stored in the EDL as a `TestNameAttribute`（raw: `34701.htm`） for a test result. Used when one of the `TEST`（raw: `29803.htm`）
    methods is subsequently called.
    
    Test names can contain any printable ASCII characters, that is, characters with codes from 32
    to 126. This includes the space, digits, lowercase letters, uppercase letters, and these
    punctuation characters: !"#$%&'()*+,-./:;<=>@?[\]^_`{|}~ There is no fixed maximum length
    for the names in SmarTest. However, STDF limits test names to 255 characters, so test names
    should not be longer if STDF data logging is intended.
行 2:
  forceSTDFTestName
  If this parameter is true, the data formatter writes the
    name value name directly into the TEST_NAM field of the `TSR record`（raw: `69139.htm`）.
    
    If the parameter is false, the data formatter calculates the content
    of the TEST_NAM field from the test suite name, test name, and pin name.
    
    This parameter is optional. The default is false.

### Example

```
TESTSET().testname("Sample_test");
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
