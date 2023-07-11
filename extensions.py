from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

# Instância do SQLAlchemy para integração com o banco de dados
db = SQLAlchemy()

# Instância do JWTManager para autenticação baseada em tokens JWT
jwt = JWTManager()

