---
type: object
title: Data Logging Profiles
layer: file
stage: results
tags: []
related: []
sources:
  - 02_System_reference/02.10_Data_Logging/02.10.01.02_Data_Logging_Profiles.htm
created: 2026-11-25
updated: 2026-11-25
verified: doc-only
---

# Data Logging Profiles

<!-- 骨架由 `extract/objscaffold.py` 生成。
     「语法 / 参数」「报错条件」两节是脚本逐字抽的，**不许改**；
     其余 `（待补）` 由 LLM 补完，补完请删掉本注释。 -->

## 语法 / 参数

<!-- 语法节 begin —— 本行到 end 行之间由 `extract/objscaffold.py` 生成，**手改会在下次 `--refresh-syntax` 时消失** -->

> 本节 **53,249 字符逐字取自** `<02_System_reference/02.10_Data_Logging/02.10.01.02_Data_Logging_Profiles.htm>` 及其子主题 `<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.169.01_ProfileMgr_class.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.169.02_Profile_class.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.169.03_Rule_class.htm>`、`<02_System_reference/02.07_Test_Method_Reference/02.07.04.01.169.04_Property_class.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.01.02.06.02_Creating_or_editing_a_data_logging_profile.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.01.02.08.01_ProfileMgr_class.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.01.02.08.02_Profile_class.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.01.02.08.03_Rule_class.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.01.02.08.04_Property_class.htm>`、`<02_System_reference/02.10_Data_Logging/02.10.01.02.08.05_Data_logging_profile_API_examples.htm>`。**不是转述。**
> 脚本能产出的不许调 LLM；参数表照抄，不改写。
> 段内的内部链接已改写为 `文本`（raw: `路径`），**不再是链接**。

### Example

You can create two different data logging profiles:

A standard profile that logs only the pass/fail results of all tests.

A debug profile that logs certain details such as pin value results, first failing cycles
and so on.

If you notice a drop in yield during a production run, just activate the debug profile to
enable more detailed logging. The system will then log the results needed to understand the
reasons for the yield drop.

There is no need to toggle all relevant flags per hand or to
modify the testflow file: The flags are automatically set through the activation of the profile
with just a single mouse click.

You can even program the testflow's test methods to
monitor yield drops. If the number of failing tests exceeds a certain threshold, a simple
function call from within a test method activates the debug profile mentioned above, to change
the flag configuration on-the-fly. This way, the debug profile is activated automatically
without user intervention.

### Example（取自子主题 Creating or editing a data logging profile）

The first rule in every data logging profile contains the property

log_events_enable
. This property switches on the data logging mechanism if its
value is set to 1.

To create this rule:

In the
Test Suite or Group
,
Test Method
, and

Test Name, Num or Bin
 fields, choose
*
.

In the
Property
field, choose

log_events_enable
.

In the
Value
field, enter
1
.

Click
Add
. The new rule is created:
*.*.*. log_events_enable
= 1

### Member functions（取自子主题 ProfileMgr class）

### activateProfile
```
bool ProfileMgr::activateProfile(Profile * profile)
```

Activates
the specified profile.

Return code:
true
 upon success;

false
 otherwise.

[表] Parameter
行 1:
  profile
  The profile to activate

### activateProfile
```
Profile * ProfileMgr::activateProfile(char * filename=)
```

Loads
a profile from disk and marks it as the active profile.

Return code: Pointer to the newly
created and activated profile upon success;
0
 otherwise.

[表] Parameter
行 1:
  filename
  The file name of the profile

### createDefaultProfiles
```
bool ProfileMgr::createDefaultProfiles()
```

Creates
the default
datalog_OFF.prf
 and
datalog_ON.prf
 profiles by
creating a new
profiles/
 sub-directory under the device directory and
placing the two default profiles within it.

This function assumes that the current working
directory is "waste", meaning the appropriate target device for this action has already been
selected.

If the
profiles/
 sub-directory already exists, no action is
taken, as it is assumed that the user removed or renamed the default profiles for a good
reason.

Return code:
true
 upon success;
false
 if the
default profiles could not be created.

Parameters: none

### createProfile
```
Profile * ProfileMgr::createProfile(char * filename)
```

Creates
a new profile (assuming the profile associated with the named file does not yet exist),
registers the profile in the profile list, and returns a pointer to the newly created
profile.

If a profile object associated with this file name already exists, the object is
re-used by first reloading the profile from disk (to ensure it is up-to-date) and then returning
the pointer to the caller.

Return code: A pointer to the instance upon success; 0 if
memory could not be allocated.

[表] Parameter
行 1:
  filename
  The name of the file to load and use for creation.
    
    If this is just a file name, the file is created in the profile directory of the current
    device directory.
    
    If it is a path, it must be an absolute path.

### createProfile
```
Profile * ProfileMgr::createProfile(WildcardProfileType)
```

Creates
a profile, registers the profile in the profile list and returns a pointer to the newly created
profile.

Return code:
true
 upon success;
false

otherwise.

[表] Parameter
行 1:
  WildcardProfileType
  Always use this profile type, other types are used only internally.

### deactivateProfile
```
void ProfileMgr::deactivateProfile()
```

Deactivates
the profile that is currently active. Immediately after calling this method, any subsequent call
to
getActiveProfile()
 will result in 0 being returned.

Return code:
void

Parameters: none

### deleteProfile
```
bool ProfileMgr::deleteProfile(Profile * profile)
```

Deletes
the profile that is passed in by first deregistering it from the profile list and then freeing
the memory that was allocated to it.

Return code:
true
 upon success;

false
 otherwise.

[表] Parameter
行 1:
  profile
  The profile to delete

### freeInstance
```
void ProfileMgr::freeInstance()[static]
```

Frees
the
ProfileMgr
 instance.

Return code: void

Parameters:
none

### getActiveProfile
```
Profile * ProfileMgr::getActiveProfile()
```

Returns
a pointer to the active profile.

Return code: A pointer to the active profile upon
success; 0 otherwise.

Parameters: none

### getContext
```
Context * ProfileMgr::getContext()
```

Returns
a pointer to the active context, which is either the system context (as defined by the position
in the SmarTest testflow) or a user defined context.

Return code: A pointer to the active
context upon success; 0 otherwise.

Parameters: none

### getInstance
```
ProfileMgr * ProfileMgr::getInstance()[static]
```

Returns
a pointer to the instance.

Return code: A pointer to the instance upon success 0 if memory
could not be allocated.

Parameters: none

### getProfile
```
Profile * ProfileMgr::getProfile(char * filename)
```

Gets
an existing profile registered in the internal data of the ProfileMgr object and returns a
pointer to this profile.

Return code: A pointer to the requested profile upon success; 0
if the profile associated with this name could not be found.

[表] Parameter
行 1:
  filename
  The name of the profile

### isActiveProfileDirty
```
bool ProfileMgr::isActiveProfileDirty()
```

Returns
whether the active profile is "dirty" or not, that is, whether the profile settings in memory
are different than those on disk. The status us determined by checking the UpToDate"flag in the
dm_data shared memory structure.

Return code:
true
 if active profile is
dirty;
false
 otherwise.

Parameters: none

### readProfileDirs
```
bool ProfileMgr::readProfileDirs(int & count,char **& fileList)
```

Returns
(by reference) a list of files found in all profile directories, which is essentially a list of
strings, where each entry is an absolute path and profile name.

