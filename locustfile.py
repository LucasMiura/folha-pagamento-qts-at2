"""Cenário Locust para o endpoint de cálculo da folha."""

from locust import HttpUser, between, task


class UsuarioFolha(HttpUser):
    wait_time = between(1, 2)

    @task
    def calcular_folha_de_pagamento(self) -> None:
        self.client.post(
            "/api/folha",
            json={"nome_funcionario": "Pessoa de Teste", "salario_bruto": 5000},
            name="POST /api/folha",
        )
