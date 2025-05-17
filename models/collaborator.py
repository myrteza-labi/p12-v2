from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Collaborator(Base):
    __tablename__="collaborators"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(128), nullable=False)
    role_id = Column(Integer, ForeignKey("roles.id"))
    role = relationship("Role", back_populates="collaborators")
    contracts = relationship("Contract", back_populates="collaborator")
    clients = relationship("Client", back_populates="assigned_salesman")