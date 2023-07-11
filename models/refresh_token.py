from extensions import db
from datetime import datetime

class RefreshToken(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    token = db.Column(db.String(500), unique=True)
    revoked = db.Column(db.Boolean, default=False)
    expires_at = db.Column(db.DateTime, default=datetime.utcnow)

    def revoke(self):
        # Revoga o token de atualização
        self.revoked = True
        db.session.commit()
        
        