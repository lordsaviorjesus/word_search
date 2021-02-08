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
from wordsearch import display_puzzle
from wordsearch import find_word

#String for find_word assertions. Words are: Augustus Sameera word search bbb
string_1 = "YhWMA4lUdPGvsjuqSif9nxIEgSBrH1lCGWuLXVacy93zsq7TreTKTUtfM0eJword"\
    "u3aOeh89VDsB99mghcraescoas1915q9bFSr"

if __name__ == "__main__":

    #test cases for reverse_string
    assert reverse_string("hello") == "olleh"
    assert reverse_string("ABCDEFGHIJKLMNOP") == "PONMLKJIHGFEDCBA"
    assert reverse_string("wordsearch") == "hcraesdrow"

    #test cases for transpose_string 
    assert transpose_string("ABCGITXYZ", 3) == "AGXBIYCTZ"
    assert transpose_string("UFIBOSDMF", 3) == "UBDFOMISF"
    assert transpose_string("QQERASDVO", 3) == "QRDQAVESO"

    #test cases for display_puzzle
    assert display_puzzle("ABCDEFGHI", 3) == print("ABC\nDEF\nGHI")
    assert display_puzzle("ZYXAOAOWM", 3) == print("ZYX\nAOA\nOWM")
    assert display_puzzle("YUTBVNAES", 3) == print("YUT\nBVN\nAES")

    #test cases for find_word
    assert find_word(string_1, "Augustus", 10) == 'Augustus: (DOWN) row: 0 '\
        'column: 4'
    assert find_word(string_1, "Sameera", 10) == 'Sameera: (UP) row: 9 '\
        'column: 8'
    assert find_word(string_1, "word", 10) == 'word: (FORWARD) row: 6 '\
        'column: 0'
    assert find_word(string_1, "search", 10) == 'search: (BACKWARD) row: 8 '\
        'column: 5'
    assert find_word(string_1, "bbb", 10) == 'bbb: word not found'






