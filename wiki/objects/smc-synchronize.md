---
type: object
title: SMC_SYNCHRONIZE()
layer: L2
stage: testmethod
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.231.43_SMC_SYNCHRONIZE.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# SMC_SYNCHRONIZE()

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **2,342 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.231.43_SMC_SYNCHRONIZE.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
Boolean SMC_SYNCHRONIZE(DOUBLE timeout = 0);
Boolean SMC_SYNCHRONIZE(DOUBLE timeout, Boolean forceErrorExitOnFail);
Boolean SMC_SYNCHRONIZE(INT *noOfSMCExecutedTests, DOUBLE timeout = 0);
Boolean SMC_SYNCHRONIZE(INT *noOfSMCExecutedTests, DOUBLE timeout, Boolean forceErrorExitOnFail);
```

This
API is defined in the header file

/opt/hp93000/soc/prod_com/include/MAPI/SMART_CALC2.h
.

Parameters
[表]
列: Parameter | Description/Range
行 1:
  timeout
  The time in seconds after which a thread should be
    canceled and SMC_SYNCHRONIZE()
    should not wait for its completion.
    
    Resolution: 1 µs
    
    The accuracy of this parameter is influenced by the
    overhead time of the operating system.
    
    The default value is 0.0 seconds which means that no timeout is set.
行 2:
  noOfSMCExecutedTests
  References a pointer to store the number of `SMC_TEST()`（raw: `120084.htm`） statements
    which have been executed during this synchronize operation per site.
    
    Note
    
    When using the class SMC_ARM_FOR_SITES() or
    SMC_ARM_OTHER_TS_FOR_SITES(),
    SMC_SYNCHRONIZE() does not not return a test count. As a result,
    noOfSMCExecutedTests is not incremented and does not count the
    number of calls to SMC_TEST().
行 3:
  forceErrorExitOnFail
  Enables a forced exit on an error. If set to
    
    true - it causes an
    exception in case a calculation routine had to be
    aborted.
    
    false - it causes
    SMC_SYCHRONIZE() to return
    false in case a calculation
    routine had to be aborted.
Return value

Returns
false
 in case threads had to be terminated or an invocation error
occurred, else
true
 is returned.

If the
noOfSMCExecutedTests
 parameter is used, the number of
`SMC_TEST()`（raw: `120084.htm`）
 statements which have been executed during this
synchronize operation per site will be stored in the integer variable
referenced by the pointer.

### Example

Waits for all calculations to be finished within 100 ms. After the timeout of
100 ms all other still running calculation threads will be
terminated!

```
SMC_SYNCHRONIZE(100 ms);
```

Waits for all
calculations to be finished within 10 ms. After the timeout of 10 ms all other still
running calculation threads will be terminated! In case a calculation had to
terminated,
SMC_SYNCRONIZE()
 throws an
exception.

```
SMC_SYNCHRONIZE(10 ms, true);
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
