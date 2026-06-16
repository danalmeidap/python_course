from fastapi import status

def test_criar_usuario(client):
    usuario = {"email": "novo@email.com", "senha": "senha123"}
    response = client.post("/usuarios/", json=usuario)
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["email"] == "novo@email.com"
    assert "senha" not in data
    assert "senha_hash" not in data

def test_criar_usuario_email_duplicado(client):
    usuario = {"email": "duplicado@email.com", "senha": "senha123"}
    client.post("/usuarios/", json=usuario)
    response = client.post("/usuarios/", json=usuario)
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_criar_usuario_senha_curta(client):
    usuario = {"email": "outro@email.com", "senha": "123"}
    response = client.post("/usuarios/", json=usuario)
    assert response.status_code == 422

def test_criar_usuario_email_invalido(client):
    usuario = {"email": "nao-e-email", "senha": "senha123"}
    response = client.post("/usuarios/", json=usuario)
    assert response.status_code == 422