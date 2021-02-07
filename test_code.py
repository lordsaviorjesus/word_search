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

def split_words(string):

    for position in range(len(string)):
        if string[position] == " ":
            print("Hello")

            
split_words("There was a dog")

