"""Fixtures e fábrica de dados compartilhadas pelos testes."""

import socket
import threading
import time
from collections.abc import Iterator

import pytest
import uvicorn
from faker import Faker
from fastapi.testclient import TestClient
from playwright.sync_api import Page

from app.folha.rotas import aplicacao


class FabricaDeDadosFolha:
    """Gera dados de funcionários para os testes."""

    def __init__(self) -> None:
        self.falsificador = Faker("pt_BR")

    def gerar_dados_validos(self) -> dict[str, str | float]:
        return {
            "nome_funcionario": self.falsificador.name(),
            "salario_bruto": round(self.falsificador.pyfloat(min_value=1500, max_value=9000), 2),
        }


@pytest.fixture
def fabrica_de_dados_folha() -> Iterator[FabricaDeDadosFolha]:
    fabrica = FabricaDeDadosFolha()
    yield fabrica
    del fabrica


@pytest.fixture
def cliente() -> Iterator[TestClient]:
    with TestClient(aplicacao) as cliente_http:
        yield cliente_http


@pytest.fixture
def pagina(page: Page) -> Page:
    """Disponibiliza em português a página fornecida pelo plugin Playwright."""
    return page


@pytest.fixture(scope="session")
def endereco_aplicacao() -> Iterator[str]:
    with socket.socket() as soquete:
        soquete.bind(("127.0.0.1", 0))
        porta = soquete.getsockname()[1]

    servidor = uvicorn.Server(
        uvicorn.Config(aplicacao, host="127.0.0.1", port=porta, log_level="critical")
    )
    thread_servidor = threading.Thread(target=servidor.run, daemon=True)
    thread_servidor.start()
    limite = time.monotonic() + 10
    while not servidor.started and thread_servidor.is_alive() and time.monotonic() < limite:
        time.sleep(0.05)
    if not servidor.started:
        servidor.should_exit = True
        thread_servidor.join(timeout=2)
        raise RuntimeError("O servidor de teste não iniciou.")

    yield "http://127.0.0.1:" + str(porta)
    servidor.should_exit = True
    thread_servidor.join(timeout=5)
