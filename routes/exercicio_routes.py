from fastapi import APIRouter, Depends
from schemas.exercicio import CriarExercicio
from services.exercicio_services import criar_exercicio_service
from core.database import get_session
from sqlalchemy.orm import Session

router= APIRouter(prefix="/exercicios", tags=["exercicios"])


@router.get("/")
def exercicios_cadastrados():

    return "ok"


@router.post("/")
def criar_exercicio(exercicio: CriarExercicio, db: Session = Depends(get_session)):
    return criar_exercicio_service(exercicio, db)


