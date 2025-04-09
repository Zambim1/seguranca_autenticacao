
# Arquitetura da API - Sistema de Autenticação

## Visão Geral

Esta API atua apenas como interface de comunicação entre o ambiente externo e a aplicação backend (que contém toda a lógica).

## Tecnologias Utilizadas

| Componente          | Tecnologia             |
|---------------------|------------------------|
| Linguagem           | Python 3.x             |
| Framework           | Flask                  |
| Banco de Dados      | MySQL (gerenciado pela aplicação) |
| ORM                 | SQLAlchemy (gerenciado pela aplicação) |
| Autenticação        | JWT                    |
| Hash de senhas      | bcrypt (gerenciado pela aplicação) |
| Proteções básicas   | Verificação de token, controle de métodos e conteúdo |
| Dependências        | requirements.txt  |

## Estrutura de Pastas do Projeto

```plaintext
/api
│
├── api/
│   ├── routes/
│   ├── middleware/
│   └── __init__.py
│
├── config/
│   └── config.py
│
├── run.py
├── requirements.txt
└── README.md
```

## Endpoints

Todos os dados recebidos e enviados serão em JSON. A API apenas repassa dados ao backend da aplicação.

| Método  | Endpoint                      | Descrição                    |
|---------|-------------------------------|------------------------------|
| POST    | /auth/register                | Enviar dados de registro     |
| POST    | /auth/login                   | Enviar dados de login        |
| GET     | /users/<id>                   | Obter dados do usuário       |
| PUT     | /users/<id>                   | Atualizar dados do usuário   |
| DELETE  | /users/<id>                   | Requisitar exclusão          |

## Segurança Básica

- Validação de formato de entrada (JSON)
- Verificação de tokens JWT nos headers
- CORS habilitado apenas para domínios permitidos
- HTTPS obrigatório em ambiente real (apenas em ambiente web real)

