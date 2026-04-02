from fastapi import APIRouter
from models.exercicio import Exercicio
from database.db import exercicios_db





router= APIRouter()


@router.get("/exercicios-cadastrados")
def exercicios_cadastrados():

    return exercicios_db


@router.post("/criar-exercicio")
def criar_exercicio(exercicio: Exercicio):

    exercicios_db.append(exercicio)

    return{
        "mensagem":"exercicio criado com sucesso",
        "exercicio": exercicio
    }

@router.get("/buscar-exercicio/{nome_exercicio}")
def buscar_exercicio_nome(nome_exercicio):

    for exercicio_cadastrado in exercicios_db:
        if exercicio_cadastrado.nome == nome_exercicio:
            return exercicio_cadastrado
        
    return {"status": "erro",
            "mensagem": "exercicio não cadastrado"
            }

@router.get("/buscar-exercicio-musculo/{grupo_muscular}")
def buscar_exercicio_musculo(grupo_muscular):

    resultados = []
    for exercicio in exercicios_db:
        if exercicio.grupo.value.lower() == grupo_muscular.lower():
            resultados.append(exercicio)
    
    if resultados:
        return resultados
        
    return {"status": "erro",
            "mensagem": "grupo muscular não cadastrado"
            }