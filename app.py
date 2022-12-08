# PAGINA DE ARRANQUE DE LA APP

from flask import Flask
app = Flask(__name__)

@app.route('/')
def inicio():
    return "Hello"