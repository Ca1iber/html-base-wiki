---
type: object
title: PQFC, PQFC? - (Parallel Query FoCus)
layer: L1
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.03.02.19_PQFC__PQFC__-__Parallel_Query_FoCus.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# PQFC, PQFC? - (Parallel Query FoCus)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **226 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.03.02.19_PQFC__PQFC__-__Parallel_Query_FoCus.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### PQFC

```
PQFC {site}
```

### PQFC?

```
PQFC?
```

### Parameters

[表]
行 1:
  site
  The site parameter is single integer representing the number of
    the site that has or shall have the query focus.

### Example

```
PQFC 2
```

This example sets the query focus to site
2.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.03.02.19_PQFC__PQFC__-__Parallel_Query_FoCus.htm>` 的 `## Warnings`、`## Errors` 段。**不是转述。**
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Warnings

PQFC
 returns a warning if the specified site
is not available. In such cases the query focus is not changed.

### Errors

An error is generated if not all pins at the site have had their
channels assigned by the
PALS
 command. \

<!-- 报错节 end -->

## 是什么

**文档事实** PQFC 定义哪个 site 拥有 query focus；该 site 是唯一可以检索 setup data 或显示结果的 site。

**文档事实** `PQFC?` 查询返回当前拥有 query focus 的 site。

**文档事实** 加载 pin configuration 后，query focus 被设为第一个可用 site，这可能不是 site 1；可用 site 由 `PSTE?` 应答中的 “1” 表示。

**文档事实** 源文给出 CAUTION：该命令实现 multisite testing 的 tpi 接口，应使用 tpi 调用而不是该 firmware 命令。

## 典型用法

**文档事实** `PQFC {site}` 设置 query focus，`PQFC?` 查询当前 focus；示例 `PQFC 2` 把 query focus 设为 site 2。

**文档事实** Application 段指明其应用位置为 Site Control window。

**文档事实** 若指定的 site 不可用，PQFC 返回 warning，且 query focus 不变。

**文档事实** 若该 site 的引脚尚未全部由 PALS 分配 channel，则产生 error。

**建议** 在依赖 query focus 读取 setup 或结果前，先确认目标 site 可用（`PSTE?` 应答为 “1”），并确保该 site 的引脚已由 PALS 分配。

## 和谁有关

- **文档事实** PSTE, PSTE? - (Parallel SiTe Enable)，源文称可用 site 由 `PSTE?` 应答中的 “1” 表示。
- **文档事实** PALS, PALS? - (Pin ALlocation for multiple Sites)，Errors 说明需由 PALS 为 site 的引脚分配 channel，否则报错。
- **文档事实** Site Control Window，源文 Application 段指明 PQFC 应用于该窗口。
- **文档事实** TPI Program Routines，源文 CAUTION 称该命令实现 tpi 接口，并建议改用 tpi 调用。
- **文档事实** Pin configuration file，源文称加载 pin configuration 后 query focus 被设为第一个可用 site。

## 版本

**文档事实** Functional changes 仅记载 Introduced before SmarTest 6.3.2。

## 出处

- `02_System_reference/02.06_Command_Reference/02.06.03.02.19_PQFC__PQFC__-__Parallel_Query_FoCus.htm`，主源，含 intro、PQFC、PQFC?、Parameters、Application、Warnings、Errors、Example 与 Functional changes。
