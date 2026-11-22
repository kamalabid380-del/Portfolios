Set fso = CreateObject("Scripting.FileSystemObject")
Set sh = CreateObject("WScript.Shell")
bat = fso.GetParentFolderName(WScript.ScriptFullName) & "\refresh-seed.bat"
sh.Run """" & bat & """ --quiet", 0, False
