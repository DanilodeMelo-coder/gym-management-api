from fastapi import HTTPException, status, Depends
from core.config import SENHA_AUTH, ASSINATURA_JWT
from fastapi.security import OAuth2PasswordBearer
import jwt

#esquema de segurança - dizer onde fica a rota de login
#extrair token da url
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/Auth/login")

def autenticar_token(token: str = Depends(oauth2_scheme) ):
    try:
        payload= jwt.decode(token, SENHA_AUTH, algorithms=[ASSINATURA_JWT])
        return payload
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido ou expirado"
        )


def apenas_admin(payload: dict = Depends(autenticar_token)):
    if payload["tipo"] != "admin":
        raise HTTPException(status_code= 403, detail="Acesso negado")
    
    return payload

def apenas_personal(payload: dict = Depends(autenticar_token)):
    if payload["tipo"] not in ["personal", "admin"]:
        raise HTTPException(status_code= 403, detail="Acesso negado")
    
    return payload
