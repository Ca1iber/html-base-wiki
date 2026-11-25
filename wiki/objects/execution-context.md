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

**文档事实** 执行上下文（execution context）由“端口列表 + 名字”构成，用于独立运行一个或多个 multiport burst 的端口子集；激活方式是在启动测试时指定该名字。一般情况下，context 的端口必须是当前 start label 中端口的子集（本页首段）。

**文档事实** 与“不完整 multiport burst”相比，execution context 更灵活，不必为每个端口子集新建 multiport burst；其主要优势是能让不同 sequencer 任务并行执行（本页正文）。

**文档事实** 并行执行受限制：两个 context 只有在不共享任何 channel 时才能并行，否则后启动者报错且不启动，先启动者继续运行。

**文档事实** 两个 context 要并行，先启动的那个必须以 `SQST RUN`（或测试方法 API `START_TEST()`）启动；若用 `FTST?`（或 `FUNCTIONAL_TEST()` / `EXECUTE_TEST()`）启动，第二个 context 要等第一个返回全局 PASS/FAIL 后才启动。

**文档事实** master clock 周期的重算会停止所有用户定义的 sequencer 任务，因此两个待并行的 context 之间必须避免会触发重算的 primary timing 变更。

**文档事实** 若两个 context 都含 DC Scale channel 的端口，则不能并行：后启动者报错且不启动，先启动者继续运行。

**文档事实** 端口的另一约束：context 只有在所有端口都包含在当前 start label 中时才能运行；protocol port 是例外，它不允许出现在 start label 中，即使它被包含在某个 context 内。

**文档事实** execution context 与不完整 multiport burst 不互斥，可以为不完整 multiport burst 的端口子集定义并运行 execution context。

## 典型用法

**文档事实** 固件侧用 `SQEC "c1",(PA,PD)` 与 `SQEC "c2",(PY)` 定义两个 context，用 `SQST RUN,"c1"` 启动第一个；再用 `SQSL "mu_burst2"` 切换 start label，然后 `SQST RUN,"c2"` 启动第二个。

**文档事实** 本页例子先以 `SQSL?` 查当前 start label（`< SQSL "mu_burst1"`），用 `SQLB? "mu_burst1",MPBU,(@@)` / `SQLB? "mu_burst2",MPBU,(@@)` 查看两个 multiport burst 的端口定义。

**文档事实** 在例子中，c1 尚未结束时启动 c2；若 PA、PD、PY 互斥，且两个 context 中至少一个只含 Smart Scale channel，则 c1 与 c2 并行运行。

**文档事实** 查询最近启动的 execution context：`SQLC?` 按端口返回信息，`SQSC?` 跨所有端口返回。

**文档事实** 测试方法侧可用 `SEQUENCER_CONTEXT`、`SEQUENCER_CONTEXT_ITEM` 编程定义 execution context，协议感知场景用 `INDEPENDENT_TEST`；测试方法示例见 `SEQUENCER_CONTEXT` 的描述。

**文档事实** context 由 `SQEC` 定义、`SQRC` 删除；启动时把 context 名加到执行测试的命令/查询（如 `FTST?` 或 `SQST RUN`）上。

**建议** 要让两个 context 真正并行，先启动者用 `SQST RUN`/`START_TEST()` 而不是 `FTST?`/`FUNCTIONAL_TEST()`，并确认两者端口/通道互斥、均为纯 Smart Scale（不含 DC Scale），且在两者之间不改 primary timing。

## 和谁有关

- **文档事实** SQEC：本页 “Related firmware commands” 说明 context 由 `SQEC` 定义、`SQEC?` 查询其定义。
- **文档事实** SQRC：本页说明 execution context 由 `SQRC` 删除。
- **文档事实** SQST：本页用 `SQST RUN,"c1"` 启动 context；`SQST` 文档也称 sequencer 集合由 execution context（端口列表）确定，并回链本页。
- **文档事实** FTST：本页说明用 `FTST?` 启动会阻塞固件接口、无法并行，是反例。
- **文档事实** START_TEST：本页说明用 `START_TEST()` 启动可满足并行条件；`START_TEST`、`EXECUTE_TEST`、`FUNCTIONAL_TEST`、`DIGITAL_CAPTURE_TEST`、`NB_DIGITAL_CAPTURE_START/END`、`WAIT_TEST_DONE` 等页的 `context` 参数说明均回链本页。
- **文档事实** SEQUENCER_CONTEXT、SEQUENCER_CONTEXT_ITEM、INDEPENDENT_TEST：本页 “Related Test Method APIs” 明确列为 execution context 的编程入口。
- **文档事实** SQLC?、SQSC?：本页称两者用于查询最近启动的 execution context（分别按端口与跨所有端口）。
- **文档事实** GET_FUNCTIONAL_RESULT：其 `context` 参数说明为“该 context 最后一次执行的测试”，并回链本页（回链证据）。
- **文档事实** SMC_EXECUTE_TEST、SMC_FUNCTIONAL_TEST、SMC_DIGITAL_CAPTURE_TEST、SMC_NB_DIGITAL_CAPTURE_END、SMC_WAIT_TEST_DONE、SMC_EXECUTE_TMU_TEST：这些 SmartCalc API 的 context 参数说明回链本页（回链证据）。
- **文档事实** TIMING_OFFSET_SEARCH_TASK、DIGITAL_OFFSET_SEARCH_TASK/PINS、TORN、DCGM、DPSR、PRLT、STRS、SQIT：这些命令/API 的 context 参数说明回链本页（回链证据）。
- **文档事实** Incomplete multi-port setups：本页与它对比，并说明两者可共存。
- **文档事实** Concurrent test framework（CCF-ISR）：其文档称 CCF 会按端口名为 CCF-ISR 模式创建 sequence context，并指向本页。
- **文档事实** Independent protocol test：其文档要求协议端口与仿真端口从不同 execution context 启动。
- **文档事实** SEQUENCER_STATUS：其文档明确不支持 execution contexts（回链证据）。

## 版本

**文档事实** `Functional changes`：Introduced in SmarTest 7.2.0。

## 出处

- 主源：`02_System_reference/02.06_Command_Reference/02.06.07.01.08.05.03.02.03_Using_execution_contexts.htm`（定义、Restrictions、Related firmware commands、Related Test Method APIs、Example、Functional changes）。
- 回链证据：由 `extract/objpack.py` 对本 rel 生成的“谁引用本页”清单，含 SQST、FTST、GET_FUNCTIONAL_RESULT、SMC_*、SEQUENCER_STATUS、CCF、DPSR、TORN、DCGM 等页的引用片段。
