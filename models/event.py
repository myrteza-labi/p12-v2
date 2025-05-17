from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    client_id = Column(Integer, ForeignKey("clients.id"), nullable=False)
    client = relationship("Client", back_populates="events")
    client_contact = Column(String(100), nullable=False)
    client_name = Column(String(100), nullable=False)
    begin_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    support_id = Column(Integer, ForeignKey("collaborators.id"), nullable=True)
    support = relationship("Collaborator", back_populates="events")
    location = Column(String(1000), nullable=False)
    attendees = Column(Integer, nullable=False)
    notes = Column(String(2000), nullable=True)