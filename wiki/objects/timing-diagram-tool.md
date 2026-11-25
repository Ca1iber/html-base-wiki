---
type: object
title: Timing Diagram Tool
layer: gui
stage: pattern
tags: []
related: []
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.33_Timing_Diagram_Tool.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Timing Diagram Tool

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **367 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.33_Timing_Diagram_Tool.htm>` 及其子主题 `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.33.01.09_Aligning_drive_and_receive_data_in_high_resolution_and_scope_mode.htm>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.33.02.04_Displaying_not_clearly_identified_areas__dotted_line.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 Aligning drive and receive data in high resolution and scope mode）

The following example shows the effect of the re-alignment:

Note that this example is only intended to illustrate the shifting mechanism. It
does not reflect the use case described above.

### Example（取自子主题 Displaying not clearly identified areas (dotted line)）

The dotted lines starting at cycle 8143 for the pins a1 to a3 indicate that no emap
data is available for them.

For the pin a0 the data is available for the whole displayed
area.

<!-- 语法节 end -->

## 是什么

- **文档事实** — Timing Diagram 是结果分析工具，显示发送给 DUT 的实际波形以及 DUT 输出的响应；它可标出收到的数据与 Pattern Tool 窗口中期望数据不一致的波形位置。
- **文档事实** — 工具按 executed pattern 区分 used pins 与 unused pins 并聚焦 used pins；还会显示 format definition 中出现的前两个 unused drive pins，但它们不能被 format，只能显示 break waveform（若定义）的虚线；其余 unused drive pins 与全部 unused receive pins 不显示，SmarTest 会在 Report window 发出警告。
- **文档事实** — cycle oriented mode 下显示全部 drive data，但一次聚焦 8K cycles 的 received data，聚焦范围外显示 expected data；failure oriented mode 下一次聚焦完整测试的 received data（前提是错误 cycle 少于 8K）。
- **文档事实** — 提供 Standard Size（默认）、Double Size（high resolution）与 Scope Size（softscope）三种分辨率；Double Size 通过放大窗口一次查看更多 pin 波形，Scope Size 的 softscope 提供更高分辨率。

## 典型用法

- **文档事实** — 从 SmarTest 菜单 `93000 > Results > Timing Diagram` 打开。
- **文档事实** — 波形左侧的 `i`/`o` 标明信号方向（输入/输出），时序或 signal format 不一致的 pin group 用 `*` 标出；Cycles 可选 1、2、5、10、25、50、100。
- **文档事实** — `Display > Standard Size` / `Display > Double Size`（左栏 `Stand` / `HiRes`）切换分辨率；softscope 由 Scope Size 进入。
- **文档事实** — 若要调试 synchronized protocol test，必须在 test method code 中调用 `unlink()` 之前设置 breakpoint。
- **文档事实** — 可与 Error Map 工具对齐，用于联合定位错误；pins 的显示规则和 dotted line 等状态见 How data is displayed 子主题。

## 和谁有关

- [[pattern-tool]] — Timing Diagram 用 Pattern Tool 窗口中的 expected data 判定 received data 是否一致；文档也建议把 Pattern Editor 与其他结果分析工具一起使用。
- [[error-map-tool]] — 文档有 "Aligning Timing Diagram and Error Map tool" 子主题，二者可对齐查看。
- [[shmoo-tool]] — Related information 列出 Shmoo Tool。
- [[timing-setup-tool]] — Related information 列出 Timing Setup Tool。
- [[signal-analyzer]] — Related information 列出 Signal Analyzer。
- `Creating a new format`（`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.33.01.07_Creating_a_new_format.htm`）— Related information 与 unused drive pins 的 format 限制都指向该页。

## 版本

- **文档事实** — Functional changes 写 "Introduced before SmarTest 6.3.2"；按版本页约定，这是哨兵值，表示文档集覆盖范围开始之前就已存在，不是 6.3.2 的变更。
- **文档事实** — "SmarTest 7.1.4: Modified display of pins"。

## 出处

- 主文档 `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.33_Timing_Diagram_Tool.htm`（`show.py 02.08.04.33` / `objpack.py`）。
- 另读了 `02.08.04.33.01_Using_the_Timing_Diagram_Tool.htm` 与 `02.08.04.33.02_How_data_is_displayed_in_the_timing_diagram.htm`，用于用法与显示规则。
- 语法节的两个 Example 逐字取自 `.01.09_Aligning_drive_and_receive_data_in_high_resolution_and_scope_mode.htm` 与 `.02.04_Displaying_not_clearly_identified_areas__dotted_line.htm`。
