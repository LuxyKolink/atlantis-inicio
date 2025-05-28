from dotenv import load_dotenv
import os
from database.base_db import Database
from database.models.sqlmodel.shared.departamento import Departamento
from database.models.sqlmodel.shared.municipio import Municipio
from database.models.sqlmodel.shared.pais import Pais

# Cargar variables de entorno
load_dotenv()


class PostgresDatabase(Database):
    def __init__(self, required=False):  # Postgres es secundario, no requerido; No es necesario inicializarlo si no está disponible
        postgres_url = os.getenv("POSTGRES_DATABASE_URL", "postgresql://user:password@localhost/dbname")
        super().__init__(postgres_url, required=required)
        
    def initialize(self):
        # Registra que modelos usar en base de datos
        return self.init_models([Pais, Departamento, Municipio])

postgres_db = PostgresDatabase(required=False)
postgres_initialized = postgres_db.initialize()  # Intenta inicializar, lanzará error si no está disponible

def get_postgres_db():
    for session in postgres_db.get_session():
        if session:  # Solo devuelve si la sesión es válida
            yield session