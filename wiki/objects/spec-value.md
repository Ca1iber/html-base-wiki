---
type: object
title: SpecValue
layer: L2
stage: level
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.02.13.03_SpecValue.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# SpecValue

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **5,140 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.02.13.03_SpecValue.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Member functions

### getValue()
```
double getValue() const;
```

This function
returns the value of a SpecValue parameter.

### getUnit()
```
const std::string& getUnit() const;
```

This
function returns the
unit
 part of a SpecValue parameter. If the parameter is
specified with a value without unit, the unit of the previous value will be returned. After a
SpecValue parameter is initialized, the current unit is the same as the specified base
unit.

### getBaseUnit()
```
const std::string& getBaseUnit() const;
```

This
function returns the base unit of a SpecValue parameter. Base unit is one of the units of a
category and is used to represents specific unit category. For example, voltage units includes
"
nV
", "
uV
", "
mV
", "
V
". Any
one of them could be the base unit for voltage.

### getUnitOptionVector()
```
const std::vector<std::string>* getUnitOptionVector() const;
```

This
function returns a pointer to unit option vector if a base unit is specified. Otherwise, 0 is
returned. The unit vector contains all units of this category indicated by the base unit. For
example, the unit option vector for voltage includes "nV", "uV", "mV", "V".

### setBaseUnit()
```
void setBaseUnit(const std::string& inputBase);
```

This
function sets the base unit and updates the unit option list if the specified based unit is not
in the current unit list. If the specified base unit is empty, the current unit will be cleaned
and no unit is available for the SpecValue parameter.

The predefined categories and units
include:

Voltages: V, mV, uV, nV

Current: A, mA, uA, nA

Time: s, ms, us, ns, ps, fs

Frequency: THz, GHz, MHz, kHz, Hz

Bit width: UI

If the input base unit is not in the predefined categories, it will be accepted as a new
unit category with this input unit only. For example,

mySpecValueVar.setBaseUnit("specalUnit");
 is valid.

[表] Parameter
行 1:
  inputBase
  The base unit to set. "[]" is not needed for this base unit
    input.

### getValueAsTargetUnit()
```
double getValueAsTargetUnit(const std::string& targetUnit);
```

This
function converts the original value to a value with the specified target unit. If no base unit
exists, it returns the current value. If the target unit is out of the unit option list, a

std::runtime_error
 will be issued.

[表] Parameter
行 1:
  targetUnit
  The target unit to use.

### inputValueUnit()
```
bool inputValueUnit(const std::string& input);
```

This
function changes the value of a SpecValue parameter. If the input value is not in the format of
"
value[unit]
", false will be returned with no change happening. Otherwise,
true will be returned.

[表] Parameter
行 1:
  input
  The value to set for the SpecValue parameter. It is in the format of
    "value[unit]".
    
    If "unit" is in the current unit category of the base unit, both
    "value" and "unit" will be set to effective.
    
    If "unit" is not in the current unit category of the base unit, the
    previous unit will be used.
    
    If the input is a pure value input, the previous unit will be used.

### parseValueUnit()
```
bool parseValueUnit(const std::string& input, std::string& valueStr, std::string& unit);
```

This
function parses out the value and unit from the input and stores them separately in the output
parameters.

[表] Parameters
列: I/O | Parameter | Description
行 1:
  I
  input
  The input value for a SpecValue parameter. It is in the format of
    "value[unit]".
行 2:
  O
  valueStr
  The "value" part of the input.
行 3:
  O
  unit
  The "[unit]" part of the input.

### reset()
```
void reset();
```

This function resets all
member variable to default. This means the base unit and the current unit are set to empty, the
value is set to zero and the pointer of unit option vector is set to zero.

### operator =
```
SpecValue& operator = (const SpecValue& rhl);
```

This
function sets a value to the SpecValue parameter by copying from another SpecValue
parameter.

[表] Parameter
行 1:
  rhl
  The SpecValue parameter to copy from.

### Example

In the following example,
specVa1
 is a parameter variable defined in
the type
SpecValue.

```
class TestSpecValue: public testmethod::TestMethod {
protected:
testmethod::SpecValue specVa1;
virtual void initialize()
{

addParameter("specVa1","SpecValue",&specVa1).setDefault("3800[mV]");
}
/**
*This test is invoked per site.
*/
virtual void run()
{
//specify a value and unit for specVa1
specVa1.inputValueUnit("1500[mV]");
//retrieves the value, unit, base unit and the unit options of specVa1
double value = specVa1.getValue();
STRING unit = specVa1.getUnit();
STRING baseUnit=specVa1.getBaseUnit();
const vector<string>* optionVec1 = specVa1.getUnitOptionVector();
cout << "******The content of specVa1******"<<endl;
cout << "value " << value <<endl;
cout <<"unit " <<unit <<endl;
cout <<"base unit " <<baseUnit <<endl;
for (size_t i=0;i<optionVec1->size();i++)
{
cout << "unit option " <<i <<":" << (*optionVec1)[i]<<endl;
}
//converts the value of specVa1 to the unit V.
value = specVa1.getValueAsTargetUnit("V");
cout <<"spec value with unit [V] " <<value <<endl;
return;
}
...
};
REGISTER_TESTMETHOD("TestSpecValue", TestSpecValue);
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
