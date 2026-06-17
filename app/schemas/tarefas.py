from typing import Optional
from pydantic import BaseModel, ConfigDict, Field, field_validator

class TarefaBase(BaseModel):
    titulo: str = Field(min_length=3, max_length=100, description="Título da tarefa")
    descricao: Optional[str] = Field(default=None, max_length=500)
    concluida: bool = False

    @field_validator('titulo')
    @classmethod
    def titulo_nao_pode_ser_vazio(cls, value):
        if value.strip() == "":
            raise ValueError("Título não pode ser apenas espaços")
        return value.strip()


class TarefaCreate(TarefaBase):
    pass


class TarefaResponse(TarefaBase):
    model_config = ConfigDict(from_attributes=True)

    id: int = Field(gt=0, description="O ID da tarefa deve ser um número inteiro positivo.")
    usuario_id: int = Field(gt=0, description="O ID do usuário deve ser um número inteiro positivo.")