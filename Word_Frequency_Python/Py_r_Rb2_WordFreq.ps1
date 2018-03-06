param (
    [Parameter(Mandatory=$true)][string]$FileName                
 )

Function find_word_freq {
[
CmdletBinding()]

  param

  (

  [string]$FileName

  )
##$FileName = "C:\Users\Michael\Desktop\Teradici\Teradici_Tech_Assnmt\Wordfreqinput.txt"
$File = Get-Content $FileName
$Linecount = $File.Count
Write-Host "Total no of lines in the file $FileName : $Linecount"

$words = ""
$exist = 0
$Count = 0
$wordarr = @{}
$linect = 0

$File | foreach {
    $Line = $_
    $linect++ 
    $Line.Split(" .,:;?!/()[]{}-```"$*@#%^&~") | foreach {
        $word = $_.ToUpper()
         If ($word[0] -replace '[^a-zA-Z0-9]', '') {
            $Count++
            If ($word.Contains($words)) { $exist++ }
            If ($wordarr.ContainsKey($Word)) {
                $wordarr.$word++
            } else {
                $wordarr.Add($word, 1)
            }
        }
    } 
}

$allwords = $wordarr.Count
Write-Host "There were $allwords total words in the text"
$wordarr.GetEnumerator() | ? { $_.Name.Length -gt 1 } | 
Sort Value -Descending | Select -First 10
}

find_word_freq -FileName $FileName