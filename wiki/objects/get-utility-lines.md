---
type: object
title: GetUtilityLines
layer: L2
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.05.04.05_GetUtilityLines.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# GetUtilityLines

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,842 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.05.04.05_GetUtilityLines.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Parameters

[表]
列: Parameter | Type | Description
行 1:
  blockId
  INT
  The utility pogo block to query.
    
    The valid value is from 0 to 8.
    
    If the three‑digit format for pogo blocks is used, the valid range is
    165 ... 172.
    
    For the second optional `Utility Card`（raw: `351250.htm`） of EXA Scale
    systems, the utility pogo blocks can be defined using only
    the three‑digit format. The valid range for the
    second card is
    265 ... 272.
    
    See also `Utility pogo block mapping`（raw: `347642.htm#_347642__s_Utility_pogo_block_mapping`）
    in `Utility pogo block - Utility Card (V93000 EXA Scale systems)`（raw: `347642.htm`）.
    
    0 means all utility line blocks and other
    valid number means the specified utility block.

### Example

### Output for two utility cards of an V93000 EXA Scale system

Output with parameter
blockId
 of the test method set to 0. The pogo blocks
of the second optional
`Utility Card`（raw: `351250.htm`）
 are listed as 265 to
272.

```
get utility block 1 =01111100101110100100010010011010
get utility block 2 =10000110110110010001101100111000
get utility block 3 =01110100010101011011111110110101
get utility block 4 =00111011101100011001010011110010
get utility block 5 =11010100110011111000100111100010
get utility block 6 =11101110100001011111010001010011
get utility block 7 =10010001011011000101101011010011
get utility block 8 =10001110010111000011001010111011
get utility block 265 =00001101000000110101001000000001
get utility block 266 =11000100010111010111011011111101
get utility block 267 =00000100110101111001100110111110
get utility block 268 =01000000100110101010011000111100
get utility block 269 =01001100010101101010011001100011
get utility block 270 =11100000010000000100100000111000
get utility block 271 =10001000000101000001110001010101
get utility block 272 =11101011100101100011100010011001
```

<!-- 语法节 end -->

## 是什么

**文档事实** GetUtilityLines 是一个 test method，读取最多 512 条 utility line 的状态，并在 report window 中显示。

**文档事实** 它仅适用于 universal test method。

**文档事实** utility line 状态也可在 93000 Hardware perspective 的 Utility Line view 中查看。

**文档事实** 使用该 test method 时，本 test suite 指定的 primary sets 不被使用，而使用前一个已执行 test suite 的 primary sets。

**文档事实** 唯一参数 blockId（INT）指定要查询的 utility pogo block：0 表示全部 utility line block，其他有效值表示指定 block。

**文档事实** blockId 的合法范围：0–8；若使用三位格式，范围为 165…172；EXA Scale 系统第二个可选 Utility Card 只能使用三位格式，范围为 265…272。

**推断** 该 test method 的文档定位是状态观测：读回 utility line 状态并打印；文档没有说明它产生 pass/fail 判定或写回状态。

## 典型用法

**文档事实** 文档示例把 blockId 设为 0，输出两张 utility card 的所有 block 状态；第二个可选 Utility Card 的 pogo block 列为 265–272。

**文档事实** 输出格式为 `get utility block <n> =<32 位二进制串>`，例如 `get utility block 1 =01111100101110100100010010011010`；示例列出 block 1–8 与 265–272。

**文档事实** 每个 block 的状态为 32 位串。GET_UTILITY_LINES_STATUS 页说明 utility lines 按 pogo block 组织、每 block 32 条，test head 配置可提供 32/64/256/512 条，对应 1/2/8/16 个 utility block。

**文档事实** 本页 Related information 指向 SetUtilityLines 与 GET_UTILITY_LINES_STATUS。

**建议** 需要按 block 排查时，先用 blockId=0 获取全量输出，再针对 1–8 或 265–272 中的单个 block 复查。

## 和谁有关

- **文档事实** SetUtilityLines，本页 Related information 列出它；SetUtilityLines 设置最多 512 条 utility line，并同样说明 primary sets 使用前一个已执行 test suite 的。
- **文档事实** GET_UTILITY_LINES_STATUS，本页 Related information 列出它；它是读取所有 utility input line 状态的 test method API，返回指定 block 的状态（"0" 表示 on，"1" 表示 off），并给出 utility block 与 utility line 数量的对应关系。
- **文档事实** Utility Pins editor（02.08.04.18.03.01.04），objpack 入边引文说明可通过 test method library（GetUtilityLines 与 SetUtilityLines）、test method API 或自写 test method 访问 utility pins。
- **文档事实** Miscellaneous test methods（02.07.05.04）与 List of predefined universal test methods（02.07.02.08），两个索引页都把 GetUtilityLines 列入，前者还给出 "Gets the status of the utility lines" 的一句话说明。
- **文档事实** Utility Card（V93000 EXA Scale systems）与 Utility pogo block mapping，blockId 参数说明和示例都以它们为参照，第二张卡的 block 为 265–272。
- **推断** GetUtilityLines（读）与 SetUtilityLines（写）构成 utility line 的读写对，GET_UTILITY_LINES_STATUS 提供同一状态信息的 API 入口；文档没有说明两者返回结果是否逐位一致。

## 版本

**文档事实** Functional changes 记载：

- Introduced in SmarTest 6.5.2
- SmarTest 7.2.1：utility line 最大数量增至 256
- SmarTest 7.10.2：最多 512 条 utility line，并支持三位 utility pogo block 编号

## 出处

- `02_System_reference/02.07_Test_Method_Reference/02.07.05.04.05_GetUtilityLines.htm`，主源，含概述、Parameters、Example 与 Functional changes。
- `02_System_reference/02.07_Test_Method_Reference/02.07.05.04.07_SetUtilityLines.htm`、`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.108_GET_UTILITY_LINES_STATUS.htm`，用于核对读写配套关系与每 block 32 条的说明（已用 show.py 读取）。
- Utility Pins editor、Miscellaneous test methods、List of predefined universal test methods 的引文取自 `extract/objpack.py` 入边索引。
