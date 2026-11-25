---
type: object
title: Command Set Programming Interface
layer: L3
stage: testflow
tags: []
related: []
sources:
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.08.05_Command_Set_Programming_Interface.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.08.05.02.02_Production_Flags.htm
  - 02_System_reference/02.09_Test_Program_Management/02.09.01.08.05.02.03_User_Flags.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Command Set Programming Interface

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **3,255 字符逐字取自** `<02_System_reference/02.09_Test_Program_Management/02.09.01.08.05_Command_Set_Programming_Interface.htm>` 及其子主题 `<02_System_reference/02.09_Test_Program_Management/02.09.01.08.05.04.03_System_Flag.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.08.05.04.07_Application_model_file_string.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.08.05.04.14_Command_Set_Message_File.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.08.05.04.19_Set_the_data_logging_profiles.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.08.05.04.23_Retrieve_the_Testsuite_Name.htm>`、`<02_System_reference/02.09_Test_Program_Management/02.09.01.08.05.04.32_Retrieving_bin_statistics.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 System Flag）

Controlling the sites to be tested in multisite
test

```
INT32 MaxSitesEnabled;
int site,i;
long status;

/* query current multi-site values */
GetNumberOfSites(&MaxSitesEnabled);

/* ------------------------------------------------------------------
* Initialization: disable all sites first (to get a known state)
* ------------------------------------------------------------------
*/
for(site=1; site<=MaxSitesEnabled;site++)
{
SetSystemFlagOfSite(CI_SITE_SETUP,site,CI_SITE_NOT_INSERTED);
}

/*--------------------------------------------------------------------------
* Set the desired Sites to be Tested: here, the example sets sites 1 & 3
*--------------------------------------------------------------------------
*/
SetSystemFlagOfSite(CI_SITE_SETUP,1,CI_SITE_INSERTED_TO_TEST);
SetSystemFlagOfSite(CI_SITE_SETUP,3,CI_SITE_INSERTED_TO_TEST);
```

### Example（取自子主题 Application model file string）

```
#include <libcicpi> // Required by these two APIs.
...
char new_wafer_id[2];
GetModelfileString("Temperature",new_wafer_id);
char* LB_ID_var="debug_LB";
SetModelfileString("LB_ID", LB_ID_var);
...
```

### Example（取自子主题 Command Set Message File）

Create the messages/string lines in any text file using the format as described by the

gencat
 Linux command:

file
myfile.msg

2001 this is message 2001

2002 this is message 2002

Generate the message file using the command:

/opt/hp93000/soc/prod_env/lbin/install_cs -m myfile.msg

Messages in the catalog file may now be accessed with the
MsgGetMsg

routine, for example:

fprintf(stderr, "%s", MsgGetMsg(2001));

generates the string
this is message 2001
 on the report window.

You might also find it useful to refer to the Linux man pages for
catopen
,

catclose
 and
catget
.

### Syntax（取自子主题 Set the data logging profiles）

```
void SetSamplingProfiles( const char * on_profile, const char * off_profile) ;
```

This
function registers two data logging profiles to be used for sampling.

The system flag

datalog_sample_size
 allows specifying that only one out of

N
 testflow executions is logged into STDF. If
on_profile
 and
off_profile
 are
defined by calling this function, the
on_profile
 is activated when a testflow execution is to be logged and the
off_profile
 is activated when a testflow execution is not to be logged.

on_profile
 and
off_profile
 are profiles in the
profiles

subdirectory of the device directory.

### Parameters（取自子主题 Set the data logging profiles）

[表]
行 1:
  on_profile
  The profile that is activated when a testflow execution is to be logged.
行 2:
  off_profile
  The profile that is activated when a testflow execution is not to be logged.

### Syntax（取自子主题 Retrieve the Testsuite Name）

```
long GetTestsuiteName(char *testsuiteName)
```

### Example（取自子主题 Retrieve the Testsuite Name）

The following example shows how this function is used:

```
char current_testsuite_name[CI_CPI_MAX_TESTSUITE_LEN];
.
.
.
/* The testsuite name is printed in the report window */
GetTestsuiteName(current_testsuite_name);

fprintf(stdout, "Current testsuite is %s\n", current_testsuite_name);
```

### Example（取自子主题 Retrieving bin statistics）

```
CI_CPI_BIN_CURSOR cursor;
for(cursor = GetBinFirst(); cursor != CI_CPI_INVALID_BIN_CURSOR; cursor = GetBinNext(cursor))
{
CI_CPI_BIN_DESCRIPTOR binDescriptor;
int deviceCount = GetBinStatistics(cursor, &binDescriptor);
fprintf(stderr, "%d devices were binned to Bin %s\n", deviceCount, binDescriptor.bin_name);
int site;
for(site = 0; site < CI_CPI_MAX_SITES; site++)
{
fprintf(stderr, "Site %d: %d devices\n", site + 1, binDescriptor.dies_per_site[site]);
}
}
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
