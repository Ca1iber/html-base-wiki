---
type: object
title: SmartCalc framework
layer: L2
stage: testmethod
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.10_SmartCalc_framework.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# SmartCalc framework

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **7,302 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.10_SmartCalc_framework.htm>` 及其子主题 `<02_System_reference/02.07_Test_Method_Reference/02.07.10.01_SmartCalc_multithreading_basics.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.10.04.04_Parallel_site_calculation.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.10.04.06_Hidden_calculation.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.10.04.07_Hidden_digital_upload_and_calculation.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.10.04.12_Terminate_SmartCalc_threads_after_binning.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.10.05_SmartCalc_recommendations.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 SmartCalc multithreading basics）

The following section shows a truncated output of the

/proc/cpuinfo
 of a XW4400 system
controller:

```
processor: 0
vendor_id: GenuineIntel
cpu family: 6
model: 15
model name: Intel(R) Core(TM)2 CPU 6700 @ 2.66GHz
stepping: 6
cpu MHz: 1596.000
cache size: 4096 KB
physical id: 0
siblings: 2
core id: 0
cpu cores: 2
....
processor: 1
vendor_id: GenuineIntel
cpu family: 6
model: 15
model name: Intel(R) Core(TM)2 CPU 6700 @ 2.66GHz
stepping: 6
cpu MHz: 1596.000
cache size: 4096 KB
physical id: 0
siblings: 2
core id: 1
cpu cores: 2
```

### Example（取自子主题 Parallel site calculation）

```
class runSNRtestMethod: public testmethod::TestMethod
{
private:

//
// Definition of member variables,
// can be accessed from all methods
// inside the class
//
DOUBLE snr[MAX_SITES], sPow[MAX_SITES], nPow[MAX_SITES];
ARRAY_D I_Capt[MAX_SITES];

protected:

virtual void run()
{
ON_FIRST_INVOCATION_BEGIN()

//
// Setup and execute your test as usual
//
DGT("pinDGT").enable();

SMC_EXECUTE_TEST( 1.0 );

//
// Upload data per site and start calculation
//
FOR_EACH_SITE_BEGIN()

//
// Upload waveform
//
INT site = CURRENT_SITE_NUMBER();
I_Capt[site] = DGT("pinDGT").getWaveform();

//
// Kick off calculation thread
SMC_ARM();

FOR_EACH_SITE_END()

ON_FIRST_INVOCATION_END()

//
// Wait until all calculations are done
//
SMC_SYNCHRONIZE();

INT site = CURRENT_SITE_NUMBER();

//
// Log all results
//
TEST("pinDGT","SNR", snr[site]);
TEST("pinDGT","signalPow", sPow[site]);
TEST("pinDGT","noisePow", nPow[site]);

} // virtual void run()

public:

void SMC_backgroundProcessing(void)
{
//
// Retrieve the thread specific site number from SmartCalc
//
INT site = SMC_SITE_NUMBER();

//
// Do your calculation
//
DSP_SNR(I_Capt[site],&snr[site],&sPow[site],&nPow[site], 1024, 1, 3, 0.0, 0);

} // void SMC_backgroundProcessing(void)

} // class runSNRtestMethod: public testmethod::TestMethod
```

### Example（取自子主题 Hidden calculation）

```
class sunSNRtestMethod: public testmethod::TestMethod
{
private:

ARRAY_D I_Capt[MS_MAX_SITES];

protected:

virtual void initialize()
{
addLimit("test_limit");
}

virtual void run()
{
ON_FIRST_INVOCATION_BEGIN();

//
// Setup and execute test as usual
//
DGT("pinDGT").enable();
...
SMC_EXECUTE_TEST(1.0);

LIMIT lim = GET_LIMIT_OBJECT("test_limit");

//
// Upload data per site and start calculation
//
FOR_EACH_SITE_BEGIN();

INT site = CURRENT_SITE_NUMBER();

//
// Upload waveform
//
I_Capt[site] = DGT("pinDGT").getWaveform();

//
// Kick off calculation thread
//
SMC_ARM(lim);

FOR_EACH_SITE_END();

ON_FIRST_INVOCATION_END();

} // virtual void run()

public:

void SMC_backgroundProcessing(LIMIT lim)
{
int hardBin;
int TestNumber;
string softBin;
DOUBLE snr;
DOUBLE sPow;
DOUBLE nPow;

int site = SMC_SITE_NUMBER();

//
// Do calculation
//
DSP_SNR(I_Capt[site],&snr,&sPow,&nPow, 1024, 1, 3, 0.0, 0);

//
// Do judgment using the syntax
//
// SMC_TEST(const STRING& pin, const STRING& testname, const LIMIT& limit,
// DOUBLE value, Boolean Continue = FALSE, INT testNumber = -1,
// const STRING& softbin= "", INT hardbin = -1);
...
...

//
//Assign bin (note: selected HW and SW bin must exist in the flow) and testnumber
//
hardBin = 5; softBin = "SNRTest"; TestNumber = 1000;

SMC_TEST("pinDGT","SNR", lim, snr,TM::CONTINUE, TestNumber,softBin,hardBin);

hardBin = 7; softBin = "SigPowTest"; TestNumber = 2000;

SMC_TEST("pinDGT","signalPow", lim, sPow,TM::CONTINUE, TestNumber,softBin,hardBin);

hardBin = 8; softBin = "NoisePowTest"; TestNumber = 3000;

SMC_TEST("pinDGT","noisePow", lim, nPow,TM::CONTINUE, TestNumber,softBin,hardBin);

} // void SMC_backgroundProcessing(LIMIT lim)

}; // class sunSNRtestMethod: public testmethod::TestMethod

class runDelayedBinLog: public testmethod::TestMethod
{
protected:

virtual void run()
{
//
// Wait until all calculations are done
//
SMC_SYNCHRONIZE();
...
...
}

}; // class runDelayedBinLog: public testmethod::TestMethod
```