The list is determined by
examining which profiles are contained in the device's
profiles/

subdirectory.

The information returned by reference is owned by the ProfileMgr; the caller
does not need to worry about freeing the memory.

Return code:
true
 if a
list could be compiled,
false
 otherwise.

[表] Parameter
行 1:
  count
  The number of items in fileList
行 2:
  fileList
  The list of available files

### reloadProfile
```
bool ProfileMgr::reloadProfile(Profile * profile)
```

Reloads
a single profile from disk, if possible. This is accomplished by first testing the reload on a
clone, as the load could possibly fail and corrupt the existing data. The profile in memory
itself is only over-written by the reload if the content of the profile on disk is
valid.

Return code:
true
 if the profile could be re-loaded;

false
 if the profile content on disk was invalid.

[表] Parameter
行 1:
  profile
  The profile to reload

### reloadProfiles
```
syntax void ProfileMgr::reloadProfiles()
```

Reloads
the profiles that are currently stored in ProfileMgr from disk. After calling this method, the
profiles in memory reflect what is stored on disk.

Return code: void

Parameters:
none

### setActiveProfileDirty
```
void ProfileMgr::setActiveProfileDirty(bool dirty)
```

Sets
whether the active profile is "dirty" or not. (See the description of

isActiveProfileDirty
, above.) This setting determines the value of the "UpToDate"
setting in the dm_data shared memory.

Return code: void

[表] Parameter
行 1:
  dirty
  true = yes; false = no

### setContext
```
void ProfileMgr::setContext(Context * context)
```

Sets
the internal context reference to the value passed in. Note that no copy is performed; the
profile subsystem assumes that this reference will remain valid at all times during the
following property evaluations.

Return code: none

[表] Parameter
行 1:
  context
  The context to set

### Example（取自子主题 ProfileMgr class）

See
`Data logging profile API examples`（raw: `98360.htm`）

### Member functions（取自子主题 Profile class）

### addSelector
```
virtual void Profile::addSelector(SelectorType selector)[pure virtual]
```

Adds
a selector by combining it with the selector bitmask using the
OR
 function. A
selector is added whenever a rule contained by this profile contains a selector field (such as
group, test suite, etc.) that has a value other than "*".

Return Code: none

[表] Parameter
行 1:
  selector
  The selector to add

### clearRules
```
virtual void Profile::clearRules()[pure virtual]
```

Clears
all rules associated with this profile.

Return code: none

Parameters:
none

### clone
```
virtual Profile* Profile::clone()[pure virtual]
```

Clones
a copy of the current instance and returns it.

Return code: a pointer to the newly
allocated memory.

Parameters: none

### copy
```
virtual void Profile::copy(Profile * profile)[pure virtual]
```

This
method handles the assignment of one Profile to another. The memory that was previously
allocated to the local string members is freed and re-allocated accordingly.

Return code:
none

[表] Parameter
行 1:
  profile
  The profile to which the current instance is to be copied.

### createRule
```
virtual Rule* Profile::createRule(char * rule)[pure virtual]
```

Creates
a new rule to be associated with this profile instance and returns a pointer to the new
rule.

This variant allows the rule string to be specified during creation of the Rule
object. The rule is first registered in the rule list and is then returned to the
caller.

Return code: pointer to the newly created rule upon success; 0
otherwise.

[表] Parameter
行 1:
  rule
  the rule string to associate with the new Rule object

### createRule
```
virtual Rule* Profile::createRule()[pure virtual]
```

Creates
a new rule to be associated with this profile instance and returns a pointer to the new
rule.

The rule is first registered in the rule list and is then returned to the caller.
Ideally, the caller would then specify the context the property resides in and the name and the
value of the property.

Return code: pointer to the newly created rule upon success; 0
otherwise.

Parameters:
none

### deleteRule
```
virtual bool Profile::deleteRule(Rule * rule)[pure virtual]
```

Deletes
the rule passed in as an argument by first deregistering the rule from the list and then by
freeing (with delete) the memory allocated to it.

Return code:
true
 if
the rule was deleted successfully;
false
 if an error was encountered.

[表] Parameter
行 1:
  rule
  The rule to delete

### equals
```
virtual bool Profile::equals(Profile * profile)[pure virtual]
```

Determines
if the passed profile is equivalent to the current profile.

Return code:

true
 if the passed profile is equal to this object;
false

otherwise.

[表] Parameter
行 1:
  profile
  The profile to compare to

### getFilename
```
virtual char* Profile::getFilename()[pure virtual]
```

Returns
the profile's file name to the caller, which consists of the absolute path and the file
name.

Return code: pointer to file
name.

Parameters:
none

### getLoadTimestamp
```
virtual long int Profile::getLoadTimestamp()[pure virtual]
```

Returns
the timestamp that represents the last time that this profile was read from disk.

Return
code: Timestamp showing the last file
modification.

Parameters:
none

### getRule
```
virtual Rule* Profile::getRule(int offset)[pure virtual]
```

Gets
the rule that is located in the
offset
 position of the list, which can be used
when scanning the list with a
for
 loop.

Return code: Pointer to the rule
upon success; 0 otherwise.

[表] Parameter
行 1:
  offset
  The offset of the rule in the list

### getRuleCount
```
virtual int Profile::getRuleCount()[pure virtual]
```

Returns
the number of rules currently stored in this profile.

Return code: The number of rules
currently stored in this profile.

Parameters: none

### getSelectorBitmask
```
virtual int Profile::getSelectorBitmask()[pure virtual]
```

Returns
the value of the selector bitmask that indicates which selector fields are defined/used by the
rules that this profile
holds.

Return
code: The value of the selector bitmask.

Parameters: none

### getType
```
virtual ProfileType Profile::getType()[pure virtual]
```

Returns
this profile's type.

Return code:
none

Parameters:
none

### isReloadNeeded
```
virtual bool Profile::isReloadNeeded()[pure virtual]
```

Checks
if a reload of this profile file is necessary based on the timestamp
information.

Return
code:
true
 if a reload of this profile is needed;
false

otherwise.

Parameters: none

### isSelectorDefined
```
virtual bool Profile::isSelectorDefined(SelectorType selector)[pure virtual]
```

Determines
if at least one rule in the profile defines the specified selector, meaning a rule defining a
field that has a value other than "*".

This method is defined for performance reasons to
prevent the update of flags based on a specific selector criteria when no selectors of that type
are defined anyway.

Return code:
true
 if a at least one rule in the
profile uses the specified selector;
false
 otherwise.

Parameters:
none

### load
```
virtual bool Profile::load(char * filename)[pure virtual]
```

Loads
a profile from disk. A new Rule object is created for each successfully read rule, that is, each
rule matching the expected format of the rule syntax.

Return code:
true

upon success;
false
 if an error was encountered.

[表] Parameter
行 1:
  filename
  The file name of the file to load

### save
```
virtual bool Profile::save(char * filename)[pure virtual]
```

Saves
a profile to disk. The individual rules are written one by one in a format that corresponds to
the rule syntax.

Return code:
true
 upon success;
false

if an error was encountered.

[表] Parameter
行 1:
  filename
  The name of the file to which to save

### setRule
```
virtual bool Profile::setRule(int offset,Rule * rule)[pure virtual]
```

