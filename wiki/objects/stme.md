---
type: object
title: STME, STME? - (SiTe Match Enable)
layer: L1
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.250_STME__STME__-__SiTe_Match_Enable.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# STME, STME? - (SiTe Match Enable)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,107 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.250_STME__STME__-__SiTe_Match_Enable.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### STME

```
STME {ON|OFF|AUTO|FAST},
```

### STME?

```
STME?
```

returns:

STME

{
ON
|
OFF
|
FAST
),

### Parameters

[表]
行 1:
  ON
  Turns the site match function on.
行 2:
  OFF
  Turns the site match function off.
行 3:
  AUTO
  Starting the sites successively affects the test negatively if the pin
    configuration contains at least one shared digital channel for triggering an analog module.
    The AUTO option checks if such a shared channel exists. If it does, the
    match site function is set to OFF; if not, it is set to
    ON. AUTO is the default.
行 4:
  FAST
  Activates the `Fast Sync`（raw: `150814.htm`） feature (local synchronization) of the test
    processor. After setting this option," STME ON" is required to turn on
    the site match function.

### Example

```
> STME AUTO,
> STME?
< STME ON,
```

This example sets the
site match function to
AUTO
, then reads the actual setting. Since the actual
setting is
ON
, the pin configuration cannot contain a shared digital
channel.

```
>SQST OFF
>NIFE 2
>STME FAST,
>STME ON,
```

This example configures the Fast Sync feature, and sets two independent Fast Sync ports
on each test processor.

<!-- 语法节 end -->

## 是什么

**文档事实** STME 定义 site match function（site 匹配功能）的状态。该功能决定所有 site 是同时启动（`OFF`）还是带轻微延迟依次启动（`ON`）；只配置一个 site 时命令不产生效果。

**文档事实** `ON` 是多 site 测试中按 site 独立评估 match loop 所必需的：若所有 site 同时启动，是否 match 的判定会基于所有 site 的 compare 结果。

**文档事实** `OFF` 在「一个数字通道被多个 site 共享、用于触发共享的模拟模块」时是必需的。

**文档事实** `FAST` 在 match loop 与条件跳转启用测试处理器的本地同步（local synchronization，即 Fast Sync）时是必需的；设置该选项后还必须发 `STME ON` 才真正打开 site match 功能。

**文档事实** `AUTO` 会检查 pin 配置中是否存在上述共享数字通道：存在则把 site match 置为 `OFF`，不存在则置为 `ON`；`AUTO` 是默认值。

**文档事实** `STME?` 返回当前生效的设置；文档列出的返回集合为 `ON|OFF|FAST`（不含 `AUTO`）。

**文档事实** 文档把 ON/OFF 的选择归纳为两种场景：pattern 含 match loop 时要求 ON；同一通道被不同 site 的同名 pin 共享时要求 OFF。若同一 setup 中两种构造都存在，无法取得最优选择；跨 site 共享 BADC 时必须关闭 site matching，以保证由 pattern 控制的 DC 测量正确。

**文档事实** site match 也可由 Site Match test suite flag 控制；用例文档把该功能描述为由 suite flags 或 STME 固件命令激活。

## 典型用法

**文档事实** `STME AUTO,` 后跟 `STME?`，文档示例读回 `STME ON,`；由于实际设置为 ON，可判断 pin 配置中不含共享数字通道。

**文档事实** Fast Sync 的组合用法：先 `SQST OFF` 停止 sequencer，再 `NIFE 2`，然后 `STME FAST,` 与 `STME ON,`；文档说明这配置了 Fast Sync 功能，并在每个 test processor 上设置两个独立的 Fast Sync port。

**文档事实** `FAST` 本身只激活 Fast Sync，不打开 site match；要打开仍需 `STME ON`。

**建议** 明知配置含共享数字通道（共享模拟模块触发）时显式写 `STME OFF`，明知含 match loop 时显式写 `STME ON`，比依赖 `AUTO` 的自动判别更易审查；`AUTO` 适合作为默认起点。

## 和谁有关

- **文档事实** Fast Sync（`02.06.07.01.08.04.03.03`）与 How to use Fast Sync（`02.06.07.01.08.04.03.03.01`）—— `FAST` 选项激活 Fast Sync；how-to 明写「在 test method 中使用 STME FAST 固件命令启用 Fast Sync 功能」。
- **文档事实** NIFE —— 示例用 `NIFE 2` 设置每个 test processor 上独立 Fast Sync port 的数量。
- **文档事实** SQSL —— 其文档写明「同一 pin 在不同 site 上的同步或异步启动由 site match function 控制，详见 STME」。
- **文档事实** SQST —— 示例先 `SQST OFF` 停止 sequencer，再配置 FAST 设置。
- **文档事实** [[match-loops]] —— `ON` 是按 site 独立评估 match loop 的前提，STME 正文直接指向该页。
- **文档事实** Controlling the site match function（`02.06.03.01.10.04`）—— 说明 site match 由 Site Match test suite flag 控制，给出 ON/OFF 的选择场景、BADC 警告，以及 multiport 下用 sequencing group 产生同样的启动偏移。
- **文档事实** PSTE、PALS、PACT、PQFC、PSFC —— `02.06.03` 的多 site 设置命令族把 STME 与它们并列。
- **文档事实** 用例 `03.08`（multiport EPRC match loop）—— 说明 site match 是可选功能、每个 site 独立；没有 site match 时所有 site 一起移动。
- **建议** 在本 wiki 内先用 [[pste]] 确认参与测试的 site 集合，再决定 [[stme]] 的 ON/OFF；两者共同决定多 site 的并行行为。

## 版本

**文档事实** Functional changes：Introduced before SmarTest 6.3.2；SmarTest 7.4.0 新增 `FAST` 选项。

## 出处

- `02_System_reference/02.06_Command_Reference/02.06.02.02.250_STME__STME__-__SiTe_Match_Enable.htm` —— 主源：正文、Parameters、Example、Related information、Functional changes。
- `02_System_reference/02.06_Command_Reference/02.06.03.01.10.04_Controlling_the_site_match_function.htm` —— 读了 test suite flag、ON/OFF 场景与 BADC 警告。
- 其余跨页条目（Fast Sync、NIFE、SQSL、SQST、match loops、命令族、03.08 用例）取自各页被 STME 引用的语境句，未整篇通读。
