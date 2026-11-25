---
type: object
title: Bins
layer: n/a
stage: testflow
tags: []
related: []
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.06_Bins.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Bins

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **260 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.06_Bins.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example

If for some reason your production run should stop unexpectedly, all devices that have
not ended up in either a good or bad bin will be assigned to the otherwise bin. This bin is also
included in yield calculations, as it can be defined as a good or a bad bin.

<!-- 语法节 end -->

## 是什么

**文档事实** Bin 是 testflow 中按测试结果对被测器件进行分选的机制。测试中通常需要按结果把器件归入不同的 bin；例如在某 test suite 中失败的器件会进入一个 bin，且不再继续测试。

**文档事实** testflow 中的一个 bin 恰好生成一个 hardware bin 和一个 software bin。

**文档事实** 文档列出三类 bin：

- stop bin：testflow 中用于收纳全部 good 或全部 bad 器件的 bin，插在 testflow 的特定位置，显示为三角形的绿色 good bin 或八边形的红色 bad bin；用 Flow Sequence Editor 插入时可定义为 good bin 或 bad bin，落入其中的器件数计入 yield。
- otherwise bin：收纳所有未落入 stop bin 的器件；该 bin 节点不在 testflow 中显示。
- floating bin：在 Flow Data Editor 的 Bins 页面定义，用作 multi-bin 的预定义 bin；它不在 Flow Sequence Editor 中显示，但随后插入的关联 multibin 会显示。

**文档事实** yield 计算包含落入 stop bin 与 otherwise bin 的器件数。

## 典型用法

**文档事实** 在 testflow 的适当位置插入 stop bin，并在插入时用 Flow Sequence Editor 将其定义为 good bin 或 bad bin。

**文档事实** 在 bin 相关窗口选中某个 bin 后点 Go To，该 bin 会在 Flow Sequence Editor 中高亮。

**文档事实** 在 Flow Data Editor 的 Bins 页面定义 floating bin，作为 multi-bin 的预定义 bin；关联的 multibin 需随后用 Flow Sequence Editor 插入。

**文档事实** 生产运行意外停止时，尚未落入 good 或 bad bin 的器件会被分配到 otherwise bin；该 bin 也计入 yield，且可定义为 good bin 或 bad bin。

**推断** otherwise bin 与 floating bin 都不作为普通节点在 Flow Sequence Editor 中直接显示，因此二者要借 stop bin 或 multibin 的插入配置才出现在 testflow 中，而不能单独放置。

## 和谁有关

- **文档事实** `[[flow-sequence-editor]]` — stop bin 在其插入并可定义为 good/bad bin；Go To 会在其中高亮选中 bin；floating bin 不在其中显示。
- **文档事实** `[[flow-data-editor]]` — floating bin 在其 Bins 页面定义。
- **文档事实** 一个 bin 恰好生成一个 hardware bin 和一个 software bin。
- **推断** `[[hardware-bin-summary-tab]]` 与 `[[software-bin-summary-tab]]` 分别汇总这两类 bin 的结果；本页未直接写明这一对应，仅由名称与汇总对象推断。
- **文档事实** Multibin SmartDisconnect test suite — 主文档把该组合节点场景链接到 Bins；多 site 下的用法见 Use of bins with multisite tests。
- **文档事实** `[[alphabetical-list-of-flags]]` — 该页说明部分 flag 会把尚未分选的 sites 送入 otherwise bin。
- **文档事实** Inserting a bin into the testflow（`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.01.05_Inserting_a_bin_into_the_testflow.htm`）— 本页 Related information 列出的插入操作页。

## 版本

**文档事实** Functional changes 记载 Introduced before SmarTest 6.3.2（哨兵值，表示文档集覆盖范围开始前已存在）。SmarTest 6.5.2 引入 floating bin。

## 出处

- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.06_Bins.htm`，主源，含 bin 定义、三类 bin 说明、otherwise bin 示例、Related information 与 Functional changes。
