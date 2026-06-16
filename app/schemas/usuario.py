from pydantic import BaseModel, EmailStr, ConfigDict, Field


class UsuarioBase(BaseModel):
    email: EmailStr


class UsuarioCreate(UsuarioBase):
    senha: str = Field(min_length=6, max_length=100)


class UsuarioResponse(UsuarioBase):
    model_config = ConfigDict(from_attributes=True)
    id: int