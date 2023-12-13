#!/usr/bin/python3

'''
module creates an object of class Flask and returns str
'''

from flask import Flask
from markupsafe import escape
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """
    funcion usa metodo route de app
    """
    return("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    funcion usa metodo route de app
    """
    return("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def print_text(text):
    """
    funcion usa metodo route de app
    """
    replaced_text = text.replace("_", " ")
    return(f"C {escape(replaced_text)}")


@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def print_text_python(text='is cool'):
    """
    funcion usa metodo route de app
    """
    replaced_text = text.replace("_", " ")
    return(f"Python {escape(replaced_text)}")


@app.route("/number/<int:n>", strict_slashes=False)
def print_number(n):
    """
    funcion usa metodo route de app
    """
    return(f"{escape(n)} is a number")


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """
    funcion usa metodo route de app
    """
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """
    funcion usa metodo route de app
    """
    return render_template('6-number_odd_or_even.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
