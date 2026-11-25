---
type: object
title: SmartCalc framework
layer: L3
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

**文档事实** SmartCalc（SMC）是 SmarTest 的多线程框架：利用系统控制器的多核，把耗时的计算与测试数据上传移到独立的后台线程，这些“隐藏”线程尽可能与 SmarTest 前台进程并行，从而缩短测试时间（主页面正文）。

**文档事实** 框架目标（主页面原文列举）：易用、对测试代码与程序流影响最小；不同 site 的并行（多线程）计算；随多 site 自动伸缩；用 delayed binning 隐藏计算与数据上传；最小开销、最大 multi-site 效率；线程与 CPU core 自动分配。

**文档事实** SmartCalc 只工作在 Universal Test Method（UTM）框架内，并支持数字 capture 的隐藏（分段）上传。SMC API 属于 MAPI，`#include "mapi.hpp"` 后可用；宏 `SMC_VERSION` 标识 SmartCalc 版本（SmartCalc test program structure 页）。

**文档事实** SMC API 以共享库实现，加载共享库与解析动态引用会带来小延迟：典型小于 1 ms，但依文件系统与操作系统负载可能显著更高（SmartCalc implementation 页 Note）。

**文档事实** 多线程本身并不易用，需要大幅改动编码与测试流程；SmartCalc 的定位就是用高层 API 克服这一限制。框架使用多线程技术但不止于此，它隐藏了大部分内部线程处理（Multithreading considerations 页）。

**推断** 本页讲“为什么要有、整体怎么组织”，具体 API 调用方式属于 [[smartcalc]] 页；两页共用同一主源（见「出处」）。

## 典型用法

**文档事实** 四步实现：① 按并行执行组织测试程序，在 `FOR_EACH_SITE_BEGIN/END` 内调用 `SMC_ARM(...)`；② 把上传、计算与测试语句封装进名为 `SMC_backgroundProcessing()` 的 public 方法，其签名必须与对应 `SMC_ARM()` 完全一致，多个此类方法需要不同签名；③ 用 `SMC_SYNCHRONIZE()` 同步计算、执行 binning 与数据记录；④ 用 SMC API 做 hidden upload（可由 wrapper API 隐式触发，也可用 `SMC_BACKGROUND_ENABLE()` / `SMC_BACKGROUND_DISABLE()` 显式触发）（Four-step SmartCalc implementation）。

**文档事实** 后台过程有两种组织方式：“Thread per site”在 `ON_FIRST_INVOCATION` 块外 arm，推荐低 site 数；“Common thread”（单线程）在块内 arm，推荐高 site 数。前者每个 site 一个线程、线程内无需 site 循环；后者需用传入的 site 列表自行循环，且 `SMC_SITE_NUMBER()` 在 common thread 中不可用（SmartCalc "Thread per site" and "Common thread"）。

**文档事实** 三种 use model：Parallel multisite calculation、Hidden multisite calculation、Hidden upload and calculation（SmartCalc use models）。

**文档事实** 后台线程中只能使用线程安全的 API，例如 `SMC_...`、`DSP_...`、TESTSET 与 Wave 类 API；`SMC_backgroundProcessing()` 中调用的外部函数若抛出未知异常，会触发 SIGABRT 并终止测试方法进程，因此异常必须自行捕获并重新抛出（Thread safety、SmartCalc recommendations）。

**文档事实** 使用 multibin 才能让 `SMC_TEST()` 正确给 DUT 分 bin；binning 之后应运行特殊测试套件 bin_disconnect，用 `SMC_CLEANUP()` 或 `SMC_SYNCHRONIZE()` 终止 SmartCalc 线程（SmartCalc recommendations、Terminate SmartCalc threads after binning）。

**建议** 保持默认开启的线程安全自动检查（环境变量 `SMC_CONCURRENCY_CHECKING`，未定义时默认 `ErrorAndLog`）；文档称该检查不显著增加测试时间且强烈建议常开。

## 和谁有关

- **文档事实** Universal Test Method（UTM）：文档明确 SmartCalc 只工作在 UTM 内，每个 site 调用一次 `run()`，测试方法参数作为成员变量。
- **文档事实** SMC API reference（`02.07.04.01.231`）：API overview 页把详细 API 描述指向它，本框架的调用面都在那里。
- **文档事实** smartCalc 测试方法库（`02.07.05.06`）：主页面 Related information 列出；recommendations 还提到其中的 `SMC__SYNCHRONIZE_ALL`。
- **文档事实** Multi-Site Efficiency and Throughput（`03.14_Application_Papers/03.14.10.03`）：主页面 Related information 把它作为效率背景。
- **文档事实** [[test]]：API overview 说 `SMC_TEST()` 的语法与参数与 TEST 类似，并负责缓冲结果、延迟到 `SMC_SYNCHRONIZE()` 才写数据记录。
- **文档事实** `ON_FIRST_INVOCATION_BEGIN/END`：两种线程模型的 arm 位置由它界定，`SMC_SYNCHRONIZE()`、`SMC_CLEANUP()` 都要求在块外按 site 调用。
- **文档事实** DSP_ APIs、TESTSET、Wave：Thread safety 页把它们列为后台过程中允许的线程安全 API。
- **文档事实** bin_disconnect、multibin / `SET_MULTIBIN`：recommendations 要求用 bin_disconnect 正确终止 SMC，并说明 multibin 是正确分 bin 的前提。
- **文档事实** `RESULT_AREA_CONFIG`：hidden digital upload 需要 result area，result area 由该 API 定义。
- **文档事实** SmartRDI：Thread per site / Common thread 页的 Related information 指向 “Using SmartCalc (SMC) with SmartRDI”。
- **推断** [[smartcalc]]：与本页同源，本页讲框架背景与结构，另一页讲 API 调用侧；按 `extract/wiki-plan.csv` 的记录分工。

## 版本

**文档事实** 主页面 `Functional changes`：Introduced in SmarTest 6.5.3。

**文档事实** 子主题另有记录：SmartCalc test program structure 页 SmarTest 7.1.0 要求 Red Hat Enterprise Linux 5 update 6；Thread safety 页 SmarTest 7.1.4 使 Wave 类线程安全、SmarTest 7.5.3 新增线程安全 API 自动检查；SmartCalc "Thread per site" and "Common thread" 页记 Introduced in SmarTest 7.5.2。

## 出处

- 主源：`02_System_reference/02.07_Test_Method_Reference/02.07.10_SmartCalc_framework.htm`（框架定义、目标列举、Related information、Functional changes）。
- 子主题：`02.07.10.01`（multithreading basics）、`02.07.10.02`（considerations）、`02.07.10.02.01`（Thread per site 与 Common thread）、`02.07.10.02.02`（Thread safety）、`02.07.10.03`（use models）、`02.07.10.04`（implementation）、`02.07.10.04.01`（test program structure）、`02.07.10.04.02`（API overview）、`02.07.10.04.03`（Four-step implementation）、`02.07.10.04.11`（Disabling SmartCalc）、`02.07.10.04.12`（Terminate SmartCalc threads after binning）、`02.07.10.05`（recommendations）。
