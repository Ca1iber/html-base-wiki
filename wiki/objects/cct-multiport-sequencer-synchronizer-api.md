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

（待补）

## 典型用法

（待补）

## 和谁有关

（待补）

## 版本

（待补）

## 出处

（待补）
