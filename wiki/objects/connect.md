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

> 本节 **431 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.18_CONNECT.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
CONNECT();
```

List of parameters

There are no parameters.

Return value

There is no return value.

### Example

```
CONNECT();
...
...
PMU_IFVM("PIN1,PIN2").iForce(100 uA).settling(5 ms);

PMU_IFVM("PIN1,PIN2").limits("limit1").execute();
...
...
```

To
use the
`PMU_IFVM`（raw: `29543.htm`）
 API, you must set the tester to the

CONNECT
 status. This example connects the tester resources to the DUT
with the
CONNECT
 API before DC measurement.

<!-- 语法节 end -->

## 是什么

**文档事实** CONNECT 是一个无参数、无返回值的测试方法 API。它把测试机资源连接到 DUT，并把测试机置为 "connect" 状态；如果资源已经连接，则不做任何动作。

**文档事实** 它与主菜单的 Connect 项作用相同，执行以下序列：把 AC relay 连接到 DUT 引脚；给 DUT 电源上电；把 sequencer 置为 break/on 状态。

**文档事实** 该 API 定义在头文件 `/opt/hp93000/soc/prod_com/include/MAPI/TestControl.h`。

**文档事实** 多 site 测试时，CONNECT 必须用在 first-invocation block 中，不能放在 "each site" 循环块内；文档明确说明它在该循环块内无法正确工作。

**文档事实** 不要混用全局 `CONNECT()/DISCONNECT()` 与逐个 relay 切换。手动切 relay（例如 SmartRDI 的数字通道 relay 控制、`PPMU_RELAY`）不会改变全局 connect 状态，因此 `CONNECT()/DISCONNECT()` 会认为没有动作可做；原先手动切换过的 relay，必须再逐个手动切回才能改变其状态。

**推断** 这里的 “全局 connect 状态” 是 API 与菜单项共用的一个状态，手动 relay 操作绕过它；两者混用会让 “API 认为的状态” 与 “实际 relay 状态” 不一致。

## 典型用法

**文档事实** 基本调用只有 `CONNECT();`。文档示例在 DC 测量前先连接测试机资源：

```cpp
CONNECT();
...
PMU_IFVM("PIN1,PIN2").iForce(100 uA).settling(5 ms);

PMU_IFVM("PIN1,PIN2").limits("limit1").execute();
```

**文档事实** 示例说明：要使用 `PMU_IFVM` API，必须先把测试机置为 CONNECT 状态；该例在 DC 测量之前用 CONNECT API 把测试机资源连接到 DUT。

**文档事实** 多 site 测试应把 CONNECT 放在 first-invocation block（而不是 each site 循环块）中调用。

**建议** 与 DISCONNECT 成对使用，并避免在同一段流程里再手动切 relay，以免全局连接状态与手动 relay 状态互相冲突。

## 和谁有关

- **DISCONNECT** — **文档事实**：本页 Related information 列出 DISCONNECT，二者互为反向操作；正文同时警告不要混用全局 `CONNECT()/DISCONNECT()` 与逐个 relay 切换。
- **FOR_EACH_SITE_BEGIN / FOR_EACH_SITE_END** — **文档事实**：本页 Related information 列出这两个 API；正文用 "each site" 循环块说明 CONNECT 在多 site 下的放置限制。
- **Connect（test control method）** — **文档事实**：正文指引读者参阅该 test control method 以了解 CONNECT 的更多信息。
- **PMU_IFVM** — **文档事实**：示例要求先处于 CONNECT 状态，再用 `PMU_IFVM` 做 DC 测量。
- **CONNECT_EX** — **文档事实**：该页说明 CONNECT_EX 连接测试系统与 DUT，功能与 CONNECT API 相同（objpack 入边引文）。
- **PPMU_RELAY、SmartRDI 数字通道 relay 控制** — **文档事实**：正文把这两者列为 “手动切 relay” 的例子，说明它们不改变全局 connect 状态。
- **DC_Test_Programming / AC_Test_Programming** — **文档事实**：两页都要求在测试前执行 CONNECT 序列，以给 DUT 上电并连接目标引脚；DC 页还要求用 DC API 做 continuity 测试时执行 DISCONNECT（objpack 入边引文）。
- **MTP_IDD_TASK / MTP_LEAKAGE_TASK** — **文档事实**：这两页要求在使用 `execute()` 前调用 CONNECT，因为 IDD/leakage 在连接状态下测量（objpack 入边引文）。
- **MTP_MEMORY_TEST.execute** — **文档事实**：该页说明 `execute()` 不会自动把测试机资源连到 DUT，需确保测试机与 DUT 已连接，例如在调用前使用 `CONNECT()`（objpack 入边引文）。

## 版本

**文档事实** Functional changes 只记一条：Introduced before SmarTest 6.3.2。

## 出处

- `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.18_CONNECT.htm`：主源，含定义、多 site 与 relay 混用注意事项、头文件、Syntax、Example、Related information、Functional changes。
