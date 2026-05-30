from fastapi import APIRouter, Depends, HTTPException
from services.aluno_services import criar_aluno_service, listar_alunos, atualizar_aluno_service, deletar_aluno_service, buscar_aluno_service
from schemas.aluno import Criar_aluno, AlunoUpdate, Aluno
from core.database import get_session
from sqlalchemy.orm import Session
from dependencias.auth_depends import autenticar_token, apenas_admin, apenas_personal


router = APIRouter(prefix="/Alunos", tags=["Alunos"])


@router.get("/", response_model=list[Aluno])
def listar_aluno(db: Session = Depends(get_session), payload = Depends(apenas_personal)):
    return listar_alunos(db)

@router.post("/")
def criar_aluno(aluno: Criar_aluno, db: Session = Depends(get_session)):
    return criar_aluno_service(aluno, db)

@router.get("/{id}")
def buscar_aluno(id: str, db: Session = Depends(get_session), payload = Depends(apenas_personal)):
    return buscar_aluno_service(id, db)


@router.put("/{id}")
def atualizar_aluno(id: str, dados: AlunoUpdate, db: Session = Depends(get_session), payload = Depends(autenticar_token)):
    if payload["sub"] != id and payload["tipo"] != "admin":
        raise HTTPException(status_code= 403, detail="Você não tem permisão para alterar outros usuarios")
    return atualizar_aluno_service(id, dados, db)


@router.delete("/{id}")
def deletar_aluno(id:str, db: Session = Depends(get_session), payload = Depends(autenticar_token)):
    if payload["sub"] != id and payload["tipo"] != "admin":
        raise HTTPException(status_code= 403, detail="Você não possui permissão para deletar outros usuarios")
    return deletar_aluno_service(id, db)