---
type: object
title: PRLT? - (request Parallel ResuLTs)
layer: L1
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.183_PRLT__-__request_Parallel_ResuLTs.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# PRLT? - (request Parallel ResuLTs)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **887 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.183_PRLT__-__request_Parallel_ResuLTs.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
PRLT? ["exec_context",] {site}
```

returns:

```
PRLT {site}, {"result"}
```

### Parameters

[表]
行 1:
  exec_context
  An execution context. For more information
    on execution contexts see `Using execution contexts`（raw: `135848.htm`）.
行 2:
  site
  The site parameter is
    
    number
    A single integer representing the site number.
    
    ALL
    Means that all the results of all configured sites are
    returned.
行 3:
  result
  The result parameter is a string containing one character for every
    site. The nth character stands for
    site n. Possible characters are:
    
    P
    If the last test passed on all pins.
    
    F
    If the last test failed at any pin.
    
    0
    If the site was masked during the last test.

### Example

```
PRLT? ALL
```

returns:

```
PRLT ALL, "PF0"
```

In
this example, site 1 passed the last test, site 2 failed it, and site 3 was masked during the
test.

<!-- 语法节 end -->

## 是什么

**文档事实**：PRLT? 并行返回指定 site 上次执行测试的 global pass/fail 结果；可在一步内得到所有 site（不仅是 query focus 所在 site）的 global 结果。query focus 所在 site 的 global 结果也可由 FTST? 给出。

**文档事实**：`exec_context` 为可选 execution context；`site` 可为单个 site 编号或 `ALL`（返回所有已配置 site 的结果）；返回字符串 `result` 每个 site 一个字符，第 n 个字符代表 site n：`P` 表示上次测试所有 pin 通过，`F` 表示任一 pin 失败，`0` 表示该 site 在上次测试中被 mask。

**文档事实**（顺序约束）：PRLT 取得的 pass/fail 结果会被 CSAS 与 PSAS 作废；文档建议在相关 functional test 之后、CSAS/PSAS 之前直接使用 PRLT。该行为同样适用于 API：`GET_FUNCTIONAL_RESULT()` 必须先于任何 `DPS_AUX_PIN_TASK.check...()` 调用，否则结果无效。

**文档事实**：Application 归属 Test Results。

## 典型用法

**文档事实**：`PRLT? ALL` 返回 `PRLT ALL, "PF0"`，表示 site 1 通过、site 2 失败、site 3 在上次测试中被 mask（示例）。

**文档事实**：查询单个 site 用 `PRLT? {site}`；带 execution context 时用 `PRLT? ["exec_context",] {site}`。

**文档事实**：multi-site 下 `GET_FUNCTIONAL_TEST()` 不适用，文档改用 PRLT? 固件命令取 pass/fail（Hidden Upload for Digital Capture 页）。

**建议**：紧接 functional test 之后、调用 CSAS/PSAS 之前读取 PRLT，避免结果被作废；需要 DPS 状态或调用 DPS_AUX_PIN_TASK.check...() 时，务必先取 PRLT / GET_FUNCTIONAL_RESULT()。

## 和谁有关

- `FTST?`：**文档事实**——正文说 query focus site 的 global 结果也由 FTST? 给出。
- `CSAS`、`PSAS`：**文档事实**——PRLT 结果会被这两个命令作废；入边显示 CSAS/PSAS 页也重复此说明。
- `GET_FUNCTIONAL_RESULT()`、`DPS_AUX_PIN_TASK.check...()`：**文档事实**——正文说 API 侧同样要求 `GET_FUNCTIONAL_RESULT()` 先于 `DPS_AUX_PIN_TASK.check...()`，否则结果无效；入边含 GET_FUNCTIONAL_RESULT 与 DPS_AUX_PIN_TASK 页。
- `PDMM`：**文档事实**——入边显示 PDMM 页说需指定 `PRLT` 额外参数才能用 PRLT? 取所有 active site 的 pass/fail，且 PDMM 额外存一个 global pass/fail 结果供后续 PRLT? 查询。
- `Hidden Upload for Digital Capture`：**文档事实**——入边说明 multi-site 下 `GET_FUNCTIONAL_TEST()` 不工作，改用 PRLT? 取 pass/fail。
- `Test Result Commands`：**文档事实**——Application 指向 Test Result Commands，PRLT? 属其命令之一。

## 版本

**文档事实**：Functional changes 仅记 "Introduced before SmarTest 6.3.2"；这是哨兵值，表示在本套文档覆盖起点之前已存在，并非 6.3.2 的变更。

## 出处

- `02_System_reference/02.06_Command_Reference/02.06.02.02.183_PRLT__-__request_Parallel_ResuLTs.htm`——正文、参数、Example、Application 与 Functional changes 均取自本篇（已用 `show.py 02.06.02.02.183` 读取；本页无独立 Errors 段）。
- `和谁有关` 的入边关系取自 `extract/objpack.py` 的 `edges_in` 索引。
