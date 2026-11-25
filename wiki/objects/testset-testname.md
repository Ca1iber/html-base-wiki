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

**文档事实** TESTSET 的成员函数 testname() 为测试结果设置测试名，名称由 name 参数直接给出，写入 EDL 时存为 TestName 属性。

**文档事实** 它用于给测试结果指定期望的名字，替代 TEST() API 自动生成的值。对功能测试结果这类本来就没有测试名的结果，在用 testnumber() 的整数形式或 TESTNUMBER 对象形式给对应结果分配数值时尤其有用。

**文档事实** 第二个参数 forceSTDFTestName 为 true 时，data formatter 把 name 原样写入 TSR 记录的 TEST_NAM 字段。为 false 时，data formatter 由测试套件名、测试名和 pin 名计算 TEST_NAM 字段内容。该参数可选，默认 false。

**文档事实** 测试名可包含任何可打印 ASCII 字符，即编码 32 到 126 的字符，包括空格、数字、大小写字母以及一组标点字符。SmarTest 对名称没有固定最大长度，但 STDF 把测试名限为 255 字符，因此若打算做 STDF 数据记录，名称不应超过该长度。

**文档事实** 在 SMC_backgroundProcessing() 测试方法中，hidden_datalog_mode 为 0 时不支持本函数。hidden_datalog_mode 为 1 或 2 时支持。

## 典型用法

**文档事实** 最小示例为 `TESTSET().testname("Sample_test");`。

**文档事实** 文档说明该名称在随后调用某个 TEST() 方法时使用，因此调用顺序是先 testname() 再 TEST() 或 judgeAndLog_* 结果方法。

**文档事实** judgeAndLog_* 系列方法的文档写明其可选值可由先前方法设置，例如 port()、cont()、reliability() 或 testname()。

**文档事实** 与 testnumber() 配合时，testnumber() 给结果分配编号，testname() 给同一结果命名。testnumber() 的 name 形式也可在需要时把名字记入 EDL。

**文档事实** testname_default() 取消先前 testname() 设置的名字并回到默认模式，且只能在该 testname() 调用之后使用。默认模式使用 TEST() 方法给出的名字或 TEST() API 自动生成的名字。

**建议** 若计划输出 STDF 数据，把测试名控制在 255 字符以内。

## 和谁有关

**文档事实** TESTSET `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244_TESTSET.htm`。本函数是其成员函数，本页 Related information 只列 TESTSET。

**文档事实** TESTSET().testname_default() `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244.24_TESTSET__.testname_default.htm`。它取消本函数设置的名字并回到默认模式，只在本函数执行后使用，所以两者成对出现。

**文档事实** TESTSET().testnumber() `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244.25_TESTSET__.testnumber.htm`。它给没有测试名的结果分配编号，本页正文把本函数与 testnumber 的两种形式并列说明为配合使用。

**文档事实** TEST() `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.241_TEST.htm`。名称在随后调用某个 TEST 方法时使用，本函数用于替代 TEST API 自动生成的名字。

**文档事实** judgeAndLog_* 系列 `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244.06` 到 `02.07.04.01.244.17`。这些方法的文档写明可选值可由 testname() 等先前方法设置。

**文档事实** TestNameAttribute `02_System_reference/02.10_Data_Logging/02.10.01.06.05.61_TestNameAttrType.htm`。名称在 EDL 中的存储类型。

**文档事实** TSR 记录 `02_System_reference/02.10_Data_Logging/02.10.03.05.26_Test_Synopsis_Record__TSR.htm`。forceSTDFTestName 为 true 时名称写入其 TEST_NAM 字段。

**文档事实** Hidden data logging `02_System_reference/02.07_Test_Method_Reference/02.07.10.04.09_Hidden_data_logging.htm` 与 `03_Use_cases_and_application_papers/03.01_Performance_Cookbook__How_to_reduce_test_times/03.01.05.05_Hidden_data_logging.htm`。这两篇引用本函数。本页正文另说明 hidden_datalog_mode 与 SMC_backgroundProcessing() 下的支持条件。

**文档事实** Test summary tab `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.02.01_Test_summary_tab.htm`。其 Test 字段显示由 TESTSET.testname() 指定的测试名。

**文档事实** TESTSET().suppressTestNameLoopCount `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244.22_TESTSET__.suppressTestNameLoopCount.htm`。它同属测试名控制的一组，引用本函数。

## 版本

**文档事实** Functional changes 记载，Introduced before SmarTest 6.3.2。SmarTest 7.1.2 新增 forceSTDFTestNam 参数。SmarTest 7.5.2 将该参数更名为 forceSTDFTestName。原文在 7.1.2 条目中把参数写作 forceSTDFTestNam，比现在的拼写少一个 e。

## 出处

- `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244.23_TESTSET__.testname.htm`。主源，含正文、Syntax、Example、Related information、Functional changes。
- `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244.24_TESTSET__.testname_default.htm` 与 `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.244.25_TESTSET__.testnumber.htm`。用于确认与本函数的成对关系与配合方式。
