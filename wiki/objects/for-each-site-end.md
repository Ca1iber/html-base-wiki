---
type: object
title: FOR_EACH_SITE_END
layer: L2
stage: testmethod
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.72_FOR_EACH_SITE_END.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# FOR_EACH_SITE_END

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **169 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.72_FOR_EACH_SITE_END.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
FOR_EACH_SITE_END();
```

List of parameters

There are no parameters.

Return value

There is no return value.

### Example

See the examples in
`FOR_EACH_SITE_BEGIN`（raw: `29344.htm`）
.

<!-- 语法节 end -->

## 是什么

**文档事实** FOR_EACH_SITE_END 是 MAPI 中的一个 test method API，用于声明由 FOR_EACH_SITE_BEGIN 开始的 each site loop block 的结束。

**文档事实** 该 API 与 FOR_EACH_SITE_BEGIN 成对使用，两者之间的区域构成 each site loop block。

**文档事实** 它没有参数，也没有返回值，调用形式为 FOR_EACH_SITE_END()。

**文档事实** 该 API 定义在头文件 /opt/hp93000/soc/prod_com/include/MAPI/MapiUtil.h 中。

**文档事实** FOR_EACH_SITE_BEGIN 页说明该 loop block 用于在并行测试执行前进行 site specific setup，对多 site 测试有意义，单 site 测试中会被忽略；block 必须放在 ON_FIRST_INVOCATION_BEGIN 与 ON_FIRST_INVOCATION_END 声明的 first-invocation block 中，或放在 ON_LAST_INVOCATION_BEGIN 与 ON_LAST_INVOCATION_END 声明的 last-invocation block 中。

**文档事实** FOR_EACH_SITE_BEGIN 页还说明，当程序为第一个被测 site 运行时，each site loop block 内的所有语句会针对所有 active site 串行执行。

## 典型用法

**文档事实** 典型写法是在 FOR_EACH_SITE_BEGIN() 之后写每个 site 的 setup 语句，再以 FOR_EACH_SITE_END() 结束，整个块位于 ON_FIRST_INVOCATION_BEGIN() 与 ON_FIRST_INVOCATION_END() 之间。

**文档事实** FOR_EACH_SITE_BEGIN 页给出的最小示例是 ON_FIRST_INVOCATION_BEGIN()、FOR_EACH_SITE_BEGIN()、省略号代表的用户代码、FOR_EACH_SITE_END()、ON_FIRST_INVOCATION_END() 依次排列。

**文档事实** 该页还给出使用可选花括号的示例，花括号用于借助相关 Eclipse 工具简化正确缩进。

**文档事实** 该页的第三个示例在每个 site 的循环中读取 PMU_IFVM 的预测量结果，并用 DGT("Aout").vOffset(V_off) 将其设为该 site 的 setup 条件，随后在循环外调用 EXECUTE_TEST(0.1 sec) 在所有 active site 上执行测试。

**文档事实** 本页的 Example 段本身不重复代码，而是指向 FOR_EACH_SITE_BEGIN 页的示例。

## 和谁有关

- **文档事实** FOR_EACH_SITE_BEGIN，本页说明二者成对使用以声明 each site loop block，且示例参见该页。
- **文档事实** FOR_EACH_SITE_BEGIN_WITH_QUERY，列在本页 Related information，FOR_EACH_SITE_BEGIN 页说明需要顺序 setup 并查询时使用它。
- **文档事实** CURRENT_SITE_NUMBER()，列在本页 Related information。
- **文档事实** ON_FIRST_INVOCATION_BEGIN 与 ON_FIRST_INVOCATION_END，列在本页 Related information，FOR_EACH_SITE_BEGIN 页说明 each site loop block 必须放在该 first-invocation block 中。
- **文档事实** FOR_SEMI_PARALLEL_TEST_BEGIN 与 FOR_SEMI_PARALLEL_TEST_END，列在本页 Related information。
- **文档事实** Controlling Multiple Sites，列在本页 Related information，是多 site 测试的上层说明。
- **文档事实** Site States and Test Method Programs，列在本页 Related information。
- **文档事实** ON_LAST_INVOCATION_BEGIN 与 ON_LAST_INVOCATION_END，FOR_EACH_SITE_BEGIN 页说明 each site loop block 也可放在该 last-invocation block 中。

## 版本

**文档事实** Functional changes 只记载 Introduced before SmarTest 6.3.2，未列出后续变更。

## 出处

- `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.72_FOR_EACH_SITE_END.htm`
- `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.70_FOR_EACH_SITE_BEGIN.htm`
