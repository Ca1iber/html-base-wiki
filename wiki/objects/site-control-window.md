---
type: object
title: Site Control Window
layer: gui
stage: run
tags: []
related: []
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.27_Site_Control_Window.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Site Control Window

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **2,240 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.27_Site_Control_Window.htm>` 及其子主题 `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.27.01_The_states_of_the_sites.htm>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.27.02_Expanded_Site_Control_window.htm>`、`<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.27.03_Changing_the_site_in_focus.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example（取自子主题 The states of the sites）

The menu items of the Site Control window
Action > Enable all

and
activate all
only affect those sites which are available.
The figure below shows an example, where the sites 2, 3, 6, 7, 9, 10, 13 and 14 are not
available.

The following figure shows the indication behavior of the check boxes in the Site
Control window during a semi-parallel test.

### Example（取自子主题 Expanded Site Control window）

For example, to test sites 1 and 2 in parallel and then sites 3 and 4 in parallel for
four-site semi-parallel testing, you can set up the test sequence by specifying

Size
 =
2
 and
Cycle
 =

Unbounded
. Each parallel test in the semi-parallel test will be executed
from the group including site 1 in numerical order.

If test sites are added afterward, additional sites will be tested according to the

Size
 and
Cycle
 settings. Therefore, you do not
have to set up this again.

The figure below shows three examples of the site test sequence settings including the
above typical example.

You can also enter the order numbers directly into the Site Test Sequence field. Hence,
you can set up a free site test sequence. In this case, if test sites are added afterward,
additional sites will be tested in parallel after tests of the existing sites are completed.

The
Parallel
 and
Serial
 buttons can be
used to change the site test sequence from
Semi-Parallel
 or free
sequence to the
Parallel
 or
Serial

sequence.

Note
 If you turn the
`Allow Parallel`（raw: `342556.htm#_342556__row_allow_parallel`）
 flag off, all sites will be tested serially. However, the sequence
might be different from the sequence specified by clicking the

Serial
 button. For example, if you click the

Semi-Parallel
 button and run the test suite in the following
sequence as sites 1 and 3 (in parallel), and site 2 and site 4 (in parallel), then after
you turn off the
Allow Parallel
 flag, the site test sequence is
site 1, site 3, site 2, and site 4. However, for the serial test (the
Allow
Parallel
 flag is turned on and the
Serial
 button
is pressed), the site test sequence is site 1, site 2, site 3, and site 4.

TIP:
 You can also set up the site test sequence for all test suites in
the Site Control window. If you want to set it up for many test suites once, it is better to use
the Site Control window.

### Example（取自子主题 Changing the site in focus）



<!-- 语法节 end -->

## 是什么

**文档事实** Site Control Window 是 SmarTest Work Center 的窗口，路径为 93000 > System > Site Control。它用于调试 multisite testflow 时识别通过和失败 site，并在结果工具中查看单个 site 的结果。

**文档事实** 它允许设置每个 site 的状态，也允许模拟 site setup 的行为，后者通常由 prober/handler library 完成。

**文档事实** 文档截图是小版本，展开视图见 Expanded Site Control window，用 Edit > Expand 打开。

**文档事实** site 状态有 Enable、Active、Focus 三种。因 pin 配置缺陷而不可用的 site 不能被 enable、activate 或获得 result focus，只能对可用 site 设置状态。

**文档事实** Enable 的含义。site 启用时，每次运行 connect sequence 都会连接。site 禁用时执行 disconnect sequence，并保持断开，不受其他 site 状态影响。已启用但未激活的 site 视为插入 bypass，禁用的 site 视为未插入。插入或移除 DUT 时应 disable site，以减少对其他 site 的干扰并降低损伤器件的可能。只有在 disconnected 状态才能交互地把 enable 按钮关掉，在 connected 状态这样做会出现警告消息。

**文档事实** Active 的含义。site 激活时对其执行 testflow，并处理该 site 在 testflow 中产生的错误。site 未激活时其 receivers 被屏蔽，没有该 site 的结果信息。active site 视为插入 test，激活 site 会自动设置 enable 复选框。

