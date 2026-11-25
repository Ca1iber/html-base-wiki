---
type: object
title: Testflow Properties view
layer: gui
stage: testflow
tags: []
related: []
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.04_Testflow_Properties_view.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Testflow Properties view

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

**文档事实** Properties view 是 Testflow 及其他工具的一部分。

**文档事实** 在 Test Program Explorer 中选中 testflow item 时，Properties view 显示当前 testflow 的信息；在 testflow 中选择 test suite、bin、group、flow control node、Assign Value node 或 Print node 时，它显示并可编辑该元素的设置。

**文档事实** Test suite properties view 显示 Flow Sequence Editor 中当前选中 test suite 的全部属性，包含 Test Suite、Flags、Site Control 与 Results 四项，其中 Results 显示 Site in Focus 的结果。Test Suite 一项显示 comment、primary settings、test type 与 test method，除 test type 外都可修改。Flags 一项显示并允许修改所有 test suite flags。Site Control 一项控制该 test suite 的多 site 测试顺序。

**文档事实** Site Control 中 Site Match 控制 site match 功能；Allow Parallel 控制是否允许并行执行，若不勾选则所有 site 串行执行，下方的 site control 设置不生效；Site Control 可为 PARALLEL、SERIAL、SEMIPARALLEL、OTHER、UNDEF；Size 与 Cycle 只在 SEMIPARALLEL 下有用；执行序列 #1、#2、#3、#4 只适用于 OTHER，可在序列后的文本编辑器指定 site 号。新建 test suite 时默认为 UNDEF，若不改则按 test method 自身是串行还是并行实现来执行。OTHER 与 UNDEF 只能在 Testflow Properties view 中设置，不能在 Expanded Site Control window 中设置。

**文档事实** 启用 Test Suites preference page 的 Automatic Validate Setups 后，invalid primary set 会以黄色背景和警告图标显示。

**文档事实** Universal test method 参数有 valid 或 invalid、enabled 或 disabled、visible 或 invisible 三个属性。invalid 参数在 Properties view 中显示黄色背景和警告图标；disabled 参数灰显；invisible 参数不显示。invisible 覆盖 invalid 与 disabled，disabled 覆盖 invalid。参数值是 testflow variable 或 expression 时，所有参数可见并假定 enabled 且 valid；对 hierarchy parameter tree，子参数部分或全部 invalid、disabled、invisible 时根节点看不到注释。

**文档事实** 修改 test suite 所用 test method 的参数或 limit 定义并 build 后，Properties view 变灰，Inconsistency Check 按钮启用；点击该按钮、检查变更并点 OK 后，test method 的参数或 limit 变更会反映到 Properties view。

## 典型用法

**文档事实** 在 Flow Sequence Editor 中选中 test suite 后，可在该视图修改 comment、primary settings、test method、flags 与 site control。参数值可直接输入，也可从定义好的选项中选；SpecVariable、SpecValue、PinString 类型的参数可点 ... 按钮，从已定义的 spec variables 和 pins 中选择。

**文档事实** 要允许并行测试，除了在 Flow Data Editor 把 testflow flag parallel_mode 设为 on，还要在每个 testsuite 的 Testflow Properties view 中勾选 Allow Parallel。Allow Parallel 不勾选时所有 site 串行执行，下方 site control 设置不生效，因此调整 Site Control 前应先确认 Allow Parallel。

**文档事实** 要使用 OTHER 模式的执行序列，在 #1、#2 等后填入 site 号，不同 site 的 test suite 会按指定顺序串行或半并行执行。

**文档事实** 修改测试方法参数或 limit 后，等 Properties view 变灰时点 Inconsistency Check，确认变更后点 OK。

**文档事实** Site Control 的 OTHER 与 UNDEF 不在 Expanded Site Control window 的可选项中，因此需要这两种模式时要通过本视图设置。

## 和谁有关

**文档事实** Flow Sequence Editor 的当前选择决定 Test suite properties view 显示哪个 test suite 的属性。

**文档事实** Expanded Site Control window 与本视图都涉及 site control，但 OTHER 与 UNDEF 只能在本视图设置；该窗口只允许 Parallel、Serial、Semi-Parallel 三种选项。

**文档事实** Alphabetical list of flags 定义 Site Match、Allow Parallel、Site Control、Size、Cycle、site sequence 等 flag，本视图的 Flags 与 Site Control 直接使用这些 flag；Cycle 在 Expanded Site Control window 可设为 unbounded，对应 testflow 文件或 Test suite properties view 中的值 -1。

**文档事实** Test Suites preference page 的 Automatic Validate Setups 控制 invalid primary set 是否显示为黄色背景加警告图标。

**文档事实** Testflow Tool 的 Elements 文档说 Properties view 显示选中 test suite 的属性；Flow Sequence Editor 与 Flow Data Editor 是它的直接上下文。

**文档事实** 它与 test method 的参数和 limit 定义相关；addParameter、addLimit、Universal test method concept、TestMethodParameterProxy 都提到本视图的灰显、Inconsistency Check、参数可见性或 limit 修改。

**文档事实** TESTSET 的 testnumber 与 testnumber_default 使用 Properties view 中 Flags 区域或 Limits 区域指定的 test number 值；GET_TESTNUMBER 也引用 Properties view 中的 test name。

**文档事实** Pattern editor properties view 是另一类 Properties view，Setup perspective 与 Debug perspective 的说明都把它与本视图并举。

## 版本

**文档事实** 该视图在 SmarTest 6.3.2 之前引入。

**文档事实** SmarTest 6.5.0 在 Testsuite view 中显示 Parameter property。

**文档事实** SmarTest 6.5.2 用 Properties view 取代 Testsuite view。

**文档事实** SmarTest 6.5.3 移除了选择哪些 item 可在 Properties view 中显示的功能。

## 出处

- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.04_Testflow_Properties_view.htm`
