"""Auditoria automatizada e navegação por teclado da página."""

import pytest
from axe_playwright_python.sync_playwright import Axe
from playwright.sync_api import Page, expect


@pytest.mark.accessibility
def test_deve_atender_auditoria_axe_wcag_21_aa(pagina: Page, endereco_aplicacao):
    pagina.goto(endereco_aplicacao)
    resultado_auditoria = Axe().run(
        pagina,
        options={
            "runOnly": {
                "type": "tag",
                "values": ["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"],
            }
        },
    )

    assert resultado_auditoria.violations_count == 0, resultado_auditoria.response


@pytest.mark.accessibility
def test_deve_permitir_foco_no_nome_do_funcionario_pelo_teclado(
    pagina: Page, endereco_aplicacao
):
    pagina.goto(endereco_aplicacao)
    pagina.keyboard.press("Tab")
    pagina.keyboard.press("Tab")

    expect(pagina.locator("#nome-funcionario")).to_be_focused()
