from extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    # Define a tabela 'user' no banco de dados
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password_hash = db.Column(db.String(180))
    is_admin = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        # Define a senha do usuário com base no password fornecido
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        # Verifica se a senha fornecida corresponde à senha do usuário
        return check_password_hash(self.password_hash, password)

