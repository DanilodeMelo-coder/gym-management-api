from sqlalchemy import Column, String, Enum
from core.database import Base
from enums.exercicio_enum import TipoExercicio
import uuid

class Exercicio(Base):
    __tablename__ = "Exercicios"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    nome = Column(String, nullable= False)
    grupo = Column(String, nullable= True)
    descricao = Column(String, default= None)
    tipo = Column(Enum(TipoExercicio), default= TipoExercicio.base)


