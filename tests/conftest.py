import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.routers.router_tarefas import banco_de_dados

@pytest.fixture
def client():
    banco_de_dados.clear()
    yield TestClient(app)
    banco_de_dados.clear()

