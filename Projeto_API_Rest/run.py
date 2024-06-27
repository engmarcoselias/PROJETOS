from app import app, db


if __name__ == '__main__':
    app.run(debug= True)# estartar o servidor
    with app.app_context():
        db.create_all() #criar as tabelas no banco de dados
    