from typing import List, Optional
from pydantic import BaseModel, Field, field_validator


# Modelo base de País - Clase base que define los campos comunes y la validación para un país.
class PaisBase(BaseModel):
    nombre: str = Field(..., pattern=r"^[A-Za-z\s]{2,50}$", description="Nombre oficial del país")
    codigo: str = Field(..., min_length=2, max_length=2, description="Código ISO del país (ej: 'CO' para Colombia)")
    
    @field_validator('codigo')
    def codigo_mayusculas(cls, v):
        return v.upper()


# Pais creation model
class PaisCreate(PaisBase):
    pass


# Pais update model (all fields optional)
class PaisUpdate(BaseModel):
    nombre: Optional[str] = None
    codigo: Optional[str] = Field(None, min_length=2, max_length=2)
    
    @field_validator('codigo')
    def codigo_mayusculas(cls, v):
        if v is not None:
            return v.upper()
        return v



# Pais response model (includes ID)
class Pais(PaisBase):
    id: int
    
    class Config:
        orm_mode = True


# Extended Pais response with related departamentos
# class PaisWithDepartamentos(Pais):
#     departamentos: List['Departamento'] = []
    
#     class Config:
#         orm_mode = True