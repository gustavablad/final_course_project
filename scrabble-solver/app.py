# pip install flask
# from flask import Flask
from collections import Counter

letter_points = {
    "a": 1, "b": 3, "c": 3, "d": 2, "e": 1, 
    "f": 4, "g": 2, "h": 4, "i": 1, "j": 8, 
    "k": 5, "l": 1, "m": 3, "n": 1, "o": 1, 
    "p": 3, "q": 10, "r": 1, "s": 1, "t": 1, 
    "u": 1, "v": 4, "w": 4, "x": 8, "y": 4,
    "z": 10, 
}
# table of letters and their respective scrabble points

with open ("scrabble-solver/dictionary.txt") as list:
    valid_words = set(word.strip().lower() for word in list)
# set of all valid words in compliance with an online scrabble dictionary

tiles = input("What tiles do you have? Use only the letters on the tiles and '*' for blank tiles. Do not use any commas or periods. Example of rack with 7 tiles: *egit*r. : ")
tile_count = Counter(tiles)

def can_build_word(word, tiles):
    remaining_tiles = list(tiles)
    for letter in word:
        if letter in remaining_tiles:
            remaining_tiles.remove(letter)
        elif "*" in remaining_tiles:
            remaining_tiles.remove("*")
        else:
            return False
    return True