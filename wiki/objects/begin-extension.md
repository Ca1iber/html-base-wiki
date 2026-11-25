---
type: object
title: BEGIN_EXTENSION
layer: L2
stage: testmethod
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.10_BEGIN_EXTENSION.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# BEGIN_EXTENSION

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **3,216 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.10_BEGIN_EXTENSION.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
void BEGIN_EXTENSION();
void BEGIN_EXTENSION(STRING& sites);
void BEGIN_EXTENSION(ARRAY_I& sites);
```
[表] Parameter
列: I/O | Parameter | Description / Range
行 1:
  I
  sites
  This parameter sets the setup focus sites for the statements in the extension
    block.
    
    To make the extension block effective for sites 1 to 3 in four sites,
    
    STRING: "1110".
    
    ARRAY_I: sites[0]=1, sites[1]=2, and sites[2]=3.

### Important points

BEGIN_EXTENSION
 and
END_EXTENSION
 should be
used as a pair. The area enclosed by
BEGIN_EXTENSION
 and

END_EXTENSION
 is called "
extension block
".

You can describe the
`FW_TASK`（raw: `29362.htm`）
 functions within the extension block. One or
more
FW_TASK
s can be applied to this block. Beside the

FW_TASK
 function, you can also describe the function you originally
created. You should not describe the other test method APIs in the extension block.

For data setup, a conflict might occur between the test method API outside the extension
block and firmware commands within the extension block. To avoid such a conflict, you should
consider the following actions:

The caching mechanism of the test method is temporarily turned off between the "extension
block" explicitly declared by
BEGIN_EXTENSION
 and

END_EXTENSION
. This is implicitly done by the system.

You should execute the
FLUSH
 API before entering the extension
block. The setup data relating to the API such as
ANALOG
,

ANALOG_STATUS
,
PRIMARY_STATUS
, and

ROUTING_STATUS
 will be stored in the caching mechanism. The

FLUSH
 API downloads the setup data to the system hardware or the
MCD.

For multi-site testing, you can specify optional parameter
sites
 to
set the setup focus sites for the statements in the extension block. Therefore, the statements
will be performed for the specified sites only.

In this case, you can make nested extension
blocks.

END_EXTENSION
 just after
BEGIN_EXTENSION

reverts the setup focus sites to the same settings as before entering the extension block.

This allows you to do complicated and flexible site management correctly. If the extension
block is not nested correctly, the nest information will be initialized at the end of the test
suite execution automatically. Also, a warning message appears in the report window.

### Examples

### Example 1: BEGIN_EXTENSION and END_EXTENSION declare the extension block
```
STRING dfcm("DFCM 1,4000,50,-1.00,1.00,4000,5,I,0,PPNP,(CP)\n");
STRING ptstq("PTST? 1,NONE,NONE,PVAL\n");

BEGIN_EXTENSION();

FW_TASK(dfcm);

STRING answer;

FW_TASK(ptstq, answer);
...
...

END_EXTENSION();
```

### Example 2: Extension block for all enabled sites
```
STRING enabled_sites;

GET_ENABLED_SITES(enabled_sites);

BEGIN_EXTENSION(enabled_sites);

//
// Your FW_TASK code
//
...
...

