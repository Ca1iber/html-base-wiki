---
type: object
title: SQST, SQST? - (SeQuencer STate)
layer: L1
stage: pattern
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.241_SQST__SQST__-__SeQuencer_STate.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# SQST, SQST? - (SeQuencer STate)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **2,198 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.241_SQST__SQST__-__SeQuencer_STate.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### SQST

SQST
 {
seq_state
}
[,"
exec_context
"]

### SQST?

```
SQST? ["exec_context"]
```

returns:

```
SQST {seq_state}
```

### Parameters

[表]
行 1:
  seq_state [跨 8 行]
  Gives the state of the sequencer: [跨 2 列]
行 2:
  OFF
  In the OFF state, both the sequencers and the clock
    are off. All pins go into the high-z state.
    
    This option can only be applied to all execution contexts.
行 3:
  HALT
  In the HALT state, both the sequencer and the clock
    are off, and the drivers keep their last level or remain in high-z state if already in
    high-z state.
    
    Note that you cannot pass directly from HALT to OFF
    or from OFF to HALT. You must first pass to
    BRK in both cases.
    
    This option can only be applied to all execution contexts.
行 4:
  BRK
  In the BRK state, the clock is on and the break
    waveform is applied to the DUT.
    
    This option can only be applied to all execution contexts.
行 5:
  ABRT
  This is not a sequencer state, but an instruction to change the state of
    an execution context from RUN to BRK.
    ABRT requires that an execution context is specified.
行 6:
  CBRK
  This is not a sequencer state, but a conditional instruction. If no
    context is in BRK or RUN state, the state of the
    global context will be changed to BRK. If any context is in
    BRK or RUN state, nothing will be done.
行 7:
  RUN
  In the RUN state, the clock is on and the sequencer applies
    vectors to the DUT. This option can be applied to a specified execution context.
行 8:
  Note that if the sequencer state changes [跨 2 列]
    from OFF or BRK to RUN, the
    sequencer runs with the global settings that have previously been defined with `SQGB, SQGB? - (SeQuencer GloBal)`（raw: `98746.htm`）.
行 9:
  exec_context
  An execution context. In the command, this [跨 2 列]
    parameter can only be added to the sequencer state RUN and the
    instruction ABRT. It must be added if ABRT is
    specified. For more information on execution contexts see `Using execution contexts`（raw: `135848.htm`） .
    
    If the query is issued without a context, then RUN will be returned if
    there is at least one context that is in the RUN state.

### Example

```
SQST RUN
```

This example starts a global sequencer run.

<!-- 语法节 end -->

## 是什么

**文档事实**：SQST 用于控制一组 sequencer 的状态。该 sequencer 组由 execution context 决定；execution context 是一组 port，SQST 控制这些 port 上的 sequencer。用户定义的 execution context 的 port 必须是当前 start label 所含 port 的子集；该 label 的 port 集合构成 global execution context。

**文档事实**：有些状态只能作用于 global execution context，这隐含所有用户定义 context 也进入该状态；但 RUN 与（间接的）BRK 可在 execution context 级别赋值。SQST? 返回当前的最大状态。

**文档事实**：状态取值：OFF（sequencer 与 clock 均关，所有 pin 进入 high-z；只能作用于全部 context）、HALT（sequencer 与 clock 关，driver 保持最后电平，或已处于 high-z 则保持 high-z；不能从 HALT 直接到 OFF 或从 OFF 直接到 HALT，两种情况都要先经 BRK；只能作用于全部 context）、BRK（clock 开，break waveform 施加到 DUT；只能作用于全部 context）、RUN（clock 开，sequencer 向 DUT 施加向量；可作用于指定 execution context）。从 OFF 或 BRK 变为 RUN 时，sequencer 使用先前由 SQGB 定义的 global 设置。

**文档事实**：`ABRT` 不是 sequencer 状态，而是把某个 execution context 从 RUN 变为 BRK 的指令，要求指定 execution context。`CBRK` 也不是状态，而是条件指令：若没有任何 context 处于 BRK 或 RUN，则把 global context 变为 BRK；若已有 context 处于 BRK 或 RUN，则不做任何事。

**文档事实**：`SQST?` 不带 context 时，只要至少有一个 context 处于 RUN 就返回 RUN。

**文档事实**：正文注明 DPS128/DPS64 用 SQST RUN 或 SEQUENCER_STATUS run() 启动 sequencer 时，不能并行执行 dynamic 与 static DC 动作；如需在 dynamic pattern 并行测量请用 profiling。Application 归属 AC tests，并要求用 Relays Control Commands 连接/断开测试系统。

## 典型用法

**文档事实**：`SQST RUN` 启动一次 global sequencer run（示例）。

**文档事实**：用 `BRK` 强制 break 可跳出 endless loop / match loop：文档在 Endless loops、Timed match loop 等页写明用 SQST 的 BRK 参数；`SQST BRK` 也出现在 connect/disconnect 序列中（如 `RLYC CNCT,OFF,(@) PSST ON CNCT ON,(@) SQST BRK`），而 `SQST OFF` 出现在 disconnect 序列中。

**文档事实**：要对单个 execution context 操作 RUN，需带上 `exec_context`；`ABRT` 必须带 execution context。查询用 `SQST? ["exec_context"]`，返回 `SQST {seq_state}`。

**建议**：涉及 HALT/OFF 时记住二者不能直接互转，必须先经 BRK；在 DPS128/DPS64 上并行 DC 测量应改用 profiling。

## 和谁有关

- `SQGB`：**文档事实**——SQST 正文说存在对 SQGB 的依赖；从 OFF/BRK 变 RUN 时使用 SQGB 先前定义的 global 设置；参数表与正文多处链接 SQGB。
- `Using execution contexts`（execution context）：**文档事实**——`exec_context` 参数只能加在 RUN 与 ABRT 上，ABRT 必须指定 context；文档链接该页。
- `SEQUENCER_STATUS`（run()）：**文档事实**——SQST 正文把 SQST RUN 与 SEQUENCER_STATUS run() 并列为启动 sequencer 的方式，并共同受 DPS128/DPS64 不能并行 DC 动作的限制；入边含 SEQUENCER_STATUS 页。
- `DPS128/DPS64`：**文档事实**——正文专门说明其 dynamic/static DC 并行限制并建议用 profiling。
- `Endless loops`、`Counted loops`、`Timed match loop`、`SVEC subroutines`：**文档事实**——入边显示这些页说明用 SQST 的 BRK 参数强制 break 以跳出 loop。
- `Relays Control Commands` / connect–disconnect：**文档事实**——Application 指向 Relays Control Commands；入边显示 disconnect 序列含 `SQST OFF`、连接序列含 `SQST BRK`。
- `DFPN`、`UDEF`：**文档事实**——入边显示 DFPN 要求 sequencer 处于 OFF（参见 SQST）；UDEF 在 sequencer 处于 run 或 break 状态时报错（参见 SQST）。
- `FLUSH`、`CONNECT`：**文档事实**——入边显示激活 master clock 的信息参见 SQST 与 CONNECT。
- `APRM`、`SPRM`：**推断**——入边只给出 `SQST RUN` 链接，推测其页面在激活 primary sets 后以 SQST RUN 启动 sequencer，文档未在入边语境内展开说明。
- `NIFE`：**文档事实**——Fast Sync 页说明在 disconnected 模式下用 SQST 与 NIFE 定义 test processor 上的最大 match port 数。

## 版本

**文档事实**：Functional changes 记：Introduced before SmarTest 6.3.2（哨兵值，表示在文档覆盖起点前已存在）；SmarTest 7.2.0 起可为 RUN 指定 execution context，并新增 `ABRT` 选项。

## 出处

- `02_System_reference/02.06_Command_Reference/02.06.02.02.241_SQST__SQST__-__SeQuencer_STate.htm`——正文、参数表、Example、Functional changes 均取自本篇（已用 `show.py 02.06.02.02.241` 读取；本页无独立 Errors 段）。
- `和谁有关` 的入边关系取自 `extract/objpack.py` 的 `edges_in` 索引。
