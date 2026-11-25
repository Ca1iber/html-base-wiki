---
type: object
title: Flow Data Editor
layer: gui
stage: testflow
tags: []
related: []
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.01_Flow_Data_Editor.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Flow Data Editor

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **164 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.01_Flow_Data_Editor.htm>` 及其子主题 `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.01.05_Variables_page.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Variables page）

You can use a user flag to branch in a testflow, depending on the current value of the flag.
This lets you control the testflow execution during a test program run.

<!-- 语法节 end -->

## 是什么

**文档事实** Flow Data Editor 是 Testflow Tool 的两个编辑器之一，以表格/电子表格形式显示 testflow 元素。文档说明这种表示便于纵览不同 testflow 组件，也便于调试。

**文档事实** Flow Data Editor 由八个页面组成：Test Suites、Parameters、Tests、Bins、Variables、Flags、Setups、Information。

**文档事实** 各页面的职责：Test Suites 页编辑每个 test suite 的设置；Parameters 页保存 test method 的参数设置；Tests 页显示 test method 中定义的测试结果 limit 范围；Bins 页编辑 bin；Variables 页增删改变量；Flags 页设置 system flags 与 testflow flags；Setups 页显示当前 testflow 使用的 primary setup 文件；Information 页编辑 testflow 的描述、器件名、器件版本与测试版本。

**文档事实** Testflow Tool 的两个编辑器处理同一份 testflow 文件，该文件位于 `<device directory>/testflow`；Flow Data Editor 与 Flow Sequence Editor 用两种不同方式表示同一文件的信息。

**文档事实** Flow Data Editor 的各页面彼此自动同步；它还会自动保持与 Flow Sequence Editor 中当前聚焦 test suite 的同步，反向亦然。

**文档事实** Test Suites 页展示三类 test suite：Run 与 Run and Branch、special test suite（青色背景）、floating test suite（灰色背景）。Bins 页展示三类 bin：stop bins、special bins（青色背景）、floating bins（灰色背景）；每个 testflow 默认含一个 otherwise bin。

## 典型用法

**文档事实** 通过 Testflow Tool 打开 Flow Data Editor 后，可用过滤行查找 test suite、bin、参数、limit、flag 等；Test Suites 页支持批量设置：可以把一个单元格的内容复制到多个单元格，也可以把一段单元格复制到文本编辑器、编辑后再粘回。

**文档事实** 在 Test Suites 页可以添加或删除 special test suite 与 floating test suite，并编辑每个 test suite 的设置；Result 列会在 test suite 或整个 testflow 运行后以边框颜色表示结果（宽绿边框为通过，宽红边框为失败）。

**文档事实** 在 Bins 页可以编辑 bin，但除 floating bin 外不能增删其他 bin；要增删其他类型的 bin，需使用 Flow Sequence Editor。

**文档事实** 在 Tests 页可以为基于 test method 的 test suite 添加或删除 limit（包括六个默认 limit）；若 limit 是在编写 test method 之前通过 Parameter and Limit Table 对话框定义的，一旦 testflow 中有 test suite 使用该 test method，它就会自动显示且不能删除。Test Name 列的内容取自 TEST API 的 `testname` 参数。

**文档事实** 在 Variables 页可以增删改变量；变量类型包括 DOUBLE、STRING、USERFLAG。Initial Value 在手动执行 testflow（例如调试）或启动测试程序时赋给变量；Current Value 列可在测试执行期间监视并修改当前值，文档指出这与 Hold 或 Hold on Fail test suite flag 配合特别有用。

**文档事实** SmarTest 6.5.2 及以后，变量必须先在 Variables 页定义，之后才能在 Assign Value node 中赋值；仅在 Assign Value node 中定义变量不再受支持。

**文档事实** Parameters 页显示 test method 的参数设置，Action Name 列对 universal test method 为 `proj.class`；要显示 test method 参数必须先构建 test method 库。若当前 testflow 所用 test method 的参数或 limit 定义被修改，Check All Inconsistencies 按钮会启用，用于按变更调整 testflow。

**文档事实** Flags 页可设置 system flags 与 testflow flags。工程模式下也可通过 Operation Control window（Production Settings）访问这些 flag，但要真正修改，所有窗口必须处于 Testflow settings 模式而非 Production settings 模式。

**文档事实** Setups 页显示当前 testflow 使用的 primary setup 文件，未加载或不存在的 setup 文件以黄色高亮。

**文档事实** Information 页可编辑 testflow 描述、器件名、器件版本号、测试版本号；这些信息可用 `GET_TEST_INFO` 查询测试。

