---
type: object
title: PSAS? - (Power Supply Accumulated Status)
layer: L1
stage: results
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.10.02.11_PSAS__-__Power_Supply_Accumulated_Status.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# PSAS? - (Power Supply Accumulated Status)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **4,315 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.10.02.11_PSAS__-__Power_Supply_Accumulated_Status.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
PSAS? [msMode ,] {mask}, {(pinlist)}
```

returns

```
PSAS {status}, {(pinlist)}
```

[表] Parameters
行 1:
  msMode
  The extra parameter controls how the return value is
    created.
    The value of the parameter can be
    PQFC:
    
    PQFC specified: The current query focus
    is respected and allows status query per site without
    affecting status bits of other sites.
    
    PQFC not specified: The command reads
    (and clears) status bits of all enabled and active sites at
    a glance, ignoring the actual query focus.
    
    The parameter applies only to use of parameter
    mask as integer value.
行 2:
  mask
  Integer bit mask or ALL.
    
    Integer bit mask: Integer value is used to mask out individual status bits. Each bit of mask is logically
    AND-ed with the corresponding bit of the DPS status. If one of the resulting bits is set, then
    F (Fail) is returned, otherwise P (Pass).
    
    It is used to check for an error condition. All bit positions of the status flags that should be checked,
    must be set to 1 in mask. If one of the selected status bits is set, then PSAS? returns
    F.
    
    ALL: Hex value (hexadecimal representation of all status bits) is returned.
    
    For setting the integer bit mask or interpreting a returned hex value, refer to the `status`（raw: `98691.htm#_98691__r_status`） parameter below.
行 3:
  pinlist
  Comma separated list of DPS128/64 or XPS256
    pins. The @ character can be used to read the status for all DPS
    pins.
行 4:
  status
  If parameter mask is
    ALL, you need to translate the hex value
    (hexadecimal representation of the status bits) to its binary form
    as follows:
    
      [子表]
      子行 1:
        Bit 0 (LSB):
        Constant voltage [跨 2 列]
      子行 2:
        Bit 1:
        Constant current [跨 2 列]
      子行 3:
        Bit 2:
        Unregulated [跨 2 列]
      子行 4:
        Bit 3:
        Overvoltage [跨 2 列]
      子行 5:
        Bit 4:
        Overpower / Overcurrent / Power [跨 2 列]
          budget exceeded
      子行 6:
        Bit 5:
        Overtemperature [跨 2 列]
      子行 7:
        Bit 6:
        Voltage drop force [跨 2 列]
      子行 8:
        Bit 7:
        Voltage drop return [跨 2 列]
      子行 9:
        Bit 8:
        DUT board disconnect
        For the special mapping of bit [跨 2 行]
          9 and 8 on UHC4 and UHC4T, refer to table `DPS flag description`（raw: `98691.htm#_98691__s_DPS_flag_description`）
          below.
      子行 10:
        Bit 9:
        Safety line
      子行 11:
        Bit 10:
        Current limit [跨 2 列]
          disconnect
      子行 12:
        Bit 11:
        Low headroom [跨 2 列]
      子行 13:
        Bit 12:
        Current limiter protection [跨 2 列]
          detected
      子行 14:
        Bit 13:
        Range overflow [跨 2 列]
      子行 15:
        Bit 14 (MSB):
        Clamp distance too [跨 2 列]
          low
      子行 16:
        Bit 15:
        Voltage drop force [跨 2 列]
          warning
      子行 17:
        Bit 16:
        Voltage drop return [跨 2 列]
          warning
    
    If parameter mask is specified as an integer
    bit-mask:
    
    Pass: P
    
    Fail: F
    
    Refer to table `DPS flag implementation`（raw: `98691.htm#_98691__s_DPS_flag_implementation_710`） below for information regarding the
    card specific implementation of the bits or flags.

### Examples

### Description

For the following examples (1 to 4), the assumed binary value of the status of the
UHC4 pin Vcc is 10000110 (Voltage drop return, Unregulated, Constant Current).

### Example 1

To get all flags:

```
PSAS? ALL,(Vcc)
```

returns

```
PSAS #86,(Vcc)
```

### Example 2

To check if Unregulated (bit 2) is set:

```
PSAS? 4,(Vcc)
```

