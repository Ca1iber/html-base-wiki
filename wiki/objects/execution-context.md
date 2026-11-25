---
type: object
title: Using execution contexts
layer: L2
stage: run
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.08.05.03.02.03_Using_execution_contexts.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Using execution contexts

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,643 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.07.01.08.05.03.02.03_Using_execution_contexts.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example

For a test method example, see the description of
`SEQUENCER_CONTEXT`（raw: `136815.htm`）
.

The
following firmware example first displays the current start label, then shows its definition and
that of another multi-port burst, then defines two execution contexts each of which is related
to one of the two multi-port bursts, and finally executes these two contexts, changing the start
label after starting the first
context:

```
> SQSL?
< SQSL "mu_burst1"
> SQLB? "mu_burst1",MPBU,(@@)
< SQLB "mu_burst1",MPBU,6,7,,(PA)
< SQLB "mu_burst1",MPBU,6,7,,(PB)
< SQLB "mu_burst1",MPBU,10,11,,(PC)
< SQLB "mu_burst1",MPBU,4,5,,(PD)
> SQLB? "mu_burst2",MPBU,(@@)
< SQLB "mu_burst2",MPBU,3,4,,(PX)
< SQLB "mu_burst2",MPBU,8,9,,(PY)
> SQEC "c1",(PA,PD)
> SQEC "c2",(PY)
> SQST RUN,"c1"
> SQSL "mu_burst2"
> SQST RUN,"c2"
```

If

c1
 has not yet been finished when
c2
 is started,

c1
 and
c2
 will now run in parallel, provided that the ports

PA
,
PD
, and
PY
 are disjunct, and at least
one of the two contexts contains only Smart Scale channels.

Note also the following points
in this example:

The primary timing has not been changed between the start of
c1
 and

c2
. If it had, then most probably the master clock period would have been
recalculated, and this would have stopped
c1
.

The first context is started with
SQST RUN
, not
FTST?
.
This is required for parallel execution; using
FTST?
 would block the
firmware interface until execution of
c1
 is finished and

FTST?
 has returned its global PASS/FAIL result.

If both contexts contain DC Scale channels,
c2
 will not
be started, and an error message will be issued.
c1
 will continue to run.

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
