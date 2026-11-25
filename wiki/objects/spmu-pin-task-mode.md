---
type: object
title: SPMU_PIN_TASK.mode()
layer: L3
stage: level
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.24_SPMU_PIN_TASK.mode.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# SPMU_PIN_TASK.mode()

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **3,502 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.24_SPMU_PIN_TASK.mode.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
SPMU_PIN_TASK& mode(const STRING& mode);
```
[表] Parameter
列: Parameter | Description
行 1:
  mode
  Default mode is "IFVM".
    Refer to the list of
    available options of the mode parameter
    below.
[表] Available options of parameter: mode
列: mode | Description
行 1:
  "IFVM"
  Force current and measure voltage.
    
    This mode is set so that voltage is forced and the required
    current is defined via symmetrical set current clamp values.
    Therefore, you must observe the minimum clamp current distance
    for setting the forced current in the "IFVM"
    mode.
    
    AVI64 and FVI16 support the real current forcing modes `"CFVM" and "CFIM"`（raw: `131275.htm#_131275__r_AVI64_FVI16`） in
    which the minimum clamp distance does not have to be
    observed.
行 2:
  "VFIM"
  Force voltage and measure current.
行 3:
  "VM_HIZ"
  High impedance voltage measurement.
行 4:
  "VM_HIZ_HAC"
  High impedance voltage measure with high accuracy. The voltage
    range is selected via `SPMU_PIN_TASK.min()`（raw: `131359.htm`） and `SPMU_PIN_TASK.max()`（raw: `131360.htm`）.
行 5:
  "IFVM_UNGANGED"
  Force current and measure voltage by temporarily separating
    ganged channels for this measurement.
    The ganged channels are
    temporarily unganged to the minimum number of channels that is
    required to force the programmed current. The voltage
    measurement is always performed on the first channel of the
    ganged group. Temporarily unganging for voltage measurements
    will improve the stability of the forced current and therefore
    improve the stability of the voltage measurement.
行 6:
  "VFIM_UNGANGED"
  Force voltage and measure current by temporarily separating
    ganged channels for this measurement.
    See also `Number of channels in unganged mode`（raw: `131275.htm#_131275__s_Number_of_channels_unganged`） below.
    
    Note that on DPS128/64 and XPS256 you cannot execute a current
    compare on a ganged group of channels in unganged mode. Already activated
    comparators are silently disabled in unganged mode. A user notification (Error or
    warning) is omitted in this case, to avoid any interrupt in the testflow. The
    previous state of the comparators is automatically restored after the ganged group
    has been restored.
行 7:
  "PPMU_BADC"
  Connects the board ADC (BADC) with the pin PMU (PPMU) for static
    measurements.
    
    Mapped to "IFVM" for DC Scale cards without a
    separate board ADC.
行 8:
  The following [跨 2 列]
    measurement modes are supported only for the `DC Scale XPS256 card`（raw: `350661.htm`）.
行 9:
  "VFVM"
  Force voltage and measure voltage.
行 10:
  "CFVM"
  Force current directly and measure voltage or current. [跨 2 行]
    
    Both the lower and the upper clamp must be set by function `SPMU_PIN_TASK.clamp()`（raw: `131358.htm`） if these modes are selected.
行 11:
  "CFIM"

Note
 If the
`SPMU_PIN_TASK.iForce()`（raw: `131352.htm`）
 or
`SPMU_PIN_TASK.vForce()`（raw: `131353.htm`）
 is
used, the corresponding mode(
"IFVM"
 or
"VFIM"
)
is set automatically.

### Return value

A reference to the
`SPMU_PIN_TASK`（raw: `55669.htm`）

object.

### Example

In the example below
"VM_HIZ"
 selects the Board ADC for a
voltage
measurement.

```
SPMU_TASK badc_task;

ON_FIRST_INVOCATION_BEGIN();
badc_task.pin("pinName").mode("VM_HIZ");
badc_task.pin("pinName").settling(1 ms).samples(1);
badc_task.pin("pinName").relay("TERM");
badc_task.pin("pinName").min(0 V).max(5 V);
badc_task.preAction("NONE").execMode("PVAL").execute();
ON_FIRST_INVOCATION_END();

cout << badc_task.getValue("pinName") << endl;
```

<!-- 语法节 end -->

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
