# MotionBuilder Python Menu Setup Module

This tool can automatucally generate menu bar for MotionBuilder.
You have only to specify your script folder path and put python contents in the folder.

# Sample 
* Put items in `Scripts` to `C:\\C:\\Users\{user}\Documents\MB\{MB_version}\config\Scripts`
* Put items in `PythonStartup` to `C:\\C:\\Users\{user}\Documents\MB\{MB_version}\config\PythonStartup`

# How to use
```
from MenuCreator import *

MenuCreator("Tool Name", "Tool Folder Name")
```

* Tool Folder Name should be specified same name for the tool folder located in `C:\\C:\\Users\{user}\Documents\MB\{MB_version}\config\Scripts\{Tool Folder Name}`