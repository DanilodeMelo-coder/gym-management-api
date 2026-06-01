from sqlalchemy.orm import Session
import secrets
import uuid
from models.convite import Convite
from datetime import datetime, timedelta, timezone
from fastapi import HTTPException
from models.aluno import Aluno





def criar_convite_service(payload: dict, db: Session ):
    personal_id = payload["sub"]
    expira_em = datetime.utcnow() + timedelta(minutes= 30)

    codigo_gerado = gerar_codigo(db)

    novo_convite = Convite(
        id= str(uuid.uuid4()),
        personal_id= str(personal_id),
        codigo= codigo_gerado,
        expira_em= expira_em,
        usado= False
    )

    db.add(novo_convite)
    db.commit()
    db.refresh(novo_convite)

    return {"status": "sucesso",
        "mensagem": "convite gerado com sucesso",
        "data": {
            "codigo": codigo_gerado,
            "expira_em": expira_em
        }}


def gerar_codigo(db: Session):
    while True:
        codigo_gerado = secrets.token_hex(3).upper()

        conferindo_codigo = db.query(Convite).filter(Convite.codigo == codigo_gerado).first()

        if conferindo_codigo:
            continue
        else:
            return codigo_gerado


def usar_convite_service(codigo: str, payload: dict, db:Session):
    convite = db.query(Convite).filter(Convite.codigo == codigo).first()

    if not convite:
        return {"status": "erro",
                "mensagem": "Convite não encontrado",
                "data": None}

    if convite.usado:
        return {"status": "erro",
                "mensagem": "Convite ja foi utilizado",
                "data": None}

    if convite.expira_em < datetime.utcnow():
        return {"status": "erro",
                "mensagem": "Convite expirado",
                "data": None}


    id_aluno = payload["sub"]

    aluno_atual = db.query(Aluno).filter(Aluno.id == id_aluno).first()

    aluno_atual.personal_id = convite.personal_id

    convite.usado = True

    db.commit()
    db.refresh(convite)
    db.refresh(aluno_atual)

    return {"status": "sucesso",
            "mensagem": "aluno linkado com sucesso",
            "data": None}

