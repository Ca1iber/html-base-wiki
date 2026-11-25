---
type: object
title: RDI_Configure file
layer: file
stage: testmethod
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.13.04_RDI_Configure_file.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# RDI_Configure file

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **5,848 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.13.04_RDI_Configure_file.htm>` 及其子主题 `<02_System_reference/02.07_Test_Method_Reference/02.07.13.04.01_Example_of_keyword_setups_in_the_RDI_Configure_file.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.04.02_getRdiConfig.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.01.02_execute.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.02.01_clearPinStatus.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.02.02_setPinStatus.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.08.02_Changing_the_default_pin_status_with_SmartRDI.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.23.01_pin.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.23.02_setOff.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.23.03_setOn.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.23.04_Sequencer_Controlled_Utility_Mask_with_SmartRDI.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.13.23_SmartRDI__Utility_lines_control.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Example of keyword setups in the RDI_Configure file）

```
// UTIL setup
UTIL_BLOCK = 12,34,5,6,7,8
UTIL_FRAM = UL_FRAM1,UL_FRAM3,UL_FRAM5,UL_FRAM6,UL_FRAM7,UL_FRAM8
UTIL_SCLK = UL_SCLK,UL_SCLK3,UL_SCLK,UL_SCLK,UL_SCLK,UL_SCLK
UTIL_SINP = UL_SINP,UL_SINP3,UL_SINP,UL_SINP,UL_SINP,UL_SINP
UTIL_SOUT = UL_SOUT,UL_SOUT3,UL_SOUT,UL_SOUT,UL_SOUT,UL_SOUT
UTIL_CTRL_MAX_SPEED = 2e6
UTIL_DYN_MASK_UNSPECIFIED_PIN = FALSE
UTIL_DYN_MASK_INACTIVE_SITE = TRUE
# UTIL_PADDING_RPTV_FLAT

// SmartVec setup
VEC_EDIT_MODE = VTT
DEFAULT_EMAP_LOCATION = TP
DEFAULT_SMV_READ_MODE = EMAP
SMV_DIGCAP_AUTO_BURSTUPLOAD = FALSE
SMV_VEC_MEM_TYPE = SHMEM
USER_NAMED_PATTERN_CONTENT_CHECK = FALSE

// Default pin status
DEFAULT_STATUS_PIN = pinA,pinB
DEFAULT_STATUS_INDEX = 0,1

// Setup name
ANALOG_SET_NAME_MD5 = TRUE
BURST_NAME_MD5 = TRUE

// PPMU setup
PPMU_DEFAULT_RELAY = NO
PPMU_DEFAULT_VALUE_MODE = SA

// Pass or fail per label
PER_LABEL_FUNC_RESULT_MODE = FLBL
PER_LABEL_FUNC_RESULT_NO_BREAK_VEC = TRUE

// ORE setup
ORE_FILE = " "
ENABLE_ORE = FALSE
ORE_TEMPLATE_BY_USER_CODE = TRUE

// Upload
DC_BURST_SITE_UPLOAD = TRUE
DIGCAP_ADAPTIVE_RESULT_SIZE = TRUE
DIGCAP_BURST_SITE_UPLOAD = TRUE

// Debug
REPORT_RESULT_IN_SINGLE_MODE = TRUE
ENABLE_RDI_INFO_LOG_FILE = TRUE

// SMC execution
DISABLE_SMC_EXEC_GLOBAL = TRUE
DISABLE_SMC_EXEC_SHORT_BURST = TRUE

// Production
SETUP_UPTODATE = TRUE

// Alarm handling for DCVI
ALARM_HANDLING_DCVI_ENABLE = TRUE
ALARM_HANDLING_DCVI_SETUP_FILE = "testmethod/RDI_Alarm_setup"

// Others
VEC_MODE_SAMPLING_WAIT = MSET
PURE_GENERATION_MODE = TRUE
ROUTING_SETUP_FILE = "testmethod/routing_tool_states_1.xml"
# ROUTING_SETUP_FILE = ./routing/Routing_Configure.xml
ALLOW_SAME_RESULT_ID_ACROSS_RDI_BLOCK = TRUE
# TMU_TIMEOUT_50ms = FALSE
```

### Syntax（取自子主题 getRdiConfig()）

```
string rdi.getRdiConfig(string optionName);
```
[表] Parameter
列: Parameter | Description
行 1:
  optionName
  The option name to be queried.

### Return Value（取自子主题 getRdiConfig()）

The option value returns.

### Example（取自子主题 getRdiConfig()）

```
rdi.getRdiConfig("RF_CAL_DEFAULT");
```

For the option

RF_CAL_DEFAULT
, one of the three values will return: ON, OFF, and
SYSTEM_CAL.

### Examples（取自子主题 Changing the default pin status with SmartRDI）

### Example 1
```
RDI_BEGIN();
rdi.setPinStatus("pinA",3);
rdi.digCap("mcsame1_DATA1_0").pin("DATA2").samples(30).execute();
rdi.clearPinStatus("pinA");
RDI_END();
```

### Example 2

Do not use
`setPinStatus()`（raw: `142779.htm`）
 and
`clearPinStatus()`（raw: `142780.htm`）
 in the
