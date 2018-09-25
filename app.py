import os
from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/cadastrar/<login>&<name>&<bio>')
def cadastrar(login, name, bio):
	#Consulta().cadastrar(login, name, bio)
	return ""


@app.route('/')
def home():
	return "Light Twitter - Modulo de Timeline - Gabriel Almeida, Gabriel Soares, Henrique Fonseca e Sadallo Andere"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
