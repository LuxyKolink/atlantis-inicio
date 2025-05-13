from dotenv import load_dotenv
import os
from database.base_db import Database
from database.models.common.departamento import Departamento
from database.models.common.municipio import Municipio
from database.models.common.pais import Pais

# Cargar variables de entorno
load_dotenv()


class SQLiteDatabase(Database):
    def __init__(self, required=True):  # SQLite es requerido, no opcional
        sqlite_file_name = os.getenv("SQLITE_FILE_NAME", "data.db")
        sqlite_url = f"sqlite:///{sqlite_file_name}"

        super().__init__(sqlite_url, required=required)
        
    def initialize(self):
        # Registra que modelos usar en base de datos
        return self.init_models([Pais, Departamento, Municipio])

sqlite_db = SQLiteDatabase(required=True)
sqlite_db.initialize()  # intenta inicializar, lanzará error si no está disponible

def get_sqlite_db():
    for session in sqlite_db.get_session():
        yield session