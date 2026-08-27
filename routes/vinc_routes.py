from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_session
from dependencias.auth_depends import autenticar_token, apenas_personal
from services.vinc_services import vincular_treino_service, listar_treinos_aluno, desativar_vinculacao


router = APIRouter(prefix="/vinculacoes", tags=["Vinculações"])


@router.post("/{aluno_id}/{treino_id}")
def vincular_treino_rota(aluno_id: str, treino_id: str, db: Session = Depends(get_session), payload: dict = Depends(apenas_personal)):
    return vincular_treino_service(aluno_id, treino_id, payload, db)


@router.get("/meus-treinos")
def listar_treinos_aluno_rota(db: Session = Depends(get_session), payload: dict = Depends(autenticar_token)):
    return listar_treinos_aluno(payload, db)


@router.patch("/{id}/desativar")
def desativar_vinculacao_rota(id: str, db: Session = Depends(get_session), payload: dict = Depends(apenas_personal)):
    return desativar_vinculacao(id, db)
