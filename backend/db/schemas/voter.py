from typing import Optional

from pydantic import BaseModel, EmailStr


# Shared properties
class VoterBase(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    address: Optional[str] = None


# Properties to receive on voter creation
class VoterCreate(VoterBase):
    document_number: str
    date_birth: str
    password: str


# Properties to receive on voter update
class VoterUpdate(VoterBase):
    password: Optional[str]


# Properties shared by models stored in DB
class VoterInDBBase(VoterBase):
    id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Voter(VoterInDBBase):
    pass


# Properties properties stored in DB
class VoterInDB(VoterInDBBase):
    hashed_password: str
