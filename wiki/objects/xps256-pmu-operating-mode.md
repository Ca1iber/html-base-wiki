---
type: object
title: XPS256 programming - PMU operating mode
layer: L2
stage: level
tags: []
related: []
sources:
  - 02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# XPS256 programming - PMU operating mode

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **6,433 字符逐字取自** `<02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Examples

### Examples

The following examples demonstrate how to set up an XPS256 pin for a standard current
measurement.

The three examples are set up in a three-step sequence of connecting the pin and
applying the basic setup, measuring the requested parameter, and disconnecting in a
separate task. This sequence is suitable for XPS256-specific tests, since very often
more than one setup has to be applied and more than one measurement has to be
carried out before the pin is disconnected again.

These examples are available in the following sections:

`Example 1: SmartRDI, pattern‑based programming`（raw: `354253.htm#_354253__e_SRDI_pattern-based`）

Pattern‑based
programming using SmartRDI is the recommended solution that requires
the least amount of code and on the other hand delivers the most stable
result in terms of timing.

`Example 2: SmartRDI, code‑based programming`（raw: `354253.htm#_354253__e_SRDI_code-based`）

Code‑based programming
using SmartRDI needs some more code and must follow the structure of
the wrapped test method APIs.

`Example 3: Test method API SPMU_TASK`（raw: `354253.htm#_354253__e_TM_API_based`）

This example is based on the test
method APIs and is strongly tied to the structure of the underlying
commands.

The code of the three examples generates the same measurement sequence for the
programmed pin. If you use the
`Trace Function`（raw: `10408.htm`）
 to compare
the code‑based SmartRDI example and the example based on the test method
APIs, you will get the same output in the
MCDLog
 file.

### Example 1: SmartRDI, pattern‑based programming

The example uses a code‑based
`RDI command`（raw: `142604.htm#_142604__dle_RDI_command`）
 to setup
and connect the XPS256 pin. The following
`RDI block`（raw: `142604.htm#_142604__dle_RDI_block`）

performs a pattern‑based measurement. The last RDI command disconnects the
XPS256 pin in code‑based mode.

Since the RDI block uses a specialized
`DC event`（raw: `345840.htm`）
 to
perform the measurement, only the measurement related parameters must be defined. In
contrast, for code‑based programming with SmartRDI or programming with test
method APIs, all parameters must be specified also for the measurement.

```
RDI_INIT();

ON_FIRST_INVOCATION_BEGIN();
{
rdi.dc().pin("XPS256_PMU_1")
.vForce ( 5.0 V) .vForceRange(7.0 V).preCharge(0.0 V)
.iClamp (-5.0 mA, 50.0 mA).iForceRange(0.1 A)
.execute ();

RDI_BEGIN();
{
rdi.dc("iMeasXPS256").pin("XPS256_PMU_1")
.iMeas ()
.average (16)
.measWait (2.5 ms)
.execute ();
}
RDI_END();

rdi.dc().pin("XPS256_PMU_1").disconnect().execute();
}
ON_FIRST_INVOCATION_END();

double resultIMeasXPS256;

resultIMeasXPS256 = rdi.id("iMeasXPS256").getValue("XPS256_PMU_1");
```

### Example 2: SmartRDI, code‑based programming

The first
`RDI command`（raw: `142604.htm#_142604__dle_RDI_command`）
 connects and sets the XPS256 pin:
DC Scale pins in PMU operating mode are automatically connected if
`iForce()`（raw: `143892.htm`）
 or
`vForce()`（raw: `143895.htm`）
 are used within the RDI command.
For more information, see also
`Setting up DC Scale pins with SmartRDI`（raw: `141515.htm`）
.

The second RDI command contains a measurement
iMeas()
. The
programmed pin remains connected after the measurement.

The third RDI command contains no measurement but the
disconnect()

function: Output relays are controlled again and the pin is disconnected.

In this example, SmartRDI is mainly a wrapper for the test method API
`SPMU_TASK`（raw: `55670.htm`）
. The structure is therefore tied to the SPMU_TASK and to the
corresponding low level commands as mentioned in
`Example 3: Test method API SPMU_TASK`（raw: `354253.htm#_354253__e_TM_API_based`）
 below.

```
RDI_INIT();

ON_FIRST_INVOCATION_BEGIN();
{
rdi.dc().pin("XPS256_PMU_1")
.vForce ( 0.0 V) .vForceRange(7.0 V).preCharge(0.0 V)
.iClamp (-5.0 mA, 50.0 mA).iForceRange(0.1 A)
.execute ();

rdi.dc("iMeasXPS256").pin("XPS256_PMU_1")
.vForce ( 5.0 V) .vForceRange(7.0 V)
.iClamp (-5.0 mA, 50.0 mA).iForceRange(0.1 A)
.iMeas ()
.average (16)
.measWait (2.5 ms)
.execute ();

rdi.dc().pin("XPS256_PMU_1").disconnect().execute();
}
ON_FIRST_INVOCATION_END();

double resultIMeasXPS256;

resultIMeasXPS256 = rdi.id("iMeasXPS256").getValue("XPS256_PMU_1");
```

### Example 3: Test method API SPMU_TASK

XPS256 measurements, created by the test method API
`SPMU_TASK`（raw: `55670.htm`）
 are based
on the low-level commands
`DCCH`（raw: `98518.htm`）
 and
`DCVH`（raw: `98530.htm`）
 in combination with
`DCEX`（raw: `98521.htm`）
. These
commands define complete measurement sequences including connecting and
disconnecting the programmed pins.

The tasks
spmuTask_connect
 as well as

spmuTask_measure
 of the example must therefore define the