END_EXTENSION();
```

The

GET_ENABLED_SITES
 API retrieves the information of the current enabled
sites and stores it to the variable
enabled_sites
.

BEGIN_EXTENSION
 and
END_EXTENSION
 declare the
extension block for multi-site testing. In this example, the extension block is effective for
the current enabled sites.
BEGIN_EXTENSION
 sets the current enabled sites
to the setup focus sites. Therefore, the statements will be performed for the current enabled
sites only.

<!-- 语法节 end -->

## 是什么

**文档事实** BEGIN_EXTENSION 是 test method API，与 END_EXTENSION 成对使用；二者围出的区域称为 extension block。

**文档事实** extension block 内可描述 FW_TASK 函数（一个或多个 FW_TASK 可作用于该块），也可描述自己创建的函数；不应在块内描述其他 test method APIs。

**文档事实** 为避免 extension block 外的 test method API 与块内 firmware 命令在数据 setup 上冲突，系统会在 BEGIN_EXTENSION 与 END_EXTENSION 之间临时关闭 test method 的 caching 机制。

**文档事实** 应在进入 extension block 前执行 FLUSH API；ANALOG、ANALOG_STATUS、PRIMARY_STATUS、ROUTING_STATUS 等 API 的 setup 数据会存于 caching 机制，FLUSH 将其下载到系统硬件或 MCD。

**文档事实** 多 site 测试可用可选参数 `sites` 设定块内语句的 setup focus sites，使语句只对指定 site 执行；extension block 可嵌套，紧接 BEGIN_EXTENSION 的 END_EXTENSION 会把 setup focus sites 恢复到进入前；嵌套不正确时 nest 信息在 test suite 执行结束时自动初始化，并在 report window 出现 warning。

**文档事实** `sites` 的两种写法：STRING 时，四 site 中让 site 1..3 生效写 `"1110"`；ARRAY_I 时，`sites[0]=1`、`sites[1]=2`、`sites[2]=3`。

**推断** 因此 BEGIN_EXTENSION 是「在 test method 中安全插入原始 firmware 命令」的边界标记，并兼管 site 焦点切换。

## 典型用法

**文档事实** 基本块：`BEGIN_EXTENSION();` 后接 `FW_TASK(dfcm);`、`FW_TASK(ptstq, answer);` 等，最后 `END_EXTENSION();`；示例中的 dfcm 为 `DFCM 1,4000,50,-1.00,1.00,4000,5,I,0,PPNP,(CP)\n`，ptstq 为 `PTST? 1,NONE,NONE,PVAL\n`。

**文档事实** 对全部 enabled sites 生效：`GET_ENABLED_SITES(enabled_sites); BEGIN_EXTENSION(enabled_sites); ... END_EXTENSION();`；BEGIN_EXTENSION 把当前 enabled sites 设为 setup focus sites，块内语句只对这些 site 执行。

**文档事实** 指定 site 子集：四 site 中只让 site 1..3 生效，STRING 写 `"1110"`，ARRAY_I 写 `sites[0]=1; sites[1]=2; sites[2]=3;`。

**文档事实** 进入块前先执行 FLUSH；块内用 FW_TASK 执行 firmware 命令，也可调用自建函数；不要把其他 test method APIs 放进块内。

**文档事实** 嵌套块中用 END_EXTENSION 逐层恢复 setup focus；若嵌套不正确，系统在 test suite 执行结束时自动初始化 nest 信息并给 warning。

**建议** 把 extension block 保持得尽量短，只在确需原始 firmware 命令时打开，并严格遵守「先 FLUSH、块内不混用其他 test method APIs」。

## 和谁有关

- **文档事实** END_EXTENSION：与 BEGIN_EXTENSION 成对声明 extension block；END_EXTENSION 页写明本 API 由 BEGIN_EXTENSION 开始、细节见 BEGIN_EXTENSION。
- **文档事实** FW_TASK：BEGIN_EXTENSION 和 END_EXTENSION 总是与 FW_TASK 一起使用；块内除 firmware 命令外也可执行自建函数。
- **文档事实** GET_ENABLED_SITES()：示例用它取得当前 enabled sites 并传给 BEGIN_EXTENSION，使块只对 enabled sites 生效。
- **文档事实** FLUSH：主源要求在进入 extension block 前执行 FLUSH，把 ANALOG、ANALOG_STATUS、PRIMARY_STATUS、ROUTING_STATUS 等缓存 setup 数据下载到硬件或 MCD。
- **文档事实** Executing Firmware Commands：该页指向 FW_TASK、BEGIN_EXTENSION、END_EXTENSION 了解如何在 test method 中执行 firmware 命令。
- **文档事实** Important Points on Multisite Programming：说明可在 first-invocation block 中用带 site 参数的 BEGIN_EXTENSION 与 END_EXTENSION 包住 FW_TASK（入边）。
- **文档事实** Usage of Parallel Hardware (PPMU) 与 Multisite handling with test flow branching：应用论文入边引用 BEGIN_EXTENSION，前者涉及多 site first-invocation，后者处于 site 重新激活后重连 AC relay 的语境。
- **文档事实** APIs in alphabetical order：BEGIN_EXTENSION 列在 test method API 总表。
- **文档事实** Extension.h：END_EXTENSION 与 FW_TASK 页给出头文件 `/opt/hp93000/soc/prod_com/include/MAPI/Extension.h`；BEGIN_EXTENSION 主源本身未给头文件。

## 版本

**文档事实** Functional changes 记：Introduced before SmarTest 6.3.2。

## 出处

- `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.10_BEGIN_EXTENSION.htm`，主源，含 Syntax、Important points、Examples 与 Functional changes，已用 `show.py` 读取。
- `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.59_END_EXTENSION.htm`、`02.07.04.01.77_FW_TASK.htm`、`02.07.04.01.86_GET_ENABLED_SITES.htm`，用于配对关系、FW_TASK 用法与 enabled sites 语义，已用 `show.py` 读取。
- `02_System_reference/02.07_Test_Method_Reference/02.07.03.10_Executing_Firmware_Commands.htm`、`02.07.03.13.08_Important_Points_on_Multisite_Programming.htm` 以及应用论文中的引用，取自 `extract/objpack.py` / `edges.jsonl` 的入边语境。
