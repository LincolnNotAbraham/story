# 🎲 Story API — Escolha seu Jogo de Aventura

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.116-009688.svg)](https://fastapi.tiangolo.com/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

API backend que gera **histórias de aventura ramificadas** (escolha sua própria aventura) usando Inteligência Artificial. Informe um tema e a API constrói, em background, uma árvore de histórias com opções, dificuldades progressivas, dados 1–20, itens e atributos do personagem — pronta para ser consumida por um frontend de RPG.

## ✨ Funcionalidades

- Geração de histórias ramificadas com LLM (Google Gemini via LangChain)
- Processamento assíncrono com jobs em background (status `pending` → `processing` → `completed`/`failed`)
- Árvore completa de nós com opções, finais vencedores e perdedores
- Identificação de jogador por sessão via cookie (funciona para visitantes)
- Documentação interativa automática (Swagger UI e ReDoc)
- Autenticação JWT em desenvolvimento (módulo `routers/auth.py`)

## 🛠️ Tecnologias

- **Python 3.11+**
- **FastAPI** — framework web async
- **SQLAlchemy 2.x** — ORM
- **LangChain + langchain-google-genai** — geração de texto com IA
- **Pydantic** — validação de dados (request/response e parsing da resposta do LLM)
- **uv** — gerenciador de pacotes e ambientes
- **PostgreSQL** (recomendado em produção) ou **SQLite** (padrão para desenvolvimento)

## 📁 Estrutura do projeto

```
story/
├── main.py                  # Ponto de entrada da aplicação FastAPI
├── core/
│   ├── config.py            # Configurações via .env (pydantic-settings)
│   ├── prompts.py           # Prompt usado pelo gerador de histórias
│   ├── models.py            # Modelos Pydantic da resposta do LLM
│   └── story_generator.py   # Orquestração LLM → banco de dados
├── db/
│   └── database.py          # Engine, sessão e criação de tabelas
├── models/                  # Modelos SQLAlchemy (Story, StoryNode, StoryJob, User, Player)
├── schemas/                 # Schemas Pydantic de request/response
├── routers/
│   ├── story.py             # Endpoints de criação e consulta de histórias
│   ├── job.py               # Endpoint de status dos jobs
│   └── auth.py              # Autenticação (em desenvolvimento)
├── pyproject.toml           # Dependências e metadados do projeto
└── uv.lock                  # Lockfile do uv
```

## 🚀 Instalação

Pré-requisitos: Python 3.11+ e [uv](https://docs.astral.sh/uv/).

```bash
# Clonar
git clone https://github.com/LincolnNotAbraham/story.git
cd story

# Instalar dependências
uv sync
```

Alternativa com pip:

```bash
python -m venv .venv
source .venv/bin/activate
pip install "fastapi[all]" langchain langchain-google-genai "passlib[bcrypt]" \
    "pyjwt[crypto]" python-dotenv python-multipart sqlalchemy uvicorn psycopg2-binary
```

## ⚙️ Variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
DATABASE_URL=sqlite:///./app.db
# Em produção: postgresql+psycopg2://user:pass@localhost:5432/story
ALLOWED_ORIGINS=http://localhost:3000
GOOGLE_API_KEY=sua_chave_do_google_ai_studio
SECRET_KEY=uma_chave_secreta_forte
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

| Variável | Obrigatória | Descrição |
|---|---|---|
| `DATABASE_URL` | Não (default SQLite) | String de conexão SQLAlchemy |
| `ALLOWED_ORIGINS` | Não | Origens CORS permitidas, separadas por vírgula |
| `GOOGLE_API_KEY` | Sim* | Chave da API do Google AI Studio (*necessária para gerar histórias) |
| `SECRET_KEY` | Sim* | Segredo para assinatura JWT (*módulo auth) |
| `ALGORITHM` | Sim* | Algoritmo de hash JWT (ex.: `HS256`) |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Sim | Tempo de expiração do token, em minutos |

> A chave `GOOGLE_API_KEY` é usada pelo modelo `gemma-3-12b-it` (ver `core/story_generator.py`). Nunca versione o arquivo `.env`.

## ▶️ Como executar

```bash
uv run uvicorn main:app --reload
```

A API ficará disponível em `http://localhost:8000`:

- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

As rotas ficam sob o prefixo `/api` (configurável via `API_PREFIX`).

## 📖 Endpoints principais

| Método | Rota | Descrição |
|---|---|---|
| `POST` | `/api/stories/create` | Cria uma história a partir de um tema (job em background) |
| `GET` | `/api/jobs/{job_id}` | Consulta o status de um job (`pending`, `processing`, `completed`, `failed`) |
| `GET` | `/api/stories/{story_id}/complete` | Retorna a árvore completa da história (nós, opções e finais) |

### Exemplo de uso

```bash
# 1. Criar uma história
curl -X POST http://localhost:8000/api/stories/create \
  -H "Content-Type: application/json" \
  -d '{"theme": "fantasia medieval"}'

# 2. Consultar o job (usar o job_id retornado no passo anterior)
curl http://localhost:8000/api/jobs/<job_id>

# 3. Buscar a história completa quando o status for "completed"
curl http://localhost:8000/api/stories/<story_id>/complete
```

O cookie `session_id` é definido automaticamente na primeira requisição e agrupa as histórias da mesma sessão.

## 🤝 Contribuindo

Contribuições são bem-vindas! Veja o guia em [CONTRIBUTING.md](CONTRIBUTING.md).

## 📄 Licença

Este projeto está licenciado sob a MIT License — veja o arquivo [LICENSE](LICENSE) para detalhes.
