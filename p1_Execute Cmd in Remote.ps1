<#Write a script that accepts command-line parameters and executes the following function within
the script:
1. The function must accept the following parameters: an FQDN, username, password and
command to execute.
2. The function must establish a connection to the host specified by the FQDN with the given
credentials, execute the provided command and return the output of the command.
3. The function should distinguish between major error cases such as “connection failed”,
“command failed to execute”, etc.
###>


param (
    [Parameter(Mandatory=$true)][string]$fqdn,
    [Parameter(Mandatory=$true)][string]$usrnm,
    [Parameter(Mandatory=$true)][string]$passwd,
    [Parameter(Mandatory=$true)][string]$cmd                     
 )

 function execute_command
 {
 param (
    [string]$fqdn,
    [string]$username,
    [string]$command,
    [string]$password                       
  ) 
 
  $passwd = ConvertTo-SecureString -AsPlainText $passwd -Force
  $credential = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList $usrnm,$passwd
 Invoke-Command -ComputerName $fqdn -credential $credential -ScriptBlock {$cmd}
 }
 
 execute_command -fqdn $fqdn -username $usrnm -password $passwd -command $cmd
