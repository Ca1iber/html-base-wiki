---
type: object
title: FW_TASK
layer: L2
stage: testmethod
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.77_FW_TASK.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# FW_TASK

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **4,828 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.77_FW_TASK.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

For
setting:

```
FWTASK_STATUS FW_TASK(const STRING& command);
```

For
query:

```
FWTASK_STATUS FW_TASK(const STRING& command, STRING& answer);
```

To
retrieve binary
data:

```
FWTASK_STATUS FW_TASK(const STRING& command, FW_ResultData & resultdata);
```

Parameters
[表]
列: I/O | Parameter | Description
行 1:
  I
  command
  Command string with one or more commands. Each string can be
    limited by a newline (\n) or a
    semicolon.
    
    Multiple FW commands, delimited with a newline
    (\n) or a semicolon, can be combined
    in the command string.
行 2:
  O
  answer
  Answer string as the response to the firmware command. Its
    maximum length is 1 MB. If the answer string exceeds the limit of
    the length, a system error will occur.
行 3:
  O
  resultdata
  A reference to an existing object of type FW_ResultData. The function fills
    this object with the retrieved data.
    
    The FW_ResultData object provides
    the following parameters:
    
      [子表]
      列: Parameter | Type | Description
      子行 1:
        Answer
        String
        The FW answer string without the binary
          data part
      子行 2:
        BinaryDataLength
        unsigned int
        The data length
      子行 3:
        BinaryData
        char*
        The data string
    
    See also `Example 3: Retrieve DPS current measurement results`（raw: `29362.htm#_29362__ex_retrive_binary_data`） below.
Return value
The following enumerators of type
FWTASK_STATUS
 are returned:

FW_PASSED
: The firmware commands are successfully
executed.

FW_WARNING
: A warning has been generated from
execution of the firmware commands. The
`Message Concentrator and Distributor (MCD)`（raw: `10402.htm#_10402__p_MCD`）
 generates the
warning and it is output to the report window. You may have to
confirm the contents of the warning and modify the test method
program.

FW_BREAK
: If the break has occurred during the firmware execution,
this is returned. When you press the
Break

button in the SmarTest Main Menu, the break signal is sent to the
MCD and the digital sequencer is changed to the

BRK
 state. The system hardware operation
stops and the digital channels continue to output the break vectors.
Then, control returns to the test method and program execution will
be continued. If the firmware execution fails for reasons not
mentioned above, an error will occur. For details, see the
`Command Reference`（raw: `103977.htm`）
 Manual. When an error occurs, the test method
execution aborts. In other words, program execution terminates at
this point. Note that two kinds of error message are output to the
report window. One is the error message generated from the test
method if error messages have been activated by the
`ENABLE_ERROR_MESSAGE`（raw: `29298.htm`）
 API. The other is the message generated from
the MCD.

### Examples

### Example 1: Execute setting command
```
FW_TASK("UTOT 1, 65535, 12345\n");
```

This API
sets output lines URW15, 14, UW13 to 7 and URW06 to 00, to 53190 (inverted value of
12345) at the firmware level. Note that you need to terminate the command string
with "
\n
" (newline) or "
;
"(semicolon)
even if the only single command string is used.

### Example 2: Execute querying command
```
STRING answer;

if (FW_TASK("DFPS?(@)\n", answer) == FW_PASSED)
{
// continue the processing ....
}
```

If
the firmware command
DFPS?
 is executed successfully and the

FW_TASK
 returns
FW_PASSED
, the
statements in the "
if
" block are executed.

### Example 3: Retrieve DPS current measurement results
```
FW_ResultData data;

FW_TASK("DPSE 1,(dps1),#150,1,2");
FW_TASK("PSST ON");
FW_TASK("PSEE 1,,,(dps1)");
FW_TASK("PSER? 1,pval", data);

cout << "Answer: " << data.Answer << endl;
cout << "BinaryData: " << endl;

for ( unsigned int i = 0; i < data.BinaryDataLength; i++ )
{
cout << data.BinaryData[i];
}
```

To
retrieve the binary data, the API executes the DPSE, PSST, and PSEE commands
followed by the PSER? query. The result contains the properties of the retrieved
data.

### Example 4: Enable the trace function / MCDLog

The following code enables and disables the
`trace function`（raw: `10408.htm`）
 using
the
`DIAG`（raw: `98562.htm`）
 command and writes some annotations to the

MCDLog
 file using the
`NOOP`（raw: `98664.htm`）

command.

```
string testSuiteName;

GET_TESTSUITE_NAME(testSuiteName);

//
// Open the MCDLog, write the first annotation
//
FW_TASK("DIAG 2");

FW_TASK("NOOP \"##########\",\"" + testSuiteName + "\",\"Start\",");

//
// Execute tests and write some annotations
//
...
...
FW_TASK("NOOP \"##########\",\"" + testSuiteName + "\",\"Step\",1");
...
...
FW_TASK("NOOP \"##########\",\"" + testSuiteName + "\",\"Step\",2");
...
...
//
// Close the MCDLog
//
FW_TASK("DIAG -2");
```

Note: You must use a backslash "\" as escape character to insert strings that are enclosed in
quotation marks into the command string.

<!-- 语法节 end -->

## 是什么

**文档事实** FW_TASK 是 test method API，允许从 test method 在 firmware 层直接访问系统硬件。