Sets
the rule passed in as an argument to the specified offset; this effectively overwrites the
previous contents of the memory occupied by the rule.

Return code:
true

if the rule could be successfully set;
false
 if the offset refers to
uninitialized memory.

[表] Parameters
行 1:
  offset
  The offset of the rule in the list
行 2:
  rule
  The rule to set

### setRuleMapDirty
```
virtual void Profile::setRuleMapDirty(bool dirty)[pure virtual]
```

Sets
whether the rule map is "dirty" or not, that is, whether the content of the rule map has been
modified and the rule map will therefore need updating before it is accessed again.

Return
code: none

[表] Parameter
行 1:
  dirty
  The "dirty" flag

### value
```
virtual int Profile::value(char * property)[pure virtual]
```

Returns
the value of the specified property within this profile.

This method is essentially the
heart of the rule engine that goes through the individual rules and determines the value of the
property based on those rules. The order of rule scan is important, as the first match will
always be taken.

Return code: the value of the property as an integer or

INT_MIN
 if the property was not defined in this context.

[表] Parameter
行 1:
  property
  the property string

### Example（取自子主题 Profile class）

See
`Data logging profile API examples`（raw: `98360.htm`）

### Member functions（取自子主题 Rule class）

### clone
```
virtual Rule* Rule::clone()[pure virtual]
```

Clones
a copy of the current instance and returns it.

Return code: a pointer to the newly
allocated memory.

Parameters: none

### copy
```
virtual void Rule::copy(Rule * rule)[pure virtual]
```

This
method handles the assignment of one Rule to another. The memory that was previously allocated
to the local string members is freed and re-allocated accordingly, with the help of the "set"
methods.

Return code: none

[表] Parameter
行 1:
  rule
  The rule to copy

### equals
```
virtual bool Rule::equals(Rule * rule)[pure virtual]
```

Determines
if the passed rule is equivalent to the current rule.

Return code:
true

if the passed rule is equal to this object;
false
 otherwise.

[表] Parameter
行 1:
  rule
  The rule to compare the current rule to

### getBin
```
virtual char* Rule::getBin()[pure virtual]
```

Returns
a pointer to the bin string defined by this rule, or 0 if none is defined.

Return code: a
pointer to the bin string; 0 if no bin string is defined.

Parameters: none

### getGroup
```
virtual char* Rule::getGroup()[pure virtual]
```

Returns
a pointer to the group defined by this rule, or 0 if none is defined.

Return code: a
pointer to the group string; 0 if no group string is defined

Parameters:
none

### getParentProfile
```
virtual Profile* Rule::getParentProfile()[pure virtual]
```

Returns
a pointer to the parent profile, that is, the profile that contains this rule
instance.

Return code: profile: a pointer to the parent profile

Parameters:
none

### getPropName
```
virtual char* Rule::getPropName()[pure virtual]
```

Returns
a pointer to the property name defined by this rule, or 0 if it is not defined.

Return
code: a pointer to the property name; 0 if the property name is not defined

Parameters:
none

### getPropValue
```
virtual int Rule::getPropValue()[pure virtual]
```

Returns
the value defined by this rule whenever the property is queried in a matching context, or 0 if
no property is defined.

Return code: the value of the property; 0 if the property is not
defined

Parameters: none

### getTestMethod
```
virtual char* Rule::getTestMethod()[pure virtual]
```

Returns
a pointer to the test method defined by this rule, or 0 if it is not defined.

Return code:
a pointer to the test method; 0 if the test method is not defined

Parameters:
none

### getTestName
```
virtual char* Rule::getTestName()[pure virtual]
```

Returns
a pointer to the test name defined by this rule, or 0 if it is not defined.

Return code: a
pointer to the test name; 0 if the test name is not defined

Parameters: none

### getTestNum
```
virtual char* Rule::getTestNum()[pure virtual]
```

Returns
a pointer to the test num string defined by this rule, or 0 if it is not defined.

Return
code: a pointer to the test number string; 0 if the string is not defined

Parameters:
none

### getTestSuite
```
virtual char* Rule::getTestSuite()[pure virtual]
```

Returns
a pointer to the test suite defined by this rule, or 0 if it is not defined.

Return code:
a pointer to the test suite; 0 if the test suite is not defined

Parameters:
none

### match
```
virtual bool Rule::match(Context * context,char * property)[pure virtual]
```

Checks
if the passed context and property match the internal rule expression, meaning each of the
fields that make up the rule matches.

Return code:
true
 if the context
matches the rule expression,
false
 otherwise.

[表] Parameters
行 1:
  context
  The context to match against
行 2:
  property
  The property to match against

### parse

virtual bool Rule::parse(char * ruleStr)[pure
virtual]

Parses a rule string and assigns the individual components of the string to the
corresponding member variables.

Return code:
true
 upon success;

false
 if an error was encountered.

[表] Parameter
行 1:
  ruleStr
  the rule string to parse

### setBin
```
virtual bool Rule::setBin(char * num)[pure virtual]
```

Sets
the internal bin value to the passed value if the parameter passes the validity check. New
memory is always allocated for the copy.

Return code:
true
 if the
string to be set is valid;
false
 otherwise.

[表] Parameter
行 1:
  strInr
  The string to set

### setGroup
```
virtual bool Rule::setGroup(char * group)[pure virtual]
```

Sets
the internal group value to the passed value if the parameter passes the validity check. New
memory is always allocated for the copy.

Return code:
true
 if the
string to be set is valid;
false
 otherwise.

[表] Parameter
行 1:
  strIn
  The string to set

### name

syntax

Description

Return
code: none

[表] Parameter
行 1:
  selector
  the selector to add

### setParentProfile
```
virtual void Rule::setParentProfile(Profile * parent)[pure virtual]
```

Sets
the parent (or creator) of this rule instance. Only Profile objects can be parents of Rule
objects.

Return code: void

[表] Parameter
行 1:
  parent
  The Profile object that is to be the parent of this Rule instance

### setPropName
```
virtual bool Rule::setPropName(char * name)[pure virtual]
```

Sets
the internal property name value to the passed value if the parameter passes the validity check.
New memory is always allocated for the copy.

Return code:
true
 if the
string to be set is valid;
false
 otherwise.

[表] Parameter
行 1:
  strIn
  The string to set

### setPropValue
```
virtual bool Rule::setPropValue(int value)[pure virtual]
```

Sets
the property value to the value passed in as an argument provided that the value lies within the
valid range.

Return code:
true
 if the value is in the valid range;

false
 otherwise.

[表] Parameter
行 1:
  value
  The value that is to be assigned to the property

### setTestMethod
```
virtual bool Rule::setTestMethod(char * method)[pure virtual]
```

Sets
the internal test method value to the passed value if the parameter passes the validity check.
New memory is always allocated for the copy.

Return code:
true
 if the
string to be set is valid;
false
 otherwise.

[表] Parameter
行 1:
  strIn
  The string to set

### setTestName
```
virtual bool Rule::setTestName(char * name)[pure virtual]
```

Sets
the internal test name value to the passed value if the parameter passes the validity check. New
memory is always allocated for the copy.

Return code:
true
 if the
string to be set is valid;
false
 otherwise.

[表] Parameter
行 1:
  strIn
  The string to set

### setTestNum
```
virtual bool Rule::setTestNum(char * num)[pure virtual]
```

