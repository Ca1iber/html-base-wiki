---
type: object
title: ON_FIRST_INVOCATION_BEGIN
layer: L2
stage: testmethod
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.138_ON_FIRST_INVOCATION_BEGIN.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# ON_FIRST_INVOCATION_BEGIN

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,612 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.138_ON_FIRST_INVOCATION_BEGIN.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
ON_FIRST_INVOCATION_BEGIN();
```

This API is defined in the header file

/opt/hp93000/soc/prod_com/include/MAPI/MapiUtil.h
.

List of parameters
There are no parameters.
Return value
There is no return value.

### Examples

### Example 1: Minimum code

The following example shows the minimum code for
a "first-invocation block". The ellipses ("...") are to be replaced with your
code.

```
ON_FIRST_INVOCATION_BEGIN();
...
...
ON_FIRST_INVOCATION_END();
```

### Example 2: Optional curly brackets

The example utilizes an optional pair
of curly brackets "{" and "}". These optional curly brackets are used for simplifying the
correct indentation with assistance of the related Eclipse
tool.

```
ON_FIRST_INVOCATION_BEGIN();
{
...
...
}
ON_FIRST_INVOCATION_END();
```

### Example 3
```
//
// Parallel Execution for All Sites - BEGIN
//
ON_FIRST_INVOCATION_BEGIN();

//
// Setup and Test Execution
//
Routing.pin("Aout").connect(TM::SINGLE);
Analog.DGT("Aout").enable();
EXECUTE_TEST(0.1 sec);

//
// Retrieve measured analog waveform
//
ARRAY_D AnaWave = Analog.DGT("Aout").getWaveform();
Routing.pin("Aout").disconnect();
Analog.DGT("Aout").disable();

FLUSH();

//
// Parallel Execution for All Sites - END
//
ON_FIRST_INVOCATION_END();
...
...
```

ON_FIRST_INVOCATION_BEGIN
 and

ON_FIRST_INVOCATION_END
 declare the first-invocation block. All APIs in
this block are executed for all sites in parallel once only when the program is run for the first
tested site. Hence, the analog modules on the all connected site, specified by the "Aout" pin,
are enabled and then the measurements are done on all connected sites.

<!-- 语法节 end -->

## 是什么

**文档事实** ON_FIRST_INVOCATION_BEGIN 声明“first-invocation block”的开始：该 block 内的 setup 与 test 会在程序首次运行到第一个被测 site 时，对所有 site 并行执行一次。它必须与 ON_FIRST_INVOCATION_END 成对使用；两者包围的区域称为 first-invocation block。

**文档事实** 文档 Application note 的要点：
- 该 API 对 multisite 测试有意义；单 site 测试时被忽略。
- block 内可写 Setup 与 Execute API，使其对所有 active site 并行生效；也可写其他函数，但这些函数要么作用于当前被测 site（如 Result API），要么与 site 无关（如 Computation API）。
- block 内所有语句只在程序运行第一个被测 site 时执行一次。
- 多 site 时，FW_TASK 若要放进 block，必须用带 site 参数的 BEGIN_EXTENSION / END_EXTENSION 包围；不要用不带参数的 BEGIN_EXTENSION。
- 不得让 first-invocation block 变成条件执行；若必须条件化，要在 else 分支放一个 dummy first-invocation block。
- CAUTION：TEST()、LIMIT() 以及 TESTSET 的所有 `judgeAndLog_***` 语句绝不能在 first-invocation block 内使用，否则有把不良器件判为 OK 的高风险。
- 无参数、无返回值；头文件：`/opt/hp93000/soc/prod_com/include/MAPI/MapiUtil.h`。

## 典型用法

**文档事实** 最小结构：
```
ON_FIRST_INVOCATION_BEGIN();
...
ON_FIRST_INVOCATION_END();
```

**文档事实** 可用一对可选花括号帮助 Eclipse 工具正确缩进：
```
ON_FIRST_INVOCATION_BEGIN();
{
...
}
ON_FIRST_INVOCATION_END();
```

**文档事实** 文档 Example 3 把并行 setup/执行放在 block 内：`Routing.pin("Aout").connect(TM::SINGLE);`、`Analog.DGT("Aout").enable();`、`EXECUTE_TEST(0.1 sec);`、取波形、disconnect/disable、`FLUSH();`，最后 `ON_FIRST_INVOCATION_END();`。按文档说明，这些 API 会在所有 connected site 上并行执行一次。

**建议** 依据上述 Application note 与示例，可归纳为：把“所有 site 共享、只需做一次”的 setup/执行放 block 内；把逐 site 的结果判定/记录（TEST、LIMIT、judgeAndLog_*）放到 block 外。此条是编码建议，不是对机台行为的额外推断。

## 和谁有关

- 与 ON_FIRST_INVOCATION_END：文档明确两者必须成对使用，Related information 也列出。
- 与 ON_LAST_INVOCATION_BEGIN / ON_LAST_INVOCATION_END：Related information 列出，属同一组 invocation block 控制 API。
- 与 FOR_EACH_SITE_BEGIN / FOR_EACH_SITE_END：Related information 列出；入边显示某些 API 要求“在 ON_FIRST_INVOCATION block 外，或在 FOR_EACH_SITE...WITH_QUERY block 内”调用（如 HW_STATE 的成员函数）。
- 与 FOR_SEMI_PARALLEL_TEST_BEGIN / FOR_SEMI_PARALLEL_TEST_END：入边明确 semi-parallel block 必须放在 ON_FIRST_INVOCATION_BEGIN 与 ON_FIRST_INVOCATION_END 之间，否则报错。
- 与 RDI_INIT / RDI_BEGIN / RDI_END：入边显示 `RDI_INIT()` 必须在 `ON_FIRST_INVOCATION_BEGIN()` 之前调用；`RDI_BEGIN()` / `RDI_END()` 预期放在 first-invocation block 内并成对使用。
- 与 SMC_SYNCHRONIZE：入边说明 `SMC_SYNCHRONIZE()` 必须逐 site 调用，因而要放在 ON_FIRST_INVOCATION block 之外。
- 与 TESTSET：本页明确禁止在 block 内使用 TEST()、LIMIT() 与 judgeAndLog_*；TESTSET 的示例也把 judgeAndLog 放在 block 后。
- 另见 Related information：Controlling Multiple Sites、Site States and Test Method Programs。

## 版本

`Functional changes`：Introduced before SmarTest 6.3.2。

## 出处

- `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.138_ON_FIRST_INVOCATION_BEGIN.htm`（正文、Application note、Syntax、Examples、Related information、Functional changes）。
- 关联判断另参考 `extract/edges.jsonl` 中指向该页的入边记录（HW_STATE、FOR_SEMI_PARALLEL_TEST_*、RDI_*、SMC_SYNCHRONIZE、CCF 模板等页面的引用语境）。
