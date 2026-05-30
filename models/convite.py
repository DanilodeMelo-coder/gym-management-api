from sqlalchemy import Column, String, DateTime, ForeignKey, Boolean
from core.database import Base
import uuid


class Convite(Base):
    __tablename__ = "Convites"

    id = Column(String, primary_key= True, default=lambda: str(uuid.uuid4()))
    personal_id = Column(String, ForeignKey("Usuarios.id"))
    codigo = Column(String, nullable= False)
    expira_em = Column(DateTime, nullable= False)
    usado = Column(Boolean, default= False)