Sets
the internal test number value to the passed value if the parameter passes the validity check.
New memory is always allocated for the copy.

Return code:
true
 if the
string to be set is valid;
false
 otherwise.

[表] Parameter
行 1:
  strInr
  The string to set

### setTestSuite
```
virtual bool Rule::setTestSuite(char * suite)[pure virtual]
```

Sets
the internal test suite value to the passed value if the parameter passes the validity check.
New memory is always allocated for the copy.

Return code:
true
 if the
string to be set is valid;
false
 otherwise.

[表] Parameter
行 1:
  strIn
  The string to set

### Example（取自子主题 Rule class）

See
`Data logging profile API examples`（raw: `98360.htm`）

### Member functions（取自子主题 Property class）

### getPropName
```
char* Property::getPropName()[inline]
```

Returns
the property name defined by this instance.

Return code: pointer to the property
name.

### isDefined

bool Property::isDefined()

Checks if the stored property
is defined in the active profile for the active context.

Return code:

true
 if the property is defined;
false

otherwise.

Parameters: none

### isDefined
```
bool Property::isDefined(char * name)[static]
```

Checks
if the passed property is defined in the active profile for the active context.

Return
code:
true
 if the property is defined;
false

otherwise.

[表] Parameter
行 1:
  name
  The name of the property to check

### Overridden bool cast operator
```
Property::operator bool()[inline]
```

Overrides the Boolean
cast operator by calling
value()
 and returning the result as a
Boolean.

Return code:
true
 if the value is non-zero;

false
 otherwise.

Parameters: none

### Overridden int cast operator
```
Property::operator int()[inline]
```

Overrides the integer
cast operator by calling
value()
 and returning the result as an
integer.

Return code: the value of the property.

Parameters: none

### setPropName
```
void Property::setPropName(char * name)
```

Sets
the internal value of the property name to the value passed in as an argument. A copy of the
string is made.

Return code: void

Parameters: none

### value

int Property::value()

Determines the value
of the property indicated by the member variable
propName
 by querying the
value within the active profile.

Return code: The value of the property specified by
member
propName
 within the active profile; 0 if the value is
unspecified.

Parameters: none

### value
```
int Property::value(char * name)[static]
```

Determines
the value of the property indicated by the passed parameter
name
 by querying
the value within the active profile.

Return code: The value of the property specified by

name
 within the active profile; 0 if the value is unspecified.

[表] Parameter
行 1:
  name
  the property name to query

### Example（取自子主题 Property class）

See
`Data logging profile API examples`（raw: `98360.htm`）

### Examples（取自子主题 Data logging profile API examples）

### Profile creation
```
// ProfileCreation.cpp
#include "tml_base.h"
extern CComModule _Module;
#include "tml_tcom.h"
#include "ProfileCreation.h"
#include "ProfileMgr.hpp"
#include "tpi_c.h" // TPI lib for GetCurrentDevice()
#include <stdio.h>
#if __GNUC__ >= 3
using namespace std;
#endif

#define PROFILE_FILENAME "ProfileTest.prf"

// This method creates and saves a sample profile programmatically.
// The profile is saved to the "profiles" subdir of the current device.

HRESULT CProfileCreation::createProfile(double _results[4])
{
ProfileMgr* mgr = ProfileMgr::getInstance();

// Create a profile and add sample rules to it:
Profile* profile = mgr->createProfile(WildcardProfileType);

// Test suite selector: AC test suites will log P/F results per pin:
profile->createRule("ts:AC* . * . * . datalog_level = 3");
profile->createRule("ts:AC* . * . * . datalog_detail = 1");

// Test method selector for a custom property: logHistogram
profile->createRule("* . evaluate* . * . logHistogram = 1");

// Test name selector: The "shortsTest" will log per pin values:
profile->createRule("* . * . name:shortsTest . datalog_level = 3");
profile->createRule("* . * . name:shortsTest . datalog_detail = 2");

// Test num selector: Log as much info as possible for test #'s 70-80:
profile->createRule("* . * . tn:70-80 . datalog_level = 3");
profile->createRule("* . * . tn:70-80 . datalog_detail = 5");

// For all other tests (*.*.*) that Do not match one of the
// above, use the following rules:
profile->createRule("* . * . * . datalog_level = 3");
profile->createRule("* . * . * . datalog_detail = 0");

// Build the filename to save:
char deviceStr[DM_MAX_DEVICE];
GetDevPath(deviceStr);
char filename[DM_MAX_DEVICE + 10 + DM_MAX_FILE + 1];
sprintf(filename, "%s/profiles/%s", deviceStr, PROFILE_FILENAME);

// Save the profile:
profile->save(filename);

return S_OK;
}
```

### Adaptive sampling
```
// SetProfile.cpp
#include "tml_base.h"
extern CComModule _Module;
#include "tml_tcom.h"
#include "SetProfile.h"
#include "ProfileMgr.hpp"
#include "tpi_c.h" // TPI lib for GetCurrentDevice()
#if __GNUC__ >= 3
using namespace std;
#endif
#define SAMPLING_ON_FILENAME "datalog_ON.prf"
#define SAMPLING_OFF_FILENAME "datalog_OFF.prf"
#define SAMPLE_SIZE 100
static int executionCount = 0;
static bool initialized = false;
static ProfileMgr* mgr = 0;
static Profile* samplingOnProfile = 0;
static Profile* samplingOffProfile = 0;

// This method shows an example of how to implement
// adaptive sampling based on an execution count
// approach. Data is only logged for every Nth device.
// Ideally, this method is called from a test suite at
// the start of a testflow.

HRESULT CSetProfile::setProfile(double _results[4])
{
// Initialize the profiles:
if (!initialized)
{
double results[4];
init(results);
}

// Only log detailed results for the Nth device:
if ((executionCount % SAMPLE_SIZE) == 0)
{
mgr->activateProfile(samplingOnProfile);
}
else
{
mgr->activateProfile(samplingOffProfile);
}

// Increment the testflow execution count:
executionCount++;

return S_OK;
}

// Initialization routine that is called only once

HRESULT CSetProfile::init(double _results[4])
{
mgr = ProfileMgr::getInstance();

// Build the filename to save:
char deviceStr[DM_MAX_DEVICE];
GetDevPath(deviceStr);
char filename[DM_MAX_DEVICE + 10 + DM_MAX_FILE + 1];

sprintf(filename, "%s/profiles/%s", deviceStr, SAMPLING_ON_FILENAME);
samplingOnProfile = mgr->createProfile(filename);

sprintf(filename, "%s/profiles/%s", deviceStr, SAMPLING_OFF_FILENAME);
samplingOffProfile = mgr->createProfile(filename);

initialized = true;

return S_OK;
}
```

### Logging by test number
```
// EdlFfcDatalog.cpp
#include "tml_base.h"
extern CComModule _Module;
#include "tml_tcom.h"
#include "EdlFfcDatalog.h"
#include "ProfileMgr.hpp"
#include "tpi_c.h" // TPI lib for GetCurrentDevice()
#if __GNUC__ >= 3
using namespace std;
#endif
#define PROFILE_FILENAME "EdlFfcDatalog.prf"

// Here is an example on how to give a test number to your
// test using the TESTSET API, which will be used by the
// profile rule engine to determine if test number specific
// logging is desired or not.

HRESULT CEdlFfcDatalog::execute(double _results[4])
{
if (profile)
{
TESTSET set;
set.testname("EdlFfcDatalog");
set.testnumber(900);

FUNCTIONAL_TEST();

// Note: Here we are calling judgeAndLog on the object 'set',
// which is associated with the test name "EdlFfcDatalog" and
// the test number 900. This information is applied by
// judgeAndLog to the active profile to determine if logging
// should be performed.
set.judgeAndLog_FunctionalTest();
}
return S_OK;
}
```