returns

```
PSAS F,(Vcc)
```

### Example 3

To check if Constant Current (bit 1) or Overpower (bit 4) is set:

```
PSAS? 18,(Vcc)
```

returns

```
PSAS F,(Vcc)
```

### Example 4

To check if Voltage Drop Force (bit 6) or DUT Board Disconnect (bit 8) is set:

```
PSAS? 320,(Vcc)
```

returns

```
PSAS P,(Vcc)
```

### Example 5

```
PSAS? ALL,(Vee)
```

returns

```
PSAS 2,(Vee)
```

This example for device pin Vee shows the DPS is working in constant current mode.

### Example 6

```
PSAS? ALL,(Vee)
```

returns

```
PSAS 64,(Vee)
```

This example for device pin Vee shows the DPS has hit the voltage drop force
threshold.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.10.02.11_PSAS__-__Power_Supply_Accumulated_Status.htm>` 的 `## Errors` 段。**不是转述。**
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if a communication error with the DPS occurs.

The status bits 4 to 11 result in a disconnect of the pin. To reconnect you must
execute a disconnect-connect sequence.

<!-- 报错节 end -->

## 是什么

**文档事实**：PSAS?（Power Supply Accumulated Status）读取并清除 DPS 内部状态标志，适用于 DPS operating mode、PMU operating mode 与 Digital I/O operating mode。返回两类结果：`mask` 为 `ALL` 时返回状态位的十六进制表示（如 `#86`）；`mask` 为整数位掩码时，把 mask 与 DPS 状态逐位 AND，只要有任一被选中的位为 1 就返回 `F`，否则返回 `P`。

**文档事实**：结果只显示自上次执行 PSAS?（或上次 connect/disconnect 序列）以来被置位的位。所有 DPS 状态标志在 connect（`PSST ON`）和 disconnect（`PSST OFF`）时复位为 0，但只有触发条件不再成立时才真正复位；若查询/连接/断开时条件仍为真，标志不复位。不同 DPS 卡的复位行为不同，见 `DPS flag reset` 表。

**文档事实**：`msMode` 的 `PQFC` 只对整数 `mask` 生效：指定 PQFC 时尊重当前 query focus，可按 site 查询且不影响其它 site 的状态位；不指定时一次读取并清除所有 enabled/active site 的状态位，忽略 query focus。命令一次只聚焦一个 site，结果在 Testflow Editor 与 result tools 中按该 site 显示；firmware 查询也只报告当前 focus site 的 setup 与结果。

**文档事实**：`pinlist` 是 DPS128/64 或 XPS256 的 pin 列表，`@` 可读所有 DPS pin。`status` 的位定义：bit0 Constant voltage、bit1 Constant current、bit2 Unregulated、bit3 Overvoltage、bit4 Overpower/Overcurrent/Power budget exceeded、bit5 Overtemperature、bit6 Voltage drop force、bit7 Voltage drop return、bit8 DUT board disconnect、bit9 Safety line、bit10 Current limit disconnect、bit11 Low headroom、bit12 Current limiter protection detected、bit13 Range overflow、bit14 Clamp distance too low、bit15 Voltage drop force warning、bit16 Voltage drop return warning。bit9/bit8 在 UHC4 与 UHC4T 上有特殊映射（见 `DPS flag description`）。

**文档事实**：status bits 4–11 会导致 pin 断开；要重新连接必须执行一次 disconnect-connect 序列。

**文档事实**：`PRLT` 取得的 pass/fail 结果会被 `CSAS` 与 `PSAS` 作废；对应 API 上，`GET_FUNCTIONAL_RESULT()` 必须先于任何 `DPS_AUX_PIN_TASK.check...()` 调用，否则结果无效。

## 典型用法

**文档事实**：取全部状态：`PSAS? ALL,(Vcc)` 返回 `PSAS #86,(Vcc)`（示例假设 UHC4 pin Vcc 的状态二进制为 10000110，即 Voltage drop return、Unregulated、Constant Current）。按位检查用整数掩码：`PSAS? 4,(Vcc)` 查 bit2（Unregulated），`PSAS? 18,(Vcc)` 查 bit1（Constant Current）或 bit4（Overpower），`PSAS? 320,(Vcc)` 查 bit6（Voltage Drop Force）或 bit8（DUT Board Disconnect）；返回 `F` 或 `P`。

