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

（待补）

## 典型用法

（待补）

## 和谁有关

（待补）

## 版本

（待补）

## 出处

（待补）
