# Python Course — Estudos para Vaga Junior

Repositório de estudos práticos com foco em Python moderno, 
FastAPI e TDD para migração de carreira.

## Tecnologias
- Python 3.13
- pytest
- FastAPI (em breve)

## Estrutura
- `dia01-python-moderno/` — Type hints, dataclasses, TDD com pytest

## Como executar

```bash
# Clonar o repositório
git clone git@github.com:danalmeidap/python_course.git

# Entrar na pasta
cd dia01-python-moderno

# Criar ambiente virtual
python3 -m venv .venv
source .venv/bin/activate

# Instalar dependências
pip install pytest

# Rodar os testes
pytest -v
```

## Aprendizados do Dia 1
- Ciclo TDD completo: Red → Green → Refactor
- Type hints e docstrings profissionais
- Tratamento de exceções em funções de negócio


## Deploy

API disponível em produção:

- **Base URL:** https://insightful-ambition-production-00b7.up.railway.app
- **Documentação interativa:** https://insightful-ambition-production-00b7.up.railway.app/docs

## Endpoints principais

| Método | Rota | Descrição |
|--------|------|-----------|
| POST | /usuarios/ | Cadastro de usuário |
| POST | /usuarios/login | Login (retorna JWT) |
| GET | /tarefas/ | Listar tarefas do usuário |
| POST | /tarefas/ | Criar tarefa |
| GET | /tarefas/{id} | Obter tarefa |
| PUT | /tarefas/{id} | Atualizar tarefa |
| DELETE | /tarefas/{id} | Deletar tarefa |
| GET | /usuarios/me/tarefas | Listar minhas tarefas |