same
mode()
 and
connectState()
 and ensure that
the same ranges are used, although the first task is used only to connect and
activate the pin while the second task is used only for the measuring:

spmuTask_connect
: The combination of

relay("NT")
 and
execMode(TM::FORCE_ON)

of the connect task enables switching of the output relays and activation of
the pin. A measurement is not supported by this task.

spmuTask_measure
: Relay control is set to

"NO"
 to inhibit actions of the output relays. The pin
remains therefore connected after the task has been performed.

execMode(TM::PVAL)
 causes that the requested value is
measured and returned as per pin value and pass/fail results.

spmuTask_disconnect
: The combination of

relay("NT")
 and

execMode(TM::FORCE_OFF)
 causes that the pin is
disconnected. Although no more measurements are performed, some parameters
such as
min()
 and
max()
 must be defined
for a valid setup.

```
SPMU_TASK spmuTask_connect;
SPMU_TASK spmuTask_measure;
SPMU_TASK spmuTask_disconnect;

ON_FIRST_INVOCATION_BEGIN();
{
spmuTask_connect.pin("XPS256_PMU_1")
.mode ("VFIM")
.vForce ( 0.0 V) .vForceRange(7.0 V).preCharge(0.0 V)
.clamp (-5.0 mA, 50.0 mA).iForceRange(0.1 A)
.min (-5.0 mA)
.max (50.0 mA)
.relay ("NT");

spmuTask_measure.pin("XPS256_PMU_1")
.mode ("VFIM")
.vForce ( 5.0 V) .vForceRange(7.0 V)
.clamp (-5.0 mA, 50.0 mA).iForceRange(0.1 A)
.min (-5.0 mA)
.max (50.0 mA)
.relay ("NO")
.settling (2.5 ms)
.samples (16);

spmuTask_disconnect.pin("XPS256_PMU_1")
.vForce ( 0.0 V)
.min ( 0.0 mA)
.max (10.0 uA)
.relay ("NT");

spmuTask_connect .execMode(TM::FORCE_ON) .execute();
spmuTask_measure .execMode(TM::PVAL) .execute();
spmuTask_disconnect.execMode(TM::FORCE_OFF).execute();
}
ON_FIRST_INVOCATION_END();

double resultIMeasXPS256;

resultIMeasXPS256 = spmuTask_measure.getValue("XPS256_PMU_1");
```

<!-- 语法节 end -->

## 是什么

**文档事实** 在 PMU operating mode 下，一个 XPS256 pin 被当作标准 PMU 使用，在单个 test suite 或一组 test suite 执行期间临时供电；pin 在 Digital Pins editor 中定义为 dc 类型（Type = dc、Mode = SIG）即处于该模式。
**文档事实** 本页覆盖 Pin definition、Hardware view、SmartRDI overview、API overview、Relay switching、Supported measurement modes：完整设置功能由 SmartRDI 的 `dc()` API 提供（code-based 与 pattern-based 均支持）；test method API 侧由 `SPMU_TASK` 与 `SPMU_PIN_TASK` 覆盖；pattern-based 的 setup 与测量由 DC events 支持。

## 典型用法

**文档事实** 文档三例完成同一测量序列——连接 / 设置 pin、测量、单独断开：Example 1 用 SmartRDI pattern-based（文档称其为代码最少、timing 最稳定的推荐方案），Example 2 用 SmartRDI code-based，Example 3 直接用 `SPMU_TASK`（基于低层 `DCCH` / `DCVH` 配合 `DCEX`）。
**文档事实** `SPMU_PIN_TASK.mode()` 支持 VFVM、VFIM、VFIM_UNGANGED、CFVM、CFIM、IFVM、IFVM_UNGANGED、VM_HIZ；`relay()` 在 DC Scale 卡上支持 NO / NT（不支持 NTMBB / NTBBM / TERM）；`SPMU_TASK.execMode()` 的 `TM::FORCE_ON` / `TM::FORCE_OFF` 用于连接 / 断开，但不能与 mode 设为 `..._UNGANGED` 组合。
**文档事实** PMU operating mode 下自动降档（automatic down-ranging）仅 pattern-based（DC events 或 SmartRDI）支持，code-based 编程不支持。**建议** 优先采用文档推荐的 pattern-based SmartRDI 方案。

## 和谁有关

- SmartRDI `dc()`：覆盖 PMU operating mode 下 XPS256 通道的完整设置与测量（源文明确）。
- SPMU_TASK / SPMU_PIN_TASK：API overview 指定的完整功能 API；本页引用 `SPMU_PIN_TASK.relay()`、`mode()`、`preCharge()`、`iMeasureRange()` 及 `SPMU_TASK.execMode()`。
- DC events：为本页所述 pattern-based setup 与测量提供支持。
- Digital Pins editor：把 pin 定义为 dc 类型即进入 PMU operating mode。
- XPS256 operating modes / XPS256 programming - DPS operating mode / XPS256 in PMU operating mode：Related information 互链；`XPS256 in PMU operating mode` 明确把细节指向本页。
- XPS256 Measure currents / Measure voltages / Force and clamp currents / Force and clamp voltages：这些页把 PMU operating mode 下的功能指向 SPMU_TASK 与 SPMU_PIN_TASK（入边）。
- 低层命令 DCCH / DCVH / DCEX：Example 3 说明 SPMU_TASK 测量基于它们。

## 版本

**文档事实** Functional changes 记为 "Introduced in SmarTest 7.10.1"。

## 出处

- `02_System_reference/02.05_Test_Head_Cards/02.05.05.03.10.15_XPS256_programming_-_PMU_operating_mode.htm`。
