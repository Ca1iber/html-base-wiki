---
type: object
title: Structure of a TMLimits CSV file
layer: file
stage: testmethod
tags: []
related: []
sources:
  - 02_System_reference/02.10_Data_Logging/02.10.01.08.01.01.03.01_Structure_of_a_TMLimits_CSV_file.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Structure of a TMLimits CSV file

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,590 字符逐字取自** `<02_System_reference/02.10_Data_Logging/02.10.01.08.01.01.03.01_Structure_of_a_TMLimits_CSV_file.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example

The example shown below is part of a bigger TMLimits CSV file. Only a few tests
and just one test mode are
shown:

```
"Suite name", "Test name", "Test number", "Units", "Lsl", "Usl", "Test_remarks"
"Test mode", "", "", "QA", "QA", "QA", ""
"Continuity2", "DC_CONT_P", "555", "UNIT", "-0.1", "0.1", "WalkZP"
"Continuity2", "DC_CONT_N", "565", "UNIT", "-0.1", "0.1", "WalkZP"
"DC_FreeVI", "IDD_Shutdown", "575", "uA", "-1", "6.88", "FreerunVI"
"DC_FreeVI", "IDD_FREG_PWR_ON", "585", "mA", "1", "10", "FreerunVI"
"DC_FreeVI", "FREG_OUT_PWR_ON", "595", "V", "1.6", "2.1", "FreerunVI"
"DC_FreeVI", "VDD_ALDO_PWR_ON", "605", "V", "1.25", "1.6", "FreerunVI"
"DC_FreeVI", "VDD_DREG_PWR_ON", "615", "V", "1.085", "1.315", "FreerunVI"
"ATECtrl", "ATECtrl", "625", "", "-0.1", "0.1", "ATEctrlEdl"
```

This
is the same example with an added user-defined column
"Status":

```
"Suite name", "Test name", "Test number", "Units", "Status", "Lsl", "Usl", "Test_remarks"
"Test mode", "", "", "QA" "", "QA", "QA", ""
"Continuity2", "DC_CONT_P", "555", "UNIT", "4", "-0.1", "0.1", "WalkZP"
"Continuity2", "DC_CONT_N", "565", "UNIT", "3", "-0.1", "0.1", "WalkZP"
"DC_FreeVI", "IDD_Shutdown", "575", "uA", "3", "-1", "6.88", "FreerunVI"
"DC_FreeVI", "IDD_FREG_PWR_ON", "585", "mA", "0", "1", "10", "FreerunVI"
"DC_FreeVI", "FREG_OUT_PWR_ON", "595", "V", "1", "1.6", "2.1", "FreerunVI"
"DC_FreeVI", "VDD_ALDO_PWR_ON", "605", "V", "4", "1.25", "1.6", "FreerunVI"
"DC_FreeVI", "VDD_DREG_PWR_ON", "615", "V", "2", "1.085", "1.315", "FreerunVI"
"ATECtrl", "ATECtrl", "625", "", "4", "-0.1", "0.1", "ATEctrlEdl"
```

<!-- 语法节 end -->

## 是什么

**文档事实**：TMLimits CSV 是带指定列结构的标准 CSV：字段以逗号分隔，记录以换行分隔；含两行 header，再加每个 test 一行。

**文档事实**：第一 header 行是列名；第二 header 行是每列对应的 test mode。若某列没有指定 test mode，该列的值适用于所有 test mode；若指定了 test mode，只在该 mode 被选中时使用。可指定任意多个 test mode；同一列名可因 test mode 不同而重复（例如一个 `Lsl` 列 mode 为 `QA`，另一个 `Lsl` 列 mode 为 `DT`）。key column 不能指定 test mode，也不能有多个版本。

**文档事实**：列由用户定义，大部分可选；但 TMLimits 可用的最小集合是：标识列（通常是 `Suite name` 与 `Test name`，也可用其他组合）、`Test number`、`Lsl`、`Usl`、`Units`。

**文档事实**：支持的列及其要点：
- `Limit key`：行名，任意字符串；可作为 test key。
- `Suite name`：test suite 名，默认 primary key。
- `Test name`：limits 应用的 test 名，默认 secondary key。
- `Pins`：test 应用的 pin；若存在，则作为 additional key，与 `Suite name`+`Test name` 或 `Limit key` 组合。
- `Test number`：已分配的 test number；未指定则用 `-1`。
- `Units`：test result 与 spec limits 的单位；可在不同 test mode/stage 下有多列。
- `Lsl`：lower spec limit；未填则假定 `1e23`，test 总是 fail；可多列。
- `Lsl_typ`：`GT`（必须大于 Lsl）、`GE`（大于等于，默认）、`NA`（无下限）；可多列。
- `Usl_typ`：`LT`（必须小于 Usl）、`LE`（小于等于，默认）、`NA`（无上限）；可多列。
- `Usl`：upper spec limit；未填则假定 `-1e23`，test 总是 fail；可多列。
- `Offset`：在按 limits 判定前加到 test result 上的固定值；可多列。
- `Bin_s_num`：`Bin_s_name` 指定的 software bin 号，0–32767；仅在 fail 分支有 multibin 时评估；要 multibinning 必须同时给 software 与 hardware bin 号。
- `Bin_s_name`：software bin 名；软件通常不评估，主要给人读。
- `Bin_h_num`：fail 时 hardware bin 号；仅在 fail 分支有 multibin 时评估；未填则 `-1`。
- `Bin_h_name`：hardware bin 名；通常不评估，给人读。
- `Bin_type`：`good`/`bad`；缺失默认 `bad`。
- `Bin_reprobe`：是否在此 bin 重测 device；`yes`/`no`，默认 `no`。
- `Bin_overon`：是否应用 overon 行为；`yes`/`no`，默认 `yes`，非法值也按 `yes`。
- `Test_remarks`：注释；软件不评估。
- `Exec`：是否执行该 test，`Y`/`N`。
- 另支持用户自定义列，其取值与含义由用户自行定义。

**文档事实**：key column 有优先级：`Suite name, Test name, Pins` → `Suite name, Test name`（推荐；SmarTest 自己创建 TMLimits CSV 时用这组）→ `Limit key, Pins` → `Limit key`；只有当前面的组合都不存在时，才评估后面的组合。

**推断**：因此同一文件中各 test 的唯一性由所选 key 组合保证，而不是由行号保证。

## 典型用法

**文档事实**：在 SmarTest 中创建 TMLimits test table 时，文件已含两行 header：第一行列名，第二行 test mode；可继续加行/列。源文示例（见上面语法节）只展示一个 test mode `QA`，`Units`/`Lsl`/`Usl` 列的 mode 都是 `QA`。

**文档事实**：若文件中没有 test mode 行，可在 SmarTest GUI 的最上方加一个空行，并在第一格输入 `Test mode`（不带引号；源文另一处写明大小写敏感）。

**文档事实**：可直接用任意能保存 CSV 的编辑器从零创建文件，但必须符合本页结构；TMLimits test table 的标准位置是 device directory 下的 `testtable` 子目录。

**文档事实**：示例二演示增加用户自定义列 `Status`：在 header 插入 `"Status"` 并在每行给值；该列的取值与含义由用户定义。

**文档事实**：行按 test 填写；`Suite name`/`Test name`/`Test number`/`Units`/`Lsl`/`Usl` 是最小可用集合；需要 multibin 时同时填 `Bin_s_num` 与 `Bin_h_num`；需要按 test 控制执行时用 `Exec` 的 `Y`/`N`。

## 和谁有关

- [[tmlimits]]：TMLimits 的 `LimitInfo` 大多对应 TMLimits CSV 的列。为什么：`02.07.04.01.250` 的入边直接写 “Most of the elements of LimitInfo correspond to columns in TMLimits CSV files.”
- **TMLimits test tables**：`Creating TMLimits test tables`、`Editing TMLimits test tables`、`Adding limits in a TMLimits test table` 都要求按本页结构理解列；标准存放位置是 `testtable` 子目录。
- **Saving test numbers as TMLimits CSV files / Using TMLimits to manage test numbers**：保存或从零创建 TMLimits CSV 时以本页结构为准。
- **TPT 的 test table**：`Test table of a TPT` 指向本页结构。
- **Concurrent test framework**：concurrent mode 下第一个 fail test 的 bin 信息取自 Limits file，因此受本页 bin 列定义影响。
- **TMLimits 的多 bin / overon**：`Bin_s_num`、`Bin_h_num`、`Bin_reprobe`、`Bin_overon`、`Bin_type` 对应 multibin 与 overon；`03.02.02.06.07` 说 TMLimits 可按 SW bin 定义 `Bin_overon`。
- **大量 test method 页**（Shmoo、OutputDC、Jitter*、Leakage、GeneralPMU、OperatingCurrent、DpsStatus、DpsConnectivity、Continuity、ProductionIddq、StandbyCurrent、ScanTest、SpecSearch 等）：这些页面要求 test 名出现在 test table 的 `Test name` 列，并回指本页。为什么：它们用 TMLimits 的 test name 作为查找键。
- **Generating Test Numbers**：未指定 `Test number` 时用 `-1`；test number 可手工或自动生成，源文指到该页。

## 版本

**文档事实**：`Functional changes` 只写 “Introduced in SmarTest 6.5.0”，没有列出后续变更。

## 出处

- 主源：`02_System_reference/02.10_Data_Logging/02.10.01.08.01.01.03.01_Structure_of_a_TMLimits_CSV_file.htm`（Header rows、Required/optional/supported columns、Key columns、Example、Related information、Functional changes）。
- 关系证据：`extract/objpack.py` 入边，主要来自 `02.07.04.01.250_TMLimits`、`02.10.01.08.01.01.03_Saving_test_numbers_as_TMLimits_CSV_files`、`02.10.01.08.02.01_Creating_TMLimits_test_tables`、`02.10.01.08.02.02_Editing_TMLimits_test_tables`、`02.09.02.05.03_Test_table_of_a_TPT` 等。
