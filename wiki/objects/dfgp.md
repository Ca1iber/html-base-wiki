---
type: object
title: DFGP, DFGP? - (DeFine GrouP)
layer: L1
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# DFGP, DFGP? - (DeFine GrouP)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,104 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### DFGP

```
DFGP {pin_type}, {(pinlist)}, {(pin_group)}
```

### DFGP?

```
DFGP? {(pin_group)}
```

returns:

```
DFGP {pin_type}, {(pinlist)}, {(pin_group)}
```

### Parameters

[表]
行 1:
  pin_type [跨 5 行]
  Defines the type of pins in the [跨 2 列]
    group. This can be:
行 2:
  I
  Identifies a group of device input pins.
行 3:
  O
  Identifies a group of device output pins.
行 4:
  DC
  Identifies a group of DC type pins.
行 5:
  X
  Identifies a group that may contain pins of any type.
行 6:
  pinlist
  The names of the pins to be [跨 2 列]
    included in the group. All pin names must be separated with a comma.
行 7:
  pin_group
  The name assigned to the pin [跨 2 列]
    group. You can use the same name for groups of different type.
    
    The symbol @ can be used with the DFGP? query to
    list all groups previously defined using the DFGP command. If you query
    a non-existent group, the system returns nothing.
    
    Maximum number of characters is 16 for 32-bit SmarTest and 64 for 64-bit SmarTest.

### Example

```
DFGP O,(Q0,Q1,Q2,Q3),(outputs)
```

This example defines a group
called
outputs
 which contains pins Q0, Q1, Q2 and Q3.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.htm>` 的 `## Errors`、`## Warnings` 段。**不是转述。**
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

 More than 2400 groups are defined.

 The intended group name is already being used for a pin.

 The intended group name is already being used for a DPS pin.

 There are too many pins in the group (max. number of pins in
all
 groups is 1843200).

### Warnings

A warning is generated if:

 A pin cannot be part of the specified group and is therefore ignored.

 A group cannot be part of the specified group and is therefore ignored.

<!-- 报错节 end -->

## 是什么

**文档事实** DFGP (DeFine GrouP) 定义一组固定的数字 pin。pin group 可以像单个 pin 一样使用；DFGP? 查询返回命名组中的 pin 与 pin type 列表。

**文档事实** 重复使用同一个组名时，新组定义中的 pin 会追加到原定义的 pin 上，而不是替换原定义。

**文档事实** pin_type 可为 I（device input pins）、O（device output pins）、DC（DC type pins）、X（可含任意类型 pin 的组）。

**文档事实** pinlist 中的 pin 名必须以逗号分隔。pin_group 的名称最长 32-bit SmarTest 为 16 字符、64-bit SmarTest 为 64 字符。

**文档事实** `@` 可与 DFGP? 查询一起使用，列出此前用 DFGP 定义的所有组；查询不存在的组时系统不返回内容。

**文档事实** 应用范围是 Pin Configuration（见 Configuration Setup Commands）。固定组与表达式组相对：固定组由 pin 列表定义，不依赖其他组；表达式组由 DFGE 用集合运算定义，会随所依赖的固定组变化而自动变化。

**文档事实** DFGP 不对组类型做 plausibility check：例如可以把 output pin 加入 I 类型的组而不被固件拒绝；实际对组执行动作时，SmarTest 只考虑符合该组类型的 pin。

**文档事实** pin group 不支持 DPS pins 与 analog pins。

**推断** 因此 DFGP 是 pin setup 阶段的批量抽象：先给一组数字 pin 命名，后续命令的 pin 参数直接引用组名，就能对整组执行同一动作，而不必重复列 pin。

## 典型用法

**文档事实** 定义组：`DFGP O,(Q0,Q1,Q2,Q3),(outputs)` 定义名为 `outputs` 的组，包含 Q0、Q1、Q2、Q3。

**文档事实** 查询组：`DFGP? (outputs)` 返回 `DFGP O,(Q0,Q1,Q2,Q3),(outputs)`；`DFGP? (@)` 列出所有此前定义的组。查询不存在的组不返回内容。

**文档事实** 组名可用于其他命令的 pinlist 参数。文档中有明确实例的命令包括 DRLV、RCLV、PCLK、VCLK、VTIM、STRS、TTMD、DCUD、SHSP、SREC、TTRS；这些页均注明参数可包含 DFGP 定义的组。

**文档事实** 组可被 DFGE 表达式直接引用：DFGE 示例先用 `DFGP? (SCAN)`、`DFGP? (OUT)` 取得两个固定组，再 `DFGE O,"SCAN * OUT",(SCAN_OUT)` 求交集；查看成员时要用 `DFGP?`，因为 `DFGE?` 返回的是定义表达式。

**文档事实** 组名不能与已有 pin 或 DPS pin 重名；最多 2400 个组；所有组的 pin 总数上限为 1843200（详见本页报错节）。

**建议** 组名控制在 16 字符以内并使用明确的用途前缀，这样同一份 pin 配置在 32-bit 与 64-bit SmarTest 上都能原样使用。

**建议** 定义后先用 `DFGP? (name)` 核对实际成员，再在 DRLV、RCLV、PCLK 等命令中引用组名；重复定义同名组会追加成员，容易与预期不符。

## 和谁有关

- **文档事实** UDGP：取消由 DFGP 或 DFGE 定义的组。
- **文档事实** DFGE：用表达式定义组；DFGP 定义的组可作为 DFGE 表达式的参数；DFGE? 对表达式组返回 DFGE 定义，对 digital fixed groups 返回 DFGP 定义；查看表达式组成员要用 DFGP?。
- **文档事实** DFPT 与 UDPT：02.06.03 的 "Commands for pin groups and ports" 把 DFGP、UDGP、DFPT、UDPT 列为一族，分别处理 pin group 与 port。
- **文档事实** Defining pin groups：该页说明 fixed groups 用 DFGP 定义、每种 fixed group 有 type，并说明 pin group 不支持 DPS 与 analog pins。
- **文档事实** DRLV、RCLV、PCLK、VCLK、VTIM、STRS、TTMD、DCUD、SHSP、SREC、TTRS：这些命令页说明 pin 参数可包含 DFGP 创建的组（objpack 入边引文）。
- **文档事实** Pin configuration setup commands / Configuration Setup Commands：DFGP 的 Application 指向 Pin Configuration；02.06.03 页把 DFGP 列入 pin group 与 port 命令。
- **文档事实** List of commands：DFGP 列在命令参考总表中。
- **文档事实** TTMD 与 SREC：前者说明 `@` 可指定所有已配置 pin，后者说明 pin 可来自 DFGP 或 DFGE 定义的组。

## 版本

**文档事实** Functional changes 记：Introduced before SmarTest 6.3.2。

## 出处

- `02_System_reference/02.06_Command_Reference/02.06.02.02.60_DFGP__DFGP__-__DeFine_GrouP.htm`，主源，含 DFGP、DFGP?、Parameters、Application、Errors、Warnings、Example 与 Functional changes，已用 `show.py` 读取。
- `02_System_reference/02.06_Command_Reference/02.06.03.01.06_Defining_pin_groups.htm`，用于固定组/表达式组的区别、组类型与 DPS/analog pin 限制，已用 `show.py` 读取。
- 命令族关系与引文取自 `extract/objpack.py` 的入边索引。
