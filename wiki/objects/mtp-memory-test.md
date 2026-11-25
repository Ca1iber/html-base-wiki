---
type: object
title: MTP_MEMORY_TEST
layer: L2
stage: pattern
tags: []
related: []
sources:
  - 02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17_MTP_MEMORY_TEST.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# MTP_MEMORY_TEST

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **35,664 字符逐字取自** `<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17_MTP_MEMORY_TEST.htm>` 及其子主题 `<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.01_MTP_MEMORY_TEST.addAddressFilter.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.02_MTP_MEMORY_TEST.addBitMapFileUserComments.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.03_MTP_MEMORY_TEST.enableAddressBasedResults.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.04_MTP_MEMORY_TEST.enableFailBitCount.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.05_MTP_MEMORY_TEST.execute.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.06_MTP_MEMORY_TEST.generateBitmapFile.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.07_MTP_MEMORY_TEST.getMemoryPatternNamesList.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.08_MTP_MEMORY_TEST.getMemoryPort.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.09_MTP_MEMORY_TEST.getMemoryPortNamesList.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.10_MTP_MEMORY_TEST.getPassFailResult.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.11_MTP_MEMORY_TEST.isRepairable.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.12_MTP_MEMORY_TEST.judgeAndLog.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.13_MTP_MEMORY_TEST.print.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.14_MTP_MEMORY_TEST.restrictToChannelCaptureMemorySize.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.15_MTP_MEMORY_TEST.setBitMapFileName.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.16_MTP_MEMORY_TEST.setBitMapFilePath.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.17_MTP_MEMORY_TEST.setBitmapMode.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.18_MTP_MEMORY_TEST.setFailAddressListOrdering.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.19_MTP_MEMORY_TEST.setFailListStyle.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.20_MTP_MEMORY_TEST.setFBCLimit.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.21_MTP_MEMORY_TEST.setImmediateBitmapToFile.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.22_MTP_MEMORY_TEST.setMaxFailingAddressesToLogPerPin.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.23_MTP_MEMORY_TEST.setMaxFailingAddressesToReconstructPerPin.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.24_MTP_MEMORY_TEST.setMultiPatternResultMode.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.25_MTP_MEMORY_TEST.setNumberOfFailCyclesToAcquirePerPin.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.26_MTP_MEMORY_TEST.setOptions.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.27_MTP_MEMORY_TEST.setRAAlgorithm.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.28_MTP_MEMORY_TEST.setRABeginAction.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.29_MTP_MEMORY_TEST.setRAConfigFile.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.30_MTP_MEMORY_TEST.setRACounting.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.31_MTP_MEMORY_TEST.setRAEnablingMode.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.32_MTP_MEMORY_TEST.setRAEndAction.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.33_MTP_MEMORY_TEST.setRAExecutionName.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.34_MTP_MEMORY_TEST.setRAGenerateOverlaidBfd.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.35_MTP_MEMORY_TEST.setRAResourceFaulty.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.36_MTP_MEMORY_TEST.setRAUseCountingResults.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.37_MTP_MEMORY_TEST.setResultPins.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.38_MTP_MEMORY_TEST.setStartCaptureCycle.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.39_MTP_MEMORY_TEST.setStopCaptureCycle.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.40_MTP_MEMORY_TEST.startTest.htm>`、`<02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17.41_MTP_MEMORY_TEST.waitTestDone.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Syntax

There are two kinds of syntaxes:

MTP_MEMORY_TEST(void);

This constructor creates an object for the MTP_
MEMORY_TEST() class.

MTP_MEMORY_TEST(const std::string&

resultArea
);

This constructor is used when
using the
`Hidden upload`（raw: `136161.htm`）
 algorithm in memory tests. Refer to Example 5 below or the
example in
`MTP_MEMORY_TEST.startTest()`（raw: `147155.htm`）
 for its usages.

[表] Parameter
列: Parameter | Description
行 1:
  resultArea
  Name of a result area that you have previously defined.
    
    This result area stores the error map of a functional test.

### Examples

### Example 1

Creating an MTP_MEMORY_TEST
object:

```
MTP_MEMORY_TEST memoryTest;
```

### Example 2

Executing a simple bitmapping test
method:

```
void MemoryTest::run()
{
MTP_MEMORY_TEST memoryTest;

memoryTest.enableAddressBasedResults(true).setImmediateBitmapToFile(true);

// Execution is called only for first site
ON_FIRST_INVOCATION_BEGIN();
{
CONNECT();
memoryTest.execute();
}
ON_FIRST_INVOCATION_END();

memoryTest.judgeAndLog();
}
```

### Example 3

Executing a simple bitmapping test method with fail bit count
enabled:

```
void MemoryTest::run()
{
MTP_MEMORY_TEST memoryTest;

memoryTest.enableAddressBasedResults(true).setImmediateBitmapToFile(true);
memoryTest.enableFailCount(true).
memoryTest.setFBCLimit(MTP:DEVICE,100).setFBCLimit(MTP:PIN,10)
.setFBCLimit(MTP:BANK,10);

// Execution is called only for first site
ON_FIRST_INVOCATION_BEGIN();
{
CONNECT();
memoryTest.execute();
}
ON_FIRST_INVOCATION_END();

memoryTest.judgeAndLog();
}
```

### Example 4

Executing an advanced bitmapping test method with retrieval of
the failed addresses, logging, and query between pin index and pin
name:

```
void MemoryTest::run()
{
MTP_MEMORY_TEST memoryTest;

memoryTest.enableAddressBasedResults(true);
memoryTest.setMaxFailingAddressesToReconstructPerPin(1024);
memoryTest.setFailAddressListOrdering(MTP:FAIL_CYCLE);

// Execution is called only for first site
ON_FIRST_INVOCATION_BEGIN();
{
CONNECT();
memoryTest.execute();
}
ON_FIRST_INVOCATION_END();

MTP_MEMORY_PATTERN& march6n = memoryTest.getMemroyPort("A").getMemoryPattern("march6n");
ARRAY_ADDRESSES addressList;
LONG nr_addresses;

nr_addresses = march6n.getFailingAddressList("DQ_00",1024, addressList);

// Loop over address list
for(int i = 0 ; i < nr_addresses ; i++)
{
MsgStream msg;
msg << x = << addressList[i].x << endl;
msg << y = << addressList[i].y << endl;
msg << z = << addressList[i].z << endl;
// Print out address to report window
cout << msg.c_str();
// Store address in datalog
PUT_DATALOG(msg.c_str());
}

// query dq index from pin name
String pinName = "DQ_00";
INT_VECTOR dqDC/DC power units = march6n. getDQDC/DC power unitsByPinName(pinName);
INT_VECTOR::iterator pinIter;
for (pinIter = dqDC/DC power units.begin(); pinIter != dqDC/DC power units.end(); ++pinIter) {
msg << "DQ index for pin " << pinName << " : " << *pinIter << ";" << endl;
}

// query pin name from pin index
int pinIdx = 0;
STRING_VECTOR pinNameList = march6n.getPinNameListByDQIndex(pinIdx);
if(!pinNameList.empty())
{
STRING_VECTOR::iterator pinNameIter;
for (pinNameIter = pinNameList.begin(); pinNameIter != pinNameList.end(); ++pinNameIter) {
msg << "Pin name for DQ index " << pinIdx << " : " << *pinNameIter << ";" << endl;
}
}

//generate bitmap file.
march6n.setBitMapFilePath("/data/bitmaps");
march6n.addBitMapFileUserComments("Manual Bitmap");
march6N.setBitMapFileName("march6N");
march6n.generateBitmapFile();
}
```

### Example 5

Testing with hidden-upload
algorithm

```
void SMCApiValidationTest::SMC_I_Mode()
{
std::string resultArea;
GET_TESTSUITE_NAME(resultArea);

MTP_MEMORY_TEST memoryTest(resultArea);
memoryTest.enableAddressBasedResults(true);
memoryTest.setBitmapMode(MTP::BINARY_ENCODING);

// Test Execution
ON_FIRST_INVOCATION_BEGIN();
{
CONNECT();

// define a new result area configuration set.
RESULT_AREA_CONFIG_SET resConfSet(resultArea);
// configure this result area for all pins.
RESULT_AREA_CONFIG_PINS& resConfSetPins = resConfSet.pin("@");
resConfSetPins.setErrorMapResultAreaSize(1024);

memoryTest.execute();

// Enable hidden calculation
FOR_EACH_SITE_BEGIN()
// kick off calculation thread
SMC_ARM(memoryTest);
FOR_EACH_SITE_END();
}
ON_FIRST_INVOCATION_END();
}

