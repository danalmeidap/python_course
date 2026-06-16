
from fastapi import status


def test_tarefa_route_should_200(client, usuario_autenticado):
    response = client.get("/tarefas/", headers=usuario_autenticado)
    assert response.status_code == status.HTTP_200_OK   


def test_criar_tarefa(client, usuario_autenticado):
    tarefa = {"id": 1, "titulo": "Tarefa 1", "descricao": "Descrição da tarefa 1"}
    response = client.post("/tarefas", json=tarefa, headers=usuario_autenticado)
    assert response.status_code == status.HTTP_201_CREATED
    json_resposta = response.json()
    assert json_resposta["id"] == tarefa["id"]
    assert json_resposta["titulo"] == tarefa["titulo"]


def test_listar_tarefas(client, usuario_autenticado):
    response = client.get("/tarefas/", headers=usuario_autenticado)
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json(), list)


def test_obter_tarefa(client, usuario_autenticado):
    tarefa = {"id": 2, "titulo": "Tarefa 2", "descricao": "Descrição da tarefa 2"}
    client.post("/tarefas", json=tarefa, headers=usuario_autenticado)
    response = client.get("/tarefas/2", headers=usuario_autenticado)
    assert response.status_code == status.HTTP_200_OK
    json_resposta = response.json()
    assert json_resposta["id"] == tarefa["id"]
    assert json_resposta["titulo"] == tarefa["titulo"]


def test_obter_tarefa_inexistente(client, usuario_autenticado):
    response = client.get("/tarefas/999", headers=usuario_autenticado)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Tarefa não encontrada"}


def test_atualizar_tarefa(client, usuario_autenticado):
    tarefa = {"id": 3, "titulo": "Tarefa 3", "descricao": "Descrição da tarefa 3"}
    client.post("/tarefas", json=tarefa, headers=usuario_autenticado)
    tarefa_atualizada = {"id": 3, "titulo": "Tarefa 3 Atualizada", "descricao": "Descrição atualizada"}
    response = client.put("/tarefas/3", json=tarefa_atualizada, headers=usuario_autenticado)
    assert response.status_code == status.HTTP_200_OK
    json_resposta = response.json()
    assert json_resposta["titulo"] == tarefa_atualizada["titulo"]


def test_deletar_tarefa(client, usuario_autenticado):
    tarefa = {"id": 4, "titulo": "Tarefa 4", "descricao": "Descrição da tarefa 4"}
    client.post("/tarefas", json=tarefa, headers=usuario_autenticado)
    response = client.delete("/tarefas/4", headers=usuario_autenticado)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    response_get = client.get("/tarefas/4", headers=usuario_autenticado)
    assert response_get.status_code == status.HTTP_404_NOT_FOUND

def test_deletar_tarefa_inexistente(client, usuario_autenticado):
    response = client.delete("/tarefas/999", headers=usuario_autenticado)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Tarefa não encontrada"}


def test_atualizar_tarefa_inexistente(client, usuario_autenticado):
    tarefa_atualizada = {"id": 999, "titulo": "Tarefa Inexistente", "descricao": "Descrição da tarefa inexistente"}
    response = client.put("/tarefas/999", json=tarefa_atualizada, headers=usuario_autenticado)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Tarefa não encontrada"}


def test_criar_tarefa_titulo_vazio(client, usuario_autenticado):
    tarefa = {"id": 1, "titulo": "  ", "descricao": "Teste"}
    response = client.post("/tarefas", json=tarefa, headers=usuario_autenticado)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT

def test_criar_tarefa_id_negativo(client, usuario_autenticado):
    tarefa = {"id": -1, "titulo": "Tarefa válida"}
    response = client.post("/tarefas", json=tarefa, headers=usuario_autenticado)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT

def test_criar_tarefa_titulo_curto(client, usuario_autenticado):
    tarefa = {"id": 1, "titulo": "ab"}
    response = client.post("/tarefas", json=tarefa, headers=usuario_autenticado)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT


def test_criar_tarefa_titulo_so_espacos(client, usuario_autenticado):
    tarefa = {"id": 1, "titulo": "     "}
    response = client.post("/tarefas", json=tarefa, headers=usuario_autenticado)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT


def test_persistencia_apos_restart_sessao(client, usuario_autenticado):
    tarefa = {"id": 100, "titulo": "Tarefa persistente"}
    client.post("/tarefas/", json=tarefa, headers=usuario_autenticado)

    response = client.get("/tarefas/100", headers=usuario_autenticado)
    assert response.status_code == 200
    assert response.json()["titulo"] == "Tarefa persistente"