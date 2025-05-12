# database/base.py
import os
from typing import List, Type
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

class Database:
    """
    Clase base para gestionar conexiones a bases de datos.
    
    Esta clase proporciona funcionalidad común para:
    - Establecer conexiones a diferentes bases de datos
    - Inicializar modelos de datos (tablas)
    - Gestionar sesiones de base de datos
    """
    
    def __init__(self, url_env_var, echo=True, required=False):
        """
        Inicializa una conexión a la base de datos.
        
        Args:
            url_env_var: Variable de entorno que contiene la URL de conexión
            echo: Activa/desactiva la salida SQL en consola (depuración)
        """
        # Obtener URL de la base de datos desde la variable de entorno
        self.url = "sqlite:///./data.db"
        self.echo = echo
        self.required = required
        # Crear el motor de base de datos (engine)
        self.engine = create_engine(self.url, echo=self.echo)
        self._is_initialized = False
        
    def init_models(self, models: List[Type[SQLModel]]):
        """
        Inicializa los modelos (tablas) en esta base de datos.
        
        Esto crea las tablas correspondientes a los modelos especificados.
        Cada base de datos puede tener diferentes modelos registrados.
        
        Args:
            models: Lista de clases de modelos a inicializar en esta base de datos
        """
        # Crear sólo las tablas para los modelos especificados
        for model in models:
            if hasattr(model, '__tablename__'):
                SQLModel.metadata.create_all(
                    self.engine, 
                    tables=[model.__table__]
                )
        self._is_initialized = True
        
    def get_session(self):
        """
        Proporciona una sesión de base de datos.
        
        Este método está diseñado para ser usado con Depends() en FastAPI.
        La sesión se cierra automáticamente al finalizar la petición.
        
        Yields:
            Una sesión activa de la base de datos
            
        Raises:
            RuntimeError: Si los modelos no han sido inicializados antes
        """
        if not self._is_initialized:
            raise RuntimeError("Base de datos no inicializada. Llame a init_models primero.")
        with Session(self.engine) as session:
            yield session