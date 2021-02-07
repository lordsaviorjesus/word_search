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
    if row_len > len(string):
        return string
    for i in range(row_len):
        new_string = new_string + string[i::row_len]
        i = i + 1
    return new_string


def display_puzzle(string, row_len):
    """Function displays puzzle in 10x10 grid
    Args:
        string(str): inputted string
        row_len: number of characters per row
    Returns:
        _puzzle(string): characters shifted around in 10x10 grid
    """
    string = transpose_string(string, row_len)
    for i in range(len(string)):
        if i % row_len == 0:
            sub = string[i:i+row_len]
            _puzzle = ""
            for j in sub:
                _puzzle = _puzzle + j
            print("".join(_puzzle))


def display_word(word, direction, row, column):
    """Function returns the conditions of word
    Args:
        word(str): user input word
        direction(str): depends on direction of puzzle
        row(int): row number
        column(int): column number
    Returns:
        string: word, direction, row, column
    """
    return f"{word.upper()}: ({direction.upper()}) row: {row} column: {column}"


def search_forward(puzzle, word, row_len):
    """Function checks for word in puzzle
    Args:
        puzzle(str): inputted puzzle
        word(str): word you're searching for
        row_len(int): length of the row
    Returns:
        display_word(str): search result
    """
    position = puzzle.find(word)
    if position == -1:
        return -1
    row = position // row_len
    column = position % row_len
    direction = "forward"
    return display_word(word, direction, row, column)


def search_backward(puzzle, word, row_len):
    """Function checks for word in puzzle
    Args:
        puzzle(str): inputted puzzle
        word(str): word you're searching for
        row_len(int): length of the row
    Returns:
        display_word(str): search result
    """
    _reverse = reverse_string(puzzle)
    position = _reverse.find(word)
    if position == -1:
        return -1
<<<<<<< Updated upstream
    position = len(puzzle) - position - 1
    column = position % row_len
    row = position//row_len
    direction = "backward"
    return display_word(word, direction, row, column)
=======
    else:
        column = position % row_len
        row = position // row_len
        direction = "backward"
        return display_word(word, direction, row, column)
>>>>>>> Stashed changes


def search_down(puzzle, word, row_len):
    """Function checks for word in puzzle
    Args:
        puzzle(str): inputted puzzle
        word(str): word you're searching for
        row_len(int): length of the row
    Returns:
        display_word(str): search result
    """
    _down = transpose_string(puzzle, row_len)
    position = _down.find(word)
    if position == -1:
        return -1
<<<<<<< Updated upstream
    row = position % row_len
    column = position//row_len
    direction = "down"
    return display_word(word, direction, row, column)
=======
    else:
        position = len(puzzle) - position -1
        row = position % row_len
        column = position // row_len
        direction = "down"
        return display_word(word, direction, row, column)
>>>>>>> Stashed changes


def search_up(puzzle, word, row_len):
    """Function checks for word in puzzle
    Args:
        puzzle(str): inputted puzzle
        word(str): word you're searching for
        row_len(int): length of the row
    Returns:
        display_word(str): search result
    """
    _up = transpose_string(puzzle, row_len)
    _up = reverse_string(_up)
    position = _up.find(word)
    if position == -1:
        return -1
    position = len(puzzle) - position -1
    row = position % row_len
    column = position // row_len
    direction = "up"
    return display_word(word, direction, row, column)


def find_word(puzzle, word, row_len):
    """Function print the search result
    Args:
        puzzle(str): inputted puzzle
        word(str): word you're searching for
        row_len(int): length of the row
    Returns:
        display_word(str): search result
    """
    if search_forward(puzzle, word, row_len) != -1:
        return search_forward(puzzle, word, row_len)
    if search_backward(puzzle, word, row_len) != -1:
        return search_backward(puzzle, word, row_len)
    if search_down(puzzle, word, row_len) != -1:
        return search_down(puzzle, word, row_len)
    if search_up(puzzle, word, row_len) != -1:
        return search_up(puzzle, word, row_len)
    return word + ": word not found"

<<<<<<< HEAD
=======
<<<<<<< Updated upstream
=======

def main():
    """
    """
    #Puzzle input
    puzzle = input("Enter a puzzle: ")
    puzzle = puzzle.strip()
    #Words seperated by spaces
    words = input("Enter target words: ")
    words = words.strip()
    #length of row
    row_len = input("Enter length of rows: ")
    row_len = row_len.strip()
    display_puzzle(puzzle, row_len)
    
    for
    find_word(puzzle,words,row_len)
    
    

    
#if __name__ == "__main__":
>>>>>>> Stashed changes
>>>>>>> parent of d879507... fixing
