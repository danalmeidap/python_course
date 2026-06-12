from fastapi import APIRouter, HTTPException
from app.schemas.tarefas import Tarefa
from fastapi import status

tarefas_router = APIRouter()
banco_de_dados = []


@tarefas_router.post("/", response_model=Tarefa, status_code=status.HTTP_201_CREATED)
def criar_tarefa(tarefa: Tarefa):
    banco_de_dados.append(tarefa)
    return tarefa


@tarefas_router.get("/", response_model=list[Tarefa])
def listar_tarefas():
    return banco_de_dados

@tarefas_router.get("/{tarefa_id}", response_model=Tarefa)
def obter_tarefa(tarefa_id: int):
    _, tarefa = _buscar_tarefa(tarefa_id)
    return tarefa

@tarefas_router.put("/{tarefa_id}", response_model=Tarefa)
def atualizar_tarefa(tarefa_id: int, tarefa_atualizada: Tarefa):
    index, _ = _buscar_tarefa(tarefa_id)
    banco_de_dados[index] = tarefa_atualizada
    return tarefa_atualizada

@tarefas_router.delete("/{tarefa_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_tarefa(tarefa_id: int):
    index, _ = _buscar_tarefa(tarefa_id)
    del banco_de_dados[index]


def _buscar_tarefa(tarefa_id: int) -> tuple[int, Tarefa]:
    for index, tarefa in enumerate(banco_de_dados):
        if tarefa.id == tarefa_id:
            return index, tarefa
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Tarefa não encontrada"
    )