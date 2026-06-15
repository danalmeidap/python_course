from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from app.repositories.tarefas import TarefasRepository
from app.settings.database import get_db

def get_tarefas_repository(db: Annotated[Session, Depends(get_db)]) -> TarefasRepository:
    return TarefasRepository(db)

TaskRepo= Annotated[TarefasRepository, Depends(get_tarefas_repository)]