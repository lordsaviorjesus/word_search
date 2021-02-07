# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 20:16:17 2021

@author: Augustus
"""

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
    
    
#Potentially simplified display_puzzle, lmk if you want to incorporate or not

def display_puzzle(string, row_len):
    start = 0
    end = row_len
    for num in range(row_len):
        print(string[start:end])
        start += row_len
        end += row_len


display_puzzle("qfYWkBq4Ynvlyo8WGJC5pEfSEkoCopzruyHFAici3Dj8XHYjw8JkWlLTf7nVQ"\
               "cYjCpmnrtzbM5h77NOYkZSR5oTNqOr4uob5SMcP",10)

print("")


"""Hey, this isn't really a function for us to use, but I think I figured out
how to split up the words so we can call the fucntions on them. Basically, under
the if statement I wrote, we could call the functions on those words to look
for them in the word search puzzle. lmk what you think"""

def split_words(string):
    past_location = 0

    for position in range(len(string)):
        if string[position] == " ":
            print(string[past_location: position])
            past_location = position

    #Accounting for the rest of the string:
    print(string[past_location:])

#Example:
split_words("There was a dog")