void SMCApiValidationTest::SMC_backgroundProcessing(MTP_MEMORY_TEST memoryTest)
{
// hidden calculation
memoryTest.judgeAndLog();
memoryTest.generateBitmapFile();
}
```

### Syntax（取自子主题 MTP_MEMORY_TEST.addAddressFilter()）

Two syntaxes are available for adding a filter with single address range, and a filter
with multiple address ranges:

MTP_MEMORY_TEST& addAddressFilter(
`MTP_ADDRESS_FILTER`（raw: `135048.htm`）
filter
)

MTP_MEMORY_TEST& addAddressFilter(
`MTP_MULTI_FILTER`（raw: `135340.htm`）
filter
)
[表]
列: Parameter | Description
行 1:
  filter
  The name of the filter which you want to use.

### Example（取自子主题 MTP_MEMORY_TEST.addAddressFilter()）

Take the test results of data bit 0 from the X-address 0 to 63, and the test results
of data bit 1 from the X-address 512 to 1024 into the bit map file. Other data bits are ignored
for the bit map
file.

```
void MemoryTest::run()
{
//Define filters
MTP_ADDRESS_FILTER filter1,filter2;
filter1.setRange(MTP::X_ADDRESS,0,63).setDbits("0", MTP::INCLUDE);
filter2.setRange(MTP::X_ADDRESS,512,1024).setDbits("1", MTP::INCLUDE);
//Add filters
MTP_MEMORY_TEST memoryTest;
memoryTest.enableAddressBasedResults(true).setImmediateBitmapToFile(true);
memoryTest.addAddressFilter(filter1).addAddressFilter(filter2);

//Execution is called only for first site
ON_FIRST_INVOCATION_BEGIN();
{
CONNECT();
memoryTest.execute();
}
ON_FIRST_INVOCATION_END();

//Test API is used for judging and logging Memory Test results.
TEST(memoryTest);
}
```

### Syntax（取自子主题 MTP_MEMORY_TEST.addBitMapFileUserComments()）

```
MTP_MEMORY_TEST& addBitMapFileUserComments(const STRING& comments)
```
[表]
列: Parameter | Description
行 1:
  comments
  Any text that you want to add as a comment to the bit fail map.
    
    The default is the list of result pins (see also `setResultPins()`（raw: `128992.htm`）).

### Example（取自子主题 MTP_MEMORY_TEST.addBitMapFileUserComments()）

To add the text "March6n Manual Filemap" to the generated bit fail map
files:

```
MTP_MEMORY_TEST memoryTest();
memoryTest.addBitMapFileUserComments("March6n Manual Filemap");
```

### Syntax（取自子主题 MTP_MEMORY_TEST.enableAddressBasedResults()）

```
MTP_MEMORY_TEST& enableAddressBasedResults(const bool status)
```
[表]
列: Parameter | Description
行 1:
  status
  This parameter is used to activate or deactivate the generation of address-based
    results:
    
    true: The test generates address-based results.
    
    false: The test does not generate address-based results.
    
    The default is false.

### Example（取自子主题 MTP_MEMORY_TEST.enableAddressBasedResults()）

Switching on address-based
results:

```
MTP_MEMORY_TEST memoryTest();
memoryTest.enableAddressBasedResults(true);
```

### Syntax（取自子主题 MTP_MEMORY_TEST.enableFailBitCount()）

```
MTP_MEMORY_TEST& enableFailBitCount(const bool status)
```
[表]
列: Parameter | Description
行 1:
  status
  Whether the overall pass/fail result is determined by the fail bit counts:
    
    true: The overall pass/fail result is determined by the fail bit
    counts. The threshold values are set by the `setFBCLimit()`（raw: `129005.htm`）
    function.
    If any of the limits set by this function is exceeded, the test fails.
    
    false: The overall pass/fail result is determined by the functional
    test result.
    
    The default is false.

### Example（取自子主题 MTP_MEMORY_TEST.enableFailBitCount()）

Switching on the fail bit count as the basis for determining the overall pass/fail
result:

```
MTP_MEMORY_TEST memoryTest();
memoryTest.enableFailBitCount(true);
```

### Syntax（取自子主题 MTP_MEMORY_TEST.execute()）

```
void execute()
```

### Example（取自子主题 MTP_MEMORY_TEST.execute()）

Enabling address-based results and executing the
test:

```
MTP_MEMORY_TEST memoryTest();
memoryTest.enableAddressBasedResults(true);
CONNECT();
memoryTest.execute();
```

### Syntax（取自子主题 MTP_MEMORY_TEST.generateBitmapFile ()）

```
void generateBitmapFile () const;
```

List of parameters

There are no parameters.

Return value

There is no return value.

### Syntax（取自子主题 MTP_MEMORY_TEST.getMemoryPatternNamesList()）

```
LONG getMemoryPatternNamesList(STRING_VECTOR& name)
```
[表]
列: Parameter | Description
行 1:
  name
  The name of an array which is used to store the retrieved memory pattern names
    which are the per pin subroutine labels for MTL.

### Example（取自子主题 MTP_MEMORY_TEST.getMemoryPatternNamesList()）

```
STRING_VECTOR pattern_names;
LONG maxPatternsNr = 0;
MTP_MEMORY_TEST memoryTest;

maxPatternsNr = memoryTest.getMemoryPatternNamesList(pattern_names);

for(int i = 0; i < maxPatternsNr; i++)
{
cout << "Memory Pattern Name: " << pattern_names[i] << endl;
string bfd_file_name = pattern_names[i];
memoryTest.getMemoryPattern(pattern_names[i]).setBitMapFileName(bfd_file_name);
}

