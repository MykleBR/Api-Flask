app.py:
responsável por criar e configurar a aplicação Flask para um projeto web.
Ele define a função create_app(), que inicializa e configura a aplicação Flask, incluindo extensões como Flask-JWT-Extended e SQLAlchemy.

Dentro do contexto da aplicação, são criadas as tabelas do banco de dados utilizando o SQLAlchemy dentro do MySQL. Em seguida, verifica-se se um usuário admin já existe no banco de dados. Caso não exista, um novo usuário admin é criado e adicionado ao banco de dados, com um nome de usuário e senha específicos(teste).

Um token de acesso é gerado para o usuário admin utilizando o Flask-JWT-Extended e armazenado no banco de dados associado ao usuário. 

Os blueprints auth_bp e admin_bp são registrados na aplicação Flask para definir as pectivamente.

Por fim, a aplicação Flask é criada e executada no servidor de desenvolvimento.