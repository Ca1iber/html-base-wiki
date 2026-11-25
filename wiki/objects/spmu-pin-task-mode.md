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

**文档事实** `SPMU_PIN_TASK.mode()` 是 `SPMU_PIN_TASK`（每 pin DC 测量条件容器）的成员函数，用于设置测量模式，例如 force current / measure voltage 或 force voltage / measure current，并在需要时连接 BADC 或 PPMU。语法为 `SPMU_PIN_TASK& mode(const STRING& mode);`，默认模式为 `"IFVM"`，返回 `SPMU_PIN_TASK` 引用以便链式调用。

**文档事实** 可选模式：`"IFVM"`（force current, measure voltage；默认）、`"VFIM"`（force voltage, measure current）、`"VM_HIZ"`（高阻电压测量）、`"VM_HIZ_HAC"`（高精度高阻电压测量，量程由 `min()`/`max()` 选择）、`"IFVM_UNGANGED"`（测量时临时拆分 ganged 通道，以最小所需通道数 force 电流，电压始终在第一通道测）、`"VFIM_UNGANGED"`（测量时临时拆分 ganged 通道）、`"PPMU_BADC"`（把 board ADC 与 pin PMU 连接做静态测量；对没有独立 board ADC 的 DC Scale 卡映射为 `"IFVM"`）。仅 `DC Scale XPS256` 支持 `"VFVM"`（force voltage, measure voltage）、`"CFVM"`、`"CFIM"`（直接 force current，测电压或电流）。

**文档事实** `"IFVM"` 实际是 force voltage、通过对称 clamp 电流值定义所需电流，因此必须遵守最小 clamp 电流间距；AVI64 与 FVI16 支持真正的 current forcing 模式 `"CFVM"`/`"CFIM"`，不需要遵守该最小间距。选择 `"CFVM"`/`"CFIM"` 时，下、上 clamp 都必须由 `SPMU_PIN_TASK.clamp()` 设置。若调用 `SPMU_PIN_TASK.iForce()` 或 `vForce()`，对应模式（`"IFVM"`/`"VFIM"`）会自动设置。

**文档事实** 若多个 pin PMU 同时连接到 BADC，会报 resource conflict error。文档指出虽然可用本函数做 Board ADC 测量，但推荐改用 `FLEX_RELAY` 类。

**文档事实** 使用 `"VFIM_UNGANGED"` 时，`max()`、`min()` 或 `limits()` 的 pass/fail 限值决定测量范围，也决定临时 ungang 后保留多少通道；文档给出 `No. of remaining ganged channels = CEIL [ P/F limit / (ilimitPerChannel …)]` 形式的规则，并说明每通道 current limit 会按该量程的最大误差下调，以确保临时 unganged 时仍能流所需电流。文档建议始终仔细核对临时 unganged 模式下的电流测量，因为自动 ungang 可能使测量落在量程边界或接近编程 clamp 电流。

**推断** `mode()` 是每 pin 设置中具有“前置约定”作用的一项：`min()`/`max()` 的单位、`clamp()` 的单位与要求、`relay()` 的动作、`connectState()` 的合法选项都取决于已选模式；这可从这些成员页的说明归纳。

## 典型用法

**文档事实** 文档示例用 `"VM_HIZ"` 选择 Board ADC 做电压测量：
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

**文档事实** 需要在 ganged 通道上做电流测量并希望改善强制电流/电压测量稳定性时，用 `"IFVM_UNGANGED"`；需要 force voltage、measure current 且临时拆分 ganged 组时用 `"VFIM_UNGANGED"`。文档提醒：在 DPS128/64 与 XPS256 上，unganged 模式下不能对 ganged 组做 current compare；已启用的 comparator 会被静默禁用（不发 error/warning，以免打断 testflow），ganged 组恢复后自动恢复原状态。

**文档事实** 在 XPS256 上可用 `"VFVM"`、`"CFVM"`、`"CFIM"`；选择 `"CFVM"`/`"CFIM"` 必须用 `clamp()` 同时设置下、上 clamp。`"VM_HIZ_HAC"` 的电压量程用 `min()`/`max()` 选。

