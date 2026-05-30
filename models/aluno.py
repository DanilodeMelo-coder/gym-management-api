from sqlalchemy import Column, String, Date, Enum, ForeignKey
from core.database import Base
from enums.usuario_enum import TipoUsuario
import uuid


class Aluno(Base):
    __tablename__ = "Usuarios"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    nome = Column(String, nullable= False)
    email = Column(String, unique=True, nullable= False)
    senha =  Column (String, nullable= False)
    cpf = Column(String, unique= True,  nullable= False)
    data_nascimento = Column(Date, nullable= False)
    tipo = Column(Enum(TipoUsuario),  default= TipoUsuario.aluno)
    personal_id = Column(String, ForeignKey("Usuarios.id"), nullable= True)