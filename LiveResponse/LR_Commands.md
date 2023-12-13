These are commands specific to CarbonBlack EDR Live Response.
Some of them are applicable to any Windows prompt as we are calling a powershell to execute them. 

# General

# Identity

## User information


## Listing all users
```execfg powershell net users```

## Listing local admins
```execfg powershell net localgroup administrators```

## Listing local groups
```execfg powershell net localgroup```

## Listing Kerberos tickets
```execfg powershell klist sessions```

##

# System

## Get computer information
```execfg powershell get-computerinfo```
```execfg powershell systeminfo```
```execfg powershell wmic computersystem list full```

## Drives connected to the computer
```drives```
```execfg powershell fsutil fsinfo drives```

## Installed updates
```execfg powershell wmic qfe```

## Installed softwares
```execfg powershell wmic product get name,version```
```execfg powershell get-package```

## Query registry
```reg query HKLM\SYSTEM\<your_key>```

## Query Event Log
```execfg powershell get-winevent -LogName 'Security' | where-object {$_.ID -eq 4688}```

# Network

## Getting network configuration
```execfg powershell ipconfig /all```

## Listing active connections
```execfg netstat -anob```

# Process 

# File

## Listing shares
```execfg powershell net share```

## Listing all files on computer
```
execfg powershell tree c:\ /F > files.txt
get files.txt
execfg powershell rm files.txt
```

## Download a file
```get <filename>```

## Upload a file
```put <path>```

This will prompt the carbonblack user to select which file to upload.

## Get hash of file
```execfg powershell get-filehash <filename> | Format-List```

Format-List will avoid having truncated filepath in the output

## Unzip a file
```execfg powershell expand-archive tool.zip```

## Execute a script/tool
After uploading using ```put```, run the following:
```execfg .\tool.exe```

## Search for string pattern recursively
```execfg findstr /s /i "<pattern>" *```

## Print content of file in live console
```execfg powershell gc <filename>```

## Print first 50 bytes of file in hex format
```hexdump <filename>```
