"""Rotas web da folha de pagamento."""

from pathlib import Path

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.folha.modelos import DadosFolha, ResultadoFolha

modelos = Jinja2Templates(directory=str(Path(__file__).parent / "templates"))


def consultar_aliquota_previdenciaria(salario_bruto: float) -> float:
    """Simula o serviço externo de alíquotas usado na atividade."""
    return 0.10


aplicacao = FastAPI(title="Folha de Pagamento")


@aplicacao.get("/", response_class=HTMLResponse)
def exibir_pagina_inicial(requisicao: Request) -> HTMLResponse:
    return modelos.TemplateResponse(request=requisicao, name="index.html", context={})


@aplicacao.post("/api/folha", response_model=ResultadoFolha)
def calcular_folha(dados: DadosFolha) -> ResultadoFolha:
    try:
        aliquota = consultar_aliquota_previdenciaria(dados.salario_bruto)
    except Exception as erro:
        raise HTTPException(
            status_code=503,
            detail="Não foi possível consultar a alíquota previdenciária.",
        ) from erro

    if not 0 <= aliquota <= 1:
        raise HTTPException(status_code=502, detail="O serviço retornou uma alíquota inválida.")

    desconto = round(dados.salario_bruto * aliquota, 2)
    return ResultadoFolha(
        nome_funcionario=dados.nome_funcionario,
        salario_bruto=dados.salario_bruto,
        desconto_previdenciario=desconto,
        salario_liquido=round(dados.salario_bruto - desconto, 2),
    )
