from fastapi import APIRouter, Depends
from services.auth_services import login_service
from core.database import get_session
from sqlalchemy.orm import Session
from schemas.auth import AuthSchema

router = APIRouter(prefix="/Auth", tags=["auth"])

@router.post("/login")
def login(usuario: AuthSchema, db: Session = Depends(get_session)):
    autenticacao= login_service(usuario.email, usuario.senha, db)

    return autenticacao


