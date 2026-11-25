---
type: object
title: FLEX_RELAY
layer: L2
stage: pin
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.68_FLEX_RELAY.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# FLEX_RELAY

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **27,676 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.68_FLEX_RELAY.htm>` 及其子主题 `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.240_TASK_LIST.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.68.01_FLEX_PIN_RELAY.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.68.02_FLEX_UTILITY_RELAY.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.68.03_FLEX_UTILITY_PURPOSE_RELAY.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.68.04_FLEX_UTILITY_CHANNEL_RES.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.69_FLUSH.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Class definition

This API is defined in the header file

/opt/hp93000/soc/prod_com/include/MAPI/FlexRelay.h
.

Constructor

```
FLEX_RELAY();
```

This constructor creates an object of the FLEX_RELAY class.

List of parameters
The constructor has no parameters.
Return value
The constructor has no return value.
Member functions

`pin()`（raw: `74892.htm#_74892__dle_pin`）

`util()`（raw: `74892.htm#_74892__dle_util`）

`util_channelRes()`（raw: `74892.htm#_74892__dle_util_channelRes`）

`util_purpose()`（raw: `74892.htm#_74892__dle_util_purpose`）

`wait()`（raw: `74892.htm#_74892__dle_wait`）

`execute()`（raw: `74892.htm#_74892__dle_execute`）

Using the class

For creating an object, which holds the settings of a
task:

```
FLEX_RELAY object;
```

For setting
up relays for the digital
channels:

```
object.pin("pinlist").member_func;
```

member_func
 is a member function of the
`FLEX_PIN_RELAY`（raw: `74898.htm`）
 class.

For
setting up utility lines (user relays) with utility line
names:

```
object.util("utilitylist").member_func;
```

member_func
 is a member function of the
`FLEX_UTILITY_RELAY`（raw: `74941.htm`）
 class.

For
setting up utility lines (user relays) with utility
purposes:

```
object.util_purpose("uti_purposelist").member_func;
```

member_func
 is a member function of the
`FLEX_UTILITY_PURPOSE_RELAY`（raw: `74899.htm`）
 class.

For
setting up utility lines (user relays) with utility channel
resources:

```
object.util_channelRes("channel_list").member_func;
```

member_func
 is a member function of the
`FLEX_UTILITY_CHANNEL_RES`（raw: `111118.htm`）
 class.

For
setting a wait time after controlling the relays specified in the task
when the task is
executed:

```
object.wait(time);
```

For executing the task defined with the
FLEX_RELAY
 API:

```
object.execute();
```

### Member functions

pin()
```
FLEX_PIN_RELAY& pin(const STRING& pinlist);
```

This member function specifies digital pins, and returns the reference to the
`FLEX_PIN_RELAY`（raw: `74898.htm`）
 class object that represents the setup data for
relays associated with the specified digital pins. To make a setting,
use the member function of the
FLEX_PIN_RELAY

API.

Parameter
[表]
列: Parameter | Description
行 1:
  pinlist
  A target pin name or pin group name of the
    digital channel pins. You can specify multiple
    pins and pin groups by separating with a
    comma.
    
    "@" specifies all the defined digital channel
    pins, including the digital pins that are used as
    the trigger source of the analog modules.
    
    All pins must be configured as i, o, io, or dc
    pin in the Pin Configuration window.
Return value
A reference to the
`FLEX_PIN_RELAY`（raw: `74898.htm`）
 class object.
util()
```
FLEX_UTILITY_RELAY& util(const STRING& utilitylist);
```

This member function specifies utility lines, and returns the reference to the
`FLEX_UTILITY_RELAY`（raw: `74941.htm`）
 class object that represents the setup data for
relays associated with the specified utility lines. To make a setting,
use the member function of the
FLEX_UTILITY_RELAY

API.

Parameter
[表]
列: Parameter | Description
行 1:
  utilitylist
  A utility line name or a list of utility line names separated with a comma. You
    can use the name defined in the `Utility Pins editor`（raw: `105637.htm`）.
Return value
A reference to the
`FLEX_UTILITY_RELAY`（raw: `74941.htm`）
 class object.
util_channelRes()
```
FLEX_UTILITY_CHANNEL_RES& util_channelRes (const STRING& channellist);
```

