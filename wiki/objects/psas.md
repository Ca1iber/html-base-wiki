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

（待补）

## 典型用法

（待补）

## 和谁有关

（待补）

## 版本

（待补）

## 出处

（待补）
