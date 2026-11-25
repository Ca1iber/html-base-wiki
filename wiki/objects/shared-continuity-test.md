---
type: object
title: SHARED_CONTINUITY_TEST
layer: n/a
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.21_SHARED_CONTINUITY_TEST.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# SHARED_CONTINUITY_TEST

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **21,449 字符逐字取自** `<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.21_SHARED_CONTINUITY_TEST.htm>` 及其子主题 `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.41_DISCONNECT.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.02_FOR_EACH_SHARED_SITE_BEGIN.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.03_FOR_EACH_SHARED_SITE_END.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.04_FOR_EACH_TEST_BEGIN.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.05_FOR_EACH_TEST_BEGIN_WITH_RESET.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.06_FOR_EACH_TEST_END.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.10.01_MTP_CONTINUITY_PIN_TASK.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.10.02_MTP_CONTINUITY_TASK.pin.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.10.03_MTP_CONTINUITY_TASK.settlingTime.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.10.04_MTP_CONTINUITY_TASK.execute.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.10.05_MTP_CONTINUITY_TASK.postExecute.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.10.06_MTP_CONTINUITY_TASK.getPassFail.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.10.07_MTP_CONTINUITY_TASK.getValue.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.10_MTP_CONTINUITY_TASK.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.21.01_SHARED_CONTINUITY_TEST.init.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.21.02_SHARED_CONTINUITY_TEST.sharingConfigFile.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.21.03_SHARED_CONTINUITY_TEST.pinShared.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.21.04_SHARED_CONTINUITY_TEST.forceVoltage.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.21.05_SHARED_CONTINUITY_TEST.pinNonShared.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.21.06_SHARED_CONTINUITY_TEST.forceCurrentNonShared.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.21.07_SHARED_CONTINUITY_TEST.pinCross.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.21.08_SHARED_CONTINUITY_TEST.forceCurrentCross.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.21.09_SHARED_CONTINUITY_TEST.terminationDPS.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.21.10_SHARED_CONTINUITY_TEST.supplyDPS.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.21.11_SHARED_CONTINUITY_TEST.settlingTime.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.21.12_SHARED_CONTINUITY_TEST.output.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.21.13_SHARED_CONTINUITY_TEST.execute.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.21.14_SHARED_CONTINUITY_TEST.judgeAndLog.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.21.15_SHARED_CONTINUITY_TEST__.print.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.21.16_SHARED_CONTINUITY_TEST.getPassFail.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.21.17_SHARED_CONTINUITY_TEST.getValue.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Class definition

### Constructor
```
SHARED_CONTINUITY_TEST ();
```

### Member functions

Initial function:

`SHARED_CONTINUITY_TEST & init ()`（raw: `129157.htm`）

Setup functions:

`SHARED_CONTINUITY_TEST & sharingConfigFile (const string &filename)`（raw: `129158.htm`）

`SHARED_CONTINUITY_TEST & pinShared (const string &pinlist)`（raw: `129159.htm`）

`SHARED_CONTINUITY_TEST & forceVoltage (double voltage)`（raw: `129160.htm`）

`SHARED_CONTINUITY_TEST & pinNonShared (const string &pinlist)`（raw: `129161.htm`）

`SHARED_CONTINUITY_TEST & forceCurrentNonShared (double current)`（raw: `129162.htm`）

`SHARED_CONTINUITY_TEST & pinCross (const string &pinlist)`（raw: `129163.htm`）

`SHARED_CONTINUITY_TEST & forceCurrentCross (double current)`（raw: `129164.htm`）

`SHARED_CONTINUITY_TEST & terminationDPS (const string &dps)`（raw: `129168.htm`）

`SHARED_CONTINUITY_TEST & supplyDPS (const string &dps)`（raw: `129169.htm`）

`SHARED_CONTINUITY_TEST & settlingTime (double time)`（raw: `129170.htm`）

`SHARED_CONTINUITY_TEST & output (MTP::OUTPUT_TYPE output)`（raw: `129171.htm`）

Execute function:

`void execute ()`（raw: `129172.htm`）

Result functions:

`void judgeAndLog () const`（raw: `129173.htm`）

`void print (const ostream &out=std::cout) const`（raw: `129174.htm`）

`bool getPassFail (void) const`（raw: `129176.htm`）

`bool getPassFail (const string &pin) const`（raw: `129176.htm`）

`double getValue (const string &pin) const`（raw: `129180.htm`）

### Examples

### Note

The following examples demonstrate how to use this API within a
test method. If you want to see a complete test method code via SHARED_CONTNUITY_TEST, find it
in

/opt/93000mts/mts/solution_tools/common/sh_lib/DriverSharing.tar.gz
.

### Example 1

Performing the continuity and short circuits test for the
shared, and non-shared
pins.

```
#include "solution_tools.h"
#include "testmethod.hpp"
#include "mapi.hpp"

