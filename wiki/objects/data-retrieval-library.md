---
type: object
title: Data Retrieval Library
layer: L2
stage: results
tags: []
related: []
sources:
  - 02_System_reference/02.10_Data_Logging/02.10.01.04_Data_Retrieval_Library.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Data Retrieval Library

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **23,045 字符逐字取自** `<02_System_reference/02.10_Data_Logging/02.10.01.04_Data_Retrieval_Library.htm>` 及其子主题 `<02_System_reference/02.10_Data_Logging/02.10.01.04.01.01_DRLEventAvailable.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.01.02_DRLEventGetAttribute.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.01.03_DRLEventGetFirstAttributeByType.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.01.04_DRLEventGetNextAttributeByType.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.01.05_DRLEventGetNoOfAttributes.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.01.06_DRLEventGetType.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.01.07_DRLFreeEvent.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.01.08_DRLGetEventMask.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.01.09_DRLGetNextUnmaskedEvent.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.01.10_DRLKeepEvent.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.01.11_DRLNumberOfPinGroups.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.01.12_DRLNumberOfPins.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.01.13_DRLNumberOfSites.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.01.14_DRLPinGroupIndexToName.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.01.15_DRLPinGroupIndexToPins.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.01.16_DRLPinGroupNameToIndex.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.01.17_DRLPinIndexToChannel.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.01.18_DRLPinIndexToName.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.01.19_DRLPinIndexToNumber.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.01.20_DRLSave.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.01.21_DRLSetEventMask.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.01.22_DRLStart.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.01.23_DRLStop.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.01.24_DRLTruncate.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.02.03_DRLAttributeRec.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.02.05_DRLBankSpecificCounts.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.02.08_DRLBitFailMapDescAttr.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.02.15_DRLErrorMapAttr.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.02.16_DRLErrorOverviewAttr.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.02.17_DRLEventMask.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.02.22_DRLFailingAddressCountAttr.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.02.23_DRLFailingAdresses.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.02.24_DRLFailingAddressesAttr.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.02.29_DRLLabelDescriptorAttr.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.02.30_DRLLabelListAttr.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.02.42_DRLPatternLabelAttr.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.02.51_DRLPinSpecificAddresses.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.02.52_DRLPinSpecificCounts.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.02.53_DRLPinType.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.02.60_DRLRARepairResult.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.02.61_DRLRARepairResultsAttr.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.02.62_DRLResultPinName.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.02.63_DRLScanInstanceDescriptorAttr.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.02.64_DRLScanInstanceListAttr.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.02.65_DRLShmooAxisData.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.02.72_DRLShmooHXInstrumentType.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.02.73_DRLShmooHXResourceType.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.02.75_DRLShmooSpecVariableType.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.02.77_DRLShmooTestCellAttr.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.02.78_DRLShmooTestCellData.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.02.79_DRLShmooTestInfoAttr.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.02.80_DRLShmooUserDefinedParamType.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.02.83_DRLSiteSetAttr.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.02.86_DRLTestConditionAttr.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.01.04.02.87_DRLTestCondition.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.02.04_Shmoo_output_of_the_Event_Formatter.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Return Value（取自子主题 DRLEventAvailable）

For the data log stream, non-zero is returned if a new
event record is ready to be read. This allows you to treat the result value as

true
 if a new record is ready and
false
 if it is
not.

For a data log file, non-zero is always returned.

Note that EOF is handled by
the
`DRLGetNextUnmaskedEvent`（raw: `34743.htm`）
 function.

### Return Value（取自子主题 DRLEventGetAttribute）

The return value is zero if the function was successful;
otherwise the error code ERR_NO_ATTR (see
`Error Codes`（raw: `34857.htm`）
) is returned if the
event has no attribute record as specified by
which
.

### Example（取自子主题 DRLEventGetAttribute）

```
void example (void)
{
DRLEventRec event;
DRLAttributeRec attribute;
int i, no_of_attributes;
if (DRLGetNextUnmaskedEvent(&event));
{ /* error handler*/ break;
}
no_of_attributes = DRLEventGetNoOfAttributes(&event);
for (i=0; i < no_of_attributes, i++)
{
DRLEventGetAttribute(&event, i, &attribute);
/* attribute is now filled with data of the
attribute record number i of event and can be
processed */
}
}
```

### Return Value（取自子主题 DRLEventGetFirstAttributeByType）

The return value is zero if the function was successful;
otherwise the error code ERR_NO_ATTR (see
`Error Codes`（raw: `34857.htm`）
) is returned if the event has
no attribute record as specified by
type
.

### Example（取自子主题 DRLEventGetFirstAttributeByType）

```
void example (void)
{
DRLEventRec event;
DRLAttributeRec attribute;
if (DRLGetNextUnmaskedEvent(&event))
{ /* error handler*/
break;
}
if (DRLEventGetFirstAttributeByType(&event, DeviceIdAttrType,
&attribute) == 0)
{
printf("Device processed: %s\n",
attribute.data.device_id_attr.device_id);
}
else
{
printf("No DeviceIdAttr found !!!\n");
}
}
```

### Return Value（取自子主题 DRLEventGetNextAttributeByType）

The return value is zero if the function was successful;
otherwise the error code ERR_NO_ATTR (see
`Error Codes`（raw: `34857.htm`）
) is returned if the event has
no more attribute records as specified by
type
.

### Example（取自子主题 DRLEventGetNextAttributeByType）

```
void example (void)
{
DRLEventRec event;
DRLAttributeRec attribute;
int error_code;
if (DRLGetNextUnmaskedEvent(&event))
{ /* error handler*/
break;
}
error_code = DRLEventGetFirstAttributeByType(&event,
DeviceIdAttrType, &attribute);
while (error_code == 0)
{
printf("Device processed: %s\n",
attribute.data.device_id_attr.device_id);
error_code = DRLEventGetNextAttributeByType(&event,
DeviceIdAttrType, &attribute);
}
}
```

### Return Value（取自子主题 DRLEventGetNoOfAttributes）

The function returns the number of attribute records coming
with
event
 or a negative number indicating an error.

### Return Value（取自子主题 DRLEventGetType）

The event type of
event
.

### Example（取自子主题 DRLEventGetType）

```
void example (void)
{
/* event has been initialized before by a call of DRLGetNextUnmaskedEvent */

DRLEventType event_type;
event_type = DRLEventGetType (&event)
switch (event_type)
{ case ProgramStartEventType:
/* analysis of the attribute records coming
with an event of the type ProgramStartEventType
*/
break;
case TestFlowStartEventType:
/* analysis of the attribute records coming with
an event of the typeTestFlowStartEventType */
break;
/*
.
.
.
.
*/
};
}
```

### Return Value（取自子主题 DRLFreeEvent）

None.

### Return Value（取自子主题 DRLGetEventMask）

The function returns a pointer to the active event mask of
the data log stream or file
event
, or NULL in case of an error.

### Return Value（取自子主题 DRLGetNextUnmaskedEvent）

The return value is zero if the function was successful.
Otherwise one of the following error codes is returned (see
`Error Codes`（raw: `34857.htm`）
):

ERR_NO_EVENT: Either no event record was available or the events related to all available
event records were masked by the current event mask.

ERR_EOF: The end of the data log stream or data log file was encountered before the event
record had been read completely.

### Example（取自子主题 DRLGetNextUnmaskedEvent）

```
void example (void)
{
DRLEventRec event;
if (DRLGetNextUnmaskedEvent (&stream,&event))
{
/* error handler */
}
/* if DRLGetNextUnmaskedEvent was successful, the
event is now filled with valid data and &event can be
used for calls of functions which expect an argument of
the type DRLEventRec* (for example, DRLEventGet... functions)
*/
}
```

### Return Value（取自子主题 DRLKeepEvent）

None.

### Example（取自子主题 DRLKeepEvent）

```
/* keeps the data of 100 event records that are read
from the data log stream */

