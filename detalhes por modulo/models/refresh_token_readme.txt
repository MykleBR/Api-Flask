Módulo RefreshToken

O módulo RefreshToken é responsável por definir o modelo de dados e as operações relacionadas aos tokens de atualização no sistema. Esses tokens são utilizados para atualizar o status do token de acesso.
Classe RefreshToken

A classe RefreshToken representa um token de atualização no sistema. Ela herda da classe db.Model, que é fornecida pela extensão SQLAlchemy, permitindo a interação com o banco de dados. A classe possui os seguintes atributos:

    id: Identificador único do token de atualização (chave primária).
    user_id: Identificador do usuário associado ao token de atualização (chave estrangeira).
    token: Token de atualização (string) utilizado para atualizar o status do token de acesso.
    revoked: Indica se o token de atualização foi revogado (booleano).
    expires_at: Data e hora de expiração do token de atualização (objeto datetime), com o valor padrão sendo o horário atual.

Método revoke()

O método revoke() é responsável por revogar o token de atualização. Ao ser chamado, ele define o atributo revoked como True e realiza um commit da sessão do banco de dados. Dessa forma, o token de atualização é marcado como revogado e não pode mais ser utilizado para atualizar o token de acesso. A revogação do token de atualização é importante para garantir a segurança e controlar o acesso aos recursos protegidos.
Utilização

A classe RefreshToken pode ser importada e utilizada em outros módulos do projeto. Ela fornece uma interface para interagir com os tokens de atualização armazenados no banco de dados. Exemplos de operações que podem ser realizadas incluem a criação de novos tokens de atualização, a revogação de tokens existentes e a verificação do status de um token de atualização