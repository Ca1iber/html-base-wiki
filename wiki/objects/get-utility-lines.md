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

（待补）

## 典型用法

（待补）

## 和谁有关

（待补）

## 版本

（待补）

## 出处

（待补）
