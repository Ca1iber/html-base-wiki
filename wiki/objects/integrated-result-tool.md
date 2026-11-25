---
type: object
title: Integrated Result Tool
layer: gui
stage: results
tags: []
related: []
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13_Integrated_Result_Tool.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Integrated Result Tool

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **3,883 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13_Integrated_Result_Tool.htm>` 及其子主题 `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.13.03.06_CSV_Export_command_line_tool.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax（取自子主题 CSV Export command line tool）

```
CsvExport -I <input_file>[-O <output_file>] -T <report>[-F <format>][-G <grouping>][-C columns][-h]
```

All
commands options have an abbreviated and a descriptive form. (For example,
-h

or
--help
.) This table shows both forms:

[表]
列: Parameter | Description
行 1:
  -I<input_file>
    
    --input<input_file>
  The input file, including the full path.
    
    EDL and STDF files are supported. They do not have to be loaded into the Data Log
    Explorer.
行 2:
  -O<output_file>
    
    --output<output_file>
  The output CSV file, including the full path.
    
    This parameter is optional. If it is not specified, the output file is saved in the same
    location as the input file and has the same name, just with the suffix
    .csv.
行 3:
  -T<report>
    
    --reporttype<report>
  The desired summary report you want to export. Available types include:
    
    testsummary
    
    devicesummary
    
    binsummary
    
    wafersummary
行 4:
  -F<format>
    
    --reportformat<format>
  Whether you want to export the summary with horizontal or vertical formatting:
    
    h: Horizontal orientation; groups are exported in adjacent
    columns.
    
    v: Vertical orientation; groups are exported in adjacent rows (the
    default).
    
    This setting has an effect only if the exported summary is grouped. (See the
    -G parameter, below.)
    
    This is an optional parameter. If it is not specified, v is
    used.
行 5:
  -G<group>
    
    --group<group>
  Whether and how the exported summaries should be `grouped`（raw: `137336.htm`）. These grouping options are available:
    
    wafer: Group by wafer. This is available for test summaries.
    
    site: Group by wafer. This is available for test summaries.
    
    pin: Group by wafer. This is available for test summaries.
    
    binsite: Group by site. This is available for bin summaries.
    
    You can specify multiple grouping levels by separating the keywords with colons. For
    example, site:pin groups by site and pin.
    
    This is an optional parameter. If it is not specified, exported summaries are not
    grouped.
行 6:
  -C<columns>
  The columns you want the exported file to contain.
    
    <columns> is a string that contains the desired columns
    separated by colons. Each individual column is specified by these elements, separated by
    vertical bars |:
    
    Field name: The title the column has in the summary tab in SmarTest.
    
    Format: If this value is set to 0, columns with group-related statistical data are
    shown besides each other.
    This setting applies only to columns whose names begin with
    "statisticData.". It is ignored for other columns. It is also ignored when the
    -F flag is set to v.
    
    Title: The title the column has in the CSV file.
    
    For example, -C Sbin|0|softbin:Dev#|0|devices exports two columns
    to the CSV file, one containing the id of the software bin (Sbin) with the title "softbin" and
    another containing the number of tested devices (Dev#) with the title "devices".
    
    This is an optional parameter. If it is not specified, a default set of columns
    (depending on the type of summary that is exported) is included in the CSV file. The titles
    are the same as in the summary tabs in SmarTest.
行 7:
  -h
    
    --help
  Displays help information for the tool.
    
    If -h or --help are specified, any other command
    line parameters are ignored and no export is performed.

### Example（取自子主题 CSV Export command line tool）

CsvExport -I ~/datalogs/myLog.std -O ~/Analysis/CSV/testSum.csv -T testsummary
-F h -G site
: Exports the test summaries for the data log file

myLog.std
 (located in the
datalogs
 folder of your
home directory) as the file
testSum.csv
 (which is saved in the

Analysis
 folder of your home directory). The summaries are grouped by
site, and the data for each site are put into adjacent columns.

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
