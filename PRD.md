# PRD — Folha de Pagamento

## Objetivo

Aplicação web demonstrativa para informar funcionário e salário bruto e consultar o cálculo do salário líquido.

## Rotas

- GET /: apresenta o formulário HTML.
- POST /api/folha: recebe nome_funcionario e salario_bruto, consulta uma alíquota previdenciária e devolve salário bruto, desconto e salário líquido em JSON.

## Regra demonstrativa

A integração de alíquota é representada por uma função substituível, que retorna 10% nesta versão. Esse valor serve somente para demonstrar o fluxo e os mocks; não representa cálculo tributário oficial.

## Requisitos não funcionais avaliados

- A interface permite preenchimento e envio por teclado, tem rótulos associados e anuncia o resultado.
- A página é auditada com Axe-core para WCAG 2.1 AA e navegação por teclado.
- O endpoint é submetido a carga com Locust; RPS, p95 e taxa de falhas são registrados no README.
