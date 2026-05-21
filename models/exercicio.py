from sqlalchemy import Column, String, Boolean, Date
from core.database import Base
import uuid

class Exercicio(Base)
    __tablename__ = "Exercicios"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    nome = Column(String, nullable= False)
    grupo = Column(String, nuallable= True)
    descricao = Column(String, default= None)
