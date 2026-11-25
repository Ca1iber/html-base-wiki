---
type: object
title: Test Suites page
layer: gui
stage: testflow
tags: []
related: []
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.01.01_Test_Suites_page.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Test Suites page

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

**文档事实**：Test Suites page 用于添加或删除 special test suite 与 floating test suite，也可在该页编辑每个 test suite 的设置；文档说明它便于进行 batch setups。

**文档事实**：可以复制一个单元格的内容并粘贴到多个单元格；也可以把一段单元格复制到文本编辑器，编辑后再粘贴回 Test Suites page。

**文档事实**：页面显示三类 test suite：Run 与 Run and Branch test suite；Special test suite（青色背景）；Floating test suite（灰色背景）。

**文档事实**：列组包括 Test Setup 列（Type 列指定 test suite 执行的测试类型，只能为 M，即 test method）、Primary Settings 列（timing、level、analog setup 与 pattern 设置）、Result 列（Pass/Fail、Exec Time、Exec Num）、Test suite flags 列与 Test suite Comment 列。

**文档事实**：Result 列边框颜色：宽绿边框表示通过的 test suite；宽红边框表示失败的 test suite；窄绿边框表示被设为 pass；窄红边框表示被设为 fail；窄黄边框表示被设为 bypass。执行后若修改 testflow，所有 test suite 边框变为虚线。

**文档事实**：multi-site 下，若页面显示所有 site 的结果，则所有 site 都 pass 时边框才为绿；任一 site fail 则所有 site 的 test suite 显示红边框。若只显示 focus site 的结果，则边框颜色只按 focus site 的结果决定。Preferences 中激活 Show All Sites 可显示所有 site 的结果。

**文档事实**：Exec Time 为每个 test suite 的总执行时间；multi-site 下显示所有 device 的平均 test suite 执行时间。Exec Num 为每个 test suite 的执行次数：非优化 testflow 中为 test suite 重复次数乘以 site 数；优化 testflow 中为 test suite 重复次数（多 site 并行测试）。

**文档事实**：Test suite flags 列控制 test suite 的输出；也可在 engineering mode 下从 Operation Control 窗口的 Production Settings 访问，但改 flag 时所有窗口必须处于 Testflow settings mode 而非 Production settings mode。

**文档事实**：Annotation bar 针对文档所列各类元素显示注释；注释分布在 Top local、Left local、Right overview ruler、Bottom overview ruler 四个 annotation bar。点击注释可定位元素，悬停显示 tooltip；可用 Next/Previous Annotation 按钮在 test suite 间导航。

**文档事实**：Show and Hide 按钮只控制可见列：test setup、primary setup、result、test suite flags 列；另有 Show all columns 与 Validate setups 按钮。Validate setups 会把无效 testflow setup（setup 文件未加载，或 setup 文件中不存在所选设置）的 equation 或 set 号标黄并显示注释。

**文档事实**：Check Inconsistency / Check All Inconsistencies 按钮用于把单个或多个不一致的 test suite 适配到当前 testflow。不一致时，test setup 条目显示黄色背景（SmarTest 默认配置），property view 中该 test suite 的属性变灰。

## 典型用法

**文档事实**：批量设置：复制一个单元格的内容，粘贴到多个单元格；或把一段单元格复制到文本编辑器，编辑后粘贴回页面。

**文档事实**：选择可见列：用 Show and Hide 按钮切换 test setup、primary setup、result、test suite flag 列，或在 Test Suites preference page 中选择要显示的列；Show all columns 显示全部列。

**文档事实**：检查无效设置：点击 Validate setups，页面把 setup 文件未加载或 setup 文件中不存在所选设置的 equation/set 号标黄并显示 annotation，悬停可看详细信息。

**文档事实**：适配不一致的 test suite：选中单个 test suite 后点击 Check Inconsistency，SmarTest 完成适配，背景色恢复默认白色，property view 可编辑；或点击 Check All Inconsistencies，在弹窗中（默认预选全部）清除不想适配的 test suite，点击 OK，SmarTest 适配所选 test suite。

**文档事实**：添加或删除 special test suite 与 floating test suite，并编辑每个 test suite 的设置；special test suite 以青色背景显示，floating test suite 以灰色背景显示。

**文档事实**：查看执行结果：Result 列显示 Pass/Fail、Exec Time 与 Exec Num，并按上述边框颜色规则标示；multi-site 下可切换显示所有 site 或仅 focus site。

## 和谁有关

**文档事实**：以下关系均有本页正文、回链或相关文档证据支撑。

- [[flow-data-editor]]：本页是 Flow Data Editor 的一页；本页说明打开 Flow Data Editor 任意页面时出现 Check Inconsistency 等按钮，Flow Data Editor 文档也把 Test Suites page 列为其页面之一（回链证据）。
- [[test-suite]]：本页编辑每个 test suite 的设置并显示其执行结果；文档以 test suite 为操作对象。
- [[special-test-suites]]：本页把 special test suite 列为三类之一（青色背景）；Special test suites 文档回链说明它们不出现在 Flow Sequence Editor，默认排序时显示在 Test Suites page 末尾。
- Test suite flags（`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.07.04_Test_suite_flags.htm`）：本页说明这些列控制输出，并给出 engineering mode 下的访问方式；该文档回链到 Test Suites page。
- Test Suites preference page（`01_Getting_started/01.01_SmarTest_Work_Center/01.01.14.26_Test_Suites_preference_page.htm`）：本页说明可见列在该 preference page 中选择；相关的 Table Annotations preference page 则控制注释显示方式。
- Testflow Tool（`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02_Using_the_Testflow_Tool.htm`）：Running a testflow 的执行结果由本页显示，本页即是其结果查看入口之一。

## 版本

**文档事实**：本页 Functional changes 记载：

- Introduced before SmarTest 6.3.2——哨兵值，表示文档集覆盖范围之前已有。
- SmarTest 6.5.2：test suite 名称可以修改。
- SmarTest 6.5.2：新增 Test suite Comment 列。
- SmarTest 6.5.2：新增 Show all columns 按钮。
- SmarTest 6.5.4：新增 Adapt test suite(s) 按钮。
- SmarTest 7.0.1：Cloned test suite 更名为 linked test suite。

## 出处

- 主源：`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.01.01_Test_Suites_page.htm`（正文、Test Setup/Primary Settings/Result 列、Annotation bar、Show and Hide、Check for inconsistency、Related information、Functional changes）。
- 回链证据：`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.01.02_Special_test_suites.htm`、`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.07.04_Test_suite_flags.htm`、`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.01_Flow_Data_Editor.htm`。