For
handling of data within the
`SMC_backgroundProcessing()`（raw: `120107.htm#_120107__s_SMC_backgroundProcessing`）
 method,
refer to
`Passing data to the background process`（raw: `119876.htm#_119876__s_Passing_data_to_the_background_process`）
 in
`SmartCalc recommendations`（raw: `119876.htm`）
.

### Example（取自子主题 Hidden digital upload and calculation）

```
class runSNRtestMethod: public testmethod::TestMethod
{
protected:
virtual void initialize()
{
addLimit("test_limit");
}
virtual void run()
{
ON_FIRST_INVOCATION_BEGIN()
// digital capture setup for hidden upload
RESULT_AREA_CONFIG resConf("pin1"); //capture pin
resConf.appendArea("1kBitArea", 3072).activate();

// setup and execute your test as usual, but use the SMC_xxx API
...
SMC_DIGITAL_CAPTURE_TEST("1kBitArea");
LIMIT lim = GET_LIMIT_OBJECT("test_limit");

FOR_EACH_SITE_BEGIN()
// kick off calculation thread
SMC_ARM("1kBitArea", lim);
FOR_EACH_SITE_END();
ON_FIRST_INVOCATION_END();
}

public:
void SMC_backgroundProcessing(STRING area, LIMIT lim)
{
// trigger upload when SMC wrappers indicate non-blocking action
// a reference to the captured data is copied here, as we
// do not access the data outside this function
// (or after SMC_SYNCHRONIZE())
const ARRAY_I& data = SMC_GET_VECTORS("VectorVariable", area);

// do your calculation
DSP_SNR(data,&snr,&sPow,&nPow, 1024, 1, 3, 0.0, 0);

// do judgment
SMC_TEST("pinDGT","SNR", lim, snr,,"55");
SMC_TEST("pinDGT","signalPow", lim, sPow,,"57");
SMC_TEST("pinDGT","noisePow", lim, nPow,,"59");
}
(...)
}

class runDelayedBinLog: public testmethod::TestMethod
{
protected:
virtual void run()
{
// wait until all calculations are done
SMC_SYNCHRONIZE();
(...)
}
}
```

### Example（取自子主题 Terminate SmartCalc threads after binning）

The following example code was created by following the description of
`Using the special test suite bin_disconnect`（raw: `113351.htm`）
 and has been adapted for SmartCalc. It is
valid for both thread per site and common thread (see
`SmartCalc "Thread per site" and "Common thread"`（raw: `347204.htm`）
).

```
virtual void run()
{
...// example of a customized disconnect
ARRAY_I enabledSites;
INT numEnabledSites;
INT hwBinNumber, goodBin, reprobe, overon, otherwiseBin;
STRING hwBinDescription, swBinDesciption, swBinNumber;

const string nonshareddisconnect="ACMD \"CNCT\",\"OFF\",(@NONSHARED@); \
FLSH MUX;WSDN;DLSO(@NONSHARED@); \
CNCT OFF,(@NONSHARED@);CHRS OFF; \
BCMD \"\",ACTION,\"Update\",; \
PSST OFF;RLYC IDLE,OFF,(@NONSHARED@);";
const string finaldisconnect ="ACMD \"CNCT\",\"OFF\",(@);FLSH MUX;WSDN; \
SQST OFF;CNCT OFF,(@);CHRS OFF; \
BCMD \"\",ACTION,\"Update\",; \
PSST OFF;RLYC IDLE,OFF,(@);";

numEnabledSites = GET_ENABLED_SITES(enabledSites);

SMC_CLEANUP(false); // kills running thread only

if (numEnabledSites == 0)
{
FW_TASK(finaldisconnect); //last enabled site to be disconnected
}
else
{
//not the last site to be disconnected
//only disconnect current site and keep shared resources connected
FW_TASK(nonshareddisconnect);
}

return;
}
```

