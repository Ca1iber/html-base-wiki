---
type: object
title: EVENT_BASE
layer: L3
stage: testmethod
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.01_EVENT_BASE.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# EVENT_BASE

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **604 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.01_EVENT_BASE.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Class definition

### Constructor

```
EVENT_BASE(const STRING & id);
EVENT_BASE( INT id);
```

### Member functions

```
void id(const STRING & id);
void id( INT id);
const STRING & getId() const;

bool operator == (const EVENT_BASE &) const;
bool operator != (const EVENT_BASE &) const;

virtual const STRING & getEventType() const = 0;
virtual bool hasXml() const = 0;
virtual void toXml(std::ostream& os) const = 0;
```

### Constructor

```
EVENT_BASE(const STRING & id);
EVENT_BASE( INT id);
```

This constructs an object of the EVENT_BASE class.

[表]
行 1:
  id
  Event identifier. It can be a string or an integer.

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
