---
type: object
title: Error Map Tool
layer: gui
stage: results
tags: []
related: []
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.08_Error_Map_Tool.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Error Map Tool

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **751 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.08_Error_Map_Tool.htm>` 及其子主题 `<02_System_reference/02.06_Command_Reference/02.06.11.01.02.01.05_Dealing_with_storage_problems_on_Smart_Scale_systems.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Dealing with storage problems on Smart Scale systems）

Suppose that the default port
@
 comprises 8 IO pins,

P1
 through
P8
, and that all these pins are associated with a
channel of the 8-channel group 10101 through 10108 on an PS1600 system. Assume further that you
want edge information about
r2
,
r4
,
r6
,
and
r8
 for pins
P1
,
P3
,

P5
, and
P7
. Then the following setup would minimize the risk
that recording is
aborted:

```
DCRT RAM,(@)
DCEL DCRT,TP,SET,(P2,P4,P6,P8)
DCRM EMAP,4,PF,"c1:2 c2:4 c3:6 c4:8",(@)
```

If
you call
EMAP?
 after completion of the test with resolution mode

EDGE
, you will get the values for the edges of interest in a format that
also identifies their edge numbers. If, for example, all 4 edges have failed in a cycle, the
result will be returned as

```
01010101
```

<!-- 语法节 end -->

## 是什么

**文档事实** Error Map Tool 是用于错误评估的应用程序，是对 functional test 结果做低层检查的主要工具；它使用 Error Map 生成输出。

**文档事实** 本页是带子主题的主题页，子主题为：Error Map、Using the Error Map Tool、Elements of the Error Map Tool、Result Configuration、Hidden Error Map Upload、Print Error Map Data。

**文档事实** Error Map 是分析测试结果的基础，SmarTest 用它记录失败测试周期的信息。系统提供两种 error map：detailed error map 提供 cycle 甚至 edge 级信息；overview error map 按测试 setup 的周期数，每 2000 个或更多 cycle 合并为一个结果。

**文档事实** 两种 error map 都位于 test processor 内；detailed error map 也可放在外部 RDRAM，默认使用内部 error map。

**文档事实** 所有结果分析工具（Error Map Tool、Timing Diagram 等）都用 error map 生成不同的结果视图。

**文档事实** 在 93000 菜单中，Error Map Tool 与 Timing Diagram Tool、Result Configuration 并列为结果工具；按功能分组时，它与 Integrated Result Tool、Pin Margin Tool、Shmoo Tool、Timing Diagram Tool、Pattern Debug Tool、Testflow Debug Tool 同组。

## 典型用法

**文档事实** 启动：菜单 `93000 > Results > Error Map`，工具随即打开。

**文档事实** 选择 result mode：`Result > Acquisition Mode`，可选 Force Cycle Oriented、Force Failure Oriented、Follow Current Mode；该模式决定 detailed error map 中结果的获取方式。

**文档事实** 选择 result granularity 与 detailed Error Map 的位置：`Result > Result Configuration`。

**文档事实** 执行测试：`Result > Execute`。

**文档事实** 在 Overview tab 查看哪些 cycle block 含错误；按所用配置切到 Cycles tab 或 Edges tab 分析错误。

**文档事实** 若并非所有错误都落在 detailed error map 的范围内，在 overview tab 选择更靠后的 cycle block，重复执行与分析步骤，直到覆盖所需范围。

**文档事实** 与 Timing Diagram 联合分析时，可对齐 Timing Diagram 与 Error Map tool（子主题 Aligning Timing Diagram and Error Map tool）。

**文档事实** 存储受限场景（Smart Scale）的 setup：`DCRT RAM,(@)`、`DCEL DCRT,TP,SET,(P2,P4,P6,P8)`、`DCRM EMAP,4,PF,"c1:2 c2:4 c3:6 c4:8",(@)`；测试后用 `EMAP?` 读取 EDGE 分辨率下关心的边沿值，结果会标出边沿号（例如 4 个边沿全失败返回 `01010101`）。

**建议** 先用 overview 定位含错误的 cycle block，再对目标 block 切 Cycles/Edges 细看，可避免一次性拉取全部详细数据。

## 和谁有关

- **文档事实** [[error-map]] —— 工具的输出来源；该子主题定义 detailed 与 overview 两种 error map，并说明所有结果分析工具都基于它。
- **文档事实** [[timing-diagram-tool]] —— 两个工具可对齐分析（Aligning Timing Diagram and Error Map tool 子主题）；Timing Diagram 的聚焦流程也要求先按 `93000 > Results > Error Map` 启动 Error Map Tool。
- **文档事实** [[result-configuration]] —— 工具通过 `Result > Result Configuration` 设定 result granularity 与 detailed error map 位置；本身也是本页子主题。
- **文档事实** Result commands（`02.06.11.01.02.01` 子树）—— 存储受限示例用的 `DCRT`、`DCEL`、`DCRM EMAP`、`EMAP?` 属于结果命令；`EMAP?` 返回的是工具所依赖的 error map 数据。
- **文档事实** Hidden Error Map Upload、Print Error Map Data —— 本页另两个操作子主题，分别覆盖隐藏 error map 上传与打印 error map 数据。
- **文档事实** [[integrated-result-tool]]、[[shmoo-tool]]、Pin Margin Tool、Pattern Debug Tool、Testflow Debug Tool —— `02.08.03` 按功能分组时与 Error Map Tool 同组。
- **文档事实** 93000 menu and its tools（`02.08.02`）—— 把 Timing Diagram Tool、Error Map Tool、Result Configuration 同列为结果工具。
- **文档事实** Testflow Tool / Timing Diagram Tool —— 入门任务第 5 步用这三者检查 pass/fail 并调试数字操作。
- **文档事实** Pin Scale 9G —— Error Map 页记载 SmarTest 7.0.1 下用该类 pin 产生 prbs 或比较 prbs 的测试 error map 不工作。
- **推断** 由于 Error Map Tool 依赖 error map 输出，上述测试下该工具没有可分析的数据源。

## 版本

**文档事实** 本页 Functional changes 仅记「Introduced before SmarTest 6.3.2」，未列该工具自身的后续变更。

**文档事实** 其子主题 Error Map 的 Functional changes 记：SmarTest 7.0.1，对用 Pin Scale 9G pin 产生 prbs 或将 DUT 数据与 prbs 比较的测试，error map 不工作。

**推断** 由于 Error Map Tool 的输出由 error map 生成，上述限制意味着这类测试下该工具没有可分析的 error map 数据。

## 出处

- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.08_Error_Map_Tool.htm` —— 主源：Subtopics、概述、Functional changes。
- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.08.01_Error_Map.htm` —— 读了 error map 定义、detailed/overview、存放位置与 Functional changes。
- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.08.02_Using_the_Error_Map_Tool.htm` —— 读了 Procedure（启动、Acquisition Mode、Result Configuration、Execute、Overview/Cycles/Edges）。
- 其余跨页条目（Timing Diagram Tool、工具分组、93000 菜单、入门任务、Pin Scale 9G）取自各页引用语境句，未整篇通读。
