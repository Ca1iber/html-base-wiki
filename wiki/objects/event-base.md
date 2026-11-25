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

**文档事实**：`EVENT_BASE` 是所有具体 event 类型的 base class，提供对各类 event 做 generic handling 的接口，例如下载或绑定到 pattern 中的 test point（`02.07.04.01.63.01` 首段）。

**文档事实**：具体 event 类型由 specialized event classes 提供，分为 Force Events、Measurement Events、Combined Force & Measure Events、Set Measurement Range Events、Force Waveform Events、Measure Waveform Events、Combined Force & Measure Waveform Events；这些类在 GUI 中也同样显示（同页首段）。

**文档事实**：该 API 定义在 `/opt/hp93000/soc/prod_com/include/MAPI/Events.h`（同页首段）。

**文档事实**：`EVENT_BASE` 的接口是 `EVENT_BASE(const STRING& id)` / `EVENT_BASE(INT id)` 构造函数、`id()`（两个重载）/`getId()`、`operator==`/`operator!=`，以及三个纯虚函数 `getEventType()`、`hasXml()`、`toXml(std::ostream&)`；构造函数参数 `id` 是 event identifier，可为字符串或整数（同页 Class definition）。

**文档事实**：DC events 用于在 DC Scale pins 和标准 pin 的 PMU 上启动测量、控制电压或电流（`02.07.04.01.63` 首段）。

**推断**：`getEventType()`/`hasXml()`/`toXml()` 声明为 `= 0`，因此 `EVENT_BASE` 本身不是可实例化的具体事件类型；实际事件对象来自其派生类，基类用于统一持有/传递以及类型与 XML 查询（依据同页签名）。

## 典型用法

**文档事实**：本页没有给出直接创建 `EVENT_BASE` 的示例；文档的用法是由 specialized 派生类提供具体事件，基类提供 generic 接口（同页首段；各派生类页均说明 `derives from the EVENT_BASE class`）。

**文档事实**：构造 `EVENT_BASE` 时传入的 `id` 是 event identifier，字符串或整数均可（同页 Constructor 说明与参数表）。

**文档事实**：`getEventType()` 的返回类型是 `const STRING&`，`hasXml()` 返回 `bool`，`toXml()` 接受 `std::ostream&`；三者在基类中均声明为纯虚函数（`= 0`）（同页 Member functions）。

**文档事实**：DC events 的时序（各卡上 DC event 之间、或 pattern 末尾所需的最小 vector 数）在本页的 Timing of DC events 系列子主题中给出：`Timing of DC events`、`- XPS256`、`- DPS128 / DPS64`、`MSET timing of digital pins`（子主题列表；`03.05.01.13` 入边语境要求查本页各卡表格）。

**建议**：写 test method 时不要直接构造 `EVENT_BASE`；从需要的具体事件类（Force / Measure / Combined / Range / Waveform）构造对象，再用基类接口统一处理（依据同页 pure virtual 声明与「base class for all other specific event types」的定位）。

## 和谁有关

- **派生事件类（`02.07.04.01.63.02`–`.40`）** — **文档事实**：Force 类 `EVENT_CF`/`EVENT_IC`/`EVENT_VC`/`EVENT_VF`，Measurement 类 `EVENT_IM`/`EVENT_VM`，Combined 类 `EVENT_CFIM`/`EVENT_CFVM`、`EVENT_ICIM`/`EVENT_ICVM`、`EVENT_VCIM`/`EVENT_VCVM`、`EVENT_VFIM`/`EVENT_VFVM`，Range 类 `EVENT_RANGE_CF`/`EVENT_RANGE_IM`/`EVENT_RANGE_VM`/`EVENT_RANGE_RESTORE`，以及 `EVENT_WAVEFORM_*` 系列（CF/CFIM/CFVM、IC/ICIM/ICVM、VC/VCIM/VCVM、VF/VFIM/VFVM、IM/VM）、`EVENT_FILTER`、`EVENT_FDM`、`EVENT_RDM`、`EVENT_IC_HAC`；各页均写明 derives from `EVENT_BASE`（各页入边语境）。
- **EVENT_... (DC events API reference)** — **文档事实**：该页是 DC events API 的索引，列出上述 event classes 并说明 `EVENT_BASE` 是基类；其 Other events 表还列出 `EVENT_CMP`（`02.07.04.01.63`）。
- **Timing of DC events 系列** — **文档事实**：本页四个子主题给出 DC events 的时序与最小 vector 间隔（`02.07.04.01.63.01.01`–`.04`）。
- **动态 DC 测试调试用例** — **文档事实**：该用例要求「Refer to the tables for each card in section EVENT_BASE」来确定 DC events 之间或 pattern 末尾的最小 vector 数（`03.05.01.13` 入边语境）。
- **DC Scale / PMU** — **文档事实**：DC events 在 DC Scale pins 与标准 pin 的 PMU 上控制电压/电流并启动测量（`02.07.04.01.63` 首段）。
- **GUI** — **文档事实**：specialized event classes 在图形界面中同样显示（本页首段）；具体界面页文档未指名。

## 版本

**文档事实**（`02.07.04.01.63.01` 的 Functional changes）：

- Introduced in SmarTest 6.5.2

除此之外没有更细的版本变更记录；6.5.2 之前的情况文档未覆盖。

## 出处

- `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.63.01_EVENT_BASE.htm`（主文档，含 Class definition、Constructor 与 Functional changes）
- `02.07.04.01.63_EVENT_...__DC_events_API_reference.htm`（事件类清单）
- `02.07.04.01.63.01.01_Timing_of_DC_events.htm`、`.01.02_Timing_of_DC_events_-_XPS256.htm`、`.01.03_Timing_of_DC_events_-_DPS128___DPS64.htm`、`.01.04_MSET_timing_of_digital_pins.htm`
- `02.07.04.01.63.02`–`.63.40`（派生事件类页，用于派生关系）
- `03_Use_cases_and_application_papers/03.05_How_to_set_up_a_dynamic_DC_test/03.05.01.13_Debugging_the_dynamic_DC_test_setup.htm`