**文档事实**：按十六进制读时：`PSAS? ALL,(Vee)` 返回 `PSAS 2,(Vee)` 表示 DPS 工作在恒流模式；返回 `PSAS 64,(Vee)` 表示达到 voltage drop force 阈值。

**文档事实**：多 site 下要按当前 focus 查询时加 `PQFC`：`PSAS? PQFC, <mask>, (<pinlist>)`；该参数只对整数 mask 有效。

**文档事实**（顺序要求）：`PRLT` 的 pass/fail 结果会被 `CSAS` 与 `PSAS` 作废，因此文档建议在相关 functional test 之后、`CSAS`/`PSAS` 之前直接使用 `PRLT`；同一条规则适用于 API：`GET_FUNCTIONAL_RESULT()` 要先于 `DPS_AUX_PIN_TASK.check...()`。

**建议**：查询前先确定要查的是"全量 hex"还是"指定错误位"：前者用 `ALL` 并自行按位解释，后者用整数 mask 直接拿 `P/F`；两种返回的形状不同，混用会把 hex 当 pass/fail 读。

## 和谁有关

- `PSST`（`PSST ON` / `PSST OFF`）：**文档事实**——PSAS? 正文说 connect 与 disconnect 会把所有 DPS 状态标志复位为 0，并直接链接 `PSST`；复位是否生效取决于触发条件是否仍成立。
- `PRLT` / `GET_FUNCTIONAL_RESULT()`：**文档事实**——PSAS? 正文明确 `PRLT` 的 pass/fail 结果会被 `CSAS` 与 `PSAS` 作废，并推荐先取 `PRLT`；API 侧同样要求 `GET_FUNCTIONAL_RESULT()` 先于 `DPS_AUX_PIN_TASK.check...()`。
- `CSAS? - (Channel Slot Accumulated Status)`：**文档事实**——本页 Related information 列出 CSAS?；正文把它与 PSAS 并列为会作废 `PRLT` 结果的命令。
- `DPS_AUX_PIN_TASK.checkPowerFlags()`、`DPS power flags - get...() functions`、`XPS256 status flags`：**文档事实**——三者都出现在本页 Related information 中。**推断**：它们是同一组 DPS 状态位的程序侧读取入口，PSAS? 是命令侧入口；文档只写"see also"，没有声明二者等价。
- `DPS flag description` / `DPS flag implementation` / `DPS flag reset` 表：**文档事实**——`mask` 与 `status` 参数说明直接让读者参考这三张表来设置位掩码、解释 hex 以及了解各卡的实现与复位差异；这些表位于同主题的另一份投放（topic `98691.htm`，即 `02.06.02.02.188`）。
- DC Measurement Commands（`02.06.10`）：**文档事实**——本页 Application 写 "DC Tests, see DC Measurement Commands"，其所属的命令列表页把 PSAS? 列为 DC measurement 命令之一。

## 版本

**文档事实**：Functional changes 记录：Introduced before SmarTest 6.3.2（哨兵值，表示在文档集覆盖起点之前已存在，不是 6.3.2 的变更）；SmarTest 7.3.1 起支持 SIG（PMU）模式的 pin，并新增 "Low Headroom" 位；7.3.2 新增 DC Scale UHC4T 卡；7.3.3 新增 `msMode` 参数；7.4.0 新增 DC Scale AVI64 卡与 DPS 的 Digital I/O operating mode，并新增 Range overflow（bit13）与 Clamp distance too low（bit14）；7.5.0 新增 DC Scale FVI16 卡。

**文档事实**：版本脚注补充：UHC4T 因硬件结构，"Safety line" 实际映射到 "DUT board disconnect"，"Safety line" 在 UHC4T 上永远不会被置位；该特殊映射只适用于 UHC4T。

## 出处

- `02_System_reference/02.06_Command_Reference/02.06.10.02.11_PSAS__-__Power_Supply_Accumulated_Status.htm`——本页正文、参数位表、示例、Errors 与 Functional changes 均取自本篇（topic `98691_2.htm`）；`DPS flag description` / `DPS flag implementation` / `DPS flag reset` 三张表在同主题 `98691.htm` 的投放中。