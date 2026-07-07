from sqlalchemy import Column, String, DateTime,  ForeignKey, Boolean, UniqueConstraint
from core.database import Base
import uuid
from datetime import datetime, timezone


class Vinc_AlunoTreino(Base):
    __tablename__ = "AlunoTreinos"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    data = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    treino_id = Column(String, ForeignKey("Treinos.id"))
    aluno_id = Column(String, ForeignKey("Usuarios.id"))
    observacao = Column(String, nullable= True)
    ativo = Column(Boolean, default= True)

#impedir criação vinculacoes duplicadas
    __table_args__ = (UniqueConstraint('aluno_id', 'treino_id'),)