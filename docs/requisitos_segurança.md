# Documento Técnico: Autenticação e Recuperação de Senha

## 1. Visão Geral

Este documento descreve os requisitos e componentes técnicos para a implementação de um sistema de autenticação seguro baseado em JWT (Access + Refresh Token) e um mecanismo seguro de recuperação de senha via token temporário enviado por e-mail. 
---

## 2. Requisitos Funcionais

### 2.1 Autenticação JWT
- Login do usuário com e-mail e senha.
- Geração de Access Token (curta duração) e Refresh Token (longa duração).
- Renovação de Access Token usando o Refresh Token.
- Logout via invalidação de Refresh Token.
- Proteção de rotas com autenticação baseada em JWT.

### 2.2 Recuperação de Senha
- Solicitação de recuperação de senha informando e-mail.
- Envio de e-mail com link contendo token temporário.
- Endpoint para redefinir a senha com validação do token recebido.

---

## 3. Requisitos Não Funcionais

- API RESTful com documentação automática via Swagger.
- Comunicação segura via HTTPS.
- Validações automáticas com Pydantic.
- Estrutura modular baseada em FastAPI + SQLAlchemy.
- Sistema de logs para rastreamento de requisições críticas.

---

## 4. Requisitos de Segurança

- Uso de `bcrypt` para hashing de senhas
- Tokens JWT assinados com chave secreta segura (via `.env`).
- Tempo de expiração configurável para Access Token e Refresh Token.
- Refresh Token armazenado de forma segura e validado no backend.
- Token de redefinição de senha com validade curta (ex: 15 minutos).
- Prevenção de vazamento de informações (mensagens de erro genéricas).
- Uso de UUIDs e headers seguros em requisições críticas.

---

## 5. Componentes Técnicos

### 5.1 Autenticação JWT

- **Login Endpoint**
  - Recebe email e senha.
  - Valida senha via `bcrypt`.
  - Gera Access Token (`15min`) e Refresh Token (`7 dias`).
  - Retorna ambos os tokens no corpo da resposta.

- **Access Token**
  - JWT contendo `sub`, `exp`, `iat`.
  - Usado no header `Authorization: Bearer <token>`.

- **Refresh Token**
  - Também um JWT, mas com maior duração.
  - Validado em endpoint específico para renovação.
  - Pode ser invalidado a qualquer momento (logout).

### 5.2 Renovação de Token

- **Endpoint** `/token/refresh`
  - Recebe Refresh Token.
  - Valida integridade e expiração.
  - Gera novo Access Token.

### 5.3 Logout

- **Endpoint** `/logout`
  - Invalida o Refresh Token atual.
  - Remove/Revoga o token armazenado (se houver persistência).

---

### 5.4 Recuperação de Senha

- **Solicitação** `/password-recovery`
  - Recebe email.
  - Gera token JWT de curta duração (`15min`).
  - Envia e-mail com link do tipo:  
    `https://seusite.com/reset-password?token=abc123...`

- **Redefinição** `/reset-password`
  - Recebe nova senha + token.
  - Valida token.
  - Atualiza a senha com novo hash via `bcrypt`.

---
## 6. Considerações Finais

- A implementação segue práticas modernas de segurança e autenticação recomendadas pela OWASP.
- O uso de JWT para autenticação e recuperação de senha por token temporário oferece escalabilidade, facilidade de integração e segurança.
- As rotas críticas estão protegidas por middlewares que validam o token de acesso.
- O sistema está pronto para uso com bancos relacionais como PostgreSQL ou MySQL, com SQLAlchemy ORM.
