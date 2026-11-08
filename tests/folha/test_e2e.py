"""Teste ponta a ponta do fluxo da folha de pagamento."""

import pytest
from playwright.sync_api import Page, expect


class PaginaFolhaPagamento:
    """Page Object para o formulário de folha de pagamento."""

    def __init__(self, pagina: Page, endereco_aplicacao: str) -> None:
        self.pagina = pagina
        self.endereco_aplicacao = endereco_aplicacao

    def abrir(self) -> None:
        self.pagina.goto(self.endereco_aplicacao)

    def preencher_e_calcular(self, nome_funcionario: str, salario_bruto: str) -> None:
        self.pagina.get_by_label("Nome do funcionário").fill(nome_funcionario)
        self.pagina.get_by_label("Salário bruto").fill(salario_bruto)
        self.pagina.get_by_role("button", name="Calcular salário líquido").click()


@pytest.mark.e2e
def test_deve_exibir_salario_liquido_apos_enviar_formulario(
    pagina: Page, endereco_aplicacao
):
    tela_folha = PaginaFolhaPagamento(pagina, endereco_aplicacao)
    tela_folha.abrir()
    tela_folha.preencher_e_calcular("Ana Silva", "5000")

    expect(pagina.locator("#resultado")).to_contain_text("Demonstrativo para Ana Silva")
    expect(pagina.locator("#resultado")).to_contain_text("R$ 4.500,00")
