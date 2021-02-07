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
        
        

        return my_string
        

print(search_forward("ABCDEFGHI","DEF",3))

