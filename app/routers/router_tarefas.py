from fastapi import APIRouter, HTTPException
from app.models.tarefa import TarefaModel
from app.schemas.tarefas import Tarefa
from fastapi import status
from app.deps import TaskRepo

tarefas_router = APIRouter()


@tarefas_router.post("/", response_model=Tarefa, status_code=status.HTTP_201_CREATED)
def criar_tarefa(tarefa: Tarefa, repository: TaskRepo):
    if repository.get_by_id(tarefa.id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Tarefa com este ID já existe.")
    nova_tarefa = TarefaModel(**tarefa.model_dump())  # ← converte Pydantic → SQLAlchemy
    return repository.create(nova_tarefa)


@tarefas_router.get("/", response_model=list[Tarefa])
def listar_tarefas(repository: TaskRepo):
    return repository.get_all()

@tarefas_router.get("/{tarefa_id}", response_model=Tarefa)
def obter_tarefa(tarefa_id: int, repository: TaskRepo):
    tarefa = repository.get_by_id(tarefa_id)
    if tarefa is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tarefa não encontrada")
    return tarefa

@tarefas_router.put("/{tarefa_id}", response_model=Tarefa)
def atualizar_tarefa(tarefa_id: int, tarefa_atualizada: Tarefa, repository: TaskRepo):
    tarefa = repository.update(tarefa_id, tarefa_atualizada.model_dump())
    if tarefa is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tarefa não encontrada")
    return tarefa

@tarefas_router.delete("/{tarefa_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_tarefa(tarefa_id: int, repository: TaskRepo):
    tarefa = repository.delete(tarefa_id)
    if tarefa is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tarefa não encontrada")
