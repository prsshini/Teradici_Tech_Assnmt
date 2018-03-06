$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$sut = (Split-Path -Leaf $MyInvocation.MyCommand.Path) -replace '\.Tests\.', '.'
. "$here\$sut"

Describe "Test_wrong_input_param" {
    it  'only allows a string to be passed to the FilePath parameter_when called' {

  mock 'Select-String'  {

  return $null

 }
{find_word_freq -FileName ([PSCustomObject]@{})} | Should throw
}
}


describe 'Test file 2' {

    $FileName = "C:\Users\Michael\Desktop\Teradici\Teradici_Tech_Assnmt\Wordfreqinput2.txt"
    $result = find_word_freq -FileName 'C:\Users\Michael\Desktop\Teradici\Teradici_Tech_Assnmt\Wordfreqinput2.txt'

    it 'should return 7 ones' {
        {find_word_freq -FileName $FileName} | Should not throw
    }

}

