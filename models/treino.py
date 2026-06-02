from sqlalchemy import Column, String, Enum, ForeignKey
from core.database import Base
from enums.treino_enum import TipoTreino
import uuid

class Treino(Base):
    __tablename__ = "Treinos"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    nome= Column(String, nullable= False)
    criado_por = Column(String, ForeignKey("Usuarios.id"), nullable= False)
    tipo = Column(Enum(TipoTreino), default= TipoTreino.proprio)