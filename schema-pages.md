# 93K 测试开发 Wiki — 页面规格

> 本文件规定 **wiki 里有哪些页面、每一部分该怎么写**。
>
> 它与语料从哪里来、用什么工具读无关：无论源层是原始 HTML、转换后的 Markdown，
> 还是别的表示，页面都按这份规格产出。
>
> **材料从哪来、怎么抽取、怎么检查——见 `schema-pipeline.md`。**
> 本文件里不出现路径、工具名和语料篇数。

---

## 0. 这个 wiki 是干什么的

让 agent 能**独立完成 Advantest V93000 / SmarTest 测试开发**，而不是只会查文档回答问题。

目标形态：agent 拿到一个器件，能自己走完

```
建工程 → Pin → Level → Timing → Pattern → Test Method → Testflow → 运行 → 结果
```

横跨三层接口：

| 层 | 内容 |
|---|---|
| **L1** | Firmware / setup command（配置文件里的命令） |
| **L2** | Test Method API（C++ 测试方法） |
| **L3** | 外部控制（SmartShell / Test suite control API / HVM） |

**wiki 只告诉 agent「该怎么做」。「做得到」是工具层的事，不要混为一谈。**

**一页 wiki 存在的理由，是它回答了一个问题。** 回答不了问题的页不要建。

### 不丢信息

**wiki 可以简写，但不能漏。**

- 源里属于本页范围的东西，页面上**至少要有名字和一句话**——
  哪怕只是一句「`XX` 见 `02.06.03.02.xx`」。
- **「没写」和「源里没有」必须能区分开。** 源里有而页面没提，就是漏。
- 深度按页类不同：**stage 页要详细**；object / concept / constraint 等可以更紧凑，
  但同样不许漏项。
- 漏了的东西，agent 就找不到——而 raw 层存在的意义正是「能被找到」。

---

## 1. 页面类型总览

七类。前五类是主干，后两类是补充。

| 类型 | 目录 | 一句话定义 |
|---|---|---|
| `stage` | `wiki/stages/` | 流程的一段 |
| `object` | `wiki/objects/` | 一个具体的东西 |
| `concept` | `wiki/concepts/` | 一条需要理解才能用对的原理 |
| `constraint` | `wiki/constraints/` | 一条前置条件 / 依赖 / 顺序要求 |
| `mapping` | `wiki/mappings/` | 跨层对应关系 |
| `error` | `wiki/errors/` | 一条排错路径 |
| `version` | `wiki/versions/` | 一个版本的变更 |

**每页必须在 frontmatter 的 `type` 里声明且只能声明一个类型。** 类型决定它进哪个目录、
必填哪些字段、必须有哪些节。

---

## 2. 七类页面

### 2.1 `stage` — 阶段页（脊椎）

**目录**：`wiki/stages/`
**数量**：固定九页，一一对应测试开发的九段流程。

```
project     建工程 / Device / 目录结构
pin         Pin / Channel 配置
level       Level 电平配置
timing      Timing / Wavetable
pattern     Pattern / Vector
testmethod  Test Instance / Test Method
testflow    Testflow 组装
run         Run / Debug
results     Results / 数据与判定
```

**stage 页是唯一允许写「流程」的地方。** 其他页提到顺序时，链接过来，不要复述。

**每页固定结构（不许省略任何一节，没有内容就写「文档未覆盖」）：**

```markdown
## 目的
这一步在整条流程里解决什么问题。

## 前置条件
做这一步之前必须完成什么。链接到 [[constraint]] 页。

## 涉及对象
本阶段用到的命令 / API / 文件 / 工具，链接到各自的 [[object]] 页，并标明层级。

### 归属判定
可选子节。写下本次建页时判给谁、不判给谁、为什么。

## L1 — Firmware / Setup Command
本阶段命令子树下的**全部命令**，逐条交代；每条至少写「命令名 + 一句作用 + 出处」，
能给最小可用示例的就附上。

## L2 — Test Method API
本阶段在 C++ 测试方法里对应的 API。

## L3 — 外部控制

## 产物
这一步产出哪些文件、放在哪里、什么格式。

## 验证
怎么确认这一步做对了（校验命令、查询命令、GUI 上应该看到什么）。

## 常见错误
出错时的典型症状与排查入口，链接到 [[error]] 页。

## 下一步
链接到下一个 [[stage]] 页。
```

