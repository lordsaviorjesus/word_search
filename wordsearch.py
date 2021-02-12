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
    """
    Function returns the transposed version of string

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

    #Searching forward
    if puzzle.find(word) != -1:

        #Initializing variables
        string1 = "" 
        value = 0
        i = 0

        #Consider example: find_word('ABCDEFGHI','DEF',3)
        while i < (len(puzzle)):
            #While i is less than 9:
            """
                First, we assign string1 to the puzzle string from position i to
            position i + row_len (from 0 to 3 in example). We then increase i
            by the row_len. We do this because we're searching through each
            row individually to find the word, that way we can return the
            specific row where the word is found if we find a word.
            """
            string1 = puzzle[i : i + row_len]
            value = string1.find(word)
            #Here, if .find() finds the word, we increment it by 1 and break
            #from the loop. This does.....(what does this do again?)
            if value != -1:
                value = value + i
                break
            i = i + row_len

        #After the while loop, if value == -1 still, then word not found
        if value == -1:
            return word + ":" + " word not found"

        """
            Here we define position so this is more readable. In our example, 
        we find 'DEF' at  position 3. Integer dividing position 3 by our row
        length 3 gives us 1, which is the current row we are in. Modulating
        our position 3 by row_len 3 gives us 0, which is the current column
        'DEF' is located in the 3 x 3 matrix for this example.

                                    column 0
                                    v
                                    ABC
                                    DEF <-- row 1
                                    GHI
        """
        position = value
        row = position // row_len
        column = position % row_len
        return word + ":" + " (FORWARD)" + " row: " + str(row) + " column: " \
            + str(column)

    """
        From here on, the code largely resembles the same process stated in the
    searching forward section. The only thing that changes is for backwards
    and up, the position is related to the puzzle_len minus where the word is
    found -1 due to the structure of searching for the words this way. Other
    than that, the process of getting row and column is identical.
    """
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
    #If -1, returning that the word was not found.
    return word + ":" + " word not found"


#displays the puzzle in 10x10 grid
def display_puzzle(puzzle, row_len):
    """
    Function displays puzzle in 10x10 grid

    Args:
        puzzle(str): inputted string
        row_len: number of characters per row

    Returns:
        10x10 puzzle (string): characters shifted around in 10x10 grid
    """
    start = 0 #start position in string index
    end = row_len #end position in string index
    for num in range(row_len): #row length determines how many rows we print
        print(puzzle[start:end])
        start += row_len
        end += row_len
    #We go through each row of 10 chars and print that line. 0-10, 10-20, etc.


def main():
    """
    Function returns the final puzzle
    
    Args:
        puzzle(str): inputted 100 characters
        word(str): words to find

    Returns:
        str: result of word search
    """
    #Getting puzzle from user
    puzzle = input("Enter a puzzle line: ")
    puzzle = puzzle.strip()
    #Getting words from user
    words = input("Enter words to search: \n\n")
    words = words.strip()
    
    #Displaying the puzzle to user
    display_puzzle(puzzle, 10)
    print("")
    
    """
    Here we have a while loop that runs as long as the 
    length of words does not equal 0. We start the while loop by 
    checking for blank spaces in "words" from user input. Everywhere
    we see a blank space, we initiate a variable called words to start
    from that index. We then search for this specifc word in puzzle
    by calling the find_word function, which prints the results. 
    """
    
    words += " "
    while len(words) != 0:
        blank = words.find(' ')
        word = words[:blank]
        words = words[blank + 1:]
        print(find_word(puzzle, word, 10))

if __name__ == "__main__":
    main()
