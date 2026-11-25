---
type: object
title: FLUSH
layer: L2
stage: run
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.69_FLUSH.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# FLUSH

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,711 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.69_FLUSH.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
void FLUSH();
void FLUSH(const TM::FLUSH_POST_ACTION action);
void FLUSH(bool force);
void FLUSH(TM::FLUSH_POST_ACTION action, bool force);
void FLUSH(TM::FLUSH_SECTION_TYPE flush_section);
void FLUSH(bool force, TM::FLUSH_SECTION_TYPE flush_section);
void FLUSH(TM::FLUSH_POST_ACTION action, bool force, TM::FLUSH_SECTION_TYPE flush_section);
```
[表] Parameters
行 1:
  action
  This parameter controls how the setup data will be downloaded
    to the hardware.
    
    You can leave it empty or use TM::APRM.
    
    When using the TM:APRM option, the command
    `APRM`（raw: `98485.htm`） with
    mode set to CNL will
    be issued following the normal FLUSH()
    actions.
行 2:
  force
  When to execute the firmware command `FLSH`（raw: `99061.htm`） and `WSDN`（raw: `99082.htm`）. It can
    be:
    
    true: always executes the firmware command `FLSH`（raw: `99061.htm`） and `WSDN`（raw: `99082.htm`） (default)
    
    false: only executes the firmware
    command `FLSH`（raw: `99061.htm`） and `WSDN`（raw: `99082.htm`） when necessary.
行 3:
  flush_section
  This parameter allows you to set which types of APIs to flush.
    You can use the
    following options:
    
    TM::FLUSH_PRIMARY`1)`（raw: `#fntarg_1`）,
    
    TM::FLUSH_UTIL`2)`（raw: `#fntarg_2`）,
    
    TM::FLUSH_ALL,
    
     or a combination hereof.

This API is defined in the header file

/opt/hp93000/soc/prod_com/include/MAPI/MapiFuncs.h.

### Example

### TM::FLUSH_PRIMARY / UTIL

```
Routing.util("UTI1").on();
Primary.getLevelSpec().change("S_VCC", 4.45);
FLUSH(TM::FLUSH_PRIMARY | TM::FLUSH_UTIL);
```

Alternatively:

```
TM::FLUSH_SECTION_TYPE flushType;
flushType = TM::FLUSH_UTIL | TM::FLUSH_PRIMARY;

Routing.util("UTI1").on();
Primary.getLevelSpec().change("S_VCC", 4.45);
FLUSH(flushType);
```

<!-- 语法节 end -->

## 是什么

**文档事实** FLUSH 是 test method API，把 ROUTING_STATUS 所指定的变更反映到 setup data 或 hardware；同时把 PRIMARY_STATUS、TIMING_SPEC / LEVEL_SPEC / SPECIFICATION 的变更反映到 MCD（firmware level），但不反映到 hardware。

**文档事实** 该 API 定义在 `/opt/hp93000/soc/prod_com/include/MAPI/MapiFuncs.h`。

**文档事实** 七个重载分别接受 `action`、`force`、`flush_section` 及其组合。`action` 可留空或取 `TM::APRM`；取 `TM::APRM` 时，会在正常 FLUSH 动作之后发出 mode 为 CNL 的 APRM 命令。`force` 控制何时执行固件命令 FLSH 与 WSDN：`true`（默认）总是执行，`false` 只在必要时执行。`flush_section` 可取 `TM::FLUSH_PRIMARY`、`TM::FLUSH_UTIL`、`TM::FLUSH_ALL` 或其组合。

**文档事实** 脚注给出刷新范围：`FLUSH(TM::FLUSH_PRIMARY)` 刷新 Primary Sets、Timing Spec、Specification Level、Spec Sequencer、Definition changes；`FLUSH(TM::FLUSH_UTIL)` 刷新 Utility Purpose control 与 Utility line control。

**文档事实** FLUSH 的操作已包含在 EXECUTE_TEST、START_TEST、DIGITAL_CAPTURE_TEST、NB_DIGITAL_CAPTURE_START 的行为中，所以多数情况下不需要调用；它主要用于调试 test method 程序。

**文档事实** 要让 FLUSH（或内部执行 FLUSH 的 API）把 ROUTING_STATUS 对 utility line 的变更反映出来，sequencer 必须 halted。对 `Routing.primary()`、`Routing.pin()`、`Routing.util()`、`Routing.uti_purpose()`，执行 FLUSH 时所有 analog module（AWG/DGT/Sampler）必须 halted。ROUTING_STATUS 的 `trigger()`、`abort()`、`getXXXX()`、`isRunning()` 不需要 FLUSH。

**文档事实** 用 LEVEL_SPEC / TIMING_SPEC（多端口用 SPECIFICATION）改 spec 值时，变更在调用 FLUSH 时反映到 desired spec data；实际反映到 hardware 则要等 EXECUTE_TEST、START_TEST、DIGITAL_CAPTURE_TEST、NB_DIGITAL_CAPTURE_START、FUNCTIONAL_TEST，或 FLUSH then SPEC_SEARCH (execute())、SEQUENCER_STATUS (run())、PMU_IFVM (execute())、PMU_VFIM (execute())、TASK_LIST (execute())、DPS_VFIM (execute())。

**文档事实** 使用 `FLUSH(TM::APRM)` 时，若应用修改同一个 spec 变量，必须在每次 change 命令后调用；若修改不同 spec 变量，只需在最后一行调用一次。

**文档事实** FLUSH 必须在被 flush 的元素离开作用域之前调用。例如元素声明在 `if{}` 块内时，FLUSH 也必须在同一块内；放在块外会导致 FLUSH error。

