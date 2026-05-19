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

with open ("dictionary.txt") as f:
    VALID_WORDS = set(word.strip().lower() for word in f)
# set of all valid words in compliance with an online scrabble dictionary



def validate_tiles(tiles):

    ALLOWED_CHARACTERS = "abcdefghijklmnopqrstuvwxyz*"

    if len(tiles) > 15:

        return "You cannot input more than 15 tiles since a standard scrabble board has 15 rows and 15 columns."

    if len(tiles) == 0:

        return "Please enter at least one tile."

    for character in tiles:

        if character not in ALLOWED_CHARACTERS:

            return "Only letters a-z and '*' are allowed."

    return None

def can_build_word(word, tiles):
    tile_count = Counter(tiles)

    blanks = tile_count["*"]
    del tile_count["*"]

    for letter, needed in Counter(word).items():
        available = tile_count.get(letter, 0)

        if available < needed:
            if blanks >= needed - available:
                blanks -= needed - available
            else:
                return False
    return True

def calculate_score(word, tiles):
    tile_count = Counter(tiles)

    blanks = tile_count["*"]
    del tile_count["*"]
    
    score = 0
    
    for letter in word:
        if tile_count.get(letter, 0) > 0:
            score += LETTER_POINTS[letter]
            tile_count[letter] -= 1

        elif blanks > 0:
            blanks -= 1

    return score

def find_words(tiles):
    results = []

    for word in VALID_WORDS:
        if len(word) > len(tiles):
            continue
        if len(word) < 2:
            continue

        if can_build_word(word, tiles):
            results.append({
                "word": word, 
                "score": calculate_score(word, tiles), 
                "length": len(word)
            })
    results.sort(key=lambda x: (-x["score"], -x["length"], x["word"]))   
    
    return results[:1000]