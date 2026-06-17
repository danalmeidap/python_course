from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.settings.database import Base

class TarefaModel(Base):
    __tablename__ = 'tarefas'

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(100), nullable=False)
    descricao = Column(String(500), nullable=True)
    concluida = Column(Boolean, default=False)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)

    usuario = relationship("UsuarioModel", back_populates="tarefas")