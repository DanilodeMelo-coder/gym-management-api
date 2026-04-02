from pydantic import BaseModel
from enum import Enum


class GruposMusculares(str,Enum):
    peito= "peito"
    costas= "costas"
    braco= "braço"
    pernas= "pernas"


class Exercicio(BaseModel):
    nome: str
    grupo: GruposMusculares