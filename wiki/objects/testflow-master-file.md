---
type: object
title: Testflow master file
layer: file
stage: testflow
tags: []
related: []
sources:
  - 02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.06_Testflow_master_file.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Testflow master file

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **1,602 字符逐字取自** `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.06_Testflow_master_file.htm>` 及其子主题 `<02_System_reference/02.08_Setup_and_Result_Tools/02.08.04.32.03.06.01_Top-level_control_structures.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example

```
hp93000,testflow_master_file,0.1

testerfile: testflow

information: files/general.tfl
flags: files/general.tfl
bins: files/general.tfl
setup: files/general.tfl
VAR_Default: files/vars.tfl

GROUP group1: files/group1.tfl
VAR myvar1: files/group1.tfl
VAR myvar2: files/group1.tfl

GROUP group2: files/group2.tfl
VAR myvar3: files/group2.tfl
```

### if statement（取自子主题 Top-level control structures）

```
if @myvar = 1

group mygroup: myfile.tfl
...

endif
```

Testflow variables must be prefixed by '@'

### for loop（取自子主题 Top-level control structures）

```
for @myvar = 0; @myvar < 10 ; @myvar = @myvar + 1

group mygroup: myfile.tfl
...

endfor
```

Testflow variables must be prefixed by '@'

The
testnumber
 increment for the STDF test numbering engine can be
specified by the optional keyword
testnumber_increment = <number>
 at the
end of the
for...
 line, separated by another semicolon.

### while loop（取自子主题 Top-level control structures）

```
while @myvar <= 10

group mygroup: myfile.tfl
...

endwhile
```

Testflow variables must be prefixed by '@'

The
testnumber
 increment for the STDF test numbering engine can be
specified by the optional keyword
testnumber_increment = <number>
 at the
end of the
while...
 line, separated by a semicolon.

### repeat until loop（取自子主题 Top-level control structures）

```
repeat until @myvar = 0

group mygroup: myfile.tfl
...

endrepeat
```

Testflow variables must be prefixed by '@'

The
testnumber
 increment for the STDF test numbering engine can be
specified by the optional keyword
testnumber_increment = <number>
 in the

if
,
for
,
while
, respectively the

repeat
 section (for example, in between
if [..] endif
),
separated by a semicolon.

### Example（取自子主题 Top-level control structures）

```
WHILE @Levels <= @FullFlow
GROUP VDDchanges: VDDchanges.tfl

if @prefix_DIG == 1
GROUP DIG: DIG.tfl
endif

endwhile
```

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
