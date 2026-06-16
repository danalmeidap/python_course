from fastapi import APIRouter, HTTPException, status
from app.schemas.usuario import UsuarioCreate, UsuarioResponse
from app.models.usuario import UsuarioModel
from app.security.hashing import hash_senha
from app.deps import UserRepo
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends
from app.security.hashing import verificar_senha
from app.security.jwt import criar_access_token

usuarios_router = APIRouter()

@usuarios_router.post("/", response_model=UsuarioResponse, status_code= status.HTTP_201_CREATED)
def criar_usuario(usuario: UsuarioCreate, repository: UserRepo):
    if repository.get_by_email(usuario.email):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email já cadastrado.")
    nova_senha = hash_senha(usuario.senha)
    novo_usuario = UsuarioModel(email=usuario.email, senha_hash=nova_senha)
    return repository.create(novo_usuario)


@usuarios_router.post("/login")
def login(repository: UserRepo, form_data: OAuth2PasswordRequestForm = Depends()):
    usuario = repository.get_by_email(form_data.username)
    if not usuario or not verificar_senha(form_data.password, usuario.senha_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou senha incorretos"
        )
    access_token = criar_access_token(dados={"sub": usuario.email})
    return {"access_token": access_token, "token_type": "bearer"}