from fastapi import APIRouter, Depends
from schemas.exercicio import CriarExercicio
from services.exercicio_services import criar_exercicio_service, listar_exercicios
from core.database import get_session
from sqlalchemy.orm import Session
from dependencias.auth_depends import autenticar_token

router= APIRouter(prefix="/exercicios", tags=["exercicios"])


@router.get("/")
def exercicios_cadastrados(db: Session= Depends(get_session), payload= Depends(autenticar_token)):

    return listar_exercicios(db)


@router.post("/")
def criar_exercicio(exercicio: CriarExercicio, db: Session = Depends(get_session), payload = Depends (autenticar_token) ):
    return criar_exercicio_service(exercicio, db)


