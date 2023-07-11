Blueprint auth_bp

O blueprint auth_bp é responsável por lidar com as operações relacionadas à autenticação de usuários no sistema. Ele fornece endpoints para registro, login, logout e atualização de tokens de acesso. Além disso, o auth_bp também permite a integração com provedores de autenticação de terceiros, como o Google.


Rotas de Autenticação (auth_bp)
Rota POST /register
Endpoint para registrar um novo usuário no sistema.
Essa rota permite o registro de um novo usuário no sistema. É necessário fornecer um nome de usuário e uma senha. O endpoint retorna uma mensagem de sucesso em caso de registro bem-sucedido ou uma mensagem de erro caso o nome de usuário já esteja em uso ou os campos não sejam fornecidos corretamente.


Rota POST /login
Endpoint para realizar o login do usuário.
Essa rota permite que o usuário faça login no sistema. É necessário fornecer um nome de usuário e uma senha. Se as credenciais forem válidas, um token de acesso e um token de atualização são gerados. O token de acesso é usado para autenticar solicitações posteriores e o token de atualização é usado para obter um novo token de acesso quando necessário. Os tokens são registrados no banco de dados para fins de controle de autenticação.


Rota POST /logout
Endpoint para encerrar a sessão do usuário e revogar o token de acesso.
Essa rota permite que o usuário encerre sua sessão e revogue o token de acesso. O usuário precisa enviar o token de acesso no cabeçalho de autorização. O token é verificado e, se válido, é excluído do banco de dados, encerrando a sessão do usuário.


Rota POST /token/refresh
Endpoint para atualizar o token de acesso do usuário com base no token de atualização.
Essa rota permite atualizar o token de acesso do usuário com base no token de atualização. O usuário precisa estar autenticado e fornecer um token de atualização válido. O token de acesso anterior é excluído do banco de dados e um novo token de acesso é gerado e retornado como resposta.


Rota POST /token/revoked
Endpoint para revogar o token de acesso do usuário.
Essa rota permite revogar o token de acesso do usuário atual. O usuário precisa estar autenticado e enviar o token de acesso no cabeçalho de autorização. O token é marcado como revogado no banco de dados.


Rota GET /login/google/callback
Endpoint para autenticação com o Google.
Essa rota é responsável por realizar o fluxo de autenticação com o Google. Ela é acionada após a interação do usuário com a página de login do Google. Nessa rota, você pode implementar a lógica para obter o código de autorização do Google, trocar o código por um token de acesso, obter informações do usuário do Google e realizar o registro ou autenticação do usuário no sistema. A implementação detalhada dessas etapas pode variar dependendo da biblioteca ou estratégia utilizada para a autenticação com o Google.

PS:Substitua <GOOGLE_CLIENT_ID>, <GOOGLE_CLIENT_SECRET> e <GOOGLE_USER_ID> pelas suas próprias credenciais e identificadores do Google.