from abc import abstractmethod
from typing import List, Optional, Type
from sqlmodel import Session, select

from database.models.sqlmodel.shared.pais import Pais
from modules.params.repositories.repository_interface import RepositoryInterface

class PaisRepositoryInterface(RepositoryInterface[Pais]):
    """
    Interface for Pais repository with specific methods for Pais model
    """
    
    @abstractmethod
    def get_by_codigo(self, codigo: str) -> Optional[Pais]:
        """Get a country by its code"""
        pass
    
    @abstractmethod
    def get_by_nombre(self, nombre: str) -> Optional[Pais]:
        """Get a country by its name"""
        pass