**建议** 做 Board ADC 测量时优先用文档推荐的 `FLEX_RELAY`；使用 `"..._UNGANGED"` 时仔细核对电流测量结果（文档明确建议 always verify），并且不要同时把 `SPMU_TASK.execMode()` 设为 `TM::FORCE_ON`/`FORCE_OFF`（相关页说明二者不能与 `"..._UNGANGED"` 组合）。

## 和谁有关

- **文档事实** `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01_SPMU_PIN_TASK.htm`：父类；`mode()` 是它的成员函数，返回 `SPMU_PIN_TASK&` 以支持链式设置。
- **文档事实** `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.14_SPMU_PIN_TASK.iForce.htm`、`.../02.07.04.01.234.01.34_SPMU_PIN_TASK.vForce.htm`：这两个函数引用 `mode()`，且文档说明使用它们会自动设置 `"IFVM"`/`"VFIM"`。
- **文档事实** `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.01_SPMU_PIN_TASK.clamp.htm`：`clamp()` 的单位（V 或 A）取决于 `mode()`，且 `"CFVM"`/`"CFIM"` 要求用 `clamp()` 设置上下 clamp。
- **文档事实** `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.21_SPMU_PIN_TASK.max.htm`、`.../02.07.04.01.234.01.23_SPMU_PIN_TASK.min.htm`：单位随模式而变（VM 模式为 V，IM 模式为 A）；在 `"VFIM_UNGANGED"` 下还决定测量范围与临时 ungang 的通道数。
- **文档事实** `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.28_SPMU_PIN_TASK.relay.htm`：relay 动作取决于 `mode()` 与 `SPMU_TASK.execMode()="FORCE_ON"` 的组合；`"VM_HIZ"`/`"VM_HIZ_HAC"` 属 HIZ 模式。
- **文档事实** `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.04_SPMU_PIN_TASK.connectState.htm`：部分 connect state 要求先用 `mode()` 选电压测量模式（如 `"IFVM"`、`"VFVM"`、`"CFVM"`）。
- **文档事实** `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.22_SPMU_PIN_TASK.measFilter.htm`：该函数为 `mode()` 选定的测量模式设置 measure filter。
- **文档事实** `02_System_reference/02.05_Test_Head_Cards/02.05.05.01.07_DPS128___DPS64_in_PMU_operating_mode.htm`、`02_System_reference/02.05_Test_Head_Cards/02.05.05.03.05.02_XPS256_in_PMU_operating_mode.htm`：这些页面说明 `SPMU_TASK.execMode()` 的 `TM::FORCE_ON`/`FORCE_OFF` 不能与 `mode()` 的 `"..._UNGANGED"` 组合。
- **文档事实** `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.htm`、`.../02.05.05.03.10.08_XPS256_programming_-_Force_and_clamp_currents.htm`、`.../02.05.05.03.10.09_XPS256_programming_-_Force_and_clamp_voltages.htm`、`.../02.05.05.03.10.14_XPS256_programming_-_Measure_voltages.htm`、`.../02.05.05.03.10.19_XPS256_programming_-_Voltage_drop_measurement.htm`、`.../02.05.05.03.10.10_XPS256_programming_-_Ganging.htm`：XPS256 专属模式及 `execMode`/`mode()`/`connectState()` 组合的说明以本页为参照。
- **文档事实** `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.68_FLEX_RELAY.htm`：文档在本页明确推荐用 `FLEX_RELAY` 代替本函数做 Board ADC 测量。

## 版本

**文档事实** 本页 `Functional changes` 记录：
- Introduced before SmarTest 6.3.2
- SmarTest 7.2.3: Support of IFVM_UNGANGED parameter with 7.2.3.1
- SmarTest 7.4.0: New measurement modes added for AVI64.
- SmarTest 7.5.0: New measurement modes added for FVI16.
- SmarTest 7.10.1: New measurement modes added for XPS256.

**推断** 结合本页模式表，XPS256 新增的模式应指 `"VFVM"`、`"CFVM"`、`"CFIM"`；但 Functional changes 未逐一列出模式名。

## 出处

- `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.234.01.24_SPMU_PIN_TASK.mode.htm`（主源：语法、模式表、unganged 通道数规则、Example、Related information、Functional changes）。
- 关联判断另参考 `extract/edges.jsonl` 中指向本页的入边；本页语法节逐字取自同页，无语法子主题。