This example works regardless of the used pin
`Mode contexts`（raw: `10633.htm`）
.

### Example（取自子主题 SmartCalc recommendations）

### Exception handling

The following example shows how a customized
exception handling can be coded in the
`SMC_backgroundProcessing()`（raw: `120107.htm#_120107__s_SMC_backgroundProcessing`）
 method using

catch()
.

```
void SMC_backgroundProcessing()
{
...
try
{
...
call my_function_that_throws();
...
}
catch(myException& e)
{
//
// Always catch user-defined exceptions
// and do what is needed in this specific error.
...
}
...
}

class myException {};

void my_function_that_throws()
{
if (...)
{
throw myException();
}
}
```

<!-- 语法节 end -->

## 是什么

**文档事实** 本页从调用侧看 SmartCalc（SMC）：它是一组高层 API，封装内部线程处理，让测试方法把计算与数据上传放进后台线程 `SMC_backgroundProcessing()` 中执行（Multithreading considerations、API overview）。

**文档事实** SMC API 属于 MAPI，`#include "mapi.hpp"` 后可用；宏 `SMC_VERSION` 标识 SmartCalc 版本；API 以共享库实现（test program structure、implementation）。

**文档事实** 核心调用链是 `SMC_ARM()` → `SMC_backgroundProcessing()` → `SMC_SYNCHRONIZE()`：`SMC_ARM()` 为 `SMC_backgroundProcessing()` 装载最多 8 个任意类型参数并自动启动计算线程；`SMC_SYNCHRONIZE()` 等待所有计算线程结束或按超时终止它们、执行其测试语句并做内部清理（API overview）。

**文档事实** `SMC_SYNCHRONIZE()` 必须按 site 调用，因此要放在 `ON_FIRST_INVOCATION_BEGIN/END()` 块外；timeout 必须 ≥ 0，等于 0 表示无限等待；计算被中止或发生 invocation error 时返回 FALSE，返回值与测试语句结果无关（API overview）。

## 典型用法

**文档事实** 在 `run()` 中用 `SMC_ARM(...)` arm；在 `SMC_backgroundProcessing()` 中用 `SMC_SITE_NUMBER()` 取本线程的 site（common thread 不可用），用 `SMC_GET_VECTORS()`、`SMC_GET_WAVEFORM()`、`SMC_GET_COMPLEX_WAVEFORM()` 做 hidden upload，用 `SMC_TEST()` 记录判定（API overview、Four-step implementation）。

**文档事实** `SMC_TEST()` 的语法与参数与 TEST 类似，结果先缓冲，直到 `SMC_SYNCHRONIZE()` 才写数据记录；common thread 下必须用带 site 的扩展版本 `SMC_TEST(INT site, const STRING& pin, ...)`（API overview、Thread per site / Common thread）。

**文档事实** wrapper API 与其非 SMC 对应：`SMC_EXECUTE_TEST`/`EXECUTE_TEST`、`SMC_FUNCTIONAL_TEST`/`FUNCTIONAL_TEST`、`SMC_WAIT_TIME`/`WAIT_TIME`、`SMC_WAIT_TEST_DONE`/`WAIT_TEST_DONE`、`SMC_DIGITAL_CAPTURE_TEST`/`DIGITAL_CAPTURE_TEST`、`SMC_NB_DIGITAL_CAPTURE_END`/`NB_DIGITAL_CAPTURE_END`；hidden upload 可由这些 wrapper 隐式触发（API overview）。

**文档事实** 显式控制 hidden upload 用 `SMC_BACKGROUND_ENABLE()` / `SMC_BACKGROUND_DISABLE()`；enable 期间不得执行任何需要与 tester 或 FW 通信的命令，结束时必须调用 disable（API overview）。

**文档事实** arm 方式按 site 数选择：低 site 数用 thread per site（`SMC_ARM()`、`SMC_ARM_OTHER_TS()`，在 `ON_FIRST_INVOCATION` 块外）；高 site 数用 common thread（另加 `SMC_ARM_FOR_SITES()`、`SMC_ARM_OTHER_TS_FOR_SITES()`，在块内）。`SMC_ARM()`/`SMC_ARM_OTHER_TS()` 处理所有 active site；带 `_FOR_SITES` 的版本由必填参数 `sites` 指定 site 列表（Thread per site / Common thread）。

**文档事实** 不同 use model 混用时，用块内的 `SMC_SYNCHRONIZE_WITHOUT_BINNING(0,true)` 等待所有线程结束，再用块外的 `SMC_SYNCHRONIZE()` 执行排队的 `SMC_TEST()` 语句完成数据记录与 binning（SmartCalc recommendations）。

