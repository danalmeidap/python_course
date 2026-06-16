from sqlalchemy.orm import Session
from app.models.usuario import UsuarioModel

class UsuarioRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(UsuarioModel).all()

    def get_by_id(self, usuario_id: int):
        return self.db.query(UsuarioModel).filter(UsuarioModel.id == usuario_id).first()
    
    def get_by_email(self, email: str):
        return self.db.query(UsuarioModel).filter(UsuarioModel.email == email).first()

    def create(self, usuario: UsuarioModel):
        self.db.add(usuario)
        self.db.commit()
        self.db.refresh(usuario)
        return usuario

    def update(self, usuario_id: int, dados: dict):
        usuario = self.get_by_id(usuario_id)
        if not usuario:
            return None
        for key, value in dados.items():
            setattr(usuario, key, value)
        self.db.commit()
        self.db.refresh(usuario)
        return usuario

    def delete(self, usuario_id: int):
        usuario = self.get_by_id(usuario_id)
        if not usuario:
            return None
        self.db.delete(usuario)
        self.db.commit()
        return usuario