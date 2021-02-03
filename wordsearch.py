"""
Contains solutions to wordsearch

CPE101

Section <05>

Project 2, Part 2

Name: <Sameera> <Balijepalli> <and> <Augustus> <Soto>

Cal Poly User: <sbalijep> <and> <ajsoto>
"""


def reverse_string(string: str):
    """Function returns the reverse of an inputted string
    Args:
        string(str): string of characters
    Returns:
        _reverse(str): the reverse of inputted string
    """
    _reverse = ""
    for _x in string:
        _reverse = _x + _reverse
    return _reverse


def transpose_string(string: str, row_len: int):
    """Function returns the transposed version of string
    Args:
        string(str): inputted string
        row_len(int): assumed integer of row length
    Returns:
        new_string(str): transposed version of inputted string
    """
    new_string = ""
    for i in range(row_len):
        for j in range(len(string)):
            if i < len(string):
                new_string = new_string + string[i]
                i = i + row_len
    return new_string


