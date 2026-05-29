from fastapi import APIRouter, Depends
from services.auth_services import login_service
from core.database import get_session
from sqlalchemy.orm import Session
from schemas.auth import AuthSchema
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(prefix="/Auth", tags=["auth"])

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_session)):
    autenticacao= login_service(form_data.username, form_data.password, db)

    return autenticacao


