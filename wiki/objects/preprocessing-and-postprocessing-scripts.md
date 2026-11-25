---
type: object
title: Preprocessing and postprocessing scripts
layer: file
stage: project
tags: []
related: []
sources:
  - 02_System_reference/02.09_Test_Program_Management/02.09.02.03.03_Preprocessing_and_postprocessing_scripts.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Preprocessing and postprocessing scripts

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **2,964 字符逐字取自** `<02_System_reference/02.09_Test_Program_Management/02.09.02.03.03_Preprocessing_and_postprocessing_scripts.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

Both the
pre_proc
 (shown below) and
post_proc

parameters have the same
syntax.

```
pre_proc = '<script>[&mdir][&sdir][&mtp_tf][&mtp_pmf][&mtp_conf][&mtp_tim][&mtp_lev][&mtp_tt][&mtp_rout][&mtp_wf][&mtp_anctrl][&mtp_chatt][&mtp_prot][&mtp_att][&stp_tf][&stp_pmf][&stp_conf][&stp_tim][&stp_lev][&stp_tt][&stp_rout][&stp_wf][&stp_anctrl][&stp_chatt][&stp_prot][&stp_att][<user_parameters>]'
```

The
available script parameters in the order in which they are listed above:

[表]
行 1:
  <script>
  The name and path of the script file to call.
    
    The path can be absolute or relative. If it is a relative path, the base directory is the
    current working directory at the time STPM was called.
行 2:
  &mdir
  Full path to the MTP directory.
行 3:
  &sdir
  Full path to the STP directory.
行 4:
  &mtp_tf
  Full path to the MTP testflow file.
行 5:
  &mtp_pmf
  Full path to the MTP pattern master file.
行 6:
  &mtp_conf
  Full path to the MTP configuration file.
行 7:
  &mtp_tim
  Full path to the MTP timing file.
行 8:
  &mtp_lev
  Full path to the MTP levels file.
行 9:
  &mtp_tt
  Full path to the MTP test table file.
行 10:
  &mtp_rout
  Full path to the MTP routing file.
行 11:
  &mtp_wf
  Full path to the MTP waveform file.
行 12:
  &mtp_anctrl
  Full path to the MTP analog control file.
行 13:
  &mtp_chatt
  Full path to the MTP channel attributes file.
行 14:
  &mtp_prot
  Full path to the MTP protocols file.
行 15:
  &mtp_att
  Full path to the MTP pin attributes file.
行 16:
  &stp_tf
  Full path to the STP testflow file.
行 17:
  &stp_pmf
  Full path to the STP pattern master file.
行 18:
  &stp_conf
  Full path to the STP configuration file.
行 19:
  &stp_tim
  Full path to the STP timing file.
行 20:
  &stp_lev
  Full path to the STP levels file.
行 21:
  &stp_tt
  Full path to the STP test table file.
行 22:
  &stp_rout
  Full path to the STP routing file.
行 23:
  &stp_wf
  Full path to the STP waveform file.
行 24:
  &stp_anctrl
  Full path to the STP analog control file.
行 25:
  &stp_chatt
  Full path to the STP channel attributes file.
行 26:
  &stp_prot
  Full path to the STP protocols file.
行 27:
  &stp_att
  Full path to the STP pin attributes file.
行 28:
  <user_parameters>
  Text that is passed unchanged to the script. This text must not contain any words
    that begin with &.

Except for the name of the script file, all elements are optional.

### Example

This example executes the
write_tp
 command with two scripts:

Before
write_tp
 itself is executed, the

preparation.py
 script from the current working directory is run. No
parameters are passed to this script.

After
write_tp
 has finished executing, the

cleanup.pl
 script is run. This script receives this parameter string
(assuming that the MTP is located in
/user/johndoe/mtp
):

--mdir
'/user/johndoe/mtp' --cmd write --stage
3

```
write_tp('user/johndoe/mtp/flow1.tf',
pre_proc = 'preparation.py',
post_proc = '/usr/tools/scripts/cleanup.pl &mdir --cmd write --stage 3')
```

<!-- 语法节 end -->

## 是什么

**文档事实**：STPM control file 中的命令允许通过 `pre_proc` 与 `post_proc` 指定预处理/后处理脚本，分别在命令本身执行之前/之后自动运行（`02.09.02.03.03`）。

**文档事实**：可以指定任何能在运行 STPM 的计算机上执行的脚本；操作者负责确保脚本所需的支持（如脚本语言的解释器）可用，并确保脚本能处理传给它的参数（`02.09.02.03.03`）。

**文档事实**：`pre_proc` 与 `post_proc` 语法相同；值由脚本名和参数组成，除脚本名外所有元素都是可选的（`02.09.02.03.03`）。

**文档事实**：系统参数以 `&` 开头，脚本执行时被替换为 `--` 加同名参数和对应值；参数列表末尾可追加任意自定义参数，原样传给脚本，且自定义参数不得以 `&` 开头（`02.09.02.03.03`）。

**文档事实**：`&mtp_*` 提供 MTP 各文件/目录的完整路径（`&mtp_tf` testflow、`&mtp_pmf` pattern master、`&mtp_conf` configuration、`&mtp_tim` timing、`&mtp_lev` levels、`&mtp_tt` test table、`&mtp_rout` routing、`&mtp_wf` waveform、`&mtp_anctrl` analog control、`&mtp_chatt` channel attributes、`&mtp_prot` protocols、`&mtp_att` pin attributes），`&stp_*` 对应 STP，另有 `&mdir`/`&sdir` 指向 MTP/STP 目录（`02.09.02.03.03`）。

**文档事实**：脚本路径可为绝对或相对路径；相对路径以调用 STPM 时的当前工作目录为基准（`02.09.02.03.03`）。

**推断**：这两个参数是 STPM 命令的通用「钩子」——在合并/写文件前后插入任意外部处理，而 STPM 只负责把路径和自定义参数拼成命令行。

## 典型用法

**文档事实**：示例在 `write_tp` 上同时用两个脚本：命令前运行当前目录的 `preparation.py`（不传参数），命令后运行 `/usr/tools/scripts/cleanup.pl &mdir --cmd write --stage 3`；若 MTP 在 `/user/johndoe/mtp`，脚本收到 `--mdir '/user/johndoe/mtp' --cmd write --stage 3`（`02.09.02.03.03`）。

**文档事实**：自定义参数加在参数列表末尾，不加 `--`、不改写，直接传给脚本；系统 `&` 参数则由 STPM 展开为 `--参数名 值`（`02.09.02.03.03`）。

**文档事实**：任何支持 `pre_proc`/`post_proc` 的 STPM 命令都可使用，例如 `write_tp`、`add_test`、`add_burst`、`add_test_to_burst`、`add_empty_test_group`、`remove_test`、`replace_test` 的参数表中都列出这两个可选参数（`02.09.02.03.03`、`02.09.02.03.04`–`02.09.02.03.10`）。

**文档事实**：脚本名是必需项；`&mdir`、`&sdir`、`&mtp_*`、`&stp_*` 与用户参数都可省略，只写脚本名也可以（`02.09.02.03.03`）。

**建议**：把 STPM 命令的前后处理放进脚本，而不是依赖手工步骤——文档的定位就是让脚本随命令自动运行；同时由使用方自行保证解释器可用（`02.09.02.03.03`）。

## 和谁有关

- **STPM control file**（[[stpm-control-file]]）— **文档事实**：控制文件中的命令带 `pre_proc`/`post_proc` 参数，这两个参数就是本主题（`02.09.02.03.03` 的 Related information）。
- **write_tp** — **文档事实**：示例命令；其参数说明把 `pre_proc`/`post_proc` 指向本主题（`02.09.02.03.03`、`02.09.02.03.04`）。
- **add_test / add_burst / add_test_to_burst / add_empty_test_group / remove_test / replace_test** — **文档事实**：这些 STPM 命令的语法都含可选的 `pre_proc`/`post_proc`，因此都可挂本主题的脚本（`02.09.02.03.03`；各命令语法见 `02.09.02.03.05`–`02.09.02.03.10`）。
- **MTP / STP 文件** — **文档事实**：`&mtp_*`/`&stp_*` 向脚本传递 MTP/STP 的 testflow、pattern master、configuration、timing、levels 等文件路径，`&mdir`/`&sdir` 传递目录（`02.09.02.03.03`）。
- **脚本解释器（Python/Perl 等）** — **文档事实**：示例使用 `preparation.py` 与 `cleanup.pl`；文档要求操作者保证脚本所需支持（如解释器）可用（`02.09.02.03.03`）。
- **STPM** — **文档事实**：脚本由 STPM 在命令执行前/后自动调用，并把 `&` 参数展开后传入（`02.09.02.03.03`）。

## 版本

**文档事实**：Functional changes 记 “Introduced in SmarTest 7.2.2”（`02.09.02.03.03`）。

**文档事实**：文档没有为 `pre_proc`/`post_proc` 的参数集给出更细的版本变更记录（`02.09.02.03.03`）。

## 出处

- `02_System_reference/02.09_Test_Program_Management/02.09.02.03.03_Preprocessing_and_postprocessing_scripts.htm`（主文档：Supported scripts、Parameters for the scripts、Syntax、Example、Related information、Functional changes）
- 关联：`02_System_reference/02.09_Test_Program_Management/02.09.02.03_STPM_control_file.htm`（命令所在控制文件）
