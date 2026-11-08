# Folha de Pagamento — AT2 de QTS

Aplicação web demonstrativa para informar o funcionário e o salário bruto, consultar a API e visualizar o salário líquido calculado.

> A alíquota de 10% usada nesta versão é ilustrativa e existe para demonstrar o fluxo da atividade. Ela não representa um cálculo oficial de folha de pagamento.

## O que o projeto contém

- Aplicação web com FastAPI, modelos Pydantic e interface HTML.
- Testes de integração com TestClient, fixtures, mocks e dados de teste com Faker.
- Teste ponta a ponta com Playwright e Page Object Model.
- Testes de acessibilidade com Axe-core e navegação por teclado.
- Cenário de carga com Locust.
- Especificação da aplicação em [PRD.md](PRD.md) e regras de implementação em [AGENTS.md](AGENTS.md).
- Registro de uso e revisão de IA em [AI_USAGE.md](AI_USAGE.md).

## Requisitos

- Python 3.12 ou superior.
- uv.

## Preparar o ambiente

Na pasta do projeto, instale as dependências:

```powershell
uv sync
```

Instale o navegador Chromium usado pelo Playwright:

```powershell
uv run playwright install chromium
```

## Executar a aplicação

Inicie o servidor:

```powershell
uv run uvicorn app.folha.rotas:aplicacao --reload
```

Abra [http://127.0.0.1:8000](http://127.0.0.1:8000) no navegador. A página permite informar nome e salário bruto. A API recebe esses dados em `POST /api/folha` e devolve o desconto ilustrativo e o salário líquido.

## Executar os testes

Execute toda a suíte:

```powershell
uv run pytest -v
```

Para executar apenas uma categoria:

```powershell
uv run pytest -v -m integration
uv run pytest -v -m e2e
uv run pytest -v -m accessibility
```

Os testes E2E e de acessibilidade iniciam a aplicação de teste e usam o Chromium instalado pelo Playwright.

### Resultado da última execução

Em 7 de novembro de 2026, a suíte apresentou 6 testes aprovados e nenhum aviso.

## Executar o teste de carga

Deixe a aplicação em execução em um terminal. Em outro terminal, inicie o Locust:

```powershell
uv run locust -f locustfile.py --host http://127.0.0.1:8000
```

Abra [http://127.0.0.1:8089](http://127.0.0.1:8089), informe a quantidade de usuários e a taxa de inicialização, e inicie a simulação. Ao terminar, registre aqui a configuração usada e os valores observados no Locust.

| Medida | Resultado |
| --- | --- |
| Usuários concorrentes | 5 |
| Taxa de inicialização | 1 usuário por segundo |
| Duração da execução | 30 segundos |
| Requisições por segundo (RPS) | 3,18 |
| Tempo de resposta p95 | 4 ms |
| Taxa de falhas | 0% (0 de 91 requisições) |

## Uso de ferramentas de IA

O registro da ferramenta utilizada, das atividades em que houve auxílio e da revisão do conteúdo está em [AI_USAGE.md](AI_USAGE.md).
