---
type: object
title: VEC_EVENTS
layer: L2
stage: pattern
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.267_VEC_EVENTS.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# VEC_EVENTS

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **5,356 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.267_VEC_EVENTS.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Class definition

Member functions:

`insert(...)`（raw: `116944.htm#_116944__dlentry_insert`）

`reinsert(...)`（raw: `116944.htm#_116944__dlentry_reinsert`）

`update(...)`（raw: `116944.htm#_116944__dlentry_update`）

`remove(...)`（raw: `116944.htm#_116944__dlentry_remove`）

`remove(...)`（raw: `116944.htm#_116944__dlentry_remove`）

`clear()`（raw: `116944.htm#_116944__dlentry_clear`）

`clearAll()`（raw: `116944.htm#_116944__dlentry_clearAll`）

`setup()`（raw: `116944.htm#_116944__dlentry_setup`）

### Member functions

insert(...)

```
VEC_EVENTS & insert(INT vector, const EVENT_BASE & event);
```

This member function inserts an event at the specified anchor vector.
Both, event and test point will be created. Note that the event and the
test point must not exist.

reinsert(...)

```
VEC_EVENTS & reinsert(INT vector, const STRING & eventId);
```

This member function inserts a test point referring to an existing event.
Note that the event must exist but not the test point.

update(...)

```
VEC_EVENTS & update(const EVENT_BASE & event);
```

This member function updates an existing event instance. If the event has
been inserted multiple times at different, vectors, all these locations
will be affected.

remove(...)

```
VEC_EVENTS & remove(INT vector);
```

This member function removes an existing test point. If the referenced
event is no longer referenced by other test points, it will be removed.
Note that the test point must exist.

```
VEC_EVENTS & remove(const STRING & eventId);
```

This member function removes an existing event and all test points that
refer to this event. Note that the event must exist.

[表] Parameters
行 1:
  vector
  Existing test point
行 2:
  eventID
  ID of an existing event
clear()

```
VEC_EVENTS & clear();
```

This member function removes all test points and events defined by this
API.

clearAll()

```
VEC_EVENTS & clearAll();
```

Use with care!

This member function removes all test points and events in the pattern,
independent of whether they have been defined by this API or manually
via user interaction, at the next call of VEC_EVENTS::setup(),
PATTERN_CONTROLLER::setup(), or PATTERN_CONTROLLER::execute().

setup()

```
void setup();
```

This member function forces the immediate download of the defined setup.

### Examples

### Example 1: Insert events into a pattern, replace an event on a single site

This example shows how events can be inserted into a
pattern and incrementally changed between test executions on a per site granularity.
Three events (frc1V, frc2V, frc3Vmeas) drive a ramp, while only the second force
voltage is measured via the third event (frc3Vmeas). In the example, the second
event on site 2 is replaced by an event that additionally measures the first force
voltage.

```
PATTERN_CONTROLLER patController;
DC_RESULT_ACCESSOR results;
ARRAY_D values;

ON_FIRST_INVOCATION_BEGIN();
{
//
// Insert events on pin Vdd1 in pattern "myRamp"
//
PATTERN & pattern(patController.label("myRamp"));

//
// Start from scratch with 2 force voltage events
//
EVENT_VF frc1V("frc1V"); frc1V.vForce(1 V);
EVENT_VF frc2V("frc2V"); frc2V.vForce(2 V);
EVENT_VFVM frc3Vmeas("frc3Vmeas"); frc3Vmeas.vForce(3 V);

pattern.vecEvents("Vdd1")
.clear()
.insert(100, frc1V)
.insert(200, frc2V)
.insert(300, frc3Vmeas);

//
// Execute the pattern and upload results
//
patController.execute();

results.uploadResult("Vdd1", TM::RESULT_INDEX);

FOR_EACH_SITE_BEGIN()
{
//
// Get measurement values for Vdd1 per site
//
results.getValues("Vdd1", values);
...
...
}
FOR_EACH_SITE_END();

//
// Now replace the event frc2V by frc2Vmeas on site 2 only
//

ARRAY_I oldSites;

GET_TEST_FOCUS(oldSites); // Get current setup-focused sites

if ( SET_TEST_FOCUS(2) ) // Select site 2 if available
{
VEC_EVENTS& site2_event(pattern.vecEvents("Vdd1"));

site2_event.remove(200)
.insert(200, EVENT_VFVM("frc2Vmeas").vForce(2 V));
}

SET_TEST_FOCUS(oldSites); // Restore setup sites

//
// Execute the pattern and upload results
//
patController.execute();

results.uploadResult("Vdd1", TM::RESULT_INDEX);
}
ON_FIRST_INVOCATION_END();

//
// Get measurement values for Vdd1 per site
//
results.getValues("Vdd1", values);

...
...
```

### Example 2: clearAll() member function

This example demonstrates the use of the

clearAll()
 member function. Be careful! It removes all events,
independent of whether they were defined by the API or
manually.

```
PATTERN_CONTROLLER pc;

ON_FIRST_INVOCATION_BEGIN();
{
PATTERN & pattern(pc.label("pat1", "@"));

VEC_EVENTS & vecEvents(pattern.vecEvents("Vdd1"));

// Schedules a forced clear of all events defined on the pin Vdd1.
// All events will be removed, independent of whether they were defined
// by the API or added manually. So be careful.
vecEvents.clearAll();

// Execute the removal step.
// Actually you may have also new events defined before the setup() call.
// Then the events will first be removed and the new ones will be defined afterwards.
vecEvents.setup();

// Instead of calling vecEvents.setup() you may also only call pc.setup(),
// which will do the changes for all patterns at once. In this example here
// the deletion of the events has happened already during vecEvents.setup().
// Therefore pc.setup() has no effect and will be an NOP.
pc.setup();
}
ON_FIRST_INVOCATION_END();
```

### Example 3: Setup per site

For an example that shows how to program an setup per site by DC events, refer to
`DC event example: Setup per site`（raw: `345918.htm`）
.

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
