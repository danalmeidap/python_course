import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from fastapi.testclient import TestClient

from app.main import app
from app.settings.database import Base, get_db

SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture
def client():
    Base.metadata.create_all(bind=engine)

    def override_get_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db

    yield TestClient(app)

    Base.metadata.drop_all(bind=engine)
    app.dependency_overrides.clear()


@pytest.fixture
def usuario_autenticado(client):
    usuario = {"email": "teste@teste.com", "senha": "senha123"}
    client.post("/usuarios/", json=usuario)

    response = client.post(
        "/usuarios/login",
        data={"username": usuario["email"], "password": usuario["senha"]}
    )
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


@pytest.fixture
def outro_usuario_autenticado(client):
    usuario = {"email": "outro@email.com", "senha": "senha123"}
    client.post("/usuarios/", json=usuario)

    login_response = client.post(
        "/usuarios/login",
        data={"username": usuario["email"], "password": usuario["senha"]}
    )
    token = login_response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


@pytest.fixture
def tarefa_criada(client, usuario_autenticado):
    tarefa = {"titulo": "Tarefa de teste", "descricao": "Descrição de teste"}
    response = client.post("/tarefas", json=tarefa, headers=usuario_autenticado)
    return response.json()