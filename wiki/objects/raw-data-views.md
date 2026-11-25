---
type: object
title: Raw data views
layer: gui
stage: results
tags: []
related: []
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.03.01_Raw_data_views.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Raw data views

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

**文档事实** raw data view 显示 loaded data log 中选中汇总行所汇总的全部单条记录，可用来细查某个 test、device、wafer 或 bin 的结果。

**文档事实** 除描述每条 data log entry 的列之外，raw data view 还包含 toolbar、左右 margin 上可配置的 fail 与 alert marks，以及 context menu。

**文档事实** toolbar 包含 Link、Pin、New、Statistics、Preferences、Next Annotation、Previous Annotation、Follow Data。Link 把视图显示链接到 data navigation view 的选中行，选择变化时自动更新；Pin 冻结当前显示，即使 data navigation view 选择变化也不更新，点 Link 可恢复动态更新；New 新建 raw data view；Statistics 显示当前显示行的汇总，内容与 data navigation view 中选中行的内容相似；Preferences 打开 Raw Data preference page；Next Annotation 与 Previous Annotation 跳到含 annotation 的下一行或上一行，下拉列表可勾选或取消 annotation 类型；Follow Data 控制新数据加入时是否自动滚到底部。

**文档事实** 表格显示 frontmost data navigation view 中选中汇总行所汇总的 data log entries，每行一条 log entry。表格最上方青色背景行是 table filter，可按条件限制显示行。列包括 Testflow、Test Suite、Test Method、Test、Test#、Pattern Name、Wafer、Site、Pin、Device、Device ID、Part ID、Part Txt、Lower、下限比较符、Value、Unit、上限比较符、Upper、P/F、Time、TS Time、Print to Datalog、Test Text、Include/Exclude 勾选列。显示哪些列及顺序可在 preferences 中设置。点击列标题按该列升序排序，再点降序，再点取消排序并恢复 data store 中的顺序。

**文档事实** 左侧 annotation ruler 用图标标出 fail、alert、excluded、shmoo hole 的行，同一行有多个图标时重叠。右侧 overview ruler 为每个含 failed device 或 alert 的行显示小块颜色矩形，点击选中对应行，悬停显示 alert 原因，悬停右上角小色块显示 failed 行、excluded 行、alert 行的总数。默认颜色为 fail 红色、exclusion 蓝色、alert 黄色、shmoo hole 青色，全部启用，可在 Annotations preference page 修改。

**文档事实** context menu 包含 Open Definition、Open With 下的 Protocol Monitor、Analyze Selection、Include 子菜单、Exclude 子菜单、Filter 子菜单、Width 下的 Autofit、Copy、Alerts、Preferences。Include 子菜单有 Selection、All；Exclude 子菜单有 Selection、Pass、Fail、All；Filter 子菜单有 Show All、Show Only Pass、Show Only Fail。

## 典型用法

**文档事实** 在 data navigation view 选中一行后，raw data view 在 Link 模式下显示该行汇总的各条记录；要固定当前内容时点 Pin，之后点 Link 恢复跟随。

**文档事实** 用表格顶部的青色 filter 行输入条件限制显示行；用 Include/Exclude 勾选列或右键 Include、Exclude 子菜单把行纳入或排除出汇总与图表。Analyze Selection 把选中行纳入汇总并把其余行全部排除，效果等同于勾选选中行并取消其余行。

**文档事实** Filter 子菜单只限制显示为 pass 或 fail，是纯显示效果，隐藏记录不会像 Exclude 那样从评估中排除。Show All 恢复显示全部记录。

**文档事实** 右键 Open Definition 打开 testflow editor 并选中产生该 log entry 的 test suite，前提是该 testflow 已加载到 SmarTest。Open With 下的 Protocol Monitor 在 Protocol Monitor view 中显示选中行代表的数据。

**文档事实** Next Annotation 与 Previous Annotation 可跳转到 fail 或 alert；在下拉列表取消某类型后，SmarTest 不再跳到该类型，例如取消 Failed Test 后只跳到含 alert 的行。

**文档事实** Copy 把选中行以 tab-separated text 复制到剪贴板；Width 下的 Autofit 让每列宽度刚好显示全部内容。

**文档事实** 新建 raw data view 用 toolbar 的 New 按钮；配置显示列与顺序用 toolbar 的 Preferences 或右键 Preferences 打开 Raw Data preference page。

## 和谁有关

**文档事实** 本视图的数据来自 data navigation view 中选中的汇总行，且表格数据取自 frontmost data navigation view；data navigation view 的选择变化可驱动本视图更新。

**文档事实** 它属于 Detail data views，与 Stream data view 并列；system data log stream 的数据可在 Stream data view 或 raw data view 中查看。

**文档事实** Raw Data preference page 配置显示哪些列和列顺序，并引用本页说明可用列。

**文档事实** Annotations preference page 配置 fail、exclusion、alert、shmoo hole 指示的颜色与启用状态；Alerts preference page 由右键 Alerts 打开，其中 Highlight Failed Tests 控制 failed tests 行是否红色高亮，并同样影响 summary views。

**文档事实** Table filter 文档详述顶部 filter 行的条件过滤；Excluding data from evaluation 使用本视图的 Exclude 与 Include 子菜单；Highlighting specific data 使用本视图的 Next Annotation 与 Previous Annotation。

**文档事实** Trend chart、Box chart、Probability chart 等图表视图的 Show in Raw Data 命令会高亮本视图中对应行；Device summary tab 的 Show In 命令可把选中行显示到 raw data view，Test summary tab 也把 Raw data view 列为可用视图；Shmoo view 的 overlay plot 依赖本视图至少两个 included rows。

**文档事实** Print to Datalog 列显示 PUT_DATALOG API 的 comment 参数记录的文本；Test Text 列显示 TESTSET 的 TEST_TXT 字段数据。

**文档事实** 打开 Protocol Monitor view 时，可从 Test summary、raw data view 或 Stream data view 的右键菜单选 Show In > Protocol Monitor。

## 版本

**文档事实** 在 SmarTest 7.2.0 引入。

**文档事实** SmarTest 7.2.1 增加右键 Open Definition、表格排序、重命名部分列、excluded rows 与 shmoo holes 指示。

**文档事实** SmarTest 7.2.2 增加 Pattern Name 列与 Analyze Selection 命令。

**文档事实** SmarTest 7.2.3 增加 Part ID 与 Part Txt 列，并把 Include 与 Exclude 命令改为子菜单。

**文档事实** SmarTest 7.10.1 增加 Test Text 列。

## 出处

- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.03.01_Raw_data_views.htm`
