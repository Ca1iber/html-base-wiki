---
type: object
title: SpecVariable
layer: L2
stage: level
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.02.13.04_SpecVariable.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# SpecVariable

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,432 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.02.13.04_SpecVariable.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example

The following example shows how to define a SpecVariable parameter and how to use it
in the test method. Some functions used in the run() function are defined in the file

SpecSearchUtil.hpp
. This example is intercepted from SpecSearch test in
the AC test method
library.

```
//for testmethod framework interfaces
#include "testmethod.hpp"
//for testmethod API interfaces
#include "mapi.hpp"

#include "SpecSearchUtil.hpp"
class SpecSearch: public testmethod::TestMethod
{
protected:
testmethod::SpecVariable spec;
...

protected:
/**
*Initialize the parameter interface to the testflow.
*This method is called just once after a testsuite is created.
*/
virtual void initialize()
{
addParameter("spec",
"SpecVariable",
&spec)
.setComment("this parameter's format like:\n"
"LEV.1.fooSpec[mV]\n"
"type is LEV, equationSetId is 1\n"
"name is fooSpec, unit is mV");
...
}

/**
*This test is invoked per site.
*/
virtual void run()
{
static SpecSearchUtil::SpecSearchUtilParam param;

SpecSearchUtil::SpecSearchUtilResult result;

/*----------------------------
* 1. prepare for test
*----------------------------
*/
ON_FIRST_INVOCATION_BEGIN();
/*process all parameters needed in test*/
SpecSearchUtil::processParameters(spec.mName,
spec.mType,
setupPinlist,
spec.mUnit,
method,
min,
max,
step,
resolution,
resultPinlist,
param);
ON_FIRST_INVOCATION_END();
...

return ;
}
};

REGISTER_TESTMETHOD("AcTest.SpecSearch", SpecSearch);
```

<!-- 语法节 end -->

## 是什么

**文档事实** `SpecVariable` 是 universal test method 的参数类型，用来表示 level 与 timing setup 文件中定义的 spec 变量。

**文档事实** 它包含 spec 类型、equation set 编号、spec 名称与单位；取值格式为 `"specType.equationSetNumber.specName[unit]"`。

**文档事实** 示例：`"LEV.1.fooSpec[mV]"` 表示 level 文件中 equation set 1 的 `fooSpec`，单位 `[mV]`；`"TIM.3.barSpec@port1[A]"` 表示 timing 文件中 port `port1` 的 equation set 3 的 `barSpec`，单位 `[A]`。

**文档事实** 字段包括 `mFullName`（完整名）、`mType`（spec 类型）、`mEquationSetId`（所属 equation set 编号）、`mName`（spec 变量名）、`mUnit`（单位）；用 `SpecVariable.field` 访问，如参数名为 `spec` 时 `spec.mUnit` 取单位。

**文档事实** 三个成员函数：`parseFullName()` 解析输入字符串并填充 type、equation set number、spec name、unit 各字段；`Reset()` 把值清空；`operator =` 从另一个 SpecVariable 复制值。

**推断** 因此 SpecVariable 是 test method 侧对 L1 level/timing spec 变量的结构化引用：testflow 传入一个按格式书写的字符串，test method 通过字段读取其类型、equation set、名称与单位。

## 典型用法

**文档事实** 在 test method 类中声明成员 `testmethod::SpecVariable spec;`，并在 `initialize()` 中调用 `addParameter("spec", "SpecVariable", &spec)` 把它暴露为 testflow 参数。

**文档事实** 示例用 `setComment` 说明参数格式 `LEV.1.fooSpec[mV]`：type 为 LEV、equationSetId 为 1、name 为 fooSpec、unit 为 mV。

**文档事实** 在 `run()` 中通过 `spec.mName`、`spec.mType`、`spec.mUnit` 把字段传给 `SpecSearchUtil::processParameters(...)`；相关函数定义在 `SpecSearchUtil.hpp`，示例取自 AC test method library 的 SpecSearch 测试。

**文档事实** `parseFullName()` 用于解析输入字符串并填充字段；`Reset()` 用于清空；`operator =` 用于从另一个 SpecVariable 复制。

**文档事实** 示例通过 `REGISTER_TESTMETHOD("AcTest.SpecSearch", SpecSearch)` 注册测试方法。

**建议** 在 testflow 中按文档格式填写参数（`specType.equationSetNumber.specName[unit]`，多端口 timing 变量可用 `@port`）；若自行解析字符串，先调用 `parseFullName()`，再从 `mType`、`mEquationSetId`、`mName`、`mUnit` 取字段，避免重复解析。

## 和谁有关

- **文档事实** `How to create a universal test method class`（`02.07.02.02.02`）— 本页 Related information 指向该页；该页正文说明 SpecVariable 用于 timing 或 level 文件中定义的 spec 变量（入边引文）。
- **文档事实** `addParameter`（`02.07.04.01.03`）— 该页同样说明 SpecVariable 用于 timing/level 文件中的 spec 变量；本页示例用 `addParameter("spec","SpecVariable",&spec)` 把 spec 注册为 SpecVariable 参数。
- **文档事实** `TestMethodParameterProxy`（`02.07.02.13.05`、`02.07.04.02.16`）— 其 `getType()` 返回的参数类型可为 int、double、string、PinString、SpecVariable、SpecValue、ContextPins 或 OptionList（入边引文）。
- **文档事实** `[[spec-value]]` — 同一 “Parameter types defined for universal test method” 节把 TestMethodParameterProxy、SpecVariable、SpecValue 并列为 universal test method 的参数类型；SpecValue 是本 wiki 的另一参数类型页。
- **文档事实** level setup 文件与 timing setup 文件 — SpecVariable 表示其中定义的 spec 变量；值的前缀 `LEV` 与 `TIM` 分别对应 level 与 timing。
- **文档事实** `SpecSearchUtil`（`SpecSearchUtil.hpp`）与 AC test method library 的 SpecSearch 测试 — 本页示例取自该处，`run()` 中把 `spec.mName`、`spec.mType`、`spec.mUnit` 传给 `SpecSearchUtil::processParameters`。
- **文档事实** `initialize()`、`run()` 与 `testmethod::TestMethod` — 示例中 SpecVariable 是 test method 的成员，在 `initialize()` 注册、在 `run()` 使用，并由 `REGISTER_TESTMETHOD` 注册。

## 版本

**文档事实** Functional changes 记：Introduced in SmarTest 6.5.0。

## 出处

- `02_System_reference/02.07_Test_Method_Reference/02.07.02.13.04_SpecVariable.htm`，主源，含概览、字段、Member function（parseFullName、Reset、operator=）、Example 与 Functional changes，已用 `show.py 02.07.02.13.04` 读取。
- 与 addParameter、TestMethodParameterProxy、How to create a universal test method class 及 Parameter types 章节的关系取自 `extract/objpack.py` / `edges.jsonl` 的入边，这些页面未单独读取。
