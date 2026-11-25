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

（待补）

## 典型用法

（待补）

## 和谁有关

（待补）

## 版本

（待补）

## 出处

（待补）
