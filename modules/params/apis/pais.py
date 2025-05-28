from typing import List
from fastapi import APIRouter, Depends
from sqlmodel import Session

from database.connections.sqlite import get_sqlite_db
from modules.params.repositories.adapter.sqlite.pais import SQLitePaisRepository
from modules.params.schemas.pais import Pais, PaisCreate
from modules.params.services.pais import PaisService

router = APIRouter()

# Necesitamos el repositorio para poder hacer las consultas a la base de datos
def get_pais_repository(db: Session = Depends(get_sqlite_db)) -> SQLitePaisRepository:
    return SQLitePaisRepository(db)

# Necesitamos los servicios para llegar a los repositorios y hacer las consultas a la base de datos
def get_pais_service(pais_repository: SQLitePaisRepository = Depends(get_pais_repository)) -> PaisService:
    return PaisService(pais_repository)

@router.get("/", response_model=List[Pais])
def get_paises(skip: int = 0, limit: int = 100, service: PaisService = Depends(get_pais_service)):
    return service.get_all(skip=skip, limit=limit)

@router.post("/", response_model=Pais)
def create_pais(pais: PaisCreate, service: PaisService = Depends(get_pais_service)):
    return service.create(pais)
