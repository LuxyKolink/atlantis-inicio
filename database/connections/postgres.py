from database.base_db import Database
from database.models.common.departamento import Departamento
from database.models.common.municipio import Municipio
from database.models.common.pais import Pais


class PostgresDatabase(Database):
    def __init__(self, required=False):  # Postgres es secundario, no requerido; No es necesario inicializarlo si no está disponible
        super().__init__("POSTGRES_DATABASE_URL", required=required)
        
    def initialize(self):
        # Registra que modelos usar en base de datos
        return self.init_models([Pais, Departamento, Municipio])

postgres_db = PostgresDatabase(required=False)
postgres_initialized = postgres_db.initialize()  # Intenta inicializar, lanzará error si no está disponible

def get_postgres_db():
    for session in postgres_db.get_session():
        if session:  # Solo devuelve si la sesión es válida
            yield session