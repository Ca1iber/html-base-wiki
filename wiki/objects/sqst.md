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

（待补）

## 典型用法

（待补）

## 和谁有关

（待补）

## 版本

（待补）

## 出处

（待补）
