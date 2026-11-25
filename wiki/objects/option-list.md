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

**文档事实** OptionList 是 universal test method 的参数类型之一，用于输入多个选项作为该类型参数的值。

**文档事实** 它定义一个包含 string 元素的 vector；vector 是标准 C++ 容器，OptionList 变量可以使用 vector 的全部成员函数，例如查询容量、访问元素和修改元素。

**文档事实** addParameter 文档把 OptionList 的用途表述为 “select multiple options”（选择多个选项）；创建测试方法类的源文档则表述为 “enter multiple options”（输入多个选项），并链接到 OptionList 独立条目。

**文档事实** 在 test suite 的 Properties 视图中输入多个选项时，选项之间只用逗号分隔。

## 典型用法

**文档事实** 在 “Create a new TestMethod class” 向导的 Parameters 区域把 Type 选为 OptionList，并填写 Identifier、Variable、Default、Options、Comment；Options 的候选值用冒号分隔，参数名可用 `.` 建立层级。

**文档事实** 文档示例定义 `class TryOptionList : public testmethod::TestMethod`，成员为 `vector<std::string> mOpt1`；`initialize()` 中调用 `addParameter("opt1","OptionList",&mOpt1,testmethod::TM_PARAMETER_INPUT).setOptions("a:1:2:3:4:5:6")`。

**文档事实** 示例的 `run()` 遍历 `mOpt1.size()`，逐个打印选项；类以 `REGISTER_TESTMETHOD("TryOptionList", TryOptionList)` 注册。

**文档事实** 在 test suite Properties 视图中，多个选项值用逗号分隔输入；向导中的 Options 候选值则用冒号分隔。

**文档事实** addParameter 的 Functional changes 记载：SmarTest 7.2.0 起支持 ContextPins 与 OptionList 参数类型。

## 和谁有关

- **文档事实** OptionList 独立条目 `02.07.02.13.02_OptionList.htm`（另有同内容条目 `02.07.04.02.12_OptionList.htm`），源文档链接到它，给出 vector 语义、Properties 视图输入规则、示例与版本。
- **文档事实** addParameter，参数表列出 OptionList 并说明其多选项用途，Related information 也链接 OptionList；Functional changes 记 7.2.0 起支持。
- **文档事实** PinString、FileString、SpecVariable、SpecValue、ContextPins，源文档把 OptionList 与它们并列为参数类型。
- **文档事实** TestMethodParameterProxy，`addParameter` 返回该代理对象；其 `getType()` 文档列出的参数类型包含 OptionList。
- **文档事实** C++ 标准库 vector，OptionList 变量可使用 vector 的全部成员函数，独立条目给出 cplusplus.com 的 vector 参考链接。
- **文档事实** Test suite Properties view，是输入多个选项（逗号分隔）的位置。
- **文档事实** Parameter types defined for universal test method，其 Subtopics 列出 OptionList。

## 版本

**文档事实** OptionList 独立条目的 Functional changes 只记一条：Introduced in SmarTest 7.2.0。

**文档事实** addParameter 的 Functional changes 记载：SmarTest 7.2.0 起支持 ContextPins 与 OptionList 参数类型。

## 出处

- `02_System_reference/02.07_Test_Method_Reference/02.07.02.02.02_How_to_create_a_universal_test_method_class.htm`，主源，含参数类型列表、OptionList 用途与向导步骤。
- `02_System_reference/02.07_Test_Method_Reference/02.07.02.13.02_OptionList.htm`，含 vector 语义、Properties 视图输入规则、示例、Related information 与 Functional changes（已用 show.py 读取）。
- `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.03_addParameter.htm`，含 OptionList 说明、API 形式与 7.2.0 支持记录（已用 show.py 读取）。
- `02_System_reference/02.07_Test_Method_Reference/02.07.02.13.05_TestMethodParameterProxy.htm`，用于核对 `getType()` 的类型列表（已用 show.py 读取）。
- `02_System_reference/02.07_Test_Method_Reference/02.07.02.13_Parameter_types_defined_for_universal_test_method.htm`，用于核对 Subtopics 中的 OptionList 条目（已用 show.py 读取）。
