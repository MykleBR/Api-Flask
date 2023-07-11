from flask import Blueprint, jsonify, request
from models.user import User
from models.token import Token 
from extensions import db
from utils.decorators import admin_required
from flask_jwt_extended import jwt_required, get_jwt_identity

# Cria o blueprint para rotas administrativas
admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/users', methods=['GET'])
@jwt_required()  # Requer autenticação JWT
def get_users():
    # Obtém todos os usuários do banco de dados
    users = User.query.all()
    current_user = User.query.get(get_jwt_identity())

    user_list = []
    for user in users:
        if current_user.is_admin:
            user_info = {'id': user.id, 'username': user.username, 'is_admin': user.is_admin}
        else:
            user_info = {'username': user.username}
        user_list.append(user_info)

    return jsonify({'users': user_list}), 200

@admin_bp.route('/users', methods=['POST'])
@admin_required  # Requer autenticação de administrador
def create_user():
    # Obtém os dados do novo usuário a ser criado
    username = request.json.get('username')
    password = request.json.get('password')
    is_admin = request.json.get('is_admin', False)

    if not username or not password:
        return jsonify({'message': 'Username and password are required'}), 400

    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({'message': 'Username already exists'}), 400

    # Cria o novo usuário
    new_user = User(username=username, is_admin=is_admin)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'}), 201

@admin_bp.route('/users/<int:user_id>', methods=['PUT'])
@admin_required  # Requer autenticação de administrador
def update_user(user_id):
    # Obtém o usuário a ser atualizado
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    # Obtém os novos dados do usuário
    username = request.json.get('username')
    password = request.json.get('password')
    is_admin = request.json.get('is_admin')

    # Atualiza as informações do usuário
    if username:
        user.username = username
    if password:
        user.set_password(password)
    if is_admin is not None:
        user.is_admin = is_admin

    db.session.commit()

    return jsonify({'message': 'User updated successfully'}), 200

@admin_bp.route('/users/<int:user_id>', methods=['DELETE'])
@admin_required  # Requer autenticação de administrador
def delete_user(user_id):
    # Consulta do token no banco de dados
    token = Token.query.filter_by(user_id=user_id).first()
    user = User.query.get(user_id)

    if user:
        if token:
            Token.delete_tokens(token)

        # Exclui o usuário do banco de dados
        db.session.delete(user)
        db.session.commit()

        return jsonify({'message': 'User deleted successfully'}), 200
    else:
        return jsonify({'message': 'User not found'}), 404