class CSharedContinuity: public testmethod::TestMethod
{
protected:
virtual void run()
{
ON_FIRST_INVOCATION_BEGIN();
{
// Always do initialization at the beginning of test
mTest.init();

// hand over the parameters to the test class
mTest.pinNonShared("DQ_Bus,DQS_DiffBus,DM")
.forceCurrentNonShared(100 uA)
.pinCross("Clock_Bus")
.forceCurrentCross(100 uA)
.sharingConfigFile("default.cfg")
.pinShared("Addr_Bus,Command_Bus")
.forceVoltage(1.1)
.terminationDPS("VTERM")
.supplyDPS("VDD,VDDQ")
.settlingTime(0)
.output(MTP::OUTPUT_REPORT_UI);

// execute the test
mTest.execute();
}
ON_FIRST_INVOCATION_END();

// set result
mTest.judgeAndLog();

// Print out in the UI Report Window.
mTest.print();
}

private:
SHARED_CONTINUITY_TEST mTest;
};
```

### Example 2

Customizing the
output.

```
#include "solution_tools.h"
#include "testmethod.hpp"
#include "mapi.hpp"

class CSharedContinuity: public testmethod::TestMethod
{
protected:
virtual void run()
{
ON_FIRST_INVOCATION_BEGIN();
{
// Always do initialization at the beginning of test
mTest.init();

// hand over the parameters to the test class
mTest.pinNonShared("DQ_Bus,DQS_DiffBus,DM")
.forceCurrentNonShared(100 uA)
.pinCross("Clock_Bus")
.forceCurrentCross(100 uA)
.sharingConfigFile("default.cfg")
.pinShared("Addr_Bus,Command_Bus")
.forceVoltage(1.1)
.terminationDPS("VTERM")
.supplyDPS("VDD,VDDQ")
.settlingTime(0)
.output(MTP::OUTPUT_REPORT_UI);

// execute the test
mTest.execute();
}
ON_FIRST_INVOCATION_END();

// set result
mTest.judgeAndLog();

// Print out in the UI Report Window.
STRING_VECTOR pinSharedNames =
PinUtility.getDigitalPinNamesFromPinList("Addr_Bus,Command_Bus", TM::ALL_DIGITAL, TRUE);
STRING_VECTOR pinNonSharedNames =
PinUtility.getDigitalPinNamesFromPinList("DQ_Bus,DQS_DiffBus,DM", TM::ALL_DIGITAL, TRUE);
STRING_VECTOR pinCrossNames =
PinUtility.getDigitalPinNamesFromPinList("Clock_Bus", TM::ALL_DIGITAL, TRUE);

cout << "Test result of site " << CURRENT_SITE_NUMBER() << ": " << mTest.getPassFail() << endl;

for (STRING_VECTOR::const_iterator it = pinSharedNames.begin();
it != pinSharedNames.end(); ++it)
{
cout << "PIN (" << *it << ")\t" << mTest.getPassFail(*it) << "\t" << mTest.getValue(*it) << endl;
}

for (STRING_VECTOR::const_iterator it = pinNonSharedNames.begin();
it != pinNonSharedNames.end(); ++it)
{
cout << "PIN (" << *it << ")\t" << mTest.getPassFail(*it) << "\t" << mTest.getValue(*it) << endl;
}

for (STRING_VECTOR::const_iterator it = pinCrossNames.begin();
it != pinCrossNames.end(); ++it)
{
cout << "PIN (" << *it << ")\t" << mTest.getPassFail(*it) << "\t" << mTest.getValue(*it) << endl;
}
}

private:
SHARED_CONTINUITY_TEST mTest;
};
```

### Syntax（取自子主题 SHARED_CONTINUITY_TEST.init()）

```
SHARED_CONTINUITY_TEST& init()
```

### Syntax（取自子主题 SHARED_CONTINUITY_TEST.sharingConfigFile()）

```
SHARED_CONTINUTIY_TEST& sharingConfigFile(const string& filename)
```
[表]
列: Parameter | Description
行 1:
  filename
  Name of the driver sharing configuration file used.
    
    This file should be in <device
    directory>/configuration/.

### Example（取自子主题 SHARED_CONTINUITY_TEST.sharingConfigFile()）

```
SHARED_CONTINUITY_TEST mTest;
mTest.sharingConfigFile("default.cfg");
```

### Syntax（取自子主题 SHARED_CONTINUITY_TEST.pinShared()）

```
SHARED_CONTINUITY_TEST& pinShared(const string& pinlist)
```
[表]
列: Parameter | Description
行 1:
  pinlist
  The list of the shared pins or pin groups to be measured.
    
    Separate entries with commas.

### Example（取自子主题 SHARED_CONTINUITY_TEST.pinShared()）

```
SHARED_CONTINUITY_TEST mTEST;
mTEST.pinShared("Addr_Bus");
mTEST.pinShared("Addr_Bus,Command_Bus");
```

### Syntax（取自子主题 SHARED_CONTINUITY_TEST.forceVoltage()）

```
SHARED_CONTINUITY_TEST& forceVoltage(double voltage)
```
[表]
列: Parameter | Description
行 1:
  voltage
  The force voltage to be applied on the termination DPS.
    
    The unit is V.
    
    The default voltage value is 1 V.

### Example（取自子主题 SHARED_CONTINUITY_TEST.forceVoltage()）

```
SHARED_CONTINUITY_TEST mTest;
mTest.forceVoltage(1.3);
mTest.forceVoltage(1300 mV);
```

### Syntax（取自子主题 SHARED_CONTINUITY_TEST.pinNonShared()）

```
SHARED_CONTINUITY_TEST& pinNonShared(const string& pinlist)
```
[表]
列: Parameter | Description
行 1:
  pinlist
  The list of the non-shared pins, pin groups that are to be measured.
    
    Separate entries with commas.

### Example（取自子主题 SHARED_CONTINUITY_TEST.pinNonShared()）

```
SHARED_CONTINUITY_TEST mTEST;
mTEST.pinNonShared("DQ_Bus");
mTEST.pinNonShared("DQ_Bus,DM");
```

### Syntax（取自子主题 SHARED_CONTINUITY_TEST.forceCurrentNonShared()）

```
SHARED_CONTINUITY_TEST& forceCurrentNonShared(double current)
```
[表]
列: Parameter | Description
行 1:
  current
  The current to be forced into the non-shared pins.
    
    The unit is A.
    
    The default current value is 1 A.

### Example（取自子主题 SHARED_CONTINUITY_TEST.forceCurrentNonShared()）

```
SHARED_CONTINUITY_TEST mTest;
mTest.forceCurrentNonShared(100 uA);
mTest.forceCurrentNonShared(0.0001);
```

### Syntax（取自子主题 SHARED_CONTINUITY_TEST.pinCross()）

```
SHARED_CONTINUITY_TEST& pinCross(const string& pinlist)
```
[表]
列: Parameter | Description
行 1:
  pinlist
  The list of the cross-terminated pins, pin groups to be measured.
    
    Separate entries with commas.

### Example（取自子主题 SHARED_CONTINUITY_TEST.pinCross()）

```
SHARED_CONTINUITY_TEST mTEST;
mTEST.pinCross("Clock_Bus");
mTEST.pinCross("Clock_Bus1,Clock_Bus2");
```

### Syntax（取自子主题 SHARED_CONTINUITY_TEST.forceCurrentCross()）

```
SHARED_CONTINUITY_TEST& forceCurrentCross(double current)
```
[表]
列: Parameter | Description
行 1:
  current
  The current to be forced into the cross-terminated pins.
    
    The unit is A.
    
    The default current value is 1 A.

### Example（取自子主题 SHARED_CONTINUITY_TEST.forceCurrentCross()）

```
SHARED_CONTINUITY_TEST mTEST;
mTEST.forceCurrentCross(100 uA);
mTEST.forceCurrentCross(0.0001);
```

### Syntax（取自子主题 SHARED_CONTINUITY_TEST.terminationDPS()）

```
SHARED_CONTINUITY_TEST& terminationDPS(const string& dps)
```
[表]
列: Parameter | Description
行 1:
  dps
  The pin list of the termination voltage DPS pins used.
    
    Separate multiple DPS pins with commas.
    
    This parameter is ignored for DPS-shared load boards for which there is a
    utility_control section in the `Sharing configuration file`（raw: `96971.htm`）.

### Example（取自子主题 SHARED_CONTINUITY_TEST.terminationDPS()）

```
SHARED_CONTINUITY_TEST mTest;
mTest.terminationDPS("VTERM");
mTest.terminationDPS("VTERM1, VTERM2");
```

### Syntax（取自子主题 SHARED_CONTINUITY_TEST.supplyDPS()）

```
SHARED_CONTINUITY_TEST& supplyDPS(const string& dps)
```
[表]
列: Parameter | Description
行 1:
  dps
  Pin lists of all the power supply DPS pins used.
    
    Separate multiple DPS pins with commas.
    
    This parameter is ignored for DPS-shared load boards for which there is a
    utility_control section in the `Sharing configuration file`（raw: `96971.htm`）.

### Example（取自子主题 SHARED_CONTINUITY_TEST.supplyDPS()）

```
SHARED_CONTINUITY_TEST mTest;
mTest.supplyDPS("VDD");
mTest.supplyDPS("VDD, VDDQ");
```

### Syntax（取自子主题 SHARED_CONTINUITY_TEST.settlingTime()）

```
SHARED_CONTINUITY_TEST& settlingTime(double time)
```
[表]
列: Parameter | Description
行 1:
  time
  The additional settling time.
    
    The unit is second (S).
    
    The default time value is 0 S.

### Example（取自子主题 SHARED_CONTINUITY_TEST.settlingTime()）

```
SHARED_CONTINUITY_TEST mTest;
mTest.settlingTime(0);
mTest.settlingTime(1);
```

### Syntax（取自子主题 SHARED_CONTINUITY_TEST.output()）

```
SHARED_CONTINUITY_TEST& output(MTP::OUTPUT_TYPE output)
```
[表]
列: Parameter | Description
行 1:
  output
  The place to show the output, either none or UI report window.
    
    Accordingly, the output types are:
    
    MTP::OUTPUT_NONE.
    
    MTP::OUTPUT_REPORT_UI

### Example（取自子主题 SHARED_CONTINUITY_TEST.output()）

```
SHARED_CONTINUITY_TEST mTest;
mTest.output(MTP::OUTPUT_REPORT_UI);
mTest.ouput(MTP::OUTPUT_NONE);
```

### Syntax（取自子主题 SHARED_CONTINUITY_TEST.execute()）

```
void execute() const
```

### Example（取自子主题 SHARED_CONTINUITY_TEST.execute()）

```
SHARED_CONTINUITY_TEST mTest;
mTest.execute();
```

### Syntax（取自子主题 SHARED_CONTINUITY_TEST.judgeAndLog()）

```
void judgeAndLog() const
```

### Example（取自子主题 SHARED_CONTINUITY_TEST.judgeAndLog()）

```
SHARED_CONTINUITY_TEST mTest;
mTest.judgeAndLog();
```

### Syntax（取自子主题 SHARED_CONTINUITY_TEST().print()）

```
void print(const ostream& out=std::cout) const
```
[表]
列: Parameter | Description
行 1:
  out
  Specify where to print the test results.
    
    The type for the output place is osteram&.
    
    The default output place is std::out, which is the UI report window
    in SmarTest.

### Example（取自子主题 SHARED_CONTINUITY_TEST().print()）

```
SHARED_CONTINUITY_TEST mTest;
mTest.print(); //Print the test results to the default stdout (UI report window).
```

### Syntax（取自子主题 SHARED_CONTINUITY_TEST.getPassFail()）

Retrieve the pass/fail results for all pins
tested.

```
bool getPassFail(void) const
```

Retrieve a pass/fail result for a given pin tested.

```
bool getPassFail(const string& pin) const
```
[表]
列: Parameter | Description
行 1:
  pin
  The name of a measurement pin.

Return Value

Returns a
Boolean true
 for pass or
false
 for fail
result of the measurement.

### Example（取自子主题 SHARED_CONTINUITY_TEST.getPassFail()）

```
SHARED_CONTINUITY_TEST mTest;
bool resultsAll, result;
resultsAll = mTest.getPassFail();
result = mTest.getPassFail("DO_Bus");
```

### Syntax（取自子主题 SHARED_CONTINUITY_TEST.getValue()）

```
double getValue(const string& pin) const
```
[表]
列: Parameter | Description
行 1:
  pin
  The name of a pin whose measured voltage value you want to get in [V].

### Example（取自子主题 SHARED_CONTINUITY_TEST.getValue()）

```
SHARED_CONTINUITY_TEST mTest;
double Value;
Value = mTest.getValue("DO_Bus");
```

### Class definition（取自子主题 MTP_CONTINUITY_TASK）

### Constructor
```
MTP_CONTINUITY_TASK();
```

### Member functions

Setup functions:

`pin(const string & pinlist)`（raw: `131262.htm`）

`settlingTime(double time)`（raw: `131263.htm`）

Execution functions:

`execute()`（raw: `131265.htm`）

`postExecute()`（raw: `131276.htm`）

Result functions:

`getPassFail(void) const`（raw: `131278.htm`）

`getPassFail(const string & pin) const`（raw: `131278.htm`）

`getValue(const string & pin) const`（raw: `131279.htm`）

Note
 You must use the
`DISCONNECT`（raw: `28770.htm`）
 API before using

execute()
 since the continuity test requests powering down DUTs and
disconnecting the digital pins before measurements. Learn more in
`SharedContinuity test method`（raw: `123420.htm`）
.

### Example（取自子主题 MTP_CONTINUITY_TASK）

This example tests the continuity for the shared, non-shared, and cross-terminated
pins.

Assume the sharing configuration file (
default.cfg
) is as
below:

```
domains: 8
4 3 2 1 ; 5 6 7 8
12 11 10 9 ; 13 14 15 16
utility_control:
continuity;(y<1);(U3=0x666&0xfff);(DEVICE_SUPPLY=VDD,FORCE_SUPPLY=(VDDQ,VDD,VTERM))
continuity;(y>=1);(U3=0x999&0xfff);(DEVICE_SUPPLY=VDD,FORCE_SUPPLY=(VDDQ,VDD,VTERM))
oc_reset;(U2=0x000&0x400,U2=0x400&0x400,U3=0x000&0xfff,U2=0x000&0x401)
default;(U3=0x000&0xfff,U2=0x000&0x401)
```

The
program
is:

```
#include "solution_tools.h"
#include "testmethod.hpp"
#include "mapi.hpp"
class CSharedContinuity: public testmethod::TestMethod
{
protected:
virtual void run()
{
ON_FIRST_INVOCATION_BEGIN();
{
// get limits
LIMIT limit, limitDM;

// set up for non-shared pins: DQ_Bus and DQS_DIffBus
mTest .pin("DQ_Bus,DQS_DiffBus")
.iForce(100 uA)
.limits(limit);
// set up for non-shared pins: DM
mTest .pin("DM")
.iForce(80 uA)
.limits(limitDM);
// set up for cross-terminated pins
mTest .pin("Clock_Bus")
.iForce(90 uA)
.limits(limit);
// set up for shared pins
mTest .pin("Addr_Bus,Command_Bus")
.vForce(1.1)
.limits(limit)
.deviceSupply("VDD")
.forceSupply("VDDQ,VDD,VTERM");
mTest.settlingTime(10);

// Continuity in general is measured in disconnect state and DUTs not powered
DISCONNECT();

FOR_EACH_TEST_BEGIN("default.cfg", "continuity");
{
FOR_EACH_SHARED_SITE_BEGIN();
{
// measurement of continuity
// It will test in 8 steps with sites (4, 12), (3, 11),
// (2, 10), (1, 9), (5, 13), (6, 14), (7, 15), (8, 16).
// Without utility control setting, it will still test
// in 8 steps but without utility setting change.
mTest.execute();
}
FOR_EACH_SHARED_SITE_END();
}
FOR_EACH_TEST_END();

// at the end of continuity test, do post execution
mTest.postExecute();
}
ON_FIRST_INVOCATION_END();
}
private:
MTP_CONTINUITY_TASK mTest;
};
```

### Class definition（取自子主题 MTP_CONTINUITY_PIN_TASK）

### Member functions

`iForce(double value)`（raw: `131233.htm`）

`vForce(double value)`（raw: `131236.htm`）

`limits(const LIMIT & limit)`（raw: `131237.htm`）

`deviceSupply(const string & pinlist)`（raw: `131239.htm`）

`forceSupply(const string & pinlist)`（raw: `131240.htm`）

Note
iForce()
 is used only for non-shared and cross-terminated pins.

vForce()
 is used only for shared pins. For the details about how to set up
tests for shared, non-shared, and cross-terminated pins, see
`SharedContinuity test method`（raw: `123420.htm`）
.

### Syntax（取自子主题 MTP_CONTINUITY_TASK.pin()）

```
MTP_CONTINUITY_PIN_TASK pin(const string & pinlist)
```
[表]
列: Parameter | Description
行 1:
  pinlist
  The list of the pins or pin groups to be measured in the shared continuity test.
    Multiple pins or pin groups are separated by commas.

### Syntax（取自子主题 MTP_CONTINUITY_TASK.settlingTime()）

```
void settlingTime(double time)
```
[表]
列: Parameter | Description
行 1:
  time
  The additional time for a test.
    
    The time unit is second.
    
    If you Do not specify a settling time, 0 is used.

### Syntax（取自子主题 MTP_CONTINUITY_TASK.execute()）

```
void execute()
```

### Syntax（取自子主题 MTP_CONTINUITY_TASK.postExecute()）

```
void postExecute()
```

### Syntax（取自子主题 MTP_CONTINUITY_TASK.getPassFail()）

To retrieve a pass/fail judgment for all measured
pins:

```
bool getPassFail(void) const
```

To retrieve a pass/fail judgment for a specific pin:

```
bool getPassFail(const string & pin) const
```
[表]
列: Parameter | Description
行 1:
  pin
  The name of a pin whose pass/fail result you want to retrieve.

Return Value

Returns a
Boolean true
 for pass or
false
 for fail
result of the measurement.

### Syntax（取自子主题 MTP_CONTINUITY_TASK.getValue()）

```
double getValue(const string & pin)const
```
[表]
列: Parameter | Description
行 1:
  pin
  The name of a pin whose measured voltage you want to retrieve.
    
    The unit for the retrieved voltage is volt.

### Syntax（取自子主题 DISCONNECT）

```
void DISCONNECT();
```

List of parameters

There are no parameters.

Return value

There is no return value.

### Example（取自子主题 DISCONNECT）

```
DISCONNECT();
...
...
PMU_IFVM("PIN1,PIN2").iForce(100 uA).settling(5 ms).mode("BP");

