---
type: object
title: SmarTest Data Formatter
layer: gui
stage: results
tags: []
related: []
sources:
  - 02_System_reference/02.10_Data_Logging/02.10.03_SmarTest_Data_Formatter.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# SmarTest Data Formatter

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **15,928 字符逐字取自** `<02_System_reference/02.10_Data_Logging/02.10.03_SmarTest_Data_Formatter.htm>` 及其子主题 `<02_System_reference/02.10_Data_Logging/02.10.03.03.07_Reprobe_data.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.03.03.11_Force_closing_out_lot_or_wafer_level_in_application_model.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.03.05.05_Version_Update_Record__VUR.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.03.05.08_Site_Description_Record__SDR.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.03.05.12_Pattern_Sequence_Record__PSR.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.03.05.27_Generic_Data_Record__GDR.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.03.05.28_Activity_Trace_Event_Record__ATER.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Examples（取自子主题 Reprobe data）

### Description

Software bin 11 is marked as a reprobe bin. If a device is tested and binned into software bin 11
(and hardware bin 1), the device will be immediately retested. If the device is retested and
binned into software bin 10 and hardware bin 0, the SBR and HBR records will show the device
binned into software bin 10 and hardware bin 0; the initial binning into software bin 11 and
hardware bin 1 is not reflected in the SBR and HBR records.

### TSR records

The TSR records reflect all tests that have been executed.
If a device is tested and then retested, the tests from both testflow executions will be
reflected in the TSR records.

### PRR records

The PART_FLG will correctly reflect the status of the
testflow execution. If a device is tested and then retested, the first PRR.PART_FLG record field
will have a 0 in bit 0 and bit 1 indicating that this is the first set of test results for the
device. The second PRR (that is associated with the retest results) will have a 1 in bit 0 if it
is a package test or a 1 in bit 1 if it is a wafer test, indicating that these are retest
results.

### PCR records

The PART_CNT field will reflect the number of devices tested
(not the number of testflow executions). The RTST_CNT field will reflect the number of devices
that have had one or more reprobes executed. The GOOD_CNT field will reflect the number of
devices that were binned into a good bin on the last testflow execution.

### Example（取自子主题 Force closing out lot or wafer level in application model）

The following example illustrates a common use of

FORCE_MODEL_LEVEL_LOGGING_COMPLETE
. It performs tests on all devices
belonging to a lot and at the end copies the finished log into a quality database. (The details
of the test are unimportant here and have been left out; the log is copied by using

EXEC_INP_CALL
 to call an external function that is assumed to perform this
task.)

To ensure that the log is properly closed before it is copied,

FORCE_MODEL_LEVEL_LOGGING_COMPLETE
 is executed just before the copying
begins. Because logs can be open simultaneously for the lot and the wafer, it is necessary to
specify which one the data formatter is to
close.

```
{ lot:
...
{ DEVICE device:
...
{ DEVICE_TEST }
...
}
...
ACTIONS
FORCE_MODEL_LEVEL_LOGGING_COMPLETE = CONST_INPUT(LOT);
EXEC_INP_CALL(push_stdf_to_database);
}
```

### Syntax（取自子主题 Version Update Record (VUR)）

[表] VUR in STDF V4/2007
列: VUR field name | Field description | Value | 93000 data source
行 1:
  UPD_NAM
  The version after STDF V4 to which this data log conforms.
  Variable-length character string.
    
    Maximum 255 characters.
  The content is taken from the `stdfVersion`（raw: `70623.htm#_70623__stdfVersion`）
    parameter.
[表] VUR in STDF V4/2007.1
列: VUR field name | Field description | Value | 93000 data source
行 1:
  UPD_CNT
  The number of UPD_NAM fields in this record.
  One-byte unsigned integer.
  
行 2:
  UPD_NAM
  An array of versions after STDF V4 to which this data log conforms.
  Array of variable-length character strings.
    
    Each array element contains a maximum of 255 characters.
  The content is based on the `stdfVersion`（raw: `70623.htm#_70623__stdfVersion`） parameter.

### Syntax（取自子主题 Site Description Record (SDR)）

[表]
列: SDR field name | Field description | Value | 93000 data source
行 1:
  HEAD_NUM
  Test head number
  One-byte unsigned integer
    
    Value = 1
  Hard-coded value
