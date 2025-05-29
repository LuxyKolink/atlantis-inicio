# database/models/sqlalchemy/core/base.py
from typing import Any, Dict, Type
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy import Column, Integer, DateTime, func
import datetime

class CustomBase:
    """
    Custom base class for all SQLAlchemy models.
    
    Provides common functionality like serialization and common fields.
    """
    # Common fields
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the model instance to a dictionary.
        
        Returns:
            Dict[str, Any]: Dictionary representation of the model
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> Any:
        """
        Create a model instance from a dictionary.
        
        Args:
            data: Dictionary with model data
            
        Returns:
            An instance of the model
        """
        return cls(**data)

# Create the base class for SQLAlchemy models
Base = declarative_base(cls=CustomBase)


# Example of a mixin that could be used with SQLAlchemy models
class TimestampMixin:
    """
    Mixin to add timestamp fields to a model.
    """
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(
        DateTime, 
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow
    )


# Example of a mixin for soft delete functionality
class SoftDeleteMixin:
    """
    Mixin to add soft delete capability to a model.
    """
    deleted_at = Column(DateTime, nullable=True)
    
    def soft_delete(self):
        """Mark the record as deleted without removing it from the database."""
        self.deleted_at = datetime.datetime.utcnow()
    
    @classmethod
    def not_deleted(cls):
        """Query filter to exclude soft-deleted records."""
        return cls.deleted_at == None  # noqa