**文档事实** Focus 的含义。处在 query focus 的 site，其结果在 testflow editor 与结果工具中显示，firmware 查询也报告该 site 当前的 setup 与结果。同一时刻只有一个 site 能在 focus。pin configuration 加载后，第一个未列入 MCDIgnore 文件的 site 获得 focus。聚焦 site 会自动设置 enable 与 active 复选框。

**文档事实** Action > Enable all 与 activate all 两个菜单项只影响可用的 site。文档示例中 site 2、3、6、7、9、10、13、14 不可用。

## 典型用法

**文档事实** 选择要测试的 site。打开 93000 > System > Site Control，对需要的 site 勾选 active 复选框，这会同时勾选 enable，对不需要的 site 取消 enable，这会同时取消 active，然后执行 testflow。执行期间 site 会自动激活和去激活，结果工具始终显示 focus site 的结果。

**文档事实** 改变 focus。勾选目标 site 的 focus 复选框，这会同时勾选 enable 与 active，然后执行 test suite 或 testflow，结果窗口显示 focus site 的结果。改变 focus 会改变结果工具的内容，但不更新 report window。

**文档事实** 只对 focus site 执行 test suite。在 testflow editor 右键 test suite 选 Execute site in focus。流程先把除 focus 外的所有活动 site 去激活并屏蔽，只对 focus site 执行 test suite，然后重新激活被屏蔽的 site。

**文档事实** 文档提醒 Execute site in focus 的第三步。重新激活 site 会重置所有 site 的 Error Map 数据，因此第三步会删掉刚为 focus site 生成的 Error Map 数据。若要保留这些数据，须先手动把除 focus 外的 site 都去激活，这样执行时第三步就省略了。

**文档事实** Expanded Site Control window 可直接查看和修改每个 test suite 的 site test sequence 设置。界面含 test suite 名单、site control 执行模式、Size 与 Cycle、Site test sequence 以及 allow parallel flag。执行模式可选 Parallel、Serial、Semi-Parallel，Testflow Properties view 中还可设为 OTHER 或 UNDEF。allow parallel flag 必须先置 yes，才能选择 Parallel 或 Semi-Parallel。

**文档事实** Size 与 Cycle 定义半并行测试自动生成的 site test sequence。Cycle 设为 Unbounded 时，Size 定义每组半并行测试的 site 数，第一组从 site 1 开始，其余 site 按数值顺序按 Size 分组。Size 与 Cycle 都取数值时，Cycle 定义 virtual group 的 site 数，Size 定义 virtual group 内 parallel group 的大小，parallel group 数为 Cycle 与 Size 之比。parallel group 内的 site 并行测试，同一 virtual group 内的 parallel group 串行测试，各 virtual group 并行测试。

**文档事实** 半并行示例。四 site 半并行测试中先并行测 site 1 与 2，再并行测 site 3 与 4，可设 Size = 2、Cycle = Unbounded。每个半并行测试从含 site 1 的组开始按数值顺序执行。若之后增加 test site，新增 site 会按 Size 与 Cycle 设置安排，无需重新设置。

**文档事实** 也直接在 Site Test Sequence 字段输入顺序号，形成自由的 site test sequence。此时执行模式变为空，对应 Testflow Properties view 的 OTHER 设置。若之后增加 test site，新增 site 会在现有 site 测试完成后并行测试。

**文档事实** 若关闭 Allow Parallel flag，所有 site 串行测试，但顺序可能与点 Serial 按钮得到的顺序不同。文档示例中先点 Semi-Parallel 并按 site 1 与 3 并行、site 2 与 4 并行的顺序运行，关掉 Allow Parallel 后顺序为 site 1、3、2、4，而在 Allow Parallel 开启并点 Serial 时顺序为 site 1、2、3、4。

**文档事实** 文档 TIP 指出 Site Control window 也可为所有 test suite 设置 site test sequence。若要一次为多个 test suite 设置，用它更合适。

## 和谁有关

**文档事实** Expanded Site Control window `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.27.02_Expanded_Site_Control_window.htm`。它由 Edit > Expand 打开，提供逐 test suite 的 site test sequence 设置。

