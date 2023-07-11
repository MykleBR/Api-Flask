O arquivo decorators.py contém o decorator admin_required, que é usado para proteger rotas e exigir autenticação de administrador.

Este decorator é usado para verificar se o usuário autenticado é um administrador antes de permitir o acesso a determinadas rotas. Ele extrai o token de acesso do cabeçalho de autorização, verifica se o token é válido e não foi revogado. Em seguida, consulta o usuário associado ao token e verifica se ele é um administrador. Se o usuário não for um administrador, é retornado um código de status 403 (acesso proibido). Caso contrário, a função original é chamada.

O decorator é aplicado usando a sintaxe @admin_required acima das rotas que exigem acesso de administrador. Isso garante que apenas usuários autenticados como administradores possam acessar essas rotas.