**L1 的覆盖范围 = 本阶段命令子树。** 例如 `pin` 阶段的命令子树是 `02.06.03.02.*`。
先用 `show.py --list 02.06.03.02` 列出全部（35 条），再逐条写。
**不许只写主路径上的几个。** 深度可以按重要性分配，但**每一条都必须出现**。

#### 归属判定

写「判给谁、不判给谁、为什么」。**这不是文档事实，是判断**，写在这里供维护者复核。

为什么需要这一节：文档按**功能**分组（命令参考、API 参考、GUI 工具），
stage 按**流程段**分组，**两套坐标不一致**。每个 stage 都会遇到
「这条命令看起来像我的，但不是」的情况。

不写下来，下次就会有人重新判一遍，而且很可能判得不一样。

#### L3 小节怎么写

**`L3` 这一节不许只写「文档未覆盖」。**

L3 不是空的：至少包括 Test suite control API、TPI（Test Programming Interface）、
HVM API 三类。写之前必须先在测试程序管理相关章节里按分类号找过一遍。

正确写法是两段：

```markdown
**L3 入口是横切的，能力面按阶段分族。** 横切入口见 [[test-suite-control-api]] /
[[tpi-program-routines]]；本阶段的专属族是 <列出分类号与成员>。
```

**依据（文档事实）**：`TestsuiteProxy` 的编号成员天然按 stage 分组——
这不是巧合，是文档自己的组织方式。TPI 的 `DataManager` 文件标识
（`dm_config` / `dm_level` / `dm_timing` / `dm_vector` / `dm_testflow` / `dm_emap` …）
也几乎一一对应九个 stage 的产物。

**四条硬规矩：**

1. **先查再写。** 写「文档未覆盖」之前，必须在测试程序管理相关章节里按分类号找过一遍。
   **「我没找到」和「文档没有」是两件事，页面只许写后者。**
2. **不许下「不提供任何 X 接口」这类全称断言。** 举证的义务在写的人；
   证不了就写「本次未找到」。
3. **错的断言比缺的断言更危险。** 缺的会被下一次发现；错的会被当成「查过了，没有」，
   从此没人再查。所以返工时要在页内留下「上一版写了什么、为什么错」的改判记录。
4. **同形陷阱要显式记一笔。** 名字里有 level/timing 但不属于本阶段的东西
   （例如 HVM 的 `GetLevelProfile`、BLC 的 `StartLevel()`——那是 application model
   的层级结构，不是电压 level），写进页面当反例。否则下一个 agent 会拿它去「补」错页。

> **这一节的来历值得记：** 建第一批九页时，有七页的 L3 只写了一句「文档未覆盖」，
> 其中四页的断言本身是错的。错误来源是建页简报里写的一句
> 「L3 语料里很薄，薄就写文档未覆盖」——被照办了。
> **枚举式的定义，漏一项就会让本该是文档事实的东西降级成猜测。**
> **清单比它自称的范围窄，窄掉的那块一直是绿的。**

---

### 2.2 `object` — 对象页

**目录**：`wiki/objects/`
一个具体的东西：一条命令、一个 API、一个文件格式、一个 setup 组件、一个工具。

**每个对象的必填字段**：`layer` + `stage`。

**内容**：是什么、语法/签名、参数、典型用法、和谁有关。
**不含流程叙述**（那是 stage 页的事）。

**必备节：**

```
## 语法 / 参数
## 报错条件
## 是什么
## 典型用法
## 和谁有关
## 版本
## 出处
```

- **语法 / 参数**：逐字取自源文档，**不重写**。重写会把「文档事实」降级成转述。
  子节按命令形态组织（如 `### DFPN`、`### DFPN?`、`### Parameters`）。
- **报错条件**：源文档 `Errors` / `Warnings` 段的逐字内容。
- **是什么**：对象本身是什么，不用流程语言。
- **典型用法**：最小可用示例。
- **和谁有关**：只写有证据的关系（链接、前置条件、同族命令），每条能回到出处。
- **版本**：该对象属于哪个版本、有哪些版本差异；有独立版本页时链过去。
- **出处**：本篇依据的源文档。

