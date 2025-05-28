from typing import TYPE_CHECKING, List, Optional
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from database.models.sqlmodel.shared.pais import Pais  # Importar aquí para evitar problemas de referencia circular
    from database.models.sqlmodel.shared.municipio import Municipio  # Importar aquí para evitar problemas de referencia circular

class Departamento(SQLModel, table=True):
    __tablename__ = "departamentos"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(index=True)
    codigo: str = Field(unique=True)
    pais_id: int = Field(foreign_key="paises.id")
    
    # Relaciones
    pais: "Pais" = Relationship(back_populates="departamentos")
    municipios: List["Municipio"] = Relationship(back_populates="departamento")