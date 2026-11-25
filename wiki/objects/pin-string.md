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

**文档事实** PinString 是 universal test method 的参数类型之一；创建测试方法类时，参数类型列表把它与 int、double、string、SpecVariable、SpecValue、ContextPins、OptionList、FileString 并列。

**文档事实** PinString 用于引脚（pins）、引脚列表（pin lists）或引脚组（pin groups）。

**文档事实** 在测试方法中，PinString 类型的参数定义引脚名称；其值可以是 `@`（所有适用引脚），也可以是任意数量的适用单个引脚。

**文档事实** 参数的 Identifier 显示在 testflow editor 中，参数变量则在测试方法的 `run()` 函数中使用。

**推断** 因此 PinString 承载的是“测试方法要作用的引脚集合”，其取值形态（`@` 或引脚名列表）由 test suite 的 Properties 视图编辑。

## 典型用法

**文档事实** 在 “Create a new TestMethod class” 向导的 Parameters 区域点击 Add，在 “Add a new parameter” 窗口把 Type 选为 PinString，并填写 Identifier、Variable、Default、Options、Comment，然后点击 OK。

**文档事实** 参数名可用 `.` 建立层级（例如 `x.start`、`x.stop`、`x.step`、`x.scale`）；Options 的候选值之间用冒号分隔。

**文档事实** 代码中在测试方法的 `initialize()` 函数里用 `addParameter("参数名","PinString",&成员变量,mode)` 定义参数；`mode` 可选 `TM_PARAMETER_INPUT` 或 `TM_PARAMETER_OUTPUT`，返回的 `TestMethodParameterProxy` 可继续链式调用 `setDefault()`、`setOptions()`、`setComment()` 等。

**文档事实** 在 test suite 的 Properties 视图中修改 PinString 参数时，点击参数值旁的按钮会打开选引脚窗口；可选择 All Pins (`@`)，或选择 Pins selected below 后从引脚列表中挑选任意数量的单个引脚，再点击 OK。

**文档事实** 文档示例为 continuity test suite 的 `dc_tml.DcTest.Continuity`，其 `pinlist` 参数是 PinString 类型，用于定义待测引脚名；选择完成后 `pinlist` 的值即被改变。

**建议** 需要覆盖全部适用引脚时直接用 `@`，只测部分引脚时用显式引脚列表，便于在 test suite 层面调整。

## 和谁有关

- **文档事实** FileString、OptionList、SpecVariable、SpecValue、ContextPins，源文档把 PinString 与它们并列为 universal test method 的参数类型；其中 FileString、OptionList、SpecVariable、SpecValue 另有独立条目。
- **文档事实** addParameter，它是定义测试方法参数的 API；参数表明确列出 PinString 并说明其用于 pins、pin lists 或 pin groups，Functional changes 记 SmarTest 6.5.0 起支持 PinString。
- **文档事实** TestMethodParameterProxy，`addParameter` 返回该代理对象，其 `getType()` 文档列出的参数类型包含 PinString。
- **文档事实** Selecting pins in the Properties view，该页专门说明如何在 Properties 视图为 PinString 参数选择引脚，并以 continuity test 的 `pinlist` 为例。
- **文档事实** Testflow editor 与 test suite Properties 视图，前者显示参数 Identifier，后者用于编辑 PinString 参数值。
- **文档事实** Create a new TestMethod class 向导，参数在向导的 Parameters 区域添加。

## 版本

**文档事实** addParameter 的 Functional changes 记载：SmarTest 6.5.0 起支持 SpecVariable 与 PinString 参数类型。

**文档事实** “Selecting pins in the Properties view” 的 Functional changes 记载该 Properties 视图选引脚流程 Introduced in SmarTest 6.5.0。

**推断** PinString 类型与针对它的 GUI 选取流程同在 SmarTest 6.5.0 引入，二者版本记录一致。

## 出处

- `02_System_reference/02.07_Test_Method_Reference/02.07.02.02.02_How_to_create_a_universal_test_method_class.htm`，主源，含参数类型列表、PinString 用途、向导步骤与参数字段说明。
- `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.03_addParameter.htm`，含 PinString 的参数类型说明、API 形式与 Functional changes（已用 show.py 读取）。
- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01.10_Selecting_pins_in_the_Properties_view.htm`，含 PinString 的 `@`/单引脚取值与 Properties 视图操作（已用 show.py 读取）。
- `02_System_reference/02.07_Test_Method_Reference/02.07.02.13.05_TestMethodParameterProxy.htm`，用于核对 `getType()` 的类型列表（已用 show.py 读取）。
