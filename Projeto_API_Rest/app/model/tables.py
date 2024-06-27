from app import db

class User(db.Model):
    __tablename__ = 'Usuarios'
        
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    password = db.Column(db.String(10))

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def to_json(self):
        return {"id": self.id, "name": self.name, "password": self.password}# função para tranformar um objeto em dicionario

    