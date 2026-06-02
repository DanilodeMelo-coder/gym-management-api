from sqlalchemy import Column, String, Integer, ForeignKey, Float
from core.database import Base
import uuid


class TreinoExercicio(Base):
    __tablename__ = "TreinoExercicios"

    id= Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    treino_id = Column(String, ForeignKey("Treinos.id"))
    exercicio_id = Column(String, ForeignKey("Exercicios.id"))
    series = Column(Integer, default= 0)
    repeticoes= Column(Integer, default = 0)
    carga= Column(Float, default= 0)