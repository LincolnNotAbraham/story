# Contribuindo com a Story API

Obrigado por seu interesse em contribuir! Este documento explica como participar do desenvolvimento do projeto.

## 🛠️ Ambiente de desenvolvimento

1. Clone o repositório e entre na pasta:

   ```bash
   git clone https://github.com/LincolnNotAbraham/story.git
   cd story
   ```

2. Instale as dependências com [uv](https://docs.astral.sh/uv/):

   ```bash
   uv sync
   ```

3. Crie o arquivo `.env` a partir das variáveis descritas no [README](README.md) e inicie o servidor:

   ```bash
   uv run uvicorn main:app --reload
   ```

## 📋 Regras gerais

- **Não commite secrets**: arquivos `.env`, chaves e credenciais nunca devem entrar no repositório.
- **Não altere comportamento sem necessidade**: mudanças de API devem ser discutidas em issue antes.
- **Padrões de código**: siga o estilo do projeto (formatação com Black, type hints nas novas funções).
- **Documentação**: atualize o README quando adicionar rotas, variáveis de ambiente ou dependências.

## 🌿 Fluxo de trabalho

1. Abra uma issue descrevendo o problema ou a feature.
2. Crie um branch a partir de `main`:

   ```bash
   git checkout -b feat/minha-feature
   ```

3. Faça seus commits com mensagens claras (padrão [Conventional Commits](https://www.conventionalcommits.org/)):

   ```
   feat: adiciona endpoint de escolha de opção
   docs: corrige typo no README
   ```

4. Abra um Pull Request descrevendo o que mudou e por quê.

## 🧪 Testes

O projeto ainda não possui suíte de testes automatizados — contribuições com testes para os endpoints principais (`stories`, `jobs`) são muito bem-vindas!

## 📄 Licença

Ao contribuir, você concorda em licenciar suas contribuições sob a [MIT License](LICENSE) do projeto.
