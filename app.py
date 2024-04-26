from flask import Flask, render_template, request, redirect, session, flash, url_for

app = Flask(__name__)

# secret_key -> necessario para armazenar dados na sessão
app.config['SECRET_KEY'] = 'projeto_estudo'

@app.route('/')
def index():
    lista_atv = ['Cronograma de aulas', 'Lançamento de notas', 'Relatórios']
    return render_template('index.html', titulo_header='Diário de Classe', atividades=lista_atv)

@app.route('/login')
def login():
    next = request.args.get('next')
    return render_template('login.html', titulo_header='Login', next=next)

@app.route('/auth', methods=['POST'])
def auth():
    #TODO-multiplos usuarios
    if '1234' == request.form['password']:
        session['user_login'] = request.form['user_name']
        next_page = request.form['next']
        flash('Usuário logado com sucesso!', 'flash-sucess')
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
app.run(debug=True) # executar  -> app.run(host='0.0.0.0', port=8080)