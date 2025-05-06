# seguranca_autenticacao

---

## 📁 Estrutura de Pastas

```
src/
├── database/            # Configuração de conexão com o banco de dados (engine, sessão, Base)
├── models/              # Schemas Pydantic + modelos ORM com SQLAlchemy
│   ├── user.py          # User, Role e seus schemas
│   └── message.py       # Message e schemas para envio e resposta
├── routes/              # Rotas da aplicação (Endpoints FastAPI)
│   ├── auth.py          # Login (JWT)
│   ├── user.py          # Cadastro, listagem e update de usuários
│   └── message.py       # Envio e recebimento de mensagens criptografadas
├── services/            # Regras de negócio (criptografia, persistência, validações)
│   ├── user.py          # Criação e atualização de usuários
│   └── message.py       # Lógica de criptografia e manipulação de mensagens
├── utils/               # Funções auxiliares e configuração de autenticação
│   └── config.py        # Hashing, JWT, validações e helpers
└── main.py              # Arquivo principal para inicializar o servidor
```

---

## Como rodar o projeto localmente

### 1. Clone o repositório

```bash
git clone https://github.com/seu_usuario/seu_repositorio.git
cd seu_repositorio
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv venv
# Ativação (Windows):
venv\Scripts\activate
# Ativação (Linux/macOS):
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

**Ou instale manualmente:**

```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary python-jose bcrypt pycryptodome python-multipart
```

---

## Inicialização do Banco de Dados

Certifique-se de configurar corretamente a URL do banco no projeto. Para isso, vá até o arquivo "env" e edite a URL do banco com as informações da sua máquina local. Depois de editar corretamente, renomeie o arquivo colocando um "." antes. ( Ficará .env).

O arquivo deve forçar a configuração do banco de dados na primeira inicialização, mas caso não aconteça, você pode criar as tabelas com:

```python
from src.database import Base, engine
Base.metadata.create_all(bind=engine)
```

---

## Executando o servidor local

Rode com o Uvicorn:

```bash
uvicorn src.main:app --reload
```

E acesse a plataforma de testes interativos em:

📍 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)