**文档事实** The states of the sites `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.27.01_The_states_of_the_sites.htm`。它说明 Enable、Active、Focus 三种状态与 Execute site in focus 的流程。

**文档事实** Changing the site in focus `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.27.03_Changing_the_site_in_focus.htm`。它说明改变 query focus 的步骤，Related information 指向 Controlling Multiple Sites、Site dependent firmware commands、Defining the query focus。

**文档事实** Selecting the sites to run your test `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.27.04_Selecting_the_sites_to_run_your_test.htm`。它说明用 Site Control window 选择参与测试的 site。

**文档事实** Site control flags `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.07.05_Site_control_flags.htm`。它说明展开的 Site Control Window 仅在进行 multisite 测试开发时用于设置 site 测试顺序。

**文档事实** Testflow Properties view `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.04_Testflow_Properties_view.htm`。执行模式也可设为 OTHER 或 UNDEF，直接输入顺序号对应的就是 OTHER。

**文档事实** allow parallel flag `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.01.02.07.01_Alphabetical_list_of_flags.htm` 的 Allow Parallel 行。它必须先置 yes，才能选择 Parallel 或 Semi-Parallel。

**文档事实** Setting Flags for Parallel Execution `03_Use_cases_and_application_papers/03.02_How_to_do_Multi-Site_Testing/03.02.02.06.04_Setting_Flags_for_Parallel_Execution.htm`。它是 Expanded Site Control window 的 Related information。

**文档事实** Site Select view `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.28_Site_Select_view.htm`。它提供与 Site Control Window 类似的 site setup 功能，更适合大量 site，因为 Site Control Window 只支持单个 site 的状态选择。

**文档事实** Debugging a testflow `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.02.04_Debugging_a_testflow.htm`。它说明调试可能为 multisite 的 testflow 时，用 Site Control Window 识别通过和失败 site 并查看单个 site 的结果。

**文档事实** Viewing the shmoo plots of different sites `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.25.03.04.07_Viewing_the_shmoo_plots_of_different_sites.htm`。它说明要查看另一 site 的 shmoo plot 时，用 Site Control Window 切换 site。

**文档事实** Controlling Multiple Sites `02_System_reference/02.07_Test_Method_Reference/02.07.03.13_Controlling_Multiple_Sites.htm`。Changing the site in focus 的 Related information 指向它，该页的引用语境也把 Site Control Window 列为相关内容。

**文档事实** 93000 menu and its tools `01_Getting_started/01.01_SmarTest_Work_Center/01.01.11.01_93000_menu_and_its_tools.htm` 与 `02_System_reference/02.08_Setup_and_Result_Tools/02.08.02_93000_menu_and_its_tools.htm`。它们把 Site Control Window 列在 93000 菜单的工具中。

**文档事实** Hardware view for digital pins `01_Getting_started/01.01_SmarTest_Work_Center/01.01.07.05.03.03_Hardware_view_for_digital_pins.htm`。它说明 multisite 调试时用 Site Control window 的 focus 按钮选择 site。

**文档事实** Pin Browser preference page `01_Getting_started/01.01_SmarTest_Work_Center/01.01.14.14_Pin_Browser_preference_page.htm`。其中一项按 Site Control Window 中 enabled site 数来显示所有活动 site。

## 版本

**文档事实** 主页以及 The states of the sites、Expanded Site Control window、Changing the site in focus 三个子主题的 Functional changes 都只写 Introduced before SmarTest 6.3.2，未记录后续版本变更。

**文档事实** 子主题 Selecting the sites to run your test 没有 Functional changes 段。

## 出处

- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.27_Site_Control_Window.htm`。主源，含窗口用途、93000 菜单路径、大小版本说明。
- `02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.27.01_The_states_of_the_sites.htm`、`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.27.02_Expanded_Site_Control_window.htm`、`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.27.03_Changing_the_site_in_focus.htm`、`02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.27.04_Selecting_the_sites_to_run_your_test.htm`。全部读过，用于状态、执行模式与版本。
