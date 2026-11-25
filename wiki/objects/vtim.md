---
type: object
title: VTIM? - (Verify TIMing)
layer: L1
stage: timing
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.329_VTIM__-__Verify_TIMing.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# VTIM? - (Verify TIMing)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **3,417 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.329_VTIM__-__Verify_TIMing.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
VTIM? {waveform_set},{timing_set},{(pinlist)}
```

returns:

```
VTIM {status}
```

### Equation-based testing

```
VTIM? {specset_id|"multi-port_spec"},{timing_set}, {(pinlist)}
```

returns:

```
VTIM {status}
```

### Parameters

[表]
行 1:
  waveform_set
  Waveform Set Number. Enter [跨 2 列]
    PRM for the Primary Waveform Set, or an integer in the range 1 to the
    maximum number of allowed waveform sets. The maximum number is determined by `WSUS, WSUS? - (Waveform Sets USed)`（raw: `98878.htm`）.
行 2:
  specset_id
  Derived as follows: [跨 2 列]
    
    100 * equation_set_no + specset_no
行 3:
  multi-port_spec
  To query a multi-port specification, enter [跨 2 列]
    the name of the specification.
行 4:
  timing_set
  Specifies the timing sets to be checked. [跨 2 列]
    Enter PRM for the Primary Timing Set, ALL for all
    timing sets, or an integer in the range 1 to the maximum number of allowed timing sets. The
    maximum number is determined by `TSUS, TSUS? - (Timing Sets USed)`（raw: `98817.htm`）.
    
    In a multi-port setup, the check is performed for those pins from
    pinlist that belong to the same port. If you specify a number, a timing
    set with this number must be present in every equation set that is associated with a port
    of the multi-port specification.
行 5:
  pinlist
  The name of the pin or pins to be checked. [跨 2 列]
    This parameter can also include groups previously created by `DFGP, DFGP? - (DeFine GrouP)`（raw: `98546.htm`）. If
    more than one pin is to be included, the names must be separated with a comma. The symbol
    @ can be used to check all configured pins.
    
    In a multi-port setup, the pins can belong to more than one port. Only those pins are
    considered that belong to one of the ports of the specification.
行 6:
  status [跨 3 行]
  The system returns: [跨 2 列]
行 7:
  0
  The timing is not the same.
行 8:
  1
  The timing is the same.

### Example

The following example illustrates the working of
VTIM?
 in a
multi-port setup. The pins S1_1 and DS0_1 belong to the same port, and S1_2 belongs to another
one.

```
> ETDS? "spec_port_1_port_2",ALL,,(S1_1,DS0_1,S1_2)
< ETDS "spec_port_1_port_2",1,,"d1:0 d2:30",(S1_1,DS0_1)
< ETDS "spec_port_1_port_2",2,,"d1:0 d2:12",(S1_1)
< ETDS "spec_port_1_port_2",2,,"d1:1 d2:12",(DS0_1)
< ETDS "spec_port_1_port_2",1,,"d1:-0.67 d2:1.33 d3:9.3",(S1_2)
```

This
call of
`ETDS?`（raw: `98599.htm`）
 shows that the edge timings of S1_1 and DS0_1 are the
same in timing set 1, but not in timing set 2 of the port to which these pins
belong.

```
> PCLK? "spec_port_1_port_2",ALL,(S1_1,DS0_1,S1_2)
< PCLK "spec_port_1_port_2",1,50,(S1_1)
< PCLK "spec_port_1_port_2",2,20,(S1_1)
< PCLK "spec_port_1_port_2",1,50,(DS0_1)
< PCLK "spec_port_1_port_2",2,20,(DS0_1)
< PCLK "spec_port_1_port_2",1,16.667,(S1_2)
```

This
call of
`PCLK?`（raw: `98682.htm`）
 shows that the periods of S1_1 and DS0_1 are the same
in the two timing sets of the
port.

```
> VTIM? "spec_port_1_port_2",ALL,(S1_1,DS0_1,S1_2)
< VTIM 0
```

VTIM?

returns 0 because of the different timings for S1_1 and DS0_1 in timing set
2.

```
> ETDS "spec_port_1_port_2",2,,"d1:0 d2:12",(DS0_1)
> VTIM? "spec_port_1_port_2",ALL,(S1_1,DS0_1,S1_2)
< VTIM 1
```

After
changing the edge timing of DS0_1 in timing set 2 to the values of S1_1 with a call of
`ETDS`（raw: `98599.htm`）
,
VTIM?
 returns 1 although DS0_1 has a different
timing in timing set 1 and in timing set 2, and S1_2, which belongs to another port, has
different values altogether.

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.329_VTIM__-__Verify_TIMing.htm>` 的 `## Errors` 段。**不是转述。**
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

The specified waveform set number is outside the range allowed by the
`WSUS`（raw: `98878.htm`）
 command.

The specified timing set number is outside the range allowed by the
`TSUS`（raw: `98817.htm`）
 command.

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
