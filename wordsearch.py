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

def find_word(puzzle, word, row_len):
    """Function print the search result
        Args:
            puzzle(str): inputted puzzle
            word(str): word you're searching for
            row_len(int): length of the row
        Returns:
            display_word(str): search result
    """
    puzzle_len = len(puzzle)
    backwards = reverse_string(puzzle)
    down = transpose_string(puzzle, row_len)
    _up = reverse_string(down)

    if puzzle.find(word) != -1:
        string1 = ""
        value = ""
        i = 0
        while i < (len(puzzle)):
            string1 = puzzle[i:i + row_len]
            value = string1.find(word)
            if value != -1:
                value = value + i
                break
            i = i + row_len
        if value == -1:
            return word + ":" + " word not found"
        position = value
        row = position // row_len
        column = position % row_len
        return word + ":" + " (FORWARD)" + " row: " + str(row) + " column: " + str(column)
    if backwards.find(word) != -1:
        position = puzzle_len - backwards.find(word) - 1
        row = position // row_len
        column = position % row_len
        return word + ":" + " (BACKWARD)" + " row: " + str(row) + " column: " + str(column)
    if down.find(word) != -1:
        position = down.find(word)
        column = position // row_len
        row = position % row_len
        return word + ":" + " (DOWN)" + " row: " + str(row) + " column: " + str(column)
    if _up.find(word) != -1:
        position = puzzle_len - _up.find(word) - 1
        row = position % row_len
        column = position // row_len
        return word + ":" + " (UP)" + " row: " + str(row) + " column: " + str(column)
    else:
        return word + ":" + " word not found"


def main():
    """Function returns the final puzzle 
    Args:
        puzzle(str): inputted 100 characters 
        word(str): words to find
    Returns: 
        str: result of word search
    """
    puzzle = input("Enter a puzzle line: ")
    puzzle = puzzle.strip()

    word = input("Enter words to search: ")
    word = word.strip()
    
    row_len = input("Enter row length:")
    row_len = row_len.strip()

    if len(puzzle) == 100:
        grid = ""
        for _x in range(0,100):
            column = _x%10
            row = _x//10
            string = puzzle[_x]
            grid += string
            if len(grid) == 10:
                print(grid)
                grid = ""
    print()
    word += " "
    while len(word) != 0:
        commas = word.find(" ")
        word = word[:commas]
        word = word[commas + 1:]
        print(find_word(puzzle, word, row_len))

if __name__ == "__main__":
    main()
