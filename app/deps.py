from typing import Annotated, TypeAlias

from fastapi import Depends
from sqlalchemy.orm import Session

from app.repositories.tarefas import TarefasRepository
from app.repositories.usuario import UsuarioRepository
from app.settings.database import get_db
from app.security.auth import get_usuario_atual
from app.models.usuario import UsuarioModel



def get_tarefas_repository(db: Annotated[Session, Depends(get_db)]) -> TarefasRepository:
    return TarefasRepository(db)

def get_usuario_repository(db: Annotated[Session, Depends(get_db)]) -> UsuarioRepository:
    return UsuarioRepository(db)

TaskRepo: TypeAlias = Annotated[TarefasRepository, Depends(get_tarefas_repository)]
UserRepo: TypeAlias = Annotated[UsuarioRepository, Depends(get_usuario_repository)]
UsuarioAtual: TypeAlias = Annotated[UsuarioModel, Depends(get_usuario_atual)]