### Evaluating a custom property
```
// PropEvalBin.cpp
#include "tml_base.h"
extern CComModule _Module;
#include "tml_tcom.h"
#include "PropEvalBin.h"
#include "Property.hpp"
#if __GNUC__ >= 3
using namespace std;
#endif

// Here is a simple example of how to evaluate the value of
// a custom property based on the current execution context.
// If the profile defines the "logHistogram" property in this
// execution context, the specified rule value is returned.
// Otherwise, 0.

HRESULT CPropEvalBin::logHistogram(double _results[4])
{
Property logHistogram("logHistogram");

// Note that the following "if" call causes the profile rule engine
// to calculate the propery's value based on the current execution
// context:

if (logHistogram)
{
drawHistogram();
}
return S_OK;
}
```

### Member functions（取自子主题 ProfileMgr class）

### activateProfile
```
bool ProfileMgr::activateProfile(Profile * profile)
```

Activates
the specified profile.

Return code:
true
 upon success;

false
 otherwise.

[表] Parameter
行 1:
  profile
  The profile to activate

### activateProfile
```
Profile * ProfileMgr::activateProfile(char * filename=)
```

Loads
a profile from disk and marks it as the active profile.

Return code: Pointer to the newly
created and activated profile upon success;
0
 otherwise.

[表] Parameter
行 1:
  filename
  The file name of the profile

### createDefaultProfiles
```
bool ProfileMgr::createDefaultProfiles()
```

Creates
the default
datalog_OFF.prf
 and
datalog_ON.prf
 profiles by
creating a new
profiles/
 sub-directory under the device directory and
placing the two default profiles within it.

This function assumes that the current working
directory is "waste", meaning the appropriate target device for this action has already been
selected.

If the
profiles/
 sub-directory already exists, no action is
taken, as it is assumed that the user removed or renamed the default profiles for a good
reason.

Return code:
true
 upon success;
false
 if the
default profiles could not be created.

Parameters: none

### createProfile
```
Profile * ProfileMgr::createProfile(char * filename)
```

Creates
a new profile (assuming the profile associated with the named file does not yet exist),
registers the profile in the profile list, and returns a pointer to the newly created
profile.

If a profile object associated with this file name already exists, the object is
re-used by first reloading the profile from disk (to ensure it is up-to-date) and then returning
the pointer to the caller.

Return code: A pointer to the instance upon success; 0 if
memory could not be allocated.

[表] Parameter
行 1:
  filename
  The name of the file to load and use for creation.
    
    If this is just a file name, the file is created in the profile directory of the current
    device directory.
    
    If it is a path, it must be an absolute path.

### createProfile
```
Profile * ProfileMgr::createProfile(WildcardProfileType)
```

Creates
a profile, registers the profile in the profile list and returns a pointer to the newly created
profile.

Return code:
true
 upon success;
false

otherwise.

[表] Parameter
行 1:
  WildcardProfileType
  Always use this profile type, other types are used only internally.

### deactivateProfile
```
void ProfileMgr::deactivateProfile()
```

Deactivates
the profile that is currently active. Immediately after calling this method, any subsequent call
to
getActiveProfile()
 will result in 0 being returned.

Return code:
void

Parameters: none

### deleteProfile
```
bool ProfileMgr::deleteProfile(Profile * profile)
```

Deletes
the profile that is passed in by first deregistering it from the profile list and then freeing
the memory that was allocated to it.

Return code:
true
 upon success;

false
 otherwise.

[表] Parameter
行 1:
  profile
  The profile to delete

### freeInstance
```
void ProfileMgr::freeInstance()[static]
```

Frees
the
ProfileMgr
 instance.

Return code: void

Parameters:
none

### getActiveProfile
```
Profile * ProfileMgr::getActiveProfile()
```

Returns
a pointer to the active profile.

Return code: A pointer to the active profile upon
success; 0 otherwise.

Parameters: none

### getContext
```
Context * ProfileMgr::getContext()
```

Returns
a pointer to the active context, which is either the system context (as defined by the position
in the SmarTest testflow) or a user defined context.

Return code: A pointer to the active
context upon success; 0 otherwise.

Parameters: none

### getInstance
```
ProfileMgr * ProfileMgr::getInstance()[static]
```

Returns
a pointer to the instance.

Return code: A pointer to the instance upon success 0 if memory
could not be allocated.

Parameters: none

### getProfile
```
Profile * ProfileMgr::getProfile(char * filename)
```

Gets
an existing profile registered in the internal data of the ProfileMgr object and returns a
pointer to this profile.

Return code: A pointer to the requested profile upon success; 0
if the profile associated with this name could not be found.

[表] Parameter
行 1:
  filename
  The name of the profile

### isActiveProfileDirty
```
bool ProfileMgr::isActiveProfileDirty()
```

Returns
whether the active profile is "dirty" or not, that is, whether the profile settings in memory
are different than those on disk. The status us determined by checking the UpToDate"flag in the
dm_data shared memory structure.

Return code:
true
 if active profile is
dirty;
false
 otherwise.

Parameters: none

### readProfileDirs
```
bool ProfileMgr::readProfileDirs(int & count,char **& fileList)
```

Returns
(by reference) a list of files found in all profile directories, which is essentially a list of
strings, where each entry is an absolute path and profile name.

The list is determined by
examining which profiles are contained in the device's
profiles/

subdirectory.

The information returned by reference is owned by the ProfileMgr; the caller
does not need to worry about freeing the memory.

Return code:
true
 if a
list could be compiled,
false
 otherwise.

[表] Parameter
行 1:
  count
  The number of items in fileList
行 2:
  fileList
  The list of available files

### reloadProfile
```
bool ProfileMgr::reloadProfile(Profile * profile)
```

Reloads
a single profile from disk, if possible. This is accomplished by first testing the reload on a
clone, as the load could possibly fail and corrupt the existing data. The profile in memory
itself is only over-written by the reload if the content of the profile on disk is
valid.

Return code:
true
 if the profile could be re-loaded;

false
 if the profile content on disk was invalid.

[表] Parameter
行 1:
  profile
  The profile to reload

### reloadProfiles
```
syntax void ProfileMgr::reloadProfiles()
```

Reloads
the profiles that are currently stored in ProfileMgr from disk. After calling this method, the
profiles in memory reflect what is stored on disk.

Return code: void

Parameters:
none

### setActiveProfileDirty
```
void ProfileMgr::setActiveProfileDirty(bool dirty)
```

Sets
whether the active profile is "dirty" or not. (See the description of

isActiveProfileDirty
, above.) This setting determines the value of the "UpToDate"
setting in the dm_data shared memory.

Return code: void

[表] Parameter
行 1:
  dirty
  true = yes; false = no

### setContext
```
void ProfileMgr::setContext(Context * context)
```