This member function specifies a list of utility line channel resources and returns the reference
to the
`FLEX_UTILITY_CHANNEL_RES`（raw: `111118.htm`）
 class object. To set the channel
resources, use the member functions of

FLEX_UTILITY_CHANNEL_RES
 API.

Parameter
[表]
列: Parameter | Description
行 1:
  channellist
  A utility line channel resource or a list
    of utility line channel resources separated with
    commas. It can be "@", that means all the utility
    line resources.
Return value
A reference to the
`FLEX_UTILITY_CHANNEL_RES`（raw: `111118.htm`）
 class object.
util_purpose()
```
FLEX_UTILITY_PURPOSE_RELAY& util_purpose(const STRING&utility_purposes);
```

This member function specifies utility purposes, and returns the reference to the
`FLEX_UTILITY_PURPOSE_RELAY`（raw: `74899.htm`）
 class object that represents the setup data for
relays associated with the specified utility lines. To make a setting,
use the member function of the

FLEX_UTILITY_PURPOSE_RELAY
 API.

Parameter
[表]
列: Parameter | Description
行 1:
  utility_purposes
  A utility purpose name or a list of utility purpose names separated with a comma.
    You can use the names defined in the `Utility Purpose Editor`（raw: `17603.htm`）.
Return value
A reference to the
`FLEX_UTILITY_PURPOSE_RELAY`（raw: `74899.htm`）
 class object.
wait()
```
void wait (const DOUBLE& time);
```

This member
function defines a wait time after controlling all relays in the task
when the task is executed.

Parameter
[表]
列: Parameter | Description
行 1:
  time
  Wait time for the task in seconds (s).
    
    Specify a positive value or zero.
Return value
There is no return value.
execute()
```
void execute();
```

This member function executes the
task defined with FLEX_RELAY.

This member function checks whether the
settings in the task are validated or not. If any error message is
generated, this member function performs no action, that is, any setting
is not downloaded to the hardware.

The sequence of the task
execution is as follows:

Download the settings of relays related to digital pins to the
hardware if defined.

Download the settings of utility lines specified with
util_purpose()/util() to the hardware if defined.

Wait for the specified time.

List of parameters
There are no parameters.
Return value
There is no return value.

### Examples

### Single site testing
```
//
// Construct TASK_LIST class object "tasklist1"
// and FLEX_RELAY class object "frelay".
//
TASK_LIST tasklist1;
FLEX_RELAY frelay;

//
// Set "PIN1" to Hi-Z by setting the AC, DC, PPMU relays to off.
//
frelay.pin("PIN1").set("IDLE","X");

// Use utility purposes "group1" and "group2":
//
// - "group1" definition: 16501:ON, 16502:ON, 16503:OFF.
// - "group2" definition: 16503:ON, 16504:OFF, 16505:ON.
//
// "16503" is included in both the groups. The setting of
// "16503" in "group1" is overwritten by the setting in "group2".
// Thus, "16503" is set to ON by the following statement.
//
frelay.util_purpose("group1,group2").set();

//
// Modify the previous utility line settings:
//
// Change 16501 to OFF.
// Change 16504 and 16506 to ON.
//
frelay.util("UTL101").off();
frelay.util("UTL104, UTL106").on();

//
// Add "frelay" of FLEX_RELAY to the task list.
//
tasklist1.add(frelay);

//
// Execute the tasklist1, that is, "frelay" task.
//
tasklist1.execute();
```

In the last statement,
frelay.execute()
 is called from the
`TASK_LIST`（raw: `29792.htm`）
 class object
tasklist1
 internally, and the task

frelay
 is executed. All the relay settings are download to
the hardware after checking whether the settings are validated or not. If an error
is found, this statement does nothing except displaying the error message.

You can also execute the
frelay
 task by executing the

frelay.execute()
 statement.

