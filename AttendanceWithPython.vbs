Set oShell = CreateObject ("Wscript.Shell") 
Dim strArgs
strArgs = "cmd /c RFID.bat"
oShell.Run strArgs, 0, false