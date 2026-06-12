from fastapi import FastAPI
from app.routers.router_tarefas import tarefas_router


app = FastAPI()
app.include_router(tarefas_router, prefix="/tarefas", tags=["tarefas"])

@app.get("/")
def root():
    return {"message": "Hello, FastApi!"}
