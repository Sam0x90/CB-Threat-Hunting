parent_name:outlook.exe -process_name:chrome.exe -process_name:excel.exe -process_name:winword.exe -process_name:firefox.exe -process_name:iexplore.exe -process_name:acrord32.exe -cmdline:CVArchiverAddin* -process_name:powerpnt.exe -process_name:acrobat.exe -process_name:winrar.exe AND netconn_count:[1 TO *] 
regmod:Outlook\Security\EnableUnsafeClientMailRules

#Probably needs more Filtering
