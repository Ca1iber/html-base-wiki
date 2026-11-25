---
type: object
title: DSCP, DSCP? - (Define System Control Parameter)
layer: L1
stage: project
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# DSCP, DSCP? - (Define System Control Parameter)

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **3,390 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### DSCP

```
DSCP [device_cycle], [waveform_set], [timing_set], [level_set], [dps_set], [pmu_set],
[devicecycle_set], [routing_set], [period_res_prec],
```

### DSCP?

```
DSCP?
```

returns:

```
DSCP {device_cycle}, {waveform_set}, {timing_set}, {level_set}, {dps_set},
{pmu_set}, {devicecycle_set}, {routing_set}, [period_res_prec],
[period_res_compatibility_model]
```

### Parameters

[表]
行 1:
  device_cycle
  The device_cycle parameter is an integer that defines the absolute
    maximum number of device cycles that you can create for one
    pin.
    Default: 256
    
    Maximum: 16384
    
    Note that the
    total number of device cycles gets evenly divided between the
    combined number of waveform sets and wavetables. If you use the
    default values, then 256 device cycles divides into the total
    number of 32 `waveform sets and wavetables`（raw: `98578.htm#_98578__row_waveform_set`） to give you 8 device cycles per
    waveform set/wavetable. If you choose values that do not divide
    evenly, then the number of device cycles will be rounded up to
    the next multiple of the `waveform_set`（raw: `98578.htm#_98578__row_waveform_set`） parameter.
行 2:
  devicecycle_set
  The devicecycle_set parameter is an integer
    that defines the maximum number of device cycle sets that you
    can create. Device cycle sets are needed for selective digital
    capture.
    
    Default: 1
    
    Maximum: 128
行 3:
  dps_set
  The dps_set parameter is an integer that
    defines the maximum number of DPS sets you can create.
    
    Default: 32
    
    Maximum: 256
行 4:
  level_set
  The level_set parameter is an integer that
    defines the combined total of level sets for fixed and equation
    based levels that you can create.
    
    Default: 32
    
    Maximum: 256
行 5:
  period_res_prec
  This parameter defines the precision with which the period
    resolution is calculated by the system. It has no effect
    on a user defined period resolution (using, for example, the
    period_res keyword in the equation
    set).
    
    The default is 4, if the .technology file
    does not contain this parameter.
    
    If it does, the value of the .technology
    file is the default.
    
    This value is set to 9, the greatest possible value, when a
    device is created.
行 6:
  pmu_set
  The pmu_set parameter is an integer that
    defines the maximum number of actions that can be contained in
    all measurement sets of all PPMU DC sets.
    
    Default: 1024
    
    Maximum: 12800
行 7:
  routing_set
  Defines the number of routing sets managed by the firmware,
    provided by the MCD.
    
    Default: 256
    
    Maximum: 512
行 8:
  timing_set
  The timing_set parameter is an integer that
    defines the maximum combined total of timing sets for fixed and
    equation based timing you can create.
    
    Default: 256
    
    Maximum: 999
    
    The number of timing sets must be equal to or greater than the
    number of waveform sets, as there must be at least one timing
    set per waveform set.
行 9:
  waveform_set
  The waveform_set parameter defines the maximum
    combined total of waveform sets (fixed timing) and wavetables
    (equation based timing) you can create. Thus, if you specify a
    value of 32, you could, for example, create 10 waveform sets and
    22 wavetables.
    
    Default: 32
    
    Maximum: 128

### Example

```
DSCP 256,16,256,32,32,1024,16,1,256,
```

<!-- 语法节 end -->

## 报错条件（脚本从 raw 的 `## Errors` / `## Warnings` 段逐字取）

<!-- 报错节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-errors` 时消失** -->

> 本节**逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.htm>` 的 `## Errors` 段。**不是转述。**
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Errors

An error is generated if:

The number of device cycles defined is out of range.

The number of waveform sets defined is out of range.

The number of timing sets defined is out of range.

The number of level sets defined is out of range.

The number of DPS sets defined is out of range.

The specified set size is too large for the memory configuration.

The specified number of timing sets is smaller than the number of waveform sets.

<!-- 报错节 end -->

## 是什么

**文档事实** DSCP 用于定义不同类型的 parameter set 可创建的最大实例数，并在 Sequencer Memory 中预留所需空间；由于同类型每个实例大小相同，所需空间可由实例数算出。`DSCP?` 查询返回当前设置。

**文档事实** DSCP 取代先前版本中的 `CNTR, CNTR?` 命令。

