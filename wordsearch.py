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
    #Hey! I changed some things:
    """
    new_string = ""
    for i in range(row_len):
        for j in range(len(string)): #what does j do here?
            if i < len(string):
                new_string = new_string + string[i]
                i = i + row_len
    return new_string

    ^^^ PREVIOUS CODE ^^^
    This is the code we had before. I realized that I wasn't sure exactly what
    purpose the for loop for j had, so I replaced it. Also, I might not be
    understanding everything, but I wasn't sure what purpose the if i<len(string):
    line served. Won't i always be less than the length of the string? essentially,
    if we had a row length larger than the string, then we can only make one row.
    Let me know on discord if you see any imminent problems with what I changed, but
    I think what I changed works.
    -Gus
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
    """
    I created this b/c it'll make the find_word function easier I think
    """
    return f"{word.upper()}: ({direction.upper()}) row: {row} column: {column}"


def find_word(puzzle: str, word: str, row_len: int):
    column = transpose_string(puzzle, row_len)
    
    """Hey! I'm thinking if we put this function in a while loop and test all functions, it'll go through 
    each if statement and then return the value"""

    #found FORWARD:
    if puzzle.find(word) != -1:
        position = puzzle.find(word)
        print(display_word(word,"forward", 1,0)) # <---need to change to variables
        
    #found BACKWARD:
    if puzzle.find(word) == -1:
        _reverse = reverse_string(puzzle)
        position = _reverse.find(word)
        position = 9 - position #I think this converts it back to original position in string?
        print(display_word(word, "backward", 1, 2)) #<---need to change variables 
    
    #found DOWN:
    if puzzle.find(word) == -1:
         _down = transpose_string(puzzle,row_len)
         position = puzzle.find(word)
         position = 9 - position
         print(display_word(word, "down", 0, 1)) #<---need to change to variables 
        
    #found UP:

    #Value not found: 

    
if __name__ == "__main__":
    
    print(transpose_string('abcbobxyz',3)) #FORWARD
    print(" ")
    find_word("abcbobxyz", "bob", 3)

    print(transpose_string('derxyzgit',3))#BACKWARD
    print(" ")
    find_word('derxyzgit',"red",3)

    print(transpose_string("abcbobxyz", 3))
    print(" ")
    find_word("abcbobxyz", "boy", 3)
    
    















    
    