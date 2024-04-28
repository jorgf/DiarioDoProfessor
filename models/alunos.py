from database import db

class Aluno(db.Model):
    __tablename__ = 'alunos'

    id = db.Column(db.Integer, autoincrement=True)
    name = db.Column(db.String(), nullable=False)
    matricula = db.Column(db.String(), primary_key=True,nullable=False)

    def __init__(self, name, matricula):
        self.name = name
        self.matricula = matricula
    
    def get_by_username(name):        
        db_aluno = Aluno.query.filter(Aluno.name == name).first()
        return db_aluno
    
    def __repr__(self):
        return f"{self.id}  |  {self.name}  -  {self.matricula}"