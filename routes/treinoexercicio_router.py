from fastapi import APIRouter, Depends, HTTPException
from services.treino_services import listar, criar_treino, buscar_treino, deletar_treino, adicionar_exercicio_service, deletar_exercicio
from schemas.treino import CriarTreino, AdicionarExercicio
from core.database import get_session
from sqlalchemy.orm import Session
from dependencias.auth_depends import autenticar_token, apenas_admin, apenas_personal


router = APIRouter(prefix="/Treinos", tags=["Treinos"])

@router.get("/")
def listar_treinos_rota(db: Session = Depends(get_session), payload= Depends(autenticar_token)):
    return listar(payload, db)

@router.post("/")
def criar_treino_rota(criartreino: CriarTreino, db: Session = Depends(get_session), payload= Depends(autenticar_token)):
    return criar_treino(payload, criartreino, db)

@router.get("/{id}")
def buscar_treino_rota(id: str, db: Session = Depends(get_session), payload = Depends(autenticar_token)):
    return buscar_treino(id, db)

@router.delete("/{id}")
def deletar_treino_rota(id: str, db: Session = Depends(get_session), payload = Depends(autenticar_token)):
    return deletar_treino(id, db)

@router.post("/{id}/exercicios")
def adicionar_exercicio_treino_rota(id: str, exercicio: AdicionarExercicio, db: Session = Depends(get_session), payload = Depends(autenticar_token)):
    return adicionar_exercicio_service(id, exercicio, db)

@router.delete("/exercicios/{id}")
def deletar_exercicio_treino_rota(id: str, db: Session = Depends(get_session), payload = Depends(autenticar_token)):
    return deletar_exercicio(id, db)

