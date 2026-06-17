from pydantic import BaseModel, EmailStr, ConfigDict, Field
from app.schemas.tarefas import TarefaResponse


class UsuarioBase(BaseModel):
    email: EmailStr


class UsuarioCreate(UsuarioBase):
    senha: str = Field(min_length=6, max_length=100)


class UsuarioResponse(UsuarioBase):
    model_config = ConfigDict(from_attributes=True)
    id: int


class UsuarioListTarefas(UsuarioBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    tarefas: list[TarefaResponse]