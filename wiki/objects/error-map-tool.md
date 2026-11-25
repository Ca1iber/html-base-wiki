---
type: object
title: Error Map Tool
layer: gui
stage: results
tags: []
related: []
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.08_Error_Map_Tool.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Error Map Tool

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **751 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.08_Error_Map_Tool.htm>` 及其子主题 `<02_System_reference/02.06_Command_Reference/02.06.11.01.02.01.05_Dealing_with_storage_problems_on_Smart_Scale_systems.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Dealing with storage problems on Smart Scale systems）

Suppose that the default port
@
 comprises 8 IO pins,

P1
 through
P8
, and that all these pins are associated with a
channel of the 8-channel group 10101 through 10108 on an PS1600 system. Assume further that you
want edge information about
r2
,
r4
,
r6
,
and
r8
 for pins
P1
,
P3
,

P5
, and
P7
. Then the following setup would minimize the risk
that recording is
aborted:

```
DCRT RAM,(@)
DCEL DCRT,TP,SET,(P2,P4,P6,P8)
DCRM EMAP,4,PF,"c1:2 c2:4 c3:6 c4:8",(@)
```

If
you call
EMAP?
 after completion of the test with resolution mode

EDGE
, you will get the values for the edges of interest in a format that
also identifies their edge numbers. If, for example, all 4 edges have failed in a cycle, the
result will be returned as

```
01010101
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
