from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Date
from sqlalchemy.orm import relationship
from .base import Base

class Contract(Base):
    __tablename__ = "contracts"

    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey("clients.id"))
    client = relationship("Client", back_populates="contracts")
    collaborator_id = Column(Integer, ForeignKey("collaborators.id"))
    collaborator = relationship("Collaborator", back_populates="contract")
    total_amount = Column(Integer, nullable=False)
    total_remaining = Column(Integer, nullable=False)
    creation_date = Column(Date, nullable=False)
    signed = Column(Boolean, default=False, nullable=False)