---

### 2.3 `concept` — 概念页

**目录**：`wiki/concepts/`
Testflow、Sequencer、Ganging、Wavetable、DC Scale 这类**需要理解才能正确使用**的东西。

**判据：如果一个概念理解错了会导致配置写错，它就该有独立一页。**
达不到这条，就不要单独建页——写进相关对象页的散文里。

**必备节：同 §2.2 的 object 骨架，去掉 `## 报错条件`。**
（`## 语法 / 参数` 只在概念有可直接引用的语法/参数时才保留。）

**`是什么` 一节组织的是「原理」**，不是操作步骤。来源是文档里的
操作模式（`Mode of operation`）、应用说明（`Application`）、基础阅读（`Fundamental reading`）
这类段落。

**允许在 `是什么` 下用 `###` 展开任意子主题**——每页的子主题应当不同，
因为它们承载的是各页真正的知识。**规格只约束 `##` 级节，不约束 `###`。**

---

### 2.4 `constraint` — 约束页

**目录**：`wiki/constraints/`
**这是全栈自动化成败的关键页类。**

内容：**前置条件、依赖、互斥、顺序要求。**

已知的典型，全部来自文档原句：

- `DFPN` 使用前 sequencer 状态必须是 OFF（见 `SQST`）
- 跨卡 ganging 之前，连接必须先由 `DDIC` 使能
- 同一 connectionSet 下的 trace 必须一致
- **Pin configuration 是 Level / Timing / Vector 的前置条件**

**每页必须写清**：约束是什么、在什么条件下成立、违反了会怎样、出处是哪一篇。

#### 真约束长什么样——四形态，三类不是

**一句话判据：句子里有没有「第二个东西」。** 只有主语自己，就不是约束。

| | 形态 | 文档实例（逐字） |
|---|---|---|
| **D1** | **顺序前置** — A 之前/之后必须 B | `The APDV command can only be issued after a label has been selected for editing with the TSTL command.`<br>`The member function uploadPeriodResults() of TMU_PINS needs to be used before using this function.`<br>`After you have defined the logical waveform with WFDF, you must specify the physical waveforms that are based on it with the WAVE command.` |
| **D2** | **状态前提** — A 只在状态 S 下成立，S 由别的东西决定 | `A test point pattern must have been executed for DC Scale pins.`<br>`The bit fail maps must have been loaded, as described in Loading bit fail maps into the BFM Viewer.`<br>`You must not change or reload a TMLimits table while an SMC background process is armed or running.`<br>`The specified label must be the main label, not a burst label or subroutine.` |
| **D3** | **一致/匹配** — 两个东西必须相同 | `For one pin, xMode must remain the same in different labels in burst; otherwise the results might be wrong.`<br>`Loopback pins must belong to the same test processor (TP).`<br>`The sequence of the pins must match the sequence of the sweep variables.`<br>`When a wavetable is combined with a timing set in a timing specification, both must specify the same value for this keyword.` |
| **D4** | **位置/归属** — A 必须放在 X 里/外，或赋给 X | `It must be used inside a RDI_BEGIN()/RDI_END() block.`<br>`The member function must be called outside of the ON_FIRST_INVOCATION…`<br>`The object that is created by this class has to be assigned to the PATTERN_CONTROLLER…` |

**D2 与 D1 的真实差别：** **D1 你按顺序写就对了；D2 你要确认「它已经在那儿了」。**
前者是书写顺序问题，后者是运行期状态问题——页面上必须分开写，
否则读的人会以为照顺序写就万事大吉。

> **一张页可以装两条不同的规矩，但必须点明是两条。**
> 例如 `RDI_BEGIN/RDI_END` 那一页里，D4 与 D3 并排——
> 页内明写「规矩一管写在哪儿、规矩二管值必须相同」，并各自标了形态。

**三类不是约束**（都不建 constraint 页）：

- **格式要求**——主语自己**量或形状**的要求，没有第二个东西：
  `If more than one pin is to be included, the names must be separated with a comma.` /
  `The list must be enclosed in square brackets..` /
  `To be compatible with STDF, the number must be between 0 and 32767.`
  **归宿是那个参数的语法表。**