**文档事实** 每次调用 DSCP 都会删除 Sequencer Memory 中原有的全部数据；因此用 DSCP 修改参数后，必须重新加载 device setup。

**文档事实** 每次切换到另一个 device 时都会调用 DSCP。这次调用的参数值可在 `.technology` 文件中指定；该文件位于每个 device 的主目录。未在 technology file 中定义的参数使用文档给出的默认值。

**文档事实** 文档 `Application` 段把该命令归入 Test Setup，参见 Introduction to firmware commands。

## 典型用法

**文档事实** 调用形式为 `DSCP [device_cycle], [waveform_set], [timing_set], [level_set], [dps_set], [pmu_set], [devicecycle_set], [routing_set], [period_res_prec]`；文档示例为 `DSCP 256,16,256,32,32,1024,16,1,256,`。

**文档事实** 用 `DSCP?` 读回当前值；返回的列表中除调用参数外还包含 `period_res_compatibility_model`。

**文档事实** `device_cycle` 定义单个 pin 可创建的 device cycle 绝对上限，默认 256、最大 16384。device cycle 总量在 waveform sets 与 wavetables 的合计数量之间均分：使用默认值时 256 除以 32，得到每个 waveform set/wavetable 8 个 device cycle；若不能整除，则向上取整到 `waveform_set` 参数的下一个倍数。

**文档事实** `timing_set` 的数量必须大于或等于 `waveform_set`，因为每个 waveform set 至少需要一个 timing set。

**文档事实** `period_res_prec` 定义系统计算 period resolution 的精度，不影响用户自定义的 period resolution（例如 equation set 中的 `period_res` 关键字）。若 `.technology` 文件不含该参数，默认值为 4；若含，则以 technology file 的值为默认；创建 device 时该值被设为最大值 9。

**文档事实** 其余参数的默认值与最大值：`devicecycle_set` 1 / 128（用于 selective digital capture 的 device cycle sets）、`dps_set` 32 / 256、`level_set` 32 / 256（fixed 与 equation based levels 合计）、`pmu_set` 1024 / 12800（所有 PPMU DC set 的全部 measurement set 内的 action 上限）、`routing_set` 256 / 512（由 MCD 提供给固件的 routing sets）、`timing_set` 256 / 999、`waveform_set` 32 / 128（fixed timing 的 waveform sets 与 equation based timing 的 wavetables 合计）。

**文档事实** 文档给出的参数语义示例：`waveform_set` 设为 32 时，可以创建 10 个 waveform set 和 22 个 wavetable。

**文档事实** 创建新测试配置前必须先定义控制参数，DSCP 就是为此提供的命令；文档的 System preparation by firmware commands 页面描述参数选择流程。

## 和谁有关

**文档事实** `.technology` 文件（`01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.01.02_Technology_file_for_a_device.htm`、`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.03.03_Technology_file_for_a_device.htm` 等）：DSCP 每次切换 device 时被调用，其参数可在 `.technology` 中指定；technology file 页面说明其中的参数对应 Command Reference 里的 DSCP 参数，未定义的参数使用 DSCP 默认值。

**文档事实** Sequencer Memory：DSCP 按各类 set 的最大实例数在 Sequencer Memory 中预留空间，且每次调用都会清空其中原有数据。

**文档事实** 创建 level set 的页面（`02.06.05.01.05.01_Create_a_fixed_level_set.htm`）：可创建的 level set 数量上限由先前 DSCP 定义的最大值决定。

**文档事实** 创建 DPS set 的页面（`02.06.05.01.05.04_Set_Fixed_Power_Supply_Levels.htm`）：可创建的 DPS sets 数量上限由 DSCP 先前定义的最大值决定。

**文档事实** 引用 set 编号的固件命令：`SPRM`、`TSUS`、`WSUS`、`LSUX`、`TORC`、`TORS`、`TORR`、`DRLV`、`RCLV`、`TERM`、`SQPG`、`UDRS`、`DSUS` 等页面都把合法编号范围追溯到 DSCP 定义的对应最大值。

**文档事实** `DTCP, DTCP?`（`02.06.02.02.93`）：在 Related information 中列为相关命令。

**文档事实** `CNTR, CNTR?`：DSCP 取代旧版本的该命令。

## 版本

**文档事实** `Functional changes` 段只写「Introduced before SmarTest 6.3.2」，未列出后续变更。

## 出处

- `02_System_reference/02.06_Command_Reference/02.06.02.02.90_DSCP__DSCP__-__Define_System_Control_Parameter.htm`（主源：命令说明、语法、参数、Application、Errors、示例、Related information、Functional changes）
