---
type: object
title: EVENT_VALUE_DOUBLE
layer: L2
stage: testmethod
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.18_EVENT_VALUE_DOUBLE.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# EVENT_VALUE_DOUBLE

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,979 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.18_EVENT_VALUE_DOUBLE.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Class definition

### Constructor
```
EVENT_VALUE_DOUBLE(const INT value);
EVENT_VALUE_DOUBLE(const FLOAT value);
EVENT_VALUE_DOUBLE(const DOUBLE value);
EVENT_VALUE_DOUBLE(const STRING & expression);
EVENT_VALUE_DOUBLE(const CHAR * expression);
EVENT_VALUE_DOUBLE();
```

### Member Functions
```
bool isExpression() const;
const STRING & getExpression() const;

DOUBLE getValue() const;
```

### Operators
```
EVENT_VALUE_DOUBLE & operator = (const EVENT_VALUE_DOUBLE &);
EVENT_VALUE_DOUBLE & operator = (INT);
EVENT_VALUE_DOUBLE & operator = (FLOAT);
EVENT_VALUE_DOUBLE & operator = (DOUBLE);
EVENT_VALUE_DOUBLE & operator = (const STRING &);
EVENT_VALUE_DOUBLE & operator = (const CHAR *);

bool operator == (const EVENT_VALUE_DOUBLE &) const;
bool operator != (const EVENT_VALUE_DOUBLE &) const;
```

### Constructor
```
EVENT_VALUE_DOUBLE(const INT value);
EVENT_VALUE_DOUBLE(const FLOAT value);
EVENT_VALUE_DOUBLE(const DOUBLE value);
EVENT_VALUE_DOUBLE(const STRING & expression);
EVENT_VALUE_DOUBLE(const CHAR * expression);
EVENT_VALUE_DOUBLE();
```

This
constructs an object of the EVENT_VALUE_DOUBLE class.

[表] Parameter
列: Parameter | Description
行 1:
  value
  A fixed number the object will represent.
行 2:
  expression
  The expression can be a spec or an equation variable.

### Member functions

### isExpression()
```
bool isExpression() const;
```

This
member function returns whether the object represents an expression (TRUE) or a
fixed value (FALSE).

### getExpression()
```
const STRING & getExpression() const;
```

This
member function returns the expression. If the object represents a fixed value the
expression string will be empty.

### getValue()
```
DOUBLE getValue() const;
```

This
member function returns the value. If the object represents an expression, the
returned value is 0. The expression is not resolved here!

### Example

Define a fixed double
value:

```
EVENT_VALUE_DOUBLE fixedValue(1.3);
```

Defines an
equation variable
reference:

```
EVENT_VALUE_DOUBLE eqnValue("LEV:frc1");
```

<!-- 语法节 end -->

## 是什么

**文档事实** EVENT_VALUE_DOUBLE 是一个 helper class，用于封装“值”的不同处理方式：值可以是固定值、spec 或 equation name。文档明确说明，该类不负责从 equation system 取出实际值，只指定执行时最终值的来源。

**文档事实** 所有 event 都支持 level equation set 中定义的 spec 与 equation variable；这些变量可用 `LEV:` 前缀引用，指向由 primaries 设置的当前 level equation set。

**文档事实** 该对象的能力：
- 用 `INT`、`FLOAT`、`DOUBLE` 构造时表示固定值。
- 用 `STRING` 或 `CHAR*` 表达式构造时表示 spec 或 equation variable。
- `isExpression()` 返回对象表示表达式（TRUE）还是固定值（FALSE）。
- `getExpression()` 返回表达式字符串；若对象表示固定值，返回空串。
- `getValue()` 返回固定值；若对象表示表达式，返回 0，且文档强调表达式不会在这里解析（"The expression is not resolved here!"）。
- 提供赋值运算符（可改固定值或表达式）以及 `==` / `!=` 比较运算符。
- 头文件：`/opt/hp93000/soc/prod_com/include/MAPI/Events.h`。

## 典型用法

**文档事实** 文档给出的两个基本用法：
- 固定值：`EVENT_VALUE_DOUBLE fixedValue(1.3);`
- equation variable 引用：`EVENT_VALUE_DOUBLE eqnValue("LEV:frc1");`

**文档事实** 赋值运算符允许在固定值与表达式之间改变对象内容；比较运算符用于判断两个对象是否相同。由于 `getValue()` 不解析表达式，需要实际数值时不能依赖它从表达式对象取值。

**推断** 从入边看，该类型主要作为事件类 API 的值参数/返回类型使用：例如 `EVENT_RANGE_CF.getIRange()` 文档称其“以 EVENT_VALUE_DOUBLE 对象返回”，EVENT_IC/ICVM/ICIM/IC_HAC 的 clamp/limit getter 也返回该类型。具体如何传入各事件应以对应 event 页面为准，本文不据此推断机台行为。

## 和谁有关

- 与 EVENT_VALUE_INT：文档 Related information 明确列出。正文说明把值分成两个 value class 是为了在编译期强制类型安全。
- 与 EVENT_VF、EVENT_VM、EVENT_IM、EVENT_VFIM、EVENT_VFVM：这些 event 页面在入边中链接到 EVENT_VALUE_DOUBLE（作为其值类型）。
- 与 EVENT_RANGE_VM、EVENT_RANGE_IM、EVENT_RANGE_CF：入边显示这些 range 类的 getter 返回 EVENT_VALUE_DOUBLE，例如 `EVENT_RANGE_CF.getIRange()`。
- 与 EVENT_IC、EVENT_ICVM、EVENT_ICIM、EVENT_IC_HAC：入边显示 `getIClampLow()` / `getIClampHigh()` / `getLimitLow()` / `getLimitHigh()` 等 getter 返回 EVENT_VALUE_DOUBLE。

以上关系来自文档正文、Related information 或入边语境，未据文档推断机台行为。

## 版本

`Functional changes`：Introduced in SmarTest 6.5.2。

## 出处

- `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.18_EVENT_VALUE_DOUBLE.htm`（正文、Class definition、Member functions、Operators、Example、Related information、Functional changes）。
- 关联判断另参考 `extract/edges.jsonl` 中指向该页的入边记录（EVENT_VALUE_INT、EVENT_VF/VM/IM、EVENT_RANGE_*、EVENT_IC* 等页面的引用语境）。
