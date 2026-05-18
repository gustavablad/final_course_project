from flask import Flask
# if run in terminal: "$ pip --version" and it shows different version from python interpreter, change interpreter to pip's version
from collections import Counter

LETTER_POINTS = {
    "a": 1, "b": 3, "c": 3, "d": 2, "e": 1, 
    "f": 4, "g": 2, "h": 4, "i": 1, "j": 8, 
    "k": 5, "l": 1, "m": 3, "n": 1, "o": 1, 
    "p": 3, "q": 10, "r": 1, "s": 1, "t": 1, 
    "u": 1, "v": 4, "w": 4, "x": 8, "y": 4,
    "z": 10, 
}
# table of letters and their respective scrabble points

with open ("scrabble-solver/dictionary.txt") as f:
    VALID_WORDS = set(word.strip().lower() for word in f)
# set of all valid words in compliance with an online scrabble dictionary

player_tiles = input("What tiles do you have? Use only the letters on the tiles and '*' for blank tiles. Do not use any commas or periods. Example of rack with 7 tiles: *egit*r. : ")
# tile_count = Counter(tiles)

def can_build_word(word, tiles):
    
    for letter in word:
        remaining_tiles = list(player_tiles)
        if letter in remaining_tiles:
            remaining_tiles.remove(letter)
        elif "*" in remaining_tiles:
            remaining_tiles.remove("*")
        else:
            return False
    return True

def calculate_score(word, tiles):
    score = 0
    for letter in word:
        remaining_tiles = list(player_tiles)
        if letter in remaining_tiles:
            score += LETTER_POINTS[letter]
            remaining_tiles.remove(letter)
        elif "*" in remaining_tiles:
            remaining_tiles.remove("*")
    return score

def find_words(tiles):
    results = []
    for word in VALID_WORDS:
        if can_build_word(word, tiles):
            results.append({"word": word, "score": calculate_score(word, tiles), "length": len(word)})
    return results

results = find_words(player_tiles)
print(results)
