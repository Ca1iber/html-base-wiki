---
type: object
title: BEGIN_EXTENSION
layer: L2
stage: testmethod
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.10_BEGIN_EXTENSION.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# BEGIN_EXTENSION

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **3,216 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.10_BEGIN_EXTENSION.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
void BEGIN_EXTENSION();
void BEGIN_EXTENSION(STRING& sites);
void BEGIN_EXTENSION(ARRAY_I& sites);
```
[表] Parameter
列: I/O | Parameter | Description / Range
行 1:
  I
  sites
  This parameter sets the setup focus sites for the statements in the extension
    block.
    
    To make the extension block effective for sites 1 to 3 in four sites,
    
    STRING: "1110".
    
    ARRAY_I: sites[0]=1, sites[1]=2, and sites[2]=3.

### Important points

BEGIN_EXTENSION
 and
END_EXTENSION
 should be
used as a pair. The area enclosed by
BEGIN_EXTENSION
 and

END_EXTENSION
 is called "
extension block
".

You can describe the
`FW_TASK`（raw: `29362.htm`）
 functions within the extension block. One or
more
FW_TASK
s can be applied to this block. Beside the

FW_TASK
 function, you can also describe the function you originally
created. You should not describe the other test method APIs in the extension block.

For data setup, a conflict might occur between the test method API outside the extension
block and firmware commands within the extension block. To avoid such a conflict, you should
consider the following actions:

The caching mechanism of the test method is temporarily turned off between the "extension
block" explicitly declared by
BEGIN_EXTENSION
 and

END_EXTENSION
. This is implicitly done by the system.

You should execute the
FLUSH
 API before entering the extension
block. The setup data relating to the API such as
ANALOG
,

ANALOG_STATUS
,
PRIMARY_STATUS
, and

ROUTING_STATUS
 will be stored in the caching mechanism. The

FLUSH
 API downloads the setup data to the system hardware or the
MCD.

For multi-site testing, you can specify optional parameter
sites
 to
set the setup focus sites for the statements in the extension block. Therefore, the statements
will be performed for the specified sites only.

In this case, you can make nested extension
blocks.

END_EXTENSION
 just after
BEGIN_EXTENSION

reverts the setup focus sites to the same settings as before entering the extension block.

This allows you to do complicated and flexible site management correctly. If the extension
block is not nested correctly, the nest information will be initialized at the end of the test
suite execution automatically. Also, a warning message appears in the report window.

### Examples

### Example 1: BEGIN_EXTENSION and END_EXTENSION declare the extension block
```
STRING dfcm("DFCM 1,4000,50,-1.00,1.00,4000,5,I,0,PPNP,(CP)\n");
STRING ptstq("PTST? 1,NONE,NONE,PVAL\n");

BEGIN_EXTENSION();

FW_TASK(dfcm);

STRING answer;

FW_TASK(ptstq, answer);
...
...

END_EXTENSION();
```

### Example 2: Extension block for all enabled sites
```
STRING enabled_sites;

GET_ENABLED_SITES(enabled_sites);

BEGIN_EXTENSION(enabled_sites);

//
// Your FW_TASK code
//
...
...

END_EXTENSION();
```

The

GET_ENABLED_SITES
 API retrieves the information of the current enabled
sites and stores it to the variable
enabled_sites
.

BEGIN_EXTENSION
 and
END_EXTENSION
 declare the
extension block for multi-site testing. In this example, the extension block is effective for
the current enabled sites.
BEGIN_EXTENSION
 sets the current enabled sites
to the setup focus sites. Therefore, the statements will be performed for the current enabled
sites only.

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
