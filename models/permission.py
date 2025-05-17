from sqlalchemy import String, Integer
from sqlalchemy.orm import rela
from .base import Base

class Permission(Base):
    __tablename__ = "permissions"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    roles = relationship("Role",
        secondary="role_permission",
        back_populates="permissions"
    )