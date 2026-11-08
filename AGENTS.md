# Diretrizes de Contexto e Qualidade do Projeto

## Objetivo e escopo

- A aplicação é um demonstrativo acadêmico de folha de pagamento.
- A alíquota de 10% é ilustrativa. Não apresente o cálculo como regra tributária ou trabalhista oficial.
- Mantenha a implementação limitada ao enunciado da AT2 e à funcionalidade descrita em PRD.md.

## Código Python

- Use Python 3.12 ou superior.
- Escreva nomes de funções, métodos, variáveis, classes e testes em português, de forma clara e descritiva.
- Dê aos testes nomes que indiquem precisamente o comportamento verificado, mesmo que fiquem compridos.
- Inclua anotações de tipo em funções e métodos quando aplicável.
- Valide os dados de entrada com Pydantic e apresente respostas claras para dados inválidos e falhas de dependências.
- Arredonde valores monetários retornados para duas casas decimais.
- Escreva comentários em português para explicar regras ou decisões que não sejam óbvias; evite comentários redundantes.

## Página HTML

- Mantenha o idioma da página como pt-BR e use elementos HTML semânticos.
- Associe cada campo a um rótulo visível e permita concluir o fluxo usando teclado.
- Preserve os nomes dos campos e a rota POST /api/folha usados pela aplicação e pelos testes.
- Apresente o resultado e os erros em linguagem clara; atualize a área anunciada por leitores de tela.
- Formate os valores como moeda brasileira e mantenha a interface utilizável em telas estreitas.
- Não use a interface para sugerir que a alíquota demonstrativa é um cálculo oficial.

## Testes

- Use Pytest e organize os testes junto da funcionalidade em tests/folha.
- Estruture os testes no padrão AAA: preparação, ação e verificação.
- Marque testes de integração com @pytest.mark.integration e use TestClient para conferir status HTTP e payloads.
- Use fixtures com yield para preparar e encerrar os recursos de teste.
- Use mocker.patch para isolar a consulta de alíquota e cobrir respostas de sucesso e falha.
- Gere dados sintéticos em português com Faker("pt_BR") por meio da fábrica de dados.
- Marque os testes de navegador com @pytest.mark.e2e; use Playwright, Page Object Model e seletores semânticos.
- Marque testes de acessibilidade com @pytest.mark.accessibility; verifique WCAG 2.1 AA com Axe-core e teste o foco pela tecla Tab.
- Dê preferência a asserts sobre resultado observável, status e conteúdo da página.

## Carga e comandos

- Mantenha em locustfile.py um usuário Locust que execute a rota POST /api/folha.
- Registre no README.md os valores realmente observados de RPS, p95 e taxa de falhas; não invente resultados.
- Instalar dependências: `uv sync`
- Instalar o Chromium: `uv run playwright install chromium`
- Iniciar a aplicação: `uv run uvicorn app.folha.rotas:aplicacao --reload`
- Executar todos os testes: `uv run pytest -v`
- Executar integração: `uv run pytest -v -m integration`
- Executar E2E: `uv run pytest -v -m e2e`
- Executar acessibilidade: `uv run pytest -v -m accessibility`
- Executar Locust com a aplicação iniciada em outro terminal: `uv run locust -f locustfile.py --host http://127.0.0.1:8000`
