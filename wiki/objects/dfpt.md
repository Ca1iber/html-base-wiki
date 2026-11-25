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

**文档事实** DFPT 即 DeFine PorT，用于定义一个 port（端口）；若重用已有 port 名，新定义中的引脚会追加到原定义的引脚之后。

**文档事实** DFPT? 查询用于检查单个或全部 port 定义。

**文档事实** 参数 pinlist 可含数字或 DC Scale 引脚，或二者组合；多个引脚用逗号分隔，`@` 可引用所有已配置引脚。

**文档事实** port 是引脚关联的端口名；32-bit SmarTest 中最多 16 个字符，64-bit SmarTest 中最多 64 个字符。

**文档事实** DFPT? 的 portlist 指定要显示关联引脚的 port 列表；`(@@)` 可检索所有 port 的定义。

**文档事实** 文档把 DFPT 归入 Pin Configuration，见 Configuration Setup Commands。

**文档事实** 源文档语法节的标题写作 "DFTP"（原文如此），但正文与命令形式均为 DFPT。

**文档事实** Defining ports 页说明每个 port 都可作为 pin group 使用。

**推断** DFPT 负责 port 的归组定义，本身不改变引脚的电气属性。

## 典型用法

**文档事实** 示例 `DFPT? (port_1, port_2)` 返回两个 port 的定义：`DFPT (CP_1,DS7_1,DS0_1,I/O7_1,...,I/O0_1,Q7_1,Q0_1,S1_1,S0_1,_MR_1),(port_1)` 与对应的 `port_2` 行。

**文档事实** 定义形式为 `DFPT {(pinlist)}, {(port)}`，即把一组引脚关联到一个 port 名。

**文档事实** `@` 可用于 pinlist 引用所有已配置引脚；`(@@)` 可用于查询所有 port 的定义。

**文档事实** 重用 port 名不会替换原定义，而是把新引脚追加到原 port。

**文档事实** Defining ports 页补充：默认 port `(@)` 由系统提供、包含所有引脚；用户自定义 port 用 DFPT 创建、用 UDPT 删除；DFPT? 返回一个或多个 port 的定义。

**建议** 重定义 port 前先用 DFPT? 查回现有成员，因为同名 DFPT 调用是追加而非覆盖，重复执行会累积引脚。

## 和谁有关

- **文档事实** UDPT，Defining ports 页说明用户自定义 port 由 DFPT 创建、由 UDPT 删除，二者是 port 生命周期的一对命令。
- **文档事实** DFGP、UDGP，Pin configuration setup commands 与 Introduction 页把 DFGP、UDGP、DFPT、UDPT 并列为 "Commands for pin groups and ports"。**推断** 从命名与分组看，DFGP/UDGP 面向 pin group，DFPT/UDPT 面向 port。
- **文档事实** Defining ports，该页说明 port 与 pin group 的关系：port 不得与 pin 或 pin group 同名；port 定义对应固定组定义，不支持表达式；port 不关联类型，但每个 port 都可用作 pin group；port 与 pin group 一样不能包含分配给 analog instruments 和 DPS 通道的引脚。
- **文档事实** Pin configuration setup commands（02.06.03）与 Introduction（02.06.03.01.01），两个索引页把 DFPT 列入 pin groups and ports 命令组（引文取自 objpack 入边）。
- **文档事实** List of commands，索引页把 DFPT 列入命令清单（引文取自 objpack 入边）。
- **推断** DFPT 位于引脚配置层，与 pin group 命令平行但语义不同：port 更接近「可独立测试的引脚集合」，并可作为 pin group 参与后续命令。

## 版本

**文档事实** Functional changes 记载：Introduced before SmarTest 6.3.2。

（该段没有其他版本条目。）

## 出处

- `02_System_reference/02.06_Command_Reference/02.06.02.02.66_DFPT__DFPT__-__DeFine_PorT.htm`，主源，含概述、Syntax（标题原文为 DFTP）、Parameters、Application、Example 与 Functional changes。
- `02_System_reference/02.06_Command_Reference/02.06.03.01.07_Defining_ports.htm`，用于核对 port 与 pin group 的关系、UDPT 与默认 port `(@)`（已用 show.py 读取）。
- Pin configuration setup commands、Introduction、List of commands 的引文取自 `extract/objpack.py` 入边索引。
