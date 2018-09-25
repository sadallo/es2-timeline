import os, requests
from flask import Flask, request
import psycopg2

app = Flask(__name__)

@app.route('/')
def index():
	return "Light Twitter - Modulo de Timeline - Gabriel Almeida, Gabriel Soares, Henrique Fonseca e Sadallo Andere"


# requisita ao modulo de Usuarios os usuarios seguidos por um determinado usuario
# auxiliar da funcao debaixo
@app.route('/getseguidos/<usuario>')
def getSeguidos(usuario):
	seguidos = requests.get('http://es2-usr.herokuapp.com/getfollowed/{}'.format(usuario)).content
	return seguidos


'''
AS FUNCOES ABAIXO SAO RASCUNHOS, AINDA NAO FUNCIONAM
#requisita ao modulo de mensagens dos seguidos um determinado usuario
def getMensagens(usuario):
	seguidos = requests.get('http://es2-usr.herokuapp.com/getfollowed/{}'.format(usuario)).content

	mensagens = requests.get('http://engsoft2-fbe.herokuapp.com/getMensagens/{}'.format(seguidos)).content
	return seguidos



#requisita ao modulo de mensagens de um determinado usuario
def getMensagens(usuario):
	mensagens = requests.get('http://engsoft2-fbe.herokuapp.com/getMensagens/{}'.format(usuario)).content
	return seguidos

'''


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)