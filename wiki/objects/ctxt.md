---
type: object
title: CTXT, CTXT? - (ConTeXT)
layer: L1
stage: level
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.35_CTXT__CTXT__-__ConTeXT.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# CTXT, CTXT? - (ConTeXT)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **576 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.35_CTXT__CTXT__-__ConTeXT.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### CTXT

```
CTXT {action},{"name"}
```

### CTXT?

```
CTXT?ALL
```

returns:

```
CTXT {DEFINE},{"name"}
```

### Parameters

[表]
行 1:
  action [跨 4 行]
  Specifies the action. Possible values [跨 2 列]
    are:
行 2:
  DEFINE
  Defines a new mode context
行 3:
  DELETE
  Deletes a mode context
行 4:
  ALL
  Displays all existing mode contexts (only in the query).
行 5:
  name
  The name of the mode context. If the [跨 2 列]
    action parameter is set to DELETE, you can also
    specify ALL to delete all mode contexts.

### Example

```
> CTXT? ALL
< CTXT DEFINE,"DEFAULT"
< CTXT DEFINE,"differential"
< CTXT DEFINE,"PdrvNPrcv"
```

<!-- 语法节 end -->

## 是什么

**文档事实**：`CTXT`（ConTeXT）定义或删除 mode context 的名称。mode context 为每个已配置的 pin 设定 type（`I`、`O` 或 `IO`）与 mode（`std` 或 `fast`）；单个 pin 的这些属性用 `CONF` 设置。

**文档事实**：`CTXT?` 返回当前已定义的 context 名称。

**文档事实**：新建 mode context 时，它作为当前 `DEFAULT` context 的副本创建；这份默认配置可用 `CONF` 修改。

**文档事实**：`action` 取 `DEFINE`（新建 mode context）、`DELETE`（删除 mode context）、`ALL`（只用于查询，显示所有已有 mode context）；`name` 为 mode context 名称。`action` 为 `DELETE` 时，`name` 也可写 `ALL` 以删除所有 mode context。

**文档事实**：查询的返回形式为 `CTXT {DEFINE},{"name"}`。

## 典型用法

**文档事实**：列出当前所有 mode context：

```
> CTXT? ALL
< CTXT DEFINE,"DEFAULT"
< CTXT DEFINE,"differential"
< CTXT DEFINE,"PdrvNPrcv"
```

**文档事实**：按语法模板 `CTXT {action},{"name"}`，定义用 `DEFINE`、删除用 `DELETE`，名称为带引号的字符串；`DELETE` 时名称可写 `ALL` 删除全部。

**文档事实**：源文的查询语法块写作 `CTXT?ALL`（无空格），示例写作 `CTXT? ALL`（有空格），两种写法都出现在同一页。

**文档事实**：因为新 context 是 `DEFAULT` 的副本，典型流程是先 `CTXT DEFINE` 建 context，再用 `CONF` 在该 context 下逐 pin 设置 type/mode。

## 和谁有关

**文档事实**：以下关系都有源文正文、参数说明或入边支撑；每条注明为什么相关。

- [[conf]]：本页正文要求用 `CONF` 定义每个 pin 的 type/mode；`CONF` 的参数说明反过来写“其他 mode context 必须用 `CTXT` 定义”，并说明 `context` 省略时使用预定义 `DEFAULT`。为什么：两页双向写明。
- `Pin configuration setup commands`（`02_System_reference/02.06_Command_Reference/02.06.03_Pin_configuration_setup_commands.htm`）与同章 `Introduction`（`02.06.03.01.01_Introduction.htm`）：都把 `CTXT`、`CONF` 归在 “Commands for mode contexts” 之下。
- `List of commands`（`02_System_reference/02.06_Command_Reference/02.06.02.02_List_of_commands.htm`）：把本页列入命令总表。
- `Disabling a pin configuration license lock`（`02_System_reference/02.04_Model_File_and_Licensing/02.04.05.08.02_Disabling_a_pin_configuration_license_lock.htm`）：该文说 `*RST`、`UDEF` 等命令会禁用 setup 相关固件命令，之后重新启用 `CONF`、`CTXT` 等 pin configuration 相关命令；本页在该文的 Related information 中。为什么：`CTXT` 属 pin configuration 相关命令。

## 版本

**文档事实**：`Functional changes` 只有 `Introduced before SmarTest 6.3.2`，没有其他版本记录。

**推断**：这一写法是文档集的哨兵，表示该内容在 6.3.2 之前已存在，不能当作 6.3.2 引入。

## 出处

- 主源：`02_System_reference/02.06_Command_Reference/02.06.02.02.35_CTXT__CTXT__-__ConTeXT.htm`（正文、Mode of operation、Parameters、Example、Functional changes）。
- 关系证据：`extract/objpack.py` 的入边（`02.06.02.02_List_of_commands`、`02.06.03_Pin_configuration_setup_commands`、`02.06.03.01.01_Introduction`、`02.04.05.08.02_Disabling_a_pin_configuration_license_lock`）；`CONF` 页的参数说明。
