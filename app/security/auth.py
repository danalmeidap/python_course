from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from typing import Annotated

from app.security.jwt import decodificar_token
from app.settings.database import get_db
from app.repositories.usuario import UsuarioRepository
from app.models.usuario import UsuarioModel

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="usuarios/login")

def get_usuario_atual(
    token: Annotated[str, Depends(oauth2_scheme)],
    db: Annotated[Session, Depends(get_db)]
) -> UsuarioModel:
    payload = decodificar_token(token)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido ou expirado",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    email = payload.get("sub")
    repository = UsuarioRepository(db)
    usuario = repository.get_by_email(email)
    if usuario is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário não encontrado",
        )
    return usuario