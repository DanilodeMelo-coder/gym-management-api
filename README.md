# 🏋️ Gym Management API

> API REST para gestão de academias — desenvolvida com **Python + FastAPI**, com autenticação JWT, controle de acesso por roles e sistema de convites entre personal trainers e alunos.

---

## O problema que essa API resolve

Academias e personal trainers ainda gerenciam alunos via planilha, WhatsApp ou papel. Não existe um sistema centralizado que permita ao personal criar treinos, vincular alunos e controlar quem acessa o quê.

Essa API resolve isso: o personal gera um convite com código único, o aluno usa o código pra se vincular — e a partir daí o personal tem acesso ao perfil e treinos daquele aluno. Cada usuário tem um papel (`admin`, `personal`, `aluno`) e o sistema aplica essas permissões em cada endpoint.

**Contexto real:** o projeto foi desenvolvido pensado no uso por um personal trainer de verdade, com requisitos que vieram de conversa direta com o usuário final.

---

## O que foi implementado

### Autenticação e Autorização
- **JWT com PyJWT** — geração e validação de tokens com expiração de 8h
- **Bcrypt** para hash de senhas no cadastro e verificação no login
- **Role-based access control** com 3 níveis: `admin`, `personal`, `aluno`
- Dependências reutilizáveis do FastAPI: `autenticar_token`, `apenas_personal`, `apenas_admin`

```python
# exemplo: rota protegida por role
@router.get("/", response_model=list[Aluno])
def listar_aluno(db: Session = Depends(get_session), payload = Depends(apenas_personal)):
    return listar_alunos(db)
```

### Sistema de Convites
- Personal gera um **código único de 6 caracteres** (via `secrets.token_hex`) com expiração de 30 minutos
- Aluno usa o código para se vincular ao personal
- O sistema valida: código existente, já utilizado, e expiração — e só então cria o vínculo no banco

### Modelos e Relacionamentos (SQLAlchemy)
| Tabela | Descrição |
|--------|-----------|
| `Usuarios` | Alunos, personais e admins — self-referência `personal_id → id` |
| `Treinos` | Criados por um usuário, tipificados como `personal` ou `proprio` |
| `Exercicios` | Catálogo de exercícios com grupo muscular e tipo |
| `TreinoExercicios` | Tabela associativa com séries, repetições e carga |
| `Convites` | Código, expiração, uso e vínculo com personal |

### Validações de negócio
- Validação de CPF com algoritmo dos dígitos verificadores
- Verificação de idade mínima (12 anos)
- Unicidade de email e CPF
- Variáveis sensíveis via `.env` com `python-dotenv`

### Stack
`FastAPI` · `SQLAlchemy 2.x` · `Alembic` · `Pydantic v2` · `PyJWT` · `Bcrypt` · `SQLite` · `Uvicorn`

---

## Como rodar localmente

**Pré-requisitos:** Python 3.10+

```bash
# 1. Clone o repositório
git clone https://github.com/DanilodeMelo-coder/gym-management-api.git
cd gym-management-api

# 2. Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Configure as variáveis de ambiente
# Crie um arquivo .env na raiz com:
echo "SECRET_KEY=sua_chave_secreta_aqui" > .env
echo "ALGORITHM=HS256" >> .env

# 5. Rode as migrations
alembic upgrade head

# 6. Inicie o servidor
uvicorn main:app --reload
```

A documentação interativa estará disponível em: **http://localhost:8000/docs**

---

## Endpoints principais

| Método | Rota | Acesso | Descrição |
|--------|------|--------|-----------|
| `POST` | `/Auth/login` | Público | Login e geração de token JWT |
| `POST` | `/Alunos/` | Público | Cadastro de usuário |
| `GET` | `/Alunos/` | Personal/Admin | Lista todos os alunos |
| `GET` | `/Alunos/{id}` | Personal/Admin | Busca aluno por ID |
| `PUT` | `/Alunos/{id}` | Próprio usuário ou Admin | Atualiza dados |
| `DELETE` | `/Alunos/{id}` | Próprio usuário ou Admin | Remove conta |
| `POST` | `/Convites/` | Personal | Gera código de convite |
| `POST` | `/Convites/utilizar-convite` | Aluno autenticado | Usa convite para se vincular |

---

## Estrutura do projeto

```
gym-management-api/
├── core/           # Config e conexão com banco
├── models/         # Entidades SQLAlchemy
├── schemas/        # Validação Pydantic
├── services/       # Lógica de negócio
├── routes/         # Endpoints FastAPI
├── dependencias/   # Guards de autenticação/autorização
├── enums/          # Tipos enumerados (roles, tipos de treino)
└── migrations/     # Alembic
```

---

## Próximos passos

- [ ] Rotas de treino e exercícios (CRUD completo)
- [ ] Containerização com Docker
- [ ] Testes automatizados com Pytest
- [ ] Deploy em nuvem (Railway / AWS)