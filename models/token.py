from datetime import datetime
from extensions import db

class Token(db.Model):
    # Define a tabela 'Token' no banco de dados
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    token = db.Column(db.String(500), unique=True)
    revoked = db.Column(db.Boolean, default=False)
    expires_at = db.Column(db.DateTime, default=datetime.utcnow)

    def delete_tokens(self):
        # Exclui todos os tokens associados ao usuário
        tokens = Token.query.filter_by(user_id=self.id).all()
        for token in tokens:
            db.session.delete(token)
        db.session.commit()