行 2:
  SITE_GRP`1)`（raw: `#fntarg_1`）
  Site group number
    (station number)
    
    If there are more than 255 sites, the group number indicates which set of 128 sites is
    described.
  One-byte unsigned integer
    
    2 = Default
  Application model variable`2)`（raw: `#_69127__fn2`）:
    SITE_GRP
    
    Data source can also be a constant value in the configuration file or a system
    environment variable.
行 3:
  SITE_CNT
  Number of active sites described in this record
  One-byte unsigned integer
  Calls the DRLNumberOfSites() test method
行 4:
  SITE_NUM
  Array of active site numbers in this record.
    For tests with more than 255 sites
    (which produce multiple SDRs), the numbering restarts with 0 in each individual SDR.
  Array of one-byte unsigned integers
  The values for this are
    0 to N-1 if using 0-based site numbers and 1 to N if using
    
    1-based site numbers (where N is the number of sites).
行 5:
  HAND_TYP
  Handler or prober type
  Variable length character string
    
    First byte is unsigned count of bytes to follow
    
    Maximum 255 bytes
    
    Length byte = 0 if missing or invalid data
  Application model variable`2)`（raw: `#_69127__fn2`）:
    HAND_TYP
    
    Data source can also be a constant value in the configuration file or a system
    environment variable.
行 6:
  HAND_ID
  Handler or prober ID
  Variable length character string
    
    First byte is unsigned count of bytes to follow
    
    Maximum 255 bytes
    
    Length byte = 0 if missing or invalid data
  Application model variable`2)`（raw: `#_69127__fn2`）:
    HAND_ID
    
    Data source can also be a constant value in the configuration file or a system
    environment variable.
行 7:
  CARD_TYP
  Probe card type
  Variable length character string
    
    First byte is unsigned count of bytes to follow
    
    Maximum 255 bytes
    
    Length byte = 0 if missing or invalid data
  Application model variable`2)`（raw: `#_69127__fn2`）:
    CARD_TYP
    
    Data source can also be a constant value in the configuration file or a system
    environment variable.
行 8:
  CARD_ID
  Probe card ID
  Variable length character string
    
    First byte is unsigned count of bytes to follow
    
    Maximum 255 bytes
    
    Length byte = 0 if missing or invalid data
  Application model variable`2)`（raw: `#_69127__fn2`）:
    CARD_ID
    
    Data source can also be a constant value in the configuration file or a system
    environment variable.
行 9:
  LOAD_TYP
  DUT board type
  Variable length character string
    
    First byte is unsigned count of bytes to follow
    
    Maximum 255 bytes
    
    Length byte = 0 if missing or invalid data
  Application model variable`2)`（raw: `#_69127__fn2`）:
    LOAD_TYP
    
    Data source can also be a constant value in the configuration file or a system
    environment variable.
行 10:
  LOAD_ID
  DUT board ID
  Variable length character string
    
    First byte is unsigned count of bytes to follow
    
    Maximum 255 bytes
    
    Length byte = 0 if missing or invalid data
  Application model variable`2)`（raw: `#_69127__fn2`）:
    LOAD_ID
    
    Data source can also be a constant value in the configuration file or a system
    environment variable.
行 11:
  DIB_TYP
  DIB board type
  Variable length character string
    
    First byte is unsigned count of bytes to follow
    
    Maximum 255 bytes
    
    Length byte = 0 if missing or invalid data
  Application model variable2:
    DIB_TYP
    
    Data source can also be a constant value in the configuration file or a system
    environment variable.
行 12:
  DIB_ID
  DIB board ID
  Variable length character string
    
    First byte is unsigned count of bytes to follow
    
    Maximum 255 bytes
    
    Length byte = 0 if missing or invalid data
  Application model variable`2)`（raw: `#_69127__fn2`）:
    DIB_ID
    
    Data source can also be a constant value in the configuration file or a system
    environment variable.
行 13:
  CABL_TYP
  Interface cable type
  Variable length character string
    
    First byte is unsigned count of bytes to follow
    
    Maximum 255 bytes
    
    Length byte = 0 if missing or invalid data
  Application model variable`2)`（raw: `#_69127__fn2`）:
    CABL_TYP
    
    Data source can also be a constant value in the configuration file or a system
    environment variable.
