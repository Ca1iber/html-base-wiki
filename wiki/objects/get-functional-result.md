---
type: object
title: GET_FUNCTIONAL_RESULT()
layer: L2
stage: testmethod
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.88_GET_FUNCTIONAL_RESULT.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# GET_FUNCTIONAL_RESULT()

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **9,462 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.88_GET_FUNCTIONAL_RESULT.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

Note
GET_FUNCTIONAL_RESULT()
 should reside outside the

`ON_FIRST_INVOCATION block`（raw: `29526.htm`）
. Any action which restarts
the sequencers will erase the functional results.

Functions returning
Boolean
:

```
Boolean GET_FUNCTIONAL_RESULT(void);
Boolean GET_FUNCTIONAL_RESULT(const STRING& pin);
Boolean GET_FUNCTIONAL_RESULT(const STRING& pin, const STRING& context);
Boolean GET_FUNCTIONAL_RESULT(const STRING& port, const STRING& labelName, TM::FUNCIONAL_RESULT_TYPE type);
```

Note
 To retrieve the result of specified label and port, the
`TM::FUNCIONAL_RESULT_TYPE`（raw: `29400.htm#_29400__div_FUNCIONAL_RESULT_TYPE`）
 type must be set to

TM::FTST_BURST
.

Functions returning the result as
`FUNC_TEST_BURST_RESULT`（raw: `29400.htm#_29400__p_FUNC_TEST_BURST_RESULT`）
:

```
void GET_FUNCTIONAL_RESULT(const STRING& port,
std::vector<FUNC_TEST_BURST_RESULT>& ret, bool bReadPinFailCycles = false);

void GET_FUNCTIONAL_RESULT(const STRING_VECTOR& portlist,
const STRING& sequencer_execution_context,
std::vector<FUNC_TEST_BURST_RESULT>& ret, bool bReadPinFailCycles = false);

void GET_FUNCTIONAL_RESULT(const STRING& port,
const STRING& sequencer_execution_context,
std::vector<FUNC_TEST_BURST_RESULT>& ret, bool bReadPinFailCycles = false);
```

This API is defined in the header file

/opt/hp93000/soc/prod_com/include/MAPI/Execute.h
.

Parameters
[表]
列: Parameter | Description
行 1:
  pin
    port
  Defines the pin name of which the functional test
    result shall be retrieved.
    For multiport testing, a
    port name can be specified instead of a single
    pin.
    
    If this parameter is omitted (first
    syntax only), TRUE is returned
    only if all pins have passed, else
    FALSE is returned.
行 2:
  portlist
  List of string elements defining ports and set up as
    `STRING_VECTOR`（raw: `131095.htm`）.
    The
    portlist is to be used if the
    functional test results for more than one port shall
    be retrieved.
行 3:
  context
  The `execution context`（raw: `135848.htm`） of
    the last executed test for that context.
行 4:
  sequencer_execution_context
  The sequencer execution context, see `SEQUENCER_CONTEXT`（raw: `136815.htm`） and `SEQUENCER_CONTEXT_ITEM`（raw: `137373.htm`）.
行 5:
  labelName
  Specifies the label of which the functional test
    result will be retrieved.
行 6:
  type
  The value type FUNCIONAL_RESULT_TYPE defines the type of the
    functional result.
    Currently the type can only be
    TM::FTST_BURST for retrieving the burst result of the multiport
    test.
    
    ```
    namespace TM
    
    typedef enum
    {
    FTST_BURST
    
    }FUNCTIONAL_RESULT_TYPE;
    ```
行 7:
  ret
  The result of type
    FUNC_TEST_BURST_RESULT containing
    the executed label, the start cycle, the pass/fail
    result and the optional fail cycles map of the
    execution.
    ret is an already
    defined vector of type
    TM::FUNC_TEST_BURST_RESULT that
    is handled as
    reference.
    
    TM::FUNC_TEST_BURST_RESULT
    is defined as follows:
    
    ```
    typedef struct
    {
    STRING labelname;
    int id;
    int startCyc;
    int numberOfCycles;
    bool result;
    std::map<std::string, int> failCyclesMap;
    int isFailCyclesValid;
    
    } FUNC_TEST_BURST_RESULT;
    ```
    
      [子表]
      列: Return value | Description
      子行 1:
        labelname
        The name of the executed label.
      子行 2:
        id
        Index of the label within the burst.
          id is set to 0 for the first
          label.
      子行 3:
        startCyc
        The start cycle of the label within the
          burst.
      子行 4:
        numberOfCycles
        The number of cycles of the label.
      子行 5:
        result
        Returns a TRUE or
          FALSE.
          
          If multiple pins or a port has been passed all
          containing pins must pass to return a
          TRUE. If any of the pins fail a
          FALSE is returned.
      子行 6:
        failCyclesMap
        A map containing the name of failing pins
          as string and the number of
          fail cycles as int.
          The map
          is filled only if parameter `bReadPinFailCycles`（raw: `29400.htm#_29400__r_bReadPinFailCycles`） has been set to
          TRUE.
      子行 7:
        isFailCyclesValid
        The parameter shows the state of filling the
          failCyclesMap:
          
          -1: The pin fail cycles were not read. The
          function was called with parameter
          bReadPinFailCycles set to
          FALSE.
          
          0: The pin fail cycles were read but are not
          valid (`ERCC?`（raw: `98594.htm`）
          valid_code flag was
          OVFL or
          LESS).
          
          1: The pin fail cycles were read
          successfully.
