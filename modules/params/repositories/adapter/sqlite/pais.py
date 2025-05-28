from typing import List
from sqlmodel import select

# from sqlmodel import select
from database.models.sqlmodel.shared.pais import Pais
from modules.params.repositories.adapter.pais_repository_interface import PaisRepositoryInterface


class SQLitePaisRepository(PaisRepositoryInterface):
    def __init__(self, db):
        self.db = db

    def get_all(self, skip: int = 0, limit: int = 100) -> List[Pais]:
        paises = self.db.exec(
            select(Pais).offset(skip).limit(limit)
        ).all()
        return paises
    
    def get_by_id(self, id: int) -> Pais:
        pais = self.db.get(Pais, id)
        return pais
    
    def get_by_codigo(self, codigo: str) -> Pais:
        pais = self.db.exec(
            select(Pais).where(Pais.codigo == codigo)
        ).first()
        return pais
    
    def get_by_nombre(self, nombre: str) -> Pais:
        pais = self.db.exec(
            select(Pais).where(Pais.nombre == nombre)
        ).first()
        return pais
    
    def create(self, pais: Pais) -> Pais:
        # db_pais = Pais(
        #     id=pais.id,
        #     descripcion=pais.nombre,
        # )
        self.db.add(pais)
        self.db.commit()
        self.db.refresh(pais)
        return pais
    
    def update(self, id: int, pais: Pais) -> Pais:
        return 'not implemented'

    def delete(self, id: int) -> bool:
        return 'not implemented'