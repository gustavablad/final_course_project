from flask import Flask, render_template, request
# if run in terminal: "$ pip --version" and it shows different version from python interpreter, change interpreter to pip's version
from collections import Counter

app = Flask(__name__)

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

#player_tiles = input(
#    "What tiles do you have? " \
#    "Use only the letters on the tiles and '*' for blank tiles. " \
#    "Do not use any commas or periods. " \
#    "Example of rack with 7 tiles: e*git*r. : "
#).lower()

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
    
    return results[:100]

@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    tiles = ""
    
    if request.method == "POST":
        tiles = request.form["tiles"].lower()
        results = find_words(tiles)
    
    return render_template(
        "index.html", 
        results=results, 
        tiles=tiles
    )

if __name__ == "__main__":
    app.run(debug=True, port=5000)