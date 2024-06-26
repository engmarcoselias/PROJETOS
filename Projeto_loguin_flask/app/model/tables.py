from app import db

class User(db.Model):
    
    id = db.Column('id',db.Integer, primary_key=True, autoincrement = True)
    nome = db.Column(db.String(128))
    password = db.Column(db.String)

    def __init__(self, nome, password):
        self.nome = nome
        self.password = password
