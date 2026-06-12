from typing import Optional
from pydantic import BaseModel

class Tarefa(BaseModel):
    id: int
    titulo:str
    descricao: Optional[str] = None
    concluida: bool = False

