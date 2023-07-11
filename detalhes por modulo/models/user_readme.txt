Módulo User

O módulo User é responsável por definir o modelo de dados e as operações relacionadas aos usuários no sistema. Ele implementa funcionalidades como o armazenamento seguro das senhas dos usuários e a verificação da correspondência entre a senha fornecida e a senha armazenada.
Classe User

A classe User representa um usuário no sistema. Ela herda da classe db.Model, fornecida pela extensão SQLAlchemy, permitindo a interação com o banco de dados. A classe possui os seguintes atributos:

    id: Identificador único do usuário (chave primária).
    username: Nome de usuário (string), único para cada usuário.
    password_hash: Hash da senha do usuário (string), armazenado de forma segura no banco de dados.
    is_admin: Indica se o usuário é um administrador (booleano).

Métodos set_password() e check_password()

O método set_password() é responsável por definir a senha do usuário com base no valor fornecido. Ele recebe a senha como parâmetro, gera o hash correspondente usando a função generate_password_hash() fornecida pela biblioteca werkzeug.security e armazena o hash na propriedade password_hash do usuário.

O método check_password() é utilizado para verificar se a senha fornecida corresponde à senha armazenada do usuário. Ele recebe a senha como parâmetro, calcula o hash correspondente e o compara com o hash armazenado na propriedade password_hash do usuário. Retorna True se a correspondência for encontrada e False caso contrário.
Utilização

A classe User pode ser importada e utilizada em outros módulos do projeto. Ela fornece uma interface para interagir com os usuários armazenados no banco de dados. Exemplos de operações que podem ser realizadas incluem a criação de novos usuários, a recuperação de usuários existentes com base em seus nomes de usuário, a definição e verificação das senhas dos usuários, e a determinação se um usuário é um administrador ou não.