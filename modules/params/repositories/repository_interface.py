from abc import ABC, abstractmethod
from typing import List, TypeVar, Generic, Type

# Create a generic type variable for models
T = TypeVar('T')

class RepositoryInterface(Generic[T], ABC):
    """
    Interface for all repository implementations.
    Defines the standard operations to be performed on a model.
    """
    
    @abstractmethod
    def get_all(self, skip: int = 0, limit: int = 100) -> List[T]:
        """Get all records with pagination"""
        pass
    
    @abstractmethod
    def get_by_id(self, id: int) -> T:
        """Get a single record by ID"""
        pass
    
    @abstractmethod
    def create(self, entity: T) -> T:
        """Create a new record"""
        pass
    
    @abstractmethod
    def update(self, entity: T) -> T:
        """Update an existing record"""
        pass
    
    @abstractmethod
    def delete(self, id: int) -> bool:
        """Delete a record by ID"""
        pass