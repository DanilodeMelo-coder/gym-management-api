from pydantic import BaseModel
from enums.treino_enum import TipoTreino
import uuid

class CriarTreino(BaseModel):
    nome: str
    tipo: TipoTreino = TipoTreino.proprio


class AdicionarExercicio(BaseModel):
    exercicio_id: str
    series: int
    repeticoes: int
    carga: float