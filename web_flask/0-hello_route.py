#!/usr/bin/python3

'''
module creates an object of class Flask and returns str
'''

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False) 
def hello_world():
    """
    A la funcion hello_world le añadimos el metodo route del objeto app de clase Flask con argumentos especifico para usarlo
    """
    return("Hello HBNB!")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