ON_FIRST_INVOCATION_BEGIN();
{
CONNECT();
memoryTest.execute();
}
ON_FIRST_INVOCATION_END();
```

### Syntax（取自子主题 MTP_MEMORY_TEST.getMemoryPort()）

```
MTP_MEMORY_PORT& getMemoryPort (const STRING & port) const;
```
[表] Parameter
列: Parameter | Description
行 1:
  port
  A port name.

### Syntax（取自子主题 MTP_MEMORY_TEST.getMemoryPortNamesList()）

```
LONG getMemoryPortNamesList (STRING_VECTOR &port_names_list) const;
```
[表] Parameter
列: Parameter | Description
行 1:
  port_names_list
  A vector which is used to store the retrieved port names.

### Return value（取自子主题 MTP_MEMORY_TEST.getMemoryPortNamesList()）

Returns the number of the retrieved port names.

### Syntax（取自子主题 MTP_MEMORY_TEST.getPassFailResult()）

```
bool getPassFailResult(void)
```

### Example（取自子主题 MTP_MEMORY_TEST.getPassFailResult()）

Enabling address-based results, executing the test, and storing the test result in an
external
variable:

```
MTP_MEMORY_TEST memoryTest();
memoryTest.enableAddressBasedResults(true);
CONNECT();
memoryTest.execute();
bool test_result;
test_result = memoryTest.getPassFailResult();
```

### Syntax（取自子主题 MTP_MEMORY_TEST.isRepairable ()）

```
bool isRepairable () const;
```

List of parameters

There are no parameters.

### Return value（取自子主题 MTP_MEMORY_TEST.isRepairable ()）

Returns:

true: The current site is repairable.

false: The current site is not repairable.

### Syntax（取自子主题 MTP_MEMORY_TEST.judgeAndLog()）

```
void judgeAndLog () const;
```

List of parameters

There are no parameters.

Return value

There is no return value.

### Syntax（取自子主题 MTP_MEMORY_TEST.print()）

```
void print (ostream & out = std::cout) const;
```
[表] Parameter
列: Parameter | Description
行 1:
  out
  The data stream to be printed out. The default stream is
    stdout.

Return value

There is no return value.

### Syntax（取自子主题 MTP_MEMORY_TEST.restrictToChannelCaptureMemorySize()）

```
MTP_MEMORY_TEST& restrictToChannelCaptureMemorySize(const bool status)
```
[表]
列: Parameter | Description
行 1:
  status
  Whether to restrict the amount of captured data to the capacity of the channel
    memory:
    
    true: When there is no more room in the channel memory for storing
    additional captured data, the test is stopped.
    
    false: When there is no more room in the channel memory for storing
    additional captured data, the data is uploaded and the test is repeated. Data capture in
    the repeated test starts from the point where the previous test was ended.
    
    The default is false, that is, all test data is captured.

### Example（取自子主题 MTP_MEMORY_TEST.restrictToChannelCaptureMemorySize()）

To capture only as much data as the channel memory can
hold:

```
MTP_MEMORY_TEST memoryTest();
memoryTest.restrictToChannelCaptureMemorySize(true);
```

### Syntax（取自子主题 MTP_MEMORY_TEST.setBitMapFileName()）

```
MTP_MEMORY_TEST& MTP_MEMORY_TEST::setBitMapFileName (const string& name) [inherited];
```
[表] Parameter
列: Parameter | Description
行 1:
  name
  A string to name the generated BFD files. The name string can contain application
    model variables, testflow variables, and the reserved variables listed below to display
    more information in the file name, such as wafer, site, and port information. The syntax
    for using a variable in the name string is ${variable name}.
    
    ${time}: The file name will show the time at which the BFD file is
    generated.
    
    ${pattern}: The file name will show the name of the memory pattern
    (per pin subroutines generated by the MTL compiler) that the BFD file is generated
    from.
    
    ${label}: The file name will show the name of the start label where
    in the pattern to start generating the BFD file.
    
    ${port}: The file name will show the name of the port that the
    pattern belongs to.
    
    ${site}: The file name will show the site number.
    
    ${test}: The file name will show the name of the test suite.
    
    If the name string contains a variable which is an application model variable and
    that is also a testflow variable, the file name will display the value of the application
    model variable.
    
    If the name string does not contain a variable, all the BFD files will have the same name
    and the later one will overwrite the earlier one.
    
    If the string does not contain the ${time} variable, the BFD file
    generated with the execution of a test and the BFD file generated with RA if you have `enabled RA`（raw: `141513.htm`） and configured `setRAEndAction(MTP::RA_END_SAVE_BFD)`（raw: `141519.htm`） will have the same name. The later one will
    overwrite the earlier one.
    
    By default, all generated BFD files are saved to:
    device/mts/bitmap/bitmap_data. You can change the path of the BFD
    file generated with an execution of a test by using `MTP_MEMORY_TEST.setBitMapFilePath()`（raw: `128998.htm`）. But you cannot
    change the path of the BFD file generated with RA.
    
    Examples:
    
    "${time}-${label}-${pattern}-Port${port}-Site${site}"
    
    "Time${time}-Port${port}-$Lot{LOT_ID}-Cassette${CASSETTE_ID}-Wafer${WAFER_ID}-X${DIE_X}-Y${DIE_Y}"

Return value

There is no return value.

### Syntax（取自子主题 MTP_MEMORY_TEST.setBitMapFilePath()）

```
MTP_MEMORY_TEST& setBitMapFilePath(const STRING& path)
```
[表]
列: Parameter | Description
行 1:
  path
  The location where the test method stores any bit fail map files it generates.
    
    You can specify either:
    
    An absolute path
    
    A relative path based on the device directory.
    
    The default is <device
    directory>/mts/bitmap/bitmap_data/.

### Example（取自子主题 MTP_MEMORY_TEST.setBitMapFilePath()）

To specify the absolute path
/data/Bitmaps/
 as the location for
generated bit fail map
files:

```
MTP_MEMORY_TEST memoryTest();
memoryTest.setBitMapFilePath("/data/Bitmaps/");
```

### Syntax（取自子主题 MTP_MEMORY_TEST.setBitmapMode()）

```
MTP_MEMORY_TEST& setBitmapMode(const MTP::BITMAP_MODE mode)
```
[表]
列: Parameter | Description
行 1:
  mode
  The way in which the results are stored in the bit fail map file:
    
    MTP::ASCII_ENCONDING: This format is human-readable but takes up a
    lot more space than the binary format. It is useful when the bit fail map file is expected
    to be read by humans.
    
    MTP::BINARY_ENCONDING: This format cannot be read by humans but
    takes up much less space and is optimized for large amounts of data.
    
    The default is MTP::BINARY_ENCONDING.

### Example（取自子主题 MTP_MEMORY_TEST.setBitmapMode()）

Switching the bit fail map files to
ASCII:

```
MTP_MEMORY_TEST memoryTest();
memoryTest.setBitmapMode.(MTP::ASCII_ENCODING);
```

### Syntax（取自子主题 MTP_MEMORY_TEST.setFailAddressListOrdering()）

```
MTP_MEMORY_TEST& setFailAddressListOrdering(MTP::ADDRESS_LIST_ORDERING order)
```
[表]
列: Parameter | Description
行 1:
  order
  The order in which the failing addresses are output:
    
    MTP::PHYSICAL_ADDRESS (default): The failing addresses are output in
    the physical address order.
    To retrieve the failing addresses, use `MTP_MEMORY_PATTERN.getFailingAddressList()`（raw: `129061.htm`）.
    
    MTP::ORDERING_CYCLE: The failing addresses are output in the cycle
    order.
    This option is the same as MTP::FAIL_CYCLE but uses less
    memory.
    
    To retrieve the failing addresses, use `MTP_MEMORY_PATTERN.getFailingCycleAddresses()`（raw: `143926.htm`）.
    
    MTP::FAIL_CYCLE: The same as MTP::ORDERING_CYCLE,
    but consumes more memory.
    To retrieve the failing addresses, use `MTP_MEMORY_PATTERN.getFailingCycleAddressList()`（raw: `141498.htm`）.

### Example（取自子主题 MTP_MEMORY_TEST.setFailAddressListOrdering()）

Setting the list of failing addresses to be ordered by
cycles:

```
MTP_MEMORY_TEST memoryTest();
memoryTest.setFailAddressListOrdering(MTP::FAIL_CYCLE);
```

### Syntax（取自子主题 MTP_MEMORY_TEST.setFailListStyle()）

```
MTP_MEMORY_TEST& setFailListStyle(const MTP::FAILLIST_TYPE mode)
```
[表]
列: Parameter | Description
行 1:
  mode
  Whether one or two bit fail maps are generated:
    
    MTP::PASS_FAIL_ONLY: One bit fail map is generated for all results,
    irrespective of whether a 0 or 1 was expected.
    
    MTP::FAIL_FOR_0_1: Two bit fail maps are generated - one containing
    all results where a 0 was expected and another containing all results where a 1 was
    expected. The file are named "Failed_for0" and "Failed_for1", respectively.
    
    The default is MTP::PASS_FAIL_ONLY.

### Example（取自子主题 MTP_MEMORY_TEST.setFailListStyle()）

Setting the test method to generate two bit fail map
files:

```
MTP_MEMORY_TEST memoryTest();
memoryTest.setFailListStyle(MTP::FAIL_FOR_0_1);
```

### Syntax（取自子主题 MTP_MEMORY_TEST.setFBCLimit()）

```
MTP_MEMORY_TEST& set FBCLimit(MTP::FBC_DIMENSION dimension, const LONG64 limit, STRING entity = "@")
MTP_MEMORY_TEST& set FBCLimit(MTP::FBC_DIMENSION dimension, const LONG64 limit, const int index)
```
[表]
列: Parameter | Description
行 1:
  dimension
  The device dimension for which the failed bits limit applies:
    
    MTP::FBC_DEVICE: The test fails if the failed bit count for the
    entire device exceeds limit.
    
    MTP::FBC_DBIT: The test fails if the failed bit count for any data
    bit exceeds limit.
    
    MTP::FBC_BANK: The test fails if the failed bit count for any bank
    exceeds limit.
行 2:
  limit
  The maximum permissible number of failed bits. If the failed bit count for the
    specified dimension is larger than this number, the test fails.
行 3:
  entity
  A list of data bits (if dimension is
    MTP::FBC_DBIT) or banks (if dimension is
    MTP::FBC_BANK) that are considered for the pass/fail result.
    
    If any of the specified data bits or banks exceeds limit, the overall
    test result is fail. Data bits or banks that are not included in
    entity do not cause a fail when they exceed limit
    failed bits.
    
    This parameter is optional. If it is not specified, all data bits or all banks are
    compared to limit, unless an index has been specified. (That is, the
    default value is "@".)
    
    This parameter is ignored if dimension is
    MTP::FBC_DEVICE.
行 4:
  index
  An index of a data bit (if dimension is
    MTP::FBC_DBIT) or bank (if dimension is
    MTP::FBC_BANK) that is considered for the pass/fail result.
    
    This is a simplified version of using the entity parameter when you
    want to check only a single data bit or bank to determine the overall pass/fail result.
    Specifying an index for an element (data bit or bank) is the same as specifying a list
    containing only the name of that element as the entity.
    
    For example, if there are two data bits DQ01 and DQ02, these two calls are equivalent:
    
    setFBCLimit(MTP::FBC_DBIT,4,"DQ02")
    
    setFBCLimit(MTP::FBC_DBIT,4,2)
    
    This parameter is optional. If it is not specified, failed bits from all devices,
    data bits, or banks are compared to limit, unless an entity has been
    specified. (That is, the default value is -1.)

### Examples（取自子主题 MTP_MEMORY_TEST.setFBCLimit()）

### Example 1

The following example switches on the fail bit count and
specifies that the test will fail if there are more than:

1024 fail bits for the entire device

256 fail bits for at least one of the banks 1, 2, 3, and 4

128 fail bits for any single data
bit

```
MTP_MEMORY_TEST memoryTest();
memoryTest.enableFailBitCount(true);
memoryTest.setFBCLimit(MTP::FBC_DEVICE,1024).setFBCLimit(MTP::FBC_BANK,256,"1,2,3,4").setFBCLimit(MTP::FBC_DBIT,128);
```

### Example 2

You can apply this function multiple times to set multiple
simultaneous limits for the same dimension. The following example sets the test to fail is any
one data bit exceeds 32 failed bits or if data bit DQ01 or data bit DQ02 exceed 20 failed
bits:

```
MTP_MEMORY_TEST memoryTest();
memoryTest.enableFailBitCount(true);
memoryTest.setFBCLimit(MTP::FBC_DBIT,32).setFBCLimit(MTP::FBC_DBIT,20,"DQ01,DQ02");
```

### Syntax（取自子主题 MTP_MEMORY_TEST.setImmediateBitmapToFile()）

```
MTP_MEMORY_TEST& setImmediateBitmapToFile(const bool status)
```
[表]
列: Parameter | Description
行 1:
  status
  Whether a bit map file will be generated:
    
    true: The test method automatically generates a bit failmap file for
    further analysis.
    
    false: No bit fail map file is generated.
    
    The default is false.

### Example（取自子主题 MTP_MEMORY_TEST.setImmediateBitmapToFile()）

To switch on bit fail map file
generation:

```
MTP_MEMORY_TEST memoryTest();
memoryTest.setImmediateBitmapToFile(true);
```

### Syntax（取自子主题 MTP_MEMORY_TEST.setMaxFailingAddressesToLogPerPin()）

```
MTP_MEMORY_TEST& setMaxFailingAddressesToLogPerPin(const LONG64 number)
```
[表]
列: Parameter | Description
行 1:
  number
  This parameter specifies the maximum number of failing addresses that will be
    logged for each result pin.
    
    We recommend that you specify the same value in this function as in `setMaxFailingAddressesToReconstructPerPin()`（raw: `128994.htm`）.
    
    The default is to log no failing addresses (that is, the default value is 0).

### Example（取自子主题 MTP_MEMORY_TEST.setMaxFailingAddressesToLogPerPin()）

To limit the number of reconstructed addresses and of logged addresses per pin to 1024
each:

```
MTP_MEMORY_TEST memoryTest();
memoryTest. setMaxFailingAddressesToReconstructPerPin(1024). setMaxFailingAddressesToLogPerPin(1024);
```

### Syntax（取自子主题 MTP_MEMORY_TEST.setMaxFailingAddressesToReconstructPerPin()）

```
MTP_MEMORY_TEST& setMaxFailingAddressesToReconstructPerPin(const LONG64 number)
```
[表]
列: Parameter | Description
行 1:
  number
  This parameter specifies the maximum number of failing addresses that will be
    reconstructed for each result pin.
    
    Normally, there is no reason to limit that number. However, characterization and failure
    analysis may not require all addresses to be reconstructed, and in that case, limiting the
    number improves performance.
    
    The default is to reconstruct all failing addresses (that is, there is no limit when you
    do not expressly set it).

### Example（取自子主题 MTP_MEMORY_TEST.setMaxFailingAddressesToReconstructPerPin()）

To limit the number of reconstructed addresses per pin to
1024:

```
MTP_MEMORY_TEST memoryTest();
memoryTest.setMaxFailingAddressesToReconstructPerPin(1024);
```

### Syntax（取自子主题 MTP_MEMORY_TEST.setMultiPatternResultMode()）

```
MTP_MEMORY_TEST& setMultiPatternResultMode(const MTP::MULTI_PATTERN_RESULT_MODE mode);
```
[表] Parameter
列: Parameter | Description
行 1:
  mode
  The mode of generating address-based results for multiple patterns in one main
    label. The default mode is MTP::FIRST_FAILING_PATTERN.
    
    The following table lists all available modes.
[表] Available options of parameter: <mode>
列: Option | Description
行 1:
  MTP::FIRST_FAILING_PATTERN
  (Default mode) Only the first failing pattern's address-based results are generated
    and logged.
行 2:
  MTP::PER_PATTERN
  Every individual pattern's address-based result is logged and generated. And an
    additional fail bit count for all failing addresses combined from all patterns is generated
    and logged.
行 3:
  MTP::ALL_PATTERNS_COMBINED
  Combines all failing addresses of all patterns, and generates and logs a fail bit
    count, a failing address list, and a BFD file naming as the main label for these combined
    failing addresses.
    
    Note that this option dose not generate the individual BFD file, fail bit count and
    failing address list for each individual pattern.

Return value

There is no return value.

### Example（取自子主题 MTP_MEMORY_TEST.setMultiPatternResultMode()）

```
MTP_MEMORY_TEST memoryTest;

