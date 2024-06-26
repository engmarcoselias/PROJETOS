from app import app, db
from app.model.tables import User
from flask import Flask,render_template, url_for, request, redirect




@app.route('/default/<int:num>') # pagina teste de arquivo estatico e rota com variavel no URL
def default(num):
    return render_template('default.html', num = num)


@app.route('/')
def index():
    usuarios = User.query.all()
    return render_template('index.html', usuarios = usuarios)

@app.route('/add', methods=['GET','POST'])
def add():
    if request.method == 'POST':
        usuario = User(request.form['nome'], request.form['password'])
        db.session.add(usuario)
        db.session.commit() 
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
     usuario = User.query.get(id)
     if request.method == 'POST':
        usuario.nome = request.form['nome']
        usuario.password = request.form['password']
        db.session.commit()
        return redirect(url_for('index'))
     return render_template('edit.html', usuario = usuario)

@app.route('/delete/<int:id>')
def delete(id):
        usuario = User.query.get(id)
        db.session.delete(usuario)
        db.session.commit()
        return redirect(url_for('index'))




   
   