### Multi-site testing
```
STRING utilgrp = "UTL1, UTL2, UTL3, UTL4, UTL5";

//
// "UTL1" to "UTL5" are the following utility lines
//
// For Site1: 16501, 16502, 16503, 16504, 16505
// For Site2: 16506, 16507, 16508, 16509, 16510
//
STRING setting_1 = "1,1,1,0,0";
STRING setting_2 = "0,1,1,0,1";

FLEX_RELAY frelay;

ON_FIRST_INVOCATION_BEGIN();

//
// common setting in all sites;
//
frelay.pin("PIN1").set("IDLE");

//
// site-specific settings
//
FOR_EACH_SITE_BEGIN();

INT site = CURRENT_SITE_NUMBER();

if(site == 1)
{
frelay.util(utilgrp).set(setting_1);
}
else if(site == 2)
{
frelay.util(utilgrp).set(setting_2);
}

FOR_EACH_SITE_END();

//
// Download the relay settings to the hardware
//
frelay.execute();

//
// Execute a test here
//
...
...

ON_FIRST_INVOCATION_END();
```

### Class definition（取自子主题 FLEX_PIN_RELAY）

This API is defined in the header file

/opt/hp93000/soc/prod_com/include/MAPI/FlexPinRelay.h
.

Constructor
This class is always called as the subsidiary data container of the
`FLEX_RELAY`（raw: `74892.htm`）
,
API. Therefore, the
FLEX_PIN_RELAY
 class does not have a
public constructor.
Member functions
In this class, the following public member functions are defined:

`set()`（raw: `74898.htm#_74898__dlentry_set`）

`setTMU()`（raw: `74898.htm#_74898__dlentry_setTMU`）

### Member functions（取自子主题 FLEX_PIN_RELAY）

set()

```
FLEX_PIN_RELAY& set (const STRING& pin_mode, const STRING& dc_target="X");
FLEX_PIN_RELAY& set (const STRING& pin_mode, const STRING& dc_target, const STRING& mux_select);
```

This member function defines the relay settings, which are applied to the
hardware when the task is executed.

Parameters
[表]
列: Parameter | Description
行 1:
  pin_mode
  This parameter controls per-pin relays (AC, DC
    and pin PMU relays) of the digital channels.
    
    The following options are available:
      [子表]
      子行 1:
        "X"
        The settings of all the relays remain
          unchanged.
      子行 2:
        "IDLE"
        Disconnects all the relays (AC, DC, and pin
          PMU relays). Use this option to set the digital
          pin to Hi-Z by disconnecting the relays.
      子行 3:
        "AC"
        Connects a DUT pin to its associated
          digital channel. Use this option for example when
          you return the disconnected digital pin to the
          state same as the connect state where the AC relay
          is closed for the i/o/io pin.
      子行 4:
        "DC"
        Closes the DC relay.
      子行 5:
        "PPMU"
        Closes the pin PMU relay to connect the pin
          to the Pin-PMU
      子行 6:
        "ACDC"
        Closes both the AC and DC relays.
      子行 7:
        "BOTH"
        Identical to ACDC.
      子行 8:
        "ACPM"
        Closes both the AC and the pin PMU
          relays.
      子行 9:
        "DCPM"
        Closes both the DC and pin PMU
          relays.
      子行 10:
        "ALL"
        Closes all the relays (AC, DC, and pin PMU
          relays).
      子行 11:
        "CNCT"
        Special connect mode: for all I, O, IO pins
          AC relay closed, for all DC pins AC relay
          open.
    
    For utility DC pins, only the pin modes
    "IDLE",
    "CNCT", and
    "X" are supported.
行 2:
  dc_target
  This optional parameter specifies the resource
    to be connected when the DC relay is closed. The
    ISOL and other
    relays are controlled. The default setting
    ("X") does not change any of
    these relays. Thus, you can omit this parameter
    for example when you set the digital pins to Hi-Z,
    and returns them to the state same as the connect
    state where the AC relays are closed for the
    i/o/io pins.
    
    This parameter is identical to the dc_target parameter of the `RLYC`（raw: `98721.htm`） firmware command. You
    can specify any "enum" value of the RLYC
    dc_target parameter. The
    "enums" specify fixed combinations of relay
    settings, necessary to perform certain
    functions.
    
    As an alternative you can control the relays individually using the string entry (not supported for utility DC pins). This has the format:
    "CCCCC", where each character "C" represents a relay on a channel board or a Clock
    board. Each "C" can take the value 0, 1, or X, where a 0/1 opens/closes the relay(s)
    respectively and an X leaves it unchanged. For example,
    flexObj.set("DC","11100").
    
    Going
    from left to right:
    
    Character 1 - ISOL relay on channel board
    
    Character. 2 - GND relay on channel board
    
    Character. 3 - PMU relay on channel board
    (BADC)
    
    Character. 4 - EXT relay on Clock board
    
    Character. 5 - DUT relay on Clock board
    
    For details, see the description of the
    dc_target parameter of the
    `RLYC, RLYC? - (ReLaY Control)`（raw: `98721.htm`） command in the Command
    Reference.
