from flask import Flask
from flask_migrate import Migrate
from database import db

app = Flask(__name__)

app.config.from_pyfile('config.py')

#db
db.init_app(app)
from models.users import User
from models.alunos import Aluno
migrate = Migrate(app, db)

#rotas
from views import *

if __name__ == '__main__':
    app.run(debug=True) # app.run(debug=True,host='0.0.0.0', port=8080)