from flask import Blueprint, jsonify, url_for, request
from models.user import User
from models.token import Token
from models.refresh_token import RefreshToken
from extensions import db
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, create_refresh_token

# Cria o blueprint para rotas de autenticação
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    # Registra um novo usuário
    username = request.json.get('username')
    password = request.json.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required'}), 400

    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({'message': 'Username already exists'}), 400

    new_user = User(username=username)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required'}), 400

    user = User.query.filter_by(username=username).first()
    if not user or not user.check_password(password):
        return jsonify({'message': 'Invalid username or password'}), 401

    # Geração do token de acesso e token de atualização
    access_token = create_access_token(identity=user.id)
    refresh_token = create_refresh_token(identity=user.id)

    # Registro do token de acesso no banco de dados
    access_token_entry = Token(user_id=user.id, token=access_token)
    db.session.add(access_token_entry)

    # Registro do token de atualização no banco de dados
    refresh_token_entry = RefreshToken(user_id=user.id, token=refresh_token)
    db.session.add(refresh_token_entry)

    db.session.commit()

    return jsonify({'access_token': access_token, 'refresh_token': refresh_token}), 200

@auth_bp.route('/logout', methods=['POST'])
def logout():
    # Encerra a sessão do usuário e revoga o token de acesso
    authorization_header = request.headers.get('Authorization')
    token = authorization_header.split(' ')[1] if authorization_header else None

    if not token:
        return jsonify({'message': 'Token is missing'}), 401

    token = Token.query.filter_by(token=token).first()
    if not token or token.revoked:
        return jsonify({'message': 'Invalid or expired token'}), 401

    db.session.delete(token)
    db.session.commit()

    return jsonify({'message': 'Logged out successfully'}), 200

@auth_bp.route('/token/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh_token():
    # Atualiza o token de acesso com base no token de atualização
    current_user = get_jwt_identity()

    # Exclui o token antigo do usuário
    Token.query.filter_by(user_id=current_user).delete()

    # Cria um novo token para o usuário
    new_token = Token(user_id=current_user, token=create_access_token(identity=current_user))
    db.session.add(new_token)
    db.session.commit()

    access_token = new_token.token
    return jsonify({'access_token': access_token}), 200

@auth_bp.route('/token/revoked', methods=['POST'])
@jwt_required()
def revoke_token():
    # Captura o usuario atual
    current_user = get_jwt_identity()

    token = Token.query.filter_by(user_id=current_user).first()

    if not token:
       return jsonify({'message': 'Token not found'}), 404

    # Revoga o token
    token.revoked = True
    db.session.commit()

    return jsonify({'message': 'Token revoked successfully'}), 200

@auth_bp.route('/login/google/callback', methods=['GET'])
def google_callback():
    # Realiza o fluxo de autenticação com o Google

    # Obtém o código de autorização do Google
    google_client_id = '<GOOGLE_CLIENT_ID>'
    google_client_secret = '<GOOGLE_CLIENT_SECRET>'
    authorization_code = request.args.get('code')

    # Troca o código de autorização por um token de acesso
    token_endpoint = 'https://accounts.google.com/o/oauth2/token'
    redirect_uri = url_for('auth.google_callback', _external=True)

    data = {
        'code': authorization_code,
        'client_id': google_client_id,
        'client_secret': google_client_secret,
        'redirect_uri': redirect_uri,
        'grant_type': 'authorization_code'
    }

    response = request.post(token_endpoint, data=data)
    if response.status_code == 200:
        token_data = response.json()
        access_token = token_data['access_token']
        id_token = token_data['id_token']

        # Obter o ID do usuário do Google a partir do token JWT (id_token)
        # Decodificar o token JWT para obter as informações do usuário
        # Exemplo: verificar o campo 'sub' para obter o ID do usuário

        # Verificar se o ID do usuário do Google já está registrado em seu sistema
        user = User.query.filter_by(google_id='<GOOGLE_USER_ID>').first()  # Substitua <GOOGLE_USER_ID> pelo ID do usuário do Google

        if user:
            # Atualizar a senha do usuário existente com o novo código de autorização
            user.password = authorization_code
            db.session.commit()
        else:
            # Criar um novo usuário com o código de autorização como senha
            user = User(google_id='<GOOGLE_USER_ID>', password=authorization_code)  # Substitua <GOOGLE_USER_ID> pelo ID do usuário do Google
            db.session.add(user)
            db.session.commit()

        # Gera um novo token de acesso para o usuário
        access_token = create_access_token(identity=user.id)
        
        # Registra o token no banco de dados
        token = Token(user_id=user.id, token=access_token)
        db.session.add(token)
        db.session.commit()

        # Retorna o token de acesso como resposta JSON
        return jsonify({'access_token': access_token})
    else:
        return jsonify({'message': 'Failed to exchange authorization code for access token'}), 400