- **单对象属性**——主语是对象本身，谓语是 supported/available/allowed，
  **不涉及第二个东西**：
  `This member function is supported only for the DC Scale XPS256 card.` /
  `The break waveform must not contain data dependent actions.`
  **归宿是那个对象自己的页。**
- **能力/用途说明**——`in order to` 表目的，不表前置：
  `In order to achieve a higher output current, parallel connection of multiple XPS256 channels is supported.`
  **它陈述的是「能这么干」，不是「必须先干什么」。**

> **前置词不是筛子。** 它只是候选清单上的一个抓手，会漏掉
> `previously`、`inside`/`outside`、`belong to the same`、`must be the main label`
> 这类写法。**用它排序可以，用它当判据不行。**

#### 取证时容易踩的三个坑

1. **同一族规矩，`Predependencies` 段和 `Errors` 段覆盖的篇目并不重合。**
   两段都是文档写了的，但没有一段是完整的——必须**两边都查、再做差**。
2. **报错句的谓语不一定是你以为的那个词。** 「集合未定义」的报错原文可能写的是
   `does not exist`，按 `is not defined` 去搜是零命中。
   **「我没找到」的原因，要先分清是「我的模式不对」还是「文档真没有」。**
3. **同一个谓语，不一定是同一条规矩。** `belong to the same test processor`
   这一个谓语底下可能压着三条不同的规矩（环回 pin / Smart Scale 搜索 /
   内存池化），**三个主语、三个条件、三个出处**。
   **判据的键名要写到「主语 + 条件」这一级，只写到谓语就会合并。**

---

### 2.5 `mapping` — 映射页

**目录**：`wiki/mappings/`
**三层对照表：** GUI 操作 ↔ 产物文件 ↔ L1 命令 ↔ L2 API ↔ L3 接口。

**为什么必须有**：文档把 GUI、文件格式、命令分三套写，**从来没人把它们对齐过**。
agent 做全栈自动化，最缺的就是这张表。

**格式**：

| 目的 | GUI 操作 | 文件 | L1 命令 | L2 API | L3 接口 |
|---|---|---|---|---|---|

一格没有对应物就写 `—`，不确定就写 `?`，**不许猜**。

**命名**：按阶段，`mapping-<stage>.md`。**必填 `layer` + `stage`；`layer` 填 `n/a`**——
对照表本身不属于任何一层接口，`n/a` 就是为这种情况留的值。

#### 证据必须分档写明

**这是 mapping 页最容易做假的地方**：表格长得对称，很容易「看着像就填上」。
所以每页都要有一节把证据分成三档，逐格说清它属于哪一档：

- **① 文档明说对应**——文档里有一句话**直接声明**了跨层对应。
  例：pin 配置文件「contains a set of firmware commands `corresponding exactly to`
  the parameters specified within the Pin Configuration tool」。
  **这一档最硬，但很少。**
- **② 文档之间有链接**——GUI 文档链到了命令/API 文档。**必须写清这档的强度**：
  一条链接**只证明「那篇文档认为读者该去看这一篇」，不证明两个东西等价**——
  可能是「见也」、可能是「区别在这里」、可能是「前提」。
- **③ 只有单侧**——只有命令侧或只有 GUI 侧有材料。
  **这一档对面那格写 `?`，不写 `—`**（`?` = 本页没找到证据；`—` = 这一层不存在这个对应物）。
  两者**不许混用**：`—` 是**结论**，得给得出理由。

> **取②档证据之前，必须先剔「跨章重复投放」。**
> 文档会把同一篇页投放在多个章下。不剔重，那些「GUI 文档 → 命令文档」的链接
> 可能是同一篇文档链它自己的另一份投放——**假证据**。
> 判据与处理见 §9「重复投放」。

---

### 2.6 `error` — 排错页

**目录**：`wiki/errors/`
报错信息、症状、边界条件、限制。来源是文档里的 `Errors` / `Warnings` / `Limits` 段落。

**每页从症状写起**（「看到这个报错」），不是从原因写起——
**agent 是拿着症状来查的。**

---

### 2.7 `version` — 版本页

**目录**：`wiki/versions/`
**这个功能哪个版本引入、哪个版本废弃。**

