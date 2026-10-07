# Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/),
e este projeto adere ao [Semantic Versioning](https://semver.org/lang/pt-BR/).

## [Unreleased]

### Added

- README completo com badges, guia de instalação, variáveis de ambiente e referência da API
- Licença MIT, guia de contribuição (CONTRIBUTING.md) e este changelog
- Docstrings nos módulos principais (config, database, story generator e routers)
- Entradas adicionais no `.gitignore` (IDEs, caches, logs e bancos locais)

### Changed

- `.gitignore` expandido para cobrir mais artefatos de desenvolvimento

## [0.1.0] - 2026-09-13

### Added

- Estrutura inicial da API FastAPI com geração de histórias via LangChain/Google Gemini
- Endpoints `POST /stories/create`, `GET /jobs/{job_id}` e `GET /stories/{story_id}/complete`
- Modelos SQLAlchemy para stories, story nodes, jobs, users e players
- Suporte a sessão via cookie e processamento de geração em background
