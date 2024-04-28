from database import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(), nullable=False)
    created_at = db.Column(db.Date, nullable=False)
    role = db.Column(db.String(), nullable=False)

    #ADICIONAR RESTRICOES
    # __table_args__ =(
    #       db.CheckConstrains(role.in_(['estudante','professor','admin']),name='role_types')
    # )
    def __init__(self, name, created_at, role):
        self.name = name
        self.created_at = created_at
        self.role = role
    
    def get_by_username(username):        
        db_user = User.query.filter(User.name == username).first()
        return db_user
    
    def __repr__(self):
        return f"{self.id}  |  {self.name}  -  {self.role}"