Sets
the internal context reference to the value passed in. Note that no copy is performed; the
profile subsystem assumes that this reference will remain valid at all times during the
following property evaluations.

Return code: none

[表] Parameter
行 1:
  context
  The context to set

### Example（取自子主题 ProfileMgr class）

See
`Data logging profile API examples`（raw: `98360.htm`）

### Member functions（取自子主题 Profile class）

### addSelector
```
virtual void Profile::addSelector(SelectorType selector)[pure virtual]
```

Adds
a selector by combining it with the selector bitmask using the
OR
 function. A
selector is added whenever a rule contained by this profile contains a selector field (such as
group, test suite, etc.) that has a value other than "*".

Return Code: none

[表] Parameter
行 1:
  selector
  The selector to add

### clearRules
```
virtual void Profile::clearRules()[pure virtual]
```

Clears
all rules associated with this profile.

Return code: none

Parameters:
none

### clone
```
virtual Profile* Profile::clone()[pure virtual]
```

Clones
a copy of the current instance and returns it.

Return code: a pointer to the newly
allocated memory.

Parameters: none

### copy
```
virtual void Profile::copy(Profile * profile)[pure virtual]
```

This
method handles the assignment of one Profile to another. The memory that was previously
allocated to the local string members is freed and re-allocated accordingly.

Return code:
none

[表] Parameter
行 1:
  profile
  The profile to which the current instance is to be copied.

### createRule
```
virtual Rule* Profile::createRule(char * rule)[pure virtual]
```

Creates
a new rule to be associated with this profile instance and returns a pointer to the new
rule.

This variant allows the rule string to be specified during creation of the Rule
object. The rule is first registered in the rule list and is then returned to the
caller.

Return code: pointer to the newly created rule upon success; 0
otherwise.

[表] Parameter
行 1:
  rule
  the rule string to associate with the new Rule object

### createRule
```
virtual Rule* Profile::createRule()[pure virtual]
```

Creates
a new rule to be associated with this profile instance and returns a pointer to the new
rule.

The rule is first registered in the rule list and is then returned to the caller.
Ideally, the caller would then specify the context the property resides in and the name and the
value of the property.

Return code: pointer to the newly created rule upon success; 0
otherwise.

Parameters:
none

### deleteRule
```
virtual bool Profile::deleteRule(Rule * rule)[pure virtual]
```

Deletes
the rule passed in as an argument by first deregistering the rule from the list and then by
freeing (with delete) the memory allocated to it.

Return code:
true
 if
the rule was deleted successfully;
false
 if an error was encountered.

[表] Parameter
行 1:
  rule
  The rule to delete

### equals
```
virtual bool Profile::equals(Profile * profile)[pure virtual]
```

Determines
if the passed profile is equivalent to the current profile.

Return code:

true
 if the passed profile is equal to this object;
false

otherwise.

[表] Parameter
行 1:
  profile
  The profile to compare to

### getFilename
```
virtual char* Profile::getFilename()[pure virtual]
```

Returns
the profile's file name to the caller, which consists of the absolute path and the file
name.

Return code: pointer to file
name.

Parameters:
none

### getLoadTimestamp
```
virtual long int Profile::getLoadTimestamp()[pure virtual]
```

Returns
the timestamp that represents the last time that this profile was read from disk.

Return
code: Timestamp showing the last file
modification.

Parameters:
none

### getRule
```
virtual Rule* Profile::getRule(int offset)[pure virtual]
```

Gets
the rule that is located in the
offset
 position of the list, which can be used
when scanning the list with a
for
 loop.

Return code: Pointer to the rule
upon success; 0 otherwise.

[表] Parameter
行 1:
  offset
  The offset of the rule in the list

### getRuleCount
```
virtual int Profile::getRuleCount()[pure virtual]
```

Returns
the number of rules currently stored in this profile.

Return code: The number of rules
currently stored in this profile.

Parameters: none

### getSelectorBitmask
```
virtual int Profile::getSelectorBitmask()[pure virtual]
```

Returns
the value of the selector bitmask that indicates which selector fields are defined/used by the
rules that this profile
holds.

Return
code: The value of the selector bitmask.

Parameters: none

### getType
```
virtual ProfileType Profile::getType()[pure virtual]
```

Returns
this profile's type.

Return code:
none

Parameters:
none

### isReloadNeeded
```
virtual bool Profile::isReloadNeeded()[pure virtual]
```

Checks
if a reload of this profile file is necessary based on the timestamp
information.

Return
code:
true
 if a reload of this profile is needed;
false

otherwise.

Parameters: none

### isSelectorDefined
```
virtual bool Profile::isSelectorDefined(SelectorType selector)[pure virtual]
```

Determines
if at least one rule in the profile defines the specified selector, meaning a rule defining a
field that has a value other than "*".

This method is defined for performance reasons to
prevent the update of flags based on a specific selector criteria when no selectors of that type
are defined anyway.

Return code:
true
 if a at least one rule in the
profile uses the specified selector;
false
 otherwise.

Parameters:
none

### load
```
virtual bool Profile::load(char * filename)[pure virtual]
```

Loads
a profile from disk. A new Rule object is created for each successfully read rule, that is, each
rule matching the expected format of the rule syntax.

Return code:
true

upon success;
false
 if an error was encountered.

[表] Parameter
行 1:
  filename
  The file name of the file to load

### save
```
virtual bool Profile::save(char * filename)[pure virtual]
```

Saves
a profile to disk. The individual rules are written one by one in a format that corresponds to
the rule syntax.

Return code:
true
 upon success;
false

if an error was encountered.

[表] Parameter
行 1:
  filename
  The name of the file to which to save

### setRule
```
virtual bool Profile::setRule(int offset,Rule * rule)[pure virtual]
```

Sets
the rule passed in as an argument to the specified offset; this effectively overwrites the
previous contents of the memory occupied by the rule.

Return code:
true

if the rule could be successfully set;
false
 if the offset refers to
uninitialized memory.

[表] Parameters
行 1:
  offset
  The offset of the rule in the list
行 2:
  rule
  The rule to set

### setRuleMapDirty
```
virtual void Profile::setRuleMapDirty(bool dirty)[pure virtual]
```

Sets
whether the rule map is "dirty" or not, that is, whether the content of the rule map has been
modified and the rule map will therefore need updating before it is accessed again.

Return
code: none

[表] Parameter
行 1:
  dirty
  The "dirty" flag

### value
```
virtual int Profile::value(char * property)[pure virtual]
```

Returns
the value of the specified property within this profile.

This method is essentially the
heart of the rule engine that goes through the individual rules and determines the value of the
property based on those rules. The order of rule scan is important, as the first match will
always be taken.

Return code: the value of the property as an integer or

INT_MIN
 if the property was not defined in this context.

[表] Parameter
行 1:
  property
  the property string

### Example（取自子主题 Profile class）

See
`Data logging profile API examples`（raw: `98360.htm`）

### Member functions（取自子主题 Rule class）

### clone
```
virtual Rule* Rule::clone()[pure virtual]
```

Clones
a copy of the current instance and returns it.

Return code: a pointer to the newly
allocated memory.

Parameters: none

### copy
```
virtual void Rule::copy(Rule * rule)[pure virtual]
```

This
method handles the assignment of one Rule to another. The memory that was previously allocated
to the local string members is freed and re-allocated accordingly, with the help of the "set"
methods.

Return code: none

