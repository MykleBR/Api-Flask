Documentação do Projeto

Para fins de teste, por padrão ao iniciar a aplicação você criará também um administrador:

username: root
password: admin

app.py:
responsável por criar e configurar a aplicação Flask para um projeto web.
Ele define a função create_app(), que inicializa e configura a aplicação Flask, incluindo extensões como Flask-JWT-Extended e SQLAlchemy.

Dentro do contexto da aplicação, são criadas as tabelas do banco de dados utilizando o SQLAlchemy dentro do MySQL. Em seguida, verifica-se se um usuário admin já existe no banco de dados. Caso não exista, um novo usuário admin é criado e adicionado ao banco de dados, com um nome de usuário e senha específicos(teste).

Um token de acesso é gerado para o usuário admin utilizando o Flask-JWT-Extended e armazenado no banco de dados associado ao usuário. 

Os blueprints auth_bp e admin_bp são registrados na aplicação Flask para definir as rotas e a lógica relacionada à autenticação e administração, respectivamente.

Por fim, a aplicação Flask é criada e executada no servidor de desenvolvimento.


config.py

contém as configurações do aplicativo. As configurações disponíveis são:

    SECRET_KEY: string (chave secreta do aplicativo)
    SQLALCHEMY_DATABASE_URI: string (URL de conexão com o banco de dados)
    SQLALCHEMY_TRACK_MODIFICATIONS: boolean (ativa ou desativa o rastreamento de modificações do SQLAlchemy)


extensions.py

contém a inicialização das extensões do Flask usadas no aplicativo. As extensões disponíveis são:

    db: SQLAlchemy para interação com o banco de dados.
    jwt: JWTManager para gerenciamento de tokens JWT.


Routes/auth.py

As rotas relacionadas à autenticação estão definidas no blueprint auth_bp.

    /register (POST): Registra um novo usuário.
        Body:
            username: string
            password: string
        Resposta:
            201: User registered successfully
            400: Invalid request or missing fields

    /login (POST): Realiza o login do usuário.
        Body:
            username: string
            password: string
        Resposta:
            200: Successful login
            401: Invalid username or password

    /logout (POST): Realiza o logout do usuário.
        Header:
            Authorization: Bearer <access_token>
        Resposta:
            200: Logged out successfully
            401: Invalid or expired token

    /token/refresh (POST): Atualiza o token de acesso do usuário.
        Header:
            Authorization: Bearer <access_token>
        Resposta:
            200: Successful token refresh
            401: Invalid or expired token

    /token/revoke (POST): revoga o token de acesso do usuário.
        Header:
            Authorization: Bearer <access_token>
        Resposta:
            200: Successful token revoked
            401: Invalid or expired token


Routes/admin.py

As rotas relacionadas à administração estão definidas no blueprint admin_bp. Essas rotas requerem autenticação JWT com um token de acesso válido.

    /users (GET):lista de usuários. Aqui os usuarios e admin vêem o mesmo conteudo, porem o admin vê mais detalhes que são ocultos a usuarios comuns
        Header:
            Authorization: Bearer <access_token>
        Resposta:
            200: Successful request
            401: Invalid or expired token
            403: Admin access required

    /users (POST): Cria um novo usuário (somente para administradores).
        Header:
            Authorization: Bearer <access_token>
        Body:
            username: string
            password: string
            is_admin: boolean (opcional)
        Resposta:
            201: User created successfully
            400: Invalid request or missing fields
            401: Invalid or expired token
            403: Admin access required

    /users/<user_id> (PUT): Atualiza um usuário (somente para administradores).
        Header:
            Authorization: Bearer <access_token>
        Parâmetros:
            user_id: integer
        Body:
            username: string (opcional)
            password: string (opcional)
            is_admin: boolean (opcional)
        Resposta:
            200: User updated successfully
            400: Invalid request
            401: Invalid or expired token
            403: Admin access required
            404: User not found

    /users/<user_id> (DELETE): Deleta um usuário (somente para administradores).
        Header:
            Authorization: Bearer <access_token>
        Parâmetros:
            user_id: integer
        Resposta:
            200: User deleted successfully
            401: Invalid or expired token
            403: Admin access required
            404: User not found


Modelos/user.py

O modelo User representa um usuário no sistema. Possui os seguintes atributos:

    id: ID do usuário (inteiro, chave primária)
    username: Nome de usuário (string, único)
    password_hash: Hash da senha do usuário (string)
    is_admin: Indica se o usuário é um administrador (booleano)


Modelos/token.py

O modelo Token representa um token de acesso no sistema. Possui os seguintes atributos:

    id: ID do token (inteiro, chave primária)
    user_id: ID do usuário associado ao token (inteiro, chave estrangeira)
    token: Token de acesso (string, único)
    revoked: Indica se o token foi revogado (booleano)
    expires_at: Data e hora de expiração do token (datetime)

O modelo Token também possui os seguintes métodos:

    revoke_tokens(): Revoga todos os tokens associados a um usuário.
    delete_tokens(): Exclui todos os tokens associados a um usuário.


Utils/decorators.py

admin_required
O decorator admin_required é usado para verificar se um usuário é um administrador antes de permitir o acesso a determinadas rotas.

