from flask import render_template, request, redirect, session, flash, url_for
from app import app
from datetime import date
from models.users import User
from models.alunos import Aluno
from database import db

@app.route('/')
def index():
    lista_atv = ['Cronograma de aulas', 'Lançamento de notas', 'Relatórios']
    return render_template('index.html', titulo_header='Diário de Classe', atividades=lista_atv)

@app.route('/home')
def home():
    return render_template('home.html', titulo_header='Ambiente de trabalho')

@app.route('/listar-usuarios')
def list_all():
    users = User.query.order_by(User.id)
    return render_template('listarUsers.html', titulo_header='DC', users=users)

@app.route('/listar-estudantes')
def listar_estudantes():
    users = User.query.order_by(User.id).filter_by(role='estudante')
    return render_template('listarUsers.html', titulo_header='DC', users=users)

@app.route('/create-user', methods=['GET','POST'])
def create_user():
    if request.method == 'POST':
        name = request.form['name']
        role = request.form['select']
        user_exist = User.get_by_username(name)

        if user_exist:

            flash(f'Usuario {name} já cadastrado!', 'flash-error')
            return redirect(url_for('index'))
        
        user = User(name=request.form['name'],created_at=date.today(),role=role)
        db.session.add(user)
        db.session.commit()
        flash('Usuário cadastrado com sucesso', 'flash-success')
        return redirect(url_for('index'))
    return render_template('createUsers.html', titulo_header='DC')

@app.route('/login')
def login():
    # next = request.args.get('next')
    next='home'
    return render_template('login.html', titulo_header='Login', next=next)

@app.route('/auth', methods=['POST'])
def auth():
    #TODO-multiplos usuarios
    if '1234' == request.form['password']:
        session['user_login'] = request.form['user_name']
        next_page = request.form['next']
        flash('Usuário logado com sucesso!', 'flash-success')
        return redirect(next_page)
    else:
        flash('Usuario e/ou senha incorreto(s)!', 'flash-error')
        return redirect(url_for('login'))
    
@app.route('/logout')
def logout():
    session['user_login'] = None
    return redirect(url_for('index'))

@app.route('/lancar-notas')
def lancar_notas():
    if 'user_login' not in session or session['user_login'] is None:
        return redirect(url_for('login', next=url_for('lancar_notas'))) # pegar a página inicial 
    return render_template('notas.html', titulo_header='Notas das avaliações')

@app.route('/salvar-notas', methods=['POST'])
def salvar_notas():
    nome = request.form['user_name']
    nota = request.form['user_nota']
    return redirect(url_for('lancar_notas')) # armazer em um arquivo ou db