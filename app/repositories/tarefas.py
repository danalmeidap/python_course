from sqlalchemy.orm import Session
from app.models.tarefa import TarefaModel


class TarefasRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(TarefaModel).all()

    def get_by_id(self, tarefa_id: int):
        return self.db.query(TarefaModel).filter(TarefaModel.id == tarefa_id).first()

    def create(self, tarefa: TarefaModel):
        self.db.add(tarefa)
        self.db.commit()
        self.db.refresh(tarefa)
        return tarefa

    def update(self, tarefa_id: int, dados: dict):
        tarefa = self.get_by_id(tarefa_id)
        if not tarefa:
            return None
        for key, value in dados.items():
            setattr(tarefa, key, value)
        self.db.commit()
        self.db.refresh(tarefa)
        return tarefa

    def delete(self, tarefa_id: int):
        tarefa = self.get_by_id(tarefa_id)
        if not tarefa:
            return None
        self.db.delete(tarefa)
        self.db.commit()
        return tarefa