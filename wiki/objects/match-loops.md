---
type: object
title: Match loops
layer: L1
stage: testmethod
tags: []
related: []
sources:
  - 02_System_reference/02.06_Command_Reference/02.06.07.01.08.04.03_Match_loops.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Match loops

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **4,942 字符逐字取自** `<02_System_reference/02.06_Command_Reference/02.06.07.01.08.04.03_Match_loops.htm>` 及其子主题 `<02_System_reference/02.06_Command_Reference/02.06.07.01.08.04.03.01.01_Adjusting_the_junctions_between_match_loop_and_surrounding_label.htm>`、`<02_System_reference/02.06_Command_Reference/02.06.07.01.08.04.03.01_Counted_match_loops.htm>`、`<02_System_reference/02.06_Command_Reference/02.06.07.01.08.04.03.02_Timed_match_loop.htm>`、`<02_System_reference/02.06_Command_Reference/02.06.07.01.08.04.03.03.01_How_to_use_Fast_Sync.htm>`、`<02_System_reference/02.06_Command_Reference/02.06.07.01.08.05.02_SVEC_subroutines.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Counted match loops）

The following is a simple example of a counted match loop:

```
SQPG 3,MACT,256,CONTINUE,,(@)
SQPG 4,GENV,5,,,(@)
SQPG 5,MRPT,5,,,(@)
```

Note that only the
GENV
 or
RPTV
 instruction is
allowed immediately before the
MACT
 instruction.
CONTINUE
,
which is optional, tells SmarTest to continue the surrounding test even if the match loop
failed.

### Example（取自子主题 Adjusting the junctions between match loop and surrounding label）

An example for junction adjustment is shown in the following diagram:

In this example, the match loop begins at the 6th cycle of an 8-cycle block.
Therefore, inserting 5 buffer vectors would be sufficient at the match loop start. But since
calculating the exact position of the first and last match loop cycle within the 8-cycle blocks
can be tiresome if your sequencer program contains loops or subroutine calls, you should always
insert 7 buffer vectors (or possibly more if this is required for other reasons). Therefore, two
more buffer cycles are present at the end of the preceding 8-cycle block in the
diagram.

### Example（取自子主题 Timed match loop）

The following listing illustrates a timed match
loop:

```
SQPG 11,WTER,,,,(@)
SQPG 12,MBGN,,,,(@)
SQPG 13,GENV,2,,,(@)
SQPG 14,WTER,,,,(@)
SQPG 15,MJPE,,,,(@)
SQPG 16,MEND,,,,(@)
```

### Examples（取自子主题 How to use Fast Sync）

### Example 1: Multiport timing

### Example 2: Define the max number of match ports on a test processor

```
class SetNife: public testmethod::TestMethod
{
public:
Boolean firstRun;

protected:
int mErrorProb;

virtual void initialize()
{
addParameter("errorProb", "int", &mErrorProb, testmethod::TM_PARAMETER_INPUT)
.setDefault("0");

firstRun = true;
}

virtual void run()
{
if (firstRun)
{
ON_FIRST_INVOCATION_BEGIN();

DISCONNECT();

if ( mErrorProb < 1 || mErrorProb > 8 )
{
cout << "NIFE not set!!!" << endl;
}
else
{
char buf[1000];

sprintf (buf, "SQST OFF\nNIFE %i\n", mErrorProb);

FW_TASK(buf);
}

ON_FIRST_INVOCATION_END();

firstRun = false;
}

return;

} // virtual void run()
...
...
};
REGISTER_TESTMETHOD(...);
```

### Example 3: Use the Fast Sync feature for blocking functional test

```
class BlockingFuncTest: public testmethod::TestMethod
{
protected:

int mFast;

virtual void initialize()
{
addParameter("fast", "int", &mFast, testmethod::TM_PARAMETER_INPUT)
.setDefault("1");
}

virtual void run()
{
static STRING tsName;
static STRING lblName;

ON_FIRST_INVOCATION_BEGIN();

GET_TESTSUITE_NAME(tsName);

lblName = Primary.getLabel();

CONNECT();

mFast?FW_TASK("STME FAST,\n"):FW_TASK("STME ON,\n");

FUNCTIONAL_TEST();

FW_TASK("STME OFF,\n");

ON_FIRST_INVOCATION_END();

Boolean res = GET_FUNCTIONAL_RESULT();

TEST(tsName, lblName, res?TM::Pass:TM::Fail,true);

return;

} // virtual void run()
...
...
};
REGISTER_TESTMETHOD(...);
```

### Example 4: Use the Fast Sync feature for non-blocking functional test

```
class NonBlockingFuncTest: public testmethod::TestMethod
{
protected:

int mFast;

virtual void initialize()
{
addParameter("fast", "int", &mFast, testmethod::TM_PARAMETER_INPUT)
.setDefault("1");
}

virtual void run()
{
static STRING tsName;
static STRING lblName;

ON_FIRST_INVOCATION_BEGIN();

GET_TESTSUITE_NAME(tsName);

lblName = Primary.getLabel();

CONNECT();

mFast?FW_TASK("STME FAST,\n"):FW_TASK("STME ON,\n");

START_TEST();

WAIT_TEST_DONE(TM::WAIT_DIGITAL);

FW_TASK("STME OFF,\n");

ON_FIRST_INVOCATION_END();

Boolean res = GET_FUNCTIONAL_RESULT();

TEST(tsName, lblName, res?TM::Pass:TM::Fail,true);

return;

} // virtual void run()
...
...
};
REGISTER_TESTMETHOD(...);
```

### Example 5: Use the Fast Sync feature for Independent Sequencer Run on the Smart Scale cards

```
class IndependentSequencerRuns: public testmethod::TestMethod
{
protected:

int mFast;

virtual void initialize()
{
addParameter("fast", "int", &mFast, testmethod::TM_PARAMETER_INPUT)
.setDefault("1");
}

virtual void run()
{
static STRING tsName;
static STRING lblName;

ON_FIRST_INVOCATION_BEGIN();

GET_TESTSUITE_NAME(tsName);

lblName = Primary.getLabel();

CONNECT();

SEQUENCER_CONTEXT_ITEM s1("matchCt");
SEQUENCER_CONTEXT_ITEM s2("otherCt");

s1.setPorts("match");
s2.setPorts("other");

SEQUENCER_CONTEXT seqCon;

seqCon.add(s1).add(s2).apply();

mFast?FW_TASK("STME FAST,\n"):FW_TASK("STME ON,\n");

START_TEST("matchCt");
FUNCTIONAL_TEST("otherCt");
WAIT_TEST_DONE(TM::WAIT_DIGITAL,"matchCt");

FW_TASK("STME OFF,\n");

ON_FIRST_INVOCATION_END();

Boolean res = GET_FUNCTIONAL_RESULT("match");

TEST(tsName, lblName, res?TM::Pass:TM::Fail,true);

return;

} // virtual void run()
...
...
};
REGISTER_TESTMETHOD(...);
```

### Example（取自子主题 SVEC subroutines）

The following listing shows a
SVEC
 subroutine that is called from
two
MAIN

labels:

```
SQPG 0,STVA,408,,,(@)
SQPG 1,STSA,,,,(@)
SQPG 2,GENV,6,,,(@)
SQPG 3,JSUB,,"sub",,(@)
SQPG 4,STOP,,,,(@)
SQPG 5,STVA,416,,,(@)
SQPG 6,STSA,,,,(@)
SQPG 7,GENV,4,,,(@)
SQPG 8,JSUB,,"sub",,(@)
SQPG 9,STOP,,,,(@)
SQPG 10,STVA,424,,,(@)
SQPG 11,GENV,400,,,(@)
SQPG 12,RSUB,,,,(@)
```

The
definitions of the three labels are as
follows:

```
SQLB "test1",MAIN,0,4,"table1"
SQLB "test2",MAIN,5,9,"table1"
SQLB "sub",SVEC,10,12,"table1"
```

<!-- 语法节 end -->

## 是什么

**文档事实**：Match loop 用于把没有 reset pin 的 DUT 置入某项测试所需的状态。一般原理是：指定一串在循环中执行的 vector，重复足够多次后 DUT 会依次进入它的各种可能状态；每次重复后检查是否达到目标状态，达到则终止循环，否则继续重复。

**文档事实**：评估 compare 结果并把它传播到控制循环重复的 error flag 需要一定时间；为提供这段时间，在 functional vectors 之后、match loop 结束之前必须产生若干不带 compare action 的 dummy vectors。

**文档事实**：该 error flag 也用于 conditional subroutine calls，文档指向 SVEC subroutines。

**文档事实**：另有一个机制在超过一定时间（timed match loop）或一定重复次数（counted match loop）后仍未达到目标状态时终止循环；此时默认整个测试 fail，counted match loop 可以改变这一行为。

**文档事实**：match loop cycles 的结果不记录到 error map；它们只影响测试的总体结果，即无法建立 match 时测试 fail。

**文档事实**：SmarTest 提供两种风格的 match loop，区别在于 dummy vector 的生成方式和终止机制。旧式仅为兼容保留，新应用应使用新式 Counted match loops。

**文档事实**：multi-site 测试中的 match loop 需要特别处理，文档指向 Controlling the site match function。

## 典型用法

**文档事实**：Counted match loop 用 MACT 启动，MACT 指定主循环允许的最大失败重复次数；文档给出示例：

```
SQPG 3,MACT,256,CONTINUE,,(@)
SQPG 4,GENV,5,,,(@)
SQPG 5,MRPT,5,,,(@)
```

**文档事实**：MACT 前只允许 GENV 或 RPTV 指令；可选 CONTINUE 表示即使 match loop 失败也继续周围测试。compare vectors 之后用 MRPT 定义 wait loop 中重复的 dummy vectors 数。

**文档事实**：counted match loop 至少要指定一个 dummy vector；系统会按需重复该 dummy vector 以取得设置 error flag 所需的时间，因此不必精确匹配该时间，通常一个就够。实际重复数取决于 dummy vector 数、pattern cycle time、pin 配置等参数；所需 dummy vector 总数通常在数百到 1000 以上。

**文档事实**：counted match loop 有两条辅助查询：CHFA? 返回最后一次 match loop cycle 在所选 pin 上的结果；MCNT? 返回满足 match 条件所需的 match loop 次数。

**文档事实**：Timed match loop 用 WTER（WaiT on ERror）和 MBGN（Match BeGiN）启动，vector 连续循环执行直到 DUT 输出与 expected data 匹配，再由 WTER、MJPE（Match JumP on Error）和 MEND（Match END）完成；文档给出示例：

```
SQPG 11,WTER,,,,(@)
SQPG 12,MBGN,,,,(@)
SQPG 13,GENV,2,,,(@)
SQPG 14,WTER,,,,(@)
SQPG 15,MJPE,,,,(@)
SQPG 16,MEND,,,,(@)
```

**文档事实**：timed match loop 期间 break vectors 自动生成；error map 不记录 match loop 期间的数据。若 DUT 输出不匹配，可用 SQST 的 BRK 参数中断序列，这时最后一个 loop 会被记录到 error map。

**文档事实**：timed match loop 若在默认 900 秒内未找到 match，会调用 SmarTest Work Center 并让 sequencer 进入 break state；可用 SQTO 设置该超时。multi-site 下 SmarTest 无法确定是哪个 site 超时，会声明所有 site fail。

**文档事实**：文档建议在 match loop 与周围 label 的 junction 处总是插入 7 个 buffer vectors（必要时更多），因为当 sequencer program 含循环或 subroutine 调用时，精确计算首、末 match loop cycle 落在 8-cycle block 中的位置很麻烦。

**文档事实**：Fast Sync（SmarTest 7.4.0）支持每个 test processor 最多 8 个 local synchronization，可并行应用于所有 test processor，从而消除 match loop 与 conditional jumps 因 site scaling synchronization 产生的开销；它支持所有 Smart Scale cards，并面向最多 1024 sites 的 massive multisite。属于 match loop 的 DUT pin 必须位于同一 test processor。

## 和谁有关

**文档事实**：以下关系均有本页正文、子主题或回链证据支撑。

- [[stme]]：STME 文档说明，multi-site 测试中按 site 评估 match loop 时 ON 选项是必需的；否则所有 site 同时启动时，match 判定会基于所有 site 的 compare 结果（回链证据）。
- [[sqst]]：timed match loop 文档说明可用 SQST 的 BRK 参数中断序列，此时最后一个 loop 会记录到 error map；sequencer 状态也由 SQST 描述。
- [[error-map]]：本页与 Counted/Timed 子主题都说明 match loop cycles 不记录到 error map，或仅在 break 时记录最后一个 loop。
- SVEC subroutines（`02_System_reference/02.06_Command_Reference/02.06.07.01.08.05.02_SVEC_subroutines.htm`）：本页说明 match loop 的 error flag 也用于 conditional subroutine calls，并直接指向该页。
- Counted match loops、Timed match loop、Fast Sync（本页子主题）：它们分别说明两种 match loop 风格与 7.4.0 新功能的具体用法。
- Controlling the site match function（`02_System_reference/02.06_Command_Reference/02.06.03.01.10.04_Controlling_the_site_match_function.htm`）：本页说明 multi-site 中的 match loop 需特别处理并指向该页。
- `Loops`（`02_System_reference/02.06_Command_Reference/02.06.07.01.08.04_Loops.htm`）：回链证据把 Match loops 与 Endless loops、Counted loops 并列。
- `Sequencing groups and pattern structure`、`Inserting counted match loops`：回链证据分别说明多端口 setup 的限制与 counted match loop 的插入方法。

## 版本

**文档事实**：本页 Functional changes 记载：

- Introduced before SmarTest 6.3.2——哨兵值，表示文档集覆盖范围之前已有。
- SmarTest 7.4.0：新增 Fast Sync 功能。

**文档事实**：子主题还记载：Counted match loops 在 SmarTest 7.1.4 为 MACT 指令新增 CONTINUE 选项；Fast Sync 子主题记为 Introduced in SmarTest 7.4.0；Timed match loop 与 Counted match loops 的 Functional changes 仅有 Introduced before SmarTest 6.3.2。

## 出处

- 主源：`02_System_reference/02.06_Command_Reference/02.06.07.01.08.04.03_Match_loops.htm`（正文、Related information、Functional changes）。
- 子主题：`02_System_reference/02.06_Command_Reference/02.06.07.01.08.04.03.01_Counted_match_loops.htm`、`02_System_reference/02.06_Command_Reference/02.06.07.01.08.04.03.01.01_Adjusting_the_junctions_between_match_loop_and_surrounding_label.htm`、`02_System_reference/02.06_Command_Reference/02.06.07.01.08.04.03.02_Timed_match_loop.htm`、`02_System_reference/02.06_Command_Reference/02.06.07.01.08.04.03.03_Fast_Sync.htm`、`02_System_reference/02.06_Command_Reference/02.06.07.01.08.04.03.03.01_How_to_use_Fast_Sync.htm`、`02_System_reference/02.06_Command_Reference/02.06.07.01.08.05.02_SVEC_subroutines.htm`（「语法 / 参数」逐字来源及上述事实）。
- 回链证据：`02_System_reference/02.06_Command_Reference/02.06.07.01.08.04_Loops.htm`、`02_System_reference/02.06_Command_Reference/02.06.02.02.250_STME__STME__-__SiTe_Match_Enable.htm`、`02_System_reference/02.06_Command_Reference/02.06.11.01.01_Global_result_queries.htm`、`02_System_reference/02.06_Command_Reference/02.06.07.01.08.04.02_Counted_loops.htm`。
