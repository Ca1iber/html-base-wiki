---
type: object
title: END_EXTENSION
layer: L2
stage: testmethod
tags: []
related: []
sources:
  - 02_System_reference/02.07_Test_Method_Reference/02.07.04.01.59_END_EXTENSION.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# END_EXTENSION

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **133 字符逐字取自** `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.59_END_EXTENSION.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

```
void END_EXTENSION();
```

List of parameters

There are no parameters.

### Example

See the Examples section of
`BEGIN_EXTENSION`（raw: `28740.htm`）
.

<!-- 语法节 end -->

## 是什么

**文档事实** END_EXTENSION 是 test method API，声明由 BEGIN_EXTENSION 开始的 extension block 到此结束；它应与 BEGIN_EXTENSION 成对使用，二者共同声明 extension block。

**文档事实** 本 API 定义在头文件 `/opt/hp93000/soc/prod_com/include/MAPI/Extension.h`。

**文档事实** 语法为 `void END_EXTENSION();`，没有参数。

**文档事实** extension block 的细节按其指引见 BEGIN_EXTENSION 页：块内可写一个或多个 FW_TASK，也可写自建函数，但不应写其他 test method API；块存在期间 test method 的 caching 机制被系统临时关闭；进入块前应先执行 FLUSH，把 ANALOG、ANALOG_STATUS、PRIMARY_STATUS、ROUTING_STATUS 等缓存数据下载到硬件或 MCD。

**文档事实** 多 site 时 BEGIN_EXTENSION 可带 `sites` 参数设置块内语句的 setup focus；紧接 BEGIN_EXTENSION 的 END_EXTENSION 会把 setup focus sites 恢复到进入 extension block 前的设置；extension block 可以嵌套，嵌套不正确时 nest 信息会在 test suite 执行结束时自动初始化，并在 report window 出现 warning。

**推断** 因此 END_EXTENSION 不只是语法上的闭合标记：对 setup focus 的恢复与嵌套层退出等语义由 BEGIN_EXTENSION 页描述，本页只给出声明与配对关系的说明。

## 典型用法

**文档事实** 基本写法是 `END_EXTENSION();`，放在 extension block 末尾；本页示例直接指向 BEGIN_EXTENSION 的 Examples 段。

**文档事实** BEGIN_EXTENSION 示例 1：`BEGIN_EXTENSION();` 后接 `FW_TASK(dfcm);`、`FW_TASK(ptstq, answer);` 等，最后以 `END_EXTENSION();` 收尾。

**文档事实** BEGIN_EXTENSION 示例 2：`GET_ENABLED_SITES(enabled_sites); BEGIN_EXTENSION(enabled_sites);` 写入块内语句后，再以 `END_EXTENSION();` 结束；块只对当前 enabled sites 生效。

**文档事实** 在嵌套 extension block 中，每个 BEGIN_EXTENSION 对应一个 END_EXTENSION；紧接 BEGIN_EXTENSION 的 END_EXTENSION 会把 setup focus 恢复为进入前的设置。

**建议** 始终把 END_EXTENSION 与对应的 BEGIN_EXTENSION 严格配对；进入块前先 FLUSH，块内只放 FW_TASK 或自建函数，不放其他 test method API。多 site 的 first-invocation block 中，应按多 site 入边所述让 BEGIN_EXTENSION 显式带 `sites` 参数，而不要使用不带参数的 BEGIN_EXTENSION（END_EXTENSION 本身没有参数）。

## 和谁有关

- **文档事实** `[[begin-extension]]` — 主源称 END_EXTENSION 与 BEGIN_EXTENSION 成对使用以声明 extension block，并明确细节与示例见 BEGIN_EXTENSION；BEGIN_EXTENSION 页给出 extension block 的完整语义、嵌套与 setup focus 恢复规则。
- **文档事实** `[[fw-task]]` — 主源 Related information 列出 FW_TASK；FW_TASK 页（objpack 入边）称 BEGIN_EXTENSION 与 END_EXTENSION 总是与 FW_TASK 一起使用，且两 API 之间除 firmware 命令外还可执行自建函数。
- **文档事实** `Extension.h` — 主源给出 END_EXTENSION 的头文件路径 `/opt/hp93000/soc/prod_com/include/MAPI/Extension.h`；BEGIN_EXTENSION 页给出相同路径。
- **文档事实** `02.07.03.10_Executing_Firmware_Commands.htm` — 入边称在 test method 中执行 firmware 命令的详情见 FW_TASK、BEGIN_EXTENSION 与 END_EXTENSION。
- **文档事实** `02.07.03.13.08_Important_Points_on_Multisite_Programming.htm` 与其应用论文版、以及 `03.01.03.01.02_Usage_of_Parallel_Hardware__PPMU.htm` — 入边说明在 first-invocation block 中用带 site 参数的 BEGIN_EXTENSION 与 END_EXTENSION 包住 FW_TASK；PPMU 页并告诫不要用不带参数的 BEGIN_EXTENSION/END_EXTENSION 来包。
- **文档事实** `02.07.04.01_APIs_in_alphabetical_order.htm` — 入边把 END_EXTENSION 列在 test method API 总表中。

## 版本

**文档事实** Functional changes 记：`Introduced before SmarTest 6.3.2`。

## 出处

- `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.59_END_EXTENSION.htm`，主源，含 API 说明、头文件、Syntax、Example 指引、Related information 与 Functional changes，已用 `show.py` 与 `objpack.py` 读取。
- `02_System_reference/02.07_Test_Method_Reference/02.07.04.01.10_BEGIN_EXTENSION.htm`，用于 extension block 语义、示例、嵌套与 setup focus 规则，已用 `show.py` 读取。
- FW_TASK、Executing Firmware Commands、Important Points on Multisite Programming、PPMU 应用论文与 APIs in alphabetical order 的引用语境取自 `extract/objpack.py` 的 `edges.jsonl`。
