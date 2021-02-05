"""
Contains solutions to wordsearch_tests
CPE101
Section <05>
Project 2, Part 2
Name: <Sameera> <Balijepalli> <and> <Augustus> <Soto>
Cal Poly User: <sbalijep> <and> <ajsoto>
"""

from wordsearch import reverse_string
from wordsearch import transpose_string
from wordsearch import display_word

#test cases for reverse_string 
assert reverse_string("hello") == "olleh"
assert reverse_string("ABCDEFGHIJKLMNOP") == "PONMLKJIHGFEDCBA"
assert reverse_string("wordsearch") == "hcraesdrow"

#test cases for transpose_string 
assert transpose_string("ABCGITXYZ", 3) == "AGXBIYCTZ"