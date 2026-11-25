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

**文档事实** SMC_SYNCHRONIZE() 等待所有由 `SMC_ARM()` 启动的线程执行结束；这些线程完成 upload 与计算任务后，排队的 `SMC_TEST()` 语句会被执行，以完成 data logging 与 binning。

**文档事实** 若使用 Hidden data logging，binning 不在 `SMC_SYNCHRONIZE()` 中处理，而在 `SMC_backgroundProcessing()` 方法中处理。

**文档事实** 它必须按 site 调用，因此要放在 `ON_FIRST_INVOCATION` 块之外；对于 "thread per site"、"common thread" 及两者混用的 testflow，文档指向 SmartCalc recommendations 中的同步说明。

**文档事实** 语法提供四个重载：可设 `timeout`（默认 0 表示不设超时，分辨率 1 µs）、可选 `forceErrorExitOnFail`（true 抛异常、false 返回 false）、可选 `noOfSMCExecutedTests`（按 site 保存本次同步期间执行的 `SMC_TEST()` 数量）。

## 典型用法

**文档事实** `SMC_SYNCHRONIZE(100 ms);` 等待所有计算在 100 ms 内完成；超时后仍运行的线程会被终止。

**文档事实** `SMC_SYNCHRONIZE(10 ms, true);` 同样等待 10 ms，但若有计算被终止则抛出异常。

**文档事实** 需要统计本次同步执行的 `SMC_TEST()` 数量时，传入 `INT*` 形式的 `noOfSMCExecutedTests`；但使用 `SMC_ARM_FOR_SITES()` 或 `SMC_ARM_OTHER_TS_FOR_SITES()` 时不会返回测试计数。

**文档事实** 返回值在需要终止线程或发生 invocation error 时为 false，否则为 true。

## 和谁有关

- `SMC_ARM()`：**文档事实** 本页定义它等待由 `SMC_ARM()` 启动的线程结束。
- `SMC_TEST()`：**文档事实** 其排队的语句在本调用时执行 data logging 与 binning；本页 `noOfSMCExecutedTests` 计数的也是这类语句。
- `SMC_SYNCHRONIZE_WITHOUT_BINNING()`：**文档事实** 本页 Related information 将其列为相关 API（不执行 binning 的同步变体）。
- `ON_FIRST_INVOCATION_BEGIN`：**文档事实** 本页要求 SMC_SYNCHRONIZE() 按 site 调用，因而位于 `ON_FIRST_INVOCATION` 块之外。
- `SMC_CLEANUP()`：**文档事实** 该 API 文档建议，当 site 无法与 `SMC_SYNCHRONIZE()` 同步时，在 bin_disconnect 例程中用 `SMC_CLEANUP()` 终止该 site 的线程。
- `SMC_DISABLE()`：**文档事实** 该 API 文档说明，即使 SmartCalc 被禁用，只要 `synchImmediately` 为 false，仍须调用 `SMC_SYNCHRONIZE()`；为 true 时才能省略。

## 版本

**文档事实** Introduced in SmarTest 6.5.3；SmarTest 6.5.3 Patch 1 新增 `noOfSMCExecutedTests` 参数；7.1.3 新增 hidden data logging（数据记录功能）；7.2.1 Patch 1 新增 `forceErrorExitOnFail` 参数。

## 出处

- `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.231.43_SMC_SYNCHRONIZE.htm`
