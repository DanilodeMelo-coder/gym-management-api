from fastapi import APIRouter
from services.aluno_services import criar_aluno_service
from database.db import alunos_db
from models.aluno import Aluno


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