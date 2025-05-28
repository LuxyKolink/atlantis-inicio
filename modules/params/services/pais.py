from typing import List

from fastapi import HTTPException
from database.models.sqlmodel.shared.pais import Pais
from modules.params.repositories.adapter.pais_repository_interface import PaisRepositoryInterface
# from modules.params.repositories.adapter.sqlite.pais import PaisRepository
from modules.params.schemas.pais import PaisCreate


class PaisService():
    def __init__(self, pais_repository: PaisRepositoryInterface):
        self.pais_repository = pais_repository

    def get_all(self, skip: int = 0, limit: int = 100) -> List[Pais]:
        return self.pais_repository.get_all(skip, limit)
    
    def create(self, pais: PaisCreate) -> Pais:
        db_pais = Pais(
            nombre=pais.nombre,
            codigo=pais.codigo
        )

        # check if the country already exists by code
        existing_pais_by_codigo = self.pais_repository.get_by_codigo(db_pais.codigo)
        if existing_pais_by_codigo:
            raise HTTPException(
                status_code=409,  # Conflict
                detail={
                    "message": f"Un país con el código '{db_pais.codigo}' ya existe",
                    "error_code": "DUPLICATE_COUNTRY_CODE",
                    "field": "codigo",
                    "value": db_pais.codigo
                }
            )
        
        #check if the country name already exists
        existing_pais_by_name = self.pais_repository.get_by_nombre(db_pais.nombre)
        if existing_pais_by_name:
            raise HTTPException(
                status_code=409,  # Conflict
                detail={
                    "message": f"Un país con el nombre '{db_pais.nombre}' ya existe",
                    "error_code": "DUPLICATE_COUNTRY_NAME",
                    "field": "nombre",
                    "value": db_pais.nombre
                }
            )
        
        return self.pais_repository.create(db_pais)
