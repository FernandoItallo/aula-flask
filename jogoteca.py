from flask import Flask, render_template, request, redirect
from model.Jogo import Jogo


app = Flask(__name__)

lista_jogos = []

jogo1 = Jogo('super mario', 'Ação', 'SNES')
jogo2 = Jogo('Pokemon Gold', 'RPG', 'GBA')

lista_jogos.append(jogo1)
lista_jogos.append(jogo2)


@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista_jogos)


@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Jogo')


@app.route('/criar', methods=['POST',])
def criar():
    nome = request. form['nome']
    categoria = request. form['categoria']
    console = request. form['console']
    jogo = Jogo(nome, categoria, console)
    lista_jogos.append(jogo)
    return redirect('/')


app.run(debug=True)
