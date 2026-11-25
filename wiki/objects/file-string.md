---
type: object
title: How to create a universal test method class
layer: L2
stage: testmethod
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.02.02.02_How_to_create_a_universal_test_method_class.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# How to create a universal test method class

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

**没有加标记的语法段。** 定义文档里没有 `Syntax` / `Parameters` / `Example`
这类**段标记**。本脚本一个字都不收录——没有段标记时「哪一段是语法」是猜，
而猜就是编。要看原文：`python show.py <分类号>`。

<!-- 语法节 end -->

## 是什么

**文档事实** FileString 是 universal test method 的参数类型之一，用于输入文件名作为测试方法参数的值。

**文档事实** FileString 变量的合法值可以是一个文件名，也可以是逗号分隔的多个文件名；文件名可以是纯文件名，也可以是文件的绝对路径。

**文档事实** 可以用 `()`、`[]`、`{}` 包含数字、字母、`-` 和 `|` 来表示一组名称相似的文件；例如 `abcde(1-3)` 表示 `abcde1, abcde2, abcde3`，`abcd(e|f)` 表示 `abcde, abcdf`。

**文档事实** 检索文件名时，`()`、`[]`、`{}` 中的数字和字母按 `()`、`[]`、`{}` 的顺序展开。

**文档事实** 创建测试方法类时，FileString 与 int、double、string、PinString、SpecVariable、SpecValue、ContextPins、OptionList 并列出现在参数 Type 列表中。

## 典型用法

**文档事实** 在 “Create a new TestMethod class” 向导的 Parameters 区域添加参数时，把 Type 选为 FileString，并填写 Identifier、Variable、Default、Options、Comment；Options 的候选值用冒号分隔，参数名可用 `.` 建立层级。

**文档事实** 代码中在 `initialize()` 里用 `addParameter("参数名","FileString",&成员变量,mode)` 定义参数；`mode` 可选 `TM_PARAMETER_INPUT` 或 `TM_PARAMETER_OUTPUT`，返回的 `TestMethodParameterProxy` 可链式调用 `setDefault()`、`setOptions()`、`setComment()` 等。

**文档事实** FileString 提供以下成员函数：`getFileNames()` 取变量中的文件名；`getFileNamesWithPath()` 取带绝对路径的文件名；`getFileNamesWithRelativePath()` 取相对于当前 device 的文件名（该小节标题写作 `getFileNameWithRelativePath()`，但签名是复数形式）；`getFileNamesWithPathNoExp()` 取不展开 `()`、`[]`、`{}` 中数字和字母的文件名；`setFileString(const std::string &value)` 设置变量值；`operator=` 把一个 FileString 对象复制到另一个对象。

**文档事实** 文档示例中 `mFile1` 是 FileString 类型的变量，示例分别调用 `getFileNames()`、`getFileNamesWithPath()`、`getFileNamesWithRelativePath()`，再按索引循环打印三组文件名。

**建议** 批量且命名有规律的文件用 `()`/`[]`/`{}` 简写，避免在 test suite 中逐个列举。

## 和谁有关

- **文档事实** FileString 独立条目 `02.07.02.13.01_FileString.htm`（另有同内容条目 `02.07.04.02.10_FileString.htm`），源文档链接到它，给出类型定义、取值语法、成员函数、示例与版本。
- **文档事实** addParameter，参数表把 FileString 列为可用参数类型并说明其用于输入文件名；Functional changes 记 SmarTest 7.2.1 起支持 FileString。
- **文档事实** OptionList、PinString、SpecVariable、SpecValue、ContextPins，源文档把 FileString 与它们并列为参数类型。
- **文档事实** TestMethodParameterProxy，`addParameter` 返回该代理对象，可链式设置默认值、选项与注释。
- **文档事实** Parameter types defined for universal test method，其 Subtopics 列出 FileString。
- **文档事实** How to create a universal test method class，是 FileString 独立条目 Related information 中指回的创建流程。

## 版本

**文档事实** FileString 独立条目的 Functional changes 只记一条：Introduced in SmarTest 7.2.1。

**文档事实** addParameter 的 Functional changes 记载：SmarTest 7.2.1 起支持 FileString 参数类型。

## 出处

- `02_System_reference/02.07_Test_Method_Reference/02.07.02.02.02_How_to_create_a_universal_test_method_class.htm`，主源，含参数类型列表、FileString 用途与向导步骤。
- `02_System_reference/02.07_Test_Method_Reference/02.07.02.13.01_FileString.htm`，含类型定义、取值语法、成员函数、示例、Related information 与 Functional changes（已用 show.py 读取）。
- `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.03_addParameter.htm`，含 API 形式与 7.2.1 支持记录（已用 show.py 读取）。
- `02_System_reference/02.07_Test_Method_Reference/02.07.02.13.05_TestMethodParameterProxy.htm`，用于核对代理对象的链式调用（已用 show.py 读取）。
- `02_System_reference/02.07_Test_Method_Reference/02.07.02.13_Parameter_types_defined_for_universal_test_method.htm`，用于核对 Subtopics 中的 FileString 条目（已用 show.py 读取）。
