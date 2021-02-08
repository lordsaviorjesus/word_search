"""
Wordsearch program that finds a word in a 10 x 10 matrix.

CPE101

Section <05>

Project 2, Part 2

Name: <Sameera> <Balijepalli> <and> <Augustus> <Soto>

Cal Poly User: <sbalijep> <and> <ajsoto>
"""


def reverse_string(string: str):
    """
    Function returns the reverse of an inputted string.

    Args:
        string(str): string of characters.

    Returns:
        string[::-1]: the reverse of inputted string.
    """
    return string[::-1] #Neat little trick!

def transpose_string(string: str, row_len: int):
    """Function returns the transposed version of string

    Args:
        string(str): inputted string.
        row_len(int): assumed integer of row length.

    Returns:
        new_string(str): transposed version of inputted string.
    """
    new_string = ""
    #accounts for case where row length is too small
    if row_len > len(string):
        return string
    
    #To understand this, take this example: string = "ABCDEFGHI" row_len = 3
    for i in range(row_len):
        """
            Here, we're simply starting at i and taking a step size equal to our
        row_len in 'string'; we then add this to new_string. Starting at i = 0 
        in our example, we get string[0] == 'A', string[3] == 'D', and 
        string[6] == 'G', which makes 'ADG', from line 55.
            At the end of the for loop, we increase i by one so we repeat this
        process adding indexes 1,4,7 ('BEH') and 2,5,8 ('CFI') to new_string. 
        This gives us our transposed string.

        (Note: You can uncomment the print statements to see this work)
        """
        new_string = new_string + string[i::row_len]
        i = i + 1
        #print(new_string)
        #print("loop " + str(i))
        #print("")
    return new_string

def find_word(puzzle, word, row_len):
    """
    Function print the search result

    Args:
        puzzle(str): inputted puzzle
        word(str): word you're searching for
        row_len(int): length of the row

    Returns:
        display_word(str): search result
    """
    #Variable definitions
    puzzle_len = len(puzzle)
    backwards = reverse_string(puzzle)
    down = transpose_string(puzzle, row_len)
    _up = reverse_string(down)

    #Searching forwards
    #This case 
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
        return word + ":" + " (FORWARD)" + " row: " + str(row) + " column: " \
            + str(column)

    #Searching backwards
    if backwards.find(word) != -1:
        position = puzzle_len - backwards.find(word) - 1
        row = position // row_len
        column = position % row_len
        return word + ":" + " (BACKWARD)" + " row: " + str(row) + " column: "\
            + str(column)

    #Searching down
    if down.find(word) != -1:
        position = down.find(word)
        column = position // row_len
        row = position % row_len
        return word + ":" + " (DOWN)" + " row: " + str(row) + " column: " \
            + str(column)

    #Searching up
    if _up.find(word) != -1:
        position = puzzle_len - _up.find(word) - 1
        row = position % row_len
        column = position // row_len
        return word + ":" + " (UP)" + " row: " + str(row) + " column: " \
            + str(column)
    return word + ":" + " word not found"


#displays the puzzle in 10x10 grid
def display_puzzle(puzzle, row_len):
    """Function displays puzzle in 10x10 grid
    Args:
        string(str): inputted string
        row_len: number of characters per row
    Returns:
        _puzzle(string): characters shifted around in 10x10 grid
    """
    for i in range(len(puzzle)):
        if i % row_len == 0:
            sub = puzzle[i:i+row_len]
            _puzzle = ""
            for j in sub:
                _puzzle = _puzzle + j
            print("".join(_puzzle))

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

    words = input("Enter words to search: \n\n")
    words = words.strip()

    display_puzzle(puzzle, 10)
    print("")
    words += " "
    while len(words) != 0:
        blank = words.find(' ')
        word = words[:blank]
        words = words[blank + 1:]
        print(find_word(puzzle, word, 10))

if __name__ == "__main__":
    main()