行 8:
  bReadPinFailCycles
  The optional parameter initiates filling the
    failCyclesMap of parameter `ret`（raw: `29400.htm#_29400__r_ret`） if set to
    TRUE.
    The default value is
    FALSE.
    Note Use
    this parameter with caution. Filling the fail
    cycles map with data that must be read from the
    hardware may significantly increase the test
    time.
Return value
There are two types of functions for this API:

Boolean

The pass/fail result is returned as

Boolean
:

TRUE
 if the selected pin or all pins of
the selected ports have passed the functional test or

FALSE
 if any of the selected pins or any
pin of the selected ports has failed the functional
test.

void

These functions have no return value. The requested data is
returned by a parameter of type

FUNC_TEST_BURST_RESULT
 that is to be
defined in the calling function and transferred as reference.
For more information refer to parameter
`ret`（raw: `29400.htm#_29400__r_ret`）
 and
`Example 3`（raw: `29400.htm#_29400__Example_3`）
.

### Examples

### Example 1

In the following example the result of
PIN1
 will be retrieved and
stored in the
result
 variable after executing
`FUNCTIONAL_TEST()`（raw: `29356.htm`）
.

```
ON_FIRST_INVOCATION_BEGIN();

FUNCTIONAL_TEST();

ON_FIRST_INVOCATION_END();

Boolean result = GET_FUNCTIONAL_RESULT("PIN1");
```

### Example 2

This example retrieves the result of all pins involved in that PPMU measurement.

```
TASK_LIST Ppmu_task;

//
// Add the measurement settings to Ppmu_task;
//

ON_FIRST_INVOCATION_BEGIN();

Ppmu_task.execute();

ON_FIRST_INVOCATION_END();

Boolean result = GET_FUNCTIONAL_RESULT();
```

### Example 3

The following example returns the result of all executed patterns.

```
std::vector<FUNC_TEST_BURST_RESULT> mpResult;

ON_FIRST_INVOCATION_BEGIN();

FW_TASK("DCRM OVEM,LMAP,,(@@)");

FUNCTIONAL_TEST();

FW_TASK("DCRM OVEM,FCM,,(@@)");

ON_FIRST_INVOCATION_END();

GET_FUNCTIONAL_RESULT("dig12_dc1Port", mpResult);

for ( uint i = 0; i < mpResult.size(); i++ )
{
FUNC_TEST_BURST_RESULT funcTestRes = mpResult[i];

cout << "Result for label " << funcTestRes.labelname << ": "
<< (funcTestRes.result==true ? "true" : "false" ) << endl;
}
```

### Example 4

The following example illustrates how to retrieve a functional result of a test
executed using
`GET_FUNCTIONAL_RESULT()`（raw: `29400.htm`）
 on a special sequencer context.

```
STRING sContext = "global";

ON_FIRST_INVOCATION_BEGIN();

SEQUENCER_CONTEXT_ITEM context1(sContext);

context1.setPorts("port1");

SEQUENCER_CONTEXT context;

context.add(context1).apply();

CONNECT();

FW_TASK("DCRM OVEM,LMAP,,(@@)");

START_TEST(sContext);

int a, b;

WAIT_TEST_DONE(36000, &a, &b ,sContext);

FW_TASK("DCRM OVEM,FCM,,(@@)");

ON_FIRST_INVOCATION_END();

std::vector<FUNC_TEST_BURST_RESULT> result;

GET_FUNCTIONAL_RESULT("port1", sContext, result);

cout << endl << "*** Current Site number: " << CURRENT_SITE_NUMBER() << " ***" << endl;

for ( uint i = 0; i < result.size(); i++ )
{
FUNC_TEST_BURST_RESULT funcTestRes = result[i];

cout << "Result for label " << funcTestRes.labelname << ": "
<< (funcTestRes.result==true ? "TRUE" : "FALSE" ) << endl;

cout << "startCycle: " << funcTestRes.startCyc << endl << "numberOfCycles: "
<< funcTestRes.numberOfCycles << endl << "----------------------------------------------------" << endl;
}

DISCONNECT();
```

### Example 5: Reading the number of fail cycles per pin
The following
example shows how to read the number of fail cycles per pin.

Note
 Use parameter
bReadPinFailCycles
 with caution.
Filling the fail cycles map with data that must be read from the hardware may
significantly increase the test time.

```
ON_FIRST_INVOCATION_BEGIN();
{
...
...

FW_TASK("DCRM OVEM,LMAP,,(@@)");

FUNCTIONAL_TEST();
}
ON_FIRST_INVOCATION_END();

vector<FUNC_TEST_BURST_RESULT> mpResult;

GET_FUNCTIONAL_RESULT("Port_1", mpResult, true);

for (uint labelIndex = 0; labelIndex < mpResult.size(); labelIndex++)
{
FUNC_TEST_BURST_RESULT funcTestRes = mpResult[labelIndex];

cout << "Label " << funcTestRes.labelname << endl;
cout << endl;
cout << "\tResult:\t\t\t" << (funcTestRes.result==true ? "true" : "false" ) << endl;
cout << "\tisValidFailCycles:\t" << funcTestRes.isFailCyclesValid << endl;
cout << endl;
cout << "\tfailCyclesMap:" << endl;
cout << endl;

map<string, int>::iterator iterator;

for (iterator = funcTestRes.failCyclesMap.begin(); iterator != funcTestRes.failCyclesMap.end(); ++iterator)
{
cout << "\t\tFail cycles for pin " << iterator->first << " : " << iterator->second << endl;
}

cout << endl;
}
```

The
code above results in the following output if failing pins have been
found:

```
Label ...

Result: false
isValidFailCycles: 1

failCyclesMap:

Fail cycles for pin ... : ...
Fail cycles for pin ... : ...
...
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
