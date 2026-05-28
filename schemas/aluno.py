from pydantic import BaseModel, Field, field_validator, EmailStr
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
    nome: str = Field(min_length= 2, max_length= 100)
    email: EmailStr
    data_nascimento: date
    cpf: str
    senha: str = Field(min_length= 8)
    tipo: TipoUsuario = TipoUsuario.aluno

    @field_validator("senha")
    @classmethod
    def validar_senha(cls, v: str) -> str:
        if not any(c.isupper() for c in v):
            raise ValueError("Senha deve ter ao menos uma letra maiúscula")
        if sum(c.isdigit() for c in v) < 2:
            raise ValueError("Senha deve ter ao menos um número")
        return v


class AlunoUpdate(BaseModel):
    nome: str
    email: str
    data_nascimento: date
    admin: Optional [bool]