from fastapi import FastAPI
from app.routers.router_tarefas import tarefas_router
from app.routers.router_usuarios import usuarios_router
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(tarefas_router, prefix="/tarefas", tags=["tarefas"])
app.include_router(usuarios_router, prefix="/usuarios", tags=["usuarios"])

@app.get("/")
def root():
    return {"message": "Hello, FastAPI!"}