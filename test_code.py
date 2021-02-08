# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 20:16:17 2021

@author: Augustus
"""
#display puzzle I wrote before I got a chance to add it:

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





def split_words(string):
    past_location = 0

    for position in range(len(string)):
        if string[position] == " ":
            print(string[past_location : position].strip())
            past_location = position

    #Accounting for the rest of the string:
    print(string[past_location:].strip())

#Example:
split_words("There was a dog")

