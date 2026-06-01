from fastapi import APIRouter, Depends, HTTPException
from services.convite_services import criar_convite_service, usar_convite_service
from core.database import get_session
from sqlalchemy.orm import Session
from dependencias.auth_depends import autenticar_token, apenas_personal


router = APIRouter(prefix="/Convites", tags=["convite"])

@router.post("/")
def criar_convites(db: Session = Depends(get_session), payload= Depends(apenas_personal)):
    return criar_convite_service(payload, db)

@router.post("/utilizar-convite")
def utilizar_convite(codigo: str, db: Session = Depends(get_session), payload= Depends(autenticar_token)):
    return usar_convite_service(codigo, payload, db)
