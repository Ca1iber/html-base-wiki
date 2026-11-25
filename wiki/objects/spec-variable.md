---
type: object
title: SpecVariable
layer: L2
stage: level
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.02.13.04_SpecVariable.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# SpecVariable

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,432 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.02.13.04_SpecVariable.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example

The following example shows how to define a SpecVariable parameter and how to use it
in the test method. Some functions used in the run() function are defined in the file

SpecSearchUtil.hpp
. This example is intercepted from SpecSearch test in
the AC test method
library.

```
//for testmethod framework interfaces
#include "testmethod.hpp"
//for testmethod API interfaces
#include "mapi.hpp"

#include "SpecSearchUtil.hpp"
class SpecSearch: public testmethod::TestMethod
{
protected:
testmethod::SpecVariable spec;
...

protected:
/**
*Initialize the parameter interface to the testflow.
*This method is called just once after a testsuite is created.
*/
virtual void initialize()
{
addParameter("spec",
"SpecVariable",
&spec)
.setComment("this parameter's format like:\n"
"LEV.1.fooSpec[mV]\n"
"type is LEV, equationSetId is 1\n"
"name is fooSpec, unit is mV");
...
}

/**
*This test is invoked per site.
*/
virtual void run()
{
static SpecSearchUtil::SpecSearchUtilParam param;

SpecSearchUtil::SpecSearchUtilResult result;

/*----------------------------
* 1. prepare for test
*----------------------------
*/
ON_FIRST_INVOCATION_BEGIN();
/*process all parameters needed in test*/
SpecSearchUtil::processParameters(spec.mName,
spec.mType,
setupPinlist,
spec.mUnit,
method,
min,
max,
step,
resolution,
resultPinlist,
param);
ON_FIRST_INVOCATION_END();
...

return ;
}
};

REGISTER_TESTMETHOD("AcTest.SpecSearch", SpecSearch);
```

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
