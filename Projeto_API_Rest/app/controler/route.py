from app import app, db
from flask import Flask, make_response, jsonify, request, render_template, url_for, redirect, Response
from app.model.bd import Users
from app.model.tables import User
import json



@app.route('/usuarios', methods=['GET'])#decorator(@app: para marcar a função get_usuarios dizendo para o flask que é uma rota da API para visualizar o db)
def get_usuarios():# função para retornar a lista de usuarios do db
    return make_response(jsonify(
        Mensagem='Lista de Usuarios',
        Dados=Users
    )
)

@app.route('/usuarios',methods=['POST'])
def create_usuarios(): # função pra criar usuarios
    usuario =  request.json # retorna o que foi enviado
    Users.append(usuario) # adicionar a db(função append e uma função de python para trabalhar com listas e adicionar ao final da lista)
    return make_response(jsonify(
        Mensagem='Carro cadastrado com Sucesso',
        Dado=usuario
    )
)

#================================================================================================================================================

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('usuario.html')


##-----CRUD------#
#Selecionar todo
#Selecionar um
#Cadastrar
#Atualizar
#Deletar

@app.route('/select', methods=['GET'])
def select():
    select_user = User.query.all()# retorna um objeto (uma lista)
    usuario_json = [usuario.to_json() for usuario in select_user]# criando uma lista e aplicando o metodo 'to_json' em todos da lista
    print(usuario_json)
    return Response(json.dumps(usuario_json))#A função json.dumps() converterá um subconjunto de objetos Python em uma string json. Nem todos os objetos são conversíveis e pode ser necessário criar um dicionário de dados que deseja expor antes de serializar para JSON.
 

@app.route('/add', methods=['GET','POST'])
def add_user():
    if request.method == 'POST':
        usuario = User(request.form['name'], request.form['password'])
        db.session.add(usuario)
        db.session.commit()
        return redirect(url_for('index'))
    return 'Erro'
