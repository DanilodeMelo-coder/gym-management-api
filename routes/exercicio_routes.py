from fastapi import APIRouter
from schemas.exercicio import CriarExercicio

router= APIRouter(prefix="/exercicios")


@router.get("/")
def exercicios_cadastrados():

    return "ok"


@router.post("/")
def criar_exercicio(exercicio: CriarExercicio):


    return{
        "mensagem":"exercicio criado com sucesso",
        "exercicio": exercicio
    }