memoryTest.enableAddressBasedResults(true);
memoryTest.enableFailBitCount(true);
memoryTest.setImmediateBitmapToFile(true);

memoryTest.setMultiPatternResultMode(MTP::PER_PATTERN);
```

### Syntax（取自子主题 MTP_MEMORY_TEST.setNumberOfFailCyclesToAcquirePerPin()）

```
MTP_MEMORY_TEST& setNumberOfFailCyclesToAcquirePerPin(const LONG64 cycles)
```
[表]
列: Parameter | Description
行 1:
  cycles
  This parameter specifies how many failing cycle the test method will acquire.
    
    Normally, there is no reason to limit that number. However, characterization and failure
    analysis may require repetitive test with large patterns that often produce large numbers
    of failing cycles. In that case, limiting the number of failing cycles acquired can improve
    performance.
    
    The default is to capture all failing cycles (that is, there is no limit when you do not
    expressly set it).

### Example（取自子主题 MTP_MEMORY_TEST.setNumberOfFailCyclesToAcquirePerPin()）

To limit the number of failing cycles per pin to
1024:

```
MTP_MEMORY_TEST memoryTest();
memoryTest.setNumberOfFailCyclesToAcquirePerPin(1024);
```

### Syntax（取自子主题 MTP_MEMORY_TEST.setOptions()）

```
MTP_MEMORY_TEST& setOptions(const MTP::MTP_OPTIONSoptions);
```
[表] Parameter
列: Parameter | Description
行 1:
  options
  One option is available here, described in the next table.
[表] Available options of parameter: <options>
列: Option | Description
行 1:
  MTP::SAME_LABEL_OVER_ALL_SITES
  When start labels for every site are the same, using this option will query the
    label only once.
    
    The default behavior is querying the label for every site.

### Example（取自子主题 MTP_MEMORY_TEST.setOptions()）

```
MTP_MEMORY_TEST memoryTest();
memoryTest.setOptions(MTP::SAME_LABEL_OVER_ALL_SITES).enableAddressBasedResults(true);
```

### Syntax（取自子主题 MTP_MEMORY_TEST.setRAAlgorithm()）

```
MTP_MEMORY_TEST& setRAAlgorithm (const MTP::RA_EXECUTE_MODE & mode);
```
[表] Parameter
列: Parameter | Description
行 1:
  mode
  The default mode is
    MTP::RA_EXECUTE_ENABLE_ON_CONCURRENT_MODE.
    
    See all the modes in the table below.
[表] Available options of parameter: <mode>
列: Option | Description
行 1:
  MTP::RA_EXECUTE_DISABLE
  Does not execute the RA algorithm.
行 2:
  MTP::RA_EXECUTE_ENABLE_ON_CONCURRENT_MODE (default)
  Executes the algorithm each time when a fail map is ready.

Return value

There is no return value.

### Syntax（取自子主题 MTP_MEMORY_TEST.setRABeginAction()）

```
MTP_MEMORY_TEST& setRABeginAction (const MTP::RA_BEGIN_MODE & mode);
```
[表] Parameter
列: Parameter | Description
行 1:
  mode
  The default mode is MTP::RA_BEGIN_START.
    
    See the available modes in the following table.
[表] Available options of parameter: <mode>
列: Option | Description
行 1:
  MTP::RA_BEGIN_START (default)
  Executes the current test suite and generates a fail map to be used for redundancy
    analysis.
    
    The corresponding RA end action is `MTP::RA_END_EXECUTE`（raw: `141519.htm`）.
行 2:
  MTP::RA_BEGIN_USE_BFD
  Use this mode only when a redundancy analysis contains multiple testflows (the
    first testflow must have been set to MTP::RA_ENABLE_BEGIN by `setRAEnablingMode()`（raw: `141513.htm`）).
    
    This mode loads a fail bit map file (.bfd) that has a matching RA service ID (RA
    execution name, DUT information, and port name), and executes the current test suite:
    
    If the previous redundancy analysis indicates that the device is reparable, an overlay
    fail map is generated, which will be used for redundancy analysis.
    
    If the previous redundancy analysis indicates that the device is not reparable, this
    test suite is skipped.
    
    When using this mode, you also need to set `setRAGenerateOverlaidBfd()`（raw: `141521.htm`） to true.
    
    The corresponding RA end action is `MTP::RA_END_SAVE_BFD`（raw: `141519.htm`）.

Note
 When RA is executed on multiple test suites, the results (including RA
results) are generated on the last test suite (
RA_end
 test suite) and DUT
has to be available during execution of the last test suite. Do not specify any BIN before the

RA_end
 test suite to ensure that both the execution is not interrupted and
the results are generated correctly. For example, do not specify BIN for the false case of the

RA_begin
 or
RA_continue
 test suite. If you do, the RA
result as well as the DUT test result cannot be generated correctly and error messages could
occur.

For multisite cases, do not create
RA_continue
 test suites in
subflow branches based on pass or fail result of the previous RA test suite such as

RA_begin
 or
RA_continue
.

Return value

There is no return value.

### Syntax（取自子主题 MTP_MEMORY_TEST.setRAConfigFile()）

```
MTP_MEMORY_TEST& MTP_MEMORY_TEST (const STRING & config_file);
```
[表] Parameter
列: Parameter | Description
行 1:
  config_file
  The file path of the redundancy analysis configuration file to be used.
    
    You can specify either an absolute path or a relative path. The relative path uses the
    mts/ra/config directory in the current device directory.
    
    The file name must contain the .xml suffix.

Return value

There is no return value.

### Syntax（取自子主题 MTP_MEMORY_TEST.setRACounting()）

```
MTP_MEMORY_TEST& setRACounting (const MTP::RA_EXECUTE_MODE & mode);
```
[表] Parameter
列: Parameter | Description
行 1:
  mode
  The default mode is
    MTP::RA_EXECUTE_ENABLE_ON_CONCURRENT_MODE.
    
    See the available modes in the following table.
[表] Available options of parameter: <mode>
列: Option | Description
行 1:
  MTP::RA_EXECUTE_DISABLE
  Does not accumulate the failed cells.
行 2:
  MTP::RA_EXECUTE_ENABLE_ON_CONCURRENT_MODE (default)
  Accumulates the number of failed cells after the execution of every test suite when
    the fail map is generated.

Return value

There is no return value.

### Syntax（取自子主题 MTP_MEMORY_TEST.setRAEnablingMode()）

```
MTP_MEMORY_TEST& setRAEnablingMode (const MTP::RA_ENABLING_MODE & mode);
```
[表] Parameter
列: Parameter | Description
行 1:
  mode
  The mode to enable or disable the redundancy analysis. The default mode is
    MTP::RA_DISABLE.
    
    See the available modes in the following table.
[表] Available options of parameter: <mode>
列: Option | Description
行 1:
  MTP::RA_DISABLE (default)
  Disables redundancy analysis.
行 2:
  MTP::RA_ENABLE_STANDALONE
  Enables redundancy analysis only for the current test suite.
行 3:
  MTP::RA_ENABLE_BEGIN
  Enables redundancy analysis and the redundancy analysis will:
    
    Start from the current test suite.
    
    Continue in the subsequent test suites that have the
    MTP::RA_ENABLE_CONTINUE modes (see below).
    
    Complete in the test suite that has the MTP::RA_ENABLE_END mode (see
    below).
行 4:
  MTP::RA_ENABLE_CONTINUE
  The current test suite will continue with the redundancy analysis from the earlier
    test suites with MTP::RA_ENABLE_BEGIN or
    MTP::RA_ENABLE_CONTINUE.
行 5:
  MTP::RA_ENABLE_END
  The current test suite will finish the redundancy analysis that begins in the
    earlier test suites.

Return value

There is no return value.

### Syntax（取自子主题 MTP_MEMORY_TEST.setRAEndAction()）

```
MTP_MEMORY_TEST& setRAEndAction (const MTP::RA_END_MODE & mode);
```
[表] Parameter
列: Parameter | Description
行 1:
  mode
  The default mode is MTP::RA_END_EXECUTE.
    
    See the available modes in the following table.
[表] Available options of parameter: <mode>
列: Option | Description
行 1:
  MTP::RA_END_EXECUTE (default)
  Ends the redundancy analysis and starts repairing if the repair is specified.
    
    The corresponding RA begin action is `MTP::RA_BEGIN_START`（raw: `141518.htm`）.
行 2:
  MTP::RA_END_SAVE_BFD
  Use this mode only when a redundancy analysis contains multiple testflows (the
    first testflow has been set to MTP::RA_ENABLE_BEGIN with the `setRAEnablingMode()`（raw: `141513.htm`） function).
    
    This mode saves the newly generated overlay fail map as a fail bit map file (.bfd). The
    name of the file is the time stamp and the RA service ID (RA execution name, DUT
    information, and port name). In addition, a `BFDL file`（raw: `123515.htm`） whose
    name is the RA service ID is generated to log the path of the overlay bit map file.
    
    The corresponding RA begin action is `MTP::RA_BEGIN_USE_BFD`（raw: `141518.htm`）.
    
    Note that, to use this mode, you also need to set `setRAGenerateOverlaidBfd()`（raw: `141521.htm`） to true.

Return value

There is no return value.

### Syntax（取自子主题 MTP_MEMORY_TEST.setRAExecutionName()）

```
MTP_MEMORY_TEST& setRAExecutionName (const STRING & execution_name);
```
[表] Parameter
列: Parameter | Description
行 1:
  execution_name
  The name which you give for the test suites sharing the same redundancy
    analysis.
    
    The default name is RAStd.

Return value

There is no return value.

### Syntax（取自子主题 MTP_MEMORY_TEST.setRAGenerateOverlaidBfd()）

```
MTP_MEMORY_TEST& setRAGenerateOverlaidBfd (const bool & status);
```
[表] Parameter
列: Parameter | Description
行 1:
  status
  The status can be:
    
    true: Generates an overlay fail bit map file (.bfd) for redundancy
    analysis.
    You must set to true if a redundancy analysis contains
    multiple testflows (the first testflow has been set to
    MTP::RA_ENABLE_BEGIN with the `setRAEnablingMode()`（raw: `141513.htm`） function).
    
    false: Does not generate an overlay fail bit map file (.bfd).

Return value

There is no return value.

### Syntax（取自子主题 MTP_MEMORY_TEST.setRAResourceFaulty()）

```
MTP_MEMORY_TEST& setRAResourceFaulty(MTP::RA_RESOURCE_TYPE resource, const std::vector<int>& fail_id);
MTP_MEMORY_TEST& setRAResourceFaulty(MTP::RA_RESOURCE_TYPE resource, int fail_id);
```
[表] Parameters
列: Parameter | Description
行 1:
  resource
  The spare rows or columns that have been found out containing failed bits.
    
    The type you can input here is:
    
    MTP::RA_SPARE_ROW
    
    MTP::RA_SPARE_COL
行 2:
  fail_id (when the data type is
    vector<int>&)
  The name of a vector that has stored a series of failed spare row or column ID
    numbers.
    
    If any ID is invalid, an error message is reported.
行 3:
  fail_id (when the data type is int)
  The ID number of a failed spare row or column.
    
    If the ID is invalid, an error message is reported.

Return value

There is no return value.

### Example（取自子主题 MTP_MEMORY_TEST.setRAResourceFaulty()）

Disabling the failed spare rows and columns in each site found in a previously
executed test suite to be used for DUT
repair.

```
virtual void run()
{
MTP_MEMORY_TEST memoryTest;
memoryTest.enableAddressBasedResults(true).setImmediateBitmapToFile(true)
.setRAEnablingMode(MTP::RA_ENABLE_STANDALONE).setRAConfigFile("raConfigFile.rcf.xml")
.setRAAlgorithm(MTP::RA_EXECUTE_ENABLE_ON_CONCURRENT_MODE);

ON_FIRST_INVOCATION_BEGIN();
{
FOR_EACH_SITE_BEGIN();
{
UINT site = CURRENT_SITE_NUMBER();

vector<int>& spareFailCols = mSpareColFailInfo[site];
vector<int>& spareFailRows = mSpareRowFailInfo[site];

memoryTest.setRAResourceFaulty(MTP::RA_SPARE_COL, spareFailCols);
memoryTest.setRAResourceFaulty(MTP::RA_SPARE_ROW, spareFailRows);
}
FOR_EACH_SITE_END();

memoryTest.execute();
}
ON_FIRST_INVOCATION_END();
return;
}
```

### Syntax（取自子主题 MTP_MEMORY_TEST.setRAUseCountingResults()）

```
MTP_MEMORY_TEST& setRAUseCountingResults (const bool & status);
```
[表] Parameter
列: Parameter | Description
行 1:
  status
  The status can be:
    
    true: The RA algorithm will use the counting results calculated from
    `setRACounting()`（raw: `141524.htm`）.
    Do not set
    setRAAlgorithm(concurrent mode) with setRACounting(delay
    mode), because the concurrent RA algorithm cannot use the delayed counting
    results.
    
    false: The RA algorithm will not use the counting results calculated
    from `setRACounting()`（raw: `141524.htm`）.

List of parameters

There are no parameters.

Return value

There is no return value.

### Syntax（取自子主题 MTP_MEMORY_TEST.setResultPins()）

```
MTP_MEMORY_TEST& setResultPins(const STRING& result_pins)
```
[表]
列: Parameter | Description
行 1:
  result_pins
  A comma-separated list of pins for which the results are to be calculated. @
    specifies all pins.
    
    The default is @, that is, creating address-based results for all pins.

### Example（取自子主题 MTP_MEMORY_TEST.setResultPins()）

Setting the result pins to DQ00, DQ01, DQ02, and
DQ03:

```
MTP_MEMORY_TEST memoryTest();
memoryTest.setResultPins("DQ00,DQ01,DQ02,DQ03");
```

### Syntax（取自子主题 MTP_MEMORY_TEST.setStartCaptureCycle()）

```
MTP_MEMORY_TEST& setStartCaptureCycle(const LONG64 cycle)
```
[表]
列: Parameter | Description
行 1:
  cycle
  The number of the first cycle that is to be captured.
    
    Specifying 0 or 1 starts data capture with the first cycle.
    
    The default is to begin the data capture with the first cycle.

### Example（取自子主题 MTP_MEMORY_TEST.setStartCaptureCycle()）

To begin capturing data with the fifth
cycle:

```
MTP_MEMORY_TEST memoryTest();
memoryTest.setStartCaptureCycle(5);
```

### Syntax（取自子主题 MTP_MEMORY_TEST.setStopCaptureCycle()）

```
MTP_MEMORY_TEST& setStopCaptureCycle(const LONG64 cycle)
```
[表]
列: Parameter | Description
行 1:
  cycle
  The number of the last cycle that is to be captured.
    
    Specifying -1 sets the data capture to end after the last cycle (that is, to capture the
    cycles until the end).
    
    The default is to end the data capture after the last cycle.

### Example（取自子主题 MTP_MEMORY_TEST.setStopCaptureCycle()）

To end capturing data after cycle
1024:

```
MTP_MEMORY_TEST memoryTest();
memoryTest.setStopCaptureCycle(1024);
```

### Syntax（取自子主题 MTP_MEMORY_TEST.startTest()）

```
void startTest();
```

List of parameters

There are no parameters.

Return value

There is no return value.

### Example（取自子主题 MTP_MEMORY_TEST.startTest()）

Testing using the hidden-upload algorithm and hiding
SMC-overhead.

```
void SMCApiValidationTest::SMC_II_Mode()
{
std::string resultArea;
GET_TESTSUITE_NAME(resultArea);

MTP_MEMORY_TEST memoryTest(resultArea);
memoryTest.enableAddressBasedResults(true);
memoryTest.setBitmapMode(MTP::BINARY_ENCODING);

// Test Execution
ON_FIRST_INVOCATION_BEGIN();
{
CONNECT();

// Define a new result area configuration set.
RESULT_AREA_CONFIG_SET resConfSet(resultArea);
// Configure this result area for all pins.
RESULT_AREA_CONFIG_PINS& resConfSetPins = resConfSet.pin("@");
resConfSetPins.setErrorMapResultAreaSize(1024);

// Inform tester to execute such functional test
memoryTest.startTest();

// Enable hidden calculation
FOR_EACH_SITE_BEGIN()
// kick off calculation thread
SMC_ARM(memoryTest);
FOR_EACH_SITE_END();

// The workstation is waiting for functional test completion
memoryTest.waitTestDone();
}
ON_FIRST_INVOCATION_END();
}

