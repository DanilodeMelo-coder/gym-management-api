from pydantic import BaseModel, Field
import uuid
from typing import Optional


class Exercicio(BaseModel):
    id: uuid.UUID = Field(default_factory= uuid.uuid4)
    nome: str
    grupo: str
    descricao: Optional[str]


class CriarExercicio(BaseModel):
    nome: str
    grupo: str
    descricao: Optional[str]