---
type: object
title: TPI Program Routines
layer: L3
stage: run
tags: []
related: []
sources:
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.09_TPI_Program_Routines.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# TPI Program Routines

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **34,366 字符逐字取自** `<02_System_reference/02.09_Test_Program_Management/02.09.01.09_TPI_Program_Routines.htm>` 及其子主题 `<02_System_reference/02.09_Test_Program_Management/02.09.01.09.01_ChangeDevice.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.09.02_DataManager.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.09.03_ExecMonitor.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.09.04_GetConnectState.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.09.05_GetActiveSites.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.09.06_GetAvailableSites.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.09.07_GetDevPath.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.09.08_GetEnabledSites.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.09.09_GetEQVariableFromCache.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.09.10_GetEQVariableValue.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.09.11_GetFileState.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.09.12_GetLoadedTestflowName.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.09.13_GetNumberOfSites.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.09.14_GetSiteInFocus.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.09.15_GetSiteState.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.09.16_GetTechPath.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.09.17_GetTestflowRevisionInfo.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.09.18_GetTmpPath.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.09.19_HpInit.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.09.20_HpTerm.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.09.21_HpFwTask.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.09.22_InsertEQVariableInCache.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.09.23_MonitorStatus.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.09.24_ReportMessage.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.09.25_RestoreSiteState.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.09.26_SetActiveSites.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.09.27_SetEnabledSites.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.09.28_SetErrorMapMode.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.09.29_SetSiteInFocus.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax（取自子主题 ChangeDevice）

```
VOID ChangeDevice(
CHAR *device_path,
CHAR *device_name,
INT32 force_change,
INT32 *return_state);
```
[表] Parameters
列: Parameter | Description
行 1:
  device_path
  path to device to change to (max. length: DM_MAX_DEVICE)
行 2:
  device_name
  name of device to change to (max. length: DM_MAX_FILE)
行 3:
  force_change [跨 2 行]
  0 - change only if paths of actual and new device are different
行 4:
  1 - change even if paths of actual and new device are identical
行 5:
  return_state
  0 if an error occurred

### Example（取自子主题 ChangeDevice）

```
#include <stdio.h>
/* List the custom header files. */
#include "tpi_c.h"
#include "ci_types.h"
#include "libcicpi.h"
int main(int argc, char* argv[])
{
char szSysCmd[256], szDevPath[256];
long lReturnValue, lDeviceState;
int iExitStatus;

#ifndef OS_LINUX
_main();
#endif

HpInit(); /* attach to SmarTest process */

/* Program Arguments:
argv[0]=="run_supervisor"
argv[1]=="device path"
argv[2]=="device name"
argv[3]=="program name"
*/

ChangeDevice(argv[1],argv[2],FALSE,&lDeviceState); /* Change device */

if (lDeviceState == 1) { /* Check for an error. */
{
sprintf(szDevPath,"%s/%s",argv[1],argv[2]); /* init path */

/* Load test program */
DataManager(dm_testprog,dm_load,szDevPath,argv[3],0,&lDeviceState);

if (lDeviceState >= -1) { /* Check for an error. */
lReturnValue = ExecTestProgram(); /* Execute test program. */
if (lReturnValue == 0) { /* Set exit status */
iExitStatus = CI_CALL_PASS;

} else {
iExitStatus = CI_CALL_ERROR;
}

} else {
iExitStatus = CI_CALL_ERROR; /* Error, cannot run data mngr */
}

} else {
iExitStatus = CI_CALL_ERROR; /* Error, cannot change device. */
}
HpTerm();
exit(iExitStatus);

}
```

### Syntax（取自子主题 DataManager）

```
VOID DataManager(
enum dm_fid Fid,
enum dm_opc Opc,
const CHAR *Device,
const CHAR *Fname,
DM_FLAGS Flags,
INT32 *State);
```

### Parameters（取自子主题 DataManager）

### Fid (File ID)

This parameter determines the type of file to operate
on.

[表] Values for Parameter Fid
列: Value | Description
行 1:
  dm_applicat
  application data file
行 2:
  dm_applicmodel
  application model file
行 3:
  dm_attrib
  pin attribute setup
行 4:
  dm_bitmap
  memory test - bitmap
行 5:
  dm_catr
  channel attributes
行 6:
  dm_config
  pin configuration setup
行 7:
  dm_dataform
  data bridge command set
行 8:
  dm_emap
  error map
行 9:
  dm_fam
  memory test - fail memory
行 10:
  dm_hplib
  prober and handler command set
行 11:
  dm_level
  level setup
行 12:
  dm_procdata
  execution input command set
行 13:
  dm_report
  report
行 14:
  dm_set
  data set
行 15:
  dm_shmoo
  shmoo
行 16:
  dm_state
  state list
行 17:
  dm_scan_res
  scan test - results
行 18:
  dm_tdiag
  timing diagram
行 19:
  dm_testflow
  testflow file
行 20:
  dm_testprog
  test program
行 21:
  dm_timing
  timing setup
行 22:
  dm_userproc
  user procedure command set
行 23:
  dm_vector
  vector setup
    
    Note Use dm_vector also to save a pattern master
    file.
    
    See also the note for dm_pattern_master_file.
行 24:
  dm_wafertyp
  wafer description file
行 25:
  dm_mx_analog
  analog setup file
行 26:
  dm_mx_waveform
  waveform file
行 27:
  dm_mx_routing
  routing setup file
行 28:
  dm_pattern_master_file
  pattern master file
    
    Note Use dm_pattern_master_file only to save the updated
    patterns in in a new pattern master file. Using dm_pattern_master_file
    SmarTest does not save unchanged patterns.
    
    To save data in existing files use dm_vector instead.
行 29:
  dm_profile
  data logging profile file
行 30:
  dm_testtable
  `test table`（raw: `118859.htm`） file

### Opc (Operation)

This parameter determines the operation to be
performed.

[表] Values for Parameter Opc
列: Entry | Operation
行 1:
  dm_load
  replace current setup by file
行 2:
  dm_merge
  merge a file (add additional pins)
行 3:
  dm_append
  append a file (add additional vectors)
行 4:
  dm_save
  save current setup to file
行 5:
  dm_print
  print file
行 6:
  dm_copy_in
  copy file from another device directory
行 7:
  dm_delete
  delete file
行 8:
  dm_utd
  return up to date status for the file specified by Fid
行 9:
  dm_optimize
  create an optimized testflow
行 10:
  dm_del_optimize
  delete a optimized testflow
行 11:
  dm_optimize_utd
  return up to date state of the optimized testflow
行 12:
  dm_replace (obsolete)
  nothing happens.
行 13:
  dm_pload
  load pattern master file
行 14:
  dm_plinit
  initialize pattern master file
行 15:
  Dm_blload
  load one label which should be in the current loaded pattern master file
行 16:
  Dm_pldump
  dump the contents of the pattern master file to a file
行 17:
  Dm_ustate
  query the firmware to get the label states and then updating the pattern master
    file with the returned states.
行 18:
  Dm_unload
  unload a library (user procedure, hplib, dataform, etc) in application model
行 19:
  Dm_labsave
  save the label to a file

### Device

Specifies the device path. The maximum length of this string is
defined by
DM_MAX_DEVICE
.

Note
 The
tpi_c.h
 header file provides the external
linkage that no manual linkage via
extern "C"
 is necessary. If your code uses
the
extern
 function, make sure that it is conform to the current
signature.

Use an
absolute path (as in interactive environment) or a path relative to the directory from where you
will start the test flow program. Trailing slash
"/"
 is allowed. The
current device is denoted with an empty string.

For some operations, this parameter has no
meaning and is ignored.

### Fname (File Name)

Specifies the name of the file. The maximum length of
this string is defined by
DM_MAX_FILE
. Only real names are permitted (no
wildcards).

Note
 The
tpi_c.h
 header file provides the external
linkage that no manual linkage via
extern "C"
 is necessary. If your code uses
the
extern
 function, make sure that it is conform to the current
signature.

### Flags

Specifies modifications to normal operation. A value of zero
denotes normal (unmodified) operation. Flags can be bitwise OR'ed to combine several
modifications.

[表] Values for Parameter Flags
列: Entry | Modification
行 1:
  DM_OWRT
  Allows the Test Program Explorer process to overwrite an existing setup file. If
    the flag is not set and the save fails, the routine returns an error code to the test flow
    program and displays an error message in the report window.
行 2:
  DM_FORCE
  Defeats the optimizing operations of the Test Program Explorer process and always
    downloads a setup file.
行 3:
  DM_SILENT
  Defeats error messages to the report window; the Test Program Explorer process
    still returns an error code to the test flow program.

### State (return state)

State
 reports the execution
return state and can have the following values:

[表] Values for Parameter State
列: Value | Description
行 1:
  1
  up-to-date for operation dm_utd
行 2:
  0
  not up-to-date for operation dm_utd;
    
    ok for other operations
行 3:
  < -1
  not ok (please refer to `Appendix A: Listing of Error Messages`（raw: `16159.htm`）)

### Example（取自子主题 DataManager）

This example loads inputted test program for the device

szDevPath
.

```
DataManager(dm_testprog,dm_load,szDevPath,argv[3],0,&lDeviceState);
```

### Syntax（取自子主题 ExecMonitor）

```
VOID ExecMonitor(
UINT16 FuncType,
CHAR *Parameter,
INT32 *ExecReturn);
```

### Parameters（取自子主题 ExecMonitor）

[表] Parameters for ExecMonitor
列: Parameter | Value | Description
行 1:
  FuncType
  TM_CONTROL_MONITOR
  Lets you program the Monitor.
行 2:
  
  TM_RESET_MONITOR_
    
    STATUS
  Lets you reset the test system Operation state displayed in
    the report window. After reset the state is updated with the actual Monitor state.
行 3:
  
  TM_UNLOCK_TESTER
  Lets you unlock the test system. Executes Connect and Disconnect after you have
    locked the test system.
行 4:
  Parameter
  
  A string containing the information necessary to execute the required Monitor
    function.
行 5:
  
  Monitor type
  Specifies Monitor function (see the table below).
行 6:
  
  Monitor settings
  Settings you can make when programming the Monitor (see the table below).
行 7:
  ExecReturn
  
  Monitor function execution state.
行 8:
  
  TM_SUCCEED
  Monitor function successfully executed.
行 9:
  
  TM_BAD_FUNC_TYPE
  Incorrect function type entered.
行 10:
  
  TM_BAD_PARAM_S_
    
    SYNTAX
  Incorrect parameter string syntax used.
行 11:
  
  TM_PARAM_S_TOO_
    
    LONG
  Parameter string is too long.
行 12:
  
  TM_POLL_TIME_OUT_OF_RANGE
  Entered Poll Time is out of the allowed range.
行 13:
  
  TM_SOFT_ALARM_OUT_OF_RANGE
  Entered Soft Alarm is out of the allowed range.
[表] Monitor Type Parameters
列: Parameter | Function
行 1:
  CalAge
  Age of current calibration
行 2:
  BoardTempr
  IO Board temperature
行 3:
  Diagnostic
  Diagnostic finished
行 4:
  DpsCurrent
  DPS forced current
[表] Monitor Settings Parameters
列: Parameter | Function | Values
行 1:
  <poll enable>
  "enable"/"disable"
  enable or disable the monitor
行 2:
  <poll time value> [跨 7 行]
  enter string to set Monitor poll time [跨 7 行]
    
    (values depend on <poll time unit>)
  3.0 ... 60.0 [seconds]
行 3:
  1.0 ... 60.0 [minutes]
行 4:
  1.0 ... 24.0 [hours]
行 5:
  1.0 ... 7.0 [days]
行 6:
  1.0 ... 4.0 [weeks]
行 7:
  1.0 ... 12.0 [months]
行 8:
  1.0 [year]
行 9:
  <poll time unit> [跨 7 行]
  set unit of Monitor poll time [跨 7 行]
  "second(s)"
行 10:
  "minute(s)"
行 11:
  "hour(s)"
行 12:
  "day(s)"
行 13:
  "week(s)"
行 14:
  "month(s)"
行 15:
  "year(s)"
行 16:
  <high soft alarm value> [跨 3 行]
  set limit for "CalAge"
  time since last cal; range is 0.0 ... 7884000.0 seconds (1/4 year)
行 17:
  set limit for "BoardTempr"
  positive temp. delta in range 0.0 ... (2.5 - max cal. temp. delta/2)
    [C]
行 18:
  set limit for "DpsCurrent"
  % value of programmed current limits of all DPSs in range 0.0 ...
    1.0
行 19:
  <low soft alarm value>
  set limit for "BoardTempr"
  negative temp. delta in range
    
    (-2.5 + max cal. temp. delta/2) ... 0.0 [C]
行 20:
  <soft alarm unit> [跨 11 行]
  set unit of soft alarm limit for "CalAge" [跨 7 行]
  "second(s)"
行 21:
  "minute(s)"
行 22:
  "hour(s)"
行 23:
  "day(s)"
行 24:
  "week(s)"
行 25:
  "month(s)"
行 26:
  "year(s)"
行 27:
  set unit of soft alarm limit for "BoardTempr" [跨 3 行]
  "C" (celsius)
行 28:
  "K" (kelvin)
行 29:
  "F" (fahrnheit)
行 30:
  set unit of soft alarm limit for "DpsCurrent"
  "A" (Ampere)
行 31:
  <lock tester enable>
  set "lock_enable" / "lock_disable" (used for DPS Current
    only)
  "lock_enable" or " lock_disable"

### Example（取自子主题 ExecMonitor）

```
INT32 ExecReturn;

ExecMonitor(TM_RESET_STATUS,"",&ExecReturn);
ExecMonitor(TM_CONTROL_MONITOR,"CalAge;enable;\
1;day(s);4.0;month(s)", &ExecReturn);
ExecMonitor(TM_CONTROL_MONITOR,"BoardTempr;enable;\
2.0;-2.0;C",&ExecReturn);
ExecMonitor(TM_CONTROL_MONITOR,"DpsCurrent; \
enable;10.0;second(s);0.8;A;\
lock_enable",&ExecReturn);
```

### Syntax（取自子主题 GetConnectState）

```
VOID GetConnectState(
INT32 *is_connected);
```

### Parameters（取自子主题 GetConnectState）

The output parameter
is_connected
 is
set to

FALSE
 if the device is actually disconnected

TRUE
 if the device is actually connected

### Example（取自子主题 GetConnectState）

```
INT32 isConnected;
GetNumberOfSites(&isConnected);
```

### Syntax（取自子主题 GetActiveSites）

```
VOID GetActiveSites(MS_SITE_SET active_set);
```

### Parameters（取自子主题 GetActiveSites）

[表]
列: Parameter | Description
行 1:
  active_set
  A character array containing whether each site is activated or not. It is in the
    type of MS_SITE_SET.
    
    If active_set[i] is not 0, site i is activated.
    
    If active_set[i] is 0, site i is deactivated.
    
    MS_SITE_SET is a character array with the length MS_MAX_SITES+1. It is
    used to access the status of all configured sites. Its element contains the status of the
    corresponding site.
    
    If you define the variable siteSet of type MS_SITE_SET,
    siteSet[i] will be used to contain the status of site
    i.
    
     
    
    The data type is defined as below:
    
     
    
    typedef char MS_SITE_SET[MS_MAX_SITES+1];
    
     
    
    MS_MAX_SITES is defined as follows for SmarTest 7.3.1 or higher
    versions:
    
    For 64-bit system: 1024
    
    For 32-bit system: 128
    
    MS_MAX_SITES is defined as follows for older versions of
    SmarTest:
    
    For 64-bit system: 256
    
    For 32-bit system: 128

Note
 Note that 0 is not a valid site number.

### Example（取自子主题 GetActiveSites）

```
MS_SITE_SET active_sites;
GetActiveSites(active_sites);
```

### Syntax（取自子主题 GetAvailableSites）

void GetAvailableSites(MS_SITE_SET available_set);

### Parameters（取自子主题 GetAvailableSites）

[表]
列: Parameter | Description
行 1:
  available_set
  A character array containing whether each site is available or not. It is in the
    type of MS_SITE_SET.
    
    If available_set[i] is not 0, site i is available.
    
    If available_set[i] is 0, site i is not available.
    
    MS_SITE_SET is a character array with the length MS_MAX_SITES+1. It is
    used to access the status of all configured sites. Its element contains the status of the
    corresponding site.
    
    If you define the variable siteSet of type MS_SITE_SET,
    siteSet[i] will be used to contain the status of site
    i.
    
     
    
    The data type is defined as below:
    
     
    
    typedef char MS_SITE_SET[MS_MAX_SITES+1];
    
     
    
    MS_MAX_SITES is defined as follows for SmarTest 7.3.1 or higher
    versions:
    
    For 64-bit system: 1024
    
    For 32-bit system: 128
    
    MS_MAX_SITES is defined as follows for older versions of
    SmarTest:
    
    For 64-bit system: 256
    
    For 32-bit system: 128

Note
 Site counting starts from 1 and 0 is not a valid site
number.

### Example（取自子主题 GetAvailableSites）

```
MS_SITE_SET available_sites;
GetAvailableSites(available_sites);
```

### Syntax（取自子主题 GetDevPath）

```
VOID GetDevPath(
CHAR *dev_path_p);
```

### Parameters（取自子主题 GetDevPath）

On return the character array
dev_path

contains the actual device path. The array should be defined of length

DM_MAX_DEVICE
.

### Example（取自子主题 GetDevPath）

```
char device_path[DM_MAX_DEVICE];
GetDevPath(device_path);
strcat (device_path, "/report/pll.csv");
cout << "path is " << device_path << endl;
```

### Syntax（取自子主题 GetEnabledSites）

```
VOID GetEnabledSites(MS_SITE_SET enabled_set);
```

### Parameters（取自子主题 GetEnabledSites）

[表]
列: Parameter | Description
行 1:
  enabled_set
  A character array containing whether each site is enabled or not. It is in the type
    of MS_SITE_SET.
    
    If enabled_set[i] is 1, site i is enabled.
    
    If enabled_set[i] is 0, site i is disabled.
    
    MS_SITE_SET is a character array with the length MS_MAX_SITES+1. It is
    used to access the status of all configured sites. Its element contains the status of the
    corresponding site.
    
    If you define the variable siteSet of type MS_SITE_SET,
    siteSet[i] will be used to contain the status of site
    i.
    
     
    
    The data type is defined as below:
    
     
    
    typedef char MS_SITE_SET[MS_MAX_SITES+1];
    
     
    
    MS_MAX_SITES is defined as follows for SmarTest 7.3.1 or higher
    versions:
    
    For 64-bit system: 1024
    
    For 32-bit system: 128
    
    MS_MAX_SITES is defined as follows for older versions of
    SmarTest:
    
    For 64-bit system: 256
    
    For 32-bit system: 128

Note
 Note that site counting starts from 1 and 0 is not a valid site
number.

### Example（取自子主题 GetEnabledSites）

```
MS_SITE_SET enabled_sites;

GetEnabledSites(enabled_sites);
```

### Syntax（取自子主题 GetEQVariableFromCache）

```
VOID GetEQVariableFromCache(
INT32 equation_system,
INT32 equation_set,
INT32 spec_set,
INT32 site_number,
CHAR *variable_name,
FLOAT64 *value,
INT32 *return_state);
```

### Parameters（取自子主题 GetEQVariableFromCache）

[表] Parameters of GetEQVariableFromCache
列: Parameter | Description | Range
行 1:
  equation_system
  type of equation system
  TIMING_EQ_SYSTEM or LEVEL_EQ_SYSTEM
行 2:
  equation_set
  equation set number
  1 ... 99
行 3:
  spec_set
  spec set number
  1 ... 99
行 4:
  site_number
  number of appropriate site
  1 ... MS_MAX_SITES
行 5:
  variable_name
  name of equation variable
  null-terminated string
行 6:
  value
  on return: actual value of variable
  
行 7:
  return_state
  execution return state
  0 if successful

### Example（取自子主题 GetEQVariableFromCache）

```
FLOAT64 variable_value;
INT32 re_state;
GetEQVariableFromCache(TIMING_EQ_SYSTEM,2,1,2,"var1",&variable_value,&re_state);
```

### Syntax（取自子主题 GetEQVariableValue）

```
VOID GetEQVariableValue(
INT32 equation_system,
INT32 equation_set,
INT32 spec_set,
INT32 site_number,
CHAR *variable_name,
FLOAT64 *value,
INT32 *return_state);
```

### Parameters（取自子主题 GetEQVariableValue）

[表] Parameters of GetEQVariableValue
列: Parameter | Description | Range
行 1:
  equation_system
  type of equation system
  TIMING_EQ_SYSTEM or LEVEL_EQ_SYSTEM
行 2:
  equation_set
  equation set number
  1 ... 99
行 3:
  spec_set
  spec set number
  1 ... 99
行 4:
  site_number
  number of appropriate site
  1 ... MS_MAX_SITES
行 5:
  variable_name
  name of equation variable
  null-terminated string
行 6:
  value
  on return: actual value of variable
  
行 7:
  return_state
  execution return state
  0 if successful

### Example（取自子主题 GetEQVariableValue）

```
FLOAT64 variable_value;
INT32 re_state;
GetEQVariableValue(TIMING_EQ_SYSTEM,2,1,2,"var1",&variable_value,&re_state);
```

### Syntax（取自子主题 GetFileState）

```
VOID GetFileState(
enum dm_fid fid;
struct dm_file_state *file_state;
INT32 *ret_state;);
```

### Parameters（取自子主题 GetFileState）



### fid（取自子主题 GetFileState）

This parameter determines the type of file to operate on (for a list
of possible values see
`DataManager`（raw: `26594.htm`）
).

### file_state（取自子主题 GetFileState）

On return this structure contains the retrieved information.
The following table shows the elements of the structure.

[表] Structure Elements of dm_file_state
列: Element | Type | Description
行 1:
  name
  dm_file
  name of the file
行 2:
  edit_name
  dm_file
  not used
行 3:
  alternate_name
  dm_file
  not used
行 4:
  Foreign
  char
  0 - local file
    
    1 - extern file
行 5:
  UpToDate
  char
  0 - file is not up to date
    
    1 - file is up to date
行 6:
  New
  char
  not used
行 7:
  edit_device
  dm_device
  not used
行 8:
  device
  dm_device
  name of the device

### ret_state（取自子主题 GetFileState）

This output parameter reports the execution return state:

 0 for OK

-1 for invalid file type

-2 for invalid file state pointer

### Example（取自子主题 GetFileState）

```
#include "/opt/hp93000/soc/pws/lib/tpi_c.h"
virtual void run()
{
...
ON_FIRST_INVOCATION_BEGIN();

{
struct dm_file_state file_state;
int ret_state;
GetFileState(dm_testflow, &file_state, &ret_state);
cout<< "My Test Flow file name is " << file_state.name << endl;
GetFileState(dm_config, &file_state, &ret_state);
cout<< "My Pin Config file name is " << file_state.name << endl;
GetFileState(dm_pattern_master_file, &file_state, &ret_state);
cout<< "My Pattern Master File name is " << file_state.name << endl;
GetFileState(dm_testtable, &file_state, &ret_state);
cout<< "My Test Table File name is " << file_state.name << endl;
}

ON_FIRST_INVOCATION_END();
...
return;
} //virtual void run()
```

### Syntax（取自子主题 GetLoadedTestflowName()）

```
const CHAR *GetLoadedTestflowName();
```

### Return value（取自子主题 GetLoadedTestflowName()）

The maximum length of the returned testflow name is defined
by
DM_MAX_FILE
. The returned pointer cannot be freed.

### Example（取自子主题 GetLoadedTestflowName()）

```
CHAR *testflowName = NULL;
testflowName = GetLoadedTestflowName();
cout << "Loaded testflow is" << testflowName << endl;
```

### Syntax（取自子主题 GetNumberOfSites）

```
VOID GetNumberOfSites(
INT32 *number_of_sites);
```

### Parameters（取自子主题 GetNumberOfSites）

On return,
number_of_sites
 specifies
the number sites currently configured.

### Example（取自子主题 GetNumberOfSites）

```
INT32 MaxSitesEnabled;
GetNumberOfSites(&MaxSitesEnabled);
```

### Syntax（取自子主题 GetSiteInFocus）

```
VOID GetSiteInFocus(
INT32 *site_in_focus);
```

### Parameters（取自子主题 GetSiteInFocus）

Note
 Another focus exists besides the query focus:
the setup focus.

On return,
site_in_focus
 specifies the number
of the site that currently has the query focus.

### Example（取自子主题 GetSiteInFocus）

```
INT32 focus_site;
GetSiteInFocus(&focus_site);
```

### Syntax（取自子主题 GetSiteState）

```
VOID GetSiteState (
MS_SITE_STATE *site_state);
```

### Parameters（取自子主题 GetSiteState）

site_state
 points to a structure of
type
MS_SITE_STATE
 containing information on the number of sites and on
the sites currently enabled, active, and in focus.

### Example（取自子主题 GetSiteState）

```
MS_SITE_STATE site_state;
GetSiteState(&site_state);
```

### Syntax（取自子主题 GetTechPath）

```
VOID GetTechPath (
CHAR *tech_path);
```

### Parameters（取自子主题 GetTechPath）

On return the character array
tech_path

contains the actual technology path. The array should be defined of length

DM_MAX_DEVICE
.

### Example（取自子主题 GetTechPath）

```
CHAR tech_path[DM_MAX_DEVICE];
GetTechPath(tech_path);
cout << "path is " << tech_path << endl;
```

### Syntax（取自子主题 GetTestflowRevisionInfo()）

```
int GetTestflowRevisionInfo(const CHAR *testflow, TESTFLOW_REVISION_INFO *revision_info);
```
[表] Parameters
列: Parameter | Description
行 1:
  testflow
  A non-null string which indicates the full path of the testflow file.
行 2:
  revision_info
  A pointer to the TESTFLOW_REVISION_INFO structure which holds the following
    information:
    
    CHAR description[TESTFLOW_REVISION_LEN]: The value of the
    description attribute defined in the testflow.
    
    CHAR device_name[TESTFLOW_REVISION_LEN]: The value of the
    device_name attribute defined in the testflow.
    
    CHAR device_revision[TESTFLOW_REVISION_LEN]: The value of the
    device_revision attribute defined in the testflow.
    
    CHAR test_revision[TESTFLOW_REVISION_LEN]: The value of the
    test_revision attribute defined in the testflow.

### Return value（取自子主题 GetTestflowRevisionInfo()）

If the function is executed successfully, it returns 0.
Otherwise, it returns -1.

### Example（取自子主题 GetTestflowRevisionInfo()）

```
TESTFLOW_REVISION_INFO testflowInfo;
int retValue = 0;
retValue = GetTestflowRevisionInfo("/home/device_demo/testflow/demo.tf", &testflowInfo);
```

### Syntax（取自子主题 GetTmpPath）

```
VOID GetTmpPath(CHAR *tmp_path_p);
```

### Parameters（取自子主题 GetTmpPath）

It returns the character array containing the actual temporary
path. The array should be defined of length
SA_TMP_PATH_LENGTH
 (defined in
the header file
/opt/hp93000/soc/com/include/sa_prc.h
).

### Example（取自子主题 GetTmpPath）

```
char tmp_path[SA_TMP_PATH_LENGTH];
GetTmpPath(tmp_path);
cout << "path is " << tmp_path << endl;
```

### Syntax（取自子主题 HpInit）

```
VOID HpInit()
```

### Parameters（取自子主题 HpInit）

None

### Example（取自子主题 HpInit）

```
#include <stdio.h>
/* List the custom header files. */
#include "tpi_c.h"
#include "ci_types.h"
#include "libcicpi.h"
int main(int argc, char* argv[])
{
char szSysCmd[256], szDevPath[256];
long lReturnValue, lDeviceState;
int iExitStatus;

#ifndef OS_LINUX
_main();
#endif

HpInit(); /* attach to SmarTest process */

/* Program Arguments:
argv[0]=="run_supervisor"
argv[1]=="device path"
argv[2]=="device name"
argv[3]=="program name"
*/

ChangeDevice(argv[1],argv[2],FALSE,&lDeviceState); /* Change device */

if (lDeviceState == 1) { /* Check for an error. */
{
sprintf(szDevPath,"%s/%s",argv[1],argv[2]); /* init path */

/* Load test program */
DataManager(dm_testprog,dm_load,szDevPath,argv[3],0,&lDeviceState);

if (lDeviceState >= -1) { /* Check for an error. */
lReturnValue = ExecTestProgram(); /* Execute test program. */
if (lReturnValue == 0) { /* Set exit status */
iExitStatus = CI_CALL_PASS;

} else {
iExitStatus = CI_CALL_ERROR;
}

} else {
iExitStatus = CI_CALL_ERROR; /* Error, cannot run data mngr */
}

} else {
iExitStatus = CI_CALL_ERROR; /* Error, cannot change device. */
}
HpTerm();
exit(iExitStatus);

}
```

### Syntax（取自子主题 HpTerm）

```
VOID HpTerm()
```

### Parameters（取自子主题 HpTerm）

None

### Example（取自子主题 HpTerm）

```
#include <stdio.h>
/* List the custom header files. */
#include "tpi_c.h"
#include "ci_types.h"
#include "libcicpi.h"
int main(int argc, char* argv[])
{
char szSysCmd[256], szDevPath[256];
long lReturnValue, lDeviceState;
int iExitStatus;

#ifndef OS_LINUX
_main();
#endif

HpInit(); /* attach to SmarTest process */

/* Program Arguments:
argv[0]=="run_supervisor"
argv[1]=="device path"
argv[2]=="device name"
argv[3]=="program name"
*/

ChangeDevice(argv[1],argv[2],FALSE,&lDeviceState); /* Change device */

if (lDeviceState == 1) { /* Check for an error. */
{
sprintf(szDevPath,"%s/%s",argv[1],argv[2]); /* init path */

/* Load test program */
DataManager(dm_testprog,dm_load,szDevPath,argv[3],0,&lDeviceState);

if (lDeviceState >= -1) { /* Check for an error. */
lReturnValue = ExecTestProgram(); /* Execute test program. */
if (lReturnValue == 0) { /* Set exit status */
iExitStatus = CI_CALL_PASS;

} else {
iExitStatus = CI_CALL_ERROR;
}

} else {
iExitStatus = CI_CALL_ERROR; /* Error, cannot run data mngr */
}

} else {
iExitStatus = CI_CALL_ERROR; /* Error, cannot change device. */
}
HpTerm();
exit(iExitStatus);

}
```

### Syntax（取自子主题 HpFwTask）

```
VOID HpFwTask(
CHAR *task_str,
INT32 *task_len,
CHAR *answ_str,
INT32 *answ_len,
INT32 *ret_state);
```

### Parameters（取自子主题 HpFwTask）

[表] Parameters for HpFwTask
列: Parameter | Value
行 1:
  task_str
  Command string with one or more commands, each limited by a newline
    (\n) or by a semicolon. It is an input parameter.
行 2:
  task_len
  Length of the command string. It is an input parameter.
行 3:
  answ_str
  Answer string. This is an output parameter.
行 4:
  answ_len
  As an input parameter: the dimensioned size of the answer string. As an output
    parameter: the length of the answer string.
行 5:
  ret_state
  Status (see `Appendix A: Listing of Error Messages`（raw: `16159.htm`）). This is an output parameter.

In order to optimize data transfer times, the size of the answer string should be
determined in relation to the amount of data to be passed.

Note
 The SmarTest
software allows you to execute firmware commands directly from a terminal. The utility that does
this is called
hpt
 and is described in the
`Command Reference`（raw: `103977.htm`）
. To
use
hpt
 the SmarTest software environment must be
running.

### Example（取自子主题 HpFwTask）

The following listing shows an example of how to build the command string for

HpFwTask
 and how to retrieve results from the answer
string.

```
#define FW_TASK_BUF_LEN 1000
#define FW_ANSW_BUF_LEN 1000

CHAR TaskBuffer[FW_TASK_BUF_LEN + 1];
CHAR *Task;
INT32 TaskLength;
CHAR AnswerBuffer[FW_ANSW_BUF_LEN + 1];
INT32 AnswerLength;
INT32 ReturnState;
double MeasurementValue;

/* create and execute the fw-string for */
/* pmu setup and measurement */
Task = TaskBuffer;
Task += sprintf(Task,"DFCM %d,%f,%f,%f,%f,%f,%f,%s,(%s);",1, /* DC set number */
800.0, /* force voltage [mA] */
200000.0, /* clamp current in [uA] */
0, 200000.0, /* PASS/ FAIL treshold */
800.0, /* precharge voltage */
1.0, /* setling time in [ms] */
"NTERM", /* termination mode */
"CP"); /* pin to measure */
Task += sprintf(Task, "PTST? %d,%s,%s\n",
1, /* DC set number */
"NONE", /* pre action: NO */
"CVAL"); /* mode: value with Rs comp. */

TaskLength = Task - TaskBuffer;
AnswerLength = FW_ANSW_BUF_LEN;
HpFwTask(TaskBuffer, &TaskLength, AnswerBuffer, &AnswerLength, &ReturnState);
AnswerBuffer[AnswerLength] = EOS; /* truncation of AnswerBuffer string */

if(ReturnState==0) {
/* extract the pmu valid code and the measured current */
/* example answer: PTST 1,3,9697.204,(CP) */
/* PTST returns the measured current in 'uA' */
sscanf(AnswerBuffer, "PTST 1,%d,%lf,", &ValidCode,
&MeasurementValue);

/* the measured value is now accessible in */
/* 'MeasurementValue' for further processing */
} else {
/**** HpFwTask ERROR ****/
}
```

### Syntax（取自子主题 InsertEQVariableInCache）

```
VOID InsertEQVariableInCache(
INT32 equation_system;
INT32 equation_set;
INT32 spec_set;
CHAR *variable_name;
INT32 *return_state)
```

### Parameters（取自子主题 InsertEQVariableInCache）

[表] Parameters of InsertEQVariableInCache
列: Parameter | Description | Range
行 1:
  equation_system
  type of equation system
  TIMING_EQ_SYSTEM or LEVEL_EQ_SYSTEM
行 2:
  equation_set
  equation set number
  1 ... 99
行 3:
  spec_set
  spec set number
  1 ... 99
行 4:
  variable_name
  name of equation variable
  null-terminated string
行 5:
  return_state
  execution return state
  0 if successful

### Example（取自子主题 InsertEQVariableInCache）

```
INT32 re_state;
InsertEQVariableInCache(TIMING_EQ_SYSTEM, 1, 1, "tim_var",&re_state);
```

### Syntax（取自子主题 MonitorStatus）

```
VOID MonitorStatus(
UINT16 *TstrOpState_p,
UINT16 *StatusReg_p);
```

### Parameters（取自子主题 MonitorStatus）

[表] Values for Parameter TstrOpState_p
列: Parameter | Value | Description
行 1:
  TstrOpState_p [跨 5 行]
  TM_GREEN_STATE
  test system operation is "In Spec"; at least one monitor function is "In
    Spec" while the others are not being monitored (DISABLED).
行 2:
  TM_YELLOW_STATE
  test system operation is "In Spec" (WARNING); at least one monitor
    function is "In Spec" (WARNING) while the others are not being monitored (DISABLED).
行 3:
  TM_RED_STATE
  test system operation is "Out of Spec" (ALARM); at least one monitor
    function is "Out of Spec" (ALARM) while the others are "In Spec", "In Spec" (WARNING), or
    not being monitored (DISABLED).
行 4:
  TM_DISABLED_STATE
  test system operation is not monitored. All monitor functions are
    DISABLED.
行 5:
  TM_OFFLINE_STATE
  test system operation is not monitored, system software was started in
    OFFLINE mode.
[表] Values for Parameter StatusReg_p
列: Parameter | Description | Value
行 1:
  StatusReg_p
  
  
行 2:
  bits 0, 1: [跨 5 行]
  Age of Calibration [跨 5 行]
  00 = test system Oper. In Spec
行 3:
  01 = test system Oper. In Spec (WARNING)
行 4:
  10 = test system Oper. Out of Spec (ALARM)
行 5:
  11 = test system Oper. Not Monitored
行 6:
  
行 7:
  bits 2, 3: [跨 5 行]
  Timing and Level Accuracy [跨 5 行]
  00 = test system Oper. In Spec
行 8:
  01 = test system Oper. In Spec (WARNING)
行 9:
  10 = test system Oper. Out of Spec (ALARM)
行 10:
  11 = test system Oper. Not Monitored
行 11:
  
行 12:
  bits 4, 5: [跨 4 行]
  Diagnostic Done [跨 4 行]
  00 = test system Oper. In Spec
行 13:
  01 = test system Oper. In Spec (WARNING)
行 14:
  10 = test system Oper. Out of Spec (ALARM)
行 15:
  11 = test system Oper. Not Monitored
行 16:
  bits 6, 7:
  unused
  
行 17:
  bits 8, 9: [跨 4 行]
  DPS Force Current [跨 4 行]
  00 = test system Oper. In Spec
行 18:
  01 = test system Oper. In Spec (WARNING)
行 19:
  10 = test system Oper. Out of Spec (ALARM)
行 20:
  11 = test system Oper. Not Monitored
行 21:
  bits 10 ... 15:
  unused

### Example（取自子主题 MonitorStatus）

```
UINT16 TstrOpState, StatusReg;

MonitorStatus(&TstrOpState, &StatusReg);
```

### Syntax（取自子主题 ReportMessage）

```
VOID ReportMessage (
INT32 type,
CHAR *message);
```

### Parameters（取自子主题 ReportMessage）

[表] Parameters of ReportMessage
列: Parameter | Description | Range
行 1:
  type
  type of message to be printed
  UI_MESSAGE, UI_WARNING, UI_ERROR, UI_FATAL
行 2:
  message
  message to be printed
  null-terminated string

The actual display depends on the type of message:

Messages are printed as they come.

For warnings the message text is preceded with
Warning: .

For errors the message text is preceded with
Error:
.

For fatals the message text is preceded with:

Fatal ['<file_name>' #
'<line_number>']:

and followed by:

System errno: '<system error text>'
.

After a fatal message a core is created and the software is shut down.

### Example（取自子主题 ReportMessage）

This code shows an example for how to use
ReportMessage
 to
display a fatal error message.

The executable is named
my_prog
. It
tries to open the file
not_there
 that does not exist. Therefore the
external variable
errno
 is set to ENONET (no such file or
directory).

fdes =
open("not_there",O_RDONLY);

ReportMessage(UI_FATAL, "This is a
Fatal");

The following message will be printed in the report window:

Fatal [my_prog tpi_sa.c #1143]:

This is a Fatal

System errno: No such file or directory

After
this message the SmarTest software will shut down.

### Syntax（取自子主题 RestoreSiteState）

```
VOID RestoreSiteState(
MS_SITE_STATE *site_state,
INT32 *return_state);
```

### Parameters（取自子主题 RestoreSiteState）

[表] Parameters for RestoreSiteState
列: Parameter | Description
行 1:
  site_state
  Points to a structure of type MS_SITE_STATE containing
    information on the number of sites and on the sites currently enabled, active, and in
    focus. This structure usually is filled by a call to `GetSiteState`（raw: `26665.htm`）.
行 2:
  return_state
  Status is set to 0 if execution was ok. Otherwise the site state could not be
    restored because the number of sites before and after restoring did not match.

Note
 To change site states use
`SetActiveSites`（raw: `26709.htm`）
,
`SetEnabledSites`（raw: `26713.htm`）
 and
`SetSiteInFocus`（raw: `26732.htm`）
.

### Example（取自子主题 RestoreSiteState）

```
MS_SITE_STATE site_state;
INT32 re_state;
GetSiteState(&site_state);
...
RestoreSiteState(&site_state, &re_state);
```

### Syntax（取自子主题 SetActiveSites）

```
VOID SetActiveSites(MS_SITE_SET active_set,
INT32 *return_state);
```

### Parameters（取自子主题 SetActiveSites）

[表]
列: Parameter | Description
行 1:
  active_set
  A character array containing whether each site is activated or not. It is in the
    type of MS_SITE_SET.
    
    If active_set[i] is not 0, site i is activated.
    
    If active_set[i] is 0, site i is deactivated.
    MS_SITE_SET is a character array with the length MS_MAX_SITES+1. It is
    used to access the status of all configured sites. Its element contains the status of the
    corresponding site.
    
    If you define the variable siteSet of type MS_SITE_SET,
    siteSet[i] will be used to contain the status of site
    i.
    
     
    
    The data type is defined as below:
    
     
    
    typedef char MS_SITE_SET[MS_MAX_SITES+1];
    
     
    
    MS_MAX_SITES is defined as follows for SmarTest 7.3.1 or higher
    versions:
    
    For 64-bit system: 1024
    
    For 32-bit system: 128
    
    MS_MAX_SITES is defined as follows for older versions of
    SmarTest:
    
    For 64-bit system: 256
    
    For 32-bit system: 128
行 2:
  return_state
  Status is set to 0 if execution was ok. Otherwise an error occurred.

Note
 You should not activate more sites than are currently configured. Site
counting starts from 1 and 0 is not a valid site number.

### Example（取自子主题 SetActiveSites）

```
INT32 re_state;
MS_SITE_SET active_sites;

active_sites[1] = 1;
active_sites[2] = 0;
active_sites[3] = 1;
active_sites[4] = 0;

SetActiveSites(active_sites,&re_state);
```

### Syntax（取自子主题 SetEnabledSites）

```
VOID SetEnabledSites(MS_SITE_SET enabled_set;
INT32 *return_state;
```

### Parameters（取自子主题 SetEnabledSites）

[表]
列: Parameter | Description
行 1:
  enabled_set
  A character array containing whether each site is enabled or not. It is in the type
    of MS_SITE_SET.
    
    If enabled_set[i] is not 0, site i is enabled.
    
    If enabled_set[i] is 0, site i is disabled.
    MS_SITE_SET is a character array with the length MS_MAX_SITES+1. It is
    used to access the status of all configured sites. Its element contains the status of the
    corresponding site.
    
    If you define the variable siteSet of type MS_SITE_SET,
    siteSet[i] will be used to contain the status of site
    i.
    
     
    
    The data type is defined as below:
    
     
    
    typedef char MS_SITE_SET[MS_MAX_SITES+1];
    
     
    
    MS_MAX_SITES is defined as follows for SmarTest 7.3.1 or higher
    versions:
    
    For 64-bit system: 1024
    
    For 32-bit system: 128
    
    MS_MAX_SITES is defined as follows for older versions of
    SmarTest:
    
    For 64-bit system: 256
    
    For 32-bit system: 128
行 2:
  return_state
  Status is set to 0 if execution was ok. Otherwise an error occurred

Note
 You should not enable more sites than are currently configured. Site
counting starts from 1 and 0 is not a valid site number.

### Example（取自子主题 SetEnabledSites）

```
include"/opt/hp93000/soc/pws/lib/tpi_c.h"
...
...
...

INT32 re_state;
MS_SITE_SET enabled_sites;

enabled_sites[1] = 1;
enabled_sites[2] = 0;
enabled_sites[3] = 1;
enabled_sites[4] = 0;

SetEnabledSites(enabled_sites,&re_state);
```

### Syntax（取自子主题 SetErrorMapMode）

```
VOID SetErrorMapMode(
INT32 mode);
```

### Parameters（取自子主题 SetErrorMapMode）

The mode variable supports two values:

ERROR_MAP_FAILURE_ORIENTED
 to set the error map to failure oriented
mode (only failed cycles are logged in the error map).

ERROR_MAP_CYCLE_ORIENTED
 to set the error map to cycle oriented mode
(all cycles are logged in the error map).

### Defaults（取自子主题 SetErrorMapMode）

Initially (while loading) the error map mode is set to

ERROR_MAP_CYCLE_ORIENTED
.

### Example（取自子主题 SetErrorMapMode）

```
SetErrorMapMode(ERROR_MAP_FAILURE_ORIENTED);
```

### Syntax（取自子主题 SetSiteInFocus）

```
VOID SetSiteInFocus(
INT32 site_in_focus,
INT32 *return_state);
```

### Parameters（取自子主题 SetSiteInFocus）

[表] Parameters for SetSiteInFocus
列: Parameter | Description
行 1:
  site_in_focus
  Specifies the number of the site to be focused.
行 2:
  return_state
  Status is set to 0 if execution was ok. Otherwise an error occurred.

### Example（取自子主题 SetSiteInFocus）

```
INT32 re_state;
SetSiteInFocus(2, &re_state);
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
