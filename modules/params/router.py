from fastapi import APIRouter
from modules.params.apis.pais import router as pais_router
# from .api.departamento import router as departamento_router
# from .api.municipio import router as municipio_router

router = APIRouter()

router.include_router(
    pais_router, 
    prefix="/paises", 
    tags=["Países"],
    responses={404: {"description": "País no encontrado"}},
)
# router.include_router(departamento_router, prefix="/departamentos", tags=["Departamentos"])
# router.include_router(municipio_router, prefix="/municipios", tags=["Municipios"])