行 3:
  mux_select
  This optional parameter connects the board
    ADC for the High Impedance measurement mode, or
    for the measurement path through the pin PMU. In
    this case you can connect only one pin PMU per
    board with the ADC, as there is only one ADC per
    board.
    This preparation is needed for
    pattern-controlled measurements.
    
    Note that
    for high-voltage pins only high-impedance
    measurements (VM_HIZ) can be executed in the
    pattern run.
    
    These are the options:
      [子表]
      子行 1:
        "MUX_VM_HIZ"
        Connects the ADC for the High Impedance
          measurement mode.
          Note
          
          The pin_mode parameter
          should be set to "DC" to
          connect the pin to the DC line.
          
          The dc_target parameter
          should be set to "PMU" to
          connect the BADC relay with the board ADC.
      子行 2:
        "MUX_PPMU"
        Connects the ADC to the Pin PMU.
          Note
          
          The pin_mode parameter
          should be set to "PPMU" to connect the pin to the
          pin PMU.
          
          The dc_target parameter can
          be ignored and set to
          ""X"".
Return value
A reference to the
FLEX_PIN_RELAY
 class object.
setTMU()

```
FLEX_PIN_RELAY& setTMU (const STRING& connect);
```

This member function defines the TMU connection mode and TMU input relay
settings, which are applied to the hardware when the task is executed.
This member function is currently available for TMU inputs of DC Scale
cards only.

The TMU input relay settings are independent from the output relay settings of channel. The
TMU relay settings are not changed by the member function
`FLEX_PIN_RELAY::set()`（raw: `74898.htm`）
 that is described
above.

Parameter
[表]
列: Parameter | Description
行 1:
  connect
  This parameter defines the connection mode
    and the input relay state of the TMU.
    
      [子表]
      子行 1:
        "HIGH_BW"
        Closes the TMU input relays in the
          high-bandwidth connection mode.
      子行 2:
        "HIGH_IMP"
        Closes the TMU input relays in the
          high-impedance connection mode.
      子行 3:
        "HIGH_SPEED"
        Closes the input relay of the TMU_H# pogo
          pin when the high-speed comparator has been
          selected.
          Not
          currently supported by any cards.
      子行 4:
        "IDLE"
        Opens the TMU the output relays.
          This is
          the default state.
Return value
A reference to the
FLEX_PIN_RELAY
 class object.

### Class definition（取自子主题 FLEX_UTILITY_RELAY）

This API is defined in the header file

/opt/hp93000/soc/prod_com/include/MAPI/FlexUtilRelay.h
.

Constructor
This class is always called as the subsidiary data container of the
`FLEX_RELAY`（raw: `74892.htm`）
,
API. Therefore, the
FLEX_UTILITY_RELAY
 class does not
have a public constructor.
Member functions
In this class, the following public member functions are defined:

`set()`（raw: `74941.htm#_74941__dle_set`）

`on()`（raw: `74941.htm#_74941__dle_in`）

`off()`（raw: `74941.htm#_74941__dle_off`）

### Member functions（取自子主题 FLEX_UTILITY_RELAY）

set()
```
FLEX_UTILITY_RELAY& set (const STRING& conditions);
```

This
member function defines the setting for each of the specified utility lines.

Parameter
[表]
列: Parameter | Description
行 1:
  conditions
  This parameter is a list of "0", "1", and "x"
    separated with a comma, or a list of "0","1","x"
    and " " (space), which represents the settings of
    the utility lines in the same order as specified
    in the parameter of the FLEX_RELAY util() member
    function. "0" sets the user relay to off, "1" sets
    it to on, and "x" remains it unchanged. For
    example, "0,0,0,0,1,1,x,1" or "0000 11x1". You may
    enter a space between values, or may omit it.
    
    For example, the following statements set UTL1
    to on, UTL2 to off, UTL3 to be unchanged.
    
    ```
    FLEX_RELAY relay;
    relay.util("UTL1, UTL2, UTL3").set("1,0,x");
    [ or relay.util("UTL1,UTL2,UTL3").set("10x"); ]
    ```
    
    The number of listed settings must be equal to
    the number of the specified utility lines.
