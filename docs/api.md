# Arquitetura da API - Sistema de Autenticação e Administração de Usuários

## Visão Geral
A API será desenvolvida em **Python** utilizando o framework **Flask** e seguirá os princípios da arquitetura **RESTful**. O sistema será modular, seguro e escalável, garantindo integração futura com outras aplicações.

## Tecnologias Utilizadas

- **Linguagem**: Python 3.x
- **Framework**: Flask
- **Banco de Dados**: MySQL
- **ORM**: SQLAlchemy
- **Autenticação**: JWT (JSON Web Token)
- **Criptografia**: bcrypt para hash de senhas
- **Controle de Acesso**: RBAC (Role-Based Access Control)
- **Documentação da API**: Swagger (Flasgger) ou Redoc
- **Gerenciamento de Dependências**: Poetry / Pipenv
- **Serviços de Log**: Logging nativo do Python + armazenamento em banco
- **Padrão de Arquitetura**: MVC (Model-View-Controller) + DAO (Data Access Object)

## Estrutura de Pastas do Projeto

```plaintext
/api
│── app/
│   ├── controllers/     # Lógica de negócios e processamento de requisições
│   ├── models/          # Definições das tabelas e classes do banco de dados
│   ├── routes/          # Rotas da API
│   ├── services/        # Serviços auxiliares (hashing, envio de email, etc.)
│   ├── middlewares/     # Interceptadores para segurança e logs
│   ├── utils/           # Funções auxiliares
│   ├── config.py        # Configuração geral do sistema
│   ├── database.py      # Conexão e inicialização do banco de dados
│── tests/               # Testes unitários e de integração
│── migrations/          # Controle de versão do banco de dados
│── requirements.txt     # Dependências do projeto
│── wsgi.py              # Ponto de entrada para execução do Flask
```

## Padrão de Rotas e Endpoints
A API seguirá um padrão RESTful, com endpoints organizados por recursos.

### Endpoints

| Método  | Endpoint                      | Descrição |
|---------|--------------------------------|-------------|
| `POST`  | `/auth/register`               | Cadastro de usuário |
| `POST`  | `/auth/login`                  | Login e geração de token JWT |
| `POST`  | `/auth/logout`                 | Logout do usuário |
| `POST`  | `/auth/reset-password`         | Envio de e-mail para redefinição de senha |
| `PUT`   | `/auth/reset-password/confirm` | Redefinição de senha |
| `GET`   | `/users`                        | Listagem de usuários (admin) |
| `GET`   | `/users/<id>`                   | Detalhes de um usuário |
| `PUT`   | `/users/<id>`                   | Atualização de informações do usuário |
| `DELETE`| `/users/<id>`                   | Exclusão de conta |

## Segurança e Autenticação

- **JWT**: Tokens serão assinados usando uma chave secreta segura.
- **MFA (Opcional)**: Suporte para autenticação multifator.
- **Proteção contra brute-force**: Bloqueio temporário após múltiplas tentativas de login.
- **Controle de Permissões (RBAC)**: Cada endpoint exigirá permissões específicas baseadas no papel do usuário.


