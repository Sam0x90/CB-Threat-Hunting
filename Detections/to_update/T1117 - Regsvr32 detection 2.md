(((process_name:regsvr32.exe ) AND (cmdline:temp* OR parent_name:powershell.exe OR cmdline:scrobj*)) OR (process_name:wscript.exe AND parent_name:regsvr32.exe)) -cmdline:Microsoft.Teams.Addin*
