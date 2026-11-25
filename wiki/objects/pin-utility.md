---
type: object
title: PIN_UTILITY
layer: L2
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.147_PIN_UTILITY.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# PIN_UTILITY

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **11,504 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.147_PIN_UTILITY.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Class definition

Constructor
This class has no public constructor.

To use the

PIN_UTILITY
 API, you must always use the
system-prepared class object
PinUtility
. You cannot
create any object of this class.

Member functions

`expandDigitalPinNamesFromPinList()`（raw: `70858.htm#_70858__dlentry_expandDigitalPinNamesFromPinList`）

`getDigitalPinNamesFromPinList()`（raw: `70858.htm#_70858__dlentry_getDigitalPinNamesFromPinList`）

`getDpsPinNamesFromPinList()`（raw: `70858.htm#_70858__dlentry_getDpsPinNamesFromPinList`）

`getPinType()`（raw: `70858.htm#_70858__dlentry_getPinType`）

`getSharedDigitalPins()`（raw: `70858.htm#_70858__dlentry_getSharedDigitalPins`）

`getSharedDpsPins()`（raw: `70858.htm#_70858__dlentry_getSharedDpsPins`）

`createPinListFromPinNames()`（raw: `70858.htm#_70858__dlentry_createPinListFromPinNames`）

### Member functions

expandDigitalPinNamesFromPinList()
```
const STRING_VECTOR expandDigitalPinNamesFromPinList(const STRING& pinList,
const TM::PIN_TYPE pinType,
const BOOLEAN ignoreMissingPinNames)
```

This
member function converts the pin names of the specified pin type
contained in the pin list into a string vector. Pin group names will be
resolved to pin names. The names in the pin list must be separated by
commas.

Since this member function will return a std::vector, you
can use all available methods provided in the Standard Template Library
(STL) for std::vector, such as loop over all the elements or adding two
separate lists.

This member function is only supported for downward compatibility. For new applications,
`getDigitalPinNamesFromPinList()`（raw: `70858.htm#_70858__dlentry_getDigitalPinNamesFromPinList`）
 should be
used instead.

[表]
列: Parameter | Description
行 1:
  pinList
  The name of the pin list (contains pin names, but
    also can contain pin group names)
行 2:
  pinType
  Type of pin definition. It can be:
    
    TM::I_PIN
    
    TM::O_PIN
    
    TM::IO_PIN
    
    TM::DC_PIN
    
    TM::ALL_DIGITAL
    
    For example, TM::O_PIN|TM::DC_PIN will return all output and dc
    pins.
行 3:
  ignoreMissingPins
  Flag to indicate whether or not to ignore pins
    that are not defined.
    
    TRUE = no error if the pin is not defined
    
    FALSE = error if pin is not defined
getDigitalPinNamesFromPinList()
```
const STRING_VECTOR getDigitalPinNamesFromPinList(const STRING& pinList,
const TM::PIN_TYPE expectedPinTypes,
const BOOLEAN throwErrorOnMissingPinNames,
const BOOLEAN throwErrorOnMismatchedPinTypes,
const SORT_ORDER sortOrder);
```

This member function, which is similar to
`expandDigitalPinNamesFromPinList()`（raw: `70858.htm#_70858__dlentry_expandDigitalPinNamesFromPinList`）
, converts
the pin names of the specified pin type contained in the pin list into a
string vector. Pin group names will be resolved to pin names. For pins
defined in pin groups, the pins are listed in alphabetical order or pin
group definition order. The names in the pin list must be separated by
commas. You can cause the function to throw an error if the list
contains undefined pins or pins that do not have the requested type.

Since this member function will return a std::vector, you
can use all available methods provided in the Standard Template Library
(STL) for std::vector, such as loop over all the elements or adding two
separate lists.

[表]
列: Parameter | Description
行 1:
  pinList
  The name of the pin [跨 2 列]
    list (contains pin names, but also can contain pin
    group names)
行 2:
  pinType
  Type of pin [跨 2 列]
    definition. It can be:
    
    TM::I_PIN
    
    TM::O_PIN
    
    TM::IO_PIN
    
    TM::DC_PIN
    
    TM::ALL_DIGITAL
    
    For example, TM::O_PIN|TM::DC_PIN will return all "o" and "dc"
    pins.
行 3:
  throwErrorOnMissingPinNames
  Flag to indicate [跨 2 列]
    whether or not to ignore pins that are not
    defined.
