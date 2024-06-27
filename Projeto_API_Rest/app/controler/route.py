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


##-------------------------------CRUD------------------------------------#



#==========Selecionar todo=============#

def gera_response(status, nome_do_conteudo, conteudo, mensagem=False):# função criada mostrar qual o conteudo do banco e uuma mensagem se necessario
    body = {}
    body[nome_do_conteudo] = conteudo
    if(mensagem):
        body["mensagem"]= mensagem

    return Response(json.dumps(body), status=status, mimetype="aplication/json")

@app.route('/select', methods=['GET'])
def select():
    select_all = User.query.all()# retorna um objeto (uma lista)
    usuario_json = [usuario.to_json() for usuario in select_all]# criando uma lista e aplicando o metodo 'to_json' em todos da lista
    print(usuario_json)
    #return Response(json.dumps(usuario_json)) A função json.dumps() converterá um subconjunto de objetos Python em uma string json. Nem todos os objetos são conversíveis e pode ser necessário criar um dicionário de dados que deseja expor antes de serializar para JSON.
    return gera_response(200,"usuarios", usuario_json, "ok")
 

#===============Selecionar um====================#

@app.route("/selectuser/<id>", methods=["GET"])
def selec_user(id):
    select_user = User.query.filter_by(id=id).first()#filter_by(id=id) é para filtrar apenas um ususario o banco o .first() e para retornar apenas um objeto(com a busca e por ID não há problema porque e primari key e so existe um)
    usuario_json = select_user.to_json()
    print(usuario_json)
    return gera_response(200, "usuario", usuario_json)
    



#=================Cadastrar======================#

@app.route("/add", methods=["POST"])
def cadastro_user():
    #validar se recebeu os parametros
    #ou utilizar try catch para gerar erro

    body = request.get_json()

    try:
        usuario = User(name=body["name"], password=body["password"])
        db.session.add(usuario)
        db.session.commit()
        return gera_response(201, "usuario", usuario.to_json(), "Criado com sucesso")
    except Exception as e:
        print("Erro",e)
        return gera_response(400, "", {}, "Erro ao cadastrar")


#=================Atualizar======================#
@app.route("/atualiza/<id>", methods=["PUT"])
def atualiza_user(id):
    #selecioana usuario
    #seleciona modificações
    
    selec_user = User.query.filter_by(id=id).first()
    body = request.get_json()

    try:
        if('name'  in body):
            selec_user.name = body['name']
        if('password' in body):
            selec_user.password = body['password']

            db.session.add(selec_user)
            db.session.commit()
            return gera_response(200, "usuario", selec_user.to_json(), "Atualizado com Sucesso")
    except Exception as e:
        return gera_response(400, "usuario", {}, "Erro ao atualizar")


#==================Deletar=======================#
@app.route('/delete/<id>',methods=["DELETE"])
def delet_user(id):
    selec_user = User.query.filter_by(id=id).first()

    try:
        db.session.delete(selec_user)
        db.session.commit()
        return gera_response(200, "usuario", selec_user.to_json(),"Deletado com sucesso")
    except Exception as e:
        return gera_response(400,"usuario",{}, "Erro ao deletar")