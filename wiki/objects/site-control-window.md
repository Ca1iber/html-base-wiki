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

（待补）

## 典型用法

（待补）

## 和谁有关

（待补）

## 版本

（待补）

## 出处

（待补）