行 4:
  
  TRUE
  An error is thrown if any pin in the list is not
    defined.
行 5:
  
  FALSE (default)
  Undefined pins are not transferred into the
    vector. No error is thrown.
行 6:
  throwErrorOnMismatchedPinTypes
  Flag to indicate whether or not to ignore pin types that are not specified by [跨 2 列]
    pinType .
行 7:
  
  TRUE
  An error is thrown if the pin list contains any pin that has not one of the types specified with
    pinType.
行 8:
  
  FALSE (default)
  Only pins that have one of the requested types are
    transferred into the vector. No error is thrown.
行 9:
  sortOrder
  It controls the order of the returned pins. It can be [跨 2 列]
    PIN_UTILITY::ALPHABETICAL for
    the alphabetical order or
    PIN_UTILITY::DEFINITION_ORDER
    for the group definition order.
getDpsPinNamesFromPinList()
```
const STRING_VECTOR getDpsPinNamesFromPinList(const STRING& dpsPinList,
const BOOLEAN throwErrorOnMissingPinNames)
```

This
member function converts the DPS pin names contained in the pin list
into a string vector. The names in the pin list must be separated by
commas. You can cause the function to throw an error if the list
contains undefined pins.

Since this member function will return a
std::vector, you can use all available methods provided in the Standard
Template Library (STL) for std::vector, such as loop over all the
elements or adding two separate lists.

[表]
列: Parameter | Description
行 1:
  dpsPinList
  The name of the pin [跨 2 列]
    list
行 2:
  throwErrorOnMissingPinNames
  Flag to indicate [跨 2 列]
    whether or not to ignore pins that are not defined
    as a DPS pin.
行 3:
  
  TRUE
  An error is thrown if any pin in the list is not
    defined as a DPS pin.
行 4:
  
  FALSE (default)
  Only pins that are defined as DPS pins are
    transferred into the vector. No error is thrown.
getPinType()
```
const STRING getPinType(char const * PinName)
```

This
member function queries the hardware capabilities behind a pin (MCB,
MCE, PS400, PS1600). For analog setups, you can query the pin type and
set filters or frequencies according to the capabilities of the
hardware.

[表]
列: Parameter | Description
行 1:
  PinName
  The name of the pin

See also Example 3 below.

getSharedDigitalPins()
```
const STRING_VECTOR getSharedDigitalPins();
```

This
member function returns all digital pins which are shared in more than
one site.

Since this member function will return a std::vector,
you can use all available methods provided in the Standard Template
Library (STL) for std::vector, such as loop over all the elements or
adding two separate lists.

getSharedDpsPins()
```
const STRING_VECTOR getSharedDpsPins();
```

This member
function returns all dps pins which are shared in more than one
site.

Since this member function will return a std::vector, you
can use all available methods provided in the Standard Template Library
(STL) for std::vector, such as loop over all the elements or adding two
separate lists.

createPinListFromPinNames()
```
const STRING& createPinListFromPinNames (const STRING_VECTOR& pinName)
```

This member function is used to convert a vector of pin names to one pin list string, where the
names will be separated by a comma. For example, if the

STRING_VECTOR
 contains three elements pin1, pin2,
and pin3, the return will be "pin1,pin2,pin3".

[表]
列: Parameter | Description
行 1:
  pinName
  Name of pin name vector

See Example 1, below.

### Examples

### Example 1
```
STRING pinList = "pin1,pin2,pin3";
STRING_VECTOR pinNameList;
pinNameList = PinUtility.getDigitalPinNamesFromPinList(pinList, TM::IO_PIN, TRUE,TRUE);
for (uint index = 0; index < pinNameList.size(); index++)
{
cout << pinNameList [index] << endl;
// pin1
// pin2
// pin3
}
```

### Example 2
```
STRING pinList1 = "pin1,pin2,pin3";
STRING pinList2 = "pin4,pin5,pin6";
STRING_VECTOR sum, sv1, sv2;
sv1 = PinUtility.getDigitalPinNamesFromPinList (pinList1, TM::IO_PIN, TRUE,TRUE);
sv2 = PinUtility.getDigitalPinNamesFromPinList (pinList2, TM::IO_PIN, TRUE,TRUE);
sum = sv1 + sv2;
sv1*=sv2;
```

### Example 3

The example shows how to use the getPinType
parameter.

