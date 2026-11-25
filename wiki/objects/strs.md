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

**文档事实** STRS?（Spec TRansition Search）在一个循环中重复执行 functional test；每次执行时，在指定区间内系统地修改某个 timing 或 level spec 变量的值，作用于查询中指定、且在其 timing/level setup 中依赖该变量的所有 pin。

**文档事实** 搜索目标是找出使测试结果从 PASS 变为 FAIL、或从 FAIL 变为 PASS 的那个变量值。

**文档事实** 若在搜索区间内找到这种跃迁，STRS? 返回最后一个结果仍与起始值相同的值，以及第一个结果已改变的值；若结果始终不变，则只返回一个值，即 stop 值。

**文档事实** `start`/`stop` 的默认值是 primary spec set 中为该 spec 变量定义的最小/最大值；文档说明给出这些最大/最小值可以加快搜索。

**文档事实** 在 Pin Scale 系统上，STRS? 可以临时改变 primary port（见 `port` 参数说明），并在搜索完成后恢复 primary port。

**文档事实** `mode` 有 L（linear search）、LB（linear/binary search）、B（binary search）；`spec_type` 为 `LEV`（levels）或 `TIM`（timing）；`resolution` 指定搜索使用的最小步长。

**文档事实** 若所用的 primary sets 不是 equation-based，将产生错误（见报错节）。

## 典型用法

**文档事实** 示例 `STRS? 0.5,2.0,LB,,LEV,"aclk_vo_swing",0.1,0.1` 返回 `STRS GE,2,,`。

**文档事实** 按语法 `[start],[stop],{mode},[(pinlist)],{spec_type},{"spec_name"},[stepwidth],{resolution}`，示例依次为 start=0.5、stop=2.0、mode=LB、pinlist 为空、spec_type=LEV、spec_name=`aclk_vo_swing`、stepwidth=0.1、resolution=0.1。

**文档事实** pinlist 为空或省略时默认 `@`（所有 pin）；pinlist 也可包含 `[[dfgp]]` 定义的组。

**文档事实** `mode` 为 B 时 `stepwidth` 可选；`resolution` 特别适用于浮点范围的二分搜索，因为 start 与 stop 之间有无穷多个值。

**文档事实** `start` 可大于 `stop`，此时搜索沿负方向进行；`stop` 也可小于 `start`。

**文档事实** 多端口 setup 中可在 `spec_name` 后加 `@port`，使变量值只对属于该 port 的 pin 修改；即使该变量在此 port 的 timing 规格中是 global scope 也如此。若不给 port，则只修改其 port 将该变量设为 global scope 的 pin；setup pins 对此没有影响。

**文档事实** 在 Pin Scale 系统上，若 `spec_name` 用于 port period 的定义，指定 port 会使该 port 临时作为 primary port；在 port 名后加 `@UNCHANGED` 可抑制这一切换。

**文档事实** 返回格式为 `STRS {res_spec}, [pass_meas_value], [fail_meas_value], [(pinlist)]`；示例响应中的 `GE` 属 res_spec（greater than or equal to），`2` 对应 pass_meas_value，后两个字段省略。

**建议** 为缩短搜索，先在 primary spec set 中为该 spec 变量给出最大/最小值；需要定位浮点边界时用 B 模式并设置 `resolution`。

## 和谁有关

- **文档事实** `[[dfgp]]` — STRS 的 pinlist 可包含由 DFGP 创建的组（参数说明）；DFGP 页也把 STRS 列入可引用组名的命令。
- **文档事实** `[[execution-context]]` — 可选的第一个参数 `exec_context` 是 execution context，文档指向 “Using execution contexts”。
- **文档事实** SHSP, SHSP?（SHmoo SPecs）与 SHVL, SHVL?（SHmoo spec VaLues）— 本页 Related information 列出二者；本 wiki 无对应对象页。
- **文档事实** `Modifying the period for a search or shmoo in a multi-port setup (Pin Scale)` — 本页在描述 port 与临时 primary port 时两次指向该页，`@port[@UNCHANGED]` 的用法见该页。
- **文档事实** `Global and local scope of base variables` — 本页在解释 port 与 spec 变量作用域时指向该页。
- **文档事实** DPSR（Define Parallel SeaRch）与 EXSR（EXecute SeaRch）— 它们的页面在 Related information 中把 STRS? 列为相关项（objpack 入边）；DPSR 把搜索条件写入 search set，EXSR 并行执行这些条件。
- **推断** STRS? 在单条查询内循环执行测试并修改 spec 变量；DPSR/EXSR 则先定义 search set 再并行执行搜索。文档只给出互列关系，没有说明二者互斥或调用顺序。
- **文档事实** equation based level setup / primary sets — 报错节要求 primary sets 为 equation-based，否则报错；本页未展开如何定义 equation based primary sets。
- **文档事实** List of commands — 入边显示 STRS? 列在命令参考总表。
- **文档事实** Application 段把 STRS? 的用途定为 Spec search testflow。

## 版本

**文档事实** Functional changes 记：

- Introduced before SmarTest 6.3.2
- SmarTest 7.1.0：Setting the primary port

## 出处

- `02_System_reference/02.06_Command_Reference/02.06.02.02.251_STRS__-__Spec_TRansition_Search.htm`，主源，含概览、临时 primary port 说明、Syntax、Parameters、Application、Errors、Example、Related information 与 Functional changes，已用 `show.py 02.06.02.02.251` 读取。
- `02_System_reference/02.06_Command_Reference/02.06.02.02.86_DPSR__DPSR__-__Define_Parallel_SeaRch.htm` 与 `02_System_reference/02.06_Command_Reference/02.06.02.02.121_EXSR_-__EXecute_SeaRch.htm`，用于确认与 STRS? 的 Related information 关系及搜索语义，已用 `show.py --head` 读取。
- 入边与交叉引用取自 `extract/objpack.py` / `edges.jsonl`。