DRLEventRec event_rec[100];
int last = 0;
while (last < 100)
{ DRLGetnextUnmaskedEvent (&my_stream, &event_rec[last]);
DRLKeepEvent(&my_stream, &event_rec[last]);
last++;
};

/* after the event records have been processed, the
allocated memory must be freed again */

while (last > 0)
{ /* process the event record event_rec[last] */
DRLFreeEvent(&event_rec[--last]);
};
```

### Return Value（取自子主题 DRLNumberOfPinGroups）

The function returns the number of pin groups in the
current pin configuration.

### Return Value（取自子主题 DRLNumberOfPins）

The function returns the number of pins in the current pin
configuration.

### Return Value（取自子主题 DRLNumberOfSites）

The function returns the number of sites in the current pin
configuration.

### Return Value（取自子主题 DRLPinGroupIndexToName）

The function returns the name of the pin group with the
index
index
.

In the case of an invalid index, the function returns
NULL.

### Return Value（取自子主题 DRLPinGroupIndexToPins）

The function returns a pointer to an array of pin names
(see
`DRLPinName`（raw: `34819.htm`）
). The variable
number_of_pins
 holds the number of pin names
in that array, that is, the number of pins in the group with the index
index
.

If
the provided index is invalid, the function returns NULL, and
number_of_pins
 is
0.

### Return Value（取自子主题 DRLPinGroupNameToIndex）

The function returns the value 1, if the index of the pin
group with the name
name
 could be determined, and the variable
index
 then holds
the index.

Otherwise, the function returns 0, and
index
 holds the value
DRLNumberOfPinGroups. (See
`DRLNumberOfPinGroups`（raw: `34751.htm`）
).

### Return Value（取自子主题 DRLPinIndexToChannel）

The function returns the channel number of the pin with the
index
pin_index
 and the site
site
. The function returns 0, if
pin_index

belongs to an analog pin, or if
pin_index
 is invalid.

### Return Value（取自子主题 DRLPinIndexToName）

The function returns the name of the pin with the index

pin_index
 and
capabilities
 holds the information on the type of that pin. In the
case of an error the function returns NULL and
type
 is undefined.

### Return Value（取自子主题 DRLPinIndexToNumber）

The function returns the number of the pin with the index

pin_index.
 In case of an error, for example, if
pin_index
 is invalid, the
function returns NULL.

### Return Value（取自子主题 DRLSave）

The return value is zero if the function was successful or
one of the following error codes (see
`Error Codes`（raw: `34857.htm`）
) is returned in case of an
error:

ERR_ACCESS: the path specified in
path
 could not be accessed

ERR_TRUNC: the data log stream could not be truncated

### Return Value（取自子主题 DRLSetEventMask）

The return value is zero if the function was successful or
non-zero if the event mask specified in
mask
 is invalid.

### Example（取自子主题 DRLSetEventMask）

```
void example (void)
{
DRLEventMask mask;
/* set the values for mask as shown in the example in
"DRLEventMask" on page 137*/
if (DRLSetEventMask(&mask,&stream))
{
/* error handler */
}
/* the active event mask is now set to that specified in mask */
}
```

### Return Value（取自子主题 DRLStart）

The return value is zero if the function was successful;
otherwise the error code ERR_ACCESS (see
`Error Codes`（raw: `34857.htm`）
) is returned if the file
specified in
path
 could not be accessed.

### Example（取自子主题 DRLStart）

```
void example (void)
{
DRLDataStream stream;
if (DRLStart (NULL,(DRL_SYNC_COUNTER | DRL_RESET_MASK,
&stream))
{
/* error handler */
};
/* starts a data retrieval operating on the data log stream and checks */
/* only for new event records. The active event mask is reset.*/
}
```

### Return Value（取自子主题 DRLStop）

None.

### Return Value（取自子主题 DRLTruncate）

The return value is zero if the function was successful. If
the data log stream could not be truncated, the error code ERR_TRUNC is returned.

### Example（取自子主题 DRLAttributeRec）

```
void example (void)
{
/* event has been initialized before by a call of DRLGetNextUnmaskedEvent */

DRLAttributeRec attribute;
int i;
i=1;
DRLEventGetAttribute (&event,i,&attribute);
/* gets the first (i=1) attribute record of event */

switch (attribute.type)
{ case TestSuiteNameAttrType:
/* processing attribute.data.test_suite_name_attr
*/
break;
case SiteSetAttrType:
/* processing attribute.data.site_set_attr
*/
break;
/*
...

*/
};
}
```

### Syntax（取自子主题 DRLBankSpecificCounts）

The struct contains these members:

bank_id
: The identifier for the bank.

failing_address_count
: The number of failed addresses for the bank.

failing_address_limit
:

DRLFailureCode
: The code for the overall result for the bank. (See the
table below for
details.)

```
typedef struct _DRLBankSpecificCounts {
unsigned int bank_id;
unsigned long long failing_address_count;
unsigned long long failing_address_limit;
enum DRLFailureCode result;
} DRLBankSpecificCounts;
```

[表] Failure code values
列: Value | Description
行 1:
  -2= DRLFailureCode_Fatal
  test method execution incomplete or test method crashed
行 2:
  -1= DRLFailureCode_NA
  no pass/fail result determined
行 3:
  0 = DRLFailureCode_Pass
  passed
行 4:
  1 = DRLFailureCode_Fail
  failed
行 5:
  2 = DRLFailureCode_Error
  error
行 6:
  3 = DRLFailureCode_Bypass
  bypassed (this applies only to test suites)

### Syntax（取自子主题 DRLBitFailMapDescAttr）

The description is contained in the label

description
.

```
typedef struct _DRLBitFailMapDescAttr {
const char* description;
} *DRLBitFailMapDescAttr;
```

### Syntax（取自子主题 DRLErrorMapAttr）

```
typedef struct _DRLErrorMapAttr {
DRLPinName pin;
const char* description;
int mode;
unsigned failure_count;
struct {
long long cycle_number;
int instance_id;
unsigned offset;
char state_character;
char received;
} cycle[1];
} *DRLErrorMapAttr;
```

### Syntax（取自子主题 DRLErrorOverviewAttr）

```
typedef struct _DRLErrorOverviewAttr {
const char* description;
long long cycle_count;
long long failure_count;
} *DRLErrorOverviewAttr;
```

### Example（取自子主题 DRLEventMask）

```
void example (void)
{
DRLEventMask event_mask = {NumberOfEventTypes,0};
/* initialization */

event_mask.event_mask[TestSuiteStartEventType] = 1;
event_mask.event_mask[TestSuiteEndEventType] = 1;
event_mask.event_mask[BinReachedEventType] = 1;
event_mask.event_mask[AssignmentEventType] = 1;
/* masking of events which are specified by the
event type*/

DRLSetEventMask(&event_mask);
/* sets the active event mask as specified in event_mask */
}
```

### Syntax（取自子主题 DRLFailingAddressCountAttr）

The struct contains these members:

global_count
: The number of failed addresses.

failing_access_count
: The sum of failed accesses to these addresses.

result_pin_count
: The number of pins with failed accesses.

bank_count
: The number of banks with failed accesses.

bank_specific_counts
: The failed address counts for the individual banks,
one per bank with failures.

pin_specific_counts
: The failed address counts for the individual pins,
one per pins with
failures.

```
typedef struct _DRLFailingAddressCountAttr {
unsigned long long global_count; /* number of failing addresses */
unsigned long long failing_access_count; /* number of failing accesses */
unsigned int result_pin_count; /* d dimension */
unsigned int bank_count; /* z_address_count */
DRLBankSpecificCounts* bank_specific_counts; /* size is bank_count */
DRLPinSpecificCounts* pin_specific_counts; /* size is result_pin_count */
} *DRLFailingAddressCountAttr;
```

### Syntax（取自子主题 DRLFailingAdresses）

The struct contains these members:

x_address
: The x-coordinate of the failing address.

y_address
: The y-coordinate of the failing address.

z_address
: The z-coordinate of the failing address.

expected_data
: The data that the test expected to find at the address - 0
or 1. If the expected data was not recorded, this member contains the value
3.

```
typedef struct _DRLFailingAddresses {
unsigned long long x_address;
unsigned long long y_address;
unsigned long long z_address;
unsigned short expected_data; /* 0 or 1 */
} DRLFailingAddresses;
```

### Syntax（取自子主题 DRLFailingAddressesAttr）

The struct contains these members:

failing_address_count
: The number of failed addresses.

failing_access_count
: The sum of failed accesses to these addresses.

result_pin_count
: The number of pins with failed accesses.

x_address_count
: The number of different x-addresses with failed
accesses.

y_address_count
: The number of different y-addresses with failed
accesses.

z_address_count
: The number of different z-addresses with failed
accesses.

pin_specific_addresses
: The failed addresses for the individual pins, one
set per pin with
failures.

```
typedef struct _DRLFailingAddressesAttr {
unsigned long long failing_address_count; /* number of failing addresses */
unsigned long long failing_access_count; /* number of failing accesses */
unsigned int result_pin_count; /* d dimension */
unsigned int x_address_count;
unsigned int y_address_count;
unsigned int z_address_count;
DRLPinSpecificAddresses* pin_specific_addresses; /* size is result_pin_count*/
} *DRLFailingAddressesAttr;
```

### Syntax（取自子主题 DRLLabelDescriptorAttr）

```
typedef struct _DRLLabelDescriptor {
int id;
const char* name;
} *DRLLabelDescriptor;
```

### Syntax（取自子主题 DRLLabelListAttr）

```
typedef struct _DRLLabelListAttr {
int label_count;
struct _DRLLabelDescriptor label[1];
} *DRLLabelListAttr;
```

### Syntax（取自子主题 DRLPatternLabelAttr）

The pattern label is contained in the label

member
.

```
typedef struct _DRLPatternLabelAttr {
const char* label;
} *DRLPatternLabelAttr;
```

### Syntax（取自子主题 DRLPinSpecificAddresses）

The struct contains these members:

result_pin_name
: The name of the pin for which the failed addresses are
listed.

logged_failing_address_count
: The number of failed addresses being
listed.

DRLFailingAdresses
: The failed address for the
pin.

```
typedef struct _DRLPinSpecificAddresses {
DRLResultPinName result_pin_name;
unsigned long long logged_failing_address_count;
DRLFailingAddresses* logged_failing_addresses;
/* size is logged_failing_address_count */
} DRLPinSpecificAddresses;
```

### Syntax（取自子主题 DRLPinSpecificCounts）

The struct contains these members:

result_pin_name
: The name of the pin.

failing_address_count
: The number of failed addresses for the pin.

failing_address_limit
:

DRLFailureCode
: The code for the overall result for the pin. (See the
table below for
details.)

```
typedef struct _DRLPinSpecificCounts {
DRLResultPinName result_pin_name;
unsigned long long failing_address_count;
unsigned long long failing_address_limit;
enum DRLFailureCode result;
} DRLPinSpecificCounts;
```

[表] Failure code values
列: Value | Description
行 1:
  -2= DRLFailureCode_Fatal
  test method execution incomplete or test method crashed
行 2:
  -1= DRLFailureCode_NA
  no pass/fail result determined
行 3:
  0 = DRLFailureCode_Pass
  passed
行 4:
  1 = DRLFailureCode_Fail
  failed
行 5:
  2 = DRLFailureCode_Error
  error
行 6:
  3 = DRLFailureCode_Bypass
  bypassed (this applies only to test suites)

### Example（取自子主题 DRLPinType）

```
void example (void)
{
DRLPinType *type;
DRLPinIndex index=1;
if (DRLPinIndexToName(index,type) = NULL)
{
/* error handler */
};
/* type now holds the information on the pin type. */
if (type->input) {/* pin 1 is an input pin*/};
if (type->output) {/* pin 1 is an output pin*/};
if (type->dps) {/* pin 1 is a DPS pin*/};
if (type->dc) {/* pin 1 is a DC pin*/};
if (type->analog) {/* pin 1 is an analog pin*/};
if (type->virt) {/* pin 1 is a virtual pin*/};
}
```

### Syntax（取自子主题 DRLRARepairResult）

The struct contains these members:

element
: The identifier of the row or column in the segment.

segment
: The identifier of the segment to which the element belongs.

spare
: The spare resource used to repair the
element.

```
typedef struct _DRLRARepairResult {
unsigned int element;
unsigned int segment;
unsigned int spare;
} *DRLRARepairResult;
```

### Syntax（取自子主题 DRLRARepairResultsAttr）

The struct contains these members:

repairable
: Whether the tested device is repairable:

DRLFailureCode_Fail
: The device is not repairable. The other members
show what has been repaired.

DRLFailureCode_Pass
: The device is repairable. The other members show
the repair solution.

dieX
: The x dimension of the die.

dieY
: The y dimension of the die.

spare_column_count
: The number of spare columns used for repairs.

spare_row_count
: The number of spare rows used for repairs.

column_results
: A list of the columns used for repairs. This is a value
of type
`DRLRARepairResult`（raw: `143552.htm`）
; the size is
spare_column_count
.

row_results
: A list of the rows used for repairs. This is a value of type

`DRLRARepairResult`（raw: `143552.htm`）
; the size is

spare_row_count
.

```
typedef struct _DRLRARepairResults {
enum DRLFailureCode repairable;
unsigned long long dieX;
unsigned long long dieY;
unsigned int spare_column_count;
unsigned int spare_row_count;
DRLRARepairResult* column_results;
DRLRARepairResult* row_results;
} *DRLRARepairResults;
```

### Syntax（取自子主题 DRLResultPinName）

The struct contains these members:

bit_pos
: The position of the pin's bit in the d dimension.

pin_name
: The name of the pin being
reported.

```
typedef struct _DRLResultPinName {
unsigned int bit_pos;
DRLPinName pin_name;
} DRLResultPinName;
```

### Syntax（取自子主题 DRLScanInstanceDescriptorAttr）

```
typedef struct _DRLScanInstanceDescriptor {
int id;
const char *name;
int label_id;
const char* label;
long long start_cycle;
long long end_cycle;
} *DRLScanInstanceDescriptor;
```

### Syntax（取自子主题 DRLScanInstanceListAttr）

```
typedef struct _DRLScanInstanceListAttr {
int instance_count;
struct _DRLScanInstanceDescriptor instance[1];
} *DRLScanInstanceListAttr;
```

### Syntax（取自子主题 DRLShmooAxisData）

```
typedef struct _DRLShmooAxisData
{
double start;
double stop;
unsigned int totalSteps;
unsigned int linearSteps;
const char* primaryValue;
const char* scale;
const char* otherDescription;
DRLShmooParametersType parameterType;
union
{
DRLShmooSpecVariableType spec;
DRLShmooHXInstrumentType HXInstrument;
DRLShmooHXResourceType HXResource;
DRLShmooUserDefinedParamType userDefinedParam;
} parameter;
} *DRLShmooAxisData;
```

### Syntax（取自子主题 DRLShmooHXInstrumentType）

```
typedef struct _DRLShmooHXInstrumentType
{
const char* instrumentPin;
const char* property;
const char* unit;
} *DRLShmooHXInstrumentType;
```

### Syntax（取自子主题 DRLShmooHXResourceType）

```
typedef struct _DRLShmooHXResourceType
{
const char* resourceName;
const char* property;
const char* unit;
} *DRLShmooHXResourceType;
```

### Syntax（取自子主题 DRLShmooSpecVariableType）

```
typedef struct _DRLShmooSpecVariableType
{
const char* spec;
const char* setupPins;
} *DRLShmooSpecVariableType ;
```

### Syntax（取自子主题 DRLShmooTestCellAttr）

```
typedef struct _DRLShmooTestCellAttr
{
unsigned int numberOfPin;
unsigned int numberOfTestMode;
const char* pinNames;
const char* testModes;

unsigned int numberOfCell;
DRLShmooTestCellData* cellData;
}*DRLShmooTestCellAttr;
```

### Syntax（取自子主题 DRLShmooTestCellData）

```
typedef struct _DRLShmooTestCellData
{
unsigned int coordinates[MAX_NUM_AXIS];
unsigned int numberOfValues;
double* cellValue;
} *DRLShmooTestCellData;
```

### Syntax（取自子主题 DRLShmooTestInfoAttr）

```
typedef struct _DRLShmooTestInfoAttr
{
const char* title;
const char* testMode;
const char* resultPins;
const char* otherDescription;
double resultResolution;
int numberOfAxis;
DRLShmooAxisData* axisData;
} *DRLShmooTestInfoAttr;
```

### Syntax（取自子主题 DRLShmooUserDefinedParamType）

```
typedef struct _DRLShmooUserDefinedParamType
{
const char* paramName;
const char* type;
}*DRLShmooUserDefinedParamType;
```

### Example（取自子主题 DRLSiteSetAttr）

```
/* lists all site Ids of a site set */
void example (DRLSiteSetAttr ss_attribute)
/* contents of ss_attribute are passed by the caller
of example */
{
int i
for (i=0; i<ss_attribute->size;i++)
{
printf(ss_attribute->site[i]);
};
}
```

### Syntax（取自子主题 DRLTestConditionAttr）

```
typedef struct _DRLTestConditionAttr {
unsigned short conditionCount;
DRLTestCondition testCondition[];
} *DRLTestConditionAttr;
```

To
write this
attribute:

```
DCLAttribute DCLMakeTestConditionAttr ( DCLTestCondition* testCondition, unsigned short testCondCnt )
```

To
read this
attribute:

```
static int TestConditionAttrConv(DRLDataStream* stream, unsigned char* p, DCLAttributeRecLength length, DRLAttributeRec* attr)
```

### Syntax（取自子主题 DRLTestCondition）

```
typedef struct _DRLTestCondition {
char* key;
char* value;
} *DRLTestCondition;
```

### Example（取自子主题 Shmoo output of the Event Formatter）

A shmoo data log shown with Event Formatter is similar to the one
below.

```
======== Started Testsuite Shmoo_2D ============================================

******** Started Site : 1 ******************************************************
Equation Set 512; Spec Set 256; Timing Set 256
Equation Set 512; Spec Set 512; Level Set 512
Startlabel: spec_search

-------- Test Name: 714 parameters[1] -----------------------------------------
-------- Shmoo -----------------------------------------------------------------
Title: 714 parameters
Test Mode: pass/fail,cycle error count
Result Pins: @
Result Resolution: 1.000000
Description:

........ Shmoo Axis Information ................................................
X-Axis
TotalSteps: 10
LinearSteps: 1
Test Range: [0.000000 ... 1.000000]
Scale: Linear
=> Step Ratio: 0.100000
PrimaryValue: 0.500000
Parameter: Spec Variable
Spec: LEV.2.VIL[V]
SetupPins: I/O0,I/O1
Description:

Y-Axis
TotalSteps: 10
LinearSteps: 1
Test Range: [0.000000 ... 10.000000]
Scale: Linear
=> Step Ratio: 1.000000
PrimaryValue: 5.000000
Parameter: Spec Variable
Spec: TIM.2.tpd_CP_IOx[ns]
SetupPins: @
Description:

........ Shmoo Matrix ..........................................................
' ' = point not calculated
'.' = point passed
'*' = point failed
'E' = point returned an error

Shmoo Pin Number : 1
Shmoo TestMode Number : 2
Shmoo Pin Names : @;
Shmoo Test Modes : pass/fail;cycle error count;

Number Of Cells : 121

Pin: @, TestMode : pass/fail

00000000001
...........
01234567890
00000000000
00000000000
+---------->
0.000|...........
1.000|...........
2.000|...........
3.000|...........
4.000|...........
5.000|...........
6.000|...........
7.000|...........
8.000|...........
9.000|...........
10.000v...........

Pin: @, TestMode : cycle error count

0 0 0 0 0 0 0 0 0 0 1
. . . . . . . . . . .
0 1 2 3 4 5 6 7 8 9 0
0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0
+------------------------------------------->
0.000| 0 0 0 0 0 0 0 0 0 0 0
1.000| 0 0 0 0 0 0 0 0 0 0 0
2.000| 0 0 0 0 0 0 0 0 0 0 0
3.000| 0 0 0 0 0 0 0 0 0 0 0
4.000| 0 0 0 0 0 0 0 0 0 0 0
5.000| 0 0 0 0 0 0 0 0 0 0 0
6.000| 0 0 0 0 0 0 0 0 0 0 0
7.000| 0 0 0 0 0 0 0 0 0 0 0
8.000| 0 0 0 0 0 0 0 0 0 0 0
9.000| 0 0 0 0 0 0 0 0 0 0 0
10.000v 0 0 0 0 0 0 0 0 0 0 0

Executed Testmethod ac_tml.AcTest.Shmoo on Site 1: PASSED
******** Ended Site : 1 ******************************************************

******** Started Site : 2 ******************************************************
Equation Set 512; Spec Set 256; Timing Set 256
Equation Set 512; Spec Set 512; Level Set 512
Startlabel: spec_search

-------- Test Name: 714 parameters[1] -----------------------------------------
-------- Shmoo -----------------------------------------------------------------
Title: 714 parameters
Test Mode: pass/fail,cycle error count
Result Pins: @
Result Resolution: 1.000000
Description:

........ Shmoo Axis Information ................................................
X-Axis
TotalSteps: 10
LinearSteps: 1
Test Range: [0.000000 ... 1.000000]
Scale: Linear
=> Step Ratio: 0.100000
PrimaryValue: 0.500000
Parameter: Spec Variable
Spec: LEV.2.VIL[V]
SetupPins: I/O0,I/O1
Description:

Y-Axis
TotalSteps: 10
LinearSteps: 1
Test Range: [0.000000 ... 10.000000]
Scale: Linear
=> Step Ratio: 1.000000
PrimaryValue: 5.000000
Parameter: Spec Variable
Spec: TIM.2.tpd_CP_IOx[ns]
SetupPins: @
Description:

........ Shmoo Matrix ..........................................................
' ' = point not calculated
'.' = point passed
'*' = point failed
'E' = point returned an error

Shmoo Pin Number : 1
Shmoo TestMode Number : 2
Shmoo Pin Names : @;
Shmoo Test Modes : pass/fail;cycle error count;

Number Of Cells : 121

Pin: @, TestMode : pass/fail

00000000001
...........
01234567890
00000000000
00000000000
+---------->
0.000|...........
1.000|...........
2.000|...........
3.000|...........
4.000|...........
5.000|...........
6.000|...........
7.000|...........
8.000|...........
9.000|...........
10.000v...........

Pin: @, TestMode : cycle error count

0 0 0 0 0 0 0 0 0 0 1
. . . . . . . . . . .
0 1 2 3 4 5 6 7 8 9 0
0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0
+------------------------------------------->
0.000| 0 0 0 0 0 0 0 0 0 0 0
1.000| 0 0 0 0 0 0 0 0 0 0 0
2.000| 0 0 0 0 0 0 0 0 0 0 0
3.000| 0 0 0 0 0 0 0 0 0 0 0
4.000| 0 0 0 0 0 0 0 0 0 0 0
5.000| 0 0 0 0 0 0 0 0 0 0 0
6.000| 0 0 0 0 0 0 0 0 0 0 0
7.000| 0 0 0 0 0 0 0 0 0 0 0
8.000| 0 0 0 0 0 0 0 0 0 0 0
9.000| 0 0 0 0 0 0 0 0 0 0 0
10.000v 0 0 0 0 0 0 0 0 0 0 0

Shmoo picture has been saved in: /home/Devices/74HC299/shmoo/shmooPNG/shmoo_2D
Executed Testmethod ac_tml.AcTest.Shmoo on Site 2: PASSED
******** Ended Site : 2 ******************************************************

======== Ended Testsuite Shmoo_2D ==============================================
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
