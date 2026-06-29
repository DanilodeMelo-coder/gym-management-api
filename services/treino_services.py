from sqlalchemy.orm import Session
from schemas.treino import CriarTreino
import uuid
from models.treino import Treino
from schemas.treino import AdicionarExercicio
from models.exercicio import Exercicio
from models.treinoExercicio import TreinoExercicio


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


def adicionar_exercicio_service(treino_id: str, adicionar_exercicio: AdicionarExercicio, db: Session ):
    treino = db.query(Treino).filter(Treino.id == treino_id).first()

    if not treino:
        return {"status": "erro", 
        "mensagem": "Treino não encontrado", 
        "data": None
        }
    
    exercicio_id = adicionar_exercicio.exercicio_id

    exercicio = db.query(Exercicio).filter(Exercicio.id == exercicio_id).first()

    if not exercicio:
        return {"status": "erro", 
        "mensagem": "Exercicio não encontrado", 
        "data": None
        }


    treino_exercicio_novo = TreinoExercicio(
        id= str(uuid.uuid4()),
        treino_id= treino.id,
        exercicio_id = exercicio_id,
        series = adicionar_exercicio.series,
        repeticoes= adicionar_exercicio.repeticoes,
        carga= adicionar_exercicio.carga
    )

    db.add(treino_exercicio_novo)
    db.commit()
    db.refresh(treino_exercicio_novo)

    return {"status": "sucesso", 
        "mensagem": "Exercicio adicionado com sucesso", 
        "data": treino_exercicio_novo
        }


def deletar_exercicio(id: str, db: Session):
    treino_exercicio =db.query(TreinoExercicio).filter(TreinoExercicio.id == id).first()

    if not treino_exercicio:
        return {"status": "erro", 
        "mensagem": "Treino não encontrado", 
        "data": None
        }
    
    db.delete(treino_exercicio)
    db.commit()

    return {"status": "sucesso", 
    "mensagem": "Exercicio deletado com sucesso", 
    "data": None
    }
