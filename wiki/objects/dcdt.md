---
type: object
title: DCDT, DCDT? - (Device Cycle DefaulT)
layer: L1
stage: timing
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.41_DCDT__DCDT__-__Device_Cycle_DefaulT.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# DCDT, DCDT? - (Device Cycle DefaulT)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **2,341 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.41_DCDT__DCDT__-__Device_Cycle_DefaulT.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### DCDT

```
DCDT {waveform_set}, {"default_name"}
```

### DCDT?



### DCDT? {waveform_set}

returns:

```
DCDT {waveform_set},{"default_name"}
```

For
equation-based
testing

```
DCDT? {"wavetable_name"}
```

returns:

```
DCDT {"wavetable_name"},{"default_name"}
```

or:

```
DCDT? {specset_id}
```

returns:

```
DCDT {specset_id}, {"default_name"}
```

or,
for multiport
specifications:

```
DCDT? {"multi-port_spec"}[, (portlist)]
```

returns:

```
DCDT {"multi-port_spec"},{"default_name"} [, (portlist)]
```

Note
specset_id
,
multi-port_spec
, and

wavetable_name
 can only be used with the
DCDT?
 query.
They are not allowed with the
DCDT
 command because overrides are only allowed
with the
CLKR
,
ETIM
(
ETDS
 for 14 or more
edge setups), and
PCLK
 commands.

[表] Parameters
行 1:
  waveform_set
  Waveform Set Number. Enter an integer in the range 1 to the maximum number of
    allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `98878.htm`）. For the
    query, you can also enter ALL for all waveform sets.
行 2:
  specset_id
  Derived as follows:
    
    100 * equation_set_no + specset_no
行 3:
  multi-port_spec
  To query a multi-port specification, enter the name of the specification.
行 4:
  wavetable_
    
    name
  The wavetable name. Enter a string of up to 40 alphanumeric characters (upper or
    lower case) enclosed in double quotes. The appropriate wavetable is determined by looking
    at which wavetable is referenced by equation_set_no and specset_no in the Timing
    Specification File.
行 5:
  default_name
  Enter a string of up to 16 alphanumeric characters (upper or lower case) enclosed
    in double quotes.
    
    Reserved names are not allowed - these are the character sequences scan,
    SCAN, c, C and BREAK. Illegal characters are also not allowed
    - these are #, (, ), ,, ;, ?, @ and
    *.
行 6:
  portlist
  For multi-port specifications, you can restrict the query to the ports specified
    here. The ports must be defined in the pin configuration and used in the specified
    multi-port specification.

### Example

```
DCDT 1,"HOLD"
```

This example defines the default device cycle name

HOLD
 for Waveform Set 1.

```
DCDT? "fast_ARM",(ARMPort)
DCDT "fast_ARM","Cycle",(ARMPort)
```

This
example queries the default device cycle name for the
ARMPort
port in the multi-port
specification
fast_ARM
.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.41_DCDT__DCDT__-__Device_Cycle_DefaulT.htm>` 的 `## Errors` 段。**不是转述。**
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

waveform_set
is greater than the range allowed by the
WSUS
 command.

waveform_set
is smaller than one.

You enter an illegal device cycle name (a reserved name, a name containing illegal
characters).

wavetable_name
does not reference a defined wavetable.

specset_id
does not reference a defined wavetable.

specset_id
is invalid because equation_set_no, specset_no or both are invalid.

multi-port_spec
does not reference a defined multi-port specification.

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
