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

**文档事实** SpecValue 是 universal test method 编程中定义的参数类型，用来表示带单位的值，格式为 `"value[unit]"`。

**文档事实** 该类提供一组成员函数，供 test method 读取和设置 SpecValue 参数的值与单位，包括 getValue()、getUnit()、getBaseUnit()、getUnitOptionVector()、setBaseUnit()、getValueAsTargetUnit()、inputValueUnit()、parseValueUnit()、reset() 与 `operator =`。

**文档事实** 参数初始化后，当前单位与指定的 base unit 相同；若以不带单位的值指定，getUnit() 返回前一个值的单位。

**文档事实** 预定义的单位类别与单位：Voltages（V, mV, uV, nV）、Current（A, mA, uA, nA）、Time（s, ms, us, ns, ps, fs）、Frequency（THz, GHz, MHz, kHz, Hz）、Bit width（UI）。若 base unit 不在预定义类别中，会被接受为只含该单位的新类别（例如 `"specalUnit"`）。

**文档事实** 文档把 SpecValue 列在 "Parameter types defined for universal test method" 之下，同组的还有 FileString、OptionList、SpecVariable、TestMethodParameterProxy。

**推断** 因此其定位是「参数容器 + 单位换算」：值以 double 保存，base unit 决定单位类别，unit option vector 列出该类别下可用的全部单位。

## 典型用法

**文档事实** 文档示例在 test method 类中声明 `testmethod::SpecValue specVa1;`，在 initialize() 中用 `addParameter("specVa1","SpecValue",&specVa1).setDefault("3800[mV]");` 注册参数，默认值为 3800 mV。

**文档事实** 在 run() 中用 `specVa1.inputValueUnit("1500[mV]")` 设置值，再用 getValue()、getUnit()、getBaseUnit()、getUnitOptionVector() 读取，最后用 `getValueAsTargetUnit("V")` 换算到 V。

**文档事实** inputValueUnit() 对不符合 `"value[unit]"` 格式的输入返回 false 且不发生改动，格式正确时返回 true；单位不在当前类别时沿用前一个单位，纯数值输入也沿用前一个单位。

**文档事实** setBaseUnit() 传入空字符串会清空当前单位，使参数没有可用单位；传入非预定义单位会建立只含该单位的新类别。

**文档事实** getValueAsTargetUnit() 在没有 base unit 时返回当前值；目标单位不在 unit option list 内会抛出 `std::runtime_error`。

**文档事实** getUnitOptionVector() 在指定了 base unit 时返回单位选项向量的指针，否则返回 0。

**建议** 在 run() 中修改参数值时优先用 inputValueUnit() 并检查其 bool 返回值，以免单位不匹配时静默沿用旧单位。

## 和谁有关

- **文档事实** addParameter，其 parameterType 可取 `SpecValue`，并说明 SpecValue 的格式为 `"value[unit]"`；SpecValue 参数通过 addParameter 在 initialize() 中注册。
- **文档事实** Parameter types defined for universal test method，该页把 SpecValue 与 FileString、OptionList、SpecVariable、TestMethodParameterProxy 并列为 universal test method 的参数类型。
- **文档事实** SpecVariable，与 SpecValue 同列在参数类型页；addParameter 页说明 SpecVariable 用于 timing/level 文件中定义的 spec variables。**推断** 两者都是 universal test method 的参数类型，但 SpecVariable 关联既有 spec variable，而 SpecValue 自带值与单位。
- **文档事实** TestMethodParameterProxy，其 `getType()` 的返回值可以是 SpecValue，说明 addParameter 返回的代理对象会携带该参数类型标识（引文取自 objpack 入边）。
- **文档事实** How to create a universal test method class，本页 Related information 指向它；该页说明创建 test method 类时可选 SpecValue 作为参数类型，格式为 `"value[unit]"`。
- **推断** 本对象贴合 level 阶段的使用场景：其单位类别包含电压、电流、时间、频率，示例使用 mV 与 V；但文档本身没有把 SpecValue 限定为 level 专用。

## 版本

**文档事实** Functional changes 记载：Introduced in SmarTest 6.5.2。

（该段没有其他版本条目。）

## 出处

- `02_System_reference/02.07_Test_Method_Reference/02.07.02.13.03_SpecValue.htm`，主源，含概述、全部成员函数、Parameter 表、Example 与 Functional changes。
- `02_System_reference/02.07_Test_Method_Reference/02.07.02.13_Parameter_types_defined_for_universal_test_method.htm`、`02_System_reference/02.07_Test_Method_Reference/02.07.02.02.02_How_to_create_a_universal_test_method_class.htm`、`02_System_reference/02.07_Test_Method_Reference/02.07.04.01.03_addParameter.htm`，用于核对 SpecValue 作为参数类型的注册方式与格式说明（已用 show.py 读取）。
- TestMethodParameterProxy 的 `getType()` 引文取自 `extract/objpack.py` 入边索引（02.07.02.13.05 与 02.07.04.02.16 两页）。