**文档事实** 若 test method 程序中需要使用多条 firmware commands，该 API 提供按需执行一条或多条 firmware commands 的环境。

**文档事实** 文档规定 BEGIN_EXTENSION 与 END_EXTENSION 始终与 FW_TASK 一起使用；除 firmware command 外，也可在二者之间执行自己创建的函数。

**文档事实** 该 API 定义在头文件 `/opt/hp93000/soc/prod_com/include/MAPI/Extension.h`。

**文档事实** 有三个重载：执行设置命令；执行查询命令并把应答写入 `STRING& answer`；取二进制数据并写入 `FW_ResultData& resultdata`。

**文档事实** 返回类型 FWTASK_STATUS 的枚举包括 FW_PASSED（命令成功执行）、FW_WARNING（MCD 产生警告并输出到 report window）、FW_BREAK（固件执行期间发生 break 时返回；按 SmarTest 主菜单 Break 后，break 信号送到 MCD，数字 sequencer 进入 BRK 状态，系统硬件停止而数字通道继续输出 break vectors，随后控制返回 test method 并继续执行）。

**文档事实** 若 firmware 执行因上述以外原因失败则发生 error，test method 执行中止；report window 输出两类错误消息：由 ENABLE_ERROR_MESSAGE 激活的 test method 错误消息，以及 MCD 产生的消息。

**文档事实** 查询用的 answer 最大 1 MB，超过限制会触发 system error。

## 典型用法

**文档事实** 设置命令示例为 `FW_TASK("UTOT 1, 65535, 12345\n");`；文档说明它在 firmware 层把输出线 URW15、14、UW13 置 7，URW06 置 00、值 53190（12345 的反相值）。命令串即使只有一条，也须以 `\n` 或 `;` 结尾。

**文档事实** 查询命令示例为 `STRING answer; if (FW_TASK("DFPS?(@)\n", answer) == FW_PASSED) { ... }`；DFPS? 成功执行且返回 FW_PASSED 后，if 块中的语句执行。

**文档事实** 取二进制数据示例依次执行 `DPSE 1,(dps1),#150,1,2`、`PSST ON`、`PSEE 1,,,(dps1)`、`PSER? 1,pval`，最后一条用 `FW_ResultData data` 接收；结果含 Answer、BinaryDataLength 与 BinaryData。

**文档事实** trace/MCDLog 示例用 `FW_TASK("DIAG 2")` 开启 trace、`FW_TASK("DIAG -2")` 关闭，并用 NOOP 命令经 FW_TASK 向 MCDLog 写注释；字符串内的引号须用反斜杠转义。

**文档事实** 多条 firmware 命令可用换行 `\n` 或分号 `;` 分隔后合并在一个 command string 中。

**文档事实** FFCI 页说明 FFCI? 命令也可用 FW_TASK 执行，取二进制数据必须使用 `FWTASK_STATUS FW_TASK(const STRING& command, FW_ResultData & resultdata);`。

**文档事实** 多 site 编程页说明：在多 site 测试的 first-invocation block 中，应把 FW_TASK 包在带 site 参数的 BEGIN_EXTENSION 与 END_EXTENSION 之间。

## 和谁有关

- **文档事实** BEGIN_EXTENSION 与 END_EXTENSION，文档规定二者始终与 FW_TASK 一起使用；extension block 内可放一个或多个 FW_TASK 及自建函数，不应放其他 test method API；BEGIN_EXTENSION 页还要求进入 block 前执行 FLUSH 下载缓存设置。
- **文档事实** Command Reference，FW_TASK 执行的是 firmware commands，文档把命令细节指向该手册。
- **文档事实** FW_ResultData，SmarTest 7.1.0 新增的类，作为二进制数据重载的输出对象，提供 Answer、BinaryDataLength、BinaryData。
- **文档事实** MCD，FW_WARNING 由 MCD 产生并输出到 report window；出错时 MCD 的消息也会输出；FLUSH 的缓存设置下载目标是系统硬件或 MCD。
- **文档事实** ENABLE_ERROR_MESSAGE，决定 test method 错误消息是否输出到 report window。
- **文档事实** DIAG 与 NOOP，Example 4 用 FW_TASK 执行它们来开关 trace 与写 MCDLog 注释。
- **文档事实** GET_TESTSUITE_NAME，Example 4 用它取得 test suite 名称后再写 MCDLog 注释。
- **文档事实** FFCI，FFCI 页说明其命令也可经 FW_TASK 执行，并指定用 FW_ResultData 重载取二进制数据。
- **文档事实** Executing firmware commands from within a program，该页把“从 test method 执行 firmware command”落到 FW_TASK。
- **文档事实** Important Points on Multisite Programming（System reference 与 Multi-Site Testing 两个版本），两页都要求把 FW_TASK 包在带 site 参数的 BEGIN_EXTENSION/END_EXTENSION 中。

## 版本

**文档事实** Functional changes 记：Introduced before SmarTest 6.3.2；SmarTest 7.1.0 新增类 FW_ResultData。

## 出处

- `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.77_FW_TASK.htm`，主源，含 Application note、Syntax、Parameters、Return value、Examples、Related information 与 Functional changes。
- `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.10_BEGIN_EXTENSION.htm`，用于核对 extension block 与 FLUSH 的关系（已用 show.py 读取）。
- FFCI、多 site、Executing firmware commands 的引文取自 objpack 入边索引。
