---
type: object
title: CONNECT
layer: L2
stage: testmethod
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.18_CONNECT.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# CONNECT

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **431 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.18_CONNECT.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
CONNECT();
```

List of parameters

There are no parameters.

Return value

There is no return value.

### Example

```
CONNECT();
...
...
PMU_IFVM("PIN1,PIN2").iForce(100 uA).settling(5 ms);

PMU_IFVM("PIN1,PIN2").limits("limit1").execute();
...
...
```

To
use the
`PMU_IFVM`（raw: `29543.htm`）
 API, you must set the tester to the

CONNECT
 status. This example connects the tester resources to the DUT
with the
CONNECT
 API before DC measurement.

<!-- 语法节 end -->

## 是什么

（待补）

## 典型用法

（待补）

## 和谁有关

（待补）

## 版本

（待补）

## 出处

（待补）
