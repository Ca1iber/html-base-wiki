---
type: object
title: ON_FIRST_INVOCATION_END
layer: L2
stage: testmethod
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.139_ON_FIRST_INVOCATION_END.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# ON_FIRST_INVOCATION_END

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,611 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.139_ON_FIRST_INVOCATION_END.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
ON_FIRST_INVOCATION_END();
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

The following example shows the minimum code for a "first-invocation block". The
ellipses ("...") are to be replaced with your code.

```
ON_FIRST_INVOCATION_BEGIN();
...
...
ON_FIRST_INVOCATION_END();
```

### Example 2: Optional curly brackets

The example utilizes an optional pair of curly brackets "{" and "}". These optional
curly brackets are used for simplifying the correct indentation with assistance of
the related Eclipse tool.

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

**文档事实** ON_FIRST_INVOCATION_END 声明由 ON_FIRST_INVOCATION_BEGIN 开始的 first-invocation block 的结束；二者必须成对使用，围起的区域称为 "first-invocation block"。块内所有 API 只在程序为第一个被测 site 运行时、对所有 site 并行执行一次。定义于 `/opt/hp93000/soc/prod_com/include/MAPI/MapiUtil.h`，无参数、无返回值。

## 典型用法

**文档事实** 最小形式为 `ON_FIRST_INVOCATION_BEGIN(); ... ON_FIRST_INVOCATION_END();`；可选的一对 `{}` 仅用于借助 Eclipse 工具简化缩进。
**文档事实** 示例 3 在该块内完成整站 setup 与测量：`Routing.pin("Aout").connect(...)`、`Analog.DGT("Aout").enable()`、`EXECUTE_TEST(...)`、读取 waveform，再 `disconnect` / `disable` 并 `FLUSH()`；文档说明这样所有连接 site 的模拟模块被启用后测量在所有 site 上完成。
**推断** 由于块内 API 对所有 site 并行且只执行一次，它适合放置各 site 共享的一次性硬件 setup。

## 和谁有关

- ON_FIRST_INVOCATION_BEGIN：必须与本 API 成对使用（源文明确 "must be used as a pair"，且互为 Related information / 入边）。
- ON_LAST_INVOCATION_BEGIN / ON_LAST_INVOCATION_END：Related information 列出，且各自入边引用本页。
- FOR_EACH_SITE_BEGIN / FOR_EACH_SITE_END、FOR_SEMI_PARALLEL_TEST_BEGIN / END：文档要求 semi-parallel 块必须放在 ON_FIRST_INVOCATION_BEGIN 与 ON_FIRST_INVOCATION_END 之间；SET_TEST_FOCUS / UNSET_TEST_FOCUS 用于该 first-invocation block（FOR_EACH_SITE 循环除外）。
- Controlling Multiple Sites / Parallel Execution / Site States and Test Method Programs：相关主题（Related information 与入边）。

## 版本

**文档事实** Functional changes 记为 "Introduced before SmarTest 6.3.2"。

## 出处

- `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.139_ON_FIRST_INVOCATION_END.htm`。
