import uuid
from sqlalchemy.orm import Session
from models.aluno import Aluno
from models.treino import Treino
from models.vinc_AlunoTreino import Vinc_AlunoTreino


def vincular_treino_service(aluno_id, treino_id, payload: dict, db: Session):

    aluno = db.query(Aluno).filter(Aluno.id == aluno_id).first()

    if not aluno:
        return {"status": "erro",
                "mensagem": "Aluno não encontrado",
                "data": None}

    treino = db.query(Treino).filter(Treino.id == treino_id).first()

    if not treino:
        return {"status": "erro",
                "mensagem": "Treino não encontrado",
                "data": None}

    vinculcaoTreino = db.query(Vinc_AlunoTreino).filter(Vinc_AlunoTreino.aluno_id == aluno_id, Vinc_AlunoTreino.treino_id == treino_id).first()

    if vinculcaoTreino:
        return {"status": "erro",
                "mensagem": "Esse treino ja esta vinculado",
                "data": None}

    vinculandoTreino = Vinc_AlunoTreino(
        id = str(uuid.uuid4()),
        treino_id = treino_id,
        aluno_id = aluno_id,
    )

    db.add(vinculandoTreino)
    db.commit()
    db.refresh(vinculandoTreino)

    return {"status": "sucesso",
            "mensagem": "vinculção criada com sucesso",
            "data": vinculandoTreino
            }


def listar_treinos_aluno(payload: dict, db: Session):

    aluno_id = payload["sub"]

    vinculacoes = db.query(Vinc_AlunoTreino).filter(
        Vinc_AlunoTreino.aluno_id == aluno_id,
        Vinc_AlunoTreino.ativo == True
    ).all()

    return {"status": "sucesso",
            "mensagem": "Treinos vinculados encontrados",
            "data": vinculacoes
            }


def desativar_vinculacao(vinculacao_id: str, db: Session):

    vinculacao = db.query(Vinc_AlunoTreino).filter(Vinc_AlunoTreino.id == vinculacao_id).first()

    if not vinculacao:
        return {"status": "erro",
                "mensagem": "Vinculação não encontrada",
                "data": None}

    vinculacao.ativo = False
    db.commit()
    db.refresh(vinculacao)

    return {"status": "sucesso",
            "mensagem": "Vinculação desativada com sucesso",
            "data": vinculacao
            }
