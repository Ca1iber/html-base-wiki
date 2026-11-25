---
type: object
title: CONF, CONF? - (CONFiguration)
layer: L1
stage: project
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.31_CONF__CONF__-__CONFiguration.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# CONF, CONF? - (CONFiguration)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **3,398 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.31_CONF__CONF__-__CONFiguration.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### CONF

```
CONF ["context",]{pin_type},[pin_oper_mode],{(pinlist)}
```

### CONF?

```
CONF? ["context"|ALL,] {(pinlist)}
```

returns:

```
CONF ["context",]{pin_type},{pin_oper_mode},{(pinlist)}
```

### Parameters

[表]
行 1:
  context
  This extra parameter specifies a mode context. If it is omitted, the default mode context
    DEFAULT is set or read. If
    DEFAULT is the only context defined, the
    parameter is omitted in the query reply.
    
    The default mode context is predefined. All other mode contexts
    must be defined with the CTXT command.
    
    If you specify ALL in the query,
    CONF? will display all mode contexts.
行 2:
  pin_type
  The mandatory parameter assigns channel resources to the pin. This can be:
    
      [子表]
      子行 1:
        I
        Configures a drive pin.
      子行 2:
        O
        Configures a receive pin.
      子行 3:
        IO
        Configures a bidirectional pin.
      子行 4:
        DC
        Configures a pin for DC measurements.
          The pin is only connected to the PMU, and no
          driver or receiver resources are allocated to it.
          
          For DC Scale channels (power or signal pins)
          the mode is always DC.
          
          This option is not allowed for Smart Scale
          pins.
      子行 5:
        OFF
        The pin is not available for measurements.
行 3:
  pin_oper_mode
  The mandatory parameter defines or indicates the operating mode of the pins in
    pinlist. The operation mode can be:
    
      [子表]
      子行 1:
        DCSIGNAL
        In the query this indicates that the pin is
          associated with a DC Scale channel and has been
          configured in PMU mode with
          DFPN.
      子行 2:
        POWER
        In the query this indicates that the pin is
          associated with a DC Scale channel and has been
          configured in DPS mode with
          DFPS.
      子行 3:
        CMON
        Configures the pin as current monitor
          output. For more information, refer to `XPS256 current monitor`（raw: `354977.htm`）.
      子行 4:
        F160
        Specifies Standard operating mode. This
          is the default. It must be selected for pins on
          PS1600 boards.
      子行 5:
        F330
        Not valid.
      子行 6:
        FAST
        This operation mode must be selected for
          fast pins. Note that no pin can be set to
          FAST in the default mode
          context DEFAULT, and that no
          IO pin can be set to
          FAST.
          
          For Smart Scale pins this mode will be mapped
          to F160.
行 4:
  pinlist
  The name of the pin or pins to be configured or listed. If
    more than one pin is to be included, the names must be separated
    with a comma.
    
    The symbol @ can be used in the query to list all pins that were
    previously either explicitly configured with the
    CONF command, or (in the case of DC Scale
    pins) implicitly with the DFPN or
    DFPS command.

### Examples

### Example 1
```
> CONF IO,F160,(D0,D1)
```

This
example configures pins
D0
 and
D1
 as bidirectional
pins operating in Standard Mode for the default mode context.

### Example 2
```
> CONF? (sdd,vdd)
< CONF DC,DCSIGNAL,(sdd)
< CONF DC,POWER,(vdd)
```

This example queries the DC Scale channels

sdd
 and
vdd
, which were set with
`DFPN`（raw: `98550.htm`）
 to PMU mode (
DCSIGNAL
) and with

`DFPS`（raw: `98551.htm`）
 to DPS mode (
POWER
),
respectively.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.31_CONF__CONF__-__CONFiguration.htm>` 的 `## Errors` 段。**不是转述。**
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if you attempt to configure pins while
the sequencer is in the run or the break state (see the
SQST

command).

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
