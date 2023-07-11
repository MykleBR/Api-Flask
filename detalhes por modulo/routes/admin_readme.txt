Blueprint admin_bp

O blueprint admin_bp é responsável por definir as rotas e as operações relacionadas à administração de usuários no sistema. Ele fornece endpoints para obter, criar, atualizar e excluir usuários, e requer autenticação de administrador para acessá-los.


Rota GET /users
Endpoint para obter a lista de usuários registrados no sistema. Essa rota requer autenticação JWT.
Essa rota retorna uma lista de usuários no formato JSON. Se o usuário autenticado for um administrador, serão retornados os detalhes completos de cada usuário, incluindo o ID, o nome de usuário e o status de administrador. Caso contrário, apenas o nome de usuário será retornado.


Rota POST /users
Endpoint para criar um novo usuário no sistema. Essa rota requer autenticação de administrador.
Essa rota permite a criação de um novo usuário no sistema. Os dados do novo usuário são enviados no corpo da solicitação no formato JSON, incluindo o nome de usuário e a senha. É possível especificar também se o novo usuário será um administrador, usando o campo opcional is_admin. A rota verifica se o nome de usuário já está sendo usado por outro usuário existente e retorna uma mensagem de erro em caso afirmativo.


Rota PUT /users/<user_id>
Endpoint para atualizar as informações de um usuário existente no sistema. Essa rota requer autenticação de administrador..
Essa rota retorna uma lista de usuários no formato JSON. Se o usuário autenticado for um administrador, serão retornados os detalhes completos de cada usuário, incluindo o ID, o nome de usuário e o status de administrador. Caso contrário, apenas o nome de usuário será retornado.


Rota DELETE /users/<user_id>
Endpoint para excluir um usuário do sistema. Essa rota requer autenticação de administrador.
Essa rota permite a exclusão de um usuário do sistema com base no seu ID. Antes de excluir o usuário, verifica-se a existência de um token associado a ele. Caso exista, todos os tokens associados ao usuário serão excluídos. Em seguida, o usuário é removido do banco de dados. A rota retorna uma mensagem de sucesso em caso de exclusão bem-sucedida ou uma mensagem de erro caso o usuário não seja encontrado.