Return value
A reference to the
FLEX_UTILITY_RELAY
 class object.
on()
```
FLEX_UTILITY_RELAY& on();
```

This member function sets the user relays connected to the specified utility lines to on.
List of parameters
There are no parameters.
Return value
A reference to the
FLEX_UTILITY_RELAY

class object.

off()
```
FLEX_UTILITY_RELAY& off();
```

This member function sets the user relays connected to the specified utility lines to off.
List of parameters
There are no parameters.
Return value
A reference to the
FLEX_UTILITY_RELAY

class object.

### Class definition（取自子主题 FLEX_UTILITY_PURPOSE_RELAY）

This API is defined in the header file

/opt/hp93000/soc/prod_com/include/MAPI/FlexUtilPurposeRelay.h
.

Constructor
This class is always called as the subsidiary data container of the
`FLEX_RELAY`（raw: `74892.htm`）
,
API. Therefore, the
FLEX_UTILITY_PURPOSE_RELAY
 class does
not have a public constructor.
Member functions
In this class, the following public member functions are defined:

`set()`（raw: `74899.htm#_74899__dle_set`）

### Member function（取自子主题 FLEX_UTILITY_PURPOSE_RELAY）

set()
```
FLEX_UTILITY_PURPOSE_RELAY& set();
```

This member
function specifies the utility line settings with the utility
purposes.

List of parameters
There are no parameters.
Return value
A reference to the
FLEX_UTILITY_PURPOSE_RELAY

class object.

### Class definition（取自子主题 FLEX_UTILITY_CHANNEL_RES）

This API is defined in the header file

/opt/hp93000/soc/prod_com/include/MAPI/FlexUtilChannelRes.h
.

Constructor
This class is always called as the subsidiary data container of the
`FLEX_RELAY`（raw: `74892.htm`）
,
API. Therefore, the
FLEX_UTILITY_CHANNEL_RES
 class does
not have a public constructor.
Member functions
In this class, the following public member functions are defined:

`set()`（raw: `111118.htm#_111118__dle_set`）

`on()`（raw: `111118.htm#_111118__dle_on`）

`off()`（raw: `111118.htm#_111118__dle_off`）

### Member functions（取自子主题 FLEX_UTILITY_CHANNEL_RES）

set()
```
FLEX_UTILITY_CHANNEL_RES& set(const STRING& conditions);
```

This
member function defines the setting for each of the specified utility
line channel resources.

Parameter
[表]
列: Parameter | Description
行 1:
  conditions
  The settings of the utility line channel
    resources in the same order as the resources
    specified in the `util_channelRes()`（raw: `74892.htm#_74892__dle_util_channelRes`） member
    function of `FLEX_RELAY`（raw: `74892.htm`）. It is a list
    of "0", "1" or "x" separated with commas or
    spaces. "0" means setting the relay to off. "1"
    means setting the relay to on. "x" means no status
    change for the relay.
Return value
A reference to the
FLEX_UTILITY_CHANNEL_RES

class object.
on()
```
FLEX_UTILITY_CHANNEL_RES& on();
```

This member
function sets the specified utility line channel resources to on.

List of parameters
There are no parameters.
Return value
A reference to the
FLEX_UTILITY_CHANNEL_RES
 class object.
off()
```
FLEX_UTILITY_CHANNEL_RES& off();
```

This member
function sets the specified utility line channel resources to off.

List of parameters
There are no parameters.
Return value
A reference to the
FLEX_UTILITY_CHANNEL_RES
 class object.

### Example（取自子主题 FLEX_UTILITY_CHANNEL_RES）

```
FLEX_RELAY flexRelay;
flexRelay.util_channelRes("UTI101,UTI102,UTI201").set("110");
flexRelay.util_channelRes("UTI301,UTI302").on();
flexRelay.util_channelRes("UTI401,UTI402").off();
flexRelay.execute();
```

This example sets the utility channel 101, 102, 301 and
302 to on and sets the utility channel 201, 401 and 402 to off.

