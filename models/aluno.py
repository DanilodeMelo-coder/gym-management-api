from pydantic import BaseModel
from typing import Optional
from datetime import date

class Aluno(BaseModel):
    id: int
    nome: str
    email: str
    data_nascimento: date
    cpf: str
    admin: Optional [bool]

class AlunoUpdate(BaseModel):
    nome: str
    idade: int
    data_nascimento: str