class Config:
    # Chave secreta para criptografia de dados
    SECRET_KEY = 'Super_mega_ultra_secret_key_rsrs'
    
    # URL de conexão com o banco de dados MySQL
    # Aqui está sendo utilizado o usuário 'root' e senha 'admin' com o banco de dados 'testedb' no localhost
    SQLALCHEMY_DATABASE_URI = 'mysql://root:admin@localhost/teste_db'
    
    # Desativa o rastreamento de modificações do SQLAlchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = False

