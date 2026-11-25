---
type: object
title: BWDS, BWDS? - (Break Waveform Definition String)
layer: L1
stage: timing
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.14_BWDS__BWDS__-__Break_Waveform_Definition_String.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# BWDS, BWDS? - (Break Waveform Definition String)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **2,050 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.14_BWDS__BWDS__-__Break_Waveform_Definition_String.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### BWDS

```
BWDS {wvf_set}, [break_waveform_index], [mode], {definition_string}, {(pinlist)}
```

### BWDS?

```
BWDS? {wvf_set|"wavetable_name"|specset_id|"multi-port_spec"}, [break_waveform_index], [mode], {(pinlist)}
```

returns:

```
BWDS {wvf_set|"wavetable_name"|specset_id|"multi-port_spec"}, [break_waveform_index], [mode], {definition_string}, {(pinlist)}
```
[表] Parameters
行 1:
  wvf_set
  Waveform Set Number (range 1 to maximum). Enter ALL for all
    waveform sets. Enter PRM for the Primary waveform set. The maximum
    number is determined by the command `WSUS, WSUS? - (Waveform Sets USed)`（raw: `98878.htm`）.
行 2:
  wavetable_name
  The wavetable name. Enter a string of up to 40 alphanumeric characters (upper or
    lower case) enclosed in double quotes. wavetable_name can only be
    specified in the query.
行 3:
  specset_id
  Derived as follows:
    
    100 * equation_set_no + specset_no
    
    specset_id can only be specified in the query.
行 4:
  multi-port_spec
  To query a multi-port specification, enter the name of the specification.
行 5:
  break_waveform_index
  Enter DEF for the default break waveform or an integer in the
    range 0 to 3. This parameter is optional in release 2.0 and can only be used to select the
    default break waveform (DEF).
行 6:
  mode
  NOT USED.
行 7:
  definition_string
  The definition string consists of a sequence of items each of which associates a drive action
    with a drive edge.
    
    Receive edge are always denoted by rn.
    
    All edges which are not explicitly specified are set to N. In the
    query only those edges that are used are printed.
    
    For details of the syntax see `WFDS, WFDS? - (WaveForm Definition String)`（raw: `98872.htm`）.
行 8:
  pinlist
  The name of the pin or pins for which break waveform definitions are to be made or
    read back. The symbol @ can be used to specify all configured input and
    IO pins. If more than one pin is to be included, the names must be separated with a comma.

### Example

```
> BWDS? 1,,,(@)
< BWDS 1,,,"",(io)
< BWDS 1,,,"d1:F00 d5:F10",(clk)
```

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.14_BWDS__BWDS__-__Break_Waveform_Definition_String.htm>` 的 `## Errors` 段。**不是转述。**
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

waveform_set
 is greater than the range allowed by the command
`WSUS, WSUS? - (Waveform Sets USed)`（raw: `98878.htm`）
.

There is a mismatch between the edge actions and edge order in the specified waveform.

A tri-state action is defined or implicitly required on edge 2 or 5 (only for P/C/Ce
systems).

<!-- 报错节 end -->

## 是什么

**文档事实** BWDS（Break Waveform Definition String）定义指定 waveform set 的 break waveform 动作；`BWDS?` 查询返回指定 pins 当前 break waveform 的定义。

**文档事实** Mode of operation：只允许 drive actions；break waveform 不得包含 data dependent actions；与所定义动作不相容的 edge delays 会被自动修正以适配；BWDS 命令只能用于 fixed timing，而查询也可用于 equation based timing。

**文档事实** 该命令取代 BWDF / BWDF?，用于 14 个及以上 edge 的 setup。

**文档事实** `wvf_set` 取 1 到最大值，或 `ALL`（所有 waveform set）、`PRM`（Primary waveform set）；最大值由 `WSUS` 决定。`wavetable_name`、`specset_id`、`multi-port_spec` 只能在 query 中使用；`specset_id = 100 * equation_set_no + specset_no`。

**文档事实** `break_waveform_index` 取 `DEF`（默认 break waveform）或 0 到 3 的整数；文档注明该参数在 release 2.0 中可选，且只能用于选择默认 break waveform（`DEF`）。`mode` 为 `NOT USED`。

**文档事实** `definition_string` 由一组“drive action 对应 drive edge”的项组成；未显式指定的 edge 置为 `N`；receive edge 总以 `rn` 表示；语法细节见 `WFDS`。`pinlist` 可用 `@` 表示所有已配置的 input 与 IO pins。

**文档事实** Application 段把该命令归入 Timing setup（见 Timing Setup Commands）。

## 典型用法

**文档事实** 查询 waveform set 1 上所有已配置 input/IO pins 的 break waveform 定义：

```
> BWDS? 1,,,(@)
< BWDS 1,,,"",(io)
< BWDS 1,,,"d1:F00 d5:F10",(clk)
```

**文档事实** 结果中 `io` 的定义为空字符串；`clk` 的定义为 `"d1:F00 d5:F10"`；查询只打印用到的 edge。

**文档事实** 因 definition string 的语法与 WFDS 相同，可参照 WFDS 的语法书写各 edge 的 drive action。

**推断** 该命令用于 fixed timing 下的 break waveform 定义；若要用于 equation based timing，只能使用查询形式。

## 和谁有关

- [[bwdf]]：**文档事实** BWDF 页说明从 release 2.1 起，在 14-edge setup 下由 BWDS/BWDS? 取代；本页也说 BWDS replaces BWDF for setups with 14 or more edges。为什么：BWDF 是 BWDS 的前身与替代关系。
- [[wsus]]：**文档事实** `wvf_set` 的最大值由 WSUS 决定，Errors 也点名 WSUS 范围。为什么：WSUS 决定 waveform set 数量上限。
- [[wfds]]：**文档事实** `definition_string` 的语法细节见 WFDS。为什么：两者共用 edge drive action 的定义语法。
- [[etds]]：**文档事实** 入边显示 ETDS 的错误说明把 break waveform definition（BWDS/BWDS?）列为与 timing set edge delays 不匹配时的相关定义。为什么：break waveform 与 edge timing 需一致。
- EUDS（`02_System_reference/02.06_Command_Reference/02.06.02.02.119_EUDS__-__Edge_Usage_Definition_String.htm`）：**文档事实** EUDS 说 edge directions 用 WFDS 或 BWDS 设置。为什么：BWDS 参与 edge direction 的设定。
- Timing Setup Commands（`02_System_reference/02.06_Command_Reference/02.06.06_Timing_Setup_Commands.htm`）：**文档事实** 本页 Application 指向该章。为什么：该章是 BWDS 所属的 timing 配置命令族。

## 版本

**文档事实** Functional changes 记：Introduced before SmarTest 6.3.2。

**文档事实** 参数说明提到 `break_waveform_index` 在 release 2.0 中可选；BWDF 页的入边说从 release 2.1 起由 BWDS 取代。

**推断** 这些 release 记录与 Functional changes 的 6.3.2 标记属于不同的版本表述，不能直接换算为 SmarTest 版本。

## 出处

- `02_System_reference/02.06_Command_Reference/02.06.02.02.14_BWDS__BWDS__-__Break_Waveform_Definition_String.htm`，主源，含概览、Mode of operation、Syntax、Parameters、Application、Errors、Example 与 Functional changes，已用 `show.py 02.06.02.02.14` 读取。
- 关系与入边取自 `extract/objpack.py`（`edges.jsonl`）：BWDF、WSUS、WFDS、ETDS、EUDS、List of commands 等。
