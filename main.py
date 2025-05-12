from fastapi import FastAPI

# from database.connections.postgres import get_postgres_db
# from database.connections.sqlite import get_sqlite_db
# from database.models.common.pais import Pais

from modules.params.router import router as parametrica_router

app = FastAPI()

app.include_router(parametrica_router, prefix="/api/parametricas")

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "q": q}

# @app.get("/sqlite/paises/")
# def get_sqlite_paises(session: Session = Depends(get_sqlite_db)):
#     paises = session.exec(select(Pais)).all()
#     return paises

# @app.get("/postgres/paises/")
# def get_postgres_paises(session: Session = Depends(get_postgres_db)):
#     paises = session.exec(select(Pais)).all()
#     return paises