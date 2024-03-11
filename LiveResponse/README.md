<div align="center">
<h1 align="center">CB Live Response cheatsheet/guideline</h1>
</div>

Response action categories:
- :e-mail: Email
- :page_facing_up: File
- :key: Identity
- :globe_with_meridians: Network
- :space_invader: Process
- :computer: System (Configuration in RE&CT)


# Email

To-do

# File

## Windows

### Listing shares
```execfg powershell net share```

### Listing all files on computer
```
execfg powershell tree c:\ /F > files.txt
get files.txt
delete files.txt
```

### Delete a file
```delete <filename>```

### Delete a folder and its content
```execfg powershell remove-item -path <path> -recurse -confirm:$false```

### Delete/Remove schedule task
```execfg schtasks /delete /tn <task_name>```

### Download a file
```get <filename>```

### Upload a file
```put <path>```

This will prompt the carbonblack user to select which file to upload.

### Get hash of file
```execfg powershell get-filehash <filename> | Format-List```

Format-List will avoid having truncated filepath in the output

### Unzip a file
```execfg powershell expand-archive tool.zip```

### Search for string pattern recursively
```execfg findstr /s /i "<pattern>" *```

### Print content of file in live console
```execfg powershell gc <filename>```

### Print first 50 bytes of file in hex format
```hexdump <filename>```

## Unix/Linux

To-do



# Identity

## Windows
### User information


### Listing all users
```execfg powershell net users```

### Listing local admins
```execfg powershell net localgroup administrators```

### Listing local groups
```execfg powershell net localgroup```

### Listing Kerberos tickets
```execfg powershell klist sessions```

## Linux/Unix

To-do



# Network

## Windows

### Getting network configuration
```execfg powershell ipconfig /all```

### Listing active connections
```execfg netstat -anob```

## Unix/Linux

To-do



# Process 

## Windows

### Kill a process
```kill <process_id>```

### Execute a script/tool
After uploading using ```put```, run the following:
```execfg .\tool.exe```

Alternatively, use ```exec``` to execute a process in the background without waiting for stdout/stderr.
For example, you can run Thor scanner on the endpoint. 
```exec thor64.exe```

## Unix/Linux

To-do


# System

## Windows

### Get computer information
```execfg powershell get-computerinfo```
```execfg powershell systeminfo```
```execfg powershell wmic computersystem list full```

### Drives connected to the computer
```drives```
```execfg powershell fsutil fsinfo drives```

### Installed updates
```execfg powershell wmic qfe```

### Installed softwares
```execfg powershell wmic product get name,version```
```execfg powershell get-package```

### Query registry
```reg query HKLM\SYSTEM\<your_key>```

### Query Event Log
```execfg powershell get-winevent -LogName 'Security' | where-object {$_.ID -eq 4688}```

### Listing all schedule tasks
```
execfg powershell schtasks /query /fo LIST /v > scheduletasks.txt
get scheduletasks.txt
```

### Unix/Linux

To-do
