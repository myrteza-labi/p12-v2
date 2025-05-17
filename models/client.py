from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from models.base import Base
from datetime import datetime 

class Client(Base):
    __tablename__="clients"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100),nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    telephone = Column(String(100), nullable=False, unique=True)
    company_name = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    last_update = Column(DateTime, default=datetime.utcnow, nullable=True)
    assigned_salesman_id = Column(Integer, ForeignKey("collaborators.id"))
    assigned_salesman = relationship("Collaborator", back_populates="clients")
    events = relationship("Event", back_populates="client", cascade="all, delete_orphan")