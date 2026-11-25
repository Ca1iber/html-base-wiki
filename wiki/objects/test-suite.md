---
type: object
title: Test suites
layer: n/a
stage: testflow
tags: []
related: []
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.01_Test_suites.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Test suites

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **503 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.01_Test_suites.htm>` 及其子主题 `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.01.04_Multibin_SmartDisconnect_test_suite.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Multibin SmartDisconnect test suite）

### Properties of a Multibin SmartDisconnect test suite

The
Multibin SmartDisconnect test suite
 is a
combination of a
`multibin node`（raw: `145085.htm`）
 and a test suite and
therefore offers properties that are typical for a test suite:

Note
 You must choose the
`wide selection`（raw: `119843.htm`）
 for
the node in order to inspect or change the properties of the
Multibin SmartDisconnect test suite
. For the narrow
selection, inspecting and changing the properties is possible only for the Run and
Branch node.

<!-- 语法节 end -->

## 是什么

**文档事实** Test suite 是对 individual, independent, executable device tests（例如 functional test 一类）的统称。它包含各类 timing set 与 level set、equations，以及一组 test suite flags。

**文档事实** 文档列出四类 test suite：

- "Run" 与 "Run and Branch" test suite：Run 只提供一条路径；Run and Branch 按测试结果分支。
- Special test suite：在特定时间点执行，执行时机可依赖或独立于 testflow。
- Multibin SmartDisconnect test suite：一个 multibin node 与一个用户定义 test suite 的组合。
- Floating test suite：不连接到 testflow 序列，可用于调试。

**文档事实** Multibin SmartDisconnect test suite 兼具 multibin node 与 test suite 的属性。要查看或修改其属性，必须为该 node 选择 wide selection；窄选择下只能查看和修改 Run and Branch node 的属性。

## 典型用法

**文档事实** Test suite 作为 testflow 的节点使用；文档说明包括 Test suites 在内的节点操作在 Flow Sequence Editor 中完成。

**文档事实** 文档以 "There are two ways to insert a test suite" 说明把 test suite 插入 testflow 有两条途径。

**文档事实** Test suite 的结果值通常可作为变量值（"Typically, such variables take result values of Test suites"）。若某变量在 test suite 中使用，相关 test suite 会在 Flow Sequence Editor 中高亮。

**文档事实** Floating test suite 不连入 testflow 序列，可用于调试。

**建议** 检查或修改 Multibin SmartDisconnect test suite 的属性时使用 wide selection，否则只能在 Run and Branch node 上查看和修改属性。

## 和谁有关

- **文档事实** `[[special-test-suites]]` — 主文档把 Special test suite 列为 test suite 的类型之一，并说明其执行时点可依赖或独立于 testflow。
- **文档事实** Multibin SmartDisconnect test suite — 主文档列为 multibin node 与 test suite 的组合；Testflow components 页把它指向 Bins。
- **文档事实** Floating test suite — 主文档列为不连 testflow 序列、用于调试的类型。
- **文档事实** "Run" / "Run and Branch" test suite — 主文档说明二者区别在于是否按测试结果分支。
- **文档事实** `[[flow-sequence-editor]]` — Working with nodes 页说明包括 Test suites 在内的节点操作都在 Flow Sequence Editor 中完成；test suite 使用变量时也在该编辑器中高亮。
- **文档事实** `[[bin]]` — Testflow components 页对 Multibin SmartDisconnect test suite 写明 "refer to Bins"。
- **文档事实** `[[testflow-variable]]` — Defining variables 页写明这类变量通常取 Test suites 的结果值。
- **文档事实** Testflow components — 把 Test suites 与 Flow control nodes、Assign Value node、Print nodes、Group node、Bins、Flags 并列。

## 版本

**文档事实** Functional changes 记载 Introduced before SmarTest 6.3.2（哨兵值，表示在文档集覆盖范围开始之前就已存在，不是 6.3.2 的变更）。SmarTest 7.6.1 新增 Multibin SmartDisconnect test suite。

## 出处

- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.01_Test_suites.htm`，主源，含 Test suite 定义、四类 test suite 的类型说明与 Functional changes。语法节另逐字引用子主题 `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.01.04_Multibin_SmartDisconnect_test_suite.htm`。