行 14:
  CABL_ID
  Interface cable ID
  Variable length character string
    
    First byte is unsigned count of bytes to follow
    
    Maximum 255 bytes
    
    Length byte = 0 if missing or invalid data
  Application model variable`2)`（raw: `#_69127__fn2`）:
    CABL_ID
    
    Data source can also be a constant value in the configuration file or a system
    environment variable.
行 15:
  CONT_TYP
  Handler contactor type
  Variable length character string
    
    First byte is unsigned count of bytes to follow
    
    Maximum 255 bytes
    
    Length byte = 0 if missing or invalid data
  Application model variable`2)`（raw: `#_69127__fn2`）:
    CONT_TYP
    
    Data source can also be a constant value in the configuration file or a system
    environment variable.
行 16:
  CONT_ID
  Handler contactor ID
  Variable length character string
    
    First byte is unsigned count of bytes to follow
    
    Maximum 255 bytes
    
    Length byte = 0 if missing or invalid data
  Application model variable`2)`（raw: `#_69127__fn2`）:
    CONT_ID
    
    Data source can also be a constant value in the configuration file or a system
    environment variable.
行 17:
  LASR_TYP
  Laser type
  Variable length character string
    
    First byte is unsigned count of bytes to follow
    
    Maximum 255 bytes
    
    Length byte = 0 if missing or invalid data
  Application model variable`2)`（raw: `#_69127__fn2`）:
    LASR_TYP
    
    Data source can also be a constant value in the configuration file or a system
    environment variable.
行 18:
  LASR_ID
  Laser ID
  Variable length character string
    
    First byte is unsigned count of bytes to follow
    
    Maximum 255 bytes
    
    Length byte = 0 if missing or invalid data
  Application model variable`2)`（raw: `#_69127__fn2`）:
    LASR_ID
    
    Data source can also be a constant value in the configuration file or a system
    environment variable.
行 19:
  EXTR_TYP
  Extra equipment type
  Variable length character string
    
    First byte is unsigned count of bytes to follow
    
    Maximum 255 bytes
    
    Length byte = 0 if missing or invalid data
  Application model variable`2)`（raw: `#_69127__fn2`）:
    EXTR_TYP
    
    Data source can also be a constant value in the configuration file or a system
    environment variable.
行 20:
  EXTR_ID
  Extra equipment ID
  Variable length character string
    
    First byte is unsigned count of bytes to follow
    
    Maximum 255 bytes
    
    Length byte = 0 if missing or invalid data
  Application model variable`2)`（raw: `#_69127__fn2`）:
    EXTR_ID
    
    Data source can also be a constant value in the configuration file or a system
    environment variable.

### Syntax（取自子主题 Pattern Sequence Record (PSR)）

[表]
列: PSR field name | Field description | Value | 93000 data source
行 1:
  CONT_FLAG
  Flag for the existence of PSR continuation records
  Variable-length bit-encoded field
    
    If the value is 1, there is a PSR continuation record after the current record.
    If
    the value is 0, this PSR is the last record.
  
行 2:
  PSR_INDX
  Index of the PSR record (used by STR records)
  Two-byte unsigned integer
    
    0 = missing or invalid data
  
行 3:
  PSR_NAM
  The symbolic name of the test suite to which the PSR belongs
  Variable length character string
    
    First byte is unsigned count of bytes to follow
    
    Maximum 255 bytes
    
    Length byte = 0 if missing or invalid data
  
行 4:
  OPT_FLG
  Flags that indicate the presence of optional fields and conventions for certain
    indexes.
  Variable-length bit-encoded field
  
行 5:
  
  
  Bit 0:
    
    If 0, the PAT_LBL field is present.
    
    If 1, the PAT_LBL field is missing.
  
行 6:
  
  
  Bit 1:
    
    If 0, the FILE_UID field is present.
    
    If 1, the FILE_UID field is missing.
  
行 7:
  
  
  Bit 2:
    
    If 0, the ATPG_DESC field is present.
    
    If 1, the ATPG_DESC field is missing.
  
行 8:
  
  
  Bit 3:
    
    If 0, the SRC_ID field is present.
    
    If 1, the SRC_ID field is missing.
  
行 9:
  
  
  Bit 4: The first cycle number (0 or 1)
  
行 10:
  
  
  Bit 5: The first pattern number (0 or 1)
  
行 11:
  
  
  Bit 6: The starting value of the bit position
  
行 12:
  TOTP_CNT
  The total number of patterns that comprise the scan test over all PSRs. This must
    be the same value in all PSRs for the test (initial record and continuation records).
  Two-byte unsigned integer
    
    Index between 1 and 32767
  
