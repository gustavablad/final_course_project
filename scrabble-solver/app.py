from flask import Flask, render_template, request
from solver import find_words, validate_tiles

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    """
    Renders the main page and handles form submissions for tile input.
    
    GET: Displays the form for tile input.
    POST: Validates the input tiles and finds valid words based on the input.
    """
    results = []
    tiles = ""
    error = None

    if request.method == "POST":
        # Get the input tiles from the form and make them lowercase, then validate them
        tiles = request.form["tiles"].lower()
        error = validate_tiles(tiles)

# If there are no validation errors, find valid words based on the input tiles
    if error is None:
        results = find_words(tiles)
    
    return render_template(
        "index.html", 
        results=results, 
        tiles=tiles,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True, port=5002)