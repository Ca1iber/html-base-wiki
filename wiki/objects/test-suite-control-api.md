---
type: object
title: Test Suite Control API
layer: L3
stage: run
tags: []
related: []
sources:
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.14_Test_Suite_Control_API.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Test Suite Control API

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **6,033 字符逐字取自** `<02_System_reference/02.09_Test_Program_Management/02.09.01.14_Test_Suite_Control_API.htm>` 及其子主题 `<02_System_reference/02.09_Test_Program_Management/02.09.01.14.01_How_to_use_the_test_suite_control_API.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.01_TestsuiteProxy.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.02_detachSession.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.03_exitProcess.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.04_initializeSession.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.05_getTestsuite.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.06_getAllTestsuiteNames.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.07_getSpecialTestsuite.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.08_createFloatingTestsuite.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.09_deleteFloatingTestsuite.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.10_selectTestmethodExecutor.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.11_getTestmethodExecutorIndex.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.12_setSiteInFocus.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.13_getSiteInFocus.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.14_setActiveSites.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.14.02.15_getActiveSites.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Examples（取自子主题 How to use the test suite control API）

### Executing an existing test suite

The following example executes an
existing test suite in the current test
flow.

```
#include "testsuitecontrol_api.hpp"
#include <iostream>
#include <stdexcept>

using namespace std;
using namespace testsuitecontrol;

int main(int argc, char** argv)
{
int nRet = -1;

try
{
initializeSession();
TestsuiteProxy ts = getTestsuite("mysuite");
//execute it on site 1,3,5
set<int> sites;
sites.insert(1);
sites.insert(3);
sites.insert(5);
setActiveSites(sites);

ts.executeActiveSites();

for(set<int>::const_iterator it = sites.begin(); it != sites.end(); ++it)
{
int siteNum = *it;
if (ts.isPass(siteNum))
{
cout<<"\"mysuite\" was executed on site"<<siteNum<<": PASSED."<<endl;
}
else
{
cout<<"\"mysuite\" was executed on site"<<siteNum<<": FAILED."<<endl;
}
}
detachSession();
nRet = 0;
}
catch(runtime_error& error)
{
cerr<<error.what()<<endl;
}
return nRet;
}
```

### Create, Setup and execute a test suite

The following example creates a
floating test suite, setup and execute the floating test
suite.

```
#include "testsuitecontrol_api.hpp"
#include <iostream>
#include <stdexcept>

using namespace std;
using namespace testsuitecontrol;

int main(int argc, char** argv)
{
int nRet = -1;
try
{
//default session: the SmarTest session of the current display
//default UTM executor: the first one (i.e. TestMethodManager).
initializeSession();

TestsuiteProxy ts = createFloatingTestsuite("floating");
ts.attachTestmethod("ac_tml.AC_TEST.FunctionalTest");

//setup this testsuite
ts.setEquationBasedLevel("2","1","3");
ts.setEquationBasedTiming("3","2","2");
ts.setSequencerLabel("\"MATCH_LOOP\"");

//execute it on currently active site
ts.executeActiveSites();
set<int> sites = getActiveSites();
for(set<int>::const_iterator it = sites.begin(); it != sites.end(); ++it)
{
int siteNum = *it;
if (ts.isPass (siteNum))
{
cout<<"\"mysuite\" was executed on site"<<siteNum<<": PASS."<<endl;
}
else
{
cout<<"\"mysuite\" was executed on site"<<siteNum<<": FAILED."<<endl;
}
}
detachSession();
nRet = 0;
}
catch(runtime_error& error)
{
cerr<<error.what()<<endl;
}

return nRet;
}
```

### Delete a test suite

The following example deletes a floating test
suite.

```
#include "testsuitecontrol_api.hpp"
#include <iostream>
#include <stdexcept>

using namespace std;
using namespace testsuitecontrol;

