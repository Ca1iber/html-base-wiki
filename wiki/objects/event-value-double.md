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

（待补）

## 典型用法

（待补）

## 和谁有关

（待补）

## 版本

（待补）

## 出处

（待补）