```
cout << "Pintype of dps1 is: \"" << PinUtility.getPinType("dps1") << "\"" << endl;
cout << "Pintype of dps2 is: \"" << PinUtility.getPinType("dps2") << "\"" << endl;
cout << "Pintype of pmu31 is: \"" << PinUtility.getPinType("pmu1") << "\"" << endl;
cout << "Pintype of pin1 is: \"" << PinUtility.getPinType("pin1") << "\"" << endl;
cout << "Pintype of hvpin1 is: \"" << PinUtility.getPinType("hvpin1") << "\"" << endl;
```

returns:

```
Pintype of dps1 is: "DCS-DPS128HC"
Pintype of dps2 is: "DCS-DPS128HV"
Pintype of pmu3 is: "DCS-VI32"
Pintype of pin1 is: "PS1600"
Pintype of hvpin1 is: "PS1600"
```

### Example 4

This is a complete example that shows how to use
PIN_UTILITY together with getDigitalPinNamesFromPinList to extract single pin
results.
dForceLow
,
dForceHigh1
 and

dForceHigh2
 are parameters defined in the test
method.

```
/**********************************
*This test is invoked per site.
**********************************/
virtual void run()
{
PPMU_SETTING setLeakLow , setLeakHigh ;
PPMU_MEASURE measLeakHigh , measLeakLow ;
PPMU_RELAY relClose , relOpen ;
TASK_LIST tskLeak ;
/*************************************************************
* Execution Section:
* This section will executed only once.
* ***********************************************************/
ON_FIRST_INVOCATION_BEGIN();
setLeakLow.pin ( "leak_pins1,leak_pins2" ).vForce (dForceLow V )
.iRange ( 100 uA).min( 1.2 uA ).max ( 20 uA ) ;
// One PPMU_SETTING can hold different values for different pins.
setLeakHigh.pin ( "leak_pins1" ).vForce (dForceHigh1 V ).iRange ( 100 uA).min( 1.2 uA ).max ( 20 uA ) ;
setLeakHigh.pin ( "leak_pins2" ).vForce (dForceHigh2 V ).iRange ( 100 uA).min( 1.2 uA ).max ( 20 uA ) ;
// value only test test OVAL is faster than PVAL
measLeakHigh.pin ( "leak_pins1, leak_pins2" ).execMode( TM::OVAL );
measLeakLow.pin ( "leak_pins1, leak_pins2" ).execMode( TM::OVAL );
relClose.pin ( "leak_pins1, leak_pins2" ).status ( "PPMU_ON" );
relClose.wait ( 1 ms );
relOpen.pin ( "leak_pins1, leak_pins2" ).status ( "AC_ON" );
//Multiple measurements and settings are combined into one measurement.
//The results of all sites are cashed in the measrement objects.
//There is not .setup() API needed because the values will NOT change during
//the testprogram run.
tskLeak.add(setLeakLow).add(relClose).add(measLeakLow)
.add(setLeakHigh).add(measLeakHigh).add(relOpen);
//Execute the Leakage Pattern and the taskList
CONNECT();
FUNCTIONAL_TEST();
tskLeak.execute();
ON_FIRST_INVOCATION_END();
/*************************************************************
* Result upload, calculation and datalog
* This section will be executed for each site.
* ***********************************************************/
STRING_VECTOR pinNameList;
int SizeOfNameList;
//Get Results and Datalog from Group leak_pins1
pinNameList = PinUtility.getDigitalPinNamesFromPinList("leak_pins1", TM::IO_PIN, TRUE,TRUE);
SizeOfNameList = pinNameList.size();
for (int index = 0; index < SizeOfNameList; index++)
{
TEST(pinNameList[index],"Leakage_Low" ,tmLimits, measLeakLow .getValue(pinNameList[index]), TRUE);
TEST(pinNameList[index],"Leakage_High",tmLimits, measLeakHigh.getValue(pinNameList[index]), TRUE);
}
//Get Results and Datalog from Group leak_pins1
pinNameList = PinUtility.getDigitalPinNamesFromPinList("leak_pins2", TM::IO_PIN, TRUE,TRUE);
SizeOfNameList = pinNameList.size();
for (int index = 0; index < SizeOfNameList; index++)
{
TEST(pinNameList[index],"Leakage_Low" ,tmLimits, measLeakLow .getValue(pinNameList[index]), TRUE);
TEST(pinNameList[index],"Leakage_High",tmLimits, measLeakHigh.getValue(pinNameList[index]), TRUE);
}
return;
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
