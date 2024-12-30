# schema.py
from pydantic import BaseModel
from typing import List, Optional

# Schema for Company Management
class CompanyBase(BaseModel):
    name: str
    location: Optional[str] = None
    linkedin_profile: Optional[str] = None
    emails: List[str]
    phone_numbers: List[str]
    comments: Optional[str] = None
    communication_periodicity: Optional[str] = None

class CompanyCreate(CompanyBase):
    pass

class CompanyUpdate(CompanyBase):
    name: Optional[str] = None
    emails: Optional[List[str]] = None
    phone_numbers: Optional[List[str]] = None

class CompanyResponse(CompanyBase):
    id: int

    class Config:
        orm_mode = True

# Schema for Communication Methods
class CommunicationMethodBase(BaseModel):
    name: str
    description: Optional[str] = None
    sequence: int
    mandatory: bool

class CommunicationMethodCreate(CommunicationMethodBase):
    pass

class CommunicationMethodUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    sequence: Optional[int] = None
    mandatory: Optional[bool] = None

class CommunicationMethodResponse(CommunicationMethodBase):
    id: int

    class Config:
        orm_mode = True
