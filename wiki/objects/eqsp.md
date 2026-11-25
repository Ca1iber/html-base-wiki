---
type: object
title: EQSP, EQSP? - (EQuation SPecification transfer)
layer: L1
stage: timing
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.05.02.10_EQSP__EQSP__-__EQuation_SPecification_transfer.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# EQSP, EQSP? - (EQuation SPecification transfer)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,489 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.05.02.10_EQSP__EQSP__-__EQuation_SPecification_transfer.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### EQSP

```
EQSP {spec_type}, {part}, {#spec(data)}
```

### EQSP?

```
EQSP?{spec_type}, {part}
```

returns:

```
EQSP {spec_type}, {part}, {#spec(data)}
```

if
these are not empty, for backward compatibility.

[表] Parameters
行 1:
  spec_type
  The mandatory parameter defines which specification type to use.
    
    Use:
    
    LEV to specify levels
    
    TIM to specify timing
行 2:
  part
  The mandatory parameter defines which part of the specification type to use.
    
    Use:
    
    EQN to specify equations
    
    SPS to specify specs
    
    WVT to specify a wavetable
    
    part can only be set to WVT,
    EQN, or CLK if spec_type is set
    to TIM.
行 3:
  #spec(data)
  An equation based set of data (for example wavetables) in binary format.
    
    This parameter enables you to define the length of the data (in bytes) and the data
    itself to be transferred. It has the following format:
    
    A # to mark the start of the data block.
    
    One digit indicating how many digits make up the data length specifier.
    
    A number of digits indicating the length (in bytes) of the data to follow.
    
    A number of characters which make up the specified equation based testing file. This
    stream of characters must be terminated with a @ character.

### Example

The following example queries the current
wavetables:

```
> EQSP? TIM,WVT
< EQSP TIM,WVT,#9000000127WAVETBL table1 # derived from waveform set 1

PINS Pin1 Pin2
WFDS 0 "d1:D11"
1 0 . . .
2 1 . . .
BWDS ""

@
```

<!-- 语法节 end -->

## 是什么

**文档事实** EQSP 把 equation based 的 setup 数据集合（例如 wavetable 或 equation set）以二进制格式下载到 firmware；EQSP? 查询以二进制格式从 firmware 返回当前的对应数据集合。

**文档事实** spec_type 必填：LEV 表示 levels，TIM 表示 timing。part 必填：EQN 表示 equations，SPS 表示 specs，WVT 表示 wavetable；参数表另称 spec_type=TIM 时 part 只能为 WVT、EQN 或 CLK，但 CLK 并未出现在 part 的取值列表中。

**文档事实** 数据块 `#spec(data)` 的格式：`#` 标记数据块开始；一位数字给出「长度说明符」的位数；随后若干位数字给出数据长度（字节）；再后是 equation based 测试文件的内容，该字符流必须以 `@` 结尾。

**文档事实** Application：EQSP 用于 level 与 timing setup 文件；EQSP? 由 test program explorer 用来生成并保存 setup 文件。

**文档事实** 只有当数据非空时，EQSP? 才返回 `EQSP {spec_type}, {part}, {#spec(data)}`，这是为向后兼容。

## 典型用法

**文档事实** 查询当前 wavetable：`> EQSP? TIM,WVT` 返回 `EQSP TIM,WVT,#9000000127WAVTBL table1 # derived from waveform set 1 ... @`；返回内容是 wavetable 定义（`WAVTBL table1`、`PINS`、`WFDS`、`BWDS`），以 `@` 结束。

**文档事实** 该例的 `#9000000127WAVTBL...` 可按参数表拆为 `#` + 一位长度位数（`9`）+ 长度数字（`000000127`）+ 数据内容 + `@`。

**推断** 按上述格式，该例声明的数据内容长度为 127 字节。

**文档事实** 在 level equation 文件中可见用法：`EQSP LEV,EQN,#9000005436`，其后为 `EQNSET 1 "levels equation set"`、`SPECS`、`EQUATIONS` 等内容（Level equation file 页示例）。

**文档事实** 在 timing setup 文件中可见 `EQSP TIM,WVT,#9000015411`、`EQSP TIM,CLK,#9000000278`、`EQSP TIM,EQN,#9000011543`、`EQSP TIM,SPS,#9000006739` 等用法（Timing equation file、Wavetable file 页示例）。

**文档事实** Data organization of equation based timing 页称：equation based timing 的 equation set、wavetable、specification set 等数据集合由 EQFS 与 EQSP 命令下载。

**建议** 构造写入数据块时严格按 `#` + 长度位数 + 长度 + 内容 + `@` 的格式；需要读取 firmware 中的当前集合时用 EQSP?，并注意返回可能为空。

## 和谁有关

- **文档事实** `[[eqfs]]` — Fixed timing 页称 equation based 的 data collection 作为 EQSP 或 EQFS 的一个字符串参数下载到 tester；Data organization of equation based timing 页称这些数据集合由 EQFS 与 EQSP 下载。两者是同一 equation based 数据通道：EQSP 面向 firmware 的二进制集合传输，EQFS 面向编辑工具的临时文件 LOAD/SAVE（后者见 EQFS 主源）。
- **文档事实** `[[test-program-explorer]]` — EQSP 主源 Application 明说 EQSP? 被 test program explorer 用来生成并保存 setup 文件。
- **文档事实** `[[level-equation-file]]` — 该页示例用 `EQSP LEV,EQN,#9000005436` 引入 level equation set，属于 EQSP 的 level 侧实际用法。
- **文档事实** `[[wavetable-file]]` — 该页示例用 `EQSP TIM,WVT,#9000015411` 引入 wavetable，属于 EQSP 的 timing/wavetable 侧实际用法。
- **文档事实** `[[timing-specification]]` — Defining the timing specification 页称 specification 通常用 spec tool 定义；若要改用 EQFS 或 EQSP 下载，必须按 timing setup file 中的编码书写。
- **文档事实** `02_System_reference/02.06_Command_Reference/02.06.05.02_List_of_level_setup_commands.htm` — 该命令总表把 EQSP、EQSP? 列入 level setup commands（objpack 入边）。

## 版本

**文档事实** Functional changes 记：`Introduced before SmarTest 6.3.2`。

## 出处

- `02_System_reference/02.06_Command_Reference/02.06.05.02.10_EQSP__EQSP__-__EQuation_SPecification_transfer.htm`，主源，含首段、语法/参数、Application、Example 与 Functional changes，已用 `show.py` 与 `objpack.py` 读取。
- `02_System_reference/02.06_Command_Reference/02.06.06.01.02_Data_organization_of_equation_based_timing.htm`、`02.06.06.01.05_Defining_the_timing_specification.htm`、`02.07_Test_Method_Reference/02.07.11.01.05.01_Level_equation_file.htm`，用于核对 EQSP/EQFS 分工、spec tool 关系与 level 侧用法，已用 `show.py` 读取。
- `02.06.06.01.07_Fixed_timing.htm`、`02.07.11.01.05.02_Timing_equation_file.htm`、`02.07.11.01.05.03_Wavetable_file.htm`，用于核对“EQSP 或 EQFS”表述与 timing/wavetable 示例，取自 `extract/sections.jsonl` 摘录与 `objpack.py` 入边。
