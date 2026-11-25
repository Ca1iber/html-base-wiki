---
type: object
title: FLUSH
layer: L2
stage: run
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.69_FLUSH.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# FLUSH

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,711 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.69_FLUSH.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
void FLUSH();
void FLUSH(const TM::FLUSH_POST_ACTION action);
void FLUSH(bool force);
void FLUSH(TM::FLUSH_POST_ACTION action, bool force);
void FLUSH(TM::FLUSH_SECTION_TYPE flush_section);
void FLUSH(bool force, TM::FLUSH_SECTION_TYPE flush_section);
void FLUSH(TM::FLUSH_POST_ACTION action, bool force, TM::FLUSH_SECTION_TYPE flush_section);
```
[表] Parameters
行 1:
  action
  This parameter controls how the setup data will be downloaded
    to the hardware.
    
    You can leave it empty or use TM::APRM.
    
    When using the TM:APRM option, the command
    `APRM`（raw: `98485.htm`） with
    mode set to CNL will
    be issued following the normal FLUSH()
    actions.
行 2:
  force
  When to execute the firmware command `FLSH`（raw: `99061.htm`） and `WSDN`（raw: `99082.htm`）. It can
    be:
    
    true: always executes the firmware command `FLSH`（raw: `99061.htm`） and `WSDN`（raw: `99082.htm`） (default)
    
    false: only executes the firmware
    command `FLSH`（raw: `99061.htm`） and `WSDN`（raw: `99082.htm`） when necessary.
行 3:
  flush_section
  This parameter allows you to set which types of APIs to flush.
    You can use the
    following options:
    
    TM::FLUSH_PRIMARY`1)`（raw: `#fntarg_1`）,
    
    TM::FLUSH_UTIL`2)`（raw: `#fntarg_2`）,
    
    TM::FLUSH_ALL,
    
     or a combination hereof.

This API is defined in the header file

/opt/hp93000/soc/prod_com/include/MAPI/MapiFuncs.h.

### Example

### TM::FLUSH_PRIMARY / UTIL

```
Routing.util("UTI1").on();
Primary.getLevelSpec().change("S_VCC", 4.45);
FLUSH(TM::FLUSH_PRIMARY | TM::FLUSH_UTIL);
```

Alternatively:

```
TM::FLUSH_SECTION_TYPE flushType;
flushType = TM::FLUSH_UTIL | TM::FLUSH_PRIMARY;

Routing.util("UTI1").on();
Primary.getLevelSpec().change("S_VCC", 4.45);
FLUSH(flushType);
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
