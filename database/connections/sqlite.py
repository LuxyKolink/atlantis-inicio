from database.base_db import Database
from database.models.common.departamento import Departamento
from database.models.common.municipio import Municipio
from database.models.common.pais import Pais


class SQLiteDatabase(Database):
    def __init__(self, required=True):  # SQLite es requerido, no opcional
        super().__init__("SQLITE_DATABASE_URL", required=required)
        
    def initialize(self):
        # Registra que modelos usar en base de datos
        return self.init_models([Pais, Departamento, Municipio])

sqlite_db = SQLiteDatabase(required=True)
sqlite_db.initialize()  # intenta inicializar, lanzará error si no está disponible

def get_sqlite_db():
    for session in sqlite_db.get_session():
        yield session