from flask import Flask, render_template, request
# if run in terminal: "$ pip --version" and it shows different version from python interpreter, change interpreter to pip's version
from solver import find_words

app = Flask(__name__)

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
    app.run(debug=True, port=5002)