**为什么重要**：agent 需要知道「这台 7.10.3 的机台到底支不支持这个做法」，
防止它推荐一个当前版本还没有的功能。

**按产品线 + 版本号组织，文件名是 `<产品>-<版本>.md`**（`smartest-7.10.3.md`、`mtp-3.4.0.md`…）。

**产品前缀不是可选项**：`Functional changes` 里不止 SmarTest 一条产品线，
同一个版本号可能**同时属于两个产品**。只写 `7.10.3.md` 会撞名，而且撞得看不出来。

**每页两类小节**，条目**原样转录、不重写**：

- **这一版改了什么** —— 文档里的 `- <产品> X.Y.Z: <变更>` 行。
- **这一版新引入** —— 文档里的 `- Introduced in <产品> X.Y.Z` 行。

**页面里不写的东西**：不写「这些变更合起来意味着什么」。
那是解释，不是文档事实；而且**是可选的**——脚本能产出的内容不许再让 LLM 补一段散文。

**三条硬约束：**

1. **`Introduced before SmarTest 6.3.2` 不许当成「6.3.2 的变更」。**
   那是一个哨兵值，意思是「在文档集覆盖范围开始之前就已经有了」。
   该页单列一节说明，**不逐条铺开**。
2. **`sources:` 只列前 30 篇**，页里明说完整出处是正文每条后面的链接。
   这是一处有意的偏离：某些版本涉及数百篇文档，逐篇列进 frontmatter
   会把正文推到很远——**而每一条后面本来就挂着自己的出处**。
   偏离的理由写在页里，不是漏列。
3. **不列 `related:`。** 版本页与对象页的关系是**单向**的：
   对象页的 `## 版本` 段会指到版本页，而版本页**不该**回指那数百篇——
   那是把目录树镜像回来（§3）。

**目录页是 `wiki/versions/index-versions.md`**（不叫 `index.md`——理由见 §4「slug 唯一性」），
按产品线列「版本 | 条目 | 涉及文档 | 页」，由脚本生成。

**每页只说明「文档这么写」，不说明「机台这样」**（§10）。
版本页的价值恰恰在于**它不解释**：它只是把条目按版本摊开，
让 agent 或人能一眼看到某个版本动了什么。

> **怪版本号是文档自带的，照原样成页。** 分组时需要归一的，正文仍原样印，
> 并把归一过的每一处打印出来——**不许悄悄替文档改字**；
> 抽不出版本号的条目要进单独的未分类清单，**没有静默丢掉**。

---

## 3. 什么不进 wiki

**这一节和「什么进」同等重要。**

- ❌ **不建 `source` 页。** 不搞「一篇原始文档一页」。
  那样做就是镜像目录树——这正是上一版 wiki 失败的原因。
  **raw 层本身就是 source**，用 frontmatter 的 `sources:` 指回去即可。
- ❌ **不抄原文。** 转述，然后指回 raw。wiki 的价值是**组织和关联**，不是复制。
- ❌ **不为每篇 raw 文档建页。** 页是从问题长出来的，不是从文件长出来的。
- ❌ **不写流程到非 `stage` 页里。**
- ❌ **不写没出处的话。** 每句断言都要有 `sources:`。
- ❌ **不把「文档里写着」说成「机台支持」。** 见 §10。

---

## 4. 命名规范

**目录与 slug：**

- **object 页**：`<name>.md`，例：`dfpn.md`、`psfc.md`、`sqst.md`（L1 命令）、
  `smartvec.md`（L2 API）、`change-device.md`（L3 接口）
- **文件格式对象页**：`<name>-file.md`，例：`pin-configuration-file.md`
- **stage 页**：阶段名，例：`pin.md`、`level.md`
- **concept 页**：描述性名词短语，例：`ganging.md`、`wavetable.md`
- **constraint 页**：`<主体>-requires-<前置>`，例：`dfpn-requires-sequencer-off.md`
- **mapping 页**：按阶段命名，例：`mapping-pin.md`
- **error 页**：按症状命名，例：`error-sequencer-not-off.md`
- **version 页**：`<产品>-<版本>.md`，例：`smartest-7.10.3.md`

**中文标题可以有，文件名必须是 ASCII。** 中文文件名会让 wikilink 和检索都不稳定。

