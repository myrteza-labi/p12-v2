from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base


class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True)
    role_name = Column(String(100), nullable=False, unique=True)
    collaborators = relationship("Collaborator", back_populates="role")
    permissions = relationship(
        "Permissions",
        secondary="role_permission",
        back_populates="roles"
    )
    