from fastapi import APIRouter
from services.aluno_services import criar_aluno_service, atualizar_aluno_service, deletar_aluno_service
from database.db import alunos_db
from models.aluno import Aluno, AlunoUpdate


router = APIRouter()


@router.get("/lista-alunos")
def home():
    return alunos_db

@router.post("/criar-aluno")
def criar_aluno(aluno: Aluno):

    
    aluno_verificado = criar_aluno_service(aluno)

    return aluno_verificado

@router.get("/buscar-aluno/{aluno}")
def buscar_aluno(aluno):

    for aluno_cadastrado in alunos_db:
        if aluno_cadastrado.nome == aluno:
            return {"aluno": aluno_cadastrado}
        
    return {"mensagem": "Aluno não cadastrado"}

@router.put("/aluno/{id}")
def atualizar_aluno(id: int, aluno: AlunoUpdate):

    aluno_atualizado = atualizar_aluno_service(id, aluno.nome, aluno.idade)

    return aluno_atualizado


@router.delete("/aluno/{id}")
def deletar_aluno(id:int):

    aluno_deletado = deletar_aluno_service(id)

    return aluno_deletado