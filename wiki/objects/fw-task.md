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

（待补）

## 典型用法

（待补）

## 和谁有关

（待补）

## 版本

（待补）

## 出处

（待补）
