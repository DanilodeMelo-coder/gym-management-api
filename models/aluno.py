from pydantic import BaseModel

class Aluno(BaseModel):
    id: int
    nome: str
    idade: int

class AlunoUpdate(BaseModel):
    nome: str
    idade: int