void SMCApiValidationTest::SMC_backgroundProcessing(MTP_MEMORY_TEST memoryTest)
{
// Hidden calculation
memoryTest.judgeAndLog();
memoryTest.generateBitmapFile();
}
```

### Syntax（取自子主题 MTP_MEMORY_TEST.waitTestDone()）

```
void waitTestDone();
```

List of parameters

There are no parameters.

Return value

There is no return value.

### Example（取自子主题 MTP_MEMORY_TEST.waitTestDone()）

See the example in
`MTP_MEMORY_TEST.startTest()`（raw: `147155.htm`）
.

<!-- 语法节 end -->

## 是什么

**文档事实**：`MTP_MEMORY_TEST` 是 MTP 的 test method API 类，在执行 memory test 后生成 address-based results 并执行 redundancy analysis（RA），支持 multiport；该 API 仅适用于 MTP，定义在 `/opt/93000mts/mts/execution_engine/include/MtpMemoryTest.h`（`02.12.06.17`）。

**文档事实**：它有两个构造函数——`MTP_MEMORY_TEST(void)`，以及 `MTP_MEMORY_TEST(const std::string& resultArea)`；后者用于 hidden upload 算法，`resultArea` 是预先定义、用来存放 functional test error map 的结果区名（`02.12.06.17`）。

**文档事实**：成员函数覆盖执行与判定（`execute()`、`startTest()`、`waitTestDone()`、`judgeAndLog()`、`generateBitmapFile()`、`print()`）、结果查询（`getPassFailResult()`、`isRepairable()`、`getMemoryPort()`、`getMemoryPortNamesList()`、`getMemoryPatternNamesList()`）、bit fail map 生成与命名（`setImmediateBitmapToFile()`、`setBitmapMode()`、`setBitMapFileName()`、`setBitMapFilePath()`、`addBitMapFileUserComments()`、`setFailListStyle()`）、fail bit count（`enableFailBitCount()`、`setFBCLimit()`）、capture 范围与数量（`setStartCaptureCycle()`、`setStopCaptureCycle()`、`setNumberOfFailCyclesToAcquirePerPin()`、`restrictToChannelCaptureMemorySize()`）、address filter（`addAddressFilter()`）、结果 pin 与多 pattern 模式（`setResultPins()`、`setMultiPatternResultMode()`、`setOptions()`）以及冗余分析（`setRA*` 系列）；完整签名以本页「语法 / 参数」为准（`02.12.06.17`）。

**文档事实**：执行结果可分为 address-based results（失败地址表）和 bit fail map（BFD）文件；`setFailAddressListOrdering()` 的选择决定失败地址的检索接口——`MTP_MEMORY_PATTERN.getFailingAddressList()`、`getFailingCycleAddresses()` 或 `getFailingCycleAddressList()`（`02.12.06.17` 子主题 `setFailAddressListOrdering()`）。

**推断**：它是「一次 memory test 的配置 + 执行 + 结果」门面：先对对象做配置，再 `CONNECT()` 后 `execute()`，最后用 `judgeAndLog()` 判定并记录；示例 5 的 hidden upload 路径则把判定与 bitmap 生成放到 `SMC_ARM()` 的后台计算中（`02.12.06.17` Examples）。

## 典型用法

**文档事实**：最小可用的执行流程来自 Example 2（address-based results + bit fail map，示例注释说明执行只对 first site 调用）（`02.12.06.17`）：

```cpp
void MemoryTest::run()
{
MTP_MEMORY_TEST memoryTest;
memoryTest.enableAddressBasedResults(true).setImmediateBitmapToFile(true);

// Execution is called only for first site
ON_FIRST_INVOCATION_BEGIN();
{
CONNECT();
memoryTest.execute();
}
ON_FIRST_INVOCATION_END();

memoryTest.judgeAndLog();
}
```

**文档事实**：需要以 fail bit count 判定时，先 `enableFailBitCount(true)`，再用 `setFBCLimit()` 分别设 device / bank / data bit 的上限（`02.12.06.17` Example 3）。注意 Example 3 原文写作 `enableFailCount(true)` 与 `MTP:DEVICE`，与同页成员名 `enableFailBitCount()`、枚举 `MTP::FBC_DEVICE` 的拼写不一致，此处照录，使用时以参数表的拼写为准。

**文档事实**：要取失败地址时按 Example 4 组合 `enableAddressBasedResults(true)`、`setMaxFailingAddressesToReconstructPerPin()`、`setFailAddressListOrdering()`，执行后通过 `getMemoryPort(...).getMemoryPattern(...)` 取得 `MTP_MEMORY_PATTERN`，再调 `getFailingAddressList()`（`02.12.06.17`）。

**文档事实**：hidden upload 用带 `resultArea` 的构造；`execute()` 后用 `SMC_ARM(memoryTest)` 启动后台计算线程，在后台函数里 `judgeAndLog()` + `generateBitmapFile()`；等待 functional test 结束的 `startTest()` + `waitTestDone()` 写法见 `startTest()` 示例（`02.12.06.17`）。

**建议**：若只做特征化或失效分析，可用 `setMaxFailingAddressesToReconstructPerPin()`、`setMaxFailingAddressesToLogPerPin()`、`setNumberOfFailCyclesToAcquirePerPin()` 把重建/记录的地址数与失败周期数限制在分析所需范围，文档说明这些限制用于改善性能（`02.12.06.17`）。

## 和谁有关

- **MTP_MEMORY_PATTERN** — **文档事实**：该类的文档说它取回「由 `getMemoryPattern()` 指定、由 `MTP_MEMORY_TEST` 测试」的 pattern 的 fail bit / functional 结果；本页 Example 4 也是这条链路（`02.12.06.15`、`02.12.06.17`）。
- **MTP_MEMORY_PORT** — **文档事实**：`getMemoryPort()` 返回该子类；MTP 3.2.1 为 multiport 新增它，并把 `getMemoryPatternNamesList()`/`getMemoryPattern()` 从 `MTP_MEMORY_TEST` 移到 port 上（本页 Functional changes 与语法节；`02.12.06.16`）。
- **MTP_ADDRESS_FILTER / MTP_MULTI_FILTER** — **文档事实**：`addAddressFilter()` 的两个重载分别接受单地址范围 filter 与多地址范围 filter（本页语法节 `addAddressFilter()`）。
- **Setting up the MTP_MEMORY_TEST API** — **文档事实**：MTP 3.3.2 之前的版本需要按该主题完成额外配置，之后系统自动完成预设置（本页 Functional changes；`02.12.02.05.06.01.04` 入边语境）。
- **Hidden upload** — **文档事实**：带 `resultArea` 的构造函数专用于 hidden upload 算法（本页 Syntax；`02.07.10.04.05`）。
- **Address-based results API / 冗余分析 API** — **文档事实**：这两篇主题都把 `MTP_MEMORY_TEST` 列为 fundamental reading；本页 Functional changes 说明 MTP 3.2.1 起支持 multiport 与 RA（`02.12.01.10.06.02`、`02.12.01.08.08`、`02.12.01.08.09` 入边语境）。
- **MTP API Reference** — **文档事实**：该索引把本类列入 MTP API 清单（`02.12.06` 入边语境）。
- **标准 L2 test method 环境** — **文档事实**：本页示例使用 `CONNECT()`、`ON_FIRST_INVOCATION_BEGIN/END`、`SMC_ARM()`、`PUT_DATALOG()` 等接口，说明它运行在 test method 的 `run()` 中（本页 Examples）。

## 版本

**文档事实**（`02.12.06.17` 的 Functional changes）：

- Introduced in MTP 3.1.3
- MTP 3.1.6（MTP on SOC 103.3.0）：新增成员函数 `addAddressFilter()` 与 `getMemoryPatternNamesList()`。
- MTP 3.1.6（MTP on SOC 103.3.0）：新增成员函数 `setMultiPatternResultMode()`。
- MTP 3.2.1：支持 multiport 与 redundancy analysis。
- MTP 3.2.1：移除成员函数 `getMemoryPatternNamesList()` 与 `getMemoryPattern()`；由支持 multiport 的新子类 `MTP_MEMORY_PORT` 提供两个类似函数。
- MTP 3.3.2：使用 `MTP_MEMORY_TEST` API 的预设置改由系统自动完成。
- MTP 3.3.2：新增构造函数语法 `MTP_MEMORY_TEST(const std::string& resultArea)`。

注：3.1.6 新增的 `getMemoryPatternNamesList()` 在 3.2.1 又被移除，两处均按原文记录。

## 出处

- `02_System_reference/02.12_Memory_Test_Plus_7.10.2/02.12.06.17_MTP_MEMORY_TEST.htm`（主文档，含 Syntax、Examples 与 Functional changes）
- 同目录 `02.12.06.17.01`–`02.12.06.17.41`（41 个成员函数子主题，语法节逐字来源）
- `02.12.06.15_MTP_MEMORY_PATTERN.htm`、`02.12.06.16_MTP_MEMORY_PORT.htm`、`02.12.06.18_MTP_MULTI_FILTER.htm`
- `02.12.02.05.06.01.04_Setting_up_the_MTP_MEMORY_TEST_API.htm`、`02.12.01.10.06.02_Address-based_results_API.htm`、`02.12.01.08.08_APIs_for_redundancy_analysis.htm`、`02.12.01.08.09_APIs_to_support_multiport_with_MTP_MEMORY_TEST.htm`
- `02_System_reference/02.07_Test_Method_Reference/02.07.10.04.05_Hidden_upload.htm`