### Syntax（取自子主题 FLUSH）

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

### Example（取自子主题 FLUSH）

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

### Class definition（取自子主题 TASK_LIST）

This API is defined in the header file

/opt/hp93000/soc/prod_com/include/MAPI/TaskList.h
.

Constructor

```
TASK_LIST();
```

This constructor defines a task list that holds task names to be
executed.

Parameters

There are no parameters associated with this function.

Member functions:

`add()`（raw: `29792.htm#_29792__dle_add`）

`setup()`（raw: `29792.htm#_29792__dle_setup`）

`execute()`（raw: `29792.htm#_29792__dle_execute`）

### Usage（取自子主题 TASK_LIST）

For creating an object:

```
TASK_LIST <object>;
```

For setting up tasks to be performed:

```
<object>.add(task1).add(task2)...add(taskN);
```

For downloading the settings in tasks:

```
<object>.setup();
```

For downloading the settings in tasks and performing the tasks:

```
<object>.execute();
```

[表]
行 1:
  <object>
  Object name to be defined
行 2:
  task1-N
  Object name of the PPMU_SETTING, PPMU_RELAY or
    PPMU_MEASURE class to specify a task to
    be performed. A task list can contain up to 10 tasks.

### Member functions（取自子主题 TASK_LIST）

add()

```
TASK_LIST & add(const TASK& task);
```

This function adds the specified task to the task list. Added tasks are
performed sequentially.

Note
 If you define a
TASK_LIST
 object as
global, the object will not be destroyed when the test method is
completed. This will have the effect that the list grows longer with
every testflow repetition, so that the test time is increased with every
repetition.

[表] Parameter
行 1:
  task
  Object name of the PPMU_SETTING, PPMU_RELAY or
    PPMU_MEASURE class to specify a
    task be performed.

Using the offline result emulation function:

Measurements can be made by using
`DPS_TASK`（raw: `55630.htm`）
,
`SPMU_TASK`（raw: `55670.htm`）
, and

`PPMU_MEASURE`（raw: `29585.htm`）
 objects directly (by calling their

execute()
 member functions) or be put in a

TASK_LIST
 object which queues up tasks to be executed (by calling
the
execute()
 method on the
TASK_LIST
 object
rather than on the task objects themselves). This requires an enhancement also on the

TASK_LIST add()
 method which takes a measurement name as
additional parameter.

```
TASK_LIST& add(const TASK& task)
```

This is the existing function which adds the specified task to the task list.

```
TASK_LIST& add(const TASK& task, const string& measurementName)
```

This function adds the specified task to the task list.

Parameter

[表]
行 1:
  measurementName
  Associate the measurement that will be executed by calling
    task_list.execute() with offline data.

For more details, see
`Parametric offline result emulation`（raw: `128581.htm`）
 in
`Offline Result Emulation`（raw: `128475.htm`）
.

setup()

```
void setup();
```

This function downloads settings defined in the task list. The tasks of
the task list are executed sequentially in the registered order. It is
used when the input parameters of the task are changed during the test
method execution. It can change the parameters of an exisiting MSET and
reuse it to avoid running out of MSETs. (Refer to
`FlexDC`（raw: `122087.htm`）
 and
`Managing DC Tests with Variable Parameters`（raw: `75890.htm`）
 for details.)

Parameters

There are no parameters associated with this function.

execute()

```
void execute();
```

This function performs a test by executing the task list. The tasks of
the task list are executed sequentially in the registered order.

Parameters

There are no parameters associated with this function.

Note
 After the
execute()
 function is performed, you cannot
define any tasks for the digital pin that is not included to the
performed task. For example, the following program defines and executes
the "tasks" task list.

```
PPMU_SETTING setting1;
TASK_LIST tasks;

tasks.add(setting1);

setting1.pin("pin1").vForce(2.1 mV);
setting1.pin("pin1").iRange("10uA");
setting1.pin("pin1").min(0.1 uA).max(5.0 uA);

tasks.execute();
```

After that, you can modify or define tasks for "pin1" as shown below:

```
setting1.pin("pin1").vForce(2.5 mV); // OK
```

However, error occurs if the following program is performed because tasks
for "pin2" is not defined in the "tasks" task list.

```
setting1.pin("pin2").vForce(2.1 mV); // error
```

