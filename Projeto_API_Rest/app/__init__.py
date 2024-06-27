from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__) # instanciando uma variavel Flask e passando nome do model (__name__ assume o nome do projeto)
app.json.sort_keys = False # por padão o flask ordena a resposta dos objetos JSON em ordem alfabetica, esse comando e para desabilitar essa função
app.config.from_object('config')
db= SQLAlchemy(app)
migrate = Migrate(app, db)

from .controler import route