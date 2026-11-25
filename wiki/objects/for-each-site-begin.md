---
type: object
title: FOR_EACH_SITE_BEGIN
layer: L2
stage: testmethod
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.70_FOR_EACH_SITE_BEGIN.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# FOR_EACH_SITE_BEGIN

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,596 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.70_FOR_EACH_SITE_BEGIN.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
FOR_EACH_SITE_BEGIN();
```

List of parameters

There are no parameters.

Return value

There is no return value.

### Examples

### Example 1: Minimum code

The following example shows the minimum code for
a "each site loop block". The ellipses ("...") are to be replaced with your
code.

```
ON_FIRST_INVOCATION_BEGIN();
...
...
FOR_EACH_SITE_BEGIN();
...
...
FOR_EACH_SITE_END();
...
...
ON_FIRST_INVOCATION_END();
```

### Example 2: Optional curly brackets

The example utilizes optional pairs
of curly brackets "{" and "}". These optional curly brackets are used for simplifying the
correct indentation with assistance of the related Eclipse
tool.

```
ON_FIRST_INVOCATION_BEGIN();
{
...
...
FOR_EACH_SITE_BEGIN();
{
...
...
}
FOR_EACH_SITE_END();
...
...
}
ON_FIRST_INVOCATION_END();
```

### Example 3
```
ON_FIRST_INVOCATION_BEGIN();
{
//
// Pre-measurement
//
PMU_IFVM pmuIfvm("Aout_trig");
...
...

//
// Serial execution for all Sites - BEGIN
//
FOR_EACH_SITE_BEGIN();
{
//
// Get pre-measurement result for each site
//
DOUBLE V_off = pmuIfvm.getValue("Aout_trig");

//
// Set pre-measurement result for each site
// as site-specific setup condition
//
DGT("Aout").vOffset(V_off);

//Serial Execution for All Sites - END
}
FOR_EACH_SITE_END();

//
// Setup and test Execution on all active sites
//
EXECUTE_TEST(0.1 sec);
...
...
}
ON_FIRST_INVOCATION_END();
```

FOR_EACH_SITE_BEGIN()

and
FOR_EACH_SITE_END()
 declare the each site loop block in the
first-invocation block. All APIs in each site loop block are executed serially for all sites
when the program is run for the first tested site.

<!-- 语法节 end -->

## 是什么

**文档事实** `FOR_EACH_SITE_BEGIN` 是 MAPI 的 test method API，用来声明一个 block 的开始；该 block 允许在并行测试之前对所有 site 依次执行 setup。若需要“顺序 setup 并查询”，文档指向 `FOR_EACH_SITE_BEGIN_WITH_QUERY`。

**文档事实** 它必须与 `FOR_EACH_SITE_END` 成对使用；两者围出的区域称为 each site loop block。

**文档事实** 该 API 对 multi-site 测试有意义；对 single-site 测试会被忽略。

**文档事实** each site loop block 用于在并行测试执行前做 site-specific setup（不同 site 可有不同 setup 条件）。该 block 必须放在 first-invocation block（由 `ON_FIRST_INVOCATION_BEGIN` / `ON_FIRST_INVOCATION_END` 声明）中，或放在 last-invocation block（由 `ON_LAST_INVOCATION_BEGIN` / `ON_LAST_INVOCATION_END` 声明）中。

**文档事实** 当程序为第一个被测 site 运行时，each site loop block 内的所有语句会针对所有 active site 串行执行。文档还提示：哪些 API 只设置处于 setup-focus 状态的 site、哪些 API 总是设置所有 site，参见 `API Behavior on Multi-Site Testing`。

**文档事实** 本 API 无参数、无返回值；定义在 `/opt/hp93000/soc/prod_com/include/MAPI/MapiUtil.h`。

## 典型用法

**文档事实** 最小写法是 `ON_FIRST_INVOCATION_BEGIN(); ... FOR_EACH_SITE_BEGIN(); ... FOR_EACH_SITE_END(); ... ON_FIRST_INVOCATION_END();`，省略号处替换为用户代码。

**文档事实** 文档说明可以选用成对的花括号 `{` `}`；这些花括号不是语法要求，而是借助相关 Eclipse 工具简化正确缩进。

**文档事实** Example 3 在每个 site 的循环中读取 `PMU_IFVM pmuIfvm("Aout_trig")` 的预测量结果 `getValue("Aout_trig")`，把该值作为该 site 的 setup 条件写入 `DGT("Aout").vOffset(V_off)`；循环结束后在循环外对所有 active site 执行 `EXECUTE_TEST(0.1 sec)`。

**建议** 把每个 site 不同的 setup 条件放进 each site loop block；如果还需要顺序查询 setup/结果信息，按文档改用 `FOR_EACH_SITE_BEGIN_WITH_QUERY`。

**建议** 在编写 block 内的 API 调用前，先按 `API Behavior on Multi-Site Testing` 确认该 API 是“只设置 setup-focus site”还是“总是设置所有 site”，以免 site-specific setup 的语义与预期不符。

## 和谁有关

- **文档事实** 与 `FOR_EACH_SITE_END`：文档明确两者必须成对使用，围出的区域即 each site loop block。
- **文档事实** 与 `FOR_EACH_SITE_BEGIN_WITH_QUERY`：文档在开头与结尾都指向它，说明若需要顺序 setup 并查询，应使用该 API。
- **文档事实** 与 `ON_FIRST_INVOCATION_BEGIN` / `ON_FIRST_INVOCATION_END`、`ON_LAST_INVOCATION_BEGIN` / `ON_LAST_INVOCATION_END`：文档规定 each site loop block 必须放在这两类 invocation block 之一中。
- **文档事实** 与 `API Behavior on Multi-Site Testing`：文档指向该主题，用于区分“只设置 setup-focus site”的 API 与“总是设置所有 site”的 API。
- **文档事实** 与 `CURRENT_SITE_NUMBER()`、`FOR_SEMI_PARALLEL_TEST_BEGIN` / `FOR_SEMI_PARALLEL_TEST_END`、`Controlling Multiple Sites`、`Site States and Test Method Programs`：这些列在本页 `Related information` 中。
- **文档事实** 与 Example 3 中的 `PMU_IFVM`、`DGT`、`EXECUTE_TEST`：示例用它们演示在 each site loop block 内按 site 读取并设置 `vOffset`，再在循环外执行测试（示例级关系）。
- **文档事实** 从入边看，`DPS_AUX_PIN_TASK.setMode` 说明在 FOR_EACH_SITE 循环内调用时所有 active site 会被设为同一 mode 并产生警告；`DPS_AUX_TASK.getRangeError` 要求调用位置在 `ON_FIRST_INVOCATION` 之外或在 FOR_EACH_SITE block 内；`LIMIT` 则注明不能在 `ON_FIRST_INVOCATION` 内使用、即使在 FOR_EACH_SITE block 内也不行。这些页面说明了在循环内使用其他 API 时的约束。

## 版本

**文档事实** `Functional changes` 只记载 `Introduced before SmarTest 6.3.2`，未列后续变更。

## 出处

- `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.70_FOR_EACH_SITE_BEGIN.htm`（Application note、Syntax、Examples、Related information、Functional changes）。
- 「和谁有关」另参考 `extract/edges.jsonl` 中指向/离开该页的边记录（所引其他 API 的约束句取自这些入边的 context）。
