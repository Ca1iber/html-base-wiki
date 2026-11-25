---
type: object
title: CONNECT
layer: L2
stage: testmethod
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.18_CONNECT.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# CONNECT

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **487 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.41_DISCONNECT.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
void DISCONNECT();
```

List of parameters

There are no parameters.

Return value

There is no return value.

### Example

```
DISCONNECT();
...
...
PMU_IFVM("PIN1,PIN2").iForce(100 uA).settling(5 ms).mode("BP");

PMU_IFVM("PIN1,PIN2").limits("limit1").execute();
...
...
```

To
use the
`PMU_IFVM`（raw: `29543.htm`）
 API for a continuity test (SP or BP mode), you must

disconnect
 the tester resources from the DUT. This example disconnects the tester
resources from the DUT before the continuity test.

<!-- 语法节 end -->

## 是什么

**文档事实** DISCONNECT 是一个无参数、无返回值的测试方法 API。它把测试系统资源从 DUT 断开，并把测试机置为 "disconnect" 状态；如果资源已经断开，则不做任何动作。

**文档事实** 它与 disconnect testmethod 或主菜单的 Disconnect 项作用相同，执行以下序列：把 sequencer 置为 off 状态；把 analog 模块从 pogo pin 断开；给器件电源下电；把数字通道从 pogo pin 断开。

**文档事实** 该 API 定义在头文件 `/opt/hp93000/soc/prod_com/include/MAPI/TestControl.h`。

**文档事实** 多 site 测试时，DISCONNECT 必须用在 first-invocation block 中，不能放在 "each site" 循环块内；文档明确说明它在该循环块内无法正确工作。

**文档事实** 不要混用全局 `CONNECT()/DISCONNECT()` 与逐个 relay 切换。手动切 relay（例如 SmartRDI 的数字通道 relay 控制、`PPMU_RELAY`）不会改变全局 connect 状态，因此 `CONNECT()/DISCONNECT()` 会认为没有动作可做；原先手动切换过的 relay，必须再逐个手动切回才能改变其状态。

**推断** 与 CONNECT 一样，DISCONNECT 维护的是全局连接状态，而不是逐 relay 的即时状态。

## 典型用法

**文档事实** 基本调用只有 `DISCONNECT();`。文档示例在 continuity 测试前先断开测试机资源：

```cpp
DISCONNECT();
...
PMU_IFVM("PIN1,PIN2").iForce(100 uA).settling(5 ms).mode("BP");

PMU_IFVM("PIN1,PIN2").limits("limit1").execute();
```

**文档事实** 示例说明：要用 `PMU_IFVM` API 做 continuity 测试（SP 或 BP 模式），必须先把测试机资源从 DUT 断开；该例在 continuity 测试之前断开资源。

**文档事实** 多 site 测试应把 DISCONNECT 放在 first-invocation block（而不是 each site 循环块）中调用。

**建议** 与 CONNECT 成对使用；若测试机可能已经处于连接状态，文档给出的做法是先 `DISCONNECT` 再 `CONNECT`（UHC4T power modes 页的入边引文）。

## 和谁有关

- **CONNECT** — **文档事实**：本页 Related information 列出 CONNECT，二者互为反向操作；正文警告不要混用全局 `CONNECT()/DISCONNECT()` 与逐个 relay 切换。
- **FOR_EACH_SITE_BEGIN / FOR_EACH_SITE_END** — **文档事实**：本页 Related information 列出这两个 API；正文用 "each site" 循环块说明 DISCONNECT 在多 site 下的放置限制。
- **Disconnect（test control method）** — **文档事实**：正文指引读者参阅该 test control method 以了解 DISCONNECT 的更多信息。
- **PMU_IFVM** — **文档事实**：示例在 continuity 测试（SP/BP 模式）前调用 DISCONNECT，再用 `PMU_IFVM` 测量。
- **DISCONNECT_EX** — **文档事实**：该页说明 DISCONNECT_EX 断开测试系统与 DUT，功能与 DISCONNECT API 相同（objpack 入边引文）。
- **Standard disconnect sequence / Comparing the disconnect methods** — **文档事实**：这两页说明 DISCONNECT API 执行标准 disconnect 序列；若定义了 `disconnect.user_def`，则执行该用户定义序列，否则执行标准序列（objpack 入边引文）。
- **DC_Test_Programming** — **文档事实**：该页要求用 DC API 做 continuity 测试时必须执行 DISCONNECT（objpack 入边引文）。
- **MTP_CONTINUITY_TASK / MTP_CONTINUITY_TASK.execute** — **文档事实**：这些页要求在使用 `execute()` 前调用 DISCONNECT，因为 continuity 测试需要先给 DUT 下电并断开数字引脚再测量（objpack 入边引文）。
- **PPMU_RELAY、SmartRDI 数字通道 relay 控制** — **文档事实**：正文把这两者列为 “手动切 relay” 的例子，说明它们不改变全局 connect 状态。

## 版本

**文档事实** Functional changes 只记一条：Introduced before SmarTest 6.3.2。

## 出处

- `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.41_DISCONNECT.htm`：DISCONNECT 专文，本页五节事实的来源，含定义、多 site 与 relay 混用注意事项、头文件、Syntax、Example、Related information、Functional changes。
- `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.18_CONNECT.htm`：本页 frontmatter 声明的共享源文档；CONNECT 页本身不含 DISCONNECT 的断开序列与 continuity 示例，故上述内容取自 DISCONNECT 专文。
