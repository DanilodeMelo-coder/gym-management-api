from fastapi import APIRouter, Depends
from services.aluno_services import criar_aluno_service, listar_alunos, atualizar_aluno_service, deletar_aluno_service, buscar_aluno_service
from schemas.aluno import Criar_aluno, AlunoUpdate, Aluno
from core.database import get_session
from sqlalchemy.orm import Session


router = APIRouter(prefix="Alunos", tag=["Alunos"])


@router.get("/", response_model=list[Aluno])
def listar_aluno(db: Session = Depends(get_session)):
    return listar_alunos(db)

@router.post("/")
def criar_aluno(aluno: Criar_aluno, db: Session = Depends(get_session)):
    return criar_aluno_service(aluno, db)

@router.get("/{id}")
def buscar_aluno(id: str, db: Session = Depends(get_session)):
    return buscar_aluno_service(id, db)


@router.put("/{id}")
def atualizar_aluno(id: str, dados: AlunoUpdate, db: Session = Depends(get_session)):
    return AlunoUpdate(id, dados, db)


@router.delete("/{id}")
def deletar_aluno(id:str, db: Session = Depends(get_session)):
    return deletar_aluno(id, db)