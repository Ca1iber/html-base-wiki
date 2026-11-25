---
type: object
title: DFPT, DFPT? - (DeFine PorT)
layer: L1
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.66_DFPT__DFPT__-__DeFine_PorT.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# DFPT, DFPT? - (DeFine PorT)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **874 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.66_DFPT__DFPT__-__DeFine_PorT.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### DFTP

```
DFPT {(pinlist)}, {(port)}
```

### DFPT?

```
DFPT? {(portlist)}
```

returns:

```
DFPT {(pinlist)}, {(port)}
```

### Parameters

[表]
行 1:
  pinlist
  Pin name or names. If more than one pin is required, the names must be separated
    with a comma. The @ character can be used to refer to all configured pins. The pin
    list can contain digital or DC Scale pins, or a combination of both.
行 2:
  port
  The name of the port to which the pins are associated. The maximum number of
    characters is 16 for 32-bit SmarTest and 64 for 64-bit SmarTest.
行 3:
  portlist
  List of ports for which the associated pins are to be displayed. Specify (@@) to
    retrieve the definitions of all ports.

### Example

```
DFPT? (port_1, port_2)
```

returns:

```
DFPT (CP_1,DS7_1,DS0_1,I/O7_1,...,I/O0_1,Q7_1,
Q0_1,S1_1,S0_1,_MR_1),(port_1)
DFPT (CP_2,DS7_2,DS0_2,I/O7_2,...,I/O0_2,Q7_2,
Q0_2,S1_2,S0_2,_MR_2),(port_2)
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
