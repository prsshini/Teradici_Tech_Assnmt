##Write a script that retrieves all installed Windows applications

$key="HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall\*"
Get-ItemProperty $key |  Select-Object DisplayName, DisplayVersion, Publisher, InstallDate | 
Format-Table –AutoSize