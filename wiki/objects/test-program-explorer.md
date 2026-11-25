---
type: object
title: Test Program Explorer
layer: gui
stage: project
tags: []
related: []
sources:
  - 01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02_Test_Program_Explorer.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Test Program Explorer

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **6,714 字符逐字取自** `<01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02_Test_Program_Explorer.htm>` 及其子主题 `<01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02.03.01_Customized_hp83_import_for_encrypted_setup_files.htm>`、`<01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02.04.05_Collision_handling.htm>`、`<01_Getting_started/01.01_SmarTest_Work_Center/01.01.08.08_Firmware_view.htm>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.03_Pattern_editor_properties_view.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Customized hp83_import for encrypted setup files）

The following code example, which assumes that the encryption pass word is
"VERIGY93K", shows a possible implementation:

```
/*
*-- system includes ------------------------------------------------------
*/
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
/*
*-- module include -------------------------------------------------------
*/
#include "tpi_c.h"
#include "ci_types.h"
#include "libcicpi.h"
/*
*-- defines -------------------------------------------------------------
*/
#define SA_PROCESS_INFO "/opt/hp93000/soc/pws/bin/saprocessinfo -sep ' '"
/*
*-- globals variables ----------------------------------------------------
*/
/*
*-- functions ------------------------------------------------------------
*/
int securityChecks()
{
FILE *fd;
char command[1024+1];
char output[1024+1];

fprintf(stderr, "\n\n");
/**************************************************/
/** Are we online or offline? **/
/**************************************************/
INT32 mode;
GetOnlineMode(&mode);
fprintf(stderr, "Online?\t\t\t%ld\t(0 = offline, 1 = online)\n", mode);
/**************************************************/
/** Which user mode? **/
/**************************************************/
long usermode;
GetUserMode(&usermode);
fprintf(stderr, "Usermode?\t\t%ld\t(Protected mode has value 5)\n", usermode);
if(5 != usermode) {
return -1;
}

/**************************************************/
/** Who has called us? **/
/**************************************************/
fprintf(stderr, "The pid of our parent is %d\n", getppid());
/**************************************************/
/**Is our caller registered with the SmarTest SW?**/
/**************************************************/
sprintf(command,"%s| grep SA_PRC_TF | awk {'print $3'}", SA_PROCESS_INFO);
fd=popen(command, "r");
int registered_pid;

fgets(output, 1024, fd);
sscanf(output,"%d", &registered_pid);

fprintf(stderr, "Pid registered for TF: %d\n", registered_pid);
fclose(fd);

if(registered_pid != getppid()) {
return -1;
}
/**************************************************/
/** md5sum of our parent **/
/**************************************************/
sprintf(command, "md5sum /proc/%d/exe", getppid());
fd=popen(command, "r");
char temp[1024+1];
fgets(output, 1024, fd);
char md5sum[32+1];
sscanf(output, "%s %s", md5sum, temp);
fprintf(stderr, "md5sum of parent:\t%s\n", md5sum);
fclose(fd);

/**************************************************/
/** location of our parent **/
/**************************************************/
sprintf(command, "/proc/%d/exe", getppid());
int length=readlink(command, output, 1024);
output[length]=0;
fprintf(stderr, "loc of parent:\t\t%s\n", output);

/**************************************************/
/** working directory of our parent **/
/**************************************************/
sprintf(command, "/proc/%d/cwd", getppid());
length=readlink(command, output, 1024);
output[length]=0;
fprintf(stderr, "cwd of parent:\t\t%s\n", output);
/**************************************************/
/** root directory of our parent **/
/**************************************************/
sprintf(command, "/proc/%d//", getppid());
length=readlink(command, output, 1024);
output[length]=0;
fprintf(stderr, "root of parent:\t\t%s\n", output);
return 0;
}
void decrypt(int argc, char* argv[])
{
if(-1 == securityChecks()) {
return;
}
char command[1024+1];
if(0 == strcmp(argv[2], "config")) {
fprintf(stderr, "Loading pins...\n");
sprintf(command, "echo %s | ccrypt -c -k - %s", "VERIGY93K", argv[1]);
system(command);
}
else if(0 == strcmp(argv[2], "level")) {
fprintf(stderr, "Loading levels...\n");
sprintf(command, "echo %s | ccrypt -c -k - %s", "VERIGY93K", argv[1]);
system(command);
}
else if(0 == strcmp(argv[2], "timing")) {
fprintf(stderr, "Loading timing...\n");
sprintf(command, "echo %s | ccrypt -c -k - %s", "VERIGY93K", argv[1]);
system(command);
}
}
void plain(int argc, char* argv[])
{
char command[1024+1];
if(strstr(argv[1], ".gz")) {
sprintf(command, "gunzip -c %s", argv[1]);
}
else if(strstr(argv[1], ".Z")) {
sprintf(command, "uncompress -c %s", argv[1]);
}
else {
sprintf(command, "cat %s", argv[1]);
}
system(command);
}
int main(int argc, char* argv[])
{
HpInit();
if(argc == 5) {
if(0 == strcmp(argv[2], "config")) {
decrypt(argc, argv);
}
else if(0 == strcmp(argv[2], "level")) {
decrypt(argc, argv);
}
else if(0 == strcmp(argv[2], "timing")) {
decrypt(argc, argv);
}
else {
plain(argc, argv);
}
}
exit(CI_CALL_PASS); /* program completed without error */
HpTerm();
}
```

### Example（取自子主题 Collision handling）

See the examples in each kind of setup master file collision handling.

### Examples（取自子主题 Pattern editor properties view）

### Vector properties

The graphic below shows the properties of a vector in
device cycle (DVC) format.

On vector properties views you cannot edit any parameters. Do this in the pattern
editor.

The vector properties view always shows the physical waveform. Drive edges and
receive edges appear on two different lines. In collapsed mode the view is based on the
`base wavetable`（raw: `107915.htm`）
, in expanded mode the properties are taken from the
primary wavetable.

Any abbreviations you may use in your wavetables, are translated into
the proper action code for
`drive edges`（raw: `10603.htm`）
 and
`receive edges`（raw: `10606.htm`）
.

[表]
列: Drive edges | | | Receive edges |
行 1:
  Abbreviation
  Action code
  
  Abbreviation
  Action code
行 2:
  0
  F00
  
  L
  E0
行 3:
  1
  F10
  
  H
  E1
行 4:
  !Z
  FN0
  
  M
  EI
行 5:
  Z
  FNZ
  
  U
  EU
行 6:
  . (period)
  N
  
  X
  EX
行 7:
  
  
  
  . (period)
  N

### Test point properties

The graphic below shows the properties of a test
point, in this case the highlighting of a force value in a dynamic DC test setup.

The properties view of a dynamic DC measure test point will also show the measure
result. See below:

### Vector variable properties

The properties view of a vector variable (see
below) allows to edit for example, the assigned pins, the transfer mode, and other parameters.
To display additional data upload formatting parameters (Upload Parameters) click the

Show Advanced Properties
 icon. For a definition of the vector variable
parameters see
`Creating a Digital Capture setup`（raw: `116306.htm`）
.

Note
 The Upload Parameters shown here are the last which were used by the
system. If you stop a testflow at a particular test suite and then open the pattern editor, the
vector variable data is shown exactly as it was last uploaded from any test method or any
command line operation.

### Example（取自子主题 Firmware view）

As the following example shows, the
VECD?
 query returns vector data
from the sequencer memory in the range between 0 and 8, for the S0_1 pin.

Add the
$
 prefix to the query command to retrieve the binary data in a
readable format.

<!-- 语法节 end -->

## 是什么

**文档事实** Test Program Explorer 包含于 Setup perspective，提供测试 setup 数据的层级视图；从这里可调出全部 device setup 工具，如 Pin Configuration Tool、Pattern Tool 等。

**文档事实** 用 Test Program Explorer 加载 setup 数据时，数据从 system controller 的文件系统加载到测试系统。

**文档事实** 若显示的是文件名而非组件名（例如 `<Levels...>`），表示加载的是对应的数据文件；文件名旁的 `*` 表示数据已改动且尚未保存；文件名旁的 `[external]` 表示加载了不属于当前 device 的组件。

**文档事实** 双击任一 setup 组件会打开相应的 setup 工具；Test Program Explorer 也显示部分结果文件，如 shmoo data。

**文档事实** 其工具栏图标提供：折叠全部 setup 组件；保存（只保存已修改未保存的组件，或保存全部已加载组件，行为可在 Test Program Explorer preference page 设定）；展开全部组件；以及一个提供展开/折叠全部组件菜单项的图标。

## 典型用法

**文档事实** 双击 Pin Configuration 会打开 Pin Configuration Tool；在 Test Program Explorer 中右键 Channel Attributes，可从快捷菜单打开相应编辑器（如 Channel Attributes Editor、Fixture Delay Tool）。

**文档事实** 加载或卸载 data logging profile 既可在 Test Program Explorer 进行，也可在 operation control window 进行。

**文档事实** 右键 testflow 选 Load all setups；右键 Protocols 节点选 Build all 可校验所有已加载 protocol（只选单个 protocol 时可只 build 该 protocol）。

**文档事实** 工具栏保存图标的行为可在 Test Program Explorer preference page 中设为"只保存已修改未保存的"或"保存全部已加载的"。

**文档事实** 子主题 Working with Test Program Explorer 给出本视图的操作步骤；Protection for your setup files、Customizable Scripts、Setup Management Tool 分别覆盖 setup 文件保护、可定制脚本与 setup 管理。

## 和谁有关

- **文档事实** Setup perspective — 明确说明 Test Program Explorer 是其组成部分，层级显示测试 setup 数据并从此启动 device setup 工具（两页互引）。
- **文档事实** Working with Test Program Explorer — 本页子主题，给出操作流程。
- **文档事实** Customizable Scripts、Protection for your setup files、Setup Management Tool — 本页子主题。
- **文档事实** Debug perspective — 该页也描述 Test Program Explorer 显示全部 device setup 工具。
- **文档事实** Channel Attributes Editor、Fixture Delay Tool — 说明在 Test Program Explorer 右键 Channel Attributes 打开编辑器。
- **文档事实** Validating a protocol definition — 说明在 Test Program Explorer 右键 Protocols > Build all。
- **文档事实** Loading a data logging profile、Unloading a data logging profile — 说明可在 Test Program Explorer 加载/卸载。
- **文档事实** Working with testflows efficiently — 说明在 Test Program Explorer 右键 testflow > Load all setups。
- **文档事实** Test Program Explorer preference page — 控制保存图标的行为。
- **文档事实** UPTD (UP To Date) 命令页 — 引用 Test Program Explorer。

## 版本

**文档事实** Functional changes 记载：Introduced before SmarTest 6.3.2；SmarTest 6.5.4：Device Information 增加 Channel attributes；SmarTest 7.0.3：从 Test Program Explorer 移除 Test control；SmarTest 7.0.3：Bitmap 结果数据不再显示在 Test Program Explorer；SmarTest 7.1.0：新增 Protocols 与 Protocol Assignments。

## 出处

- `01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02_Test_Program_Explorer.htm`，主源，含视图说明、工具栏图标表与 Functional changes。
- 语法节子主题 `01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02.03.01_Customized_hp83_import_for_encrypted_setup_files.htm`。
- 语法节子主题 `01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.02.02.04.05_Collision_handling.htm`、`01_Getting_started/01.01_SmarTest_Work_Center/01.01.08.08_Firmware_view.htm`、`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.16.02.03_Pattern_editor_properties_view.htm`。
