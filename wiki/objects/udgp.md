---
type: object
title: UDGP - (UnDefine GrouP)
layer: L1
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.296_UDGP_-__UnDefine_GrouP.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# UDGP - (UnDefine GrouP)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **301 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.296_UDGP_-__UnDefine_GrouP.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
UDGP {(group)}
```

### Parameters

[表]
行 1:
  group
  Defines the name of the group of pins to be removed. The symbol @ can be
    used to dismantle all groups. If more than one group is to be removed, the names must be
    separated by a comma.

### Example

```
UDGP (Qout)
```

This command dismantles the group entitled Qout.

<!-- 语法节 end -->

## 是什么

**文档事实** UDGP（UnDefine GrouP）拆除（dismantles）一个此前由 `[[dfgp]]`（DFGP）或 `[[dfge]]`（DFGE）定义的 pin group。

**文档事实** `group` 参数给出要移除的 pin group 名称；符号 `@` 可拆除所有组，多个组名以逗号分隔。

**文档事实** Defining pin groups 页的 “Deleting group definitions” 节写明：UDGP 删除 fixed 与 expression based 两种组定义。

**文档事实** 该页还说明 pin group 不支持 DPS pins 与 analog pins；expression based group 会在其依赖的 fixed group 改变时自动改变。

**文档事实** Application 段把 UDGP 归入 Pin configuration，并指向 Configuration Setup Commands。

## 典型用法

**文档事实** 示例 `UDGP (Qout)` 拆除名为 Qout 的组。

**文档事实** 一次拆除多个组时以逗号分隔组名；拆除全部组用 `UDGP (@)`（参数说明）。

**文档事实** 固定组与表达式组都可被删除（Defining pin groups 的 Deleting group definitions）。

**文档事实** 组名来自此前的 DFGP/DFGE 定义；Defining pin groups 页说明查看表达式组成员要用 DFGP?，DFGE? 返回的是定义表达式。

**建议** 删除前先用 `DFGP? (name)` 核对组是否存在及成员，确认要拆除的是目标组，而不是同名或成员相近的另一个组。

## 和谁有关

- **文档事实** `[[dfgp]]` — DFGP 定义固定组；本命令拆除 DFGP 定义的组。
- **文档事实** `[[dfge]]` — DFGE 用集合表达式定义组；本命令也拆除 DFGE 定义的表达式组（Defining pin groups 的 Deleting group definitions）。
- **文档事实** `[[dfpt]]`、`[[udpt]]` — 02.06.03 的 “Commands for pin groups and ports” 把 DFGP、UDGP、DFPT、UDPT 列为一族：前两者处理 pin group，后两者处理 port。
- **文档事实** Defining pin groups（`02.06.03.01.06`）— 该页的 Deleting group definitions 节与 Related information 都指向 UDGP，并说明它删除 fixed 与 expression based 两种组定义。
- **文档事实** Pin configuration setup commands（`02.06.03`）与 Introduction（`02.06.03.01.01`）— 入边显示 UDGP 被列为 “Commands for pin groups and ports” 的成员。
- **文档事实** List of commands — 入边显示 UDGP 列在命令参考总表。

## 版本

**文档事实** Functional changes 记：Introduced before SmarTest 6.3.2。

## 出处

- `02_System_reference/02.06_Command_Reference/02.06.02.02.296_UDGP_-__UnDefine_GrouP.htm`，主源，含概览、Syntax、Parameters、Application、Example 与 Functional changes，已用 `show.py 02.06.02.02.296` 读取。
- `02_System_reference/02.06_Command_Reference/02.06.03.01.06_Defining_pin_groups.htm`，用于确认 UDGP 删除 fixed/expression based 两种组定义、pin group 不支持 DPS/analog pins，已用 `show.py 02.06.03.01.06` 读取。
- 命令族与入边关系取自 `extract/objpack.py` / `edges.jsonl`。
