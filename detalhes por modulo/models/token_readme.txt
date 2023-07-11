Módulo Token

O módulo Token é responsável por definir o modelo de dados e as operações relacionadas aos tokens de acesso no sistema. Esses tokens são utilizados para autenticar e autorizar os usuários nas requisições.
Classe Token

A classe Token representa um token de acesso no sistema. Ela herda da classe db.Model, que é fornecida pela extensão SQLAlchemy, permitindo a interação com o banco de dados. A classe possui os seguintes atributos:

    id: Identificador único do token de acesso (chave primária).
    user_id: Identificador do usuário associado ao token de acesso (chave estrangeira).
    token: Token de acesso (string) utilizado para autenticar e autorizar as requisições.
    revoked: Indica se o token de acesso foi revogado (booleano).
    expires_at: Data e hora de expiração do token de acesso (objeto datetime), com o valor padrão sendo o horário atual.

Método delete_tokens()

O método delete_tokens() é responsável por excluir todos os tokens de acesso associados a um usuário específico. Ele consulta o banco de dados em busca dos tokens de acesso do usuário e os exclui individualmente, em seguida, realiza um commit da sessão do banco de dados para efetivar as exclusões. Dessa forma, todos os tokens de acesso do usuário são removidos do sistema.
Utilização

A classe Token pode ser importada e utilizada em outros módulos do projeto. Ela fornece uma interface para interagir com os tokens de acesso armazenados no banco de dados. Exemplos de operações que podem ser realizadas incluem a criação de novos tokens de acesso, a revogação de tokens existentes, a verificação do status de um token de acesso e a exclusão de todos os tokens de acesso de um usuário.