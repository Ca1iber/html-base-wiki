---
type: object
title: UDUT - (UnDefine UTility line)
layer: L1
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.302_UDUT_-__UnDefine_UTility_line.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# UDUT - (UnDefine UTility line)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **331 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.302_UDUT_-__UnDefine_UTility_line.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
UDUT {(util_name)}
```

### Parameters

[表]
行 1:
  util_name
  Specifies the utility line name or names to be undefined.
    
    The symbol @ removes all utility line definitions.
    
    If more than one name is to be removed, the names must be
    separated by a comma.

### Example

```
UDUT (@)
```

This command undefines all defined utility line
names.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.302_UDUT_-__UnDefine_UTility_line.htm>` 的 `## Errors` 段。**不是转述。**
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if the referenced utility line has not been
defined before.

<!-- 报错节 end -->

## 是什么

**文档事实** UDUT（UnDefine UTility line）从当前配置中删除已定义的 utility line 名称；删除后，write utility line 的输出状态置为 0（low output）。

**文档事实** 参数 `util_name` 可给一个或多个名称，多个名称用逗号分隔；符号 `@` 删除全部 utility line 定义。

**文档事实** 文档的 Application 段只把 utility line 的细节指向 Configuration Setup Commands（02.06.03）。

## 典型用法

**文档事实** 语法为 `UDUT {(util_name)}`。示例 `UDUT (@)` 删除全部已定义的 utility line 名称。

**文档事实** 若引用的 utility line 此前未定义，命令报错。

**推断** 单条 utility line 的撤销应写成 `UDUT (name)`（与 `@` 同一参数位）；文档只给出 `@` 的示例，未演示单个名称写法。

## 和谁有关

- **文档事实** `[[dfut]]` — Configuration Setup Commands 把 utility line 命令组列为 DFUT、UDUT、DFUP、UPAS、UDUP；Defining a utility line 页说明 DFUT 给 utility line channel 关联 pin name 与 operation mode，而 “The UDUT command removes a utility line.”
- **文档事实** `[[dfup]]`、`[[upas]]`、`[[udup]]` — 与 UDUT 同属 utility line / utility purpose 命令组（Pin configuration setup commands 与 Introduction 均列出 DFUT、UDUT、DFUP、UPAS、UDUP）。
- **文档事实** `[[pin-configuration-file]]` — `02.04.05.08.02 Disabling a pin configuration license lock` 把 UDUT 与 *RST、UDEF、UDPS、UDUP 等并列为会使 device-specific license signature 失效、并禁用 setup 相关命令（VECC、VECD、SQLB、DMAS）的命令；之后需重新加载 pin configuration 才恢复。
- **推断** UDUT 删除的是 utility line 的定义，而 UTST 设置已命名 utility line 的输出状态、DFUP 定义 utility purpose；文档没有给出三者组合的完整流程。

## 版本

**文档事实** Functional changes 记载 “Introduced before SmarTest 6.3.2”。

## 出处

- `02_System_reference/02.06_Command_Reference/02.06.02.02.302_UDUT_-__UnDefine_UTility_line.htm`，主源，含用途、参数、Application、Errors、示例与 Functional changes。
- `02_System_reference/02.06_Command_Reference/02.06.03.01.05_Defining_a_utility_line.htm`，用于确认 UDUT 与 DFUT/UTST/DFUP 的关系及 utility line 编号背景。
- `02_System_reference/02.04_Model_File_and_Licensing/02.04.05.08.02_Disabling_a_pin_configuration_license_lock.htm`，用于确认 license lock 影响。
