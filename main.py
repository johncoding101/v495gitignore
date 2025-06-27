# - coding: utf-8 -_-
'''
Created on Wednesday Jun 25 20:25:10 2025
Udemy -100 Days of code (Angela Yu)
video -495  Gitignore
Author: JohnC
'''

# *   Gitignore

import os
from flask import Flask
from getname import random_name
from dotenv import load_dotenv


load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("FLASK_KEY")


@app.route("/")
def hello_world():
    """_summary_

    Returns:
        _type_: _description_
    """
    return f"<h1>Behold, I am {random_name('superhero')}!</h1>"


if __name__ == "__main__":
    app.run(debug=True, port=5000)
