from pydantic import BaseModel, Field
from typing import Optional
from datetime import date
import uuid

class Aluno(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    nome: str
    email: str
    data_nascimento: date
    cpf: str
    admin: Optional [bool]

class AlunoUpdate(BaseModel):
    nome: str
    idade: int
    data_nascimento: str
    admin: Optional [bool]