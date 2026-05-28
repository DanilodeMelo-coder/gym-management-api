from pydantic import BaseModel, Field
from typing import Optional
from enums.usuario_enum import TipoUsuario
from datetime import date
import uuid

class Aluno(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    nome: str
    email: str
    data_nascimento: date
    cpf: str
    tipo: TipoUsuario = TipoUsuario.aluno

    class Config:
        from_attributes = True 

class Criar_aluno(BaseModel):
    nome: str
    email: str
    data_nascimento: date
    cpf: str
    tipo: TipoUsuario = TipoUsuario.aluno

class AlunoUpdate(BaseModel):
    nome: str
    email: str
    data_nascimento: date
    admin: Optional [bool]