**文档事实** 需要强制串行时可把代码包在 `SMC_SERIAL_EXECUTION_BEGIN()` / `SMC_SERIAL_EXECUTION_END()` 之间；`SMC_DISABLE(TRUE)` 会关闭多线程与 hidden upload 等 SMC 特性，但 `SMC_TEST()` 语句仍会在 `SMC_SYNCHRONIZE()` 时求值（Disabling SmartCalc）。

**文档事实** TMLimits 在 SMC 下的规则：`getLimit()`、`getLimitRef()`、`getLimitObj()` 是线程安全的；必须在调用 `SMC_ARM()` 前把 TMLimits 表载入内存；armed 或 running 期间不得更改或重载 TMLimits 表（SmartCalc recommendations）。

**文档事实** `SMC_CLEANUP()` 中止多线程执行：等待计算线程结束或以 10 ms 超时终止，并做内部清理；它只作用于 active site，因此也须在 `ON_FIRST_INVOCATION` 块外调用（API overview）。

**文档事实** `SMC_EXECUTE_DEBUG_ACTION()` 可执行 SmartCalc 调试动作，提供 hidden upload 利用率统计，用于 test flow 性能优化（API overview）。

**建议** 需要观测 hidden upload 是否真正并行时，可先用 `SMC_EXECUTE_DEBUG_ACTION()` 的统计定位，再调整 arm 方式与数据传递（避免按值传大结构、避免静态变量）。

## 和谁有关

- **文档事实** SMC API reference（`02.07.04.01.231`）：API overview 明确把逐个 API 的详细说明指向它。
- **文档事实** [[smartcalc-framework]]：同源主页面，讲框架背景与结构；本页讲调用侧（API overview、Four-step implementation 的调用内容）。
- **文档事实** [[test]]：`SMC_TEST()` 的语法与参数与 TEST 类似，且负责缓冲结果、延迟到 `SMC_SYNCHRONIZE()` 写数据记录。
- **文档事实** `ON_FIRST_INVOCATION_BEGIN/END`：thread per site / common thread 的 arm 位置由它界定，`SMC_SYNCHRONIZE()` 与 `SMC_CLEANUP()` 须在块外调用。
- **文档事实** DSP_ APIs、TESTSET、Wave：Thread safety 页规定 `SMC_backgroundProcessing()` 只能包含这些线程安全 API。
- **文档事实** SET_MULTIBIN / multibin：recommendations 要求用 multibin 才能让 `SMC_TEST()` 正确分 bin。
- **文档事实** `SMC__SYNCHRONIZE_ALL`（smartCalc 测试方法库 `02.07.05.06.02`）：recommendations 的“任意 use model 同步”把它列为参考实现。
- **文档事实** `setStopSiteLoop()`：common thread 用它让 `run()` 只执行一次以缩短测试时间。
- **文档事实** TMLimits：SMC 内使用 TMLimits 的线程安全与加载顺序由 recommendations 规定。
- **文档事实** `RESULT_AREA_CONFIG`：hidden digital upload 需要 result area；示例用 `resConf.appendArea(...).activate()` 配置。
- **文档事实** `GET_LIMIT_OBJECT`：hidden calculation 示例用它取得 `LIMIT` 对象后传给 `SMC_ARM()`。

## 版本

**文档事实** 主页面 `Functional changes`：Introduced in SmarTest 6.5.3。API overview、Four-step implementation、recommendations 等子主题同样记为 Introduced in SmarTest 6.5.3。

**文档事实** 相关子主题记录的后续变化：Thread safety 页 SmarTest 7.1.4 使 Wave 类线程安全、SmarTest 7.5.3 新增线程安全 API 自动检查；SmartCalc "Thread per site" and "Common thread" 页记 Introduced in SmarTest 7.5.2。

## 出处

- 主源：`02_System_reference/02.07_Test_Method_Reference/02.07.10_SmartCalc_framework.htm`（框架定位、Related information、Functional changes）。
- 调用侧细节：`02.07.10.04.02_SmartCalc_API_overview.htm`（API 清单与语义）、`02.07.10.04.03_Four-step_SmartCalc_implementation.htm`（四步）、`02.07.10.05_SmartCalc_recommendations.htm`（同步、TMLimits、multibin）、`02.07.10.02.01_SmartCalc__Thread_per_site__and__Common_thread.htm`（两种线程模型）、`02.07.10.02.02_Thread_safety.htm`（线程安全）、`02.07.10.04.11_Disabling_SmartCalc.htm`（禁用与强制串行）、`02.07.10.04.01_SmartCalc_test_program_structure.htm`（MAPI 与 `SMC_VERSION`）。
