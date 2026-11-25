---
type: object
title: PinPropertyMonitor
layer: L2
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.148_PinPropertyMonitor.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# PinPropertyMonitor

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **2,687 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.148_PinPropertyMonitor.htm>` 及其子主题 `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.148.01_PinPropertyMonitor.printStatus.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.148.02_PinPropertyMonitor.printStatus2File.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Class definition

### Constructor

```
PinPropertyMonitor();
PinPropertyMonitor(const ARRAY_I& sites, const string& pins);
PinPropertyMonitor(const ARRAY_I& sites, const string& pins, const string& instruments);
PinPropertyMonitor(const ARRAY_I& sites, const string& pins, const string& instruments, const string& property);
```

### Parameters

[表]
列: Parameter | Description
行 1:
  Instruments
  Possible options are: RELAY, PE_Driver,
    PE_Receiver, PE_Termination,
    PPMU,
    DPS, RELS, DPS128HC,
    CSAS, PSAS.

### Member functions
[表]
行 1:
  `printStatus()`（raw: `346545.htm`）
    
    `printStatus2File()`（raw: `346546.htm`）

### Example

```
ARRAY_I sites;
GET_ACTIVE_SITES(sites);
//string pinList = "SWITCH_R/4,SWITCH_R/2,SWITCH_R,SWITCH_2R";
pinList = "@";
PinPropertyMonitor ppm1(); //get tester status for all sites and pins
PinPropertyMonitor ppm1(sites, pinList); //get tester status for given sites and pins
PinPropertyMonitor ppm1(sites, pinList, "PPMU"); //filter by instrument "PPMU"
PinPropertyMonitor ppm1(sites, pinList, "PPMU", "slewI"); //filter by instrument "PPMU" and property "slewI"
```

### Syntax（取自子主题 PinPropertyMonitor.printStatus()）

```
PinPropertyMonitor & printStatus();
PinPropertyMonitor & printStatus(std::ostream& ss);
```
[表] Parameter
列: Parameter | Description
行 1:
  ss
  A string stream which holds the retrieved tester status for further output.

### Examples（取自子主题 PinPropertyMonitor.printStatus()）

### Example 1

The following example saves tester status in memory and then prints it to system control.

```
ARRAY_I sites;
GET_ACTIVE_SITES(sites);
PinPropertyMonitor ppm1(sites, "@");
ppm1.printStatus();
```

### Example 2

The following example saves tester status in memory as a string stream and then prints it to
system control.

```
ARRAY_I sites;
GET_ACTIVE_SITES(sites);
PinPropertyMonitor ppm1(sites, "@");
stringstream ss;
ppm1.printStatus(ss);
cout<<ss.str()<<endl;
```

### Syntax（取自子主题 PinPropertyMonitor.printStatus2File()）

```
PinPropertyMonitor & printStatus2File(const string& targetName, openmode openMode=NEW);
```
[表] Parameter
列: Parameter | Description
行 1:
  targetName
  A string given by user based on which the output files are named.
行 2:
  openmode
  Decides how to save the updated tester status when a named file exists.
    
    NEW keeps the existing file (for example a)
    and saves the updated tester status to a new file (for example a_1).
    
    Default value.
    
    OUT overwrites the existing file with the updated tester
    status.
    
    APP keeps the old contents in the existing file and appends the
    updated tester status at the end of the file.

### Example（取自子主题 PinPropertyMonitor.printStatus2File()）

```
ARRAY_I sites;
GET_ACTIVE_SITES(sites);
PinPropertyMonitor ppm1(sites, "@");
ppm1.printStatus2File("a", PinPropertyMonitor::NEW);
ppm1.printStatus2File("b", PinPropertyMonitor::OUT);
ppm1.printStatus2File("c", PinPropertyMonitor::APP);
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
