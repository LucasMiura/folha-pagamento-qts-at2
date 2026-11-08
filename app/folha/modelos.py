"""Modelos de entrada e saída da folha de pagamento."""

from pydantic import BaseModel, Field


class DadosFolha(BaseModel):
    nome_funcionario: str = Field(min_length=2, max_length=100)
    salario_bruto: float = Field(gt=0)


class ResultadoFolha(BaseModel):
    nome_funcionario: str
    salario_bruto: float
    desconto_previdenciario: float
    salario_liquido: float
