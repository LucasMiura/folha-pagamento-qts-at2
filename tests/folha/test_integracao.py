"""Testes de integração das rotas da folha."""

import pytest


@pytest.mark.integration
def test_deve_calcular_salario_liquido_quando_consulta_de_aliquota_tem_sucesso(
    cliente, fabrica_de_dados_folha, mocker
):
    dados_funcionario = fabrica_de_dados_folha.gerar_dados_validos()
    consulta = mocker.patch(
        "app.folha.rotas.consultar_aliquota_previdenciaria", return_value=0.10
    )

    resposta = cliente.post("/api/folha", json=dados_funcionario)

    salario_bruto = dados_funcionario["salario_bruto"]
    assert resposta.status_code == 200
    assert resposta.json() == {
        "nome_funcionario": dados_funcionario["nome_funcionario"],
        "salario_bruto": salario_bruto,
        "desconto_previdenciario": round(salario_bruto * 0.10, 2),
        "salario_liquido": round(salario_bruto * 0.90, 2),
    }
    consulta.assert_called_once_with(salario_bruto)


@pytest.mark.integration
def test_deve_retornar_indisponibilidade_quando_consulta_de_aliquota_falha(
    cliente, fabrica_de_dados_folha, mocker
):
    dados_funcionario = fabrica_de_dados_folha.gerar_dados_validos()
    mocker.patch(
        "app.folha.rotas.consultar_aliquota_previdenciaria",
        side_effect=TimeoutError("Serviço indisponível"),
    )

    resposta = cliente.post("/api/folha", json=dados_funcionario)

    assert resposta.status_code == 503
    assert resposta.json()["detail"] == "Não foi possível consultar a alíquota previdenciária."


@pytest.mark.integration
def test_deve_rejeitar_salario_bruto_zero(cliente, fabrica_de_dados_folha):
    dados_funcionario = fabrica_de_dados_folha.gerar_dados_validos()
    dados_funcionario["salario_bruto"] = 0

    resposta = cliente.post("/api/folha", json=dados_funcionario)

    assert resposta.status_code == 422