PMU_IFVM("PIN1,PIN2").limits("limit1").execute();
...
...
```

To
use the
`PMU_IFVM`（raw: `29543.htm`）
 API for a continuity test (SP or BP mode), you must

disconnect
 the tester resources from the DUT. This example disconnects the tester
resources from the DUT before the continuity test.

### Syntax（取自子主题 FOR_EACH_TEST_BEGIN）

```
FOR_EACH_TEST_BEGIN(configFile,testName)
```
[表]
列: Parameter | Description
行 1:
  configFile
  The name of the sharing configuration file you want to use.
    
    This file must be in the <device directory>/configuration/
    directory. FOR_EACH_TEST_BEGIN will automatically use the `SHARING_CONFIGURATION`（raw: `131630.htm`） API to
    load the file for you.
行 2:
  testName
  The name of a utility control line in the utility_control section of `Sharing configuration file`（raw: `96971.htm`）. Multiple names are separated by commas.
    
    The name represents all settings of this utility control line.
    
    If there is one name, the FOR_EACH_TEST_BEGIN and FOR_EACH_TEST_END block will
    automatically execute the represented utility control settings.
    
    If there are more than one names, you must execute each represented utility control
    settings manually by using `GET_CURRENT_UTILITY_CONTROL()`（raw: `131767.htm`） and
    `SHARING_CONFIGURATION.utilityActionExecute()`（raw: `131650.htm`）.

Note
 This macro has the similar functionality to
`FOR_EACH_TEST_BEGIN_WITH_RESET()`（raw: `131743.htm`）
. The only difference is FOR_EACH_TEST_BEGIN cannot
prevent sites which are not under test from drawing current, which may affect the sites under
test.

### Examples（取自子主题 FOR_EACH_TEST_BEGIN）

### Example1: Execute IDD tests for each shared sites

Assume the

default.cfg
 sharing configuration file is used, which contains these
settings:

```
domains: 8
4 3 2 1 ; 5 6 7 8
12 11 10 9 ; 13 14 15 16
utility_control:
idd;(y<1);(U3=0x222&0xfff);(DEVICE_SUPPLY=VDD)
idd;(y>=1);(U3=0x111&0xfff);(DEVICE_SUPPLY=VDD)
iddq;(y<1);(U3=0x777&0xfff);(DEVICE_SUPPLY=VDD)
iddq;(y>=1);(U3=0xbbb&0xfff);(DEVICE_SUPPLY=VDD)
oc_reset;(U2=0x000&0x400,U2=0x400&0x400,U3=0x000&0xfff,U2=0x000&0x401)
default;(U3=0x000&0xfff,U2=0x000&0x401)
```

This
IDD test program fragment tests all
sites:

```
FOR_EACH_TEST_BEGIN("default.cfg", "idd");
{
// As the utility control setting, it will test the shared sites in two steps:
//(4, 3, 2, 1, 12, 11, 10, 9) and (5, 6, 7, 8, 13, 14, 15, 16).
// Without utility control setting, it will test all the sites in one step.

// measurement of IDD of the VDD pins
}
FOR_EACH_TEST_END();
```

### Example2: Execute IDD and IDDQ tests for each shared sites

Assume the
same sharing configuration file as in example 1 is used.

This test program fragment
performs IDD and IDDQ tests on all
sites:

```
FOR_EACH_TEST_BEGIN("default.cfg", "idd, iddq");
{
//As the utility control setting, it will test the shared sites in two steps:
//(4, 3, 2, 1, 12, 11, 10, 9) and (5, 6, 7, 8, 13, 14, 15, 16).

//Since there are two testNames in FOR_EACH_TEST_BEGIN(),
//you have to execute the respective utilities by yourself.

int index = GET_CURRENT_UTILITY_CONTROL("idd");
SHARING_CONFIGURATION::getInstance().utilityActionExecute(index);
// measurement of IDD of VDD pins

index = GET_CURRENT_UTILITY_CONTROL("iddq");
SHARING_CONFIGURATION::getInstance().utilityActionExecute(index);
// measurement of IDDQ of VDDQ pins
}
FOR_EACH_TEST_END();
```

### Syntax（取自子主题 FOR_EACH_TEST_BEGIN_WITH_RESET）

```
FOR_EACH_TEST_BEGIN_WITH_RESET(configFile,testName,resetPin)
```
[表]
列: Parameter | Description
行 1:
  configFile
  The name of the sharing configuration file you want to use.
    
    This file must be be in the <device directory>/configuration/
    directory. FOR_EACH_TEST_BEGIN_WITH_RESET will automatically use the `SHARING_CONFIGURATION`（raw: `131630.htm`） API to load the file for you.
行 2:
  testName
  The name of a utility control line in the utility_control section of `Sharing configuration file`（raw: `96971.htm`）. Multiple names are separated by commas.
    
    The name represents all settings of a utility control line.
    
    If there is one name, the FOR_EACH_TEST_BEGIN_WITH_RESET and FOR_EACH_TEST_END block will
    automatically execute the represented utility control settings.
    
    If there are more than one names, you must execute each represented utility control
    settings manually by using `GET_CURRENT_UTILITY_CONTROL()`（raw: `131767.htm`） and
    `SHARING_CONFIGURATION.utilityActionExecute()`（raw: `131650.htm`）.
行 3:
  resetPin
  Name of the reset pin.
    
    If there is no pin specified for resetPin, the
    FOR_EACH_TEST__BEGIN_WITH_RESET marco works the same as `FOR_EACH_TEST_BEGIN`（raw: `131739.htm`）.

### Examples（取自子主题 FOR_EACH_TEST_BEGIN_WITH_RESET）

### Example1: Execute IDD tests for each shared sites

Assume the

default.cfg
 sharing configuration file is used, which contains these
settings:

```
domains: 8
4 3 2 1 ; 5 6 7 8
12 11 10 9 ; 13 14 15 16
utility_control:
idd;(y<1);(U3=0x222&0xfff);(DEVICE_SUPPLY=VDD)
idd;(y>=1);(U3=0x111&0xfff);(DEVICE_SUPPLY=VDD)
iddq;(y<1);(U3=0x777&0xfff);(DEVICE_SUPPLY=VDD)
iddq;(y>=1);(U3=0xbbb&0xfff);(DEVICE_SUPPLY=VDD)
oc_reset;(U2=0x000&0x400,U2=0x400&0x400,U3=0x000&0xfff,U2=0x000&0x401)
default;(U3=0x000&0xfff,U2=0x000&0x401)
```

This
IDD test program fragment tests all
sites:

```
FOR_EACH_TEST_BEGIN_WITH_RESET("default.cfg", "idd", "nRESET");
{
// As the utility control setting, it will test the shared sites in two steps:
//(4, 3, 2, 1, 12, 11, 10, 9) and (5, 6, 7, 8, 13, 14, 15, 16).
// Without utility control setting, it will test all the sites in one step.

// measurement of IDD of the VDD pins
}
FOR_EACH_TEST_END();
```

### Example2: Execute IDD and IDDQ tests for each shared sites

Assume the
same sharing configuration file as in the example 1 is used.

This test program fragment
performs IDD and IDDQ tests on all
sites:

```
FOR_EACH_TEST_BEGIN_WITH_RESET("default.cfg", "idd, iddq", "nRESET");
{
//As the utility control setting, it will test the shared sites in two steps:
//(4, 3, 2, 1, 12, 11, 10, 9) and (5, 6, 7, 8, 13, 14, 15, 16).

//Since there are two testNames in FOR_EACH_TEST_BEGIN_WITH_RESET(),
//you have to execute the respective utilities by yourself.

int index = GET_CURRENT_UTILITY_CONTROL("idd");
SHARING_CONFIGURATION::getInstance().utilityActionExecute(index);
// measurement of IDD of VDD pins

index = GET_CURRENT_UTILITY_CONTROL("iddq");
SHARING_CONFIGURATION::getInstance().utilityActionExecute(index);
// measurement of IDDQ of VDDQ pins
}
FOR_EACH_TEST_END();
```

### Syntax（取自子主题 FOR_EACH_TEST_END）

```
FOR_EACH_TEST_END()
```

### Syntax（取自子主题 FOR_EACH_SHARED_SITE_BEGIN）

```
FOR_EACH_SHARED_SITE_BEGIN()
```

### Example（取自子主题 FOR_EACH_SHARED_SITE_BEGIN）

Assume the
default.cfg
 sharing configuration file is used, which
contains these
settings:

```
domains: 8
4 3 2 1 ; 5 6 7 8
12 11 10 9 ; 13 14 15 16
utility_control:
continuity;(y<1);(U3=0x666&0xfff);(DEVICE_SUPPLY=VDD,FORCE_SUPPLY=(VDDQ,VDD,VTERM))
continuity;(y>=1);(U3=0x999&0xfff);(DEVICE_SUPPLY=VDD,FORCE_SUPPLY=(VDDQ,VDD,VTERM))
oc_reset;(U2=0x000&0x400,U2=0x400&0x400,U3=0x000&0xfff,U2=0x000&0x401)
default;(U3=0x000&0xfff,U2=0x000&0x401)
```

The
example displays how FOR_EACH_SHARED_SITE_BEGIN and FOR_EACH_SHARED_SITE_END()
work.

```
FOR_EACH_TEST_BEGIN("default.cfg", "continuity");
{
FOR_EACH_SHARED_SITE_BEGIN();
{
// It will test in 8 steps in twice:
// The first time sequentially tests sites: (4, 12), (3, 11), (2, 10), (1, 9),
// The second time sequentially tests sties: (5, 13), (6, 14), (7, 15), (8, 16).

// If without utility control setting, it will test in 8 steps sequentially
// (4, 12), (3, 11), (2, 10), (1, 9), (5, 13), (6, 14), (7, 15), (8, 16).

// measurement of continuity
}
FOR_EACH_SHARED_SITE_END();
}
FOR_EACH_TEST_END();
```

### Syntax（取自子主题 FOR_EACH_SHARED_SITE_END）

```
FOR_EACH_SHARED_SITE_END()
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
