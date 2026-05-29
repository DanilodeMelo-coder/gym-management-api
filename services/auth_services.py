from sqlalchemy.orm import Session
import bcrypt
from models.aluno import Aluno
import jwt
from datetime import datetime, timedelta
from core.config import SENHA_AUTH, ASSINATURA_JWT


def login_service(email: str, senha: str, db: Session):

    usuario = db.query(Aluno).filter(Aluno.email == email).first()
    if not usuario:
        return {"status": "erro",
                "mensagem": "email ou senha incorretos",
                "data": None}

    checar_senha_usuario = bcrypt.checkpw(senha.encode("utf-8"), usuario.senha)
    if not checar_senha_usuario:
        return {"status": "erro",
                "mensagem": "email ou senha incorretos",
                "data": None}

    token_atual = gerar_token(usuario)

    return {"status": "sucesso",
            "mensagem": "Login realizado com sucesso",
            "data": token_atual}


def gerar_token(usuario):
    payload = {
        "sub": usuario.id,
        "tipo": usuario.tipo,
        "exp": datetime.utcnow() + timedelta(hours= 8)
    }

    token = jwt.encode(payload, SENHA_AUTH, algorithm= ASSINATURA_JWT)

    return token