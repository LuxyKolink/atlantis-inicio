from typing import List, Optional
from pydantic import BaseModel, Field


# Base Departamento model
class DepartamentoBase(BaseModel):
    nombre: str = Field(..., description="Nombre oficial del departamento")
    codigo: str = Field(..., description="Código del departamento")
    pais_id: int = Field(..., description="ID del país al que pertenece el departamento")


# Departamento creation model
class DepartamentoCreate(DepartamentoBase):
    pass


# Departamento update model (all fields optional)
class DepartamentoUpdate(BaseModel):
    nombre: Optional[str] = None
    codigo: Optional[str] = None
    pais_id: Optional[int] = None


# Departamento response model (includes ID)
class Departamento(DepartamentoBase):
    id: int
    
    class Config:
        from_attributes = True


# Extended Departamento response with related país
# class DepartamentoWithPais(Departamento):
#     pais: Pais
    
#     class Config:
#         orm_mode = True


# # Extended Departamento response with related municipios
# class DepartamentoWithMunicipios(Departamento):
#     municipios: List['Municipio'] = []
    
#     class Config:
#         orm_mode = True


# # Full Departamento response with related país and municipios
# class DepartamentoFull(DepartamentoWithPais, DepartamentoWithMunicipios):
#     class Config:
#         orm_mode = True