from sqlalchemy.orm import Session
import bcrypt
from models.aluno import Aluno
import jwt
from datetime import datetime, timedelta, timezone
from core.config import SENHA_AUTH, ASSINATURA_JWT


def login_service(email: str, senha: str, db: Session):

    usuario = db.query(Aluno).filter(Aluno.email == email).first()
    if not usuario:
        return {"status": "erro",
                "mensagem": "email ou senha incorretos",
                "data": None}

    checar_senha_usuario = bcrypt.checkpw(senha.encode("utf-8"), usuario.senha.encode("utf-8"))
    if not checar_senha_usuario:
        return {"status": "erro",
                "mensagem": "email ou senha incorretos",
                "data": None}

    token_atual = gerar_token(usuario)

    return {"access_token": token_atual,
            "token_type": "bearer"}


def gerar_token(usuario):
    payload = {
        "sub": usuario.id,
        "tipo": usuario.tipo,
        "exp": datetime.now(timezone.utc) + timedelta(hours= 8)
    }

    token = jwt.encode(payload, SENHA_AUTH, algorithm= ASSINATURA_JWT)

    return token