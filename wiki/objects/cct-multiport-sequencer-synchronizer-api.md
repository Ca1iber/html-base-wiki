---
type: object
title: CCT Multiport Sequencer Synchronizer API
layer: L2
stage: pattern
tags: []
related: []
sources:
  - 03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.05.09_CCT_Multiport_Sequencer_Synchronizer_API.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# CCT Multiport Sequencer Synchronizer API

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,538 字符逐字取自** `<03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.05.09_CCT_Multiport_Sequencer_Synchronizer_API.htm>` 及其子主题 `<03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.05.09.01_Using_the_CCT_Multi-Port_Sequencer_Synchronizer_API.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Using the CCT Multi-Port Sequencer Synchronizer API）

Example code for checking the transaction port against the
multi-port
burst:

```
CCTMultiportSync Sync;
Sync.registerSyncPort(Lshift::getInstance(tsName));
Lshift::getINstance(tsName).write(0x18, 0x22);
Lshift::getINstance(tsName).write(0x18, 0x86);
Lshift::getINstance(tsName).read(0x18, "readID1");
Lshift::getINstance(tsName).readExpect(0x18, 0xFE);
Lshift::getINstance(tsName).getReadValue("readID1") //get the read value marked as "readID1"
```

### Example（取自子主题 Using the CCT Multi-Port Sequencer Synchronizer API）

Code example for adding a sequencer‑controlled DC to an assigned
port:

```
CCTMultiportSync Sync;
DCDynamicPort::getInstance().setPort("pPPMUDC");
Sync.registerSyncPort(DCDynamicPort::getInstance());
DCDynamicPort::getInstance().PPMU_Relay("DC_Pin1", "PPMU_ON", 20 ns);
DCDynamicPort::getInstance().PPMU_Setting_VForce("DC_Pin1", vin V, 10 mA, -12 uA, 12 mA, 10 ns);
DCDynamicPort::getInstance().PPMU_Relay(MeasPin, "PPMU_ON", 20 us);
DCDynamicPort::getInstance().PPMU_Setting_IForce(MeasPin, "CLAMP_ON", 0 uA, 100 uA, -1 uA, 1 uA, 0.002 ms);
DCDynamicPort::getInstance().PPMU_VClamp(MeasPin, "CLAMP_ON", 0, 4 V, 0.1 us);
DCDynamicPort::getInstance().PPMU_Meas(MeasPin, "VMUM", "PVAL", 2, 10 ns);
```

### Example（取自子主题 Using the CCT Multi-Port Sequencer Synchronizer API）

Code example for adding a dynamic DC test to an assigned
ports:

```
CCTMultiportSync Sync;
DCDynamicPort::getInstance().setPort("pDPS128");
Sync.registerSyncPort(DCDynamicPort::getInstance());
DCDynamicPort::getInstance().DPS_MeasVoltageRange(mDpsPins, 3.0);
DCDynamicPort::getInstance().DPS_Force("DPS128_2"), vin, 50 mA);
DCDynamicPort::getInstance().DPS_MeasVoltage(mDpsPins, 2);
```

<!-- 语法节 end -->

## 是什么

**文档事实**：CCT Multi-port Sequencer Synchronizer API 是一组 API，用于编写 digital multi-port burst，并处理跨 port 的同步（`03.03.05.09`）。

**文档事实**：关键能力包括（`03.03.05.09`）：
- 在下一个 label 开始前，按各 port 的 vector/cycle 长度或执行时间自动保持同步；可同步不同 port 上的 flat pattern，以及 PA transaction sequence 与普通 pattern。
- 用预定义 protocol 对 DUT 执行 write/read/read from，可为不同 site 指定不同值。
- 在 pattern 中插入 sequencer-controlled DC 测试（需指定同步点）。
- 插入 DC Dynamic 测试，并与其他 port 的 pattern 保持同步。
- 按 analog sequencer group 或 analog sequence program 在指定 port 生成 trigger pattern 或 PA transaction 序列，并与其他 port 同步。
- 在 multiport burst 中插入 digital capture pattern，并自动生成其 VECTOR_VARIABLE。
- 提供 protocol 活动的统一 wrapper API（基于 PA）。
- 工程模式与生产模式之间平滑切换；可视化 multiport assembly。
- 在 multiport burst 的 port 上创建/插入 flat label，并在 HIF port 附加 protocol-type label。
- 支持多个 digital capture port 上的多次 digital capture（DigitalCapturePort）。

**文档事实**：普通 digital pattern 可用所有 smart scale digital cards；API 本身不需要专用 license，但要在 multiport burst 中附加 protocol-type label 时需要 protocol-aware license（`03.03.05.09`）。

**文档事实**：前置条件为 digital pattern 必须基于 multi-port、timing set 必须基于 multi-port、必须在 Concurrent Test Framework 环境中使用；限制为 pattern 中含 CTIM/CLEV 的 port 不支持、D2S 不支持、BADC 不支持（`03.03.05.09`）。

**文档事实**：同步动作由用户显式发起（"The synchronization activity is user-initiated"），不是自动全局生效（`03.03.05.09`）。

**推断**：它解决的是「多个 port 的 burst 长度/执行时间不一致，导致下一个 label 起跑不对齐」的问题；本页只复述文档，具体机台是否具备相关硬件需另行确认。

## 典型用法

**文档事实**：
- 需要同步的 port 必须先注册（`registerSyncPort`）；API 通过查询各 label 的 cycles 与 period 追踪已注册 port 上 label 的执行时间（`03.03.05.09`、`03.03.05.09.01`）。
- 先创建 flat pattern，再给 multiport burst 的某个 port 添加 flat label，或附加 protocol-type label；API 计算各 port 执行时间差，对执行时间较短的 port 追加重复 idle vector（普通 port）或 IDLE 命令（transaction port），使各 port 的 sequencer 同时结束，从而让下一个 vector 同时开始（`03.03.05.09`）。
- 用户可指定同步点时间 `Tsync`，API 对执行时间小于 `Tsync` 的已分配 port 追加 dummy cycles/IDLE（`03.03.05.09`）。
- 同步示例（`03.03.05.09.01`）：

```cpp
CCTMultiportSync Sync;
Sync.registerSyncPort(Lshift::getInstance(tsName));
Lshift::getInstance(tsName).write(0x18, 0x22);
Lshift::getInstance(tsName).read(0x18, "readID1");
Lshift::getInstance(tsName).getReadValue("readID1");
```

- 把 sequencer-controlled DC 接到已分配 port：先 `DCDynamicPort::getInstance().setPort("pPPMUDC")`，再 `Sync.registerSyncPort(DCDynamicPort::getInstance())`，然后调用 `PPMU_Relay`/`PPMU_Setting_VForce`/`PPMU_Setting_IForce`/`PPMU_VClamp`/`PPMU_Meas`（`03.03.05.09.01`）。
- 动态 DC 测试同理：`DCDynamicPort::getInstance().setPort("pDPS128")` 后调用 `DPS_MeasVoltageRange`/`DPS_Force`/`DPS_MeasVoltage`（`03.03.05.09.01`）。

**推断**：示例中的 `Lshift`、`DCDynamicPort` 是 port 侧对象，`CCTMultiportSync` 负责注册与同步；具体某类 port 是否可用还受前置条件/限制约束。

## 和谁有关

- **Concurrent Tests (CCT)** — 文档事实：本页位于 CCT 专题下，CCT 总览页链接到本页（`03.03.05`，入边）。
- **Using the CCT Multi-Port Sequencer Synchronizer API** — 文档事实：本页子主题，给出同步、sequencer-controlled DC 与 dynamic DC 的示例（`03.03.05.09.01`）。
- **CCT multi-port user interface APIs** — 文档事实：本页子主题，另一个相关 API 面（`03.03.05.09.02`）。
- **CCTMultiportSync** — 文档事实：同步对象，示例中用于 `registerSyncPort`；其 `start()`/`sync()`/`flush()` 有独立页面（`02.07.04.01.14.25` 及其子页）。
- **registerSyncPort** — 文档事实：把 port 注册到同步器（`02.07.04.01.180`，入边）。
- **`DCDynamicPort` / `PPMU_*` / `DPS_*`** — 文档事实：示例用 `DCDynamicPort::getInstance()` 接入 PPMU/DPS 的 sequencer-controlled DC 与 dynamic DC 测试；相关函数页反向引用本页（`02.07.04.01.23`、`02.07.04.01.155`–`.163`、`02.07.04.01.44`–`.48`，入边）。
- **DigitalCapturePort / PatternPort / Capture / playPattern / Trigger / AnalogSeqGroup** — 文档事实：这些 API 页面反向引用本页，对应 digital capture、pattern 与 analog trigger 能力（`02.07.04.01.32`–`.34`、`.143`、`.149`、`.259`、`.04`，入边）。
- **SynchronizedPort::setPort/setIdentifier、attachPA、dumpMPBGraph** — 文档事实：相关 API 页面反向引用本页（`02.07.04.01.237`、`.238`、`.06`、`.54`，入边）。

## 版本

文档事实（`03.03.05.09` 的 Functional changes）：
- Introduced in SmarTest 7.3.2

该页没有更细的版本变更记录。

## 出处

- `03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.05.09_CCT_Multiport_Sequencer_Synchronizer_API.htm`（主文档）
- `03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.05.09.01_Using_the_CCT_Multi-Port_Sequencer_Synchronizer_API.htm`
- `03_Use_cases_and_application_papers/03.03_How_to_use_Multiport_for_specific_Applications/03.03.05.09.02_CCT_multi-port_user_interface_APIs.htm`
- 相关入边页：`02.07.04.01.14.25_CCTMultiportSync.htm`、`02.07.04.01.180_registerSyncPort.htm`、`02.07.04.01.23_DCDynamicPort__getInstance.htm`（以及 `.155`–`.163`、`.44`–`.48`、`.32`–`.34` 等）