`burstLabel`（raw: `149059.htm`）
 block of
`smartVec`（raw: `149036.htm`）
.

Wrong position:

```
RDI_BEGIN();
rdi.smartVec().burstLabel("labelName").begin();
...
rdi.setPinStatus("A",1); // This is not allowed.
...
rdi.smartVec().burstLabel().end();
RDI_END();
```

Correct
position:

```
RDI_BEGIN();
rdi.setPinStatus("A",1); // This is correct.
rdi.smartVec().burstLabel("labelName").begin();
...
...
rdi.smartVec().burstLabel().end();
RDI_END();
```

### Syntax（取自子主题 clearPinStatus()）

```
clearPinStatus(const string& sPin);
```
[表] List of parameters
列: Parameter | Description
行 1:
  sPin
  The pin name.

### Example（取自子主题 clearPinStatus()）

```
rdi.clearPinStatus("pinA");
```

### Syntax（取自子主题 setPinStatus()）

```
setPinStatus(const string& sPin, int iWfIndex);
```
[表] List of parameters
列: Parameter | Description
行 1:
  sPin
  The pin name.
行 2:
  iWfIndex
  The waveform index.

Note
 The pin status setting is valid only for the current test suite. This means
that even without calling
`clearPinStatus()`（raw: `142780.htm`）
, the following test suite will use the
`default pin status`（raw: `142781.htm`）
.

### Example（取自子主题 setPinStatus()）

```
rdi.setPinStatus("pinA",3)
```

### Example（取自子主题 SmartRDI: Utility lines control）

```
class RDI_STAT_UTIL: public testmethod::TestMethod
{
protected:

string sMode;
STRING_VECTOR utilitylineStatus_1,utilitylineStatus_2,utilitylineStatus_3;

virtual void initialize()
{
addParameter("RDIMode","string",&amp;sMode, testmethod::TM_PARAMETER_INPUT).setOptions("SINGLE:BURST:PROD").setDefault("BURST");
}

virtual void run()
{
RDI_INIT();

ON_FIRST_INVOCATION_BEGIN();

//
// Select smartRDI Mode
//
TA::USER_RUN_MODE mode;

if (sMode == "SINGLE") mode = TA::SINGLE;
else if (sMode == "BURST") mode = TA::BURST;
else if (sMode == "PROD") mode = TA::PROD;

utilitylineStatus_1 = GET_UTILITY_LINES_STATUS(0);

//
// Set 4 util lines of util block 2-9 defined in pin file
//
rdi.util().pin("SEQ_LED_201,SEQ_LED_207, SEQ_LED_209,SEQ_LED_215").setOn().execute();
rdi.wait(2 ms);
utilitylineStatus_2 = GET_UTILITY_LINES_STATUS(0);

//
// Reset 4 util lines of util block 2-9 defined in pin file
//
rdi.util().pin("SEQ_LED_201,SEQ_LED_207,SEQ_LED_209,SEQ_LED_215").setOff().execute();
rdi.wait(4 ms);
utilitylineStatus_3 = GET_UTILITY_LINES_STATUS(0);

ON_FIRST_INVOCATION_END();

//
// Datalog
//
cout << "after reset" << endl;

for(int i=1; i<9;i++)
{
cout << "STAT_UTIL" << i << " = " << utilitylineStatus_1[i-1] << endl;
}

cout << "after set on" << endl;

for(int i=1; i<9;i++)
{
cout << "STAT_UTIL" << i << " = " << utilitylineStatus_2[i-1] << endl;
}
cout << "after set off" << endl;

for(int i=1; i<9;i++)
{
cout << "STAT_UTIL" << i << " = " << utilitylineStatus_3[i-1] << endl;
}

return;
}

virtual void postParameterChange(const string&amp; parameterIdentifier)
{
return;
}

virtual const string getComment() const
{
string comment = "please add your comment for this method.";
return comment;
}
};
```

### Syntax（取自子主题 pin()）

```
pin(const string& sPin);
```
[表] List of parameters
列: Parameter | Description
行 1:
  sPin
  One or more utility pin names.
    
    For more pine names, separate them with comma.

### Example（取自子主题 pin()）

```
rdi.util().pin("upin_A").setOn().pin("upin_B").setOff().execute();
```

### Syntax（取自子主题 setOff()）

```
setOff();
```

### Example（取自子主题 setOff()）

```
rdi.util().pin("upin_B").setOff().execute();
```

### Syntax（取自子主题 setOn()）

```
setOn();
```

### Example（取自子主题 setOn()）

```
rdi.util().pin("upin_A").setOn().execute();
```

### Examples（取自子主题 Sequencer Controlled Utility Mask with SmartRDI）

### Utility Mask with Unganged Configuration

Below is an example of
sequencer‑controlled utility mask in an unganged configuration.

### Utility Mask with Ganged (1-8) Configuration

Below is an example of
sequencer‑controlled utility mask in an ganged configuration.

### Syntax（取自子主题 execute()）

```
execute();
```

List of parameters

There are no parameters.

Return value

There is no return value.

### Example（取自子主题 execute()）

```
rdi.util().pin("upin_A").setOn().pin("upin_B").setOff().execute();
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