### Example（取自子主题 TASK_LIST）

In the following example, the task
setting
,
precharge
,

relay_on
,
relay_off
,

ppmuMeasure
,
clamp_on
 and

clamp_off
 are defined and added to the task list. Then a PPMU
measurement is performed by executing the task list.

```
PPMU_SETTING ppmuSetting;
PPMU_RELAY ppmuRelay_on, ppmuRelay_off;
PPMU_MEASURE ppmuMeasure;
PPMU_CLAMP ppmuClamp_on, ppmuClamp_off;
TASK_LIST taskList_1;

ON_FIRST_INVOCATION_BEGIN();

//
// Setups for PPMU
//
ppmuSetting.pin("S0").iRange(1 mA).min(0 V).max(4.3 V).iForce(10 uA);
ppmuSetting.pin("S1").iRange(10 mA).min(-10 uA).max(30 uA).vForce(3.3 V);

//
// Relay setups
//
ppmuRelay_on.pin("S0,S1").status("PPMU_ON");
ppmuRelay_on.wait(1.3 ms);
ppmuRelay_off.pin("S0,S1").status("AC_ON");

//
// Measurement setups
//
ppmuMeasure.pin("S0,S1").execMode(TM::PVAL);

//
// Hardware specific programming to avoid hot switching on the current force setup
//
ppmuClamp_on.pin("S0").status("CLAMP_ON").low(2.6 V).high(2.9 V);
ppmuClamp_off.pin("S0").status("CLAMP_OFF");

//
// Build and execute the task list
//
taskList_1.add(ppmuSetting)
.add(ppmuClamp_on)
.add(ppmuRelay_on)
.add(ppmuClamp_off)
.add(ppmuMeasure)
.add(ppmuRelay_off);

taskList_1.execute();

ON_FIRST_INVOCATION_END();

//
// Result upload and Datalog
//
double VMeas, IMeas;

VMeas = ppmuMeasure.getValue("S0");
IMeas = ppmuMeasure.getValue("S1");

TEST("DC_Test",ppmuMeasure, true);
```

The following example shows how to measure a current on a device pin and then use it
as a force value for a following measurement for multi-sites. The result value of
the first measurement differs from site to site.

```
PPMU_MEASURE ppmuMeasure2;

ON_FIRST_INVOCATION_BEGIN();

PPMU_MEASURE ppmuMeasure1;
PPMU_SETTING ppmuSetting1,ppmuSetting2;
PPMU_RELAY ppmuRelayOn, acRelayOn;
TASK_LIST multiDeltaFlexDc1, multiDeltaFlexDc2;

// 1st measurement
ppmuSetting1.pin("I/O1").vForce(0 V).iRange(1 uA).max(1 uA).min(-1 uA);
ppmuRelayOn.pin("I/O1").status("PPMU_ON");
ppmuRelayOn.wait(1.3 ms);
ppmuMeasure1.pin("I/O1").execMode(TM::PVAL);
acRelayOn.pin("I/O1").status("AC_ON");
multiDeltaFlexDc1.add(ppmuSetting1).add(ppmuRelayOn).add(ppmuMeasure1);
multiDeltaFlexDc1.execute();

// dummy setting for avoiding DC set run out
ppmuSetting2.pin("I/O1").iForce(0 uA).iRange(1 mA).max(0.5 V).min(-0.5 V);
ppmuSetting2.wait(1 ms);
ppmuMeasure2.pin("I/O1").execMode(TM::PVAL);
multiDeltaFlexDc2.add(ppmuSetting2).add(ppmuMeasure2).add(acRelayOn);
multiDeltaFlexDc2.setup();

// 2nd measurement
FOR_EACH_SITE_BEGIN();

ppmuSetting2.pin("I/O1")
.iForce(ppmuMeasure1.getValue("I/O1"))
.iRange(ppmuMeasure1.getValue("I/O1"))
.max(0.5 V)
.min(-0.5 V);

FOR_EACH_SITE_END();

multiDeltaFlexDc2.execute();

ON_FIRST_INVOCATION_END();

TEST("I/O1",
"multi_delta",
ppmuMeasure2.getPassFail("I/O1")?TM::Pass:TM::Fail,
ppmuMeasure2.getValue("I/O1"),
true );
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
