# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 20:16:17 2021

@author: Augustus
"""
from wordsearch import transpose_string

def search_forward(puzzle, word, row_len):
    column = puzzle.find(word)
    if column == -1:
        return -1
    else:
        my_string = transpose_string(puzzle,row_len)
        
        

<<<<<<< HEAD
        return my_string
        

print(search_forward("ABCDEFGHI","DEF",3))

=======
display_puzzle("qfYWkBq4Ynvlyo8WGJC5pEfSEkoCopzruyHFAici3Dj8XHYjw8JkWlLTf7nVQ"\
               "cYjCpmnrtzbM5h77NOYkZSR5oTNqOr4uob5SMcP",10)

print("")

def split_words(string):

    for position in range(len(string)):
        if string[position] == " ":
            print("Hello")

            
split_words("There was a dog")

            
>>>>>>> parent of d879507... fixing
