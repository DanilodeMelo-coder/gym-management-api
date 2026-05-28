from pydantic import BaseModel, Field
from enums.exercicio_enum import TipoExercicio
import uuid
from typing import Optional


class Exercicio(BaseModel):
    id: uuid.UUID = Field(default_factory= uuid.uuid4)
    nome: str
    grupo: str
    descricao: Optional[str]
    tipo: TipoExercicio = TipoExercicio.base


class CriarExercicio(BaseModel):
    nome: str
    grupo: str
    descricao: Optional[str]
    tipo: TipoExercicio = TipoExercicio.customizado