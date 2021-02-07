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
    #Main loop:
    for i in range(row_len):
        new_string = new_string + string[i::row_len]
        i = i + 1
    return new_string


def display_word(word, direction, row, column):
    return f"{word.upper()}: ({direction.upper()}) row: {row} column: {column}"


def find_word(puzzle: str, word: str, row_len: int): #finds the word
    column = transpose_string(puzzle, row_len)
    
    while puzzle.find(word) == -1:
        #found BACKWARD
        if puzzle.find(word) == -1:
            _reverse = reverse_string(puzzle)
            position = _reverse.find(word)
            position = 9 - position 
            direction = "backward"
            return (display_word(word, direction, 1, 2)) #<---need to change variables 
        #found DOWN
        if puzzle.find(word) == -1:
            _down = transpose_string(puzzle,row_len)
            position = puzzle.find(word)
            position = 9 - position
            direction = "down"
            return (display_word(word, direction, 0, 1)) #<---need to change to variables 
        #found UP
        if puzzle.find(word) == -1:
            _up = transpose_string(puzzle, row_len)
            _up = reverse_string(_up)
            position = _up.find(word)
            position = 9 - position
            direction = "up"
            return (display_word(word, direction, 1, 2))
        break

    if puzzle.find(word) != -1:
        position = puzzle.find(word)
        direction = "forward"
        return (display_word(word, direction, 1, 0))
    else: 
        return puzzle.find(word)
    
def display_puzzle(string, row_len): #displays puzzle
    string = transpose_string(string, row_len)
    for i in range(len(string)):
        if i % row_len == 0:
            sub = string[i:i+row_len]
            _puzzle = ""
            for j in sub:
                _puzzle = _puzzle + j
            print(" ".join(_puzzle))

def main():
    
    
if __name__ == "__main__":
    
    print(transpose_string('abcbobxyz',3)) #FORWARD
    print(" ")
    print(find_word("abcbobxyz", "bob", 3))

    print(display_puzzle("abcbobxyz", 3))


    















    
    