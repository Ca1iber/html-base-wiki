---
type: object
title: EVENT_VALUE_INT
layer: L2
stage: testmethod
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.19_EVENT_VALUE_INT.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# EVENT_VALUE_INT

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,678 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.19_EVENT_VALUE_INT.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Class definition

### Constructor
```
EVENT_VALUE_INT(const INT value);
EVENT_VALUE_INT(const STRING & expression);
EVENT_VALUE_INT(const CHAR * expression);
EVENT_VALUE_INT();
```

### Member Functions
```
bool isExpression() const;
const STRING & getExpression() const;

INT getValue() const;
```

### Operators
```
EVENT_VALUE_INT & operator = (const EVENT_VALUE_INT &);
EVENT_VALUE_INT & operator = (INT);
EVENT_VALUE_INT & operator = (const STRING &);
EVENT_VALUE_INT & operator = (const CHAR *);

bool operator == (const EVENT_VALUE_INT &) const;
bool operator != (const EVENT_VALUE_INT &) const;
```

### Constructor
```
EVENT_VALUE_INT(const INT value);
EVENT_VALUE_INT(const STRING & expression);
EVENT_VALUE_INT(const CHAR * expression);
EVENT_VALUE_INT();
```

This
constructs an object of the EVENT_VALUE_INT class.

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

### getExpresssion()
```
const STRING & getExpression() const;
```

This
member function returns the expression. If the object represents a fixed value the
expression string will be empty.

### getValue()
```
INT getValue() const;
```

This member
function returns the value. If the object represents an expression, the returned
value is 0. The expression is not resolved here!

### Example

Defines a fixed double
value:

```
EVENT_VALUE_INT fixedValue(1);
```

Defines an
equation variable
reference:

```
EVENT_VALUE_INT eqnValue("LEV:frc1");
```

<!-- 语法节 end -->

## 是什么

**文档事实** `EVENT_VALUE_INT` 是一个 helper class，用于封装“值可能为固定值、spec 或 equation name”这三种情况的处理。它并不负责从 equation system 取实际值；它只指明“最终值在执行时从哪里取”。定义在 `/opt/hp93000/soc/prod_com/include/MAPI/Events.h`。

**文档事实** 文档说明所有 event 都支持 level equation set 中定义的 spec 与 equation variable；这些变量用 `LEV:` 前缀引用，指向由 primaries 设定的当前 level equation set。

**文档事实** 另有 `EVENT_VALUE_DOUBLE` 类；文档说明把值拆成两个类是为了在编译期强制类型安全（type safety at compile time）。

**文档事实** 该类提供四个构造函数：固定 `INT` 值、`STRING` 表达式、`CHAR *` 表达式、无参默认构造；成员函数为 `isExpression()`、`getExpression()`、`getValue()`；运算符包括对同类/`INT`/`STRING`/`CHAR *` 的赋值，以及同类之间的 `==`、`!=`。

## 典型用法

**文档事实** 文档示例只给出两种构造方式：固定值 `EVENT_VALUE_INT fixedValue(1);`，以及 equation variable 引用 `EVENT_VALUE_INT eqnValue("LEV:frc1");`。

**文档事实** `isExpression()` 返回对象表示的是表达式（`TRUE`）还是固定值（`FALSE`）。`getExpression()` 返回表达式；若对象表示固定值，返回的表达式字符串为空。`getValue()` 返回值；若对象表示表达式，返回值为 0，文档明确“表达式不在这里解析”（The expression is not resolved here!）。

**推断** 因为文档说明“所有 event 都支持 spec 与 equation variable”，`EVENT_VALUE_INT` 的实际用途是作为 event API 的整数值参数容器，用来区分“固定整数”和“level equation 变量引用”；具体哪些 event 以 `EVENT_VALUE_INT` 作参数，需查对应 event 页。

**建议** 不要在 `EVENT_VALUE_INT` 上期待取得表达式解析后的值：`getValue()` 对表达式固定返回 0；按文档，最终值是在执行时从它指明的来源取得的，本类只保存“来源”。

## 和谁有关

- **文档事实** 与 `EVENT_VALUE_DOUBLE`：主文档 `See also` 明确指向它，并说明拆分两个值类是为了编译期类型安全；入边显示 `EVENT_VALUE_DOUBLE` 页也回指 `EVENT_VALUE_INT`，两页互为对照。
- **文档事实** 与 DC events：`EVENT_...` 系列页面（`EVENT_VM`、`EVENT_IM`、`EVENT_VFIM`、`EVENT_VFVM`、`EVENT_CFIM`、`EVENT_CFVM`、`EVENT_ICIM`、`EVENT_ICVM`、`EVENT_VCIM`、`EVENT_VCVM`、`EVENT_FDM`、`EVENT_RDM` 及 `EVENT_WAVEFORM_*`）的入边都指向本页；其中多个 `getAverages()`/`averages` 页面明确写着“返回值以 `EVENT_VALUE_INT` 对象返回”，说明这些 event 的测量平均值用本类承载。
- **文档事实** 与 `EVENT_...__DC_events_API_reference`：该索引页的入边列出 `EVENT_VALUE_INT`，说明它属于 DC events API 体系的公共值类型。

## 版本

**文档事实** `Functional changes` 只记载 `Introduced in SmarTest 6.5.2`，未列后续变更。

## 出处

- `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.19_EVENT_VALUE_INT.htm`（Class definition、Member functions、Example、Related information、Functional changes）。
- 「和谁有关」另参考 `extract/edges.jsonl` 中指向该页的入边记录（各 `EVENT_*` 页与 `EVENT_VALUE_DOUBLE` 页的 context）。