**文档事实** 若通过 FTCG 设置 keep alive ports 并执行 `FLUSH(TM::APRM)`（命令 FLSH），更新 clock 时会发出消息：至少一个端口无法保持不变，Flush 强制 clock off，导致所有 channel 停止。

**推断** 因此 FLUSH 是「把已缓冲的 setup 变更提交并同步到 MCD/硬件」的同步点，而不是一次测试执行；它既可作为调试时的显式提交，也作为执行类 API 的内部前置步骤。

## 典型用法

**文档事实** 最小示例：`Routing.util("UTI1").on(); Primary.getLevelSpec().change("S_VCC", 4.45); FLUSH(TM::FLUSH_PRIMARY | TM::FLUSH_UTIL);`。也可先把组合存入 `TM::FLUSH_SECTION_TYPE flushType = TM::FLUSH_UTIL | TM::FLUSH_PRIMARY;`，再 `FLUSH(flushType)`。

**文档事实** 调试时若用 Spec Tool 改了 spec 值，并希望在下一个执行 API 之前生效，就调用 FLUSH；文档明确这一用途是调试 test method 程序。

**文档事实** 改同一 spec 变量时，每次 change 后调 `FLUSH(TM::APRM)`；改不同变量时可在最后调用一次。

**文档事实** 若被 flush 的元素在 `if{}` 内声明，FLUSH 必须写在同一块内。

**文档事实** 要让 utility line 的路由变更经 FLUSH 生效，先停住 sequencer，并确认相关 analog module 已 halted。

**文档事实** Performance Cookbook 的 Generic Test Program Setup 建议尽量避免不必要的 `ABORT_TEST()` 或 `FLUSH()` API。

**建议** 正常测试流程不要手工插 FLUSH，交给 EXECUTE_TEST / START_TEST 等执行 API；只在调试 test method、或需要在执行前立即确认 spec / utility 变更时显式调用。

**建议** 使用 `FLUSH(TM::APRM)` 前确认没有通过 FTCG 设置 keep alive ports，否则会强制 clock off 并停掉所有 channel。

## 和谁有关

- **文档事实** ROUTING_STATUS：FLUSH 把其变更反映到 setup data 或 hardware；其 utility line 变更需要 sequencer halted，Routing.primary/pin/util/uti_purpose 需要 analog module halted；trigger/abort/getXXXX/isRunning 不需要 FLUSH。
- **文档事实** PRIMARY_STATUS：FLUSH 把其变更反映到 MCD（不反映到 hardware）；PRIMARY_STATUS 页说明该反映是让 Test Program Explorer、Spec Tool 等 UI 看到变更的选项。
- **文档事实** TIMING_SPEC、LEVEL_SPEC、SPECIFICATION：其 spec 值变更在 FLUSH 时反映到 desired spec data；TIMING_SPEC 页还说明 FLUSH 后的变更会用于后续 testsuite，要恢复原值需 `restore()` 加 FLUSH。
- **文档事实** APRM：`FLUSH(TM::APRM)` 在正常 FLUSH 后发出 mode 为 CNL 的 APRM 命令。
- **文档事实** FLSH 与 WSDN：`force` 参数决定何时执行这两个固件命令；FTCG 页把 `FLUSH(TM::APRM)` 注明为命令 FLSH。
- **文档事实** FTCG：keep alive ports 与 `FLUSH(TM::APRM)` 的 clock off 消息，文档链接到 Suppressing Reactivation of Primary Sets with FTCG。
- **文档事实** SQST 与 CONNECT：激活 master clock 的信息见这两页。
- **文档事实** EXECUTE_TEST、START_TEST、DIGITAL_CAPTURE_TEST、NB_DIGITAL_CAPTURE_START、FUNCTIONAL_TEST：FLUSH 的操作包含在前四个 API 中；这些页说明在启动测试时会内部执行 FLUSH，以反映 setup 变更。
- **文档事实** SPEC_SEARCH、SEQUENCER_STATUS、PMU_IFVM、PMU_VFIM、TASK_LIST、DPS_VFIM：文档以 "FLUSH then <API> (execute()/run())" 的形式说明它们与 FLUSH 的配合顺序。
- **文档事实** SEQUENCER_CONTEXT 与 GET_FUNCTIONAL_RESULT：SEQUENCER_CONTEXT 变更会使 GET_FUNCTIONAL_RESULT 的结果失效，需用 Primary.label() 后接 FLUSH() 恢复起始 label 再读取。
- **文档事实** SMC_EXECUTE_TEST、SMC_DIGITAL_CAPTURE_TEST、SMC_FUNCTIONAL_TEST：前两者内部执行 FLUSH()，SMC_FUNCTIONAL_TEST 页说明如需激活设置要先执行 FLUSH API。
- **文档事实** PMU_TASK.preAction：该页要求在用 PRIMARY_STATUS 指定的 primary 设置前执行 FLUSH()。
- **文档事实** FLEX_RELAY：该页说明可用 task 激活 utility line 设置，而不使用 FLUSH API。
- **文档事实** Working with FLUSH()：本页 Related information 列出的性能与用法说明页。

## 版本

**文档事实** Functional changes 记：Introduced before SmarTest 6.3.2；SmarTest 7.1.3 支持 MBAV8+；SmarTest 7.1.4 起 master clock 关闭时不能访问 analog module 硬件，会发出错误并在 report window 显示消息；SmarTest 7.6.1 新增 `flush_section` 参数。

## 出处

- `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.69_FLUSH.htm`，主源，含 Introduction、Application note、Syntax、Example、Related information 与 Functional changes，已用 `show.py` 读取。
- 相关页（ROUTING_STATUS、PRIMARY_STATUS、TIMING_SPEC、APRM、FLSH、WSDN、FTCG、SQST、CONNECT、各执行 API 等）的引文取自 `extract/objpack.py` 的入边索引。
