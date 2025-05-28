from typing import TYPE_CHECKING, List, Optional
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from database.models.sqlmodel.shared.departamento import Departamento  # Importar aquí para evitar problemas de referencia circular


class Pais(SQLModel, table=True):
    __tablename__ = "paises"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(index=True, schema_extra={"pattern": r"^[A-Za-z\s]+$"}, description="Nombre oficial del país")
    codigo: str = Field(max_length=2, unique=True)
    
    # Relación con Departamento (se define después de la clase Departamento)
    departamentos: List["Departamento"] = Relationship(back_populates="pais")

    class Config:
        validate_assignment = True