**stage 名是保留 slug。** 对象页与九页撞名时**加限定词**（本例取 `-object`）：
例如 L2 的 `PATTERN` 类 → `[[pattern-object]]`，与 stage 页 `[[pattern]]` 区分。
**不改 stage 名**（脊椎改名要动全库）。

> **指错比重复更坏：重复页看得见，指错看不见。**

#### slug 唯一性

**文件名（stem）就是页面的身份，全库不许有两个文件共用一个 stem。**

这不是美学，是**机器事实**：凡判「这个页存不存在」的地方一律按 stem 建集合。
两个文件同一个 stem，**集合把它们当同一个东西**，谁遮谁取决于遍历顺序，
**而且没有任何一处会报错**。

- 版本目录的索引页必须叫 `index-versions.md`，不能叫 `index.md`——
  后者会与根 `index.md` 共用 stem。
- 子索引一律用 `index-<类型>.md`，这个名字不会与任何类型页撞。

#### 文件名小写，正文保留原大小写

两条规矩看着矛盾，分工是：

- **文件名（slug）一律小写 + 连字符。** `[[dfpn]]`、`[[tmlimits]]`
- **页面正文里写原样大小写。** `DFPN` 就是 `DFPN`，`TMLimits` 就是 `TMLimits`

理由：slug 是**标识符**，要稳、要能跨平台、要不因排版习惯漂移；
正文是**给人和 agent 读的**，必须和机台、文档、代码里的写法一致。

> **按不同 slug 去建页，就会建出重复页。** 而重复页看不见——
> 检查器只对自己看得见的部分负责，所以它可能一直是绿的。

---

## 5. Frontmatter

所有页面必填：

```yaml
---
type: stage | object | concept | constraint | mapping | error | version
title: 人类可读标题
tags: []
related: []              # [[wikilink]] 目标
sources: []              # raw 相对路径，必填且至少一条
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

`object` / `constraint` / `mapping` 页额外必填：

```yaml
layer: L1 | L2 | L3 | file | gui | n/a    # 属于哪一层接口
stage: project | pin | level | timing | pattern | testmethod | testflow | run | results
```

**`stage` 填的是「最近的一段」，不是「归属」。**

允许为不属于任何一段流程的对象建页（判据是入度），而这里又要求 `stage` 必填——
两条规矩只有这一个填法能同时成立。

- 这个字段的用处是**「读者该去哪一段里找它的用法」**，填最近的一段对这个用处是对的。
- **填成「归属」会把「没人要它」的东西伪装成某一环的正式成员**，
  而那正是 §2.1「归属判定」要防的错。
- 所以：**页里要写明这是「最近」不是「归属」**，字段本身承载不了这个区别。

其余类型（`concept` / `error` / `version`）**不要求** `layer`/`stage`。
带了也合法，**但带了就得合法**——拼错的值不许一路绿到底。

**所有页额外必填：**

```yaml
verified: doc-only | tested
```

- `doc-only` — 只在 TDC 文档里确认存在
- `tested` — 在真实 93K 机台/环境上验证过

**默认一律 `doc-only`。** 改成 `tested` 必须有人或 agent 真的跑过，并在 `log.md` 留下记录。

### 5.1 `sources:` 有两个含义，所以「谁能改它」是个规矩

`sources:` 不只是给读者看的出处，它**同时是一条检查的输入**：

| 谁在读 | 读成什么意思 |
|---|---|
| 读者 | **本页内容的来源** |
| 检查器 | **「这一篇已经有页了」**——它拿 `sources:` 数「这个高入度候选有没有归宿」 |

**一个字段两个含义，于是改它就不是写作动作，而是会动检查的动作。** 三条规矩：

1. **写散文的人不许动 `sources:`。** `type` / `title` / `layer` / `stage` /
   `sources` / `created` / `verified` 原样留着。`sources:` 由建页计划决定。
2. **主会话可以加，但要同时满足两条**：
   - **页面里有一整块逐字内容来自那一篇**（否则追溯「任何一句话都要能顺着
     `sources:` 找回原文」会落空）；
   - **那一篇不是「未建页的候选」**——即它的入度低于建页门槛，或者它已经有页。
3. **绝对不许加的那一种**：入度高于门槛且还没有页的那一篇。
   加了会让检查器以为「它有人认领了」，**判据当场被掏空而报告照样绿**。

**判这条规矩的判据是入度，不是感觉。**

---

## 6. `index.md` 格式

`wiki/index.md` 是**每次查询第一个被读的文件**。

**硬约束：`index.md` 必须能塞进一个 context window（预算 < 25,000 token）。**

分节列出：

```
## 阶段（9）
## 概念
## 约束
## 映射
## 对象
## 排错 / 版本
```

每行一条：`- [[slug]] — 一句话说明`。

**子索引**放在 `index-<类型>.md`，用于条目过多的类型（对象、版本）。
子索引本身也算进预算。

**索引条目不写数字。** 页数、token 数由脚本量，不手抄。

---

## 7. `log.md` 格式

`wiki/log.md` 追加式，**正序**（新的在末尾）。前缀固定，保证可 grep。

```markdown
## [YYYY-MM-DD] ingest | <标题>
- 读了哪些 raw
- 新建/更新了哪些页
- 有没有跟已有页面冲突

