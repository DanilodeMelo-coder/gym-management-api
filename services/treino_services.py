from sqlalchemy.orm import Session
from schemas.treino import CriarTreino
import uuid
from models.treino import Treino


def criar_treino(payload: dict, criar_treino: CriarTreino, db: Session):

    criado_por = payload["sub"]

    treino_novo = Treino(
        id = str(uuid.uuid4()),
        nome= criar_treino.nome.lower().strip(),
        criado_por = criado_por,
        tipo = criar_treino.tipo
    )

    db.add(treino_novo)
    db.commit()
    db.refresh(treino_novo)

    return {"status": "sucesso",
        "mensagem": "treino criado com sucesso",
        "data": treino_novo
        }


def listar_treinos(payload: dict, db: Session):
    usuario_id = payload["sub"]
    return db.query(Treino).filter(Treino.criado_por == usuario_id).all()

def buscar_treino(id: str, db: Session):
    treino = db.query(Treino).filter(Treino.id == id).first()

    if not treino:
        return {"status": "erro", 
        "mensagem": "Treino não encontrado", 
        "data": None
        }
    
    return {"status": "sucesso", 
    "mensagem": "Treino encontrado", 
    "data": treino
    }


def deletar_treino(id: str, db: Session):
    treino = db.query(Treino).filter(Treino.id == id).first()

    if not treino:
        return {"status": "erro", 
        "mensagem": "Treino não encontrado", 
        "data": None
        }
    
    db.delete(treino)
    db.commit()

    return {"status": "sucesso", 
    "mensagem": "Treino deletado com sucesso", 
    "data": None
    }
