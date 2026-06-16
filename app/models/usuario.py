from sqlalchemy import Column, Integer, String
from app.settings.database import Base


class UsuarioModel(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    senha_hash= Column(String(255), nullable=False)
