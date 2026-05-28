from schemas.exercicio import CriarExercicio
from sqlalchemy.orm import Session
from models.exercicio import Exercicio
import uuid
import re


GRUPOS_MUSCULARES = {"peito", "costas", "biceps", "triceps", 
                    "ante_braço", "quadriceps", "posterior",
                    "panturrilha", "abdomen", "gluteo", "ombro"
                    }

def criar_exercicio_service(exercicio: CriarExercicio, db: Session):

    nome_tratado = tratar_nome(exercicio.nome)

#Checagens do nome
    if nome_tratado is None:
        return {"status": "erro",
                "menssage": f"o nome do exercicio {exercicio.nome} não é valido por possuir números ou caractéres",
                "data": None}

    exercicio_existente = db.query(Exercicio).filter(Exercicio.nome == nome_tratado).first()
    if exercicio_existente:
        return {"status": "erro",
        "menssage": "esse exercicio ja esta cadastrado no sistema",
        "data": None}

#checagens do grupo
    nome_grupo_tratado = tratar_nome(exercicio.grupo)

    if nome_grupo_tratado is None:
        return {"status": "erro",
                "menssage": f"o nome do grupo muscular {exercicio.grupo} não é valido por possuir números ou caractéres",
                "data": None}

    grupo_verificado = checar_grupo_muscular(nome_grupo_tratado)

    if grupo_verificado is False:
        return {"status": "erro",
                "menssage": f"o grupo muscular {exercicio.grupo} não pertence a lista dos grupos validos: {GRUPOS_MUSCULARES}",
                "data": None}


    exercicio_novo = Exercicio(
        id= str(uuid.uuid4()),
        nome= exercicio.nome.lower().strip(),
        grupo= exercicio.grupo.lower().strip(),
        descricao= exercicio.descricao
    )

    db.add(exercicio_novo)
    db.commit()
    db.refresh(exercicio_novo)

    return {"status": "sucesso",
    "menssage": "Exercicio criado com sucesso",
    "data": exercicio_novo}



def tratar_nome(nome: str):

    nome_tratado = nome.lower().strip()

    if re.search(r'[0-9]', nome) or re.search(r'[^a-zA-ZÀ-ÿ\s\-\']', nome):

        return None

    return nome_tratado


def checar_grupo_muscular(nome: str) -> bool:

    if nome not in GRUPOS_MUSCULARES:
        return False

    return True



