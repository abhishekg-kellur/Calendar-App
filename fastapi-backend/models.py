from sqlalchemy import Column, Integer, String, Text, ARRAY, Interval, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Company(Base):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    location = Column(String(255))
    linkedin_profile = Column(Text)
    emails = Column(ARRAY(String))
    phone_numbers = Column(ARRAY(String))
    comments = Column(Text)
    communication_periodicity = Column(Interval, default='14 days')

class CommunicationMethod(Base):
    __tablename__ = "communication_methods"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    sequence = Column(Integer, nullable=False)
    mandatory = Column(Integer, default=False)

class CommunicationLog(Base):
    __tablename__ = "communications_log"
    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("companies.id"))
    method_id = Column(Integer, ForeignKey("communication_methods.id"))
    date_of_communication = Column(String, nullable=False)
    notes = Column(Text)

    company = relationship("Company")
    method = relationship("CommunicationMethod")
