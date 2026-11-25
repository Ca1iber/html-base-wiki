---
type: object
title: UDUP - (UnDefine Utility Purpose)
layer: L1
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.301_UDUP_-__UnDefine_Utility_Purpose.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# UDUP - (UnDefine Utility Purpose)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **346 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.301_UDUP_-__UnDefine_Utility_Purpose.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
UDUP {(purpose_name)}
```

### Parameters

[表]
行 1:
  purpose_name
  Specifies the utility purpose name or names to be undefined.
    
    The symbol @ removes all utility purpose definitions.
    
    If more than one name is to be removed, the names must be
    separated by a comma.

### Example

```
UDUP (@)
```

This command undefines all defined utility purpose
names.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.301_UDUP_-__UnDefine_Utility_Purpose.htm>` 的 `## Errors` 段。**不是转述。**
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if the referenced utility purpose has not
been defined before.

<!-- 报错节 end -->

## 是什么

**文档事实** UDUP（UnDefine Utility Purpose）从 configuration 中删除一个或多个已定义的 utility purpose 名。

**文档事实** utility purpose 是由名字与每个成员的标准输出（期望）状态标识的一组 utility lines，用 DFUP 创建；这种构造允许用一条语句控制多条 utility line（`Defining a utility purpose`）。

**文档事实** `purpose_name` 写 `@` 会删除所有 utility purpose 定义；要删除多个名字时以逗号分隔。

**文档事实** 若引用的 utility purpose 此前未定义，命令报错。

**文档事实** 主源只说明删除定义，未描述对 utility line 当前输出状态的即时影响。

**推断** 因此 UDUP 撤销的是「名字 → utility line 组与标准状态」的配置；要改变或激活输出状态，应走 DFUP/UPST/FLSH 这条路径。

## 典型用法

**文档事实** `UDUP (@)` 删除所有已定义的 utility purpose 名。

**文档事实** 删除单个或多个：按语法 `UDUP {(purpose_name)}` 在括号内给出名字，多个名字用逗号分隔。

**文档事实** 删除前可用 `DFUP?` 查询 utility purpose 的定义（DFUP 页）。

**文档事实** 若要把某个 utility purpose 的标准状态真正输出，需先用 UPST 选择要激活的状态，再用 FLSH 下载；UDUP 删除的是该定义本身。

**文档事实** 引用的名字未定义过会报错（见本页报错节）。

**建议** 用 `UDUP (@)` 批量清理前先确认没有其他测试段仍引用这些 purpose；只删个别名字时用逗号列出，避免误删。

## 和谁有关

- **文档事实** DFUP, DFUP?：utility purpose 由 DFUP 创建，DFUP? 返回其定义；`Defining a utility purpose` 明确 UDUP 用于移除 utility purpose。
- **文档事实** UPST 与 FLSH：DFUP 设定的标准状态需先用 UPST 选为待激活值、再用 FLSH 下载。
- **文档事实** UPTI：为被激活的 utility purpose 设定用作等待时间的 settling time（`Defining a utility purpose`）。
- **文档事实** UPAS：为 site > 1 控制 utility purpose 的标准状态，可为不同 site 定义不同状态；其前提是已用 DFUP 定义。
- **文档事实** DFUT 与 UDUT：`Pin configuration setup commands` 的 “Commands for utility lines” 把 DFUT、UDUT、DFUP、UPAS、UDUP 列为一族。
- **文档事实** List of commands 与 List of configuration commands：UDUP 分别列在命令总表与配置命令表中（入边）。
- **文档事实** Disabling a pin configuration license lock：该页在命令列表中引用 UDUP（入边）。
- **文档事实** Configuration Setup Commands：主源 Application 指向该组命令以了解 utility purposes 的细节。

## 版本

**文档事实** Functional changes 记：Introduced before SmarTest 6.3.2。

## 出处

- `02_System_reference/02.06_Command_Reference/02.06.02.02.301_UDUP_-__UnDefine_Utility_Purpose.htm`，主源，含概览、Syntax、Parameters、Application、Errors、Example 与 Functional changes，已用 `show.py` 读取。
- `02_System_reference/02.06_Command_Reference/02.06.02.02.69_DFUP__DFUP__-__DeFine_Utility_Purpose.htm`、`02.06.03.01.08_Defining_a_utility_purpose.htm`、`02.06.02.02.305_UPST__UPST__-__Utility_Purpose_STate.htm`、`02.06.02.02.302_UDUT_-__UnDefine_UTility_line.htm`、`02.06.03_Pin_configuration_setup_commands.htm`，用于 utility purpose 语义与命令族关系，已用 `show.py` 读取。
- 入边与引用语境取自 `extract/objpack.py` / `edges.jsonl`。
