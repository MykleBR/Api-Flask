from functools import wraps
from flask import request, jsonify
from models.token import Token
from models.user import User

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Obtém o token do cabeçalho de autorização
        authorization_header = request.headers.get('Authorization')
        if not authorization_header:
            return jsonify({'message': 'Missing authorization header'}), 401

        token_string = authorization_header.split('Bearer ')[1].strip()
        if not token_string:
            return jsonify({'message': 'Invalid token'}), 401

        # Consulta do token no banco de dados
        token = Token.query.filter_by(token=token_string).first()
        if not token or token.revoked:
            return jsonify({'message': 'Invalid or expired token'}), 401

        user_id = token.user_id
        user = User.query.get(user_id)

        if not user.is_admin:
            return jsonify({'message': 'Admin access required'}), 403

        return f(*args, **kwargs)

    return decorated_function

