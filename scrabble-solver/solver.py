from collections import Counter


# Constants 


# Letter values based on standard Scrabble scoring
LETTER_POINTS = {
    "a": 1, "b": 3, "c": 3, "d": 2, "e": 1, 
    "f": 4, "g": 2, "h": 4, "i": 1, "j": 8, 
    "k": 5, "l": 1, "m": 3, "n": 1, "o": 1, 
    "p": 3, "q": 10, "r": 1, "s": 1, "t": 1, 
    "u": 1, "v": 4, "w": 4, "x": 8, "y": 4,
    "z": 10, 
}

# Load the dictionary of valid words into a set for fast lookup
with open ("dictionary.txt") as f:
    VALID_WORDS = set(word.strip().lower() for word in f)


# Validation


def validate_tiles(tiles):
    """
    Validates the input tiles for the Scrabble solver.
    Checks for length constraints and allowed characters.
    Returns an error message if validation fails, or None if the input is valid.

    Rules:
    - Maximum of 15 tiles (since a standard Scrabble board has 15 rows and 15 columns)
    - At least 1 tile must be entered
    - Only lowercase letters a-z and '*' (representing blank tiles) are allowed
    """
    ALLOWED_CHARACTERS = "abcdefghijklmnopqrstuvwxyz*"

    if len(tiles) > 15:
        return "You cannot input more than 15 tiles since a standard scrabble board has 15 rows and 15 columns."
    
    if len(tiles) == 0:
        return "Please enter at least one tile."

    for character in tiles: 
        if character not in ALLOWED_CHARACTERS:
            return "Only letters a-z and '*' are allowed."

    return None # No validation errors


# Core logic


def can_build_word(word, tiles):
    """
    Returns True if the given word can be built using the provided tiles.

    Blanks (represented by '*') can be used as wildcards for any letter.
    Uses a Counter to count the frequency of each letter in the tiles and the word, and checks if the word can be formed with the available tiles.
    If the word requires more of a certain letter than is available in the tiles, it checks if there are enough blanks to cover the difference. 
    If not, it returns False. If all letters can be covered by the tiles and blanks, it returns True.
    """
    
    tile_count = Counter(tiles)

    # Remove blanks from the tile count and keep track of how many there are
    blanks = tile_count["*"]
    del tile_count["*"]

    for letter, needed in Counter(word).items():
        available = tile_count.get(letter, 0)

        if available < needed:
            # If there are not enough of the letter available, check if blanks can cover the difference
            if blanks >= needed - available:
                blanks -= needed - available
            else:
                return False # Not enough tiles or blanks to cover the needed letters
            
    return True


def calculate_score(word, tiles):
    """
    Calculates the Scrabble score for a given word based on the provided tiles.
    
    Blanks (represented by '*') do not contribute to the score, but can be used as wildcards for any letter. 
    The function mirrors the logic of can_build_word to determine which letters are covered by actual tiles and which are covered by blanks, and only adds points for the letters covered by actual tiles.
    """
    tile_count = Counter(tiles)

    blanks = tile_count["*"]
    del tile_count["*"]
    
    score = 0
    
    for letter in word:
        if tile_count.get(letter, 0) > 0:
            # Use the tile for this letter and add its points to the score
            score += LETTER_POINTS[letter]
            tile_count[letter] -= 1
        elif blanks > 0:
            # Use a blank for this letter (no points added)
            blanks -= 1

    return score



def find_words(tiles):
    """
    Finds all valid words that can be formed with the given tiles and calculates their scores.
    
    Returns a list of dictionaries containing the word, its score, and its length, sorted by score (descending), then by length (descending), and then alphabetically.
    Only returns the top 1000 results to ensure performance.
    """
    
    results = []

    for word in VALID_WORDS:
        # Skip words that are longer than the number of tiles, since they cannot be formed
        if len(word) > len(tiles):
            continue

        # Skip words that are too short (1 letter or less), since they are not valid Scrabble words
        if len(word) < 2:
            continue

        if can_build_word(word, tiles):
            results.append({
                "word": word, 
                "score": calculate_score(word, tiles), 
                "length": len(word)
            })
    
    # Sort results by score (descending), then by length (descending), and then alphabetically
    results.sort(key=lambda x: (-x["score"], -x["length"], x["word"]))   
    
    # Limit results to top 1000 to ensure fast response times
    return results[:1000]