[表] Parameter
行 1:
  rule
  The rule to copy

### equals
```
virtual bool Rule::equals(Rule * rule)[pure virtual]
```

Determines
if the passed rule is equivalent to the current rule.

Return code:
true

if the passed rule is equal to this object;
false
 otherwise.

[表] Parameter
行 1:
  rule
  The rule to compare the current rule to

### getBin
```
virtual char* Rule::getBin()[pure virtual]
```

Returns
a pointer to the bin string defined by this rule, or 0 if none is defined.

Return code: a
pointer to the bin string; 0 if no bin string is defined.

Parameters: none

### getGroup
```
virtual char* Rule::getGroup()[pure virtual]
```

Returns
a pointer to the group defined by this rule, or 0 if none is defined.

Return code: a
pointer to the group string; 0 if no group string is defined

Parameters:
none

### getParentProfile
```
virtual Profile* Rule::getParentProfile()[pure virtual]
```

Returns
a pointer to the parent profile, that is, the profile that contains this rule
instance.

Return code: profile: a pointer to the parent profile

Parameters:
none

### getPropName
```
virtual char* Rule::getPropName()[pure virtual]
```

Returns
a pointer to the property name defined by this rule, or 0 if it is not defined.

Return
code: a pointer to the property name; 0 if the property name is not defined

Parameters:
none

### getPropValue
```
virtual int Rule::getPropValue()[pure virtual]
```

Returns
the value defined by this rule whenever the property is queried in a matching context, or 0 if
no property is defined.

Return code: the value of the property; 0 if the property is not
defined

Parameters: none

### getTestMethod
```
virtual char* Rule::getTestMethod()[pure virtual]
```

Returns
a pointer to the test method defined by this rule, or 0 if it is not defined.

Return code:
a pointer to the test method; 0 if the test method is not defined

Parameters:
none

### getTestName
```
virtual char* Rule::getTestName()[pure virtual]
```

Returns
a pointer to the test name defined by this rule, or 0 if it is not defined.

Return code: a
pointer to the test name; 0 if the test name is not defined

Parameters: none

### getTestNum
```
virtual char* Rule::getTestNum()[pure virtual]
```

Returns
a pointer to the test num string defined by this rule, or 0 if it is not defined.

Return
code: a pointer to the test number string; 0 if the string is not defined

Parameters:
none

### getTestSuite
```
virtual char* Rule::getTestSuite()[pure virtual]
```

Returns
a pointer to the test suite defined by this rule, or 0 if it is not defined.

Return code:
a pointer to the test suite; 0 if the test suite is not defined

Parameters:
none

### match
```
virtual bool Rule::match(Context * context,char * property)[pure virtual]
```

Checks
if the passed context and property match the internal rule expression, meaning each of the
fields that make up the rule matches.

Return code:
true
 if the context
matches the rule expression,
false
 otherwise.

[表] Parameters
行 1:
  context
  The context to match against
行 2:
  property
  The property to match against

### parse

virtual bool Rule::parse(char * ruleStr)[pure
virtual]

Parses a rule string and assigns the individual components of the string to the
corresponding member variables.

Return code:
true
 upon success;

false
 if an error was encountered.

[表] Parameter
行 1:
  ruleStr
  the rule string to parse

### setBin
```
virtual bool Rule::setBin(char * num)[pure virtual]
```

Sets
the internal bin value to the passed value if the parameter passes the validity check. New
memory is always allocated for the copy.

Return code:
true
 if the
string to be set is valid;
false
 otherwise.

[表] Parameter
行 1:
  strInr
  The string to set

### setGroup
```
virtual bool Rule::setGroup(char * group)[pure virtual]
```

Sets
the internal group value to the passed value if the parameter passes the validity check. New
memory is always allocated for the copy.

Return code:
true
 if the
string to be set is valid;
false
 otherwise.

[表] Parameter
行 1:
  strIn
  The string to set

### name

syntax

Description

Return
code: none

[表] Parameter
行 1:
  selector
  the selector to add

### setParentProfile
```
virtual void Rule::setParentProfile(Profile * parent)[pure virtual]
```

Sets
the parent (or creator) of this rule instance. Only Profile objects can be parents of Rule
objects.

Return code: void

[表] Parameter
行 1:
  parent
  The Profile object that is to be the parent of this Rule instance

### setPropName
```
virtual bool Rule::setPropName(char * name)[pure virtual]
```

Sets
the internal property name value to the passed value if the parameter passes the validity check.
New memory is always allocated for the copy.

Return code:
true
 if the
string to be set is valid;
false
 otherwise.

[表] Parameter
行 1:
  strIn
  The string to set

### setPropValue
```
virtual bool Rule::setPropValue(int value)[pure virtual]
```

Sets
the property value to the value passed in as an argument provided that the value lies within the
valid range.

Return code:
true
 if the value is in the valid range;

false
 otherwise.

[表] Parameter
行 1:
  value
  The value that is to be assigned to the property

### setTestMethod
```
virtual bool Rule::setTestMethod(char * method)[pure virtual]
```

Sets
the internal test method value to the passed value if the parameter passes the validity check.
New memory is always allocated for the copy.

Return code:
true
 if the
string to be set is valid;
false
 otherwise.

[表] Parameter
行 1:
  strIn
  The string to set

### setTestName
```
virtual bool Rule::setTestName(char * name)[pure virtual]
```

Sets
the internal test name value to the passed value if the parameter passes the validity check. New
memory is always allocated for the copy.

Return code:
true
 if the
string to be set is valid;
false
 otherwise.

[表] Parameter
行 1:
  strIn
  The string to set

### setTestNum
```
virtual bool Rule::setTestNum(char * num)[pure virtual]
```

Sets
the internal test number value to the passed value if the parameter passes the validity check.
New memory is always allocated for the copy.

Return code:
true
 if the
string to be set is valid;
false
 otherwise.

[表] Parameter
行 1:
  strInr
  The string to set

### setTestSuite
```
virtual bool Rule::setTestSuite(char * suite)[pure virtual]
```

Sets
the internal test suite value to the passed value if the parameter passes the validity check.
New memory is always allocated for the copy.

Return code:
true
 if the
string to be set is valid;
false
 otherwise.

[表] Parameter
行 1:
  strIn
  The string to set

### Example（取自子主题 Rule class）

See
`Data logging profile API examples`（raw: `98360.htm`）

### Member functions（取自子主题 Property class）

### getPropName
```
char* Property::getPropName()[inline]
```

Returns
the property name defined by this instance.

Return code: pointer to the property
name.

### isDefined

bool Property::isDefined()

Checks if the stored property
is defined in the active profile for the active context.

Return code:

true
 if the property is defined;
false

otherwise.

Parameters: none

### isDefined
```
bool Property::isDefined(char * name)[static]
```

Checks
if the passed property is defined in the active profile for the active context.

Return
code:
true
 if the property is defined;
false

otherwise.

[表] Parameter
行 1:
  name
  The name of the property to check

### Overridden bool cast operator
```
Property::operator bool()[inline]
```

Overrides the Boolean
cast operator by calling
value()
 and returning the result as a
Boolean.

Return code:
true
 if the value is non-zero;

false
 otherwise.

Parameters: none

### Overridden int cast operator
```
Property::operator int()[inline]
```

Overrides the integer
cast operator by calling
value()
 and returning the result as an
