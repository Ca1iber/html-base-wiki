---
type: object
title: LSUS, LSUS? - (Level Sets USed)
layer: L1
stage: level
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.155_LSUS__LSUS__-__Level_Sets_USed.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# LSUS, LSUS? - (Level Sets USed)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **904 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.155_LSUS__LSUS__-__Level_Sets_USed.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### LSUS

```
LSUS {level_set_no}
```

### LSUS?

```
LSUS? [level_set_no]
```

returns:

```
LSUS {level_set_no}
```

or:

```
LSUS? [equation_set_no]
```

returns:

```
LSUS {level_set_no}
```

### Parameters

[表]
行 1:
  level_set_no
  Level Set Number. This is the highest number currently allocated to a level set or
    the highest number of set you want to load. The number you type must not exceed the maximum
    number of level sets allowed (defined by the `DSCP`（raw: `98578.htm`） command).
    
    This number is automatically updated to include any new level set as it is created. At
    power-on only one level set (containing the default values) is available.
行 2:
  equation_set_no
  The level equation set number for which the number of currently defined level sets
    is to be determined. Enter an integer in the range 1 to 99. Valid for Equation based
    testing only.

### Example

```
LSUS 4
```

This example defines a maximum of 4 level
sets.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.155_LSUS__LSUS__-__Level_Sets_USed.htm>` 的 `## Errors` 段。**不是转述。**
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

The
level_set_no
 is greater than the range allowed by the
`DSCP`（raw: `98578.htm`）
 command.

The
level_set_no
 is smaller than one.

The
equation_set_no
 is undefined.

<!-- 报错节 end -->

## 是什么

**文档事实**：`LSUS`（Level Sets USed）命令把已定义 level set 的数量设为给定值；新值必须是 1 到允许最大 level set 数之间的整数。本页正文称该最大值由 `CONF, CONF?` 设定（默认 32，最大 256）。

**文档事实**：`LSUS` 可用于删除 set：若想加载到硬件的 level setup 文件包含的 level set 比需要多，可用它删除指定数目以上的所有 set。

**文档事实**：在非 equation-based 环境，`LSUS?` 返回当前已定义的 level set 数；在 equation-based 环境，`LSUS?` 返回指定 level equation set 中当前已定义的 level set 数。

**文档事实**：参数表与 `Errors` 段把 `level_set_no` 的上限来源写作 `DSCP` 命令（不得超过 DSCP 允许的最大 level set 数），与正文的 `CONF` 表述不一致，照原样记录。

**文档事实**：上电时只有一个 level set（含默认值）可用；每新建一个 level set，这个编号会自动更新。`equation_set_no` 取 1 到 99，仅用于 equation based testing。

## 典型用法

**文档事实**：`LSUS 4` 定义最多 4 个 level set。

**文档事实**：`LSUS?` 不带参数查询当前定义的 level set 数；写 `equation_set_no` 时查询该 equation set 中已定义的 level set 数；返回形式为 `LSUS {level_set_no}`。

**文档事实**：`Application` 指明它属于 Level Setup（见 Level Setup Commands）。回链文档 `Delete a Fixed Level Set` 说明可用 `LSUS` 删除单个、多个或全部 level set，但 level set 1 除外。

## 和谁有关

**文档事实**：以下关系均由来源文档的正文、参数说明或回链证据支撑。

- [[conf]]：本页正文称允许的最大 level set 数由 `CONF, CONF?` 设定（默认 32、最大 256）；CONF 页也把 `LSUS` 列为受其上限约束的 set 数命令之一（回链证据）。
- [[dscp]]：本页参数与 `Errors` 把 `level_set_no` 的上限来源写作 `DSCP`（Define System Control Parameter）；同一页正文却写作 `CONF`，两处表述不一致。
- [[lsux]]：LSUX 文档称 Test Flow Optimizer 内部用 LSUX 生成额外（优化）level set，而 `LSUS?` 返回全部 level set 数（回链证据）。
- [[sprm]]：SPRM 文档称 level set 识别号的范围是 1 到 `LSUS` 决定的最大 level set 数（回链证据）。
- [[term]]：TERM 文档称 level set 编号不得超过 `DSCP` 允许的最大值以及 `LSUS` 定义的已用 level set 数（回链证据）。
- `FTST`（`02_System_reference/02.06_Command_Reference/02.06.02.02.127_FTST__-__Functional_TeST.htm`）：FTST 的报错条件称 Primary Level Set number 大于 `LSUS` 允许的范围会报错（回链证据）。
- `Level Setup Commands`（`02_System_reference/02.06_Command_Reference/02.06.05_Level_Setup_Commands.htm`）、`Delete a Fixed Level Set`（`02_System_reference/02.06_Command_Reference/02.06.05.01.05.02_Delete_a_Fixed_Level_Set.htm`）：本页 `Application` 与删除语义所依据的章节（回链证据）。

## 版本

**文档事实**：`Functional changes` 只记录 `Introduced before SmarTest 6.3.2`。这是哨兵值，表示文档集覆盖范围之前已有，不能当作 6.3.2 的变更；文档未记录更晚变更。

## 出处

- 主源：`02_System_reference/02.06_Command_Reference/02.06.02.02.155_LSUS__LSUS__-__Level_Sets_USed.htm`（正文、LSUS/LSUS?、Parameters、Application、Errors、Example、Functional changes）。
- 回链证据：`02_System_reference/02.06_Command_Reference/02.06.02.02_List_of_commands.htm`、`02.06.05.01.05.01_Create_a_fixed_level_set.htm`、`02.06.05.01.05.02_Delete_a_Fixed_Level_Set.htm`、`02.06.02.02.127_FTST__-__Functional_TeST.htm`、`02.06.02.02.156_LSUX__LSUX__-__Level_Sets_Used_eXtended.htm`、`02.06.02.02.228_SPRM__SPRM__-__Set_PRiMary_sets.htm`、`02.06.02.02.257_TERM__TERM__-__TERMination_mode.htm`、`02.06.02.02.31_CONF__CONF__-__CONFiguration.htm`、`02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.htm`。
