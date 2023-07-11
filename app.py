from flask import Flask
from routes.auth import auth_bp
from routes.admin import admin_bp
from extensions import db, jwt
from models import User, Token
from flask_jwt_extended import create_access_token

# Função para criar e configurar a aplicação Flask
def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')  # Carrega as configurações da aplicação

    db.init_app(app)  # Inicialização da extensão SQLAlchemy
    jwt.init_app(app)  # Inicialização da extensão Flask-JWT-Extended

    with app.app_context():
        db.create_all()  # Cria as tabelas do banco de dados definidas nos modelos

        # Verifica se o usuário admin já existe no banco de dados
        admin_username = 'root'
        admin_password = 'admin'
        admin_user = User.query.filter_by(username=admin_username).first()

        if not admin_user:
            # Cria um novo usuário admin caso não exista
            admin_user = User(username=admin_username)
            admin_user.set_password(admin_password)
            admin_user.is_admin = True
            db.session.add(admin_user)
            db.session.commit()

            # Gera um token de acesso para o usuário admin
            admin_access_token = create_access_token(identity=admin_user.id)
            admin_token = Token(user_id=admin_user.id, token=admin_access_token)
            db.session.add(admin_token)
            db.session.commit()

    # Registra os blueprints para rotas de autenticação e administração
    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)

    return app

# Cria a instância da aplicação Flask
app = create_app()

if __name__ == '__main__':
    app.run()  # Inicia o servidor de desenvolvimento

