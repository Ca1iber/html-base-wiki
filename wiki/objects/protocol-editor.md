---
type: object
title: Protocol editor
layer: gui
stage: pattern
tags: []
related: []
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.22_Protocol_editor.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Protocol editor

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,504 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.22_Protocol_editor.htm>` 及其子主题 `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.22.02_Transaction_details.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Parameters（取自子主题 Transaction details）

Transaction parameters can be used within test methods to
pass variables to a transaction. This way one can create dynamic transactions. Typical
parameters of read/write transactions are register address, physical address and register
data.

The order of the parameter definition has an impact to the corresponding transaction
and the resulting state character sequence.

The state character sequence representing a
decoded field will be mapped back to transaction parameters during parameter reconstruction in
order to be readable from test methods.

[表] Properties
列: Property | Description
行 1:
  Direction
  Defines the direction from a DUT perspective.
    
    IN - parameter values will be passed to the DUT
    
    OUT - the DUT is passing parameter values to the application
行 2:
  Length
  Defines the length of this parameter in bits/state characters.
行 3:
  Decode function
  For input parameters the decode functions describes which field is used to fill in
    the parameter value.
    
    For output parameters the decode function describes how the received bits/state character
    sequence (represented by the parameter value) is transferred back to fields.
行 4:
  Display mode
  Specifies the number format in which numerical parameter values are displayed in
    the TA column of the Pattern Debug Tool. Possible values are "BINARY", "DECIMAL",
    and "HEX". HEX is the default.
    
    The property is ignored if the parameter value is specified as a state character
    sequence.

<!-- 语法节 end -->

## 是什么

**文档事实** Protocol editor 是 SmarTest 的图形用户界面，用于设置和编辑 protocol 以及 protocol 相关的 levels、timing 和 wavetable。

**文档事实** 它默认打开 Protocol Definition 标签页。

**文档事实** 左侧 Overview area 显示当前在 test program explorer 中选中的 protocol 结构，结构符号分别表示 protocol、transactions、pin roles、fields、用于 parallel protocol 的 pin role groups，以及未定义的 protocol 元素；未定义元素的可能原因是 protocol details 与 pin role details 中的 pin role 名称不匹配。

**文档事实** 右侧 Details area 随 Overview area 中选中的元素显示不同内容，包括 Protocol details、Transaction details、Pin role details 和 Field details。

**文档事实** 底部标签页可在 Protocol Definition、Level、Wavetable、Timing 之间快速切换，因此无需离开 protocol editor 即可录入 protocol 专用 levels、timing 等信息。

**文档事实** 当 protocol 定义有错误时，Details area 会在鼠标悬停于高亮字段时给出进一步信息；也可使用 Problems View，双击 Protocol Marker 类型错误后光标会跳到对应编辑器中的错误处。

**文档事实** protocol editor 的 preference settings 控制各 section 以展开还是折叠方式显示。

## 典型用法

**文档事实** 文档的 Using the protocol editor 子主题把使用场景列为打开 protocol、设置 protocol definition、卸载 protocol、编辑 transaction details、编辑 pin role details、编辑 field details、编辑 protocol 专用 levels、编辑 protocol 专用 wavetable 与 state map、编辑 protocol 专用 timing、验证 protocol definition、生成 protocol wrappers。

**文档事实** Working with Protocols 子主题给出两类主要用法，一是创建全新的 protocol，二是复用已有的 protocol；其下分别有 Defining a new Protocol MDIO 与 Using a predefined protocol 页面。

**文档事实** Protocol details 页说明 pin role 是 pin 在 transaction 中使用的 protocol 专用名称，必须先在此定义，之后才能在 protocol assignments editor 中分配给物理 pin。

**文档事实** Build feature 页说明 protocol 从零定义或修改后应检查形式错误；build 会把 constants、variables、pin roles 和 pin role groups 应用到对应 protocol definition 的 transaction specification 上，从而在执行前检查 pin 资源与 protocol 的一致性。该 build feature 与 Project 菜单的 build action 不同，不受 Build Automatically 选项控制。

**文档事实** Protocol wrapper 页说明 SmarTest 还提供 protocol wrapper wizard，可从 protocol definition 生成 C++ 类；生成的 wrapper 源码可供 test method 编程使用，避免直接使用通用 API 带来的繁琐。

**文档事实** Wavetable 标签页要求 protocol definition 使用 STATEMAP；每个 protocol timing setup 必须恰好包含一个 wavetable definition，为 protocol 的所有 pin roles 定义 waveform，且所有 state map entry 必须使用相同 x-mode。

## 和谁有关

- **文档事实** test program explorer，Overview area 显示的正是其中当前选中的 protocol 结构。
- **文档事实** Protocol details、Transaction details、Pin role details、Field details，它们是 Details area 针对不同选中元素显示的四个子主题，也列在本页 Subtopics 中。
- **文档事实** Level tab、Wavetable tab、Timing tab，它们是底部三个 protocol 专用编辑标签页子主题。
- **文档事实** Pin role 与 Transaction，二者列在本页 Related information。
- **文档事实** Protocol Editor preference page，列在本页 Related information，并控制 Details area 各 section 的展开或折叠。
- **文档事实** Problems View，作为 Details area 之外的错误查看方式，双击 Protocol Marker 错误可跳转到对应编辑器的错误处。
- **文档事实** Protocol wrapper 与 2nd level protocol wrapper tool，前者说明从 protocol definition 生成 C++ 类，后者是其子主题工具。
- **文档事实** Build feature of the protocol editor and test program explorer，用于在执行前检查 protocol definition 的一致性。
- **文档事实** protocol assignments editor，Protocol details 子主题说明 pin role 必须先定义，之后才能在该编辑器中分配给物理 pin。
- **文档事实** Using the protocol editor 与 Working with Protocols，前者列出 protocol editor 的典型使用场景，后者给出新建与复用 protocol 两类用法。

## 版本

**文档事实** Functional changes 记载 Introduced in SmarTest 7.1.0，SmarTest 7.1.3 增强错误处理与呈现。

## 出处

- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.22_Protocol_editor.htm`
- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.22.01_Protocol_details.htm`
- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.22.02_Transaction_details.htm`
- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.22.05_Level_tab.htm`
- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.22.06_Wavetable_tab.htm`
- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.22.07_Timing_tab.htm`
- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.22.08_Protocol_wrapper.htm`
- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.22.09_Build_feature_of_the_protocol_editor_and_test_program_explorer.htm`
- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.22.10_Using_the_protocol_editor.htm`
- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.22.11_Working_with_Protocols.htm`