## [YYYY-MM-DD] lint | <范围>
- 查到什么问题

## [YYYY-MM-DD] verify | <对象>
- 在什么环境上验证了什么，结果如何
```

---

## 8. 链接规则

- 页面间用 `[[page-slug]]`
- **`related` 从证据来，不要凭感觉编。** 文档之间的交叉引用是现成的强证据。
- 链接的三种情况要分清：
  - **交叉引用**（「相关」）→ 写进 `related:`
  - **依赖/顺序**（「必须先」）→ 必须建 `constraint` 页，不能只放个链接
  - **同层对照**（GUI ↔ 文件 ↔ 命令）→ 必须进 `mapping` 页
- 每个 `object` / `concept` 页都必须出现在 `index.md` 里
- 每个 `stage` 页都要链到前后阶段

### 8.1 只许链向「会存在的页」

`[[...]]` 只许指向**确实会存在**的目标，其余一律写成**反引号包住的名字 + 源路径**。

判据：这个目标是不是建页计划里认领过的，或者是不是文档自己声明的父子关系。

**为什么不许链别的**：建页计划只为**高入度**对象建页。给一个入度不够建页的兄弟
加 `[[...]]`，就是**亲手造一个永远不会被填上的悬空目标**——
悬空清单一旦混进噪声，就再也不能当工作单用了。

> **这条规矩的代价要写明白：** 有些「相关」就只能写成反引号，读者点不动。
> 这是故意的——**点不动但指向明确，好过点得动但那页永远不存在。**

> **解释「为什么不链这一页」的时候，也不许把那两个方括号写出来。**
> 写「本页不写 X 的链接」可以，写「本页不链 `[[X]]`」**不行**——
> 检查器按字面认，它分不清「这是引用」和「这是举例说明我不引用」。
> **判据不变的场合，就改写法；只有判据本身站不住，才改判据。**

---

## 9. 冲突与追溯

**两份源文档说法不一致时：**

0. **先查是不是同一篇被投放了两次。** 这一步漏掉，实测必然误判。
1. 先看版本——是不是 `Functional changes` 说明其中一个已废弃？是则按新版写，并在页里注明废弃版本。
2. 不是版本问题，就在该页开一个「冲突」小节，**两种说法并列写出，各自附 `sources:`**。
3. **不要自行选一个当正确答案。** 记录下来，标 `verified: doc-only`，等实机验证。

#### 重复投放

TDC 把**同一篇页**投放在多个章下：字母序命令索引、各专题章、GUI 工具章
（某些 GUI 章是命令章的**整章镜像**，序号一一对应）、用例章。

**判据：源文档标识去掉 `_2` `_3` 这类后缀后相同，就是同一篇。**

**三个后果，都是数错数的：**

1. **入度统计被灌水**——同一篇页存在 5 份，它的引用就被记 5 次。
   **按入度排的建页优先级表必须去重后再排。**
2. **`sources:` 计数虚高**——同篇列两个路径就是两条来源。
3. **「两篇文档都说 X」可能只是同一篇说了两次**——**这是最危险的**，
   它会凭空造出一个「冲突」，然后按第 2 步并列写出，**把假冲突写进页面当文档事实**。

**追溯：** wiki 里任何一句话，都要能顺着 `sources:` 找回 raw 原文。做不到的句子，删掉。

---

## 10. 领域约定

- **严格区分三种话**，并在页面上标明：
  - **文档事实** — TDC 里明确写着，附 `sources:`（默认 `verified: doc-only`）
  - **推断** — 从多处证据推出来的，必须写明推断链
  - **建议** — 工程上的推荐做法，标明是建议而非文档要求
- **「文档里有」≠「这台机器上能用」。** 接口是否存在、是否开放、权限是否允许，
  都可能不同。这是 `verified` 字段存在的理由。
- **不臆造 API。** TDC 里没有的接口，不许写进 wiki，哪怕它「应该存在」。
- **命令大小写敏感**，原样保留（`DFPN` 不是 `dfpn`）。
- **版本始终写明。** 本 wiki 面向 **SmarTest 7.10.3**。其他版本的行为差异写进 `version` 页。

### 10.1 引文规矩

页面里凡是用 `> 「…」` 或代码块**引原文**的地方，
**引号内就是原文，不是你加工过的文本**。

- **`…`、列表符 `- `、表格单元格分隔符，都算原文的一部分。**
  引文里出现 `…`，等于承认**中间有字没抄**——
  **那就不是引文，是转述：要么补全，要么去掉引号。**
- **分界**：**跨段合并不算错**（字还是连续的），**丢字符才算错**。
  原句 `the tables listed above tables` 抄成 `the tables listed above`——
  **丢了一个词，算错。**
- **规范化只许做下面这几件——这是闭合清单：**
  ① **折叠空白**（换行、缩进、行首空格全折叠成一个空格）；
  ② **剥链接标记**——源句里的某个词带着指向另一篇文档的链接，
  页面引这句时只保留可见文字（`The TEST() and …`），去掉链接标记。
  **这条是必须的**：不剥，等于**因为页面把引用做对了而扣它分**；
  ③ 去 `**` 与反引号；④ 去 `「」『』`（源里没有这两个字符）；
  ⑤ 统一破折号 `— – −` → `-`；⑥ 统一弯引号 `“”‘’` → `""''`。
  **除此以外一律不许动。** 特别是：**不许把相邻两格合成一行、不许补列表符、不许补标点。**
  前六条都是**排版差异、不承载语义**；**合成一行是加进了源里没有的结构**。
- **截取只许发生在引文块的头和尾；块内部必须连续。**
  可以从原文里**截一段**来引——截取不是「丢字符」。
  但**块中间不许跳过任何原文内容**，无论用什么写法表示跳过。
  真要跳，就**断开成两个引文块**，各自逐字，中间用散文说明跳了什么。
- **`…` / `...` 出现在引文里的唯一合法场合：原文自己就写着它。**
  例：错误信息模板 `Flag ... must be between ... and ...`。
- **引文里不插 `**` 加粗、不改大小写、不修错拼、不补标点、不合并重复词。**
  源文档自己写错的（`singel-port`、`App Centertab`、重复的 `tables`），
  **原样抄进引文，然后在旁边的散文里记一笔「原文如此」**——
  **修的是「记录」，不是「引文」**（§9：raw 一个字节都不动）。
- **没打算逐字，就别用引号。** 转述不丢人，**把转述包装成引文才是错。**

---

## 11. 演化

**schema 是因，wiki 是果。** 页面出问题，先看规格有没有说清；
规格说清了而页面没照做，才是执行问题。

**规格没回答的地方，页面作者会自己发明一个答案。** 所以：

- 发现一类反复出现的错误，先在规格里补一条判据，再改页面。
- 补判据时要问：**这条判据看不见的那部分是什么？** 报绿不等于正确。
- **口头规矩必须落成可检查的判据**，否则它只存在于记得它的人脑子里。

**一条贯穿全篇的教训：**

> 枚举式的定义漏一项，就会让本该是文档事实的东西降级成猜测；
> 检查器只对自己看得见的部分负责；一个数背后可能压着几件不同的事。
>
> **看见「✅」之前，先问：这次检查漏了什么？**
