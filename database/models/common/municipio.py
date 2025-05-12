from typing import TYPE_CHECKING, Optional
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from database.models.common.departamento import Departamento  # Importar aquí para evitar problemas de referencia circular


class Municipio(SQLModel, table=True):
    __tablename__ = "municipios"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(index=True)
    codigo: str
    departamento_id: int = Field(foreign_key="departamentos.id")
    
    # Relaciones
    departamento: "Departamento" = Relationship(back_populates="municipios")