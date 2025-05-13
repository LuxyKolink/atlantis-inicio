from typing import Optional
from pydantic import BaseModel, Field


# Base Municipio model
class MunicipioBase(BaseModel):
    nombre: str = Field(..., description="Nombre oficial del municipio")
    codigo: str = Field(..., description="Código del municipio")
    departamento_id: int = Field(..., description="ID del departamento al que pertenece el municipio")


# Municipio creation model
class MunicipioCreate(MunicipioBase):
    pass


# Municipio update model (all fields optional)
class MunicipioUpdate(BaseModel):
    nombre: Optional[str] = None
    codigo: Optional[str] = None
    departamento_id: Optional[int] = None


# Municipio response model (includes ID)
class Municipio(MunicipioBase):
    id: int
    
    class Config:
        from_attributes = True


# Extended Municipio response with related departamento
# class MunicipioWithDepartamento(Municipio):
#     departamento: Departamento
    
#     class Config:
#         orm_mode = True