行 13:
  LOCP_CNT
  Count of pattern file information sets in this record
  Two-byte unsigned integer
    
    Index between 1 and 32767
  
行 14:
  PAT_BGN
  Array of cycle numbers at which the patterns begin. The number of the first cycle
    (0 or 1) is determined by bit 4 of OPT_FLG.
  Array with the dimension LOCP_CNT
    
    Each value is an eight-byte unsigned integer
  
行 15:
  PAT_END
  Array of cycle numbers at which the patterns stop
  Array with the dimension LOCP_CNT
    
    Each value is an eight-byte unsigned integer
  
行 16:
  PAT_FILE
  Array of pattern file names
  Array with the dimension LOCP_CNT
    
    Variable length character string:
    - First byte is unsigned count of bytes to
    follow
    
    - Maximum 255 bytes
    
    - Length byte = 0 if missing or invalid data
  
行 17:
  PAT_LBL
  Optional array of symbolic pattern names
  Array with the dimension LOCP_CNT
    
    Variable length character string:
    - First byte is unsigned count of bytes to
    follow
    
    - Maximum 255 bytes
    
    - Length byte = 0 if missing or invalid data
  
行 18:
  FILE_UID
  Optional array of file identifier codes
  Array with the dimension LOCP_CNT
    
    Variable length character string:
    - First byte is unsigned count of bytes to
    follow
    
    - Maximum 255 bytes
    
    - Length byte = 0 if missing or invalid data
  
行 19:
  ATPG_DESC
  Optional array of ATPG information
  Array with the dimension LOCP_CNT
    
    Variable length character string:
    - First byte is unsigned count of bytes to
    follow
    
    - Maximum 255 bytes
    
    - Length byte = 0 if missing or invalid data
  
行 20:
  SRC_ID
  Optional array of PatternInSrcFileIDs
  Array with the dimension LOCP_CNT
    
    Variable length character string:
    - First byte is unsigned count of bytes to
    follow
    
    - Maximum 255 bytes
    
    - Length byte = 0 if missing or invalid data

### Example（取自子主题 Generic Data Record (GDR)）

The following table describes a sample GDR that contains three data fields of
different data types. We are assuming that numeric data of more than one byte must begin on an
even boundary. Pad bytes are used to meet the requirements.

[表]
列: Data | Code | Alignment Requirement
行 1:
  "AB"
  10
  A variable-length character string can begin on any byte. This field will contain
    one data byte, one length byte, and two data bytes, for a total length of 4 bytes. Because
    this field begins on an even byte, the next field also begins on an even byte.
行 2:
  255
  1
  A one-byte numeric value can begin on any byte. This field contains two bytes, so
    the next field also begins on an even byte.
行 3:
  510
  5
  A two-byte numeric value must begin on an even byte. This GEN_DATA field would
    begin on an even byte; and, because the first byte is the data code, the actual numeric
    value would begin on an odd byte. This field must be preceded by a pad byte.

The byte representation for this example GDR is shown below, and is shown for sample
purposes only. The actual data representation differs between CPUs. The byte values are in
hexadecimal, with the decimal equivalents given in the byte descriptions.

[表]
列: Even byte | Odd byte | Description (with decimal values)
行 1:
  0c
  00
  Number of bytes following the header (12)
行 2:
  32
  0a
  Record type (50); record subtype (10)
行 3:
  04
  00
  Number of data fields (4)
行 4:
  0a
  02
  Character string: code (10) and length (2)
行 5:
  41
  42
  Character string: data bytes ("A" and "B")
行 6:
  01
  ff
  One-byte integer: code (1) and data (255 = 0xff)
行 7:
  00
  05
  Pad byte (0); code (5) for next field
行 8:
  fe
  01
  Two-byte signed integer (510 = 0x01fe)

### Example（取自子主题 Activity Trace Event Record (ATER)）

```
GDR Record
REC_CUSTM: ACTIVITY_TRACE_LOG
EVT_SRC: Demo2
HEAD_NUM: 0x0
SITE_NUM: 0x1
ACTIVITY: *********
[PERSPEC 1010] 240 18 0 1
[USER 2020] *********
00000000000000000000004294927948 : ####2#

shmoo_size: 1
[PERSPEC 6708282] 223 0 -39348 1145128001 1145128001
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
