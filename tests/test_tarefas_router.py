from fastapi import status


def test_tarefa_route_should_200(client, usuario_autenticado):
    response = client.get("/tarefas/", headers=usuario_autenticado)
    assert response.status_code == status.HTTP_200_OK


def test_criar_tarefa(client, usuario_autenticado):
    tarefa = {"titulo": "Tarefa 1", "descricao": "Descrição da tarefa 1"}
    response = client.post("/tarefas", json=tarefa, headers=usuario_autenticado)
    assert response.status_code == status.HTTP_201_CREATED
    json_resposta = response.json()
    assert json_resposta["titulo"] == tarefa["titulo"]
    assert "id" in json_resposta
    assert "usuario_id" in json_resposta


def test_listar_tarefas(client, usuario_autenticado):
    response = client.get("/tarefas/", headers=usuario_autenticado)
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json(), list)


def test_listar_tarefas_nao_inclui_tarefas_de_outro_usuario(client, tarefa_criada, outro_usuario_autenticado):
    response = client.get("/tarefas/", headers=outro_usuario_autenticado)
    assert response.status_code == status.HTTP_200_OK
    ids_retornados = [t["id"] for t in response.json()]
    assert tarefa_criada["id"] not in ids_retornados


def test_obter_tarefa(client, usuario_autenticado, tarefa_criada):
    response = client.get(f"/tarefas/{tarefa_criada['id']}", headers=usuario_autenticado)
    assert response.status_code == status.HTTP_200_OK
    json_resposta = response.json()
    assert json_resposta["id"] == tarefa_criada["id"]
    assert json_resposta["titulo"] == tarefa_criada["titulo"]


def test_obter_tarefa_de_outro_usuario_retorna_404(client, tarefa_criada, outro_usuario_autenticado):
    response = client.get(f"/tarefas/{tarefa_criada['id']}", headers=outro_usuario_autenticado)
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_obter_tarefa_inexistente(client, usuario_autenticado):
    response = client.get("/tarefas/999", headers=usuario_autenticado)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Tarefa não encontrada"}


def test_atualizar_tarefa(client, usuario_autenticado, tarefa_criada):
    tarefa_atualizada = {"titulo": "Tarefa Atualizada", "descricao": "Descrição atualizada"}
    response = client.put(
        f"/tarefas/{tarefa_criada['id']}", json=tarefa_atualizada, headers=usuario_autenticado
    )
    assert response.status_code == status.HTTP_200_OK
    json_resposta = response.json()
    assert json_resposta["titulo"] == tarefa_atualizada["titulo"]


def test_atualizar_tarefa_de_outro_usuario_retorna_404(client, tarefa_criada, outro_usuario_autenticado):
    tarefa_atualizada = {"titulo": "Tentativa de alterar"}
    response = client.put(
        f"/tarefas/{tarefa_criada['id']}", json=tarefa_atualizada, headers=outro_usuario_autenticado
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_atualizar_tarefa_inexistente(client, usuario_autenticado):
    tarefa_atualizada = {"titulo": "Tarefa Inexistente", "descricao": "Descrição"}
    response = client.put("/tarefas/999", json=tarefa_atualizada, headers=usuario_autenticado)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Tarefa não encontrada"}


def test_deletar_tarefa(client, usuario_autenticado, tarefa_criada):
    response = client.delete(f"/tarefas/{tarefa_criada['id']}", headers=usuario_autenticado)
    assert response.status_code == status.HTTP_204_NO_CONTENT

    response_get = client.get(f"/tarefas/{tarefa_criada['id']}", headers=usuario_autenticado)
    assert response_get.status_code == status.HTTP_404_NOT_FOUND


def test_deletar_tarefa_de_outro_usuario_retorna_404(client, tarefa_criada, outro_usuario_autenticado):
    response = client.delete(f"/tarefas/{tarefa_criada['id']}", headers=outro_usuario_autenticado)
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_deletar_tarefa_inexistente(client, usuario_autenticado):
    response = client.delete("/tarefas/999", headers=usuario_autenticado)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Tarefa não encontrada"}


def test_criar_tarefa_titulo_vazio(client, usuario_autenticado):
    tarefa = {"titulo": "  ", "descricao": "Teste"}
    response = client.post("/tarefas", json=tarefa, headers=usuario_autenticado)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT


def test_criar_tarefa_titulo_curto(client, usuario_autenticado):
    tarefa = {"titulo": "ab"}
    response = client.post("/tarefas", json=tarefa, headers=usuario_autenticado)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT


def test_criar_tarefa_titulo_so_espacos(client, usuario_autenticado):
    tarefa = {"titulo": "     "}
    response = client.post("/tarefas", json=tarefa, headers=usuario_autenticado)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT


def test_persistencia_apos_restart_sessao(client, usuario_autenticado):
    tarefa = {"titulo": "Tarefa persistente"}
    response_post = client.post("/tarefas/", json=tarefa, headers=usuario_autenticado)
    tarefa_id = response_post.json()["id"]

    response = client.get(f"/tarefas/{tarefa_id}", headers=usuario_autenticado)
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["titulo"] == "Tarefa persistente"


def test_obter_minhas_tarefas(client, usuario_autenticado, tarefa_criada):
    response = client.get("/usuarios/me/tarefas", headers=usuario_autenticado)
    assert response.status_code == status.HTTP_200_OK
    json_resposta = response.json()
    assert len(json_resposta["tarefas"]) >= 1