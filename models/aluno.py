from sqlalchemy import Column, String, Date, Enum
from core.database import Base
from enums.usuario_enum import TipoUsuario
import uuid


class Aluno(Base):
    __tablename__ = "Alunos"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    nome = Column(String, nullable= False)
    email = Column(String, unique=True, nullable= False)
    cpf = Column(String, unique= True,  nullable= False)
    data_nascimento = Column(Date, nullable= False)
    tipo = Column(Enum(TipoUsuario),  default= TipoUsuario.aluno)