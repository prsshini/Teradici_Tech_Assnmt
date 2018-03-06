#!/usr/bin/env python
import unittest
import subprocess
from Wordcount import wordcnt

class MyTests(unittest.TestCase):
    def test_valid_file(self):
        result = wordcnt("input1.txt")
        self.assertEqual("[('this', 6), ('has', 3), ('is', 2), ('three', 2), ('one', 1), ('will', 1), ('be', 1), ('two', 1), ('four', 1), ('fie', 1)]", result)

    def test_ignore_punctuations(self):
        result = wordcnt("input2.txt")
        self.assertEqual("[('one', 7), ('one22', 1)]",result)

    def test_ignore_multiword_line_punctuations(self):
        result = wordcnt("input3.txt")
        self.assertEqual("[('this', 6), ('has', 3), ('is', 2), ('three', 2), ('one', 1), ('will', 1), ('be', 1), ('two', 1), ('four', 1), ('fie', 1)]", result)

    def test_script_as_script(file):
        return subprocess.check_output(['./Wordcount.py', '-f', file]).decode('utf-8').rstrip()

    def test_usage(self):
        assert subprocess.check_output(['./Wordcount.py', '-h']).decode('utf-8').rstrip() == "USAGE:  Wordcount.py  -f <file>"

if __name__ == '__main__':
   # command_line_param = sys.argv[1]
   suite = unittest.TestLoader().loadTestsFromTestCase(MyTests)
   unittest.TextTestRunner().run(suite)