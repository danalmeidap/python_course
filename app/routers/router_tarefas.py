from fastapi import APIRouter, HTTPException, status
from app.models.tarefa import TarefaModel

from app.schemas.tarefas import TarefaCreate, TarefaResponse 
from app.deps import TaskRepo, UsuarioAtual

tarefas_router = APIRouter()


@tarefas_router.post("/", response_model=TarefaResponse, status_code=status.HTTP_201_CREATED)
def criar_tarefa(tarefa: TarefaCreate, repository: TaskRepo, usuario_atual: UsuarioAtual):
    nova_tarefa = TarefaModel(**tarefa.model_dump(), usuario_id=usuario_atual.id)
    return repository.create(nova_tarefa)


@tarefas_router.get("/", response_model=list[TarefaResponse])
def listar_tarefas(repository: TaskRepo, usuario_atual: UsuarioAtual):
    return repository.get_all_by_usuario(usuario_atual.id)


@tarefas_router.get("/{tarefa_id}", response_model=TarefaResponse)
def obter_tarefa(tarefa_id: int, repository: TaskRepo, usuario_atual: UsuarioAtual):
    tarefa = repository.get_by_id(tarefa_id)
    if tarefa is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tarefa não encontrada")
    if tarefa.usuario_id != usuario_atual.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Acesso negado à tarefa")       
    return tarefa


@tarefas_router.put("/{tarefa_id}", response_model=TarefaResponse)
def atualizar_tarefa(tarefa_id: int, tarefa_atualizada: TarefaCreate, repository: TaskRepo, usuario_atual: UsuarioAtual):
    tarefa_existente = repository.get_by_id(tarefa_id)
    if tarefa_existente is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tarefa não encontrada")     
    if tarefa_existente.usuario_id != usuario_atual.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Acesso negado à tarefa")
    tarefa = repository.update(tarefa_id, tarefa_atualizada.model_dump())
    return tarefa


@tarefas_router.delete("/{tarefa_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_tarefa(tarefa_id: int, repository: TaskRepo, usuario_atual: UsuarioAtual):
    tarefa = repository.get_by_id(tarefa_id)
    if tarefa is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tarefa não encontrada")
    if tarefa.usuario_id != usuario_atual.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Acesso negado à tarefa")
    repository.delete(tarefa_id)