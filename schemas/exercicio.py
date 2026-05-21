from pydantic import BaseModel, Field
import uuid


class Exercicio(BaseModel):
    id: uuid.UUID = Field(default_factory= uudi.uuid4)
    nome: str
    grupo: str
    descricao; Optional[str]


