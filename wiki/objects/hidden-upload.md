---
type: object
title: Hidden upload
layer: L2
stage: testmethod
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.10.04.05_Hidden_upload.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Hidden upload

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

**没有加标记的语法段。** 定义文档里没有 `Syntax` / `Parameters` / `Example`
这类**段标记**。本脚本一个字都不收录——没有段标记时「哪一段是语法」是猜，
而猜就是编。要看原文：`python show.py <分类号>`。

<!-- 语法节 end -->

## 是什么

**文档事实** Hidden upload 是 SmartCalc 的一种数据上传机制，SmartCalc 自动决定要上传到 test system controller 的数据包大小，并在当前正在运行的测试即 sequencer execution 背后执行优化的上传。

**文档事实** 上传由 SmartCalc API 完成，这些 API 知道 sequencer execution 的开始与结束时间，因此可以在当前运行测试期间上传数据；这种把上传隐藏在下一个测试的 sequencer execution 背后的技术称为 hidden upload。

**文档事实** 要使用该机制，上传任务必须放在 test method 的 SmartCalc 即 SMC section 中；SMC 会在不影响主 test flow 吞吐量时自动管理上传。

**文档事实** 数据包大小取决于下一个测试的预计 sequencer 运行时间，计算目标是使用 100% 的 sequencer 运行时间，因此 SMC 能自动合并较小的包或拆分较大的包。

**文档事实** 执行 test flow 时，SmartCalc 会自动测量并缓存每次测试执行的 sequencer execution 时间；缓存值会针对同一 sequencer run 的下一次执行进行动态补偿。最佳上传包大小取决于预测的 sequencer execution 时间。上传完成后，系统恢复默认 packet 大小，或恢复用户指定的包大小。

## 典型用法

**文档事实** 将数据上传任务放入 test method 的 SMC section，由 SMC 自动安排上传。

**文档事实** 当自动算法无法足够精确地计算执行时间时，例如使用 Match Loops，可用 SMC_SET_TEST_EXECUTION_TIME() 覆盖 SMC 预测的 sequencer execution 时间，把下一个测试的 sequencer execution 时间设为用户定义值，并控制当预测执行时间已过但 sequencer 仍在运行时是否继续上传。

**文档事实** 由 SMC_ARM() 控制并启动的 hidden upload 必须在 Mode context 改变之前完成。

**文档事实** 在同一个 test suite 内改变 Mode context 时，建议在改变之前调用 SMC_SYNCHRONIZE_WITHOUT_BINNING()。

**文档事实** 跨多个 test suite 改变 Mode context 时，建议插入一个不定义 level、timing 或 pattern 信息的新 test suite，并为其分配系统准备的 test method smartCalc.SMC__SYNCHRONIZE。

**文档事实** 文档提示在 MBAV8+ 上使用 hidden upload 时，FPGA 兼容性需参考 service note E8001-140611A。

## 和谁有关

- **文档事实** SmartCalc 即 SMC，hidden upload 的上传任务必须位于 test method 的 SMC section，由 SMC 自动管理。
- **文档事实** SMC_ARM()，文档说明由它控制并启动 hidden upload，且这类上传必须在 Mode context 改变前完成。
- **文档事实** SMC_SET_TEST_EXECUTION_TIME()，用于覆盖 SMC 预测的 sequencer execution 时间，并可控制预测时间过后是否继续上传。
- **文档事实** SMC_SYNCHRONIZE_WITHOUT_BINNING()，在同一个 test suite 内改变 Mode context 前建议调用。
- **文档事实** smartCalc.SMC__SYNCHRONIZE，跨多个 test suite 改变 Mode context 时建议插入的新 test suite 使用该系统准备的 test method。
- **文档事实** Mode context，hidden upload 必须在其改变前完成，文档并针对 suite 内与跨 suite 两种改变给出建议。
- **文档事实** Match Loops，文档将其列为自动算法难以精确计算执行时间的例子，此时可用 SMC_SET_TEST_EXECUTION_TIME()。
- **文档事实** MBAV8+，文档提示与其配合使用 hidden upload 时需参考 service note E8001-140611A 的 FPGA 兼容性说明。

## 版本

**文档事实** Functional changes 记载 Introduced in SmarTest 6.5.3。

**文档事实** SmarTest 7.2.0 起 SMC 的默认行为改为自动确定优化的包大小。

**文档事实** SmarTest 7.2.1 起需要确保 FPGA 兼容性。

## 出处

- `02_System_reference/02.07_Test_Method_Reference/02.07.10.04.05_Hidden_upload.htm`
