---
type: object
title: STRS? - (Spec TRansition Search)
layer: L1
stage: timing
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.251_STRS__-__Spec_TRansition_Search.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# STRS? - (Spec TRansition Search)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **4,737 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.251_STRS__-__Spec_TRansition_Search.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
STRS? ["exec_context",] [start], [stop], {mode}, [(pinlist)], {spec_type}, {"spec_name[@port[@UNCHANGED]]"}, [stepwidth], {resolution}
```

returns:

```
STRS {res_spec}, [pass_meas_value], [fail_meas_value], [(pinlist)]
```

### Parameters

[表]
行 1:
  exec_context
  An execution context. For more information on execution contexts see `Using execution contexts`（raw: `135848.htm`） .
行 2:
  start
  Double float with up to 5 digits after the decimal point defining the value of
    spec_name at the start of the search. The maximum valid range is
    -21474.83648 to +21474.83647, though this may be limited by the maximum and minimum values
    defined with the spec. If the parameter is omitted, the minimum value as defined in the
    spec set will be used.
    
    The start value can be greater than the stop value. In this case the search will be in
    the negative direction.
行 3:
  stop
  Double float with up to 5 digits after the decimal point defining the value of
    spec_name where you want the search to end. The maximum valid range is
    -21474.83648 to +21474.83647, though this may be limited by the maximum and minimum values
    defined with the spec. If the parameter is omitted, the maximum value as defined in the
    spec set will be used.
    
    The stop value can be smaller than the start value. In this case the search will be in
    the negative direction.
行 4:
  mode
  Search mode. Use:
    
    L to specify a linear search,
    
    LB to specify linear/binary search,
    
    B to specify a binary search.
行 5:
  pinlist
  The name of the pin or pins for which the value of the spec variable is to be
    modified. This parameter may also include groups previously created by the `DFGP`（raw: `98546.htm`） command. If more than one pin is to be included, the names must
    be separated with a comma.
    
    The @ character indicates all pins. This is the default.
行 6:
  spec_type
  Which specification type to use. Use :
    
    LEV to specify levels, or
    
    TIM to specify timing.
行 7:
  spec_name
  A string of up to 64 alphanumeric characters (upper or lower case) enclosed in
    double quotes.
    
    If you use the option
    @port[@UNCHANGED],
    (see the port parameter), you must include this extension in the double
    quotes, too.
行 8:
  port
  In a multi-port setup, you can add a port name to the spec variable. This will have
    the effect that the value of the variable will be modified only for pins belonging to this
    port. This holds even if the variable has global scope for this port in the timing
    specification.
    
    If you specify the spec variable without a port in a multi-port setup, its value
    will only be modified for a pin whose port has the spec variable set to global scope.
    
    For more information on the scope of a variable see `Global and local scope of base variables`（raw: `58766.htm`）.
    
    Note that if a port that is specified with the name of the variable it is this port on
    which the value of the variable will be modified. The setup pins have no influence on
    this.
    
    On a Pin Scale system, the specification of a port will have an additional
    effect:
    
    If spec_name is used in the definition of the port period, this port
    will be temporarily used as the primary port. For more information see `Modifying the period for a search or shmoo in a multi-port setup`（raw: `127456.htm`）.
    
    This switch can be suppressed by adding @UNCHANGED to the port
    name.
行 9:
  stepwidth
  The search step width in the unit specified with the corresponding spec. This is
    optional if mode is B.
行 10:
  resolution
  The smallest step size to be used in the search. Especially useful in a binary
    search of a range of floating point numbers, where the number of values between start and
    stop is infinite. The unit must be the same as defined with the spec.
行 11:
  res_spec
  LT (less than)
    
    LE (less than or equal to)
    
    EQ (equal to)
    
    GE (greater than or equal to)
    
    GT (greater than).
行 12:
  pass_meas_value
  A double float defining the passed measured value, with up to 5 digits after the
    decimal point. Valid range is -21474.83648 to +21474.83647.
    
    This parameter contains the last (in a PASS/FAIL transition) or the first (in a FAIL/PASS
    transition) value where the test passed.
行 13:
  fail_meas_value
  A double float defining the failed measured value, with up to 5 digits after the
    decimal point. Valid range is -21474.83648 to +21474.83647.
    
    This parameter contains the first (in a PASS/FAIL transition) or the last (in a FAIL/PASS
    transition) value where the test failed.

### Example

```
STRS? 0.5,2.0,LB,,LEV,"aclk_vo_swing",0.1,0.1
```

returns

```
STRS GE,2,,
```

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.251_STRS__-__Spec_TRansition_Search.htm>` 的 `## Errors` 段。**不是转述。**
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if the primary sets used are not
equation-based.

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
