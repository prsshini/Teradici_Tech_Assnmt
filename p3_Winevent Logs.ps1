#Write a script that saves Windows event logs to a text file.

$Location="C:\Logs"
$datefmt=(Get-Date).AddDays(-1).ToString('MM-dd-yyyy')
$filename= $file + "_" + $datefmt + ".txt"
Get-EventLog -LogName System -Newest 24 | Where-Object { $_.EventID -eq 7045 } | Out-File -FilePath $Location\$filename