**建议** 批量改 test suite 设置优先用 Test Suites 页的复制/粘贴；增删非 floating 的 bin 则切到 Flow Sequence Editor，避免在错误的页面找入口。

## 和谁有关

- **Testflow Tool** — **文档事实**：Flow Data Editor 是 Testflow Tool 的两个编辑器之一，通过 Testflow Tool 打开。
- **Flow Sequence Editor** — **文档事实**：两者处理同一 testflow 文件、以不同方式表示；Flow Data Editor 与其当前聚焦 test suite 双向同步。增删非 floating 的 bin 需用 Flow Sequence Editor；floating bin 在 Bins 页定义，但不在 Flow Sequence Editor 显示，后续插入的关联 multibin 才会显示。
- **Synchronization between the Flow Data Editor and the Flow Sequence Editor** — **文档事实**：本页 Related information 列出该页；同步不生效时需检查两个编辑器的自动同步设置。
- **Testflow Properties view** — **文档事实**：显示所选 test suite 的属性；integrated 打开模式会与两个编辑器一起打开该视图。
- **Testflow file** — **文档事实**：两个编辑器处理同一份位于 `<device_dir>/testflow` 的文件。
- **Assign Value node** — **文档事实**：SmarTest 6.5.2 及以后，变量必须先在 Variables 页定义，之后才能在 Assign Value node 中使用。
- **User Flags window** — **文档事实**：USERFLAG 类型的变量可在测试程序执行期间从 User Flags 窗口查看和编辑（Variables 页）。
- **Operation Control window** — **文档事实**：工程模式下可通过 Production Settings 访问 system/testflow flags，但修改时所有窗口须处于 Testflow settings 模式。
- **Parameter and Limit Table 对话框** — **文档事实**：在编写 test method 前通过该对话框定义的 limit 会在 Tests 页自动显示且不能删除。
- **Test Number Generator and TMLimits** — **文档事实**：Tests 页 Related information 列出该页，与 limit/test number 的处理相关。
- **GET_TEST_INFO** — **文档事实**：Information 页上的 testflow 基本信息可用该 API 查询。
- **Testflow Tool preference page** — **文档事实**：提供 “Synchronize selection between Flow Data Editor and Flow Sequence Editor” 等选项（objpack 入边引文）。

## 版本

**文档事实** 主文档 Functional changes 记载：Introduced before SmarTest 6.3.2；SmarTest 6.5.2 移除 Testtree 页、以 Test suites 页取代 Testlist 页、以 Tests 页取代 Limits 页。

**文档事实** 子页面另记有：Test Suites 页 6.5.2 可改 test suite 名、新增 Comment 列与 Show all columns 按钮，6.5.4 新增 Adapt test suite(s) 按钮；Parameters 页 6.5.2 参数可编辑、6.5.3 提供 Check All Inconsistencies 按钮；Tests 页 7.0.3 移除 test number manager；Bins 页 6.5.2 显示 stop/otherwise/floating bins、7.4.4 最大 bin 数增至 65536；Variables 页 6.5.2 可在页面上增删变量且不再支持在 Assign Value node 定义变量、7.5.1 增加变量数量上限链接；Setups 页 6.5.2 可在 Setups 页加载 test table。

## 出处

- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.01_Flow_Data_Editor.htm`：主源，含八个页面的清单、Related information 与 Functional changes。
- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.01.01_Test_Suites_page.htm`：Test Suites 页的三类 test suite、批量编辑、结果边框与版本。
- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.01.02_Parameters_page.htm`：参数页内容、构建 test method 库的前置条件与 Check All Inconsistencies。
- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.01.03_Tests_page.htm`：Tests 页的 limit 范围、默认 limit、`testname` 来源与版本。
- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.01.04_Bins_page.htm`：Bins 页的三类 bin、列含义、otherwise bin 与版本。
- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.01.05_Variables_page.htm`：变量类型、Initial/Current Value、Assign Value node 限制与版本。
- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.01.06_Flags_page.htm`、`02.08.04.32.03.01.07_Setups_page.htm`、`02.08.04.32.03.01.08_Information_page.htm`：Flags、Setups、Information 三页的职责与相关 API。
- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03_Elements_of_the_Testflow_Tool.htm`、`02.08.04.32.03.03_Synchronization_between_the_Flow_Data_Editor_and_the_Flow_Sequence_Edito.htm`、`02.08.04.32.02.01.01_Opening_the_Testflow_Tool.htm`：编辑器定位、同步与打开方式。