integer.

Return code: the value of the property.

Parameters: none

### setPropName
```
void Property::setPropName(char * name)
```

Sets
the internal value of the property name to the value passed in as an argument. A copy of the
string is made.

Return code: void

Parameters: none

### value

int Property::value()

Determines the value
of the property indicated by the member variable
propName
 by querying the
value within the active profile.

Return code: The value of the property specified by
member
propName
 within the active profile; 0 if the value is
unspecified.

Parameters: none

### value
```
int Property::value(char * name)[static]
```

Determines
the value of the property indicated by the passed parameter
name
 by querying
the value within the active profile.

Return code: The value of the property specified by

name
 within the active profile; 0 if the value is unspecified.

[表] Parameter
行 1:
  name
  the property name to query

### Example（取自子主题 Property class）

See
`Data logging profile API examples`（raw: `98360.htm`）

<!-- 语法节 end -->

## 是什么

**文档事实** data logging profile 是一组 data logging rules，决定测试系统记录哪些数据以及如何记录。它把 data logging 配置保存为可复用的 setup，并能在不删除生产 testflow 优化的情况下改变 flag 设置。

**文档事实** 文档列出的优势：Ease of use（一键开关 data logging）、Flexibility（预定义多种配置，生产时按需切换）、Efficiency（支持固定与自适应 sampling）。

**文档事实** SmarTest 交付两个默认 profile：`datalog_OFF.prf` 加载后不记录数据，也不向 log file 写信息；`datalog_ON.prf` 逐 pin 记录所有 test 的 value results。两者都可定制。

**文档事实** profile 由 rule 组成；每个 profile 的第一条 rule 含属性 `log_events_enable`，值为 1 时打开 data logging 机制。rule 的选择字段包括 Test Suite or Group、Test Method、Test Name/Num/Bin 与 Property/Value。

**文档事实** profile 的编程接口分四个类：ProfileMgr 负责 profile 的创建、加载、激活、反激活、删除、重载与目录枚举；Profile 管理 rule 集合与 selector bitmask；Rule 表示一条 rule（含 suite/method/name/num/bin/属性/值）；Property 在当前活动 profile 与上下文中查询属性值。

**文档事实** rule engine 按 rule 顺序扫描，第一个匹配的 rule 生效（`Profile::value` 的说明）；未定义属性返回 `INT_MIN`，`Property::value` 在未指定时返回 0。

**文档事实** 兼容性：既有 production settings file 可复制到 `<device directory>/profiles/`，再按只读 data logging profile 加载使用。

**推断** 因此 profile 的本质是「按执行上下文求值的 flag 规则集」：激活 profile 等价于按 rule 批量设置 data logging flags，而不是修改 testflow 文件；文档的 Example 明说不必手工切换 flags，也不必修改 testflow 文件。

## 典型用法

**文档事实** 文档的典型做法是建两个 profile：standard profile 只记录所有 test 的 pass/fail；debug profile 记录 pin value results、first failing cycles 等细节。产线良率下降时激活 debug profile，即可获得定位良率下降所需的详细结果。

**文档事实** 可在 testflow 的 test method 中监控良率下降：当失败 test 数超过阈值时，从 test method 内做一次函数调用激活 debug profile，在运行中改变 flag 配置，无需人工介入。

**文档事实** 创建规则的步骤（Creating or editing a data logging profile）：在 Test Suite or Group、Test Method、Test Name/Num/Bin 字段选 `*`，Property 选 `log_events_enable`，Value 填 `1`，点 Add，得到 rule `*.*.*. log_events_enable = 1`。

**文档事实** 编程创建 profile（Data logging profile API examples）：`ProfileMgr::getInstance()` 后 `createProfile(WildcardProfileType)`，逐条 `profile->createRule("ts:AC* . * . * . datalog_level = 3")`，再拼出 `<device>/profiles/ProfileTest.prf` 并 `profile->save(filename)`。示例还演示按 test suite、test method、test name、test num 选择器分别设规则，最后用 `* . * . *` 兜底。

**文档事实** 自适应 sampling 示例：初始化时把 `datalog_ON.prf` 与 `datalog_OFF.prf` 用 `createProfile` 载入，每次 testflow 执行按 `executionCount % SAMPLE_SIZE == 0` 调 `activateProfile` 切换。

**文档事实** Logging by test number 示例：用 TESTSET 设 `testname("EdlFfcDatalog")` 与 `testnumber(900)`，执行 FUNCTIONAL_TEST 后调用 `set.judgeAndLog_FunctionalTest()`，由活动 profile 判断是否记录。

**文档事实** 自定义属性示例：`Property logHistogram("logHistogram"); if (logHistogram) { drawHistogram(); }`；profile 在当前上下文定义该属性时返回规则值，否则为 0。

**建议** 按文档说明优先使用 profile 而不是逐 flag 手工设置；Performance Cookbook 的 Data logging settings 页也明确推荐 profiles，理由是更快、更不易漏设。

## 和谁有关

- **文档事实** Data logging profile API 与 ProfileMgr、Profile、Rule、Property：本页子主题，定义创建与处理 profile、rule、property 的编程接口；本页语法节逐字收录其成员函数与示例。
- **文档事实** Profile Editor（含 Starting the Profile Editor、Creating or editing a data logging profile、Data logging profile rule syntax）：本页子主题，提供图形化创建/编辑规则与规则语法。
- **文档事实** Loading a data logging profile、Unloading a data logging profile、Associating a data logging profile with a testflow、Restoring the default data logging profiles：本页子主题，覆盖 profile 的生命周期与与 testflow 的关联。
- **文档事实** Flags and data logging profiles 与 Data logging profiles and sampling：本页子主题，说明 profile 与 data logging flags 的关系，以及固定/自适应 sampling。
- **文档事实** Datalog Control tool：其 Setting the data log general information 子主题说明选择 profile 时点 Active，并从列表选择 data log profile。
- **文档事实** Setting up the data log information（Test Program Management）：该页说明若使用 Data Logging Profiles，profile 中的设置优先级高于 testflow 中的设置。
- **文档事实** System flags 与 Testflow flags（Memory Test Plus）：两页都说明 flag 设置可作为 Data Logging Profiles 的一部分，通过切换 profile 改变 flag 而不修改原 setup。
- **文档事实** Performance Cookbook 的 Data logging 与 Data logging settings：前者说 profiles 可把任意数量 flag 设置打包并一步切换，后者强烈推荐使用 profiles。
- **文档事实** Profile（`02.08.04.21`）：该页引用本页（objpack 入边）；本页未展开该工具与 profile 的具体关系。

## 版本

**文档事实** Functional changes 记：Introduced before SmarTest 6.3.2。

## 出处

- `02_System_reference/02.10_Data_Logging/02.10.01.02_Data_Logging_Profiles.htm`，主源，含子主题列表、advantages、默认 profiles、Example、Compatibility 与 Functional changes，已用 `show.py` 读取。
- 语法节逐字收录的子主题：`02.10.01.02.06.02_Creating_or_editing_a_data_logging_profile.htm`、`02.07.04.01.169.01`–`.04`（ProfileMgr/Profile/Rule/Property class）、`02.10.01.02.08.01`–`.05`（同上及 Data logging profile API examples）。
- 入边关系与引文取自 `extract/objpack.py` 的入边索引。
