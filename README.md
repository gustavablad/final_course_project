**Scrabble Solver**

This project is a web-based Scrabble solver built using Flask and Python.
Enter the letters on your tile rack and the solver returns the 1000 highest scoring valid words, ranked by point value.

**Features**
- Support for blank tiles: Use "*" to represent a blank tile (wild card, worth 0 points)
- Full dictionary lookup: Validates words against a standard Scrabble word list.
- Score calculation: Results get sorted by point value, then word lenght.
- Input validation: Error messages for invalid characters or too short/long of an input.
- Responsive UI: Works on both desktop and mobile screens.

**Getting started**

*Dependencies:*

- Python 3.10+

- Flask

*Installment order*

1. Clone the repository:

    bash

    git clone https://github.com/gustavablad/scrabble_solver.git

    cd scrabble-solver

2. Install dependencies:
    
    bash

    pip install flask

    (make sure python interpreter version is the same as the version that pip is running)

3. Run the app:

    bash

    python app.py

4. Open in your browser:

    bash

    https://localhost:5002

**Usage**

*input:*

- a-z (regular letter tile)

- * (blank tile, wild card)

Example: typing aeinrst returns words like "nastier", "retains", "stainer" 

Maximum of 15 tiles (length of scrabble board row and column)

Only letters a-z and * are accepted as valid input values.

**Authors:**

Github user gustavablad: https://github.com/gustavablad

Contact information: gustav.ablad@edu.huddinge.se