int main(int argc, char** argv)
{
int nRet = -1;
try
{
initializeSession();
bool isRemoved =deleteFloatingTestsuite("dummy");
if (isRemoved)
{
cout<<"\"dummy\" testsuite was removed: succeed."<<endl;
}
else
{
cout<<"\"dummy\" testsuite was removed: failed."<<endl;
}

detachSession();
nRet = 0;
}
catch(runtime_error& error)
{
cerr<<error.what()<<endl;
}

return nRet;
```

}

### Member functions（取自子主题 TestsuiteProxy）

Setup
functions:

```
attachTestmethod()
setAnalogSet()
setEquationBasedLevel()
setEquationBasedTiming()
setMultiportTiming()
setName()
setSequencerLabel()
setSiteMatch()
setTestmethodLimits()
setTestmethodParameterValues()
setTestsuiteFlag()
```

Execution
functions:

```
executeActiveSites()
executeSiteInFocus()
```

Query
functions:

```
getAnalogSet()
getLevelEquation()
getLevelSet()
getLevelSpec()
getName()
getSequencerLabel()
getSiteMatch()
getTestmethodDefaultLimitNames()
getTestmethodLimitValue()
getTestmethodName()
getTestmethodParameterNames()
getTestmethodParameterValue()
getTestmethodUserDefinedLimitNames()
getTestsuiteFlag()
getTimingEquation()
getTimingSet()
getTimingSpec()
isExecuted()
isMultiportTiming()
isPass()
```

### Syntax（取自子主题 detachSession()）

```
void detachSession();
```

### Syntax（取自子主题 exitProcess()）

```
void exitProcess(const int exitCode);
```
[表] Parameters
行 1:
  I
  exitCode
  The exit code of the process. It has the same meaning with the parameter
    status of exit(). (Type man 3 exit in the shell to see
    the details.)
```

```

### Syntax（取自子主题 initializeSession()）

```
void initializeSession(const std::string& sessionId = "",
const int testmethodExecutor = 1);
```
[表] Parameters
行 1:
  sesionId
  The ID of the SmarTest session to work with. Default value is empty, which means
    the API will automatically gets the SmarTest session ID of the current display.
行 2:
  TestmethodExecutor
  The test method executor to be used for execution. Default is the first one.

### Syntax（取自子主题 getTestsuite()）

```
TestsuiteProxy getTestsuite(const std::string& name);
```
[表] Parameters
行 1:
  name
  The test suite name.

### Syntax（取自子主题 getAllTestsuiteNames()）

```
const std::vector<std::string> getAllTestsuiteNames();
```

### Syntax（取自子主题 getSpecialTestsuite()）

```
TestsuiteProxy getSpecialTestsuite (const std::string& name);
```
[表] Parameters
行 1:
  name
  The name of the special test suite. It can be "init",
    "abort", "download",
    "pause", "reset",
    "exit", or "bin_disconnect".

### Syntax（取自子主题 createFloatingTestsuite()）

```
TestsuiteProxy createFloatingTestsuite(const std::string& testsuiteName);
```
[表] Parameters
行 1:
  testsuiteName
  The test suite name.

### Syntax（取自子主题 deleteFloatingTestsuite()）

```
bool deleteFloatingTestsuite(const std::string& name);
```
[表] Parameters
行 1:
  name
  The test suite to delete.

### Syntax（取自子主题 selectTestmethodExecutor()）

```
bool selectTestmethodExecutor( const int executor);
```
[表] Parameters
行 1:
  executor
  The index number of the UTM executor to use. It can be:
    
    1: the first executor for production execution.
    
    2: the second executor for debug purpose and non-production
    execution.

### Syntax（取自子主题 getTestmethodExecutorIndex()）

```
int getTestmethodExecutorIndex();
```

### Syntax（取自子主题 setSiteInFocus()）

```
void setSiteInFocus(const int site);
```
[表] Parameters
行 1:
  site
  The site to set in focus.

### Syntax（取自子主题 getSiteInFocus()）

```
int getSiteInFocus();
```

### Syntax（取自子主题 setActiveSites()）

```
void setActiveSites(const std::set<int>& sites);
```
[表] Parameters
行 1:
  sites
  The site number stored in set<int>.

### Example（取自子主题 setActiveSites()）

```
set<int> sites;
sites.insert(1);
sites.insert(3);
setActiveSites(sites);
```

In
this example, site 1 and 3 are set to active.

### Syntax（取自子主题 getActiveSites()）

```
const std::set<int> getActiveSites();
```

### Example（取自子主题 getActiveSites()）

The following example executes the test suite
mysuite
 and print the
test result of each active
site.

```
TestsuiteProxy ts = getTestsuite("mysuite");
ts.executeActiveSites();
set<int> sites = getActiveSites();
for(set<int>::const_iterator it = sites.begin(); it != sites.end(); ++it)
{
int siteNum = *it;
if (ts.isPass (siteNum))
{
cout<<"\"mysuite\" was executed on site"<<siteNum<<": PASS."<<endl;
}
else
{
cout<<"\"mysuite\" was executed on site"<<siteNum<<": FAILED."<<endl;
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
